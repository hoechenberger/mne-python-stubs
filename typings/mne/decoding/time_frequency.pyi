from ..utils import fill_doc as fill_doc, verbose as verbose
from .base import BaseEstimator as BaseEstimator
from .mixin import TransformerMixin as TransformerMixin
from _typeshed import Incomplete

class TimeFrequency(TransformerMixin, BaseEstimator):
    """Time-frequency transform of times series along the last axis.

        Parameters
        ----------
        X : array, shape (n_samples, n_channels, n_times)
            The training data samples. The channel dimension can be zero- or
            1-dimensional.

        Returns
        -------
        Xt : array, shape (n_samples, n_channels, n_freqs, n_times)
            The time-frequency transform of the data, where n_channels can be
            zero- or 1-dimensional.
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

    def __init__(self, freqs, sfreq: float=..., method: str=..., n_cycles: float=..., time_bandwidth: Incomplete | None=..., use_fft: bool=..., decim: int=..., output: str=..., n_jobs: int=..., verbose: Incomplete | None=...) -> None:
        """Init TimeFrequency transformer."""

    def fit_transform(self, X, y: Incomplete | None=...):
        """Time-frequency transform of times series along the last axis.

        Parameters
        ----------
        X : array, shape (n_samples, n_channels, n_times)
            The training data samples. The channel dimension can be zero- or
            1-dimensional.
        y : None
            For scikit-learn compatibility purposes.

        Returns
        -------
        Xt : array, shape (n_samples, n_channels, n_freqs, n_times)
            The time-frequency transform of the data, where n_channels can be
            zero- or 1-dimensional.
        """

    def fit(self, X, y: Incomplete | None=...):
        """Do nothing (for scikit-learn compatibility purposes).

        Parameters
        ----------
        X : array, shape (n_samples, n_channels, n_times)
            The training data.
        y : array | None
            The target values.

        Returns
        -------
        self : object
            Return self.
        """

    def transform(self, X):
        """Time-frequency transform of times series along the last axis.

        Parameters
        ----------
        X : array, shape (n_samples, n_channels, n_times)
            The training data samples. The channel dimension can be zero- or
            1-dimensional.

        Returns
        -------
        Xt : array, shape (n_samples, n_channels, n_freqs, n_times)
            The time-frequency transform of the data, where n_channels can be
            zero- or 1-dimensional.
        """