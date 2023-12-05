from ..cov import Covariance as Covariance
from ..filter import filter_data as filter_data
from ..fixes import BaseEstimator as BaseEstimator
from ..rank import compute_rank as compute_rank
from ..time_frequency import psd_array_welch as psd_array_welch
from ..utils import fill_doc as fill_doc, logger as logger
from .mixin import TransformerMixin as TransformerMixin
from _typeshed import Incomplete

class SSD(BaseEstimator, TransformerMixin):
    """
    Signal decomposition using the Spatio-Spectral Decomposition (SSD).

    SSD seeks to maximize the power at a frequency band of interest while
    simultaneously minimizing it at the flanking (surrounding) frequency bins
    (considered noise). It extremizes the covariance matrices associated with
    signal and noise :footcite:`NikulinEtAl2011`.

    SSD can either be used as a dimensionality reduction method or a
    ‘denoised’ low rank factorization method :footcite:`HaufeEtAl2014b`.

    Parameters
    ----------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement. Must match the input data.
    filt_params_signal : dict
        Filtering for the frequencies of interest.
    filt_params_noise : dict
        Filtering for the frequencies of non-interest.
    reg : float | str | None (default)
        Which covariance estimator to use.
        If not None (same as 'empirical'), allow regularization for covariance
        estimation. If float, shrinkage is used (0 <= shrinkage <= 1). For str
        options, reg will be passed to method `mne.compute_covariance`.
    n_components : int | None (default None)
        The number of components to extract from the signal.
        If None, the number of components equal to the rank of the data are
        returned (see ``rank``).
    picks : array of int | None (default None)
        The indices of good channels.
    sort_by_spectral_ratio : bool (default True)
        If set to True, the components are sorted according to the spectral
        ratio.
        See Eq. (24) in :footcite:`NikulinEtAl2011`.
    return_filtered : bool (default False)
        If return_filtered is True, data is bandpassed and projected onto the
        SSD components.
    n_fft : int (default None)
       If sort_by_spectral_ratio is set to True, then the SSD sources will be
       sorted according to their spectral ratio which is calculated based on
       `mne.time_frequency.psd_array_welch`. The n_fft parameter sets the
       length of FFT used.
       See `mne.time_frequency.psd_array_welch` for more information.
    cov_method_params : dict | None (default None)
        As in `mne.decoding.SPoC`
        The default is None.
    rank : None | dict | ‘info’ | ‘full’
        As in `mne.decoding.SPoC`
        This controls the rank computation that can be read from the
        measurement info or estimated from the data, which determines the
        maximum possible number of components.
        See Notes of `mne.compute_rank` for details.
        We recommend to use 'full' when working with epoched data.

    Attributes
    ----------
    filters_ : array, shape (n_channels, n_components)
        The spatial filters to be multiplied with the signal.
    patterns_ : array, shape (n_components, n_channels)
        The patterns for reconstructing the signal from the filtered data.

    References
    ----------
    .. footbibliography::
    """

    picks_: Incomplete
    info: Incomplete
    freqs_signal: Incomplete
    freqs_noise: Incomplete
    filt_params_signal: Incomplete
    filt_params_noise: Incomplete
    sort_by_spectral_ratio: Incomplete
    n_fft: Incomplete
    return_filtered: Incomplete
    reg: Incomplete
    n_components: Incomplete
    rank: Incomplete
    cov_method_params: Incomplete

    def __init__(
        self,
        info,
        filt_params_signal,
        filt_params_noise,
        reg=None,
        n_components=None,
        picks=None,
        sort_by_spectral_ratio: bool = True,
        return_filtered: bool = False,
        n_fft=None,
        cov_method_params=None,
        rank=None,
    ) -> None:
        """Initialize instance."""
        ...
    eigvals_: Incomplete
    filters_: Incomplete
    patterns_: Incomplete
    sorter_spec: Incomplete

    def fit(self, X, y=None):
        """Estimate the SSD decomposition on raw or epoched data.

        Parameters
        ----------
        X : array, shape ([n_epochs, ]n_channels, n_times)
            The input data from which to estimate the SSD. Either 2D array
            obtained from continuous data or 3D array obtained from epoched
            data.
        y : None | array, shape (n_samples,)
            Used for scikit-learn compatibility.

        Returns
        -------
        self : instance of SSD
            Returns the modified instance.
        """
        ...

    def transform(self, X):
        """Estimate epochs sources given the SSD filters.

        Parameters
        ----------
        X : array, shape ([n_epochs, ]n_channels, n_times)
            The input data from which to estimate the SSD. Either 2D array
            obtained from continuous data or 3D array obtained from epoched
            data.

        Returns
        -------
        X_ssd : array, shape ([n_epochs, ]n_components, n_times)
            The processed data.
        """
        ...

    def get_spectral_ratio(self, ssd_sources):
        """Get the spectal signal-to-noise ratio for each spatial filter.

        Spectral ratio measure for best n_components selection
        See :footcite:`NikulinEtAl2011`, Eq. (24).

        Parameters
        ----------
        ssd_sources : array
            Data projected to SSD space.

        Returns
        -------
        spec_ratio : array, shape (n_channels)
            Array with the sprectal ratio value for each component.
        sorter_spec : array, shape (n_channels)
            Array of indices for sorting spec_ratio.

        References
        ----------
        .. footbibliography::
        """
        ...

    def inverse_transform(self) -> None:
        """Not implemented yet."""
        ...

    def apply(self, X):
        """Remove selected components from the signal.

        This procedure will reconstruct M/EEG signals from which the dynamics
        described by the excluded components is subtracted
        (denoised by low-rank factorization).
        See :footcite:`HaufeEtAl2014b` for more information.

        💡 Unlike in other classes with an apply method,
           only NumPy arrays are supported (not instances of MNE objects).

        Parameters
        ----------
        X : array, shape ([n_epochs, ]n_channels, n_times)
            The input data from which to estimate the SSD. Either 2D array
            obtained from continuous data or 3D array obtained from epoched
            data.

        Returns
        -------
        X : array, shape ([n_epochs, ]n_channels, n_times)
            The processed data.
        """
        ...
