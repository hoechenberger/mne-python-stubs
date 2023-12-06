from ..utils import (
    check_random_state as check_random_state,
    fill_doc as fill_doc,
    logger as logger,
)

def power_iteration_kron(
    A, C, max_iter: int = 1000, tol: float = 0.001, random_state: int = 0
):
    """Find the largest singular value for the matrix kron(C.T, A).

    It uses power iterations.

    Parameters
    ----------
    A : array
        An array
    C : array
        An array
    max_iter : int
        Maximum number of iterations

    random_state : None | int | instance of ~numpy.random.RandomState
        A seed for the NumPy random number generator (RNG). If ``None`` (default),
        the seed will be  obtained from the operating system
        (see  `RandomState` for details), meaning it will most
        likely produce different output every time this function or method is run.
        To achieve reproducible results, pass a value here to explicitly initialize
        the RNG with a defined state.

    Returns
    -------
    L : float
        largest singular value

    Notes
    -----
    http://en.wikipedia.org/wiki/Power_iteration
    """
    ...

def compute_bias(
    M, G, X, max_iter: int = 1000, tol: float = 1e-06, n_orient: int = 1, verbose=None
):
    """Compute scaling to correct amplitude bias.

    It solves the following optimization problem using FISTA:

    min 1/2 * (|| M - GDX ||fro)^2
    s.t. D >= 1 and D is a diagonal matrix

    Reference for the FISTA algorithm:
    Amir Beck and Marc Teboulle
    A Fast Iterative Shrinkage-Thresholding Algorithm for Linear Inverse
    Problems, SIAM J. Imaging Sci., 2(1), 183-202. (20 pages)
    http://epubs.siam.org/doi/abs/10.1137/080716542

    Parameters
    ----------
    M : array
        measurement data.
    G : array
        leadfield matrix.
    X : array
        reconstructed time courses with amplitude bias.
    max_iter : int
        Maximum number of iterations.
    tol : float
        The tolerance on convergence.
    n_orient : int
        The number of orientations (1 for fixed and 3 otherwise).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    D : array
        Debiasing weights.
    """
    ...
