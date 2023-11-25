from ._fiff.constants import FIFF as FIFF, FWD as FWD
from ._fiff.open import fiff_open as fiff_open
from ._fiff.tag import find_tag as find_tag
from ._fiff.tree import dir_tree_find as dir_tree_find
from ._fiff.write import (
    end_block as end_block,
    start_and_end_file as start_and_end_file,
    start_block as start_block,
    write_float as write_float,
    write_float_matrix as write_float_matrix,
    write_int as write_int,
    write_int_matrix as write_int_matrix,
    write_string as write_string,
)
from .surface import (
    complete_surface_info as complete_surface_info,
    decimate_surface as decimate_surface,
    read_surface as read_surface,
    read_tri as read_tri,
    transform_surface_to as transform_surface_to,
    write_surface as write_surface,
)
from .transforms import Transform as Transform, apply_trans as apply_trans
from .utils import (
    get_subjects_dir as get_subjects_dir,
    logger as logger,
    path_like as path_like,
    run_subprocess as run_subprocess,
    warn as warn,
)
from .viz.misc import plot_bem as plot_bem

class ConductorModel(dict):
    """Sphere radius if an EEG sphere model."""

    def copy(self):
        """Return copy of ConductorModel instance."""
    @property
    def radius(self):
        """Sphere radius if an EEG sphere model."""

def make_bem_solution(surfs, *, solver: str = ..., verbose=...):
    """Create a BEM solution using the linear collocation approach.

    Parameters
    ----------
    surfs : list of dict
        The BEM surfaces to use (from :func:`mne.make_bem_model`).
    solver : str
        Can be ``'mne'`` (default) to use MNE-Python, or ``'openmeeg'`` to use
        the :doc:`OpenMEEG <openmeeg:index>` package.

        .. versionadded:: 1.2

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    bem : instance of ConductorModel
        The BEM solution.

    See Also
    --------
    make_bem_model
    read_bem_surfaces
    write_bem_surfaces
    read_bem_solution
    write_bem_solution

    Notes
    -----
    .. versionadded:: 0.10.0
    """

def make_bem_model(
    subject, ico: int = ..., conductivity=..., subjects_dir=..., verbose=...
):
    """Create a BEM model for a subject.

    Use :func:mne.make_bem_solution` to turn the returned surfaces into a
    :class:mne.bem.ConductorModel` suitable for forward calculation.

    .. note:: To get a single layer bem corresponding to the --homog flag in
              the command line tool set the ``conductivity`` parameter
              to a float (e.g. ``0.3``).

    Parameters
    ----------

    subject : str
        The FreeSurfer subject name.
    ico : int | None
        The surface ico downsampling to use, e.g. ``5=20484``, ``4=5120``,
        ``3=1280``. If None, no subsampling is applied.
    conductivity : float | array of float of shape (3,) or (1,)
        The conductivities to use for each shell. Should be a single element
        for a one-layer model, or three elements for a three-layer model.
        Defaults to ``[0.3, 0.006, 0.3]``. The MNE-C default for a
        single-layer model is ``[0.3]``.

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
    surfaces : list of dict
        The BEM surfaces. Use :func:mne.make_bem_solution` to turn these into a
        :class:mne.bem.ConductorModel` suitable for forward calculation.

    See Also
    --------
    make_bem_solution
    make_sphere_model
    read_bem_surfaces
    write_bem_surfaces

    Notes
    -----
    .. versionadded:: 0.10.0
    """

def make_sphere_model(
    r0=...,
    head_radius: float = ...,
    info=...,
    relative_radii=...,
    sigmas=...,
    verbose=...,
):
    """Create a spherical model for forward solution calculation.

    Parameters
    ----------
    r0 : array-like | str
        Head center to use (in head coordinates). If 'auto', the head
        center will be calculated from the digitization points in info.
    head_radius : float | str | None
        If float, compute spherical shells for EEG using the given radius.
        If ``'auto'``, estimate an appropriate radius from the dig points in the
        :class:mne.Info` provided by the argument ``info``.
        If None, exclude shells (single layer sphere model).

    info : mne.Info | None
        The :class:`mne.Info` object with information about the sensors and methods of measurement. Only needed if ``r0`` or ``head_radius`` are ``'auto'``.
    relative_radii : array-like
        Relative radii for the spherical shells.
    sigmas : array-like
        Sigma values for the spherical shells.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    sphere : instance of ConductorModel
        The resulting spherical conductor model.

    See Also
    --------
    make_bem_model
    make_bem_solution

    Notes
    -----
    The default model has::

        relative_radii = (0.90, 0.92, 0.97, 1.0)
        sigmas = (0.33, 1.0, 0.004, 0.33)

    These correspond to compartments (with relative radii in ``m`` and
    conductivities σ in ``S/m``) for the brain, CSF, skull, and scalp,
    respectively.

    .. versionadded:: 0.9.0
    """

def fit_sphere_to_headshape(info, dig_kinds: str = ..., units: str = ..., verbose=...):
    """Fit a sphere to the headshape points to determine head center.

    Parameters
    ----------

    info : mne.Info
        The :class:`mne.Info` object with information about the sensors and methods of measurement.

    dig_kinds : list of str | str
        Kind of digitization points to use in the fitting. These can be any
        combination of ('cardinal', 'hpi', 'eeg', 'extra'). Can also
        be 'auto' (default), which will use only the 'extra' points if
        enough (more than 4) are available, and if not, uses 'extra' and
        'eeg' points.
    units : str
        Can be ``"m"`` (default) or ``"mm"``.

        .. versionadded:: 0.12

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    radius : float
        Sphere radius.
    origin_head: ndarray, shape (3,)
        Head center in head coordinates.
    origin_device: ndarray, shape (3,)
        Head center in device coordinates.

    Notes
    -----
    This function excludes any points that are low and frontal
    (``z < 0 and y > 0``) to improve the fit.
    """

def get_fitting_dig(
    info, dig_kinds: str = ..., exclude_frontal: bool = ..., verbose=...
):
    """Get digitization points suitable for sphere fitting.

    Parameters
    ----------

    info : mne.Info
        The :class:`mne.Info` object with information about the sensors and methods of measurement.

    dig_kinds : list of str | str
        Kind of digitization points to use in the fitting. These can be any
        combination of ('cardinal', 'hpi', 'eeg', 'extra'). Can also
        be 'auto' (default), which will use only the 'extra' points if
        enough (more than 4) are available, and if not, uses 'extra' and
        'eeg' points.

    exclude_frontal : bool
        If True, exclude points that have both negative Z values
        (below the nasion) and positive Y values (in front of the LPA/RPA).
        Default is True.

        .. versionadded:: 0.19

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    dig : array, shape (n_pts, 3)
        The digitization points (in head coordinates) to use for fitting.

    Notes
    -----
    This will exclude digitization locations that have ``z < 0 and y > 0``,
    i.e. points on the nose and below the nose on the face.

    .. versionadded:: 0.14
    """

def make_watershed_bem(
    subject,
    subjects_dir=...,
    overwrite: bool = ...,
    volume: str = ...,
    atlas: bool = ...,
    gcaatlas: bool = ...,
    preflood=...,
    show: bool = ...,
    copy: bool = ...,
    T1=...,
    brainmask: str = ...,
    verbose=...,
) -> None:
    """Create BEM surfaces using the FreeSurfer watershed algorithm.

    See :ref:`bem_watershed_algorithm` for additional information.

    Parameters
    ----------
    subject : str
        Subject name.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.

    overwrite : bool
        If True (default False), overwrite the destination file if it
        exists.
    volume : str
        Defaults to T1.
    atlas : bool
        Specify the ``--atlas option`` for ``mri_watershed``.
    gcaatlas : bool
        Specify the ``--brain_atlas`` option for ``mri_watershed``.
    preflood : int
        Change the preflood height.
    show : bool
        Show surfaces to visually inspect all three BEM surfaces (recommended).

        .. versionadded:: 0.12

    copy : bool
        If True (default), use copies instead of symlinks for surfaces
        (if they do not already exist).

        .. versionadded:: 0.18
        .. versionchanged:: 1.1 Use copies instead of symlinks.
    T1 : bool | None
        If True, pass the ``-T1`` flag.
        By default (None), this takes the same value as ``gcaatlas``.

        .. versionadded:: 0.19
    brainmask : str
        The filename for the brainmask output file relative to the
        ``$SUBJECTS_DIR/$SUBJECT/bem/watershed/`` directory.
        Can be for example ``"../../mri/brainmask.mgz"`` to overwrite
        the brainmask obtained via ``recon-all -autorecon1``.

        .. versionadded:: 0.19

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    mne.viz.plot_bem

    Notes
    -----
    If your BEM meshes do not look correct when viewed in
    :func:`mne.viz.plot_alignment` or :func:`mne.viz.plot_bem`, consider
    potential solutions from the :ref:`FAQ <faq_watershed_bem_meshes>`.

    .. versionadded:: 0.10
    """

def read_bem_surfaces(
    fname, patch_stats: bool = ..., s_id=..., on_defects: str = ..., verbose=...
):
    """Read the BEM surfaces from a FIF file.

    Parameters
    ----------
    fname : path-like
        The name of the file containing the surfaces.
    patch_stats : bool, optional (default False)
        Calculate and add cortical patch statistics to the surfaces.
    s_id : int | None
        If int, only read and return the surface with the given ``s_id``.
        An error will be raised if it doesn't exist. If None, all
        surfaces are read and returned.

    on_defects : 'raise' | 'warn' | 'ignore'
        What to do if the surface is found to have topological defects.
        Can be ``'raise'`` (default) to raise an error, ``'warn'`` to emit a
        warning, or ``'ignore'`` to ignore when one or more defects are found.
        Note that a lot of computations in MNE-Python assume the surfaces to be
        topologically correct, topological defects may still make other
        computations (e.g., `mne.make_bem_model` and `mne.make_bem_solution`)
        fail irrespective of this parameter.

        .. versionadded:: 0.23

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    surf: list | dict
        A list of dictionaries that each contain a surface. If ``s_id``
        is not None, only the requested surface will be returned.

    See Also
    --------
    write_bem_surfaces, write_bem_solution, make_bem_model
    """

def read_bem_solution(fname, *, verbose=...):
    """Read the BEM solution from a file.

    Parameters
    ----------
    fname : path-like
        The file containing the BEM solution.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    bem : instance of ConductorModel
        The BEM solution.

    See Also
    --------
    read_bem_surfaces
    write_bem_surfaces
    make_bem_solution
    write_bem_solution
    """

def write_bem_surfaces(fname, surfs, overwrite: bool = ..., *, verbose=...) -> None:
    """Write BEM surfaces to a FIF file.

    Parameters
    ----------
    fname : path-like
        Filename to write. Can end with ``.h5`` to write using HDF5.
    surfs : dict | list of dict
        The surfaces, or a single surface.

    overwrite : bool
        If True (default False), overwrite the destination file if it
        exists.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.
    """

def write_head_bem(
    fname, rr, tris, on_defects: str = ..., overwrite: bool = ..., *, verbose=...
) -> None:
    """Write a head surface to a FIF file.

    Parameters
    ----------
    fname : path-like
        Filename to write.
    rr : array, shape (n_vertices, 3)
        Coordinate points in the MRI coordinate system.
    tris : ndarray of int, shape (n_tris, 3)
        Triangulation (each line contains indices for three points which
        together form a face).

    on_defects : 'raise' | 'warn' | 'ignore'
        What to do if the surface is found to have topological defects.
        Can be ``'raise'`` (default) to raise an error, ``'warn'`` to emit a
        warning, or ``'ignore'`` to ignore when one or more defects are found.
        Note that a lot of computations in MNE-Python assume the surfaces to be
        topologically correct, topological defects may still make other
        computations (e.g., `mne.make_bem_model` and `mne.make_bem_solution`)
        fail irrespective of this parameter.

    overwrite : bool
        If True (default False), overwrite the destination file if it
        exists.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.
    """

def write_bem_solution(fname, bem, overwrite: bool = ..., *, verbose=...) -> None:
    """Write a BEM model with solution.

    Parameters
    ----------
    fname : path-like
        The filename to use. Can end with ``.h5`` to write using HDF5.
    bem : instance of ConductorModel
        The BEM model with solution to save.

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
    read_bem_solution
    """

def convert_flash_mris(
    subject,
    flash30: bool = ...,
    unwarp: bool = ...,
    subjects_dir=...,
    flash5: bool = ...,
    verbose=...,
):
    """Synthesize the flash 5 files for use with make_flash_bem.

    This function aims to produce a synthesized flash 5 MRI from
    multiecho flash (MEF) MRI data. This function can use MEF data
    with 5 or 30 flip angles. If flash5 (and flash30) images are not
    explicitly provided, it will assume that the different echos are available
    in the mri/flash folder of the subject with the following naming
    convention "mef<angle>_<echo>.mgz", e.g. "mef05_001.mgz"
    or "mef30_001.mgz".

    Parameters
    ----------

    subject : str
        The FreeSurfer subject name.
    flash30 : bool | list of SpatialImage or path-like | SpatialImage | path-like
        If False do not use 30-degree flip angle data.
        The list of flash 5 echos to use. If True it will look for files
        named mef30_*.mgz in the subject's mri/flash directory and if not False
        the list of flash 5 echos images will be written to the mri/flash
        folder with convention mef05_<echo>.mgz. If a SpatialImage object
        each frame of the image will be interpreted as an echo.
    unwarp : bool
        Run grad_unwarp with -unwarp option on each of the converted
        data sets. It requires FreeSurfer's MATLAB toolbox to be properly
        installed.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    flash5 : list of SpatialImage or path-like | SpatialImage | path-like | True
        The list of flash 5 echos to use. If True it will look for files
        named mef05_*.mgz in the subject's mri/flash directory and if not None
        the list of flash 5 echos images will be written to the mri/flash
        folder with convention mef05_<echo>.mgz. If a SpatialImage object
        each frame of the image will be interpreted as an echo.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    flash5_img : path-like
        The path the synthesized flash 5 MRI.

    Notes
    -----
    This function assumes that the Freesurfer segmentation of the subject
    has been completed. In particular, the T1.mgz and brain.mgz MRI volumes
    should be, as usual, in the subject's mri directory.
    """

def make_flash_bem(
    subject,
    overwrite: bool = ...,
    show: bool = ...,
    subjects_dir=...,
    copy: bool = ...,
    *,
    flash5_img=...,
    register: bool = ...,
    verbose=...,
) -> None:
    """Create 3-Layer BEM model from prepared flash MRI images.

    See :ref:`bem_flash_algorithm` for additional information.

    Parameters
    ----------

    subject : str
        The FreeSurfer subject name.
    overwrite : bool
        Write over existing .surf files in bem folder.
    show : bool
        Show surfaces to visually inspect all three BEM surfaces (recommended).

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    copy : bool
        If True (default), use copies instead of symlinks for surfaces
        (if they do not already exist).

        .. versionadded:: 0.18
        .. versionchanged:: 1.1 Use copies instead of symlinks.
    flash5_img : None | path-like | Nifti1Image
        The path to the synthesized flash 5 MRI image or the image itself. If
        None (default), the path defaults to
        ``mri/flash/parameter_maps/flash5.mgz`` within the subject
        reconstruction. If not present the image is copied or written to the
        default location.

        .. versionadded:: 1.1.0
    register : bool
        Register the flash 5 image with T1.mgz file. If False, we assume
        that the images are already coregistered.

        .. versionadded:: 1.1.0

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    convert_flash_mris

    Notes
    -----
    This program assumes that FreeSurfer is installed and sourced properly.

    This function extracts the BEM surfaces (outer skull, inner skull, and
    outer skin) from a FLASH 5 MRI image synthesized from multiecho FLASH
    images acquired with spin angles of 5 and 30 degrees.
    """

def make_scalp_surfaces(
    subject,
    subjects_dir=...,
    force: bool = ...,
    overwrite: bool = ...,
    no_decimate: bool = ...,
    *,
    threshold: int = ...,
    mri: str = ...,
    verbose=...,
):
    """Create surfaces of the scalp and neck.

    The scalp surfaces are required for using the MNE coregistration GUI, and
    allow for a visualization of the alignment between anatomy and channel
    locations.

    Parameters
    ----------

    subject : str
        The FreeSurfer subject name.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    force : bool
        Force creation of the surface even if it has some topological defects.
        Defaults to ``True``. See :ref:`tut-fix-meshes` for ideas on how to
        fix problematic meshes.

    overwrite : bool
        If True (default False), overwrite the destination file if it
        exists.
    no_decimate : bool
        Disable the "medium" and "sparse" decimations. In this case, only
        a "dense" surface will be generated. Defaults to ``False``, i.e.,
        create surfaces for all three types of decimations.
    threshold : int
        The threshold to use with the MRI in the call to ``mkheadsurf``.
        The default is ``20``.

        .. versionadded:: 1.1
    mri : str
        The MRI to use. Should exist in ``$SUBJECTS_DIR/$SUBJECT/mri``.

        .. versionadded:: 1.1

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.
    """

def distance_to_bem(pos, bem, trans=..., verbose=...):
    """Calculate the distance of positions to inner skull surface.

    Parameters
    ----------
    pos : array, shape (..., 3)
        Position(s) in m, in head coordinates.
    bem : instance of ConductorModel
        Conductor model.

    trans : path-like | dict | instance of Transform | ``"fsaverage"`` | None
        If str, the path to the head<->MRI transform ``*-trans.fif`` file produced
        during coregistration. Can also be ``'fsaverage'`` to use the built-in
        fsaverage transformation.
        If trans is None, an identity matrix is assumed. If None (default), assumes bem is in head coordinates.

        .. versionchanged:: 0.19
            Support for 'fsaverage' argument.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    distances : float | array, shape (...)
        The computed distance(s). A float is returned if pos is
        an array of shape (3,) corresponding to a single position.

    Notes
    -----
    .. versionadded:: 1.1
    """
