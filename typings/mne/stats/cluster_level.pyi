from ..fixes import has_numba as has_numba, jit as jit
from ..parallel import parallel_func as parallel_func
from ..source_estimate import MixedSourceEstimate as MixedSourceEstimate, SourceEstimate as SourceEstimate, VolSourceEstimate as VolSourceEstimate
from ..source_space import SourceSpaces as SourceSpaces
from ..utils import ProgressBar as ProgressBar, check_random_state as check_random_state, logger as logger, split_list as split_list, verbose as verbose, warn as warn
from .parametric import f_oneway as f_oneway, ttest_1samp_no_p as ttest_1samp_no_p
from _typeshed import Incomplete

def bin_perm_rep(ndim, a: int=..., b: int=...):
    """Ndim permutations with repetitions of (a,b).

    Returns an array with all the possible permutations with repetitions of
    (0,1) in ndim dimensions.  The array is shaped as (2**ndim,ndim), and is
    ordered with the last index changing fastest.  For examble, for ndim=3:

    Examples
    --------
    >>> bin_perm_rep(3)
    array([[0, 0, 0],
           [0, 0, 1],
           [0, 1, 0],
           [0, 1, 1],
           [1, 0, 0],
           [1, 0, 1],
           [1, 1, 0],
           [1, 1, 1]])
    """

def permutation_cluster_test(X, threshold: Incomplete | None=..., n_permutations: int=..., tail: int=..., stat_fun: Incomplete | None=..., adjacency: Incomplete | None=..., n_jobs: Incomplete | None=..., seed: Incomplete | None=..., max_step: int=..., exclude: Incomplete | None=..., step_down_p: int=..., t_power: int=..., out_type: str=..., check_disjoint: bool=..., buffer_size: int=..., verbose: Incomplete | None=...):
    """Cluster-level statistical permutation test.

    For a list of :class:`NumPy arrays <numpy.ndarray>` of data,
    calculate some statistics corrected for multiple comparisons using
    permutations and cluster-level correction. Each element of the list ``X``
    should contain the data for one group of observations (e.g., 2D arrays for
    time series, 3D arrays for time-frequency power values). Permutations are
    generated with random partitions of the data. For details, see
    :footcite:p:`MarisOostenveld2007,Sassenhagen2019`.

    Parameters
    ----------
    X : list of array, shape (n_observations, p[, q][, r])
        The data to be clustered. Each array in ``X`` should contain the
        observations for one group. The first dimension of each array is the
        number of observations from that group; remaining dimensions comprise
        the size of a single observation. For example if ``X = [X1, X2]``
        with ``X1.shape = (20, 50, 4)`` and ``X2.shape = (17, 50, 4)``, then
        ``X`` has 2 groups with respectively 20 and 17 observations in each,
        and each data point is of shape ``(50, 4)``. Note: that the
        *last dimension* of each element of ``X`` should correspond to the
        dimension represented in the ``adjacency`` parameter
        (e.g., spectral data should be provided as
        ``(observations, frequencies, channels/vertices)``).
    
    threshold : float | dict | None
        The so-called "cluster forming threshold" in the form of a test statistic
        (note: this is not an alpha level / "p-value").
        If numeric, vertices with data values more extreme than ``threshold`` will
        be used to form clusters. If ``None``, an F-threshold will be chosen
        automatically that corresponds to a p-value of 0.05 for the given number of
        observations (only valid when using an F-statistic). If ``threshold`` is a
        :class:`dict` (with keys ``'start'`` and ``'step'``) then threshold-free
        cluster enhancement (TFCE) will be used (see the
        :ref:`TFCE example <tfce_example>` and :footcite:`SmithNichols2009`).
        See Notes for an example on how to compute a threshold based on
        a particular p-value for one-tailed or two-tailed tests.
    
    n_permutations : int
        The number of permutations to compute.
    
    tail : int
        If tail is 1, the statistic is thresholded above threshold.
        If tail is -1, the statistic is thresholded below threshold.
        If tail is 0, the statistic is thresholded on both sides of
        the distribution.
    
    stat_fun : callable | None
        Function called to calculate the test statistic. Must accept 1D-array as
        input and return a 1D array. If ``None`` (the default), uses
        `mne.stats.f_oneway`.
    
    adjacency : scipy.sparse.spmatrix | None | False
        Defines adjacency between locations in the data, where "locations" can be
        spatial vertices, frequency bins, time points, etc. For spatial vertices
        (i.e. sensor space data), see :func:`mne.channels.find_ch_adjacency` or
        :func:`mne.spatial_inter_hemi_adjacency`. For source space data, see
        :func:`mne.spatial_src_adjacency` or
        :func:`mne.spatio_temporal_src_adjacency`. If ``False``, assumes
        no adjacency (each location is treated as independent and unconnected).
        If ``None``, a regular lattice adjacency is assumed, connecting
        each  location to its neighbor(s) along the last dimension
        of each group  ``X[k]`` (or the last two dimensions if ``X[k]`` is 2D).
        If ``adjacency`` is a matrix, it is assumed to be symmetric (only the
        upper triangular half is used) and must be square with dimension equal to
        ``X[k].shape[-1]`` (for 2D data) or ``X[k].shape[-1] * X[k].shape[-2]``
        (for 3D data) or (optionally)
        ``X[k].shape[-1] * X[k].shape[-2] * X[k].shape[-3]``
        (for 4D data). The function `mne.stats.combine_adjacency` may be useful for 4D data.
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
    
    max_step : int
        Maximum distance between samples along the second axis of ``X`` to be
        considered adjacent (typically the second axis is the "time" dimension).
        Only used when ``adjacency`` has shape (n_vertices, n_vertices), that is,
        when adjacency is only specified for sensors (e.g., via
        :func:`mne.channels.find_ch_adjacency`), and not via sensors **and**
        further dimensions such as time points (e.g., via an additional call of
        :func:`mne.stats.combine_adjacency`).
    
    exclude : bool array or None
        Mask to apply to the data to exclude certain points from clustering
        (e.g., medial wall vertices). Should be the same shape as ``X``.
        If ``None``, no points are excluded.
    
    step_down_p : float
        To perform a step-down-in-jumps test, pass a p-value for clusters to
        exclude from each successive iteration. Default is zero, perform no
        step-down test (since no clusters will be smaller than this value).
        Setting this to a reasonable value, e.g. 0.05, can increase sensitivity
        but costs computation time.
    
    t_power : float
        Power to raise the statistical values (usually F-values) by before
        summing (sign will be retained). Note that ``t_power=0`` will give a
        count of locations in each cluster, ``t_power=1`` will weight each location
        by its statistical score.
    
    out_type : 'mask' | 'indices'
        Output format of clusters within a list.
        If ``'mask'``, returns a list of boolean arrays,
        each with the same shape as the input data (or slices if the shape is 1D
        and adjacency is None), with ``True`` values indicating locations that are
        part of a cluster. If ``'indices'``, returns a list of tuple of ndarray,
        where each ndarray contains the indices of locations that together form the
        given cluster along the given dimension. Note that for large datasets,
        ``'indices'`` may use far less memory than ``'mask'``.
        Default is ``'indices'``.
    
    check_disjoint : bool
        Whether to check if the connectivity matrix can be separated into disjoint
        sets before clustering. This may lead to faster clustering, especially if
        the second dimension of ``X`` (usually the "time" dimension) is large.
    
    buffer_size : int | None
        Block size to use when computing test statistics. This can significantly
        reduce memory usage when ``n_jobs > 1`` and memory sharing between
        processes is enabled (see :func:`mne.set_cache_dir`), because ``X`` will be
        shared between processes and each process only needs to allocate space for
        a small block of locations at a time.
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    F_obs : array, shape (p[, q][, r])
        Statistic (F by default) observed for all variables.
    clusters : list
        List type defined by out_type above.
    cluster_pv : array
        P-value for each cluster.
    H0 : array, shape (n_permutations,)
        Max cluster level stats observed under permutation.

    Notes
    -----
    
    For computing a ``threshold`` based on a p-value, use the conversion
    from :meth:`scipy.stats.rv_continuous.ppf`::
    
        pval = 0.001  # arbitrary
        dfn = n_conditions - 1  # degrees of freedom numerator
        dfd = n_observations - n_conditions  # degrees of freedom denominator
        thresh = scipy.stats.f.ppf(1 - pval, dfn=dfn, dfd=dfd)  # F distribution

    References
    ----------
    .. footbibliography::
    """

def permutation_cluster_1samp_test(X, threshold: Incomplete | None=..., n_permutations: int=..., tail: int=..., stat_fun: Incomplete | None=..., adjacency: Incomplete | None=..., n_jobs: Incomplete | None=..., seed: Incomplete | None=..., max_step: int=..., exclude: Incomplete | None=..., step_down_p: int=..., t_power: int=..., out_type: str=..., check_disjoint: bool=..., buffer_size: int=..., verbose: Incomplete | None=...):
    """Non-parametric cluster-level paired t-test.

    For details, see :footcite:p:`MarisOostenveld2007,Sassenhagen2019`.

    Parameters
    ----------
    X : array, shape (n_observations, p[, q][, r])
        The data to be clustered. The first dimension should correspond to the
        difference between paired samples (observations) in two conditions.
        The subarrays ``X[k]`` can be 1D (e.g., time series), 2D (e.g.,
        time series over channels), or 3D (e.g., time-frequencies over
        channels) associated with the kth observation. For spatiotemporal data,
        see also :func:`mne.stats.spatio_temporal_cluster_1samp_test`.
    
    threshold : float | dict | None
        The so-called "cluster forming threshold" in the form of a test statistic
        (note: this is not an alpha level / "p-value").
        If numeric, vertices with data values more extreme than ``threshold`` will
        be used to form clusters. If ``None``, a t-threshold will be chosen
        automatically that corresponds to a p-value of 0.05 for the given number of
        observations (only valid when using a t-statistic). If ``threshold`` is a
        :class:`dict` (with keys ``'start'`` and ``'step'``) then threshold-free
        cluster enhancement (TFCE) will be used (see the
        :ref:`TFCE example <tfce_example>` and :footcite:`SmithNichols2009`).
        See Notes for an example on how to compute a threshold based on
        a particular p-value for one-tailed or two-tailed tests.
    
    n_permutations : int | 'all'
        The number of permutations to compute. Can be 'all' to perform
        an exact test.
    
    tail : int
        If tail is 1, the statistic is thresholded above threshold.
        If tail is -1, the statistic is thresholded below threshold.
        If tail is 0, the statistic is thresholded on both sides of
        the distribution.
    
    stat_fun : callable | None
        Function called to calculate the test statistic. Must accept 1D-array as
        input and return a 1D array. If ``None`` (the default), uses
        `mne.stats.ttest_1samp_no_p`.
    
    adjacency : scipy.sparse.spmatrix | None | False
        Defines adjacency between locations in the data, where "locations" can be
        spatial vertices, frequency bins, time points, etc. For spatial vertices
        (i.e. sensor space data), see :func:`mne.channels.find_ch_adjacency` or
        :func:`mne.spatial_inter_hemi_adjacency`. For source space data, see
        :func:`mne.spatial_src_adjacency` or
        :func:`mne.spatio_temporal_src_adjacency`. If ``False``, assumes
        no adjacency (each location is treated as independent and unconnected).
        If ``None``, a regular lattice adjacency is assumed, connecting
        each  location to its neighbor(s) along the last dimension
        of  ``X`` (or the last two dimensions if ``X`` is 2D).
        If ``adjacency`` is a matrix, it is assumed to be symmetric (only the
        upper triangular half is used) and must be square with dimension equal to
        ``X.shape[-1]`` (for 2D data) or ``X.shape[-1] * X.shape[-2]``
        (for 3D data) or (optionally)
        ``X.shape[-1] * X.shape[-2] * X.shape[-3]``
        (for 4D data). The function `mne.stats.combine_adjacency` may be useful for 4D data.
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
    
    max_step : int
        Maximum distance between samples along the second axis of ``X`` to be
        considered adjacent (typically the second axis is the "time" dimension).
        Only used when ``adjacency`` has shape (n_vertices, n_vertices), that is,
        when adjacency is only specified for sensors (e.g., via
        :func:`mne.channels.find_ch_adjacency`), and not via sensors **and**
        further dimensions such as time points (e.g., via an additional call of
        :func:`mne.stats.combine_adjacency`).
    
    exclude : bool array or None
        Mask to apply to the data to exclude certain points from clustering
        (e.g., medial wall vertices). Should be the same shape as ``X``.
        If ``None``, no points are excluded.
    
    step_down_p : float
        To perform a step-down-in-jumps test, pass a p-value for clusters to
        exclude from each successive iteration. Default is zero, perform no
        step-down test (since no clusters will be smaller than this value).
        Setting this to a reasonable value, e.g. 0.05, can increase sensitivity
        but costs computation time.
    
    t_power : float
        Power to raise the statistical values (usually t-values) by before
        summing (sign will be retained). Note that ``t_power=0`` will give a
        count of locations in each cluster, ``t_power=1`` will weight each location
        by its statistical score.
    
    out_type : 'mask' | 'indices'
        Output format of clusters within a list.
        If ``'mask'``, returns a list of boolean arrays,
        each with the same shape as the input data (or slices if the shape is 1D
        and adjacency is None), with ``True`` values indicating locations that are
        part of a cluster. If ``'indices'``, returns a list of tuple of ndarray,
        where each ndarray contains the indices of locations that together form the
        given cluster along the given dimension. Note that for large datasets,
        ``'indices'`` may use far less memory than ``'mask'``.
        Default is ``'indices'``.
    
    check_disjoint : bool
        Whether to check if the connectivity matrix can be separated into disjoint
        sets before clustering. This may lead to faster clustering, especially if
        the second dimension of ``X`` (usually the "time" dimension) is large.
    
    buffer_size : int | None
        Block size to use when computing test statistics. This can significantly
        reduce memory usage when ``n_jobs > 1`` and memory sharing between
        processes is enabled (see :func:`mne.set_cache_dir`), because ``X`` will be
        shared between processes and each process only needs to allocate space for
        a small block of locations at a time.
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    t_obs : array, shape (p[, q][, r])
        T-statistic observed for all variables.
    clusters : list
        List type defined by out_type above.
    cluster_pv : array
        P-value for each cluster.
    H0 : array, shape (n_permutations,)
        Max cluster level stats observed under permutation.

    Notes
    -----
    From an array of paired observations, e.g. a difference in signal
    amplitudes or power spectra in two conditions, calculate if the data
    distributions in the two conditions are significantly different.
    The procedure uses a cluster analysis with permutation test
    for calculating corrected p-values. Randomized data are generated with
    random sign flips. See :footcite:`MarisOostenveld2007` for more
    information.

    Because a 1-sample t-test on the difference in observations is
    mathematically equivalent to a paired t-test, internally this function
    computes a 1-sample t-test (by default) and uses sign flipping (always)
    to perform permutations. This might not be suitable for the case where
    there is truly a single observation under test; see :ref:`disc-stats`.
    
    For computing a ``threshold`` based on a p-value, use the conversion
    from :meth:`scipy.stats.rv_continuous.ppf`::
    
        pval = 0.001  # arbitrary
        df = n_observations - 1  # degrees of freedom for the test
        thresh = scipy.stats.t.ppf(1 - pval / 2, df)  # two-tailed, t distribution
    
    For a one-tailed test (``tail=1``), don't divide the p-value by 2.
    For testing the lower tail (``tail=-1``), don't subtract ``pval`` from 1.

    If ``n_permutations`` exceeds the maximum number of possible permutations
    given the number of observations, then ``n_permutations`` and ``seed``
    will be ignored since an exact test (full permutation test) will be
    performed (this is the case when
    ``n_permutations >= 2 ** (n_observations - (tail == 0))``).

    If no initial clusters are found because all points in the true
    distribution are below the threshold, then ``clusters``, ``cluster_pv``,
    and ``H0`` will all be empty arrays.

    References
    ----------
    .. footbibliography::
    """

def spatio_temporal_cluster_1samp_test(X, threshold: Incomplete | None=..., n_permutations: int=..., tail: int=..., stat_fun: Incomplete | None=..., adjacency: Incomplete | None=..., n_jobs: Incomplete | None=..., seed: Incomplete | None=..., max_step: int=..., spatial_exclude: Incomplete | None=..., step_down_p: int=..., t_power: int=..., out_type: str=..., check_disjoint: bool=..., buffer_size: int=..., verbose: Incomplete | None=...):
    """Non-parametric cluster-level paired t-test for spatio-temporal data.

    This function provides a convenient wrapper for
    :func:`mne.stats.permutation_cluster_1samp_test`, for use with data
    organized in the form (observations × time × space),
    (observations × frequencies × space), or optionally
    (observations × time × frequencies × space). For details, see
    :footcite:p:`MarisOostenveld2007,Sassenhagen2019`.

    Parameters
    ----------
    X : array, shape (n_observations, p[, q], n_vertices)
        The data to be clustered. The first dimension should correspond to the
        difference between paired samples (observations) in two conditions.
        The second, and optionally third, dimensions correspond to the
        time or time-frequency data. And, the last dimension should be spatial.
    
    threshold : float | dict | None
        The so-called "cluster forming threshold" in the form of a test statistic
        (note: this is not an alpha level / "p-value").
        If numeric, vertices with data values more extreme than ``threshold`` will
        be used to form clusters. If ``None``, a t-threshold will be chosen
        automatically that corresponds to a p-value of 0.05 for the given number of
        observations (only valid when using a t-statistic). If ``threshold`` is a
        :class:`dict` (with keys ``'start'`` and ``'step'``) then threshold-free
        cluster enhancement (TFCE) will be used (see the
        :ref:`TFCE example <tfce_example>` and :footcite:`SmithNichols2009`).
        See Notes for an example on how to compute a threshold based on
        a particular p-value for one-tailed or two-tailed tests.
    
    n_permutations : int | 'all'
        The number of permutations to compute. Can be 'all' to perform
        an exact test.
    
    tail : int
        If tail is 1, the statistic is thresholded above threshold.
        If tail is -1, the statistic is thresholded below threshold.
        If tail is 0, the statistic is thresholded on both sides of
        the distribution.
    
    stat_fun : callable | None
        Function called to calculate the test statistic. Must accept 1D-array as
        input and return a 1D array. If ``None`` (the default), uses
        `mne.stats.ttest_1samp_no_p`.
    
    adjacency : scipy.sparse.spmatrix | None | False
        Defines adjacency between locations in the data, where "locations" can be
        spatial vertices, frequency bins, time points, etc. For spatial vertices
        (i.e. sensor space data), see :func:`mne.channels.find_ch_adjacency` or
        :func:`mne.spatial_inter_hemi_adjacency`. For source space data, see
        :func:`mne.spatial_src_adjacency` or
        :func:`mne.spatio_temporal_src_adjacency`. If ``False``, assumes
        no adjacency (each location is treated as independent and unconnected).
        If ``None``, a regular lattice adjacency is assumed, connecting
        each spatial location to its neighbor(s) along the last dimension
        of  ``X``.
        If ``adjacency`` is a matrix, it is assumed to be symmetric (only the
        upper triangular half is used) and must be square with dimension equal to
        ``X.shape[-1]`` (n_vertices) or ``X.shape[-1] * X.shape[-2]``
        (n_times * n_vertices) or (optionally)
        ``X.shape[-1] * X.shape[-2] * X.shape[-3]``
        (n_times * n_freqs * n_vertices). If spatial adjacency is uniform in time, it is recommended to use a square matrix with dimension ``X.shape[-1]`` (n_vertices) to save memory and computation, and to use ``max_step`` to define the extent of temporal adjacency to consider when clustering.
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
    
    max_step : int
        Maximum distance between samples along the second axis of ``X`` to be
        considered adjacent (typically the second axis is the "time" dimension).
        Only used when ``adjacency`` has shape (n_vertices, n_vertices), that is,
        when adjacency is only specified for sensors (e.g., via
        :func:`mne.channels.find_ch_adjacency`), and not via sensors **and**
        further dimensions such as time points (e.g., via an additional call of
        :func:`mne.stats.combine_adjacency`).
    spatial_exclude : list of int or None
        List of spatial indices to exclude from clustering.
    
    step_down_p : float
        To perform a step-down-in-jumps test, pass a p-value for clusters to
        exclude from each successive iteration. Default is zero, perform no
        step-down test (since no clusters will be smaller than this value).
        Setting this to a reasonable value, e.g. 0.05, can increase sensitivity
        but costs computation time.
    
    t_power : float
        Power to raise the statistical values (usually t-values) by before
        summing (sign will be retained). Note that ``t_power=0`` will give a
        count of locations in each cluster, ``t_power=1`` will weight each location
        by its statistical score.
    
    out_type : 'mask' | 'indices'
        Output format of clusters within a list.
        If ``'mask'``, returns a list of boolean arrays,
        each with the same shape as the input data (or slices if the shape is 1D
        and adjacency is None), with ``True`` values indicating locations that are
        part of a cluster. If ``'indices'``, returns a list of tuple of ndarray,
        where each ndarray contains the indices of locations that together form the
        given cluster along the given dimension. Note that for large datasets,
        ``'indices'`` may use far less memory than ``'mask'``.
        Default is ``'indices'``.
    
    check_disjoint : bool
        Whether to check if the connectivity matrix can be separated into disjoint
        sets before clustering. This may lead to faster clustering, especially if
        the second dimension of ``X`` (usually the "time" dimension) is large.
    
    buffer_size : int | None
        Block size to use when computing test statistics. This can significantly
        reduce memory usage when ``n_jobs > 1`` and memory sharing between
        processes is enabled (see :func:`mne.set_cache_dir`), because ``X`` will be
        shared between processes and each process only needs to allocate space for
        a small block of locations at a time.
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    t_obs : array, shape (p[, q], n_vertices)
        T-statistic observed for all variables.
    clusters : list
        List type defined by out_type above.
    cluster_pv : array
        P-value for each cluster.
    H0 : array, shape (n_permutations,)
        Max cluster level stats observed under permutation.

    Notes
    -----
    
    For computing a ``threshold`` based on a p-value, use the conversion
    from :meth:`scipy.stats.rv_continuous.ppf`::
    
        pval = 0.001  # arbitrary
        df = n_observations - 1  # degrees of freedom for the test
        thresh = scipy.stats.t.ppf(1 - pval / 2, df)  # two-tailed, t distribution
    
    For a one-tailed test (``tail=1``), don't divide the p-value by 2.
    For testing the lower tail (``tail=-1``), don't subtract ``pval`` from 1.

    References
    ----------
    .. footbibliography::
    """

def spatio_temporal_cluster_test(X, threshold: Incomplete | None=..., n_permutations: int=..., tail: int=..., stat_fun: Incomplete | None=..., adjacency: Incomplete | None=..., n_jobs: Incomplete | None=..., seed: Incomplete | None=..., max_step: int=..., spatial_exclude: Incomplete | None=..., step_down_p: int=..., t_power: int=..., out_type: str=..., check_disjoint: bool=..., buffer_size: int=..., verbose: Incomplete | None=...):
    """Non-parametric cluster-level test for spatio-temporal data.

    This function provides a convenient wrapper for
    :func:`mne.stats.permutation_cluster_test`, for use with data
    organized in the form (observations × time × space),
    (observations × time × space), or optionally
    (observations × time × frequencies × space). For more information,
    see :footcite:p:`MarisOostenveld2007,Sassenhagen2019`.

    Parameters
    ----------
    X : list of array, shape (n_observations, p[, q], n_vertices)
        The data to be clustered. Each array in ``X`` should contain the
        observations for one group. The first dimension of each array is the
        number of observations from that group (and may vary between groups).
        The second, and optionally third, dimensions correspond to the
        time or time-frequency data. And, the last dimension should be spatial.
        All dimensions except the first should match across all groups.
    
    threshold : float | dict | None
        The so-called "cluster forming threshold" in the form of a test statistic
        (note: this is not an alpha level / "p-value").
        If numeric, vertices with data values more extreme than ``threshold`` will
        be used to form clusters. If ``None``, an F-threshold will be chosen
        automatically that corresponds to a p-value of 0.05 for the given number of
        observations (only valid when using an F-statistic). If ``threshold`` is a
        :class:`dict` (with keys ``'start'`` and ``'step'``) then threshold-free
        cluster enhancement (TFCE) will be used (see the
        :ref:`TFCE example <tfce_example>` and :footcite:`SmithNichols2009`).
        See Notes for an example on how to compute a threshold based on
        a particular p-value for one-tailed or two-tailed tests.
    
    n_permutations : int
        The number of permutations to compute.
    
    tail : int
        If tail is 1, the statistic is thresholded above threshold.
        If tail is -1, the statistic is thresholded below threshold.
        If tail is 0, the statistic is thresholded on both sides of
        the distribution.
    
    stat_fun : callable | None
        Function called to calculate the test statistic. Must accept 1D-array as
        input and return a 1D array. If ``None`` (the default), uses
        `mne.stats.f_oneway`.
    
    adjacency : scipy.sparse.spmatrix | None | False
        Defines adjacency between locations in the data, where "locations" can be
        spatial vertices, frequency bins, time points, etc. For spatial vertices
        (i.e. sensor space data), see :func:`mne.channels.find_ch_adjacency` or
        :func:`mne.spatial_inter_hemi_adjacency`. For source space data, see
        :func:`mne.spatial_src_adjacency` or
        :func:`mne.spatio_temporal_src_adjacency`. If ``False``, assumes
        no adjacency (each location is treated as independent and unconnected).
        If ``None``, a regular lattice adjacency is assumed, connecting
        each spatial location to its neighbor(s) along the last dimension
        of each group  ``X[k]``.
        If ``adjacency`` is a matrix, it is assumed to be symmetric (only the
        upper triangular half is used) and must be square with dimension equal to
        ``X[k].shape[-1]`` (n_vertices) or ``X[k].shape[-1] * X[k].shape[-2]``
        (n_times * n_vertices) or (optionally)
        ``X[k].shape[-1] * X[k].shape[-2] * X[k].shape[-3]``
        (n_times * n_freqs * n_vertices). If spatial adjacency is uniform in time, it is recommended to use a square matrix with dimension ``X[k].shape[-1]`` (n_vertices) to save memory and computation, and to use ``max_step`` to define the extent of temporal adjacency to consider when clustering.
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
    
    max_step : int
        Maximum distance between samples along the second axis of ``X`` to be
        considered adjacent (typically the second axis is the "time" dimension).
        Only used when ``adjacency`` has shape (n_vertices, n_vertices), that is,
        when adjacency is only specified for sensors (e.g., via
        :func:`mne.channels.find_ch_adjacency`), and not via sensors **and**
        further dimensions such as time points (e.g., via an additional call of
        :func:`mne.stats.combine_adjacency`).
    spatial_exclude : list of int or None
        List of spatial indices to exclude from clustering.
    
    step_down_p : float
        To perform a step-down-in-jumps test, pass a p-value for clusters to
        exclude from each successive iteration. Default is zero, perform no
        step-down test (since no clusters will be smaller than this value).
        Setting this to a reasonable value, e.g. 0.05, can increase sensitivity
        but costs computation time.
    
    t_power : float
        Power to raise the statistical values (usually F-values) by before
        summing (sign will be retained). Note that ``t_power=0`` will give a
        count of locations in each cluster, ``t_power=1`` will weight each location
        by its statistical score.
    
    out_type : 'mask' | 'indices'
        Output format of clusters within a list.
        If ``'mask'``, returns a list of boolean arrays,
        each with the same shape as the input data (or slices if the shape is 1D
        and adjacency is None), with ``True`` values indicating locations that are
        part of a cluster. If ``'indices'``, returns a list of tuple of ndarray,
        where each ndarray contains the indices of locations that together form the
        given cluster along the given dimension. Note that for large datasets,
        ``'indices'`` may use far less memory than ``'mask'``.
        Default is ``'indices'``.
    
    check_disjoint : bool
        Whether to check if the connectivity matrix can be separated into disjoint
        sets before clustering. This may lead to faster clustering, especially if
        the second dimension of ``X`` (usually the "time" dimension) is large.
    
    buffer_size : int | None
        Block size to use when computing test statistics. This can significantly
        reduce memory usage when ``n_jobs > 1`` and memory sharing between
        processes is enabled (see :func:`mne.set_cache_dir`), because ``X`` will be
        shared between processes and each process only needs to allocate space for
        a small block of locations at a time.
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    F_obs : array, shape (p[, q], n_vertices)
        Statistic (F by default) observed for all variables.
    clusters : list
        List type defined by out_type above.
    cluster_pv: array
        P-value for each cluster.
    H0 : array, shape (n_permutations,)
        Max cluster level stats observed under permutation.

    Notes
    -----
    
    For computing a ``threshold`` based on a p-value, use the conversion
    from :meth:`scipy.stats.rv_continuous.ppf`::
    
        pval = 0.001  # arbitrary
        dfn = n_conditions - 1  # degrees of freedom numerator
        dfd = n_observations - n_conditions  # degrees of freedom denominator
        thresh = scipy.stats.f.ppf(1 - pval, dfn=dfn, dfd=dfd)  # F distribution

    References
    ----------
    .. footbibliography::
    """

def summarize_clusters_stc(clu, p_thresh: float=..., tstep: float=..., tmin: int=..., subject: str=..., vertices: Incomplete | None=...):
    """Assemble summary SourceEstimate from spatiotemporal cluster results.

    This helps visualizing results from spatio-temporal-clustering
    permutation tests.

    Parameters
    ----------
    clu : tuple
        The output from clustering permutation tests.
    p_thresh : float
        The significance threshold for inclusion of clusters.
    tstep : float
        The time step between samples of the original :class:`STC
        <mne.SourceEstimate>`, in seconds (i.e., ``1 / stc.sfreq``). Defaults
        to ``1``, which will yield a colormap indicating cluster duration
        measured in *samples* rather than *seconds*.
    tmin : float | int
        The time of the first sample.
    subject : str
        The name of the subject.
    vertices : list of array | instance of SourceSpaces | None
        The vertex numbers associated with the source space locations. Defaults
        to None. If None, equals ``[np.arange(10242), np.arange(10242)]``.
        Can also be an instance of SourceSpaces to get vertex numbers from.

        .. versionchanged:: 0.21
           Added support for SourceSpaces.

    Returns
    -------
    out : instance of SourceEstimate
        A summary of the clusters. The first time point in this SourceEstimate
        object is the summation of all the clusters. Subsequent time points
        contain each individual cluster. The magnitude of the activity
        corresponds to the duration spanned by the cluster (duration units are
        determined by ``tstep``).

        .. versionchanged:: 0.21
           Added support for volume and mixed source estimates.
    """