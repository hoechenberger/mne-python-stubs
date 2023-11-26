from ..._fiff.meas_info import create_info as create_info
from ...utils import fill_doc as fill_doc, logger as logger, warn as warn
from ..base import BaseRaw as BaseRaw

def read_raw_eximia(fname, preload: bool = False, verbose=None):
    """### Reader for an eXimia EEG file.

    -----
    ### 🛠️ Parameters

    fname : path-like
        Path to the eXimia ``.nxe`` data file.

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

    -----
    ### ⏎ Returns

    raw : instance of RawEximia
        A Raw object containing eXimia data.
        See `mne.io.Raw` for documentation of attributes and methods.

    -----
    ### 👉 See Also

    mne.io.Raw : Documentation of attributes and methods of RawEximia.
    """
    ...

class RawEximia(BaseRaw):
    """### Raw object from an Eximia EEG file.

    -----
    ### 🛠️ Parameters

    fname : path-like
        Path to the eXimia data file (.nxe).

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

    -----
    ### 👉 See Also

    mne.io.Raw : Documentation of attributes and methods.
    """

    def __init__(self, fname, preload: bool = False, verbose=None) -> None: ...
