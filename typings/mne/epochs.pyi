from ._fiff.constants import FIFF as FIFF
from ._fiff.meas_info import (
    ContainsMixin as ContainsMixin,
    SetChannelsMixin as SetChannelsMixin,
    read_meas_info as read_meas_info,
    write_meas_info as write_meas_info,
)
from ._fiff.open import fiff_open as fiff_open
from ._fiff.pick import (
    channel_indices_by_type as channel_indices_by_type,
    channel_type as channel_type,
    pick_channels as pick_channels,
    pick_info as pick_info,
)
from ._fiff.proj import ProjMixin as ProjMixin, setup_proj as setup_proj
from ._fiff.tag import read_tag as read_tag, read_tag_info as read_tag_info
from ._fiff.tree import dir_tree_find as dir_tree_find
from ._fiff.write import (
    INT32_MAX as INT32_MAX,
    end_block as end_block,
    start_and_end_file as start_and_end_file,
    start_block as start_block,
    write_complex_double_matrix as write_complex_double_matrix,
    write_complex_float_matrix as write_complex_float_matrix,
    write_double_matrix as write_double_matrix,
    write_float as write_float,
    write_float_matrix as write_float_matrix,
    write_id as write_id,
    write_int as write_int,
    write_string as write_string,
)
from .annotations import EpochAnnotationsMixin as EpochAnnotationsMixin
from .baseline import rescale as rescale
from .channels.channels import (
    InterpolationMixin as InterpolationMixin,
    ReferenceMixin as ReferenceMixin,
    UpdateChannelsMixin as UpdateChannelsMixin,
)
from .event import (
    make_fixed_length_events as make_fixed_length_events,
    match_event_names as match_event_names,
)
from .evoked import EvokedArray as EvokedArray
from .filter import FilterMixin as FilterMixin, detrend as detrend
from .fixes import rng_uniform as rng_uniform
from .parallel import parallel_func as parallel_func
from .time_frequency.spectrum import (
    EpochsSpectrum as EpochsSpectrum,
    SpectrumMixin as SpectrumMixin,
)
from .utils import (
    ExtendedTimeMixin as ExtendedTimeMixin,
    GetEpochsMixin as GetEpochsMixin,
    SizeMixin as SizeMixin,
    check_fname as check_fname,
    check_random_state as check_random_state,
    copy_function_doc_to_method_doc as copy_function_doc_to_method_doc,
    logger as logger,
    object_size as object_size,
    repr_html as repr_html,
    sizeof_fmt as sizeof_fmt,
    warn as warn,
)
from .utils.docs import fill_doc as fill_doc
from .viz import (
    plot_drop_log as plot_drop_log,
    plot_epochs as plot_epochs,
    plot_epochs_image as plot_epochs_image,
    plot_topo_image_epochs as plot_topo_image_epochs,
)
from _typeshed import Incomplete
from collections.abc import Generator

class BaseEpochs(
    ProjMixin,
    ContainsMixin,
    UpdateChannelsMixin,
    ReferenceMixin,
    SetChannelsMixin,
    InterpolationMixin,
    FilterMixin,
    ExtendedTimeMixin,
    SizeMixin,
    GetEpochsMixin,
    EpochAnnotationsMixin,
    SpectrumMixin,
):
    """Abstract base class for `mne.Epochs`-type classes.

    .. note::
        This class should not be instantiated directly via
        ``mne.BaseEpochs(...)``. Instead, use one of the functions listed in
        the See Also section below.

    Parameters
    ----------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    data : ndarray | None
        If ``None``, data will be read from the Raw object. If ndarray, must be
        of shape (n_epochs, n_channels, n_times).

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

    tmin, tmax : float
        Start and end time of the epochs in seconds, relative to the time-locked
        event. The closest or matching samples corresponding to the start and end
        time are included. Defaults to ``-0.2`` and ``0.5``, respectively.

    baseline : None | tuple of length 2
        The time interval to consider as "baseline" when applying baseline
        correction. If ``None``, do not apply baseline correction.
        If a tuple ``(a, b)``, the interval is between ``a`` and ``b``
        (in seconds), including the endpoints.
        If ``a`` is ``None``, the **beginning** of the data is used; and if ``b``
        is ``None``, it is set to the **end** of the interval.
        If ``(None, None)``, the entire time interval is used.

        .. note:: The baseline ``(a, b)`` includes both endpoints, i.e. all
                    timepoints ``t`` such that ``a <= t <= b``.

        Correction is applied **to each epoch and channel individually** in the
        following way:

        1. Calculate the mean signal of the baseline period.
        2. Subtract this mean from the **entire** epoch.

        Defaults to ``(None, 0)``, i.e. beginning of the the data until
        time point zero.

    raw : Raw object
        An instance of `mne.io.Raw`.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick all channels. Note that channels in
        ``info['bads']`` *will be included* if their names or indices are
        explicitly provided.

    reject : dict | None
        Reject epochs based on **maximum** peak-to-peak signal amplitude (PTP),
        i.e. the absolute difference between the lowest and the highest signal
        value. In each individual epoch, the PTP is calculated for every channel.
        If the PTP of any one channel exceeds the rejection threshold, the
        respective epoch will be dropped.

        The dictionary keys correspond to the different channel types; valid
        **keys** can be any channel type present in the object.

        Example::

            reject = dict(grad=4000e-13,  # unit: T / m (gradiometers)
                          mag=4e-12,      # unit: T (magnetometers)
                          eeg=40e-6,      # unit: V (EEG channels)
                          eog=250e-6      # unit: V (EOG channels)
                          )

        .. note:: Since rejection is based on a signal **difference**
                  calculated for each channel separately, applying baseline
                  correction does not affect the rejection procedure, as the
                  difference will be preserved.

        .. note:: To constrain the time period used for estimation of signal
                  quality, pass the ``reject_tmin`` and ``reject_tmax`` parameters.

        If ``reject`` is ``None`` (default), no rejection is performed.

    flat : dict | None
        Reject epochs based on **minimum** peak-to-peak signal amplitude (PTP).
        Valid **keys** can be any channel type present in the object. The
        **values** are floats that set the minimum acceptable PTP. If the PTP
        is smaller than this threshold, the epoch will be dropped. If ``None``
        then no rejection is performed based on flatness of the signal.

        .. note:: To constrain the time period used for estimation of signal
                  quality, pass the ``reject_tmin`` and ``reject_tmax`` parameters.

    decim : int
        Factor by which to subsample the data.

        .. warning:: Low-pass filtering is not performed, this simply selects
                     every Nth sample (where N is the value passed to
                     ``decim``), i.e., it compresses the signal (see Notes).
                     If the data are not properly filtered, aliasing artifacts
                     may occur.

    reject_tmin, reject_tmax : float | None
        Start and end of the time window used to reject epochs based on
        peak-to-peak (PTP) amplitudes as specified via ``reject`` and ``flat``.
        The default ``None`` corresponds to the first and last time points of the
        epochs, respectively.

        .. note:: This parameter controls the time period used in conjunction with
                  both, ``reject`` and ``flat``.

    detrend : int | None
        If 0 or 1, the data channels (MEG and EEG) will be detrended when
        loaded. 0 is a constant (DC) detrend, 1 is a linear detrend. None
        is no detrending. Note that detrending is performed before baseline
        correction. If no DC offset is preferred (zeroth order detrending),
        either turn off baseline correction, as this may introduce a DC
        shift, or set baseline correction to use the entire time interval
        (will yield equivalent results but be slower).

    proj : bool | 'delayed'
        Apply SSP projection vectors. If proj is 'delayed' and reject is not
        None the single epochs will be projected before the rejection
        decision, but used in unprojected state if they are kept.
        This way deciding which projection vectors are good can be postponed
        to the evoked stage without resulting in lower epoch counts and
        without producing results different from early SSP application
        given comparable parameters. Note that in this case baselining,
        detrending and temporal decimation will be postponed.
        If proj is False no projections will be applied which is the
        recommended value if SSPs are not used for cleaning the data.

    on_missing : 'raise' | 'warn' | 'ignore'
        What to do if one or several event ids are not found in the recording.
        Valid keys are 'raise' | 'warn' | 'ignore'
        Default is ``'raise'``. If ``'warn'``, it will proceed but
        warn; if ``'ignore'``, it will proceed silently.

        .. note::
           If none of the event ids are found in the data, an error will be
           automatically generated irrespective of this parameter.
    preload_at_end : bool

        Load all epochs from disk when creating the object
        or wait before accessing each epoch (more memory
        efficient but can be slower).

    selection : iterable | None
        Iterable of indices of selected epochs. If ``None``, will be
        automatically generated, corresponding to all non-zero events.

        .. versionadded:: 0.16

    drop_log : tuple | None
        Tuple of tuple of strings indicating which epochs have been marked to
        be ignored.
    filename : str | None
        The filename (if the epochs are read from disk).

    metadata : instance of pandas.DataFrame | None
        A `pandas.DataFrame` specifying metadata about each epoch.
        If given, ``len(metadata)`` must equal ``len(events)``. The DataFrame
        may only contain values of type (str | int | float | bool).
        If metadata is given, then pandas-style queries may be used to select
        subsets of data, see `mne.Epochs.__getitem__`.
        When a subset of the epochs is created in this (or any other
        supported) manner, the metadata object is subsetted accordingly, and
        the row indices will be modified to match ``epochs.selection``.

        .. versionadded:: 0.16

    event_repeated : str
        How to handle duplicates in ``events[:, 0]``. Can be ``'error'``
        (default), to raise an error, 'drop' to only retain the row occurring
        first in the :term:`events`, or ``'merge'`` to combine the coinciding
        events (=duplicates) into a new event (see Notes for details).

        .. versionadded:: 0.19

    raw_sfreq : float
        The original Raw object sampling rate. If None, then it is set to
        ``info['sfreq']``.
    annotations : instance of mne.Annotations | None
        Annotations to set.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    Epochs
    EpochsArray
    make_fixed_length_epochs

    Notes
    -----
    The ``BaseEpochs`` class is public to allow for stable type-checking in
    user code (i.e., ``isinstance(my_epochs, BaseEpochs)``) but should not be
    used as a constructor for Epochs objects (use instead `mne.Epochs`).
    """

    event_id: Incomplete
    selection: Incomplete
    events: Incomplete
    drop_log: Incomplete
    metadata: Incomplete
    detrend: Incomplete
    picks: Incomplete
    info: Incomplete
    preload: bool
    reject_tmin: Incomplete
    reject_tmax: Incomplete
    baseline: Incomplete
    reject: Incomplete
    flat: Incomplete

    def __init__(
        self,
        info,
        data,
        events,
        event_id=None,
        tmin: float = -0.2,
        tmax: float = 0.5,
        baseline=(None, 0),
        raw=None,
        picks=None,
        reject=None,
        flat=None,
        decim: int = 1,
        reject_tmin=None,
        reject_tmax=None,
        detrend=None,
        proj: bool = True,
        on_missing: str = "raise",
        preload_at_end: bool = False,
        selection=None,
        drop_log=None,
        filename=None,
        metadata=None,
        event_repeated: str = "error",
        *,
        raw_sfreq=None,
        annotations=None,
        verbose=None,
    ) -> None: ...
    def reset_drop_log_selection(self) -> None:
        """Reset the drop_log and selection entries.

        This method will simplify ``self.drop_log`` and ``self.selection``
        so that they are meaningless (tuple of empty tuples and increasing
        integers, respectively). This can be useful when concatenating
        many Epochs instances, as ``drop_log`` can accumulate many entries
        which can become problematic when saving.
        """
        ...
    def load_data(self):
        """Load the data if not already preloaded.

        Returns
        -------
        epochs : instance of Epochs
            The epochs object.

        Notes
        -----
        This function operates in-place.

        .. versionadded:: 0.10.0
        """
        ...
    def apply_baseline(self, baseline=(None, 0), *, verbose=None):
        """Baseline correct epochs.

        Parameters
        ----------

        baseline : None | tuple of length 2
            The time interval to consider as "baseline" when applying baseline
            correction. If ``None``, do not apply baseline correction.
            If a tuple ``(a, b)``, the interval is between ``a`` and ``b``
            (in seconds), including the endpoints.
            If ``a`` is ``None``, the **beginning** of the data is used; and if ``b``
            is ``None``, it is set to the **end** of the interval.
            If ``(None, None)``, the entire time interval is used.

            .. note:: The baseline ``(a, b)`` includes both endpoints, i.e. all
                        timepoints ``t`` such that ``a <= t <= b``.

            Correction is applied **to each epoch and channel individually** in the
            following way:

            1. Calculate the mean signal of the baseline period.
            2. Subtract this mean from the **entire** epoch.

            Defaults to ``(None, 0)``, i.e. beginning of the the data until
            time point zero.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        epochs : instance of Epochs
            The baseline-corrected Epochs object.

        Notes
        -----
        Baseline correction can be done multiple times, but can never be
        reverted once the data has been loaded.

        .. versionadded:: 0.10.0
        """
        ...
    def iter_evoked(self, copy: bool = False) -> Generator[Incomplete, None, None]:
        """Iterate over epochs as a sequence of Evoked objects.

        The Evoked objects yielded will each contain a single epoch (i.e., no
        averaging is performed).

        This method resets the object iteration state to the first epoch.

        Parameters
        ----------
        copy : bool
            If False copies of data and measurement info will be omitted
            to save time.
        """
        ...
    def subtract_evoked(self, evoked=None):
        """Subtract an evoked response from each epoch.

        Can be used to exclude the evoked response when analyzing induced
        activity, see e.g. [1]_.

        Parameters
        ----------
        evoked : instance of Evoked | None
            The evoked response to subtract. If None, the evoked response
            is computed from Epochs itself.

        Returns
        -------
        self : instance of Epochs
            The modified instance (instance is also modified inplace).

        References
        ----------
        .. [1] David et al. "Mechanisms of evoked and induced responses in
               MEG/EEG", NeuroImage, vol. 31, no. 4, pp. 1580-1591, July 2006.
        """
        ...
    def average(self, picks=None, method: str = "mean", by_event_type: bool = False):
        """Compute an average over epochs.

        Parameters
        ----------
        picks : str | array-like | slice | None
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel *type* strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick all data channels. Note that channels
            in ``info['bads']`` *will be included* if their names or indices are
            explicitly provided.
        method : str | callable
            How to combine the data. If "mean"/"median", the mean/median
            are returned.
            Otherwise, must be a callable which, when passed an array of shape
            (n_epochs, n_channels, n_time) returns an array of shape
            (n_channels, n_time).
            Note that due to file type limitations, the kind for all
            these will be "average".

        by_event_type : bool
            When ``False`` (the default) all epochs are processed together and a single
            `mne.Evoked` object is returned. When ``True``, epochs are first
            grouped by event type (as specified using the ``event_id`` parameter) and a
            list is returned containing a separate `mne.Evoked` object for each
            event type. The ``.comment`` attribute is set to the label of the event
            type.

            .. versionadded:: 0.24.0

        Returns
        -------

        evoked : instance of Evoked | list of Evoked
            The averaged epochs.
            When ``by_event_type=True`` was specified, a list is returned containing a
            separate `mne.Evoked` object for each event type. The list has the
            same order as the event types as specified in the ``event_id``
            dictionary.

        Notes
        -----
        Computes an average of all epochs in the instance, even if
        they correspond to different conditions. To average by condition,
        do ``epochs[condition].average()`` for each condition separately.

        When picks is None and epochs contain only ICA channels, no channels
        are selected, resulting in an error. This is because ICA channels
        are not considered data channels (they are of misc type) and only data
        channels are selected when picks is None.

        The ``method`` parameter allows e.g. robust averaging.
        For example, one could do:

            >>> from scipy.stats import trim_mean  # doctest:+SKIP
            >>> trim = lambda x: trim_mean(x, 0.1, axis=0)  # doctest:+SKIP
            >>> epochs.average(method=trim)  # doctest:+SKIP

        This would compute the trimmed mean.
        """
        ...
    def standard_error(self, picks=None, by_event_type: bool = False):
        """Compute standard error over epochs.

        Parameters
        ----------
        picks : str | array-like | slice | None
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel *type* strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick all data channels. Note that channels
            in ``info['bads']`` *will be included* if their names or indices are
            explicitly provided.

        by_event_type : bool
            When ``False`` (the default) all epochs are processed together and a single
            `mne.Evoked` object is returned. When ``True``, epochs are first
            grouped by event type (as specified using the ``event_id`` parameter) and a
            list is returned containing a separate `mne.Evoked` object for each
            event type. The ``.comment`` attribute is set to the label of the event
            type.

            .. versionadded:: 0.24.0

        Returns
        -------

        std_err : instance of Evoked | list of Evoked
            The standard error over epochs.
            When ``by_event_type=True`` was specified, a list is returned containing a
            separate `mne.Evoked` object for each event type. The list has the
            same order as the event types as specified in the ``event_id``
            dictionary.
        """
        ...
    @property
    def ch_names(self):
        """Channel names."""
        ...
    def plot(
        self,
        picks=None,
        scalings=None,
        n_epochs: int = 20,
        n_channels: int = 20,
        title=None,
        events: bool = False,
        event_color=None,
        order=None,
        show: bool = True,
        block: bool = False,
        decim: str = "auto",
        noise_cov=None,
        butterfly: bool = False,
        show_scrollbars: bool = True,
        show_scalebars: bool = True,
        epoch_colors=None,
        event_id=None,
        group_by: str = "type",
        precompute=None,
        use_opengl=None,
        *,
        theme=None,
        overview_mode=None,
        splash: bool = True,
    ):
        """Visualize epochs.

        Bad epochs can be marked with a left click on top of the epoch. Bad
        channels can be selected by clicking the channel name on the left side of
        the main axes. Calling this function drops all the selected bad epochs as
        well as bad epochs marked beforehand with rejection parameters.

        Parameters
        ----------
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
            Events to show with vertical bars. You can use `mne.viz.plot_events`
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
            See also `mne.Evoked.plot_white` for additional inspection
            of noise covariance properties when whitening evoked data.
            For data processed with SSS, the effective dependence between
            magnetometers and gradiometers may introduce differences in scaling,
            consider using `mne.Evoked.plot_white`.

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
            see `mne.set_config`.

            .. versionadded:: 0.24

        theme : str | path-like
            Can be "auto", "light", or "dark" or a path-like to a
            custom stylesheet. For Dark-Mode and automatic Dark-Mode-Detection,
            `qdarkstyle` and
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
        `raw.plot()<mne.io.Raw.plot>`, `epochs.plot()<mne.Epochs.plot>`,
        and `ica.plot_sources()<mne.preprocessing.ICA.plot_sources>`). One is
        based on `matplotlib`, and the other is based on
        :doc:`PyQtGraph<pyqtgraph:index>`. You can set the backend temporarily with the
        context manager `mne.viz.use_browser_backend`, you can set it for the
        duration of a Python session using `mne.viz.set_browser_backend`, and you
        can set the default for your computer via
        `mne.set_config('MNE_BROWSER_BACKEND', 'matplotlib')<mne.set_config>`
        (or ``'qt'``).

        .. note:: For the PyQtGraph backend to run in IPython with ``block=False``
                  you must run the magic command ``%gui qt5`` first.
        .. note:: To report issues with the PyQtGraph backend, please use the
                  `issues <https://github.com/mne-tools/mne-qt-browser/issues>`_
                  of ``mne-qt-browser``.

        .. versionadded:: 0.10.0
        """
        ...
    def plot_topo_image(
        self,
        layout=None,
        sigma: float = 0.0,
        vmin=None,
        vmax=None,
        colorbar=None,
        order=None,
        cmap: str = "RdBu_r",
        layout_scale: float = 0.95,
        title=None,
        scalings=None,
        border: str = "none",
        fig_facecolor: str = "k",
        fig_background=None,
        font_color: str = "w",
        show: bool = True,
    ):
        """Plot Event Related Potential / Fields image on topographies.

        Parameters
        ----------
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
            `matplotlib.pyplot.imshow`. Defaults to ``None``.
        font_color : color
            The color of tick labels in the colorbar. Defaults to white.
        show : bool
            Whether to show the figure. Defaults to ``True``.

        Returns
        -------
        fig : instance of `matplotlib.figure.Figure`
            Figure distributing one image per channel across sensor topography.

        Notes
        -----
        In an interactive Python session, this plot will be interactive; clicking
        on a channel image will pop open a larger view of the image; this image
        will always have a colorbar even when the topo plot does not (because it
        shows multiple sensor types).
        """
        ...
    def drop_bad(self, reject: str = "existing", flat: str = "existing", verbose=None):
        """Drop bad epochs without retaining the epochs data.

        Should be used before slicing operations.

        .. warning:: This operation is slow since all epochs have to be read
                     from disk. To avoid reading epochs from disk multiple
                     times, use `mne.Epochs.load_data()`.

        .. note:: To constrain the time period used for estimation of signal
                  quality, set ``epochs.reject_tmin`` and
                  ``epochs.reject_tmax``, respectively.

        Parameters
        ----------

        reject : dict | str | None
            Reject epochs based on **maximum** peak-to-peak signal amplitude (PTP),
            i.e. the absolute difference between the lowest and the highest signal
            value. In each individual epoch, the PTP is calculated for every channel.
            If the PTP of any one channel exceeds the rejection threshold, the
            respective epoch will be dropped.

            The dictionary keys correspond to the different channel types; valid
            **keys** can be any channel type present in the object.

            Example::

                reject = dict(grad=4000e-13,  # unit: T / m (gradiometers)
                              mag=4e-12,      # unit: T (magnetometers)
                              eeg=40e-6,      # unit: V (EEG channels)
                              eog=250e-6      # unit: V (EOG channels)
                              )

            .. note:: Since rejection is based on a signal **difference**
                      calculated for each channel separately, applying baseline
                      correction does not affect the rejection procedure, as the
                      difference will be preserved.

            If ``reject`` is ``None``, no rejection is performed. If ``'existing'``
            (default), then the rejection parameters set at instantiation are used.

        flat : dict | str | None
            Reject epochs based on **minimum** peak-to-peak signal amplitude (PTP).
            Valid **keys** can be any channel type present in the object. The
            **values** are floats that set the minimum acceptable PTP. If the PTP
            is smaller than this threshold, the epoch will be dropped. If ``None``
            then no rejection is performed based on flatness of the signal.
            If ``'existing'``, then the flat parameters set during epoch creation are
            used.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        epochs : instance of Epochs
            The epochs with bad epochs dropped. Operates in-place.

        Notes
        -----
        Dropping bad epochs can be done multiple times with different
        ``reject`` and ``flat`` parameters. However, once an epoch is
        dropped, it is dropped forever, so if more lenient thresholds may
        subsequently be applied, `epochs.copy <mne.Epochs.copy>` should be
        used.
        """
        ...
    def drop_log_stats(self, ignore=("IGNORED",)):
        """Compute the channel stats based on a drop_log from Epochs.

        Parameters
        ----------
        ignore : list
            The drop reasons to ignore.

        Returns
        -------
        perc : float
            Total percentage of epochs dropped.

        See Also
        --------
        plot_drop_log
        """
        ...
    def plot_drop_log(
        self,
        threshold: int = 0,
        n_max_plot: int = 20,
        subject=None,
        color=(0.9, 0.9, 0.9),
        width: float = 0.8,
        ignore=("IGNORED",),
        show: bool = True,
    ):
        """Show the channel stats based on a drop_log from Epochs.

        Parameters
        ----------
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
        ...
    def plot_image(
        self,
        picks=None,
        sigma: float = 0.0,
        vmin=None,
        vmax=None,
        colorbar: bool = True,
        order=None,
        show: bool = True,
        units=None,
        scalings=None,
        cmap=None,
        fig=None,
        axes=None,
        overlay_times=None,
        combine=None,
        group_by=None,
        evoked: bool = True,
        ts_args=None,
        title=None,
        clear: bool = False,
    ):
        """Plot Event Related Potential / Fields image.

        Parameters
        ----------
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
            of the image. If it is an array of `int`, its length should
            match the number of good epochs. If it is a callable it should accept
            two positional parameters (``times`` and ``data``, where
            ``data.shape == (len(good_epochs), len(times))``) and return an
            `array <numpy.ndarray>` of indices that will sort ``data`` along
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
            `matplotlib.figure.Figure` instance to draw the image to.
            Figure must contain the correct number of axes for drawing the epochs
            image, the evoked response, and a colorbar (depending on values of
            ``evoked`` and ``colorbar``). If ``None`` a new figure is created.
            Defaults to ``None``.
        axes : list of Axes | dict of list of Axes | None
            List of `matplotlib.axes.Axes` objects in which to draw the
            image, evoked response, and colorbar (in that order). Length of list
            must be 1, 2, or 3 (depending on values of ``colorbar`` and ``evoked``
            parameters). If a `dict`, each entry must be a list of Axes
            objects with the same constraints as above. If both ``axes`` and
            ``group_by`` are dicts, their keys must match. Providing non-``None``
            values for both ``fig`` and ``axes``  results in an error. Defaults to
            ``None``.
        overlay_times : array_like, shape (n_epochs,) | None
            Times (in seconds) at which to draw a line on the corresponding row of
            the image (e.g., a reaction time associated with each epoch). Note that
            ``overlay_times`` should be ordered to correspond with the
            `mne.Epochs` object (i.e., ``overlay_times[0]`` corresponds to
            ``epochs[0]``, etc).

        combine : None | str | callable
            How to combine information across channels. If a `str`, must be
            one of 'mean', 'median', 'std' (standard deviation) or 'gfp' (global
            field power).
            If callable, the callable must accept one positional input (data of
            shape ``(n_epochs, n_channels, n_times)``) and return an
            `array <numpy.ndarray>` of shape ``(n_epochs, n_times)``. For
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
            ``None``, one `matplotlib.figure.Figure` is made per dict
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
            Arguments passed to a call to `mne.viz.plot_compare_evokeds` to style
            the evoked plot below the image. Defaults to an empty dictionary,
            meaning `mne.viz.plot_compare_evokeds` will be called with default
            parameters.
        title : None | str
            If `str`, will be plotted as figure title. Otherwise, the
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
        ``combine`` parameters. If ``group_by`` is a `dict`, the result is
        one `matplotlib.figure.Figure` per dictionary key (for any valid
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
        ...
    def drop(self, indices, reason: str = "USER", verbose=None):
        """Drop epochs based on indices or boolean mask.

        .. note:: The indices refer to the current set of undropped epochs
                  rather than the complete set of dropped and undropped epochs.
                  They are therefore not necessarily consistent with any
                  external indices (e.g., behavioral logs). To drop epochs
                  based on external criteria, do not use the ``preload=True``
                  flag when constructing an Epochs object, and call this
                  method before calling the `mne.Epochs.drop_bad` or
                  `mne.Epochs.load_data` methods.

        Parameters
        ----------
        indices : array of int or bool
            Set epochs to remove by specifying indices to remove or a boolean
            mask to apply (where True values get removed). Events are
            correspondingly modified.
        reason : str
            Reason for dropping the epochs ('ECG', 'timeout', 'blink' etc).
            Default: 'USER'.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        epochs : instance of Epochs
            The epochs with indices dropped. Operates in-place.
        """
        ...
    def get_data(
        self,
        picks=None,
        item=None,
        units=None,
        tmin=None,
        tmax=None,
        *,
        copy=None,
        verbose=None,
    ):
        """Get all epochs as a 3D array.

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
        item : slice | array-like | str | list | None
            The items to get. See `mne.Epochs.__getitem__` for
            a description of valid options. This can be substantially faster
            for obtaining an ndarray than `mne.Epochs.__getitem__`
            for repeated access on large Epochs objects.
            None (default) is an alias for ``slice(None)``.

            .. versionadded:: 0.20

        units : str | dict | None
            Specify the unit(s) that the data should be returned in. If
            ``None`` (default), the data is returned in the
            channel-type-specific default units, which are SI units (see
            :ref:`units` and :term:`data channels`). If a string, must be a
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

            .. versionadded:: 0.24
        tmin : int | float | None
            Start time of data to get in seconds.

            .. versionadded:: 0.24.0
        tmax : int | float | None
            End time of data to get in seconds.

            .. versionadded:: 0.24.0
        copy : bool
            Whether to return a copy of the object's data, or (if possible) a view.
            See :ref:`the NumPy docs <numpy:basics.copies-and-views>` for an
            explanation. Default is ``False`` in 1.6 but will change to ``True`` in 1.7,
            set it explicitly to avoid a warning in some cases. A view is only possible
            when ``item is None``, ``picks is None``, ``units is None``, and data are
            preloaded.

            .. warning::
               Using ``copy=False`` and then modifying the returned ``data`` will in
               turn modify the Epochs object. Use with caution!

            .. versionchanged:: 1.7
               The default changed from ``False`` to ``True``.

            .. versionadded:: 1.6

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        data : array of shape (n_epochs, n_channels, n_times)
            The epochs data. Will be a copy when ``copy=True`` and will be a view
            when possible when ``copy=False``.
        """
        ...
    def apply_function(
        self,
        fun,
        picks=None,
        dtype=None,
        n_jobs=None,
        channel_wise: bool = True,
        verbose=None,
        **kwargs,
    ):
        """Apply a function to a subset of channels.

        The function ``fun`` is applied to the channels defined in ``picks``.
        The epochs object's data is modified in-place. If the function returns a different
        data type (e.g. :py:obj:`numpy.complex128`) it must be specified
        using the ``dtype`` parameter, which causes the data type of **all** the data
        to change (even if the function is only applied to channels in ``picks``). The object has to have the data loaded e.g. with ``preload=True`` or ``self.load_data()``.

        .. note:: If ``n_jobs`` > 1, more memory is required as
                  ``len(picks) * n_times`` additional time points need to
                  be temporarily stored in memory.
        .. note:: If the data type changes (``dtype != None``), more memory is
                  required since the original and the converted data needs
                  to be stored in memory.

        Parameters
        ----------

        fun : callable
            A function to be applied to the channels. The first argument of
            fun has to be a timeseries (`numpy.ndarray`). The function must
            operate on an array of shape ``(n_times,)``  if ``channel_wise=True`` and ``(len(picks), n_times)`` otherwise.
            The function must return an `numpy.ndarray` shaped like its input.
        picks : str | array-like | slice | None
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel *type* strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick all data channels (excluding reference
            MEG channels). Note that channels in ``info['bads']`` *will be included* if
            their names or indices are explicitly provided.

        dtype : numpy.dtype
            Data type to use after applying the function. If None
            (default) the data type is not modified.
        n_jobs : int | None
            The number of jobs to run in parallel. If ``-1``, it is set
            to the number of CPU cores. Requires the `joblib` package.
            ``None`` (default) is a marker for 'unset' that will be interpreted
            as ``n_jobs=1`` (sequential execution) unless the call is performed under
            a `joblib:joblib.parallel_config` context manager that sets another
            value for ``n_jobs``. Ignored if ``channel_wise=False`` as the workload
            is split across channels.

        channel_wise : bool
            Whether to apply the function to each channel in each epoch individually. If ``False``,
            the function will be applied to all epochs and channels at once. Default ``True``.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        **kwargs : dict
            Additional keyword arguments to pass to ``fun``.

        Returns
        -------
        self : instance of Epochs
            The epochs object with transformed data.
        """
        ...
    @property
    def filename(self):
        """The filename."""
        ...
    def crop(self, tmin=None, tmax=None, include_tmax: bool = True, verbose=None):
        """Crop a time interval from the epochs.

        Parameters
        ----------
        tmin : float | None
            Start time of selection in seconds.
        tmax : float | None
            End time of selection in seconds.

        include_tmax : bool
            If True (default), include tmax. If False, exclude tmax (similar to how
            Python indexing typically works).

            .. versionadded:: 0.19

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        epochs : instance of Epochs
            The cropped epochs object, modified in-place.

        Notes
        -----

        Unlike Python slices, MNE time intervals by default include **both**
        their end points; ``crop(tmin, tmax)`` returns the interval
        ``tmin <= t <= tmax``. Pass ``include_tmax=False`` to specify the half-open
        interval ``tmin <= t < tmax`` instead.
        """
        ...
    def copy(self):
        """Return copy of Epochs instance.

        Returns
        -------
        epochs : instance of Epochs
            A copy of the object.
        """
        ...
    def __deepcopy__(self, memodict):
        """Make a deepcopy."""
        ...
    def save(
        self,
        fname,
        split_size: str = "2GB",
        fmt: str = "single",
        overwrite: bool = False,
        split_naming: str = "neuromag",
        verbose=None,
    ) -> None:
        """Save epochs in a fif file.

        Parameters
        ----------
        fname : path-like
            The name of the file, which should end with ``-epo.fif`` or
            ``-epo.fif.gz``.
        split_size : str | int
            Large raw files are automatically split into multiple pieces. This
            parameter specifies the maximum size of each piece. If the
            parameter is an integer, it specifies the size in Bytes. It is
            also possible to pass a human-readable string, e.g., 100MB.
            Note: Due to FIFF file limitations, the maximum split size is 2GB.

            .. versionadded:: 0.10.0
        fmt : str
            Format to save data. Valid options are 'double' or
            'single' for 64- or 32-bit float, or for 128- or
            64-bit complex numbers respectively. Note: Data are processed with
            double precision. Choosing single-precision, the saved data
            will slightly differ due to the reduction in precision.

            .. versionadded:: 0.17

        overwrite : bool
            If True (default False), overwrite the destination file if it
            exists.
            To overwrite original file (the same one that was loaded),
            data must be preloaded upon reading. This defaults to True in 0.18
            but will change to False in 0.19.

            .. versionadded:: 0.18

        split_naming : 'neuromag' | 'bids'
            When splitting files, append a filename partition with the appropriate
            naming schema: for ``'neuromag'``, a split file ``fname.fif`` will be named
            ``fname.fif``, ``fname-1.fif``, ``fname-2.fif`` etc.; while for ``'bids'``,
            it will be named ``fname_split-01.fif``, ``fname_split-02.fif``, etc.

            .. versionadded:: 0.24

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        Notes
        -----
        Bad epochs will be dropped before saving the epochs to disk.
        """
        ...
    def export(
        self, fname, fmt: str = "auto", *, overwrite: bool = False, verbose=None
    ) -> None:
        """Export Epochs to external formats.

        Supported formats:
            - EEGLAB (``.set``, uses `eeglabio`)

        .. warning::
            Since we are exporting to external formats, there's no guarantee that all
            the info will be preserved in the external format. See Notes for details.

        Parameters
        ----------

        fname : str
            Name of the output file.

        fmt : 'auto' | 'eeglab'
            Format of the export. Defaults to ``'auto'``, which will infer the format
            from the filename extension. See supported formats above for more
            information.

        overwrite : bool
            If True (default False), overwrite the destination file if it
            exists.

            .. versionadded:: 0.24.1

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        Notes
        -----
        .. versionadded:: 0.24

        Export to external format may not preserve all the information from the
        instance. To save in native MNE format (``.fif``) without information loss,
        use `mne.Epochs.save` instead.
        Export does not apply projector(s). Unapplied projector(s) will be lost.
        Consider applying projector(s) before exporting with
        `mne.Epochs.apply_proj`.

        For EEGLAB exports, channel locations are expanded to full EEGLAB format.
        For more details see `eeglabio.utils.cart_to_eeglab`.
        """
        ...
    def equalize_event_counts(self, event_ids=None, method: str = "mintime"):
        """Equalize the number of trials in each condition.

        It tries to make the remaining epochs occurring as close as possible in
        time. This method works based on the idea that if there happened to be
        some time-varying (like on the scale of minutes) noise characteristics
        during a recording, they could be compensated for (to some extent) in
        the equalization process. This method thus seeks to reduce any of
        those effects by minimizing the differences in the times of the events
        within a `mne.Epochs` instance. For example, if one event type
        occurred at time points ``[1, 2, 3, 4, 120, 121]`` and the another one
        at ``[3.5, 4.5, 120.5, 121.5]``, this method would remove the events at
        times ``[1, 2]`` for the first event type – and not the events at times
        ``[120, 121]``.

        Parameters
        ----------
        event_ids : None | list | dict
            The event types to equalize.

            If ``None`` (default), equalize the counts of **all** event types
            present in the `mne.Epochs` instance.

            If a list, each element can either be a string (event name) or a
            list of strings. In the case where one of the entries is a list of
            strings, event types in that list will be grouped together before
            equalizing trial counts across conditions.

            If a dictionary, the keys are considered as the event names whose
            counts to equalize, i.e., passing ``dict(A=1, B=2)`` will have the
            same effect as passing ``['A', 'B']``. This is useful if you intend
            to pass an ``event_id`` dictionary that was used when creating
            `mne.Epochs`.

            In the case where partial matching is used (using ``/`` in
            the event names), the event types will be matched according to the
            provided tags, that is, processing works as if the ``event_ids``
            matched by the provided tags had been supplied instead.
            The ``event_ids`` must identify non-overlapping subsets of the
            epochs.
        method : str
            If ``'truncate'``, events will be truncated from the end of each
            type of events. If ``'mintime'``, timing differences between each
            event type will be minimized.

        Returns
        -------
        epochs : instance of Epochs
            The modified instance. It is modified in-place.
        indices : array of int
            Indices from the original events list that were dropped.

        Notes
        -----
        For example (if ``epochs.event_id`` was ``{'Left': 1, 'Right': 2,
        'Nonspatial':3}``:

            epochs.equalize_event_counts([['Left', 'Right'], 'Nonspatial'])

        would equalize the number of trials in the ``'Nonspatial'`` condition
        with the total number of trials in the ``'Left'`` and ``'Right'``
        conditions combined.

        If multiple indices are provided (e.g. ``'Left'`` and ``'Right'`` in
        the example above), it is not guaranteed that after equalization the
        conditions will contribute equally. E.g., it is possible to end up
        with 70 ``'Nonspatial'`` epochs, 69 ``'Left'`` and 1 ``'Right'``.

        .. versionchanged:: 0.23
            Default to equalizing all events in the passed instance if no
            event names were specified explicitly.
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
        """Perform spectral analysis on sensor data.

        Parameters
        ----------

        method : ``'welch'`` | ``'multitaper'``
            Spectral estimation method. ``'welch'`` uses Welch's
            method :footcite:p:`Welch1967`, ``'multitaper'`` uses DPSS
            tapers :footcite:p:`Slepian1978`.
            Default is ``'multitaper'``.
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

        remove_dc : bool
            If ``True``, the mean is subtracted from each segment before computing
            its spectrum.
        exclude : list of str | 'bads'
            Channel names to exclude. If ``'bads'``, channels
            in ``info['bads']`` are excluded; pass an empty list to
            include all channels (including "bad" channels, if any).
        n_jobs : int | None
            The number of jobs to run in parallel. If ``-1``, it is set
            to the number of CPU cores. Requires the `joblib` package.
            ``None`` (default) is a marker for 'unset' that will be interpreted
            as ``n_jobs=1`` (sequential execution) unless the call is performed under
            a `joblib:joblib.parallel_config` context manager that sets another
            value for ``n_jobs``.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
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
        spectrum : instance of EpochsSpectrum
            The spectral representation of each epoch.

        Notes
        -----
        .. versionadded:: 1.2

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
        """Plot power or amplitude spectra.

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

            .. versionadded:: 0.20
            .. versionchanged:: 1.1 Added ``'eeglab'`` option.

            .. versionadded:: 0.22.0
        exclude : list of str | 'bads'
            Channels names to exclude from being shown. If 'bads', the bad
            channels are excluded. Pass an empty list to plot all channels
            (including channels marked "bad", if any).

            .. versionadded:: 0.24.0
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
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
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
        """Export data in tabular structure as a pandas DataFrame.

        Channels are converted to columns in the DataFrame. By default,
        additional columns "time", "epoch" (epoch number), and "condition"
        (epoch event description) are added, unless ``index`` is not ``None``
        (in which case the columns specified in ``index`` will be used to form
        the DataFrame's index instead).

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
            integer index (`pandas.RangeIndex`) will be used. If ``'time'``, a
            ``pandas.Index`` or `pandas.TimedeltaIndex` will be used
            (depending on the value of ``time_format``). If a list of two or more string values, a `pandas.MultiIndex` will be created.
            Valid string values are 'time', 'epoch', and 'condition'.
            Defaults to ``None``.

        scalings : dict | None
            Scaling factor applied to the channels picked. If ``None``, defaults to
            ``dict(eeg=1e6, mag=1e15, grad=1e13)`` — i.e., converts EEG to µV,
            magnetometers to fT, and gradiometers to fT/cm.

        copy : bool
            If ``True``, data will be copied. Otherwise data may be modified in place.
            Defaults to ``True``.

        long_format : bool
            If True, the DataFrame is returned in long format where each row is one
            observation of the signal at a unique combination of time point, channel, epoch number, and condition.
            For convenience, a ``ch_type`` column is added to facilitate subsetting the resulting DataFrame. Defaults to ``False``.

        time_format : str | None
            Desired time format. If ``None``, no conversion is applied, and time values
            remain as float values in seconds. If ``'ms'``, time values will be rounded
            to the nearest millisecond and converted to integers. If ``'timedelta'``,
            time values will be converted to `pandas.Timedelta` values.
            Default is ``None``.

            .. versionadded:: 0.20

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------

        df : instance of pandas.DataFrame
            A dataframe suitable for usage with other statistical/plotting/analysis
            packages.
        """
        ...
    def as_type(self, ch_type: str = "grad", mode: str = "fast"):
        """Compute virtual epochs using interpolated fields.

        .. Warning:: Using virtual epochs to compute inverse can yield
            unexpected results. The virtual channels have ``'_v'`` appended
            at the end of the names to emphasize that the data contained in
            them are interpolated.

        Parameters
        ----------
        ch_type : str
            The destination channel type. It can be 'mag' or 'grad'.
        mode : str
            Either ``'accurate'`` or ``'fast'``, determines the quality of the
            Legendre polynomial expansion used. ``'fast'`` should be sufficient
            for most applications.

        Returns
        -------
        epochs : instance of mne.EpochsArray
            The transformed epochs object containing only virtual channels.

        Notes
        -----
        This method returns a copy and does not modify the data it
        operates on. It also returns an EpochsArray instance.

        .. versionadded:: 0.20.0
        """
        ...

def make_metadata(
    events,
    event_id,
    tmin,
    tmax,
    sfreq,
    row_events=None,
    keep_first=None,
    keep_last=None,
):
    """Automatically generate metadata for use with `mne.Epochs` from events.

    This function mimics the epoching process (it constructs time windows
    around time-locked "events of interest") and collates information about
    any other events that occurred within those time windows. The information
    is returned as a `pandas.DataFrame`, suitable for use as
    `mne.Epochs` metadata: one row per time-locked event, and columns
    indicating presence or absence and latency of each ancillary event type.

    The function will also return a new ``events`` array and ``event_id``
    dictionary that correspond to the generated metadata, which together can then be
    readily fed into `mne.Epochs`.

    Parameters
    ----------
    events : array, shape (m, 3)
        The :term:`events array <events>`. By default, the returned metadata
        `pandas.DataFrame` will have as many rows as the events array.
        To create rows for only a subset of events, pass the ``row_events``
        parameter.
    event_id : dict
        A mapping from event names (keys) to event IDs (values). The event
        names will be incorporated as columns of the returned metadata
        `pandas.DataFrame`.
    tmin, tmax : float | None
        Start and end of the time interval for metadata generation in seconds, relative
        to the time-locked event of the respective time window (the "row events").

        .. note::
           If you are planning to attach the generated metadata to
           `mne.Epochs` and intend to include only events that fall inside
           your epochs time interval, pass the same ``tmin`` and ``tmax``
           values here as you use for your epochs.

        If ``None``, the time window used for metadata generation is bounded by the
        ``row_events``. This is can be particularly practical if trial duration varies
        greatly, but each trial starts with a known event (e.g., a visual cue or
        fixation).

        .. note::
           If ``tmin=None``, the first time window for metadata generation starts with
           the first row event. If ``tmax=None``, the last time window for metadata
           generation ends with the last event in ``events``.

        .. versionchanged:: 1.6.0
           Added support for ``None``.
    sfreq : float
        The sampling frequency of the data from which the events array was
        extracted.
    row_events : list of str | str | None
        Event types around which to create the time windows. For each of these
        time-locked events, we will create a **row** in the returned metadata
        `pandas.DataFrame`. If provided, the string(s) must be keys of
        ``event_id``. If ``None`` (default), rows are created for **all** event types
        present in ``event_id``.
    keep_first : str | list of str | None
        Specify subsets of :term:`hierarchical event descriptors` (HEDs,
        inspired by :footcite:`BigdelyShamloEtAl2013`) matching events of which
        the **first occurrence** within each time window shall be stored in
        addition to the original events.

        .. note::
           There is currently no way to retain **all** occurrences of a
           repeated event. The ``keep_first`` parameter can be used to specify
           subsets of HEDs, effectively creating a new event type that is the
           union of all events types described by the matching HED pattern.
           Only the very first event of this set will be kept.

        For example, you might have two response events types,
        ``response/left`` and ``response/right``; and in trials with both
        responses occurring, you want to keep only the first response. In this
        case, you can pass ``keep_first='response'``. This will add two new
        columns to the metadata: ``response``, indicating at what **time** the
        event  occurred, relative to the time-locked event; and
        ``first_response``, stating which **type** (``'left'`` or ``'right'``)
        of event occurred.
        To match specific subsets of HEDs describing different sets of events,
        pass a list of these subsets, e.g.
        ``keep_first=['response', 'stimulus']``. If ``None`` (default), no
        event aggregation will take place and no new columns will be created.

        .. note::
           By default, this function will always retain  the first instance
           of any event in each time window. For example, if a time window
           contains two ``'response'`` events, the generated ``response``
           column will automatically refer to the first of the two events. In
           this specific case, it is therefore **not** necessary to make use of
           the ``keep_first`` parameter – unless you need to differentiate
           between two types of responses, like in the example above.

    keep_last : list of str | None
        Same as ``keep_first``, but for keeping only the **last**  occurrence
        of matching events. The column indicating the **type** of an event
        ``myevent`` will be named ``last_myevent``.

    Returns
    -------
    metadata : pandas.DataFrame
        Metadata for each row event, with the following columns:

        - ``event_name``, with strings indicating the name of the time-locked
          event ("row event") for that specific time window

        - one column per event type in ``event_id``, with the same name; floats
          indicating the latency of the event in seconds, relative to the
          time-locked event

        - if applicable, additional columns named after the ``keep_first`` and
          ``keep_last`` event types; floats indicating the latency  of the
          event in seconds, relative to the time-locked event

        - if applicable, additional columns ``first_{event_type}`` and
          ``last_{event_type}`` for ``keep_first`` and ``keep_last`` event
          types, respetively; the values will be strings indicating which event
          types were matched by the provided HED patterns

    events : array, shape (n, 3)
        The events corresponding to the generated metadata, i.e. one
        time-locked event per row.
    event_id : dict
        The event dictionary corresponding to the new events array. This will
        be identical to the input dictionary unless ``row_events`` is supplied,
        in which case it will only contain the events provided there.

    Notes
    -----
    The time window used for metadata generation need not correspond to the
    time window used to create the `mne.Epochs`, to which the metadata will
    be attached; it may well be much shorter or longer, or not overlap at all,
    if desired. This can be useful, for example, to include events that
    occurred before or after an epoch, e.g. during the inter-trial interval.
    If either ``tmin``, ``tmax``, or both are ``None``, the time window will
    typically vary, too.

    .. versionadded:: 0.23

    References
    ----------
    .. footbibliography::
    """
    ...

class Epochs(BaseEpochs):
    """Epochs extracted from a Raw instance.

    Parameters
    ----------

    raw : Raw object
        An instance of `mne.io.Raw`.

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

    tmin, tmax : float
        Start and end time of the epochs in seconds, relative to the time-locked
        event. The closest or matching samples corresponding to the start and end
        time are included. Defaults to ``-0.2`` and ``0.5``, respectively.

    baseline : None | tuple of length 2
        The time interval to consider as "baseline" when applying baseline
        correction. If ``None``, do not apply baseline correction.
        If a tuple ``(a, b)``, the interval is between ``a`` and ``b``
        (in seconds), including the endpoints.
        If ``a`` is ``None``, the **beginning** of the data is used; and if ``b``
        is ``None``, it is set to the **end** of the interval.
        If ``(None, None)``, the entire time interval is used.

        .. note:: The baseline ``(a, b)`` includes both endpoints, i.e. all
                    timepoints ``t`` such that ``a <= t <= b``.

        Correction is applied **to each epoch and channel individually** in the
        following way:

        1. Calculate the mean signal of the baseline period.
        2. Subtract this mean from the **entire** epoch.

        Defaults to ``(None, 0)``, i.e. beginning of the the data until
        time point zero.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick all channels. Note that channels in
        ``info['bads']`` *will be included* if their names or indices are
        explicitly provided.
    preload : bool

        Load all epochs from disk when creating the object
        or wait before accessing each epoch (more memory
        efficient but can be slower).

    reject : dict | None
        Reject epochs based on **maximum** peak-to-peak signal amplitude (PTP),
        i.e. the absolute difference between the lowest and the highest signal
        value. In each individual epoch, the PTP is calculated for every channel.
        If the PTP of any one channel exceeds the rejection threshold, the
        respective epoch will be dropped.

        The dictionary keys correspond to the different channel types; valid
        **keys** can be any channel type present in the object.

        Example::

            reject = dict(grad=4000e-13,  # unit: T / m (gradiometers)
                          mag=4e-12,      # unit: T (magnetometers)
                          eeg=40e-6,      # unit: V (EEG channels)
                          eog=250e-6      # unit: V (EOG channels)
                          )

        .. note:: Since rejection is based on a signal **difference**
                  calculated for each channel separately, applying baseline
                  correction does not affect the rejection procedure, as the
                  difference will be preserved.

        .. note:: To constrain the time period used for estimation of signal
                  quality, pass the ``reject_tmin`` and ``reject_tmax`` parameters.

        If ``reject`` is ``None`` (default), no rejection is performed.

    flat : dict | None
        Reject epochs based on **minimum** peak-to-peak signal amplitude (PTP).
        Valid **keys** can be any channel type present in the object. The
        **values** are floats that set the minimum acceptable PTP. If the PTP
        is smaller than this threshold, the epoch will be dropped. If ``None``
        then no rejection is performed based on flatness of the signal.

        .. note:: To constrain the time period used for estimation of signal
                  quality, pass the ``reject_tmin`` and ``reject_tmax`` parameters.

    proj : bool | 'delayed'
        Apply SSP projection vectors. If proj is 'delayed' and reject is not
        None the single epochs will be projected before the rejection
        decision, but used in unprojected state if they are kept.
        This way deciding which projection vectors are good can be postponed
        to the evoked stage without resulting in lower epoch counts and
        without producing results different from early SSP application
        given comparable parameters. Note that in this case baselining,
        detrending and temporal decimation will be postponed.
        If proj is False no projections will be applied which is the
        recommended value if SSPs are not used for cleaning the data.

    decim : int
        Factor by which to subsample the data.

        .. warning:: Low-pass filtering is not performed, this simply selects
                     every Nth sample (where N is the value passed to
                     ``decim``), i.e., it compresses the signal (see Notes).
                     If the data are not properly filtered, aliasing artifacts
                     may occur.

    reject_tmin, reject_tmax : float | None
        Start and end of the time window used to reject epochs based on
        peak-to-peak (PTP) amplitudes as specified via ``reject`` and ``flat``.
        The default ``None`` corresponds to the first and last time points of the
        epochs, respectively.

        .. note:: This parameter controls the time period used in conjunction with
                  both, ``reject`` and ``flat``.

    detrend : int | None
        If 0 or 1, the data channels (MEG and EEG) will be detrended when
        loaded. 0 is a constant (DC) detrend, 1 is a linear detrend. None
        is no detrending. Note that detrending is performed before baseline
        correction. If no DC offset is preferred (zeroth order detrending),
        either turn off baseline correction, as this may introduce a DC
        shift, or set baseline correction to use the entire time interval
        (will yield equivalent results but be slower).

    on_missing : 'raise' | 'warn' | 'ignore'
        What to do if one or several event ids are not found in the recording.
        Valid keys are 'raise' | 'warn' | 'ignore'
        Default is ``'raise'``. If ``'warn'``, it will proceed but
        warn; if ``'ignore'``, it will proceed silently.

        .. note::
           If none of the event ids are found in the data, an error will be
           automatically generated irrespective of this parameter.

    reject_by_annotation : bool
        Whether to reject based on annotations. If ``True`` (default), epochs
        overlapping with segments whose description begins with ``'bad'`` are
        rejected. If ``False``, no rejection based on annotations is performed.

    metadata : instance of pandas.DataFrame | None
        A `pandas.DataFrame` specifying metadata about each epoch.
        If given, ``len(metadata)`` must equal ``len(events)``. The DataFrame
        may only contain values of type (str | int | float | bool).
        If metadata is given, then pandas-style queries may be used to select
        subsets of data, see `mne.Epochs.__getitem__`.
        When a subset of the epochs is created in this (or any other
        supported) manner, the metadata object is subsetted accordingly, and
        the row indices will be modified to match ``epochs.selection``.

        .. versionadded:: 0.16

    event_repeated : str
        How to handle duplicates in ``events[:, 0]``. Can be ``'error'``
        (default), to raise an error, 'drop' to only retain the row occurring
        first in the :term:`events`, or ``'merge'`` to combine the coinciding
        events (=duplicates) into a new event (see Notes for details).

        .. versionadded:: 0.19

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Attributes
    ----------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    event_id : dict
        Names of conditions corresponding to event_ids.
    ch_names : list of string
        List of channel names.
    selection : array
        List of indices of selected events (not dropped or ignored etc.). For
        example, if the original event array had 4 events and the second event
        has been dropped, this attribute would be np.array([0, 2, 3]).
    preload : bool
        Indicates whether epochs are in memory.
    drop_log : tuple of tuple
        A tuple of the same length as the event array used to initialize the
        Epochs object. If the i-th original event is still part of the
        selection, drop_log[i] will be an empty tuple; otherwise it will be
        a tuple of the reasons the event is not longer in the selection, e.g.:

        - 'IGNORED'
            If it isn't part of the current subset defined by the user
        - 'NO_DATA' or 'TOO_SHORT'
            If epoch didn't contain enough data names of channels that exceeded
            the amplitude threshold
        - 'EQUALIZED_COUNTS'
            See `mne.Epochs.equalize_event_counts`
        - 'USER'
            For user-defined reasons (see `mne.Epochs.drop`).
    filename : str
        The filename of the object.
    times :  ndarray
        Time vector in seconds. Goes from ``tmin`` to ``tmax``. Time interval
        between consecutive time samples is equal to the inverse of the
        sampling frequency.

    See Also
    --------
    mne.epochs.combine_event_ids
    mne.Epochs.equalize_event_counts

    Notes
    -----
    When accessing data, Epochs are detrended, baseline-corrected, and
    decimated, then projectors are (optionally) applied.

    For indexing and slicing using ``epochs[...]``, see
    `mne.Epochs.__getitem__`.

    All methods for iteration over objects (using `mne.Epochs.__iter__`,
    `mne.Epochs.iter_evoked` or `mne.Epochs.next`) use the same
    internal state.

    If ``event_repeated`` is set to ``'merge'``, the coinciding events
    (duplicates) will be merged into a single event_id and assigned a new
    id_number as::

        event_id['{event_id_1}/{event_id_2}/...'] = new_id_number

    For example with the event_id ``{'aud': 1, 'vis': 2}`` and the events
    ``[[0, 0, 1], [0, 0, 2]]``, the "merge" behavior will update both event_id
    and events to be: ``{'aud/vis': 3}`` and ``[[0, 0, 3]]`` respectively.

    There is limited support for `mne.Annotations` in the
    `mne.Epochs` class. Currently annotations that are present in the
    `mne.io.Raw` object will be preserved in the resulting
    `mne.Epochs` object, but:

    1. It is not yet possible to add annotations
       to the Epochs object programmatically (via code) or interactively
       (through the plot window)
    2. Concatenating `mne.Epochs` objects
       that contain annotations is not supported, and any annotations will
       be dropped when concatenating.
    3. Annotations will be lost on save.
    """

    reject_by_annotation: Incomplete

    def __init__(
        self,
        raw,
        events,
        event_id=None,
        tmin: float = -0.2,
        tmax: float = 0.5,
        baseline=(None, 0),
        picks=None,
        preload: bool = False,
        reject=None,
        flat=None,
        proj: bool = True,
        decim: int = 1,
        reject_tmin=None,
        reject_tmax=None,
        detrend=None,
        on_missing: str = "raise",
        reject_by_annotation: bool = True,
        metadata=None,
        event_repeated: str = "error",
        verbose=None,
    ) -> None: ...

class EpochsArray(BaseEpochs):
    """Epochs object from numpy array.

    Parameters
    ----------
    data : array, shape (n_epochs, n_channels, n_times)
        The channels' time series for each epoch. See notes for proper units of
        measure.

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement. Consider using `mne.create_info` to populate this
        structure.

    events : array of int, shape (n_events, 3)
        The array of :term:`events`. The first column contains the event time in
        samples, with :term:`first_samp` included. The third column contains the
        event id.
        If some events don't match the events of interest as specified by
        ``event_id``, they will be marked as ``IGNORED`` in the drop log.

    tmin : float
        Start time before event. If nothing provided, defaults to 0.

    event_id : int | list of int | dict | None
        The id of the :term:`events` to consider. If dict, the keys can later be
        used to access associated :term:`events`. Example:
        dict(auditory=1, visual=3). If int, a dict will be created with the id as
        string. If a list, all :term:`events` with the IDs specified in the list
        are used. If None, all :term:`events` will be used and a dict is created
        with string integer names corresponding to the event id integers.

    reject : dict | None
        Reject epochs based on **maximum** peak-to-peak signal amplitude (PTP),
        i.e. the absolute difference between the lowest and the highest signal
        value. In each individual epoch, the PTP is calculated for every channel.
        If the PTP of any one channel exceeds the rejection threshold, the
        respective epoch will be dropped.

        The dictionary keys correspond to the different channel types; valid
        **keys** can be any channel type present in the object.

        Example::

            reject = dict(grad=4000e-13,  # unit: T / m (gradiometers)
                          mag=4e-12,      # unit: T (magnetometers)
                          eeg=40e-6,      # unit: V (EEG channels)
                          eog=250e-6      # unit: V (EOG channels)
                          )

        .. note:: Since rejection is based on a signal **difference**
                  calculated for each channel separately, applying baseline
                  correction does not affect the rejection procedure, as the
                  difference will be preserved.

        .. note:: To constrain the time period used for estimation of signal
                  quality, pass the ``reject_tmin`` and ``reject_tmax`` parameters.

        If ``reject`` is ``None`` (default), no rejection is performed.

    flat : dict | None
        Reject epochs based on **minimum** peak-to-peak signal amplitude (PTP).
        Valid **keys** can be any channel type present in the object. The
        **values** are floats that set the minimum acceptable PTP. If the PTP
        is smaller than this threshold, the epoch will be dropped. If ``None``
        then no rejection is performed based on flatness of the signal.

        .. note:: To constrain the time period used for estimation of signal
                  quality, pass the ``reject_tmin`` and ``reject_tmax`` parameters.

    reject_tmin, reject_tmax : float | None
        Start and end of the time window used to reject epochs based on
        peak-to-peak (PTP) amplitudes as specified via ``reject`` and ``flat``.
        The default ``None`` corresponds to the first and last time points of the
        epochs, respectively.

        .. note:: This parameter controls the time period used in conjunction with
                  both, ``reject`` and ``flat``.

    baseline : None | tuple of length 2
        The time interval to consider as "baseline" when applying baseline
        correction. If ``None``, do not apply baseline correction.
        If a tuple ``(a, b)``, the interval is between ``a`` and ``b``
        (in seconds), including the endpoints.
        If ``a`` is ``None``, the **beginning** of the data is used; and if ``b``
        is ``None``, it is set to the **end** of the interval.
        If ``(None, None)``, the entire time interval is used.

        .. note:: The baseline ``(a, b)`` includes both endpoints, i.e. all
                    timepoints ``t`` such that ``a <= t <= b``.

        Correction is applied **to each epoch and channel individually** in the
        following way:

        1. Calculate the mean signal of the baseline period.
        2. Subtract this mean from the **entire** epoch.

        Defaults to ``None``, i.e. no baseline correction.

    proj : bool | 'delayed'
        Apply SSP projection vectors. If proj is 'delayed' and reject is not
        None the single epochs will be projected before the rejection
        decision, but used in unprojected state if they are kept.
        This way deciding which projection vectors are good can be postponed
        to the evoked stage without resulting in lower epoch counts and
        without producing results different from early SSP application
        given comparable parameters. Note that in this case baselining,
        detrending and temporal decimation will be postponed.
        If proj is False no projections will be applied which is the
        recommended value if SSPs are not used for cleaning the data.

    on_missing : 'raise' | 'warn' | 'ignore'
        What to do if one or several event ids are not found in the recording.
        Valid keys are 'raise' | 'warn' | 'ignore'
        Default is ``'raise'``. If ``'warn'``, it will proceed but
        warn; if ``'ignore'``, it will proceed silently.

        .. note::
           If none of the event ids are found in the data, an error will be
           automatically generated irrespective of this parameter.

    metadata : instance of pandas.DataFrame | None
        A `pandas.DataFrame` specifying metadata about each epoch.
        If given, ``len(metadata)`` must equal ``len(events)``. The DataFrame
        may only contain values of type (str | int | float | bool).
        If metadata is given, then pandas-style queries may be used to select
        subsets of data, see `mne.Epochs.__getitem__`.
        When a subset of the epochs is created in this (or any other
        supported) manner, the metadata object is subsetted accordingly, and
        the row indices will be modified to match ``epochs.selection``.

        .. versionadded:: 0.16

    selection : iterable | None
        Iterable of indices of selected epochs. If ``None``, will be
        automatically generated, corresponding to all non-zero events.

    drop_log : tuple | None
        Tuple of tuple of strings indicating which epochs have been marked to
        be ignored.

        .. versionadded:: 1.3

    raw_sfreq : float
        The original Raw object sampling rate. If None, then it is set to
        ``info['sfreq']``.

        .. versionadded:: 1.3

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    create_info
    EvokedArray
    io.RawArray

    Notes
    -----
    Proper units of measure:

    * V: eeg, eog, seeg, dbs, emg, ecg, bio, ecog
    * T: mag
    * T/m: grad
    * M: hbo, hbr
    * Am: dipole
    * AU: misc

    EpochsArray does not set `Annotations`. If you would like to create
    simulated data with Annotations that are then preserved in the Epochs
    object, you would use `mne.io.RawArray` first and then create an
    `mne.Epochs` object.
    """

    def __init__(
        self,
        data,
        info,
        events=None,
        tmin: int = 0,
        event_id=None,
        reject=None,
        flat=None,
        reject_tmin=None,
        reject_tmax=None,
        baseline=None,
        proj: bool = True,
        on_missing: str = "raise",
        metadata=None,
        selection=None,
        *,
        drop_log=None,
        raw_sfreq=None,
        verbose=None,
    ) -> None: ...

def combine_event_ids(epochs, old_event_ids, new_event_id, copy: bool = True):
    """Collapse event_ids from an epochs instance into a new event_id.

    Parameters
    ----------
    epochs : instance of Epochs
        The epochs to operate on.
    old_event_ids : str, or list
        Conditions to collapse together.
    new_event_id : dict, or int
        A one-element dict (or a single integer) for the new
        condition. Note that for safety, this cannot be any
        existing id (in epochs.event_id.values()).
    copy : bool
        Whether to return a new instance or modify in place.

    Returns
    -------
    epochs : instance of Epochs
        The modified epochs.

    Notes
    -----
    This For example (if epochs.event_id was ``{'Left': 1, 'Right': 2}``::

        combine_event_ids(epochs, ['Left', 'Right'], {'Directional': 12})

    would create a 'Directional' entry in epochs.event_id replacing
    'Left' and 'Right' (combining their trials).
    """
    ...

def equalize_epoch_counts(epochs_list, method: str = "mintime") -> None:
    """Equalize the number of trials in multiple Epoch instances.

    Parameters
    ----------
    epochs_list : list of Epochs instances
        The Epochs instances to equalize trial counts for.
    method : str
        If 'truncate', events will be truncated from the end of each event
        list. If 'mintime', timing differences between each event list will be
        minimized.

    Notes
    -----
    This tries to make the remaining epochs occurring as close as possible in
    time. This method works based on the idea that if there happened to be some
    time-varying (like on the scale of minutes) noise characteristics during
    a recording, they could be compensated for (to some extent) in the
    equalization process. This method thus seeks to reduce any of those effects
    by minimizing the differences in the times of the events in the two sets of
    epochs. For example, if one had event times [1, 2, 3, 4, 120, 121] and the
    other one had [3.5, 4.5, 120.5, 121.5], it would remove events at times
    [1, 2] in the first epochs and not [120, 121].

    Examples
    --------
    >>> equalize_epoch_counts([epochs1, epochs2])  # doctest: +SKIP
    """
    ...

def read_epochs(fname, proj: bool = True, preload: bool = True, verbose=None):
    """Read epochs from a fif file.

    Parameters
    ----------

    fname : path-like | file-like
        The epochs to load. If a filename, should end with ``-epo.fif`` or
        ``-epo.fif.gz``. If a file-like object, preloading must be used.

    proj : bool | 'delayed'
        Apply SSP projection vectors. If proj is 'delayed' and reject is not
        None the single epochs will be projected before the rejection
        decision, but used in unprojected state if they are kept.
        This way deciding which projection vectors are good can be postponed
        to the evoked stage without resulting in lower epoch counts and
        without producing results different from early SSP application
        given comparable parameters. Note that in this case baselining,
        detrending and temporal decimation will be postponed.
        If proj is False no projections will be applied which is the
        recommended value if SSPs are not used for cleaning the data.
    preload : bool
        If True, read all epochs from disk immediately. If ``False``, epochs
        will be read on demand.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    epochs : instance of Epochs
        The epochs.
    """
    ...

class _RawContainer:
    """Helper for a raw data container."""

    fid: Incomplete
    data_tag: Incomplete
    event_samps: Incomplete
    epoch_shape: Incomplete
    cals: Incomplete
    proj: bool
    fmt: Incomplete

    def __init__(self, fid, data_tag, event_samps, epoch_shape, cals, fmt) -> None: ...
    def __del__(self) -> None: ...

class EpochsFIF(BaseEpochs):
    """Epochs read from disk.

    Parameters
    ----------

    fname : path-like | file-like
        The epochs to load. If a filename, should end with ``-epo.fif`` or
        ``-epo.fif.gz``. If a file-like object, preloading must be used.

    proj : bool | 'delayed'
        Apply SSP projection vectors. If proj is 'delayed' and reject is not
        None the single epochs will be projected before the rejection
        decision, but used in unprojected state if they are kept.
        This way deciding which projection vectors are good can be postponed
        to the evoked stage without resulting in lower epoch counts and
        without producing results different from early SSP application
        given comparable parameters. Note that in this case baselining,
        detrending and temporal decimation will be postponed.
        If proj is False no projections will be applied which is the
        recommended value if SSPs are not used for cleaning the data.
    preload : bool
        If True, read all epochs from disk immediately. If False, epochs will
        be read on demand.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    mne.Epochs
    mne.epochs.combine_event_ids
    mne.Epochs.equalize_event_counts
    """

    baseline: Incomplete

    def __init__(
        self, fname, proj: bool = True, preload: bool = True, verbose=None
    ) -> None: ...

def bootstrap(epochs, random_state=None):
    """Compute epochs selected by bootstrapping.

    Parameters
    ----------
    epochs : Epochs instance
        epochs data to be bootstrapped

    random_state : None | int | instance of ~numpy.random.RandomState
        A seed for the NumPy random number generator (RNG). If ``None`` (default),
        the seed will be  obtained from the operating system
        (see  `numpy.random.RandomState` for details), meaning it will most
        likely produce different output every time this function or method is run.
        To achieve reproducible results, pass a value here to explicitly initialize
        the RNG with a defined state.

    Returns
    -------
    epochs : Epochs instance
        The bootstrap samples
    """
    ...

def concatenate_epochs(
    epochs_list, add_offset: bool = True, *, on_mismatch: str = "raise", verbose=None
):
    """Concatenate a list of `mne.Epochs` into one `mne.Epochs` object.

    .. note:: Unlike `mne.concatenate_raws`, this function does **not**
              modify any of the input data.

    Parameters
    ----------
    epochs_list : list
        List of `mne.Epochs` instances to concatenate (in that order).
    add_offset : bool
        If True, a fixed offset is added to the event times from different
        Epochs sets, such that they are easy to distinguish after the
        concatenation.
        If False, the event times are unaltered during the concatenation.

    on_mismatch : 'raise' | 'warn' | 'ignore'
        Can be ``'raise'`` (default) to raise an error, ``'warn'`` to emit a
        warning, or ``'ignore'`` to ignore when the device-to-head transformation differs between
        instances.

        .. versionadded:: 0.24

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

        .. versionadded:: 0.24

    Returns
    -------
    epochs : instance of EpochsArray
        The result of the concatenation. All data will be loaded into memory.

    Notes
    -----
    .. versionadded:: 0.9.0
    """
    ...

def average_movements(
    epochs,
    head_pos=None,
    orig_sfreq=None,
    picks=None,
    origin: str = "auto",
    weight_all: bool = True,
    int_order: int = 8,
    ext_order: int = 3,
    destination=None,
    ignore_ref: bool = False,
    return_mapping: bool = False,
    mag_scale: float = 100.0,
    verbose=None,
):
    """Average data using Maxwell filtering, transforming using head positions.

    Parameters
    ----------
    epochs : instance of Epochs
        The epochs to operate on.

    head_pos : array | None
        If array, movement compensation will be performed.
        The array should be of shape (N, 10), holding the position
        parameters as returned by e.g. ``read_head_pos``.
    orig_sfreq : float | None
        The original sample frequency of the data (that matches the
        event sample numbers in ``epochs.events``). Can be ``None``
        if data have not been decimated or resampled.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick all data channels. Note that channels
        in ``info['bads']`` *will be included* if their names or indices are
        explicitly provided.

    origin : array-like, shape (3,) | str
        Origin of internal and external multipolar moment space in meters.
        The default is ``'auto'``, which means ``(0., 0., 0.)`` when
        ``coord_frame='meg'``, and a head-digitization-based
        origin fit using `mne.bem.fit_sphere_to_headshape`
        when ``coord_frame='head'``. If automatic fitting fails (e.g., due
        to having too few digitization points),
        consider separately calling the fitting function with different
        options or specifying the origin manually.
    weight_all : bool
        If True, all channels are weighted by the SSS basis weights.
        If False, only MEG channels are weighted, other channels
        receive uniform weight per epoch.

    int_order : int
        Order of internal component of spherical expansion.

    ext_order : int
        Order of external component of spherical expansion.

    destination : path-like | array-like, shape (3,) | None
        The destination location for the head. Can be ``None``, which
        will not change the head position, or a path to a FIF file
        containing a MEG device<->head transformation, or a 3-element array
        giving the coordinates to translate to (with no rotations).
        For example, ``destination=(0, 0, 0.04)`` would translate the bases
        as ``--trans default`` would in MaxFilter™ (i.e., to the default
        head location).

    ignore_ref : bool
        If True, do not include reference channels in compensation. This
        option should be True for KIT files, since Maxwell filtering
        with reference channels is not currently supported.
    return_mapping : bool
        If True, return the mapping matrix.

    mag_scale : float | str
        The magenetometer scale-factor used to bring the magnetometers
        to approximately the same order of magnitude as the gradiometers
        (default 100.), as they have different units (T vs T/m).
        Can be ``'auto'`` to use the reciprocal of the physical distance
        between the gradiometer pickup loops (e.g., 0.0168 m yields
        59.5 for VectorView).

        .. versionadded:: 0.13

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    evoked : instance of Evoked
        The averaged epochs.

    See Also
    --------
    mne.preprocessing.maxwell_filter
    mne.chpi.read_head_pos

    Notes
    -----
    The Maxwell filtering version of this algorithm is described in [1]_,
    in section V.B "Virtual signals and movement correction", equations
    40-44. For additional validation, see [2]_.

    Regularization has not been added because in testing it appears to
    decrease dipole localization accuracy relative to using all components.
    Fine calibration and cross-talk cancellation, however, could be added
    to this algorithm based on user demand.

    .. versionadded:: 0.11

    References
    ----------
    .. [1] Taulu S. and Kajola M. "Presentation of electromagnetic
           multichannel data: The signal space separation method,"
           Journal of Applied Physics, vol. 97, pp. 124905 1-10, 2005.
    .. [2] Wehner DT, Hämäläinen MS, Mody M, Ahlfors SP. "Head movements
           of children in MEG: Quantification, effects on source
           estimation, and compensation. NeuroImage 40:541–550, 2008.
    """
    ...

def make_fixed_length_epochs(
    raw,
    duration: float = 1.0,
    preload: bool = False,
    reject_by_annotation: bool = True,
    proj: bool = True,
    overlap: float = 0.0,
    id: int = 1,
    verbose=None,
):
    """Divide continuous raw data into equal-sized consecutive epochs.

    Parameters
    ----------
    raw : instance of Raw
        Raw data to divide into segments.
    duration : float
        Duration of each epoch in seconds. Defaults to 1.

    preload : bool or str (default False)
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).

    reject_by_annotation : bool
        Whether to reject based on annotations. If ``True`` (default), epochs
        overlapping with segments whose description begins with ``'bad'`` are
        rejected. If ``False``, no rejection based on annotations is performed.

        .. versionadded:: 0.21.0

    proj : bool | 'delayed'
        Apply SSP projection vectors. If proj is 'delayed' and reject is not
        None the single epochs will be projected before the rejection
        decision, but used in unprojected state if they are kept.
        This way deciding which projection vectors are good can be postponed
        to the evoked stage without resulting in lower epoch counts and
        without producing results different from early SSP application
        given comparable parameters. Note that in this case baselining,
        detrending and temporal decimation will be postponed.
        If proj is False no projections will be applied which is the
        recommended value if SSPs are not used for cleaning the data.

        .. versionadded:: 0.22.0
    overlap : float
        The overlap between epochs, in seconds. Must be
        ``0 <= overlap < duration``. Default is 0, i.e., no overlap.

        .. versionadded:: 0.23.0
    id : int
        The id to use (default 1).

        .. versionadded:: 0.24.0

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    epochs : instance of Epochs
        Segmented data.

    Notes
    -----
    .. versionadded:: 0.20
    """
    ...
