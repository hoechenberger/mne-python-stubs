from ._fiff.constants import FIFF as FIFF
from ._fiff.pick import pick_types as pick_types
from ._fiff.proj import make_projector as make_projector
from ._freesurfer import (
    head_to_mni as head_to_mni,
    head_to_mri as head_to_mri,
    read_freesurfer_lut as read_freesurfer_lut,
)
from .cov import compute_whitener as compute_whitener
from .fixes import pinvh as pinvh
from .parallel import parallel_func as parallel_func
from .source_space._source_space import SourceSpaces as SourceSpaces
from .surface import transform_surface_to as transform_surface_to
from .transforms import apply_trans as apply_trans
from .utils import (
    ExtendedTimeMixin as ExtendedTimeMixin,
    TimeMixin as TimeMixin,
    check_fname as check_fname,
    copy_function_doc_to_method_doc as copy_function_doc_to_method_doc,
    fill_doc as fill_doc,
    logger as logger,
    warn as warn,
)
from .viz import (
    plot_dipole_amplitudes as plot_dipole_amplitudes,
    plot_dipole_locations as plot_dipole_locations,
)
from _typeshed import Incomplete

class Dipole(TimeMixin):
    """Dipole class for sequential dipole fits.

    💡 This class should usually not be instantiated directly via
        ``mne.Dipole(...)``. Instead, use one of the functions
        listed in the See Also section below.

    Used to store positions, orientations, amplitudes, times, goodness of fit
    of dipoles, typically obtained with Neuromag/xfit, mne_dipole_fit
    or certain inverse solvers. Note that dipole position vectors are given in
    the head coordinate frame.

    Parameters
    ----------
    times : array, shape (n_dipoles,)
        The time instants at which each dipole was fitted (s).
    pos : array, shape (n_dipoles, 3)
        The dipoles positions (m) in head coordinates.
    amplitude : array, shape (n_dipoles,)
        The amplitude of the dipoles (Am).
    ori : array, shape (n_dipoles, 3)
        The dipole orientations (normalized to unit length).
    gof : array, shape (n_dipoles,)
        The goodness of fit.
    name : str | None
        Name of the dipole.
    conf : dict
        Confidence limits in dipole orientation for "vol" in m^3 (volume),
        "depth" in m (along the depth axis), "long" in m (longitudinal axis),
        "trans" in m (transverse axis), "qlong" in Am, and "qtrans" in Am
        (currents). The current confidence limit in the depth direction is
        assumed to be zero (although it can be non-zero when a BEM is used).

        ✨ Added in version 0.15
    khi2 : array, shape (n_dipoles,)
        The χ^2 values for the fits.

        ✨ Added in version 0.15
    nfree : array, shape (n_dipoles,)
        The number of free parameters for each fit.

        ✨ Added in version 0.15

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    fit_dipole
    DipoleFixed
    read_dipole

    Notes
    -----
    This class is for sequential dipole fits, where the position
    changes as a function of time. For fixed dipole fits, where the
    position is fixed as a function of time, use `mne.DipoleFixed`.
    """

    pos: Incomplete
    amplitude: Incomplete
    ori: Incomplete
    gof: Incomplete
    name: Incomplete
    conf: Incomplete
    khi2: Incomplete
    nfree: Incomplete

    def __init__(
        self,
        times,
        pos,
        amplitude,
        ori,
        gof,
        name=None,
        conf=None,
        khi2=None,
        nfree=None,
        *,
        verbose=None,
    ) -> None: ...
    def save(self, fname, overwrite: bool = False, *, verbose=None) -> None:
        """Save dipole in a ``.dip`` or ``.bdip`` file.

        Parameters
        ----------
        fname : path-like
            The name of the ``.dip`` or ``.bdip`` file.

        overwrite : bool
            If True (default False), overwrite the destination file if it
            exists.

            ✨ Added in version 0.20

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        Notes
        -----
        🎭 Changed in version 0.20
           Support for writing bdip (Xfit binary) files.
        """
        ...

    def crop(self, tmin=None, tmax=None, include_tmax: bool = True, verbose=None):
        """Crop data to a given time interval.

        Parameters
        ----------
        tmin : float | None
            Start time of selection in seconds.
        tmax : float | None
            End time of selection in seconds.

        include_tmax : bool
            If True (default), include tmax. If False, exclude tmax (similar to how
            Python indexing typically works).

            ✨ Added in version 0.19

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        self : instance of Dipole
            The cropped instance.
        """
        ...

    def copy(self):
        """Copy the Dipoles object.

        Returns
        -------
        dip : instance of Dipole
            The copied dipole instance.
        """
        ...

    def plot_locations(
        self,
        trans,
        subject,
        subjects_dir=None,
        mode: str = "orthoview",
        coord_frame: str = "mri",
        idx: str = "gof",
        show_all: bool = True,
        ax=None,
        block: bool = False,
        show: bool = True,
        scale=None,
        color=None,
        *,
        highlight_color: str = "r",
        fig=None,
        title=None,
        head_source: str = "seghead",
        surf: str = "pial",
        width=None,
        verbose=None,
    ):
        """Plot dipole locations.

        If mode is set to 'arrow' or 'sphere', only the location of the first
        time point of each dipole is shown else use the show_all parameter.

        Parameters
        ----------
        trans : dict | None
            The mri to head trans.
            Can be None with mode set to '3d'.
        subject : str | None
            The FreeSurfer subject name (will be used to set the FreeSurfer
            environment variable ``SUBJECT``).
            Can be ``None`` with mode set to ``'3d'``.

        subjects_dir : path-like | None
            The path to the directory containing the FreeSurfer subjects
            reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
            variable.
        mode : str
            Can be:

            ``'arrow'`` or ``'sphere'``
                Plot in 3D mode using PyVista with the given glyph type.
            ``'orthoview'``
                Plot in matplotlib ``Axes3D`` using matplotlib with MRI slices
                shown on the sides of a cube, with the dipole(s) shown as arrows
                extending outward from a dot (i.e., the arrows pivot on the tail).
            ``'outlines'``
                Plot in matplotlib ``Axes`` using a quiver of arrows for the
                dipoles in three axes (axial, coronal, and sagittal views),
                with the arrow pivoting in the middle of the arrow.

            🎭 Changed in version 1.1
               Added support for ``'outlines'``.
        coord_frame : str
            Coordinate frame to use: 'head' or 'mri'. Can also be 'mri_rotated'
            when mode equals ``'outlines'``. Defaults to 'mri'.

            ✨ Added in version 0.14.0
            🎭 Changed in version 1.1
               Added support for ``'mri_rotated'``.
        idx : int | 'gof' | 'amplitude'
            Index of the initially plotted dipole. Can also be 'gof' to plot the
            dipole with highest goodness of fit value or 'amplitude' to plot the
            dipole with the highest amplitude. The dipoles can also be browsed
            through using up/down arrow keys or mouse scroll. Defaults to 'gof'.
            Only used if mode equals 'orthoview'.

            ✨ Added in version 0.14.0
        show_all : bool
            Whether to always plot all the dipoles. If ``True`` (default), the
            active dipole is plotted as a red dot and its location determines the
            shown MRI slices. The non-active dipoles are plotted as small blue
            dots. If ``False``, only the active dipole is plotted.
            Only used if ``mode='orthoview'``.

            ✨ Added in version 0.14.0
        ax : instance of matplotlib Axes3D | list of matplotlib Axes | None
            Axes to plot into. If None (default), axes will be created.
            If mode equals ``'orthoview'``, must be a single ``Axes3D``.
            If mode equals ``'outlines'``, must be a list of three ``Axes``.

            ✨ Added in version 0.14.0
        block : bool
            Whether to halt program execution until the figure is closed. Defaults
            to False.
            Only used if mode equals 'orthoview'.

            ✨ Added in version 0.14.0
        show : bool
            Show figure if True. Defaults to True.
            Only used if mode equals 'orthoview'.
        scale : float
            The scale (size in meters) of the dipoles if ``mode`` is not
            ``'orthoview'``. The default is 0.03 when mode is ``'outlines'`` and
            0.005 otherwise.
        color : tuple
            The color of the dipoles.
            The default (None) will use ``'y'`` if mode is ``'orthoview'`` and
            ``show_all`` is True, else 'r'. Can also be a list of colors to use
            when mode is ``'outlines'``.

            🎭 Changed in version 0.19.0
               Color is now passed in orthoview mode.
        highlight_color : color
            The highlight color. Only used in orthoview mode with
            ``show_all=True``.

            ✨ Added in version 0.19.0
        fig : instance of Figure3D | None
            3D figure in which to plot the alignment.
            If ``None``, creates a new 600x600 pixel figure with black background.
            Only used when mode is ``'arrow'`` or ``'sphere'``.

            ✨ Added in version 0.19.0
        title : str | None
            The title of the figure if ``mode='orthoview'`` (ignored for all other
            modes). If ``None``, dipole number and its properties (amplitude,
            orientation etc.) will be shown. Defaults to ``None``.

            ✨ Added in version 0.21.0

        head_source : str | list of str
            Head source(s) to use. See the ``source`` option of
            `mne.get_head_surf` for more information.
            Only used when mode equals ``'outlines'``.

            ✨ Added in version 1.1
        surf : str | None
            Brain surface to show outlines for, can be ``'white'``, ``'pial'``, or
            ``None``. Only used when mode is ``'outlines'``.

            ✨ Added in version 1.1
        width : float | None
            Width of the matplotlib quiver arrow, see
            `matplotlib:matplotlib.axes.Axes.quiver`. If None (default),
            when mode is ``'outlines'`` 0.015 will be used, and when mode is
            ``'orthoview'`` the matplotlib default is used.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        fig : instance of Figure3D or matplotlib.figure.Figure
            The PyVista figure or matplotlib Figure.

        Notes
        -----
        ✨ Added in version 0.9.0
        """
        ...

    def to_mni(self, subject, trans, subjects_dir=None, verbose=None):
        """Convert dipole location from head to MNI coordinates.

        Parameters
        ----------

        subject : str
            The FreeSurfer subject name.

        trans : str | dict | instance of Transform
            If str, the path to the head<->MRI transform ``*-trans.fif`` file produced
            during coregistration. Can also be ``'fsaverage'`` to use the built-in
            fsaverage transformation.

        subjects_dir : path-like | None
            The path to the directory containing the FreeSurfer subjects
            reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
            variable.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        pos_mni : array, shape (n_pos, 3)
            The MNI coordinates (in mm) of pos.
        """
        ...

    def to_mri(self, subject, trans, subjects_dir=None, verbose=None):
        """Convert dipole location from head to MRI surface RAS coordinates.

        Parameters
        ----------

        subject : str
            The FreeSurfer subject name.

        trans : str | dict | instance of Transform
            If str, the path to the head<->MRI transform ``*-trans.fif`` file produced
            during coregistration. Can also be ``'fsaverage'`` to use the built-in
            fsaverage transformation.

        subjects_dir : path-like | None
            The path to the directory containing the FreeSurfer subjects
            reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
            variable.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        pos_mri : array, shape (n_pos, 3)
            The Freesurfer surface RAS coordinates (in mm) of pos.
        """
        ...

    def to_volume_labels(
        self,
        trans,
        subject: str = "fsaverage",
        aseg: str = "aparc+aseg",
        subjects_dir=None,
        verbose=None,
    ):
        """Find an ROI in atlas for the dipole positions.

        Parameters
        ----------

        trans : path-like | dict | instance of Transform | ``"fsaverage"`` | None
            If str, the path to the head<->MRI transform ``*-trans.fif`` file produced
            during coregistration. Can also be ``'fsaverage'`` to use the built-in
            fsaverage transformation.
            If trans is None, an identity matrix is assumed.

            🎭 Changed in version 0.19
                Support for 'fsaverage' argument.

        subject : str
            The FreeSurfer subject name.

        aseg : str
            The anatomical segmentation file. Default ``aparc+aseg``. This may
            be any anatomical segmentation file in the mri subdirectory of the
            Freesurfer subject directory.

        subjects_dir : path-like | None
            The path to the directory containing the FreeSurfer subjects
            reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
            variable.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        labels : list
            List of anatomical region names from anatomical segmentation atlas.

        Notes
        -----
        ✨ Added in version 0.24
        """
        ...

    def plot_amplitudes(self, color: str = "k", show: bool = True):
        """Plot the dipole amplitudes as a function of time.

        Parameters
        ----------
        color : matplotlib color
            Color to use for the trace.
        show : bool
            Show figure if True.

        Returns
        -------
        fig : matplotlib.figure.Figure
            The figure object containing the plot.
        """
        ...

    def __getitem__(self, item):
        """Get a time slice.

        Parameters
        ----------
        item : array-like or slice
            The slice of time points to use.

        Returns
        -------
        dip : instance of Dipole
            The sliced dipole.
        """
        ...

    def __len__(self) -> int:
        """Return the number of dipoles.

        Returns
        -------
        len : int
            The number of dipoles.

        Examples
        --------
        This can be used as::

            >>> len(dipoles)  # doctest: +SKIP
            10
        """
        ...

class DipoleFixed(ExtendedTimeMixin):
    """Dipole class for fixed-position dipole fits.

    💡 This class should usually not be instantiated directly
        via ``mne.DipoleFixed(...)``. Instead, use one of the functions
        listed in the See Also section below.

    Parameters
    ----------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    data : array, shape (n_channels, n_times)
        The dipole data.
    times : array, shape (n_times,)
        The time points.
    nave : int
        Number of averages.
    aspect_kind : int
        The kind of data.
    comment : str
        The dipole comment.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    read_dipole
    Dipole
    fit_dipole

    Notes
    -----
    This class is for fixed-position dipole fits, where the position
    (and maybe orientation) is static over time. For sequential dipole fits,
    where the position can change a function of time, use `mne.Dipole`.

    ✨ Added in version 0.12
    """

    info: Incomplete
    nave: Incomplete
    kind: Incomplete
    comment: Incomplete
    data: Incomplete
    preload: bool

    def __init__(
        self, info, data, times, nave, aspect_kind, comment: str = "", *, verbose=None
    ) -> None: ...
    def copy(self):
        """Copy the DipoleFixed object.

        Returns
        -------
        inst : instance of DipoleFixed
            The copy.

        Notes
        -----
        ✨ Added in version 0.16
        """
        ...

    @property
    def ch_names(self):
        """Channel names."""
        ...

    def save(self, fname, verbose=None) -> None:
        """Save dipole in a .fif file.

        Parameters
        ----------
        fname : path-like
            The name of the .fif file. Must end with ``'.fif'`` or
            ``'.fif.gz'`` to make it explicit that the file contains
            dipole information in FIF format.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.
        """
        ...

    def plot(self, show: bool = True, time_unit: str = "s"):
        """Plot dipole data.

        Parameters
        ----------
        show : bool
            Call pyplot.show() at the end or not.
        time_unit : str
            The units for the time axis, can be "ms" or "s" (default).

            ✨ Added in version 0.16

        Returns
        -------
        fig : instance of matplotlib.figure.Figure
            The figure containing the time courses.
        """
        ...

def read_dipole(fname, verbose=None):
    """Read ``.dip`` file from Neuromag/xfit or MNE.

    Parameters
    ----------
    fname : path-like
        The name of the ``.dip`` or ``.fif`` file.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------

    dipole : instance of Dipole | list of Dipole
        Dipole object containing position, orientation and amplitude of
        one or more dipoles. Multiple simultaneous dipoles may be defined by
        assigning them identical times. Alternatively, multiple simultaneous
        dipoles may also be specified as a list of Dipole objects.

        🎭 Changed in version 1.1
            Added support for a list of `mne.Dipole` instances.

    See Also
    --------
    Dipole
    DipoleFixed
    fit_dipole

    Notes
    -----
    🎭 Changed in version 0.20
       Support for reading bdip (Xfit binary) format.
    """
    ...

def fit_dipole(
    evoked,
    cov,
    bem,
    trans=None,
    min_dist: float = 5.0,
    n_jobs=None,
    pos=None,
    ori=None,
    rank=None,
    accuracy: str = "normal",
    tol: float = 5e-05,
    verbose=None,
):
    """Fit a dipole.

    Parameters
    ----------
    evoked : instance of Evoked
        The dataset to fit.
    cov : str | instance of Covariance
        The noise covariance.
    bem : path-like | instance of ConductorModel
        The BEM filename (str) or conductor model.
    trans : path-like | None
        The head<->MRI transform filename. Must be provided unless BEM
        is a sphere model.
    min_dist : float
        Minimum distance (in millimeters) from the dipole to the inner skull.
        Must be positive. Note that because this is a constraint passed to
        a solver it is not strict but close, i.e. for a ``min_dist=5.`` the
        fits could be 4.9 mm from the inner skull.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.
        It is used in field computation and fitting.
    pos : ndarray, shape (3,) | None
        Position of the dipole to use. If None (default), sequential
        fitting (different position and orientation for each time instance)
        is performed. If a position (in head coords) is given as an array,
        the position is fixed during fitting.

        ✨ Added in version 0.12
    ori : ndarray, shape (3,) | None
        Orientation of the dipole to use. If None (default), the
        orientation is free to change as a function of time. If an
        orientation (in head coordinates) is given as an array, ``pos``
        must also be provided, and the routine computes the amplitude and
        goodness of fit of the dipole at the given position and orientation
        for each time instant.

        ✨ Added in version 0.12

    rank : None | 'info' | 'full' | dict
        This controls the rank computation that can be read from the
        measurement info or estimated from the data. When a noise covariance
        is used for whitening, this should reflect the rank of that covariance,
        otherwise amplification of noise components can occur in whitening (e.g.,
        often during source localization).

        :data:`python:None`
            The rank will be estimated from the data after proper scaling of
            different channel types.
        ``'info'``
            The rank is inferred from ``info``. If data have been processed
            with Maxwell filtering, the Maxwell filtering header is used.
            Otherwise, the channel counts themselves are used.
            In both cases, the number of projectors is subtracted from
            the (effective) number of channels in the data.
            For example, if Maxwell filtering reduces the rank to 68, with
            two projectors the returned value will be 66.
        ``'full'``
            The rank is assumed to be full, i.e. equal to the
            number of good channels. If a `Covariance` is passed, this can
            make sense if it has been (possibly improperly) regularized without
            taking into account the true data rank.
        `dict`
            Calculate the rank only for a subset of channel types, and explicitly
            specify the rank for the remaining channel types. This can be
            extremely useful if you already **know** the rank of (part of) your
            data, for instance in case you have calculated it earlier.

            This parameter must be a dictionary whose **keys** correspond to
            channel types in the data (e.g. ``'meg'``, ``'mag'``, ``'grad'``,
            ``'eeg'``), and whose **values** are integers representing the
            respective ranks. For example, ``{'mag': 90, 'eeg': 45}`` will assume
            a rank of ``90`` and ``45`` for magnetometer data and EEG data,
            respectively.

            The ranks for all channel types present in the data, but
            **not** specified in the dictionary will be estimated empirically.
            That is, if you passed a dataset containing magnetometer, gradiometer,
            and EEG data together with the dictionary from the previous example,
            only the gradiometer rank would be determined, while the specified
            magnetometer and EEG ranks would be taken for granted.

        The default is ``None``.

        ✨ Added in version 0.20
    accuracy : str
        Can be ``"normal"`` (default) or ``"accurate"``, which gives the most
        accurate coil definition but is typically not necessary for real-world
        data.

        ✨ Added in version 0.24
    tol : float
        Final accuracy of the optimization (see ``rhoend`` argument of
        `scipy.optimize.fmin_cobyla`).

        ✨ Added in version 0.24

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    dip : instance of Dipole or DipoleFixed
        The dipole fits. A `mne.DipoleFixed` is returned if
        ``pos`` and ``ori`` are both not None, otherwise a
        `mne.Dipole` is returned.
    residual : instance of Evoked
        The M-EEG data channels with the fitted dipolar activity removed.

    See Also
    --------
    mne.beamformer.rap_music
    Dipole
    DipoleFixed
    read_dipole

    Notes
    -----
    ✨ Added in version 0.9.0
    """
    ...

def get_phantom_dipoles(kind: str = "vectorview"):
    """Get standard phantom dipole locations and orientations.

    Parameters
    ----------
    kind : str
        Get the information for the given system:

            ``vectorview`` (default)
              The Neuromag VectorView phantom.
            ``otaniemi``
              The older Neuromag phantom used at Otaniemi.
            ``oyama``
              The phantom from `OyamaEtAl2015`.

        🎭 Changed in version 1.6
           Support added for ``'oyama'``.

    Returns
    -------
    pos : ndarray, shape (n_dipoles, 3)
        The dipole positions.
    ori : ndarray, shape (n_dipoles, 3)
        The dipole orientations.

    See Also
    --------
    mne.datasets.fetch_phantom

    Notes
    -----
    The Elekta phantoms have a radius of 79.5mm, and HPI coil locations
    in the XY-plane at the axis extrema (e.g., (79.5, 0), (0, -79.5), ...).

    References
    ----------
    .. footbibliography::
    """
    ...
