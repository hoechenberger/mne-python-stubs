from .._fiff.pick import channel_type as channel_type, pick_types as pick_types
from ..utils import Bunch as Bunch, fill_doc as fill_doc
from .utils import DraggableColorbar as DraggableColorbar, add_background_image as add_background_image, plt_show as plt_show
from _typeshed import Incomplete

def iter_topography(info, layout: Incomplete | None=..., on_pick: Incomplete | None=..., fig: Incomplete | None=..., fig_facecolor: str=..., axis_facecolor: str=..., axis_spinecolor: str=..., layout_scale: Incomplete | None=..., legend: bool=...):
    """Create iterator over channel positions.

    This function returns a generator that unpacks into
    a series of matplotlib axis objects and data / channel
    indices, both corresponding to the sensor positions
    of the related layout passed or inferred from the channel info.
    Hence, this enables convenient topography plot customization.

    Parameters
    ----------
    
    info : mne.Info
        The :class:`mne.Info` object with information about the sensors and methods of measurement.
    layout : instance of mne.channels.Layout | None
        The layout to use. If None, layout will be guessed.
    on_pick : callable | None
        The callback function to be invoked on clicking one
        of the axes. Is supposed to instantiate the following
        API: ``function(axis, channel_index)``.
    fig : matplotlib.figure.Figure | None
        The figure object to be considered. If None, a new
        figure will be created.
    fig_facecolor : color
        The figure face color. Defaults to black.
    axis_facecolor : color
        The axis face color. Defaults to black.
    axis_spinecolor : color
        The axis spine color. Defaults to black. In other words,
        the color of the axis' edge lines.
    layout_scale : float | None
        Scaling factor for adjusting the relative size of the layout
        on the canvas. If None, nothing will be scaled.
    legend : bool
        If True, an additional axis is created in the bottom right corner
        that can be used to, e.g., construct a legend. The index of this
        axis will be -1.

    Returns
    -------
    gen : generator
        A generator that can be unpacked into:

        ax : matplotlib.axis.Axis
            The current axis of the topo plot.
        ch_dx : int
            The related channel index.
    """

def plot_topo_image_epochs(epochs, layout: Incomplete | None=..., sigma: float=..., vmin: Incomplete | None=..., vmax: Incomplete | None=..., colorbar: Incomplete | None=..., order: Incomplete | None=..., cmap: str=..., layout_scale: float=..., title: Incomplete | None=..., scalings: Incomplete | None=..., border: str=..., fig_facecolor: str=..., fig_background: Incomplete | None=..., font_color: str=..., show: bool=...):
    """Plot Event Related Potential / Fields image on topographies.

    Parameters
    ----------
    epochs : instance of :class:`~mne.Epochs`
        The epochs.
    layout : instance of Layout
        System specific sensor positions.
    sigma : float
        The standard deviation of the Gaussian smoothing to apply along
        the epoch axis to apply in the image. If 0., no smoothing is applied.
    vmin : float
        The min value in the image. The unit is µV for EEG channels,
        fT for magnetometers and fT/cm for gradiometers.
    vmax : float
        The max value in the image. The unit is µV for EEG channels,
        fT for magnetometers and fT/cm for gradiometers.
    colorbar : bool | None
        Whether to display a colorbar or not. If ``None`` a colorbar will be
        shown only if all channels are of the same type. Defaults to ``None``.
    order : None | array of int | callable
        If not None, order is used to reorder the epochs on the y-axis
        of the image. If it's an array of int it should be of length
        the number of good epochs. If it's a callable the arguments
        passed are the times vector and the data as 2d array
        (data.shape[1] == len(times)).
    cmap : colormap
        Colors to be mapped to the values.
    layout_scale : float
        Scaling factor for adjusting the relative size of the layout
        on the canvas.
    title : str
        Title of the figure.
    scalings : dict | None
        The scalings of the channel types to be applied for plotting. If
        ``None``, defaults to ``dict(eeg=1e6, grad=1e13, mag=1e15)``.
    border : str
        Matplotlib borders style to be used for each sensor plot.
    fig_facecolor : color
        The figure face color. Defaults to black.
    fig_background : None | array
        A background image for the figure. This must be a valid input to
        :func:`matplotlib.pyplot.imshow`. Defaults to ``None``.
    font_color : color
        The color of tick labels in the colorbar. Defaults to white.
    show : bool
        Whether to show the figure. Defaults to ``True``.

    Returns
    -------
    fig : instance of :class:`matplotlib.figure.Figure`
        Figure distributing one image per channel across sensor topography.

    Notes
    -----
    In an interactive Python session, this plot will be interactive; clicking
    on a channel image will pop open a larger view of the image; this image
    will always have a colorbar even when the topo plot does not (because it
    shows multiple sensor types).
    """