from .._fiff.pick import pick_info as pick_info, pick_types as pick_types
from ..filter import filter_data as filter_data
from ..time_frequency import psd_array_multitaper as psd_array_multitaper
from ..utils import fill_doc as fill_doc
from .base import BaseEstimator as BaseEstimator
from .mixin import TransformerMixin as TransformerMixin
from _typeshed import Incomplete

class _ConstantScaler:
    """Scale channel types using constant values."""

    def __init__(self, info, scalings, do_scaling: bool = True) -> None: ...
    std_: Incomplete
    mean_: Incomplete

    def fit(self, X, y=None): ...
    def transform(self, X): ...
    def inverse_transform(self, X, y=None): ...
    def fit_transform(self, X, y=None): ...

class Scaler(TransformerMixin, BaseEstimator):
    """Standardize channel data.

    This class scales data for each channel. It differs from scikit-learn
    classes (e.g., `sklearn.preprocessing.StandardScaler`) in that
    it scales each *channel* by estimating μ and σ using data from all
    time points and epochs, as opposed to standardizing each *feature*
    (i.e., each time point for each channel) by estimating using μ and σ
    using data from all epochs.

    Parameters
    ----------

    info : mne.Info | None
        The `mne.Info` object with information about the sensors and methods of measurement. Only necessary if ``scalings`` is a dict or None.
    scalings : dict, str, default None
        Scaling method to be applied to data channel wise.

        * if scalings is None (default), scales mag by 1e15, grad by 1e13,
          and eeg by 1e6.
        * if scalings is `dict`, keys are channel types and values
          are scale factors.
        * if ``scalings=='median'``,
          `sklearn.preprocessing.RobustScaler`
          is used (requires sklearn version 0.17+).
        * if ``scalings=='mean'``,
          `sklearn.preprocessing.StandardScaler`
          is used.

    with_mean : bool, default True
        If True, center the data using mean (or median) before scaling.
        Ignored for channel-type scaling.
    with_std : bool, default True
        If True, scale the data to unit variance (``scalings='mean'``),
        quantile range (``scalings='median``), or using channel type
        if ``scalings`` is a dict or None).
    """

    info: Incomplete
    with_mean: Incomplete
    with_std: Incomplete
    scalings: Incomplete

    def __init__(
        self, info=None, scalings=None, with_mean: bool = True, with_std: bool = True
    ) -> None: ...
    def fit(self, epochs_data, y=None):
        """Standardize data across channels.

        Parameters
        ----------
        epochs_data : array, shape (n_epochs, n_channels, n_times)
            The data to concatenate channels.
        y : array, shape (n_epochs,)
            The label for each epoch.

        Returns
        -------
        self : instance of Scaler
            The modified instance.
        """
        ...

    def transform(self, epochs_data):
        """Standardize data across channels.

        Parameters
        ----------
        epochs_data : array, shape (n_epochs, n_channels[, n_times])
            The data.

        Returns
        -------
        X : array, shape (n_epochs, n_channels, n_times)
            The data concatenated over channels.

        Notes
        -----
        This function makes a copy of the data before the operations and the
        memory usage may be large with big data.
        """
        ...

    def fit_transform(self, epochs_data, y=None):
        """Fit to data, then transform it.

        Fits transformer to epochs_data and y and returns a transformed version
        of epochs_data.

        Parameters
        ----------
        epochs_data : array, shape (n_epochs, n_channels, n_times)
            The data.
        y : None | array, shape (n_epochs,)
            The label for each epoch.
            Defaults to None.

        Returns
        -------
        X : array, shape (n_epochs, n_channels, n_times)
            The data concatenated over channels.

        Notes
        -----
        This function makes a copy of the data before the operations and the
        memory usage may be large with big data.
        """
        ...

    def inverse_transform(self, epochs_data):
        """Invert standardization of data across channels.

        Parameters
        ----------
        epochs_data : array, shape (n_epochs, n_channels, n_times)
            The data.

        Returns
        -------
        X : array, shape (n_epochs, n_channels, n_times)
            The data concatenated over channels.

        Notes
        -----
        This function makes a copy of the data before the operations and the
        memory usage may be large with big data.
        """
        ...

class Vectorizer(TransformerMixin):
    """Transform n-dimensional array into 2D array of n_samples by n_features.

    This class reshapes an n-dimensional array into an n_samples * n_features
    array, usable by the estimators and transformers of scikit-learn.

    Attributes
    ----------
    features_shape_ : tuple
         Stores the original shape of data.

    Examples
    --------
    clf = make_pipeline(SpatialFilter(), _XdawnTransformer(), Vectorizer(),
                        LogisticRegression())
    """

    features_shape_: Incomplete

    def fit(self, X, y=None):
        """Store the shape of the features of X.

        Parameters
        ----------
        X : array-like
            The data to fit. Can be, for example a list, or an array of at
            least 2d. The first dimension must be of length n_samples, where
            samples are the independent samples used by the estimator
            (e.g. n_epochs for epoched data).
        y : None | array, shape (n_samples,)
            Used for scikit-learn compatibility.

        Returns
        -------
        self : instance of Vectorizer
            Return the modified instance.
        """
        ...

    def transform(self, X):
        """Convert given array into two dimensions.

        Parameters
        ----------
        X : array-like
            The data to fit. Can be, for example a list, or an array of at
            least 2d. The first dimension must be of length n_samples, where
            samples are the independent samples used by the estimator
            (e.g. n_epochs for epoched data).

        Returns
        -------
        X : array, shape (n_samples, n_features)
            The transformed data.
        """
        ...

    def fit_transform(self, X, y=None):
        """Fit the data, then transform in one step.

        Parameters
        ----------
        X : array-like
            The data to fit. Can be, for example a list, or an array of at
            least 2d. The first dimension must be of length n_samples, where
            samples are the independent samples used by the estimator
            (e.g. n_epochs for epoched data).
        y : None | array, shape (n_samples,)
            Used for scikit-learn compatibility.

        Returns
        -------
        X : array, shape (n_samples, -1)
            The transformed data.
        """
        ...

    def inverse_transform(self, X):
        """Transform 2D data back to its original feature shape.

        Parameters
        ----------
        X : array-like, shape (n_samples,  n_features)
            Data to be transformed back to original shape.

        Returns
        -------
        X : array
            The data transformed into shape as used in fit. The first
            dimension is of length n_samples.
        """
        ...

class PSDEstimator(TransformerMixin):
    """Compute power spectral density (PSD) using a multi-taper method.

    Parameters
    ----------
    sfreq : float
        The sampling frequency.
    fmin : float
        The lower frequency of interest.
    fmax : float
        The upper frequency of interest.
    bandwidth : float
        The bandwidth of the multi taper windowing function in Hz.
    adaptive : bool
        Use adaptive weights to combine the tapered spectra into PSD
        (slow, use n_jobs >> 1 to speed up computation).
    low_bias : bool
        Only use tapers with more than 90% spectral concentration within
        bandwidth.
    n_jobs : int
        Number of parallel jobs to use (only used if adaptive=True).
    normalization : 'full' | 'length'
        Normalization strategy. If "full", the PSD will be normalized by the
        sampling rate as well as the length of the signal (as in
        `Nitime <nitime:users-guide>`). Default is ``'length'``.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    mne.time_frequency.psd_array_multitaper
    mne.io.Raw.compute_psd
    mne.Epochs.compute_psd
    mne.Evoked.compute_psd
    """

    sfreq: Incomplete
    fmin: Incomplete
    fmax: Incomplete
    bandwidth: Incomplete
    adaptive: Incomplete
    low_bias: Incomplete
    n_jobs: Incomplete
    normalization: Incomplete

    def __init__(
        self,
        sfreq=6.283185307179586,
        fmin: int = 0,
        fmax=...,
        bandwidth=None,
        adaptive: bool = False,
        low_bias: bool = True,
        n_jobs=None,
        normalization: str = "length",
        *,
        verbose=None,
    ) -> None: ...
    def fit(self, epochs_data, y):
        """Compute power spectral density (PSD) using a multi-taper method.

        Parameters
        ----------
        epochs_data : array, shape (n_epochs, n_channels, n_times)
            The data.
        y : array, shape (n_epochs,)
            The label for each epoch.

        Returns
        -------
        self : instance of PSDEstimator
            The modified instance.
        """
        ...

    def transform(self, epochs_data):
        """Compute power spectral density (PSD) using a multi-taper method.

        Parameters
        ----------
        epochs_data : array, shape (n_epochs, n_channels, n_times)
            The data.

        Returns
        -------
        psd : array, shape (n_signals, n_freqs) or (n_freqs,)
            The computed PSD.
        """
        ...

class FilterEstimator(TransformerMixin):
    """Estimator to filter RtEpochs.

    Applies a zero-phase low-pass, high-pass, band-pass, or band-stop
    filter to the channels selected by "picks".

    l_freq and h_freq are the frequencies below which and above which,
    respectively, to filter out of the data. Thus the uses are:

        - l_freq < h_freq: band-pass filter
        - l_freq > h_freq: band-stop filter
        - l_freq is not None, h_freq is None: low-pass filter
        - l_freq is None, h_freq is not None: high-pass filter

    If n_jobs > 1, more memory is required as "len(picks) * n_times"
    additional time points need to be temporarily stored in memory.

    Parameters
    ----------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.

    l_freq : float | None
        For FIR filters, the lower pass-band edge; for IIR filters, the lower
        cutoff frequency. If None the data are only low-passed.

    h_freq : float | None
        For FIR filters, the upper pass-band edge; for IIR filters, the upper
        cutoff frequency. If None the data are only high-passed.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick `data
        channels`. None (default) will pick good data channels. Note that channels
        in ``info['bads']`` *will be included* if their names or indices are
        explicitly provided.

    filter_length : str | int
        Length of the FIR filter to use (if applicable):

        * **'auto' (default)**: The filter length is chosen based
          on the size of the transition regions (6.6 times the reciprocal
          of the shortest transition band for fir_window='hamming'
          and fir_design="firwin2", and half that for "firwin").
        * **str**: A human-readable time in
          units of "s" or "ms" (e.g., "10s" or "5500ms") will be
          converted to that number of samples if ``phase="zero"``, or
          the shortest power-of-two length at least that duration for
          ``phase="zero-double"``.
        * **int**: Specified length in samples. For fir_design="firwin",
          this should not be used.

    l_trans_bandwidth : float | str
        Width of the transition band at the low cut-off frequency in Hz
        (high pass or cutoff 1 in bandpass). Can be "auto"
        (default) to use a multiple of ``l_freq``::

            min(max(l_freq * 0.25, 2), l_freq)

        Only used for ``method='fir'``.

    h_trans_bandwidth : float | str
        Width of the transition band at the high cut-off frequency in Hz
        (low pass or cutoff 2 in bandpass). Can be "auto"
        (default in 0.14) to use a multiple of ``h_freq``::

            min(max(h_freq * 0.25, 2.), info['sfreq'] / 2. - h_freq)

        Only used for ``method='fir'``.
    n_jobs : int | str
        Number of jobs to run in parallel.
        Can be 'cuda' if ``cupy`` is installed properly and method='fir'.
    method : str
        'fir' will use overlap-add FIR filtering, 'iir' will use IIR filtering.
    iir_params : dict | None
        Dictionary of parameters to use for IIR filtering.
        See mne.filter.construct_iir_filter for details. If iir_params
        is None and method="iir", 4th order Butterworth will be used.

    fir_design : str
        Can be "firwin" (default) to use `scipy.signal.firwin`,
        or "firwin2" to use `scipy.signal.firwin2`. "firwin" uses
        a time-domain design technique that generally gives improved
        attenuation using fewer samples than "firwin2".

        ✨ Added in version 0.15

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    TemporalFilter

    Notes
    -----
    This is primarily meant for use in realtime applications.
    In general it is not recommended in a normal processing pipeline as it may result
    in edge artifacts. Use with caution.
    """

    info: Incomplete
    l_freq: Incomplete
    h_freq: Incomplete
    picks: Incomplete
    filter_length: Incomplete
    l_trans_bandwidth: Incomplete
    h_trans_bandwidth: Incomplete
    n_jobs: Incomplete
    method: Incomplete
    iir_params: Incomplete
    fir_design: Incomplete

    def __init__(
        self,
        info,
        l_freq,
        h_freq,
        picks=None,
        filter_length: str = "auto",
        l_trans_bandwidth: str = "auto",
        h_trans_bandwidth: str = "auto",
        n_jobs=None,
        method: str = "fir",
        iir_params=None,
        fir_design: str = "firwin",
        *,
        verbose=None,
    ) -> None: ...
    def fit(self, epochs_data, y):
        """Filter data.

        Parameters
        ----------
        epochs_data : array, shape (n_epochs, n_channels, n_times)
            The data.
        y : array, shape (n_epochs,)
            The label for each epoch.

        Returns
        -------
        self : instance of FilterEstimator
            The modified instance.
        """
        ...

    def transform(self, epochs_data):
        """Filter data.

        Parameters
        ----------
        epochs_data : array, shape (n_epochs, n_channels, n_times)
            The data.

        Returns
        -------
        X : array, shape (n_epochs, n_channels, n_times)
            The data after filtering.
        """
        ...

class UnsupervisedSpatialFilter(TransformerMixin, BaseEstimator):
    """Use unsupervised spatial filtering across time and samples.

    Parameters
    ----------
    estimator : instance of sklearn.base.BaseEstimator
        Estimator using some decomposition algorithm.
    average : bool, default False
        If True, the estimator is fitted on the average across samples
        (e.g. epochs).
    """

    estimator: Incomplete
    average: Incomplete

    def __init__(self, estimator, average: bool = False) -> None: ...
    def fit(self, X, y=None):
        """Fit the spatial filters.

        Parameters
        ----------
        X : array, shape (n_epochs, n_channels, n_times)
            The data to be filtered.
        y : None | array, shape (n_samples,)
            Used for scikit-learn compatibility.

        Returns
        -------
        self : instance of UnsupervisedSpatialFilter
            Return the modified instance.
        """
        ...

    def fit_transform(self, X, y=None):
        """Transform the data to its filtered components after fitting.

        Parameters
        ----------
        X : array, shape (n_epochs, n_channels, n_times)
            The data to be filtered.
        y : None | array, shape (n_samples,)
            Used for scikit-learn compatibility.

        Returns
        -------
        X : array, shape (n_epochs, n_channels, n_times)
            The transformed data.
        """
        ...

    def transform(self, X):
        """Transform the data to its spatial filters.

        Parameters
        ----------
        X : array, shape (n_epochs, n_channels, n_times)
            The data to be filtered.

        Returns
        -------
        X : array, shape (n_epochs, n_channels, n_times)
            The transformed data.
        """
        ...

    def inverse_transform(self, X):
        """Inverse transform the data to its original space.

        Parameters
        ----------
        X : array, shape (n_epochs, n_components, n_times)
            The data to be inverted.

        Returns
        -------
        X : array, shape (n_epochs, n_channels, n_times)
            The transformed data.
        """
        ...

class TemporalFilter(TransformerMixin):
    """Estimator to filter data array along the last dimension.

    Applies a zero-phase low-pass, high-pass, band-pass, or band-stop
    filter to the channels.

    l_freq and h_freq are the frequencies below which and above which,
    respectively, to filter out of the data. Thus the uses are:

        - l_freq < h_freq: band-pass filter
        - l_freq > h_freq: band-stop filter
        - l_freq is not None, h_freq is None: low-pass filter
        - l_freq is None, h_freq is not None: high-pass filter

    See `mne.filter.filter_data`.

    Parameters
    ----------
    l_freq : float | None
        Low cut-off frequency in Hz. If None the data are only low-passed.
    h_freq : float | None
        High cut-off frequency in Hz. If None the data are only
        high-passed.
    sfreq : float, default 1.0
        Sampling frequency in Hz.
    filter_length : str | int, default 'auto'
        Length of the FIR filter to use (if applicable):

            * int: specified length in samples.
            * 'auto' (default in 0.14): the filter length is chosen based
              on the size of the transition regions (7 times the reciprocal
              of the shortest transition band).
            * str: (default in 0.13 is "10s") a human-readable time in
              units of "s" or "ms" (e.g., "10s" or "5500ms") will be
              converted to that number of samples if ``phase="zero"``, or
              the shortest power-of-two length at least that duration for
              ``phase="zero-double"``.

    l_trans_bandwidth : float | str
        Width of the transition band at the low cut-off frequency in Hz
        (high pass or cutoff 1 in bandpass). Can be "auto"
        (default in 0.14) to use a multiple of ``l_freq``::

            min(max(l_freq * 0.25, 2), l_freq)

        Only used for ``method='fir'``.
    h_trans_bandwidth : float | str
        Width of the transition band at the high cut-off frequency in Hz
        (low pass or cutoff 2 in bandpass). Can be "auto"
        (default in 0.14) to use a multiple of ``h_freq``::

            min(max(h_freq * 0.25, 2.), info['sfreq'] / 2. - h_freq)

        Only used for ``method='fir'``.
    n_jobs : int | str, default 1
        Number of jobs to run in parallel.
        Can be 'cuda' if ``cupy`` is installed properly and method='fir'.
    method : str, default 'fir'
        'fir' will use overlap-add FIR filtering, 'iir' will use IIR
        forward-backward filtering (via filtfilt).
    iir_params : dict | None, default None
        Dictionary of parameters to use for IIR filtering.
        See mne.filter.construct_iir_filter for details. If iir_params
        is None and method="iir", 4th order Butterworth will be used.
    fir_window : str, default 'hamming'
        The window to use in FIR design, can be "hamming", "hann",
        or "blackman".
    fir_design : str
        Can be "firwin" (default) to use `scipy.signal.firwin`,
        or "firwin2" to use `scipy.signal.firwin2`. "firwin" uses
        a time-domain design technique that generally gives improved
        attenuation using fewer samples than "firwin2".

        ✨ Added in version 0.15

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    FilterEstimator
    Vectorizer
    mne.filter.filter_data
    """

    l_freq: Incomplete
    h_freq: Incomplete
    sfreq: Incomplete
    filter_length: Incomplete
    l_trans_bandwidth: Incomplete
    h_trans_bandwidth: Incomplete
    n_jobs: Incomplete
    method: Incomplete
    iir_params: Incomplete
    fir_window: Incomplete
    fir_design: Incomplete

    def __init__(
        self,
        l_freq=None,
        h_freq=None,
        sfreq: float = 1.0,
        filter_length: str = "auto",
        l_trans_bandwidth: str = "auto",
        h_trans_bandwidth: str = "auto",
        n_jobs=None,
        method: str = "fir",
        iir_params=None,
        fir_window: str = "hamming",
        fir_design: str = "firwin",
        *,
        verbose=None,
    ) -> None: ...
    def fit(self, X, y=None):
        """Do nothing (for scikit-learn compatibility purposes).

        Parameters
        ----------
        X : array, shape (n_epochs, n_channels, n_times) or or shape (n_channels, n_times)
            The data to be filtered over the last dimension. The channels
            dimension can be zero when passing a 2D array.
        y : None
            Not used, for scikit-learn compatibility issues.

        Returns
        -------
        self : instance of TemporalFilter
            The modified instance.
        """
        ...

    def transform(self, X):
        """Filter data along the last dimension.

        Parameters
        ----------
        X : array, shape (n_epochs, n_channels, n_times) or shape (n_channels, n_times)
            The data to be filtered over the last dimension. The channels
            dimension can be zero when passing a 2D array.

        Returns
        -------
        X : array
            The data after filtering.
        """
        ...
