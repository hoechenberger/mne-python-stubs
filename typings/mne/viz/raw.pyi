from .._fiff.pick import pick_channels as pick_channels, pick_types as pick_types
from ..filter import create_filter as create_filter
from ..utils import legacy as legacy

def plot_raw(
    raw,
    events=None,
    duration: float = 10.0,
    start: float = 0.0,
    n_channels: int = 20,
    bgcolor: str = "w",
    color=None,
    bad_color: str = "lightgray",
    event_color: str = "cyan",
    scalings=None,
    remove_dc: bool = True,
    order=None,
    show_options: bool = False,
    title=None,
    show: bool = True,
    block: bool = False,
    highpass=None,
    lowpass=None,
    filtorder: int = 4,
    clipping=1.5,
    show_first_samp: bool = False,
    proj: bool = True,
    group_by: str = "type",
    butterfly: bool = False,
    decim: str = "auto",
    noise_cov=None,
    event_id=None,
    show_scrollbars: bool = True,
    show_scalebars: bool = True,
    time_format: str = "float",
    precompute=None,
    use_opengl=None,
    *,
    theme=None,
    overview_mode=None,
    splash: bool = True,
    verbose=None,
):
    """### Plot raw data.

    ### 🛠️ Parameters
    ----------
    raw : instance of Raw
        The raw data to plot.
    events : array | None
        Events to show with vertical bars.
    duration : float
        Time window (s) to plot. The lesser of this value and the duration
        of the raw file will be used.
    start : float
        Initial time to show (can be changed dynamically once plotted). If
        show_first_samp is True, then it is taken relative to
        ``raw.first_samp``.
    n_channels : int
        Number of channels to plot at once. Defaults to 20. The lesser of
        ``n_channels`` and ``len(raw.ch_names)`` will be shown.
        Has no effect if ``order`` is 'position', 'selection' or 'butterfly'.
    bgcolor : color object
        Color of the background.
    color : dict | color object | None
        Color for the data traces. If None, defaults to::

            dict(mag='darkblue', grad='b', eeg='k', eog='k', ecg='m',
                 emg='k', ref_meg='steelblue', misc='k', stim='k',
                 resp='k', chpi='k')

    bad_color : color object
        Color to make bad channels.

    event_color : color object | dict | None
        Color(s) to use for :term:`events`. To show all :term:`events` in the same
        color, pass any matplotlib-compatible color. To color events differently,
        pass a `dict` that maps event names or integer event numbers to colors
        (must include entries for *all* events, or include a "fallback" entry with
        key ``-1``). If ``None``, colors are chosen from the current Matplotlib
        color cycle.
        Defaults to ``'cyan'``.

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

        ### 💡 Note
            A particular scaling value ``s`` corresponds to half of the visualized
            signal range around zero (i.e. from ``0`` to ``+s`` or from ``0`` to
            ``-s``). For example, the default scaling of ``20e-6`` (20µV) for EEG
            signals means that the visualized range will be 40 µV (20 µV in the
            positive direction and 20 µV in the negative direction).
    remove_dc : bool
        If True remove DC component when plotting data.
    order : array of int | None
        Order in which to plot data. If the array is shorter than the number of
        channels, only the given channels are plotted. If None (default), all
        channels are plotted. If ``group_by`` is ``'position'`` or
        ``'selection'``, the ``order`` parameter is used only for selecting the
        channels to be plotted.
    show_options : bool
        If True, a dialog for options related to projection is shown.
    title : str | None
        The title of the window. If None, and either the filename of the
        raw object or '<unknown>' will be displayed as title.
    show : bool
        Show figure if True.
    block : bool
        Whether to halt program execution until the figure is closed.
        Useful for setting bad channels on the fly by clicking on a line.
        May not work on all systems / platforms.
        (Only Qt) If you run from a script, this needs to
        be ``True`` or a Qt-eventloop needs to be started somewhere
        else in the script (e.g. if you want to implement the browser
        inside another Qt-Application).
    highpass : float | None
        Highpass to apply when displaying data.
    lowpass : float | None
        Lowpass to apply when displaying data.
        If highpass > lowpass, a bandstop rather than bandpass filter
        will be applied.
    filtorder : int
        Filtering order. 0 will use FIR filtering with MNE defaults.
        Other values will construct an IIR filter of the given order
        and apply it with `scipy.signal.filtfilt` (making the effective
        order twice ``filtorder``). Filtering may produce some edge artifacts
        (at the left and right edges) of the signals during display.

        🎭 Changed in version 0.18
           Support for ``filtorder=0`` to use FIR filtering.
    clipping : str | float | None
        If None, channels are allowed to exceed their designated bounds in
        the plot. If "clamp", then values are clamped to the appropriate
        range for display, creating step-like artifacts. If "transparent",
        then excessive values are not shown, creating gaps in the traces.
        If float, clipping occurs for values beyond the ``clipping`` multiple
        of their dedicated range, so ``clipping=1.`` is an alias for
        ``clipping='transparent'``.

        🎭 Changed in version 0.21
           Support for float, and default changed from None to 1.5.
    show_first_samp : bool
        If True, show time axis relative to the ``raw.first_samp``.
    proj : bool
        Whether to apply projectors prior to plotting (default is ``True``).
        Individual projectors can be enabled/disabled interactively (see
        Notes). This argument only affects the plot; use ``raw.apply_proj()``
        to modify the data stored in the Raw object.

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
    butterfly : bool
        Whether to start in butterfly mode. Defaults to False.
    decim : int | 'auto'
        Amount to decimate the data during display for speed purposes.
        You should only decimate if the data are sufficiently low-passed,
        otherwise aliasing can occur. The 'auto' mode (default) uses
        the decimation that results in a sampling rate least three times
        larger than ``min(info['lowpass'], lowpass)`` (e.g., a 40 Hz lowpass
        will result in at least a 120 Hz displayed sample rate).
    noise_cov : instance of Covariance | str | None
        Noise covariance used to whiten the data while plotting.
        Whitened data channels are scaled by ``scalings['whitened']``,
        and their channel names are shown in italic.
        Can be a string to load a covariance from disk.
        See also `mne.Evoked.plot_white` for additional inspection
        of noise covariance properties when whitening evoked data.
        For data processed with SSS, the effective dependence between
        magnetometers and gradiometers may introduce differences in scaling,
        consider using `mne.Evoked.plot_white`.

        ✨ Added in vesion 0.16.0
    event_id : dict | None
        Event IDs used to show at event markers (default None shows
        the event numbers).

        ✨ Added in vesion 0.16.0

    show_scrollbars : bool
        Whether to show scrollbars when the plot is initialized. Can be toggled
        after initialization by pressing :kbd:`z` ("zen mode") while the plot
        window is focused. Default is ``True``.

        ✨ Added in vesion 0.19.0

    show_scalebars : bool
        Whether to show scale bars when the plot is initialized. Can be toggled
        after initialization by pressing :kbd:`s` while the plot window is focused.
        Default is ``True``.

        ✨ Added in vesion 0.20.0

    time_format : 'float' | 'clock'
        Style of time labels on the horizontal axis. If ``'float'``, labels will be
        number of seconds from the start of the recording. If ``'clock'``,
        labels will show "clock time" (hours/minutes/seconds) inferred from
        ``raw.info['meas_date']``. Default is ``'float'``.

        ✨ Added in vesion 0.24

    precompute : bool | str
        Whether to load all data (not just the visible portion) into RAM and
        apply preprocessing (e.g., projectors) to the full data array in a separate
        processor thread, instead of window-by-window during scrolling. The default
        None uses the ``MNE_BROWSER_PRECOMPUTE`` variable, which defaults to
        ``'auto'``. ``'auto'`` compares available RAM space to the expected size of
        the precomputed data, and precomputes only if enough RAM is available.
        This is only used with the Qt backend.

        ✨ Added in vesion 0.24
        🎭 Changed in version 1.0
           Support for the MNE_BROWSER_PRECOMPUTE config variable.

    use_opengl : bool | None
        Whether to use OpenGL when rendering the plot (requires ``pyopengl``).
        May increase performance, but effect is dependent on system CPU and
        graphics hardware. Only works if using the Qt backend. Default is
        None, which will use False unless the user configuration variable
        ``MNE_BROWSER_USE_OPENGL`` is set to ``'true'``,
        see `mne.set_config`.

        ✨ Added in vesion 0.24

    theme : str | path-like
        Can be "auto", "light", or "dark" or a path-like to a
        custom stylesheet. For Dark-Mode and automatic Dark-Mode-Detection,
        `qdarkstyle` and
        `darkdetect <https://github.com/albertosottile/darkdetect>`__,
        respectively, are required.    If None (default), the config option MNE_BROWSER_THEME will be used,
        defaulting to "auto" if it's not found.
        Only supported by the ``'qt'`` backend.

        ✨ Added in vesion 1.0

    overview_mode : str | None
        Can be "channels", "empty", or "hidden" to set the overview bar mode
        for the ``'qt'`` backend. If None (default), the config option
        ``MNE_BROWSER_OVERVIEW_MODE`` will be used, defaulting to "channels"
        if it's not found.

        ✨ Added in vesion 1.1

    splash : bool
        If True (default), a splash screen is shown during the application startup. Only
        applicable to the ``qt`` backend.

        ✨ Added in vesion 1.6

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------

    fig : matplotlib.figure.Figure | mne_qt_browser.figure.MNEQtBrowser
        Browser instance.

    ### 📖 Notes
    -----
    The arrow keys (up/down/left/right) can typically be used to navigate
    between channels and time ranges, but this depends on the backend
    matplotlib is configured to use (e.g., mpl.use('TkAgg') should work). The
    left/right arrows will scroll by 25% of ``duration``, whereas
    shift+left/shift+right will scroll by 100% of ``duration``. The scaling
    can be adjusted with - and + (or =) keys. The viewport dimensions can be
    adjusted with page up/page down and home/end keys. Full screen mode can be
    toggled with the F11 key, and scrollbars can be hidden/shown by pressing
    'z'. Right-click a channel label to view its location. To mark or un-mark a
    channel as bad, click on a channel label or a channel trace. The changes
    will be reflected immediately in the raw object's ``raw.info['bads']``
    entry.

    If projectors are present, a button labelled "Prj" in the lower right
    corner of the plot window opens a secondary control window, which allows
    enabling/disabling specific projectors individually. This provides a means
    of interactively observing how each projector would affect the raw data if
    it were applied.

    Annotation mode is toggled by pressing 'a', butterfly mode by pressing
    'b', and whitening mode (when ``noise_cov is not None``) by pressing 'w'.
    By default, the channel means are removed when ``remove_dc`` is set to
    ``True``. This flag can be toggled by pressing 'd'.

    MNE-Python provides two different backends for browsing plots (i.e.,
    `raw.plot()<mne.io.Raw.plot>`, `epochs.plot()<mne.Epochs.plot>`,
    and `ica.plot_sources()<mne.preprocessing.ICA.plot_sources>`). One is
    based on `matplotlib`, and the other is based on
    :doc:`PyQtGraph<pyqtgraph:index>`. You can set the backend temporarily with the
    context manager `mne.viz.use_browser_backend`, you can set it for the
    duration of a Python session using `mne.viz.set_browser_backend`, and you
    can set the default for your computer via
    `mne.set_config('MNE_BROWSER_BACKEND', 'matplotlib')<mne.set_config>`
    (or ``'qt'``).

    ### 💡 Note For the PyQtGraph backend to run in IPython with ``block=False``
              you must run the magic command ``%gui qt5`` first.
    ### 💡 Note To report issues with the PyQtGraph backend, please use the
              `issues <https://github.com/mne-tools/mne-qt-browser/issues>`_
              of ``mne-qt-browser``.
    """
    ...

def plot_raw_psd(
    raw,
    fmin: int = 0,
    fmax=...,
    tmin=None,
    tmax=None,
    proj: bool = False,
    n_fft=None,
    n_overlap: int = 0,
    reject_by_annotation: bool = True,
    picks=None,
    ax=None,
    color: str = "black",
    xscale: str = "linear",
    area_mode: str = "std",
    area_alpha: float = 0.33,
    dB: bool = True,
    estimate: str = "auto",
    show: bool = True,
    n_jobs=None,
    average: bool = False,
    line_alpha=None,
    spatial_colors: bool = True,
    sphere=None,
    window: str = "hamming",
    exclude: str = "bads",
    verbose=None,
):
    """### ### ⛔️ Warning LEGACY: New code should use Raw.compute_psd().plot().

    Plot power or amplitude spectra.

    Separate plots are drawn for each channel type. When the data have been
    processed with a bandpass, lowpass or highpass filter, dashed lines (╎)
    indicate the boundaries of the filter. The line noise frequency is also
    indicated with a dashed line (⋮). If ``average=False``, the plot will
    be interactive, and click-dragging on the spectrum will generate a
    scalp topography plot for the chosen frequency range in a new figure.

    ### 🛠️ Parameters
    ----------
    raw : instance of Raw
        The raw object.
    fmin, fmax : float
        The lower- and upper-bound on frequencies of interest. Default is ``fmin=0, fmax=np.inf`` (spans all frequencies present in the data).
    tmin, tmax : float | None
        First and last times to include, in seconds. ``None`` uses the first or
        last time present in the data. Default is ``tmin=None, tmax=None`` (all
        times).
    proj : bool
        Whether to apply SSP projection vectors before spectral estimation.
        Default is ``False``.
    n_fft : int | None
        Number of points to use in Welch FFT calculations. Default is ``None``,
        which uses the minimum of 2048 and the number of time points.
    n_overlap : int
        The number of points of overlap between blocks. The default value
        is 0 (no overlap).
    reject_by_annotation : bool
        Whether to omit bad spans of data before spectral estimation. If
        ``True``, spans with annotations whose description begins with
        ``bad`` will be omitted.
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
        The axes to plot to. If ``None``, a new `matplotlib.figure.Figure`
        will be created with the correct number of axes. If `matplotlib.axes.Axes` are provided (either as a single instance or a `list` of axes), the number of axes provided must match the number of channel types present in the object..Default is ``None``.
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
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
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
        of a spherical `mne.bem.ConductorModel` to use the origin and
        radius from that object. If ``'auto'`` the sphere is fit to digitization
        points. If ``'eeglab'`` the head circle is defined by EEG electrodes
        ``'Fpz'``, ``'Oz'``, ``'T7'``, and ``'T8'`` (if ``'Fpz'`` is not present,
        it will be approximated from the coordinates of ``'Oz'``). ``None`` (the
        default) is equivalent to ``'auto'`` when enough extra digitization points
        are available, and (0, 0, 0, 0.095) otherwise.

        ✨ Added in vesion 0.20
        🎭 Changed in version 1.1 Added ``'eeglab'`` option.
    window : str | float | tuple
        Windowing function to use. See `scipy.signal.get_window`.

        ✨ Added in vesion 0.22.0
    exclude : list of str | 'bads'
        Channels names to exclude from being shown. If 'bads', the bad channels
        are excluded. Pass an empty list to plot all channels (including
        channels marked "bad", if any).

        ✨ Added in vesion 0.24.0

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    fig : instance of Figure
        Figure with frequency spectra of the data channels.

    ### 📖 Notes
    -----
    This function exists to support legacy code; for new code the preferred
    idiom is ``inst.compute_psd().plot()`` (where ``inst`` is an instance
    of `mne.io.Raw`, `mne.Epochs`, or `mne.Evoked`).
    """
    ...

def plot_raw_psd_topo(
    raw,
    tmin: float = 0.0,
    tmax=None,
    fmin: float = 0.0,
    fmax: float = 100.0,
    proj: bool = False,
    *,
    n_fft: int = 2048,
    n_overlap: int = 0,
    dB: bool = True,
    layout=None,
    color: str = "w",
    fig_facecolor: str = "k",
    axis_facecolor: str = "k",
    axes=None,
    block: bool = False,
    show: bool = True,
    n_jobs=None,
    verbose=None,
):
    """### ### ⛔️ Warning LEGACY: New code should use Raw.compute_psd().plot_topo().

    Plot power spectral density, separately for each channel.

    ### 🛠️ Parameters
    ----------
    raw : instance of io.Raw
        The raw instance to use.
    tmin, tmax : float | None
        First and last times to include, in seconds. ``None`` uses the first or
        last time present in the data. Default is ``tmin=None, tmax=None`` (all
        times).
    fmin, fmax : float
        The lower- and upper-bound on frequencies of interest. Default is ``fmin=0, fmax=100``.
    proj : bool
        Whether to apply SSP projection vectors before spectral estimation.
        Default is ``False``.
    n_fft : int
        Number of points to use in Welch FFT calculations. Defaults to 2048.
    n_overlap : int
        The number of points of overlap between blocks. Defaults to 0
        (no overlap).
    dB : bool
        Whether to plot on a decibel-like scale. If ``True``, plots
        10 × log₁₀(spectral power). Ignored if ``normalize=True``.
    layout : instance of Layout | None
        Layout instance specifying sensor positions (does not need to be
        specified for Neuromag data). If ``None`` (default), the layout is
        inferred from the data.
    color : str | tuple
        A matplotlib-compatible color to use for the curves. Defaults to white.
    fig_facecolor : str | tuple
        A matplotlib-compatible color to use for the figure background.
        Defaults to black.
    axis_facecolor : str | tuple
        A matplotlib-compatible color to use for the axis background.
        Defaults to black.
    axes : instance of Axes | list of Axes | None
        The axes to plot to. If ``None``, a new `matplotlib.figure.Figure`
        will be created with the correct number of axes. If `matplotlib.axes.Axes` are provided (either as a single instance or a `list` of axes), the number of axes provided must be length 1 (for efficiency, subplots for each channel are simulated within a single `matplotlib.axes.Axes` object).Default is ``None``.
    block : bool
        Whether to halt program execution until the figure is closed.
        May not work on all systems / platforms. Defaults to False.
    show : bool
        Show the figure if ``True``.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    fig : instance of matplotlib.figure.Figure
        Figure distributing one image per channel across sensor topography.
    """
    ...
