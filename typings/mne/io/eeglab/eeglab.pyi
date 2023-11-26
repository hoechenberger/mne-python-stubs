from ..._fiff.constants import FIFF as FIFF
from ..._fiff.meas_info import create_info as create_info
from ...annotations import (
    Annotations as Annotations,
    read_annotations as read_annotations,
)
from ...channels import make_dig_montage as make_dig_montage
from ...defaults import DEFAULTS as DEFAULTS
from ...epochs import BaseEpochs as BaseEpochs
from ...event import read_events as read_events
from ...utils import (
    Bunch as Bunch,
    fill_doc as fill_doc,
    logger as logger,
    warn as warn,
)
from ..base import BaseRaw as BaseRaw

CAL: float

def read_raw_eeglab(
    input_fname,
    eog=(),
    preload: bool = False,
    uint16_codec=None,
    montage_units: str = "auto",
    verbose=None,
):
    """## 🧠 Read an EEGLAB .set file.

    -----
    ### 🛠️ Parameters

    #### `input_fname : path-like`
        Path to the ``.set`` file. If the data is stored in a separate ``.fdt``
        file, it is expected to be in the same folder as the ``.set`` file.
    #### `eog : list | tuple | ``'auto'```
        Names or indices of channels that should be designated EOG channels.
        If 'auto', the channel names containing ``EOG`` or ``EYE`` are used.
        Defaults to empty tuple.

    #### `preload : bool or str (default False)`
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).
        Note that ``preload=False`` will be effective only if the data is
        stored in a separate binary file.

    uint16_codec : str | None
        If your set file contains non-ascii characters, sometimes reading
        it may fail and give rise to error message stating that "buffer is
        too small". ``uint16_codec`` allows to specify what codec (for example:
        'latin1' or 'utf-8') should be used when reading character arrays and
        can therefore help you solve this problem.

    #### `montage_units : str`
        Units that channel positions are represented in. Defaults to "mm"
        (millimeters), but can be any prefix + "m" combination (including just
        "m" for meters).

        ✨ Added in vesion 1.3

        🎭 Changed in version 1.6
           Support for ``'auto'`` was added and is the new default.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `raw : instance of RawEEGLAB`
        A Raw object containing EEGLAB .set data.
        See `mne.io.Raw` for documentation of attributes and methods.

    -----
    ### 👉 See Also

    mne.io.Raw : Documentation of attributes and methods of RawEEGLAB.

    -----
    ### 📖 Notes

    ✨ Added in vesion 0.11.0
    """
    ...

def read_epochs_eeglab(
    input_fname,
    events=None,
    event_id=None,
    eog=(),
    *,
    uint16_codec=None,
    montage_units: str = "auto",
    verbose=None,
):
    """## 🧠 Reader function for EEGLAB epochs files.

    -----
    ### 🛠️ Parameters

    #### `input_fname : path-like`
        Path to the ``.set`` file. If the data is stored in a separate ``.fdt``
        file, it is expected to be in the same folder as the ``.set`` file.
    #### `events : path-like | array, shape (n_events, 3) | None`
        Path to events file. If array, it is the events typically returned
        by the read_events function. If some events don't match the events
        of interest as specified by event_id, they will be marked as 'IGNORED'
        in the drop log. If None, it is constructed from the EEGLAB (.set) file
        with each unique event encoded with a different integer.
    #### `event_id : int | list of int | dict | None`
        The id of the event to consider. If dict, the keys can later be used
        to access associated events.
        Example::

            {"auditory":1, "visual":3}

        If int, a dict will be created with
        the id as string. If a list, all events with the IDs specified
        in the list are used. If None, the event_id is constructed from the
        EEGLAB (.set) file with each descriptions copied from ``eventtype``.
    #### `eog : list | tuple | 'auto'`
        Names or indices of channels that should be designated EOG channels.
        If 'auto', the channel names containing ``EOG`` or ``EYE`` are used.
        Defaults to empty tuple.

    uint16_codec : str | None
        If your set file contains non-ascii characters, sometimes reading
        it may fail and give rise to error message stating that "buffer is
        too small". ``uint16_codec`` allows to specify what codec (for example:
        'latin1' or 'utf-8') should be used when reading character arrays and
        can therefore help you solve this problem.

    #### `montage_units : str`
        Units that channel positions are represented in. Defaults to "mm"
        (millimeters), but can be any prefix + "m" combination (including just
        "m" for meters).

        ✨ Added in vesion 1.3

        🎭 Changed in version 1.6
           Support for ``'auto'`` was added and is the new default.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `epochs : instance of Epochs`
        The epochs.

    -----
    ### 👉 See Also

    mne.Epochs : Documentation of attributes and methods.

    -----
    ### 📖 Notes

    ✨ Added in vesion 0.11.0
    """
    ...

class RawEEGLAB(BaseRaw):
    """## 🧠 Raw object from EEGLAB .set file.

    -----
    ### 🛠️ Parameters

    #### `input_fname : path-like`
        Path to the ``.set`` file. If the data is stored in a separate ``.fdt``
        file, it is expected to be in the same folder as the ``.set`` file.
    #### `eog : list | tuple | 'auto'`
        Names or indices of channels that should be designated EOG channels.
        If 'auto', the channel names containing ``EOG`` or ``EYE`` are used.
        Defaults to empty tuple.

    #### `preload : bool or str (default False)`
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).
        Note that preload=False will be effective only if the data is stored
        in a separate binary file.

    uint16_codec : str | None
        If your set file contains non-ascii characters, sometimes reading
        it may fail and give rise to error message stating that "buffer is
        too small". ``uint16_codec`` allows to specify what codec (for example:
        'latin1' or 'utf-8') should be used when reading character arrays and
        can therefore help you solve this problem.

    #### `montage_units : str`
        Units that channel positions are represented in. Defaults to "mm"
        (millimeters), but can be any prefix + "m" combination (including just
        "m" for meters).

        ✨ Added in vesion 1.3

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### 👉 See Also

    mne.io.Raw : Documentation of attributes and methods.

    -----
    ### 📖 Notes

    ✨ Added in vesion 0.11.0
    """

    def __init__(
        self,
        input_fname,
        eog=(),
        preload: bool = False,
        *,
        uint16_codec=None,
        montage_units: str = "auto",
        verbose=None,
    ) -> None: ...

class EpochsEEGLAB(BaseEpochs):
    """## 🧠 Epochs from EEGLAB .set file.

    -----
    ### 🛠️ Parameters

    #### `input_fname : path-like`
        Path to the ``.set`` file. If the data is stored in a separate ``.fdt``
        file, it is expected to be in the same folder as the ``.set`` file.
    #### `events : path-like | array, shape (n_events, 3) | None`
        Path to events file. If array, it is the events typically returned
        by the read_events function. If some events don't match the events
        of interest as specified by event_id, they will be marked as 'IGNORED'
        in the drop log. If None, it is constructed from the EEGLAB (.set) file
        with each unique event encoded with a different integer.
    #### `event_id : int | list of int | dict | None`
        The id of the event to consider. If dict,
        the keys can later be used to access associated events. Example:
        dict(auditory=1, visual=3). If int, a dict will be created with
        the id as string. If a list, all events with the IDs specified
        in the list are used. If None, the event_id is constructed from the
        EEGLAB (.set) file with each descriptions copied from ``eventtype``.
    #### `tmin : float`
        Start time before event.
    #### `baseline : None or tuple of length 2 (default (None, 0))`
        The time interval to apply baseline correction.
        If None do not apply it. If baseline is (a, b)
        the interval is between "a (s)" and "b (s)".
        If a is None the beginning of the data is used
        and if b is None then b is set to the end of the interval.
        If baseline is equal to (None, None) all the time
        interval is used.
        The baseline (a, b) includes both endpoints, i.e. all
        timepoints t such that a <= t <= b.
    #### `reject : dict | None`
        Rejection parameters based on peak-to-peak amplitude.
        Valid keys are 'grad' | 'mag' | 'eeg' | 'eog' | 'ecg'.
        If reject is None then no rejection is done. Example::

            reject = dict(grad=4000e-13, # T / m (gradiometers)
                          mag=4e-12, # T (magnetometers)
                          eeg=40e-6, # V (EEG channels)
                          eog=250e-6 # V (EOG channels)
                          )
    #### `flat : dict | None`
        Rejection parameters based on flatness of signal.
        Valid keys are 'grad' | 'mag' | 'eeg' | 'eog' | 'ecg', and values
        are floats that set the minimum acceptable peak-to-peak amplitude.
        If flat is None then no rejection is done.
    #### `reject_tmin : scalar | None`
        Start of the time window used to reject epochs (with the default None,
        the window will start with tmin).
    #### `reject_tmax : scalar | None`
        End of the time window used to reject epochs (with the default None,
        the window will end with tmax).
    #### `eog : list | tuple | 'auto'`
        Names or indices of channels that should be designated EOG channels.
        If 'auto', the channel names containing ``EOG`` or ``EYE`` are used.
        Defaults to empty tuple.
    %(uint16_codec)s
    %(montage_units)s
    %(verbose)s

    -----
    ### 👉 See Also

    mne.Epochs : Documentation of attributes and methods.

    -----
    ### 📖 Notes

    ✨ Added in vesion 0.11.0
    """

    def __init__(
        self,
        input_fname,
        events=None,
        event_id=None,
        tmin: int = 0,
        baseline=None,
        reject=None,
        flat=None,
        reject_tmin=None,
        reject_tmax=None,
        eog=(),
        uint16_codec=None,
        montage_units: str = "auto",
        verbose=None,
    ) -> None: ...
