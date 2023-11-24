from .._fiff.constants import FIFF as FIFF
from .._fiff.meas_info import Info as Info, create_info as create_info
from .._fiff.open import fiff_open as fiff_open
from .._fiff.pick import channel_type as channel_type
from .._fiff.tag import find_tag as find_tag, read_tag as read_tag
from .._fiff.tree import dir_tree_find as dir_tree_find
from .._fiff.write import end_block as end_block, start_and_end_file as start_and_end_file, start_block as start_block, write_coord_trans as write_coord_trans, write_float_matrix as write_float_matrix, write_float_sparse_rcs as write_float_sparse_rcs, write_id as write_id, write_int as write_int, write_int_matrix as write_int_matrix, write_string as write_string
from .._freesurfer import get_mni_fiducials as get_mni_fiducials, get_volume_labels_from_aseg as get_volume_labels_from_aseg, read_freesurfer_lut as read_freesurfer_lut
from ..bem import ConductorModel as ConductorModel, read_bem_surfaces as read_bem_surfaces
from ..parallel import parallel_func as parallel_func
from ..surface import complete_surface_info as complete_surface_info, fast_cross_3d as fast_cross_3d, mesh_dist as mesh_dist, read_surface as read_surface
from ..transforms import Transform as Transform, apply_trans as apply_trans, combine_transforms as combine_transforms, invert_transform as invert_transform
from ..utils import check_fname as check_fname, fill_doc as fill_doc, get_subjects_dir as get_subjects_dir, logger as logger, object_size as object_size, sizeof_fmt as sizeof_fmt, verbose as verbose, warn as warn
from ..viz import plot_alignment as plot_alignment
from _typeshed import Incomplete

class SourceSpaces(list):
    """Export source spaces to nifti or mgz file.

        Parameters
        ----------
        fname : path-like
            Name of nifti or mgz file to write.
        include_surfaces : bool
            If True, include surface source spaces.
        include_discrete : bool
            If True, include discrete source spaces.
        dest : ``'mri'`` | ``'surf'``
            If ``'mri'`` the volume is defined in the coordinate system of the
            original T1 image. If ``'surf'`` the coordinate system of the
            FreeSurfer surface is used (Surface RAS).
        trans : dict, str, or None
            Either a transformation filename (usually made using mne_analyze)
            or an info dict (usually opened using read_trans()). If string, an
            ending of ``.fif`` or ``.fif.gz`` will be assumed to be in FIF
            format, any other ending will be assumed to be a text file with a
            4x4 transformation matrix (like the ``--trans`` MNE-C option.
            Must be provided if source spaces are in head coordinates and
            include_surfaces and mri_resolution are True.
        mri_resolution : bool | str
            If True, the image is saved in MRI resolution
            (e.g. 256 x 256 x 256), and each source region (surface or
            segmentation volume) filled in completely. If "sparse", only a
            single voxel in the high-resolution MRI is filled in for each
            source point.

            .. versionchanged:: 0.21.0
               Support for ``"sparse"`` was added.
        use_lut : bool
            If True, assigns a numeric value to each source space that
            corresponds to a color on the freesurfer lookup table.
        
        overwrite : bool
            If True (default False), overwrite the destination file if it
            exists.

            .. versionadded:: 0.19
        
        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Notes
        -----
        This method requires nibabel.
        """
    info: Incomplete

    def __init__(self, source_spaces, info: Incomplete | None=...) -> None:
        ...

    @property
    def kind(self):
        ...

    def plot(self, head: bool=..., brain: Incomplete | None=..., skull: Incomplete | None=..., subjects_dir: Incomplete | None=..., trans: Incomplete | None=..., verbose: Incomplete | None=...):
        """Plot the source space.

        Parameters
        ----------
        head : bool
            If True, show head surface.
        brain : bool | str
            If True, show the brain surfaces. Can also be a str for
            surface type (e.g., ``'pial'``, same as True). Default is None,
            which means ``'white'`` for surface source spaces and ``False``
            otherwise.
        skull : bool | str | list of str | list of dict | None
            Whether to plot skull surface. If string, common choices would be
            ``'inner_skull'``, or ``'outer_skull'``. Can also be a list to plot
            multiple skull surfaces. If a list of dicts, each dict must
            contain the complete surface info (such as you get from
            :func:`mne.make_bem_model`). True is an alias of 'outer_skull'.
            The subjects bem and bem/flash folders are searched for the 'surf'
            files. Defaults to None, which is False for surface source spaces,
            and True otherwise.
        subjects_dir : path-like | None
            Path to ``SUBJECTS_DIR`` if it is not set in the environment.
        trans : path-like | ``'auto'`` | dict | None
            The full path to the head<->MRI transform ``*-trans.fif`` file
            produced during coregistration. If trans is None, an identity
            matrix is assumed. This is only needed when the source space is in
            head coordinates.
        
        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        fig : instance of Figure3D
            The figure.
        """

    def __getitem__(self, *args, **kwargs):
        """Get an item."""

    def __add__(self, other):
        """Combine source spaces."""

    def copy(self):
        """Make a copy of the source spaces.

        Returns
        -------
        src : instance of SourceSpaces
            The copied source spaces.
        """

    def __deepcopy__(self, memodict):
        """Make a deepcopy."""

    def save(self, fname, overwrite: bool=..., *, verbose: Incomplete | None=...) -> None:
        """Save the source spaces to a fif file.

        Parameters
        ----------
        fname : path-like
            File to write, which should end with ``-src.fif`` or ``-src.fif.gz``.
        
        overwrite : bool
            If True (default False), overwrite the destination file if it
            exists.
        
        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.
        """

    def export_volume(self, fname, include_surfaces: bool=..., include_discrete: bool=..., dest: str=..., trans: Incomplete | None=..., mri_resolution: bool=..., use_lut: bool=..., overwrite: bool=..., verbose: Incomplete | None=...) -> None:
        """Export source spaces to nifti or mgz file.

        Parameters
        ----------
        fname : path-like
            Name of nifti or mgz file to write.
        include_surfaces : bool
            If True, include surface source spaces.
        include_discrete : bool
            If True, include discrete source spaces.
        dest : ``'mri'`` | ``'surf'``
            If ``'mri'`` the volume is defined in the coordinate system of the
            original T1 image. If ``'surf'`` the coordinate system of the
            FreeSurfer surface is used (Surface RAS).
        trans : dict, str, or None
            Either a transformation filename (usually made using mne_analyze)
            or an info dict (usually opened using read_trans()). If string, an
            ending of ``.fif`` or ``.fif.gz`` will be assumed to be in FIF
            format, any other ending will be assumed to be a text file with a
            4x4 transformation matrix (like the ``--trans`` MNE-C option.
            Must be provided if source spaces are in head coordinates and
            include_surfaces and mri_resolution are True.
        mri_resolution : bool | str
            If True, the image is saved in MRI resolution
            (e.g. 256 x 256 x 256), and each source region (surface or
            segmentation volume) filled in completely. If "sparse", only a
            single voxel in the high-resolution MRI is filled in for each
            source point.

            .. versionchanged:: 0.21.0
               Support for ``"sparse"`` was added.
        use_lut : bool
            If True, assigns a numeric value to each source space that
            corresponds to a color on the freesurfer lookup table.
        
        overwrite : bool
            If True (default False), overwrite the destination file if it
            exists.

            .. versionadded:: 0.19
        
        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Notes
        -----
        This method requires nibabel.
        """

def read_source_spaces(fname, patch_stats: bool=..., verbose: Incomplete | None=...):
    """Read the source spaces from a FIF file.

    Parameters
    ----------
    fname : path-like
        The name of the file, which should end with ``-src.fif`` or
        ``-src.fif.gz``.
    patch_stats : bool, optional (default False)
        Calculate and add cortical patch statistics to the surfaces.
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    src : SourceSpaces
        The source spaces.

    See Also
    --------
    write_source_spaces, setup_source_space, setup_volume_source_space
    """

def find_source_space_hemi(src):
    """Return the hemisphere id for a source space.

    Parameters
    ----------
    src : dict
        The source space to investigate.

    Returns
    -------
    hemi : int
        Deduced hemisphere id.
    """

def label_src_vertno_sel(label, src):
    """Find vertex numbers and indices from label.

    Parameters
    ----------
    label : Label
        Source space label.
    src : dict
        Source space.

    Returns
    -------
    vertices : list of length 2
        Vertex numbers for lh and rh.
    src_sel : array of int (len(idx) = len(vertices[0]) + len(vertices[1]))
        Indices of the selected vertices in sourse space.
    """

def write_source_spaces(fname, src, *, overwrite: bool=..., verbose: Incomplete | None=...) -> None:
    """Write source spaces to a file.

    Parameters
    ----------
    fname : path-like
        The name of the file, which should end with ``-src.fif`` or
        ``-src.fif.gz``.
    src : instance of SourceSpaces
        The source spaces (as returned by read_source_spaces).
    
    overwrite : bool
        If True (default False), overwrite the destination file if it
        exists.
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    read_source_spaces
    """

def setup_source_space(subject, spacing: str=..., surface: str=..., subjects_dir: Incomplete | None=..., add_dist: bool=..., n_jobs: Incomplete | None=..., *, verbose: Incomplete | None=...):
    """Set up bilateral hemisphere surface-based source space with subsampling.

    Parameters
    ----------
    
    subject : str
        The FreeSurfer subject name.
    spacing : str
        The spacing to use. Can be ``'ico#'`` for a recursively subdivided
        icosahedron, ``'oct#'`` for a recursively subdivided octahedron,
        ``'all'`` for all points, or an integer to use approximate
        distance-based spacing (in mm).

        .. versionchanged:: 0.18
           Support for integers for distance-based spacing.
    surface : str
        The surface to use.
    
    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    add_dist : bool | str
        Add distance and patch information to the source space. This takes some
        time so precomputing it is recommended. Can also be 'patch' to only
        compute patch information.

        .. versionchanged:: 0.20
           Support for ``add_dist='patch'``.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the :mod:`joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a :class:`joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.
        Ignored if ``add_dist=='patch'``.
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    src : SourceSpaces
        The source space for each hemisphere.

    See Also
    --------
    setup_volume_source_space
    """

def setup_volume_source_space(subject: Incomplete | None=..., pos: float=..., mri: Incomplete | None=..., sphere: Incomplete | None=..., bem: Incomplete | None=..., surface: Incomplete | None=..., mindist: float=..., exclude: float=..., subjects_dir: Incomplete | None=..., volume_label: Incomplete | None=..., add_interpolator: bool=..., sphere_units: str=..., single_volume: bool=..., *, n_jobs: Incomplete | None=..., verbose: Incomplete | None=...):
    """Set up a volume source space with grid spacing or discrete source space.

    Parameters
    ----------
    subject : str | None
        Subject to process. If None, the path to the MRI volume must be
        absolute to get a volume source space. If a subject name
        is provided the ``T1.mgz`` file will be found automatically.
        Defaults to None.
    pos : float | dict
        Positions to use for sources. If float, a grid will be constructed
        with the spacing given by ``pos`` in mm, generating a volume source
        space. If dict, ``pos['rr']`` and ``pos['nn']`` will be used as the source
        space locations (in meters) and normals, respectively, creating a
        discrete source space.

        .. note:: For a discrete source space (``pos`` is a dict),
                  ``mri`` must be None.
    mri : str | None
        The filename of an MRI volume (mgh or mgz) to create the
        interpolation matrix over. Source estimates obtained in the
        volume source space can then be morphed onto the MRI volume
        using this interpolator. If pos is a dict, this cannot be None.
        If subject name is provided, ``pos`` is a float or ``volume_label``
        are not provided then the ``mri`` parameter will default to ``'T1.mgz'``
        or ``aseg.mgz``, respectively, else it will stay None.
    sphere : ndarray, shape (4,) | ConductorModel | None
        Define spherical source space bounds using origin and radius given
        by ``(Ox, Oy, Oz, rad)`` in ``sphere_units``.
        Only used if ``bem`` and ``surface`` are both None. Can also be a
        spherical ConductorModel, which will use the origin and radius.
        None (the default) uses a head-digitization fit.
    bem : path-like | None | ConductorModel
        Define source space bounds using a BEM file (specifically the inner
        skull surface) or a :class:`~mne.bem.ConductorModel` for a 1-layer of 3-layers
        BEM. See :func:`~mne.make_bem_model` and :func:`~mne.make_bem_solution` to
        create a :class:`~mne.bem.ConductorModel`. If provided, ``surface`` must be
        None.
    surface : path-like | dict | None
        Define source space bounds using a FreeSurfer surface file. Can
        also be a dictionary with entries ``'rr'`` and ``'tris'``, such as
        those returned by :func:`mne.read_surface`. If provided, ``bem`` must be None.
    mindist : float
        Exclude points closer than this distance (mm) to the bounding surface.
    exclude : float
        Exclude points closer than this distance (mm) from the center of mass
        of the bounding surface.
    
    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    volume_label : str | dict | list | None
        Region(s) of interest to use. None (default) will create a single
        whole-brain source space. Otherwise, a separate source space will be
        created for each entry in the list or dict (str will be turned into
        a single-element list). If list of str, standard Freesurfer labels
        are assumed. If dict, should be a mapping of region names to atlas
        id numbers, allowing the use of other atlases.

        .. versionchanged:: 0.21.0
           Support for dict added.
    add_interpolator : bool
        If True and ``mri`` is not None, then an interpolation matrix
        will be produced.
    sphere_units : str
        Defaults to ``"m"``.

        .. versionadded:: 0.20
    single_volume : bool
        If True, multiple values of ``volume_label`` will be merged into a
        a single source space instead of occupying multiple source spaces
        (one for each sub-volume), i.e., ``len(src)`` will be ``1`` instead of
        ``len(volume_label)``. This can help conserve memory and disk space
        when many labels are used.

        .. versionadded:: 0.21
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the :mod:`joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a :class:`joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.

        .. versionadded:: 1.6
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    src : SourceSpaces
        A :class:`SourceSpaces` object containing one source space for each
        entry of ``volume_labels``, or a single source space if
        ``volume_labels`` was not specified.

    See Also
    --------
    setup_source_space

    Notes
    -----
    Volume source spaces are related to an MRI image such as T1 and allow to
    visualize source estimates overlaid on MRIs and to morph estimates
    to a template brain for group analysis. Discrete source spaces
    don't allow this. If you provide a subject name the T1 MRI will be
    used by default.

    When you work with a source space formed from a grid you need to specify
    the domain in which the grid will be defined. There are three ways
    of specifying this:
    (i) sphere, (ii) bem model, and (iii) surface.
    The default behavior is to use sphere model
    (``sphere=(0.0, 0.0, 0.0, 90.0)``) if ``bem`` or ``surface`` is not
    ``None`` then ``sphere`` is ignored.
    If you're going to use a BEM conductor model for forward model
    it is recommended to pass it here.

    To create a discrete source space, ``pos`` must be a dict, ``mri`` must be
    None, and ``volume_label`` must be None. To create a whole brain volume
    source space, ``pos`` must be a float and 'mri' must be provided.

    To create a volume source space from label, ``pos`` must be a float,
    ``volume_label`` must be provided, and 'mri' must refer to a .mgh or .mgz
    file with values corresponding to the freesurfer lookup-table (typically
    ``aseg.mgz``).
    """

def add_source_space_distances(src, dist_limit=..., n_jobs: Incomplete | None=..., *, verbose: Incomplete | None=...):
    """Compute inter-source distances along the cortical surface.

    This function will also try to add patch info for the source space.
    It will only occur if the ``dist_limit`` is sufficiently high that all
    points on the surface are within ``dist_limit`` of a point in the
    source space.

    Parameters
    ----------
    src : instance of SourceSpaces
        The source spaces to compute distances for.
    dist_limit : float
        The upper limit of distances to include (in meters).
        Note: if limit < np.inf, scipy > 0.13 (bleeding edge as of
        10/2013) must be installed. If 0, then only patch (nearest vertex)
        information is added.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the :mod:`joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a :class:`joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.
        Ignored if ``dist_limit==0.``.
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    src : instance of SourceSpaces
        The original source spaces, with distance information added.
        The distances are stored in src[n]['dist'].
        Note: this function operates in-place.

    Notes
    -----
    This function can be memory- and CPU-intensive. On a high-end machine
    (2012) running 6 jobs in parallel, an ico-5 (10242 per hemi) source space
    takes about 10 minutes to compute all distances (``dist_limit = np.inf``).
    With ``dist_limit = 0.007``, computing distances takes about 1 minute.

    We recommend computing distances once per source space and then saving
    the source space to disk, as the computed distances will automatically be
    stored along with the source space data for future use.
    """

def get_volume_labels_from_src(src, subject, subjects_dir):
    """Return a list of Label of segmented volumes included in the src space.

    Parameters
    ----------
    src : instance of SourceSpaces
        The source space containing the volume regions.
    
    subject : str
        The FreeSurfer subject name.
    subjects_dir : str
        Freesurfer folder of the subjects.

    Returns
    -------
    labels_aseg : list of Label
        List of Label of segmented volumes included in src space.
    """

def morph_source_spaces(src_from, subject_to, surf: str=..., subject_from: Incomplete | None=..., subjects_dir: Incomplete | None=..., verbose: Incomplete | None=...):
    """Morph an existing source space to a different subject.

    .. warning:: This can be used in place of morphing source estimates for
                 multiple subjects, but there may be consequences in terms
                 of dipole topology.

    Parameters
    ----------
    src_from : instance of SourceSpaces
        Surface source spaces to morph.
    subject_to : str
        The destination subject.
    surf : str
        The brain surface to use for the new source space.
    subject_from : str | None
        The "from" subject. For most source spaces this shouldn't need
        to be provided, since it is stored in the source space itself.
    subjects_dir : path-like | None
        Path to ``SUBJECTS_DIR`` if it is not set in the environment.
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    src : instance of SourceSpaces
        The morphed source spaces.

    Notes
    -----
    .. versionadded:: 0.10.0
    """

def compute_distance_to_sensors(src, info, picks: Incomplete | None=..., trans: Incomplete | None=..., verbose: Incomplete | None=...):
    """Compute distances between vertices and sensors.

    Parameters
    ----------
    src : instance of SourceSpaces
        The object with vertex positions for which to compute distances to
        sensors.
    
    info : mne.Info | None
        The :class:`mne.Info` object with information about the sensors and methods of measurement. Must contain sensor positions to which distances shall
        be computed.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as 
        channel indices. In lists, channel *type* strings (e.g., ``['meg', 
        'eeg']``) will pick channels of those types, channel *name* strings (e.g., 
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the 
        string values "all" to pick all channels, or "data" to pick :term:`data 
        channels`. None (default) will pick good data channels. Note that channels 
        in ``info['bads']`` *will be included* if their names or indices are 
        explicitly provided.
    
    trans : str | dict | instance of Transform
        If str, the path to the head<->MRI transform ``*-trans.fif`` file produced
        during coregistration. Can also be ``'fsaverage'`` to use the built-in
        fsaverage transformation.
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    depth : array of shape (n_vertices, n_channels)
        The Euclidean distances of source space vertices with respect to
        sensors.
    """

def get_decimated_surfaces(src):
    """Get the decimated surfaces from a source space.

    Parameters
    ----------
    src : instance of SourceSpaces | path-like
        The source space with decimated surfaces.

    Returns
    -------
    surfaces : list of dict
        The decimated surfaces present in the source space. Each dict
        which contains 'rr' and 'tris' keys for vertices positions and
        triangle indices.

    Notes
    -----
    .. versionadded:: 1.0
    """