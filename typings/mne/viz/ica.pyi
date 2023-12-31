from .._fiff.meas_info import create_info as create_info
from .._fiff.pick import pick_types as pick_types
from ..defaults import DEFAULTS as DEFAULTS
from ..utils import fill_doc as fill_doc
from .epochs import plot_epochs_image as plot_epochs_image
from .utils import plt_show as plt_show

def plot_ica_sources(
    ica,
    inst,
    picks=None,
    start=None,
    stop=None,
    title=None,
    show: bool = True,
    block: bool = False,
    show_first_samp: bool = False,
    show_scrollbars: bool = True,
    time_format: str = "float",
    precompute=None,
    use_opengl=None,
    *,
    theme=None,
    overview_mode=None,
    splash: bool = True,
):
    """Plot estimated latent sources given the unmixing matrix.

    Typical usecases:

    1. plot evolution of latent sources over time based on (Raw input)
    2. plot latent source around event related time windows (Epochs input)
    3. plot time-locking in ICA space (Evoked input)

    Parameters
    ----------
    ica : instance of mne.preprocessing.ICA
        The ICA solution.
    inst : instance of Raw, Epochs or Evoked
        The object to plot the sources from.

    picks : int | list of int | slice | None
        Indices of the independent components (ICs) to visualize.
        If an integer, represents the index of the IC to pick.
        Multiple ICs can be selected using a list of int or a slice.
        The indices are 0-indexed, so ``picks=1`` will pick the second
        IC: ``ICA001``. ``None`` will pick all independent components in the order
        fitted.
    start, stop : float | int | None
       If ``inst`` is a `Raw` or an `Evoked` object, the first and
       last time point (in seconds) of the data to plot. If ``inst`` is a
       `Raw` object, ``start=None`` and ``stop=None`` will be
       translated into ``start=0.`` and ``stop=3.``, respectively. For
       `Evoked`, ``None`` refers to the beginning and end of the evoked
       signal. If ``inst`` is an `Epochs` object, specifies the index of
       the first and last epoch to show.
    title : str | None
        The window title. If None a default is provided.
    show : bool
        Show figure if True.
    block : bool
        Whether to halt program execution until the figure is closed.
        Useful for interactive selection of components in raw and epoch
        plotter. For evoked, this parameter has no effect. Defaults to False.
    show_first_samp : bool
        If True, show time axis relative to the ``raw.first_samp``.

    show_scrollbars : bool
        Whether to show scrollbars when the plot is initialized. Can be toggled
        after initialization by pressing `z` ("zen mode") while the plot
        window is focused. Default is ``True``.

        ✨ Added in version 0.19.0

    time_format : 'float' | 'clock'
        Style of time labels on the horizontal axis. If ``'float'``, labels will be
        number of seconds from the start of the recording. If ``'clock'``,
        labels will show "clock time" (hours/minutes/seconds) inferred from
        ``raw.info['meas_date']``. Default is ``'float'``.

        ✨ Added in version 0.24

    precompute : bool | str
        Whether to load all data (not just the visible portion) into RAM and
        apply preprocessing (e.g., projectors) to the full data array in a separate
        processor thread, instead of window-by-window during scrolling. The default
        None uses the ``MNE_BROWSER_PRECOMPUTE`` variable, which defaults to
        ``'auto'``. ``'auto'`` compares available RAM space to the expected size of
        the precomputed data, and precomputes only if enough RAM is available.
        This is only used with the Qt backend.

        ✨ Added in version 0.24
        🎭 Changed in version 1.0
           Support for the MNE_BROWSER_PRECOMPUTE config variable.

    use_opengl : bool | None
        Whether to use OpenGL when rendering the plot (requires ``pyopengl``).
        May increase performance, but effect is dependent on system CPU and
        graphics hardware. Only works if using the Qt backend. Default is
        None, which will use False unless the user configuration variable
        ``MNE_BROWSER_USE_OPENGL`` is set to ``'true'``,
        see `mne.set_config`.

        ✨ Added in version 0.24

    theme : str | path-like
        Can be "auto", "light", or "dark" or a path-like to a
        custom stylesheet. For Dark-Mode and automatic Dark-Mode-Detection,
        `qdarkstyle <https://github.com/ColinDuquesnoy/QDarkStyleSheet>`__ and
        `darkdetect <https://github.com/albertosottile/darkdetect>`__,
        respectively, are required.    If None (default), the config option MNE_BROWSER_THEME will be used,
        defaulting to "auto" if it's not found.
        Only supported by the ``'qt'`` backend.

        ✨ Added in version 1.0

    overview_mode : str | None
        Can be "channels", "empty", or "hidden" to set the overview bar mode
        for the ``'qt'`` backend. If None (default), the config option
        ``MNE_BROWSER_OVERVIEW_MODE`` will be used, defaulting to "channels"
        if it's not found.

        ✨ Added in version 1.1

    splash : bool
        If True (default), a splash screen is shown during the application startup. Only
        applicable to the ``qt`` backend.

        ✨ Added in version 1.6

    Returns
    -------

    fig : matplotlib.figure.Figure | mne_qt_browser.figure.MNEQtBrowser
        Browser instance.

    Notes
    -----
    For raw and epoch instances, it is possible to select components for
    exclusion by clicking on the line. The selected components are added to
    ``ica.exclude`` on close.

    MNE-Python provides two different backends for browsing plots (i.e.,
    `raw.plot()<mne.io.Raw.plot>`, `epochs.plot()<mne.Epochs.plot>`,
    and `ica.plot_sources()<mne.preprocessing.ICA.plot_sources>`). One is
    based on `matplotlib`, and the other is based on
    `PyQtGraph<pyqtgraph:index>`. You can set the backend temporarily with the
    context manager `mne.viz.use_browser_backend`, you can set it for the
    duration of a Python session using `mne.viz.set_browser_backend`, and you
    can set the default for your computer via
    `mne.set_config('MNE_BROWSER_BACKEND', 'matplotlib')<mne.set_config>`
    (or ``'qt'``).

    💡 For the PyQtGraph backend to run in IPython with ``block=False``
              you must run the magic command ``%gui qt5`` first.
    💡 To report issues with the PyQtGraph backend, please use the
              `issues <https://github.com/mne-tools/mne-qt-browser/issues>`_
              of ``mne-qt-browser``.

    ✨ Added in version 0.10.0
    """
    ...

def plot_ica_properties(
    ica,
    inst,
    picks=None,
    axes=None,
    dB: bool = True,
    plot_std: bool = True,
    log_scale: bool = False,
    topomap_args=None,
    image_args=None,
    psd_args=None,
    figsize=None,
    show: bool = True,
    reject: str = "auto",
    reject_by_annotation: bool = True,
    *,
    verbose=None,
):
    """Display component properties.

    Properties include the topography, epochs image, ERP/ERF, power
    spectrum, and epoch variance.

    Parameters
    ----------
    ica : instance of mne.preprocessing.ICA
        The ICA solution.
    inst : instance of Epochs or Raw
        The data to use in plotting properties.

        💡 You can interactively cycle through topographic maps for different
           channel types by pressing `T`.
    picks : int | list of int | slice | None
        Indices of the independent components (ICs) to visualize.
        If an integer, represents the index of the IC to pick.
        Multiple ICs can be selected using a list of int or a slice.
        The indices are 0-indexed, so ``picks=1`` will pick the second
        IC: ``ICA001``. ``None`` will pick the first 5 components.
    axes : list of Axes | None
        List of five matplotlib axes to use in plotting: [topomap_axis,
        image_axis, erp_axis, spectrum_axis, variance_axis]. If None a new
        figure with relevant axes is created. Defaults to None.
    dB : bool
        Whether to plot spectrum in dB. Defaults to True.
    plot_std : bool | float
        Whether to plot standard deviation/confidence intervals in ERP/ERF and
        spectrum plots.
        Defaults to True, which plots one standard deviation above/below for
        the spectrum. If set to float allows to control how many standard
        deviations are plotted for the spectrum. For example 2.5 will plot 2.5
        standard deviation above/below.
        For the ERP/ERF, by default, plot the 95 percent parametric confidence
        interval is calculated. To change this, use ``ci`` in ``ts_args`` in
        ``image_args`` (see below).
    log_scale : bool
        Whether to use a logarithmic frequency axis to plot the spectrum.
        Defaults to ``False``.

        💡 You can interactively toggle this setting by pressing `L`.

        ✨ Added in version 1.1
    topomap_args : dict | None
        Dictionary of arguments to ``plot_topomap``. If None, doesn't pass any
        additional arguments. Defaults to None.
    image_args : dict | None
        Dictionary of arguments to ``plot_epochs_image``. If None, doesn't pass
        any additional arguments. Defaults to None.
    psd_args : dict | None
        Dictionary of arguments to `compute_psd`. If
        ``None``, doesn't pass any additional arguments. Defaults to ``None``.
    figsize : array-like, shape (2,) | None
        Allows to control size of the figure. If None, the figure size
        defaults to [7., 6.].
    show : bool
        Show figure if True.
    reject : 'auto' | dict | None
        Allows to specify rejection parameters used to drop epochs
        (or segments if continuous signal is passed as inst).
        If None, no rejection is applied. The default is 'auto',
        which applies the rejection parameters used when fitting
        the ICA object.

    reject_by_annotation : bool
        Whether to omit bad segments from the data before fitting. If ``True``
        (default), annotated segments whose description begins with ``'bad'`` are
        omitted. If ``False``, no rejection based on annotations is performed.

        Has no effect if ``inst`` is not a `mne.io.Raw` object.

        ✨ Added in version 0.21.0

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    fig : list
        List of matplotlib figures.

    Notes
    -----
    ✨ Added in version 0.13
    """
    ...

def plot_ica_scores(
    ica,
    scores,
    exclude=None,
    labels=None,
    axhline=None,
    title: str = "ICA component scores",
    figsize=None,
    n_cols=None,
    show: bool = True,
):
    """Plot scores related to detected components.

    Use this function to asses how well your score describes outlier
    sources and how well you were detecting them.

    Parameters
    ----------
    ica : instance of mne.preprocessing.ICA
        The ICA object.
    scores : array-like of float, shape (n_ica_components,) | list of array
        Scores based on arbitrary metric to characterize ICA components.
    exclude : array-like of int
        The components marked for exclusion. If None (default), ICA.exclude
        will be used.
    labels : str | list | 'ecg' | 'eog' | None
        The labels to consider for the axes tests. Defaults to None.
        If list, should match the outer shape of ``scores``.
        If 'ecg' or 'eog', the ``labels_`` attributes will be looked up.
        Note that '/' is used internally for sublabels specifying ECG and
        EOG channels.
    axhline : float
        Draw horizontal line to e.g. visualize rejection threshold.
    title : str
        The figure title.
    figsize : tuple of int | None
        The figure size. If None it gets set automatically.
    n_cols : int | None
        Scores are plotted in a grid. This parameter controls how
        many to plot side by side before starting a new row. By
        default, a number will be chosen to make the grid as square as
        possible.
    show : bool
        Show figure if True.

    Returns
    -------
    fig : instance of Figure
        The figure object.
    """
    ...

def plot_ica_overlay(
    ica,
    inst,
    exclude=None,
    picks=None,
    start=None,
    stop=None,
    title=None,
    show: bool = True,
    n_pca_components=None,
    *,
    on_baseline: str = "warn",
    verbose=None,
):
    """Overlay of raw and cleaned signals given the unmixing matrix.

    This method helps visualizing signal quality and artifact rejection.

    Parameters
    ----------
    ica : instance of mne.preprocessing.ICA
        The ICA object.
    inst : instance of Raw or Evoked
        The signal to plot. If `Raw`, the raw data per channel type is displayed
        before and after cleaning. A second panel with the RMS for MEG sensors and the
        `GFP` for EEG sensors is displayed. If `Evoked`, butterfly traces for
        signals before and after cleaning will be superimposed.
    exclude : array-like of int | None (default)
        The components marked for exclusion. If ``None`` (default), the components
        listed in ``ICA.exclude`` will be used.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick `data
        channels`. None (default) will pick all channels that were included during fitting.
    start, stop : float | None
       The first and last time point (in seconds) of the data to plot. If
       ``inst`` is a `Raw` object, ``start=None`` and ``stop=None``
       will be translated into ``start=0.`` and ``stop=3.``, respectively. For
       `Evoked`, ``None`` refers to the beginning and end of the evoked
       signal.

    title : str | None
        The title of the generated figure. If ``None`` (default), no title is
        displayed.
    show : bool
        Show the figure if ``True``.

    n_pca_components : int | float | None
        The number of PCA components to be kept, either absolute (int)
        or fraction of the explained variance (float). If None (default),
        the ``ica.n_pca_components`` from initialization will be used in 0.22;
        in 0.23 all components will be used.

        ✨ Added in version 0.22

    on_baseline : str
        How to handle baseline-corrected epochs or evoked data.
        Can be ``'raise'`` to raise an error, ``'warn'`` (default) to emit a
        warning, ``'ignore'`` to ignore, or "reapply" to reapply the baseline
        after applying ICA.

        ✨ Added in version 1.2

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    fig : instance of Figure
        The figure.
    """
    ...
