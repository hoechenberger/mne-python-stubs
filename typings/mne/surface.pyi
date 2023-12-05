from ._fiff.constants import FIFF as FIFF
from ._fiff.pick import pick_types as pick_types
from .fixes import bincount as bincount, jit as jit, prange as prange
from .parallel import parallel_func as parallel_func
from .transforms import (
    Transform as Transform,
    apply_trans as apply_trans,
    transform_surface_to as transform_surface_to,
)
from .utils import (
    fill_doc as fill_doc,
    get_subjects_dir as get_subjects_dir,
    logger as logger,
    run_subprocess as run_subprocess,
    warn as warn,
)
from _typeshed import Incomplete

def get_head_surf(
    subject,
    source=("bem", "head"),
    subjects_dir=None,
    on_defects: str = "raise",
    verbose=None,
):
    """Load the subject head surface.

    Parameters
    ----------
    subject : str
        Subject name.
    source : str | list of str
        Type to load. Common choices would be ``'bem'`` or ``'head'``. We first
        try loading ``'$SUBJECTS_DIR/$SUBJECT/bem/$SUBJECT-$SOURCE.fif'``, and
        then look for ``'$SUBJECT*$SOURCE.fif'`` in the same directory by going
        through all files matching the pattern. The head surface will be read
        from the first file containing a head surface. Can also be a list
        to try multiple strings.
    subjects_dir : path-like | None
        Path to the ``SUBJECTS_DIR``. If None, the path is obtained by using
        the environment variable ``SUBJECTS_DIR``.

    on_defects : 'raise' | 'warn' | 'ignore'
        What to do if the surface is found to have topological defects.
        Can be ``'raise'`` (default) to raise an error, ``'warn'`` to emit a
        warning, or ``'ignore'`` to ignore when one or more defects are found.
        Note that a lot of computations in MNE-Python assume the surfaces to be
        topologically correct, topological defects may still make other
        computations (e.g., `mne.make_bem_model` and `mne.make_bem_solution`)
        fail irrespective of this parameter.

        ✨ Added in version 1.0

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    surf : dict
        The head surface.
    """
    ...

def get_meg_helmet_surf(info, trans=None, *, verbose=None):
    """Load the MEG helmet associated with the MEG sensors.

    Parameters
    ----------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    trans : dict
        The head<->MRI transformation, usually obtained using
        read_trans(). Can be None, in which case the surface will
        be in head coordinates instead of MRI coordinates.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    surf : dict
        The MEG helmet as a surface.

    Notes
    -----
    A built-in helmet is loaded if possible. If not, a helmet surface
    will be approximated based on the sensor locations.
    """
    ...

def fast_cross_3d(x, y):
    """Compute cross product between list of 3D vectors.

    Much faster than np.cross() when the number of cross products
    becomes large (>= 500). This is because np.cross() methods become
    less memory efficient at this stage.

    Parameters
    ----------
    x : array
        Input array 1, shape (..., 3).
    y : array
        Input array 2, shape (..., 3).

    Returns
    -------
    z : array, shape (..., 3)
        Cross product of x and y along the last dimension.

    Notes
    -----
    x and y must broadcast against each other.
    """
    ...

def complete_surface_info(
    surf,
    do_neighbor_vert: bool = False,
    copy: bool = True,
    do_neighbor_tri: bool = True,
    *,
    verbose=None,
):
    """Complete surface information.

    Parameters
    ----------
    surf : dict
        The surface.
    do_neighbor_vert : bool
        If True (default False), add neighbor vertex information.
    copy : bool
        If True (default), make a copy. If False, operate in-place.
    do_neighbor_tri : bool
        If True (default), compute triangle neighbors.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    surf : dict
        The transformed surface.
    """
    ...

class _CDist:
    """Wrapper for cdist that uses a Tree-like pattern."""

    def __init__(self, xhs) -> None: ...
    def query(self, rr): ...

class _DistanceQuery:
    """Wrapper for fast distance queries."""

    query: Incomplete
    data: Incomplete

    def __init__(
        self, xhs, method: str = "BallTree", allow_kdtree: bool = False
    ) -> None: ...

class _CheckInside:
    """Efficiently check if points are inside a surface."""

    mode: Incomplete
    surf: Incomplete

    def __init__(self, surf, *, mode: str = "old", verbose=None) -> None: ...
    def __call__(self, rr, n_jobs=None, verbose=None): ...

def read_curvature(filepath, binary: bool = True):
    """Load in curvature values from the ?h.curv file.

    Parameters
    ----------
    filepath : path-like
        Input path to the ``.curv`` file.
    binary : bool
        Specify if the output array is to hold binary values. Defaults to True.

    Returns
    -------
    curv : array of shape (n_vertices,)
        The curvature values loaded from the user given file.
    """
    ...

def read_surface(
    fname,
    read_metadata: bool = False,
    return_dict: bool = False,
    file_format: str = "auto",
    verbose=None,
):
    """Load a Freesurfer surface mesh in triangular format.

    Parameters
    ----------
    fname : path-like
        The name of the file containing the surface.
    read_metadata : bool
        Read metadata as key-value pairs. Only works when reading a FreeSurfer
        surface file. For .obj files this dictionary will be empty.

        Valid keys:

            * 'head' : array of int
            * 'valid' : str
            * 'filename' : str
            * 'volume' : array of int, shape (3,)
            * 'voxelsize' : array of float, shape (3,)
            * 'xras' : array of float, shape (3,)
            * 'yras' : array of float, shape (3,)
            * 'zras' : array of float, shape (3,)
            * 'cras' : array of float, shape (3,)

        ✨ Added in version 0.13.0

    return_dict : bool
        If True, a dictionary with surface parameters is returned.
    file_format : 'auto' | 'freesurfer' | 'obj'
        File format to use. Can be 'freesurfer' to read a FreeSurfer surface
        file, or 'obj' to read a Wavefront .obj file (common format for
        importing in other software), or 'auto' to attempt to infer from the
        file name. Defaults to 'auto'.

        ✨ Added in version 0.21.0

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    rr : array, shape=(n_vertices, 3)
        Coordinate points.
    tris : int array, shape=(n_faces, 3)
        Triangulation (each line contains indices for three points which
        together form a face).
    volume_info : dict-like
        If read_metadata is true, key-value pairs found in the geometry file.
    surf : dict
        The surface parameters. Only returned if ``return_dict`` is True.

    See Also
    --------
    write_surface
    read_tri
    """
    ...

def write_surface(
    fname,
    coords,
    faces,
    create_stamp: str = "",
    volume_info=None,
    file_format: str = "auto",
    overwrite: bool = False,
    *,
    verbose=None,
) -> None:
    """Write a triangular Freesurfer surface mesh.

    Accepts the same data format as is returned by read_surface().

    Parameters
    ----------
    fname : path-like
        File to write.
    coords : array, shape=(n_vertices, 3)
        Coordinate points.
    faces : int array, shape=(n_faces, 3)
        Triangulation (each line contains indices for three points which
        together form a face).
    create_stamp : str
        Comment that is written to the beginning of the file. Can not contain
        line breaks.
    volume_info : dict-like or None
        Key-value pairs to encode at the end of the file.
        Valid keys:

            * 'head' : array of int
            * 'valid' : str
            * 'filename' : str
            * 'volume' : array of int, shape (3,)
            * 'voxelsize' : array of float, shape (3,)
            * 'xras' : array of float, shape (3,)
            * 'yras' : array of float, shape (3,)
            * 'zras' : array of float, shape (3,)
            * 'cras' : array of float, shape (3,)

        ✨ Added in version 0.13.0
    file_format : 'auto' | 'freesurfer' | 'obj'
        File format to use. Can be 'freesurfer' to write a FreeSurfer surface
        file, or 'obj' to write a Wavefront .obj file (common format for
        importing in other software), or 'auto' to attempt to infer from the
        file name. Defaults to 'auto'.

        ✨ Added in version 0.21.0

    overwrite : bool
        If True (default False), overwrite the destination file if it
        exists.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    read_surface
    read_tri
    """
    ...

def decimate_surface(
    points, triangles, n_triangles, method: str = "quadric", *, verbose=None
):
    """Decimate surface data.

    Parameters
    ----------
    points : ndarray
        The surface to be decimated, a 3 x number of points array.
    triangles : ndarray
        The surface to be decimated, a 3 x number of triangles array.
    n_triangles : int
        The desired number of triangles.
    method : str
        Can be "quadric" or "sphere". "sphere" will inflate the surface to a
        sphere using Freesurfer and downsample to an icosahedral or
        octahedral mesh.

        ✨ Added in version 0.20

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    points : ndarray
        The decimated points.
    triangles : ndarray
        The decimated triangles.

    Notes
    -----
    **"quadric" mode**

    This requires VTK. If an odd target number was requested,
    the ``'decimation'`` algorithm used results in the
    next even number of triangles. For example a reduction request
    to 30001 triangles may result in 30000 triangles.

    **"sphere" mode**

    This requires Freesurfer to be installed and available in the
    environment. The destination number of triangles must be one of
    ``[20, 80, 320, 1280, 5120, 20480]`` for ico (0-5) downsampling or one of
    ``[8, 32, 128, 512, 2048, 8192, 32768]`` for oct (1-7) downsampling.

    This mode is slower, but could be more suitable for decimating meshes for
    BEM creation (recommended ``n_triangles=5120``) due to better topological
    property preservation.
    """
    ...

def mesh_edges(tris):
    """Return sparse matrix with edges as an adjacency matrix.

    Parameters
    ----------
    tris : array of shape [n_triangles x 3]
        The triangles.

    Returns
    -------
    edges : scipy.sparse.spmatrix
        The adjacency matrix.
    """
    ...

def mesh_dist(tris, vert):
    """Compute adjacency matrix weighted by distances.

    It generates an adjacency matrix where the entries are the distances
    between neighboring vertices.

    Parameters
    ----------
    tris : array (n_tris x 3)
        Mesh triangulation.
    vert : array (n_vert x 3)
        Vertex locations.

    Returns
    -------
    dist_matrix : scipy.sparse.csr_matrix
        Sparse matrix with distances between adjacent vertices.
    """
    ...

def read_tri(fname_in, swap: bool = False, verbose=None):
    """Read triangle definitions from an ascii file.

    Parameters
    ----------
    fname_in : path-like
        Path to surface ASCII file (ending with ``'.tri'``).
    swap : bool
        Assume the ASCII file vertex ordering is clockwise instead of
        counterclockwise.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    rr : array, shape=(n_vertices, 3)
        Coordinate points.
    tris : int array, shape=(n_faces, 3)
        Triangulation (each line contains indices for three points which
        together form a face).

    See Also
    --------
    read_surface
    write_surface

    Notes
    -----
    ✨ Added in version 0.13.0
    """
    ...

def dig_mri_distances(
    info,
    trans,
    subject,
    subjects_dir=None,
    dig_kinds: str = "auto",
    exclude_frontal: bool = False,
    on_defects: str = "raise",
    verbose=None,
):
    """Compute distances between head shape points and the scalp surface.

    This function is useful to check that coregistration is correct.
    Unless outliers are present in the head shape points,
    one can assume an average distance around 2-3 mm.

    Parameters
    ----------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement. Must contain the head shape points in ``info['dig']``.
    trans : str | instance of Transform
        The head<->MRI transform. If str is passed it is the
        path to file on disk.
    subject : str
        The name of the subject.
    subjects_dir : str | None
        Directory containing subjects data. If None use
        the Freesurfer SUBJECTS_DIR environment variable.

    dig_kinds : list of str | str
        Kind of digitization points to use in the fitting. These can be any
        combination of ('cardinal', 'hpi', 'eeg', 'extra'). Can also
        be 'auto' (default), which will use only the 'extra' points if
        enough (more than 4) are available, and if not, uses 'extra' and
        'eeg' points.

    exclude_frontal : bool
        If True, exclude points that have both negative Z values
        (below the nasion) and positive Y values (in front of the LPA/RPA).
        Default is False.

    on_defects : 'raise' | 'warn' | 'ignore'
        What to do if the surface is found to have topological defects.
        Can be ``'raise'`` (default) to raise an error, ``'warn'`` to emit a
        warning, or ``'ignore'`` to ignore when one or more defects are found.
        Note that a lot of computations in MNE-Python assume the surfaces to be
        topologically correct, topological defects may still make other
        computations (e.g., `mne.make_bem_model` and `mne.make_bem_solution`)
        fail irrespective of this parameter.

        ✨ Added in version 1.0

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    dists : array, shape (n_points,)
        The distances.

    See Also
    --------
    mne.bem.get_fitting_dig

    Notes
    -----
    ✨ Added in version 0.19
    """
    ...

def get_montage_volume_labels(
    montage, subject, subjects_dir=None, aseg: str = "aparc+aseg", dist: int = 2
):
    """Get regions of interest near channels from a Freesurfer parcellation.

    💡 Note This is applicable for channels inside the brain
              (intracranial electrodes).

    Parameters
    ----------

    montage : None | str | DigMontage
        A montage containing channel positions. If a string or
        `mne.channels.DigMontage` is
        specified, the existing channel information will be updated with the
        channel positions from the montage. Valid strings are the names of the
        built-in montages that ship with MNE-Python; you can list those via
        `mne.channels.get_builtin_montages`.
        If ``None`` (default), the channel positions will be removed from the
        `mne.Info`.

    subject : str
        The FreeSurfer subject name.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.

    aseg : str
        The anatomical segmentation file. Default ``aparc+aseg``. This may
        be any anatomical segmentation file in the mri subdirectory of the
        Freesurfer subject directory.
    dist : float
        The distance in mm to use for identifying regions of interest.

    Returns
    -------
    labels : dict
        The regions of interest labels within ``dist`` of each channel.
    colors : dict
        The Freesurfer lookup table colors for the labels.
    """
    ...
