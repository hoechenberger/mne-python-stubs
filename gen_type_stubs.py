# %%
import ast
import dataclasses
import importlib
import shutil
import subprocess
import sys
from pathlib import Path

from mypy import stubgen

# Module exclusion patterns
# Note that __init__.py files are handled specially below, do not
# include them here.
# Note that individual objects can be excluded via OBJS_EXCLUDES below
MODULE_PY_EXCLUDE_PATTERNS = [
    # "mne/viz/backends/_pyvista.py",  # causing errors when running stubdefaulter
    "mne/report/js_and_css/bootstrap-icons/gen_css_for_mne.py",  # cannot be imported
    "**/tests/**",  # don't include any tests
]

mne_base_path = Path("../mne-python")
stubs_out_dir = Path("./typings")

if stubs_out_dir.exists():
    print(f"🪣  Found existing output directory, deleting: {stubs_out_dir}")
    shutil.rmtree(stubs_out_dir)

# Generate list of module paths we want to process
# We first glob all modules, then drop all that were selected for exclusion

module_py_paths = list((mne_base_path / "mne").rglob("*.py"))
module_py_paths_excludes = []
for module_py_path in module_py_paths:
    for exclude_pattern in MODULE_PY_EXCLUDE_PATTERNS:
        if module_py_path.match(exclude_pattern):
            module_py_paths_excludes.append(module_py_path)

del module_py_path

# Additionally to the exclusion patterns specified above, we also
# exclude all __init__.py files for which a .pyi type stub already exists
# for lazy loading. But we keep the remaining __init__.py files
init_pyi_paths = list((mne_base_path / "mne").rglob("__init__.pyi"))
for init_pyi_path in init_pyi_paths:
    if init_pyi_path.with_suffix(".py") in module_py_paths:
        module_py_paths_excludes.append(init_pyi_path.with_suffix(".py"))

module_py_paths = sorted(set(module_py_paths) - set(module_py_paths_excludes))

del module_py_paths_excludes

# %%
# Create stubs
print("⏳ Generating type stubs …")
stubgen.main(
    [
        "--include-docstring",
        f"--output={stubs_out_dir}",
        *[str(p) for p in module_py_paths + init_pyi_paths],
    ]
)

# %%
# Move __init__.pyi-based stubs to the correct location
# e.g.:
#     typings/mne.pyi -> typings/mme/__init__.pyi
#     typings/mne/decoding.pyi -> typings/mne/decoding/__init__.pyi
# etc.
for init_pyi_path in init_pyi_paths:
    source_path = stubs_out_dir / Path(
        str(init_pyi_path).replace(f"{mne_base_path}/", "")
    ).parent.with_suffix(".pyi")
    target_path = stubs_out_dir / str(init_pyi_path).replace(f"{mne_base_path}/", "")
    print(f"📦 Moving {source_path} -> {target_path}")
    source_path.rename(target_path)

# %%
# Iterate over all top-level objects and replace the docstrings in the stub files with
# the expanded docstrings (generated through importing the respective .py modules)

stub_paths = list(stubs_out_dir.rglob("*.pyi"))

OBJS_EXCLUDES = [
    # NamedTuples – somehow I cannot detect them via isinstance(obj, tuple)??
    "CurryParameters",
    "CNTEventType1",
    "CNTEventType2",
    "CNTEventType3",
    "_ica_node",
]

for stub_path in stub_paths:
    module_ast = ast.parse(stub_path.read_text(encoding="utf-8"))
    module_name = (
        str(stub_path.with_suffix(""))
        .replace(f"{stubs_out_dir}/", "")
        .replace("/", ".")
    )
    module_imported = importlib.import_module(module_name)

    top_level_objs = [
        o for o in module_ast.body if isinstance(o, (ast.ClassDef, ast.FunctionDef))
    ]
    for obj in top_level_objs:
        expanded_docstring = getattr(module_imported, obj.name).__doc__

        if isinstance(obj, ast.ClassDef):
            obj_type = "class"
        else:
            assert isinstance(obj, ast.FunctionDef)
            obj_type = "function"

        if obj.name in OBJS_EXCLUDES:
            print(f"⏭️  {module_name}.{obj.name} is explicitly excluded, skipping")
            continue
        if dataclasses.is_dataclass(getattr(module_imported, obj.name)):
            print(f"⏭️  {module_name}.{obj.name} is a dataclass, skipping")
            continue
        elif expanded_docstring:
            print(f"📝 Expanding docstring for {module_name}.{obj.name}")

            # Special handling for docstring manipulation done through
            # the @deprecated decorator
            # We need to correct the indentation (add spaces before
            # the ".. warning::" directive)
            expanded_docstring = expanded_docstring.split("\n")
            for line_idx, line in enumerate(expanded_docstring):
                if line.startswith(".. warning:: DEPRECATED:"):
                    print(
                        f"🦄 Applying special handling for @deprecated {obj_type} "
                        f"{module_name}.{obj.name}"
                    )
                    line = line.replace(".. warning:: DEPRECATED:", "# DEPRECATED")
                    expanded_docstring[line_idx] = (obj.col_offset + 4) * " " + line
                    break

            # Make first line bold
            expanded_docstring[0] = f"### {expanded_docstring[0]}"

            expanded_docstring = "\n".join(expanded_docstring)
            obj.body[0].value.value = expanded_docstring

            # FIXME We do have a docstring, but sometimes the AST doesn't
            # contain the method body?! So we add an ellipsis here manually
            if len(obj.body) == 1:
                print(
                    f"⛑️  Fixing empty body for {obj_type} "
                    f"{module_name}.{obj.name}.{obj.name}"
                )
                obj.body.append(ast.Expr(ast.Ellipsis()))
        else:
            print(f"⏭️  No docstring found for {module_name}.{obj.name}, skipping")
            # Still continue below if object is a class
            if not isinstance(obj, ast.ClassDef):
                continue

        # If it's a class, iterate over its methods
        if obj_type == "class":
            methods = [m for m in obj.body if isinstance(m, ast.FunctionDef)]
            if not methods:
                continue

            for method in methods:
                expanded_docstring = getattr(
                    getattr(module_imported, obj.name), method.name
                ).__doc__
                if expanded_docstring:
                    print(
                        f"📝 Expanding docstring for method "
                        f"{module_name}.{obj.name}.{method.name}"
                    )

                    # Special handling for docstring manipulation done through
                    # the @deprecated decorator
                    # We need to correct the indentation (add spaces before
                    # the ".. warning::" directive)
                    expanded_docstring = expanded_docstring.split("\n")
                    for line_idx, line in enumerate(expanded_docstring):
                        if line.startswith(".. warning:: DEPRECATED:"):
                            print(
                                f"🦄 Applying special handling for @deprecated method "
                                f"{module_name}.{obj.name}.{method.name}"
                            )
                            line = line.replace(
                                ".. warning:: DEPRECATED:", "# DEPRECATED"
                            )
                            expanded_docstring[line_idx] = (
                                method.col_offset + 4
                            ) * " " + line
                            break

                    # Make first line bold
                    expanded_docstring[0] = f"### {expanded_docstring[0]}"

                    expanded_docstring = "\n".join(expanded_docstring)
                    method.body[0].value.value = expanded_docstring

                    # FIXME We do have a docstring, but sometimes the AST doesn't
                    # contain the method body?! So we add an ellipsis here manually
                    if len(method.body) == 1:
                        print(
                            f"⛑️  Fixing empty body for method "
                            f"{module_name}.{obj.name}.{method.name}"
                        )
                        method.body.append(ast.Expr(ast.Ellipsis()))
                else:
                    print(
                        f"⏭️  No docstring found for "
                        f"{module_name}.{obj.name}.{method.name}, skipping"
                    )
                    continue

    # Clean the stub file contents
    print(f"🧽 Cleaning stub file: {stub_path}")
    unparsed = ast.unparse(module_ast)
    unparsed_cleaned = (
        unparsed.replace(": Incomplete | None=", "=")
        .replace(", verbose as verbose,", ",")
        .replace(", verbose as verbose", "")
        .replace("import verbose as verbose,", "import")
        .replace("from ..utils import verbose as verbose", "")
        .replace("from ...utils import verbose as verbose", "")
        .replace("`~", "`")
        .replace(":class:", "")
        .replace(":meth:", "")
        .replace(":func:", "")
        .replace(":mod:", "")
        .replace(":ref:", "")
        .replace(".. warning::", "### ⛔️ Warning")
        .replace(".. Warning::", "### ⛔️ Warning")
        .replace(".. note::", "### 💡 Note")
        .replace(".. versionadded::", "✨ Added in vesion")
        .replace(".. versionchanged::", "🎭 Changed in version")
        .replace("Parameters\n", "### 🛠️ Parameters\n")
        .replace("Attributes\n", "### 📊 Attributes\n")
        .replace("Returns\n", "### ⏎ Returns\n")
        .replace("Notes\n", "### 📖 Notes\n")
        .replace("See Also\n", "### 👉 See Also\n")
    )
    del unparsed

    # Write modified stub to disk
    print(f"💾 Writing stub file to disk: {stub_path}")
    stub_path.write_text(unparsed_cleaned, encoding="utf-8")

print("💾 Writing py.typed file")
(stubs_out_dir / "mne" / "py.typed").write_text("partial\n", encoding="utf-8")

print("📊 Adding parameter default values to stub files")
if (
    subprocess.run(["python", "-m", "stubdefaulter", "--packages=typings"]).returncode
    != 0
):
    sys.exit(1)

print("😵 Running Ruff on stub files")
if (
    subprocess.run(
        ["ruff", "--ignore=F811,F821", "--fix", f"{stubs_out_dir}/mne"]
    ).returncode
    != 0
):
    sys.exit(1)

print("⚫️ Running Black on stub files")
if subprocess.run(["black", "--quiet", f"{stubs_out_dir}/mne"]).returncode != 0:
    sys.exit(1)

print("\n💚 Done! Happy typing!")
