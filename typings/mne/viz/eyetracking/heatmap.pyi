from ...utils import fill_doc as fill_doc, logger as logger
from ..utils import plt_show as plt_show
from _typeshed import Incomplete

def plot_gaze(epochs, width, height, *, sigma: int=..., cmap: Incomplete | None=..., alpha: float=..., vlim=..., axes: Incomplete | None=..., show: bool=...):
    """Plot a heatmap of eyetracking gaze data.

    Parameters
    ----------
    epochs : instance of Epochs
        The :class:`~mne.Epochs` object containing eyegaze channels.
    width : int
        The width dimension of the plot canvas. For example, if the eyegaze data units
        are pixels, and the participant screen resolution was 1920x1080, then the width
        should be 1920.
    height : int
        The height dimension of the plot canvas. For example, if the eyegaze data units
        are pixels, and the participant screen resolution was 1920x1080, then the height
        should be 1080.
    sigma : float | None
        The amount of Gaussian smoothing applied to the heatmap data (standard
        deviation in pixels). If ``None``, no smoothing is applied. Default is 25.
    
    cmap : matplotlib colormap | str | None
            The :class:`~matplotlib.colors.Colormap` to use. Defaults to ``None``, which
            will use the matplotlib default colormap.
    alpha : float
        The opacity of the heatmap (default is 1).
    
    vlim : tuple of length 2
        Colormap limits to use. If a :class:`tuple` of floats, specifies the
        lower and upper bounds of the colormap (in that order); providing
        ``None`` for either entry will set the corresponding boundary at the
        min/max of the data. Defaults to ``(None, None)``.
    axes : instance of Axes | None
        The axes to plot to. If ``None``, a new :class:`~matplotlib.figure.Figure`
        will be created. Default is ``None``.
    show : bool
        Show the figure if ``True``.

    Returns
    -------
    fig : instance of Figure
        The resulting figure object for the heatmap plot.

    Notes
    -----
    .. versionadded:: 1.6
    """