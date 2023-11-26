from ..utils import fill_doc as fill_doc
from .base import BaseEstimator as BaseEstimator
from .mixin import TransformerMixin as TransformerMixin
from _typeshed import Incomplete

class TimeFrequency(TransformerMixin, BaseEstimator):
    """### Time frequency transformer.

    Time-frequency transform of times series along the last axis.

    -----
    ### 🛠️ Parameters

    freqs : array-like of float, shape (n_freqs,)
        The frequencies.
    sfreq : float | int, default 1.0
        Sampling frequency of the data.
    method : 'multitaper' | 'morlet', default 'morlet'
        The time-frequency method. 'morlet' convolves a Morlet wavelet.
        'multitaper' uses Morlet wavelets windowed with multiple DPSS
        multitapers.
    n_cycles : float | array of float, default 7.0
        Number of cycles  in the Morlet wavelet. Fixed number
        or one per frequency.
    time_bandwidth : float, default None
        If None and method=multitaper, will be set to 4.0 (3 tapers).
        Time x (Full) Bandwidth product. Only applies if
        method == 'multitaper'. The number of good tapers (low-bias) is
        chosen automatically based on this to equal floor(time_bandwidth - 1).
    use_fft : bool, default True
        Use the FFT for convolutions or not.
    decim : int | slice, default 1
        To reduce memory usage, decimation factor after time-frequency
        decomposition.
        If `int`, returns tfr[..., ::decim].
        If `slice`, returns tfr[..., decim].

        ### 💡 Note Decimation may create aliasing artifacts, yet decimation
                  is done after the convolutions.

    output : str, default 'complex'
        * 'complex' : single trial complex.
        * 'power' : single trial power.
        * 'phase' : single trial phase.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.
        The number of epochs to process at the same time. The parallelization
        is implemented across channels.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### 👉 See Also

    mne.time_frequency.tfr_morlet
    mne.time_frequency.tfr_multitaper
    """

    freqs: Incomplete
    sfreq: Incomplete
    method: Incomplete
    n_cycles: Incomplete
    time_bandwidth: Incomplete
    use_fft: Incomplete
    decim: Incomplete
    output: Incomplete
    n_jobs: Incomplete
    verbose: Incomplete

    def __init__(
        self,
        freqs,
        sfreq: float = 1.0,
        method: str = "morlet",
        n_cycles: float = 7.0,
        time_bandwidth=None,
        use_fft: bool = True,
        decim: int = 1,
        output: str = "complex",
        n_jobs: int = 1,
        verbose=None,
    ) -> None:
        """### Init TimeFrequency transformer."""
        ...
    def fit_transform(self, X, y=None):
        """### Time-frequency transform of times series along the last axis.

        -----
        ### 🛠️ Parameters

        X : array, shape (n_samples, n_channels, n_times)
            The training data samples. The channel dimension can be zero- or
            1-dimensional.
        y : None
            For scikit-learn compatibility purposes.

        -----
        ### ⏎ Returns

        Xt : array, shape (n_samples, n_channels, n_freqs, n_times)
            The time-frequency transform of the data, where n_channels can be
            zero- or 1-dimensional.
        """
        ...
    def fit(self, X, y=None):
        """### Do nothing (for scikit-learn compatibility purposes).

        -----
        ### 🛠️ Parameters

        X : array, shape (n_samples, n_channels, n_times)
            The training data.
        y : array | None
            The target values.

        -----
        ### ⏎ Returns

        self : object
            Return self.
        """
        ...
    def transform(self, X):
        """### Time-frequency transform of times series along the last axis.

        -----
        ### 🛠️ Parameters

        X : array, shape (n_samples, n_channels, n_times)
            The training data samples. The channel dimension can be zero- or
            1-dimensional.

        -----
        ### ⏎ Returns

        Xt : array, shape (n_samples, n_channels, n_freqs, n_times)
            The time-frequency transform of the data, where n_channels can be
            zero- or 1-dimensional.
        """
        ...
