from ._fiff.constants import FIFF as FIFF
from ._fiff.meas_info import read_fiducials as read_fiducials
from .surface import read_surface as read_surface
from .transforms import (
    Transform as Transform,
    apply_trans as apply_trans,
    combine_transforms as combine_transforms,
    invert_transform as invert_transform,
    read_ras_mni_t as read_ras_mni_t,
)
from .utils import get_subjects_dir as get_subjects_dir, logger as logger

def get_volume_labels_from_aseg(mgz_fname, return_colors: bool = False, atlas_ids=None):
    """Return a list of names and colors of segmented volumes.

    Parameters
    ----------
    mgz_fname : path-like
        Filename to read. Typically ``aseg.mgz`` or some variant in the
        freesurfer pipeline.
    return_colors : bool
        If True returns also the labels colors.
    atlas_ids : dict | None
        A lookup table providing a mapping from region names (str) to ID values
        (int). Can be None to use the standard Freesurfer LUT.

        .. versionadded:: 0.21.0

    Returns
    -------
    label_names : list of str
        The names of segmented volumes included in this mgz file.
    label_colors : list of str
        The RGB colors of the labels included in this mgz file.

    See Also
    --------
    read_freesurfer_lut

    Notes
    -----
    .. versionchanged:: 0.21.0
       The label names are now sorted in the same order as their corresponding
       values in the MRI file.

    .. versionadded:: 0.9.0
    """
    ...

def head_to_mri(
    pos,
    subject,
    mri_head_t,
    subjects_dir=None,
    *,
    kind: str = "mri",
    unscale: bool = False,
    verbose=None,
):
    """Convert pos from head coordinate system to MRI ones.

    Parameters
    ----------
    pos : array, shape (n_pos, 3)
        The coordinates (in m) in head coordinate system.

    subject : str
        The FreeSurfer subject name.
    mri_head_t : instance of Transform
        MRI<->Head coordinate transformation.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    kind : str
        The  MRI coordinate frame kind, can be ``'mri'`` (default) for
        FreeSurfer surface RAS or ``'ras'`` (default in 1.2) to use MRI RAS
        (scanner RAS).

        .. versionadded:: 1.2
    unscale : bool
        For surrogate MRIs (e.g., scaled using ``mne coreg``), if True
        (default False), use the MRI scaling parameters to obtain points in
        the original/surrogate subject's MRI space.

        .. versionadded:: 1.2

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    coordinates : array, shape (n_pos, 3)
        The MRI RAS coordinates (in mm) of pos.

    Notes
    -----
    This function requires nibabel.
    """
    ...

def vertex_to_mni(vertices, hemis, subject, subjects_dir=None, verbose=None):
    """Convert the array of vertices for a hemisphere to MNI coordinates.

    Parameters
    ----------
    vertices : int, or list of int
        Vertex number(s) to convert.
    hemis : int, or list of int
        Hemisphere(s) the vertices belong to.

    subject : str
        The FreeSurfer subject name.
    subjects_dir : str, or None
        Path to ``SUBJECTS_DIR`` if it is not set in the environment.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    coordinates : array, shape (n_vertices, 3)
        The MNI coordinates (in mm) of the vertices.
    """
    ...

def head_to_mni(pos, subject, mri_head_t, subjects_dir=None, verbose=None):
    """Convert pos from head coordinate system to MNI ones.

    Parameters
    ----------
    pos : array, shape (n_pos, 3)
        The coordinates (in m) in head coordinate system.

    subject : str
        The FreeSurfer subject name.
    mri_head_t : instance of Transform
        MRI<->Head coordinate transformation.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    coordinates : array, shape (n_pos, 3)
        The MNI coordinates (in mm) of pos.

    Notes
    -----
    This function requires either nibabel.
    """
    ...

def get_mni_fiducials(subject, subjects_dir=None, verbose=None):
    """Estimate fiducials for a subject.

    Parameters
    ----------

    subject : str
        The FreeSurfer subject name.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    fids_mri : list
        List of estimated fiducials (each point in a dict), in the order
        LPA, nasion, RPA.

    Notes
    -----
    This takes the ``fsaverage-fiducials.fif`` file included with MNE—which
    contain the LPA, nasion, and RPA for the ``fsaverage`` subject—and
    transforms them to the given FreeSurfer subject's MRI space.
    The MRI of ``fsaverage`` is already in MNI Talairach space, so applying
    the inverse of the given subject's MNI Talairach affine transformation
    (``$SUBJECTS_DIR/$SUBJECT/mri/transforms/talairach.xfm``) is used
    to estimate the subject's fiducial locations.

    For more details about the coordinate systems and transformations involved,
    see https://surfer.nmr.mgh.harvard.edu/fswiki/CoordinateSystems and
    :ref:`tut-source-alignment`.
    """
    ...

def estimate_head_mri_t(subject, subjects_dir=None, verbose=None):
    """Estimate the head->mri transform from fsaverage fiducials.

    A subject's fiducials can be estimated given a Freesurfer ``recon-all``
    by transforming ``fsaverage`` fiducials using the inverse Talairach
    transform, see :func:`mne.coreg.get_mni_fiducials`.

    Parameters
    ----------

    subject : str
        The FreeSurfer subject name.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------

    trans : str | dict | instance of Transform
        If str, the path to the head<->MRI transform ``*-trans.fif`` file produced
        during coregistration. Can also be ``'fsaverage'`` to use the built-in
        fsaverage transformation.
    """
    ...

def read_lta(fname, verbose=None):
    """Read a Freesurfer linear transform array file.

    Parameters
    ----------
    fname : path-like
        The transform filename.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    affine : ndarray
        The affine transformation described by the lta file.
    """
    ...

def read_talxfm(subject, subjects_dir=None, verbose=None):
    """Compute MRI-to-MNI transform from FreeSurfer talairach.xfm file.

    Parameters
    ----------

    subject : str
        The FreeSurfer subject name.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    mri_mni_t : instance of Transform
        The affine transformation from MRI to MNI space for the subject.
    """
    ...

def read_freesurfer_lut(fname=None):
    """Read a Freesurfer-formatted LUT.

    Parameters
    ----------
    fname : path-like | None
        The filename. Can be None to read the standard Freesurfer LUT.

    Returns
    -------
    atlas_ids : dict
        Mapping from label names to IDs.
    colors : dict
        Mapping from label names to colors.
    """
    ...
