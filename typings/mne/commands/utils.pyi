from _typeshed import Incomplete

def load_module(name, path):
    """Load module from .py/.pyc file.

    Parameters
    ----------
    name : str
        Name of the module.
    path : str
        Path to .py/.pyc file.

    Returns
    -------
    mod : module
        Imported module.

    """

def get_optparser(cmdpath, usage: Incomplete | None=..., prog_prefix: str=..., version: Incomplete | None=...):
    """Create OptionParser with cmd specific settings (e.g., prog value)."""

def main() -> None:
    """Entrypoint for mne <command> usage."""