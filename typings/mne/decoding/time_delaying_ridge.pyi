from ..filter import next_fast_len as next_fast_len
from ..fixes import jit as jit
from ..utils import ProgressBar as ProgressBar, logger as logger, warn as warn
from .base import BaseEstimator as BaseEstimator
from _typeshed import Incomplete

class TimeDelayingRidge(BaseEstimator):
    """Ridge regression of data with time delays.

    Parameters
    ----------
    tmin : int | float
        The starting lag, in seconds (or samples if ``sfreq`` == 1).
        Negative values correspond to times in the past.
    tmax : int | float
        The ending lag, in seconds (or samples if ``sfreq`` == 1).
        Positive values correspond to times in the future.
        Must be >= tmin.
    sfreq : float
        The sampling frequency used to convert times into samples.
    alpha : float
        The ridge (or laplacian) regularization factor.
    reg_type : str | list
        Can be ``"ridge"`` (default) or ``"laplacian"``.
        Can also be a 2-element list specifying how to regularize in time
        and across adjacent features.
    fit_intercept : bool
        If True (default), the sample mean is removed before fitting.
    n_jobs : int | str
        The number of jobs to use. Can be an int (default 1) or ``'cuda'``.

        .. versionadded:: 0.18
    edge_correction : bool
        If True (default), correct the autocorrelation coefficients for
        non-zero delays for the fact that fewer samples are available.
        Disabling this speeds up performance at the cost of accuracy
        depending on the relationship between epoch length and model
        duration. Only used if ``estimator`` is float or None.

        .. versionadded:: 0.18

    See Also
    --------
    mne.decoding.ReceptiveField

    Notes
    -----
    This class is meant to be used with `mne.decoding.ReceptiveField`
    by only implicitly doing the time delaying. For reasonable receptive
    field and input signal sizes, it should be more CPU and memory
    efficient by using frequency-domain methods (FFTs) to compute the
    auto- and cross-correlations.
    """

    tmin: Incomplete
    tmax: Incomplete
    sfreq: Incomplete
    alpha: Incomplete
    reg_type: Incomplete
    fit_intercept: Incomplete
    edge_correction: Incomplete
    n_jobs: Incomplete

    def __init__(
        self,
        tmin,
        tmax,
        sfreq,
        alpha: float = 0.0,
        reg_type: str = "ridge",
        fit_intercept: bool = True,
        n_jobs=None,
        edge_correction: bool = True,
    ) -> None: ...
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
        ...
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
        ...
