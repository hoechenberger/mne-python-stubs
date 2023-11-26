def data_path(
    path=None,
    force_update: bool = False,
    update_path: bool = True,
    download: bool = True,
    *,
    verbose=None,
):
    """### Get path to local copy of ucl_opm_auditory dataset.

    ### 🛠️ Parameters
    ----------
    path : None | str
        Location of where to look for the ucl_opm_auditory dataset.
        If None, the environment variable or config parameter
        ``MNE_DATASETS_UCL_OPM_AUDITORY_PATH`` is used. If it doesn't exist, the
        "~/mne_data" directory is used. If the ucl_opm_auditory dataset
        is not found under the given path, the data
        will be automatically downloaded to the specified folder.
    force_update : bool
        Force update of the ucl_opm_auditory dataset even if a local copy exists.
        Default is False.
    update_path : bool | None
        If True (default), set the ``MNE_DATASETS_UCL_OPM_AUDITORY_PATH`` in mne-python
        config to the given path. If None, the user is prompted.
    download : bool
        If False and the ucl_opm_auditory dataset has not been downloaded yet,
        it will not be downloaded and the path will be returned as
        '' (empty string). This is mostly used for debugging purposes
        and can be safely ignored by most users.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    path : instance of Path
        Path to ucl_opm_auditory dataset directory."""
    ...

def get_version():
    """### Get version of the local ucl_opm_auditory dataset.

    ### ⏎ Returns
    -------
    version : str | None
        Version of the ucl_opm_auditory local dataset, or None if the dataset
        does not exist locally."""
    ...
