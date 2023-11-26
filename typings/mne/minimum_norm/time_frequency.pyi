from .._fiff.constants import FIFF as FIFF
from .._fiff.pick import pick_info as pick_info
from ..baseline import rescale as rescale
from ..epochs import Epochs as Epochs
from ..event import make_fixed_length_events as make_fixed_length_events
from ..evoked import EvokedArray as EvokedArray
from ..label import BiHemiLabel as BiHemiLabel, Label as Label
from ..parallel import parallel_func as parallel_func
from ..time_frequency.tfr import cwt as cwt, morlet as morlet
from ..utils import ProgressBar as ProgressBar, logger as logger
from .inverse import INVERSE_METHODS as INVERSE_METHODS, combine_xyz as combine_xyz

def source_band_induced_power(
    epochs,
    inverse_operator,
    bands,
    label=None,
    lambda2=0.1111111111111111,
    method: str = "dSPM",
    nave: int = 1,
    n_cycles: int = 5,
    df: int = 1,
    use_fft: bool = False,
    decim: int = 1,
    baseline=None,
    baseline_mode: str = "logratio",
    pca: bool = True,
    n_jobs=None,
    prepared: bool = False,
    method_params=None,
    use_cps: bool = True,
    *,
    verbose=None,
):
    """Compute source space induced power in given frequency bands.

    Parameters
    ----------
    epochs : instance of Epochs
        The epochs.
    inverse_operator : instance of InverseOperator
        The inverse operator.
    bands : dict
        Example : bands = dict(alpha=[8, 9]).
    label : Label | list of Label
        Restricts the source estimates to a given label or list of labels. If
        labels are provided in a list, power will be averaged over vertices.
    lambda2 : float
        The regularization parameter of the minimum norm.
    method : "MNE" | "dSPM" | "sLORETA" | "eLORETA"
        Use minimum norm, dSPM (default), sLORETA, or eLORETA.
    nave : int
        The number of averages used to scale the noise covariance matrix.
    n_cycles : float | array of float
        Number of cycles. Fixed number or one per frequency.
    df : float
        Delta frequency within bands.
    use_fft : bool
        Do convolutions in time or frequency domain with FFT.
    decim : int
        Temporal decimation factor.
    baseline : None (default) or tuple, shape (2,)
        The time interval to apply baseline correction. If None do not apply
        it. If baseline is (a, b) the interval is between "a (s)" and "b (s)".
        If a is None the beginning of the data is used and if b is None then b
        is set to the end of the interval. If baseline is equal to (None, None)
        all the time interval is used.
    baseline_mode : 'mean' | 'ratio' | 'logratio' | 'percent' | 'zscore' | 'zlogratio'
        Perform baseline correction by

        - subtracting the mean of baseline values ('mean')
        - dividing by the mean of baseline values ('ratio')
        - dividing by the mean of baseline values and taking the log
          ('logratio')
        - subtracting the mean of baseline values followed by dividing by
          the mean of baseline values ('percent')
        - subtracting the mean of baseline values and dividing by the
          standard deviation of baseline values ('zscore')
        - dividing by the mean of baseline values, taking the log, and
          dividing by the standard deviation of log baseline values
          ('zlogratio')

    pca : bool
        If True, the true dimension of data is estimated before running
        the time-frequency transforms. It reduces the computation times
        e.g. with a dataset that was maxfiltered (true dim is 64).
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the :mod:`joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a :class:`joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.
    prepared : bool
        If True, do not call :func:`prepare_inverse_operator`.
    method_params : dict | None
        Additional options for eLORETA. See Notes of :func:`apply_inverse`.

        .. versionadded:: 0.16

    use_cps : bool
        Whether to use cortical patch statistics to define normal orientations for
        surfaces (default True).

        Only used when the inverse is free orientation (``loose=1.``),
        not in surface orientation, and ``pick_ori='normal'``.

        .. versionadded:: 0.20

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    stcs : dict of SourceEstimate (or VolSourceEstimate)
        The estimated source space induced power estimates in shape
        (n_vertices, n_frequencies, n_samples) if label=None or label=label.
        For lists of one or more labels, the induced power estimate has shape
        (n_labels, n_frequencies, n_samples).
    """
    ...

def source_induced_power(
    epochs,
    inverse_operator,
    freqs,
    label=None,
    lambda2=0.1111111111111111,
    method: str = "dSPM",
    nave: int = 1,
    n_cycles: int = 5,
    decim: int = 1,
    use_fft: bool = False,
    pick_ori=None,
    baseline=None,
    baseline_mode: str = "logratio",
    pca: bool = True,
    n_jobs=None,
    *,
    return_plv: bool = True,
    zero_mean: bool = False,
    prepared: bool = False,
    method_params=None,
    use_cps: bool = True,
    verbose=None,
):
    """Compute induced power and phase lock.

    Computation can optionally be restricted in a label.

    Parameters
    ----------
    epochs : instance of Epochs
        The epochs.
    inverse_operator : instance of InverseOperator
        The inverse operator.
    freqs : array
        Array of frequencies of interest.
    label : Label | list of Label
        Restricts the source estimates to a given label or list of labels. If
        labels are provided in a list, power will be averaged over vertices within each
        label.
    lambda2 : float
        The regularization parameter of the minimum norm.
    method : "MNE" | "dSPM" | "sLORETA" | "eLORETA"
        Use minimum norm, dSPM (default), sLORETA, or eLORETA.
    nave : int
        The number of averages used to scale the noise covariance matrix.
    n_cycles : float | array of float
        Number of cycles. Fixed number or one per frequency.
    decim : int
        Temporal decimation factor.
    use_fft : bool
        Do convolutions in time or frequency domain with FFT.
    pick_ori : None | "normal"
        If "normal", rather than pooling the orientations by taking the norm,
        only the radial component is kept. This is only implemented
        when working with loose orientations.
    baseline : None (default) or tuple of length 2
        The time interval to apply baseline correction.
        If None do not apply it. If baseline is (a, b)
        the interval is between "a (s)" and "b (s)".
        If a is None the beginning of the data is used
        and if b is None then b is set to the end of the interval.
        If baseline is equal to (None, None) all the time
        interval is used.
    baseline_mode : 'mean' | 'ratio' | 'logratio' | 'percent' | 'zscore' | 'zlogratio'
        Perform baseline correction by

        - subtracting the mean of baseline values ('mean')
        - dividing by the mean of baseline values ('ratio')
        - dividing by the mean of baseline values and taking the log
          ('logratio')
        - subtracting the mean of baseline values followed by dividing by
          the mean of baseline values ('percent')
        - subtracting the mean of baseline values and dividing by the
          standard deviation of baseline values ('zscore')
        - dividing by the mean of baseline values, taking the log, and
          dividing by the standard deviation of log baseline values
          ('zlogratio')

    pca : bool
        If True, the true dimension of data is estimated before running
        the time-frequency transforms. It reduces the computation times
        e.g. with a dataset that was maxfiltered (true dim is 64).
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the :mod:`joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a :class:`joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.
    return_plv : bool
        If True, return the phase-locking value array. Else, only return power.

        .. versionadded:: 1.6
    zero_mean : bool
        Make sure the wavelets are zero mean.
    prepared : bool
        If True, do not call :func:`prepare_inverse_operator`.
    method_params : dict | None
        Additional options for eLORETA. See Notes of :func:`apply_inverse`.

    use_cps : bool
        Whether to use cortical patch statistics to define normal orientations for
        surfaces (default True).

        Only used when the inverse is free orientation (``loose=1.``),
        not in surface orientation, and ``pick_ori='normal'``.

        .. versionadded:: 0.20

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    power : array
        The induced power array with shape (n_sources, n_freqs, n_samples) if
        label=None or label=label. For lists of one or more labels, the induced
        power estimate has shape (n_labels, n_frequencies, n_samples).
    plv : array
        The phase-locking value array with shape (n_sources, n_freqs,
        n_samples). Only returned if ``return_plv=True``.
    """
    ...

def compute_source_psd(
    raw,
    inverse_operator,
    lambda2=0.1111111111111111,
    method: str = "dSPM",
    tmin: float = 0.0,
    tmax=None,
    fmin: float = 0.0,
    fmax: float = 200.0,
    n_fft: int = 2048,
    overlap: float = 0.5,
    pick_ori=None,
    label=None,
    nave: int = 1,
    pca: bool = True,
    prepared: bool = False,
    method_params=None,
    inv_split=None,
    bandwidth: str = "hann",
    adaptive: bool = False,
    low_bias: bool = False,
    n_jobs=None,
    return_sensor: bool = False,
    dB: bool = False,
    *,
    verbose=None,
):
    """Compute source power spectral density (PSD).

    Parameters
    ----------
    raw : instance of Raw
        The raw data.
    inverse_operator : instance of InverseOperator
        The inverse operator.
    lambda2 : float
        The regularization parameter.
    method : "MNE" | "dSPM" | "sLORETA"
        Use minimum norm, dSPM (default), sLORETA, or eLORETA.
    tmin : float
        The beginning of the time interval of interest (in seconds).
        Use 0. for the beginning of the file.
    tmax : float | None
        The end of the time interval of interest (in seconds). If None
        stop at the end of the file.
    fmin : float
        The lower frequency of interest.
    fmax : float
        The upper frequency of interest.
    n_fft : int
        Window size for the FFT. Should be a power of 2.
    overlap : float
        The overlap fraction between windows. Should be between 0 and 1.
        0 means no overlap.
    pick_ori : None | "normal"
        If "normal", rather than pooling the orientations by taking the norm,
        only the radial component is kept. This is only implemented
        when working with loose orientations.
    label : Label
        Restricts the source estimates to a given label.
    nave : int
        The number of averages used to scale the noise covariance matrix.
    pca : bool
        If True, the true dimension of data is estimated before running
        the time-frequency transforms. It reduces the computation times
        e.g. with a dataset that was maxfiltered (true dim is 64).
    prepared : bool
        If True, do not call :func:`prepare_inverse_operator`.
    method_params : dict | None
        Additional options for eLORETA. See Notes of :func:`apply_inverse`.

        .. versionadded:: 0.16
    inv_split : int or None
        Split inverse operator into inv_split parts in order to save memory.

        .. versionadded:: 0.17
    bandwidth : float | str
        The bandwidth of the multi taper windowing function in Hz.
        Can also be a string (e.g., 'hann') to use a single window.

        For backward compatibility, the default is 'hann'.

        .. versionadded:: 0.17
    adaptive : bool
        Use adaptive weights to combine the tapered spectra into PSD
        (slow, use n_jobs >> 1 to speed up computation).

        .. versionadded:: 0.17
    low_bias : bool
        Only use tapers with more than 90% spectral concentration within
        bandwidth.

        .. versionadded:: 0.17
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the :mod:`joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a :class:`joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.
        It is only used if adaptive=True.

        .. versionadded:: 0.17
    return_sensor : bool
        If True, return the sensor PSDs as an EvokedArray.

        .. versionadded:: 0.17
    dB : bool
        If True (default False), return output it decibels.

        .. versionadded:: 0.17

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    stc_psd : instance of SourceEstimate | VolSourceEstimate
        The PSD of each of the sources.
    sensor_psd : instance of EvokedArray
        The PSD of each sensor. Only returned if ``return_sensor`` is True.

    See Also
    --------
    compute_source_psd_epochs

    Notes
    -----
    Each window is multiplied by a window before processing, so
    using a non-zero overlap is recommended.

    This function is different from :func:`compute_source_psd_epochs` in that:

    1. ``bandwidth='hann'`` by default, skipping multitaper estimation
    2. For convenience it wraps
       :func:`mne.make_fixed_length_events` and :class:`mne.Epochs`.

    Otherwise the two should produce identical results.
    """
    ...

def compute_source_psd_epochs(
    epochs,
    inverse_operator,
    lambda2=0.1111111111111111,
    method: str = "dSPM",
    fmin: float = 0.0,
    fmax: float = 200.0,
    pick_ori=None,
    label=None,
    nave: int = 1,
    pca: bool = True,
    inv_split=None,
    bandwidth: float = 4.0,
    adaptive: bool = False,
    low_bias: bool = True,
    return_generator: bool = False,
    n_jobs=None,
    prepared: bool = False,
    method_params=None,
    return_sensor: bool = False,
    use_cps: bool = True,
    verbose=None,
):
    """Compute source power spectral density (PSD) from Epochs.

    This uses the multi-taper method to compute the PSD for each epoch.

    Parameters
    ----------
    epochs : instance of Epochs
        The raw data.
    inverse_operator : instance of InverseOperator
        The inverse operator.
    lambda2 : float
        The regularization parameter.
    method : "MNE" | "dSPM" | "sLORETA" | "eLORETA"
        Use minimum norm, dSPM (default), sLORETA, or eLORETA.
    fmin : float
        The lower frequency of interest.
    fmax : float
        The upper frequency of interest.
    pick_ori : None | "normal"
        If "normal", rather than pooling the orientations by taking the norm,
        only the radial component is kept. This is only implemented
        when working with loose orientations.
    label : Label
        Restricts the source estimates to a given label.
    nave : int
        The number of averages used to scale the noise covariance matrix.
    pca : bool
        If True, the true dimension of data is estimated before running
        the time-frequency transforms. It reduces the computation times
        e.g. with a dataset that was maxfiltered (true dim is 64).
    inv_split : int or None
        Split inverse operator into inv_split parts in order to save memory.
    bandwidth : float | str
        The bandwidth of the multi taper windowing function in Hz.
        Can also be a string (e.g., 'hann') to use a single window.
    adaptive : bool
        Use adaptive weights to combine the tapered spectra into PSD
        (slow, use n_jobs >> 1 to speed up computation).
    low_bias : bool
        Only use tapers with more than 90% spectral concentration within
        bandwidth.
    return_generator : bool
        Return a generator object instead of a list. This allows iterating
        over the stcs without having to keep them all in memory.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the :mod:`joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a :class:`joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.
        It is only used if adaptive=True.
    prepared : bool
        If True, do not call :func:`prepare_inverse_operator`.
    method_params : dict | None
        Additional options for eLORETA. See Notes of :func:`apply_inverse`.

        .. versionadded:: 0.16
    return_sensor : bool
        If True, also return the sensor PSD for each epoch as an EvokedArray.

        .. versionadded:: 0.17

    use_cps : bool
        Whether to use cortical patch statistics to define normal orientations for
        surfaces (default True).

        Only used when the inverse is free orientation (``loose=1.``),
        not in surface orientation, and ``pick_ori='normal'``.

        .. versionadded:: 0.20

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    out : list (or generator object)
        A list (or generator) for the source space PSD (and optionally the
        sensor PSD) for each epoch.

    See Also
    --------
    compute_source_psd
    """
    ...
