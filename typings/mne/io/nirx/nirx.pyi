from ..._fiff.constants import FIFF as FIFF
from ..._fiff.meas_info import create_info as create_info
from ..._freesurfer import get_mni_fiducials as get_mni_fiducials
from ...annotations import Annotations as Annotations
from ...transforms import apply_trans as apply_trans
from ...utils import fill_doc as fill_doc, logger as logger, warn as warn
from ..base import BaseRaw as BaseRaw

def read_raw_nirx(
    fname, saturated: str = "annotate", preload: bool = False, verbose=None
):
    """Reader for a NIRX fNIRS recording.

    Parameters
    ----------
    fname : path-like
        Path to the NIRX data folder or header file.
    saturated : str
        Replace saturated segments of data with NaNs, can be:

        ``"ignore"``
            The measured data is returned, even if it contains measurements
            while the amplifier was saturated.
        ``"nan"``
            The returned data will contain NaNs during time segments
            when the amplifier was saturated.
        ``"annotate"`` (default)
            The returned data will contain annotations specifying
            sections the saturate segments.

        This argument will only be used if there is no .nosatflags file
        (only if a NIRSport device is used and saturation occurred).

        .. versionadded:: 0.24

    preload : bool or str (default False)
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    raw : instance of RawNIRX
        A Raw object containing NIRX data.
        See `mne.io.Raw` for documentation of attributes and methods.

    See Also
    --------
    mne.io.Raw : Documentation of attributes and methods of RawNIRX.

    Notes
    -----

    This function has only been tested with NIRScout and NIRSport devices,
    and with the NIRStar software version 15 and above and Aurora software
    2021 and above.

    The NIRSport device can detect if the amplifier is saturated.
    Starting from NIRStar 14.2, those saturated values are replaced by NaNs
    in the standard .wlX files.
    The raw unmodified measured values are stored in another file
    called .nosatflags_wlX. As NaN values can cause unexpected behaviour with
    mathematical functions the default behaviour is to return the
    saturated data.
    """
    ...

class RawNIRX(BaseRaw):
    """Raw object from a NIRX fNIRS file.

    Parameters
    ----------
    fname : path-like
        Path to the NIRX data folder or header file.
    saturated : str
        Replace saturated segments of data with NaNs, can be:

        ``"ignore"``
            The measured data is returned, even if it contains measurements
            while the amplifier was saturated.
        ``"nan"``
            The returned data will contain NaNs during time segments
            when the amplifier was saturated.
        ``"annotate"`` (default)
            The returned data will contain annotations specifying
            sections the saturate segments.

        This argument will only be used if there is no .nosatflags file
        (only if a NIRSport device is used and saturation occurred).

        .. versionadded:: 0.24

    preload : bool or str (default False)
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    mne.io.Raw : Documentation of attributes and methods.

    Notes
    -----

    This function has only been tested with NIRScout and NIRSport devices,
    and with the NIRStar software version 15 and above and Aurora software
    2021 and above.

    The NIRSport device can detect if the amplifier is saturated.
    Starting from NIRStar 14.2, those saturated values are replaced by NaNs
    in the standard .wlX files.
    The raw unmodified measured values are stored in another file
    called .nosatflags_wlX. As NaN values can cause unexpected behaviour with
    mathematical functions the default behaviour is to return the
    saturated data.
    """

    def __init__(
        self, fname, saturated, preload: bool = False, verbose=None
    ) -> None: ...
