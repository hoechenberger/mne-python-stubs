from .._fiff.constants import FIFF as FIFF
from .._fiff.pick import (
    pick_channels as pick_channels,
    pick_info as pick_info,
    pick_types as pick_types,
)
from .._fiff.proj import make_projector as make_projector
from ..defaults import DEFAULTS as DEFAULTS
from ..filter import estimate_ringing_samples as estimate_ringing_samples
from ..rank import compute_rank as compute_rank
from ..surface import read_surface as read_surface
from ..transforms import apply_trans as apply_trans
from ..utils import (
    fill_doc as fill_doc,
    get_subjects_dir as get_subjects_dir,
    logger as logger,
    warn as warn,
)
from .utils import plt_show as plt_show

def plot_cov(
    cov,
    info,
    exclude=(),
    colorbar: bool = True,
    proj: bool = False,
    show_svd: bool = True,
    show: bool = True,
    verbose=None,
):
    """Plot Covariance data.

    Parameters
    ----------
    cov : instance of Covariance
        The covariance matrix.

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    exclude : list of str | str
        List of channels to exclude. If empty do not exclude any channel.
        If 'bads', exclude info['bads'].
    colorbar : bool
        Show colorbar or not.
    proj : bool
        Apply projections or not.
    show_svd : bool
        Plot also singular values of the noise covariance for each sensor
        type. We show square roots ie. standard deviations.
    show : bool
        Show figure if True.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    fig_cov : instance of matplotlib.figure.Figure
        The covariance plot.
    fig_svd : instance of matplotlib.figure.Figure | None
        The SVD spectra plot of the covariance.

    See Also
    --------
    mne.compute_rank

    Notes
    -----
    For each channel type, the rank is estimated using
    `mne.compute_rank`.

    🎭 Changed in version 0.19
       Approximate ranks for each channel type are shown with red dashed lines.
    """
    ...

def plot_source_spectrogram(
    stcs,
    freq_bins,
    tmin=None,
    tmax=None,
    source_index=None,
    colorbar: bool = False,
    show: bool = True,
):
    """Plot source power in time-freqency grid.

    Parameters
    ----------
    stcs : list of SourceEstimate
        Source power for consecutive time windows, one SourceEstimate object
        should be provided for each frequency bin.
    freq_bins : list of tuples of float
        Start and end points of frequency bins of interest.
    tmin : float
        Minimum time instant to show.
    tmax : float
        Maximum time instant to show.
    source_index : int | None
        Index of source for which the spectrogram will be plotted. If None,
        the source with the largest activation will be selected.
    colorbar : bool
        If true, a colorbar will be added to the plot.
    show : bool
        Show figure if True.

    Returns
    -------
    fig : instance of Figure
        The figure.
    """
    ...

def plot_bem(
    subject,
    subjects_dir=None,
    orientation: str = "coronal",
    slices=None,
    brain_surfaces=None,
    src=None,
    show: bool = True,
    show_indices: bool = True,
    mri: str = "T1.mgz",
    show_orientation: bool = True,
):
    """Plot BEM contours on anatomical MRI slices.

    Parameters
    ----------

    subject : str
        The FreeSurfer subject name.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    orientation : str
        'coronal' or 'axial' or 'sagittal'.
    slices : list of int | None
        The indices of the MRI slices to plot. If ``None``, automatically
        pick 12 equally-spaced slices.
    brain_surfaces : str | list of str | None
        One or more brain surface to plot (optional). Entries should correspond
        to files in the subject's ``surf`` directory (e.g. ``"white"``).
    src : SourceSpaces | path-like | None
        SourceSpaces instance or path to a source space to plot individual
        sources as scatter-plot. Sources will be shown on exactly one slice
        (whichever slice is closest to each source in the given orientation
        plane). Path can be absolute or relative to the subject's ``bem``
        folder.

        🎭 Changed in version 0.20
           All sources are shown on the nearest slice rather than some
           being omitted.
    show : bool
        Show figure if True.
    show_indices : bool
        Show slice indices if True.

        ✨ Added in version 0.20
    mri : str
        The name of the MRI to use. Can be a standard FreeSurfer MRI such as
        ``'T1.mgz'``, or a full path to a custom MRI file.

        ✨ Added in version 0.21
    show_orientation : bool | str
        Show the orientation (L/R, P/A, I/S) of the data slices.
        True (default) will only show it on the outside most edges of the
        figure, False will never show labels, and "always" will label each
        plot.

        ✨ Added in version 0.21
        🎭 Changed in version 0.24
           Added support for "always".

    Returns
    -------
    fig : instance of matplotlib.figure.Figure
        The figure.

    See Also
    --------
    mne.viz.plot_alignment

    Notes
    -----
    Images are plotted in MRI voxel coordinates.

    If ``src`` is not None, for a given slice index, all source points are
    shown that are halfway between the previous slice and the given slice,
    and halfway between the given slice and the next slice.
    For large slice decimations, this can
    make some source points appear outside the BEM contour, which is shown
    for the given slice index. For example, in the case where the single
    midpoint slice is used ``slices=[128]``, all source points will be shown
    on top of the midpoint MRI slice with the BEM boundary drawn for that
    slice.
    """
    ...

def plot_events(
    events,
    sfreq=None,
    first_samp: int = 0,
    color=None,
    event_id=None,
    axes=None,
    equal_spacing: bool = True,
    show: bool = True,
    on_missing: str = "raise",
    verbose=None,
):
    """Plot :term:`events` to get a visual display of the paradigm.

    Parameters
    ----------

    events : array of int, shape (n_events, 3)
        The array of :term:`events`. The first column contains the event time in
        samples, with :term:`first_samp` included. The third column contains the
        event id.
    sfreq : float | None
        The sample frequency. If None, data will be displayed in samples (not
        seconds).
    first_samp : int
        The index of the first sample. Recordings made on Neuromag systems
        number samples relative to the system start (not relative to the
        beginning of the recording). In such cases the ``raw.first_samp``
        attribute can be passed here. Default is 0.
    color : dict | None
        Dictionary of event_id integers as keys and colors as values. If None,
        colors are automatically drawn from a default list (cycled through if
        number of events longer than list of default colors). Color can be any
        valid `matplotlib color <matplotlib:colors_def>`.
    event_id : dict | None
        Dictionary of event labels (e.g. 'aud_l') as keys and their associated
        event_id values. Labels are used to plot a legend. If None, no legend
        is drawn.
    axes : instance of Axes
       The subplot handle.
    equal_spacing : bool
        Use equal spacing between events in y-axis.
    show : bool
        Show figure if True.

    on_missing : 'raise' | 'warn' | 'ignore'
        Can be ``'raise'`` (default) to raise an error, ``'warn'`` to emit a
        warning, or ``'ignore'`` to ignore when event numbers from ``event_id`` are missing from
        :term:`events`. When numbers from :term:`events` are missing from
        ``event_id`` they will be ignored and a warning emitted; consider
        using ``verbose='error'`` in this case.

        ✨ Added in version 0.21

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    fig : matplotlib.figure.Figure
        The figure object containing the plot.

    Notes
    -----
    ✨ Added in version 0.9.0
    """
    ...

def plot_dipole_amplitudes(dipoles, colors=None, show: bool = True):
    """Plot the amplitude traces of a set of dipoles.

    Parameters
    ----------
    dipoles : list of instance of Dipole
        The dipoles whose amplitudes should be shown.
    colors : list of color | None
        Color to plot with each dipole. If None default colors are used.
    show : bool
        Show figure if True.

    Returns
    -------
    fig : matplotlib.figure.Figure
        The figure object containing the plot.

    Notes
    -----
    ✨ Added in version 0.9.0
    """
    ...

def adjust_axes(axes, remove_spines=("top", "right"), grid: bool = True) -> None:
    """Adjust some properties of axes.

    Parameters
    ----------
    axes : list
        List of axes to process.
    remove_spines : list of str
        Which axis spines to remove.
    grid : bool
        Turn grid on (True) or off (False).
    """
    ...

def plot_filter(
    h,
    sfreq,
    freq=None,
    gain=None,
    title=None,
    color: str = "#1f77b4",
    flim=None,
    fscale: str = "log",
    alim=(-80, 10),
    show: bool = True,
    compensate: bool = False,
    plot=("time", "magnitude", "delay"),
    axes=None,
    *,
    dlim=None,
):
    """Plot properties of a filter.

    Parameters
    ----------
    h : dict or ndarray
        An IIR dict or 1D ndarray of coefficients (for FIR filter).
    sfreq : float
        Sample rate of the data (Hz).
    freq : array-like or None
        The ideal response frequencies to plot (must be in ascending order).
        If None (default), do not plot the ideal response.
    gain : array-like or None
        The ideal response gains to plot.
        If None (default), do not plot the ideal response.
    title : str | None
        The title to use. If None (default), determine the title based
        on the type of the system.
    color : color object
        The color to use (default '#1f77b4').
    flim : tuple or None
        If not None, the x-axis frequency limits (Hz) to use.
        If None, freq will be used. If None (default) and freq is None,
        ``(0.1, sfreq / 2.)`` will be used.
    fscale : str
        Frequency scaling to use, can be "log" (default) or "linear".
    alim : tuple
        The y-axis amplitude limits (dB) to use (default: (-60, 10)).
    show : bool
        Show figure if True (default).
    compensate : bool
        If True, compensate for the filter delay (phase will not be shown).

        - For linear-phase FIR filters, this visualizes the filter coefficients
          assuming that the output will be shifted by ``N // 2``.
        - For IIR filters, this changes the filter coefficient display
          by filtering backward and forward, and the frequency response
          by squaring it.

        ✨ Added in version 0.18
    plot : list | tuple | str
        A list of the requested plots from ``time``, ``magnitude`` and
        ``delay``. Default is to plot all three filter properties
        ('time', 'magnitude', 'delay').

        ✨ Added in version 0.21.0
    axes : instance of Axes | list | None
        The axes to plot to. If list, the list must be a list of Axes of
        the same length as the number of requested plot types. If instance of
        Axes, there must be only one filter property plotted.
        Defaults to ``None``.

        ✨ Added in version 0.21.0
    dlim : None | tuple
        The y-axis delay limits (s) to use (default:
        ``(-tmax / 2., tmax / 2.)``).

        ✨ Added in version 1.1.0

    Returns
    -------
    fig : matplotlib.figure.Figure
        The figure containing the plots.

    See Also
    --------
    mne.filter.create_filter
    plot_ideal_filter

    Notes
    -----
    ✨ Added in version 0.14
    """
    ...

def plot_ideal_filter(
    freq,
    gain,
    axes=None,
    title: str = "",
    flim=None,
    fscale: str = "log",
    alim=(-80, 10),
    color: str = "r",
    alpha: float = 0.5,
    linestyle: str = "--",
    show: bool = True,
):
    """Plot an ideal filter response.

    Parameters
    ----------
    freq : array-like
        The ideal response frequencies to plot (must be in ascending order).
    gain : array-like or None
        The ideal response gains to plot.
    axes : instance of Axes | None
        The subplot handle. With None (default), axes are created.
    title : str
        The title to use, (default: '').
    flim : tuple or None
        If not None, the x-axis frequency limits (Hz) to use.
        If None (default), freq used.
    fscale : str
        Frequency scaling to use, can be "log" (default) or "linear".
    alim : tuple
        If not None (default), the y-axis limits (dB) to use.
    color : color object
        The color to use (default: 'r').
    alpha : float
        The alpha to use (default: 0.5).
    linestyle : str
        The line style to use (default: '--').
    show : bool
        Show figure if True (default).

    Returns
    -------
    fig : instance of matplotlib.figure.Figure
        The figure.

    See Also
    --------
    plot_filter

    Notes
    -----
    ✨ Added in version 0.14

    Examples
    --------
    Plot a simple ideal band-pass filter::

        >>> from mne.viz import plot_ideal_filter
        >>> freq = [0, 1, 40, 50]
        >>> gain = [0, 1, 1, 0]
        >>> plot_ideal_filter(freq, gain, flim=(0.1, 100))  #doctest: +SKIP
        <...Figure...>
    """
    ...

def plot_csd(
    csd,
    info=None,
    mode: str = "csd",
    colorbar: bool = True,
    cmap=None,
    n_cols=None,
    show: bool = True,
):
    """Plot CSD matrices.

    A sub-plot is created for each frequency. If an info object is passed to
    the function, different channel types are plotted in different figures.

    Parameters
    ----------
    csd : instance of CrossSpectralDensity
        The CSD matrix to plot.

    info : mne.Info | None
        The `mne.Info` object with information about the sensors and methods of measurement.
        Used to split the figure by channel-type, if provided.
        By default, the CSD matrix is plotted as a whole.
    mode : 'csd' | 'coh'
        Whether to plot the cross-spectral density ('csd', the default), or
        the coherence ('coh') between the channels.
    colorbar : bool
        Whether to show a colorbar. Defaults to ``True``.
    cmap : str | None
        The matplotlib colormap to use. Defaults to None, which means the
        colormap will default to matplotlib's default.
    n_cols : int | None
        CSD matrices are plotted in a grid. This parameter controls how
        many matrix to plot side by side before starting a new row. By
        default, a number will be chosen to make the grid as square as
        possible.
    show : bool
        Whether to show the figure. Defaults to ``True``.

    Returns
    -------
    fig : list of Figure
        The figures created by this function.
    """
    ...

def plot_chpi_snr(snr_dict, axes=None):
    """Plot time-varying SNR estimates of the HPI coils.

    Parameters
    ----------
    snr_dict : dict
        The dictionary returned by `mne.chpi.compute_chpi_snr`. Must have keys
        ``times``, ``freqs``, ``TYPE_snr``, ``TYPE_power``, and ``TYPE_resid``
        (where ``TYPE`` can be ``mag`` or ``grad`` or both).
    axes : None | list of matplotlib.axes.Axes
        Figure axes in which to draw the SNR, power, and residual plots. The
        number of axes should be 3× the number of MEG sensor types present in
        ``snr_dict``. If ``None`` (the default), a new
        `matplotlib.figure.Figure` is created with the required number of
        axes.

    Returns
    -------
    fig : instance of matplotlib.figure.Figure
        A figure with subplots for SNR, power, and residual variance,
        separately for magnetometers and/or gradiometers (depending on what is
        present in ``snr_dict``).

    Notes
    -----
    If you supply a list of existing `matplotlib.axes.Axes`, then the figure
    legend will not be drawn automatically. If you still want it, running
    ``fig.legend(loc='right', title='cHPI frequencies')`` will recreate it.

    ✨ Added in version 0.24
    """
    ...
