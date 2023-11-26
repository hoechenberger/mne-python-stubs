from ..utils import logger as logger, warn as warn
from .config import (
    MISC_VERSIONED as MISC_VERSIONED,
    RELEASES as RELEASES,
    TESTING_VERSIONED as TESTING_VERSIONED,
)

def fetch_dataset(
    dataset_params,
    processor=None,
    path=None,
    force_update: bool = False,
    update_path: bool = True,
    download: bool = True,
    check_version: bool = False,
    return_version: bool = False,
    accept: bool = False,
    auth=None,
    token=None,
):
    """### Fetch an MNE-compatible dataset using pooch.

    ### 🛠️ Parameters
    ----------
    dataset_params : list of dict | dict
        The dataset name(s) and corresponding parameters to download the
        dataset(s). The dataset parameters that contains the following keys:
        ``archive_name``, ``url``, ``folder_name``, ``hash``,
        ``config_key`` (optional). See Notes.
    processor : None | "unzip" | "untar" | instance of pooch.Unzip | instance of pooch.Untar
        What to do after downloading the file. ``"unzip"`` and ``"untar"`` will
        decompress the downloaded file in place; for custom extraction (e.g.,
        only extracting certain files from the archive) pass an instance of
        `pooch.Unzip` or `pooch.Untar`. If ``None`` (the
        default), the files are left as-is.
    path : None | str
        Directory in which to put the dataset. If ``None``, the dataset
        location is determined by first checking whether
        ``dataset_params['config_key']`` is defined, and if so, whether that
        config key exists in the MNE-Python config file. If so, the configured
        path is used; if not, the location is set to the value of the
        ``MNE_DATA`` config key (if it exists), or ``/mne_data`` otherwise.
    force_update : bool
        Force update of the dataset even if a local copy exists.
        Default is False.
    update_path : bool | None
        If True (default), set the mne-python config to the given
        path. If None, the user is prompted.
    download : bool
        If False and the dataset has not been downloaded yet, it will not be
        downloaded and the path will be returned as ``''`` (empty string). This
        is mostly used for testing purposes and can be safely ignored by most
        users.
    check_version : bool
        Whether to check the version of the dataset or not. Each version
        of the dataset is stored in the root with a ``version.txt`` file.
    return_version : bool
        Whether or not to return the version of the dataset or not.
        Defaults to False.
    accept : bool
        Some MNE-supplied datasets require acceptance of an additional license.
        Default is ``False``.
    auth : tuple | None
        Optional authentication tuple containing the username and
        password/token, passed to `pooch.HTTPDownloader` (e.g.,
        ``auth=('foo', 012345)``).
    token : str | None
        Optional authentication token passed to `pooch.HTTPDownloader`.

    ### ⏎ Returns
    -------
    data_path : instance of Path
        The path to the fetched dataset.
    version : str
        Only returned if ``return_version`` is True.

    ### 👉 See Also
    --------
    mne.get_config
    mne.set_config
    mne.datasets.has_dataset

    ### 📖 Notes
    -----
    The ``dataset_params`` argument must contain the following keys:

    - ``archive_name``: The name of the (possibly compressed) file to download
    - ``url``: URL from which the file can be downloaded
    - ``folder_name``: the subfolder within the ``MNE_DATA`` folder in which to
        save and uncompress (if needed) the file(s)
    - ``hash``: the cryptographic hash type of the file followed by a colon and
        then the hash value (examples: "sha256:19uheid...", "md5:upodh2io...")
    - ``config_key`` (optional): key passed to `mne.set_config` to store
        the on-disk location of the downloaded dataset (e.g.,
        ``"MNE_DATASETS_EEGBCI_PATH"``). This will only work for the provided
        datasets listed `here <datasets>`; do not use for user-defined
        datasets.

    An example would look like::

        {'dataset_name': 'sample',
         'archive_name': 'MNE-sample-data-processed.tar.gz',
         'hash': 'md5:12b75d1cb7df9dfb4ad73ed82f61094f',
         'url': 'https://osf.io/86qa2/download?version=5',
         'folder_name': 'MNE-sample-data',
         'config_key': 'MNE_DATASETS_SAMPLE_PATH'}

    For datasets where a single (possibly compressed) file must be downloaded,
    pass a single `dict` as ``dataset_params``. For datasets where
    multiple files must be downloaded and (optionally) uncompressed separately,
    pass a list of dicts.
    """
    ...
