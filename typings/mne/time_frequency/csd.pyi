from .._fiff.pick import pick_channels as pick_channels
from ..parallel import parallel_func as parallel_func
from ..utils import (
    ProgressBar as ProgressBar,
    copy_function_doc_to_method_doc as copy_function_doc_to_method_doc,
    logger as logger,
    warn as warn,
)
from ..viz.misc import plot_csd as plot_csd
from .tfr import EpochsTFR as EpochsTFR, morlet as morlet
from _typeshed import Incomplete

def pick_channels_csd(
    csd, include=[], exclude=[], ordered=None, copy: bool = True, *, verbose=None
):
    """## 🧠 Pick channels from cross-spectral density matrix.

    -----
    ### 🛠️ Parameters

    #### `csd : instance of CrossSpectralDensity`
        The CSD object to select the channels from.
    #### `include : list of str`
        List of channels to include (if empty, include all available).
    #### `exclude : list of str`
        Channels to exclude (if empty, do not exclude any).

    #### `ordered : bool`
        If True (default False), ensure that the order of the channels in
        the modified instance matches the order of ``ch_names``.

        ✨ Added in vesion 0.20.0
        🎭 Changed in version 1.5
            The default changed from False in 1.4 to True in 1.5.
    #### `copy : bool`
        If True (the default), return a copy of the CSD matrix with the
        modified channels. If False, channels are modified in-place.

        ✨ Added in vesion 0.20.0

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `res : instance of CrossSpectralDensity`
        Cross-spectral density restricted to selected channels.
    """
    ...

class CrossSpectralDensity:
    """## 🧠 Cross-spectral density.

    Given a list of time series, the CSD matrix denotes for each pair of time
    series, the cross-spectral density. This matrix is symmetric and internally
    stored as a vector.

    This object can store multiple CSD matrices: one for each frequency.
    Use ``.get_data(freq)`` to obtain an CSD matrix as an ndarray.

    -----
    ### 🛠️ Parameters

    #### `data : ndarray, shape ((n_channels**2 + n_channels) // 2, n_frequencies)`
        For each frequency, the cross-spectral density matrix in vector format.
    #### `ch_names : list of str`
        List of string names for each channel.
    #### `frequencies : float | list of float | list of list of float`
        Frequency or frequencies for which the CSD matrix was calculated. When
        averaging across frequencies (see the `CrossSpectralDensity.mean`
        function), this will be a list of lists that contains for each
        frequency bin, the frequencies that were averaged. Frequencies should
        always be sorted.
    #### `n_fft : int`
        The number of FFT points or samples that have been used in the
        computation of this CSD.
    #### `tmin : float | None`
        Start of the time window for which CSD was calculated in seconds. Can
        be ``None`` (the default) to indicate no timing information is
        available.
    #### `tmax : float | None`
        End of the time window for which CSD was calculated in seconds. Can be
        ``None`` (the default) to indicate no timing information is available.
    #### `projs : list of Projection | None`
        List of projectors to apply to timeseries data when using this CSD
        object to compute a DICS beamformer. Defaults to ``None``, which means
        no projectors will be applied.

    -----
    ### 👉 See Also

    csd_fourier
    csd_multitaper
    csd_morlet
    csd_array_fourier
    csd_array_multitaper
    csd_array_morlet
    """

    ch_names: Incomplete
    tmin: Incomplete
    tmax: Incomplete
    frequencies: Incomplete
    n_fft: Incomplete
    projs: Incomplete

    def __init__(
        self, data, ch_names, frequencies, n_fft, tmin=None, tmax=None, projs=None
    ) -> None: ...
    @property
    def n_channels(self):
        """### Number of time series defined in this CSD object."""
        ...
    def __len__(self) -> int:
        """### Return number of frequencies.

        -----
        ### ⏎ Returns

        #### `n_freqs : int`
            The number of frequencies.
        """
        ...
    def sum(self, fmin=None, fmax=None):
        """### Calculate the sum CSD in the given frequency range(s).

        If the exact given frequencies are not available, the nearest
        frequencies will be chosen.

        -----
        ### 🛠️ Parameters

        #### `fmin : float | list of float | None`
            Lower bound of the frequency range in Hertz. Defaults to the lowest
            frequency available. When a list of frequencies is given, these are
            used as the lower bounds (inclusive) of frequency bins and the sum
            is taken for each bin.
        #### `fmax : float | list of float | None`
            Upper bound of the frequency range in Hertz. Defaults to the
            highest frequency available. When a list of frequencies is given,
            these are used as the upper bounds (inclusive) of frequency bins
            and the sum is taken for each bin.

        -----
        ### ⏎ Returns

        #### `csd : instance of CrossSpectralDensity`
            The CSD matrix, summed across the given frequency range(s).
        """
        ...
    def mean(self, fmin=None, fmax=None):
        """### Calculate the mean CSD in the given frequency range(s).

        -----
        ### 🛠️ Parameters

        #### `fmin : float | list of float | None`
            Lower bound of the frequency range in Hertz. Defaults to the lowest
            frequency available. When a list of frequencies is given, these are
            used as the lower bounds (inclusive) of frequency bins and the mean
            is taken for each bin.
        #### `fmax : float | list of float | None`
            Upper bound of the frequency range in Hertz. Defaults to the
            highest frequency available. When a list of frequencies is given,
            these are used as the upper bounds (inclusive) of frequency bins
            and the mean is taken for each bin.

        -----
        ### ⏎ Returns

        #### `csd : instance of CrossSpectralDensity`
            The CSD matrix, averaged across the given frequency range(s).
        """
        ...
    def pick_frequency(self, freq=None, index=None):
        """### Get a CrossSpectralDensity object with only the given frequency.

        -----
        ### 🛠️ Parameters

        #### `freq : float | None`
            Return the CSD matrix for a specific frequency. Only available
            when no averaging across frequencies has been done.
        #### `index : int | None`
            Return the CSD matrix for the frequency or frequency-bin with the
            given index.

        -----
        ### ⏎ Returns

        #### `csd : instance of CrossSpectralDensity`
            A CSD object containing a single CSD matrix that corresponds to the
            requested frequency or frequency-bin.

        -----
        ### 👉 See Also

        get_data
        """
        ...
    def get_data(self, frequency=None, index=None, as_cov: bool = False):
        """### Get the CSD matrix for a given frequency as NumPy array.

        If there is only one matrix defined in the CSD object, calling this
        method without any parameters will return it. If multiple matrices are
        defined, use either the ``frequency`` or ``index`` parameter to select
        one.

        -----
        ### 🛠️ Parameters

        #### `frequency : float | None`
            Return the CSD matrix for a specific frequency. Only available when
            no averaging across frequencies has been done.
        #### `index : int | None`
            Return the CSD matrix for the frequency or frequency-bin with the
            given index.
        #### `as_cov : bool`
            Whether to return the data as a numpy array (`False`, the default),
            or pack it in a `mne.Covariance` object (`True`).

            ✨ Added in vesion 0.20

        -----
        ### ⏎ Returns

        #### `csd : ndarray, shape (n_channels, n_channels) | instance of Covariance`
            The CSD matrix corresponding to the requested frequency.

        -----
        ### 👉 See Also

        pick_frequency
        """
        ...
    def plot(
        self,
        info=None,
        mode: str = "csd",
        colorbar: bool = True,
        cmap: str = "viridis",
        n_cols=None,
        show: bool = True,
    ):
        """### Plot CSD matrices.

        A sub-plot is created for each frequency. If an info object is passed to
        the function, different channel types are plotted in different figures.

        -----
        ### 🛠️ Parameters

        #### `info : mne.Info | None`
            The `mne.Info` object with information about the sensors and methods of measurement.
            Used to split the figure by channel-type, if provided.
            By default, the CSD matrix is plotted as a whole.
        #### `mode : 'csd' | 'coh'`
            Whether to plot the cross-spectral density ('csd', the default), or
            the coherence ('coh') between the channels.
        #### `colorbar : bool`
            Whether to show a colorbar. Defaults to ``True``.
        #### `cmap : str | None`
            The matplotlib colormap to use. Defaults to None, which means the
            colormap will default to matplotlib's default.
        #### `n_cols : int | None`
            CSD matrices are plotted in a grid. This parameter controls how
            many matrix to plot side by side before starting a new row. By
            default, a number will be chosen to make the grid as square as
            possible.
        #### `show : bool`
            Whether to show the figure. Defaults to ``True``.

        -----
        ### ⏎ Returns

        #### `fig : list of Figure`
            The figures created by this function.
        """
        ...
    def __getitem__(self, sel):
        """### Subselect frequencies.

        -----
        ### 🛠️ Parameters

        #### `sel : ndarray`
            Array of frequency indices to subselect.

        -----
        ### ⏎ Returns

        #### `csd : instance of CrossSpectralDensity`
            A new CSD instance with the subset of frequencies.
        """
        ...
    def save(self, fname, *, overwrite: bool = False, verbose=None) -> None:
        """### Save the CSD to an HDF5 file.

        -----
        ### 🛠️ Parameters

        #### `fname : path-like`
            The name of the file to save the CSD to. The extension ``'.h5'``
            will be appended if the given filename doesn't have it already.

        #### `overwrite : bool`
            If True (default False), overwrite the destination file if it
            exists.

            ✨ Added in vesion 1.0

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

            ✨ Added in vesion 1.0

        -----
        ### 👉 See Also

        #### `read_csd : For reading CSD objects from a file.`
        """
        ...
    def copy(self):
        """### Return copy of the CrossSpectralDensity object.

        -----
        ### ⏎ Returns

        #### `copy : instance of CrossSpectralDensity`
            A copy of the object.
        """
        ...
    def pick_channels(self, ch_names, ordered: bool = False):
        """### Pick channels from this cross-spectral density matrix.

        -----
        ### 🛠️ Parameters

        #### `ch_names : list of str`
            List of channels to keep. All other channels are dropped.
        #### `ordered : bool`
            If True (default False), ensure that the order of the channels
            matches the order of ``ch_names``.

        -----
        ### ⏎ Returns

        #### `csd : instance of CrossSpectralDensity.`
            The modified cross-spectral density object.

        -----
        ### 📖 Notes

        Operates in-place.

        ✨ Added in vesion 0.20.0
        """
        ...

def read_csd(fname):
    """## 🧠 Read a CrossSpectralDensity object from an HDF5 file.

    -----
    ### 🛠️ Parameters

    #### `fname : path-like`
        The name of the file to read the CSD from. The extension ``'.h5'`` will
        be appended if the given filename doesn't have it already.

    -----
    ### ⏎ Returns

    #### `csd : instance of CrossSpectralDensity`
        The CSD that was stored in the file.

    -----
    ### 👉 See Also

    CrossSpectralDensity.save : For saving CSD objects.
    """
    ...

def csd_fourier(
    epochs,
    fmin: int = 0,
    fmax=...,
    tmin=None,
    tmax=None,
    picks=None,
    n_fft=None,
    projs=None,
    n_jobs=None,
    *,
    verbose=None,
):
    """## 🧠 Estimate cross-spectral density from an array using short-time fourier.

    -----
    ### 🛠️ Parameters

    #### `epochs : instance of Epochs`
        The epochs to compute the CSD for.
    #### `fmin : float`
        Minimum frequency of interest, in Hertz.
    #### `fmax : float | np.inf`
        Maximum frequency of interest, in Hertz.
    #### `tmin : float | None`
        Minimum time instant to consider, in seconds. If ``None`` start at
        first sample.
    #### `tmax : float | None`
        Maximum time instant to consider, in seconds. If ``None`` end at last
        sample.
    #### `picks : str | array-like | slice | None`
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick good data channels (excluding reference
        MEG channels). Note that channels in ``info['bads']`` *will be included* if
        their names or indices are explicitly provided.
    #### `n_fft : int | None`
        Length of the FFT. If ``None``, the exact number of samples between
        ``tmin`` and ``tmax`` will be used.
    #### `projs : list of Projection | None`
        List of projectors to store in the CSD object. Defaults to ``None``,
        which means the projectors defined in the Epochs object will be copied.
    #### `n_jobs : int | None`
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `csd : instance of CrossSpectralDensity`
        The computed cross-spectral density.

    -----
    ### 👉 See Also

    csd_array_fourier
    csd_array_morlet
    csd_array_multitaper
    csd_morlet
    csd_multitaper
    """
    ...

def csd_array_fourier(
    X,
    sfreq,
    t0: int = 0,
    fmin: int = 0,
    fmax=...,
    tmin=None,
    tmax=None,
    ch_names=None,
    n_fft=None,
    projs=None,
    n_jobs=None,
    *,
    verbose=None,
):
    """## 🧠 Estimate cross-spectral density from an array using short-time fourier.

    -----
    ### 🛠️ Parameters

    X : array-like, shape (n_epochs, n_channels, n_times)
        The time series data consisting of n_epochs separate observations
        of signals with n_channels time-series of length n_times.
    #### `sfreq : float`
        Sampling frequency of observations.
    t0 : float
        Time of the first sample relative to the onset of the epoch, in
        seconds. Defaults to 0.
    #### `fmin : float`
        Minimum frequency of interest, in Hertz.
    #### `fmax : float | np.inf`
        Maximum frequency of interest, in Hertz.
    #### `tmin : float | None`
        Minimum time instant to consider, in seconds. If ``None`` start at
        first sample.
    #### `tmax : float | None`
        Maximum time instant to consider, in seconds. If ``None`` end at last
        sample.
    #### `ch_names : list of str | None`
        A name for each time series. If ``None`` (the default), the series will
        be named 'SERIES###'.
    #### `n_fft : int | None`
        Length of the FFT. If ``None``, the exact number of samples between
        ``tmin`` and ``tmax`` will be used.
    #### `projs : list of Projection | None`
        List of projectors to store in the CSD object. Defaults to ``None``,
        which means no projectors are stored.
    #### `n_jobs : int | None`
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `csd : instance of CrossSpectralDensity`
        The computed cross-spectral density.

    -----
    ### 👉 See Also

    csd_array_morlet
    csd_array_multitaper
    csd_fourier
    csd_morlet
    csd_multitaper
    """
    ...

def csd_multitaper(
    epochs,
    fmin: int = 0,
    fmax=...,
    tmin=None,
    tmax=None,
    picks=None,
    n_fft=None,
    bandwidth=None,
    adaptive: bool = False,
    low_bias: bool = True,
    projs=None,
    n_jobs=None,
    *,
    verbose=None,
):
    """## 🧠 Estimate cross-spectral density from epochs using a multitaper method.

    -----
    ### 🛠️ Parameters

    #### `epochs : instance of Epochs`
        The epochs to compute the CSD for.
    #### `fmin : float | None`
        Minimum frequency of interest, in Hertz.
    #### `fmax : float | np.inf`
        Maximum frequency of interest, in Hertz.
    #### `tmin : float`
        Minimum time instant to consider, in seconds. If ``None`` start at
        first sample.
    #### `tmax : float | None`
        Maximum time instant to consider, in seconds. If ``None`` end at last
        sample.
    #### `picks : str | array-like | slice | None`
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick good data channels (excluding reference
        MEG channels). Note that channels in ``info['bads']`` *will be included* if
        their names or indices are explicitly provided.
    #### `n_fft : int | None`
        Length of the FFT. If ``None``, the exact number of samples between
        ``tmin`` and ``tmax`` will be used.
    #### `bandwidth : float | None`
        The bandwidth of the multitaper windowing function in Hz.
    #### `adaptive : bool`
        Use adaptive weights to combine the tapered spectra into PSD.
    #### `low_bias : bool`
        Only use tapers with more than 90% spectral concentration within
        bandwidth.
    #### `projs : list of Projection | None`
        List of projectors to store in the CSD object. Defaults to ``None``,
        which means the projectors defined in the Epochs object will by copied.
    #### `n_jobs : int | None`
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `csd : instance of CrossSpectralDensity`
        The computed cross-spectral density.

    -----
    ### 👉 See Also

    csd_array_fourier
    csd_array_morlet
    csd_array_multitaper
    csd_fourier
    csd_morlet
    """
    ...

def csd_array_multitaper(
    X,
    sfreq,
    t0: int = 0,
    fmin: int = 0,
    fmax=...,
    tmin=None,
    tmax=None,
    ch_names=None,
    n_fft=None,
    bandwidth=None,
    adaptive: bool = False,
    low_bias: bool = True,
    projs=None,
    n_jobs=None,
    max_iter: int = 250,
    *,
    verbose=None,
):
    """## 🧠 Estimate cross-spectral density from an array using a multitaper method.

    -----
    ### 🛠️ Parameters

    X : array-like, shape (n_epochs, n_channels, n_times)
        The time series data consisting of n_epochs separate observations
        of signals with n_channels time-series of length n_times.
    #### `sfreq : float`
        Sampling frequency of observations.
    t0 : float
        Time of the first sample relative to the onset of the epoch, in
        seconds. Defaults to 0.
    #### `fmin : float`
        Minimum frequency of interest, in Hertz.
    #### `fmax : float | np.inf`
        Maximum frequency of interest, in Hertz.
    #### `tmin : float | None`
        Minimum time instant to consider, in seconds. If ``None`` start at
        first sample.
    #### `tmax : float | None`
        Maximum time instant to consider, in seconds. If ``None`` end at last
        sample.
    #### `ch_names : list of str | None`
        A name for each time series. If ``None`` (the default), the series will
        be named 'SERIES###'.
    #### `n_fft : int | None`
        Length of the FFT. If ``None``, the exact number of samples between
        ``tmin`` and ``tmax`` will be used.
    #### `bandwidth : float | None`
        The bandwidth of the multitaper windowing function in Hz.
    #### `adaptive : bool`
        Use adaptive weights to combine the tapered spectra into PSD.
    #### `low_bias : bool`
        Only use tapers with more than 90% spectral concentration within
        bandwidth.
    #### `projs : list of Projection | None`
        List of projectors to store in the CSD object. Defaults to ``None``,
        which means no projectors are stored.
    #### `n_jobs : int | None`
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.

    #### `max_iter : int`
        Maximum number of iterations to reach convergence when combining the
        tapered spectra with adaptive weights (see argument ``adaptive``). This
        argument has not effect if ``adaptive`` is set to ``False``.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `csd : instance of CrossSpectralDensity`
        The computed cross-spectral density.

    -----
    ### 👉 See Also

    csd_array_fourier
    csd_array_morlet
    csd_fourier
    csd_morlet
    csd_multitaper
    """
    ...

def csd_morlet(
    epochs,
    frequencies,
    tmin=None,
    tmax=None,
    picks=None,
    n_cycles: int = 7,
    use_fft: bool = True,
    decim: int = 1,
    projs=None,
    n_jobs=None,
    *,
    verbose=None,
):
    """## 🧠 Estimate cross-spectral density from epochs using Morlet wavelets.

    -----
    ### 🛠️ Parameters

    #### `epochs : instance of Epochs`
        The epochs to compute the CSD for.
    #### `frequencies : list of float`
        The frequencies of interest, in Hertz.
    #### `tmin : float | None`
        Minimum time instant to consider, in seconds. If ``None`` start at
        first sample.
    #### `tmax : float | None`
        Maximum time instant to consider, in seconds. If ``None`` end at last
        sample.
    #### `picks : str | array-like | slice | None`
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick good data channels (excluding reference
        MEG channels). Note that channels in ``info['bads']`` *will be included* if
        their names or indices are explicitly provided.
    #### `n_cycles : float | list of float | None`
        Number of cycles to use when constructing Morlet wavelets. Fixed number
        or one per frequency. Defaults to 7.
    #### `use_fft : bool`
        Whether to use FFT-based convolution to compute the wavelet transform.
        Defaults to True.
    #### `decim : int | slice`
        To reduce memory usage, decimation factor during time-frequency
        decomposition. Defaults to 1 (no decimation).

        If `int`, uses tfr[..., ::decim].
        If `slice`, uses tfr[..., decim].

    #### `projs : list of Projection | None`
        List of projectors to store in the CSD object. Defaults to ``None``,
        which means the projectors defined in the Epochs object will be copied.
    #### `n_jobs : int | None`
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `csd : instance of CrossSpectralDensity`
        The computed cross-spectral density.

    -----
    ### 👉 See Also

    csd_array_fourier
    csd_array_morlet
    csd_array_multitaper
    csd_fourier
    csd_multitaper
    """
    ...

def csd_array_morlet(
    X,
    sfreq,
    frequencies,
    t0: int = 0,
    tmin=None,
    tmax=None,
    ch_names=None,
    n_cycles: int = 7,
    use_fft: bool = True,
    decim: int = 1,
    projs=None,
    n_jobs=None,
    *,
    verbose=None,
):
    """## 🧠 Estimate cross-spectral density from an array using Morlet wavelets.

    -----
    ### 🛠️ Parameters

    X : array-like, shape (n_epochs, n_channels, n_times)
        The time series data consisting of n_epochs separate observations
        of signals with n_channels time-series of length n_times.
    #### `sfreq : float`
        Sampling frequency of observations.
    #### `frequencies : list of float`
        The frequencies of interest, in Hertz.
    t0 : float
        Time of the first sample relative to the onset of the epoch, in
        seconds. Defaults to 0.
    #### `tmin : float | None`
        Minimum time instant to consider, in seconds. If ``None`` start at
        first sample.
    #### `tmax : float | None`
        Maximum time instant to consider, in seconds. If ``None`` end at last
        sample.
    #### `ch_names : list of str | None`
        A name for each time series. If ``None`` (the default), the series will
        be named 'SERIES###'.
    #### `n_cycles : float | list of float | None`
        Number of cycles to use when constructing Morlet wavelets. Fixed number
        or one per frequency. Defaults to 7.
    #### `use_fft : bool`
        Whether to use FFT-based convolution to compute the wavelet transform.
        Defaults to True.
    #### `decim : int | slice`
        To reduce memory usage, decimation factor during time-frequency
        decomposition. Defaults to 1 (no decimation).

        If `int`, uses tfr[..., ::decim].
        If `slice`, uses tfr[..., decim].

    #### `projs : list of Projection | None`
        List of projectors to store in the CSD object. Defaults to ``None``,
        which means the projectors defined in the Epochs object will be copied.
    #### `n_jobs : int | None`
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `csd : instance of CrossSpectralDensity`
        The computed cross-spectral density.

    -----
    ### 👉 See Also

    csd_array_fourier
    csd_array_multitaper
    csd_fourier
    csd_morlet
    csd_multitaper
    """
    ...

def csd_tfr(epochs_tfr, tmin=None, tmax=None, picks=None, projs=None, verbose=None):
    """## 🧠 Compute covariance matrices across frequencies for TFR epochs.

    -----
    ### 🛠️ Parameters

    #### `epochs_tfr : EpochsTFR`
        The time-frequency resolved epochs over which to compute the
        covariance.
    #### `tmin : float | None`
        Minimum time instant to consider, in seconds. If ``None`` start at
        first sample.
    #### `tmax : float | None`
        Maximum time instant to consider, in seconds. If ``None`` end at last
        sample.
    #### `picks : str | array-like | slice | None`
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick good data channels (excluding reference
        MEG channels). Note that channels in ``info['bads']`` *will be included* if
        their names or indices are explicitly provided.
    #### `projs : list of Projection | None`
        List of projectors to store in the CSD object. Defaults to ``None``,
        which means the projectors defined in the EpochsTFR object will be
        copied.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `res : instance of CrossSpectralDensity`
        Cross-spectral density restricted to selected channels.
    """
    ...
