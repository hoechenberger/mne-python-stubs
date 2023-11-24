from ..cov import Covariance as Covariance
from ..filter import filter_data as filter_data
from ..fixes import BaseEstimator as BaseEstimator
from ..rank import compute_rank as compute_rank
from ..time_frequency import psd_array_welch as psd_array_welch
from ..utils import fill_doc as fill_doc, logger as logger
from .mixin import TransformerMixin as TransformerMixin
from _typeshed import Incomplete

class SSD(BaseEstimator, TransformerMixin):
    """Remove selected components from the signal.

        This procedure will reconstruct M/EEG signals from which the dynamics
        described by the excluded components is subtracted
        (denoised by low-rank factorization).
        See :footcite:`HaufeEtAl2014b` for more information.

        .. note:: Unlike in other classes with an apply method,
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

    def __init__(self, info, filt_params_signal, filt_params_noise, reg: Incomplete | None=..., n_components: Incomplete | None=..., picks: Incomplete | None=..., sort_by_spectral_ratio: bool=..., return_filtered: bool=..., n_fft: Incomplete | None=..., cov_method_params: Incomplete | None=..., rank: Incomplete | None=...) -> None:
        """Initialize instance."""
    eigvals_: Incomplete
    filters_: Incomplete
    patterns_: Incomplete
    sorter_spec: Incomplete

    def fit(self, X, y: Incomplete | None=...):
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

    def inverse_transform(self) -> None:
        """Not implemented yet."""

    def apply(self, X):
        """Remove selected components from the signal.

        This procedure will reconstruct M/EEG signals from which the dynamics
        described by the excluded components is subtracted
        (denoised by low-rank factorization).
        See :footcite:`HaufeEtAl2014b` for more information.

        .. note:: Unlike in other classes with an apply method,
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