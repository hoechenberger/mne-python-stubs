from ..filter import next_fast_len as next_fast_len
from ..fixes import jit as jit
from ..utils import ProgressBar as ProgressBar, logger as logger, warn as warn
from .base import BaseEstimator as BaseEstimator
from _typeshed import Incomplete

class TimeDelayingRidge(BaseEstimator):
    """Predict the output.

        Parameters
        ----------
        X : array, shape (n_samples[, n_epochs], n_features)
            The data.

        Returns
        -------
        X : ndarray
            The predicted response.
        """
    tmin: Incomplete
    tmax: Incomplete
    sfreq: Incomplete
    alpha: Incomplete
    reg_type: Incomplete
    fit_intercept: Incomplete
    edge_correction: Incomplete
    n_jobs: Incomplete

    def __init__(self, tmin, tmax, sfreq, alpha: float=..., reg_type: str=..., fit_intercept: bool=..., n_jobs: Incomplete | None=..., edge_correction: bool=...) -> None:
        ...
    coef_: Incomplete
    intercept_: Incomplete

    def fit(self, X, y):
        """Estimate the coefficients of the linear model.

        Parameters
        ----------
        X : array, shape (n_samples[, n_epochs], n_features)
            The training input samples to estimate the linear coefficients.
        y : array, shape (n_samples[, n_epochs],  n_outputs)
            The target values.

        Returns
        -------
        self : instance of TimeDelayingRidge
            Returns the modified instance.
        """

    def predict(self, X):
        """Predict the output.

        Parameters
        ----------
        X : array, shape (n_samples[, n_epochs], n_features)
            The data.

        Returns
        -------
        X : ndarray
            The predicted response.
        """