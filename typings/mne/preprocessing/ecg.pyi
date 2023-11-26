from .._fiff.meas_info import create_info as create_info
from .._fiff.pick import pick_channels as pick_channels, pick_types as pick_types
from ..epochs import BaseEpochs as BaseEpochs, Epochs as Epochs
from ..evoked import Evoked as Evoked
from ..filter import filter_data as filter_data
from ..io import BaseRaw as BaseRaw, RawArray as RawArray
from ..utils import (
    int_like as int_like,
    logger as logger,
    sum_squared as sum_squared,
    warn as warn,
)

def qrs_detector(
    sfreq,
    ecg,
    thresh_value: float = 0.6,
    levels: float = 2.5,
    n_thresh: int = 3,
    l_freq: int = 5,
    h_freq: int = 35,
    tstart: int = 0,
    filter_length: str = "10s",
    verbose=None,
):
    """Detect QRS component in ECG channels.

    QRS is the main wave on the heart beat.

    Parameters
    ----------
    sfreq : float
        Sampling rate
    ecg : array
        ECG signal
    thresh_value : float | str
        qrs detection threshold. Can also be "auto" for automatic
        selection of threshold.
    levels : float
        number of std from mean to include for detection
    n_thresh : int
        max number of crossings
    l_freq : float
        Low pass frequency
    h_freq : float
        High pass frequency

    tstart : float
        Start ECG detection after ``tstart`` seconds. Useful when the beginning
        of the run is noisy.

    filter_length : str | int | None
        Number of taps to use for filtering.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    events : array
        Indices of ECG peaks.
    """
    ...

def find_ecg_events(
    raw,
    event_id: int = 999,
    ch_name=None,
    tstart: float = 0.0,
    l_freq: int = 5,
    h_freq: int = 35,
    qrs_threshold: str = "auto",
    filter_length: str = "10s",
    return_ecg: bool = False,
    reject_by_annotation: bool = True,
    verbose=None,
):
    """Find ECG events by localizing the R wave peaks.

    Parameters
    ----------
    raw : instance of Raw
        The raw data.

    event_id : int
        The index to assign to found ECG events.

    ch_name : None | str
        The name of the channel to use for ECG peak detection.
        If ``None`` (default), ECG channel is used if present. If ``None`` and
        **no** ECG channel is present, a synthetic ECG channel is created from
        the cross-channel average. This synthetic channel can only be created from
        MEG channels.

    tstart : float
        Start ECG detection after ``tstart`` seconds. Useful when the beginning
        of the run is noisy.

    l_freq : float
        Low pass frequency to apply to the ECG channel while finding events.
    h_freq : float
        High pass frequency to apply to the ECG channel while finding events.
    qrs_threshold : float | str
        Between 0 and 1. qrs detection threshold. Can also be "auto" to
        automatically choose the threshold that generates a reasonable
        number of heartbeats (40-160 beats / min).

    filter_length : str | int | None
        Number of taps to use for filtering.
    return_ecg : bool
        Return the ECG data. This is especially useful if no ECG channel
        is present in the input data, so one will be synthesized. Defaults to
        ``False``.

    reject_by_annotation : bool
        Whether to omit bad segments from the data before fitting. If ``True``
        (default), annotated segments whose description begins with ``'bad'`` are
        omitted. If ``False``, no rejection based on annotations is performed.

        .. versionadded:: 0.18

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    ecg_events : array
        The events corresponding to the peaks of the R waves.
    ch_ecg : string
        Name of channel used.
    average_pulse : float
        The estimated average pulse. If no ECG events could be found, this will
        be zero.
    ecg : array | None
        The ECG data of the synthesized ECG channel, if any. This will only
        be returned if ``return_ecg=True`` was passed.

    See Also
    --------
    create_ecg_epochs
    compute_proj_ecg
    """
    ...

def create_ecg_epochs(
    raw,
    ch_name=None,
    event_id: int = 999,
    picks=None,
    tmin: float = -0.5,
    tmax: float = 0.5,
    l_freq: int = 8,
    h_freq: int = 16,
    reject=None,
    flat=None,
    baseline=None,
    preload: bool = True,
    keep_ecg: bool = False,
    reject_by_annotation: bool = True,
    decim: int = 1,
    verbose=None,
):
    """Conveniently generate epochs around ECG artifact events.

    This function will:

    #. Filter the ECG data channel.

    #. Find ECG R wave peaks using :func:`mne.preprocessing.find_ecg_events`.

    #. Create mne.Epochs` around the R wave peaks, capturing the heartbeats.

    .. note:: Filtering is only applied to the ECG channel while finding
                events. The resulting ``ecg_epochs`` will have no filtering
                applied (i.e., have the same filter properties as the input
                ``raw`` instance).

    Parameters
    ----------
    raw : instance of Raw
        The raw data.

    ch_name : None | str
        The name of the channel to use for ECG peak detection.
        If ``None`` (default), ECG channel is used if present. If ``None`` and
        **no** ECG channel is present, a synthetic ECG channel is created from
        the cross-channel average. This synthetic channel can only be created from
        MEG channels.

    event_id : int
        The index to assign to found ECG events.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick all channels. Note that channels in
        ``info['bads']`` *will be included* if their names or indices are
        explicitly provided.
    tmin : float
        Start time before event.
    tmax : float
        End time after event.

    l_freq : float
        Low pass frequency to apply to the ECG channel while finding events.
    h_freq : float
        High pass frequency to apply to the ECG channel while finding events.

    reject : dict | None
        Reject epochs based on **maximum** peak-to-peak signal amplitude (PTP),
        i.e. the absolute difference between the lowest and the highest signal
        value. In each individual epoch, the PTP is calculated for every channel.
        If the PTP of any one channel exceeds the rejection threshold, the
        respective epoch will be dropped.

        The dictionary keys correspond to the different channel types; valid
        **keys** can be any channel type present in the object.

        Example::

            reject = dict(grad=4000e-13,  # unit: T / m (gradiometers)
                          mag=4e-12,      # unit: T (magnetometers)
                          eeg=40e-6,      # unit: V (EEG channels)
                          eog=250e-6      # unit: V (EOG channels)
                          )

        .. note:: Since rejection is based on a signal **difference**
                  calculated for each channel separately, applying baseline
                  correction does not affect the rejection procedure, as the
                  difference will be preserved.

        .. note:: To constrain the time period used for estimation of signal
                  quality, pass the ``reject_tmin`` and ``reject_tmax`` parameters.

        If ``reject`` is ``None`` (default), no rejection is performed.

    flat : dict | None
        Reject epochs based on **minimum** peak-to-peak signal amplitude (PTP).
        Valid **keys** can be any channel type present in the object. The
        **values** are floats that set the minimum acceptable PTP. If the PTP
        is smaller than this threshold, the epoch will be dropped. If ``None``
        then no rejection is performed based on flatness of the signal.

        .. note:: To constrain the time period used for estimation of signal
                  quality, pass the ``reject_tmin`` and ``reject_tmax`` parameters.

    baseline : None | tuple of length 2
        The time interval to consider as "baseline" when applying baseline
        correction. If ``None``, do not apply baseline correction.
        If a tuple ``(a, b)``, the interval is between ``a`` and ``b``
        (in seconds), including the endpoints.
        If ``a`` is ``None``, the **beginning** of the data is used; and if ``b``
        is ``None``, it is set to the **end** of the interval.
        If ``(None, None)``, the entire time interval is used.

        .. note:: The baseline ``(a, b)`` includes both endpoints, i.e. all
                    timepoints ``t`` such that ``a <= t <= b``.

        Correction is applied **to each epoch and channel individually** in the
        following way:

        1. Calculate the mean signal of the baseline period.
        2. Subtract this mean from the **entire** epoch.

    preload : bool
        Preload epochs or not (default True). Must be True if
        keep_ecg is True.
    keep_ecg : bool
        When ECG is synthetically created (after picking), should it be added
        to the epochs? Must be False when synthetic channel is not used.
        Defaults to False.

    reject_by_annotation : bool
        Whether to reject based on annotations. If ``True`` (default), epochs
        overlapping with segments whose description begins with ``'bad'`` are
        rejected. If ``False``, no rejection based on annotations is performed.

        .. versionadded:: 0.14.0

    decim : int
        Factor by which to subsample the data.

        .. warning:: Low-pass filtering is not performed, this simply selects
                     every Nth sample (where N is the value passed to
                     ``decim``), i.e., it compresses the signal (see Notes).
                     If the data are not properly filtered, aliasing artifacts
                     may occur.

        .. versionadded:: 0.21.0

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    ecg_epochs : instance of Epochs
        Data epoched around ECG R wave peaks.

    See Also
    --------
    find_ecg_events
    compute_proj_ecg

    Notes
    -----
    If you already have a list of R-peak times, or want to compute R-peaks
    outside MNE-Python using a different algorithm, the recommended approach is
    to call the :class:mne.Epochs` constructor directly, with your R-peaks
    formatted as an :term:`events` array (here we also demonstrate the relevant
    default values)::

        mne.Epochs(raw, r_peak_events_array, tmin=-0.5, tmax=0.5,
                   baseline=None, preload=True, proj=False)  # doctest: +SKIP
    """
    ...
