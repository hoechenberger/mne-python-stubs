from ._fiff.constants import FIFF as FIFF
from ._fiff.open import fiff_open as fiff_open
from ._fiff.tag import read_tag as read_tag
from ._fiff.write import (
    start_and_end_file as start_and_end_file,
    write_coord_trans as write_coord_trans,
)
from .fixes import jit as jit
from .utils import (
    check_fname as check_fname,
    fill_doc as fill_doc,
    get_subjects_dir as get_subjects_dir,
    logger as logger,
    wrapped_stdout as wrapped_stdout,
)
from _typeshed import Incomplete

als_ras_trans: Incomplete

class Transform(dict):
    """A transform.

    Parameters
    ----------
    fro : str | int
        The starting coordinate frame. See notes for valid coordinate frames.
    to : str | int
        The ending coordinate frame. See notes for valid coordinate frames.
    trans : array of shape (4, 4) | None
        The transformation matrix. If None, an identity matrix will be
        used.

    Notes
    -----
    Valid coordinate frames are ``'meg'``, ``'mri'``, ``'mri_voxel'``,
    ``'head'``, ``'mri_tal'``, ``'ras'``, ``'fs_tal'``, ``'ctf_head'``,
    ``'ctf_meg'``, ``'unknown'``.
    """

    def __init__(self, fro, to, trans=None) -> None: ...
    def __eq__(self, other, rtol: float = 0.0, atol: float = 0.0):
        """Check for equality.

        Parameter
        ---------
        other : instance of Transform
            The other transform.
        rtol : float
            Relative tolerance.
        atol : float
            Absolute tolerance.

        Returns
        -------
        eq : bool
            True if the transforms are equal.
        """
        ...
    def __ne__(self, other, rtol: float = 0.0, atol: float = 0.0):
        """Check for inequality.

        Parameter
        ---------
        other : instance of Transform
            The other transform.
        rtol : float
            Relative tolerance.
        atol : float
            Absolute tolerance.

        Returns
        -------
        eq : bool
            True if the transforms are not equal.
        """
        ...
    @property
    def from_str(self):
        """The "from" frame as a string."""
        ...
    @property
    def to_str(self):
        """The "to" frame as a string."""
        ...
    def save(self, fname, *, overwrite: bool = False, verbose=None) -> None:
        """Save the transform as -trans.fif file.

        Parameters
        ----------
        fname : path-like
            The name of the file, which should end in ``-trans.fif``.

        overwrite : bool
            If True (default False), overwrite the destination file if it
            exists.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.
        """
        ...
    def copy(self):
        """Make a copy of the transform."""
        ...

def apply_trans(trans, pts, move: bool = True):
    """Apply a transform matrix to an array of points.

    Parameters
    ----------
    trans : array, shape = (4, 4) | instance of Transform
        Transform matrix.
    pts : array, shape = (3,) | (n, 3)
        Array with coordinates for one or n points.
    move : bool
        If True (default), apply translation.

    Returns
    -------
    transformed_pts : shape = (3,) | (n, 3)
        Transformed point(s).
    """

def rotation(x: int = 0, y: int = 0, z: int = 0):
    """Create an array with a 4 dimensional rotation matrix.

    Parameters
    ----------
    x, y, z : scalar
        Rotation around the origin (in rad).

    Returns
    -------
    r : array, shape = (4, 4)
        The rotation matrix.
    """

def rotation3d(x: int = 0, y: int = 0, z: int = 0):
    """Create an array with a 3 dimensional rotation matrix.

    Parameters
    ----------
    x, y, z : scalar
        Rotation around the origin (in rad).

    Returns
    -------
    r : array, shape = (3, 3)
        The rotation matrix.
    """

def rotation3d_align_z_axis(target_z_axis):
    """Compute a rotation matrix to align [ 0 0 1] with supplied target z axis.

    Parameters
    ----------
    target_z_axis : array, shape (1, 3)
        z axis. computed matrix (r) will map [0 0 1] to target_z_axis

    Returns
    -------
    r : array, shape (3, 3)
        The rotation matrix.
    """

def rotation_angles(m):
    """Find rotation angles from a transformation matrix.

    Parameters
    ----------
    m : array, shape >= (3, 3)
        Rotation matrix. Only the top left 3 x 3 partition is accessed.

    Returns
    -------
    x, y, z : float
        Rotation around x, y and z axes.
    """

def scaling(x: int = 1, y: int = 1, z: int = 1):
    """Create an array with a scaling matrix.

    Parameters
    ----------
    x, y, z : scalar
        Scaling factors.

    Returns
    -------
    s : array, shape = (4, 4)
        The scaling matrix.
    """

def translation(x: int = 0, y: int = 0, z: int = 0):
    """Create an array with a translation matrix.

    Parameters
    ----------
    x, y, z : scalar
        Translation parameters.

    Returns
    -------
    m : array, shape = (4, 4)
        The translation matrix.
    """

def combine_transforms(t_first, t_second, fro, to):
    """Combine two transforms.

    Parameters
    ----------
    t_first : dict
        First transform.
    t_second : dict
        Second transform.
    fro : int
        From coordinate frame.
    to : int
        To coordinate frame.

    Returns
    -------
    trans : dict
        Combined transformation.
    """

def read_trans(fname, return_all: bool = False, verbose=None):
    """Read a ``-trans.fif`` file.

    Parameters
    ----------
    fname : path-like
        The name of the file.
    return_all : bool
        If True, return all transformations in the file.
        False (default) will only return the first.

        .. versionadded:: 0.15

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    trans : dict | list of dict
        The transformation dictionary from the fif file.

    See Also
    --------
    write_trans
    mne.transforms.Transform
    """

def write_trans(fname, trans, *, overwrite: bool = False, verbose=None) -> None:
    """Write a transformation FIF file.

    Parameters
    ----------
    fname : path-like
        The name of the file, which should end in ``-trans.fif``.
    trans : dict
        Trans file data, as returned by mne.read_trans`.

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
    read_trans
    """

def invert_transform(trans):
    """Invert a transformation between coordinate systems.

    Parameters
    ----------
    trans : dict
        Transform to invert.

    Returns
    -------
    inv_trans : dict
        Inverse transform.
    """

def transform_surface_to(surf, dest, trans, copy: bool = False):
    """Transform surface to the desired coordinate system.

    Parameters
    ----------
    surf : dict
        Surface.
    dest : 'meg' | 'mri' | 'head' | int
        Destination coordinate system. Can be an integer for using
        FIFF types.
    trans : dict | list of dict
        Transformation to use (or a list of possible transformations to
        check).
    copy : bool
        If False (default), operate in-place.

    Returns
    -------
    res : dict
        Transformed source space.
    """

def get_ras_to_neuromag_trans(nasion, lpa, rpa):
    """Construct a transformation matrix to the MNE head coordinate system.

    Construct a transformation matrix from an arbitrary RAS coordinate system
    to the MNE head coordinate system, in which the x axis passes through the
    two preauricular points, and the y axis passes through the nasion and is
    normal to the x axis. (see mne manual, pg. 97)

    Parameters
    ----------
    nasion : array_like, shape (3,)
        Nasion point coordinate.
    lpa : array_like, shape (3,)
        Left peri-auricular point coordinate.
    rpa : array_like, shape (3,)
        Right peri-auricular point coordinate.

    Returns
    -------
    trans : numpy.array, shape = (4, 4)
        Transformation matrix to MNE head space.
    """

class _TPSWarp:
    """Transform points using thin-plate spline (TPS) warping.

    Notes
    -----
    Based on the method by :footcite:`Bookstein1989` and
    adapted from code by Wang Lin (wanglin193@hotmail.com>).

    References
    ----------
    .. footbibliography::
    """

    def fit(self, source, destination, reg: float = 0.001): ...
    def transform(self, pts, verbose=None):
        """Apply the warp.

        Parameters
        ----------
        pts : shape (n_transform, 3)
            Source points to warp to the destination.

        Returns
        -------
        dest : shape (n_transform, 3)
            The transformed points.
        """
        ...

class _SphericalSurfaceWarp:
    """Warp surfaces via spherical harmonic smoothing and thin-plate splines.

    Notes
    -----
    This class can be used to warp data from a source subject to
    a destination subject, as described in :footcite:`DarvasEtAl2006`.

    The procedure is:

        1. Perform a spherical harmonic approximation to the source and
           destination surfaces, which smooths them and allows arbitrary
           interpolation.
        2. Choose a set of matched points on the two surfaces.
        3. Use thin-plate spline warping (common in 2D image manipulation)
           to generate transformation coefficients.
        4. Warp points from the source subject (which should be inside the
           original surface) to the destination subject.

    .. versionadded:: 0.14

    References
    ----------
    .. footbibliography::
    """

    def fit(
        self,
        source,
        destination,
        order: int = 4,
        reg: float = 1e-05,
        center: bool = True,
        match: str = "oct5",
        verbose=None,
    ):
        """Fit the warp from source points to destination points.

        Parameters
        ----------
        source : array, shape (n_src, 3)
            The source points.
        destination : array, shape (n_dest, 3)
            The destination points.
        order : int
            Order of the spherical harmonic fit.
        reg : float
            Regularization of the TPS warp.
        center : bool
            If True, center the points by fitting a sphere to points
            that are in a reasonable region for head digitization.
        match : str
            The uniformly-spaced points to match on the two surfaces.
            Can be "ico#" or "oct#" where "#" is an integer.
            The default is "oct5".

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        inst : instance of SphericalSurfaceWarp
            The warping object (for chaining).
        """
        ...
    def transform(self, source, verbose=None):
        """Transform arbitrary source points to the destination.

        Parameters
        ----------
        source : ndarray, shape (n_pts, 3)
            Source points to transform. They do not need to be the same
            points that were used to generate the model, although ideally
            they will be inside the convex hull formed by the original
            source points.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        destination : ndarray, shape (n_pts, 3)
            The points transformed to the destination space.
        """
        ...

def quat_to_rot(quat):
    """Convert a set of quaternions to rotations.

    Parameters
    ----------
    quat : array, shape (..., 3)
        The q1, q2, and q3 (x, y, z) parameters of a unit quaternion.

    Returns
    -------
    rot : array, shape (..., 3, 3)
        The corresponding rotation matrices.

    See Also
    --------
    rot_to_quat
    """

def rot_to_quat(rot):
    """Convert a set of rotations to quaternions.

    Parameters
    ----------
    rot : array, shape (..., 3, 3)
        The rotation matrices to convert.

    Returns
    -------
    quat : array, shape (..., 3)
        The q1, q2, and q3 (x, y, z) parameters of the corresponding
        unit quaternions.

    See Also
    --------
    quat_to_rot
    """

def read_ras_mni_t(subject, subjects_dir=None):
    """Read a subject's RAS to MNI transform.

    Parameters
    ----------
    subject : str
        The subject.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.

    Returns
    -------
    ras_mni_t : instance of Transform
        The transform from RAS to MNI (in mm).
    """

def compute_volume_registration(
    moving,
    static,
    pipeline: str = "all",
    zooms=None,
    niter=None,
    *,
    starting_affine=None,
    verbose=None,
):
    """Align two volumes using an affine and, optionally, SDR.

    Parameters
    ----------

    moving : instance of SpatialImage
        The image to morph ("from" volume).

    static : instance of SpatialImage
        The image to align with ("to" volume).

    pipeline : str | tuple
        The volume registration steps to perform (a ``str`` for a single step,
        or ``tuple`` for a set of sequential steps). The following steps can be
        performed, and do so by matching mutual information between the images
        (unless otherwise noted):

        ``'translation'``
            Translation.

        ``'rigid'``
            Rigid-body, i.e., rotation and translation.

        ``'affine'``
            A full affine transformation, which includes translation, rotation,
            scaling, and shear.

        ``'sdr'``
            Symmetric diffeomorphic registration :footcite:`AvantsEtAl2008`, a
            non-linear similarity-matching algorithm.

        The following string shortcuts can also be used:

        ``'all'`` (default)
            All steps will be performed above in the order above, i.e.,
            ``('translation', 'rigid', 'affine', 'sdr')``.

        ``'rigids'``
            The rigid steps (first two) will be performed, which registers
            the volume without distorting its underlying structure, i.e.,
            ``('translation', 'rigid')``. This is useful for
            example when registering images from the same subject, such as
            CT and MR images.

        ``'affines'``
            The affine steps (first three) will be performed, i.e., omitting
            the SDR step.
    zooms : float | tuple | dict | None
        The voxel size of volume for each spatial dimension in mm.
        If None (default), MRIs won't be resliced (slow, but most accurate).
        Can be a tuple to provide separate zooms for each dimension (X/Y/Z),
        or a dict with keys ``['translation', 'rigid', 'affine', 'sdr']``
        (each with values that are float`, tuple, or None) to provide separate
        reslicing/accuracy for the steps.

    niter : dict | tuple | None
        For each phase of the volume registration, ``niter`` is the number of
        iterations per successive stage of optimization. If a tuple is
        provided, it will be used for all steps (except center of mass, which does
        not iterate). It should have length 3 to
        correspond to ``sigmas=[3.0, 1.0, 0.0]`` and ``factors=[4, 2, 1]`` in
        the pipeline (see :func:`dipy.align.affine_registration
        <dipy.align._public.affine_registration>` for details).
        If a dictionary is provided, number of iterations can be set for each
        step as a key. Steps not in the dictionary will use the default value.
        The default (None) is equivalent to:

            niter=dict(translation=(100, 100, 10),
                       rigid=(100, 100, 10),
                       affine=(100, 100, 10),
                       sdr=(5, 5, 3))
    starting_affine : ndarray
        The affine to initialize the registration with.

        .. versionadded:: 1.2

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------

    reg_affine : ndarray of float, shape (4, 4)
        The affine that registers one volume to another.

    sdr_morph : instance of dipy.align.DiffeomorphicMap
        The class that applies the the symmetric diffeomorphic registration
        (SDR) morph.

    Notes
    -----
    This function is heavily inspired by and extends
    :func:`dipy.align.affine_registration
    <dipy.align._public.affine_registration>`.

    .. versionadded:: 0.24
    """

def apply_volume_registration(
    moving,
    static,
    reg_affine,
    sdr_morph=None,
    interpolation: str = "linear",
    cval: float = 0.0,
    verbose=None,
):
    """Apply volume registration.

    Uses registration parameters computed by
    :func:mne.transforms.compute_volume_registration`.

    Parameters
    ----------

    moving : instance of SpatialImage
        The image to morph ("from" volume).

    static : instance of SpatialImage
        The image to align with ("to" volume).

    reg_affine : ndarray of float, shape (4, 4)
        The affine that registers one volume to another.

    sdr_morph : instance of dipy.align.DiffeomorphicMap
        The class that applies the the symmetric diffeomorphic registration
        (SDR) morph.
    interpolation : str
        Interpolation to be used during the interpolation.
        Can be ``"linear"`` (default) or ``"nearest"``.
    cval : float | str
        The constant value to assume exists outside the bounds of the
        ``moving`` image domain. Can be a string percentage like ``'1%'``
        to use the given percentile of image data as the constant value.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    reg_img : instance of SpatialImage
        The image after affine (and SDR, if provided) registration.

    Notes
    -----
    .. versionadded:: 0.24
    """

def apply_volume_registration_points(
    info, trans, moving, static, reg_affine, sdr_morph=None, verbose=None
):
    """Apply volume registration.

    Uses registration parameters computed by
    :func:mne.transforms.compute_volume_registration`.

    Parameters
    ----------

    info : mne.Info
        The :class:`mne.Info` object with information about the sensors and methods of measurement.

    trans : str | dict | instance of Transform
        If str, the path to the head<->MRI transform ``*-trans.fif`` file produced
        during coregistration. Can also be ``'fsaverage'`` to use the built-in
        fsaverage transformation.

    moving : instance of SpatialImage
        The image to morph ("from" volume).

    static : instance of SpatialImage
        The image to align with ("to" volume).

    reg_affine : ndarray of float, shape (4, 4)
        The affine that registers one volume to another.

    sdr_morph : instance of dipy.align.DiffeomorphicMap
        The class that applies the the symmetric diffeomorphic registration
        (SDR) morph.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------

    info : mne.Info
        The :class:`mne.Info` object with information about the sensors and methods of measurement.
    trans2 : instance of Transform
        The head->mri (surface RAS) transform for the static image.

    Notes
    -----
    .. versionadded:: 1.4.0
    """

class _MatchedDisplacementFieldInterpolator:
    """Interpolate from matched points using a displacement field in ND.

    For a demo, see
    https://gist.github.com/larsoner/fbe32d57996848395854d5e59dff1e10
    and related tests.
    """

    def __init__(self, fro, to, *, extrema=None) -> None: ...
    def __call__(self, x): ...
