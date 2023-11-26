from .._fiff.constants import FIFF as FIFF
from .._fiff.meas_info import Info as Info
from .._fiff.open import show_fiff as show_fiff
from .._fiff.pick import (
    channel_indices_by_type as channel_indices_by_type,
    channel_type as channel_type,
    pick_channels as pick_channels,
    pick_channels_cov as pick_channels_cov,
    pick_info as pick_info,
)
from .._fiff.proj import Projection as Projection, setup_proj as setup_proj
from ..rank import compute_rank as compute_rank
from ..transforms import apply_trans as apply_trans
from ..utils import (
    check_version as check_version,
    fill_doc as fill_doc,
    get_config as get_config,
    logger as logger,
    warn as warn,
)
from .ui_events import (
    ColormapRange as ColormapRange,
    publish as publish,
    subscribe as subscribe,
)
from _typeshed import Incomplete

def safe_event(fun, *args, **kwargs):
    """## 🧠 Protect against Qt exiting on event-handling errors."""
    ...

def plt_show(show: bool = True, fig=None, **kwargs) -> None:
    """## 🧠 Show a figure while suppressing warnings.

    -----
    ### 🛠️ Parameters

    #### `show : bool`
        Show the figure.
    #### `fig : instance of Figure | None`
        If non-None, use fig.show().
    **kwargs : dict
        Extra arguments for `matplotlib.pyplot.show`.
    """
    ...

def mne_analyze_colormap(limits=[5, 10, 15], format: str = "vtk"):
    """## 🧠 Return a colormap similar to that used by mne_analyze.

    -----
    ### 🛠️ Parameters

    #### `limits : list (or array) of length 3 or 6`
        Bounds for the colormap, which will be mirrored across zero if length
        3, or completely specified (and potentially asymmetric) if length 6.
    #### `format : str`
        Type of colormap to return. If 'matplotlib', will return a
        matplotlib.colors.LinearSegmentedColormap. If 'vtk', will
        return an RGBA array of shape (256, 4).

    -----
    ### ⏎ Returns

    #### `cmap : instance of colormap | array`
        A teal->blue->gray->red->yellow colormap. See docstring of the 'format'
        argument for further details.

    -----
    ### 📖 Notes

    For this will return a colormap that will display correctly for data
    that are scaled by the plotting function to span [-fmax, fmax].
    """
    ...

def compare_fiff(
    fname_1,
    fname_2,
    fname_out=None,
    show: bool = True,
    indent: str = "    ",
    read_limit=...,
    max_str: int = 30,
    verbose=None,
):
    """## 🧠 Compare the contents of two fiff files using diff and show_fiff.

    -----
    ### 🛠️ Parameters

    fname_1 : path-like
        First file to compare.
    fname_2 : path-like
        Second file to compare.
    #### `fname_out : path-like | None`
        Filename to store the resulting diff. If None, a temporary
        file will be created.
    #### `show : bool`
        If True, show the resulting diff in a new tab in a web browser.
    #### `indent : str`
        How to indent the lines.
    #### `read_limit : int`
        Max number of bytes of data to read from a tag. Can be np.inf
        to always read all data (helps test read completion).
    #### `max_str : int`
        Max number of characters of string representation to print for
        each tag's data.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `fname_out : str`
        The filename used for storing the diff. Could be useful for
        when a temporary file is used.
    """
    ...

def figure_nobar(*args, **kwargs):
    """## 🧠 Make matplotlib figure with no toolbar.

    -----
    ### 🛠️ Parameters

    *args : list
        Arguments to pass to `matplotlib.pyplot.figure`.
    **kwargs : dict
        Keyword arguments to pass to `matplotlib.pyplot.figure`.

    -----
    ### ⏎ Returns

    #### `fig : instance of Figure`
        The figure.
    """
    ...

class ClickableImage:
    """## 🧠 Display an image so you can click on it and store x/y positions.

    Takes as input an image array (can be any array that works with imshow,
    but will work best with images.  Displays the image and lets you
    click on it.  Stores the xy coordinates of each click, so now you can
    superimpose something on top of it.

    Upon clicking, the x/y coordinate of the cursor will be stored in
    self.coords, which is a list of (x, y) tuples.

    -----
    ### 🛠️ Parameters

    #### `imdata : ndarray`
        The image that you wish to click on for 2-d points.
    **kwargs : dict
        Keyword arguments. Passed to ax.imshow.

    -----
    ### 📖 Notes

    ✨ Added in vesion 0.9.0
    """

    coords: Incomplete
    imdata: Incomplete
    fig: Incomplete
    ax: Incomplete
    ymax: Incomplete
    xmax: Incomplete
    im: Incomplete

    def __init__(self, imdata, **kwargs) -> None:
        """## 🧠 Display the image for clicking."""
        ...
    def onclick(self, event) -> None:
        """## 🧠 Handle Mouse clicks.

        -----
        ### 🛠️ Parameters

        #### `event : matplotlib.backend_bases.Event`
            The matplotlib object that we use to get x/y position.
        """
        ...
    def plot_clicks(self, **kwargs) -> None:
        """## 🧠 Plot the x/y positions stored in self.coords.

        -----
        ### 🛠️ Parameters

        **kwargs : dict
            Arguments are passed to imshow in displaying the bg image.
        """
        ...
    def to_layout(self, **kwargs):
        """## 🧠 Turn coordinates into an MNE Layout object.

        Normalizes by the image you used to generate clicks

        -----
        ### 🛠️ Parameters

        **kwargs : dict
            Arguments are passed to generate_2d_layout.

        -----
        ### ⏎ Returns

        #### `layout : instance of Layout`
            The layout.
        """
        ...

def add_background_image(fig, im, set_ratios=None):
    """## 🧠 Add a background image to a plot.

    Adds the image specified in ``im`` to the
    figure ``fig``. This is generally meant to
    be done with topo plots, though it could work
    for any plot.

    ### 💡 Note This modifies the figure and/or axes in place.

    -----
    ### 🛠️ Parameters

    #### `fig : Figure`
        The figure you wish to add a bg image to.
    #### `im : array, shape (M, N, {3, 4})`
        A background image for the figure. This must be a valid input to
        `matplotlib.pyplot.imshow`. Defaults to None.
    #### `set_ratios : None | str`
        Set the aspect ratio of any axes in fig
        to the value in set_ratios. Defaults to None,
        which does nothing to axes.

    -----
    ### ⏎ Returns

    #### `ax_im : instance of Axes`
        Axes created corresponding to the image you added.

    -----
    ### 📖 Notes

    ✨ Added in vesion 0.9.0
    """
    ...

def plot_sensors(
    info,
    kind: str = "topomap",
    ch_type=None,
    title=None,
    show_names: bool = False,
    ch_groups=None,
    to_sphere: bool = True,
    axes=None,
    block: bool = False,
    show: bool = True,
    sphere=None,
    pointsize=None,
    linewidth: int = 2,
    *,
    cmap=None,
    verbose=None,
):
    """## 🧠 Plot sensors positions.

    -----
    ### 🛠️ Parameters


    #### `info : mne.Info`
        The `mne.Info` object with information about the sensors and methods of measurement.
    #### `kind : str`
        Whether to plot the sensors as 3d, topomap or as an interactive
        sensor selection dialog. Available options ``'topomap'``, ``'3d'``,
        ``'select'``. If ``'select'``, a set of channels can be selected
        interactively by using lasso selector or clicking while holding control
        key. The selected channels are returned along with the figure instance.
        Defaults to ``'topomap'``.
    #### `ch_type : None | str`
        The channel type to plot. Available options ``'mag'``, ``'grad'``,
        ``'eeg'``, ``'seeg'``, ``'dbs'``, ``'ecog'``, ``'all'``. If ``'all'``,
        all the available mag, grad, eeg, seeg, dbs and ecog channels are
        plotted. If None (default), then channels are chosen in the order given
        above.
    #### `title : str | None`
        Title for the figure. If None (default), equals to
        ``'Sensor positions (%s)' % ch_type``.
    #### `show_names : bool | array of str`
        Whether to display all channel names. If an array, only the channel
        names in the array are shown. Defaults to False.
    #### `ch_groups : 'position' | list of list | None`
        Channel groups for coloring the sensors. If None (default), default
        coloring scheme is used. If 'position', the sensors are divided
        into 8 regions. See ``order`` kwarg of `mne.viz.plot_raw`. If
        array, the channels are divided by picks given in the array. Also
        accepts a list of lists to allow channel groups of the same or
        different sizes.

        ✨ Added in vesion 0.13.0
    #### `to_sphere : bool`
        Whether to project the 3d locations to a sphere. When False, the
        sensor array appears similar as to looking downwards straight above the
        subject's head. Has no effect when ``kind='3d'``. Defaults to True.

        ✨ Added in vesion 0.14.0

    #### `axes : instance of Axes | instance of Axes3D | None`
        Axes to draw the sensors to. If ``kind='3d'``, axes must be an instance
        of Axes3D. If None (default), a new axes will be created.

        ✨ Added in vesion 0.13.0
    #### `block : bool`
        Whether to halt program execution until the figure is closed. Defaults
        to False.

        ✨ Added in vesion 0.13.0
    #### `show : bool`
        Show figure if True. Defaults to True.
    #### `sphere : float | array-like | instance of ConductorModel | None  | 'auto' | 'eeglab'`
        The sphere parameters to use for the head outline. Can be array-like of
        shape (4,) to give the X/Y/Z origin and radius in meters, or a single float
        to give just the radius (origin assumed 0, 0, 0). Can also be an instance
        of a spherical `mne.bem.ConductorModel` to use the origin and
        radius from that object. If ``'auto'`` the sphere is fit to digitization
        points. If ``'eeglab'`` the head circle is defined by EEG electrodes
        ``'Fpz'``, ``'Oz'``, ``'T7'``, and ``'T8'`` (if ``'Fpz'`` is not present,
        it will be approximated from the coordinates of ``'Oz'``). ``None`` (the
        default) is equivalent to ``'auto'`` when enough extra digitization points
        are available, and (0, 0, 0, 0.095) otherwise.

        ✨ Added in vesion 0.20
        🎭 Changed in version 1.1 Added ``'eeglab'`` option.
    #### `pointsize : float | None`
        The size of the points. If None (default), will bet set to ``75`` if
        ``kind='3d'``, or ``25`` otherwise.
    #### `linewidth : float`
        The width of the outline. If ``0``, the outline will not be drawn.
    #### `cmap : str | instance of matplotlib.colors.Colormap | None`
        Colormap for coloring ch_groups. Has effect only when ``ch_groups``
        is list of list. If None, set to ``matplotlib.rcParams["image.cmap"]``.
        Defaults to None.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `fig : instance of Figure`
        Figure containing the sensor topography.
    #### `selection : list`
        A list of selected channels. Only returned if ``kind=='select'``.

    -----
    ### 👉 See Also

    mne.viz.plot_layout

    -----
    ### 📖 Notes

    This function plots the sensor locations from the info structure using
    matplotlib. For drawing the sensors using PyVista see
    `mne.viz.plot_alignment`.

    ✨ Added in vesion 0.12.0
    """
    ...

class DraggableColorbar:
    """## 🧠 Enable interactive colorbar.

    See http://www.ster.kuleuven.be/~pieterd/python/html/plotting/interactive_colorbar.html
    """

    cbar: Incomplete
    mappable: Incomplete
    kind: Incomplete
    ch_type: Incomplete
    fig: Incomplete
    press: Incomplete
    cycle: Incomplete
    index: Incomplete
    lims: Incomplete

    def __init__(self, cbar, mappable, kind, ch_type) -> None: ...
    cidpress: Incomplete
    cidrelease: Incomplete
    cidmotion: Incomplete
    keypress: Incomplete
    scroll: Incomplete

    def connect(self) -> None:
        """## 🧠 Connect to all the events we need."""
        ...
    def on_press(self, event) -> None:
        """## 🧠 Handle button press."""
        ...
    def key_press(self, event) -> None:
        """## 🧠 Handle key press."""
        ...
    def on_motion(self, event) -> None:
        """## 🧠 Handle mouse movements."""
        ...
    def on_release(self, event) -> None:
        """## 🧠 Handle release."""
        ...
    def on_scroll(self, event) -> None:
        """## 🧠 Handle scroll."""
        ...

class SelectFromCollection:
    """## 🧠 Select channels from a matplotlib collection using ``LassoSelector``.

    Selected channels are saved in the ``selection`` attribute. This tool
    highlights selected points by fading other points out (i.e., reducing their
    alpha values).

    -----
    ### 🛠️ Parameters

    #### `ax : instance of Axes`
        Axes to interact with.
    #### `collection : instance of matplotlib collection`
        Collection you want to select from.
    #### `alpha_other : 0 <= float <= 1`
        To highlight a selection, this tool sets all selected points to an
        alpha value of 1 and non-selected points to ``alpha_other``.
        Defaults to 0.3.
    #### `linewidth_other : float`
        Linewidth to use for non-selected sensors. Default is 1.

    -----
    ### 📖 Notes

    This tool selects collection objects based on their `origins`     (i.e., ``offsets``). Calls all callbacks in self.callbacks when selection
    is ready.
    """

    canvas: Incomplete
    collection: Incomplete
    ch_names: Incomplete
    alpha_other: Incomplete
    linewidth_other: Incomplete
    alpha_selected: Incomplete
    linewidth_selected: Incomplete
    xys: Incomplete
    Npts: Incomplete
    fc: Incomplete
    ec: Incomplete
    lw: Incomplete
    lasso: Incomplete
    selection: Incomplete
    callbacks: Incomplete

    def __init__(
        self,
        ax,
        collection,
        ch_names,
        alpha_other: float = 0.5,
        linewidth_other: float = 0.5,
        alpha_selected: int = 1,
        linewidth_selected: int = 1,
    ) -> None: ...
    def on_select(self, verts) -> None:
        """## 🧠 Select a subset from the collection."""
        ...
    def select_one(self, ind) -> None:
        """## 🧠 Select or deselect one sensor."""
        ...
    def notify(self) -> None:
        """## 🧠 Notify listeners that a selection has been made."""
        ...
    def select_many(self, inds) -> None:
        """## 🧠 Select many sensors using indices (for predefined selections)."""
        ...
    def style_sensors(self, inds) -> None:
        """## 🧠 Style selected sensors as "active"."""
        ...
    def disconnect(self) -> None:
        """## 🧠 Disconnect the lasso selector."""
        ...

class DraggableLine:
    """## 🧠 Custom matplotlib line for moving around by drag and drop.

    -----
    ### 🛠️ Parameters

    #### `line : instance of matplotlib Line2D`
        Line to add interactivity to.
    #### `callback : function`
        Callback to call when line is released.
    """

    line: Incomplete
    press: Incomplete
    x0: Incomplete
    modify_callback: Incomplete
    drag_callback: Incomplete
    cidpress: Incomplete
    cidrelease: Incomplete
    cidmotion: Incomplete

    def __init__(self, line, modify_callback, drag_callback) -> None: ...
    def set_x(self, x) -> None:
        """## 🧠 Repoisition the line."""
        ...
    def on_press(self, event) -> None:
        """## 🧠 Store button press if on top of the line."""
        ...
    def on_motion(self, event) -> None:
        """## 🧠 Move the line on drag."""
        ...
    def on_release(self, event) -> None:
        """## 🧠 Handle release."""
        ...
    def remove(self) -> None:
        """## 🧠 Remove the line."""
        ...

def centers_to_edges(*arrays):
    """## 🧠 Convert center points to edges.

    -----
    ### 🛠️ Parameters

    *arrays : list of ndarray
        Each input array should be 1D monotonically increasing,
        and will be cast to float.

    -----
    ### ⏎ Returns

    #### `arrays : list of ndarray`
        Given each input of shape (N,), the output will have shape (N+1,).

    -----
    ### 🖥️ Examples

    >>> x = [0., 0.1, 0.2, 0.3]
    >>> y = [20, 30, 40]
    >>> centers_to_edges(x, y)  # doctest: +SKIP
    [array([-0.05, 0.05, 0.15, 0.25, 0.35]), array([15., 25., 35., 45.])]
    """
    ...

def concatenate_images(
    images,
    axis: int = 0,
    bgcolor: str = "black",
    centered: bool = True,
    n_channels: int = 3,
):
    """## 🧠 Concatenate a list of images.

    -----
    ### 🛠️ Parameters

    #### `images : list of ndarray`
        The list of images to concatenate.
    #### `axis : 0 or 1`
        The images are concatenated horizontally if 0 and vertically otherwise.
        The default orientation is horizontal.
    #### `bgcolor : str | list`
        The color of the background. The name of the color is accepted
        (e.g 'red') or a list of RGB values between 0 and 1. Defaults to
        'black'.
    #### `centered : bool`
        If True, the images are centered. Defaults to True.
    #### `n_channels : int`
        Number of color channels. Can be 3 or 4. The default value is 3.

    -----
    ### ⏎ Returns

    #### `img : ndarray`
        The concatenated image.
    """
    ...
