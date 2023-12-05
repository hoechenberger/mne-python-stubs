from ..._fiff.meas_info import Info as Info
from ..._fiff.pick import pick_types as pick_types
from ..._freesurfer import (
    read_freesurfer_lut as read_freesurfer_lut,
    read_talxfm as read_talxfm,
    vertex_to_mni as vertex_to_mni,
)
from ...defaults import DEFAULTS as DEFAULTS
from ...surface import mesh_edges as mesh_edges
from ...transforms import Transform as Transform, apply_trans as apply_trans
from ...utils import (
    Bunch as Bunch,
    fill_doc as fill_doc,
    get_subjects_dir as get_subjects_dir,
    logger as logger,
    use_log_level as use_log_level,
    warn as warn,
)
from ..ui_events import (
    ColormapRange as ColormapRange,
    PlaybackSpeed as PlaybackSpeed,
    TimeChange as TimeChange,
    VertexSelect as VertexSelect,
    disable_ui_events as disable_ui_events,
    publish as publish,
    subscribe as subscribe,
    unsubscribe as unsubscribe,
)
from ..utils import concatenate_images as concatenate_images, safe_event as safe_event
from .colormap import calculate_lut as calculate_lut
from .view import views_dicts as views_dicts
from _typeshed import Incomplete

class Brain:
    """Class for visualizing a brain.

    ⛔️
       The API for this class is not currently complete. We suggest using
       `mne.viz.plot_source_estimates` with the PyVista backend
       enabled to obtain a ``Brain`` instance.

    Parameters
    ----------
    subject : str
        Subject name in Freesurfer subjects dir.

        🎭 Changed in version 1.2
           This parameter was renamed from ``subject_id`` to ``subject``.
    hemi : str
        Hemisphere id (ie 'lh', 'rh', 'both', or 'split'). In the case
        of 'both', both hemispheres are shown in the same window.
        In the case of 'split' hemispheres are displayed side-by-side
        in different viewing panes.
    surf : str
        FreeSurfer surface mesh name (ie 'white', 'inflated', etc.).
    title : str
        Title for the window.
    cortex : str, list, dict
        Specifies how the cortical surface is rendered. Options:

        1. The name of one of the preset cortex styles:
            ``'classic'`` (default), ``'high_contrast'``,
            ``'low_contrast'``, or ``'bone'``.
        2. A single color-like argument to render the cortex as a single
            color, e.g. ``'red'`` or ``(0.1, 0.4, 1.)``.
        3. A list of two color-like used to render binarized curvature
            values for gyral (first) and sulcal (second). regions, e.g.,
            ``['red', 'blue']`` or ``[(1, 0, 0), (0, 0, 1)]``.
        4. A dict containing keys ``'vmin', 'vmax', 'colormap'`` with
            values used to render the binarized curvature (where 0 is gyral,
            1 is sulcal).

        🎭 Changed in version 0.24
           Add support for non-string arguments.
    alpha : float in [0, 1]
        Alpha level to control opacity of the cortical surface.
    size : int | array-like, shape (2,)
        The size of the window, in pixels. can be one number to specify
        a square window, or a length-2 sequence to specify (width, height).
    background : tuple(int, int, int)
        The color definition of the background: (red, green, blue).
    foreground : matplotlib color
        Color of the foreground (will be used for colorbars and text).
        None (default) will use black or white depending on the value
        of ``background``.
    figure : list of Figure | None
        If None (default), a new window will be created with the appropriate
        views.
    subjects_dir : str | None
        If not None, this directory will be used as the subjects directory
        instead of the value set using the SUBJECTS_DIR environment
        variable.

    views : str | list
        View to use. Using multiple views (list) is not supported for mpl
        backend. See `Brain.show_view <mne.viz.Brain.show_view>` for
        valid string options.
    offset : bool | str
        If True, shifts the right- or left-most x coordinate of the left and
        right surfaces, respectively, to be at zero. This is useful for viewing
        inflated surface where hemispheres typically overlap. Can be "auto"
        (default) use True with inflated surfaces and False otherwise
        (Default: 'auto'). Only used when ``hemi='both'``.

        🎭 Changed in version 0.23
           Default changed to "auto".
    offscreen : bool
        If True, rendering will be done offscreen (not shown). Useful
        mostly for generating images or screenshots, but can be buggy.
        Use at your own risk.
    interaction : str
        Can be "trackball" (default) or "terrain", i.e. a turntable-style
        camera.
    units : str
        Can be 'm' or 'mm' (default).

    view_layout : str
        Can be "vertical" (default) or "horizontal". When using "horizontal" mode,
        the PyVista backend must be used and hemi cannot be "split".
    silhouette : dict | bool
       As a dict, it contains the ``color``, ``linewidth``, ``alpha`` opacity
       and ``decimate`` (level of decimation between 0 and 1 or None) of the
       brain's silhouette to display. If True, the default values are used
       and if False, no silhouette will be displayed. Defaults to False.

    theme : str | path-like
        Can be "auto", "light", or "dark" or a path-like to a
        custom stylesheet. For Dark-Mode and automatic Dark-Mode-Detection,
        `qdarkstyle <https://github.com/ColinDuquesnoy/QDarkStyleSheet>`__ and
        `darkdetect <https://github.com/albertosottile/darkdetect>`__,
        respectively, are required.    If None (default), the config option MNE_3D_OPTION_THEME will be used,
        defaulting to "auto" if it's not found.
    show : bool
        Display the window as soon as it is ready. Defaults to True.
    block : bool
        If True, start the Qt application event loop. Default to False.

    Attributes
    ----------
    geo : dict
        A dictionary of PyVista surface objects for each hemisphere.
    overlays : dict
        The overlays.

    Notes
    -----
    The figure will publish and subscribe to the following UI events:

    * `mne.viz.ui_events.TimeChange`
    * `mne.viz.ui_events.PlaybackSpeed`
    * `mne.viz.ui_events.ColormapRange`, ``kind="distributed_source_power"``
    * `mne.viz.ui_events.VertexSelect`

    This table shows the capabilities of each Brain backend ("✓" for full
    support, and "-" for partial support):

    .. table::
       :widths: auto

       +-------------------------------------+--------------+---------------+
       | 3D function:                        | surfer.Brain | mne.viz.Brain |
       +=====================================+==============+===============+
       | `add_annotation`              | ✓            | ✓             |
       +-------------------------------------+--------------+---------------+
       | `add_data`                    | ✓            | ✓             |
       +-------------------------------------+--------------+---------------+
       | `add_dipole`                  |              | ✓             |
       +-------------------------------------+--------------+---------------+
       | `add_foci`                    | ✓            | ✓             |
       +-------------------------------------+--------------+---------------+
       | `add_forward`                 |              | ✓             |
       +-------------------------------------+--------------+---------------+
       | `add_head`                    |              | ✓             |
       +-------------------------------------+--------------+---------------+
       | `add_label`                   | ✓            | ✓             |
       +-------------------------------------+--------------+---------------+
       | `add_sensors`                 |              | ✓             |
       +-------------------------------------+--------------+---------------+
       | `add_skull`                   |              | ✓             |
       +-------------------------------------+--------------+---------------+
       | `add_text`                    | ✓            | ✓             |
       +-------------------------------------+--------------+---------------+
       | `add_volume_labels`           |              | ✓             |
       +-------------------------------------+--------------+---------------+
       | `close`                       | ✓            | ✓             |
       +-------------------------------------+--------------+---------------+
       | data                                | ✓            | ✓             |
       +-------------------------------------+--------------+---------------+
       | foci                                | ✓            |               |
       +-------------------------------------+--------------+---------------+
       | labels                              | ✓            | ✓             |
       +-------------------------------------+--------------+---------------+
       | `remove_data`                 |              | ✓             |
       +-------------------------------------+--------------+---------------+
       | `remove_dipole`               |              | ✓             |
       +-------------------------------------+--------------+---------------+
       | `remove_forward`              |              | ✓             |
       +-------------------------------------+--------------+---------------+
       | `remove_head`                 |              | ✓             |
       +-------------------------------------+--------------+---------------+
       | `remove_labels`               | ✓            | ✓             |
       +-------------------------------------+--------------+---------------+
       | `remove_annotations`          | -            | ✓             |
       +-------------------------------------+--------------+---------------+
       | `remove_sensors`              |              | ✓             |
       +-------------------------------------+--------------+---------------+
       | `remove_skull`                |              | ✓             |
       +-------------------------------------+--------------+---------------+
       | `remove_text`                 |              | ✓             |
       +-------------------------------------+--------------+---------------+
       | `remove_volume_labels`        |              | ✓             |
       +-------------------------------------+--------------+---------------+
       | `save_image`                  | ✓            | ✓             |
       +-------------------------------------+--------------+---------------+
       | `save_movie`                  | ✓            | ✓             |
       +-------------------------------------+--------------+---------------+
       | `screenshot`                  | ✓            | ✓             |
       +-------------------------------------+--------------+---------------+
       | `show_view`                   | ✓            | ✓             |
       +-------------------------------------+--------------+---------------+
       | TimeViewer                          | ✓            | ✓             |
       +-------------------------------------+--------------+---------------+
       | `get_picked_points`           |              | ✓             |
       +-------------------------------------+--------------+---------------+
       | `add_data(volume) <add_data>` |              | ✓             |
       +-------------------------------------+--------------+---------------+
       | view_layout                         |              | ✓             |
       +-------------------------------------+--------------+---------------+
       | flatmaps                            |              | ✓             |
       +-------------------------------------+--------------+---------------+
       | vertex picking                      |              | ✓             |
       +-------------------------------------+--------------+---------------+
       | label picking                       |              | ✓             |
       +-------------------------------------+--------------+---------------+
    """

    time_viewer: bool
    silhouette: bool
    geo: Incomplete
    plotter: Incomplete
    widgets: Incomplete

    def __init__(
        self,
        subject,
        hemi: str = "both",
        surf: str = "pial",
        title=None,
        cortex: str = "classic",
        alpha: float = 1.0,
        size: int = 800,
        background: str = "black",
        foreground=None,
        figure=None,
        subjects_dir=None,
        views: str = "auto",
        *,
        offset: str = "auto",
        offscreen: bool = False,
        interaction: str = "trackball",
        units: str = "mm",
        view_layout: str = "vertical",
        silhouette: bool = False,
        theme=None,
        show: bool = True,
        block: bool = False,
    ) -> None: ...
    orientation: Incomplete
    default_smoothing_range: Incomplete
    playback: bool
    visibility: bool
    refresh_rate_ms: Incomplete
    default_scaling_range: Incomplete
    default_playback_speed_range: Incomplete
    default_playback_speed_value: float
    default_status_bar_msg: str
    default_label_extract_modes: Incomplete
    default_trace_modes: Incomplete
    annot: Incomplete
    label_extract_mode: Incomplete
    act_data_smooth: Incomplete
    color_list: Incomplete
    color_cycle: Incomplete
    mpl_canvas: Incomplete
    help_canvas: Incomplete
    rms: Incomplete
    picked_patches: Incomplete
    picked_points: Incomplete
    pick_table: Incomplete
    playback_speed: Incomplete
    interactor_fraction: float
    show_traces: bool
    separate_canvas: bool
    traces_mode: str

    def setup_time_viewer(
        self, time_viewer: bool = True, show_traces: bool = True
    ) -> None:
        """Configure the time viewer parameters.

        Parameters
        ----------
        time_viewer : bool
            If True, enable widgets interaction. Defaults to True.

        show_traces : bool
            If True, enable visualization of time traces. Defaults to True.

        Notes
        -----
        The keyboard shortcuts are the following:

        '?': Display help window
        'i': Toggle interface
        's': Apply auto-scaling
        'r': Restore original clim
        'c': Clear all traces
        'n': Shift the time forward by the playback speed
        'b': Shift the time backward by the playback speed
        'Space': Start/Pause playback
        'Up': Decrease camera elevation angle
        'Down': Increase camera elevation angle
        'Left': Decrease camera azimuth angle
        'Right': Increase camera azimuth angle
        """
        ...

    def toggle_interface(self, value=None) -> None:
        """Toggle the interface.

        Parameters
        ----------
        value : bool | None
            If True, the widgets are shown and if False, they
            are hidden. If None, the state of the widgets is
            toggled. Defaults to None.
        """
        ...

    def apply_auto_scaling(self) -> None:
        """Detect automatically fitting scaling parameters."""
        ...

    def restore_user_scaling(self) -> None:
        """Restore original scaling parameters."""
        ...

    def toggle_playback(self, value=None) -> None:
        """Toggle time playback.

        Parameters
        ----------
        value : bool | None
            If True, automatic time playback is enabled and if False,
            it's disabled. If None, the state of time playback is toggled.
            Defaults to None.
        """
        ...

    def reset(self) -> None:
        """Reset view, current time and time step."""
        ...

    def set_playback_speed(self, speed) -> None:
        """Set the time playback speed.

        Parameters
        ----------
        speed : float
            The speed of the playback.
        """
        ...

    def clear_glyphs(self) -> None:
        """Clear the picking glyphs."""
        ...

    def plot_time_course(self, hemi, vertex_id, color, update: bool = True):
        """Plot the vertex time course.

        Parameters
        ----------
        hemi : str
            The hemisphere id of the vertex.
        vertex_id : int
            The vertex identifier in the mesh.
        color : matplotlib color
            The color of the time course.

        update : bool
            Force an update of the plot. Defaults to True.

        Returns
        -------
        line : matplotlib object
            The time line object.
        """
        ...
    time_line: Incomplete

    def plot_time_line(self, update: bool = True) -> None:
        """Add the time line to the MPL widget.

        Parameters
        ----------

        update : bool
            Force an update of the plot. Defaults to True.
        """
        ...

    def help(self) -> None:
        """Display the help window."""
        ...

    @property
    def interaction(self):
        """The interaction style."""
        ...

    @interaction.setter
    def interaction(self, interaction) -> None:
        """The interaction style."""
        ...

    def add_data(
        self,
        array,
        fmin=None,
        fmid=None,
        fmax=None,
        thresh=None,
        center=None,
        transparent: bool = False,
        colormap: str = "auto",
        alpha: int = 1,
        vertices=None,
        smoothing_steps=None,
        time=None,
        time_label: str = "auto",
        colorbar: bool = True,
        hemi=None,
        remove_existing=None,
        time_label_size=None,
        initial_time=None,
        scale_factor=None,
        vector_alpha=None,
        clim=None,
        src=None,
        volume_options: float = 0.4,
        colorbar_kwargs=None,
        verbose=None,
    ) -> None:
        """Display data from a numpy array on the surface or volume.

        This provides a similar interface to
        `surfer.Brain.add_overlay`, but it displays
        it with a single colormap. It offers more flexibility over the
        colormap, and provides a way to display four-dimensional data
        (i.e., a timecourse) or five-dimensional data (i.e., a
        vector-valued timecourse).

        💡 ``fmin`` sets the low end of the colormap, and is separate
                  from thresh (this is a different convention from
                  `surfer.Brain.add_overlay`).

        Parameters
        ----------
        array : numpy array, shape (n_vertices[, 3][, n_times])
            Data array. For the data to be understood as vector-valued
            (3 values per vertex corresponding to X/Y/Z surface RAS),
            then ``array`` must be have all 3 dimensions.
            If vectors with no time dimension are desired, consider using a
            singleton (e.g., ``np.newaxis``) to create a "time" dimension
            and pass ``time_label=None`` (vector values are not supported).

        fmin : float
            Minimum value in colormap (uses real fmin if None).
        fmid : float
            Intermediate value in colormap (fmid between fmin and
            fmax if None).
        fmax : float
            Maximum value in colormap (uses real max if None).

        thresh : None or float
            Not supported yet.
            If not None, values below thresh will not be visible.

        center : float or None
            If not None, center of a divergent colormap, changes the meaning of
            fmin, fmax and fmid.

        transparent : bool | None
            If True: use a linear transparency between fmin and fmid
            and make values below fmin fully transparent (symmetrically for
            divergent colormaps). None will choose automatically based on colormap
            type.
        colormap : str, list of color, or array
            Name of matplotlib colormap to use, a list of matplotlib colors,
            or a custom look up table (an n x 4 array coded with RBGA values
            between 0 and 255), the default "auto" chooses a default divergent
            colormap, if "center" is given (currently "icefire"), otherwise a
            default sequential colormap (currently "rocket").
        alpha : float in [0, 1]
            Alpha level to control opacity of the overlay.
        vertices : numpy array
            Vertices for which the data is defined (needed if
            ``len(data) < nvtx``).
        smoothing_steps : int or None
            Number of smoothing steps (smoothing is used if len(data) < nvtx)
            The value 'nearest' can be used too. None (default) will use as
            many as necessary to fill the surface.
        time : numpy array
            Time points in the data array (if data is 2D or 3D).

        time_label : str | callable | None
            Format of the time label (a format string, a function that maps
            floating point time values to strings, or None for no label). The
            default is ``'auto'``, which will use ``time=%0.2f ms`` if there
            is more than one time point.
        colorbar : bool
            Whether to add a colorbar to the figure. Can also be a tuple
            to give the (row, col) index of where to put the colorbar.
        hemi : str | None
            If None, it is assumed to belong to the hemisphere being
            shown. If two hemispheres are being shown, an error will
            be thrown.
        remove_existing : bool
            Not supported yet.
            Remove surface added by previous "add_data" call. Useful for
            conserving memory when displaying different data in a loop.
        time_label_size : int
            Font size of the time label (default 14).
        initial_time : float | None
            Time initially shown in the plot. ``None`` to use the first time
            sample (default).
        scale_factor : float | None (default)
            The scale factor to use when displaying glyphs for vector-valued
            data.
        vector_alpha : float | None
            Alpha level to control opacity of the arrows. Only used for
            vector-valued data. If None (default), ``alpha`` is used.
        clim : dict
            Original clim arguments.

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
                Can be "mip" (default) for :term:`maximum intensity projection` or
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
        colorbar_kwargs : dict | None
            Options to pass to ``pyvista.Plotter.add_scalar_bar``
            (e.g., ``dict(title_font_size=10)``).

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        Notes
        -----
        If the data is defined for a subset of vertices (specified
        by the "vertices" parameter), a smoothing method is used to interpolate
        the data onto the high resolution surface. If the data is defined for
        subsampled version of the surface, smoothing_steps can be set to None,
        in which case only as many smoothing steps are applied until the whole
        surface is filled with non-zeros.

        Due to a VTK alpha rendering bug, ``vector_alpha`` is
        clamped to be strictly < 1.
        """
        ...

    def remove_data(self) -> None:
        """Remove rendered data from the mesh."""
        ...

    def remove_labels(self) -> None:
        """Remove all the ROI labels from the image."""
        ...

    def remove_annotations(self) -> None:
        """Remove all annotations from the image."""
        ...

    def add_label(
        self,
        label,
        color=None,
        alpha: int = 1,
        scalar_thresh=None,
        borders: bool = False,
        hemi=None,
        subdir=None,
    ) -> None:
        """Add an ROI label to the image.

        Parameters
        ----------
        label : str | instance of Label
            Label filepath or name. Can also be an instance of
            an object with attributes "hemi", "vertices", "name", and
            optionally "color" and "values" (if scalar_thresh is not None).
        color : matplotlib-style color | None
            Anything matplotlib accepts: string, RGB, hex, etc. (default
            "crimson").
        alpha : float in [0, 1]
            Alpha level to control opacity.
        scalar_thresh : None | float
            Threshold the label ids using this value in the label
            file's scalar field (i.e. label only vertices with
            scalar >= thresh).
        borders : bool | int
            Show only label borders. If int, specify the number of steps
            (away from the true border) along the cortical mesh to include
            as part of the border definition.
        hemi : str | None
            If None, it is assumed to belong to the hemisphere being
            shown.
        subdir : None | str
            If a label is specified as name, subdir can be used to indicate
            that the label file is in a sub-directory of the subject's
            label directory rather than in the label directory itself (e.g.
            for ``$SUBJECTS_DIR/$SUBJECT/label/aparc/lh.cuneus.label``
            ``brain.add_label('cuneus', subdir='aparc')``).

        Notes
        -----
        To remove previously added labels, run Brain.remove_labels().
        """
        ...

    def add_forward(self, fwd, trans, alpha: int = 1, scale=None) -> None:
        """Add a quiver to render positions of dipoles.

        Parameters
        ----------

        fwd : instance of Forward
            The forward solution. If present, the orientations of the dipoles
            present in the forward solution are displayed.

        trans : str | dict | instance of Transform
            If str, the path to the head<->MRI transform ``*-trans.fif`` file produced
            during coregistration. Can also be ``'fsaverage'`` to use the built-in
            fsaverage transformation.

        alpha : float in [0, 1]
            Alpha level to control opacity. Default 1.
        scale : None | float
            The size of the arrow representing the dipoles in
            `mne.viz.Brain` units. Default 1.5mm.

        Notes
        -----
        ✨ Added in version 1.0
        """
        ...

    def remove_forward(self) -> None:
        """Remove forward sources from the rendered scene."""
        ...

    def add_dipole(
        self, dipole, trans, colors: str = "red", alpha: int = 1, scales=None
    ) -> None:
        """Add a quiver to render positions of dipoles.

        Parameters
        ----------
        dipole : instance of Dipole
            Dipole object containing position, orientation and amplitude of
            one or more dipoles or in the forward solution.

        trans : str | dict | instance of Transform
            If str, the path to the head<->MRI transform ``*-trans.fif`` file produced
            during coregistration. Can also be ``'fsaverage'`` to use the built-in
            fsaverage transformation.
        colors : list | matplotlib-style color | None
            A single color or list of anything matplotlib accepts:
            string, RGB, hex, etc. Default red.

        alpha : float in [0, 1]
            Alpha level to control opacity. Default 1.
        scales : list | float | None
            The size of the arrow representing the dipole in
            `mne.viz.Brain` units. Default 5mm.

        Notes
        -----
        ✨ Added in version 1.0
        """
        ...

    def remove_dipole(self) -> None:
        """Remove dipole objects from the rendered scene."""
        ...

    def add_head(
        self, dense: bool = True, color: str = "gray", alpha: float = 0.5
    ) -> None:
        """Add a mesh to render the outer head surface.

        Parameters
        ----------
        dense : bool
            Whether to plot the dense head (``seghead``) or the less dense head
            (``head``).

        color : color
            A list of anything matplotlib accepts: string, RGB, hex, etc.

        alpha : float in [0, 1]
            Alpha level to control opacity.

        Notes
        -----
        ✨ Added in version 0.24
        """
        ...

    def remove_head(self) -> None:
        """Remove head objects from the rendered scene."""
        ...

    def add_skull(
        self, outer: bool = True, color: str = "gray", alpha: float = 0.5
    ) -> None:
        """Add a mesh to render the skull surface.

        Parameters
        ----------
        outer : bool
            Adds the outer skull if ``True``, otherwise adds the inner skull.

        color : color
            A list of anything matplotlib accepts: string, RGB, hex, etc.

        alpha : float in [0, 1]
            Alpha level to control opacity.

        Notes
        -----
        ✨ Added in version 0.24
        """
        ...

    def remove_skull(self) -> None:
        """Remove skull objects from the rendered scene."""
        ...

    def add_volume_labels(
        self,
        aseg: str = "aparc+aseg",
        labels=None,
        colors=None,
        alpha: float = 0.5,
        smooth: float = 0.9,
        fill_hole_size=None,
        legend=None,
    ) -> None:
        """Add labels to the rendering from an anatomical segmentation.

        Parameters
        ----------

        aseg : str
            The anatomical segmentation file. Default ``aparc+aseg``. This may
            be any anatomical segmentation file in the mri subdirectory of the
            Freesurfer subject directory.
        labels : list
            Labeled regions of interest to plot. See
            `mne.get_montage_volume_labels`
            for one way to determine regions of interest. Regions can also be
            chosen from the :term:`FreeSurfer LUT`.
        colors : list | matplotlib-style color | None
            A list of anything matplotlib accepts: string, RGB, hex, etc.
            (default :term:`FreeSurfer LUT` colors).

        alpha : float in [0, 1]
            Alpha level to control opacity.

        smooth : float in [0, 1)
            The smoothing factor to be applied. Default 0 is no smoothing.
        fill_hole_size : int | None
            The size of holes to remove in the mesh in voxels. Default is None,
            no holes are removed. Warning, this dilates the boundaries of the
            surface by ``fill_hole_size`` number of voxels so use the minimal
            size.
        legend : bool | None | dict
            Add a legend displaying the names of the ``labels``. Default (None)
            is ``True`` if the number of ``labels`` is 10 or fewer.
            Can also be a dict of ``kwargs`` to pass to
            ``pyvista.Plotter.add_legend``.

        Notes
        -----
        ✨ Added in version 0.24
        """
        ...

    def remove_volume_labels(self) -> None:
        """Remove the volume labels from the rendered scene."""
        ...

    def add_foci(
        self,
        coords,
        coords_as_verts: bool = False,
        map_surface=None,
        scale_factor: int = 1,
        color: str = "white",
        alpha: int = 1,
        name=None,
        hemi=None,
        resolution: int = 50,
    ) -> None:
        """Add spherical foci, possibly mapping to displayed surf.

        The foci spheres can be displayed at the coordinates given, or
        mapped through a surface geometry. In other words, coordinates
        from a volume-based analysis in MNI space can be displayed on an
        inflated average surface by finding the closest vertex on the
        white surface and mapping to that vertex on the inflated mesh.

        Parameters
        ----------
        coords : ndarray, shape (n_coords, 3)
            Coordinates in stereotaxic space (default) or array of
            vertex ids (with ``coord_as_verts=True``).
        coords_as_verts : bool
            Whether the coords parameter should be interpreted as vertex ids.
        map_surface : str | None
            Surface to project the coordinates to, or None to use raw coords.
            When set to a surface, each foci is positioned at the closest
            vertex in the mesh.
        scale_factor : float
            Controls the size of the foci spheres (relative to 1cm).

        color : color
            A list of anything matplotlib accepts: string, RGB, hex, etc.

        alpha : float in [0, 1]
            Alpha level to control opacity. Default is 1.
        name : str
            Internal name to use.
        hemi : str | None
            If None, it is assumed to belong to the hemisphere being
            shown. If two hemispheres are being shown, an error will
            be thrown.
        resolution : int
            The resolution of the spheres.
        """
        ...

    def add_sensors(
        self,
        info,
        trans,
        meg=None,
        eeg: str = "original",
        fnirs: bool = True,
        ecog: bool = True,
        seeg: bool = True,
        dbs: bool = True,
        max_dist: float = 0.004,
        *,
        sensor_colors=None,
        verbose=None,
    ) -> None:
        """Add mesh objects to represent sensor positions.

        Parameters
        ----------

        info : mne.Info
            The `mne.Info` object with information about the sensors and methods of measurement.

        trans : str | dict | instance of Transform
            If str, the path to the head<->MRI transform ``*-trans.fif`` file produced
            during coregistration. Can also be ``'fsaverage'`` to use the built-in
            fsaverage transformation.

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

        fnirs : str | list | dict | bool | None
            Can be "channels", "pairs", "detectors", and/or "sources" to show the
            fNIRS channel locations, optode locations, or line between
            source-detector pairs, or a combination like ``('pairs', 'channels')``.
            True translates to ``('pairs',)``. A dict can also be used to specify
            alpha values (but only "channels" and "pairs" will be used), e.g.
            ``dict(channels=0.2, pairs=0.7)``.

            🎭 Changed in version 1.6
               Added support for specifying alpha values as a dict.

        ecog : bool
            If True (default), show ECoG sensors.

        seeg : bool
            If True (default), show sEEG electrodes.

        dbs : bool
            If True (default), show DBS (deep brain stimulation) electrodes.

        max_dist : float
            The maximum distance to project a sensor to the pial surface in meters.
            Sensors that are greater than this distance from the pial surface will
            not be assigned locations. Projections can be done to the inflated or
            flat brain.

        sensor_colors : array-like of color | dict | None
            Colors to use for the sensor glyphs. Can be None (default) to use default colors.
            A dict should provide the colors (values) for each channel type (keys), e.g.::

                dict(eeg=eeg_colors)

            Where the value (``eeg_colors`` above) can be broadcast to an array of colors with
            length that matches the number of channels of that type, i.e., is compatible with
            `matplotlib.colors.to_rgba_array`. A few examples of this for the case above
            are the string ``"k"``, a list of ``n_eeg`` color strings, or an NumPy ndarray of
            shape ``(n_eeg, 3)`` or ``(n_eeg, 4)``.

            ✨ Added in version 1.6

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        Notes
        -----
        ✨ Added in version 0.24
        """
        ...

    def remove_sensors(self, kind=None) -> None:
        """Remove sensors from the rendered scene.

        Parameters
        ----------
        kind : str | list | None
            If None, removes all sensor-related data including the helmet.
            Can be "meg", "eeg", "fnirs", "ecog", "seeg", "dbs" or "helmet"
            to remove that item.
        """
        ...

    def add_text(
        self,
        x,
        y,
        text,
        name=None,
        color=None,
        opacity: float = 1.0,
        row: int = 0,
        col: int = 0,
        font_size=None,
        justification=None,
    ) -> None:
        """Add a text to the visualization.

        Parameters
        ----------
        x : float
            X coordinate.
        y : float
            Y coordinate.
        text : str
            Text to add.
        name : str
            Name of the text (text label can be updated using update_text()).
        color : tuple
            Color of the text. Default is the foreground color set during
            initialization (default is black or white depending on the
            background color).
        opacity : float
            Opacity of the text (default 1.0).
        row : int | None
            Row index of which brain to use. Default is the top row.
        col : int | None
            Column index of which brain to use. Default is the left-most
            column.
        font_size : float | None
            The font size to use.
        justification : str | None
            The text justification.
        """
        ...

    def remove_text(self, name=None) -> None:
        """Remove text from the rendered scene.

        Parameters
        ----------
        name : str | None
            Remove specific text by name. If None, all text will be removed.
        """
        ...

    def add_annotation(
        self,
        annot,
        borders: bool = True,
        alpha: int = 1,
        hemi=None,
        remove_existing: bool = True,
        color=None,
    ) -> None:
        """Add an annotation file.

        Parameters
        ----------
        annot : str | tuple
            Either path to annotation file or annotation name. Alternatively,
            the annotation can be specified as a ``(labels, ctab)`` tuple per
            hemisphere, i.e. ``annot=(labels, ctab)`` for a single hemisphere
            or ``annot=((lh_labels, lh_ctab), (rh_labels, rh_ctab))`` for both
            hemispheres. ``labels`` and ``ctab`` should be arrays as returned
            by `nibabel.freesurfer.io.read_annot`.
        borders : bool | int
            Show only label borders. If int, specify the number of steps
            (away from the true border) along the cortical mesh to include
            as part of the border definition.

        alpha : float in [0, 1]
            Alpha level to control opacity. Default is 1.
        hemi : str | None
            If None, it is assumed to belong to the hemisphere being
            shown. If two hemispheres are being shown, data must exist
            for both hemispheres.
        remove_existing : bool
            If True (default), remove old annotations.
        color : matplotlib-style color code
            If used, show all annotations in the same (specified) color.
            Probably useful only when showing annotation borders.
        """
        ...

    def close(self) -> None:
        """Close all figures and cleanup data structure."""
        ...

    def show(self) -> None:
        """Display the window."""
        ...

    def get_view(self, row: int = 0, col: int = 0, *, align: bool = True):
        """Get the camera orientation for a given subplot display.

        Parameters
        ----------
        row : int
            The row to use, default is the first one.
        col : int
            The column to check, the default is the first one.

        align : bool
            If True, consider view arguments relative to canonical MRI
            directions (closest to MNI for the subject) rather than native MRI
            space. This helps when MRIs are not in standard orientation (e.g.,
            have large rotations).

        Returns
        -------

        roll : float | None
            The roll of the camera rendering the view in degrees.

        distance : float | "auto" | None
            The distance from the camera rendering the view to the focalpoint
            in plot units (either m or mm). If "auto", the bounds of visible objects will be
            used to set a reasonable distance.

            🎭 Changed in version 1.6
               ``None`` will no longer change the distance, use ``"auto"`` instead.

        azimuth : float
            The azimuthal angle of the camera rendering the view in degrees.

        elevation : float
            The The zenith angle of the camera rendering the view in degrees.

        focalpoint : tuple, shape (3,) | str | None
            The focal point of the camera rendering the view: (x, y, z) in
            plot units (either m or mm). When ``"auto"``, it is set to the center of
            mass of the visible bounds.
        """
        ...

    def show_view(
        self,
        view=None,
        roll=None,
        distance=None,
        *,
        row=None,
        col=None,
        hemi=None,
        align: bool = True,
        azimuth=None,
        elevation=None,
        focalpoint=None,
        update: bool = True,
        verbose=None,
    ) -> None:
        """Orient camera to display view.

        Parameters
        ----------

        view : str | None
            The name of the view to show (e.g. "lateral"). Other arguments
            take precedence and modify the camera starting from the ``view``.
            See `Brain.show_view <mne.viz.Brain.show_view>` for valid
            string shortcut options.

        roll : float | None
            The roll of the camera rendering the view in degrees.

        distance : float | "auto" | None
            The distance from the camera rendering the view to the focalpoint
            in plot units (either m or mm). If "auto", the bounds of visible objects will be
            used to set a reasonable distance.

            🎭 Changed in version 1.6
               ``None`` will no longer change the distance, use ``"auto"`` instead.
        row : int | None
            The row to set. Default all rows.
        col : int | None
            The column to set. Default all columns.
        hemi : str | None
            Which hemi to use for view lookup (when in "both" mode).

        align : bool
            If True, consider view arguments relative to canonical MRI
            directions (closest to MNI for the subject) rather than native MRI
            space. This helps when MRIs are not in standard orientation (e.g.,
            have large rotations).

        azimuth : float
            The azimuthal angle of the camera rendering the view in degrees.

        elevation : float
            The The zenith angle of the camera rendering the view in degrees.

        focalpoint : tuple, shape (3,) | str | None
            The focal point of the camera rendering the view: (x, y, z) in
            plot units (either m or mm). When ``"auto"``, it is set to the center of
            mass of the visible bounds.

        update : bool
            Force an update of the plot. Defaults to True.

            ✨ Added in version 1.6

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        Notes
        -----
        The builtin string views are the following perspectives, based on the
        :term:`RAS` convention. If not otherwise noted, the view will have the
        top of the brain (superior, +Z) in 3D space shown upward in the 2D
        perspective:

        ``'lateral'``
            From the left or right side such that the lateral (outside)
            surface of the given hemisphere is visible.
        ``'medial'``
            From the left or right side such that the medial (inside)
            surface of the given hemisphere is visible (at least when in split
            or single-hemi mode).
        ``'rostral'``
            From the front.
        ``'caudal'``
            From the rear.
        ``'dorsal'``
            From above, with the front of the brain pointing up.
        ``'ventral'``
            From below, with the front of the brain pointing up.
        ``'frontal'``
            From the front and slightly lateral, with the brain slightly
            tilted forward (yielding a view from slightly above).
        ``'parietal'``
            From the rear and slightly lateral, with the brain slightly tilted
            backward (yielding a view from slightly above).
        ``'axial'``
            From above with the brain pointing up (same as ``'dorsal'``).
        ``'sagittal'``
            From the right side.
        ``'coronal'``
            From the rear.

        Three letter abbreviations (e.g., ``'lat'``) of all of the above are
        also supported.
        """
        ...

    def reset_view(self) -> None:
        """Reset the camera."""
        ...

    def save_image(self, filename=None, mode: str = "rgb") -> None:
        """Save view from all panels to disk.

        Parameters
        ----------
        filename : path-like
            Path to new image file.
        mode : str
            Either ``'rgb'`` or ``'rgba'`` for values to return.
        """
        ...

    def screenshot(self, mode: str = "rgb", time_viewer: bool = False):
        """Generate a screenshot of current view.

        Parameters
        ----------
        mode : str
            Either ``'rgb'`` or ``'rgba'`` for values to return.

        time_viewer : bool
            If True, include time viewer traces. Only used if
            ``time_viewer=True`` and ``separate_canvas=False``.

        Returns
        -------
        screenshot : array
            Image pixel values.
        """
        ...

    def update_lut(self, fmin=None, fmid=None, fmax=None, alpha=None) -> None:
        """Update the range of the color map.

        Parameters
        ----------

        fmin : float
            Minimum value in colormap (uses real fmin if None).
        fmid : float
            Intermediate value in colormap (fmid between fmin and
            fmax if None).
        fmax : float
            Maximum value in colormap (uses real max if None).

        alpha : float in [0, 1]
            Alpha level to control opacity.
        """
        ...

    def set_data_smoothing(self, n_steps) -> None:
        """Set the number of smoothing steps.

        Parameters
        ----------
        n_steps : int
            Number of smoothing steps.
        """
        ...

    @property
    def time_interpolation(self):
        """The interpolation mode."""
        ...

    def set_time_interpolation(self, interpolation) -> None:
        """Set the interpolation mode.

        Parameters
        ----------

        interpolation : str | None
            Interpolation method (`scipy.interpolate.interp1d` parameter).
            Must be one of ``'linear'``, ``'nearest'``, ``'zero'``, ``'slinear'``,
            ``'quadratic'`` or ``'cubic'``.
        """
        ...

    def set_time_point(self, time_idx) -> None:
        """Set the time point to display (can be a float to interpolate).

        Parameters
        ----------
        time_idx : int | float
            The time index to use. Can be a float to use interpolation
            between indices.
        """
        ...

    def set_time(self, time) -> None:
        """Set the time to display (in seconds).

        Parameters
        ----------
        time : float
            The time to show, in seconds.
        """
        ...

    @property
    def data(self):
        """Data used by time viewer and color bar widgets."""
        ...

    @property
    def labels(self): ...
    @property
    def views(self): ...
    @property
    def hemis(self): ...
    def save_movie(
        self,
        filename=None,
        time_dilation: float = 4.0,
        tmin=None,
        tmax=None,
        framerate: int = 24,
        interpolation=None,
        codec=None,
        bitrate=None,
        callback=None,
        time_viewer: bool = False,
        **kwargs,
    ) -> None:
        """Save a movie (for data with a time axis).

        The movie is created through the `imageio` module. The format is
        determined by the extension, and additional options can be specified
        through keyword arguments that depend on the format, see
        :doc:`imageio's format page <imageio:formats/index>`.

        ⛔️
            This method assumes that time is specified in seconds when adding
            data. If time is specified in milliseconds this will result in
            movies 1000 times longer than expected.

        Parameters
        ----------
        filename : str
            Path at which to save the movie. The extension determines the
            format (e.g., ``'*.mov'``, ``'*.gif'``, ...; see the `imageio`
            documentation for available formats).
        time_dilation : float
            Factor by which to stretch time (default 4). For example, an epoch
            from -100 to 600 ms lasts 700 ms. With ``time_dilation=4`` this
            would result in a 2.8 s long movie.
        tmin : float
            First time point to include (default: all data).
        tmax : float
            Last time point to include (default: all data).
        framerate : float
            Framerate of the movie (frames per second, default 24).

        interpolation : str | None
            Interpolation method (`scipy.interpolate.interp1d` parameter).
            Must be one of ``'linear'``, ``'nearest'``, ``'zero'``, ``'slinear'``,
            ``'quadratic'`` or ``'cubic'``.
            If None, it uses the current ``brain.interpolation``,
            which defaults to ``'nearest'``. Defaults to None.
        codec : str | None
            The codec to use.
        bitrate : float | None
            The bitrate to use.
        callback : callable | None
            A function to call on each iteration. Useful for status message
            updates. It will be passed keyword arguments ``frame`` and
            ``n_frames``.

        time_viewer : bool
            If True, include time viewer traces. Only used if
            ``time_viewer=True`` and ``separate_canvas=False``.
        **kwargs : dict
            Specify additional options for `imageio`.
        """
        ...

    def get_picked_points(self):
        """Return the vertices of the picked points.

        Returns
        -------
        points : list of int | None
            The vertices picked by the time viewer.
        """
        ...

    def __hash__(self):
        """Hash the object."""
        ...

class _FakeIren:
    def EnterEvent(self) -> None: ...
    def MouseMoveEvent(self) -> None: ...
    def LeaveEvent(self) -> None: ...
    def SetEventInformation(self, *args, **kwargs) -> None: ...
    def CharEvent(self) -> None: ...
    def KeyPressEvent(self, *args, **kwargs) -> None: ...
    def KeyReleaseEvent(self, *args, **kwargs) -> None: ...
