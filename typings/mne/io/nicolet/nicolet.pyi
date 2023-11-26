from ..._fiff.constants import FIFF as FIFF
from ...utils import fill_doc as fill_doc, logger as logger
from ..base import BaseRaw as BaseRaw

def read_raw_nicolet(
    input_fname,
    ch_type,
    eog=(),
    ecg=(),
    emg=(),
    misc=(),
    preload: bool = False,
    verbose=None,
):
    """## 🧠 Read Nicolet data as raw object.

    ..note:: This reader takes data files with the extension ``.data`` as an
             input. The header file with the same file name stem and an
             extension ``.head`` is expected to be found in the same
             directory.

    -----
    ### 🛠️ Parameters

    #### `input_fname : path-like`
        Path to the data file (ending with ``.data`` not ``.head``).
    #### `ch_type : str`
        Channel type to designate to the data channels. Supported data types
        include ``'eeg'``, ``'dbs'``.
    #### `eog : list | tuple | ``'auto'```
        Names of channels or list of indices that should be designated
        EOG channels. If ``'auto'``, the channel names beginning with
        ``EOG`` are used. Defaults to empty tuple.
    #### `ecg : list or tuple | ``'auto'```
        Names of channels or list of indices that should be designated
        ECG channels. If ``'auto'``, the channel names beginning with
        ``ECG`` are used. Defaults to empty tuple.
    #### `emg : list or tuple | ``'auto'```
        Names of channels or list of indices that should be designated
        EMG channels. If ``'auto'``, the channel names beginning with
        ``EMG`` are used. Defaults to empty tuple.
    #### `misc : list or tuple`
        Names of channels or list of indices that should be designated
        MISC channels. Defaults to empty tuple.

    #### `preload : bool or str (default False)`
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `raw : instance of Raw`
        A Raw object containing the data.

    -----
    ### 👉 See Also

    mne.io.Raw : Documentation of attributes and methods.
    """
    ...

class RawNicolet(BaseRaw):
    """## 🧠 Raw object from Nicolet file.

    -----
    ### 🛠️ Parameters

    #### `input_fname : path-like`
        Path to the Nicolet file.
    #### `ch_type : str`
        Channel type to designate to the data channels. Supported data types
        include ``'eeg'``, ``'seeg'``.
    #### `eog : list | tuple | ``'auto'```
        Names of channels or list of indices that should be designated
        EOG channels. If ``'auto'``, the channel names beginning with
        ``EOG`` are used. Defaults to empty tuple.
    #### `ecg : list or tuple | ``'auto'```
        Names of channels or list of indices that should be designated
        ECG channels. If ``'auto'``, the channel names beginning with
        ``ECG`` are used. Defaults to empty tuple.
    #### `emg : list or tuple | ``'auto'```
        Names of channels or list of indices that should be designated
        EMG channels. If ``'auto'``, the channel names beginning with
        ``EMG`` are used. Defaults to empty tuple.
    #### `misc : list or tuple`
        Names of channels or list of indices that should be designated
        MISC channels. Defaults to empty tuple.
    %(preload)s
    %(verbose)s

    -----
    ### 👉 See Also

    mne.io.Raw : Documentation of attributes and methods.
    """

    def __init__(
        self,
        input_fname,
        ch_type,
        eog=(),
        ecg=(),
        emg=(),
        misc=(),
        preload: bool = False,
        verbose=None,
    ) -> None: ...
