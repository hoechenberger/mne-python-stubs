from ..parallel import parallel_func as parallel_func
from ..utils import check_random_state as check_random_state, logger as logger, verbose as verbose
from _typeshed import Incomplete

def permutation_t_test(X, n_permutations: int=..., tail: int=..., n_jobs: Incomplete | None=..., seed: Incomplete | None=..., verbose: Incomplete | None=...):
    """One sample/paired sample permutation test based on a t-statistic.

    This function can perform the test on one variable or
    simultaneously on multiple variables. When applying the test to multiple
    variables, the "tmax" method is used for adjusting the p-values of each
    variable for multiple comparisons. Like Bonferroni correction, this method
    adjusts p-values in a way that controls the family-wise error rate.
    However, the permutation method will be more
    powerful than Bonferroni correction when different variables in the test
    are correlated (see :footcite:`NicholsHolmes2002`).

    Parameters
    ----------
    X : array, shape (n_samples, n_tests)
        Samples (observations) by number of tests (variables).
    n_permutations : int | 'all'
        Number of permutations. If n_permutations is 'all' all possible
        permutations are tested. It's the exact test, that
        can be untractable when the number of samples is big (e.g. > 20).
        If n_permutations >= 2**n_samples then the exact test is performed.
    tail : -1 or 0 or 1 (default = 0)
        If tail is 1, the alternative hypothesis is that the
        mean of the data is greater than 0 (upper tailed test).  If tail is 0,
        the alternative hypothesis is that the mean of the data is different
        than 0 (two tailed test).  If tail is -1, the alternative hypothesis
        is that the mean of the data is less than 0 (lower tailed test).
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the :mod:`joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a :class:`joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.
    
    seed : None | int | instance of ~numpy.random.RandomState
        A seed for the NumPy random number generator (RNG). If ``None`` (default),
        the seed will be  obtained from the operating system
        (see  :class:`~numpy.random.RandomState` for details), meaning it will most
        likely produce different output every time this function or method is run.
        To achieve reproducible results, pass a value here to explicitly initialize
        the RNG with a defined state.
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    T_obs : array of shape [n_tests]
        T-statistic observed for all variables.
    p_values : array of shape [n_tests]
        P-values for all the tests (a.k.a. variables).
    H0 : array of shape [n_permutations]
        T-statistic obtained by permutations and t-max trick for multiple
        comparison.

    Notes
    -----
    If ``n_permutations >= 2 ** (n_samples - (tail == 0))``,
    ``n_permutations`` and ``seed`` will be ignored since an exact test
    (full permutation test) will be performed.

    References
    ----------
    .. footbibliography::
    """

def bootstrap_confidence_interval(arr, ci: float=..., n_bootstraps: int=..., stat_fun: str=..., random_state: Incomplete | None=...):
    """Get confidence intervals from non-parametric bootstrap.

    Parameters
    ----------
    arr : ndarray, shape (n_samples, ...)
        The input data on which to calculate the confidence interval.
    ci : float
        Level of the confidence interval between 0 and 1.
    n_bootstraps : int
        Number of bootstraps.
    stat_fun : str | callable
        Can be "mean", "median", or a callable operating along ``axis=0``.
    random_state : int | float | array_like | None
        The seed at which to initialize the bootstrap.

    Returns
    -------
    cis : ndarray, shape (2, ...)
        Containing the lower boundary of the CI at ``cis[0, ...]`` and the
        upper boundary of the CI at ``cis[1, ...]``.
    """