from ...utils import get_config as get_config, verbose as verbose
from ..utils import has_dataset as has_dataset
from _typeshed import Incomplete
has_spm_data: Incomplete

def data_path(path: Incomplete | None=..., force_update: bool=..., update_path: bool=..., download: bool=..., *, verbose: Incomplete | None=...):
    """Get path to local copy of spm dataset.

    Parameters
    ----------
    path : None | str
        Location of where to look for the spm dataset.
        If None, the environment variable or config parameter
        ``MNE_DATASETS_SPM_DATA_PATH`` is used. If it doesn't exist, the
        "~/mne_data" directory is used. If the spm dataset
        is not found under the given path, the data
        will be automatically downloaded to the specified folder.
    force_update : bool
        Force update of the spm dataset even if a local copy exists.
        Default is False.
    update_path : bool | None
        If True (default), set the ``MNE_DATASETS_SPM_DATA_PATH`` in mne-python
        config to the given path. If None, the user is prompted.
    download : bool
        If False and the spm dataset has not been downloaded yet,
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
        Path to spm dataset directory.
"""

def get_version():
    """Get version of the local spm dataset.

    Returns
    -------
    version : str | None
        Version of the spm local dataset, or None if the dataset
        does not exist locally.
"""

def requires_spm_data(func):
    """Skip testing data test."""