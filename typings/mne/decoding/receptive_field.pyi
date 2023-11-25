from ..fixes import pinv as pinv
from ..utils import fill_doc as fill_doc
from .base import BaseEstimator as BaseEstimator, get_coef as get_coef
from .time_delaying_ridge import TimeDelayingRidge as TimeDelayingRidge
from _typeshed import Incomplete

class ReceptiveField(BaseEstimator):
    """Fit a receptive field model.

    This allows you to fit an encoding model (stimulus to brain) or a decoding
    model (brain to stimulus) using time-lagged input features (for example, a
    spectro- or spatio-temporal receptive field, or STRF)
    :footcite:`TheunissenEtAl2001,WillmoreSmyth2003,CrosseEtAl2016,HoldgrafEtAl2016`.

    Parameters
    ----------
    tmin : float
        The starting lag, in seconds (or samples if ``sfreq`` == 1).
    tmax : float
        The ending lag, in seconds (or samples if ``sfreq`` == 1).
        Must be >= tmin.
    sfreq : float
        The sampling frequency used to convert times into samples.
    feature_names : array, shape (n_features,) | None
        Names for input features to the model. If None, feature names will
        be auto-generated from the shape of input data after running `fit`.
    estimator : instance of sklearn.base.BaseEstimator | float | None
        The model used in fitting inputs and outputs. This can be any
        scikit-learn-style model that contains a fit and predict method. If a
        float is passed, it will be interpreted as the ``alpha`` parameter
        to be passed to a Ridge regression model. If `None`, then a Ridge
        regression model with an alpha of 0 will be used.
    fit_intercept : bool | None
        If True (default), the sample mean is removed before fitting.
        If ``estimator`` is a :class:`sklearn.base.BaseEstimator`,
        this must be None or match ``estimator.fit_intercept``.
    scoring : ['r2', 'corrcoef']
        Defines how predictions will be scored. Currently must be one of
        'r2' (coefficient of determination) or 'corrcoef' (the correlation
        coefficient).
    patterns : bool
        If True, inverse coefficients will be computed upon fitting using the
        covariance matrix of the inputs, and the cross-covariance of the
        inputs/outputs, according to :footcite:`HaufeEtAl2014`. Defaults to
        False.
    n_jobs : int | str
        Number of jobs to run in parallel. Can be 'cuda' if CuPy
        is installed properly and ``estimator is None``.

        .. versionadded:: 0.18
    edge_correction : bool
        If True (default), correct the autocorrelation coefficients for
        non-zero delays for the fact that fewer samples are available.
        Disabling this speeds up performance at the cost of accuracy
        depending on the relationship between epoch length and model
        duration. Only used if ``estimator`` is float or None.

        .. versionadded:: 0.18

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Attributes
    ----------
    coef_ : array, shape ([n_outputs, ]n_features, n_delays)
        The coefficients from the model fit, reshaped for easy visualization.
        During :meth:`mne.decoding.ReceptiveField.fit`, if ``y`` has one
        dimension (time), the ``n_outputs`` dimension here is omitted.
    patterns_ : array, shape ([n_outputs, ]n_features, n_delays)
        If fit, the inverted coefficients from the model.
    delays_ : array, shape (n_delays,), dtype int
        The delays used to fit the model, in indices. To return the delays
        in seconds, use ``self.delays_ / self.sfreq``
    valid_samples_ : slice
        The rows to keep during model fitting after removing rows with
        missing values due to time delaying. This can be used to get an
        output equivalent to using :func:`numpy.convolve` or
        :func:`numpy.correlate` with ``mode='valid'``.

    See Also
    --------
    mne.decoding.TimeDelayingRidge

    Notes
    -----
    For a causal system, the encoding model will have significant
    non-zero values only at positive lags. In other words, lags point
    backward in time relative to the input, so positive lags correspond
    to previous input time samples, while negative lags correspond to
    future input time samples.

    References
    ----------
    .. footbibliography::
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
        feature_names=None,
        estimator=None,
        fit_intercept=None,
        scoring: str = "r2",
        patterns: bool = False,
        n_jobs=None,
        edge_correction: bool = True,
        verbose=None,
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
        ...
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
        ...
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
        ...
