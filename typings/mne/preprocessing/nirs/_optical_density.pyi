from ..._fiff.constants import FIFF as FIFF
from ...io import BaseRaw as BaseRaw
from ...utils import warn as warn

def optical_density(raw, *, verbose=None):
    """Convert NIRS raw data to optical density.

    Parameters
    ----------
    raw : instance of Raw
        The raw data.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    raw : instance of Raw
        The modified raw instance.
    """
