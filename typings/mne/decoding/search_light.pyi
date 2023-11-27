from ..parallel import parallel_func as parallel_func
from ..utils import (
    ProgressBar as ProgressBar,
    array_split_idx as array_split_idx,
    fill_doc as fill_doc,
)
from .base import BaseEstimator as BaseEstimator
from .mixin import TransformerMixin as TransformerMixin
from _typeshed import Incomplete

class SlidingEstimator(BaseEstimator, TransformerMixin):
    """## Search Light.

    Fit, predict and score a series of models to each subset of the dataset
    along the last dimension. Each entry in the last dimension is referred
    to as a task.

    -----
    ### 🛠️ Parameters


    #### `base_estimator : object`
        The base estimator to iteratively fit on a subset of the dataset.

    #### `scoring : callable | str | None`
        Score function (or loss function) with signature
        ``score_func(y, y_pred, **kwargs)``.
        Note that the "predict" method is automatically identified if scoring is
        a string (e.g. ``scoring='roc_auc'`` calls ``predict_proba``), but is
        `not`  automatically set if ``scoring`` is a callable (e.g.
        ``scoring=sklearn.metrics.roc_auc_score``).
    #### `n_jobs : int | None`
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.

    #### `position : int`
        The position for the progress bar.

    allow_2d : bool
        If True, allow 2D data as input (i.e. n_samples, n_features).

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### 📊 Attributes

    #### `estimators_ : array-like, shape (n_tasks,)`
        List of fitted scikit-learn estimators (one per task).
    """

    base_estimator: Incomplete
    n_jobs: Incomplete
    scoring: Incomplete
    position: Incomplete
    allow_2d: Incomplete
    verbose: Incomplete

    def __init__(
        self,
        base_estimator,
        scoring=None,
        n_jobs=None,
        *,
        position: int = 0,
        allow_2d: bool = False,
        verbose=None,
    ) -> None: ...
    estimators_: Incomplete
    fit_params_: Incomplete

    def fit(self, X, y, **fit_params):
        """## Fit a series of independent estimators to the dataset.

        -----
        ### 🛠️ Parameters

        X : array, shape (n_samples, nd_features, n_tasks)
            The training input samples. For each data slice, a clone estimator
            is fitted independently. The feature dimension can be
            multidimensional e.g.
            X.shape = (n_samples, n_features_1, n_features_2, n_tasks).
        #### `y : array, shape (n_samples,) | (n_samples, n_targets)`
            The target values.
        **fit_params : dict of string -> object
            Parameters to pass to the fit method of the estimator.

        -----
        ### ⏎ Returns

        #### `self : object`
            Return self.
        """
        ...
    def fit_transform(self, X, y, **fit_params):
        """## Fit and transform a series of independent estimators to the dataset.

        -----
        ### 🛠️ Parameters

        X : array, shape (n_samples, nd_features, n_tasks)
            The training input samples. For each task, a clone estimator
            is fitted independently. The feature dimension can be
            multidimensional, e.g.::

                X.shape = (n_samples, n_features_1, n_features_2, n_estimators)
        #### `y : array, shape (n_samples,) | (n_samples, n_targets)`
            The target values.
        **fit_params : dict of string -> object
            Parameters to pass to the fit method of the estimator.

        -----
        ### ⏎ Returns

        #### `y_pred : array, shape (n_samples, n_tasks) | (n_samples, n_tasks, n_targets)`
            The predicted values for each estimator.
        """
        ...
    def transform(self, X):
        """## Transform each data slice/task with a series of independent estimators.

        The number of tasks in X should match the number of tasks/estimators
        given at fit time.

        -----
        ### 🛠️ Parameters

        X : array, shape (n_samples, nd_features, n_tasks)
            The input samples. For each data slice/task, the corresponding
            estimator makes a transformation of the data, e.g.
            ``[estimators[ii].transform(X[..., ii]) for ii in range(n_estimators)]``.
            The feature dimension can be multidimensional e.g.
            X.shape = (n_samples, n_features_1, n_features_2, n_tasks).

        -----
        ### ⏎ Returns

        Xt : array, shape (n_samples, n_estimators)
            The transformed values generated by each estimator.
        """
        ...
    def predict(self, X):
        """## Predict each data slice/task with a series of independent estimators.

        The number of tasks in X should match the number of tasks/estimators
        given at fit time.

        -----
        ### 🛠️ Parameters

        X : array, shape (n_samples, nd_features, n_tasks)
            The input samples. For each data slice, the corresponding estimator
            makes the sample predictions, e.g.:
            ``[estimators[ii].predict(X[..., ii]) for ii in range(n_estimators)]``.
            The feature dimension can be multidimensional e.g.
            X.shape = (n_samples, n_features_1, n_features_2, n_tasks).

        -----
        ### ⏎ Returns

        #### `y_pred : array, shape (n_samples, n_estimators) | (n_samples, n_tasks, n_targets)`
            Predicted values for each estimator/data slice.
        """
        ...
    def predict_proba(self, X):
        """## Predict each data slice with a series of independent estimators.

        The number of tasks in X should match the number of tasks/estimators
        given at fit time.

        -----
        ### 🛠️ Parameters

        X : array, shape (n_samples, nd_features, n_tasks)
            The input samples. For each data slice, the corresponding estimator
            makes the sample probabilistic predictions, e.g.:
            ``[estimators[ii].predict_proba(X[..., ii]) for ii in range(n_estimators)]``.
            The feature dimension can be multidimensional e.g.
            X.shape = (n_samples, n_features_1, n_features_2, n_tasks).

        -----
        ### ⏎ Returns

        #### `y_pred : array, shape (n_samples, n_tasks, n_classes)`
            Predicted probabilities for each estimator/data slice/task.
        """
        ...
    def decision_function(self, X):
        """## Estimate distances of each data slice to the hyperplanes.

        -----
        ### 🛠️ Parameters

        X : array, shape (n_samples, nd_features, n_tasks)
            The input samples. For each data slice, the corresponding estimator
            outputs the distance to the hyperplane, e.g.:
            ``[estimators[ii].decision_function(X[..., ii]) for ii in range(n_estimators)]``.
            The feature dimension can be multidimensional e.g.
            X.shape = (n_samples, n_features_1, n_features_2, n_estimators).

        -----
        ### ⏎ Returns

        #### `y_pred : array, shape (n_samples, n_estimators, n_classes * (n_classes-1) // 2)`
            Predicted distances for each estimator/data slice.

        -----
        ### 📖 Notes

        This requires base_estimator to have a ``decision_function`` method.
        """
        ...
    def score(self, X, y):
        """## Score each estimator on each task.

        The number of tasks in X should match the number of tasks/estimators
        given at fit time, i.e. we need
        ``X.shape[-1] == len(self.estimators_)``.

        -----
        ### 🛠️ Parameters

        X : array, shape (n_samples, nd_features, n_tasks)
            The input samples. For each data slice, the corresponding estimator
            scores the prediction, e.g.:
            ``[estimators[ii].score(X[..., ii], y) for ii in range(n_estimators)]``.
            The feature dimension can be multidimensional e.g.
            X.shape = (n_samples, n_features_1, n_features_2, n_tasks).
        #### `y : array, shape (n_samples,) | (n_samples, n_targets)`
            The target values.

        -----
        ### ⏎ Returns

        #### `score : array, shape (n_samples, n_estimators)`
            Score for each estimator/task.
        """
        ...
    @property
    def classes_(self): ...

class GeneralizingEstimator(SlidingEstimator):
    """## Generalization Light.

    Fit a search-light along the last dimension and use them to apply a
    systematic cross-tasks generalization.

    -----
    ### 🛠️ Parameters


    #### `base_estimator : object`
        The base estimator to iteratively fit on a subset of the dataset.

    #### `scoring : callable | str | None`
        Score function (or loss function) with signature
        ``score_func(y, y_pred, **kwargs)``.
        Note that the "predict" method is automatically identified if scoring is
        a string (e.g. ``scoring='roc_auc'`` calls ``predict_proba``), but is
        `not`  automatically set if ``scoring`` is a callable (e.g.
        ``scoring=sklearn.metrics.roc_auc_score``).
    #### `n_jobs : int | None`
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.

    #### `position : int`
        The position for the progress bar.

    allow_2d : bool
        If True, allow 2D data as input (i.e. n_samples, n_features).

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.
    """

    def transform(self, X):
        """## Transform each data slice with all possible estimators.

        -----
        ### 🛠️ Parameters

        X : array, shape (n_samples, nd_features, n_slices)
            The input samples. For estimator the corresponding data slice is
            used to make a transformation. The feature dimension can be
            multidimensional e.g.
            X.shape = (n_samples, n_features_1, n_features_2, n_estimators).

        -----
        ### ⏎ Returns

        Xt : array, shape (n_samples, n_estimators, n_slices)
            The transformed values generated by each estimator.
        """
        ...
    def predict(self, X):
        """## Predict each data slice with all possible estimators.

        -----
        ### 🛠️ Parameters

        X : array, shape (n_samples, nd_features, n_slices)
            The training input samples. For each data slice, a fitted estimator
            predicts each slice of the data independently. The feature
            dimension can be multidimensional e.g.
            X.shape = (n_samples, n_features_1, n_features_2, n_estimators).

        -----
        ### ⏎ Returns

        #### `y_pred : array, shape (n_samples, n_estimators, n_slices) | (n_samples, n_estimators, n_slices, n_targets)`
            The predicted values for each estimator.
        """
        ...
    def predict_proba(self, X):
        """## Estimate probabilistic estimates of each data slice with all possible estimators.

        -----
        ### 🛠️ Parameters

        X : array, shape (n_samples, nd_features, n_slices)
            The training input samples. For each data slice, a fitted estimator
            predicts a slice of the data. The feature dimension can be
            multidimensional e.g.
            ``X.shape = (n_samples, n_features_1, n_features_2, n_estimators)``.

        -----
        ### ⏎ Returns

        #### `y_pred : array, shape (n_samples, n_estimators, n_slices, n_classes)`
            The predicted values for each estimator.

        -----
        ### 📖 Notes

        This requires ``base_estimator`` to have a ``predict_proba`` method.
        """
        ...
    def decision_function(self, X):
        """## Estimate distances of each data slice to all hyperplanes.

        -----
        ### 🛠️ Parameters

        X : array, shape (n_samples, nd_features, n_slices)
            The training input samples. Each estimator outputs the distance to
            its hyperplane, e.g.:
            ``[estimators[ii].decision_function(X[..., ii]) for ii in range(n_estimators)]``.
            The feature dimension can be multidimensional e.g.
            ``X.shape = (n_samples, n_features_1, n_features_2, n_estimators)``.

        -----
        ### ⏎ Returns

        #### `y_pred : array, shape (n_samples, n_estimators, n_slices, n_classes * (n_classes-1) // 2)`
            The predicted values for each estimator.

        -----
        ### 📖 Notes

        This requires ``base_estimator`` to have a ``decision_function``
        method.
        """
        ...
    def score(self, X, y):
        """## Score each of the estimators on the tested dimensions.

        -----
        ### 🛠️ Parameters

        X : array, shape (n_samples, nd_features, n_slices)
            The input samples. For each data slice, the corresponding estimator
            scores the prediction, e.g.:
            ``[estimators[ii].score(X[..., ii], y) for ii in range(n_slices)]``.
            The feature dimension can be multidimensional e.g.
            ``X.shape = (n_samples, n_features_1, n_features_2, n_estimators)``.
        #### `y : array, shape (n_samples,) | (n_samples, n_targets)`
            The target values.

        -----
        ### ⏎ Returns

        #### `score : array, shape (n_samples, n_estimators, n_slices)`
            Score for each estimator / data slice couple.
        """
        ...
