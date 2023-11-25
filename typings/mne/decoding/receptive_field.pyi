from ..fixes import pinv as pinv
from ..utils import fill_doc as fill_doc
from .base import BaseEstimator as BaseEstimator, get_coef as get_coef
from .time_delaying_ridge import TimeDelayingRidge as TimeDelayingRidge
from _typeshed import Incomplete

class ReceptiveField(BaseEstimator):
    """Score predictions generated with a receptive field.

    This calls ``self.predict``, then masks the output of this
    and ``y` with ``self.valid_samples_``. Finally, it passes
    this to a :mod:`sklearn.metrics` scorer.

    Parameters
    ----------
    X : array, shape (n_times[, n_epochs], n_channels)
        The input features for the model.
    y : array, shape (n_times[, n_epochs][, n_outputs])
        Used for scikit-learn compatibility.

    Returns
    -------
    scores : list of float, shape (n_outputs,)
        The scores estimated by the model for each output (e.g. mean
        R2 of ``predict(X)``).
    """

    feature_names: Incomplete
    sfreq: Incomplete
    tmin: Incomplete
    tmax: Incomplete
    estimator: Incomplete
    fit_intercept: Incomplete
    scoring: Incomplete
    patterns: Incomplete
    n_jobs: Incomplete
    edge_correction: Incomplete

    def __init__(
        self,
        tmin,
        tmax,
        sfreq,
        feature_names=...,
        estimator=...,
        fit_intercept=...,
        scoring: str = ...,
        patterns: bool = ...,
        n_jobs=...,
        edge_correction: bool = ...,
        verbose=...,
    ) -> None: ...
    delays_: Incomplete
    valid_samples_: Incomplete
    fit_intercept_: bool
    estimator_: Incomplete
    coef_: Incomplete
    patterns_: Incomplete

    def fit(self, X, y):
        """Fit a receptive field model.

        Parameters
        ----------
        X : array, shape (n_times[, n_epochs], n_features)
            The input features for the model.
        y : array, shape (n_times[, n_epochs][, n_outputs])
            The output features for the model.

        Returns
        -------
        self : instance
            The instance so you can chain operations.
        """
    def predict(self, X):
        """Generate predictions with a receptive field.

        Parameters
        ----------
        X : array, shape (n_times[, n_epochs], n_channels)
            The input features for the model.

        Returns
        -------
        y_pred : array, shape (n_times[, n_epochs][, n_outputs])
            The output predictions. "Note that valid samples (those
            unaffected by edge artifacts during the time delaying step) can
            be obtained using ``y_pred[rf.valid_samples_]``.
        """
    def score(self, X, y):
        """Score predictions generated with a receptive field.

        This calls ``self.predict``, then masks the output of this
        and ``y` with ``self.valid_samples_``. Finally, it passes
        this to a :mod:`sklearn.metrics` scorer.

        Parameters
        ----------
        X : array, shape (n_times[, n_epochs], n_channels)
            The input features for the model.
        y : array, shape (n_times[, n_epochs][, n_outputs])
            Used for scikit-learn compatibility.

        Returns
        -------
        scores : list of float, shape (n_outputs,)
            The scores estimated by the model for each output (e.g. mean
            R2 of ``predict(X)``).
        """
