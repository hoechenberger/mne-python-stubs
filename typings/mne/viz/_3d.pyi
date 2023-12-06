from .._fiff.constants import FIFF as FIFF
from .._fiff.meas_info import (
    Info as Info,
    create_info as create_info,
    read_fiducials as read_fiducials,
)
from .._fiff.pick import (
    channel_type as channel_type,
    pick_info as pick_info,
    pick_types as pick_types,
)
from .._freesurfer import read_freesurfer_lut as read_freesurfer_lut
from ..defaults import DEFAULTS as DEFAULTS
from ..surface import get_meg_helmet_surf as get_meg_helmet_surf
from ..transforms import (
    Transform as Transform,
    apply_trans as apply_trans,
    combine_transforms as combine_transforms,
    read_ras_mni_t as read_ras_mni_t,
    rot_to_quat as rot_to_quat,
    rotation as rotation,
    transform_surface_to as transform_surface_to,
)
from ..utils import (
    check_version as check_version,
    fill_doc as fill_doc,
    get_config as get_config,
    get_subjects_dir as get_subjects_dir,
    logger as logger,
    warn as warn,
)
from .evoked_field import EvokedField as EvokedField
from .utils import figure_nobar as figure_nobar, plt_show as plt_show
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Optional

verbose_dec = verbose
FIDUCIAL_ORDER: Incomplete

def plot_head_positions(
    pos,
    mode: str = "traces",
    cmap: str = "viridis",
    direction: str = "z",
    show: bool = True,
    destination=None,
    info=None,
    color: str = "k",
    axes=None,
):
    """Plot head positions.

    Parameters
    ----------
    pos : ndarray, shape (n_pos, 10) | list of ndarray
        The head position data. Can also be a list to treat as a
        concatenation of runs.
    mode : str
        Can be 'traces' (default) to show position and quaternion traces,
        or 'field' to show the position as a vector field over time.
    cmap : colormap
        Colormap to use for the trace plot, default is "viridis".
    direction : str
        Can be any combination of "x", "y", or "z" (default: "z") to show
        directional axes in "field" mode.
    show : bool
        Show figure if True. Defaults to True.
    destination : str | array-like, shape (3,) | None
        The destination location for the head, assumed to be in head
        coordinates. See `mne.preprocessing.maxwell_filter` for
        details.

        ✨ Added in version 0.16

    info : mne.Info | None
        The `mne.Info` object with information about the sensors and methods of measurement. If provided, will be used to show the destination position when
        ``destination is None``, and for showing the MEG sensors.

        ✨ Added in version 0.16
    color : color object
        The color to use for lines in ``mode == 'traces'`` and quiver
        arrows in ``mode == 'field'``.

        ✨ Added in version 0.16
    axes : array-like, shape (3, 2)
        The matplotlib axes to use. Only used for ``mode == 'traces'``.

        ✨ Added in version 0.16

    Returns
    -------
    fig : instance of matplotlib.figure.Figure
        The figure.
    """
    ...

def plot_evoked_field(
    evoked,
    surf_maps,
    time=None,
    time_label: str = "t = %0.0f ms",
    n_jobs=None,
    fig=None,
    vmax=None,
    n_contours: int = 21,
    *,
    show_density: bool = True,
    alpha=None,
    interpolation: str = "nearest",
    interaction: str = "terrain",
    time_viewer: str = "auto",
    verbose=None,
):
    """Plot MEG/EEG fields on head surface and helmet in 3D.

    Parameters
    ----------
    evoked : instance of mne.Evoked
        The evoked object.
    surf_maps : list
        The surface mapping information obtained with make_field_map.
    time : float | None
        The time point at which the field map shall be displayed. If None,
        the average peak latency (across sensor types) is used.
    time_label : str | None
        How to print info about the time instant visualized.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.
    fig : Figure3D | mne.viz.Brain | None
        If None (default), a new figure will be created, otherwise it will
        plot into the given figure.

        ✨ Added in version 0.20
        ✨ Added in version 1.4
            ``fig`` can also be a ``Brain`` figure.
    vmax : float | dict | None
        Maximum intensity. Can be a dictionary with two entries ``"eeg"`` and ``"meg"``
        to specify separate values for EEG and MEG fields respectively. Can be
        ``None`` to use the maximum value of the data.

        ✨ Added in version 0.21
        ✨ Added in version 1.4
            ``vmax`` can be a dictionary to specify separate values for EEG and
            MEG fields.
    n_contours : int
        The number of contours.

        ✨ Added in version 0.21
    show_density : bool
        Whether to draw the field density as an overlay on top of the helmet/head
        surface. Defaults to ``True``.

        ✨ Added in version 1.6
    alpha : float | dict | None
        Opacity of the meshes (between 0 and 1). Can be a dictionary with two
        entries ``"eeg"`` and ``"meg"`` to specify separate values for EEG and
        MEG fields respectively. Can be ``None`` to use 1.0 when a single field
        map is shown, or ``dict(eeg=1.0, meg=0.5)`` when both field maps are shown.

        ✨ Added in version 1.4

    interpolation : str | None
        Interpolation method (`scipy.interpolate.interp1d` parameter).
        Must be one of ``'linear'``, ``'nearest'``, ``'zero'``, ``'slinear'``,
        ``'quadratic'`` or ``'cubic'``.

        ✨ Added in version 1.6

    interaction : 'trackball' | 'terrain'
        How interactions with the scene via an input device (e.g., mouse or
        trackpad) modify the camera position. If ``'terrain'``, one axis is
        fixed, enabling "turntable-style" rotations. If ``'trackball'``,
        movement along all axes is possible, which provides more freedom of
        movement, but you may incidentally perform unintentional rotations along
        some axes.
        Defaults to ``'terrain'``.

        ✨ Added in version 1.1
    time_viewer : bool | str
        Display time viewer GUI. Can also be ``"auto"``, which will mean
        ``True`` if there is more than one time point and ``False`` otherwise.

        ✨ Added in version 1.6

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    fig : Figure3D | mne.viz.EvokedField
        Without the time viewer active, the figure is returned. With the time
        viewer active, an object is returned that can be used to control
        different aspects of the figure.
    """
    ...

def plot_alignment(
    info=None,
    trans=None,
    subject=None,
    subjects_dir=None,
    surfaces: str = "auto",
    coord_frame: str = "auto",
    meg=None,
    eeg: str = "original",
    fwd=None,
    dig: bool = False,
    ecog: bool = True,
    src=None,
    mri_fiducials: bool = False,
    bem=None,
    seeg: bool = True,
    fnirs: bool = True,
    show_axes: bool = False,
    dbs: bool = True,
    fig=None,
    interaction: str = "terrain",
    sensor_colors=None,
    verbose=None,
):
    """Plot head, sensor, and source space alignment in 3D.

    Parameters
    ----------

    info : mne.Info | None
        The `mne.Info` object with information about the sensors and methods of measurement. If None (default), no sensor information will be shown.

    trans : path-like | dict | instance of Transform | ``"fsaverage"`` | None
        If str, the path to the head<->MRI transform ``*-trans.fif`` file produced
        during coregistration. Can also be ``'fsaverage'`` to use the built-in
        fsaverage transformation.
        If trans is None, an identity matrix is assumed. "auto" will load trans from the FreeSurfer directory
        specified by ``subject`` and ``subjects_dir`` parameters.

        🎭 Changed in version 0.19
            Support for 'fsaverage' argument.

    subject : str
        The FreeSurfer subject name. Can be omitted if ``src`` is provided.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    surfaces : str | list | dict
        Surfaces to plot. Supported values:

        * scalp: one of 'head', 'outer_skin' (alias for 'head'),
          'head-dense', or 'seghead' (alias for 'head-dense')
        * skull: 'outer_skull', 'inner_skull', 'brain' (alias for
          'inner_skull')
        * brain: one of 'pial', 'white', 'inflated', or 'brain'
          (alias for 'pial').

        Can be dict to specify alpha values for each surface. Use None
        to specify default value. Specified values must be between 0 and 1.
        for example::

            surfaces=dict(brain=0.4, outer_skull=0.6, head=None)

        Defaults to 'auto', which will look for a head surface and plot
        it if found.

        💡 For single layer BEMs it is recommended to use ``'brain'``.
    coord_frame : 'auto' | 'head' | 'meg' | 'mri'
        The coordinate frame to use. If ``'auto'`` (default), chooses ``'mri'``
        if ``trans`` was passed, and ``'head'`` otherwise.

        🎭 Changed in version 1.0
           Defaults to ``'auto'``.

    meg : str | list | dict | bool | None
        Can be "helmet", "sensors" or "ref" to show the MEG helmet, sensors or
        reference sensors respectively, or a combination like
        ``('helmet', 'sensors')`` (same as None, default). True translates to
        ``('helmet', 'sensors', 'ref')``. Can also be a dict to specify alpha values,
        e.g. ``{"helmet": 0.1, "sensors": 0.8}``.

        🎭 Changed in version 1.6
           Added support for specifying alpha values as a dict.

    eeg : bool | str | list | dict
        String options are:

        - "original" (default; equivalent to ``True``)
            Shows EEG sensors using their digitized locations (after
            transformation to the chosen ``coord_frame``)
        - "projected"
            The EEG locations projected onto the scalp, as is done in
            forward modeling

        Can also be a list of these options, or a dict to specify the alpha values
        to use, e.g. ``dict(original=0.2, projected=0.8)``.

        🎭 Changed in version 1.6
           Added support for specifying alpha values as a dict.

    fwd : instance of Forward
        The forward solution. If present, the orientations of the dipoles
        present in the forward solution are displayed.
    dig : bool | 'fiducials'
        If True, plot the digitization points; 'fiducials' to plot fiducial
        points only.

    ecog : bool
        If True (default), show ECoG sensors.
    src : instance of SourceSpaces | None
        If not None, also plot the source space points.
    mri_fiducials : bool | str | path-like
        Plot MRI fiducials (default False). If ``True``, look for a file with
        the canonical name (``bem/{subject}-fiducials.fif``). If ``str``,
        it can be ``'estimated'`` to use `mne.coreg.get_mni_fiducials`,
        otherwise it should provide the full path to the fiducials file.

        ✨ Added in version 0.22
           Support for ``'estimated'``.
    bem : list of dict | instance of ConductorModel | None
        Can be either the BEM surfaces (list of dict), a BEM solution or a
        sphere model. If None, we first try loading
        ``'$SUBJECTS_DIR/$SUBJECT/bem/$SUBJECT-$SOURCE.fif'``, and then look
        for ``'$SUBJECT*$SOURCE.fif'`` in the same directory. For
        ``'outer_skin'``, the subjects bem and bem/flash folders are searched.
        Defaults to None.

    seeg : bool
        If True (default), show sEEG electrodes.

    fnirs : str | list | dict | bool | None
        Can be "channels", "pairs", "detectors", and/or "sources" to show the
        fNIRS channel locations, optode locations, or line between
        source-detector pairs, or a combination like ``('pairs', 'channels')``.
        True translates to ``('pairs',)``. A dict can also be used to specify
        alpha values (but only "channels" and "pairs" will be used), e.g.
        ``dict(channels=0.2, pairs=0.7)``.

        🎭 Changed in version 1.6
           Added support for specifying alpha values as a dict.
        ✨ Added in version 0.20
    show_axes : bool
        If True (default False), coordinate frame axis indicators will be
        shown:

        * head in pink.
        * MRI in gray (if ``trans is not None``).
        * MEG in blue (if MEG sensors are present).

        ✨ Added in version 0.16

    dbs : bool
        If True (default), show DBS (deep brain stimulation) electrodes.
    fig : Figure3D | None
        PyVista scene in which to plot the alignment.
        If ``None``, creates a new 600x600 pixel figure with black background.

        ✨ Added in version 0.16

    interaction : 'trackball' | 'terrain'
        How interactions with the scene via an input device (e.g., mouse or
        trackpad) modify the camera position. If ``'terrain'``, one axis is
        fixed, enabling "turntable-style" rotations. If ``'trackball'``,
        movement along all axes is possible, which provides more freedom of
        movement, but you may incidentally perform unintentional rotations along
        some axes.

        ✨ Added in version 0.16
        🎭 Changed in version 1.0
           Defaults to ``'terrain'``.

    sensor_colors : array-like of color | dict | None
        Colors to use for the sensor glyphs. Can be None (default) to use default colors.
        A dict should provide the colors (values) for each channel type (keys), e.g.::

            dict(eeg=eeg_colors)

        Where the value (``eeg_colors`` above) can be broadcast to an array of colors with
        length that matches the number of channels of that type, i.e., is compatible with
        `matplotlib.colors.to_rgba_array`. A few examples of this for the case above
        are the string ``"k"``, a list of ``n_eeg`` color strings, or an NumPy ndarray of
        shape ``(n_eeg, 3)`` or ``(n_eeg, 4)``.

        🎭 Changed in version 1.6
            Support for passing a ``dict`` was added.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    fig : instance of Figure3D
        The figure.

    See Also
    --------
    mne.viz.plot_bem

    Notes
    -----
    This function serves the purpose of checking the validity of the many
    different steps of source reconstruction:

    - Transform matrix (keywords ``trans``, ``meg`` and ``mri_fiducials``),
    - BEM surfaces (keywords ``bem`` and ``surfaces``),
    - sphere conductor model (keywords ``bem`` and ``surfaces``) and
    - source space (keywords ``surfaces`` and ``src``).

    ✨ Added in version 0.15
    """
    ...

def link_brains(
    brains,
    time: bool = True,
    camera: bool = False,
    colorbar: bool = True,
    picking: bool = False,
) -> None:
    """Plot multiple SourceEstimate objects with PyVista.

    Parameters
    ----------
    brains : list, tuple or np.ndarray
        The collection of brains to plot.
    time : bool
        If True, link the time controllers. Defaults to True.
    camera : bool
        If True, link the camera controls. Defaults to False.
    colorbar : bool
        If True, link the colorbar controllers. Defaults to True.
    picking : bool
        If True, link the vertices picked with the mouse. Defaults to False.
    """
    ...

def plot_source_estimates(
    stc,
    subject=None,
    surface: str = "inflated",
    hemi: str = "lh",
    colormap: str = "auto",
    time_label: str = "auto",
    smoothing_steps: int = 10,
    transparent: bool = True,
    alpha: float = 1.0,
    time_viewer: str = "auto",
    subjects_dir=None,
    figure=None,
    views: str = "auto",
    colorbar: bool = True,
    clim: str = "auto",
    cortex: str = "classic",
    size: int = 800,
    background: str = "black",
    foreground=None,
    initial_time=None,
    time_unit: str = "s",
    backend: str = "auto",
    spacing: str = "oct6",
    title=None,
    show_traces: str = "auto",
    src=None,
    volume_options: float = 1.0,
    view_layout: str = "vertical",
    add_data_kwargs=None,
    brain_kwargs=None,
    verbose=None,
):
    """Plot SourceEstimate.

    Parameters
    ----------
    stc : SourceEstimate
        The source estimates to plot.

    subject : str | None
        The FreeSurfer subject name.
        If ``None``, ``stc.subject`` will be used.
    surface : str
        The type of surface (inflated, white etc.).
    hemi : str
        Hemisphere id (ie ``'lh'``, ``'rh'``, ``'both'``, or ``'split'``). In
        the case of ``'both'``, both hemispheres are shown in the same window.
        In the case of ``'split'`` hemispheres are displayed side-by-side
        in different viewing panes.

    colormap : str | np.ndarray of float, shape(n_colors, 3 | 4)
        Name of colormap to use or a custom look up table. If array, must
        be (n x 3) or (n x 4) array for with RGB or RGBA values between
        0 and 255.
        The default ('auto') uses ``'hot'`` for one-sided data and
        'mne' for two-sided data.

    time_label : str | callable | None
        Format of the time label (a format string, a function that maps
        floating point time values to strings, or None for no label). The
        default is ``'auto'``, which will use ``time=%0.2f ms`` if there
        is more than one time point.
    smoothing_steps : int
        The amount of smoothing.

    transparent : bool | None
        If True: use a linear transparency between fmin and fmid
        and make values below fmin fully transparent (symmetrically for
        divergent colormaps). None will choose automatically based on colormap
        type.
    alpha : float
        Alpha value to apply globally to the overlay. Has no effect with mpl
        backend.
    time_viewer : bool | str
        Display time viewer GUI. Can also be 'auto', which will mean True
        for the PyVista backend and False otherwise.

        🎭 Changed in version 0.20.0
           "auto" mode added.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    figure : instance of Figure3D | instance of matplotlib.figure.Figure | list | int | None
        If None, a new figure will be created. If multiple views or a
        split view is requested, this must be a list of the appropriate
        length. If int is provided it will be used to identify the PyVista
        figure by it's id or create a new figure with the given id. If an
        instance of matplotlib figure, mpl backend is used for plotting.

    views : str | list
        View to use. Using multiple views (list) is not supported for mpl
        backend. See `Brain.show_view <mne.viz.Brain.show_view>` for
        valid string options.

        When plotting a standard SourceEstimate (not volume, mixed, or vector)
        and using the PyVista backend, ``views='flat'`` is also supported to
        plot cortex as a flatmap.

        Using multiple views (list) is not supported by the matplotlib backend.

        🎭 Changed in version 0.21.0
           Support for flatmaps.
    colorbar : bool
        If True, display colorbar on scene.

    clim : str | dict
        Colorbar properties specification. If 'auto', set clim automatically
        based on data percentiles. If dict, should contain:

            ``kind`` : 'value' | 'percent'
                Flag to specify type of limits.
            ``lims`` : list | np.ndarray | tuple of float, 3 elements
                Lower, middle, and upper bounds for colormap.
            ``pos_lims`` : list | np.ndarray | tuple of float, 3 elements
                Lower, middle, and upper bound for colormap. Positive values
                will be mirrored directly across zero during colormap
                construction to obtain negative control points.

        💡 Only one of ``lims`` or ``pos_lims`` should be provided.
                  Only sequential colormaps should be used with ``lims``, and
                  only divergent colormaps should be used with ``pos_lims``.
    cortex : str | tuple
        Specifies how binarized curvature values are rendered.
        Either the name of a preset Brain cortex colorscheme (one of
        ``'classic'``, ``'bone'``, ``'low_contrast'``, or ``'high_contrast'``),
        or the name of a colormap, or a tuple with values
        ``(colormap, min, max, reverse)`` to fully specify the curvature
        colors. Has no effect with the matplotlib backend.
    size : float or tuple of float
        The size of the window, in pixels. can be one number to specify
        a square window, or the (width, height) of a rectangular window.
        Has no effect with mpl backend.
    background : matplotlib color
        Color of the background of the display window.
    foreground : matplotlib color | None
        Color of the foreground of the display window. Has no effect with mpl
        backend. None will choose white or black based on the background color.
    initial_time : float | None
        The time to display on the plot initially. ``None`` to display the
        first time sample (default).
    time_unit : ``'s'`` | ``'ms'``
        Whether time is represented in seconds ("s", default) or
        milliseconds ("ms").
    backend : ``'auto'`` | ``'pyvistaqt'`` | ``'matplotlib'``
        Which backend to use. If ``'auto'`` (default), tries to plot with
        pyvistaqt, but resorts to matplotlib if no 3d backend is available.

        ✨ Added in version 0.15.0
    spacing : str
        Only affects the matplotlib backend.
        The spacing to use for the source space. Can be ``'ico#'`` for a
        recursively subdivided icosahedron, ``'oct#'`` for a recursively
        subdivided octahedron, or ``'all'`` for all points. In general, you can
        speed up the plotting by selecting a sparser source space.
        Defaults  to 'oct6'.

        ✨ Added in version 0.15.0
    title : str | None
        Title for the figure. If None, the subject name will be used.

        ✨ Added in version 0.17.0

    show_traces : bool | str | float
        If True, enable interactive picking of a point on the surface of the
        brain and plot its time course.
        This feature is only available with the PyVista 3d backend, and requires
        ``time_viewer=True``. Defaults to 'auto', which will use True if and
        only if ``time_viewer=True``, the backend is PyVista, and there is more
        than one time point. If float (between zero and one), it specifies what
        proportion of the total window should be devoted to traces (True is
        equivalent to 0.25, i.e., it will occupy the bottom 1/4 of the figure).

        ✨ Added in version 0.20.0

    src : instance of SourceSpaces | None
        The source space corresponding to the source estimate. Only necessary
        if the STC is a volume or mixed source estimate.
    volume_options : float | dict | None
        Options for volumetric source estimate plotting, with key/value pairs:

        - ``'resolution'`` : float | None
            Resolution (in mm) of volume rendering. Smaller (e.g., 1.) looks
            better at the cost of speed. None (default) uses the volume source
            space resolution, which is often something like 7 or 5 mm,
            without resampling.
        - ``'blending'`` : str
            Can be "mip" (default) for `maximum intensity projection` or
            "composite" for composite blending using alpha values.
        - ``'alpha'`` : float | None
            Alpha for the volumetric rendering. Defaults are 0.4 for vector source
            estimates and 1.0 for scalar source estimates.
        - ``'surface_alpha'`` : float | None
            Alpha for the surface enclosing the volume(s). None (default) will use
            half the volume alpha. Set to zero to avoid plotting the surface.
        - ``'silhouette_alpha'`` : float | None
            Alpha for a silhouette along the outside of the volume. None (default)
            will use ``0.25 * surface_alpha``.
        - ``'silhouette_linewidth'`` : float
            The line width to use for the silhouette. Default is 2.

        A float input (default 1.) or None will be used for the ``'resolution'``
        entry.

    view_layout : str
        Can be "vertical" (default) or "horizontal". When using "horizontal" mode,
        the PyVista backend must be used and hemi cannot be "split".

    add_data_kwargs : dict | None
        Additional arguments to brain.add_data (e.g.,
        ``dict(time_label_size=10)``).

    brain_kwargs : dict | None
        Additional arguments to the `mne.viz.Brain` constructor (e.g.,
        ``dict(silhouette=True)``).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    figure : instance of mne.viz.Brain | matplotlib.figure.Figure
        An instance of `mne.viz.Brain` or matplotlib figure.

    Notes
    -----
    Flatmaps are available by default for ``fsaverage`` but not for other
    subjects reconstructed by FreeSurfer. We recommend using
    `mne.compute_source_morph` to morph source estimates to ``fsaverage``
    for flatmap plotting. If you want to construct your own flatmap for a given
    subject, these links might help:

    - https://surfer.nmr.mgh.harvard.edu/fswiki/FreeSurferOccipitalFlattenedPatch
    - https://openwetware.org/wiki/Beauchamp:FreeSurfer
    """
    ...

def plot_volume_source_estimates(
    stc,
    src,
    subject=None,
    subjects_dir=None,
    mode: str = "stat_map",
    bg_img: str = "T1.mgz",
    colorbar: bool = True,
    colormap: str = "auto",
    clim: str = "auto",
    transparent=None,
    show: bool = True,
    initial_time=None,
    initial_pos=None,
    verbose=None,
):
    """Plot Nutmeg style volumetric source estimates using nilearn.

    Parameters
    ----------
    stc : VectorSourceEstimate
        The vector source estimate to plot.
    src : instance of SourceSpaces | instance of SourceMorph
        The source space. Can also be a SourceMorph to morph the STC to
        a new subject (see Examples).

        🎭 Changed in version 0.18
           Support for `SpatialImage`.

    subject : str | None
        The FreeSurfer subject name.
        If ``None``, ``stc.subject`` will be used.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    mode : ``'stat_map'`` | ``'glass_brain'``
        The plotting mode to use. For ``'glass_brain'``, activation absolute values are
        displayed after being transformed to a standard MNI brain.
    bg_img : instance of SpatialImage | str
        The background image used in the nilearn plotting function.
        Can also be a string to use the ``bg_img`` file in the subject's
        MRI directory (default is ``'T1.mgz'``).
        Not used in "glass brain" plotting.
    colorbar : bool, optional
        If True, display a colorbar on the right of the plots.

    colormap : str | np.ndarray of float, shape(n_colors, 3 | 4)
        Name of colormap to use or a custom look up table. If array, must
        be (n x 3) or (n x 4) array for with RGB or RGBA values between
        0 and 255.

    clim : str | dict
        Colorbar properties specification. If 'auto', set clim automatically
        based on data percentiles. If dict, should contain:

            ``kind`` : 'value' | 'percent'
                Flag to specify type of limits.
            ``lims`` : list | np.ndarray | tuple of float, 3 elements
                Lower, middle, and upper bounds for colormap.
            ``pos_lims`` : list | np.ndarray | tuple of float, 3 elements
                Lower, middle, and upper bound for colormap. Positive values
                will be mirrored directly across zero during colormap
                construction to obtain negative control points.

        💡 Only one of ``lims`` or ``pos_lims`` should be provided.
                  Only sequential colormaps should be used with ``lims``, and
                  only divergent colormaps should be used with ``pos_lims``.

    transparent : bool | None
        If True: use a linear transparency between fmin and fmid
        and make values below fmin fully transparent (symmetrically for
        divergent colormaps). None will choose automatically based on colormap
        type.
    show : bool
        Show figures if True. Defaults to True.
    initial_time : float | None
        The initial time to plot. Can be None (default) to use the time point
        with the maximal absolute value activation across all voxels
        or the ``initial_pos`` voxel (if ``initial_pos is None`` or not,
        respectively).

        ✨ Added in version 0.19
    initial_pos : ndarray, shape (3,) | None
        The initial position to use (in m). Can be None (default) to use the
        voxel with the maximum absolute value activation across all time points
        or at ``initial_time`` (if ``initial_time is None`` or not,
        respectively).

        ✨ Added in version 0.19

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    fig : instance of Figure
        The figure.

    Notes
    -----
    Click on any of the anatomical slices to explore the time series.
    Clicking on any time point will bring up the corresponding anatomical map.

    The left and right arrow keys can be used to navigate in time.
    To move in time by larger steps, use shift+left and shift+right.

    In ``'glass_brain'`` mode, values are transformed to the standard MNI
    brain using the FreeSurfer Talairach transformation
    ``$SUBJECTS_DIR/$SUBJECT/mri/transforms/talairach.xfm``.

    ✨ Added in version 0.17

    🎭 Changed in version 0.19
       MRI volumes are automatically transformed to MNI space in
       ``'glass_brain'`` mode.

    Examples
    --------
    Passing a `mne.SourceMorph` as the ``src``
    parameter can be useful for plotting in a different subject's space
    (here, a ``'sample'`` STC in ``'fsaverage'``'s space)::

    >>> morph = mne.compute_source_morph(src_sample, subject_to='fsaverage')  # doctest: +SKIP
    >>> fig = stc_vol_sample.plot(morph)  # doctest: +SKIP
    """
    ...

def plot_vector_source_estimates(
    stc,
    subject=None,
    hemi: str = "lh",
    colormap: str = "hot",
    time_label: str = "auto",
    smoothing_steps: int = 10,
    transparent=None,
    brain_alpha: float = 0.4,
    overlay_alpha=None,
    vector_alpha: float = 1.0,
    scale_factor=None,
    time_viewer: str = "auto",
    subjects_dir=None,
    figure=None,
    views: str = "lateral",
    colorbar: bool = True,
    clim: str = "auto",
    cortex: str = "classic",
    size: int = 800,
    background: str = "black",
    foreground=None,
    initial_time=None,
    time_unit: str = "s",
    show_traces: str = "auto",
    src=None,
    volume_options: float = 1.0,
    view_layout: str = "vertical",
    add_data_kwargs=None,
    brain_kwargs=None,
    verbose=None,
):
    """Plot VectorSourceEstimate with PyVista.

    A "glass brain" is drawn and all dipoles defined in the source estimate
    are shown using arrows, depicting the direction and magnitude of the
    current moment at the dipole. Additionally, an overlay is plotted on top of
    the cortex with the magnitude of the current.

    Parameters
    ----------
    stc : VectorSourceEstimate | MixedVectorSourceEstimate
        The vector source estimate to plot.

    subject : str | None
        The FreeSurfer subject name.
        If ``None``, ``stc.subject`` will be used.
    hemi : str, 'lh' | 'rh' | 'split' | 'both'
        The hemisphere to display.

    colormap : str | np.ndarray of float, shape(n_colors, 3 | 4)
        Name of colormap to use or a custom look up table. If array, must
        be (n x 3) or (n x 4) array for with RGB or RGBA values between
        0 and 255.
        This should be a sequential colormap.

    time_label : str | callable | None
        Format of the time label (a format string, a function that maps
        floating point time values to strings, or None for no label). The
        default is ``'auto'``, which will use ``time=%0.2f ms`` if there
        is more than one time point.
    smoothing_steps : int
        The amount of smoothing.

    transparent : bool | None
        If True: use a linear transparency between fmin and fmid
        and make values below fmin fully transparent (symmetrically for
        divergent colormaps). None will choose automatically based on colormap
        type.
    brain_alpha : float
        Alpha value to apply globally to the surface meshes. Defaults to 0.4.
    overlay_alpha : float
        Alpha value to apply globally to the overlay. Defaults to
        ``brain_alpha``.
    vector_alpha : float
        Alpha value to apply globally to the vector glyphs. Defaults to 1.
    scale_factor : float | None
        Scaling factor for the vector glyphs. By default, an attempt is made to
        automatically determine a sane value.
    time_viewer : bool | str
        Display time viewer GUI. Can be "auto", which is True for the PyVista
        backend and False otherwise.

        🎭 Changed in version 0.20
           Added "auto" option and default.
    subjects_dir : str
        The path to the freesurfer subjects reconstructions.
        It corresponds to Freesurfer environment variable SUBJECTS_DIR.
    figure : instance of Figure3D | list | int | None
        If None, a new figure will be created. If multiple views or a
        split view is requested, this must be a list of the appropriate
        length. If int is provided it will be used to identify the PyVista
        figure by it's id or create a new figure with the given id.

    views : str | list
        View to use. Using multiple views (list) is not supported for mpl
        backend. See `Brain.show_view <mne.viz.Brain.show_view>` for
        valid string options.
    colorbar : bool
        If True, display colorbar on scene.

    clim : str | dict
        Colorbar properties specification. If 'auto', set clim automatically
        based on data percentiles. If dict, should contain:

            ``kind`` : 'value' | 'percent'
                Flag to specify type of limits.
            ``lims`` : list | np.ndarray | tuple of float, 3 elements
                Lower, middle, and upper bound for colormap.

        Unlike `stc.plot <mne.SourceEstimate.plot>`, it cannot use
        ``pos_lims``, as the surface plot must show the magnitude.
    cortex : str or tuple
        Specifies how binarized curvature values are rendered.
        either the name of a preset Brain cortex colorscheme (one of
        'classic', 'bone', 'low_contrast', or 'high_contrast'), or the
        name of a colormap, or a tuple with values (colormap, min,
        max, reverse) to fully specify the curvature colors.
    size : float or tuple of float
        The size of the window, in pixels. can be one number to specify
        a square window, or the (width, height) of a rectangular window.
    background : matplotlib color
        Color of the background of the display window.
    foreground : matplotlib color | None
        Color of the foreground of the display window.
        None will choose black or white based on the background color.
    initial_time : float | None
        The time to display on the plot initially. ``None`` to display the
        first time sample (default).
    time_unit : 's' | 'ms'
        Whether time is represented in seconds ("s", default) or
        milliseconds ("ms").

    show_traces : bool | str | float
        If True, enable interactive picking of a point on the surface of the
        brain and plot its time course.
        This feature is only available with the PyVista 3d backend, and requires
        ``time_viewer=True``. Defaults to 'auto', which will use True if and
        only if ``time_viewer=True``, the backend is PyVista, and there is more
        than one time point. If float (between zero and one), it specifies what
        proportion of the total window should be devoted to traces (True is
        equivalent to 0.25, i.e., it will occupy the bottom 1/4 of the figure).

        ✨ Added in version 0.20.0

    src : instance of SourceSpaces | None
        The source space corresponding to the source estimate. Only necessary
        if the STC is a volume or mixed source estimate.
    volume_options : float | dict | None
        Options for volumetric source estimate plotting, with key/value pairs:

        - ``'resolution'`` : float | None
            Resolution (in mm) of volume rendering. Smaller (e.g., 1.) looks
            better at the cost of speed. None (default) uses the volume source
            space resolution, which is often something like 7 or 5 mm,
            without resampling.
        - ``'blending'`` : str
            Can be "mip" (default) for `maximum intensity projection` or
            "composite" for composite blending using alpha values.
        - ``'alpha'`` : float | None
            Alpha for the volumetric rendering. Defaults are 0.4 for vector source
            estimates and 1.0 for scalar source estimates.
        - ``'surface_alpha'`` : float | None
            Alpha for the surface enclosing the volume(s). None (default) will use
            half the volume alpha. Set to zero to avoid plotting the surface.
        - ``'silhouette_alpha'`` : float | None
            Alpha for a silhouette along the outside of the volume. None (default)
            will use ``0.25 * surface_alpha``.
        - ``'silhouette_linewidth'`` : float
            The line width to use for the silhouette. Default is 2.

        A float input (default 1.) or None will be used for the ``'resolution'``
        entry.

    view_layout : str
        Can be "vertical" (default) or "horizontal". When using "horizontal" mode,
        the PyVista backend must be used and hemi cannot be "split".

    add_data_kwargs : dict | None
        Additional arguments to brain.add_data (e.g.,
        ``dict(time_label_size=10)``).

    brain_kwargs : dict | None
        Additional arguments to the `mne.viz.Brain` constructor (e.g.,
        ``dict(silhouette=True)``).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    brain : mne.viz.Brain
        A instance of `mne.viz.Brain`.

    Notes
    -----
    ✨ Added in version 0.15

    If the current magnitude overlay is not desired, set ``overlay_alpha=0``
    and ``smoothing_steps=1``.
    """
    ...

def plot_sparse_source_estimates(
    src,
    stcs,
    colors=None,
    linewidth: int = 2,
    fontsize: int = 18,
    bgcolor=(0.05, 0, 0.1),
    opacity: float = 0.2,
    brain_color=(0.7, 0.7, 0.7),
    show: bool = True,
    high_resolution: bool = False,
    fig_name=None,
    fig_number=None,
    labels=None,
    modes=("cone", "sphere"),
    scale_factors=(1, 0.6),
    verbose=None,
    **kwargs,
):
    """Plot source estimates obtained with sparse solver.

    Active dipoles are represented in a "Glass" brain.
    If the same source is active in multiple source estimates it is
    displayed with a sphere otherwise with a cone in 3D.

    Parameters
    ----------
    src : dict
        The source space.
    stcs : instance of SourceEstimate or list of instances of SourceEstimate
        The source estimates.
    colors : list
        List of colors.
    linewidth : int
        Line width in 2D plot.
    fontsize : int
        Font size.
    bgcolor : tuple of length 3
        Background color in 3D.
    opacity : float in [0, 1]
        Opacity of brain mesh.
    brain_color : tuple of length 3
        Brain color.
    show : bool
        Show figures if True.
    high_resolution : bool
        If True, plot on the original (non-downsampled) cortical mesh.
    fig_name : str
        PyVista figure name.
    fig_number : int
        Matplotlib figure number.
    labels : ndarray or list of ndarray
        Labels to show sources in clusters. Sources with the same
        label and the waveforms within each cluster are presented in
        the same color. labels should be a list of ndarrays when
        stcs is a list ie. one label for each stc.
    modes : list
        Should be a list, with each entry being ``'cone'`` or ``'sphere'``
        to specify how the dipoles should be shown.
        The pivot for the glyphs in ``'cone'`` mode is always the tail
        whereas the pivot in ``'sphere'`` mode is the center.
    scale_factors : list
        List of floating point scale factors for the markers.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.
    **kwargs : kwargs
        Keyword arguments to pass to renderer.mesh.

    Returns
    -------
    surface : instance of Figure3D
        The 3D figure containing the triangular mesh surface.
    """
    ...

def plot_dipole_locations(
    dipoles,
    trans=None,
    subject=None,
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
    dipoles : list of instances of Dipole | Dipole
        The dipoles to plot.
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

def snapshot_brain_montage(fig, montage, hide_sensors: bool = True):
    """Take a snapshot of a PyVista Scene and project channels onto 2d coords.

    Note that this will take the raw values for 3d coordinates of each channel,
    without applying any transforms. If brain images are flipped up/dn upon
    using `imshow`, check your matplotlib backend as this
    behavior changes.

    Parameters
    ----------
    fig : instance of Figure3D
        The figure on which you've plotted electrodes using
        `mne.viz.plot_alignment`.
    montage : instance of DigMontage or Info | dict
        The digital montage for the electrodes plotted in the scene. If
        `Info`, channel positions will be pulled from the ``loc``
        field of ``chs``. dict should have ch:xyz mappings.
    hide_sensors : bool
        Whether to remove the spheres in the scene before taking a snapshot.
        The sensors will always be shown in the final figure. If you want an
        image of just the brain, use `mne.viz.Brain` instead.

    Returns
    -------
    xy : array, shape (n_channels, 2)
        The 2d location of each channel on the image of the current scene view.
    im : array, shape (m, n, 3)
        The screenshot of the current scene view.
    """
    ...

RAS_AFFINE: Incomplete
RAS_SHAPE: Incomplete

def plot_brain_colorbar(
    ax,
    clim,
    colormap: str = "auto",
    transparent: bool = True,
    orientation: str = "vertical",
    label: str = "Activation",
    bgcolor: str = "0.5",
):
    """Plot a colorbar that corresponds to a brain activation map.

    Parameters
    ----------
    ax : instance of Axes
        The Axes to plot into.

    clim : str | dict
        Colorbar properties specification. If 'auto', set clim automatically
        based on data percentiles. If dict, should contain:

            ``kind`` : 'value' | 'percent'
                Flag to specify type of limits.
            ``lims`` : list | np.ndarray | tuple of float, 3 elements
                Lower, middle, and upper bounds for colormap.
            ``pos_lims`` : list | np.ndarray | tuple of float, 3 elements
                Lower, middle, and upper bound for colormap. Positive values
                will be mirrored directly across zero during colormap
                construction to obtain negative control points.

        💡 Only one of ``lims`` or ``pos_lims`` should be provided.
                  Only sequential colormaps should be used with ``lims``, and
                  only divergent colormaps should be used with ``pos_lims``.

    colormap : str | np.ndarray of float, shape(n_colors, 3 | 4)
        Name of colormap to use or a custom look up table. If array, must
        be (n x 3) or (n x 4) array for with RGB or RGBA values between
        0 and 255.

    transparent : bool | None
        If True: use a linear transparency between fmin and fmid
        and make values below fmin fully transparent (symmetrically for
        divergent colormaps). None will choose automatically based on colormap
        type.
    orientation : str
        Orientation of the colorbar, can be "vertical" or "horizontal".
    label : str
        The colorbar label.
    bgcolor : color
        The color behind the colorbar (for alpha blending).

    Returns
    -------
    cbar : instance of ColorbarBase
        The colorbar.

    Notes
    -----
    ✨ Added in version 0.19
    """
    ...
@dataclass()
class _3d_Options:
    antialias: Optional[bool]
    depth_peeling: Optional[bool]
    smooth_shading: Optional[bool]
    multi_samples: Optional[int]

    def __init__(
        self, antialias, depth_peeling, smooth_shading, multi_samples
    ) -> None: ...

def set_3d_options(
    antialias=None, depth_peeling=None, smooth_shading=None, *, multi_samples=None
) -> None:
    """Set 3D rendering options.

    Parameters
    ----------
    antialias : bool | None
        If bool, whether to enable or disable full-screen anti-aliasing.
        False is useful when renderers have problems (such as software
        MESA renderers). If None, use the default setting. This option
        can also be controlled using an environment variable, e.g.,
        ``MNE_3D_OPTION_ANTIALIAS=false``.
    depth_peeling : bool | None
        If bool, whether to enable or disable accurate transparency.
        False is useful when renderers have problems (for instance
        while X forwarding on remote servers). If None, use the default
        setting. This option can also be controlled using an environment
        variable, e.g., ``MNE_3D_OPTION_DEPTH_PEELING=false``.
    smooth_shading : bool | None
        If bool, whether to enable or disable smooth color transitions
        between polygons. False is useful on certain configurations
        where this type of shading is not supported or for performance
        reasons. This option can also be controlled using an environment
        variable, e.g., ``MNE_3D_OPTION_SMOOTH_SHADING=false``.
    multi_samples : int
        Number of multi-samples. Should be 1 for MESA for volumetric rendering
        to work properly.

        ✨ Added in version 1.1

    Notes
    -----
    ✨ Added in version 0.21.0
    """
    ...
