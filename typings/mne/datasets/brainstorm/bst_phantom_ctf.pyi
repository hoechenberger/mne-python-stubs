
def data_path(
    path=...,
    force_update: bool = ...,
    update_path: bool = ...,
    download: bool = ...,
    accept: bool = ...,
    *,
    verbose=...,
):
    """Get path to local copy of brainstorm (bst_phantom_ctf) dataset.

    Parameters
    ----------
    path : None | str
        Location of where to look for the brainstorm (bst_phantom_ctf) dataset.
        If None, the environment variable or config parameter
        ``MNE_DATASETS_BRAINSTORM_DATA_PATH`` is used. If it doesn't exist, the
        "~/mne_data" directory is used. If the brainstorm (bst_phantom_ctf) dataset
        is not found under the given path, the data
        will be automatically downloaded to the specified folder.
    force_update : bool
        Force update of the brainstorm (bst_phantom_ctf) dataset even if a local copy exists.
        Default is False.
    update_path : bool | None
        If True (default), set the ``MNE_DATASETS_BRAINSTORM_DATA_PATH`` in mne-python
        config to the given path. If None, the user is prompted.
    download : bool
        If False and the brainstorm (bst_phantom_ctf) dataset has not been downloaded yet,
        it will not be downloaded and the path will be returned as
        '' (empty string). This is mostly used for debugging purposes
        and can be safely ignored by most users.

    accept : bool
        If True (default False), accept the license terms of this dataset.
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    path : instance of Path
        Path to brainstorm (bst_phantom_ctf) dataset directory."""

def get_version():
    """Get version of the local brainstorm dataset.

    Returns
    -------
    version : str | None
        Version of the brainstorm local dataset, or None if the dataset
        does not exist locally."""

def description() -> None:
    """Get description of brainstorm (bst_phantom_ctf) dataset."""
