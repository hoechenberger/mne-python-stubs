from .._fiff.pick import (
    channel_indices_by_type as channel_indices_by_type,
    channel_type as channel_type,
    pick_info as pick_info,
)
from ..utils import fill_doc as fill_doc, logger as logger, warn as warn
from .topomap import plot_topomap as plot_topomap
from .utils import DraggableColorbar as DraggableColorbar, plt_show as plt_show

def plot_evoked(
    evoked,
    picks=None,
    exclude: str = "bads",
    unit: bool = True,
    show: bool = True,
    ylim=None,
    xlim: str = "tight",
    proj: bool = False,
    hline=None,
    units=None,
    scalings=None,
    titles=None,
    axes=None,
    gfp: bool = False,
    window_title=None,
    spatial_colors: bool = False,
    zorder: str = "unsorted",
    selectable: bool = True,
    noise_cov=None,
    time_unit: str = "s",
    sphere=None,
    *,
    highlight=None,
    verbose=None,
):
    """Plot evoked data using butterfly plots.

    Left click to a line shows the channel name. Selecting an area by clicking
    and holding left mouse button plots a topographic map of the painted area.

    💡 Note If bad channels are not excluded they are shown in red.

    Parameters
    ----------
    evoked : instance of Evoked
        The evoked data.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick all channels. Note that channels in
        ``info['bads']`` *will be included* if their names or indices are
        explicitly provided.
    exclude : list of str | 'bads'
        Channels names to exclude from being shown. If 'bads', the
        bad channels are excluded.
    unit : bool
        Scale plot with channel (SI) unit.
    show : bool
        Show figure if True.
    ylim : dict | None
        Y limits for plots (after scaling has been applied). e.g.
        ylim = dict(eeg=[-20, 20])
        Valid keys are eeg, mag, grad, misc. If None, the ylim parameter
        for each channel equals the pyplot default.
    xlim : 'tight' | tuple | None
        X limits for plots.

    proj : bool | 'interactive' | 'reconstruct'
        If true SSP projections are applied before display. If 'interactive',
        a check box for reversible selection of SSP projection vectors will
        be shown. If 'reconstruct', projection vectors will be applied and then
        M/EEG data will be reconstructed via field mapping to reduce the signal
        bias caused by projection.

        🎭 Changed in version 0.21
           Support for 'reconstruct' was added.
    hline : list of float | None
        The values at which to show an horizontal line.
    units : dict | None
        The units of the channel types used for axes labels. If None,
        defaults to ``dict(eeg='µV', grad='fT/cm', mag='fT')``.
    scalings : dict | None
        The scalings of the channel types to be applied for plotting. If None,
        defaults to ``dict(eeg=1e6, grad=1e13, mag=1e15)``.
    titles : dict | None
        The titles associated with the channels. If None, defaults to
        ``dict(eeg='EEG', grad='Gradiometers', mag='Magnetometers')``.
    axes : instance of Axes | list | None
        The axes to plot to. If list, the list must be a list of Axes of
        the same length as the number of channel types. If instance of
        Axes, there must be only one channel type plotted.
    gfp : bool | 'only'
        Plot the global field power (GFP) or the root mean square (RMS) of the
        data. For MEG data, this will plot the RMS. For EEG, it plots GFP,
        i.e. the standard deviation of the signal across channels. The GFP is
        equivalent to the RMS of an average-referenced signal.

        - ``True``
            Plot GFP or RMS (for EEG and MEG, respectively) and traces for all
            channels.
        - ``'only'``
            Plot GFP or RMS (for EEG and MEG, respectively), and omit the
            traces for individual channels.

        The color of the GFP/RMS trace will be green if
        ``spatial_colors=False``, and black otherwise.

        🎭 Changed in version 0.23
           Plot GFP for EEG instead of RMS. Label RMS traces correctly as such.
    window_title : str | None
        The title to put at the top of the figure.
    spatial_colors : bool | 'auto'
        If True, the lines are color coded by mapping physical sensor
        coordinates into color values. Spatially similar channels will have
        similar colors. Bad channels will be dotted. If False, the good
        channels are plotted black and bad channels red. If ``'auto'``, uses
        True if channel locations are present, and False if channel locations
        are missing or if the data contains only a single channel. Defaults to
        ``'auto'``.
    zorder : str | callable
        Which channels to put in the front or back. Only matters if
        ``spatial_colors`` is used.
        If str, must be ``std`` or ``unsorted`` (defaults to ``unsorted``). If
        ``std``, data with the lowest standard deviation (weakest effects) will
        be put in front so that they are not obscured by those with stronger
        effects. If ``unsorted``, channels are z-sorted as in the evoked
        instance.
        If callable, must take one argument: a numpy array of the same
        dimensionality as the evoked raw data; and return a list of
        unique integers corresponding to the number of channels.

        ✨ Added in version 0.13.0

    selectable : bool
        Whether to use interactive features. If True (default), it is possible
        to paint an area to draw topomaps. When False, the interactive features
        are disabled. Disabling interactive features reduces memory consumption
        and is useful when using ``axes`` parameter to draw multiaxes figures.

        ✨ Added in version 0.13.0

    noise_cov : instance of Covariance | str | None
        Noise covariance used to whiten the data while plotting.
        Whitened data channel names are shown in italic.
        Can be a string to load a covariance from disk.
        See also `mne.Evoked.plot_white` for additional inspection
        of noise covariance properties when whitening evoked data.
        For data processed with SSS, the effective dependence between
        magnetometers and gradiometers may introduce differences in scaling,
        consider using `mne.Evoked.plot_white`.

        ✨ Added in version 0.16.0
    time_unit : str
        The units for the time axis, can be "s" (default) or "ms".

        ✨ Added in version 0.16
    sphere : float | array-like | instance of ConductorModel | None  | 'auto' | 'eeglab'
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

        ✨ Added in version 0.20
        🎭 Changed in version 1.1 Added ``'eeglab'`` option.
    highlight : array-like of float, shape(2,) | array-like of float, shape (n, 2) | None
        Segments of the data to highlight by means of a light-yellow
        background color. Can be used to put visual emphasis on certain
        time periods. The time periods must be specified as ``array-like``
        objects in the form of ``(t_start, t_end)`` in the unit given by the
        ``time_unit`` parameter.
        Multiple time periods can be specified by passing an ``array-like``
        object of individual time periods (e.g., for 3 time periods, the shape
        of the passed object would be ``(3, 2)``. If ``None``, no highlighting
        is applied.

        ✨ Added in version 1.1

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    fig : instance of matplotlib.figure.Figure
        Figure containing the butterfly plots.

    See Also
    --------
    mne.viz.plot_evoked_white
    """
    ...

def plot_evoked_topo(
    evoked,
    layout=None,
    layout_scale: float = 0.945,
    color=None,
    border: str = "none",
    ylim=None,
    scalings=None,
    title=None,
    proj: bool = False,
    vline=[0.0],
    fig_background=None,
    merge_grads: bool = False,
    legend: bool = True,
    axes=None,
    background_color: str = "w",
    noise_cov=None,
    exclude: str = "bads",
    show: bool = True,
):
    """Plot 2D topography of evoked responses.

    Clicking on the plot of an individual sensor opens a new figure showing
    the evoked response for the selected sensor.

    Parameters
    ----------
    evoked : list of Evoked | Evoked
        The evoked response to plot.
    layout : instance of Layout | None
        Layout instance specifying sensor positions (does not need to
        be specified for Neuromag data). If possible, the correct layout is
        inferred from the data.
    layout_scale : float
        Scaling factor for adjusting the relative size of the layout
        on the canvas.
    color : list of color | color | None
        Everything matplotlib accepts to specify colors. If not list-like,
        the color specified will be repeated. If None, colors are
        automatically drawn.
    border : str
        Matplotlib borders style to be used for each sensor plot.
    ylim : dict | None
        Y limits for plots (after scaling has been applied). The value
        determines the upper and lower subplot limits. e.g.
        ylim = dict(eeg=[-20, 20]). Valid keys are eeg, mag, grad, misc.
        If None, the ylim parameter for each channel type is determined by
        the minimum and maximum peak.
    scalings : dict | None
        The scalings of the channel types to be applied for plotting. If None,`
        defaults to ``dict(eeg=1e6, grad=1e13, mag=1e15)``.
    title : str
        Title of the figure.
    proj : bool | 'interactive'
        If true SSP projections are applied before display. If 'interactive',
        a check box for reversible selection of SSP projection vectors will
        be shown.
    vline : list of float | None
        The values at which to show a vertical line.
    fig_background : None | ndarray
        A background image for the figure. This must work with a call to
        plt.imshow. Defaults to None.
    merge_grads : bool
        Whether to use RMS value of gradiometer pairs. Only works for Neuromag
        data. Defaults to False.
    legend : bool | int | str | tuple
        If True, create a legend based on evoked.comment. If False, disable the
        legend. Otherwise, the legend is created and the parameter value is
        passed as the location parameter to the matplotlib legend call. It can
        be an integer (e.g. 0 corresponds to upper right corner of the plot),
        a string (e.g. 'upper right'), or a tuple (x, y coordinates of the
        lower left corner of the legend in the axes coordinate system).
        See matplotlib documentation for more details.
    axes : instance of matplotlib Axes | None
        Axes to plot into. If None, axes will be created.
    background_color : color
        Background color. Typically 'k' (black) or 'w' (white; default).

        ✨ Added in version 0.15.0
    noise_cov : instance of Covariance | str | None
        Noise covariance used to whiten the data while plotting.
        Whitened data channel names are shown in italic.
        Can be a string to load a covariance from disk.

        ✨ Added in version 0.16.0
    exclude : list of str | 'bads'
        Channels names to exclude from the plot. If 'bads', the
        bad channels are excluded. By default, exclude is set to 'bads'.
    show : bool
        Show figure if True.

    Returns
    -------
    fig : instance of matplotlib.figure.Figure
        Images of evoked responses at sensor locations.
    """
    ...

def plot_evoked_image(
    evoked,
    picks=None,
    exclude: str = "bads",
    unit: bool = True,
    show: bool = True,
    clim=None,
    xlim: str = "tight",
    proj: bool = False,
    units=None,
    scalings=None,
    titles=None,
    axes=None,
    cmap: str = "RdBu_r",
    colorbar: bool = True,
    mask=None,
    mask_style=None,
    mask_cmap: str = "Greys",
    mask_alpha: float = 0.25,
    time_unit: str = "s",
    show_names: str = "auto",
    group_by=None,
    sphere=None,
):
    """Plot evoked data as images.

    Parameters
    ----------
    evoked : instance of Evoked
        The evoked data.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick all channels. Note that channels in
        ``info['bads']`` *will be included* if their names or indices are
        explicitly provided.
        This parameter can also be used to set the order the channels
        are shown in, as the channel image is sorted by the order of picks.
    exclude : list of str | 'bads'
        Channels names to exclude from being shown. If 'bads', the
        bad channels are excluded.
    unit : bool
        Scale plot with channel (SI) unit.
    show : bool
        Show figure if True.
    clim : dict | None
        Color limits for plots (after scaling has been applied). e.g.
        ``clim = dict(eeg=[-20, 20])``.
        Valid keys are eeg, mag, grad, misc. If None, the clim parameter
        for each channel equals the pyplot default.
    xlim : 'tight' | tuple | None
        X limits for plots.
    proj : bool | 'interactive'
        If true SSP projections are applied before display. If 'interactive',
        a check box for reversible selection of SSP projection vectors will
        be shown.
    units : dict | None
        The units of the channel types used for axes labels. If None,
        defaults to ``dict(eeg='µV', grad='fT/cm', mag='fT')``.
    scalings : dict | None
        The scalings of the channel types to be applied for plotting. If None,`
        defaults to ``dict(eeg=1e6, grad=1e13, mag=1e15)``.
    titles : dict | None
        The titles associated with the channels. If None, defaults to
        ``dict(eeg='EEG', grad='Gradiometers', mag='Magnetometers')``.
    axes : instance of Axes | list | dict | None
        The axes to plot to. If list, the list must be a list of Axes of
        the same length as the number of channel types. If instance of
        Axes, there must be only one channel type plotted.
        If ``group_by`` is a dict, this cannot be a list, but it can be a dict
        of lists of axes, with the keys matching those of ``group_by``. In that
        case, the provided axes will be used for the corresponding groups.
        Defaults to ``None``.
    cmap : matplotlib colormap | (colormap, bool) | 'interactive'
        Colormap. If tuple, the first value indicates the colormap to use and
        the second value is a boolean defining interactivity. In interactive
        mode the colors are adjustable by clicking and dragging the colorbar
        with left and right mouse button. Left mouse button moves the scale up
        and down and right mouse button adjusts the range. Hitting space bar
        resets the scale. Up and down arrows can be used to change the
        colormap. If 'interactive', translates to ``('RdBu_r', True)``.
        Defaults to ``'RdBu_r'``.
    colorbar : bool
        If True, plot a colorbar. Defaults to True.

        ✨ Added in version 0.16
    mask : ndarray | None
        An array of booleans of the same shape as the data. Entries of the
        data that correspond to ``False`` in the mask are masked (see
        ``do_mask`` below). Useful for, e.g., masking for statistical
        significance.

        ✨ Added in version 0.16
    mask_style : None | 'both' | 'contour' | 'mask'
        If ``mask`` is not None: if 'contour', a contour line is drawn around
        the masked areas (``True`` in ``mask``). If 'mask', entries not
        ``True`` in ``mask`` are shown transparently. If 'both', both a contour
        and transparency are used.
        If ``None``, defaults to 'both' if ``mask`` is not None, and is ignored
        otherwise.

         ✨ Added in version 0.16
    mask_cmap : matplotlib colormap | (colormap, bool) | 'interactive'
        The colormap chosen for masked parts of the image (see below), if
        ``mask`` is not ``None``. If None, ``cmap`` is reused. Defaults to
        ``Greys``. Not interactive. Otherwise, as ``cmap``.
    mask_alpha : float
        A float between 0 and 1. If ``mask`` is not None, this sets the
        alpha level (degree of transparency) for the masked-out segments.
        I.e., if 0, masked-out segments are not visible at all.
        Defaults to .25.

        ✨ Added in version 0.16
    time_unit : str
        The units for the time axis, can be "ms" or "s" (default).

        ✨ Added in version 0.16
    show_names : bool | 'auto' | 'all'
        Determines if channel names should be plotted on the y axis. If False,
        no names are shown. If True, ticks are set automatically by matplotlib
        and the corresponding channel names are shown. If "all", all channel
        names are shown. If "auto", is set to False if ``picks`` is ``None``,
        to ``True`` if ``picks`` contains 25 or more entries, or to "all"
        if ``picks`` contains fewer than 25 entries.
    group_by : None | dict
        If a dict, the values must be picks, and ``axes`` must also be a dict
        with matching keys, or None. If ``axes`` is None, one figure and one
        axis will be created for each entry in ``group_by``.Then, for each
        entry, the picked channels will be plotted to the corresponding axis.
        If ``titles`` are None, keys will become plot titles. This is useful
        for e.g. ROIs. Each entry must contain only one channel type.
        For example::

            group_by=dict(Left_ROI=[1, 2, 3, 4], Right_ROI=[5, 6, 7, 8])

        If None, all picked channels are plotted to the same axis.
    sphere : float | array-like | instance of ConductorModel | None  | 'auto' | 'eeglab'
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

        ✨ Added in version 0.20
        🎭 Changed in version 1.1 Added ``'eeglab'`` option.

    Returns
    -------
    fig : instance of matplotlib.figure.Figure
        Figure containing the images.
    """
    ...

def plot_evoked_white(
    evoked,
    noise_cov,
    show: bool = True,
    rank=None,
    time_unit: str = "s",
    sphere=None,
    axes=None,
    verbose=None,
):
    """Plot whitened evoked response.

    Plots the whitened evoked response and the whitened GFP as described in
    :footcite:`EngemannGramfort2015`. This function is especially useful for
    investigating noise covariance properties to determine if data are
    properly whitened (e.g., achieving expected values in line with model
    assumptions, see Notes below).

    Parameters
    ----------
    evoked : instance of mne.Evoked
        The evoked response.
    noise_cov : list | instance of Covariance | path-like
        The noise covariance. Can be a string to load a covariance from disk.
    show : bool
        Show figure if True.

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
            number of good channels. If a `mne.Covariance` is passed, this can
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
    time_unit : str
        The units for the time axis, can be "ms" or "s" (default).

        ✨ Added in version 0.16
    sphere : float | array-like | instance of ConductorModel | None  | 'auto' | 'eeglab'
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

        ✨ Added in version 0.20
        🎭 Changed in version 1.1 Added ``'eeglab'`` option.
    axes : list | None
        List of axes to plot into.

        ✨ Added in version 0.21.0

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    fig : instance of matplotlib.figure.Figure
        The figure object containing the plot.

    See Also
    --------
    mne.Evoked.plot

    Notes
    -----
    If baseline signals match the assumption of Gaussian white noise,
    values should be centered at 0, and be within 2 standard deviations
    (±1.96) for 95% of the time points. For the global field power (GFP),
    we expect it to fluctuate around a value of 1.

    If one single covariance object is passed, the GFP panel (bottom)
    will depict different sensor types. If multiple covariance objects are
    passed as a list, the left column will display the whitened evoked
    responses for each channel based on the whitener from the noise covariance
    that has the highest log-likelihood. The left column will depict the
    whitened GFPs based on each estimator separately for each sensor type.
    Instead of numbers of channels the GFP display shows the estimated rank.
    Note. The rank estimation will be printed by the logger
    (if ``verbose=True``) for each noise covariance estimator that is passed.

    References
    ----------
    .. [1] Engemann D. and Gramfort A. (2015) Automated model selection in
           covariance estimation and spatial whitening of MEG and EEG
           signals, vol. 108, 328-342, NeuroImage.
    """
    ...

def plot_snr_estimate(evoked, inv, show: bool = True, axes=None, verbose=None):
    """Plot a data SNR estimate.

    Parameters
    ----------
    evoked : instance of Evoked
        The evoked instance. This should probably be baseline-corrected.
    inv : instance of InverseOperator
        The minimum-norm inverse operator.
    show : bool
        Show figure if True.
    axes : instance of Axes | None
        The axes to plot into.

        ✨ Added in version 0.21.0

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    fig : instance of matplotlib.figure.Figure
        The figure object containing the plot.

    Notes
    -----
    The bluish green line is the SNR determined by the GFP of the whitened
    evoked data. The orange line is the SNR estimated based on the mismatch
    between the data and the data re-estimated from the regularized inverse.

    ✨ Added in version 0.9.0
    """
    ...

def plot_evoked_joint(
    evoked,
    times: str = "peaks",
    title: str = "",
    picks=None,
    exclude=None,
    show: bool = True,
    ts_args=None,
    topomap_args=None,
):
    """Plot evoked data as butterfly plot and add topomaps for time points.

    💡 Note Axes to plot in can be passed by the user through ``ts_args`` or
              ``topomap_args``. In that case both ``ts_args`` and
              ``topomap_args`` axes have to be used. Be aware that when the
              axes are provided, their position may be slightly modified.

    Parameters
    ----------
    evoked : instance of Evoked
        The evoked instance.
    times : float | array of float | "auto" | "peaks"
        The time point(s) to plot. If ``"auto"``, 5 evenly spaced topographies
        between the first and last time instant will be shown. If ``"peaks"``,
        finds time points automatically by checking for 3 local maxima in
        Global Field Power. Defaults to ``"peaks"``.
    title : str | None
        The title. If ``None``, suppress printing channel type title. If an
        empty string, a default title is created. Defaults to ''. If custom
        axes are passed make sure to set ``title=None``, otherwise some of your
        axes may be removed during placement of the title axis.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick all channels. Note that channels in
        ``info['bads']`` *will be included* if their names or indices are
        explicitly provided.
    exclude : None | list of str | 'bads'
        Channels names to exclude from being shown. If ``'bads'``, the
        bad channels are excluded. Defaults to ``None``.
    show : bool
        Show figure if ``True``. Defaults to ``True``.
    ts_args : None | dict
        A dict of ``kwargs`` that are forwarded to `mne.Evoked.plot` to
        style the butterfly plot. If they are not in this dict, the following
        defaults are passed: ``spatial_colors=True``, ``zorder='std'``.
        ``show`` and ``exclude`` are illegal.
        If ``None``, no customizable arguments will be passed.
        Defaults to ``None``.
    topomap_args : None | dict
        A dict of ``kwargs`` that are forwarded to
        `mne.Evoked.plot_topomap` to style the topomaps.
        If it is not in this dict, ``outlines='head'`` will be passed.
        ``show``, ``times``, ``colorbar`` are illegal.
        If ``None``, no customizable arguments will be passed.
        Defaults to ``None``.

    Returns
    -------
    fig : instance of matplotlib.figure.Figure | list
        The figure object containing the plot. If ``evoked`` has multiple
        channel types, a list of figures, one for each channel type, is
        returned.

    Notes
    -----
    ✨ Added in version 0.12.0
    """
    ...

def plot_compare_evokeds(
    evokeds,
    picks=None,
    colors=None,
    linestyles=None,
    styles=None,
    cmap=None,
    vlines: str = "auto",
    ci: bool = True,
    truncate_yaxis: str = "auto",
    truncate_xaxis: bool = True,
    ylim=None,
    invert_y: bool = False,
    show_sensors=None,
    legend: bool = True,
    split_legend=None,
    axes=None,
    title=None,
    show: bool = True,
    combine=None,
    sphere=None,
    time_unit: str = "s",
):
    """Plot evoked time courses for one or more conditions and/or channels.

    Parameters
    ----------
    evokeds : instance of mne.Evoked | list | dict
        If a single Evoked instance, it is plotted as a time series.
        If a list of Evokeds, the contents are plotted with their
        ``.comment`` attributes used as condition labels. If no comment is set,
        the index of the respective Evoked the list will be used instead,
        starting with ``1`` for the first Evoked.
        If a dict whose values are Evoked objects, the contents are plotted as
        single time series each and the keys are used as labels.
        If a [dict/list] of lists, the unweighted mean is plotted as a time
        series and the parametric confidence interval is plotted as a shaded
        area. All instances must have the same shape - channel numbers, time
        points etc.
        If dict, keys must be of type str.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick all data channels. Note that channels
        in ``info['bads']`` *will be included* if their names or indices are
        explicitly provided.

        * If picks is None or a (collection of) data channel types, the
          global field power will be plotted for all data channels.
          Otherwise, picks will be averaged.
        * If multiple channel types are selected, one
          figure will be returned for each channel type.
        * If the selected channels are gradiometers, the signal from
          corresponding (gradiometer) pairs will be combined.

    colors : list | dict | None
        Colors to use when plotting the ERP/F lines and confidence bands. If
        ``cmap`` is not ``None``, ``colors`` must be a `list` or
        `dict` of `ints <int>` or `floats <float>`
        indicating steps or percentiles (respectively) along the colormap. If
        ``cmap`` is ``None``, list elements or dict values of ``colors`` must
        be `ints <int>` or valid `matplotlib colors
        <matplotlib:colors_def>`; lists are cycled through
        sequentially,
        while dicts must have keys matching the keys or conditions of an
        ``evokeds`` dict (see Notes for details). If ``None``, the current
        :doc:`matplotlib color cycle
        <matplotlib:gallery/color/color_cycle_default>`
        is used. Defaults to ``None``.
    linestyles : list | dict | None
        Styles to use when plotting the ERP/F lines. If a `list` or
        `dict`, elements must be valid :doc:`matplotlib linestyles
        <matplotlib:gallery/lines_bars_and_markers/linestyles>`. Lists are
        cycled through sequentially; dictionaries must have keys matching the
        keys or conditions of an ``evokeds`` dict (see Notes for details). If
        ``None``, all lines will be solid. Defaults to ``None``.
    styles : dict | None
        Dictionary of styles to use when plotting ERP/F lines. Keys must match
        keys or conditions of ``evokeds``, and values must be a `dict`
        of legal inputs to `matplotlib.pyplot.plot`. Those values will be
        passed as parameters to the line plot call of the corresponding
        condition, overriding defaults (e.g.,
        ``styles={"Aud/L": {"linewidth": 3}}`` will set the linewidth for
        "Aud/L" to 3). As with ``colors`` and ``linestyles``, keys matching
        conditions in ``/``-separated ``evokeds`` keys are supported (see Notes
        for details).
    cmap : None | str | tuple | instance of matplotlib.colors.Colormap
        Colormap from which to draw color values when plotting the ERP/F lines
        and confidence bands. If not ``None``, ints or floats in the ``colors``
        parameter are mapped to steps or percentiles (respectively) along the
        colormap. If ``cmap`` is a `str`, it will be passed to
        ``matplotlib.colormaps``; if ``cmap`` is a tuple, its first
        element will be used as a string to label the colorbar, and its
        second element will be passed to ``matplotlib.colormaps`` (unless
        it is already an instance of `matplotlib.colors.Colormap`).

        🎭 Changed in version 0.19
            Support for passing `matplotlib.colors.Colormap` instances.

    vlines : "auto" | list of float
        A list in seconds at which to plot dashed vertical lines.
        If "auto" and the supplied data includes 0, it is set to [0.]
        and a vertical bar is plotted at time 0. If an empty list is passed,
        no vertical lines are plotted.
    ci : float | bool | callable | None
        Confidence band around each ERP/F time series. If ``False`` or ``None``
        no confidence band is drawn. If `float`, ``ci`` must be between
        0 and 1, and will set the threshold for a bootstrap
        (single plot)/parametric (when ``axes=='topo'``)  estimation of the
        confidence band; ``True`` is equivalent to setting a threshold of 0.95
        (i.e., the 95% confidence band is drawn). If a callable, it must take
        a single array (n_observations × n_times) as input and return upper and
        lower confidence margins (2 × n_times). Defaults to ``True``.
    truncate_yaxis : bool | 'auto'
        Whether to shorten the y-axis spine. If 'auto', the spine is truncated
        at the minimum and maximum ticks. If ``True``, it is truncated at the
        multiple of 0.25 nearest to half the maximum absolute value of the
        data. If ``truncate_xaxis=False``, only the far bound of the y-axis
        will be truncated. Defaults to 'auto'.
    truncate_xaxis : bool
        Whether to shorten the x-axis spine. If ``True``, the spine is
        truncated at the minimum and maximum ticks. If
        ``truncate_yaxis=False``, only the far bound of the x-axis will be
        truncated. Defaults to ``True``.
    ylim : dict | None
        Y-axis limits for plots (after scaling has been applied). `dict`
        keys should match channel types; valid keys are eeg, mag, grad, misc
        (example: ``ylim=dict(eeg=[-20, 20])``). If ``None``, the y-axis limits
        will be set automatically by matplotlib. Defaults to ``None``.
    invert_y : bool
        Whether to plot negative values upward (as is sometimes done
        for ERPs out of tradition). Defaults to ``False``.
    show_sensors : bool | int | str | None
        Whether to display an inset showing sensor locations on a head outline.
        If `int` or `str`, indicates position of the inset (see
        `mpl_toolkits.axes_grid1.inset_locator.inset_axes`). If ``None``,
        treated as ``True`` if there is only one channel in ``picks``. If
        ``True``, location is upper or lower right corner, depending on data
        values. Defaults to ``None``.
    legend : bool | int | str
        Whether to show a legend for the colors/linestyles of the conditions
        plotted. If `int` or `str`, indicates position of the
        legend (see `mpl_toolkits.axes_grid1.inset_locator.inset_axes`).
        If ``True``, equivalent to ``'upper left'``. Defaults to ``True``.
    split_legend : bool | None
        Whether to separate color and linestyle in the legend. If ``None``,
        a separate linestyle legend will still be shown if ``cmap`` is
        specified. Defaults to ``None``.
    axes : None | Axes instance | list of Axes | 'topo'
        `matplotlib.axes.Axes` object to plot into. If plotting
        multiple channel types (or multiple channels when ``combine=None``),
        ``axes`` should be a list of appropriate length containing
        `matplotlib.axes.Axes` objects. If ``'topo'``, a new
        `matplotlib.figure.Figure` is created with one axis for each
        channel, in a topographical layout. If ``None``, a new
        `matplotlib.figure.Figure` is created for each channel type.
        Defaults to ``None``.
    title : str | None
        Title printed above the plot. If ``None``, a title will be
        automatically generated based on channel name(s) or type(s) and the
        value of the ``combine`` parameter. Defaults to ``None``.
    show : bool
        Whether to show the figure. Defaults to ``True``.

    combine : None | str | callable
        How to combine information across channels. If a `str`, must be
        one of 'mean', 'median', 'std' (standard deviation) or 'gfp' (global
        field power).
        If callable, the callable must accept one positional input (data of
        shape ``(n_evokeds, n_channels, n_times)``) and return an
        `array <numpy.ndarray>` of shape ``(n_epochs, n_times)``. For
        example::

            combine = lambda data: np.median(data, axis=1)

        If ``combine`` is ``None``, channels are combined by computing GFP,
        unless ``picks`` is a single channel (not channel type) or
        ``axes='topo'``, in which cases no combining is performed. Defaults to
        ``None``.
    sphere : float | array-like | instance of ConductorModel | None  | 'auto' | 'eeglab'
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

        ✨ Added in version 0.20
        🎭 Changed in version 1.1 Added ``'eeglab'`` option.
    time_unit : str
        The units for the time axis, can be "s" (default) or "ms".

        ✨ Added in version 1.1

    Returns
    -------
    fig : list of Figure instances
        A list of the figure(s) generated.

    Notes
    -----
    If the parameters ``styles``, ``colors``, or ``linestyles`` are passed as
    `dicts <python:dict>`, then ``evokeds`` must also be a
    `python:dict`, and
    the keys of the plot-style parameters must either match the keys of
    ``evokeds``, or match a ``/``-separated partial key ("condition") of
    ``evokeds``. For example, if evokeds has keys "Aud/L", "Aud/R", "Vis/L",
    and "Vis/R", then ``linestyles=dict(L='--', R='-')`` will plot both Aud/L
    and Vis/L conditions with dashed lines and both Aud/R and Vis/R conditions
    with solid lines. Similarly, ``colors=dict(Aud='r', Vis='b')`` will plot
    Aud/L and Aud/R conditions red and Vis/L and Vis/R conditions blue.

    Color specification depends on whether a colormap has been provided in the
    ``cmap`` parameter. The following table summarizes how the ``colors``
    parameter is interpreted:

    .. cssclass:: table-bordered
    .. rst-class:: midvalign

    +-------------+----------------+------------------------------------------+
    | ``cmap``    | ``colors``     | result                                   |
    +=============+================+==========================================+
    |             | None           | matplotlib default color cycle; unique   |
    |             |                | color for each condition                 |
    |             +----------------+------------------------------------------+
    |             |                | matplotlib default color cycle; lowest   |
    |             | list or dict   | integer mapped to first cycle color;     |
    |             | of integers    | conditions with same integer get same    |
    | None        |                | color; unspecified conditions are "gray" |
    |             +----------------+------------------------------------------+
    |             | list or dict   | ``ValueError``                           |
    |             | of floats      |                                          |
    |             +----------------+------------------------------------------+
    |             | list or dict   | the specified hex colors; unspecified    |
    |             | of hexadecimal | conditions are "gray"                    |
    |             | color strings  |                                          |
    +-------------+----------------+------------------------------------------+
    |             | None           | equally spaced colors on the colormap;   |
    |             |                | unique color for each condition          |
    |             +----------------+------------------------------------------+
    |             |                | equally spaced colors on the colormap;   |
    |             | list or dict   | lowest integer mapped to first cycle     |
    | string or   | of integers    | color; conditions with same integer      |
    | instance of |                | get same color                           |
    | matplotlib  +----------------+------------------------------------------+
    | Colormap    | list or dict   | floats mapped to corresponding colormap  |
    |             | of floats      | values                                   |
    |             +----------------+------------------------------------------+
    |             | list or dict   |                                          |
    |             | of hexadecimal | ``TypeError``                            |
    |             | color strings  |                                          |
    +-------------+----------------+------------------------------------------+
    """
    ...
