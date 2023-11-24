from ...utils import verbose as verbose
from _typeshed import Incomplete

def data_path(path: Incomplete | None=..., force_update: bool=..., update_path: bool=..., download: bool=..., *, verbose: Incomplete | None=...):
    """Get path to local copy of the kiloword dataset.

    This is the dataset from :footcite:`DufauEtAl2015`.

    Parameters
    ----------
    path : None | str
        Location of where to look for the kiloword data storing
        location. If None, the environment variable or config parameter
        MNE_DATASETS_KILOWORD_PATH is used. If it doesn't exist,
        the "mne-python/examples" directory is used. If the
        kiloword dataset is not found under the given path (e.g.,
        as "mne-python/examples/MNE-kiloword-data"), the data
        will be automatically downloaded to the specified folder.
    force_update : bool
        Force update of the dataset even if a local copy exists.
    update_path : bool | None
        If True, set the MNE_DATASETS_KILOWORD_PATH in mne-python
        config to the given path. If None, the user is prompted.
    download : bool
        If False and the kiloword dataset has not been downloaded yet,
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
    path : list of Path
        Local path to the given data file. This path is contained inside a list
        of length one, for compatibility.

    References
    ----------
    .. footbibliography::
    """

def get_version():
    """Get version of the local kiloword dataset.

    Returns
    -------
    version : str | None
        Version of the kiloword local dataset, or None if the dataset
        does not exist locally.
"""