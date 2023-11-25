from ..._fiff.meas_info import create_info as create_info
from ...annotations import Annotations as Annotations
from ...utils import fill_doc as fill_doc, logger as logger
from ..base import BaseRaw as BaseRaw

def read_raw_boxy(fname, preload: bool = False, verbose=None):
    """Reader for an optical imaging recording.

    This function has been tested using the ISS Imagent I and II systems
    and versions 0.40/0.84 of the BOXY recording software.

    Parameters
    ----------
    fname : path-like
        Path to the BOXY data file.

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
    raw : instance of RawBOXY
        A Raw object containing BOXY data.
        See :class:`mne.io.Raw` for documentation of attributes and methods.

    See Also
    --------
    mne.io.Raw : Documentation of attributes and methods of RawBOXY.
    """

class RawBOXY(BaseRaw):
    """Raw object from a BOXY optical imaging file.

    Parameters
    ----------
    fname : path-like
        Path to the BOXY data file.

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

    See Also
    --------
    mne.io.Raw : Documentation of attributes and methods.
    """

    def __init__(self, fname, preload: bool = False, verbose=None) -> None: ...
