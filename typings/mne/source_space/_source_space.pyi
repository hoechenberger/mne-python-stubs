from .._fiff.constants import FIFF as FIFF
from .._fiff.meas_info import Info as Info, create_info as create_info
from .._fiff.open import fiff_open as fiff_open
from .._fiff.pick import channel_type as channel_type
from .._fiff.tag import find_tag as find_tag, read_tag as read_tag
from .._fiff.tree import dir_tree_find as dir_tree_find
from .._fiff.write import (
    end_block as end_block,
    start_and_end_file as start_and_end_file,
    start_block as start_block,
    write_coord_trans as write_coord_trans,
    write_float_matrix as write_float_matrix,
    write_float_sparse_rcs as write_float_sparse_rcs,
    write_id as write_id,
    write_int as write_int,
    write_int_matrix as write_int_matrix,
    write_string as write_string,
)
from .._freesurfer import (
    get_mni_fiducials as get_mni_fiducials,
    get_volume_labels_from_aseg as get_volume_labels_from_aseg,
    read_freesurfer_lut as read_freesurfer_lut,
)
from ..bem import (
    ConductorModel as ConductorModel,
    read_bem_surfaces as read_bem_surfaces,
)
from ..parallel import parallel_func as parallel_func
from ..surface import (
    complete_surface_info as complete_surface_info,
    fast_cross_3d as fast_cross_3d,
    mesh_dist as mesh_dist,
    read_surface as read_surface,
)
from ..transforms import (
    Transform as Transform,
    apply_trans as apply_trans,
    combine_transforms as combine_transforms,
    invert_transform as invert_transform,
)
from ..utils import (
    check_fname as check_fname,
    fill_doc as fill_doc,
    get_subjects_dir as get_subjects_dir,
    logger as logger,
    object_size as object_size,
    sizeof_fmt as sizeof_fmt,
    warn as warn,
)
from ..viz import plot_alignment as plot_alignment
from _typeshed import Incomplete

class SourceSpaces(list):
    """## 🧠 Represent a list of source space.

    This class acts like a list of dictionaries containing the source
    space information, one entry in the list per source space type. See
    Notes for details.

    ### ⛔️ Warning
        This class should not be created or modified by the end user. Use
        `mne.setup_source_space`, `mne.setup_volume_source_space`,
        or `mne.read_source_spaces` to create `SourceSpaces`.

    -----
    ### 🛠️ Parameters

    #### `source_spaces : list`
        A list of dictionaries containing the source space information.
    #### `info : dict | None`
        Dictionary with information about the creation of the source space
        file. Has keys ``'working_dir'`` and ``'command_line'``.

    -----
    ### 📊 Attributes

    #### `kind : ``'surface'`` | ``'volume'`` | ``'discrete'`` | ``'mixed'```
        The kind of source space.
    #### `info : dict`
        Dictionary with information about the creation of the source space
        file. Has keys ``'working_dir'`` and ``'command_line'``.

    -----
    ### 👉 See Also

    mne.setup_source_space : Setup a surface source space.
    mne.setup_volume_source_space : Setup a volume source space.
    mne.read_source_spaces : Read source spaces from a file.

    -----
    ### 📖 Notes

    Each element in SourceSpaces (e.g., ``src[0]``) is a dictionary. For
    example, a surface source space will have ``len(src) == 2``, one entry for
    each hemisphere. A volume source space will have ``len(src) == 1`` if it
    uses a single monolithic grid, or ``len(src) == len(volume_label)`` when
    created with a list-of-atlas-labels. A mixed source space consists of both
    surface and volumetric source spaces in a single SourceSpaces object.

    Each of those dictionaries can be accessed using standard Python
    `python:dict` access using the string keys listed below (e.g.,
    ``src[0]['type'] == 'surf'``). The relevant key/value pairs depend on
    the source space type:

    `Relevant to all source spaces`

    The following are always present:

        #### `id : int`
            The FIF ID, either ``FIFF.FIFFV_MNE_SURF_LEFT_HEMI`` or
            ``FIFF.FIFFV_MNE_SURF_RIGHT_HEMI`` for surfaces, or
            ``FIFF.FIFFV_MNE_SURF_UNKNOWN`` for volume source spaces.
        #### `type : str`
            The type of source space, one of ``{'surf', 'vol', 'discrete'}``.
        #### `np : int`
            Number of vertices in the dense surface or complete volume.
        #### `coord_frame : int`
            The coordinate frame, usually ``FIFF.FIFFV_COORD_MRI``.
        #### `rr : ndarray, shape (np, 3)`
            The dense surface or complete volume vertex locations.
        #### `nn : ndarray, shape (np, 3)`
            The dense surface or complete volume normals.
        #### `nuse : int`
            The number of points in the subsampled surface.
        #### `inuse : ndarray, shape (np,)`
            An integer array defining whether each dense surface vertex is used
            (``1``) or unused (``0``).
        #### `vertno : ndarray, shape (n_src,)`
            The vertex numbers of the dense surface or complete volume that are
            used (i.e., ``np.where(src[0]['inuse'])[0]``).
        #### `subject_his_id : str`
            The FreeSurfer subject name.

    `Surface source spaces`

    Surface source spaces created using `mne.setup_source_space` can have
    the following additional entries (which will be missing, or have values of
    ``None`` or ``0`` for volumetric source spaces):

        #### `ntri : int`
            Number of triangles in the dense surface triangulation.
        #### `tris : ndarray, shape (ntri, 3)`
            The dense surface triangulation.
        #### `nuse_tri : int`
            The number of triangles in the subsampled surface.
        #### `use_tris : ndarray, shape (nuse_tri, 3)`
            The subsampled surface triangulation.
        #### `dist : scipy.sparse.csr_matrix, shape (n_src, n_src) | None`
            The distances (euclidean for volume, along the cortical surface for
            surfaces) between source points.
        #### `dist_limit : float`
            The maximum distance allowed for inclusion in ``nearest``.
        #### `pinfo : list of ndarray`
            For each vertex in the subsampled surface, the indices of the
            vertices in the dense surface that it represents (i.e., is closest
            to of all subsampled indices), e.g. for the left hemisphere
            (here constructed for ``sample`` with ``spacing='oct-6'``),
            which vertices did we choose? Note the first is 14::

                >>> src[0]['vertno']  # doctest:+SKIP
                array([    14,     54,     59, ..., 155295, 155323, 155330])

            And which dense surface verts did our vertno[0] (14 on dense) represent? ::

                >>> src[0]['pinfo'][0]  # doctest:+SKIP
                array([  6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17,  18,
                        19,  20,  21,  22,  23,  24,  25,  29,  30,  31,  39, 134, 135,
                       136, 137, 138, 139, 141, 142, 143, 144, 149, 150, 151, 152, 156,
                       162, 163, 173, 174, 185, 448, 449, 450, 451, 452, 453, 454, 455,
                       456, 462, 463, 464, 473, 474, 475, 485, 496, 497, 512, 864, 876,
                       881, 889, 890, 904])

        #### `patch_inds : ndarray, shape (n_src_remaining,)`
            The patch indices that have been retained (if relevant, following
            forward computation. After just `mne.setup_source_space`,
            this will be ``np.arange(src[0]['nuse'])``. After forward
            computation, some vertices can be excluded, in which case this
            tells you which patches (of the original ``np.arange(nuse)``)
            are still in use. So if some vertices have been excluded, the
            line above for ``pinfo`` for completeness should be (noting that
            the first subsampled vertex ([0]) represents the following dense
            vertices)::

                >>> src[0]['pinfo'][src[0]['patch_inds'][0]]  # doctest:+SKIP
                array([  6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17,  18,
                        19,  20,  21,  22,  23,  24,  25,  29,  30,  31,  39, 134, 135,
                       136, 137, 138, 139, 141, 142, 143, 144, 149, 150, 151, 152, 156,
                       162, 163, 173, 174, 185, 448, 449, 450, 451, 452, 453, 454, 455,
                       456, 462, 463, 464, 473, 474, 475, 485, 496, 497, 512, 864, 876,
                       881, 889, 890, 904])

        #### `nearest : ndarray, shape (np,)`
            For each vertex on the dense surface, this gives the vertex index
            (in the dense surface) that each dense surface vertex is closest to
            of the vertices chosen for subsampling. This is essentially the
            reverse map off ``pinfo``, e.g.::

                >>> src[0]['nearest'].shape  # doctest:+SKIP
                (115407,)

            Based on ``pinfo`` above, this should be 14:

                >>> src[0]['nearest'][6]  # doctest:+SKIP
                14

        #### `nearest_dist : ndarray, shape (np,)`
            The distances corresponding to ``nearest``.

    `Volume source spaces`

    Volume source spaces created using `mne.setup_volume_source_space`
    can have the following additional entries (which will be missing, or
    have values of ``None`` or ``0`` for surface source spaces):

        #### `mri_width, mri_height, mri_depth : int`
            The MRI dimensions (in voxels).
        #### `neighbor_vert : ndarray`
            The 26-neighborhood information for each vertex.
        #### `interpolator : scipy.sparse.csr_matrix | None`
            The linear interpolator to go from the subsampled volume vertices
            to the high-resolution volume.
        #### `shape : tuple of int`
            The shape of the subsampled grid.
        #### `mri_ras_t : instance of `mne.transforms.Transform``
            The transformation from MRI surface RAS (``FIFF.FIFFV_COORD_MRI``)
            to MRI scanner RAS (``FIFF.FIFFV_MNE_COORD_RAS``).
        #### `src_mri_t : instance of `mne.transforms.Transform``
            The transformation from subsampled source space voxel to MRI
            surface RAS.
        #### `vox_mri_t : instance of `mne.transforms.Transform``
            The transformation from the original MRI voxel
            (``FIFF.FIFFV_MNE_COORD_MRI_VOXEL``) space to MRI surface RAS.
        #### `mri_volume_name : str`
            The MRI volume name, e.g. ``'subjects_dir/subject/mri/T1.mgz'``.
        #### `seg_name : str`
            The MRI atlas segmentation name (e.g., ``'Left-Cerebellum-Cortex'``
            from the parameter ``volume_label``).

    Source spaces also have some attributes that are accessible via ``.``
    access, like ``src.kind``.
    """

    info: Incomplete

    def __init__(self, source_spaces, info=None) -> None: ...
    @property
    def kind(self): ...
    def plot(
        self,
        head: bool = False,
        brain=None,
        skull=None,
        subjects_dir=None,
        trans=None,
        verbose=None,
    ):
        """## 🧠 Plot the source space.

        -----
        ### 🛠️ Parameters

        #### `head : bool`
            If True, show head surface.
        #### `brain : bool | str`
            If True, show the brain surfaces. Can also be a str for
            surface type (e.g., ``'pial'``, same as True). Default is None,
            which means ``'white'`` for surface source spaces and ``False``
            otherwise.
        #### `skull : bool | str | list of str | list of dict | None`
            Whether to plot skull surface. If string, common choices would be
            ``'inner_skull'``, or ``'outer_skull'``. Can also be a list to plot
            multiple skull surfaces. If a list of dicts, each dict must
            contain the complete surface info (such as you get from
            `mne.make_bem_model`). True is an alias of 'outer_skull'.
            The subjects bem and bem/flash folders are searched for the 'surf'
            files. Defaults to None, which is False for surface source spaces,
            and True otherwise.
        #### `subjects_dir : path-like | None`
            Path to ``SUBJECTS_DIR`` if it is not set in the environment.
        #### `trans : path-like | ``'auto'`` | dict | None`
            The full path to the head<->MRI transform ``*-trans.fif`` file
            produced during coregistration. If trans is None, an identity
            matrix is assumed. This is only needed when the source space is in
            head coordinates.

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns

        #### `fig : instance of Figure3D`
            The figure.
        """
        ...
    def __getitem__(self, *args, **kwargs):
        """## 🧠 Get an item."""
        ...
    def __add__(self, other):
        """## 🧠 Combine source spaces."""
        ...
    def copy(self):
        """## 🧠 Make a copy of the source spaces.

        -----
        ### ⏎ Returns

        #### `src : instance of SourceSpaces`
            The copied source spaces.
        """
        ...
    def __deepcopy__(self, memodict):
        """## 🧠 Make a deepcopy."""
        ...
    def save(self, fname, overwrite: bool = False, *, verbose=None) -> None:
        """## 🧠 Save the source spaces to a fif file.

        -----
        ### 🛠️ Parameters

        #### `fname : path-like`
            File to write, which should end with ``-src.fif`` or ``-src.fif.gz``.

        #### `overwrite : bool`
            If True (default False), overwrite the destination file if it
            exists.

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.
        """
        ...
    def export_volume(
        self,
        fname,
        include_surfaces: bool = True,
        include_discrete: bool = True,
        dest: str = "mri",
        trans=None,
        mri_resolution: bool = False,
        use_lut: bool = True,
        overwrite: bool = False,
        verbose=None,
    ) -> None:
        """## 🧠 Export source spaces to nifti or mgz file.

        -----
        ### 🛠️ Parameters

        #### `fname : path-like`
            Name of nifti or mgz file to write.
        #### `include_surfaces : bool`
            If True, include surface source spaces.
        #### `include_discrete : bool`
            If True, include discrete source spaces.
        #### `dest : ``'mri'`` | ``'surf'```
            If ``'mri'`` the volume is defined in the coordinate system of the
            original T1 image. If ``'surf'`` the coordinate system of the
            FreeSurfer surface is used (Surface RAS).
        #### `trans : dict, str, or None`
            Either a transformation filename (usually made using mne_analyze)
            or an info dict (usually opened using read_trans()). If string, an
            ending of ``.fif`` or ``.fif.gz`` will be assumed to be in FIF
            format, any other ending will be assumed to be a text file with a
            4x4 transformation matrix (like the ``--trans`` MNE-C option.
            Must be provided if source spaces are in head coordinates and
            include_surfaces and mri_resolution are True.
        #### `mri_resolution : bool | str`
            If True, the image is saved in MRI resolution
            (e.g. 256 x 256 x 256), and each source region (surface or
            segmentation volume) filled in completely. If "sparse", only a
            single voxel in the high-resolution MRI is filled in for each
            source point.

            🎭 Changed in version 0.21.0
               Support for ``"sparse"`` was added.
        #### `use_lut : bool`
            If True, assigns a numeric value to each source space that
            corresponds to a color on the freesurfer lookup table.

        #### `overwrite : bool`
            If True (default False), overwrite the destination file if it
            exists.

            ✨ Added in vesion 0.19

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### 📖 Notes

        This method requires nibabel.
        """
        ...

def read_source_spaces(fname, patch_stats: bool = False, verbose=None):
    """## 🧠 Read the source spaces from a FIF file.

    -----
    ### 🛠️ Parameters

    #### `fname : path-like`
        The name of the file, which should end with ``-src.fif`` or
        ``-src.fif.gz``.
    #### `patch_stats : bool, optional (default False)`
        Calculate and add cortical patch statistics to the surfaces.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `src : SourceSpaces`
        The source spaces.

    -----
    ### 👉 See Also

    write_source_spaces, setup_source_space, setup_volume_source_space
    """
    ...

def find_source_space_hemi(src):
    """## 🧠 Return the hemisphere id for a source space.

    -----
    ### 🛠️ Parameters

    #### `src : dict`
        The source space to investigate.

    -----
    ### ⏎ Returns

    #### `hemi : int`
        Deduced hemisphere id.
    """
    ...

def label_src_vertno_sel(label, src):
    """## 🧠 Find vertex numbers and indices from label.

    -----
    ### 🛠️ Parameters

    #### `label : Label`
        Source space label.
    #### `src : dict`
        Source space.

    -----
    ### ⏎ Returns

    #### `vertices : list of length 2`
        Vertex numbers for lh and rh.
    #### `src_sel : array of int (len(idx) = len(vertices[0]) + len(vertices[1]))`
        Indices of the selected vertices in sourse space.
    """
    ...

def write_source_spaces(fname, src, *, overwrite: bool = False, verbose=None) -> None:
    """## 🧠 Write source spaces to a file.

    -----
    ### 🛠️ Parameters

    #### `fname : path-like`
        The name of the file, which should end with ``-src.fif`` or
        ``-src.fif.gz``.
    #### `src : instance of SourceSpaces`
        The source spaces (as returned by read_source_spaces).

    #### `overwrite : bool`
        If True (default False), overwrite the destination file if it
        exists.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### 👉 See Also

    read_source_spaces
    """
    ...

def setup_source_space(
    subject,
    spacing: str = "oct6",
    surface: str = "white",
    subjects_dir=None,
    add_dist: bool = True,
    n_jobs=None,
    *,
    verbose=None,
):
    """## 🧠 Set up bilateral hemisphere surface-based source space with subsampling.

    -----
    ### 🛠️ Parameters


    #### `subject : str`
        The FreeSurfer subject name.
    #### `spacing : str`
        The spacing to use. Can be ``'ico#'`` for a recursively subdivided
        icosahedron, ``'oct#'`` for a recursively subdivided octahedron,
        ``'all'`` for all points, or an integer to use approximate
        distance-based spacing (in mm).

        🎭 Changed in version 0.18
           Support for integers for distance-based spacing.
    #### `surface : str`
        The surface to use.

    #### `subjects_dir : path-like | None`
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    #### `add_dist : bool | str`
        Add distance and patch information to the source space. This takes some
        time so precomputing it is recommended. Can also be 'patch' to only
        compute patch information.

        🎭 Changed in version 0.20
           Support for ``add_dist='patch'``.
    #### `n_jobs : int | None`
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.
        Ignored if ``add_dist=='patch'``.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `src : SourceSpaces`
        The source space for each hemisphere.

    -----
    ### 👉 See Also

    setup_volume_source_space
    """
    ...

def setup_volume_source_space(
    subject=None,
    pos: float = 5.0,
    mri=None,
    sphere=None,
    bem=None,
    surface=None,
    mindist: float = 5.0,
    exclude: float = 0.0,
    subjects_dir=None,
    volume_label=None,
    add_interpolator: bool = True,
    sphere_units: str = "m",
    single_volume: bool = False,
    *,
    n_jobs=None,
    verbose=None,
):
    """## 🧠 Set up a volume source space with grid spacing or discrete source space.

    -----
    ### 🛠️ Parameters

    #### `subject : str | None`
        Subject to process. If None, the path to the MRI volume must be
        absolute to get a volume source space. If a subject name
        is provided the ``T1.mgz`` file will be found automatically.
        Defaults to None.
    #### `pos : float | dict`
        Positions to use for sources. If float, a grid will be constructed
        with the spacing given by ``pos`` in mm, generating a volume source
        space. If dict, ``pos['rr']`` and ``pos['nn']`` will be used as the source
        space locations (in meters) and normals, respectively, creating a
        discrete source space.

        ### 💡 Note For a discrete source space (``pos`` is a dict),
                  ``mri`` must be None.
    #### `mri : str | None`
        The filename of an MRI volume (mgh or mgz) to create the
        interpolation matrix over. Source estimates obtained in the
        volume source space can then be morphed onto the MRI volume
        using this interpolator. If pos is a dict, this cannot be None.
        If subject name is provided, ``pos`` is a float or ``volume_label``
        are not provided then the ``mri`` parameter will default to ``'T1.mgz'``
        or ``aseg.mgz``, respectively, else it will stay None.
    #### `sphere : ndarray, shape (4,) | ConductorModel | None`
        Define spherical source space bounds using origin and radius given
        by ``(Ox, Oy, Oz, rad)`` in ``sphere_units``.
        Only used if ``bem`` and ``surface`` are both None. Can also be a
        spherical ConductorModel, which will use the origin and radius.
        None (the default) uses a head-digitization fit.
    #### `bem : path-like | None | ConductorModel`
        Define source space bounds using a BEM file (specifically the inner
        skull surface) or a `mne.bem.ConductorModel` for a 1-layer of 3-layers
        BEM. See `mne.make_bem_model` and `mne.make_bem_solution` to
        create a `mne.bem.ConductorModel`. If provided, ``surface`` must be
        None.
    #### `surface : path-like | dict | None`
        Define source space bounds using a FreeSurfer surface file. Can
        also be a dictionary with entries ``'rr'`` and ``'tris'``, such as
        those returned by `mne.read_surface`. If provided, ``bem`` must be None.
    #### `mindist : float`
        Exclude points closer than this distance (mm) to the bounding surface.
    #### `exclude : float`
        Exclude points closer than this distance (mm) from the center of mass
        of the bounding surface.

    #### `subjects_dir : path-like | None`
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    #### `volume_label : str | dict | list | None`
        Region(s) of interest to use. None (default) will create a single
        whole-brain source space. Otherwise, a separate source space will be
        created for each entry in the list or dict (str will be turned into
        a single-element list). If list of str, standard Freesurfer labels
        are assumed. If dict, should be a mapping of region names to atlas
        id numbers, allowing the use of other atlases.

        🎭 Changed in version 0.21.0
           Support for dict added.
    #### `add_interpolator : bool`
        If True and ``mri`` is not None, then an interpolation matrix
        will be produced.
    #### `sphere_units : str`
        Defaults to ``"m"``.

        ✨ Added in vesion 0.20
    #### `single_volume : bool`
        If True, multiple values of ``volume_label`` will be merged into a
        a single source space instead of occupying multiple source spaces
        (one for each sub-volume), i.e., ``len(src)`` will be ``1`` instead of
        ``len(volume_label)``. This can help conserve memory and disk space
        when many labels are used.

        ✨ Added in vesion 0.21
    #### `n_jobs : int | None`
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.

        ✨ Added in vesion 1.6

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `src : SourceSpaces`
        A `SourceSpaces` object containing one source space for each
        entry of ``volume_labels``, or a single source space if
        ``volume_labels`` was not specified.

    -----
    ### 👉 See Also

    setup_source_space

    -----
    ### 📖 Notes

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
    ...

def add_source_space_distances(src, dist_limit=..., n_jobs=None, *, verbose=None):
    """## 🧠 Compute inter-source distances along the cortical surface.

    This function will also try to add patch info for the source space.
    It will only occur if the ``dist_limit`` is sufficiently high that all
    points on the surface are within ``dist_limit`` of a point in the
    source space.

    -----
    ### 🛠️ Parameters

    #### `src : instance of SourceSpaces`
        The source spaces to compute distances for.
    #### `dist_limit : float`
        The upper limit of distances to include (in meters).
        Note: if limit < np.inf, scipy > 0.13 (bleeding edge as of
        10/2013) must be installed. If 0, then only patch (nearest vertex)
        information is added.
    #### `n_jobs : int | None`
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.
        Ignored if ``dist_limit==0.``.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `src : instance of SourceSpaces`
        The original source spaces, with distance information added.
        The distances are stored in src[n]['dist'].
        Note: this function operates in-place.

    -----
    ### 📖 Notes

    This function can be memory- and CPU-intensive. On a high-end machine
    (2012) running 6 jobs in parallel, an ico-5 (10242 per hemi) source space
    takes about 10 minutes to compute all distances (``dist_limit = np.inf``).
    With ``dist_limit = 0.007``, computing distances takes about 1 minute.

    We recommend computing distances once per source space and then saving
    the source space to disk, as the computed distances will automatically be
    stored along with the source space data for future use.
    """
    ...

def get_volume_labels_from_src(src, subject, subjects_dir):
    """## 🧠 Return a list of Label of segmented volumes included in the src space.

    -----
    ### 🛠️ Parameters

    #### `src : instance of SourceSpaces`
        The source space containing the volume regions.

    #### `subject : str`
        The FreeSurfer subject name.
    #### `subjects_dir : str`
        Freesurfer folder of the subjects.

    -----
    ### ⏎ Returns

    #### `labels_aseg : list of Label`
        List of Label of segmented volumes included in src space.
    """
    ...

def morph_source_spaces(
    src_from,
    subject_to,
    surf: str = "white",
    subject_from=None,
    subjects_dir=None,
    verbose=None,
):
    """## 🧠 Morph an existing source space to a different subject.

    ### ⛔️ Warning This can be used in place of morphing source estimates for
                 multiple subjects, but there may be consequences in terms
                 of dipole topology.

    -----
    ### 🛠️ Parameters

    #### `src_from : instance of SourceSpaces`
        Surface source spaces to morph.
    #### `subject_to : str`
        The destination subject.
    #### `surf : str`
        The brain surface to use for the new source space.
    #### `subject_from : str | None`
        The "from" subject. For most source spaces this shouldn't need
        to be provided, since it is stored in the source space itself.
    #### `subjects_dir : path-like | None`
        Path to ``SUBJECTS_DIR`` if it is not set in the environment.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `src : instance of SourceSpaces`
        The morphed source spaces.

    -----
    ### 📖 Notes

    ✨ Added in vesion 0.10.0
    """
    ...

def compute_distance_to_sensors(src, info, picks=None, trans=None, verbose=None):
    """## 🧠 Compute distances between vertices and sensors.

    -----
    ### 🛠️ Parameters

    #### `src : instance of SourceSpaces`
        The object with vertex positions for which to compute distances to
        sensors.

    #### `info : mne.Info | None`
        The `mne.Info` object with information about the sensors and methods of measurement. Must contain sensor positions to which distances shall
        be computed.
    #### `picks : str | array-like | slice | None`
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel `type` strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel `name` strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick good data channels. Note that channels
        in ``info['bads']`` `will be included` if their names or indices are
        explicitly provided.

    #### `trans : str | dict | instance of Transform`
        If str, the path to the head<->MRI transform ``*-trans.fif`` file produced
        during coregistration. Can also be ``'fsaverage'`` to use the built-in
        fsaverage transformation.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `depth : array of shape (n_vertices, n_channels)`
        The Euclidean distances of source space vertices with respect to
        sensors.
    """
    ...

def get_decimated_surfaces(src):
    """## 🧠 Get the decimated surfaces from a source space.

    -----
    ### 🛠️ Parameters

    #### `src : instance of SourceSpaces | path-like`
        The source space with decimated surfaces.

    -----
    ### ⏎ Returns

    #### `surfaces : list of dict`
        The decimated surfaces present in the source space. Each dict
        which contains 'rr' and 'tris' keys for vertices positions and
        triangle indices.

    -----
    ### 📖 Notes

    ✨ Added in vesion 1.0
    """
    ...
