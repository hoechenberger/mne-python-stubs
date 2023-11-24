from ...utils import verbose as verbose
from ._utils import TEMAZEPAM_SLEEP_RECORDS as TEMAZEPAM_SLEEP_RECORDS
from _typeshed import Incomplete
data_path: Incomplete
BASE_URL: str

def fetch_data(subjects, path: Incomplete | None=..., force_update: bool=..., base_url=..., *, verbose: Incomplete | None=...):
    """Get paths to local copies of PhysioNet Polysomnography dataset files.

    This will fetch data from the publicly available subjects from PhysioNet's
    study of Temazepam effects on sleep :footcite:`KempEtAl2000`. This
    corresponds to a set of 22 subjects. Subjects had mild difficulty falling
    asleep but were otherwise healthy.

    See more details in the `physionet website
    <https://physionet.org/physiobank/database/sleep-edfx/>`_
    :footcite:`GoldbergerEtAl2000`.

    Parameters
    ----------
    subjects : list of int
        The subjects to use. Can be in the range of 0-21 (inclusive).
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
        The base URL to download from.
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    paths : list
        List of local data paths of the given type.

    See Also
    --------
    mne.datasets.sleep_physionet.age.fetch_data

    Notes
    -----
    For example, one could do:

        >>> from mne.datasets import sleep_physionet
        >>> sleep_physionet.temazepam.fetch_data(subjects=[1]) # doctest: +SKIP

    This would download data for subject 0 if it isn't there already.

    References
    ----------
    .. footbibliography::
    """