from ...utils import verbose as verbose
from _typeshed import Incomplete

def data_path(path: Incomplete | None=..., force_update: bool=..., update_path: bool=..., download: bool=..., *, verbose: Incomplete | None=...):
    """Get path to local copy of phantom_kernel dataset.

    Parameters
    ----------
    path : None | str
        Location of where to look for the phantom_kernel dataset.
        If None, the environment variable or config parameter
        ``MNE_DATASETS_PHANTOM_KERNEL_PATH`` is used. If it doesn't exist, the
        "~/mne_data" directory is used. If the phantom_kernel dataset
        is not found under the given path, the data
        will be automatically downloaded to the specified folder.
    force_update : bool
        Force update of the phantom_kernel dataset even if a local copy exists.
        Default is False.
    update_path : bool | None
        If True (default), set the ``MNE_DATASETS_PHANTOM_KERNEL_PATH`` in mne-python
        config to the given path. If None, the user is prompted.
    download : bool
        If False and the phantom_kernel dataset has not been downloaded yet,
        it will not be downloaded and the path will be returned as
        '' (empty string). This is mostly used for debugging purposes
        and can be safely ignored by most users.
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    path : instance of Path
        Path to phantom_kernel dataset directory.
"""

def get_version():
    """Get version of the local phantom_kernel dataset.

    Returns
    -------
    version : str | None
        Version of the phantom_kernel local dataset, or None if the dataset
        does not exist locally.
"""