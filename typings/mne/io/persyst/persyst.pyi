from ..._fiff.constants import FIFF as FIFF
from ..._fiff.meas_info import create_info as create_info
from ...annotations import Annotations as Annotations
from ...utils import fill_doc as fill_doc, logger as logger, warn as warn
from ..base import BaseRaw as BaseRaw

def read_raw_persyst(fname, preload: bool = False, verbose=None):
    """Reader for a Persyst (.lay/.dat) recording.

    Parameters
    ----------
    fname : path-like
        Path to the Persyst header ``.lay`` file.

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
    raw : instance of RawPersyst
        A Raw object containing Persyst data.
        See :class:`mne.io.Raw` for documentation of attributes and methods.

    See Also
    --------
    mne.io.Raw : Documentation of attributes and methods of RawPersyst.

    Notes
    -----
    It is assumed that the ``.lay`` and ``.dat`` file
    are in the same directory. To get the correct file path to the
    ``.dat`` file, ``read_raw_persyst`` will get the corresponding dat
    filename from the lay file, and look for that file inside the same
    directory as the lay file.
    """

class RawPersyst(BaseRaw):
    """Raw object from a Persyst file.

    Parameters
    ----------
    fname : path-like
        Path to the Persyst header (.lay) file.

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
