from ..._fiff.constants import FIFF as FIFF
from ..._fiff.meas_info import create_info as create_info
from ...annotations import Annotations as Annotations
from ...transforms import (
    Transform as Transform,
    apply_trans as apply_trans,
    combine_transforms as combine_transforms,
    get_ras_to_neuromag_trans as get_ras_to_neuromag_trans,
    invert_transform as invert_transform,
    rot_to_quat as rot_to_quat,
)
from ...utils import check_fname as check_fname, logger as logger
from ..base import BaseRaw as BaseRaw
from _typeshed import Incomplete
from typing import NamedTuple

FILE_EXTENSIONS: Incomplete
CHANTYPES: Incomplete
FIFFV_CHANTYPES: Incomplete
FIFFV_COILTYPES: Incomplete
SI_UNITS: Incomplete
SI_UNIT_SCALE: Incomplete

class CurryParameters(NamedTuple):
    n_samples: Incomplete
    sfreq: Incomplete
    is_ascii: Incomplete
    unit_dict: Incomplete
    n_chans: Incomplete
    dt_start: Incomplete
    chanidx_in_file: Incomplete

def read_raw_curry(fname, preload: bool = ..., verbose=...):
    """Read raw data from Curry files.

    Parameters
    ----------
    fname : path-like
        Path to a curry file with extensions ``.dat``, ``.dap``, ``.rs3``,
        ``.cdt``, ``.cdt.dpa``, ``.cdt.cef`` or ``.cef``.

    preload : bool or str (default False)
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    raw : instance of RawCurry
        A Raw object containing Curry data.
        See :class:`mne.io.Raw` for documentation of attributes and methods.

    See Also
    --------
    mne.io.Raw : Documentation of attributes and methods of RawCurry.
    """

class RawCurry(BaseRaw):
    """Raw object from Curry file.

    Parameters
    ----------
    fname : path-like
        Path to a curry file with extensions ``.dat``, ``.dap``, ``.rs3``,
        ``.cdt``, ``.cdt.dpa``, ``.cdt.cef`` or ``.cef``.
    %(preload)s
    %(verbose)s

    See Also
    --------
    mne.io.Raw : Documentation of attributes and methods.

    """

    def __init__(self, fname, preload: bool = ..., verbose=...) -> None: ...
