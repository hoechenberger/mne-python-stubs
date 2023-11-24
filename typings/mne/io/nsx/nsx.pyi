from ..._fiff.constants import FIFF as FIFF
from ...annotations import Annotations as Annotations
from ...utils import fill_doc as fill_doc, logger as logger, warn as warn
from ..base import BaseRaw as BaseRaw
from _typeshed import Incomplete
CH_TYPE_MAPPING: Incomplete
DATA_BYTE_SIZE: int
ORIG_FORMAT: str
nsx_header_dict: Incomplete

def read_raw_nsx(input_fname, stim_channel: bool=..., eog: Incomplete | None=..., misc: Incomplete | None=..., preload: bool=..., *, verbose: Incomplete | None=...):
    """Reader function for NSx (Blackrock Microsystems) files.

    Parameters
    ----------
    input_fname : str
        Path to the NSx file.
    stim_channel : ``'auto'`` | str | list of str | int | list of int
        Defaults to ``'auto'``, which means that channels named ``'status'`` or
        ``'trigger'`` (case insensitive) are set to STIM. If str (or list of
        str), all channels matching the name(s) are set to STIM. If int (or
        list of ints), channels corresponding to the indices are set to STIM.
    eog : list or tuple
        Names of channels or list of indices that should be designated EOG
        channels. Values should correspond to the electrodes in the file.
        Default is None.
    misc : list or tuple
        Names of channels or list of indices that should be designated MISC
        channels. Values should correspond to the electrodes in the file.
        Default is None.
    
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
    raw : instance of RawEDF
        The raw instance.
        See :class:`mne.io.Raw` for documentation of attributes and methods.

    Notes
    -----
    NSx files with id (= NEURALSG), i.e., version 2.1 is currently not
    supported.

    If channels named 'status' or 'trigger' are present, they are considered as
    STIM channels by default. Use func:`mne.find_events` to parse events
    encoded in such analog stim channels.
    """

class RawNSX(BaseRaw):
    """Raw object from NSx file from Blackrock Microsystems.

    Parameters
    ----------
    input_fname : str
        Path to the NSx file.
    stim_channel : ``'auto'`` | str | list of str | int | list of int
        Defaults to ``'auto'``, which means that channels named ``'status'`` or
        ``'trigger'`` (case insensitive) are set to STIM. If str (or list of
        str), all channels matching the name(s) are set to STIM. If int (or
        list of ints), channels corresponding to the indices are set to STIM.
    eog : list or tuple
        Names of channels or list of indices that should be designated EOG
        channels. Values should correspond to the electrodes in the file.
        Default is None.
    misc : list or tuple
        Names of channels or list of indices that should be designated MISC
        channels. Values should correspond to the electrodes in the file.
        Default is None.
    
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

    Notes
    -----
    NSx files with id (= NEURALSG), i.e., version 2.1 is currently not
    supported.

    If channels named 'status' or 'trigger' are present, they are considered as
    STIM channels by default. Use func:`mne.find_events` to parse events
    encoded in such analog stim channels.
    """

    def __init__(self, input_fname, stim_channel: str=..., eog: Incomplete | None=..., misc: Incomplete | None=..., preload: bool=..., verbose: Incomplete | None=...) -> None:
        ...