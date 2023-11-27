from ..time_frequency._stft import (
    istft as istft,
    stft as stft,
    stft_norm1 as stft_norm1,
    stft_norm2 as stft_norm2,
)
from ..utils import logger as logger, sum_squared as sum_squared, warn as warn
from .mxne_debiasing import compute_bias as compute_bias
from _typeshed import Incomplete

def groups_norm2(A, n_orient):
    """## Compute squared L2 norms of groups inplace."""
    ...

def norm_l2inf(A, n_orient, copy: bool = True):
    """## L2-inf norm."""
    ...

def norm_l21(A, n_orient, copy: bool = True):
    """## L21 norm."""
    ...

def dgap_l21(M, G, X, active_set, alpha, n_orient):
    """## Duality gap for the mixed norm inverse problem.

    See :footcite:`GramfortEtAl2012`.

    -----
    ### 🛠️ Parameters

    M : array, shape (n_sensors, n_times)
        The data.
    G : array, shape (n_sensors, n_active)
        The gain matrix a.k.a. lead field.
    X : array, shape (n_active, n_times)
        Sources.
    #### `active_set : array of bool, shape (n_sources, )`
        Mask of active sources.
    #### `alpha : float`
        The regularization parameter.
    #### `n_orient : int`
        Number of dipoles per locations (typically 1 or 3).

    -----
    ### ⏎ Returns

    #### `gap : float`
        Dual gap.
    #### `p_obj : float`
        Primal objective.
    #### `d_obj : float`
        Dual objective. gap = p_obj - d_obj.
    R : array, shape (n_sensors, n_times)
        Current residual (M - G * X).

    References
    ----------
    .. footbibilography::
    """
    ...

def mixed_norm_solver(
    M,
    G,
    alpha,
    maxit: int = 3000,
    tol: float = 1e-08,
    verbose=None,
    active_set_size: int = 50,
    debias: bool = True,
    n_orient: int = 1,
    solver: str = "auto",
    return_gap: bool = False,
    dgap_freq: int = 10,
    active_set_init=None,
    X_init=None,
):
    """## Solve L1/L2 mixed-norm inverse problem with active set strategy.

    See references :footcite:`GramfortEtAl2012,StrohmeierEtAl2016,
    BertrandEtAl2020`.

    -----
    ### 🛠️ Parameters

    M : array, shape (n_sensors, n_times)
        The data.
    G : array, shape (n_sensors, n_dipoles)
        The gain matrix a.k.a. lead field.
    #### `alpha : float`
        The regularization parameter. It should be between 0 and 100.
        A value of 100 will lead to an empty active set (no active source).
    #### `maxit : int`
        The number of iterations.
    #### `tol : float`
        Tolerance on dual gap for convergence checking.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.
    #### `active_set_size : int`
        Size of active set increase at each iteration.
    #### `debias : bool`
        Debias source estimates.
    #### `n_orient : int`
        The number of orientation (1 : fixed or 3 : free or loose).
    #### `solver : 'cd' | 'bcd' | 'auto'`
        The algorithm to use for the optimization. Block Coordinate Descent
        (BCD) uses Anderson acceleration for faster convergence.
    #### `return_gap : bool`
        Return final duality gap.
    #### `dgap_freq : int`
        The duality gap is computed every dgap_freq iterations of the solver on
        the active set.
    #### `active_set_init : array, shape (n_dipoles,) or None`
        The initial active set (boolean array) used at the first iteration.
        If None, the usual active set strategy is applied.
    X_init : array, shape (n_dipoles, n_times) or None
        The initial weight matrix used for warm starting the solver. If None,
        the weights are initialized at zero.

    -----
    ### ⏎ Returns

    X : array, shape (n_active, n_times)
        The source estimates.
    #### `active_set : array, shape (new_active_set_size,)`
        The mask of active sources. Note that new_active_set_size is the size
        of the active set after convergence of the solver.
    E : list
        The value of the objective function over the iterations.
    #### `gap : float`
        Final duality gap. Returned only if return_gap is True.

    References
    ----------
    .. footbibliography::
    """
    ...

def iterative_mixed_norm_solver(
    M,
    G,
    alpha,
    n_mxne_iter,
    maxit: int = 3000,
    tol: float = 1e-08,
    verbose=None,
    active_set_size: int = 50,
    debias: bool = True,
    n_orient: int = 1,
    dgap_freq: int = 10,
    solver: str = "auto",
    weight_init=None,
):
    """## Solve L0.5/L2 mixed-norm inverse problem with active set strategy.

    See reference :footcite:`StrohmeierEtAl2016`.

    -----
    ### 🛠️ Parameters

    M : array, shape (n_sensors, n_times)
        The data.
    G : array, shape (n_sensors, n_dipoles)
        The gain matrix a.k.a. lead field.
    #### `alpha : float`
        The regularization parameter. It should be between 0 and 100.
        A value of 100 will lead to an empty active set (no active source).
    #### `n_mxne_iter : int`
        The number of MxNE iterations. If > 1, iterative reweighting
        is applied.
    #### `maxit : int`
        The number of iterations.
    #### `tol : float`
        Tolerance on dual gap for convergence checking.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.
    #### `active_set_size : int`
        Size of active set increase at each iteration.
    #### `debias : bool`
        Debias source estimates.
    #### `n_orient : int`
        The number of orientation (1 : fixed or 3 : free or loose).
    #### `dgap_freq : int or np.inf`
        The duality gap is evaluated every dgap_freq iterations.
    #### `solver : 'cd' | 'bcd' | 'auto'`
        The algorithm to use for the optimization.
    #### `weight_init : array, shape (n_dipoles,) or None`
        The initial weight used for reweighting the gain matrix. If None, the
        weights are initialized with ones.

    -----
    ### ⏎ Returns

    X : array, shape (n_active, n_times)
        The source estimates.
    #### `active_set : array`
        The mask of active sources.
    E : list
        The value of the objective function over the iterations.

    References
    ----------
    .. footbibliography::
    """
    ...

def tf_lipschitz_constant(M, G, phi, phiT, tol: float = 0.001, verbose=None):
    """## Compute lipschitz constant for FISTA.

    It uses a power iteration method.
    """
    ...

def safe_max_abs(A, ia):
    """## Compute np.max(np.abs(A[ia])) possible with empty A."""
    ...

def safe_max_abs_diff(A, ia, B, ib):
    """## Compute np.max(np.abs(A)) possible with empty A."""
    ...

class _Phi:
    """## Have phi stft as callable w/o using a lambda that does not pickle."""

    wsize: Incomplete
    tstep: Incomplete
    n_coefs: Incomplete
    n_dicts: Incomplete
    n_freqs: Incomplete
    n_steps: Incomplete
    n_times: Incomplete
    ops: Incomplete

    def __init__(self, wsize, tstep, n_coefs, n_times) -> None: ...
    def __call__(self, x): ...
    def norm(self, z, ord: int = 2):
        """## Squared L2 norm if ord == 2 and L1 norm if order == 1."""
        ...

class _PhiT:
    """## Have phi.T istft as callable w/o using a lambda that does not pickle."""

    tstep: Incomplete
    n_freqs: Incomplete
    n_steps: Incomplete
    n_times: Incomplete
    n_dicts: Incomplete
    n_coefs: Incomplete
    op_re: Incomplete
    op_im: Incomplete

    def __init__(self, tstep, n_freqs, n_steps, n_times) -> None: ...
    def __call__(self, z): ...

def norm_l21_tf(Z, phi, n_orient, w_space=None):
    """## L21 norm for TF."""
    ...

def norm_l1_tf(Z, phi, n_orient, w_time):
    """## L1 norm for TF."""
    ...

def norm_epsilon(Y, l1_ratio, phi, w_space: float = 1.0, w_time=None):
    """## Weighted epsilon norm.

    The weighted epsilon norm is the dual norm of::

    w_{space} * (1. - l1_ratio) * ||Y||_2 + l1_ratio * ||Y||_{1, w_{time}}.

    where `||Y||_{1, w_{time}} = (np.abs(Y) * w_time).sum()`

    Warning: it takes into account the fact that Y only contains coefficients
    corresponding to the positive frequencies (see `stft_norm2()`): some
    entries will be counted twice. It is also assumed that all entries of both
    Y and w_time are non-negative. See
    :footcite:`NdiayeEtAl2016,BurdakovMerkulov2001`.

    -----
    ### 🛠️ Parameters

    Y : array, shape (n_coefs,)
        The input data.
    l1_ratio : float between 0 and 1
        Tradeoff between L2 and L1 regularization. When it is 0, no temporal
        regularization is applied.
    #### `phi : instance of _Phi`
        The TF operator.
    #### `w_space : float`
        Scalar weight of the L2 norm. By default, it is taken equal to 1.
    #### `w_time : array, shape (n_coefs, ) | None`
        Weights of each TF coefficient in the L1 norm. If None, weights equal
        to 1 are used.


    -----
    ### ⏎ Returns

    #### `nu : float`
        The value of the dual norm evaluated at Y.

    References
    ----------
    .. footbibliography::
    """
    ...

def norm_epsilon_inf(G, R, phi, l1_ratio, n_orient, w_space=None, w_time=None):
    """## Weighted epsilon-inf norm of phi(np.dot(G.T, R)).

    -----
    ### 🛠️ Parameters

    G : array, shape (n_sensors, n_sources)
        Gain matrix a.k.a. lead field.
    R : array, shape (n_sensors, n_times)
        Residual.
    #### `phi : instance of _Phi`
        The TF operator.
    l1_ratio : float between 0 and 1
        Parameter controlling the tradeoff between L21 and L1 regularization.
        0 corresponds to an absence of temporal regularization, ie MxNE.
    #### `n_orient : int`
        Number of dipoles per location (typically 1 or 3).
    #### `w_space : array, shape (n_positions,) or None.`
        Weights for the L2 term of the epsilon norm. If None, weights are
        all equal to 1.
    #### `w_time : array, shape (n_positions, n_coefs) or None`
        Weights for the L1 term of the epsilon norm. If None, weights are
        all equal to 1.

    -----
    ### ⏎ Returns

    #### `nu : float`
        The maximum value of the epsilon norms over groups of n_orient dipoles
        (consecutive rows of phi(np.dot(G.T, R))).
    """
    ...

def dgap_l21l1(
    M,
    G,
    Z,
    active_set,
    alpha_space,
    alpha_time,
    phi,
    phiT,
    n_orient,
    highest_d_obj,
    w_space=None,
    w_time=None,
):
    """## Duality gap for the time-frequency mixed norm inverse problem.

    See :footcite:`GramfortEtAl2012,NdiayeEtAl2016`

    -----
    ### 🛠️ Parameters

    M : array, shape (n_sensors, n_times)
        The data.
    G : array, shape (n_sensors, n_sources)
        Gain matrix a.k.a. lead field.
    Z : array, shape (n_active, n_coefs)
        Sources in TF domain.
    #### `active_set : array of bool, shape (n_sources, )`
        Mask of active sources.
    #### `alpha_space : float`
        The spatial regularization parameter.
    #### `alpha_time : float`
        The temporal regularization parameter. The higher it is the smoother
        will be the estimated time series.
    #### `phi : instance of _Phi`
        The TF operator.
    phiT : instance of _PhiT
        The transpose of the TF operator.
    #### `n_orient : int`
        Number of dipoles per locations (typically 1 or 3).
    #### `highest_d_obj : float`
        The highest value of the dual objective so far.
    #### `w_space : array, shape (n_positions, )`
        Array of spatial weights.
    #### `w_time : array, shape (n_positions, n_coefs)`
        Array of TF weights.

    -----
    ### ⏎ Returns

    #### `gap : float`
        Dual gap
    #### `p_obj : float`
        Primal objective
    #### `d_obj : float`
        Dual objective. gap = p_obj - d_obj
    R : array, shape (n_sensors, n_times)
        Current residual (M - G * X)

    References
    ----------
    .. footbibliography::
    """
    ...

def tf_mixed_norm_solver(
    M,
    G,
    alpha_space,
    alpha_time,
    wsize: int = 64,
    tstep: int = 4,
    n_orient: int = 1,
    maxit: int = 200,
    tol: float = 1e-08,
    active_set_size=None,
    debias: bool = True,
    return_gap: bool = False,
    dgap_freq: int = 10,
    verbose=None,
):
    """## Solve TF L21+L1 inverse solver with BCD and active set approach.

    See :footcite:`GramfortEtAl2013b,GramfortEtAl2011,BekhtiEtAl2016`.

    -----
    ### 🛠️ Parameters

    M : array, shape (n_sensors, n_times)
        The data.
    G : array, shape (n_sensors, n_dipoles)
        The gain matrix a.k.a. lead field.
    #### `alpha_space : float`
        The spatial regularization parameter.
    #### `alpha_time : float`
        The temporal regularization parameter. The higher it is the smoother
        will be the estimated time series.
    wsize: int or array-like
        Length of the STFT window in samples (must be a multiple of 4).
        If an array is passed, multiple TF dictionaries are used (each having
        its own wsize and tstep) and each entry of wsize must be a multiple
        of 4.
    tstep: int or array-like
        Step between successive windows in samples (must be a multiple of 2,
        a divider of wsize and smaller than wsize/2) (default: wsize/2).
        If an array is passed, multiple TF dictionaries are used (each having
        its own wsize and tstep), and each entry of tstep must be a multiple
        of 2 and divide the corresponding entry of wsize.
    #### `n_orient : int`
        The number of orientation (1 : fixed or 3 : free or loose).
    #### `maxit : int`
        The number of iterations.
    #### `tol : float`
        If absolute difference between estimates at 2 successive iterations
        is lower than tol, the convergence is reached.
    #### `debias : bool`
        Debias source estimates.
    #### `return_gap : bool`
        Return final duality gap.
    #### `dgap_freq : int or np.inf`
        The duality gap is evaluated every dgap_freq iterations.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    X : array, shape (n_active, n_times)
        The source estimates.
    #### `active_set : array`
        The mask of active sources.
    E : list
        The value of the objective function every dgap_freq iteration. If
        log_objective is False or dgap_freq is np.inf, it will be empty.
    #### `gap : float`
        Final duality gap. Returned only if return_gap is True.

    References
    ----------
    .. footbibliography::
    """
    ...

def iterative_tf_mixed_norm_solver(
    M,
    G,
    alpha_space,
    alpha_time,
    n_tfmxne_iter,
    wsize: int = 64,
    tstep: int = 4,
    maxit: int = 3000,
    tol: float = 1e-08,
    debias: bool = True,
    n_orient: int = 1,
    dgap_freq: int = 10,
    verbose=None,
):
    """## Solve TF L0.5/L1 + L0.5 inverse problem with BCD + active set approach.

    -----
    ### 🛠️ Parameters

    M: array, shape (n_sensors, n_times)
        The data.
    G: array, shape (n_sensors, n_dipoles)
        The gain matrix a.k.a. lead field.
    alpha_space: float
        The spatial regularization parameter. The higher it is the less there
        will be active sources.
    #### `alpha_time : float`
        The temporal regularization parameter. The higher it is the smoother
        will be the estimated time series. 0 means no temporal regularization,
        a.k.a. irMxNE.
    #### `n_tfmxne_iter : int`
        Number of TF-MxNE iterations. If > 1, iterative reweighting is applied.
    #### `wsize : int or array-like`
        Length of the STFT window in samples (must be a multiple of 4).
        If an array is passed, multiple TF dictionaries are used (each having
        its own wsize and tstep) and each entry of wsize must be a multiple
        of 4.
    #### `tstep : int or array-like`
        Step between successive windows in samples (must be a multiple of 2,
        a divider of wsize and smaller than wsize/2) (default: wsize/2).
        If an array is passed, multiple TF dictionaries are used (each having
        its own wsize and tstep), and each entry of tstep must be a multiple
        of 2 and divide the corresponding entry of wsize.
    #### `maxit : int`
        The maximum number of iterations for each TF-MxNE problem.
    #### `tol : float`
        If absolute difference between estimates at 2 successive iterations
        is lower than tol, the convergence is reached. Also used as criterion
        on duality gap for each TF-MxNE problem.
    #### `debias : bool`
        Debias source estimates.
    #### `n_orient : int`
        The number of orientation (1 : fixed or 3 : free or loose).
    #### `dgap_freq : int or np.inf`
        The duality gap is evaluated every dgap_freq iterations.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    X : array, shape (n_active, n_times)
        The source estimates.
    #### `active_set : array`
        The mask of active sources.
    E : list
        The value of the objective function over iterations.
    """
    ...
