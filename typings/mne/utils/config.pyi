from ._logging import logger as logger, warn as warn
from .docs import fill_doc as fill_doc

def set_cache_dir(cache_dir) -> None:
    """Set the directory to be used for temporary file storage.

    This directory is used by joblib to store memmapped arrays,
    which reduces memory requirements and speeds up parallel
    computation.

    Parameters
    ----------
    cache_dir : str or None
        Directory to use for temporary file storage. None disables
        temporary file storage.
    """
    ...

def set_memmap_min_size(memmap_min_size) -> None:
    """Set the minimum size for memmaping of arrays for parallel processing.

    Parameters
    ----------
    memmap_min_size : str or None
        Threshold on the minimum size of arrays that triggers automated memory
        mapping for parallel processing, e.g., '1M' for 1 megabyte.
        Use None to disable memmaping of large arrays.
    """
    ...

def get_config_path(home_dir=None):
    """Get path to standard mne-python config file.

    Parameters
    ----------
    home_dir : str | None
        The folder that contains the .mne config folder.
        If None, it is found automatically.

    Returns
    -------
    config_path : str
        The path to the mne-python configuration file. On windows, this
        will be '%USERPROFILE%\\.mne\\mne-python.json'. On every other
        system, this will be ~/.mne/mne-python.json.
    """
    ...

def get_config(
    key=None,
    default=None,
    raise_error: bool = False,
    home_dir=None,
    use_env: bool = True,
):
    """Read MNE-Python preferences from environment or config file.

    Parameters
    ----------
    key : None | str
        The preference key to look for. The os environment is searched first,
        then the mne-python config file is parsed.
        If None, all the config parameters present in environment variables or
        the path are returned. If key is an empty string, a list of all valid
        keys (but not values) is returned.
    default : str | None
        Value to return if the key is not found.
    raise_error : bool
        If True, raise an error if the key is not found (instead of returning
        default).
    home_dir : str | None
        The folder that contains the .mne config folder.
        If None, it is found automatically.
    use_env : bool
        If True, consider env vars, if available.
        If False, only use MNE-Python configuration file values.

        ✨ Added in version 0.18

    Returns
    -------
    value : dict | str | None
        The preference key value.

    See Also
    --------
    set_config
    """
    ...

def set_config(key, value, home_dir=None, set_env: bool = True) -> None:
    """Set a MNE-Python preference key in the config file and environment.

    Parameters
    ----------
    key : str
        The preference key to set.
    value : str |  None
        The value to assign to the preference key. If None, the key is
        deleted.
    home_dir : str | None
        The folder that contains the .mne config folder.
        If None, it is found automatically.
    set_env : bool
        If True (default), update :data:`os.environ` in addition to
        updating the MNE-Python config file.

    See Also
    --------
    get_config
    """
    ...

def get_subjects_dir(subjects_dir=None, raise_error: bool = False):
    """Safely use subjects_dir input to return SUBJECTS_DIR.

    Parameters
    ----------
    subjects_dir : path-like | None
        If a value is provided, return subjects_dir. Otherwise, look for
        SUBJECTS_DIR config and return the result.
    raise_error : bool
        If True, raise a KeyError if no value for SUBJECTS_DIR can be found
        (instead of returning None).

    Returns
    -------
    value : Path | None
        The SUBJECTS_DIR value.
    """
    ...

def sys_info(
    fid=None,
    show_paths: bool = False,
    *,
    dependencies: str = "user",
    unicode: bool = True,
    check_version: bool = True,
) -> None:
    """Print system information.

    This function prints system information useful when triaging bugs.

    Parameters
    ----------
    fid : file-like | None
        The file to write to. Will be passed to `print()`. Can be None to
        use :data:`sys.stdout`.
    show_paths : bool
        If True, print paths for each module.
    dependencies : 'user' | 'developer'
        Show dependencies relevant for users (default) or for developers
        (i.e., output includes additional dependencies).
    unicode : bool
        Include Unicode symbols in output.

        ✨ Added in version 0.24
    check_version : bool | float
        If True (default), attempt to check that the version of MNE-Python is up to date
        with the latest release on GitHub. Can be a float to give a different timeout
        (in sec) from the default (2 sec).

        ✨ Added in version 1.6
    """
    ...
