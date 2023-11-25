from ..utils import (
    check_random_state as check_random_state,
    logger as logger,
    random_permutation as random_permutation,
)

def infomax(
    data,
    weights=...,
    l_rate=...,
    block=...,
    w_change: float = ...,
    anneal_deg: float = ...,
    anneal_step: float = ...,
    extended: bool = ...,
    n_subgauss: int = ...,
    kurt_size: int = ...,
    ext_blocks: int = ...,
    max_iter: int = ...,
    random_state=...,
    blowup: float = ...,
    blowup_fac: float = ...,
    n_small_angle: int = ...,
    use_bias: bool = ...,
    verbose=...,
    return_n_iter: bool = ...,
):
    """Run (extended) Infomax ICA decomposition on raw data.

    Parameters
    ----------
    data : np.ndarray, shape (n_samples, n_features)
        The whitened data to unmix.
    weights : np.ndarray, shape (n_features, n_features)
        The initialized unmixing matrix.
        Defaults to None, which means the identity matrix is used.
    l_rate : float
        This quantity indicates the relative size of the change in weights.
        Defaults to ``0.01 / log(n_features ** 2)``.

        .. note:: Smaller learning rates will slow down the ICA procedure.

    block : int
        The block size of randomly chosen data segments.
        Defaults to floor(sqrt(n_times / 3.)).
    w_change : float
        The change at which to stop iteration. Defaults to 1e-12.
    anneal_deg : float
        The angle (in degrees) at which the learning rate will be reduced.
        Defaults to 60.0.
    anneal_step : float
        The factor by which the learning rate will be reduced once
        ``anneal_deg`` is exceeded: ``l_rate *= anneal_step.``
        Defaults to 0.9.
    extended : bool
        Whether to use the extended Infomax algorithm or not.
        Defaults to True.
    n_subgauss : int
        The number of subgaussian components. Only considered for extended
        Infomax. Defaults to 1.
    kurt_size : int
        The window size for kurtosis estimation. Only considered for extended
        Infomax. Defaults to 6000.
    ext_blocks : int
        Only considered for extended Infomax. If positive, denotes the number
        of blocks after which to recompute the kurtosis, which is used to
        estimate the signs of the sources. In this case, the number of
        sub-gaussian sources is automatically determined.
        If negative, the number of sub-gaussian sources to be used is fixed
        and equal to n_subgauss. In this case, the kurtosis is not estimated.
        Defaults to 1.
    max_iter : int
        The maximum number of iterations. Defaults to 200.

    random_state : None | int | instance of ~numpy.random.RandomState
        A seed for the NumPy random number generator (RNG). If ``None`` (default),
        the seed will be  obtained from the operating system
        (see  :class:numpy.random.RandomState` for details), meaning it will most
        likely produce different output every time this function or method is run.
        To achieve reproducible results, pass a value here to explicitly initialize
        the RNG with a defined state.
    blowup : float
        The maximum difference allowed between two successive estimations of
        the unmixing matrix. Defaults to 10000.
    blowup_fac : float
        The factor by which the learning rate will be reduced if the difference
        between two successive estimations of the unmixing matrix exceededs
        ``blowup``: ``l_rate *= blowup_fac``. Defaults to 0.5.
    n_small_angle : int | None
        The maximum number of allowed steps in which the angle between two
        successive estimations of the unmixing matrix is less than
        ``anneal_deg``. If None, this parameter is not taken into account to
        stop the iterations. Defaults to 20.
    use_bias : bool
        This quantity indicates if the bias should be computed.
        Defaults to True.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.
    return_n_iter : bool
        Whether to return the number of iterations performed. Defaults to
        False.

    Returns
    -------
    unmixing_matrix : np.ndarray, shape (n_features, n_features)
        The linear unmixing operator.
    n_iter : int
        The number of iterations. Only returned if ``return_max_iter=True``.

    References
    ----------
    .. [1] A. J. Bell, T. J. Sejnowski. An information-maximization approach to
           blind separation and blind deconvolution. Neural Computation, 7(6),
           1129-1159, 1995.
    .. [2] T. W. Lee, M. Girolami, T. J. Sejnowski. Independent component
           analysis using an extended infomax algorithm for mixed subgaussian
           and supergaussian sources. Neural Computation, 11(2), 417-441, 1999.
    """
