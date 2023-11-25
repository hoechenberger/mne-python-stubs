# %%
import ast
import dataclasses
import importlib
import shutil
from pathlib import Path

from mypy import stubgen

# Module exclusion patterns
# Note that __init__.py files are handled specially below, do not
# include them here.
MODULE_PY_EXCLUDE_PATTERNS = [
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

objs_excludes = [
    # NamedTuples – somehow I cannot detect them via isinstance(obj, tuple)??
    "CurryParameters",
    "CNTEventType1",
    "CNTEventType2",
    "CNTEventType3",
    "_ica_node",
    # PyVista stuff causing trouble
    "_SafeBackgroundPlotter",
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
        if obj.name.startswith(("_Abstract", "_Base")):
            print(f"⏭️  Skipping base class {obj.name}")
            continue

        expanded_docstring = getattr(module_imported, obj.name).__doc__

        if obj.name in objs_excludes:
            print(f"⏭️  {module_name}.{obj.name} is explicitly excluded, skipping")
            continue
        if dataclasses.is_dataclass(getattr(module_imported, obj.name)):
            print(f"⏭️  {module_name}.{obj.name} is a dataclass, skipping")
            continue
        elif expanded_docstring:
            print(f"📝 Expanding docstring for {module_name}.{obj.name}")
            obj.body[0].value.value = expanded_docstring
        else:
            print(f"⏭️  No docstring found for {module_name}.{obj.name}, skipping")
            # Still continue below if object is a class
            if not isinstance(obj, ast.ClassDef):
                continue

        # If it's a class, iterate over its methods
        if isinstance(obj, ast.ClassDef):
            methods = [m for m in obj.body if isinstance(m, ast.FunctionDef)]
            if not methods:
                continue
            for method in methods:
                expanded_docstring = getattr(
                    getattr(module_imported, obj.name), method.name
                ).__doc__
                if expanded_docstring:
                    print(
                        f"📝 Expanding docstring for "
                        f"{module_name}.{obj.name}.{method.name}"
                    )
                    obj.body[0].value.value = expanded_docstring
                else:
                    print(
                        f"⏭️  No docstring found for "
                        f"{module_name}.{obj.name}.{method.name}, skipping"
                    )
                    continue

                method.body[0].value.value = expanded_docstring

    # Write modified stub to disk
    print(f"💾 Writing stub file to disk: {stub_path}")
    unparsed = ast.unparse(module_ast)
    stub_path.write_text(unparsed, encoding="utf-8")

print("💾 Writing py.typed file")
(stubs_out_dir / "mne" / "py.typed").write_text("partial\n", encoding="utf-8")

print("\n💚 Done! Happy typing!")
