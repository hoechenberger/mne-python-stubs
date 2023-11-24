from .._fiff.pick import pick_info as pick_info, pick_types as pick_types
from ..filter import filter_data as filter_data
from ..time_frequency import psd_array_multitaper as psd_array_multitaper
from ..utils import fill_doc as fill_doc, verbose as verbose
from .base import BaseEstimator as BaseEstimator
from .mixin import TransformerMixin as TransformerMixin
from _typeshed import Incomplete

class _ConstantScaler:
    """Scale channel types using constant values."""

    def __init__(self, info, scalings, do_scaling: bool=...) -> None:
        ...
    std_: Incomplete
    mean_: Incomplete

    def fit(self, X, y: Incomplete | None=...):
        ...

    def transform(self, X):
        ...

    def inverse_transform(self, X, y: Incomplete | None=...):
        ...

    def fit_transform(self, X, y: Incomplete | None=...):
        ...

class Scaler(TransformerMixin, BaseEstimator):
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
    info: Incomplete
    with_mean: Incomplete
    with_std: Incomplete
    scalings: Incomplete

    def __init__(self, info: Incomplete | None=..., scalings: Incomplete | None=..., with_mean: bool=..., with_std: bool=...) -> None:
        ...

    def fit(self, epochs_data, y: Incomplete | None=...):
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

    def fit_transform(self, epochs_data, y: Incomplete | None=...):
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

class Vectorizer(TransformerMixin):
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
    features_shape_: Incomplete

    def fit(self, X, y: Incomplete | None=...):
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

    def fit_transform(self, X, y: Incomplete | None=...):
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

class PSDEstimator(TransformerMixin):
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
    sfreq: Incomplete
    fmin: Incomplete
    fmax: Incomplete
    bandwidth: Incomplete
    adaptive: Incomplete
    low_bias: Incomplete
    n_jobs: Incomplete
    normalization: Incomplete

    def __init__(self, sfreq=..., fmin: int=..., fmax=..., bandwidth: Incomplete | None=..., adaptive: bool=..., low_bias: bool=..., n_jobs: Incomplete | None=..., normalization: str=..., *, verbose: Incomplete | None=...) -> None:
        ...

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

class FilterEstimator(TransformerMixin):
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

    def __init__(self, info, l_freq, h_freq, picks: Incomplete | None=..., filter_length: str=..., l_trans_bandwidth: str=..., h_trans_bandwidth: str=..., n_jobs: Incomplete | None=..., method: str=..., iir_params: Incomplete | None=..., fir_design: str=..., *, verbose: Incomplete | None=...) -> None:
        ...

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

class UnsupervisedSpatialFilter(TransformerMixin, BaseEstimator):
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
    estimator: Incomplete
    average: Incomplete

    def __init__(self, estimator, average: bool=...) -> None:
        ...

    def fit(self, X, y: Incomplete | None=...):
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

    def fit_transform(self, X, y: Incomplete | None=...):
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

class TemporalFilter(TransformerMixin):
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

    def __init__(self, l_freq: Incomplete | None=..., h_freq: Incomplete | None=..., sfreq: float=..., filter_length: str=..., l_trans_bandwidth: str=..., h_trans_bandwidth: str=..., n_jobs: Incomplete | None=..., method: str=..., iir_params: Incomplete | None=..., fir_window: str=..., fir_design: str=..., *, verbose: Incomplete | None=...) -> None:
        ...

    def fit(self, X, y: Incomplete | None=...):
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