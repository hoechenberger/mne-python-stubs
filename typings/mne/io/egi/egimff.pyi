import datetime
from ..._fiff.constants import FIFF as FIFF
from ..._fiff.meas_info import create_info as create_info
from ..._fiff.proj import setup_proj as setup_proj
from ...annotations import Annotations as Annotations
from ...channels.montage import make_dig_montage as make_dig_montage
from ...evoked import EvokedArray as EvokedArray
from ...utils import logger as logger, warn as warn
from ..base import BaseRaw as BaseRaw
from _typeshed import Incomplete

REFERENCE_NAMES: Incomplete

class _FixedOffset(datetime.tzinfo):
    """Fixed offset in minutes east from UTC.

    Adapted from the official Python documentation.
    """

    def __init__(self, offset) -> None: ...
    def utcoffset(self, dt): ...
    def tzname(self, dt): ...
    def dst(self, dt): ...

class RawMff(BaseRaw):
    """RawMff class."""

    event_id: Incomplete

    def __init__(
        self,
        input_fname,
        eog=None,
        misc=None,
        include=None,
        exclude=None,
        preload: bool = False,
        channel_naming: str = "E%d",
        verbose=None,
    ) -> None:
        """Init the RawMff class."""
        ...

def read_evokeds_mff(
    fname, condition=None, channel_naming: str = "E%d", baseline=None, verbose=None
):
    """Read averaged MFF file as EvokedArray or list of EvokedArray.

    Parameters
    ----------
    fname : path-like
        File path to averaged MFF file. Should end in ``.mff``.
    condition : int or str | list of int or str | None
        The index (indices) or category (categories) from which to read in
        data. Averaged MFF files can contain separate averages for different
        categories. These can be indexed by the block number or the category
        name. If ``condition`` is a list or None, a list of EvokedArray objects
        is returned.
    channel_naming : str
        Channel naming convention for EEG channels. Defaults to 'E%d'
        (resulting in channel names 'E1', 'E2', 'E3'...).
    baseline : None (default) or tuple of length 2
        The time interval to apply baseline correction. If None do not apply
        it. If baseline is (a, b) the interval is between "a (s)" and "b (s)".
        If a is None the beginning of the data is used and if b is None then b
        is set to the end of the interval. If baseline is equal to (None, None)
        all the time interval is used. Correction is applied by computing mean
        of the baseline period and subtracting it from the data. The baseline
        (a, b) includes both endpoints, i.e. all timepoints t such that
        a <= t <= b.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    evoked : EvokedArray or list of EvokedArray
        The evoked dataset(s); one EvokedArray if condition is int or str,
        or list of EvokedArray if condition is None or list.

    Raises
    ------
    ValueError
        If ``fname`` has file extension other than '.mff'.
    ValueError
        If the MFF file specified by ``fname`` is not averaged.
    ValueError
        If no categories.xml file in MFF directory specified by ``fname``.

    See Also
    --------
    Evoked, EvokedArray, create_info

    Notes
    -----
    ✨ Added in version 0.22
    """
    ...
