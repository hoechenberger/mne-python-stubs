from .._fiff.pick import pick_channels as pick_channels, pick_types as pick_types
from ..epochs import Epochs as Epochs
from ..filter import filter_data as filter_data
from ..utils import logger as logger
from ._peak_finder import peak_finder as peak_finder

def find_eog_events(
    raw,
    event_id: int = 998,
    l_freq: int = 1,
    h_freq: int = 10,
    filter_length: str = "10s",
    ch_name=None,
    tstart: int = 0,
    reject_by_annotation: bool = False,
    thresh=None,
    verbose=None,
):
    """## Locate EOG artifacts.

    ### 💡 Note To control true-positive and true-negative detection rates, you
              may adjust the ``thresh`` parameter.

    -----
    ### 🛠️ Parameters

    #### `raw : instance of Raw`
        The raw data.
    #### `event_id : int`
        The index to assign to found events.
    #### `l_freq : float`
        Low cut-off frequency to apply to the EOG channel in Hz.
    #### `h_freq : float`
        High cut-off frequency to apply to the EOG channel in Hz.
    #### `filter_length : str | int | None`
        Number of taps to use for filtering.

    #### `ch_name : str | list of str | None`
        The name of the channel(s) to use for EOG peak detection. If a string,
        can be an arbitrary channel. This doesn't have to be a channel of
        ``eog`` type; it could, for example, also be an ordinary EEG channel
        that was placed close to the eyes, like ``Fp1`` or ``Fp2``.

        Multiple channel names can be passed as a list of strings.

        If ``None`` (default), use the channel(s) in ``raw`` with type ``eog``.
    #### `tstart : float`
        Start detection after tstart seconds.
    #### `reject_by_annotation : bool`
        Whether to omit data that is annotated as bad.
    #### `thresh : float | None`
        Threshold to trigger the detection of an EOG event. This controls the
        thresholding of the underlying peak-finding algorithm. Larger values
        mean that fewer peaks (i.e., fewer EOG events) will be detected.
        If ``None``, use the default of ``(max(eog) - min(eog)) / 4``,
        with ``eog`` being the filtered EOG signal.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `eog_events : array`
        Events.

    -----
    ### 👉 See Also

    create_eog_epochs
    compute_proj_eog
    """
    ...

def create_eog_epochs(
    raw,
    ch_name=None,
    event_id: int = 998,
    picks=None,
    tmin: float = -0.5,
    tmax: float = 0.5,
    l_freq: int = 1,
    h_freq: int = 10,
    reject=None,
    flat=None,
    baseline=None,
    preload: bool = True,
    reject_by_annotation: bool = True,
    thresh=None,
    decim: int = 1,
    verbose=None,
):
    """## Conveniently generate epochs around EOG artifact events.

    This function will:

    #. Filter the EOG data channel.

    #. Find the peaks of eyeblinks in the EOG data using
       `mne.preprocessing.find_eog_events`.

    #. Create `mne.Epochs` around the eyeblinks.

    -----
    ### 🛠️ Parameters

    #### `raw : instance of Raw`
        The raw data.

    #### `ch_name : str | list of str | None`
        The name of the channel(s) to use for EOG peak detection. If a string,
        can be an arbitrary channel. This doesn't have to be a channel of
        ``eog`` type; it could, for example, also be an ordinary EEG channel
        that was placed close to the eyes, like ``Fp1`` or ``Fp2``.

        Multiple channel names can be passed as a list of strings.

        If ``None`` (default), use the channel(s) in ``raw`` with type ``eog``.
    #### `event_id : int`
        The index to assign to found events.
    #### `picks : str | array-like | slice | None`
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick all channels. Note that channels in
        ``info['bads']`` *will be included* if their names or indices are
        explicitly provided.
    #### `tmin : float`
        Start time before event.
    #### `tmax : float`
        End time after event.
    #### `l_freq : float`
        Low pass frequency to apply to the EOG channel while finding events.
    #### `h_freq : float`
        High pass frequency to apply to the EOG channel while finding events.
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
    #### `baseline : tuple or list of length 2, or None`
        The time interval to apply rescaling / baseline correction.
        If None do not apply it. If baseline is (a, b)
        the interval is between "a (s)" and "b (s)".
        If a is None the beginning of the data is used
        and if b is None then b is set to the end of the interval.
        If baseline is equal to (None, None) all the time
        interval is used. If None, no correction is applied.
    #### `preload : bool`
        Preload epochs or not.

    #### `reject_by_annotation : bool`
        Whether to reject based on annotations. If ``True`` (default), epochs
        overlapping with segments whose description begins with ``'bad'`` are
        rejected. If ``False``, no rejection based on annotations is performed.

        ✨ Added in version 0.14.0
    #### `thresh : float`
        Threshold to trigger EOG event.

    #### `decim : int`
        Factor by which to subsample the data.

        ### ⛔️ Warning Low-pass filtering is not performed, this simply selects
                     every Nth sample (where N is the value passed to
                     ``decim``), i.e., it compresses the signal (see Notes).
                     If the data are not properly filtered, aliasing artifacts
                     may occur.

        ✨ Added in version 0.21.0

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `eog_epochs : instance of Epochs`
        Data epoched around EOG events.

    -----
    ### 👉 See Also

    find_eog_events
    compute_proj_eog

    -----
    ### 📖 Notes

    Filtering is only applied to the EOG channel while finding events.
    The resulting ``eog_epochs`` will have no filtering applied (i.e., have
    the same filter properties as the input ``raw`` instance).
    """
    ...
