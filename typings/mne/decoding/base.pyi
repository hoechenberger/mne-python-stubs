from ..fixes import BaseEstimator as BaseEstimator
from ..parallel import parallel_func as parallel_func
from ..utils import warn as warn
from _typeshed import Incomplete

class LinearModel(BaseEstimator):
    """Estimate the coefficients of the linear model.

    Save the coefficients in the attribute ``filters_`` and
    computes the attribute ``patterns_``.

    Parameters
    ----------
    X : array, shape (n_samples, n_features)
        The training input samples to estimate the linear coefficients.
    y : array, shape (n_samples, [n_targets])
        The target values.
    **fit_params : dict of string -> object
        Parameters to pass to the fit method of the estimator.

    Returns
    -------
    self : instance of LinearModel
        Returns the modified instance.
    """

    model: Incomplete

    def __init__(self, model=...) -> None: ...
    def __getattr__(self, attr):
        """Wrap to model for some attributes."""
    patterns_: Incomplete

    def fit(self, X, y, **fit_params):
        """Estimate the coefficients of the linear model.

        Save the coefficients in the attribute ``filters_`` and
        computes the attribute ``patterns_``.

        Parameters
        ----------
        X : array, shape (n_samples, n_features)
            The training input samples to estimate the linear coefficients.
        y : array, shape (n_samples, [n_targets])
            The target values.
        **fit_params : dict of string -> object
            Parameters to pass to the fit method of the estimator.

        Returns
        -------
        self : instance of LinearModel
            Returns the modified instance.
        """
    @property
    def filters_(self): ...

def get_coef(estimator, attr: str = ..., inverse_transform: bool = ...):
    """Retrieve the coefficients of an estimator ending with a Linear Model.

    This is typically useful to retrieve "spatial filters" or "spatial
    patterns" of decoding models :footcite:`HaufeEtAl2014`.

    Parameters
    ----------
    estimator : object | None
        An estimator from scikit-learn.
    attr : str
        The name of the coefficient attribute to retrieve, typically
        ``'filters_'`` (default) or ``'patterns_'``.
    inverse_transform : bool
        If True, returns the coefficients after inverse transforming them with
        the transformer steps of the estimator.

    Returns
    -------
    coef : array
        The coefficients.

    References
    ----------
    .. footbibliography::
    """

def cross_val_multiscore(
    estimator,
    X,
    y=...,
    groups=...,
    scoring=...,
    cv=...,
    n_jobs=...,
    verbose=...,
    fit_params=...,
    pre_dispatch: str = ...,
):
    """Evaluate a score by cross-validation.

    Parameters
    ----------
    estimator : instance of sklearn.base.BaseEstimator
        The object to use to fit the data.
        Must implement the 'fit' method.
    X : array-like, shape (n_samples, n_dimensional_features,)
        The data to fit. Can be, for example a list, or an array at least 2d.
    y : array-like, shape (n_samples, n_targets,)
        The target variable to try to predict in the case of
        supervised learning.
    groups : array-like, with shape (n_samples,)
        Group labels for the samples used while splitting the dataset into
        train/test set.
    scoring : str, callable | None
        A string (see model evaluation documentation) or
        a scorer callable object / function with signature
        ``scorer(estimator, X, y)``.
        Note that when using an estimator which inherently returns
        multidimensional output - in particular, SlidingEstimator
        or GeneralizingEstimator - you should set the scorer
        there, not here.
    cv : int, cross-validation generator | iterable
        Determines the cross-validation splitting strategy.
        Possible inputs for cv are:

        - None, to use the default 5-fold cross validation,
        - integer, to specify the number of folds in a ``(Stratified)KFold``,
        - An object to be used as a cross-validation generator.
        - An iterable yielding train, test splits.

        For integer/None inputs, if the estimator is a classifier and ``y`` is
        either binary or multiclass,
        :class:`sklearn.model_selection.StratifiedKFold` is used. In all
        other cases, :class:`sklearn.model_selection.KFold` is used.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the :mod:`joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a :class:`joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.
    fit_params : dict, optional
        Parameters to pass to the fit method of the estimator.
    pre_dispatch : int, or str, optional
        Controls the number of jobs that get dispatched during parallel
        execution. Reducing this number can be useful to avoid an
        explosion of memory consumption when more jobs get dispatched
        than CPUs can process. This parameter can be:

        - None, in which case all the jobs are immediately
          created and spawned. Use this for lightweight and
          fast-running jobs, to avoid delays due to on-demand
          spawning of the jobs
        - An int, giving the exact number of total jobs that are
          spawned
        - A string, giving an expression as a function of n_jobs,
          as in '2*n_jobs'

    Returns
    -------
    scores : array of float, shape (n_splits,) | shape (n_splits, n_scores)
        Array of scores of the estimator for each run of the cross validation.
    """