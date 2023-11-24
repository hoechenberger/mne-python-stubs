from ..._fiff.meas_info import create_info as create_info
from ...utils import verbose as verbose, warn as warn
from ..base import BaseRaw as BaseRaw
from _typeshed import Incomplete

class RawNedf(BaseRaw):
    """Raw object from NeuroElectrics nedf file."""

    def __init__(self, filename, preload: bool=..., verbose: Incomplete | None=...) -> None:
        ...

def read_raw_nedf(filename, preload: bool=..., verbose: Incomplete | None=...):
    """Read NeuroElectrics .nedf files.

    NEDF file versions starting from 1.3 are supported.

    Parameters
    ----------
    filename : path-like
        Path to the ``.nedf`` file.
    
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
    raw : instance of RawNedf
        A Raw object containing NEDF data.
        See :class:`mne.io.Raw` for documentation of attributes and methods.

    See Also
    --------
    mne.io.Raw : Documentation of attributes and methods of RawNedf.
    """