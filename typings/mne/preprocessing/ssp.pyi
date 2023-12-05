from .._fiff.pick import pick_types as pick_types
from .._fiff.reference import make_eeg_average_ref_proj as make_eeg_average_ref_proj
from ..epochs import Epochs as Epochs
from ..proj import (
    compute_proj_epochs as compute_proj_epochs,
    compute_proj_evoked as compute_proj_evoked,
)
from ..utils import logger as logger, warn as warn
from .ecg import find_ecg_events as find_ecg_events
from .eog import find_eog_events as find_eog_events

def compute_proj_ecg(
    raw,
    raw_event=None,
    tmin: float = -0.2,
    tmax: float = 0.4,
    n_grad: int = 2,
    n_mag: int = 2,
    n_eeg: int = 2,
    l_freq: float = 1.0,
    h_freq: float = 35.0,
    average: bool = True,
    filter_length: str = "10s",
    n_jobs=None,
    ch_name=None,
    reject={"grad": 2e-10, "mag": 3e-12, "eeg": 5e-05, "eog": 0.00025},
    flat=None,
    bads=[],
    avg_ref: bool = False,
    no_proj: bool = False,
    event_id: int = 999,
    ecg_l_freq: int = 5,
    ecg_h_freq: int = 35,
    tstart: float = 0.0,
    qrs_threshold: str = "auto",
    filter_method: str = "fir",
    iir_params=None,
    copy: bool = True,
    return_drop_log: bool = False,
    meg: str = "separate",
    verbose=None,
):
    """Compute SSP (signal-space projection) vectors for ECG artifacts.

    This function will:

    #. Filter the ECG data channel.

    #. Find ECG R wave peaks using `mne.preprocessing.find_ecg_events`.

    #. Filter the raw data.

    #. Create `mne.Epochs` around the R wave peaks, capturing the heartbeats.

    #. Optionally average the `mne.Epochs` to produce an `mne.Evoked` if
       ``average=True`` was passed (default).

    #. Calculate SSP projection vectors on that data to capture the artifacts.

    💡 Note Raw data will be loaded if it hasn't been preloaded already.

    Parameters
    ----------
    raw : mne.io.Raw
        Raw input file.
    raw_event : mne.io.Raw or None
        Raw file to use for event detection (if None, raw is used).
    tmin : float
        Time before event in seconds.
    tmax : float
        Time after event in seconds.
    n_grad : int
        Number of SSP vectors for gradiometers.
    n_mag : int
        Number of SSP vectors for magnetometers.
    n_eeg : int
        Number of SSP vectors for EEG.
    l_freq : float | None
        Filter low cut-off frequency for the data channels in Hz.
    h_freq : float | None
        Filter high cut-off frequency for the data channels in Hz.
    average : bool
        Compute SSP after averaging. Default is True.
    filter_length : str | int | None
        Number of taps to use for filtering.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.
    ch_name : str | None
        Channel to use for ECG detection (Required if no ECG found).
    reject : dict | None
        Epoch rejection configuration (see Epochs).
    flat : dict | None
        Epoch flat configuration (see Epochs).
    bads : list
        List with (additional) bad channels.
    avg_ref : bool
        Add EEG average reference proj.
    no_proj : bool
        Exclude the SSP projectors currently in the fiff file.
    event_id : int
        ID to use for events.
    ecg_l_freq : float
        Low pass frequency applied to the ECG channel for event detection.
    ecg_h_freq : float
        High pass frequency applied to the ECG channel for event detection.
    tstart : float
        Start artifact detection after tstart seconds.
    qrs_threshold : float | str
        Between 0 and 1. qrs detection threshold. Can also be "auto" to
        automatically choose the threshold that generates a reasonable
        number of heartbeats (40-160 beats / min).
    filter_method : str
        Method for filtering ('iir' or 'fir').
    iir_params : dict | None
        Dictionary of parameters to use for IIR filtering.
        See mne.filter.construct_iir_filter for details. If iir_params
        is None and method="iir", 4th order Butterworth will be used.
    copy : bool
        If False, filtering raw data is done in place. Defaults to True.
    return_drop_log : bool
        If True, return the drop log.

        ✨ Added in version 0.15
    meg : str
        Can be ``'separate'`` (default) or ``'combined'`` to compute projectors
        for magnetometers and gradiometers separately or jointly.
        If ``'combined'``, ``n_mag == n_grad`` is required and the number of
        projectors computed for MEG will be ``n_mag``.

        ✨ Added in version 0.18

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------

    projs : list of Projection
        List of computed projection vectors.
    ecg_events : ndarray
        Detected ECG events.
    drop_log : list
        The drop log, if requested.

    See Also
    --------
    find_ecg_events
    create_ecg_epochs

    Notes
    -----
    Filtering is applied to the ECG channel while finding events using
    ``ecg_l_freq`` and ``ecg_h_freq``, and then to the ``raw`` instance
    using ``l_freq`` and ``h_freq`` before creation of the epochs used to
    create the projectors.
    """
    ...

def compute_proj_eog(
    raw,
    raw_event=None,
    tmin: float = -0.2,
    tmax: float = 0.2,
    n_grad: int = 2,
    n_mag: int = 2,
    n_eeg: int = 2,
    l_freq: float = 1.0,
    h_freq: float = 35.0,
    average: bool = True,
    filter_length: str = "10s",
    n_jobs=None,
    reject=...,
    flat=None,
    bads=[],
    avg_ref: bool = False,
    no_proj: bool = False,
    event_id: int = 998,
    eog_l_freq: int = 1,
    eog_h_freq: int = 10,
    tstart: float = 0.0,
    filter_method: str = "fir",
    iir_params=None,
    ch_name=None,
    copy: bool = True,
    return_drop_log: bool = False,
    meg: str = "separate",
    verbose=None,
):
    """Compute SSP (signal-space projection) vectors for EOG artifacts.

    This function will:

    #. Filter the EOG data channel.

    #. Find the peaks of eyeblinks in the EOG data using
       `mne.preprocessing.find_eog_events`.

    #. Filter the raw data.

    #. Create `mne.Epochs` around the eyeblinks.

    #. Optionally average the `mne.Epochs` to produce an `mne.Evoked` if
       ``average=True`` was passed (default).

    #. Calculate SSP projection vectors on that data to capture the artifacts.

    💡 Note Raw data must be preloaded.

    Parameters
    ----------
    raw : mne.io.Raw
        Raw input file.
    raw_event : mne.io.Raw or None
        Raw file to use for event detection (if None, raw is used).
    tmin : float
        Time before event in seconds.
    tmax : float
        Time after event in seconds.
    n_grad : int
        Number of SSP vectors for gradiometers.
    n_mag : int
        Number of SSP vectors for magnetometers.
    n_eeg : int
        Number of SSP vectors for EEG.
    l_freq : float | None
        Filter low cut-off frequency for the data channels in Hz.
    h_freq : float | None
        Filter high cut-off frequency for the data channels in Hz.
    average : bool
        Compute SSP after averaging. Default is True.
    filter_length : str | int | None
        Number of taps to use for filtering.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.
    reject : dict | None
        Epoch rejection configuration (see Epochs).
    flat : dict | None
        Epoch flat configuration (see Epochs).
    bads : list
        List with (additional) bad channels.
    avg_ref : bool
        Add EEG average reference proj.
    no_proj : bool
        Exclude the SSP projectors currently in the fiff file.
    event_id : int
        ID to use for events.
    eog_l_freq : float
        Low pass frequency applied to the E0G channel for event detection.
    eog_h_freq : float
        High pass frequency applied to the EOG channel for event detection.
    tstart : float
        Start artifact detection after tstart seconds.
    filter_method : str
        Method for filtering ('iir' or 'fir').
    iir_params : dict | None
        Dictionary of parameters to use for IIR filtering.
        See mne.filter.construct_iir_filter for details. If iir_params
        is None and method="iir", 4th order Butterworth will be used.
    ch_name : str | None
        If not None, specify EOG channel name.
    copy : bool
        If False, filtering raw data is done in place. Defaults to True.
    return_drop_log : bool
        If True, return the drop log.

        ✨ Added in version 0.15
    meg : str
        Can be 'separate' (default) or 'combined' to compute projectors
        for magnetometers and gradiometers separately or jointly.
        If 'combined', ``n_mag == n_grad`` is required and the number of
        projectors computed for MEG will be ``n_mag``.

        ✨ Added in version 0.18

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------

    projs : list of Projection
        List of computed projection vectors.
    eog_events: ndarray
        Detected EOG events.
    drop_log : list
        The drop log, if requested.

    See Also
    --------
    find_eog_events
    create_eog_epochs

    Notes
    -----
    Filtering is applied to the EOG channel while finding events using
    ``eog_l_freq`` and ``eog_h_freq``, and then to the ``raw`` instance
    using ``l_freq`` and ``h_freq`` before creation of the epochs used to
    create the projectors.
    """
    ...
