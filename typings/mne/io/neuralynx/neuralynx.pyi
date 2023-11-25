from ..._fiff.meas_info import create_info as create_info
from ...utils import fill_doc as fill_doc, logger as logger
from ..base import BaseRaw as BaseRaw

def read_raw_neuralynx(
    fname, *, preload: bool = False, exclude_fname_patterns=None, verbose=None
):
    """Reader for Neuralynx files.

    Parameters
    ----------
    fname : path-like
        Path to a folder with Neuralynx .ncs files.

    preload : bool or str (default False)
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).
    exclude_fname_patterns : list of str
        List of glob-like string patterns to exclude from channel list.
        Useful when not all channels have the same number of samples
        so you can read separate instances.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    raw : instance of RawNeuralynx
        A Raw object containing Neuralynx data.
        See :class:`mne.io.Raw` for documentation of attributes and methods.

    See Also
    --------
    mne.io.Raw : Documentation of attributes and methods of RawNeuralynx.
    """

class RawNeuralynx(BaseRaw):
    """RawNeuralynx class."""

    def __init__(
        self,
        fname,
        preload: bool = False,
        verbose=None,
        exclude_fname_patterns: list = None,
    ) -> None: ...
