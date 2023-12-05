from .._fiff.meas_info import ContainsMixin as ContainsMixin, Info as Info
from .._fiff.pick import pick_info as pick_info
from ..channels.channels import UpdateChannelsMixin as UpdateChannelsMixin
from ..channels.layout import find_layout as find_layout
from ..utils import (
    GetEpochsMixin as GetEpochsMixin,
    fill_doc as fill_doc,
    legacy as legacy,
    logger as logger,
    object_diff as object_diff,
    repr_html as repr_html,
    warn as warn,
)
from ..utils.check import check_fname as check_fname
from ..viz.topomap import plot_psds_topomap as plot_psds_topomap
from ..viz.utils import plt_show as plt_show
from .multitaper import psd_array_multitaper as psd_array_multitaper
from .psd import psd_array_welch as psd_array_welch
from _typeshed import Incomplete

class SpectrumMixin:
    """Mixin providing spectral plotting methods to sensor-space containers."""

    def plot_psd(
        self,
        fmin: int = 0,
        fmax=...,
        tmin=None,
        tmax=None,
        picks=None,
        proj: bool = False,
        reject_by_annotation: bool = True,
        *,
        method: str = "auto",
        average: bool = False,
        dB: bool = True,
        estimate: str = "auto",
        xscale: str = "linear",
        area_mode: str = "std",
        area_alpha: float = 0.33,
        color: str = "black",
        line_alpha=None,
        spatial_colors: bool = True,
        sphere=None,
        exclude: str = "bads",
        ax=None,
        show: bool = True,
        n_jobs: int = 1,
        verbose=None,
        **method_kw,
    ):
        """⛔️ LEGACY: New code should use .compute_psd().plot().

        Plot power or amplitude spectra.

        Separate plots are drawn for each channel type. When the data have been
        processed with a bandpass, lowpass or highpass filter, dashed lines (╎)
        indicate the boundaries of the filter. The line noise frequency is also
        indicated with a dashed line (⋮). If ``average=False``, the plot will
        be interactive, and click-dragging on the spectrum will generate a
        scalp topography plot for the chosen frequency range in a new figure.

        Parameters
        ----------
        fmin, fmax : float
            The lower- and upper-bound on frequencies of interest. Default is ``fmin=0, fmax=np.inf`` (spans all frequencies present in the data).
        tmin, tmax : float | None
            First and last times to include, in seconds. ``None`` uses the first or
            last time present in the data. Default is ``tmin=None, tmax=None`` (all
            times).
        picks : str | array-like | slice | None
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel *type* strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick good data channels (excluding reference
            MEG channels). Note that channels in ``info['bads']`` *will be included* if
            their names or indices are explicitly provided.
        proj : bool
            Whether to apply SSP projection vectors before spectral estimation.
            Default is ``False``.
        reject_by_annotation : bool
            Whether to omit bad spans of data before spectral estimation. If
            ``True``, spans with annotations whose description begins with
            ``bad`` will be omitted.

        method : ``'welch'`` | ``'multitaper'`` | ``'auto'``
            Spectral estimation method. ``'welch'`` uses Welch's
            method :footcite:p:`Welch1967`, ``'multitaper'`` uses DPSS
            tapers :footcite:p:`Slepian1978`. ``'auto'`` (default) uses Welch's method for continuous data and multitaper for `mne.Epochs` or `mne.Evoked` data.
        average : bool
            If False, the PSDs of all channels is displayed. No averaging
            is done and parameters area_mode and area_alpha are ignored. When
            False, it is possible to paint an area (hold left mouse button and
            drag) to plot a topomap.
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
        xscale : 'linear' | 'log'
            Scale of the frequency axis. Default is ``'linear'``.
        area_mode : str | None
            Mode for plotting area. If 'std', the mean +/- 1 STD (across channels)
            will be plotted. If 'range', the min and max (across channels) will be
            plotted. Bad channels will be excluded from these calculations.
            If None, no area will be plotted. If average=False, no area is plotted.
        area_alpha : float
            Alpha for the area.
        color : str | tuple
            A matplotlib-compatible color to use. Has no effect when
            spatial_colors=True.
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

            ✨ Added in version 0.20
            🎭 Changed in version 1.1 Added ``'eeglab'`` option.

            ✨ Added in version 0.22.0
        exclude : list of str | 'bads'
            Channels names to exclude from being shown. If 'bads', the bad
            channels are excluded. Pass an empty list to plot all channels
            (including channels marked "bad", if any).

            ✨ Added in version 0.24.0
        ax : instance of Axes | list of Axes | None
            The axes to plot to. If ``None``, a new `matplotlib.figure.Figure`
            will be created with the correct number of axes. If `matplotlib.axes.Axes` are provided (either as a single instance or a `list` of axes), the number of axes provided must match the number of channel types present in the object..Default is ``None``.
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
        **method_kw
            Additional keyword arguments passed to the spectral estimation
            function (e.g., ``n_fft, n_overlap, n_per_seg, average, window``
            for Welch method, or
            ``bandwidth, adaptive, low_bias, normalization`` for multitaper
            method). See `mne.time_frequency.psd_array_welch` and
            `mne.time_frequency.psd_array_multitaper` for details.

        Returns
        -------
        fig : instance of Figure
            Figure with frequency spectra of the data channels.

        Notes
        -----
        This method exists to support legacy code; for new code the preferred
        idiom is ``inst.compute_psd().plot()`` (where ``inst`` is an instance
        of `mne.io.Raw`, `mne.Epochs`, or `mne.Evoked`).
        """
        ...

    def plot_psd_topo(
        self,
        tmin=None,
        tmax=None,
        fmin: int = 0,
        fmax: int = 100,
        proj: bool = False,
        *,
        method: str = "auto",
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
        **method_kw,
    ):
        """⛔️ LEGACY: New code should use .compute_psd().plot_topo().

        Plot power spectral density, separately for each channel.

        Parameters
        ----------
        tmin, tmax : float | None
            First and last times to include, in seconds. ``None`` uses the first or
            last time present in the data. Default is ``tmin=None, tmax=None`` (all
            times).
        fmin, fmax : float
            The lower- and upper-bound on frequencies of interest. Default is ``fmin=0, fmax=100``.
        proj : bool
            Whether to apply SSP projection vectors before spectral estimation.
            Default is ``False``.

        method : ``'welch'`` | ``'multitaper'`` | ``'auto'``
            Spectral estimation method. ``'welch'`` uses Welch's
            method :footcite:p:`Welch1967`, ``'multitaper'`` uses DPSS
            tapers :footcite:p:`Slepian1978`. ``'auto'`` (default) uses Welch's method for continuous data and multitaper for `mne.Epochs` or `mne.Evoked` data.
        dB : bool
            Whether to plot on a decibel-like scale. If ``True``, plots
            10 × log₁₀(spectral power). Ignored if ``normalize=True``.
        layout : instance of Layout | None
            Layout instance specifying sensor positions (does not need to be
            specified for Neuromag data). If ``None`` (default), the layout is
            inferred from the data.
        color : str | tuple
            A matplotlib-compatible color to use for the curves. Defaults to
            white.
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
            May not work on all systems / platforms. Defaults to ``False``.
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
        **method_kw
            Additional keyword arguments passed to the spectral estimation
            function (e.g., ``n_fft, n_overlap, n_per_seg, average, window``
            for Welch method, or
            ``bandwidth, adaptive, low_bias, normalization`` for multitaper
            method). See `mne.time_frequency.psd_array_welch` and
            `mne.time_frequency.psd_array_multitaper` for details. Defaults to ``dict(n_fft=2048)``.

        Returns
        -------
        fig : instance of matplotlib.figure.Figure
            Figure distributing one image per channel across sensor topography.
        """
        ...

    def plot_psd_topomap(
        self,
        bands=None,
        tmin=None,
        tmax=None,
        ch_type=None,
        *,
        proj: bool = False,
        method: str = "auto",
        normalize: bool = False,
        agg_fun=None,
        dB: bool = False,
        sensors: bool = True,
        show_names: bool = False,
        mask=None,
        mask_params=None,
        contours: int = 0,
        outlines: str = "head",
        sphere=None,
        image_interp="cubic",
        extrapolate="auto",
        border="mean",
        res: int = 64,
        size: int = 1,
        cmap=None,
        vlim=(None, None),
        cnorm=None,
        colorbar: bool = True,
        cbar_fmt: str = "auto",
        units=None,
        axes=None,
        show: bool = True,
        n_jobs=None,
        verbose=None,
        **method_kw,
    ):
        """⛔️ LEGACY: New code should use .compute_psd().plot_topomap().

        Plot scalp topography of PSD for chosen frequency bands.

        Parameters
        ----------

        bands : None | dict | list of tuple
            The frequencies or frequency ranges to plot. If a `dict`, keys will
            be used as subplot titles and values should be either a single frequency
            (e.g., ``{'presentation rate': 6.5}``) or a length-two sequence of lower
            and upper frequency band edges (e.g., ``{'theta': (4, 8)}``). If a single
            frequency is provided, the plot will show the frequency bin that is closest
            to the requested value. If ``None`` (the default), expands to::

                bands = {'Delta (0-4 Hz)': (0, 4), 'Theta (4-8 Hz)': (4, 8),
                         'Alpha (8-12 Hz)': (8, 12), 'Beta (12-30 Hz)': (12, 30),
                         'Gamma (30-45 Hz)': (30, 45)}

            💡
               For backwards compatibility, `tuples<tuple>` of length 2 or 3 are
               also accepted, where the last element of the tuple is the subplot title
               and the other entries are frequency values (a single value or band
               edges). New code should use `dict` or ``None``.

            🎭 Changed in version 1.2
               Allow passing a dict and discourage passing tuples.
        tmin, tmax : float | None
            First and last times to include, in seconds. ``None`` uses the first or
            last time present in the data. Default is ``tmin=None, tmax=None`` (all
            times).
        ch_type : 'mag' | 'grad' | 'planar1' | 'planar2' | 'eeg' | None
            The channel type to plot. For ``'grad'``, the gradiometers are
            collected in pairs and the mean for each pair is plotted. If
            ``None`` the first available channel type from order shown above is used. Defaults to ``None``.
        proj : bool
            Whether to apply SSP projection vectors before spectral estimation.
            Default is ``False``.

        method : ``'welch'`` | ``'multitaper'`` | ``'auto'``
            Spectral estimation method. ``'welch'`` uses Welch's
            method :footcite:p:`Welch1967`, ``'multitaper'`` uses DPSS
            tapers :footcite:p:`Slepian1978`. ``'auto'`` (default) uses Welch's method for continuous data and multitaper for `mne.Epochs` or `mne.Evoked` data.

        normalize : bool
            If True, each band will be divided by the total power. Defaults to
            False.

        agg_fun : callable
            The function used to aggregate over frequencies. Defaults to
            `numpy.sum` if ``normalize=True``, else `numpy.mean`.
        dB : bool
            Whether to plot on a decibel-like scale. If ``True``, plots
            10 × log₁₀(spectral power) following the application of ``agg_fun``. Ignored if ``normalize=True``.

        sensors : bool | str
            Whether to add markers for sensor locations. If `str`, should be a
            valid matplotlib format string (e.g., ``'r+'`` for red plusses, see the
            Notes section of `matplotlib.axes.Axes.plot`). If ``True`` (the
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
            of a spherical `mne.bem.ConductorModel` to use the origin and
            radius from that object. If ``'auto'`` the sphere is fit to digitization
            points. If ``'eeglab'`` the head circle is defined by EEG electrodes
            ``'Fpz'``, ``'Oz'``, ``'T7'``, and ``'T8'`` (if ``'Fpz'`` is not present,
            it will be approximated from the coordinates of ``'Oz'``). ``None`` (the
            default) is equivalent to ``'auto'`` when enough extra digitization points
            are available, and (0, 0, 0, 0.095) otherwise.

            ✨ Added in version 0.20
            🎭 Changed in version 1.1 Added ``'eeglab'`` option.

        image_interp : str
            The image interpolation to be used. Options are ``'cubic'`` (default)
            to use `scipy.interpolate.CloughTocher2DInterpolator`,
            ``'nearest'`` to use `scipy.spatial.Voronoi` or
            ``'linear'`` to use `scipy.interpolate.LinearNDInterpolator`.

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

        border : float | 'mean'
            Value to extrapolate to on the topomap borders. If ``'mean'`` (default),
            then each extrapolated point has the average value of its neighbours.

        res : int
            The resolution of the topomap image (number of pixels along each side).

        size : float
            Side length of each subplot in inches.

        cmap : matplotlib colormap | (colormap, bool) | 'interactive' | None
            Colormap to use. If `tuple`, the first value indicates the colormap
            to use and the second value is a boolean defining interactivity. In
            interactive mode the colors are adjustable by clicking and dragging the
            colorbar with left and right mouse button. Left mouse button moves the
            scale up and down and right mouse button adjusts the range. Hitting
            space bar resets the range. Up and down arrows can be used to change
            the colormap. If ``None``, ``'Reds'`` is used for data that is either
            all-positive or all-negative, and ``'RdBu_r'`` is used otherwise.
            ``'interactive'`` is equivalent to ``(None, True)``. Defaults to ``None``.

            ⛔️  Interactive mode works smoothly only for a small amount
                of topomaps. Interactive mode is disabled by default for more than
                2 topomaps.

        vlim : tuple of length 2 | 'joint'
            Colormap limits to use. If a `tuple` of floats, specifies the
            lower and upper bounds of the colormap (in that order); providing
            ``None`` for either entry will set the corresponding boundary at the
            min/max of the data (separately for each topomap). Elements of the `tuple` may also be callable functions which take in a `NumPy array <numpy.ndarray>` and return a scalar. If ``vlim='joint'``, will compute the colormap limits jointly across all topomaps of the same channel type, using the min/max of the data for that channel type. Defaults to ``(None, None)``.

        cnorm : matplotlib.colors.Normalize | None
            How to normalize the colormap. If ``None``, standard linear normalization
            is performed. If not ``None``, ``vmin`` and ``vmax`` will be ignored.
            See `Matplotlib docs <matplotlib:colormapnorms>`
            for more details on colormap normalization, and
            `the ERDs example<cnorm-example>` for an example of its use.

            ✨ Added in version 1.2

        colorbar : bool
            Plot a colorbar in the rightmost column of the figure.
        cbar_fmt : str
            Formatting string for colorbar tick labels. See `formatspec` for
            details.
            If ``'auto'``, is equivalent to '%0.3f' if ``dB=False`` and '%0.1f' if
            ``dB=True``. Defaults to ``'auto'``.

        units : str | None
            The units to use for the colorbar label. Ignored if ``colorbar=False``.
            If ``None`` the label will be "AU" indicating arbitrary units.
            Default is ``None``.
        axes : instance of Axes | list of Axes | None
            The axes to plot to. If ``None``, a new `matplotlib.figure.Figure`
            will be created with the correct number of axes. If `matplotlib.axes.Axes` are provided (either as a single instance or a `list` of axes), the number of axes provided must match the length of ``bands``.Default is ``None``.
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
        **method_kw
            Additional keyword arguments passed to the spectral estimation
            function (e.g., ``n_fft, n_overlap, n_per_seg, average, window``
            for Welch method, or
            ``bandwidth, adaptive, low_bias, normalization`` for multitaper
            method). See `mne.time_frequency.psd_array_welch` and
            `mne.time_frequency.psd_array_multitaper` for details.

        Returns
        -------
        fig : instance of Figure
            Figure showing one scalp topography per frequency band.
        """
        ...

class BaseSpectrum(ContainsMixin, UpdateChannelsMixin):
    """Base class for Spectrum and EpochsSpectrum."""

    inst: Incomplete
    info: Incomplete
    preload: bool

    def __init__(
        self,
        inst,
        method,
        fmin,
        fmax,
        tmin,
        tmax,
        picks,
        exclude,
        proj,
        remove_dc,
        *,
        n_jobs,
        verbose=None,
        **method_kw,
    ) -> None: ...
    def __eq__(self, other):
        """Test equivalence of two Spectrum instances."""
        ...

    @property
    def ch_names(self): ...
    @property
    def freqs(self): ...
    @property
    def method(self): ...
    @property
    def sfreq(self): ...
    @property
    def shape(self): ...
    def copy(self):
        """Return copy of the Spectrum instance.

        Returns
        -------
        spectrum : instance of Spectrum
            A copy of the object.
        """
        ...

    def get_data(
        self,
        picks=None,
        exclude: str = "bads",
        fmin: int = 0,
        fmax=...,
        return_freqs: bool = False,
    ):
        """Get spectrum data in NumPy array format.

        Parameters
        ----------
        picks : str | array-like | slice | None
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel *type* strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick good data channels (excluding reference
            MEG channels). Note that channels in ``info['bads']`` *will be included* if
            their names or indices are explicitly provided.
        exclude : list of str | 'bads'
            Channel names to exclude. If ``'bads'``, channels
            in ``spectrum.info['bads']`` are excluded; pass an empty list to
            include all channels (including "bad" channels, if any).
        fmin, fmax : float
            The lower- and upper-bound on frequencies of interest. Default is ``fmin=0, fmax=np.inf`` (spans all frequencies present in the data).
        return_freqs : bool
            Whether to return the frequency bin values for the requested
            frequency range. Default is ``False``.

        Returns
        -------
        data : array
            The requested data in a NumPy array.
        freqs : array
            The frequency values for the requested range. Only returned if
            ``return_freqs`` is ``True``.
        """
        ...

    def plot(
        self,
        *,
        picks=None,
        average: bool = False,
        dB: bool = True,
        amplitude: str = "auto",
        xscale: str = "linear",
        ci: str = "sd",
        ci_alpha: float = 0.3,
        color: str = "black",
        alpha=None,
        spatial_colors: bool = True,
        sphere=None,
        exclude=(),
        axes=None,
        show: bool = True,
    ):
        """Plot power or amplitude spectra.

        Separate plots are drawn for each channel type. When the data have been
        processed with a bandpass, lowpass or highpass filter, dashed lines (╎)
        indicate the boundaries of the filter. The line noise frequency is also
        indicated with a dashed line (⋮). If ``average=False``, the plot will
        be interactive, and click-dragging on the spectrum will generate a
        scalp topography plot for the chosen frequency range in a new figure.

        Parameters
        ----------
        picks : str | array-like | slice | None
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel *type* strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick all data channels (excluding reference
            MEG channels). Note that channels in ``info['bads']`` *will be included* if
            their names or indices are explicitly provided.

            🎭 Changed in version 1.5
                In version 1.5, the default behavior changed so that all
                :term:`data channels` (not just "good" data channels) are shown
                by default.
        average : bool
            Whether to average across channels before plotting. If ``True``,
            interactive plotting of scalp topography is disabled, and
            parameters ``ci`` and ``ci_alpha`` control the style of the
            confidence band around the mean. Default is ``False``.
        dB : bool
            Whether to plot on a decibel-like scale. If ``True``, plots
            10 × log₁₀(spectral power).
        amplitude : bool | 'auto'
            Whether to plot an amplitude spectrum (``True``) or power spectrum
            (``False``). If ``'auto'``, will plot a power spectrum when
            ``dB=True`` and an amplitude spectrum otherwise. Default is
            ``'auto'``.
        xscale : 'linear' | 'log'
            Scale of the frequency axis. Default is ``'linear'``.
        ci : float | 'sd' | 'range' | None
            Type of confidence band drawn around the mean when
            ``average=True``. If ``'sd'`` the band spans ±1 standard deviation
            across channels. If ``'range'`` the band spans the range across
            channels at each frequency. If a `float`, it indicates the
            (bootstrapped) confidence interval to display, and must satisfy
            ``0 < ci <= 100``. If ``None``, no band is drawn. Default is
            ``sd``.
        ci_alpha : float
            Opacity of the confidence band. Must satisfy
            ``0 <= ci_alpha <= 1``. Default is 0.3.
        color : str | tuple
            A matplotlib-compatible color to use. Has no effect when
            spatial_colors=True.
        alpha : float | None
            Opacity of the spectrum line(s). If `float`, must satisfy
            ``0 <= alpha <= 1``. If ``None``, opacity will be ``1`` when
            ``average=True`` and ``0.1`` when ``average=False``. Default is
            ``None``.
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

            ✨ Added in version 0.20
            🎭 Changed in version 1.1 Added ``'eeglab'`` option.
        exclude : list of str | 'bads'
            Channel names to exclude from being drawn. If ``'bads'``, channels
            in ``spectrum.info['bads']`` are excluded; pass an empty list to
            include all channels (including "bad" channels, if any).

            🎭 Changed in version 1.5
                In version 1.5, the default behavior changed from
                ``exclude='bads'`` to ``exclude=()``.
        axes : instance of Axes | list of Axes | None
            The axes to plot to. If ``None``, a new `matplotlib.figure.Figure`
            will be created with the correct number of axes. If `matplotlib.axes.Axes` are provided (either as a single instance or a `list` of axes), the number of axes provided must match the length of ``bands``.Default is ``None``.
        show : bool
            Show the figure if ``True``.

        Returns
        -------
        fig : instance of matplotlib.figure.Figure
            Figure with spectra plotted in separate subplots for each channel
            type.
        """
        ...

    def plot_topo(
        self,
        *,
        dB: bool = True,
        layout=None,
        color: str = "w",
        fig_facecolor: str = "k",
        axis_facecolor: str = "k",
        axes=None,
        block: bool = False,
        show: bool = True,
    ):
        """Plot power spectral density, separately for each channel.

        Parameters
        ----------
        dB : bool
            Whether to plot on a decibel-like scale. If ``True``, plots
            10 × log₁₀(spectral power). Ignored if ``normalize=True``.
        layout : instance of Layout | None
            Layout instance specifying sensor positions (does not need to be
            specified for Neuromag data). If ``None`` (default), the layout is
            inferred from the data.
        color : str | tuple
            A matplotlib-compatible color to use for the curves. Defaults to
            white.
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
            May not work on all systems / platforms. Defaults to ``False``.
        show : bool
            Show the figure if ``True``.

        Returns
        -------
        fig : instance of matplotlib.figure.Figure
            Figure distributing one image per channel across sensor topography.
        """
        ...

    def plot_topomap(
        self,
        bands=None,
        ch_type=None,
        *,
        normalize: bool = False,
        agg_fun=None,
        dB: bool = False,
        sensors: bool = True,
        show_names: bool = False,
        mask=None,
        mask_params=None,
        contours: int = 6,
        outlines: str = "head",
        sphere=None,
        image_interp="cubic",
        extrapolate="auto",
        border="mean",
        res: int = 64,
        size: int = 1,
        cmap=None,
        vlim=(None, None),
        cnorm=None,
        colorbar: bool = True,
        cbar_fmt: str = "auto",
        units=None,
        axes=None,
        show: bool = True,
    ):
        """Plot scalp topography of PSD for chosen frequency bands.

        Parameters
        ----------

        bands : None | dict | list of tuple
            The frequencies or frequency ranges to plot. If a `dict`, keys will
            be used as subplot titles and values should be either a single frequency
            (e.g., ``{'presentation rate': 6.5}``) or a length-two sequence of lower
            and upper frequency band edges (e.g., ``{'theta': (4, 8)}``). If a single
            frequency is provided, the plot will show the frequency bin that is closest
            to the requested value. If ``None`` (the default), expands to::

                bands = {'Delta (0-4 Hz)': (0, 4), 'Theta (4-8 Hz)': (4, 8),
                         'Alpha (8-12 Hz)': (8, 12), 'Beta (12-30 Hz)': (12, 30),
                         'Gamma (30-45 Hz)': (30, 45)}

            💡
               For backwards compatibility, `tuples<tuple>` of length 2 or 3 are
               also accepted, where the last element of the tuple is the subplot title
               and the other entries are frequency values (a single value or band
               edges). New code should use `dict` or ``None``.

            🎭 Changed in version 1.2
               Allow passing a dict and discourage passing tuples.
        ch_type : 'mag' | 'grad' | 'planar1' | 'planar2' | 'eeg' | None
            The channel type to plot. For ``'grad'``, the gradiometers are
            collected in pairs and the mean for each pair is plotted. If
            ``None`` the first available channel type from order shown above is used. Defaults to ``None``.

        normalize : bool
            If True, each band will be divided by the total power. Defaults to
            False.

        agg_fun : callable
            The function used to aggregate over frequencies. Defaults to
            `numpy.sum` if ``normalize=True``, else `numpy.mean`.
        dB : bool
            Whether to plot on a decibel-like scale. If ``True``, plots
            10 × log₁₀(spectral power) following the application of ``agg_fun``. Ignored if ``normalize=True``.

        sensors : bool | str
            Whether to add markers for sensor locations. If `str`, should be a
            valid matplotlib format string (e.g., ``'r+'`` for red plusses, see the
            Notes section of `matplotlib.axes.Axes.plot`). If ``True`` (the
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
            of a spherical `mne.bem.ConductorModel` to use the origin and
            radius from that object. If ``'auto'`` the sphere is fit to digitization
            points. If ``'eeglab'`` the head circle is defined by EEG electrodes
            ``'Fpz'``, ``'Oz'``, ``'T7'``, and ``'T8'`` (if ``'Fpz'`` is not present,
            it will be approximated from the coordinates of ``'Oz'``). ``None`` (the
            default) is equivalent to ``'auto'`` when enough extra digitization points
            are available, and (0, 0, 0, 0.095) otherwise.

            ✨ Added in version 0.20
            🎭 Changed in version 1.1 Added ``'eeglab'`` option.

        image_interp : str
            The image interpolation to be used. Options are ``'cubic'`` (default)
            to use `scipy.interpolate.CloughTocher2DInterpolator`,
            ``'nearest'`` to use `scipy.spatial.Voronoi` or
            ``'linear'`` to use `scipy.interpolate.LinearNDInterpolator`.

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

        border : float | 'mean'
            Value to extrapolate to on the topomap borders. If ``'mean'`` (default),
            then each extrapolated point has the average value of its neighbours.

        res : int
            The resolution of the topomap image (number of pixels along each side).

        size : float
            Side length of each subplot in inches.

        cmap : matplotlib colormap | (colormap, bool) | 'interactive' | None
            Colormap to use. If `tuple`, the first value indicates the colormap
            to use and the second value is a boolean defining interactivity. In
            interactive mode the colors are adjustable by clicking and dragging the
            colorbar with left and right mouse button. Left mouse button moves the
            scale up and down and right mouse button adjusts the range. Hitting
            space bar resets the range. Up and down arrows can be used to change
            the colormap. If ``None``, ``'Reds'`` is used for data that is either
            all-positive or all-negative, and ``'RdBu_r'`` is used otherwise.
            ``'interactive'`` is equivalent to ``(None, True)``. Defaults to ``None``.

            ⛔️  Interactive mode works smoothly only for a small amount
                of topomaps. Interactive mode is disabled by default for more than
                2 topomaps.

        vlim : tuple of length 2 | 'joint'
            Colormap limits to use. If a `tuple` of floats, specifies the
            lower and upper bounds of the colormap (in that order); providing
            ``None`` for either entry will set the corresponding boundary at the
            min/max of the data (separately for each topomap). Elements of the `tuple` may also be callable functions which take in a `NumPy array <numpy.ndarray>` and return a scalar. If ``vlim='joint'``, will compute the colormap limits jointly across all topomaps of the same channel type, using the min/max of the data for that channel type. Defaults to ``(None, None)``.

        cnorm : matplotlib.colors.Normalize | None
            How to normalize the colormap. If ``None``, standard linear normalization
            is performed. If not ``None``, ``vmin`` and ``vmax`` will be ignored.
            See `Matplotlib docs <matplotlib:colormapnorms>`
            for more details on colormap normalization, and
            `the ERDs example<cnorm-example>` for an example of its use.

        colorbar : bool
            Plot a colorbar in the rightmost column of the figure.
        cbar_fmt : str
            Formatting string for colorbar tick labels. See `formatspec` for
            details.
            If ``'auto'``, is equivalent to '%0.3f' if ``dB=False`` and '%0.1f' if
            ``dB=True``. Defaults to ``'auto'``.

        units : str | None
            The units to use for the colorbar label. Ignored if ``colorbar=False``.
            If ``None`` the label will be "AU" indicating arbitrary units.
            Default is ``None``.
        axes : instance of Axes | list of Axes | None
            The axes to plot to. If ``None``, a new `matplotlib.figure.Figure`
            will be created with the correct number of axes. If `matplotlib.axes.Axes` are provided (either as a single instance or a `list` of axes), the number of axes provided must match the length of ``bands``.Default is ``None``.
        show : bool
            Show the figure if ``True``.

        Returns
        -------
        fig : instance of Figure
            Figure showing one scalp topography per frequency band.
        """
        ...

    def save(self, fname, *, overwrite: bool = False, verbose=None) -> None:
        """Save spectrum data to disk (in HDF5 format).

        Parameters
        ----------
        fname : path-like
            Path of file to save to.

        overwrite : bool
            If True (default False), overwrite the destination file if it
            exists.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        See Also
        --------
        mne.time_frequency.read_spectrum
        """
        ...

    def to_data_frame(
        self,
        picks=None,
        index=None,
        copy: bool = True,
        long_format: bool = False,
        *,
        verbose=None,
    ):
        """Export data in tabular structure as a pandas DataFrame.

        Channels are converted to columns in the DataFrame. By default,
        an additional column "freq" is added, unless ``index='freq'``
        (in which case frequency values form the DataFrame's index).

        Parameters
        ----------
        picks : str | array-like | slice | None
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel *type* strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick all channels. Note that channels in
            ``info['bads']`` *will be included* if their names or indices are
            explicitly provided.
        index : str | list of str | None
            Kind of index to use for the DataFrame. If ``None``, a sequential
            integer index (`pandas.RangeIndex`) will be used. If a
            `str`, a `pandas.Index` will be used (see Notes). If
            a list of two or more string values, a `pandas.MultiIndex`
            will be used. Defaults to ``None``.

        copy : bool
            If ``True``, data will be copied. Otherwise data may be modified in place.
            Defaults to ``True``.

        long_format : bool
            If True, the DataFrame is returned in long format where each row is one
            observation of the signal at a unique combination of frequency and channel.
            For convenience, a ``ch_type`` column is added to facilitate subsetting the resulting DataFrame. Defaults to ``False``.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------

        df : instance of pandas.DataFrame
            A dataframe suitable for usage with other statistical/plotting/analysis
            packages.

        Notes
        -----
        Valid values for ``index`` depend on whether the Spectrum was created
        from continuous data (`mne.io.Raw`, `mne.Evoked`) or
        discontinuous data (`mne.Epochs`). For continuous data, only
        ``None`` or ``'freq'`` is supported. For discontinuous data, additional
        valid values are ``'epoch'`` and ``'condition'``, or a `list`
        comprising some of the valid string values (e.g.,
        ``['freq', 'epoch']``).
        """
        ...

    def units(self, latex: bool = False):
        """Get the spectrum units for each channel type.

        Parameters
        ----------
        latex : bool
            Whether to format the unit strings as LaTeX. Default is ``False``.

        Returns
        -------
        units : dict
            Mapping from channel type to a string representation of the units
            for that channel type.
        """
        ...

class Spectrum(BaseSpectrum):
    """Data object for spectral representations of continuous data.

    ⛔️ The preferred means of creating Spectrum objects from
                 continuous or averaged data is via the instance methods
                 `mne.io.Raw.compute_psd` or
                 `mne.Evoked.compute_psd`. Direct class instantiation
                 is not supported.

    Parameters
    ----------
    inst : instance of Raw or Evoked
        The data from which to compute the frequency spectrum.

    method : ``'welch'`` | ``'multitaper'`` | ``'auto'``
        Spectral estimation method. ``'welch'`` uses Welch's
        method :footcite:p:`Welch1967`, ``'multitaper'`` uses DPSS
        tapers :footcite:p:`Slepian1978`.
        ``'auto'`` (default) uses Welch's method for continuous data
        and multitaper for `mne.Evoked` data.
    fmin, fmax : float
        The lower- and upper-bound on frequencies of interest. Default is ``fmin=0, fmax=np.inf`` (spans all frequencies present in the data).
    tmin, tmax : float | None
        First and last times to include, in seconds. ``None`` uses the first or
        last time present in the data. Default is ``tmin=None, tmax=None`` (all
        times).
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick good data channels (excluding reference
        MEG channels). Note that channels in ``info['bads']`` *will be included* if
        their names or indices are explicitly provided.
    exclude : list of str | 'bads'
        Channel names to exclude. If ``'bads'``, channels
        in ``info['bads']`` are excluded; pass an empty list to
        include all channels (including "bad" channels, if any).
    proj : bool
        Whether to apply SSP projection vectors before spectral estimation.
        Default is ``False``.

    remove_dc : bool
        If ``True``, the mean is subtracted from each segment before computing
        its spectrum.
    reject_by_annotation : bool
        Whether to omit bad spans of data before spectral estimation. If
        ``True``, spans with annotations whose description begins with
        ``bad`` will be omitted.
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
    **method_kw
        Additional keyword arguments passed to the spectral estimation
        function (e.g., ``n_fft, n_overlap, n_per_seg, average, window``
        for Welch method, or
        ``bandwidth, adaptive, low_bias, normalization`` for multitaper
        method). See `mne.time_frequency.psd_array_welch` and
        `mne.time_frequency.psd_array_multitaper` for details.

    Attributes
    ----------
    ch_names : list
        The channel names.
    freqs : array
        Frequencies at which the amplitude, power, or fourier coefficients
        have been computed.

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    method : str
        The method used to compute the spectrum (``'welch'`` or
        ``'multitaper'``).

    See Also
    --------
    EpochsSpectrum
    SpectrumArray
    mne.io.Raw.compute_psd
    mne.Epochs.compute_psd
    mne.Evoked.compute_psd

    References
    ----------
    .. footbibliography::
    """

    def __init__(
        self,
        inst,
        method,
        fmin,
        fmax,
        tmin,
        tmax,
        picks,
        exclude,
        proj,
        remove_dc,
        reject_by_annotation,
        *,
        n_jobs,
        verbose=None,
        **method_kw,
    ) -> None: ...
    def __getitem__(self, item):
        """Get Spectrum data.

        Parameters
        ----------
        item : int | slice | array-like
            Indexing is similar to a `NumPy array<numpy.ndarray>`; see
            Notes.

        Returns
        -------
        %(getitem_spectrum_return)s

        Notes
        -----
        Integer-, list-, and slice-based indexing is possible:

        - ``spectrum[0]`` gives all frequency bins in the first channel
        - ``spectrum[:3]`` gives all frequency bins in the first 3 channels
        - ``spectrum[[0, 2], 5]`` gives the value in the sixth frequency bin of
          the first and third channels
        - ``spectrum[(4, 7)]`` is the same as ``spectrum[4, 7]``.

        💡

           Unlike `mne.io.Raw` objects (which returns a tuple of the
           requested data values and the corresponding times), accessing
           `mne.time_frequency.Spectrum` values via subscript does
           **not** return the corresponding frequency bin values. If you need
           them, use ``spectrum.freqs[freq_indices]``.
        """
        ...

class SpectrumArray(Spectrum):
    """Data object for precomputed spectral data (in NumPy array format).

    Parameters
    ----------
    data : array, shape (n_channels, n_freqs)
        The power spectral density for each channel.

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.

    freqs : array of float, shape (n_freqs,)
        The frequencies of interest in Hz.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    mne.create_info
    mne.EvokedArray
    mne.io.RawArray
    EpochsSpectrumArray

    Notes
    -----

    It is assumed that the data passed in represent spectral *power* (not amplitude,
    phase, model coefficients, etc) and downstream methods (such as
    `mne.time_frequency.SpectrumArray.plot`) assume power data. If you pass in
    something other than power, at the very least axis labels will be inaccurate (and
    other things may also not work or be incorrect).

        ✨ Added in version 1.6
    """

    def __init__(self, data, info, freqs, *, verbose=None) -> None: ...

class EpochsSpectrum(BaseSpectrum, GetEpochsMixin):
    """Data object for spectral representations of epoched data.

    ⛔️ The preferred means of creating Spectrum objects from Epochs
                 is via the instance method `mne.Epochs.compute_psd`.
                 Direct class instantiation is not supported.

    Parameters
    ----------
    inst : instance of Epochs
        The data from which to compute the frequency spectrum.

    method : ``'welch'`` | ``'multitaper'``
        Spectral estimation method. ``'welch'`` uses Welch's
        method :footcite:p:`Welch1967`, ``'multitaper'`` uses DPSS
        tapers :footcite:p:`Slepian1978`.
    fmin, fmax : float
        The lower- and upper-bound on frequencies of interest. Default is ``fmin=0, fmax=np.inf`` (spans all frequencies present in the data).
    tmin, tmax : float | None
        First and last times to include, in seconds. ``None`` uses the first or
        last time present in the data. Default is ``tmin=None, tmax=None`` (all
        times).
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick good data channels (excluding reference
        MEG channels). Note that channels in ``info['bads']`` *will be included* if
        their names or indices are explicitly provided.
    exclude : list of str | 'bads'
        Channel names to exclude. If ``'bads'``, channels
        in ``info['bads']`` are excluded; pass an empty list to
        include all channels (including "bad" channels, if any).
    proj : bool
        Whether to apply SSP projection vectors before spectral estimation.
        Default is ``False``.

    remove_dc : bool
        If ``True``, the mean is subtracted from each segment before computing
        its spectrum.
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
    **method_kw
        Additional keyword arguments passed to the spectral estimation
        function (e.g., ``n_fft, n_overlap, n_per_seg, average, window``
        for Welch method, or
        ``bandwidth, adaptive, low_bias, normalization`` for multitaper
        method). See `mne.time_frequency.psd_array_welch` and
        `mne.time_frequency.psd_array_multitaper` for details.

    Attributes
    ----------
    ch_names : list
        The channel names.
    freqs : array
        Frequencies at which the amplitude, power, or fourier coefficients
        have been computed.

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    method : str
        The method used to compute the spectrum ('welch' or 'multitaper').

    See Also
    --------
    EpochsSpectrumArray
    Spectrum
    mne.Epochs.compute_psd

    References
    ----------
    .. footbibliography::
    """

    event_id: Incomplete
    events: Incomplete
    selection: Incomplete
    drop_log: Incomplete

    def __init__(
        self,
        inst,
        method,
        fmin,
        fmax,
        tmin,
        tmax,
        picks,
        exclude,
        proj,
        remove_dc,
        *,
        n_jobs,
        verbose=None,
        **method_kw,
    ) -> None: ...
    def __getitem__(self, item):
        """Subselect epochs from an EpochsSpectrum.

        Parameters
        ----------
        item : int | slice | array-like | str
            Access options are the same as for `mne.Epochs` objects,
            see the docstring of `mne.Epochs.__getitem__` for
            explanation.

        Returns
        -------
        %(getitem_epochspectrum_return)s
        """
        ...

    def average(self, method: str = "mean"):
        """Average the spectra across epochs.

        Parameters
        ----------
        method : 'mean' | 'median' | callable
            How to aggregate spectra across epochs. If callable, must take a
            `NumPy array<numpy.ndarray>` of shape
            ``(n_epochs, n_channels, n_freqs)`` and return an array of shape
            ``(n_channels, n_freqs)``. Default is ``'mean'``.

        Returns
        -------
        spectrum : instance of Spectrum
            The aggregated spectrum object.
        """
        ...

class EpochsSpectrumArray(EpochsSpectrum):
    """Data object for precomputed epoched spectral data (in NumPy array format).

    Parameters
    ----------
    data : array, shape (n_epochs, n_channels, n_freqs)
        The power spectral density for each channel in each epoch.

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.

    freqs : array of float, shape (n_freqs,)
        The frequencies of interest in Hz.

    events : array of int, shape (n_events, 3)
        The array of :term:`events`. The first column contains the event time in
        samples, with :term:`first_samp` included. The third column contains the
        event id.
        If some events don't match the events of interest as specified by
        ``event_id``, they will be marked as ``IGNORED`` in the drop log.

    event_id : int | list of int | dict | None
        The id of the :term:`events` to consider. If dict, the keys can later be
        used to access associated :term:`events`. Example:
        dict(auditory=1, visual=3). If int, a dict will be created with the id as
        string. If a list, all :term:`events` with the IDs specified in the list
        are used. If None, all :term:`events` will be used and a dict is created
        with string integer names corresponding to the event id integers.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    mne.create_info
    mne.EpochsArray
    SpectrumArray

    Notes
    -----

    It is assumed that the data passed in represent spectral *power* (not amplitude,
    phase, model coefficients, etc) and downstream methods (such as
    `mne.time_frequency.SpectrumArray.plot`) assume power data. If you pass in
    something other than power, at the very least axis labels will be inaccurate (and
    other things may also not work or be incorrect).

        ✨ Added in version 1.6
    """

    def __init__(
        self, data, info, freqs, events=None, event_id=None, *, verbose=None
    ) -> None: ...

def read_spectrum(fname):
    """Load a `mne.time_frequency.Spectrum` object from disk.

    Parameters
    ----------
    fname : path-like
        Path to a spectrum file in HDF5 format.

    Returns
    -------
    spectrum : instance of Spectrum
        The loaded Spectrum object.

    See Also
    --------
    mne.time_frequency.Spectrum.save
    """
    ...
