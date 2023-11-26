from ...utils import logger as logger

EEGMI_URL: str

def data_path(
    url, path=None, force_update: bool = False, update_path=None, *, verbose=None
):
    """## 🧠 Get path to local copy of EEGMMI dataset URL.

    This is a low-level function useful for getting a local copy of a remote EEGBCI
    dataset :footcite:`SchalkEtAl2004`, which is also available at PhysioNet
    :footcite:`GoldbergerEtAl2000`.

    -----
    ### 🛠️ Parameters

    #### `url : str`
        The dataset to use.
    #### `path : None | path-like`
        Location of where to look for the EEGBCI data. If ``None``, the environment
        variable or config parameter ``MNE_DATASETS_EEGBCI_PATH`` is used. If neither
        exists, the ``/mne_data`` directory is used. If the EEGBCI dataset is not found
        under the given path, the data will be automatically downloaded to the specified
        folder.
    #### `force_update : bool`
        Force update of the dataset even if a local copy exists.
    #### `update_path : bool | None`
        If ``True``, set ``MNE_DATASETS_EEGBCI_PATH`` in the configuration to the given
        path. If ``None``, the user is prompted.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `path : list of Path`
        Local path to the given data file. This path is contained inside a list of
        length one for compatibility.

    -----
    ### 📖 Notes

    For example, one could do:

        >>> from mne.datasets import eegbci
        >>> url = "http://www.physionet.org/physiobank/database/eegmmidb/"
        >>> eegbci.data_path(url, "~/datasets") # doctest:+SKIP

    This would download the given EEGBCI data file to the ``/datasets`` folder and
    prompt the user to store this path in the config (if it does not already exist).

    References
    ----------
    .. footbibliography::
    """
    ...

def load_data(
    subject,
    runs,
    path=None,
    force_update: bool = False,
    update_path=None,
    base_url="https://physionet.org/files/eegmmidb/1.0.0/",
    verbose=None,
):
    """## 🧠 Get paths to local copies of EEGBCI dataset files.

    This will fetch data for the EEGBCI dataset :footcite:`SchalkEtAl2004`, which is
    also available at PhysioNet :footcite:`GoldbergerEtAl2000`.

    -----
    ### 🛠️ Parameters

    #### `subject : int`
        The subject to use. Can be in the range of 1-109 (inclusive).
    #### `runs : int | list of int`
        The runs to use (see Notes for details).
    #### `path : None | path-like`
        Location of where to look for the EEGBCI data. If ``None``, the environment
        variable or config parameter ``MNE_DATASETS_EEGBCI_PATH`` is used. If neither
        exists, the ``/mne_data`` directory is used. If the EEGBCI dataset is not found
        under the given path, the data will be automatically downloaded to the specified
        folder.
    #### `force_update : bool`
        Force update of the dataset even if a local copy exists.
    #### `update_path : bool | None`
        If ``True``, set ``MNE_DATASETS_EEGBCI_PATH`` in the configuration to the given
        path. If ``None``, the user is prompted.
    #### `base_url : str`
        The URL root for the data.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `paths : list`
        List of local data paths of the given type.

    -----
    ### 📖 Notes

    The run numbers correspond to:

    =========  ===================================
    run        task
    =========  ===================================
    1          Baseline, eyes open
    2          Baseline, eyes closed
    3, 7, 11   Motor execution: left vs right hand
    4, 8, 12   Motor imagery: left vs right hand
    5, 9, 13   Motor execution: hands vs feet
    6, 10, 14  Motor imagery: hands vs feet
    =========  ===================================

    For example, one could do::

        >>> from mne.datasets import eegbci
        >>> eegbci.load_data(1, [6, 10, 14], "~/datasets") # doctest:+SKIP

    This would download runs 6, 10, and 14 (hand/foot motor imagery) runs from subject 1
    in the EEGBCI dataset to "~/datasets" and prompt the user to store this path in the
    config (if it does not already exist).

    References
    ----------
    .. footbibliography::
    """
    ...

def standardize(raw) -> None:
    """## 🧠 Standardize channel positions and names.

    -----
    ### 🛠️ Parameters

    #### `raw : instance of Raw`
        The raw data to standardize. Operates in-place.
    """
    ...
