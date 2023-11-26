from ._fiff.constants import FIFF as FIFF
from ._fiff.meas_info import (
    ContainsMixin as ContainsMixin,
    SetChannelsMixin as SetChannelsMixin,
    read_meas_info as read_meas_info,
    write_meas_info as write_meas_info,
)
from ._fiff.open import fiff_open as fiff_open
from ._fiff.pick import pick_types as pick_types
from ._fiff.proj import ProjMixin as ProjMixin
from ._fiff.tag import read_tag as read_tag
from ._fiff.tree import dir_tree_find as dir_tree_find
from ._fiff.write import (
    end_block as end_block,
    start_and_end_file as start_and_end_file,
    start_block as start_block,
    write_complex_float_matrix as write_complex_float_matrix,
    write_float as write_float,
    write_float_matrix as write_float_matrix,
    write_id as write_id,
    write_int as write_int,
    write_string as write_string,
)
from .baseline import rescale as rescale
from .channels.channels import (
    InterpolationMixin as InterpolationMixin,
    ReferenceMixin as ReferenceMixin,
    UpdateChannelsMixin as UpdateChannelsMixin,
)
from .filter import FilterMixin as FilterMixin, detrend as detrend
from .parallel import parallel_func as parallel_func
from .time_frequency.spectrum import (
    Spectrum as Spectrum,
    SpectrumMixin as SpectrumMixin,
)
from .utils import (
    ExtendedTimeMixin as ExtendedTimeMixin,
    SizeMixin as SizeMixin,
    check_fname as check_fname,
    copy_function_doc_to_method_doc as copy_function_doc_to_method_doc,
    fill_doc as fill_doc,
    logger as logger,
    repr_html as repr_html,
    sizeof_fmt as sizeof_fmt,
    warn as warn,
)
from .viz import (
    plot_evoked as plot_evoked,
    plot_evoked_field as plot_evoked_field,
    plot_evoked_image as plot_evoked_image,
    plot_evoked_topo as plot_evoked_topo,
    plot_evoked_topomap as plot_evoked_topomap,
)
from .viz.evoked import (
    plot_evoked_joint as plot_evoked_joint,
    plot_evoked_white as plot_evoked_white,
)
from _typeshed import Incomplete

class Evoked(
    ProjMixin,
    ContainsMixin,
    UpdateChannelsMixin,
    ReferenceMixin,
    SetChannelsMixin,
    InterpolationMixin,
    FilterMixin,
    ExtendedTimeMixin,
    SizeMixin,
    SpectrumMixin,
):
    """## 🧠 Evoked data.

    -----
    ### 🛠️ Parameters

    #### `fname : path-like`
        Name of evoked/average FIF file to load.
        If None no data is loaded.
    #### `condition : int, or str`
        Dataset ID number (int) or comment/name (str). Optional if there is
        only one data set in file.
    #### `proj : bool, optional`
        Apply SSP projection vectors.
    #### `kind : str`
        Either ``'average'`` or ``'standard_error'``. The type of data to read.
        Only used if 'condition' is a str.
    #### `allow_maxshield : bool | str (default False)`
        If True, allow loading of data that has been recorded with internal
        active compensation (MaxShield). Data recorded with MaxShield should
        generally not be loaded directly, but should first be processed using
        SSS/tSSS to remove the compensation signals that may also affect brain
        activity. Can also be ``"yes"`` to load without eliciting a warning.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### 📊 Attributes


    #### `info : mne.Info`
        The `mne.Info` object with information about the sensors and methods of measurement.
    #### `ch_names : list of str`
        List of channels' names.
    #### `nave : int`
        Number of averaged epochs.
    #### `kind : str`
        Type of data, either average or standard_error.
    #### `comment : str`
        Comment on dataset. Can be the condition.
    #### `data : array of shape (n_channels, n_times)`
        Evoked response.
    #### `first : int`
        First time sample.
    #### `last : int`
        Last time sample.
    #### `tmin : float`
        The first time point in seconds.
    #### `tmax : float`
        The last time point in seconds.
    #### `times :  array`
        Time vector in seconds. Goes from ``tmin`` to ``tmax``. Time interval
        between consecutive time samples is equal to the inverse of the
        sampling frequency.
    #### `baseline : None | tuple of length 2`
         This attribute reflects whether the data has been baseline-corrected
         (it will be a ``tuple`` then) or not (it will be ``None``).

    -----
    ### 📖 Notes

    Evoked objects can only contain the average of a single set of conditions.
    """

    preload: bool
    filename: Incomplete

    def __init__(
        self,
        fname,
        condition=None,
        proj: bool = True,
        kind: str = "average",
        allow_maxshield: bool = False,
        *,
        verbose=None,
    ) -> None: ...
    @property
    def kind(self):
        """## 🧠 The data kind."""
        ...
    @kind.setter
    def kind(self, kind) -> None:
        """## 🧠 The data kind."""
        ...
    @property
    def data(self):
        """## 🧠 The data matrix."""
        ...
    @data.setter
    def data(self, data) -> None:
        """## 🧠 The data matrix."""
        ...
    def get_data(self, picks=None, units=None, tmin=None, tmax=None):
        """## 🧠 Get evoked data as 2D array.

        -----
        ### 🛠️ Parameters

        #### `picks : str | array-like | slice | None`
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel `type` strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel `name` strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick all channels. Note that channels in
            ``info['bads']`` `will be included` if their names or indices are
            explicitly provided.

        #### `units : str | dict | None`
            Specify the unit(s) that the data should be returned in. If
            ``None`` (default), the data is returned in the
            channel-type-specific default units, which are SI units (see
            `units` and :term:`data channels`). If a string, must be a
            sub-multiple of SI units that will be used to scale the data from
            all channels of the type associated with that unit. This only works
            if the data contains one channel type that has a unit (unitless
            channel types are left unchanged). For example if there are only
            EEG and STIM channels, ``units='uV'`` will scale EEG channels to
            micro-Volts while STIM channels will be unchanged. Finally, if a
            dictionary is provided, keys must be channel types, and values must
            be units to scale the data of that channel type to. For example
            ``dict(grad='fT/cm', mag='fT')`` will scale the corresponding types
            accordingly, but all other channel types will remain in their
            channel-type-specific default unit.
        #### `tmin : float | None`
            Start time of data to get in seconds.
        #### `tmax : float | None`
            End time of data to get in seconds.

        -----
        ### ⏎ Returns

        #### `data : ndarray, shape (n_channels, n_times)`
            A view on evoked data.

        -----
        ### 📖 Notes

        ✨ Added in vesion 0.24
        """
        ...
    def apply_function(
        self, fun, picks=None, dtype=None, n_jobs=None, verbose=None, **kwargs
    ):
        """## 🧠 Apply a function to a subset of channels.

        The function ``fun`` is applied to the channels defined in ``picks``.
        The evoked object's data is modified in-place. If the function returns a different
        data type (e.g. :py:obj:`numpy.complex128`) it must be specified
        using the ``dtype`` parameter, which causes the data type of `all` the data
        to change (even if the function is only applied to channels in ``picks``).

        ### 💡 Note If ``n_jobs`` > 1, more memory is required as
                  ``len(picks) * n_times`` additional time points need to
                  be temporarily stored in memory.
        ### 💡 Note If the data type changes (``dtype != None``), more memory is
                  required since the original and the converted data needs
                  to be stored in memory.

        -----
        ### 🛠️ Parameters


        #### `fun : callable`
            A function to be applied to the channels. The first argument of
            fun has to be a timeseries (`numpy.ndarray`). The function must
            operate on an array of shape ``(n_times,)``  because it will apply channel-wise.
            The function must return an `numpy.ndarray` shaped like its input.
        #### `picks : str | array-like | slice | None`
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel `type` strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel `name` strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick all data channels (excluding reference
            MEG channels). Note that channels in ``info['bads']`` `will be included` if
            their names or indices are explicitly provided.

        #### `dtype : numpy.dtype`
            Data type to use after applying the function. If None
            (default) the data type is not modified.
        #### `n_jobs : int | None`
            The number of jobs to run in parallel. If ``-1``, it is set
            to the number of CPU cores. Requires the `joblib` package.
            ``None`` (default) is a marker for 'unset' that will be interpreted
            as ``n_jobs=1`` (sequential execution) unless the call is performed under
            a `joblib:joblib.parallel_config` context manager that sets another
            value for ``n_jobs``. Ignored if ``channel_wise=False`` as the workload
            is split across channels.

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        **kwargs : dict
            Additional keyword arguments to pass to ``fun``.

        -----
        ### ⏎ Returns

        #### `self : instance of Evoked`
            The evoked object with transformed data.
        """
        ...
    baseline: Incomplete

    def apply_baseline(self, baseline=(None, 0), *, verbose=None):
        """## 🧠 Baseline correct evoked data.

        -----
        ### 🛠️ Parameters


        #### `baseline : None | tuple of length 2`
            The time interval to consider as "baseline" when applying baseline
            correction. If ``None``, do not apply baseline correction.
            If a tuple ``(a, b)``, the interval is between ``a`` and ``b``
            (in seconds), including the endpoints.
            If ``a`` is ``None``, the `beginning` of the data is used; and if ``b``
            is ``None``, it is set to the `end` of the interval.
            If ``(None, None)``, the entire time interval is used.

            ### 💡 Note The baseline ``(a, b)`` includes both endpoints, i.e. all
                        timepoints ``t`` such that ``a <= t <= b``.

            Correction is applied `to each channel individually` in the following
            way:

            1. Calculate the mean signal of the baseline period.
            2. Subtract this mean from the `entire` ``Evoked``.

            Defaults to ``(None, 0)``, i.e. beginning of the the data until
            time point zero.

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns

        #### `evoked : instance of Evoked`
            The baseline-corrected Evoked object.

        -----
        ### 📖 Notes

        Baseline correction can be done multiple times.

        ✨ Added in vesion 0.13.0
        """
        ...
    def save(self, fname, *, overwrite: bool = False, verbose=None) -> None:
        """## 🧠 Save evoked data to a file.

        -----
        ### 🛠️ Parameters

        #### `fname : path-like`
            The name of the file, which should end with ``-ave.fif(.gz)`` or
            ``_ave.fif(.gz)``.

        #### `overwrite : bool`
            If True (default False), overwrite the destination file if it
            exists.

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### 📖 Notes

        To write multiple conditions into a single file, use
        `mne.write_evokeds`.

        🎭 Changed in version 0.23
            Information on baseline correction will be stored with the data,
            and will be restored when reading again via `mne.read_evokeds`.
        """
        ...
    def export(
        self, fname, fmt: str = "auto", *, overwrite: bool = False, verbose=None
    ) -> None:
        """## 🧠 Export Evoked to external formats.

        Supported formats:
            - MFF (``.mff``, uses `mne.export.export_evokeds_mff`)

        ### ⛔️ Warning
            Since we are exporting to external formats, there's no guarantee that all
            the info will be preserved in the external format. See Notes for details.

        -----
        ### 🛠️ Parameters


        #### `fname : str`
            Name of the output file.

        #### `fmt : 'auto' | 'mff'`
            Format of the export. Defaults to ``'auto'``, which will infer the format
            from the filename extension. See supported formats above for more
            information.

        #### `overwrite : bool`
            If True (default False), overwrite the destination file if it
            exists.

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### 📖 Notes

        ✨ Added in vesion 1.1

        Export to external format may not preserve all the information from the
        instance. To save in native MNE format (``.fif``) without information loss,
        use `mne.Evoked.save` instead.
        Export does not apply projector(s). Unapplied projector(s) will be lost.
        Consider applying projector(s) before exporting with
        `mne.Evoked.apply_proj`.
        """
        ...
    @property
    def ch_names(self):
        """## 🧠 Channel names."""
        ...
    def plot(
        self,
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
        spatial_colors: str = "auto",
        zorder: str = "unsorted",
        selectable: bool = True,
        noise_cov=None,
        time_unit: str = "s",
        sphere=None,
        *,
        highlight=None,
        verbose=None,
    ):
        """## 🧠 Plot evoked data using butterfly plots.

        Left click to a line shows the channel name. Selecting an area by clicking
        and holding left mouse button plots a topographic map of the painted area.

        ### 💡 Note If bad channels are not excluded they are shown in red.

        -----
        ### 🛠️ Parameters

        #### `picks : str | array-like | slice | None`
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel `type` strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel `name` strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick all channels. Note that channels in
            ``info['bads']`` `will be included` if their names or indices are
            explicitly provided.
        #### `exclude : list of str | 'bads'`
            Channels names to exclude from being shown. If 'bads', the
            bad channels are excluded.
        #### `unit : bool`
            Scale plot with channel (SI) unit.
        #### `show : bool`
            Show figure if True.
        #### `ylim : dict | None`
            Y limits for plots (after scaling has been applied). e.g.
            ylim = dict(eeg=[-20, 20])
            Valid keys are eeg, mag, grad, misc. If None, the ylim parameter
            for each channel equals the pyplot default.
        #### `xlim : 'tight' | tuple | None`
            X limits for plots.

        #### `proj : bool | 'interactive' | 'reconstruct'`
            If true SSP projections are applied before display. If 'interactive',
            a check box for reversible selection of SSP projection vectors will
            be shown. If 'reconstruct', projection vectors will be applied and then
            M/EEG data will be reconstructed via field mapping to reduce the signal
            bias caused by projection.

            🎭 Changed in version 0.21
               Support for 'reconstruct' was added.
        #### `hline : list of float | None`
            The values at which to show an horizontal line.
        #### `units : dict | None`
            The units of the channel types used for axes labels. If None,
            defaults to ``dict(eeg='µV', grad='fT/cm', mag='fT')``.
        #### `scalings : dict | None`
            The scalings of the channel types to be applied for plotting. If None,
            defaults to ``dict(eeg=1e6, grad=1e13, mag=1e15)``.
        #### `titles : dict | None`
            The titles associated with the channels. If None, defaults to
            ``dict(eeg='EEG', grad='Gradiometers', mag='Magnetometers')``.
        #### `axes : instance of Axes | list | None`
            The axes to plot to. If list, the list must be a list of Axes of
            the same length as the number of channel types. If instance of
            Axes, there must be only one channel type plotted.
        #### `gfp : bool | 'only'`
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
        #### `window_title : str | None`
            The title to put at the top of the figure.
        #### `spatial_colors : bool | 'auto'`
            If True, the lines are color coded by mapping physical sensor
            coordinates into color values. Spatially similar channels will have
            similar colors. Bad channels will be dotted. If False, the good
            channels are plotted black and bad channels red. If ``'auto'``, uses
            True if channel locations are present, and False if channel locations
            are missing or if the data contains only a single channel. Defaults to
            ``'auto'``.
        #### `zorder : str | callable`
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

            ✨ Added in vesion 0.13.0

        #### `selectable : bool`
            Whether to use interactive features. If True (default), it is possible
            to paint an area to draw topomaps. When False, the interactive features
            are disabled. Disabling interactive features reduces memory consumption
            and is useful when using ``axes`` parameter to draw multiaxes figures.

            ✨ Added in vesion 0.13.0

        #### `noise_cov : instance of Covariance | str | None`
            Noise covariance used to whiten the data while plotting.
            Whitened data channel names are shown in italic.
            Can be a string to load a covariance from disk.
            See also `mne.Evoked.plot_white` for additional inspection
            of noise covariance properties when whitening evoked data.
            For data processed with SSS, the effective dependence between
            magnetometers and gradiometers may introduce differences in scaling,
            consider using `mne.Evoked.plot_white`.

            ✨ Added in vesion 0.16.0
        #### `time_unit : str`
            The units for the time axis, can be "s" (default) or "ms".

            ✨ Added in vesion 0.16
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
        #### `highlight : array-like of float, shape(2,) | array-like of float, shape (n, 2) | None`
            Segments of the data to highlight by means of a light-yellow
            background color. Can be used to put visual emphasis on certain
            time periods. The time periods must be specified as ``array-like``
            objects in the form of ``(t_start, t_end)`` in the unit given by the
            ``time_unit`` parameter.
            Multiple time periods can be specified by passing an ``array-like``
            object of individual time periods (e.g., for 3 time periods, the shape
            of the passed object would be ``(3, 2)``. If ``None``, no highlighting
            is applied.

            ✨ Added in vesion 1.1

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns

        #### `fig : instance of matplotlib.figure.Figure`
            Figure containing the butterfly plots.

        -----
        ### 👉 See Also

        mne.viz.plot_evoked_white
        """
        ...
    def plot_image(
        self,
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
        show_names=None,
        group_by=None,
        sphere=None,
    ):
        """## 🧠 Plot evoked data as images.

        -----
        ### 🛠️ Parameters

        #### `picks : str | array-like | slice | None`
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel `type` strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel `name` strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick all channels. Note that channels in
            ``info['bads']`` `will be included` if their names or indices are
            explicitly provided.
            This parameter can also be used to set the order the channels
            are shown in, as the channel image is sorted by the order of picks.
        #### `exclude : list of str | 'bads'`
            Channels names to exclude from being shown. If 'bads', the
            bad channels are excluded.
        #### `unit : bool`
            Scale plot with channel (SI) unit.
        #### `show : bool`
            Show figure if True.
        #### `clim : dict | None`
            Color limits for plots (after scaling has been applied). e.g.
            ``clim = dict(eeg=[-20, 20])``.
            Valid keys are eeg, mag, grad, misc. If None, the clim parameter
            for each channel equals the pyplot default.
        #### `xlim : 'tight' | tuple | None`
            X limits for plots.
        #### `proj : bool | 'interactive'`
            If true SSP projections are applied before display. If 'interactive',
            a check box for reversible selection of SSP projection vectors will
            be shown.
        #### `units : dict | None`
            The units of the channel types used for axes labels. If None,
            defaults to ``dict(eeg='µV', grad='fT/cm', mag='fT')``.
        #### `scalings : dict | None`
            The scalings of the channel types to be applied for plotting. If None,`
            defaults to ``dict(eeg=1e6, grad=1e13, mag=1e15)``.
        #### `titles : dict | None`
            The titles associated with the channels. If None, defaults to
            ``dict(eeg='EEG', grad='Gradiometers', mag='Magnetometers')``.
        #### `axes : instance of Axes | list | dict | None`
            The axes to plot to. If list, the list must be a list of Axes of
            the same length as the number of channel types. If instance of
            Axes, there must be only one channel type plotted.
            If ``group_by`` is a dict, this cannot be a list, but it can be a dict
            of lists of axes, with the keys matching those of ``group_by``. In that
            case, the provided axes will be used for the corresponding groups.
            Defaults to ``None``.
        #### `cmap : matplotlib colormap | (colormap, bool) | 'interactive'`
            Colormap. If tuple, the first value indicates the colormap to use and
            the second value is a boolean defining interactivity. In interactive
            mode the colors are adjustable by clicking and dragging the colorbar
            with left and right mouse button. Left mouse button moves the scale up
            and down and right mouse button adjusts the range. Hitting space bar
            resets the scale. Up and down arrows can be used to change the
            colormap. If 'interactive', translates to ``('RdBu_r', True)``.
            Defaults to ``'RdBu_r'``.
        #### `colorbar : bool`
            If True, plot a colorbar. Defaults to True.

            ✨ Added in vesion 0.16
        #### `mask : ndarray | None`
            An array of booleans of the same shape as the data. Entries of the
            data that correspond to ``False`` in the mask are masked (see
            ``do_mask`` below). Useful for, e.g., masking for statistical
            significance.

            ✨ Added in vesion 0.16
        #### `mask_style : None | 'both' | 'contour' | 'mask'`
            If ``mask`` is not None: if 'contour', a contour line is drawn around
            the masked areas (``True`` in ``mask``). If 'mask', entries not
            ``True`` in ``mask`` are shown transparently. If 'both', both a contour
            and transparency are used.
            If ``None``, defaults to 'both' if ``mask`` is not None, and is ignored
            otherwise.

             ✨ Added in vesion 0.16
        #### `mask_cmap : matplotlib colormap | (colormap, bool) | 'interactive'`
            The colormap chosen for masked parts of the image (see below), if
            ``mask`` is not ``None``. If None, ``cmap`` is reused. Defaults to
            ``Greys``. Not interactive. Otherwise, as ``cmap``.
        #### `mask_alpha : float`
            A float between 0 and 1. If ``mask`` is not None, this sets the
            alpha level (degree of transparency) for the masked-out segments.
            I.e., if 0, masked-out segments are not visible at all.
            Defaults to .25.

            ✨ Added in vesion 0.16
        #### `time_unit : str`
            The units for the time axis, can be "ms" or "s" (default).

            ✨ Added in vesion 0.16
        #### `show_names : bool | 'auto' | 'all'`
            Determines if channel names should be plotted on the y axis. If False,
            no names are shown. If True, ticks are set automatically by matplotlib
            and the corresponding channel names are shown. If "all", all channel
            names are shown. If "auto", is set to False if ``picks`` is ``None``,
            to ``True`` if ``picks`` contains 25 or more entries, or to "all"
            if ``picks`` contains fewer than 25 entries.
        #### `group_by : None | dict`
            If a dict, the values must be picks, and ``axes`` must also be a dict
            with matching keys, or None. If ``axes`` is None, one figure and one
            axis will be created for each entry in ``group_by``.Then, for each
            entry, the picked channels will be plotted to the corresponding axis.
            If ``titles`` are None, keys will become plot titles. This is useful
            for e.g. ROIs. Each entry must contain only one channel type.
            For example::

                group_by=dict(Left_ROI=[1, 2, 3, 4], Right_ROI=[5, 6, 7, 8])

            If None, all picked channels are plotted to the same axis.
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

        -----
        ### ⏎ Returns

        #### `fig : instance of matplotlib.figure.Figure`
            Figure containing the images.
        """
        ...
    def plot_topo(
        self,
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
        """## 🧠 Plot 2D topography of evoked responses.

        Clicking on the plot of an individual sensor opens a new figure showing
        the evoked response for the selected sensor.

        -----
        ### 🛠️ Parameters

        #### `layout : instance of Layout | None`
            Layout instance specifying sensor positions (does not need to
            be specified for Neuromag data). If possible, the correct layout is
            inferred from the data.
        #### `layout_scale : float`
            Scaling factor for adjusting the relative size of the layout
            on the canvas.
        #### `color : list of color | color | None`
            Everything matplotlib accepts to specify colors. If not list-like,
            the color specified will be repeated. If None, colors are
            automatically drawn.
        #### `border : str`
            Matplotlib borders style to be used for each sensor plot.
        #### `ylim : dict | None`
            Y limits for plots (after scaling has been applied). The value
            determines the upper and lower subplot limits. e.g.
            ylim = dict(eeg=[-20, 20]). Valid keys are eeg, mag, grad, misc.
            If None, the ylim parameter for each channel type is determined by
            the minimum and maximum peak.
        #### `scalings : dict | None`
            The scalings of the channel types to be applied for plotting. If None,`
            defaults to ``dict(eeg=1e6, grad=1e13, mag=1e15)``.
        #### `title : str`
            Title of the figure.
        #### `proj : bool | 'interactive'`
            If true SSP projections are applied before display. If 'interactive',
            a check box for reversible selection of SSP projection vectors will
            be shown.
        #### `vline : list of float | None`
            The values at which to show a vertical line.
        #### `fig_background : None | ndarray`
            A background image for the figure. This must work with a call to
            plt.imshow. Defaults to None.
        #### `merge_grads : bool`
            Whether to use RMS value of gradiometer pairs. Only works for Neuromag
            data. Defaults to False.
        #### `legend : bool | int | str | tuple`
            If True, create a legend based on evoked.comment. If False, disable the
            legend. Otherwise, the legend is created and the parameter value is
            passed as the location parameter to the matplotlib legend call. It can
            be an integer (e.g. 0 corresponds to upper right corner of the plot),
            a string (e.g. 'upper right'), or a tuple (x, y coordinates of the
            lower left corner of the legend in the axes coordinate system).
            See matplotlib documentation for more details.
        #### `axes : instance of matplotlib Axes | None`
            Axes to plot into. If None, axes will be created.
        #### `background_color : color`
            Background color. Typically 'k' (black) or 'w' (white; default).

            ✨ Added in vesion 0.15.0
        #### `noise_cov : instance of Covariance | str | None`
            Noise covariance used to whiten the data while plotting.
            Whitened data channel names are shown in italic.
            Can be a string to load a covariance from disk.

            ✨ Added in vesion 0.16.0
        #### `exclude : list of str | 'bads'`
            Channels names to exclude from the plot. If 'bads', the
            bad channels are excluded. By default, exclude is set to 'bads'.
        #### `show : bool`
            Show figure if True.

        -----
        ### ⏎ Returns

        #### `fig : instance of matplotlib.figure.Figure`
            Images of evoked responses at sensor locations.

            -----
            ### 📖 Notes

            ✨ Added in vesion 0.10.0
        """
        ...
    def plot_topomap(
        self,
        times: str = "auto",
        *,
        average=None,
        ch_type=None,
        scalings=None,
        proj: bool = False,
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
        cbar_fmt: str = "%3.1f",
        units=None,
        axes=None,
        time_unit: str = "s",
        time_format=None,
        nrows: int = 1,
        ncols: str = "auto",
        show: bool = True,
    ):
        """## 🧠 Plot topographic maps of specific time points of evoked data.

        -----
        ### 🛠️ Parameters

        #### `times : float | array of float | "auto" | "peaks" | "interactive"`
            The time point(s) to plot. If "auto", the number of ``axes`` determines
            the amount of time point(s). If ``axes`` is also None, at most 10
            topographies will be shown with a regular time spacing between the
            first and last time instant. If "peaks", finds time points
            automatically by checking for local maxima in global field power. If
            "interactive", the time can be set interactively at run-time by using a
            slider.

        #### `average : float | array-like of float, shape (n_times,) | None`
            The time window (in seconds) around a given time point to be used for
            averaging. For example, 0.2 would translate into a time window that
            starts 0.1 s before and ends 0.1 s after the given time point. If the
            time window exceeds the duration of the data, it will be clipped.
            Different time windows (one per time point) can be provided by
            passing an ``array-like`` object (e.g., ``[0.1, 0.2, 0.3]``). If
            ``None`` (default), no averaging will take place.

            🎭 Changed in version 1.1
               Support for ``array-like`` input.
        #### `ch_type : 'mag' | 'grad' | 'planar1' | 'planar2' | 'eeg' | None`
            The channel type to plot. For ``'grad'``, the gradiometers are
            collected in pairs and the RMS for each pair is plotted. If
            ``None`` the first available channel type from order shown above is used. Defaults to ``None``.

        #### `scalings : dict | float | None`
            The scalings of the channel types to be applied for plotting.
            If None, defaults to ``dict(eeg=1e6, grad=1e13, mag=1e15)``.

        #### `proj : bool | 'interactive' | 'reconstruct'`
            If true SSP projections are applied before display. If 'interactive',
            a check box for reversible selection of SSP projection vectors will
            be shown. If 'reconstruct', projection vectors will be applied and then
            M/EEG data will be reconstructed via field mapping to reduce the signal
            bias caused by projection.

            🎭 Changed in version 0.21
               Support for 'reconstruct' was added.

        #### `sensors : bool | str`
            Whether to add markers for sensor locations. If `str`, should be a
            valid matplotlib format string (e.g., ``'r+'`` for red plusses, see the
            Notes section of `matplotlib.axes.Axes.plot`). If ``True`` (the
            default), black circles will be used.

        #### `show_names : bool | callable`
            If ``True``, show channel names next to each sensor marker. If callable,
            channel names will be formatted using the callable; e.g., to
            delete the prefix 'MEG ' from all channel names, pass the function
            ``lambda x: x.replace('MEG ', '')``. If ``mask`` is not ``None``, only
            non-masked sensor names will be shown.

        #### `mask : ndarray of bool, shape (n_channels, n_times) | None`
            Array indicating channel-time combinations to highlight with a distinct
            plotting style (useful for, e.g. marking which channels at which times a statistical test of the data reaches significance). Array elements set to ``True`` will be plotted
            with the parameters given in ``mask_params``. Defaults to ``None``,
            equivalent to an array of all ``False`` elements.

        #### `mask_params : dict | None`
            Additional plotting parameters for plotting significant sensors.
            Default (None) equals::

                dict(marker='o', markerfacecolor='w', markeredgecolor='k',
                        linewidth=0, markersize=4)

        #### `contours : int | array-like`
            The number of contour lines to draw. If ``0``, no contours will be drawn.
            If a positive integer, that number of contour levels are chosen using the
            matplotlib tick locator (may sometimes be inaccurate, use array for
            accuracy). If array-like, the array values are used as the contour levels.
            The values should be in µV for EEG, fT for magnetometers and fT/m for
            gradiometers. If ``colorbar=True``, the colorbar will have ticks
            corresponding to the contour levels. Default is ``6``.

        #### `outlines : 'head' | dict | None`
            The outlines to be drawn. If 'head', the default head scheme will be
            drawn. If dict, each key refers to a tuple of x and y positions, the values
            in 'mask_pos' will serve as image mask.
            Alternatively, a matplotlib patch object can be passed for advanced
            masking options, either directly or as a function that returns patches
            (required for multi-axis plots). If None, nothing will be drawn.
            Defaults to 'head'.
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

        #### `image_interp : str`
            The image interpolation to be used. Options are ``'cubic'`` (default)
            to use `scipy.interpolate.CloughTocher2DInterpolator`,
            ``'nearest'`` to use `scipy.spatial.Voronoi` or
            ``'linear'`` to use `scipy.interpolate.LinearNDInterpolator`.

        #### `extrapolate : str`
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

            ✨ Added in vesion 0.18

            🎭 Changed in version 0.21

               - The default was changed to ``'local'`` for MEG sensors.
               - ``'local'`` was changed to use a convex hull mask
               - ``'head'`` was changed to extrapolate out to the clipping circle.

        #### `border : float | 'mean'`
            Value to extrapolate to on the topomap borders. If ``'mean'`` (default),
            then each extrapolated point has the average value of its neighbours.

            ✨ Added in vesion 0.20

        #### `res : int`
            The resolution of the topomap image (number of pixels along each side).

        #### `size : float`
            Side length of each subplot in inches.

        #### `cmap : matplotlib colormap | (colormap, bool) | 'interactive' | None`
            Colormap to use. If `tuple`, the first value indicates the colormap
            to use and the second value is a boolean defining interactivity. In
            interactive mode the colors are adjustable by clicking and dragging the
            colorbar with left and right mouse button. Left mouse button moves the
            scale up and down and right mouse button adjusts the range. Hitting
            space bar resets the range. Up and down arrows can be used to change
            the colormap. If ``None``, ``'Reds'`` is used for data that is either
            all-positive or all-negative, and ``'RdBu_r'`` is used otherwise.
            ``'interactive'`` is equivalent to ``(None, True)``. Defaults to ``None``.

            ### ⛔️ Warning  Interactive mode works smoothly only for a small amount
                of topomaps. Interactive mode is disabled by default for more than
                2 topomaps.

        #### `vlim : tuple of length 2 | 'joint'`
            Colormap limits to use. If a `tuple` of floats, specifies the
            lower and upper bounds of the colormap (in that order); providing
            ``None`` for either entry will set the corresponding boundary at the
            min/max of the data (separately for each topomap). Elements of the `tuple` may also be callable functions which take in a `NumPy array <numpy.ndarray>` and return a scalar. If ``vlim='joint'``, will compute the colormap limits jointly across all topomaps of the same channel type, using the min/max of the data for that channel type. Defaults to ``(None, None)``.

            ✨ Added in vesion 1.2

        #### `cnorm : matplotlib.colors.Normalize | None`
            How to normalize the colormap. If ``None``, standard linear normalization
            is performed. If not ``None``, ``vmin`` and ``vmax`` will be ignored.
            See `Matplotlib docs <matplotlib:colormapnorms>`
            for more details on colormap normalization, and
            `the ERDs example<cnorm-example>` for an example of its use.

            ✨ Added in vesion 1.2

        #### `colorbar : bool`
            Plot a colorbar in the rightmost column of the figure.
        #### `cbar_fmt : str`
            Formatting string for colorbar tick labels. See `formatspec` for
            details.

        #### `units : dict | str | None`
            The units to use for the colorbar label. Ignored if ``colorbar=False``.
            If ``None`` and ``scalings=None`` the unit is automatically determined, otherwise the label will be "AU" indicating arbitrary units.
            Default is ``None``.
        #### `axes : instance of Axes | list of Axes | None`
            The axes to plot to. If ``None``, a new `matplotlib.figure.Figure`
            will be created with the correct number of axes. If `matplotlib.axes.Axes` are provided (either as a single instance or a `list` of axes), the number of axes provided must match the number of ``times`` provided (unless ``times`` is ``None``).Default is ``None``.
        #### `time_unit : str`
            The units for the time axis, can be "ms" or "s" (default).

            ✨ Added in vesion 0.16
        #### `time_format : str | None`
            String format for topomap values. Defaults (None) to "%01d ms" if
            ``time_unit='ms'``, "%0.3f s" if ``time_unit='s'``, and
            "%g" otherwise. Can be an empty string to omit the time label.

        #### `nrows, ncols : int | 'auto'`
            The number of rows and columns of topographies to plot. If either ``nrows``
            or ``ncols`` is ``'auto'``, the necessary number will be inferred. Defaults
            to ``nrows=1, ncols='auto'``. Ignored when times == 'interactive'.

            ✨ Added in vesion 0.20
        #### `show : bool`
            Show the figure if ``True``.

        -----
        ### ⏎ Returns

        #### `fig : instance of matplotlib.figure.Figure`
           The figure.

        -----
        ### 📖 Notes

        When existing ``axes`` are provided and ``colorbar=True``, note that the
        colorbar scale will only accurately reflect topomaps that are generated in
        the same call as the colorbar. Note also that the colorbar will not be
        resized automatically when ``axes`` are provided; use Matplotlib's
        `axes.set_position() <matplotlib.axes.Axes.set_position>` method or
        `gridspec <matplotlib:arranging_axes>` interface to adjust the colorbar
        size yourself.

        When ``time=="interactive"``, the figure will publish and subscribe to the
        following UI events:

        * `mne.viz.ui_events.TimeChange` whenever a new time is selected.
        """
        ...
    def plot_field(
        self,
        surf_maps,
        time=None,
        time_label: str = "t = %0.0f ms",
        n_jobs=None,
        fig=None,
        vmax=None,
        n_contours: int = 21,
        *,
        show_density: bool = True,
        alpha=None,
        interpolation: str = "nearest",
        interaction: str = "terrain",
        time_viewer: str = "auto",
        verbose=None,
    ):
        """## 🧠 Plot MEG/EEG fields on head surface and helmet in 3D.

        -----
        ### 🛠️ Parameters

        #### `surf_maps : list`
            The surface mapping information obtained with make_field_map.
        #### `time : float | None`
            The time point at which the field map shall be displayed. If None,
            the average peak latency (across sensor types) is used.
        #### `time_label : str | None`
            How to print info about the time instant visualized.
        #### `n_jobs : int | None`
            The number of jobs to run in parallel. If ``-1``, it is set
            to the number of CPU cores. Requires the `joblib` package.
            ``None`` (default) is a marker for 'unset' that will be interpreted
            as ``n_jobs=1`` (sequential execution) unless the call is performed under
            a `joblib:joblib.parallel_config` context manager that sets another
            value for ``n_jobs``.
        #### `fig : Figure3D | mne.viz.Brain | None`
            If None (default), a new figure will be created, otherwise it will
            plot into the given figure.

            ✨ Added in vesion 0.20
            ✨ Added in vesion 1.4
                ``fig`` can also be a ``Brain`` figure.
        #### `vmax : float | dict | None`
            Maximum intensity. Can be a dictionary with two entries ``"eeg"`` and ``"meg"``
            to specify separate values for EEG and MEG fields respectively. Can be
            ``None`` to use the maximum value of the data.

            ✨ Added in vesion 0.21
            ✨ Added in vesion 1.4
                ``vmax`` can be a dictionary to specify separate values for EEG and
                MEG fields.
        #### `n_contours : int`
            The number of contours.

            ✨ Added in vesion 0.21
        #### `show_density : bool`
            Whether to draw the field density as an overlay on top of the helmet/head
            surface. Defaults to ``True``.

            ✨ Added in vesion 1.6
        #### `alpha : float | dict | None`
            Opacity of the meshes (between 0 and 1). Can be a dictionary with two
            entries ``"eeg"`` and ``"meg"`` to specify separate values for EEG and
            MEG fields respectively. Can be ``None`` to use 1.0 when a single field
            map is shown, or ``dict(eeg=1.0, meg=0.5)`` when both field maps are shown.

            ✨ Added in vesion 1.4

        #### `interpolation : str | None`
            Interpolation method (`scipy.interpolate.interp1d` parameter).
            Must be one of ``'linear'``, ``'nearest'``, ``'zero'``, ``'slinear'``,
            ``'quadratic'`` or ``'cubic'``.

            ✨ Added in vesion 1.6

        #### `interaction : 'trackball' | 'terrain'`
            How interactions with the scene via an input device (e.g., mouse or
            trackpad) modify the camera position. If ``'terrain'``, one axis is
            fixed, enabling "turntable-style" rotations. If ``'trackball'``,
            movement along all axes is possible, which provides more freedom of
            movement, but you may incidentally perform unintentional rotations along
            some axes.
            Defaults to ``'terrain'``.

            ✨ Added in vesion 1.1
        #### `time_viewer : bool | str`
            Display time viewer GUI. Can also be ``"auto"``, which will mean
            ``True`` if there is more than one time point and ``False`` otherwise.

            ✨ Added in vesion 1.6

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns

        #### `fig : Figure3D | mne.viz.EvokedField`
            Without the time viewer active, the figure is returned. With the time
            viewer active, an object is returned that can be used to control
            different aspects of the figure.
        """
        ...
    def plot_white(
        self,
        noise_cov,
        show: bool = True,
        rank=None,
        time_unit: str = "s",
        sphere=None,
        axes=None,
        verbose=None,
    ):
        """## 🧠 Plot whitened evoked response.

        Plots the whitened evoked response and the whitened GFP as described in
        :footcite:`EngemannGramfort2015`. This function is especially useful for
        investigating noise covariance properties to determine if data are
        properly whitened (e.g., achieving expected values in line with model
        assumptions, see Notes below).

        -----
        ### 🛠️ Parameters

        #### `noise_cov : list | instance of Covariance | path-like`
            The noise covariance. Can be a string to load a covariance from disk.
        #### `show : bool`
            Show figure if True.

        #### `rank : None | 'info' | 'full' | dict`
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
                extremely useful if you already `know` the rank of (part of) your
                data, for instance in case you have calculated it earlier.

                This parameter must be a dictionary whose `keys` correspond to
                channel types in the data (e.g. ``'meg'``, ``'mag'``, ``'grad'``,
                ``'eeg'``), and whose `values` are integers representing the
                respective ranks. For example, ``{'mag': 90, 'eeg': 45}`` will assume
                a rank of ``90`` and ``45`` for magnetometer data and EEG data,
                respectively.

                The ranks for all channel types present in the data, but
                `not` specified in the dictionary will be estimated empirically.
                That is, if you passed a dataset containing magnetometer, gradiometer,
                and EEG data together with the dictionary from the previous example,
                only the gradiometer rank would be determined, while the specified
                magnetometer and EEG ranks would be taken for granted.

            The default is ``None``.
        #### `time_unit : str`
            The units for the time axis, can be "ms" or "s" (default).

            ✨ Added in vesion 0.16
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
        #### `axes : list | None`
            List of axes to plot into.

            ✨ Added in vesion 0.21.0

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns

        #### `fig : instance of matplotlib.figure.Figure`
            The figure object containing the plot.

        -----
        ### 👉 See Also

        mne.Evoked.plot

        -----
        ### 📖 Notes

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
    def plot_joint(
        self,
        times: str = "peaks",
        title: str = "",
        picks=None,
        exclude: str = "bads",
        show: bool = True,
        ts_args=None,
        topomap_args=None,
    ):
        """## 🧠 Plot evoked data as butterfly plot and add topomaps for time points.

        ### 💡 Note Axes to plot in can be passed by the user through ``ts_args`` or
                  ``topomap_args``. In that case both ``ts_args`` and
                  ``topomap_args`` axes have to be used. Be aware that when the
                  axes are provided, their position may be slightly modified.

        -----
        ### 🛠️ Parameters

        #### `times : float | array of float | "auto" | "peaks"`
            The time point(s) to plot. If ``"auto"``, 5 evenly spaced topographies
            between the first and last time instant will be shown. If ``"peaks"``,
            finds time points automatically by checking for 3 local maxima in
            Global Field Power. Defaults to ``"peaks"``.
        #### `title : str | None`
            The title. If ``None``, suppress printing channel type title. If an
            empty string, a default title is created. Defaults to ''. If custom
            axes are passed make sure to set ``title=None``, otherwise some of your
            axes may be removed during placement of the title axis.
        #### `picks : str | array-like | slice | None`
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel `type` strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel `name` strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick all channels. Note that channels in
            ``info['bads']`` `will be included` if their names or indices are
            explicitly provided.
        #### `exclude : None | list of str | 'bads'`
            Channels names to exclude from being shown. If ``'bads'``, the
            bad channels are excluded. Defaults to ``None``.
        #### `show : bool`
            Show figure if ``True``. Defaults to ``True``.
        #### `ts_args : None | dict`
            A dict of ``kwargs`` that are forwarded to `mne.Evoked.plot` to
            style the butterfly plot. If they are not in this dict, the following
            defaults are passed: ``spatial_colors=True``, ``zorder='std'``.
            ``show`` and ``exclude`` are illegal.
            If ``None``, no customizable arguments will be passed.
            Defaults to ``None``.
        #### `topomap_args : None | dict`
            A dict of ``kwargs`` that are forwarded to
            `mne.Evoked.plot_topomap` to style the topomaps.
            If it is not in this dict, ``outlines='head'`` will be passed.
            ``show``, ``times``, ``colorbar`` are illegal.
            If ``None``, no customizable arguments will be passed.
            Defaults to ``None``.

        -----
        ### ⏎ Returns

        #### `fig : instance of matplotlib.figure.Figure | list`
            The figure object containing the plot. If ``evoked`` has multiple
            channel types, a list of figures, one for each channel type, is
            returned.

        -----
        ### 📖 Notes

        ✨ Added in vesion 0.12.0
        """
        ...
    def animate_topomap(
        self,
        ch_type=None,
        times=None,
        frame_rate=None,
        butterfly: bool = False,
        blit: bool = True,
        show: bool = True,
        time_unit: str = "s",
        sphere=None,
        *,
        image_interp="cubic",
        extrapolate="auto",
        vmin=None,
        vmax=None,
        verbose=None,
    ):
        """## 🧠 Make animation of evoked data as topomap timeseries.

        The animation can be paused/resumed with left mouse button.
        Left and right arrow keys can be used to move backward or forward
        in time.

        -----
        ### 🛠️ Parameters

        #### `ch_type : str | None`
            Channel type to plot. Accepted data types: 'mag', 'grad', 'eeg',
            'hbo', 'hbr', 'fnirs_cw_amplitude',
            'fnirs_fd_ac_amplitude', 'fnirs_fd_phase', and 'fnirs_od'.
            If None, first available channel type from the above list is used.
            Defaults to None.
        #### `times : array of float | None`
            The time points to plot. If None, 10 evenly spaced samples are
            calculated over the evoked time series. Defaults to None.
        #### `frame_rate : int | None`
            Frame rate for the animation in Hz. If None,
            frame rate = sfreq / 10. Defaults to None.
        #### `butterfly : bool`
            Whether to plot the data as butterfly plot under the topomap.
            Defaults to False.
        #### `blit : bool`
            Whether to use blit to optimize drawing. In general, it is
            recommended to use blit in combination with ``show=True``. If you
            intend to save the animation it is better to disable blit.
            Defaults to True.
        #### `show : bool`
            Whether to show the animation. Defaults to True.
        #### `time_unit : str`
            The units for the time axis, can be "ms" (default in 0.16)
            or "s" (will become the default in 0.17).

            ✨ Added in vesion 0.16
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

        #### `image_interp : str`
            The image interpolation to be used. Options are ``'cubic'`` (default)
            to use `scipy.interpolate.CloughTocher2DInterpolator`,
            ``'nearest'`` to use `scipy.spatial.Voronoi` or
            ``'linear'`` to use `scipy.interpolate.LinearNDInterpolator`.

        #### `extrapolate : str`
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

            ✨ Added in vesion 0.22

        #### `vmin, vmax : float | callable | None`
            Lower and upper bounds of the colormap, in the same units as the data.
            If ``vmin`` and ``vmax`` are both ``None``, they are set at ± the
            maximum absolute value of the data (yielding a colormap with midpoint
            at 0). If only one of ``vmin``, ``vmax`` is ``None``, will use
            ``min(data)`` or ``max(data)``, respectively. If callable, should
            accept a `NumPy array <numpy.ndarray>` of data and return a
            float.

            ✨ Added in vesion 1.1.0

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns

        #### `fig : instance of matplotlib.figure.Figure`
            The figure.
        #### `anim : instance of matplotlib.animation.FuncAnimation`
            Animation of the topomap.

        -----
        ### 📖 Notes

        ✨ Added in vesion 0.12.0
        """
        ...
    def as_type(self, ch_type: str = "grad", mode: str = "fast"):
        """## 🧠 Compute virtual evoked using interpolated fields.

        ### ⛔️ Warning Using virtual evoked to compute inverse can yield
            unexpected results. The virtual channels have ``'_v'`` appended
            at the end of the names to emphasize that the data contained in
            them are interpolated.

        -----
        ### 🛠️ Parameters

        #### `ch_type : str`
            The destination channel type. It can be 'mag' or 'grad'.
        #### `mode : str`
            Either ``'accurate'`` or ``'fast'``, determines the quality of the
            Legendre polynomial expansion used. ``'fast'`` should be sufficient
            for most applications.

        -----
        ### ⏎ Returns

        #### `evoked : instance of mne.Evoked`
            The transformed evoked object containing only virtual channels.

        -----
        ### 📖 Notes

        This method returns a copy and does not modify the data it
        operates on. It also returns an EvokedArray instance.

        ✨ Added in vesion 0.9.0
        """
        ...
    def detrend(self, order: int = 1, picks=None):
        """## 🧠 Detrend data.

        This function operates in-place.

        -----
        ### 🛠️ Parameters

        #### `order : int`
            Either 0 or 1, the order of the detrending. 0 is a constant
            (DC) detrend, 1 is a linear detrend.
        #### `picks : str | array-like | slice | None`
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel `type` strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel `name` strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick good data channels. Note that channels
            in ``info['bads']`` `will be included` if their names or indices are
            explicitly provided.

        -----
        ### ⏎ Returns

        #### `evoked : instance of Evoked`
            The detrended evoked object.
        """
        ...
    def copy(self):
        """## 🧠 Copy the instance of evoked.

        -----
        ### ⏎ Returns

        #### `evoked : instance of Evoked`
            A copy of the object.
        """
        ...
    def __neg__(self):
        """## 🧠 Negate channel responses.

        -----
        ### ⏎ Returns

        #### `evoked_neg : instance of Evoked`
            The Evoked instance with channel data negated and '-'
            prepended to the comment.
        """
        ...
    def get_peak(
        self,
        ch_type=None,
        tmin=None,
        tmax=None,
        mode: str = "abs",
        time_as_index: bool = False,
        merge_grads: bool = False,
        return_amplitude: bool = False,
    ):
        """## 🧠 Get location and latency of peak amplitude.

        -----
        ### 🛠️ Parameters

        #### `ch_type : str | None`
            The channel type to use. Defaults to None. If more than one channel
            type is present in the data, this value `must` be provided.
        #### `tmin : float | None`
            The minimum point in time to be considered for peak getting.
            If None (default), the beginning of the data is used.
        #### `tmax : float | None`
            The maximum point in time to be considered for peak getting.
            If None (default), the end of the data is used.
        #### `mode : 'pos' | 'neg' | 'abs'`
            How to deal with the sign of the data. If 'pos' only positive
            values will be considered. If 'neg' only negative values will
            be considered. If 'abs' absolute values will be considered.
            Defaults to 'abs'.
        #### `time_as_index : bool`
            Whether to return the time index instead of the latency in seconds.
        #### `merge_grads : bool`
            If True, compute peak from merged gradiometer data.
        #### `return_amplitude : bool`
            If True, return also the amplitude at the maximum response.

            ✨ Added in vesion 0.16

        -----
        ### ⏎ Returns

        #### `ch_name : str`
            The channel exhibiting the maximum response.
        #### `latency : float | int`
            The time point of the maximum response, either latency in seconds
            or index.
        #### `amplitude : float`
            The amplitude of the maximum response. Only returned if
            return_amplitude is True.

            ✨ Added in vesion 0.16
        """
        ...
    def compute_psd(
        self,
        method: str = "multitaper",
        fmin: int = 0,
        fmax=...,
        tmin=None,
        tmax=None,
        picks=None,
        proj: bool = False,
        remove_dc: bool = True,
        exclude=(),
        *,
        n_jobs: int = 1,
        verbose=None,
        **method_kw,
    ):
        """## 🧠 Perform spectral analysis on sensor data.

        -----
        ### 🛠️ Parameters


        #### `method : ``'welch'`` | ``'multitaper'```
            Spectral estimation method. ``'welch'`` uses Welch's
            method :footcite:p:`Welch1967`, ``'multitaper'`` uses DPSS
            tapers :footcite:p:`Slepian1978`.
            Default is ``'multitaper'``.
        #### `fmin, fmax : float`
            The lower- and upper-bound on frequencies of interest. Default is ``fmin=0, fmax=np.inf`` (spans all frequencies present in the data).
        #### `tmin, tmax : float | None`
            First and last times to include, in seconds. ``None`` uses the first or
            last time present in the data. Default is ``tmin=None, tmax=None`` (all
            times).
        #### `picks : str | array-like | slice | None`
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel `type` strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel `name` strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick good data channels (excluding reference
            MEG channels). Note that channels in ``info['bads']`` `will be included` if
            their names or indices are explicitly provided.
        #### `proj : bool`
            Whether to apply SSP projection vectors before spectral estimation.
            Default is ``False``.

        #### `remove_dc : bool`
            If ``True``, the mean is subtracted from each segment before computing
            its spectrum.
        #### `exclude : list of str | 'bads'`
            Channel names to exclude. If ``'bads'``, channels
            in ``info['bads']`` are excluded; pass an empty list to
            include all channels (including "bad" channels, if any).
        #### `n_jobs : int | None`
            The number of jobs to run in parallel. If ``-1``, it is set
            to the number of CPU cores. Requires the `joblib` package.
            ``None`` (default) is a marker for 'unset' that will be interpreted
            as ``n_jobs=1`` (sequential execution) unless the call is performed under
            a `joblib:joblib.parallel_config` context manager that sets another
            value for ``n_jobs``.

        #### `verbose : bool | str | int | None`
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

        -----
        ### ⏎ Returns

        #### `spectrum : instance of Spectrum`
            The spectral representation of the data.

        -----
        ### 📖 Notes

        ✨ Added in vesion 1.2

        References
        ----------
        .. footbibliography::
        """
        ...
    def plot_psd(
        self,
        fmin: int = 0,
        fmax=...,
        tmin=None,
        tmax=None,
        picks=None,
        proj: bool = False,
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
        """## 🧠 Plot power or amplitude spectra.

        Separate plots are drawn for each channel type. When the data have been
        processed with a bandpass, lowpass or highpass filter, dashed lines (╎)
        indicate the boundaries of the filter. The line noise frequency is also
        indicated with a dashed line (⋮). If ``average=False``, the plot will
        be interactive, and click-dragging on the spectrum will generate a
        scalp topography plot for the chosen frequency range in a new figure.

        -----
        ### 🛠️ Parameters

        #### `fmin, fmax : float`
            The lower- and upper-bound on frequencies of interest. Default is ``fmin=0, fmax=np.inf`` (spans all frequencies present in the data).
        #### `tmin, tmax : float | None`
            First and last times to include, in seconds. ``None`` uses the first or
            last time present in the data. Default is ``tmin=None, tmax=None`` (all
            times).
        #### `picks : str | array-like | slice | None`
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel `type` strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel `name` strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick good data channels (excluding reference
            MEG channels). Note that channels in ``info['bads']`` `will be included` if
            their names or indices are explicitly provided.
        #### `proj : bool`
            Whether to apply SSP projection vectors before spectral estimation.
            Default is ``False``.

        #### `method : ``'welch'`` | ``'multitaper'`` | ``'auto'```
            Spectral estimation method. ``'welch'`` uses Welch's
            method :footcite:p:`Welch1967`, ``'multitaper'`` uses DPSS
            tapers :footcite:p:`Slepian1978`. ``'auto'`` (default) uses Welch's method for continuous data and multitaper for `mne.Epochs` or `mne.Evoked` data.
        #### `average : bool`
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
        #### `estimate : str, {'auto', 'power', 'amplitude'}`
            Can be "power" for power spectral density (PSD), "amplitude" for
            amplitude spectrum density (ASD), or "auto" (default), which uses
            "power" when dB is True and "amplitude" otherwise.
        #### `xscale : 'linear' | 'log'`
            Scale of the frequency axis. Default is ``'linear'``.
        #### `area_mode : str | None`
            Mode for plotting area. If 'std', the mean +/- 1 STD (across channels)
            will be plotted. If 'range', the min and max (across channels) will be
            plotted. Bad channels will be excluded from these calculations.
            If None, no area will be plotted. If average=False, no area is plotted.
        #### `area_alpha : float`
            Alpha for the area.
        #### `color : str | tuple`
            A matplotlib-compatible color to use. Has no effect when
            spatial_colors=True.
        #### `line_alpha : float | None`
            Alpha for the PSD line. Can be None (default) to use 1.0 when
            ``average=True`` and 0.1 when ``average=False``.
        #### `spatial_colors : bool`
            Whether to color spectrum lines by channel location. Ignored if
            ``average=True``.
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

            ✨ Added in vesion 0.22.0
        #### `exclude : list of str | 'bads'`
            Channels names to exclude from being shown. If 'bads', the bad
            channels are excluded. Pass an empty list to plot all channels
            (including channels marked "bad", if any).

            ✨ Added in vesion 0.24.0
        #### `ax : instance of Axes | list of Axes | None`
            The axes to plot to. If ``None``, a new `matplotlib.figure.Figure`
            will be created with the correct number of axes. If `matplotlib.axes.Axes` are provided (either as a single instance or a `list` of axes), the number of axes provided must match the number of channel types present in the object..Default is ``None``.
        #### `show : bool`
            Show the figure if ``True``.
        #### `n_jobs : int | None`
            The number of jobs to run in parallel. If ``-1``, it is set
            to the number of CPU cores. Requires the `joblib` package.
            ``None`` (default) is a marker for 'unset' that will be interpreted
            as ``n_jobs=1`` (sequential execution) unless the call is performed under
            a `joblib:joblib.parallel_config` context manager that sets another
            value for ``n_jobs``.

        #### `verbose : bool | str | int | None`
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

        -----
        ### ⏎ Returns

        #### `fig : instance of Figure`
            Figure with frequency spectra of the data channels.

        -----
        ### 📖 Notes

        This method exists to support legacy code; for new code the preferred
        idiom is ``inst.compute_psd().plot()`` (where ``inst`` is an instance
        of `mne.io.Raw`, `mne.Epochs`, or `mne.Evoked`).
        """
        ...
    def to_data_frame(
        self,
        picks=None,
        index=None,
        scalings=None,
        copy: bool = True,
        long_format: bool = False,
        time_format=None,
        *,
        verbose=None,
    ):
        """## 🧠 Export data in tabular structure as a pandas DataFrame.

        Channels are converted to columns in the DataFrame. By default,
        an additional column "time" is added, unless ``index='time'``
        (in which case time values form the DataFrame's index).

        -----
        ### 🛠️ Parameters

        #### `picks : str | array-like | slice | None`
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel `type` strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel `name` strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick all channels. Note that channels in
            ``info['bads']`` `will be included` if their names or indices are
            explicitly provided.

        #### `index : 'time' | None`
            Kind of index to use for the DataFrame. If ``None``, a sequential
            integer index (`pandas.RangeIndex`) will be used. If ``'time'``, a
            ``pandas.Index`` or `pandas.TimedeltaIndex` will be used
            (depending on the value of ``time_format``).
            Defaults to ``None``.

        #### `scalings : dict | None`
            Scaling factor applied to the channels picked. If ``None``, defaults to
            ``dict(eeg=1e6, mag=1e15, grad=1e13)`` — i.e., converts EEG to µV,
            magnetometers to fT, and gradiometers to fT/cm.

        #### `copy : bool`
            If ``True``, data will be copied. Otherwise data may be modified in place.
            Defaults to ``True``.

        #### `long_format : bool`
            If True, the DataFrame is returned in long format where each row is one
            observation of the signal at a unique combination of time point and channel.
            For convenience, a ``ch_type`` column is added to facilitate subsetting the resulting DataFrame. Defaults to ``False``.

        #### `time_format : str | None`
            Desired time format. If ``None``, no conversion is applied, and time values
            remain as float values in seconds. If ``'ms'``, time values will be rounded
            to the nearest millisecond and converted to integers. If ``'timedelta'``,
            time values will be converted to `pandas.Timedelta` values.
            Default is ``None``.

            ✨ Added in vesion 0.20

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns


        #### `df : instance of pandas.DataFrame`
            A dataframe suitable for usage with other statistical/plotting/analysis
            packages.
        """
        ...

class EvokedArray(Evoked):
    """## 🧠 Evoked object from numpy array.

    -----
    ### 🛠️ Parameters

    #### `data : array of shape (n_channels, n_times)`
        The channels' evoked response. See notes for proper units of measure.

    #### `info : mne.Info`
        The `mne.Info` object with information about the sensors and methods of measurement. Consider using `mne.create_info` to populate this
        structure.
    #### `tmin : float`
        Start time before event. Defaults to 0.
    #### `comment : str`
        Comment on dataset. Can be the condition. Defaults to ''.
    #### `nave : int`
        Number of averaged epochs. Defaults to 1.
    #### `kind : str`
        Type of data, either average or standard_error. Defaults to 'average'.

    #### `baseline : None | tuple of length 2`
        The time interval to consider as "baseline" when applying baseline
        correction. If ``None``, do not apply baseline correction.
        If a tuple ``(a, b)``, the interval is between ``a`` and ``b``
        (in seconds), including the endpoints.
        If ``a`` is ``None``, the `beginning` of the data is used; and if ``b``
        is ``None``, it is set to the `end` of the interval.
        If ``(None, None)``, the entire time interval is used.

        ### 💡 Note The baseline ``(a, b)`` includes both endpoints, i.e. all
                    timepoints ``t`` such that ``a <= t <= b``.

        Correction is applied `to each channel individually` in the following
        way:

        1. Calculate the mean signal of the baseline period.
        2. Subtract this mean from the `entire` ``Evoked``.

        Defaults to ``None``, i.e. no baseline correction.

        ✨ Added in vesion 0.23

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### 👉 See Also

    EpochsArray, io.RawArray, create_info

    -----
    ### 📖 Notes

    Proper units of measure:

    * V: eeg, eog, seeg, dbs, emg, ecg, bio, ecog
    * T: mag
    * T/m: grad
    * M: hbo, hbr
    * Am: dipole
    * AU: misc
    """

    data: Incomplete
    first: Incomplete
    last: Incomplete
    info: Incomplete
    nave: Incomplete
    kind: Incomplete
    comment: Incomplete
    picks: Incomplete
    preload: bool
    baseline: Incomplete

    def __init__(
        self,
        data,
        info,
        tmin: float = 0.0,
        comment: str = "",
        nave: int = 1,
        kind: str = "average",
        baseline=None,
        *,
        verbose=None,
    ) -> None: ...

def combine_evoked(all_evoked, weights):
    """## 🧠 Merge evoked data by weighted addition or subtraction.

    Each `mne.Evoked` in ``all_evoked`` should have the same channels and the
    same time instants. Subtraction can be performed by passing
    ``weights=[1, -1]``.

    ### ⛔️ Warning
        Other than cases like simple subtraction mentioned above (where all
        weights are -1 or 1), if you provide numeric weights instead of using
        ``'equal'`` or ``'nave'``, the resulting `mne.Evoked` object's
        ``.nave`` attribute (which is used to scale noise covariance when
        applying the inverse operator) may not be suitable for inverse imaging.

    -----
    ### 🛠️ Parameters

    #### `all_evoked : list of Evoked`
        The evoked datasets.
    #### `weights : list of float | 'equal' | 'nave'`
        The weights to apply to the data of each evoked instance, or a string
        describing the weighting strategy to apply: ``'nave'`` computes
        sum-to-one weights proportional to each object's ``nave`` attribute;
        ``'equal'`` weights each `mne.Evoked` by ``1 / len(all_evoked)``.

    -----
    ### ⏎ Returns

    #### `evoked : Evoked`
        The new evoked data.

    -----
    ### 📖 Notes

    ✨ Added in vesion 0.9.0
    """
    ...

def read_evokeds(
    fname,
    condition=None,
    baseline=None,
    kind: str = "average",
    proj: bool = True,
    allow_maxshield: bool = False,
    verbose=None,
):
    """## 🧠 Read evoked dataset(s).

    -----
    ### 🛠️ Parameters

    #### `fname : path-like`
        The filename, which should end with ``-ave.fif`` or ``-ave.fif.gz``.
    #### `condition : int or str | list of int or str | None`
        The index or list of indices of the evoked dataset to read. FIF files
        can contain multiple datasets. If None, all datasets are returned as a
        list.

    #### `baseline : None | tuple of length 2`
        The time interval to consider as "baseline" when applying baseline
        correction. If ``None``, do not apply baseline correction.
        If a tuple ``(a, b)``, the interval is between ``a`` and ``b``
        (in seconds), including the endpoints.
        If ``a`` is ``None``, the `beginning` of the data is used; and if ``b``
        is ``None``, it is set to the `end` of the interval.
        If ``(None, None)``, the entire time interval is used.

        ### 💡 Note The baseline ``(a, b)`` includes both endpoints, i.e. all
                    timepoints ``t`` such that ``a <= t <= b``.

        Correction is applied `to each channel individually` in the following
        way:

        1. Calculate the mean signal of the baseline period.
        2. Subtract this mean from the `entire` ``Evoked``.

        If ``None`` (default), do not apply baseline correction.

        ### 💡 Note Note that if the read  `mne.Evoked` objects have already
                  been baseline-corrected, the data retrieved from disk will
                  `always` be baseline-corrected (in fact, only the
                  baseline-corrected version of the data will be saved, so
                  there is no way to undo this procedure). Only `after` the
                  data has been loaded, a custom (additional) baseline
                  correction `may` be optionally applied by passing a tuple
                  here. Passing ``None`` will `not` remove an existing
                  baseline correction, but merely omit the optional, additional
                  baseline correction.
    #### `kind : str`
        Either 'average' or 'standard_error', the type of data to read.
    #### `proj : bool`
        If False, available projectors won't be applied to the data.
    #### `allow_maxshield : bool | str (default False)`
        If True, allow loading of data that has been recorded with internal
        active compensation (MaxShield). Data recorded with MaxShield should
        generally not be loaded directly, but should first be processed using
        SSS/tSSS to remove the compensation signals that may also affect brain
        activity. Can also be "yes" to load without eliciting a warning.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `evoked : Evoked or list of Evoked`
        The evoked dataset(s); one `mne.Evoked` if ``condition`` is an
        integer or string; or a list of `mne.Evoked` if ``condition`` is
        ``None`` or a list.

    -----
    ### 👉 See Also

    write_evokeds

    -----
    ### 📖 Notes

    🎭 Changed in version 0.23
        If the read `mne.Evoked` objects had been baseline-corrected before
        saving, this will be reflected in their ``baseline`` attribute after
        reading.
    """
    ...

def write_evokeds(
    fname, evoked, *, on_mismatch: str = "raise", overwrite: bool = False, verbose=None
) -> None:
    """## 🧠 Write an evoked dataset to a file.

    -----
    ### 🛠️ Parameters

    #### `fname : path-like`
        The file name, which should end with ``-ave.fif`` or ``-ave.fif.gz``.
    #### `evoked : Evoked instance, or list of Evoked instances`
        The evoked dataset, or list of evoked datasets, to save in one file.
        Note that the measurement info from the first evoked instance is used,
        so be sure that information matches.

    #### `on_mismatch : 'raise' | 'warn' | 'ignore'`
        Can be ``'raise'`` (default) to raise an error, ``'warn'`` to emit a
        warning, or ``'ignore'`` to ignore when the device-to-head transformation differs between
        instances.

        ✨ Added in vesion 0.24

    #### `overwrite : bool`
        If True (default False), overwrite the destination file if it
        exists.

        ✨ Added in vesion 1.0

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

        ✨ Added in vesion 0.24

    -----
    ### 👉 See Also

    read_evokeds

    -----
    ### 📖 Notes

    🎭 Changed in version 0.23
        Information on baseline correction will be stored with each individual
        `mne.Evoked` object, and will be restored when reading the data again
        via `mne.read_evokeds`.
    """
    ...
