from .._fiff.meas_info import create_info as create_info
from ..utils import fill_doc as fill_doc, legacy as legacy, logger as logger, verbose as verbose, warn as warn
from .utils import DraggableColorbar as DraggableColorbar, plt_show as plt_show
from _typeshed import Incomplete

def plot_epochs_image(epochs, picks: Incomplete | None=..., sigma: float=..., vmin: Incomplete | None=..., vmax: Incomplete | None=..., colorbar: bool=..., order: Incomplete | None=..., show: bool=..., units: Incomplete | None=..., scalings: Incomplete | None=..., cmap: Incomplete | None=..., fig: Incomplete | None=..., axes: Incomplete | None=..., overlay_times: Incomplete | None=..., combine: Incomplete | None=..., group_by: Incomplete | None=..., evoked: bool=..., ts_args: Incomplete | None=..., title: Incomplete | None=..., clear: bool=...):
    """Plot Event Related Potential / Fields image.

    Parameters
    ----------
    epochs : instance of Epochs
        The epochs.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as 
        channel indices. In lists, channel *type* strings (e.g., ``['meg', 
        'eeg']``) will pick channels of those types, channel *name* strings (e.g., 
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the 
        string values "all" to pick all channels, or "data" to pick :term:`data 
        channels`. None (default) will pick good data channels. Note that channels 
        in ``info['bads']`` *will be included* if their names or indices are 
        explicitly provided.
        ``picks`` interacts with ``group_by`` and ``combine`` to determine the
        number of figures generated; see Notes.
    sigma : float
        The standard deviation of a Gaussian smoothing window applied along
        the epochs axis of the image. If 0, no smoothing is applied.
        Defaults to 0.
    vmin : None | float | callable
        The min value in the image (and the ER[P/F]). The unit is µV for
        EEG channels, fT for magnetometers and fT/cm for gradiometers.
        If vmin is None and multiple plots are returned, the limit is
        equalized within channel types.
        Hint: to specify the lower limit of the data, use
        ``vmin=lambda data: data.min()``.
    vmax : None | float | callable
        The max value in the image (and the ER[P/F]). The unit is µV for
        EEG channels, fT for magnetometers and fT/cm for gradiometers.
        If vmin is None and multiple plots are returned, the limit is
        equalized within channel types.
    colorbar : bool
        Display or not a colorbar.
    order : None | array of int | callable
        If not ``None``, order is used to reorder the epochs along the y-axis
        of the image. If it is an array of :class:`int`, its length should
        match the number of good epochs. If it is a callable it should accept
        two positional parameters (``times`` and ``data``, where
        ``data.shape == (len(good_epochs), len(times))``) and return an
        :class:`array <numpy.ndarray>` of indices that will sort ``data`` along
        its first axis.
    show : bool
        Show figure if True.
    units : dict | None
        The units of the channel types used for axes labels. If None,
        defaults to ``units=dict(eeg='µV', grad='fT/cm', mag='fT')``.
    scalings : dict | None
        The scalings of the channel types to be applied for plotting.
        If None, defaults to ``scalings=dict(eeg=1e6, grad=1e13, mag=1e15,
        eog=1e6)``.
    cmap : None | colormap | (colormap, bool) | 'interactive'
        Colormap. If tuple, the first value indicates the colormap to use and
        the second value is a boolean defining interactivity. In interactive
        mode the colors are adjustable by clicking and dragging the colorbar
        with left and right mouse button. Left mouse button moves the scale up
        and down and right mouse button adjusts the range. Hitting space bar
        resets the scale. Up and down arrows can be used to change the
        colormap. If 'interactive', translates to ('RdBu_r', True).
        If None, "RdBu_r" is used, unless the data is all positive, in which
        case "Reds" is used.
    fig : Figure | None
        :class:`~matplotlib.figure.Figure` instance to draw the image to.
        Figure must contain the correct number of axes for drawing the epochs
        image, the evoked response, and a colorbar (depending on values of
        ``evoked`` and ``colorbar``). If ``None`` a new figure is created.
        Defaults to ``None``.
    axes : list of Axes | dict of list of Axes | None
        List of :class:`~matplotlib.axes.Axes` objects in which to draw the
        image, evoked response, and colorbar (in that order). Length of list
        must be 1, 2, or 3 (depending on values of ``colorbar`` and ``evoked``
        parameters). If a :class:`dict`, each entry must be a list of Axes
        objects with the same constraints as above. If both ``axes`` and
        ``group_by`` are dicts, their keys must match. Providing non-``None``
        values for both ``fig`` and ``axes``  results in an error. Defaults to
        ``None``.
    overlay_times : array_like, shape (n_epochs,) | None
        Times (in seconds) at which to draw a line on the corresponding row of
        the image (e.g., a reaction time associated with each epoch). Note that
        ``overlay_times`` should be ordered to correspond with the
        :class:`~mne.Epochs` object (i.e., ``overlay_times[0]`` corresponds to
        ``epochs[0]``, etc).
    
    combine : None | str | callable
        How to combine information across channels. If a :class:`str`, must be
        one of 'mean', 'median', 'std' (standard deviation) or 'gfp' (global
        field power).
        If callable, the callable must accept one positional input (data of
        shape ``(n_epochs, n_channels, n_times)``) and return an
        :class:`array <numpy.ndarray>` of shape ``(n_epochs, n_times)``. For
        example::

            combine = lambda data: np.median(data, axis=1)

        If ``combine`` is ``None``, channels are combined by computing GFP,
        unless ``group_by`` is also ``None`` and ``picks`` is a list of
        specific channels (not channel types), in which case no combining is
        performed and each channel gets its own figure. See Notes for further
        details. Defaults to ``None``.
    group_by : None | dict
        Specifies which channels are aggregated into a single figure, with
        aggregation method determined by the ``combine`` parameter. If not
        ``None``, one :class:`~matplotlib.figure.Figure` is made per dict
        entry; the dict key will be used as the figure title and the dict
        values must be lists of picks (either channel names or integer indices
        of ``epochs.ch_names``). For example::

            group_by=dict(Left_ROI=[1, 2, 3, 4], Right_ROI=[5, 6, 7, 8])

        Note that within a dict entry all channels must have the same type.
        ``group_by`` interacts with ``picks`` and ``combine`` to determine the
        number of figures generated; see Notes. Defaults to ``None``.
    evoked : bool
        Draw the ER[P/F] below the image or not.
    ts_args : None | dict
        Arguments passed to a call to `~mne.viz.plot_compare_evokeds` to style
        the evoked plot below the image. Defaults to an empty dictionary,
        meaning `~mne.viz.plot_compare_evokeds` will be called with default
        parameters.
    title : None | str
        If :class:`str`, will be plotted as figure title. Otherwise, the
        title will indicate channel(s) or channel type being plotted. Defaults
        to ``None``.
    clear : bool
        Whether to clear the axes before plotting (if ``fig`` or ``axes`` are
        provided). Defaults to ``False``.

    Returns
    -------
    figs : list of Figure
        One figure per channel, channel type, or group, depending on values of
        ``picks``, ``group_by``, and ``combine``. See Notes.

    Notes
    -----
    You can control how channels are aggregated into one figure or plotted in
    separate figures through a combination of the ``picks``, ``group_by``, and
    ``combine`` parameters. If ``group_by`` is a :class:`dict`, the result is
    one :class:`~matplotlib.figure.Figure` per dictionary key (for any valid
    values of ``picks`` and ``combine``). If ``group_by`` is ``None``, the
    number and content of the figures generated depends on the values of
    ``picks`` and ``combine``, as summarized in this table:

    .. cssclass:: table-bordered
    .. rst-class:: midvalign

    +----------+----------------------------+------------+-------------------+
    | group_by | picks                      | combine    | result            |
    +==========+============================+============+===================+
    |          | None, int, list of int,    | None,      |                   |
    | dict     | ch_name, list of ch_names, | string, or | 1 figure per      |
    |          | ch_type, list of ch_types  | callable   | dict key          |
    +----------+----------------------------+------------+-------------------+
    |          | None,                      | None,      |                   |
    |          | ch_type,                   | string, or | 1 figure per      |
    |          | list of ch_types           | callable   | ch_type           |
    | None     +----------------------------+------------+-------------------+
    |          | int,                       | None       | 1 figure per pick |
    |          | ch_name,                   +------------+-------------------+
    |          | list of int,               | string or  | 1 figure          |
    |          | list of ch_names           | callable   |                   |
    +----------+----------------------------+------------+-------------------+
    """

def plot_drop_log(drop_log, threshold: int=..., n_max_plot: int=..., subject: Incomplete | None=..., color: str=..., width: float=..., ignore=..., show: bool=...):
    """Show the channel stats based on a drop_log from Epochs.

    Parameters
    ----------
    drop_log : list of list
        Epoch drop log from Epochs.drop_log.
    threshold : float
        The percentage threshold to use to decide whether or not to
        plot. Default is zero (always plot).
    n_max_plot : int
        Maximum number of channels to show stats for.
    subject : str | None
        The subject name to use in the title of the plot. If ``None``, do not
        display a subject name.

        .. versionchanged:: 0.23
           Added support for ``None``.

        .. versionchanged:: 1.0
           Defaults to ``None``.
    color : tuple | str
        Color to use for the bars.
    width : float
        Width of the bars.
    ignore : list
        The drop reasons to ignore.
    show : bool
        Show figure if True.

    Returns
    -------
    fig : instance of matplotlib.figure.Figure
        The figure.
    """

def plot_epochs(epochs, picks: Incomplete | None=..., scalings: Incomplete | None=..., n_epochs: int=..., n_channels: int=..., title: Incomplete | None=..., events: bool=..., event_color: Incomplete | None=..., order: Incomplete | None=..., show: bool=..., block: bool=..., decim: str=..., noise_cov: Incomplete | None=..., butterfly: bool=..., show_scrollbars: bool=..., show_scalebars: bool=..., epoch_colors: Incomplete | None=..., event_id: Incomplete | None=..., group_by: str=..., precompute: Incomplete | None=..., use_opengl: Incomplete | None=..., *, theme: Incomplete | None=..., overview_mode: Incomplete | None=..., splash: bool=...):
    """Visualize epochs.

    Bad epochs can be marked with a left click on top of the epoch. Bad
    channels can be selected by clicking the channel name on the left side of
    the main axes. Calling this function drops all the selected bad epochs as
    well as bad epochs marked beforehand with rejection parameters.

    Parameters
    ----------
    epochs : instance of Epochs
        The epochs object.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as 
        channel indices. In lists, channel *type* strings (e.g., ``['meg', 
        'eeg']``) will pick channels of those types, channel *name* strings (e.g., 
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the 
        string values "all" to pick all channels, or "data" to pick :term:`data 
        channels`. None (default) will pick good data channels. Note that channels 
        in ``info['bads']`` *will be included* if their names or indices are 
        explicitly provided.
    
    scalings : 'auto' | dict | None
        Scaling factors for the traces. If a dictionary where any
        value is ``'auto'``, the scaling factor is set to match the 99.5th
        percentile of the respective data. If ``'auto'``, all scalings (for all
        channel types) are set to ``'auto'``. If any values are ``'auto'`` and the
        data is not preloaded, a subset up to 100 MB will be loaded. If ``None``,
        defaults to::
    
            dict(mag=1e-12, grad=4e-11, eeg=20e-6, eog=150e-6, ecg=5e-4,
                 emg=1e-3, ref_meg=1e-12, misc=1e-3, stim=1,
                 resp=1, chpi=1e-4, whitened=1e2)
    
        .. note::
            A particular scaling value ``s`` corresponds to half of the visualized
            signal range around zero (i.e. from ``0`` to ``+s`` or from ``0`` to
            ``-s``). For example, the default scaling of ``20e-6`` (20µV) for EEG
            signals means that the visualized range will be 40 µV (20 µV in the
            positive direction and 20 µV in the negative direction).
    n_epochs : int
        The number of epochs per view. Defaults to 20.
    n_channels : int
        The number of channels per view. Defaults to 20.
    title : str | None
        The title of the window. If None, the event names (from
        ``epochs.event_id``) will be displayed. Defaults to None.
    events : bool | array, shape (n_events, 3)
        Events to show with vertical bars. You can use `~mne.viz.plot_events`
        as a legend for the colors. By default, the coloring scheme is the
        same. ``True`` plots ``epochs.events``. Defaults to ``False`` (do not
        plot events).

        .. warning::  If the epochs have been resampled, the events no longer
            align with the data.

        .. versionadded:: 0.14.0

        .. versionchanged:: 1.6
            Passing ``events=None`` was disallowed.
            The new equivalent is ``events=False``.
    
    event_color : color object | dict | None
        Color(s) to use for :term:`events`. To show all :term:`events` in the same
        color, pass any matplotlib-compatible color. To color events differently,
        pass a `dict` that maps event names or integer event numbers to colors
        (must include entries for *all* events, or include a "fallback" entry with
        key ``-1``). If ``None``, colors are chosen from the current Matplotlib
        color cycle.
        Defaults to ``None``.
    order : array of str | None
        Order in which to plot channel types.

        .. versionadded:: 0.18.0
    show : bool
        Show figure if True. Defaults to True.
    block : bool
        Whether to halt program execution until the figure is closed.
        Useful for rejecting bad trials on the fly by clicking on an epoch.
        Defaults to False.
    decim : int | 'auto'
        Amount to decimate the data during display for speed purposes.
        You should only decimate if the data are sufficiently low-passed,
        otherwise aliasing can occur. The 'auto' mode (default) uses
        the decimation that results in a sampling rate at least three times
        larger than ``info['lowpass']`` (e.g., a 40 Hz lowpass will result in
        at least a 120 Hz displayed sample rate).

        .. versionadded:: 0.15.0
    noise_cov : instance of Covariance | str | None
        Noise covariance used to whiten the data while plotting.
        Whitened data channels are scaled by ``scalings['whitened']``,
        and their channel names are shown in italic.
        Can be a string to load a covariance from disk.
        See also :meth:`mne.Evoked.plot_white` for additional inspection
        of noise covariance properties when whitening evoked data.
        For data processed with SSS, the effective dependence between
        magnetometers and gradiometers may introduce differences in scaling,
        consider using :meth:`mne.Evoked.plot_white`.

        .. versionadded:: 0.16.0
    butterfly : bool
        Whether to directly call the butterfly view.

        .. versionadded:: 0.18.0
    
    show_scrollbars : bool
        Whether to show scrollbars when the plot is initialized. Can be toggled
        after initialization by pressing :kbd:`z` ("zen mode") while the plot
        window is focused. Default is ``True``.
    
        .. versionadded:: 0.19.0
    
    show_scalebars : bool
        Whether to show scale bars when the plot is initialized. Can be toggled
        after initialization by pressing :kbd:`s` while the plot window is focused.
        Default is ``True``.

        .. versionadded:: 0.24.0
    epoch_colors : list of (n_epochs) list (of n_channels) | None
        Colors to use for individual epochs. If None, use default colors.
    event_id : bool | dict
        Determines to label the event markers on the plot. If ``True``, uses
        ``epochs.event_id``. If ``False``, uses integer event codes instead of IDs.
        If a ``dict`` is passed, uses its *keys* as event labels on the plot for
        entries whose *values* are integer codes for events being drawn. Ignored if
        ``events=False``.

        .. versionadded:: 0.20
    
    group_by : str
        How to group channels. ``'type'`` groups by channel type,
        ``'original'`` plots in the order of ch_names, ``'selection'`` uses
        Elekta's channel groupings (only works for Neuromag data),
        ``'position'`` groups the channels by the positions of the sensors.
        ``'selection'`` and ``'position'`` modes allow custom selections by
        using a lasso selector on the topomap. In butterfly mode, ``'type'``
        and ``'original'`` group the channels by type, whereas ``'selection'``
        and ``'position'`` use regional grouping. ``'type'`` and ``'original'``
        modes are ignored when ``order`` is not ``None``. Defaults to ``'type'``.
    
    precompute : bool | str
        Whether to load all data (not just the visible portion) into RAM and
        apply preprocessing (e.g., projectors) to the full data array in a separate
        processor thread, instead of window-by-window during scrolling. The default
        None uses the ``MNE_BROWSER_PRECOMPUTE`` variable, which defaults to
        ``'auto'``. ``'auto'`` compares available RAM space to the expected size of
        the precomputed data, and precomputes only if enough RAM is available.
        This is only used with the Qt backend.
    
        .. versionadded:: 0.24
        .. versionchanged:: 1.0
           Support for the MNE_BROWSER_PRECOMPUTE config variable.
    
    use_opengl : bool | None
        Whether to use OpenGL when rendering the plot (requires ``pyopengl``).
        May increase performance, but effect is dependent on system CPU and
        graphics hardware. Only works if using the Qt backend. Default is
        None, which will use False unless the user configuration variable
        ``MNE_BROWSER_USE_OPENGL`` is set to ``'true'``,
        see :func:`mne.set_config`.
    
        .. versionadded:: 0.24
    
    theme : str | path-like
        Can be "auto", "light", or "dark" or a path-like to a
        custom stylesheet. For Dark-Mode and automatic Dark-Mode-Detection,
        :mod:`qdarkstyle` and
        `darkdetect <https://github.com/albertosottile/darkdetect>`__,
        respectively, are required.    If None (default), the config option MNE_BROWSER_THEME will be used,
        defaulting to "auto" if it's not found.
        Only supported by the ``'qt'`` backend.

        .. versionadded:: 1.0
    
    overview_mode : str | None
        Can be "channels", "empty", or "hidden" to set the overview bar mode
        for the ``'qt'`` backend. If None (default), the config option
        ``MNE_BROWSER_OVERVIEW_MODE`` will be used, defaulting to "channels"
        if it's not found.

        .. versionadded:: 1.1
    
    splash : bool
        If True (default), a splash screen is shown during the application startup. Only
        applicable to the ``qt`` backend.

        .. versionadded:: 1.6

    Returns
    -------
    
    fig : matplotlib.figure.Figure | mne_qt_browser.figure.MNEQtBrowser
        Browser instance.

    Notes
    -----
    The arrow keys (up/down/left/right) can be used to navigate between
    channels and epochs and the scaling can be adjusted with - and + (or =)
    keys, but this depends on the backend matplotlib is configured to use
    (e.g., mpl.use(``TkAgg``) should work). Full screen mode can be toggled
    with f11 key. The amount of epochs and channels per view can be adjusted
    with home/end and page down/page up keys. ``h`` key plots a histogram of
    peak-to-peak values along with the used rejection thresholds. Butterfly
    plot can be toggled with ``b`` key. Left mouse click adds a vertical line
    to the plot. Click 'help' button at bottom left corner of the plotter to
    view all the options.

    MNE-Python provides two different backends for browsing plots (i.e.,
    :meth:`raw.plot()<mne.io.Raw.plot>`, :meth:`epochs.plot()<mne.Epochs.plot>`,
    and :meth:`ica.plot_sources()<mne.preprocessing.ICA.plot_sources>`). One is
    based on :mod:`matplotlib`, and the other is based on
    :doc:`PyQtGraph<pyqtgraph:index>`. You can set the backend temporarily with the
    context manager :func:`mne.viz.use_browser_backend`, you can set it for the
    duration of a Python session using :func:`mne.viz.set_browser_backend`, and you
    can set the default for your computer via
    :func:`mne.set_config('MNE_BROWSER_BACKEND', 'matplotlib')<mne.set_config>`
    (or ``'qt'``).
    
    .. note:: For the PyQtGraph backend to run in IPython with ``block=False``
              you must run the magic command ``%gui qt5`` first.
    .. note:: To report issues with the PyQtGraph backend, please use the
              `issues <https://github.com/mne-tools/mne-qt-browser/issues>`_
              of ``mne-qt-browser``.

    .. versionadded:: 0.10.0
    """

def plot_epochs_psd(epochs, fmin: int=..., fmax=..., tmin: Incomplete | None=..., tmax: Incomplete | None=..., proj: bool=..., bandwidth: Incomplete | None=..., adaptive: bool=..., low_bias: bool=..., normalization: str=..., picks: Incomplete | None=..., ax: Incomplete | None=..., color: str=..., xscale: str=..., area_mode: str=..., area_alpha: float=..., dB: bool=..., estimate: str=..., show: bool=..., n_jobs: Incomplete | None=..., average: bool=..., line_alpha: Incomplete | None=..., spatial_colors: bool=..., sphere: Incomplete | None=..., exclude: str=..., verbose: Incomplete | None=...):
    """.. warning:: LEGACY: New code should use Epochs.compute_psd().plot().

    Plot power or amplitude spectra.
    
    Separate plots are drawn for each channel type. When the data have been
    processed with a bandpass, lowpass or highpass filter, dashed lines (╎)
    indicate the boundaries of the filter. The line noise frequency is also
    indicated with a dashed line (⋮). If ``average=False``, the plot will
    be interactive, and click-dragging on the spectrum will generate a
    scalp topography plot for the chosen frequency range in a new figure.

    Parameters
    ----------
    epochs : instance of Epochs
        The epochs object.
    fmin, fmax : float
        The lower- and upper-bound on frequencies of interest. Default is ``fmin=0, fmax=np.inf`` (spans all frequencies present in the data).
    tmin, tmax : float | None
        First and last times to include, in seconds. ``None`` uses the first or
        last time present in the data. Default is ``tmin=None, tmax=None`` (all
        times).
    proj : bool
        Whether to apply SSP projection vectors before spectral estimation.
        Default is ``False``.
    bandwidth : float
        The bandwidth of the multi taper windowing function in Hz. The default
        value is a window half-bandwidth of 4.
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
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as 
        channel indices. In lists, channel *type* strings (e.g., ``['meg', 
        'eeg']``) will pick channels of those types, channel *name* strings (e.g., 
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the 
        string values "all" to pick all channels, or "data" to pick :term:`data 
        channels`. None (default) will pick good data channels (excluding reference 
        MEG channels). Note that channels in ``info['bads']`` *will be included* if 
        their names or indices are explicitly provided.
    ax : instance of Axes | list of Axes | None
        The axes to plot to. If ``None``, a new :class:`~matplotlib.figure.Figure`
        will be created with the correct number of axes. If :class:`~matplotlib.axes.Axes` are provided (either as a single instance or a :class:`list` of axes), the number of axes provided must match the number of channel types present in the object..Default is ``None``.
    color : str | tuple
        A matplotlib-compatible color to use. Has no effect when
        spatial_colors=True.
    xscale : 'linear' | 'log'
        Scale of the frequency axis. Default is ``'linear'``.
    area_mode : str | None
        Mode for plotting area. If 'std', the mean +/- 1 STD (across channels)
        will be plotted. If 'range', the min and max (across channels) will be
        plotted. Bad channels will be excluded from these calculations.
        If None, no area will be plotted. If average=False, no area is plotted.
    area_alpha : float
        Alpha for the area.
    dB : bool
        Plot Power Spectral Density (PSD), in units (amplitude**2/Hz (dB)) if
        ``dB=True``, and ``estimate='power'`` or ``estimate='auto'``. Plot PSD
        in units (amplitude**2/Hz) if ``dB=False`` and,
        ``estimate='power'``. Plot Amplitude Spectral Density (ASD), in units
        (amplitude/sqrt(Hz)), if ``dB=False`` and ``estimate='amplitude'`` or
        ``estimate='auto'``. Plot ASD, in units (amplitude/sqrt(Hz) (dB)), if
        ``dB=True`` and ``estimate='amplitude'``.
    estimate : str, {'auto', 'power', 'amplitude'}
        Can be "power" for power spectral density (PSD), "amplitude" for
        amplitude spectrum density (ASD), or "auto" (default), which uses
        "power" when dB is True and "amplitude" otherwise.
    show : bool
        Show the figure if ``True``.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the :mod:`joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a :class:`joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.
    average : bool
        If False, the PSDs of all channels is displayed. No averaging
        is done and parameters area_mode and area_alpha are ignored. When
        False, it is possible to paint an area (hold left mouse button and
        drag) to plot a topomap.
    line_alpha : float | None
        Alpha for the PSD line. Can be None (default) to use 1.0 when
        ``average=True`` and 0.1 when ``average=False``.
    spatial_colors : bool
        Whether to color spectrum lines by channel location. Ignored if
        ``average=True``.
    sphere : float | array-like | instance of ConductorModel | None  | 'auto' | 'eeglab'
        The sphere parameters to use for the head outline. Can be array-like of
        shape (4,) to give the X/Y/Z origin and radius in meters, or a single float
        to give just the radius (origin assumed 0, 0, 0). Can also be an instance
        of a spherical :class:`~mne.bem.ConductorModel` to use the origin and
        radius from that object. If ``'auto'`` the sphere is fit to digitization
        points. If ``'eeglab'`` the head circle is defined by EEG electrodes
        ``'Fpz'``, ``'Oz'``, ``'T7'``, and ``'T8'`` (if ``'Fpz'`` is not present,
        it will be approximated from the coordinates of ``'Oz'``). ``None`` (the
        default) is equivalent to ``'auto'`` when enough extra digitization points
        are available, and (0, 0, 0, 0.095) otherwise.
    
        .. versionadded:: 0.20
        .. versionchanged:: 1.1 Added ``'eeglab'`` option.
    exclude : list of str | 'bads'
        Channels names to exclude from being shown. If 'bads', the bad channels
        are excluded. Pass an empty list to plot all channels (including
        channels marked "bad", if any).

        .. versionadded:: 0.24.0
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    fig : instance of Figure
        Figure with frequency spectra of the data channels.

    Notes
    -----
    This function exists to support legacy code; for new code the preferred
    idiom is ``inst.compute_psd().plot()`` (where ``inst`` is an instance
    of :class:`~mne.io.Raw`, :class:`~mne.Epochs`, or :class:`~mne.Evoked`).
    """