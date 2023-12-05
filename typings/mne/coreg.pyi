from ._fiff.constants import FIFF as FIFF
from ._fiff.meas_info import (
    Info as Info,
    read_fiducials as read_fiducials,
    read_info as read_info,
    write_fiducials as write_fiducials,
)
from ._freesurfer import (
    estimate_head_mri_t as estimate_head_mri_t,
    get_mni_fiducials as get_mni_fiducials,
)
from .bem import (
    read_bem_surfaces as read_bem_surfaces,
    write_bem_surfaces as write_bem_surfaces,
)
from .channels import make_dig_montage as make_dig_montage
from .label import Label as Label, read_label as read_label
from .source_space import (
    add_source_space_distances as add_source_space_distances,
    read_source_spaces as read_source_spaces,
    write_source_spaces as write_source_spaces,
)
from .surface import (
    complete_surface_info as complete_surface_info,
    decimate_surface as decimate_surface,
    read_surface as read_surface,
    write_surface as write_surface,
)
from .transforms import (
    Transform as Transform,
    apply_trans as apply_trans,
    combine_transforms as combine_transforms,
    invert_transform as invert_transform,
    rot_to_quat as rot_to_quat,
    rotation as rotation,
    rotation3d as rotation3d,
    scaling as scaling,
    translation as translation,
)
from .utils import (
    fill_doc as fill_doc,
    get_config as get_config,
    get_subjects_dir as get_subjects_dir,
    logger as logger,
    pformat as pformat,
    warn as warn,
)
from _typeshed import Incomplete

trans_fname: Incomplete
subject_dirname: Incomplete
bem_dirname: Incomplete
mri_dirname: Incomplete
mri_transforms_dirname: Incomplete
surf_dirname: Incomplete
bem_fname: Incomplete
head_bem_fname: Incomplete
head_sparse_fname: Incomplete
fid_fname: Incomplete
fid_fname_general: Incomplete
src_fname: Incomplete

def coregister_fiducials(info, fiducials, tol: float = 0.01):
    """Create a head-MRI transform by aligning 3 fiducial points.

    Parameters
    ----------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    fiducials : path-like | list of dict
        Fiducials in MRI coordinate space (either path to a ``*-fiducials.fif``
        file or list of fiducials as returned by `read_fiducials`.

    Returns
    -------
    trans : Transform
        The device-MRI transform.

    💡 The `mne.Info` object fiducials must be in the
              head coordinate space.
    """
    ...

def create_default_subject(
    fs_home=None, update: bool = False, subjects_dir=None, verbose=None
) -> None:
    """Create an average brain subject for subjects without structural MRI.

    Create a copy of fsaverage from the Freesurfer directory in subjects_dir
    and add auxiliary files from the mne package.

    Parameters
    ----------
    fs_home : None | str
        The freesurfer home directory (only needed if ``FREESURFER_HOME`` is
        not specified as environment variable).
    update : bool
        In cases where a copy of the fsaverage brain already exists in the
        subjects_dir, this option allows to only copy files that don't already
        exist in the fsaverage directory.
    subjects_dir : None | path-like
        Override the ``SUBJECTS_DIR`` environment variable
        (``os.environ['SUBJECTS_DIR']``) as destination for the new subject.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Notes
    -----
    When no structural MRI is available for a subject, an average brain can be
    substituted. Freesurfer comes with such an average brain model, and MNE
    comes with some auxiliary files which make coregistration easier.
    :py`create_default_subject` copies the relevant
    files from Freesurfer into the current subjects_dir, and also adds the
    auxiliary files provided by MNE.
    """
    ...

def fit_matched_points(
    src_pts,
    tgt_pts,
    rotate: bool = True,
    translate: bool = True,
    scale: bool = False,
    tol=None,
    x0=None,
    out: str = "trans",
    weights=None,
):
    """Find a transform between matched sets of points.

    This minimizes the squared distance between two matching sets of points.

    Uses `scipy.optimize.leastsq` to find a transformation involving
    a combination of rotation, translation, and scaling (in that order).

    Parameters
    ----------
    src_pts : array, shape = (n, 3)
        Points to which the transform should be applied.
    tgt_pts : array, shape = (n, 3)
        Points to which src_pts should be fitted. Each point in tgt_pts should
        correspond to the point in src_pts with the same index.
    rotate : bool
        Allow rotation of the ``src_pts``.
    translate : bool
        Allow translation of the ``src_pts``.
    scale : bool
        Number of scaling parameters. With False, points are not scaled. With
        True, points are scaled by the same factor along all axes.
    tol : scalar | None
        The error tolerance. If the distance between any of the matched points
        exceeds this value in the solution, a RuntimeError is raised. With
        None, no error check is performed.
    x0 : None | tuple
        Initial values for the fit parameters.
    out : 'params' | 'trans'
        In what format to return the estimate: 'params' returns a tuple with
        the fit parameters; 'trans' returns a transformation matrix of shape
        (4, 4).

    Returns
    -------
    trans : array, shape (4, 4)
        Transformation that, if applied to src_pts, minimizes the squared
        distance to tgt_pts. Only returned if out=='trans'.
    params : array, shape (n_params, )
        A single tuple containing the rotation, translation, and scaling
        parameters in that order (as applicable).
    """
    ...

def read_mri_cfg(subject, subjects_dir=None):
    """Read information from the cfg file of a scaled MRI brain.

    Parameters
    ----------
    subject : str
        Name of the scaled MRI subject.
    subjects_dir : None | path-like
        Override the ``SUBJECTS_DIR`` environment variable.

    Returns
    -------
    cfg : dict
        Dictionary with entries from the MRI's cfg file.
    """
    ...

def scale_bem(
    subject_to,
    bem_name,
    subject_from=None,
    scale=None,
    subjects_dir=None,
    *,
    on_defects: str = "raise",
    verbose=None,
) -> None:
    """Scale a bem file.

    Parameters
    ----------
    subject_to : str
        Name of the scaled MRI subject (the destination mri subject).
    bem_name : str
        Name of the bem file. For example, to scale
        ``fsaverage-inner_skull-bem.fif``, the bem_name would be
        "inner_skull-bem".
    subject_from : None | str
        The subject from which to read the source space. If None, subject_from
        is read from subject_to's config file.
    scale : None | float | array, shape = (3,)
        Scaling factor. Has to be specified if subjects_from is specified,
        otherwise it is read from subject_to's config file.
    subjects_dir : None | str
        Override the SUBJECTS_DIR environment variable.

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
    """
    ...

def scale_labels(
    subject_to,
    pattern=None,
    overwrite: bool = False,
    subject_from=None,
    scale=None,
    subjects_dir=None,
) -> None:
    """Scale labels to match a brain that was previously created by scaling.

    Parameters
    ----------
    subject_to : str
        Name of the scaled MRI subject (the destination brain).
    pattern : str | None
        Pattern for finding the labels relative to the label directory in the
        MRI subject directory (e.g., "lh.BA3a.label" will scale
        "fsaverage/label/lh.BA3a.label"; "aparc/\\*.label" will find all labels
        in the "fsaverage/label/aparc" directory). With None, scale all labels.
    overwrite : bool
        Overwrite any label file that already exists for subject_to (otherwise
        existing labels are skipped).
    subject_from : None | str
        Name of the original MRI subject (the brain that was scaled to create
        subject_to). If None, the value is read from subject_to's cfg file.
    scale : None | float | array_like, shape = (3,)
        Scaling parameter. If None, the value is read from subject_to's cfg
        file.
    subjects_dir : None | path-like
        Override the ``SUBJECTS_DIR`` environment variable.
    """
    ...

def scale_mri(
    subject_from,
    subject_to,
    scale,
    overwrite: bool = False,
    subjects_dir=None,
    skip_fiducials: bool = False,
    labels: bool = True,
    annot: bool = False,
    *,
    on_defects: str = "raise",
    verbose=None,
) -> None:
    """Create a scaled copy of an MRI subject.

    Parameters
    ----------
    subject_from : str
        Name of the subject providing the MRI.
    subject_to : str
        New subject name for which to save the scaled MRI.
    scale : float | array_like, shape = (3,)
        The scaling factor (one or 3 parameters).
    overwrite : bool
        If an MRI already exists for subject_to, overwrite it.
    subjects_dir : None | path-like
        Override the ``SUBJECTS_DIR`` environment variable.
    skip_fiducials : bool
        Do not scale the MRI fiducials. If False (default), an OSError will be
        raised if no fiducials file can be found.
    labels : bool
        Also scale all labels (default True).
    annot : bool
        Copy ``*.annot`` files to the new location (default False).

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

    See Also
    --------
    scale_bem : Add a scaled BEM to a scaled MRI.
    scale_labels : Add labels to a scaled MRI.
    scale_source_space : Add a source space to a scaled MRI.

    Notes
    -----
    This function will automatically call `scale_bem`,
    `scale_labels`, and `scale_source_space` based on expected
    filename patterns in the subject directory.
    """
    ...

def scale_source_space(
    subject_to,
    src_name,
    subject_from=None,
    scale=None,
    subjects_dir=None,
    n_jobs=None,
    verbose=None,
) -> None:
    """Scale a source space for an mri created with scale_mri().

    Parameters
    ----------
    subject_to : str
        Name of the scaled MRI subject (the destination mri subject).
    src_name : str
        Source space name. Can be a spacing parameter (e.g., ``'7'``,
        ``'ico4'``, ``'oct6'``) or a file name of a source space file relative
        to the bem directory; if the file name contains the subject name, it
        should be indicated as "{subject}" in ``src_name`` (e.g.,
        ``"{subject}-my_source_space-src.fif"``).
    subject_from : None | str
        The subject from which to read the source space. If None, subject_from
        is read from subject_to's config file.
    scale : None | float | array, shape = (3,)
        Scaling factor. Has to be specified if subjects_from is specified,
        otherwise it is read from subject_to's config file.
    subjects_dir : None | str
        Override the SUBJECTS_DIR environment variable.
    n_jobs : int
        Number of jobs to run in parallel if recomputing distances (only
        applies if scale is an array of length 3, and will not use more cores
        than there are source spaces).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Notes
    -----
    When scaling volume source spaces, the source (vertex) locations are
    scaled, but the reference to the MRI volume is left unchanged. Transforms
    are updated so that source estimates can be plotted on the original MRI
    volume.
    """
    ...

class Coregistration:
    """Class for MRI<->head coregistration.

    Parameters
    ----------
    info : instance of Info | None
        The measurement info.

    subject : str
        The FreeSurfer subject name.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.

    fiducials : list | dict | str
        The fiducials given in the MRI (surface RAS) coordinate
        system. If a dictionary is provided, it must contain the **keys**
        ``'lpa'``, ``'rpa'``, and ``'nasion'``, with **values** being the
        respective coordinates in meters.
        If a list, it must be a list of ``DigPoint`` instances as returned by the
        `mne.io.read_fiducials` function.
        If ``'estimated'``, the fiducials are derived from the ``fsaverage``
        template. If ``'auto'`` (default), tries to find the fiducials
        in a file with the canonical name
        (``{subjects_dir}/{subject}/bem/{subject}-fiducials.fif``)
        and if absent, falls back to ``'estimated'``.

    on_defects : 'raise' | 'warn' | 'ignore'
        What to do if the surface is found to have topological defects.
        Can be ``'raise'`` (default) to raise an error, ``'warn'`` to emit a
        warning, or ``'ignore'`` to ignore when one or more defects are found.
        Note that a lot of computations in MNE-Python assume the surfaces to be
        topologically correct, topological defects may still make other
        computations (e.g., `mne.make_bem_model` and `mne.make_bem_solution`)
        fail irrespective of this parameter.

        ✨ Added in version 1.0

    Attributes
    ----------
    fiducials : instance of DigMontage
        A montage containing the MRI fiducials.
    trans : instance of Transform
        MRI<->Head coordinate transformation.

    See Also
    --------
    mne.scale_mri

    Notes
    -----
    Internal computation quantities parameters are in the following units:

    - rotation are in radians
    - translation are in m
    - scale are in scale proportion

    If using a scale mode, the `mne.scale_mri` should be used
    to create a surrogate MRI subject with the proper scale factors.
    """

    def __init__(
        self,
        info,
        subject,
        subjects_dir=None,
        fiducials: str = "auto",
        *,
        on_defects: str = "raise",
    ) -> None: ...
    def set_scale_mode(self, scale_mode):
        """Select how to fit the scale parameters.

        Parameters
        ----------
        scale_mode : None | str
            The scale mode can be 'uniform', '3-axis' or disabled.
            Defaults to None.

            * 'uniform': 1 scale factor is recovered.
            * '3-axis': 3 scale factors are recovered.
            * None: do not scale the MRI.

        Returns
        -------
        self : Coregistration
            The modified Coregistration object.
        """
        ...

    def set_grow_hair(self, value):
        """Compensate for hair on the digitizer head shape.

        Parameters
        ----------
        value : float
            Move the back of the MRI head outwards by ``value`` (mm).

        Returns
        -------
        self : Coregistration
            The modified Coregistration object.
        """
        ...

    def set_rotation(self, rot):
        """Set the rotation parameter.

        Parameters
        ----------
        rot : array, shape (3,)
            The rotation parameter (in radians).

        Returns
        -------
        self : Coregistration
            The modified Coregistration object.
        """
        ...

    def set_translation(self, tra):
        """Set the translation parameter.

        Parameters
        ----------
        tra : array, shape (3,)
            The translation parameter (in m.).

        Returns
        -------
        self : Coregistration
            The modified Coregistration object.
        """
        ...

    def set_scale(self, sca):
        """Set the scale parameter.

        Parameters
        ----------
        sca : array, shape (3,)
            The scale parameter.

        Returns
        -------
        self : Coregistration
            The modified Coregistration object.
        """
        ...

    @property
    def scale(self):
        """Get the current scale factor.

        Returns
        -------
        scale : ndarray, shape (3,)
            The scale factors.
        """
        ...

    def fit_fiducials(
        self,
        lpa_weight: float = 1.0,
        nasion_weight: float = 10.0,
        rpa_weight: float = 1.0,
        verbose=None,
    ):
        """Find rotation and translation to fit all 3 fiducials.

        Parameters
        ----------
        lpa_weight : float
            Relative weight for LPA. The default value is 1.
        nasion_weight : float
            Relative weight for nasion. The default value is 10.
        rpa_weight : float
            Relative weight for RPA. The default value is 1.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        self : Coregistration
            The modified Coregistration object.
        """
        ...

    def set_fid_match(self, match):
        """Set the strategy for fitting anatomical landmark (fiducial) points.

        Parameters
        ----------
        match : 'nearest' | 'matched'
            Alignment strategy; ``'nearest'`` aligns anatomical landmarks to
            any point on the head surface; ``'matched'`` aligns to the fiducial
            points in the MRI.

        Returns
        -------
        self : Coregistration
            The modified Coregistration object.
        """
        ...

    def fit_icp(
        self,
        n_iterations: int = 20,
        lpa_weight: float = 1.0,
        nasion_weight: float = 10.0,
        rpa_weight: float = 1.0,
        hsp_weight: float = 1.0,
        eeg_weight: float = 1.0,
        hpi_weight: float = 1.0,
        callback=None,
        verbose=None,
    ):
        """Find MRI scaling, translation, and rotation to match HSP.

        Parameters
        ----------
        n_iterations : int
            Maximum number of iterations.
        lpa_weight : float
            Relative weight for LPA. The default value is 1.
        nasion_weight : float
            Relative weight for nasion. The default value is 10.
        rpa_weight : float
            Relative weight for RPA. The default value is 1.
        hsp_weight : float
            Relative weight for HSP. The default value is 1.
        eeg_weight : float
            Relative weight for EEG. The default value is 1.
        hpi_weight : float
            Relative weight for HPI. The default value is 1.
        callback : callable | None
            A function to call on each iteration. Useful for status message
            updates. It will be passed the keyword arguments ``iteration``
            and ``n_iterations``.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        self : Coregistration
            The modified Coregistration object.
        """
        ...

    def omit_head_shape_points(self, distance):
        """Exclude head shape points that are far away from the MRI head.

        Parameters
        ----------
        distance : float
            Exclude all points that are further away from the MRI head than
            this distance (in m.). A value of distance <= 0 excludes nothing.

        Returns
        -------
        self : Coregistration
            The modified Coregistration object.
        """
        ...

    def compute_dig_mri_distances(self):
        """Compute distance between head shape points and MRI skin surface.

        Returns
        -------
        dist : array, shape (n_points,)
            The distance of the head shape points to the MRI skin surface.

        See Also
        --------
        mne.dig_mri_distances
        """
        ...

    @property
    def trans(self):
        """The head->mri `mne.transforms.Transform`."""
        ...

    def reset(self):
        """Reset all the parameters affecting the coregistration.

        Returns
        -------
        self : Coregistration
            The modified Coregistration object.
        """
        ...
