def eigh(a, overwrite_a: bool = False, check_finite: bool = True):
    """Efficient wrapper for eigh.

    Parameters
    ----------
    a : ndarray, shape (n_components, n_components)
        The symmetric array operate on.
    overwrite_a : bool
        If True, the contents of a can be overwritten for efficiency.
    check_finite : bool
        If True, check that all elements are finite.

    Returns
    -------
    w : ndarray, shape (n_components,)
        The N eigenvalues, in ascending order, each repeated according to
        its multiplicity.
    v : ndarray, shape (n_components, n_components)
        The normalized eigenvector corresponding to the eigenvalue ``w[i]``
        is the column ``v[:, i]``.
    """

def sqrtm_sym(A, rcond: float = 1e-07, inv: bool = False):
    """Compute the sqrt of a positive, semi-definite matrix (or its inverse).

    Parameters
    ----------
    A : ndarray, shape (..., n, n)
        The array to take the square root of.
    rcond : float
        The relative condition number used during reconstruction.
    inv : bool
        If True, compute the inverse of the square root rather than the
        square root itself.

    Returns
    -------
    A_sqrt : ndarray, shape (..., n, n)
        The (possibly inverted) square root of A.
    s : ndarray, shape (..., n)
        The original square root singular values (not inverted).
    """
