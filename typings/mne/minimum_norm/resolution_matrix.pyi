from .._fiff.constants import FIFF as FIFF
from .._fiff.pick import pick_channels_forward as pick_channels_forward
from ..evoked import EvokedArray as EvokedArray
from ..forward.forward import (
    Forward as Forward,
    convert_forward_solution as convert_forward_solution,
)
from ..label import Label as Label
from ..source_space._source_space import SourceSpaces as SourceSpaces
from ..utils import logger as logger
from .inverse import apply_inverse as apply_inverse
from mne.minimum_norm.inverse import InverseOperator as InverseOperator

def make_inverse_resolution_matrix(
    forward,
    inverse_operator,
    method: str = "dSPM",
    lambda2=0.1111111111111111,
    verbose=None,
):
    """Compute resolution matrix for linear inverse operator.

    Parameters
    ----------
    forward : instance of Forward
        Forward Operator.
    inverse_operator : instance of InverseOperator
        Inverse operator.
    method : 'MNE' | 'dSPM' | 'sLORETA'
        Inverse method to use (MNE, dSPM, sLORETA).
    lambda2 : float
        The regularisation parameter.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    resmat: array, shape (n_orient_inv * n_dipoles, n_orient_fwd * n_dipoles)
        Resolution matrix (inverse operator times forward operator).
        The result of applying the inverse operator to the forward operator.
        If source orientations are not fixed, all source components will be
        computed (i.e. for n_orient_inv > 1 or n_orient_fwd > 1).
        The columns of the resolution matrix are the point-spread functions
        (PSFs) and the rows are the cross-talk functions (CTFs).
    """
    ...

def get_point_spread(
    resmat,
    src,
    idx,
    mode=None,
    *,
    n_comp: int = 1,
    norm: bool = False,
    return_pca_vars: bool = False,
    vector: bool = False,
    verbose=None,
):
    """Get point-spread (PSFs) functions for vertices.

    Parameters
    ----------
    resmat : array, shape (n_dipoles, n_dipoles)
        Forward Operator.
    src : instance of SourceSpaces | instance of InverseOperator | instance of Forward
        Source space used to compute resolution matrix.
        Must be an InverseOperator if ``vector=True`` and a surface
        source space is used.

    idx : list of int | list of Label
        Source for indices for which to compute PSFs or CTFs. If mode is None,
        PSFs/CTFs will be returned for all indices. If mode is not None, the
        corresponding summary measure will be computed across all PSFs/CTFs
        available from idx.
        Can be:

        * list of integers : Compute PSFs/CTFs for all indices to source space
          vertices specified in idx.
        * list of Label : Compute PSFs/CTFs for source space vertices in
          specified labels.

    mode : None | 'mean' | 'max' | 'svd'
        Compute summary of PSFs/CTFs across all indices specified in 'idx'.
        Can be:

        * None : Output individual PSFs/CTFs for each specific vertex
          (Default).
        * 'mean' : Mean of PSFs/CTFs across vertices.
        * 'max' : PSFs/CTFs with maximum norm across vertices. Returns the
          n_comp largest PSFs/CTFs.
        * 'svd' : SVD components across PSFs/CTFs across vertices. Returns the
          n_comp first SVD components.

    n_comp : int
        Number of PSF/CTF components to return for mode='max' or mode='svd'.
        Default n_comp=1.

    norm : None | 'max' | 'norm'
        Whether and how to normalise the PSFs and CTFs. This will be applied
        before computing summaries as specified in 'mode'.
        Can be:

        * None : Use un-normalized PSFs/CTFs (Default).
        * 'max' : Normalize to maximum absolute value across all PSFs/CTFs.
        * 'norm' : Normalize to maximum norm across all PSFs/CTFs.

    return_pca_vars : bool
        Whether or not to return the explained variances across the specified
        vertices for individual SVD components. This is only valid if
        mode='svd'.
        Default return_pca_vars=False.

    vector : bool
        Whether to return PSF/CTF as vector source estimate (3 values per
        location) or source estimate object (1 intensity value per location).
        Only allowed to be True if corresponding dimension of resolution matrix
        is 3 * n_dipoles. Defaults to False.

        ✨ Added in version 1.2

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------

    stcs : instance of SourceEstimate | list of instances of SourceEstimate
        The PSFs or CTFs as STC objects. All PSFs/CTFs will be returned as
        successive samples in STC objects, in the order they are specified
        in idx. STCs for different labels willbe returned as a list.
        If resmat was computed with n_orient_inv==3 for CTFs or
        n_orient_fwd==3 for PSFs then 3 functions per vertex will be returned
        as successive samples (i.e. one function per orientation).
        If vector=False (default) and resmat was computed with
        n_orient_inv==3 for PSFs or n_orient_fwd==3 for CTFs, then the three
        values per vertex will be combined into one intensity value per
        vertex in a SourceEstimate object. If vector=True, PSFs or CTFs
        with 3 values per vertex (one per orientation) will be returned in
        a VectorSourceEstimate object.

    pca_vars : array, shape (n_comp,) | list of array
        The explained variances of the first n_comp SVD components across the
        PSFs/CTFs for the specified vertices. Arrays for multiple labels are
        returned as list. Only returned if ``mode='svd'`` and ``return_pca_vars=True``.
    """
    ...

def get_cross_talk(
    resmat,
    src,
    idx,
    mode=None,
    *,
    n_comp: int = 1,
    norm: bool = False,
    return_pca_vars: bool = False,
    vector: bool = False,
    verbose=None,
):
    """Get cross-talk (CTFs) function for vertices.

    Parameters
    ----------
    resmat : array, shape (n_dipoles, n_dipoles)
        Forward Operator.
    src : instance of SourceSpaces | instance of InverseOperator | instance of Forward
        Source space used to compute resolution matrix.
        Must be an InverseOperator if ``vector=True`` and a surface
        source space is used.

    idx : list of int | list of Label
        Source for indices for which to compute PSFs or CTFs. If mode is None,
        PSFs/CTFs will be returned for all indices. If mode is not None, the
        corresponding summary measure will be computed across all PSFs/CTFs
        available from idx.
        Can be:

        * list of integers : Compute PSFs/CTFs for all indices to source space
          vertices specified in idx.
        * list of Label : Compute PSFs/CTFs for source space vertices in
          specified labels.

    mode : None | 'mean' | 'max' | 'svd'
        Compute summary of PSFs/CTFs across all indices specified in 'idx'.
        Can be:

        * None : Output individual PSFs/CTFs for each specific vertex
          (Default).
        * 'mean' : Mean of PSFs/CTFs across vertices.
        * 'max' : PSFs/CTFs with maximum norm across vertices. Returns the
          n_comp largest PSFs/CTFs.
        * 'svd' : SVD components across PSFs/CTFs across vertices. Returns the
          n_comp first SVD components.

    n_comp : int
        Number of PSF/CTF components to return for mode='max' or mode='svd'.
        Default n_comp=1.

    norm : None | 'max' | 'norm'
        Whether and how to normalise the PSFs and CTFs. This will be applied
        before computing summaries as specified in 'mode'.
        Can be:

        * None : Use un-normalized PSFs/CTFs (Default).
        * 'max' : Normalize to maximum absolute value across all PSFs/CTFs.
        * 'norm' : Normalize to maximum norm across all PSFs/CTFs.

    return_pca_vars : bool
        Whether or not to return the explained variances across the specified
        vertices for individual SVD components. This is only valid if
        mode='svd'.
        Default return_pca_vars=False.

    vector : bool
        Whether to return PSF/CTF as vector source estimate (3 values per
        location) or source estimate object (1 intensity value per location).
        Only allowed to be True if corresponding dimension of resolution matrix
        is 3 * n_dipoles. Defaults to False.

        ✨ Added in version 1.2

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------

    stcs : instance of SourceEstimate | list of instances of SourceEstimate
        The PSFs or CTFs as STC objects. All PSFs/CTFs will be returned as
        successive samples in STC objects, in the order they are specified
        in idx. STCs for different labels willbe returned as a list.
        If resmat was computed with n_orient_inv==3 for CTFs or
        n_orient_fwd==3 for PSFs then 3 functions per vertex will be returned
        as successive samples (i.e. one function per orientation).
        If vector=False (default) and resmat was computed with
        n_orient_inv==3 for PSFs or n_orient_fwd==3 for CTFs, then the three
        values per vertex will be combined into one intensity value per
        vertex in a SourceEstimate object. If vector=True, PSFs or CTFs
        with 3 values per vertex (one per orientation) will be returned in
        a VectorSourceEstimate object.

    pca_vars : array, shape (n_comp,) | list of array
        The explained variances of the first n_comp SVD components across the
        PSFs/CTFs for the specified vertices. Arrays for multiple labels are
        returned as list. Only returned if ``mode='svd'`` and ``return_pca_vars=True``.
    """
    ...
