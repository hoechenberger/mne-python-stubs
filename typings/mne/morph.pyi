from .morph_map import read_morph_map as read_morph_map
from .parallel import parallel_func as parallel_func
from .source_space._source_space import SourceSpaces as SourceSpaces
from .surface import mesh_edges as mesh_edges, read_surface as read_surface
from .utils import (
    BunchConst as BunchConst,
    ProgressBar as ProgressBar,
    check_version as check_version,
    fill_doc as fill_doc,
    get_subjects_dir as get_subjects_dir,
    logger as logger,
    use_log_level as use_log_level,
    warn as warn,
)
from _typeshed import Incomplete

def compute_source_morph(
    src,
    subject_from=None,
    subject_to: str = "fsaverage",
    subjects_dir=None,
    zooms: str = "auto",
    niter_affine=(100, 100, 10),
    niter_sdr=(5, 5, 3),
    spacing: int = 5,
    smooth=None,
    warn: bool = True,
    xhemi: bool = False,
    sparse: bool = False,
    src_to=None,
    precompute: bool = False,
    verbose=None,
):
    """Create a SourceMorph from one subject to another.

    Method is based on spherical morphing by FreeSurfer for surface
    cortical estimates `GreveEtAl2013` and
    Symmetric Diffeomorphic Registration for volumic data
    `AvantsEtAl2008`.

    Parameters
    ----------
    src : instance of SourceSpaces | instance of SourceEstimate
        The SourceSpaces of subject_from (can be a
        SourceEstimate if only using a surface source space).
    subject_from : str | None
        Name of the original subject as named in the SUBJECTS_DIR.
        If None (default), then ``src[0]['subject_his_id]'`` will be used.
    subject_to : str | None
        Name of the subject to which to morph as named in the SUBJECTS_DIR.
        Default is ``'fsaverage'``. If None, ``src_to[0]['subject_his_id']``
        will be used.

        🎭 Changed in version 0.20
           Support for subject_to=None.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    zooms : float | tuple | str | None
        The voxel size of volume for each spatial dimension in mm.
        If spacing is None, MRIs won't be resliced, and both volumes
        must have the same number of spatial dimensions.
        Can also be ``'auto'`` to use ``5.`` if ``src_to is None`` and
        the zooms from ``src_to`` otherwise.

        🎭 Changed in version 0.20
           Support for 'auto' mode.
    niter_affine : tuple of int
        Number of levels (``len(niter_affine)``) and number of
        iterations per level - for each successive stage of iterative
        refinement - to perform the affine transform.
        Default is niter_affine=(100, 100, 10).
    niter_sdr : tuple of int
        Number of levels (``len(niter_sdr)``) and number of
        iterations per level - for each successive stage of iterative
        refinement - to perform the Symmetric Diffeomorphic Registration (sdr)
        transform. Default is niter_sdr=(5, 5, 3).
    spacing : int | list | None
        The resolution of the icosahedral mesh (typically 5).
        If None, all vertices will be used (potentially filling the
        surface). If a list, then values will be morphed to the set of
        vertices specified in in ``spacing[0]`` and ``spacing[1]``.
        This will be ignored if ``src_to`` is supplied.

        🎭 Changed in version 0.21
           src_to, if provided, takes precedence.
    smooth : int | str | None
        Number of iterations for the smoothing of the surface data.
        If None, smooth is automatically defined to fill the surface
        with non-zero values. Can also be ``'nearest'`` to use the nearest
        vertices on the surface.

        🎭 Changed in version 0.20
           Added support for 'nearest'.
    warn : bool
        If True, warn if not all vertices were used. The default is warn=True.
    xhemi : bool
        Morph across hemisphere. Currently only implemented for
        ``subject_to == subject_from``. See notes below.
        The default is xhemi=False.
    sparse : bool
        Morph as a sparse source estimate. Works only with (Vector)
        SourceEstimate. If True the only parameters used are subject_to and
        subject_from, and spacing has to be None. Default is sparse=False.
    src_to : instance of SourceSpaces | None
        The destination source space.

        - For surface-based morphing, this is the preferred over ``spacing``
          for providing the vertices.
        - For volumetric morphing, this should be passed so that 1) the
          resultingmorph volume is properly constrained to the brain volume,
          and 2) STCs from multiple subjects morphed to the same destination
          subject/source space have the vertices.
        - For mixed (surface + volume) morphing, this is required.

        ✨ Added in version 0.20
    precompute : bool
        If True (default False), compute the sparse matrix representation of
        the volumetric morph (if present). This takes a long time to
        compute, but can make morphs faster when thousands of points are used.
        See `mne.SourceMorph.compute_vol_morph_mat` (which can be called
        later if desired) for more information.

        ✨ Added in version 0.22

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    morph : instance of SourceMorph
        The `mne.SourceMorph` object.

    Notes
    -----
    This function can be used to morph surface data between hemispheres by
    setting ``xhemi=True``. The full cross-hemisphere morph matrix maps left
    to right and right to left. A matrix for cross-mapping only one hemisphere
    can be constructed by specifying the appropriate vertices, for example, to
    map the right hemisphere to the left::

        vertices_from=[[], vert_rh], vertices_to=[vert_lh, []]

    Cross-hemisphere mapping requires appropriate ``sphere.left_right``
    morph-maps in the subject's directory. These morph maps are included
    with the ``fsaverage_sym`` FreeSurfer subject, and can be created for other
    subjects with the ``mris_left_right_register`` FreeSurfer command. The
    ``fsaverage_sym`` subject is included with FreeSurfer > 5.1 and can be
    obtained as described `here
    <https://surfer.nmr.mgh.harvard.edu/fswiki/Xhemi>`_. For statistical
    comparisons between hemispheres, use of the symmetric ``fsaverage_sym``
    model is recommended to minimize bias `GreveEtAl2013`.

    ✨ Added in version 0.17.0

    ✨ Added in version 0.21.0
       Support for morphing mixed source estimates.

    References
    ----------
    .. footbibliography::
    """
    ...

class SourceMorph:
    """Morph source space data from one subject to another.

    💡 This class should not be instantiated directly via
        ``mne.SourceMorph(...)``. Instead, use one of the functions
        listed in the See Also section below.

    Parameters
    ----------
    subject_from : str | None
        Name of the subject from which to morph as named in the SUBJECTS_DIR.
    subject_to : str | array | list of array
        Name of the subject on which to morph as named in the SUBJECTS_DIR.
        The default is 'fsaverage'. If morphing a volume source space,
        subject_to can be the path to a MRI volume. Can also be a list of
        two arrays if morphing to hemisphere surfaces.
    kind : str | None
        Kind of source estimate. E.g. ``'volume'`` or ``'surface'``.
    zooms : float | tuple
        See `mne.compute_source_morph`.
    niter_affine : tuple of int
        Number of levels (``len(niter_affine)``) and number of
        iterations per level - for each successive stage of iterative
        refinement - to perform the affine transform.
    niter_sdr : tuple of int
        Number of levels (``len(niter_sdr)``) and number of
        iterations per level - for each successive stage of iterative
        refinement - to perform the Symmetric Diffeomorphic Registration (sdr)
        transform `AvantsEtAl2008`.
    spacing : int | list | None
        See `mne.compute_source_morph`.
    smooth : int | str | None
        See `mne.compute_source_morph`.
    xhemi : bool
        Morph across hemisphere.
    morph_mat : scipy.sparse.csr_matrix
        The sparse surface morphing matrix for spherical surface
        based morphing `GreveEtAl2013`.
    vertices_to : list of ndarray
        The destination surface vertices.
    shape : tuple
        The volume MRI shape.
    affine : ndarray
        The volume MRI affine.
    pre_affine : instance of dipy.align.AffineMap
        The transformation that is applied before the before ``sdr_morph``.
    sdr_morph : instance of dipy.align.DiffeomorphicMap
        The class that applies the the symmetric diffeomorphic registration
        (SDR) morph.
    src_data : dict
        Additional source data necessary to perform morphing.
    vol_morph_mat : scipy.sparse.csr_matrix | None
        The volumetric morph matrix, if `compute_vol_morph_mat`
        was used.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    compute_source_morph
    read_source_morph

    Notes
    -----
    ✨ Added in version 0.17

    References
    ----------
    .. footbibliography::
    """

    subject_from: Incomplete
    subject_to: Incomplete
    kind: Incomplete
    zooms: Incomplete
    niter_affine: Incomplete
    niter_sdr: Incomplete
    spacing: Incomplete
    smooth: Incomplete
    xhemi: Incomplete
    morph_mat: Incomplete
    shape: Incomplete
    affine: Incomplete
    sdr_morph: Incomplete
    pre_affine: Incomplete
    src_data: Incomplete
    vol_morph_mat: Incomplete
    vertices_to: Incomplete

    def __init__(
        self,
        subject_from,
        subject_to,
        kind,
        zooms,
        niter_affine,
        niter_sdr,
        spacing,
        smooth,
        xhemi,
        morph_mat,
        vertices_to,
        shape,
        affine,
        pre_affine,
        sdr_morph,
        src_data,
        vol_morph_mat,
        *,
        verbose=None,
    ) -> None: ...
    def apply(
        self,
        stc_from,
        output: str = "stc",
        mri_resolution: bool = False,
        mri_space=None,
        verbose=None,
    ):
        """Morph source space data.

        Parameters
        ----------
        stc_from : VolSourceEstimate | VolVectorSourceEstimate | SourceEstimate | VectorSourceEstimate
            The source estimate to morph.
        output : str
            Can be ``'stc'`` (default) or possibly ``'nifti1'``, or
            ``'nifti2'`` when working with a volume source space defined on a
            regular grid.
        mri_resolution : bool | tuple | int | float
            If True the image is saved in MRI resolution. Default False.

            .. warning: If you have many time points the file produced can be
                        huge. The default is ``mri_resolution=False``.
        mri_space : bool | None
            Whether the image to world registration should be in mri space. The
            default (None) is mri_space=mri_resolution.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        stc_to : VolSourceEstimate | SourceEstimate | VectorSourceEstimate | Nifti1Image | Nifti2Image
            The morphed source estimates.
        """
        ...

    def compute_vol_morph_mat(self, *, verbose=None):
        """Compute the sparse matrix representation of the volumetric morph.

        Parameters
        ----------

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        morph : instance of SourceMorph
            The instance (modified in-place).

        Notes
        -----
        For a volumetric morph, this will compute the morph for an identity
        source volume, i.e., with one source vertex active at a time, and store
        the result as a `sparse <scipy.sparse.csr_matrix>`
        morphing matrix. This takes a long time (minutes) to compute initially,
        but drastically speeds up `apply` for STCs, so it can be
        beneficial when many time points or many morphs (i.e., greater than
        the number of volumetric ``src_from`` vertices) will be performed.

        When calling `save`, this sparse morphing matrix is saved with
        the instance, so this only needs to be called once. This function does
        nothing if the morph matrix has already been computed, or if there is
        no volume morphing necessary.

        ✨ Added in version 0.22
        """
        ...

    def save(self, fname, overwrite: bool = False, verbose=None) -> None:
        """Save the morph for source estimates to a file.

        Parameters
        ----------
        fname : path-like
            The path to the file. ``'-morph.h5'`` will be added if fname does
            not end with ``'.h5'``.

        overwrite : bool
            If True (default False), overwrite the destination file if it
            exists.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.
        """
        ...

def read_source_morph(fname):
    """Load the morph for source estimates from a file.

    Parameters
    ----------
    fname : path-like
        Path to the file containing the morph source estimates.

    Returns
    -------
    source_morph : instance of SourceMorph
        The loaded morph.
    """
    ...

def grade_to_vertices(subject, grade, subjects_dir=None, n_jobs=None, verbose=None):
    """Convert a grade to source space vertices for a given subject.

    Parameters
    ----------
    subject : str
        Name of the subject.
    grade : int | list
        Resolution of the icosahedral mesh (typically 5). If None, all
        vertices will be used (potentially filling the surface). If a list,
        then values will be morphed to the set of vertices specified in
        in grade[0] and grade[1]. Note that specifying the vertices (e.g.,
        grade=[np.arange(10242), np.arange(10242)] for fsaverage on a
        standard grade 5 source space) can be substantially faster than
        computing vertex locations. Note that if subject='fsaverage'
        and 'grade=5', this set of vertices will automatically be used
        (instead of computed) for speed, since this is a common morph.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    vertices : list of array of int
        Vertex numbers for LH and RH.
    """
    ...
