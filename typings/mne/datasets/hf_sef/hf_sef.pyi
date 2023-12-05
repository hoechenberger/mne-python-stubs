from ..config import MNE_DATASETS as MNE_DATASETS

def data_path(
    dataset: str = "evoked",
    path=None,
    force_update: bool = False,
    update_path: bool = True,
    *,
    verbose=None,
):
    """Get path to local copy of the high frequency SEF dataset.

    Gets a local copy of the high frequency SEF MEG dataset
    :footcite:`NurminenEtAl2017`.

    Parameters
    ----------
    dataset : 'evoked' | 'raw'
        Whether to get the main dataset (evoked, structural and the rest) or
        the separate dataset containing raw MEG data only.
    path : None | str
        Where to look for the HF-SEF data storing location.
        If None, the environment variable or config parameter
        ``MNE_DATASETS_HF_SEF_PATH`` is used. If it doesn't exist, the
        "~/mne_data" directory is used. If the HF-SEF dataset
        is not found under the given path, the data
        will be automatically downloaded to the specified folder.
    force_update : bool
        Force update of the dataset even if a local copy exists.
    update_path : bool | None
        If True, set the MNE_DATASETS_HF_SEF_PATH in mne-python
        config to the given path. If None, the user is prompted.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    path : str
        Local path to the directory where the HF-SEF data is stored.

    References
    ----------
    .. footbibliography::
    """
    ...
