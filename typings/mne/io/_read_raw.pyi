from ..utils import fill_doc as fill_doc
from .base import BaseRaw as BaseRaw

def split_name_ext(fname):
    """Return name and supported file extension."""
    ...

def read_raw(fname, *, preload: bool = False, verbose=None, **kwargs) -> BaseRaw:
    """Read raw file.

    This function is a convenient wrapper for readers defined in `mne.io`. The
    correct reader is automatically selected based on the detected file format.
    All function arguments are passed to the respective reader.

    The following readers are currently supported:

    `read_raw_artemis123`, `read_raw_bdf`,
    `read_raw_boxy`, `read_raw_brainvision`,
    `read_raw_cnt`, `read_raw_ctf`, `read_raw_edf`,
    `read_raw_eeglab`, `read_raw_egi`,
    `read_raw_eximia`, `read_raw_fieldtrip`,
    `read_raw_fif`,  `read_raw_gdf`, `read_raw_kit`,
    `read_raw_fil`,
    `read_raw_nicolet`, `read_raw_nirx`,
    `read_raw_curry`, and `read_raw_nedf`.

    Parameters
    ----------
    fname : path-like
        Name of the file to read.

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
    **kwargs
        Additional keyword arguments to pass to the underlying reader. For
        details, see the arguments of the reader for the respective file
        format.

    Returns
    -------
    raw : mne.io.Raw
        Raw object.
    """
    ...
