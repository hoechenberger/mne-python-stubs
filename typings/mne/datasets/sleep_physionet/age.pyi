from ._utils import AGE_SLEEP_RECORDS as AGE_SLEEP_RECORDS
from _typeshed import Incomplete

data_path: Incomplete
BASE_URL: str

def fetch_data(
    subjects,
    recording=(1, 2),
    path=None,
    force_update: bool = False,
    base_url="https://physionet.org/physiobank/database/sleep-edfx/sleep-cassette/",
    on_missing: str = "raise",
    *,
    verbose=None,
):
    """### Get paths to local copies of PhysioNet Polysomnography dataset files.

    This will fetch data from the publicly available subjects from PhysioNet's
    study of age effects on sleep in healthy subjects
    :footcite:`MourtazaevEtAl1995,GoldbergerEtAl2000`. This
    corresponds to a subset of 153 recordings from 37 males and 41 females that
    were 25-101 years old at the time of the recordings. There are two night
    recordings per subject except for subjects 13, 36 and 52 which have one
    record missing each due to missing recording hardware.

    See more details in
    `physionet website <https://physionet.org/physiobank/database/sleep-edfx/sleep-cassette/>`_.

    ### 🛠️ Parameters
    ----------
    subjects : list of int
        The subjects to use. Can be in the range of 0-82 (inclusive), however
        the following subjects are not available: 39, 68, 69, 78 and 79.
    recording : list of int
        The night recording indices. Valid values are : [1], [2], or [1, 2].
        The following recordings are not available: recording 1 for subject 36
        and 52, and recording 2 for subject 13.
    path : None | str
        Location of where to look for the PhysioNet data storing location.
        If None, the environment variable or config parameter
        ``PHYSIONET_SLEEP_PATH`` is used. If it doesn't exist, the "~/mne_data"
        directory is used. If the Polysomnography dataset is not found under
        the given path, the data will be automatically downloaded to the
        specified folder.
    force_update : bool
        Force update of the dataset even if a local copy exists.
    base_url : str
        The URL root.
    on_missing : 'raise' | 'warn' | 'ignore'
        What to do if one or several recordings are not available. Valid keys
        are 'raise' | 'warn' | 'ignore'. Default is 'error'. If on_missing
        is 'warn' it will proceed but warn, if 'ignore' it will proceed
        silently.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    paths : list
        List of local data paths of the given type.

    ### 👉 See Also
    --------
    mne.datasets.sleep_physionet.temazepam.fetch_data

    ### 📖 Notes
    -----
    For example, one could do:

        >>> from mne.datasets import sleep_physionet
        >>> sleep_physionet.age.fetch_data(subjects=[0])  # doctest: +SKIP

    This would download data for subject 0 if it isn't there already.

    References
    ----------
    .. footbibliography::
    """
    ...
