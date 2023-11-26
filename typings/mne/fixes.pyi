import numpy as np
from _typeshed import Incomplete

def rng_uniform(rng):
    """### Get the unform/randint from the rng."""
    ...

class BaseEstimator:
    """### Base class for all estimators in scikit-learn.

    -----
    ### 📖 Notes

    All estimators should specify all the parameters that can be set
    at the class level in their ``__init__`` as explicit keyword
    arguments (no ``*args`` or ``**kwargs``).
    """

    def get_params(self, deep: bool = True):
        """### Get parameters for this estimator.

        -----
        ### 🛠️ Parameters

        deep : bool, optional
            If True, will return the parameters for this estimator and
            contained subobjects that are estimators.

        -----
        ### ⏎ Returns

        params : dict
            Parameter names mapped to their values.
        """
        ...
    def set_params(self, **params):
        """### Set the parameters of this estimator.

        The method works on simple estimators as well as on nested objects
        (such as pipelines). The latter have parameters of the form
        ``<component>__<parameter>`` so that it's possible to update each
        component of a nested object.

        -----
        ### 🛠️ Parameters

        **params : dict
            Parameters.

        -----
        ### ⏎ Returns

        inst : instance
            The object.
        """
        ...

def empirical_covariance(X, assume_centered: bool = False):
    """### Compute the Maximum likelihood covariance estimator.

    -----
    ### 🛠️ Parameters

    X : ndarray, shape (n_samples, n_features)
        Data from which to compute the covariance estimate

    assume_centered : Boolean
        If True, data are not centered before computation.
        Useful when working with data whose mean is almost, but not exactly
        zero.
        If False, data are centered before computation.

    -----
    ### ⏎ Returns

    covariance : 2D ndarray, shape (n_features, n_features)
        Empirical covariance (Maximum Likelihood Estimator).
    """
    ...

class EmpiricalCovariance(BaseEstimator):
    """### Maximum likelihood covariance estimator.

    Read more in the `User Guide <covariance>`.

    -----
    ### 🛠️ Parameters

    store_precision : bool
        Specifies if the estimated precision is stored.

    assume_centered : bool
        If True, data are not centered before computation.
        Useful when working with data whose mean is almost, but not exactly
        zero.
        If False (default), data are centered before computation.

    -----
    ### 📊 Attributes

    covariance_ : 2D ndarray, shape (n_features, n_features)
        Estimated covariance matrix

    precision_ : 2D ndarray, shape (n_features, n_features)
        Estimated pseudo-inverse matrix.
        (stored only if store_precision is True)
    """

    store_precision: Incomplete
    assume_centered: Incomplete

    def __init__(
        self, store_precision: bool = True, assume_centered: bool = False
    ) -> None: ...
    def get_precision(self):
        """### Getter for the precision matrix.

        -----
        ### ⏎ Returns

        precision_ : array-like,
            The precision matrix associated to the current covariance object.

        """
        ...
    location_: Incomplete

    def fit(self, X, y=None):
        """### Fit the Maximum Likelihood Estimator covariance model.

        -----
        ### 🛠️ Parameters

        X : array-like, shape = [n_samples, n_features]
          Training data, where n_samples is the number of samples and
          n_features is the number of features.
        y : ndarray | None
            Not used, present for API consistency.

        -----
        ### ⏎ Returns

        self : object
            Returns self.
        """
        ...
    def score(self, X_test, y=None):
        """### Compute the log-likelihood of a Gaussian dataset.

        Uses ``self.covariance_`` as an estimator of its covariance matrix.

        -----
        ### 🛠️ Parameters

        X_test : array-like, shape = [n_samples, n_features]
            Test data of which we compute the likelihood, where n_samples is
            the number of samples and n_features is the number of features.
            X_test is assumed to be drawn from the same distribution than
            the data used in fit (including centering).
        y : ndarray | None
            Not used, present for API consistency.

        -----
        ### ⏎ Returns

        res : float
            The likelihood of the data set with `self.covariance_` as an
            estimator of its covariance matrix.
        """
        ...
    def error_norm(
        self,
        comp_cov,
        norm: str = "frobenius",
        scaling: bool = True,
        squared: bool = True,
    ):
        """### Compute the Mean Squared Error between two covariance estimators.

        -----
        ### 🛠️ Parameters

        comp_cov : array-like, shape = [n_features, n_features]
            The covariance to compare with.
        norm : str
            The type of norm used to compute the error. Available error types:
            - 'frobenius' (default): sqrt(tr(A^t.A))
            - 'spectral': sqrt(max(eigenvalues(A^t.A))
            where A is the error ``(comp_cov - self.covariance_)``.
        scaling : bool
            If True (default), the squared error norm is divided by n_features.
            If False, the squared error norm is not rescaled.
        squared : bool
            Whether to compute the squared error norm or the error norm.
            If True (default), the squared error norm is returned.
            If False, the error norm is returned.

        -----
        ### ⏎ Returns

        The Mean Squared Error (in the sense of the Frobenius norm) between
        `self` and `comp_cov` covariance estimators.
        """
        ...
    def mahalanobis(self, observations):
        """### Compute the squared Mahalanobis distances of given observations.

        -----
        ### 🛠️ Parameters

        observations : array-like, shape = [n_observations, n_features]
            The observations, the Mahalanobis distances of the which we
            compute. Observations are assumed to be drawn from the same
            distribution than the data used in fit.

        -----
        ### ⏎ Returns

        mahalanobis_distance : array, shape = [n_observations,]
            Squared Mahalanobis distances of the observations.
        """
        ...

def log_likelihood(emp_cov, precision):
    """### Compute the sample mean of the log_likelihood under a covariance model.

    computes the empirical expected log-likelihood (accounting for the
    normalization terms and scaling), allowing for universal comparison (beyond
    this software package)

    -----
    ### 🛠️ Parameters

    emp_cov : 2D ndarray (n_features, n_features)
        Maximum Likelihood Estimator of covariance

    precision : 2D ndarray (n_features, n_features)
        The precision matrix of the covariance model to be tested

    -----
    ### ⏎ Returns

    sample mean of the log-likelihood
    """
    ...

def svd_flip(u, v, u_based_decision: bool = True): ...
def stable_cumsum(arr, axis=None, rtol: float = 1e-05, atol: float = 1e-08):
    """### Use high precision for cumsum and check that final value matches sum.

    -----
    ### 🛠️ Parameters

    arr : array-like
        To be cumulatively summed as flat
    axis : int, optional
        Axis along which the cumulative sum is computed.
        The default (None) is to compute the cumsum over the flattened array.
    rtol : float
        Relative tolerance, see ``np.allclose``
    atol : float
        Absolute tolerance, see ``np.allclose``
    """
    ...

prange: Incomplete

def jit(
    nopython: bool = True,
    nogil: bool = True,
    fastmath: bool = True,
    cache: bool = True,
    **kwargs,
): ...

has_numba: bool
prange = range
bincount = np.bincount

def pinvh(a, rtol=None):
    """### Compute a pseudo-inverse of a Hermitian matrix."""
    ...

def pinv(a, rtol=None):
    """### Compute a pseudo-inverse of a matrix."""
    ...
