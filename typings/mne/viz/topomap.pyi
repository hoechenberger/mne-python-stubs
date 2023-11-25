from .._fiff.meas_info import Info as Info
from .._fiff.pick import (
    pick_channels as pick_channels,
    pick_info as pick_info,
    pick_types as pick_types,
)
from ..baseline import rescale as rescale
from ..transforms import (
    apply_trans as apply_trans,
    invert_transform as invert_transform,
)
from ..utils import (
    check_version as check_version,
    fill_doc as fill_doc,
    legacy as legacy,
    logger as logger,
    warn as warn,
)
from .ui_events import (
    TimeChange as TimeChange,
    publish as publish,
    subscribe as subscribe,
)
from .utils import (
    DraggableColorbar as DraggableColorbar,
    figure_nobar as figure_nobar,
    plot_sensors as plot_sensors,
    plt_show as plt_show,
)
from _typeshed import Incomplete

def plot_projs_topomap(
    projs,
    info,
    *,
    sensors: bool = ...,
    show_names: bool = ...,
    contours: int = ...,
    outlines: str = ...,
    sphere=...,
    image_interp=...,
    extrapolate=...,
    border=...,
    res: int = ...,
    size: int = ...,
    cmap=...,
    vlim=...,
    cnorm=...,
    colorbar: bool = ...,
    cbar_fmt: str = ...,
    units=...,
    axes=...,
    show: bool = ...,
):
    """Plot topographic maps of SSP projections.

    Parameters
    ----------
    projs : list of Projection
        The projections.

    info : mne.Info
        The :class:`mne.Info` object with information about the sensors and methods of measurement. Must be associated with the channels in the projectors.

        .. versionchanged:: 0.20
            The positional argument ``layout`` was deprecated and replaced
            by ``info``.

    sensors : bool | str
        Whether to add markers for sensor locations. If :class:`str`, should be a
        valid matplotlib format string (e.g., ``'r+'`` for red plusses, see the
        Notes section of :meth:matplotlib.axes.Axes.plot`). If ``True`` (the
        default), black circles will be used.

    show_names : bool | callable
        If ``True``, show channel names next to each sensor marker. If callable,
        channel names will be formatted using the callable; e.g., to
        delete the prefix 'MEG ' from all channel names, pass the function
        ``lambda x: x.replace('MEG ', '')``. If ``mask`` is not ``None``, only
        non-masked sensor names will be shown.

        .. versionadded:: 1.2

    contours : int | array-like
        The number of contour lines to draw. If ``0``, no contours will be drawn.
        If a positive integer, that number of contour levels are chosen using the
        matplotlib tick locator (may sometimes be inaccurate, use array for
        accuracy). If array-like, the array values are used as the contour levels.
        The values should be in µV for EEG, fT for magnetometers and fT/m for
        gradiometers. If ``colorbar=True``, the colorbar will have ticks
        corresponding to the contour levels. Default is ``6``.

    outlines : 'head' | dict | None
        The outlines to be drawn. If 'head', the default head scheme will be
        drawn. If dict, each key refers to a tuple of x and y positions, the values
        in 'mask_pos' will serve as image mask.
        Alternatively, a matplotlib patch object can be passed for advanced
        masking options, either directly or as a function that returns patches
        (required for multi-axis plots). If None, nothing will be drawn.
        Defaults to 'head'.
    sphere : float | array-like | instance of ConductorModel | None  | 'auto' | 'eeglab'
        The sphere parameters to use for the head outline. Can be array-like of
        shape (4,) to give the X/Y/Z origin and radius in meters, or a single float
        to give just the radius (origin assumed 0, 0, 0). Can also be an instance
        of a spherical :class:mne.bem.ConductorModel` to use the origin and
        radius from that object. If ``'auto'`` the sphere is fit to digitization
        points. If ``'eeglab'`` the head circle is defined by EEG electrodes
        ``'Fpz'``, ``'Oz'``, ``'T7'``, and ``'T8'`` (if ``'Fpz'`` is not present,
        it will be approximated from the coordinates of ``'Oz'``). ``None`` (the
        default) is equivalent to ``'auto'`` when enough extra digitization points
        are available, and (0, 0, 0, 0.095) otherwise.

        .. versionadded:: 0.20
        .. versionchanged:: 1.1 Added ``'eeglab'`` option.

    image_interp : str
        The image interpolation to be used. Options are ``'cubic'`` (default)
        to use :class:`scipy.interpolate.CloughTocher2DInterpolator`,
        ``'nearest'`` to use :class:`scipy.spatial.Voronoi` or
        ``'linear'`` to use :class:`scipy.interpolate.LinearNDInterpolator`.

    extrapolate : str
        Options:

        - ``'box'``
            Extrapolate to four points placed to form a square encompassing all
            data points, where each side of the square is three times the range
            of the data in the respective dimension.
        - ``'local'`` (default for MEG sensors)
            Extrapolate only to nearby points (approximately to points closer than
            median inter-electrode distance). This will also set the
            mask to be polygonal based on the convex hull of the sensors.
        - ``'head'`` (default for non-MEG sensors)
            Extrapolate out to the edges of the clipping circle. This will be on
            the head circle when the sensors are contained within the head circle,
            but it can extend beyond the head when sensors are plotted outside
            the head circle.

        .. versionadded:: 0.20

        .. versionchanged:: 0.21

           - The default was changed to ``'local'`` for MEG sensors.
           - ``'local'`` was changed to use a convex hull mask
           - ``'head'`` was changed to extrapolate out to the clipping circle.

    border : float | 'mean'
        Value to extrapolate to on the topomap borders. If ``'mean'`` (default),
        then each extrapolated point has the average value of its neighbours.

        .. versionadded:: 0.20

    res : int
        The resolution of the topomap image (number of pixels along each side).

    size : float
        Side length of each subplot in inches.

    cmap : matplotlib colormap | (colormap, bool) | 'interactive' | None
        Colormap to use. If :class:`tuple`, the first value indicates the colormap
        to use and the second value is a boolean defining interactivity. In
        interactive mode the colors are adjustable by clicking and dragging the
        colorbar with left and right mouse button. Left mouse button moves the
        scale up and down and right mouse button adjusts the range. Hitting
        space bar resets the range. Up and down arrows can be used to change
        the colormap. If ``None``, ``'Reds'`` is used for data that is either
        all-positive or all-negative, and ``'RdBu_r'`` is used otherwise.
        ``'interactive'`` is equivalent to ``(None, True)``. Defaults to ``None``.

        .. warning::  Interactive mode works smoothly only for a small amount
            of topomaps. Interactive mode is disabled by default for more than
            2 topomaps.

    vlim : tuple of length 2 | 'joint'
        Colormap limits to use. If a :class:`tuple` of floats, specifies the
        lower and upper bounds of the colormap (in that order); providing
        ``None`` for either entry will set the corresponding boundary at the
        min/max of the data (separately for each projector). Elements of the :class:`tuple` may also be callable functions which take in a :class:`NumPy array <numpy.ndarray>` and return a scalar. If ``vlim='joint'``, will compute the colormap limits jointly across all projectors of the same channel type, using the min/max of the data for that channel type. If vlim is ``'joint'``, ``info`` must not be ``None``. Defaults to ``(None, None)``.

    cnorm : matplotlib.colors.Normalize | None
        How to normalize the colormap. If ``None``, standard linear normalization
        is performed. If not ``None``, ``vmin`` and ``vmax`` will be ignored.
        See :ref:`Matplotlib docs <matplotlib:colormapnorms>`
        for more details on colormap normalization, and
        :ref:`the ERDs example<cnorm-example>` for an example of its use.

        .. versionadded:: 1.2

    colorbar : bool
        Plot a colorbar in the rightmost column of the figure.
    cbar_fmt : str
        Formatting string for colorbar tick labels. See :ref:`formatspec` for
        details.

        .. versionadded:: 1.2

    units : str | None
        The units to use for the colorbar label. Ignored if ``colorbar=False``.
        If ``None`` the label will be "AU" indicating arbitrary units.
        Default is ``None``.

        .. versionadded:: 1.2
    axes : instance of Axes | list of Axes | None
        The axes to plot to. If ``None``, a new :class:matplotlib.figure.Figure`
        will be created with the correct number of axes. If :class:matplotlib.axes.Axes` are provided (either as a single instance or a :class:`list` of axes), the number of axes provided must match the number of projectors.Default is ``None``.
    show : bool
        Show the figure if ``True``.

    Returns
    -------
    fig : instance of matplotlib.figure.Figure
        Figure with a topomap subplot for each projector.

    Notes
    -----
    .. versionadded:: 0.9.0
    """

class _GridData:
    """Evaluate the interpolator."""

    n_extra: Incomplete
    mask_pts: Incomplete
    border: Incomplete
    tri: Incomplete
    interp: Incomplete

    def __init__(
        self, pos, image_interp, extrapolate, origin, radii, border
    ) -> None: ...
    interpolator: Incomplete

    def set_values(self, v):
        """Set the values at interpolation points."""
    Xi: Incomplete
    Yi: Incomplete

    def set_locations(self, Xi, Yi):
        """Set locations for easier (delayed) calling."""
    def __call__(self, *args):
        """Evaluate the interpolator."""

def plot_topomap(
    data,
    pos,
    *,
    ch_type: str = ...,
    sensors: bool = ...,
    names=...,
    mask=...,
    mask_params=...,
    contours: int = ...,
    outlines: str = ...,
    sphere=...,
    image_interp=...,
    extrapolate=...,
    border=...,
    res: int = ...,
    size: int = ...,
    cmap=...,
    vlim=...,
    cnorm=...,
    axes=...,
    show: bool = ...,
    onselect=...,
):
    """Plot a topographic map as image.

    Parameters
    ----------
    data : array, shape (n_chan,)
        The data values to plot.
    pos : array, shape (n_channels, 2) | instance of Info
        Location information for the channels. If an array, should provide the x
        and y coordinates for plotting the channels in 2D.
        If an :class:mne.Info` object it must contain only one channel type
        and exactly ``len(data)`` channels; the x/y coordinates will
        be inferred from the montage in the :class:mne.Info` object.
    ch_type : 'mag' | 'grad' | 'planar1' | 'planar2' | 'eeg' | None
        The channel type to plot. For ``'grad'``, the gradiometers are
        collected in pairs and the RMS for each pair is plotted. If
        ``None`` the first available channel type from order shown above is used. Defaults to ``None``.

        .. versionadded:: 0.21

    sensors : bool | str
        Whether to add markers for sensor locations. If :class:`str`, should be a
        valid matplotlib format string (e.g., ``'r+'`` for red plusses, see the
        Notes section of :meth:matplotlib.axes.Axes.plot`). If ``True`` (the
        default), black circles will be used.
    names : None | list
        Labels for the sensors. If a :class:`list`, labels should correspond
        to the order of channels in ``data``. If ``None`` (default), no channel
        names are plotted.

    mask : ndarray of bool, shape (n_channels,) | None
        Array indicating channel(s) to highlight with a distinct
        plotting style. Array elements set to ``True`` will be plotted
        with the parameters given in ``mask_params``. Defaults to ``None``,
        equivalent to an array of all ``False`` elements.

    mask_params : dict | None
        Additional plotting parameters for plotting significant sensors.
        Default (None) equals::

            dict(marker='o', markerfacecolor='w', markeredgecolor='k',
                    linewidth=0, markersize=4)

    contours : int | array-like
        The number of contour lines to draw. If ``0``, no contours will be drawn.
        If a positive integer, that number of contour levels are chosen using the
        matplotlib tick locator (may sometimes be inaccurate, use array for
        accuracy). If array-like, the array values are used as the contour levels.
        The values should be in µV for EEG, fT for magnetometers and fT/m for
        gradiometers. If ``colorbar=True``, the colorbar will have ticks
        corresponding to the contour levels. Default is ``6``.

    outlines : 'head' | dict | None
        The outlines to be drawn. If 'head', the default head scheme will be
        drawn. If dict, each key refers to a tuple of x and y positions, the values
        in 'mask_pos' will serve as image mask.
        Alternatively, a matplotlib patch object can be passed for advanced
        masking options, either directly or as a function that returns patches
        (required for multi-axis plots). If None, nothing will be drawn.
        Defaults to 'head'.
    sphere : float | array-like | instance of ConductorModel | None  | 'auto' | 'eeglab'
        The sphere parameters to use for the head outline. Can be array-like of
        shape (4,) to give the X/Y/Z origin and radius in meters, or a single float
        to give just the radius (origin assumed 0, 0, 0). Can also be an instance
        of a spherical :class:mne.bem.ConductorModel` to use the origin and
        radius from that object. If ``'auto'`` the sphere is fit to digitization
        points. If ``'eeglab'`` the head circle is defined by EEG electrodes
        ``'Fpz'``, ``'Oz'``, ``'T7'``, and ``'T8'`` (if ``'Fpz'`` is not present,
        it will be approximated from the coordinates of ``'Oz'``). ``None`` (the
        default) is equivalent to ``'auto'`` when enough extra digitization points
        are available, and (0, 0, 0, 0.095) otherwise.

        .. versionadded:: 0.20
        .. versionchanged:: 1.1 Added ``'eeglab'`` option.

    image_interp : str
        The image interpolation to be used. Options are ``'cubic'`` (default)
        to use :class:`scipy.interpolate.CloughTocher2DInterpolator`,
        ``'nearest'`` to use :class:`scipy.spatial.Voronoi` or
        ``'linear'`` to use :class:`scipy.interpolate.LinearNDInterpolator`.

    extrapolate : str
        Options:

        - ``'box'``
            Extrapolate to four points placed to form a square encompassing all
            data points, where each side of the square is three times the range
            of the data in the respective dimension.
        - ``'local'`` (default for MEG sensors)
            Extrapolate only to nearby points (approximately to points closer than
            median inter-electrode distance). This will also set the
            mask to be polygonal based on the convex hull of the sensors.
        - ``'head'`` (default for non-MEG sensors)
            Extrapolate out to the edges of the clipping circle. This will be on
            the head circle when the sensors are contained within the head circle,
            but it can extend beyond the head when sensors are plotted outside
            the head circle.

        .. versionadded:: 0.18

        .. versionchanged:: 0.21

           - The default was changed to ``'local'`` for MEG sensors.
           - ``'local'`` was changed to use a convex hull mask
           - ``'head'`` was changed to extrapolate out to the clipping circle.

    border : float | 'mean'
        Value to extrapolate to on the topomap borders. If ``'mean'`` (default),
        then each extrapolated point has the average value of its neighbours.

        .. versionadded:: 0.20

    res : int
        The resolution of the topomap image (number of pixels along each side).

    size : float
        Side length of each subplot in inches.

    cmap : matplotlib colormap | (colormap, bool) | 'interactive' | None
        Colormap to use. If :class:`tuple`, the first value indicates the colormap
        to use and the second value is a boolean defining interactivity. In
        interactive mode the colors are adjustable by clicking and dragging the
        colorbar with left and right mouse button. Left mouse button moves the
        scale up and down and right mouse button adjusts the range. Hitting
        space bar resets the range. Up and down arrows can be used to change
        the colormap. If ``None``, ``'Reds'`` is used for data that is either
        all-positive or all-negative, and ``'RdBu_r'`` is used otherwise.
        ``'interactive'`` is equivalent to ``(None, True)``. Defaults to ``None``.

        .. warning::  Interactive mode works smoothly only for a small amount
            of topomaps. Interactive mode is disabled by default for more than
            2 topomaps.

    vlim : tuple of length 2
        Colormap limits to use. If a :class:`tuple` of floats, specifies the
        lower and upper bounds of the colormap (in that order); providing
        ``None`` for either entry will set the corresponding boundary at the
        min/max of the data. Defaults to ``(None, None)``.

        .. versionadded:: 1.2

    cnorm : matplotlib.colors.Normalize | None
        How to normalize the colormap. If ``None``, standard linear normalization
        is performed. If not ``None``, ``vmin`` and ``vmax`` will be ignored.
        See :ref:`Matplotlib docs <matplotlib:colormapnorms>`
        for more details on colormap normalization, and
        :ref:`the ERDs example<cnorm-example>` for an example of its use.

        .. versionadded:: 0.24
    axes : instance of Axes | None
        The axes to plot to. If ``None``, a new :class:matplotlib.figure.Figure`
        will be created. Default is ``None``.

        .. versionchanged:: 1.2
           If ``axes=None``, a new :class:matplotlib.figure.Figure` is
           created instead of plotting into the current axes.
    show : bool
        Show the figure if ``True``.
    onselect : callable | None
        A function to be called when the user selects a set of channels by
        click-dragging (uses a matplotlib
        :class:matplotlib.widgets.RectangleSelector`). If ``None``
        interactive channel selection is disabled. Defaults to ``None``.

    Returns
    -------
    im : matplotlib.image.AxesImage
        The interpolated data.
    cn : matplotlib.contour.ContourSet
        The fieldlines.
    """

def plot_ica_components(
    ica,
    picks=...,
    ch_type=...,
    *,
    inst=...,
    plot_std: bool = ...,
    reject: str = ...,
    sensors: bool = ...,
    show_names: bool = ...,
    contours: int = ...,
    outlines: str = ...,
    sphere=...,
    image_interp=...,
    extrapolate=...,
    border=...,
    res: int = ...,
    size: int = ...,
    cmap: str = ...,
    vlim=...,
    cnorm=...,
    colorbar: bool = ...,
    cbar_fmt: str = ...,
    axes=...,
    title=...,
    nrows: str = ...,
    ncols: str = ...,
    show: bool = ...,
    image_args=...,
    psd_args=...,
    verbose=...,
):
    """Project mixing matrix on interpolated sensor topography.

    Parameters
    ----------
    ica : instance of mne.preprocessing.ICA
        The ICA solution.

    picks : int | list of int | slice | None
        Indices of the independent components (ICs) to visualize.
        If an integer, represents the index of the IC to pick.
        Multiple ICs can be selected using a list of int or a slice.
        The indices are 0-indexed, so ``picks=1`` will pick the second
        IC: ``ICA001``. ``None`` will pick all independent components in the order
        fitted.
    ch_type : 'mag' | 'grad' | 'planar1' | 'planar2' | 'eeg' | None
        The channel type to plot. For ``'grad'``, the gradiometers are
        collected in pairs and the RMS for each pair is plotted. If
        ``None`` the first available channel type from order shown above is used. Defaults to ``None``.
    inst : Raw | Epochs | None
        To be able to see component properties after clicking on component
        topomap you need to pass relevant data - instances of Raw or Epochs
        (for example the data that ICA was trained on). This takes effect
        only when running matplotlib in interactive mode.
    plot_std : bool | float
        Whether to plot standard deviation in ERP/ERF and spectrum plots.
        Defaults to True, which plots one standard deviation above/below.
        If set to float allows to control how many standard deviations are
        plotted. For example 2.5 will plot 2.5 standard deviation above/below.
    reject : ``'auto'`` | dict | None
        Allows to specify rejection parameters used to drop epochs
        (or segments if continuous signal is passed as inst).
        If None, no rejection is applied. The default is 'auto',
        which applies the rejection parameters used when fitting
        the ICA object.

    sensors : bool | str
        Whether to add markers for sensor locations. If :class:`str`, should be a
        valid matplotlib format string (e.g., ``'r+'`` for red plusses, see the
        Notes section of :meth:matplotlib.axes.Axes.plot`). If ``True`` (the
        default), black circles will be used.

    show_names : bool | callable
        If ``True``, show channel names next to each sensor marker. If callable,
        channel names will be formatted using the callable; e.g., to
        delete the prefix 'MEG ' from all channel names, pass the function
        ``lambda x: x.replace('MEG ', '')``. If ``mask`` is not ``None``, only
        non-masked sensor names will be shown.

    contours : int | array-like
        The number of contour lines to draw. If ``0``, no contours will be drawn.
        If a positive integer, that number of contour levels are chosen using the
        matplotlib tick locator (may sometimes be inaccurate, use array for
        accuracy). If array-like, the array values are used as the contour levels.
        The values should be in µV for EEG, fT for magnetometers and fT/m for
        gradiometers. If ``colorbar=True``, the colorbar will have ticks
        corresponding to the contour levels. Default is ``6``.

    outlines : 'head' | dict | None
        The outlines to be drawn. If 'head', the default head scheme will be
        drawn. If dict, each key refers to a tuple of x and y positions, the values
        in 'mask_pos' will serve as image mask.
        Alternatively, a matplotlib patch object can be passed for advanced
        masking options, either directly or as a function that returns patches
        (required for multi-axis plots). If None, nothing will be drawn.
        Defaults to 'head'.
    sphere : float | array-like | instance of ConductorModel | None  | 'auto' | 'eeglab'
        The sphere parameters to use for the head outline. Can be array-like of
        shape (4,) to give the X/Y/Z origin and radius in meters, or a single float
        to give just the radius (origin assumed 0, 0, 0). Can also be an instance
        of a spherical :class:mne.bem.ConductorModel` to use the origin and
        radius from that object. If ``'auto'`` the sphere is fit to digitization
        points. If ``'eeglab'`` the head circle is defined by EEG electrodes
        ``'Fpz'``, ``'Oz'``, ``'T7'``, and ``'T8'`` (if ``'Fpz'`` is not present,
        it will be approximated from the coordinates of ``'Oz'``). ``None`` (the
        default) is equivalent to ``'auto'`` when enough extra digitization points
        are available, and (0, 0, 0, 0.095) otherwise.

        .. versionadded:: 0.20
        .. versionchanged:: 1.1 Added ``'eeglab'`` option.

    image_interp : str
        The image interpolation to be used. Options are ``'cubic'`` (default)
        to use :class:`scipy.interpolate.CloughTocher2DInterpolator`,
        ``'nearest'`` to use :class:`scipy.spatial.Voronoi` or
        ``'linear'`` to use :class:`scipy.interpolate.LinearNDInterpolator`.

    extrapolate : str
        Options:

        - ``'box'``
            Extrapolate to four points placed to form a square encompassing all
            data points, where each side of the square is three times the range
            of the data in the respective dimension.
        - ``'local'`` (default for MEG sensors)
            Extrapolate only to nearby points (approximately to points closer than
            median inter-electrode distance). This will also set the
            mask to be polygonal based on the convex hull of the sensors.
        - ``'head'`` (default for non-MEG sensors)
            Extrapolate out to the edges of the clipping circle. This will be on
            the head circle when the sensors are contained within the head circle,
            but it can extend beyond the head when sensors are plotted outside
            the head circle.

        .. versionadded:: 1.3

    border : float | 'mean'
        Value to extrapolate to on the topomap borders. If ``'mean'`` (default),
        then each extrapolated point has the average value of its neighbours.

        .. versionadded:: 1.3

    res : int
        The resolution of the topomap image (number of pixels along each side).

    size : float
        Side length of each subplot in inches.

        .. versionadded:: 1.3

    cmap : matplotlib colormap | (colormap, bool) | 'interactive' | None
        Colormap to use. If :class:`tuple`, the first value indicates the colormap
        to use and the second value is a boolean defining interactivity. In
        interactive mode the colors are adjustable by clicking and dragging the
        colorbar with left and right mouse button. Left mouse button moves the
        scale up and down and right mouse button adjusts the range. Hitting
        space bar resets the range. Up and down arrows can be used to change
        the colormap. If ``None``, ``'Reds'`` is used for data that is either
        all-positive or all-negative, and ``'RdBu_r'`` is used otherwise.
        ``'interactive'`` is equivalent to ``(None, True)``. Defaults to ``None``.

        .. warning::  Interactive mode works smoothly only for a small amount
            of topomaps. Interactive mode is disabled by default for more than
            2 topomaps.

    vlim : tuple of length 2
        Colormap limits to use. If a :class:`tuple` of floats, specifies the
        lower and upper bounds of the colormap (in that order); providing
        ``None`` for either entry will set the corresponding boundary at the
        min/max of the data. Defaults to ``(None, None)``.

        .. versionadded:: 1.3

    cnorm : matplotlib.colors.Normalize | None
        How to normalize the colormap. If ``None``, standard linear normalization
        is performed. If not ``None``, ``vmin`` and ``vmax`` will be ignored.
        See :ref:`Matplotlib docs <matplotlib:colormapnorms>`
        for more details on colormap normalization, and
        :ref:`the ERDs example<cnorm-example>` for an example of its use.

        .. versionadded:: 1.3

    colorbar : bool
        Plot a colorbar in the rightmost column of the figure.
    cbar_fmt : str
        Formatting string for colorbar tick labels. See :ref:`formatspec` for
        details.
    axes : Axes | array of Axes | None
        The subplot(s) to plot to. Either a single Axes or an iterable of Axes
        if more than one subplot is needed. The number of subplots must match
        the number of selected components. If None, new figures will be created
        with the number of subplots per figure controlled by ``nrows`` and
        ``ncols``.
    title : str | None
        The title of the generated figure. If ``None`` (default) and
        ``axes=None``, a default title of "ICA Components" will be used.

    nrows, ncols : int | 'auto'
        The number of rows and columns of topographies to plot. If both ``nrows``
        and ``ncols`` are ``'auto'``, will plot up to 20 components in a 5×4 grid,
        and return multiple figures if more than 20 components are requested.
        If one is ``'auto'`` and the other a scalar, a single figure is generated.
        If scalars are provided for both arguments, will plot up to ``nrows*ncols``
        components in a grid and return multiple figures as needed. Default is
        ``nrows='auto', ncols='auto'``.

        .. versionadded:: 1.3
    show : bool
        Show the figure if ``True``.
    image_args : dict | None
        Dictionary of arguments to pass to :func:mne.viz.plot_epochs_image`
        in interactive mode. Ignored if ``inst`` is not supplied. If ``None``,
        nothing is passed. Defaults to ``None``.
    psd_args : dict | None
        Dictionary of arguments to pass to :meth:mne.Epochs.compute_psd` in
        interactive  mode. Ignored if ``inst`` is not supplied. If ``None``,
        nothing is passed. Defaults to ``None``.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    fig : instance of matplotlib.figure.Figure | list of matplotlib.figure.Figure
        The figure object(s).

    Notes
    -----
    When run in interactive mode, ``plot_ica_components`` allows to reject
    components by clicking on their title label. The state of each component
    is indicated by its label color (gray: rejected; black: retained). It is
    also possible to open component properties by clicking on the component
    topomap (this option is only available when the ``inst`` argument is
    supplied).
    """

def plot_tfr_topomap(
    tfr,
    tmin=...,
    tmax=...,
    fmin: float = ...,
    fmax=...,
    *,
    ch_type=...,
    baseline=...,
    mode: str = ...,
    sensors: bool = ...,
    show_names: bool = ...,
    mask=...,
    mask_params=...,
    contours: int = ...,
    outlines: str = ...,
    sphere=...,
    image_interp=...,
    extrapolate=...,
    border=...,
    res: int = ...,
    size: int = ...,
    cmap=...,
    vlim=...,
    cnorm=...,
    colorbar: bool = ...,
    cbar_fmt: str = ...,
    units=...,
    axes=...,
    show: bool = ...,
):
    """Plot topographic maps of specific time-frequency intervals of TFR data.

    Parameters
    ----------
    tfr : AverageTFR
        The AverageTFR object.
    tmin, tmax : float | None
        First and last times to include, in seconds. ``None`` uses the first or
        last time present in the data. Default is ``tmin=None, tmax=None`` (all
        times).
    fmin, fmax : float
        The lower- and upper-bound on frequencies of interest. Default is ``fmin=0, fmax=np.inf`` (spans all frequencies present in the data).
    ch_type : 'mag' | 'grad' | 'planar1' | 'planar2' | 'eeg' | None
        The channel type to plot. For ``'grad'``, the gradiometers are
        collected in pairs and the mean for each pair is plotted. If
        ``None`` the first available channel type from order shown above is used. Defaults to ``None``.
    baseline : tuple or list of length 2
        The time interval to apply rescaling / baseline correction. If None do
        not apply it. If baseline is (a, b) the interval is between "a (s)" and
        "b (s)". If a is None the beginning of the data is used and if b is
        None then b is set to the end of the interval. If baseline is equal to
        (None, None) the whole time interval is used.
    mode : 'mean' | 'ratio' | 'logratio' | 'percent' | 'zscore' | 'zlogratio' | None
        Perform baseline correction by

          - subtracting the mean baseline power ('mean')
          - dividing by the mean baseline power ('ratio')
          - dividing by the mean baseline power and taking the log ('logratio')
          - subtracting the mean baseline power followed by dividing by the
            mean baseline power ('percent')
          - subtracting the mean baseline power and dividing by the standard
            deviation of the baseline power ('zscore')
          - dividing by the mean baseline power, taking the log, and dividing
            by the standard deviation of the baseline power ('zlogratio')

        If None no baseline correction is applied.

    sensors : bool | str
        Whether to add markers for sensor locations. If :class:`str`, should be a
        valid matplotlib format string (e.g., ``'r+'`` for red plusses, see the
        Notes section of :meth:matplotlib.axes.Axes.plot`). If ``True`` (the
        default), black circles will be used.

    show_names : bool | callable
        If ``True``, show channel names next to each sensor marker. If callable,
        channel names will be formatted using the callable; e.g., to
        delete the prefix 'MEG ' from all channel names, pass the function
        ``lambda x: x.replace('MEG ', '')``. If ``mask`` is not ``None``, only
        non-masked sensor names will be shown.

    mask : ndarray of bool, shape (n_channels, n_times) | None
        Array indicating channel-time combinations to highlight with a distinct
        plotting style (useful for, e.g. marking which channels at which times a statistical test of the data reaches significance). Array elements set to ``True`` will be plotted
        with the parameters given in ``mask_params``. Defaults to ``None``,
        equivalent to an array of all ``False`` elements.

    mask_params : dict | None
        Additional plotting parameters for plotting significant sensors.
        Default (None) equals::

            dict(marker='o', markerfacecolor='w', markeredgecolor='k',
                    linewidth=0, markersize=4)

    contours : int | array-like
        The number of contour lines to draw. If ``0``, no contours will be drawn.
        If a positive integer, that number of contour levels are chosen using the
        matplotlib tick locator (may sometimes be inaccurate, use array for
        accuracy). If array-like, the array values are used as the contour levels.
        The values should be in µV for EEG, fT for magnetometers and fT/m for
        gradiometers. If ``colorbar=True``, the colorbar will have ticks
        corresponding to the contour levels. Default is ``6``.

    outlines : 'head' | dict | None
        The outlines to be drawn. If 'head', the default head scheme will be
        drawn. If dict, each key refers to a tuple of x and y positions, the values
        in 'mask_pos' will serve as image mask.
        Alternatively, a matplotlib patch object can be passed for advanced
        masking options, either directly or as a function that returns patches
        (required for multi-axis plots). If None, nothing will be drawn.
        Defaults to 'head'.
    sphere : float | array-like | instance of ConductorModel | None  | 'auto' | 'eeglab'
        The sphere parameters to use for the head outline. Can be array-like of
        shape (4,) to give the X/Y/Z origin and radius in meters, or a single float
        to give just the radius (origin assumed 0, 0, 0). Can also be an instance
        of a spherical :class:mne.bem.ConductorModel` to use the origin and
        radius from that object. If ``'auto'`` the sphere is fit to digitization
        points. If ``'eeglab'`` the head circle is defined by EEG electrodes
        ``'Fpz'``, ``'Oz'``, ``'T7'``, and ``'T8'`` (if ``'Fpz'`` is not present,
        it will be approximated from the coordinates of ``'Oz'``). ``None`` (the
        default) is equivalent to ``'auto'`` when enough extra digitization points
        are available, and (0, 0, 0, 0.095) otherwise.

        .. versionadded:: 0.20
        .. versionchanged:: 1.1 Added ``'eeglab'`` option.

    image_interp : str
        The image interpolation to be used. Options are ``'cubic'`` (default)
        to use :class:`scipy.interpolate.CloughTocher2DInterpolator`,
        ``'nearest'`` to use :class:`scipy.spatial.Voronoi` or
        ``'linear'`` to use :class:`scipy.interpolate.LinearNDInterpolator`.

    extrapolate : str
        Options:

        - ``'box'``
            Extrapolate to four points placed to form a square encompassing all
            data points, where each side of the square is three times the range
            of the data in the respective dimension.
        - ``'local'`` (default for MEG sensors)
            Extrapolate only to nearby points (approximately to points closer than
            median inter-electrode distance). This will also set the
            mask to be polygonal based on the convex hull of the sensors.
        - ``'head'`` (default for non-MEG sensors)
            Extrapolate out to the edges of the clipping circle. This will be on
            the head circle when the sensors are contained within the head circle,
            but it can extend beyond the head when sensors are plotted outside
            the head circle.

        .. versionchanged:: 0.21

           - The default was changed to ``'local'`` for MEG sensors.
           - ``'local'`` was changed to use a convex hull mask
           - ``'head'`` was changed to extrapolate out to the clipping circle.

    border : float | 'mean'
        Value to extrapolate to on the topomap borders. If ``'mean'`` (default),
        then each extrapolated point has the average value of its neighbours.

        .. versionadded:: 0.20

    res : int
        The resolution of the topomap image (number of pixels along each side).

    size : float
        Side length of each subplot in inches.

    cmap : matplotlib colormap | (colormap, bool) | 'interactive' | None
        Colormap to use. If :class:`tuple`, the first value indicates the colormap
        to use and the second value is a boolean defining interactivity. In
        interactive mode the colors are adjustable by clicking and dragging the
        colorbar with left and right mouse button. Left mouse button moves the
        scale up and down and right mouse button adjusts the range. Hitting
        space bar resets the range. Up and down arrows can be used to change
        the colormap. If ``None``, ``'Reds'`` is used for data that is either
        all-positive or all-negative, and ``'RdBu_r'`` is used otherwise.
        ``'interactive'`` is equivalent to ``(None, True)``. Defaults to ``None``.

        .. warning::  Interactive mode works smoothly only for a small amount
            of topomaps. Interactive mode is disabled by default for more than
            2 topomaps.

    vlim : tuple of length 2
        Colormap limits to use. If a :class:`tuple` of floats, specifies the
        lower and upper bounds of the colormap (in that order); providing
        ``None`` for either entry will set the corresponding boundary at the
        min/max of the data. Defaults to ``(None, None)``.

        .. versionadded:: 1.2

    cnorm : matplotlib.colors.Normalize | None
        How to normalize the colormap. If ``None``, standard linear normalization
        is performed. If not ``None``, ``vmin`` and ``vmax`` will be ignored.
        See :ref:`Matplotlib docs <matplotlib:colormapnorms>`
        for more details on colormap normalization, and
        :ref:`the ERDs example<cnorm-example>` for an example of its use.

        .. versionadded:: 1.2

    colorbar : bool
        Plot a colorbar in the rightmost column of the figure.
    cbar_fmt : str
        Formatting string for colorbar tick labels. See :ref:`formatspec` for
        details.

    units : str | None
        The units to use for the colorbar label. Ignored if ``colorbar=False``.
        If ``None`` the label will be "AU" indicating arbitrary units.
        Default is ``None``.
    axes : instance of Axes | None
        The axes to plot to. If ``None``, a new :class:matplotlib.figure.Figure`
        will be created. Default is ``None``.
    show : bool
        Show the figure if ``True``.

    Returns
    -------
    fig : matplotlib.figure.Figure
        The figure containing the topography.
    """

def plot_evoked_topomap(
    evoked,
    times: str = ...,
    *,
    average=...,
    ch_type=...,
    scalings=...,
    proj: bool = ...,
    sensors: bool = ...,
    show_names: bool = ...,
    mask=...,
    mask_params=...,
    contours: int = ...,
    outlines: str = ...,
    sphere=...,
    image_interp=...,
    extrapolate=...,
    border=...,
    res: int = ...,
    size: int = ...,
    cmap=...,
    vlim=...,
    cnorm=...,
    colorbar: bool = ...,
    cbar_fmt: str = ...,
    units=...,
    axes=...,
    time_unit: str = ...,
    time_format=...,
    nrows: int = ...,
    ncols: str = ...,
    show: bool = ...,
):
    """Plot topographic maps of specific time points of evoked data.

    Parameters
    ----------
    evoked : Evoked
        The Evoked object.
    times : float | array of float | "auto" | "peaks" | "interactive"
        The time point(s) to plot. If "auto", the number of ``axes`` determines
        the amount of time point(s). If ``axes`` is also None, at most 10
        topographies will be shown with a regular time spacing between the
        first and last time instant. If "peaks", finds time points
        automatically by checking for local maxima in global field power. If
        "interactive", the time can be set interactively at run-time by using a
        slider.

    average : float | array-like of float, shape (n_times,) | None
        The time window (in seconds) around a given time point to be used for
        averaging. For example, 0.2 would translate into a time window that
        starts 0.1 s before and ends 0.1 s after the given time point. If the
        time window exceeds the duration of the data, it will be clipped.
        Different time windows (one per time point) can be provided by
        passing an ``array-like`` object (e.g., ``[0.1, 0.2, 0.3]``). If
        ``None`` (default), no averaging will take place.

        .. versionchanged:: 1.1
           Support for ``array-like`` input.
    ch_type : 'mag' | 'grad' | 'planar1' | 'planar2' | 'eeg' | None
        The channel type to plot. For ``'grad'``, the gradiometers are
        collected in pairs and the RMS for each pair is plotted. If
        ``None`` the first available channel type from order shown above is used. Defaults to ``None``.

    scalings : dict | float | None
        The scalings of the channel types to be applied for plotting.
        If None, defaults to ``dict(eeg=1e6, grad=1e13, mag=1e15)``.

    proj : bool | 'interactive' | 'reconstruct'
        If true SSP projections are applied before display. If 'interactive',
        a check box for reversible selection of SSP projection vectors will
        be shown. If 'reconstruct', projection vectors will be applied and then
        M/EEG data will be reconstructed via field mapping to reduce the signal
        bias caused by projection.

        .. versionchanged:: 0.21
           Support for 'reconstruct' was added.

    sensors : bool | str
        Whether to add markers for sensor locations. If :class:`str`, should be a
        valid matplotlib format string (e.g., ``'r+'`` for red plusses, see the
        Notes section of :meth:matplotlib.axes.Axes.plot`). If ``True`` (the
        default), black circles will be used.

    show_names : bool | callable
        If ``True``, show channel names next to each sensor marker. If callable,
        channel names will be formatted using the callable; e.g., to
        delete the prefix 'MEG ' from all channel names, pass the function
        ``lambda x: x.replace('MEG ', '')``. If ``mask`` is not ``None``, only
        non-masked sensor names will be shown.

    mask : ndarray of bool, shape (n_channels, n_times) | None
        Array indicating channel-time combinations to highlight with a distinct
        plotting style (useful for, e.g. marking which channels at which times a statistical test of the data reaches significance). Array elements set to ``True`` will be plotted
        with the parameters given in ``mask_params``. Defaults to ``None``,
        equivalent to an array of all ``False`` elements.

    mask_params : dict | None
        Additional plotting parameters for plotting significant sensors.
        Default (None) equals::

            dict(marker='o', markerfacecolor='w', markeredgecolor='k',
                    linewidth=0, markersize=4)

    contours : int | array-like
        The number of contour lines to draw. If ``0``, no contours will be drawn.
        If a positive integer, that number of contour levels are chosen using the
        matplotlib tick locator (may sometimes be inaccurate, use array for
        accuracy). If array-like, the array values are used as the contour levels.
        The values should be in µV for EEG, fT for magnetometers and fT/m for
        gradiometers. If ``colorbar=True``, the colorbar will have ticks
        corresponding to the contour levels. Default is ``6``.

    outlines : 'head' | dict | None
        The outlines to be drawn. If 'head', the default head scheme will be
        drawn. If dict, each key refers to a tuple of x and y positions, the values
        in 'mask_pos' will serve as image mask.
        Alternatively, a matplotlib patch object can be passed for advanced
        masking options, either directly or as a function that returns patches
        (required for multi-axis plots). If None, nothing will be drawn.
        Defaults to 'head'.
    sphere : float | array-like | instance of ConductorModel | None  | 'auto' | 'eeglab'
        The sphere parameters to use for the head outline. Can be array-like of
        shape (4,) to give the X/Y/Z origin and radius in meters, or a single float
        to give just the radius (origin assumed 0, 0, 0). Can also be an instance
        of a spherical :class:mne.bem.ConductorModel` to use the origin and
        radius from that object. If ``'auto'`` the sphere is fit to digitization
        points. If ``'eeglab'`` the head circle is defined by EEG electrodes
        ``'Fpz'``, ``'Oz'``, ``'T7'``, and ``'T8'`` (if ``'Fpz'`` is not present,
        it will be approximated from the coordinates of ``'Oz'``). ``None`` (the
        default) is equivalent to ``'auto'`` when enough extra digitization points
        are available, and (0, 0, 0, 0.095) otherwise.

        .. versionadded:: 0.20
        .. versionchanged:: 1.1 Added ``'eeglab'`` option.

    image_interp : str
        The image interpolation to be used. Options are ``'cubic'`` (default)
        to use :class:`scipy.interpolate.CloughTocher2DInterpolator`,
        ``'nearest'`` to use :class:`scipy.spatial.Voronoi` or
        ``'linear'`` to use :class:`scipy.interpolate.LinearNDInterpolator`.

    extrapolate : str
        Options:

        - ``'box'``
            Extrapolate to four points placed to form a square encompassing all
            data points, where each side of the square is three times the range
            of the data in the respective dimension.
        - ``'local'`` (default for MEG sensors)
            Extrapolate only to nearby points (approximately to points closer than
            median inter-electrode distance). This will also set the
            mask to be polygonal based on the convex hull of the sensors.
        - ``'head'`` (default for non-MEG sensors)
            Extrapolate out to the edges of the clipping circle. This will be on
            the head circle when the sensors are contained within the head circle,
            but it can extend beyond the head when sensors are plotted outside
            the head circle.

        .. versionadded:: 0.18

        .. versionchanged:: 0.21

           - The default was changed to ``'local'`` for MEG sensors.
           - ``'local'`` was changed to use a convex hull mask
           - ``'head'`` was changed to extrapolate out to the clipping circle.

    border : float | 'mean'
        Value to extrapolate to on the topomap borders. If ``'mean'`` (default),
        then each extrapolated point has the average value of its neighbours.

        .. versionadded:: 0.20

    res : int
        The resolution of the topomap image (number of pixels along each side).

    size : float
        Side length of each subplot in inches.

    cmap : matplotlib colormap | (colormap, bool) | 'interactive' | None
        Colormap to use. If :class:`tuple`, the first value indicates the colormap
        to use and the second value is a boolean defining interactivity. In
        interactive mode the colors are adjustable by clicking and dragging the
        colorbar with left and right mouse button. Left mouse button moves the
        scale up and down and right mouse button adjusts the range. Hitting
        space bar resets the range. Up and down arrows can be used to change
        the colormap. If ``None``, ``'Reds'`` is used for data that is either
        all-positive or all-negative, and ``'RdBu_r'`` is used otherwise.
        ``'interactive'`` is equivalent to ``(None, True)``. Defaults to ``None``.

        .. warning::  Interactive mode works smoothly only for a small amount
            of topomaps. Interactive mode is disabled by default for more than
            2 topomaps.

    vlim : tuple of length 2 | 'joint'
        Colormap limits to use. If a :class:`tuple` of floats, specifies the
        lower and upper bounds of the colormap (in that order); providing
        ``None`` for either entry will set the corresponding boundary at the
        min/max of the data (separately for each topomap). Elements of the :class:`tuple` may also be callable functions which take in a :class:`NumPy array <numpy.ndarray>` and return a scalar. If ``vlim='joint'``, will compute the colormap limits jointly across all topomaps of the same channel type, using the min/max of the data for that channel type. Defaults to ``(None, None)``.

        .. versionadded:: 1.2

    cnorm : matplotlib.colors.Normalize | None
        How to normalize the colormap. If ``None``, standard linear normalization
        is performed. If not ``None``, ``vmin`` and ``vmax`` will be ignored.
        See :ref:`Matplotlib docs <matplotlib:colormapnorms>`
        for more details on colormap normalization, and
        :ref:`the ERDs example<cnorm-example>` for an example of its use.

        .. versionadded:: 1.2

    colorbar : bool
        Plot a colorbar in the rightmost column of the figure.
    cbar_fmt : str
        Formatting string for colorbar tick labels. See :ref:`formatspec` for
        details.

    units : dict | str | None
        The units to use for the colorbar label. Ignored if ``colorbar=False``.
        If ``None`` and ``scalings=None`` the unit is automatically determined, otherwise the label will be "AU" indicating arbitrary units.
        Default is ``None``.
    axes : instance of Axes | list of Axes | None
        The axes to plot to. If ``None``, a new :class:matplotlib.figure.Figure`
        will be created with the correct number of axes. If :class:matplotlib.axes.Axes` are provided (either as a single instance or a :class:`list` of axes), the number of axes provided must match the number of ``times`` provided (unless ``times`` is ``None``).Default is ``None``.
    time_unit : str
        The units for the time axis, can be "ms" or "s" (default).

        .. versionadded:: 0.16
    time_format : str | None
        String format for topomap values. Defaults (None) to "%01d ms" if
        ``time_unit='ms'``, "%0.3f s" if ``time_unit='s'``, and
        "%g" otherwise. Can be an empty string to omit the time label.

    nrows, ncols : int | 'auto'
        The number of rows and columns of topographies to plot. If either ``nrows``
        or ``ncols`` is ``'auto'``, the necessary number will be inferred. Defaults
        to ``nrows=1, ncols='auto'``. Ignored when times == 'interactive'.

        .. versionadded:: 0.20
    show : bool
        Show the figure if ``True``.

    Returns
    -------
    fig : instance of matplotlib.figure.Figure
       The figure.

    Notes
    -----
    When existing ``axes`` are provided and ``colorbar=True``, note that the
    colorbar scale will only accurately reflect topomaps that are generated in
    the same call as the colorbar. Note also that the colorbar will not be
    resized automatically when ``axes`` are provided; use Matplotlib's
    :meth:`axes.set_position() <matplotlib.axes.Axes.set_position>` method or
    :ref:`gridspec <matplotlib:arranging_axes>` interface to adjust the colorbar
    size yourself.

    When ``time=="interactive"``, the figure will publish and subscribe to the
    following UI events:

    * :class:mne.viz.ui_events.TimeChange` whenever a new time is selected.
    """

def plot_epochs_psd_topomap(
    epochs,
    bands=...,
    tmin=...,
    tmax=...,
    proj: bool = ...,
    *,
    bandwidth=...,
    adaptive: bool = ...,
    low_bias: bool = ...,
    normalization: str = ...,
    ch_type=...,
    normalize: bool = ...,
    agg_fun=...,
    dB: bool = ...,
    sensors: bool = ...,
    names=...,
    mask=...,
    mask_params=...,
    contours: int = ...,
    outlines: str = ...,
    sphere=...,
    image_interp=...,
    extrapolate=...,
    border=...,
    res: int = ...,
    size: int = ...,
    cmap=...,
    vlim=...,
    cnorm=...,
    colorbar: bool = ...,
    cbar_fmt: str = ...,
    units=...,
    axes=...,
    show: bool = ...,
    n_jobs=...,
    verbose=...,
):
    """.. warning:: LEGACY: New code should use Epochs.compute_psd().plot_topomap().

    Plot the topomap of the power spectral density across epochs.

    Parameters
    ----------
    epochs : instance of Epochs
        The epochs object.

    bands : None | dict | list of tuple
        The frequencies or frequency ranges to plot. If a :class:`dict`, keys will
        be used as subplot titles and values should be either a single frequency
        (e.g., ``{'presentation rate': 6.5}``) or a length-two sequence of lower
        and upper frequency band edges (e.g., ``{'theta': (4, 8)}``). If a single
        frequency is provided, the plot will show the frequency bin that is closest
        to the requested value. If ``None`` (the default), expands to::

            bands = {'Delta (0-4 Hz)': (0, 4), 'Theta (4-8 Hz)': (4, 8),
                     'Alpha (8-12 Hz)': (8, 12), 'Beta (12-30 Hz)': (12, 30),
                     'Gamma (30-45 Hz)': (30, 45)}

        .. note::
           For backwards compatibility, :class:`tuples<tuple>` of length 2 or 3 are
           also accepted, where the last element of the tuple is the subplot title
           and the other entries are frequency values (a single value or band
           edges). New code should use :class:`dict` or ``None``.

        .. versionchanged:: 1.2
           Allow passing a dict and discourage passing tuples.
    tmin, tmax : float | None
        First and last times to include, in seconds. ``None`` uses the first or
        last time present in the data. Default is ``tmin=None, tmax=None`` (all
        times).
    proj : bool
        Whether to apply SSP projection vectors before spectral estimation.
        Default is ``False``.
    bandwidth : float
        The bandwidth of the multi taper windowing function in Hz. The default
        value is a window half-bandwidth of 4 Hz.
    adaptive : bool
        Use adaptive weights to combine the tapered spectra into PSD
        (slow, use n_jobs >> 1 to speed up computation).
    low_bias : bool
        Only use tapers with more than 90% spectral concentration within
        bandwidth.
    normalization : 'full' | 'length'
        Normalization strategy. If "full", the PSD will be normalized by the
        sampling rate as well as the length of the signal (as in
        :ref:`Nitime <nitime:users-guide>`). Default is ``'length'``.
    ch_type : 'mag' | 'grad' | 'planar1' | 'planar2' | 'eeg' | None
        The channel type to plot. For ``'grad'``, the gradiometers are
        collected in pairs and the mean for each pair is plotted. If
        ``None`` the first available channel type from order shown above is used. Defaults to ``None``.

    normalize : bool
        If True, each band will be divided by the total power. Defaults to
        False.

    agg_fun : callable
        The function used to aggregate over frequencies. Defaults to
        :func:`numpy.sum` if ``normalize=True``, else :func:`numpy.mean`.
    dB : bool
        Whether to plot on a decibel-like scale. If ``True``, plots
        10 × log₁₀(spectral power) following the application of ``agg_fun``. Ignored if ``normalize=True``.

    sensors : bool | str
        Whether to add markers for sensor locations. If :class:`str`, should be a
        valid matplotlib format string (e.g., ``'r+'`` for red plusses, see the
        Notes section of :meth:matplotlib.axes.Axes.plot`). If ``True`` (the
        default), black circles will be used.
    names : None | list
        Labels for the sensors. If a :class:`list`, labels should correspond
        to the order of channels in ``data``. If ``None`` (default), no channel
        names are plotted.

    mask : ndarray of bool, shape (n_channels, n_times) | None
        Array indicating channel-time combinations to highlight with a distinct
        plotting style (useful for, e.g. marking which channels at which times a statistical test of the data reaches significance). Array elements set to ``True`` will be plotted
        with the parameters given in ``mask_params``. Defaults to ``None``,
        equivalent to an array of all ``False`` elements.

    mask_params : dict | None
        Additional plotting parameters for plotting significant sensors.
        Default (None) equals::

            dict(marker='o', markerfacecolor='w', markeredgecolor='k',
                    linewidth=0, markersize=4)

    contours : int | array-like
        The number of contour lines to draw. If ``0``, no contours will be drawn.
        If a positive integer, that number of contour levels are chosen using the
        matplotlib tick locator (may sometimes be inaccurate, use array for
        accuracy). If array-like, the array values are used as the contour levels.
        The values should be in µV for EEG, fT for magnetometers and fT/m for
        gradiometers. If ``colorbar=True``, the colorbar will have ticks
        corresponding to the contour levels. Default is ``6``.

    outlines : 'head' | dict | None
        The outlines to be drawn. If 'head', the default head scheme will be
        drawn. If dict, each key refers to a tuple of x and y positions, the values
        in 'mask_pos' will serve as image mask.
        Alternatively, a matplotlib patch object can be passed for advanced
        masking options, either directly or as a function that returns patches
        (required for multi-axis plots). If None, nothing will be drawn.
        Defaults to 'head'.
    sphere : float | array-like | instance of ConductorModel | None  | 'auto' | 'eeglab'
        The sphere parameters to use for the head outline. Can be array-like of
        shape (4,) to give the X/Y/Z origin and radius in meters, or a single float
        to give just the radius (origin assumed 0, 0, 0). Can also be an instance
        of a spherical :class:mne.bem.ConductorModel` to use the origin and
        radius from that object. If ``'auto'`` the sphere is fit to digitization
        points. If ``'eeglab'`` the head circle is defined by EEG electrodes
        ``'Fpz'``, ``'Oz'``, ``'T7'``, and ``'T8'`` (if ``'Fpz'`` is not present,
        it will be approximated from the coordinates of ``'Oz'``). ``None`` (the
        default) is equivalent to ``'auto'`` when enough extra digitization points
        are available, and (0, 0, 0, 0.095) otherwise.

        .. versionadded:: 0.20
        .. versionchanged:: 1.1 Added ``'eeglab'`` option.

    image_interp : str
        The image interpolation to be used. Options are ``'cubic'`` (default)
        to use :class:`scipy.interpolate.CloughTocher2DInterpolator`,
        ``'nearest'`` to use :class:`scipy.spatial.Voronoi` or
        ``'linear'`` to use :class:`scipy.interpolate.LinearNDInterpolator`.

    extrapolate : str
        Options:

        - ``'box'``
            Extrapolate to four points placed to form a square encompassing all
            data points, where each side of the square is three times the range
            of the data in the respective dimension.
        - ``'local'`` (default for MEG sensors)
            Extrapolate only to nearby points (approximately to points closer than
            median inter-electrode distance). This will also set the
            mask to be polygonal based on the convex hull of the sensors.
        - ``'head'`` (default for non-MEG sensors)
            Extrapolate out to the edges of the clipping circle. This will be on
            the head circle when the sensors are contained within the head circle,
            but it can extend beyond the head when sensors are plotted outside
            the head circle.

        .. versionchanged:: 0.21

           - The default was changed to ``'local'`` for MEG sensors.
           - ``'local'`` was changed to use a convex hull mask
           - ``'head'`` was changed to extrapolate out to the clipping circle.

    border : float | 'mean'
        Value to extrapolate to on the topomap borders. If ``'mean'`` (default),
        then each extrapolated point has the average value of its neighbours.

        .. versionadded:: 0.20

    res : int
        The resolution of the topomap image (number of pixels along each side).

    size : float
        Side length of each subplot in inches.

    cmap : matplotlib colormap | (colormap, bool) | 'interactive' | None
        Colormap to use. If :class:`tuple`, the first value indicates the colormap
        to use and the second value is a boolean defining interactivity. In
        interactive mode the colors are adjustable by clicking and dragging the
        colorbar with left and right mouse button. Left mouse button moves the
        scale up and down and right mouse button adjusts the range. Hitting
        space bar resets the range. Up and down arrows can be used to change
        the colormap. If ``None``, ``'Reds'`` is used for data that is either
        all-positive or all-negative, and ``'RdBu_r'`` is used otherwise.
        ``'interactive'`` is equivalent to ``(None, True)``. Defaults to ``None``.

        .. warning::  Interactive mode works smoothly only for a small amount
            of topomaps. Interactive mode is disabled by default for more than
            2 topomaps.

    vlim : tuple of length 2 | 'joint'
        Colormap limits to use. If a :class:`tuple` of floats, specifies the
        lower and upper bounds of the colormap (in that order); providing
        ``None`` for either entry will set the corresponding boundary at the
        min/max of the data (separately for each topomap). Elements of the :class:`tuple` may also be callable functions which take in a :class:`NumPy array <numpy.ndarray>` and return a scalar. If ``vlim='joint'``, will compute the colormap limits jointly across all topomaps of the same channel type, using the min/max of the data for that channel type. Defaults to ``(None, None)``.

        .. versionadded:: 0.21

    cnorm : matplotlib.colors.Normalize | None
        How to normalize the colormap. If ``None``, standard linear normalization
        is performed. If not ``None``, ``vmin`` and ``vmax`` will be ignored.
        See :ref:`Matplotlib docs <matplotlib:colormapnorms>`
        for more details on colormap normalization, and
        :ref:`the ERDs example<cnorm-example>` for an example of its use.

        .. versionadded:: 1.2

    colorbar : bool
        Plot a colorbar in the rightmost column of the figure.
    cbar_fmt : str
        Formatting string for colorbar tick labels. See :ref:`formatspec` for
        details.
        If ``'auto'``, is equivalent to '%0.3f' if ``dB=False`` and '%0.1f' if
        ``dB=True``. Defaults to ``'auto'``.

    units : str | None
        The units to use for the colorbar label. Ignored if ``colorbar=False``.
        If ``None`` the label will be "AU" indicating arbitrary units.
        Default is ``None``.
    axes : instance of Axes | list of Axes | None
        The axes to plot to. If ``None``, a new :class:matplotlib.figure.Figure`
        will be created with the correct number of axes. If :class:matplotlib.axes.Axes` are provided (either as a single instance or a :class:`list` of axes), the number of axes provided must match the length of ``bands``.Default is ``None``.
    show : bool
        Show the figure if ``True``.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the :mod:`joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a :class:`joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    fig : instance of Figure
        Figure showing one scalp topography per frequency band.
    """

def plot_psds_topomap(
    psds,
    freqs,
    pos,
    *,
    bands=...,
    ch_type: str = ...,
    normalize: bool = ...,
    agg_fun=...,
    dB: bool = ...,
    sensors: bool = ...,
    names=...,
    mask=...,
    mask_params=...,
    contours: int = ...,
    outlines: str = ...,
    sphere=...,
    image_interp=...,
    extrapolate=...,
    border=...,
    res: int = ...,
    size: int = ...,
    cmap=...,
    vlim=...,
    cnorm=...,
    colorbar: bool = ...,
    cbar_fmt: str = ...,
    unit=...,
    axes=...,
    show: bool = ...,
):
    """Plot spatial maps of PSDs.

    Parameters
    ----------
    psds : array of float, shape (n_channels, n_freqs)
        Power spectral densities.
    freqs : array of float, shape (n_freqs,)
        Frequencies used to compute psds.
    pos : array, shape (n_channels, 2)
        Location information for the channels. If an array, should provide the x
        and y coordinates for plotting the channels in 2D.

    bands : None | dict | list of tuple
        The frequencies or frequency ranges to plot. If a :class:`dict`, keys will
        be used as subplot titles and values should be either a single frequency
        (e.g., ``{'presentation rate': 6.5}``) or a length-two sequence of lower
        and upper frequency band edges (e.g., ``{'theta': (4, 8)}``). If a single
        frequency is provided, the plot will show the frequency bin that is closest
        to the requested value. If ``None`` (the default), expands to::

            bands = {'Delta (0-4 Hz)': (0, 4), 'Theta (4-8 Hz)': (4, 8),
                     'Alpha (8-12 Hz)': (8, 12), 'Beta (12-30 Hz)': (12, 30),
                     'Gamma (30-45 Hz)': (30, 45)}

        .. note::
           For backwards compatibility, :class:`tuples<tuple>` of length 2 or 3 are
           also accepted, where the last element of the tuple is the subplot title
           and the other entries are frequency values (a single value or band
           edges). New code should use :class:`dict` or ``None``.

        .. versionchanged:: 1.2
           Allow passing a dict and discourage passing tuples.
    ch_type : 'mag' | 'grad' | 'planar1' | 'planar2' | 'eeg' | None
        The channel type to plot. For ``'grad'``, the gradiometers are
        collected in pairs and the RMS for each pair is plotted. If
        ``None`` the first available channel type from order shown above is used. Defaults to ``None``.

    normalize : bool
        If True, each band will be divided by the total power. Defaults to
        False.

    agg_fun : callable
        The function used to aggregate over frequencies. Defaults to
        :func:`numpy.sum` if ``normalize=True``, else :func:`numpy.mean`.
    dB : bool
        Whether to plot on a decibel-like scale. If ``True``, plots
        10 × log₁₀(spectral power) following the application of ``agg_fun``. Ignored if ``normalize=True``.

    sensors : bool | str
        Whether to add markers for sensor locations. If :class:`str`, should be a
        valid matplotlib format string (e.g., ``'r+'`` for red plusses, see the
        Notes section of :meth:matplotlib.axes.Axes.plot`). If ``True`` (the
        default), black circles will be used.
    names : None | list
        Labels for the sensors. If a :class:`list`, labels should correspond
        to the order of channels in ``data``. If ``None`` (default), no channel
        names are plotted.

    mask : ndarray of bool, shape (n_channels, n_times) | None
        Array indicating channel-time combinations to highlight with a distinct
        plotting style (useful for, e.g. marking which channels at which times a statistical test of the data reaches significance). Array elements set to ``True`` will be plotted
        with the parameters given in ``mask_params``. Defaults to ``None``,
        equivalent to an array of all ``False`` elements.

    mask_params : dict | None
        Additional plotting parameters for plotting significant sensors.
        Default (None) equals::

            dict(marker='o', markerfacecolor='w', markeredgecolor='k',
                    linewidth=0, markersize=4)

    contours : int | array-like
        The number of contour lines to draw. If ``0``, no contours will be drawn.
        If a positive integer, that number of contour levels are chosen using the
        matplotlib tick locator (may sometimes be inaccurate, use array for
        accuracy). If array-like, the array values are used as the contour levels.
        The values should be in µV for EEG, fT for magnetometers and fT/m for
        gradiometers. If ``colorbar=True``, the colorbar will have ticks
        corresponding to the contour levels. Default is ``6``.

    outlines : 'head' | dict | None
        The outlines to be drawn. If 'head', the default head scheme will be
        drawn. If dict, each key refers to a tuple of x and y positions, the values
        in 'mask_pos' will serve as image mask.
        Alternatively, a matplotlib patch object can be passed for advanced
        masking options, either directly or as a function that returns patches
        (required for multi-axis plots). If None, nothing will be drawn.
        Defaults to 'head'.
    sphere : float | array-like | instance of ConductorModel | None  | 'auto' | 'eeglab'
        The sphere parameters to use for the head outline. Can be array-like of
        shape (4,) to give the X/Y/Z origin and radius in meters, or a single float
        to give just the radius (origin assumed 0, 0, 0). Can also be an instance
        of a spherical :class:mne.bem.ConductorModel` to use the origin and
        radius from that object. If ``'auto'`` the sphere is fit to digitization
        points. If ``'eeglab'`` the head circle is defined by EEG electrodes
        ``'Fpz'``, ``'Oz'``, ``'T7'``, and ``'T8'`` (if ``'Fpz'`` is not present,
        it will be approximated from the coordinates of ``'Oz'``). ``None`` (the
        default) is equivalent to ``'auto'`` when enough extra digitization points
        are available, and (0, 0, 0, 0.095) otherwise.

        .. versionadded:: 0.20
        .. versionchanged:: 1.1 Added ``'eeglab'`` option.

    image_interp : str
        The image interpolation to be used. Options are ``'cubic'`` (default)
        to use :class:`scipy.interpolate.CloughTocher2DInterpolator`,
        ``'nearest'`` to use :class:`scipy.spatial.Voronoi` or
        ``'linear'`` to use :class:`scipy.interpolate.LinearNDInterpolator`.

    extrapolate : str
        Options:

        - ``'box'``
            Extrapolate to four points placed to form a square encompassing all
            data points, where each side of the square is three times the range
            of the data in the respective dimension.
        - ``'local'`` (default for MEG sensors)
            Extrapolate only to nearby points (approximately to points closer than
            median inter-electrode distance). This will also set the
            mask to be polygonal based on the convex hull of the sensors.
        - ``'head'`` (default for non-MEG sensors)
            Extrapolate out to the edges of the clipping circle. This will be on
            the head circle when the sensors are contained within the head circle,
            but it can extend beyond the head when sensors are plotted outside
            the head circle.

        .. versionchanged:: 0.21

           - The default was changed to ``'local'`` for MEG sensors.
           - ``'local'`` was changed to use a convex hull mask
           - ``'head'`` was changed to extrapolate out to the clipping circle.

    border : float | 'mean'
        Value to extrapolate to on the topomap borders. If ``'mean'`` (default),
        then each extrapolated point has the average value of its neighbours.

        .. versionadded:: 0.20

    res : int
        The resolution of the topomap image (number of pixels along each side).

    size : float
        Side length of each subplot in inches.

    cmap : matplotlib colormap | (colormap, bool) | 'interactive' | None
        Colormap to use. If :class:`tuple`, the first value indicates the colormap
        to use and the second value is a boolean defining interactivity. In
        interactive mode the colors are adjustable by clicking and dragging the
        colorbar with left and right mouse button. Left mouse button moves the
        scale up and down and right mouse button adjusts the range. Hitting
        space bar resets the range. Up and down arrows can be used to change
        the colormap. If ``None``, ``'Reds'`` is used for data that is either
        all-positive or all-negative, and ``'RdBu_r'`` is used otherwise.
        ``'interactive'`` is equivalent to ``(None, True)``. Defaults to ``None``.

        .. warning::  Interactive mode works smoothly only for a small amount
            of topomaps. Interactive mode is disabled by default for more than
            2 topomaps.

    vlim : tuple of length 2 | 'joint'
        Colormap limits to use. If a :class:`tuple` of floats, specifies the
        lower and upper bounds of the colormap (in that order); providing
        ``None`` for either entry will set the corresponding boundary at the
        min/max of the data (separately for each topomap). Elements of the :class:`tuple` may also be callable functions which take in a :class:`NumPy array <numpy.ndarray>` and return a scalar. If ``vlim='joint'``, will compute the colormap limits jointly across all topomaps of the same channel type, using the min/max of the data for that channel type. Defaults to ``(None, None)``.

        .. versionadded:: 0.21

    cnorm : matplotlib.colors.Normalize | None
        How to normalize the colormap. If ``None``, standard linear normalization
        is performed. If not ``None``, ``vmin`` and ``vmax`` will be ignored.
        See :ref:`Matplotlib docs <matplotlib:colormapnorms>`
        for more details on colormap normalization, and
        :ref:`the ERDs example<cnorm-example>` for an example of its use.

        .. versionadded:: 1.2

    colorbar : bool
        Plot a colorbar in the rightmost column of the figure.
    cbar_fmt : str
        Formatting string for colorbar tick labels. See :ref:`formatspec` for
        details.
        If ``'auto'``, is equivalent to '%0.3f' if ``dB=False`` and '%0.1f' if
        ``dB=True``. Defaults to ``'auto'``.
    unit : str | None
        Measurement unit to be displayed with the colorbar. If ``None``, no
        unit is displayed (only "power" or "dB" as appropriate).
    axes : instance of Axes | list of Axes | None
        The axes to plot to. If ``None``, a new :class:matplotlib.figure.Figure`
        will be created with the correct number of axes. If :class:matplotlib.axes.Axes` are provided (either as a single instance or a :class:`list` of axes), the number of axes provided must match the length of ``bands``.Default is ``None``.
    show : bool
        Show the figure if ``True``.

    Returns
    -------
    fig : instance of matplotlib.figure.Figure
        Figure with a topomap subplot for each band.
    """

def plot_layout(layout, picks=..., show_axes: bool = ..., show: bool = ...):
    """Plot the sensor positions.

    Parameters
    ----------
    layout : None | Layout
        Layout instance specifying sensor positions.
    picks : list | slice | None
        Channels to include. Slices and lists of integers will be interpreted as channel indices.
        None (default) will pick all channels. Note that channels in ``info['bads']`` *will be included* if their indices are explicitly provided.
    show_axes : bool
            Show layout axes if True. Defaults to False.
    show : bool
        Show figure if True. Defaults to True.

    Returns
    -------
    fig : instance of Figure
        Figure containing the sensor topography.

    Notes
    -----
    .. versionadded:: 0.12.0
    """

def plot_arrowmap(
    data,
    info_from,
    info_to=...,
    scale: float = ...,
    vlim=...,
    cnorm=...,
    cmap=...,
    sensors: bool = ...,
    res: int = ...,
    axes=...,
    show_names: bool = ...,
    mask=...,
    mask_params=...,
    outlines: str = ...,
    contours: int = ...,
    image_interp=...,
    show: bool = ...,
    onselect=...,
    extrapolate=...,
    sphere=...,
):
    """Plot arrow map.

    Compute arrowmaps, based upon the Hosaka-Cohen transformation
    :footcite:`CohenHosaka1976`, these arrows represents an estimation of the
    current flow underneath the MEG sensors. They are a poor man's MNE.

    Since planar gradiometers takes gradients along latitude and longitude,
    they need to be projected to the flattened manifold span by magnetometer
    or radial gradiometers before taking the gradients in the 2D Cartesian
    coordinate system for visualization on the 2D topoplot. You can use the
    ``info_from`` and ``info_to`` parameters to interpolate from
    gradiometer data to magnetometer data.

    Parameters
    ----------
    data : array, shape (n_channels,)
        The data values to plot.
    info_from : instance of Info
        The measurement info from data to interpolate from.
    info_to : instance of Info | None
        The measurement info to interpolate to. If None, it is assumed
        to be the same as info_from.
    scale : float, default 3e-10
        To scale the arrows.

    vlim : tuple of length 2
        Colormap limits to use. If a :class:`tuple` of floats, specifies the
        lower and upper bounds of the colormap (in that order); providing
        ``None`` for either entry will set the corresponding boundary at the
        min/max of the data. Defaults to ``(None, None)``.

        .. versionadded:: 1.2

    cnorm : matplotlib.colors.Normalize | None
        How to normalize the colormap. If ``None``, standard linear normalization
        is performed. If not ``None``, ``vmin`` and ``vmax`` will be ignored.
        See :ref:`Matplotlib docs <matplotlib:colormapnorms>`
        for more details on colormap normalization, and
        :ref:`the ERDs example<cnorm-example>` for an example of its use.

        .. versionadded:: 1.2

    cmap : matplotlib colormap | None
        Colormap to use. If None, 'Reds' is used for all positive data,
        otherwise defaults to 'RdBu_r'.

    sensors : bool | str
        Whether to add markers for sensor locations. If :class:`str`, should be a
        valid matplotlib format string (e.g., ``'r+'`` for red plusses, see the
        Notes section of :meth:matplotlib.axes.Axes.plot`). If ``True`` (the
        default), black circles will be used.

    res : int
        The resolution of the topomap image (number of pixels along each side).
    axes : instance of Axes | None
        The axes to plot to. If ``None``, a new :class:matplotlib.figure.Figure`
        will be created. Default is ``None``.

    show_names : bool | callable
        If ``True``, show channel names next to each sensor marker. If callable,
        channel names will be formatted using the callable; e.g., to
        delete the prefix 'MEG ' from all channel names, pass the function
        ``lambda x: x.replace('MEG ', '')``. If ``mask`` is not ``None``, only
        non-masked sensor names will be shown.
        If ``True``, a list of names must be provided (see ``names`` keyword).

    mask : ndarray of bool, shape (n_channels,) | None
        Array indicating channel(s) to highlight with a distinct
        plotting style. Array elements set to ``True`` will be plotted
        with the parameters given in ``mask_params``. Defaults to ``None``,
        equivalent to an array of all ``False`` elements.

    mask_params : dict | None
        Additional plotting parameters for plotting significant sensors.
        Default (None) equals::

            dict(marker='o', markerfacecolor='w', markeredgecolor='k',
                    linewidth=0, markersize=4)

    outlines : 'head' | dict | None
        The outlines to be drawn. If 'head', the default head scheme will be
        drawn. If dict, each key refers to a tuple of x and y positions, the values
        in 'mask_pos' will serve as image mask.
        Alternatively, a matplotlib patch object can be passed for advanced
        masking options, either directly or as a function that returns patches
        (required for multi-axis plots). If None, nothing will be drawn.
        Defaults to 'head'.

    contours : int | array-like
        The number of contour lines to draw. If ``0``, no contours will be drawn.
        If a positive integer, that number of contour levels are chosen using the
        matplotlib tick locator (may sometimes be inaccurate, use array for
        accuracy). If array-like, the array values are used as the contour levels.
        The values should be in µV for EEG, fT for magnetometers and fT/m for
        gradiometers. If ``colorbar=True``, the colorbar will have ticks
        corresponding to the contour levels. Default is ``6``.

    image_interp : str
        The image interpolation to be used. Options are ``'cubic'`` (default)
        to use :class:`scipy.interpolate.CloughTocher2DInterpolator`,
        ``'nearest'`` to use :class:`scipy.spatial.Voronoi` or
        ``'linear'`` to use :class:`scipy.interpolate.LinearNDInterpolator`.
    show : bool
        Show the figure if ``True``.
    onselect : callable | None
        Handle for a function that is called when the user selects a set of
        channels by rectangle selection (matplotlib ``RectangleSelector``). If
        None interactive selection is disabled. Defaults to None.

    extrapolate : str
        Options:

        - ``'box'``
            Extrapolate to four points placed to form a square encompassing all
            data points, where each side of the square is three times the range
            of the data in the respective dimension.
        - ``'local'`` (default for MEG sensors)
            Extrapolate only to nearby points (approximately to points closer than
            median inter-electrode distance). This will also set the
            mask to be polygonal based on the convex hull of the sensors.
        - ``'head'`` (default for non-MEG sensors)
            Extrapolate out to the edges of the clipping circle. This will be on
            the head circle when the sensors are contained within the head circle,
            but it can extend beyond the head when sensors are plotted outside
            the head circle.

        .. versionadded:: 0.18

        .. versionchanged:: 0.21

           - The default was changed to ``'local'`` for MEG sensors.
           - ``'local'`` was changed to use a convex hull mask
           - ``'head'`` was changed to extrapolate out to the clipping circle.
    sphere : float | array-like | instance of ConductorModel | None  | 'auto' | 'eeglab'
        The sphere parameters to use for the head outline. Can be array-like of
        shape (4,) to give the X/Y/Z origin and radius in meters, or a single float
        to give just the radius (origin assumed 0, 0, 0). Can also be an instance
        of a spherical :class:mne.bem.ConductorModel` to use the origin and
        radius from that object. If ``'auto'`` the sphere is fit to digitization
        points. If ``'eeglab'`` the head circle is defined by EEG electrodes
        ``'Fpz'``, ``'Oz'``, ``'T7'``, and ``'T8'`` (if ``'Fpz'`` is not present,
        it will be approximated from the coordinates of ``'Oz'``). ``None`` (the
        default) is equivalent to ``'auto'`` when enough extra digitization points
        are available, and (0, 0, 0, 0.095) otherwise.

        .. versionadded:: 0.20
        .. versionchanged:: 1.1 Added ``'eeglab'`` option.

    Returns
    -------
    fig : matplotlib.figure.Figure
        The Figure of the plot.

    Notes
    -----
    .. versionadded:: 0.17

    References
    ----------
    .. footbibliography::
    """

def plot_bridged_electrodes(info, bridged_idx, ed_matrix, title=..., topomap_args=...):
    """Topoplot electrode distance matrix with bridged electrodes connected.

    Parameters
    ----------

    info : mne.Info
        The :class:`mne.Info` object with information about the sensors and methods of measurement.
    bridged_idx : list of tuple
        The indices of channels marked as bridged with each bridged
        pair stored as a tuple.
        Can be generated via
        :func:`mne.preprocessing.compute_bridged_electrodes`.
    ed_matrix : array of float, shape (n_channels, n_channels)
        The electrical distance matrix for each pair of EEG electrodes.
        Can be generated via
        :func:`mne.preprocessing.compute_bridged_electrodes`.
    title : str
        A title to add to the plot.
    topomap_args : dict | None
        Arguments to pass to :func:`mne.viz.plot_topomap`.

    Returns
    -------
    fig : instance of matplotlib.figure.Figure
        The topoplot figure handle.

    See Also
    --------
    mne.preprocessing.compute_bridged_electrodes
    """

def plot_ch_adjacency(info, adjacency, ch_names, kind: str = ..., edit: bool = ...):
    """Plot channel adjacency.

    Parameters
    ----------
    info : instance of Info
        Info object with channel locations.
    adjacency : array
        Array of channels x channels shape. Defines which channels are adjacent
        to each other. Note that if you edit adjacencies
        (via ``edit=True``), this array will be modified in place.
    ch_names : list of str
        Names of successive channels in the ``adjacency`` matrix.
    kind : str
        How to plot the adjacency. Can be either ``'3d'`` or ``'2d'``.
    edit : bool
        Whether to allow interactive editing of the adjacency matrix via
        clicking respective channel pairs. Once clicked, the channel is
        "activated" and turns green. Clicking on another channel adds or
        removes adjacency relation between the activated and newly clicked
        channel (depending on whether the channels are already adjacent or
        not); the newly clicked channel now becomes activated. Clicking on
        an activated channel deactivates it. Editing is currently only
        supported for ``kind='2d'``.

    Returns
    -------
    fig : Figure
        The :class:matplotlib.figure.Figure` instance where the channel
        adjacency is plotted.

    See Also
    --------
    mne.channels.get_builtin_ch_adjacencies
    mne.channels.read_ch_adjacency
    mne.channels.find_ch_adjacency

    Notes
    -----
    .. versionadded:: 1.1
    """

def plot_regression_weights(
    model,
    *,
    ch_type=...,
    sensors: bool = ...,
    show_names: bool = ...,
    mask=...,
    mask_params=...,
    contours: int = ...,
    outlines: str = ...,
    sphere=...,
    image_interp=...,
    extrapolate=...,
    border=...,
    res: int = ...,
    size: int = ...,
    cmap=...,
    vlim=...,
    cnorm=...,
    axes=...,
    colorbar: bool = ...,
    cbar_fmt: str = ...,
    title=...,
    show: bool = ...,
):
    """Plot the regression weights of a fitted EOGRegression model.

    Parameters
    ----------
    model : EOGRegression
        The fitted EOGRegression model whose weights will be plotted.
    ch_type : 'mag' | 'grad' | 'planar1' | 'planar2' | 'eeg' | None
        The channel type to plot. For ``'grad'``, the gradiometers are
        collected in pairs and the RMS for each pair is plotted. If
        ``None`` the first available channel type from order shown above is used. Defaults to ``None``.

    sensors : bool | str
        Whether to add markers for sensor locations. If :class:`str`, should be a
        valid matplotlib format string (e.g., ``'r+'`` for red plusses, see the
        Notes section of :meth:matplotlib.axes.Axes.plot`). If ``True`` (the
        default), black circles will be used.

    show_names : bool | callable
        If ``True``, show channel names next to each sensor marker. If callable,
        channel names will be formatted using the callable; e.g., to
        delete the prefix 'MEG ' from all channel names, pass the function
        ``lambda x: x.replace('MEG ', '')``. If ``mask`` is not ``None``, only
        non-masked sensor names will be shown.

    mask : ndarray of bool, shape (n_channels,) | None
        Array indicating channel(s) to highlight with a distinct
        plotting style. Array elements set to ``True`` will be plotted
        with the parameters given in ``mask_params``. Defaults to ``None``,
        equivalent to an array of all ``False`` elements.

    mask_params : dict | None
        Additional plotting parameters for plotting significant sensors.
        Default (None) equals::

            dict(marker='o', markerfacecolor='w', markeredgecolor='k',
                    linewidth=0, markersize=4)

    contours : int | array-like
        The number of contour lines to draw. If ``0``, no contours will be drawn.
        If a positive integer, that number of contour levels are chosen using the
        matplotlib tick locator (may sometimes be inaccurate, use array for
        accuracy). If array-like, the array values are used as the contour levels.
        The values should be in µV for EEG, fT for magnetometers and fT/m for
        gradiometers. If ``colorbar=True``, the colorbar will have ticks
        corresponding to the contour levels. Default is ``6``.

    outlines : 'head' | dict | None
        The outlines to be drawn. If 'head', the default head scheme will be
        drawn. If dict, each key refers to a tuple of x and y positions, the values
        in 'mask_pos' will serve as image mask.
        Alternatively, a matplotlib patch object can be passed for advanced
        masking options, either directly or as a function that returns patches
        (required for multi-axis plots). If None, nothing will be drawn.
        Defaults to 'head'.
    sphere : float | array-like | instance of ConductorModel | None  | 'auto' | 'eeglab'
        The sphere parameters to use for the head outline. Can be array-like of
        shape (4,) to give the X/Y/Z origin and radius in meters, or a single float
        to give just the radius (origin assumed 0, 0, 0). Can also be an instance
        of a spherical :class:mne.bem.ConductorModel` to use the origin and
        radius from that object. If ``'auto'`` the sphere is fit to digitization
        points. If ``'eeglab'`` the head circle is defined by EEG electrodes
        ``'Fpz'``, ``'Oz'``, ``'T7'``, and ``'T8'`` (if ``'Fpz'`` is not present,
        it will be approximated from the coordinates of ``'Oz'``). ``None`` (the
        default) is equivalent to ``'auto'`` when enough extra digitization points
        are available, and (0, 0, 0, 0.095) otherwise.

        .. versionadded:: 0.20
        .. versionchanged:: 1.1 Added ``'eeglab'`` option.

    image_interp : str
        The image interpolation to be used. Options are ``'cubic'`` (default)
        to use :class:`scipy.interpolate.CloughTocher2DInterpolator`,
        ``'nearest'`` to use :class:`scipy.spatial.Voronoi` or
        ``'linear'`` to use :class:`scipy.interpolate.LinearNDInterpolator`.

    extrapolate : str
        Options:

        - ``'box'``
            Extrapolate to four points placed to form a square encompassing all
            data points, where each side of the square is three times the range
            of the data in the respective dimension.
        - ``'local'`` (default for MEG sensors)
            Extrapolate only to nearby points (approximately to points closer than
            median inter-electrode distance). This will also set the
            mask to be polygonal based on the convex hull of the sensors.
        - ``'head'`` (default for non-MEG sensors)
            Extrapolate out to the edges of the clipping circle. This will be on
            the head circle when the sensors are contained within the head circle,
            but it can extend beyond the head when sensors are plotted outside
            the head circle.

        .. versionchanged:: 0.21

           - The default was changed to ``'local'`` for MEG sensors.
           - ``'local'`` was changed to use a convex hull mask
           - ``'head'`` was changed to extrapolate out to the clipping circle.

    border : float | 'mean'
        Value to extrapolate to on the topomap borders. If ``'mean'`` (default),
        then each extrapolated point has the average value of its neighbours.

        .. versionadded:: 0.20

    res : int
        The resolution of the topomap image (number of pixels along each side).

    size : float
        Side length of each subplot in inches.

    cmap : matplotlib colormap | (colormap, bool) | 'interactive' | None
        Colormap to use. If :class:`tuple`, the first value indicates the colormap
        to use and the second value is a boolean defining interactivity. In
        interactive mode the colors are adjustable by clicking and dragging the
        colorbar with left and right mouse button. Left mouse button moves the
        scale up and down and right mouse button adjusts the range. Hitting
        space bar resets the range. Up and down arrows can be used to change
        the colormap. If ``None``, ``'Reds'`` is used for data that is either
        all-positive or all-negative, and ``'RdBu_r'`` is used otherwise.
        ``'interactive'`` is equivalent to ``(None, True)``. Defaults to ``None``.

        .. warning::  Interactive mode works smoothly only for a small amount
            of topomaps. Interactive mode is disabled by default for more than
            2 topomaps.

    vlim : tuple of length 2
        Colormap limits to use. If a :class:`tuple` of floats, specifies the
        lower and upper bounds of the colormap (in that order); providing
        ``None`` for either entry will set the corresponding boundary at the
        min/max of the data. Defaults to ``(None, None)``.

    cnorm : matplotlib.colors.Normalize | None
        How to normalize the colormap. If ``None``, standard linear normalization
        is performed. If not ``None``, ``vmin`` and ``vmax`` will be ignored.
        See :ref:`Matplotlib docs <matplotlib:colormapnorms>`
        for more details on colormap normalization, and
        :ref:`the ERDs example<cnorm-example>` for an example of its use.
    axes : instance of Axes | list of Axes | None
        The axes to plot to. If ``None``, a new :class:matplotlib.figure.Figure`
        will be created with the correct number of axes. If :class:matplotlib.axes.Axes` are provided (either as a single instance or a :class:`list` of axes), the number of axes provided must match the number of ``times`` provided (unless ``times`` is ``None``).Default is ``None``.

    colorbar : bool
        Plot a colorbar in the rightmost column of the figure.
    cbar_fmt : str
        Formatting string for colorbar tick labels. See :ref:`formatspec` for
        details.

    title : str | None
        The title of the generated figure. If ``None`` (default), no title is
        displayed.
    show : bool
        Show the figure if ``True``.

    Returns
    -------
    fig : instance of matplotlib.figure.Figure
        Figure with a topomap subplot for each channel type.

    Notes
    -----
    .. versionadded:: 1.2
    """
