from ..._fiff.meas_info import create_info as create_info
from ...channels import make_standard_montage as make_standard_montage
from ...epochs import EpochsArray as EpochsArray
from ...utils import logger as logger, verbose as verbose
from _typeshed import Incomplete
root_url: str

def data_path(subject, path: Incomplete | None=..., force_update: bool=..., update_path: Incomplete | None=..., *, verbose: Incomplete | None=...):
    """Get path to local copy of LIMO dataset URL.

    This is a low-level function useful for getting a local copy of the
    remote LIMO dataset :footcite:`Rousselet2016`. The complete dataset is
    available at datashare.is.ed.ac.uk/.

    Parameters
    ----------
    subject : int
        Subject to download. Must be of :class:`ìnt` in the range from 1
        to 18 (inclusive).
    path : None | str
        Location of where to look for the LIMO data storing directory.
        If None, the environment variable or config parameter
        ``MNE_DATASETS_LIMO_PATH`` is used. If it doesn't exist, the
        "~/mne_data" directory is used. If the LIMO dataset
        is not found under the given path, the data
        will be automatically downloaded to the specified folder.
    force_update : bool
        Force update of the dataset even if a local copy exists.
    update_path : bool | None
        If True, set the MNE_DATASETS_LIMO_PATH in mne-python
        config to the given path. If None, the user is prompted.
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    path : str
        Local path to the given data file.

    Notes
    -----
    For example, one could do:

        >>> from mne.datasets import limo
        >>> limo.data_path(subject=1, path=os.getenv('HOME') + '/datasets') # doctest:+SKIP

    This would download the LIMO data file to the 'datasets' folder,
    and prompt the user to save the 'datasets' path to the mne-python config,
    if it isn't there already.

    References
    ----------
    .. footbibliography::
    """

def load_data(subject, path: Incomplete | None=..., force_update: bool=..., update_path: Incomplete | None=..., verbose: Incomplete | None=...):
    """Fetch subjects epochs data for the LIMO data set.

    Parameters
    ----------
    subject : int
        Subject to use. Must be of class ìnt in the range from 1 to 18.
    path : str
        Location of where to look for the LIMO data.
        If None, the environment variable or config parameter
        ``MNE_DATASETS_LIMO_PATH`` is used. If it doesn't exist, the
        "~/mne_data" directory is used.
    force_update : bool
        Force update of the dataset even if a local copy exists.
    update_path : bool | None
        If True, set the MNE_DATASETS_LIMO_PATH in mne-python
        config to the given path. If None, the user is prompted.
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    epochs : instance of Epochs
        The epochs.
    """