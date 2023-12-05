from ..._fiff.constants import FIFF as FIFF
from ..._fiff.meas_info import create_info as create_info
from ..._freesurfer import get_mni_fiducials as get_mni_fiducials
from ...annotations import Annotations as Annotations
from ...transforms import apply_trans as apply_trans
from ...utils import fill_doc as fill_doc, logger as logger, warn as warn
from ..base import BaseRaw as BaseRaw

def read_raw_snirf(
    fname, optode_frame: str = "unknown", preload: bool = False, verbose=None
):
    """Reader for a continuous wave SNIRF data.

    💡 Note This reader supports the .snirf file type only,
              not the .jnirs version.
              Files with either 3D or 2D locations can be read.
              However, we strongly recommend using 3D positions.
              If 2D positions are used the behaviour of MNE functions
              can not be guaranteed.

    Parameters
    ----------
    fname : path-like
        Path to the SNIRF data file.
    optode_frame : str
        Coordinate frame used for the optode positions. The default is unknown,
        in which case the positions are not modified. If a known coordinate
        frame is provided (head, meg, mri), then the positions are transformed
        in to the Neuromag head coordinate frame (head).

    preload : bool or str (default False)
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    raw : instance of RawSNIRF
        A Raw object containing fNIRS data.
        See `mne.io.Raw` for documentation of attributes and methods.

    See Also
    --------
    mne.io.Raw : Documentation of attributes and methods of RawSNIRF.
    """
    ...

class RawSNIRF(BaseRaw):
    """Raw object from a continuous wave SNIRF file.

    Parameters
    ----------
    fname : path-like
        Path to the SNIRF data file.
    optode_frame : str
        Coordinate frame used for the optode positions. The default is unknown,
        in which case the positions are not modified. If a known coordinate
        frame is provided (head, meg, mri), then the positions are transformed
        in to the Neuromag head coordinate frame (head).

    preload : bool or str (default False)
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    mne.io.Raw : Documentation of attributes and methods.
    """

    def __init__(
        self, fname, optode_frame: str = "unknown", preload: bool = False, verbose=None
    ) -> None: ...
