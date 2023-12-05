from ...utils import fill_doc as fill_doc, logger as logger
from ..base import BaseRaw as BaseRaw
from .constants import CTF as CTF

def read_raw_ctf(
    directory,
    system_clock: str = "truncate",
    preload: bool = False,
    clean_names: bool = False,
    verbose=None,
):
    """Raw object from CTF directory.

    Parameters
    ----------
    directory : path-like
        Path to the CTF data (ending in ``'.ds'``).
    system_clock : str
        How to treat the system clock. Use "truncate" (default) to truncate
        the data file when the system clock drops to zero, and use "ignore"
        to ignore the system clock (e.g., if head positions are measured
        multiple times during a recording).

    preload : bool or str (default False)
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).
    clean_names : bool, optional
        If True main channel names and compensation channel names will
        be cleaned from CTF suffixes. The default is False.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    raw : instance of RawCTF
        The raw data.
        See `mne.io.Raw` for documentation of attributes and methods.

    See Also
    --------
    mne.io.Raw : Documentation of attributes and methods of RawCTF.

    Notes
    -----
    ✨ Added in version 0.11

    To read in the Polhemus digitization data (for example, from
    a .pos file), include the file in the CTF directory. The
    points will then automatically be read into the `mne.io.Raw`
    instance via `mne.io.read_raw_ctf`.
    """
    ...

class RawCTF(BaseRaw):
    """Raw object from CTF directory.

    Parameters
    ----------
    directory : path-like
        Path to the CTF data (ending in ``'.ds'``).
    system_clock : str
        How to treat the system clock. Use ``"truncate"`` (default) to truncate
        the data file when the system clock drops to zero, and use ``"ignore"``
        to ignore the system clock (e.g., if head positions are measured
        multiple times during a recording).

    preload : bool or str (default False)
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).
    clean_names : bool, optional
        If True main channel names and compensation channel names will
        be cleaned from CTF suffixes. The default is False.

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
        self,
        directory,
        system_clock: str = "truncate",
        preload: bool = False,
        verbose=None,
        clean_names: bool = False,
    ) -> None: ...
