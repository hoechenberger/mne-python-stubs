from .._fiff.compensator import (
    make_compensator as make_compensator,
    set_current_comp as set_current_comp,
)
from .._fiff.constants import FIFF as FIFF
from .._fiff.meas_info import (
    ContainsMixin as ContainsMixin,
    SetChannelsMixin as SetChannelsMixin,
    write_meas_info as write_meas_info,
)
from .._fiff.pick import (
    channel_type as channel_type,
    pick_channels as pick_channels,
    pick_info as pick_info,
    pick_types as pick_types,
)
from .._fiff.proj import (
    ProjMixin as ProjMixin,
    activate_proj as activate_proj,
    setup_proj as setup_proj,
)
from .._fiff.write import (
    end_block as end_block,
    start_and_end_file as start_and_end_file,
    start_block as start_block,
    write_complex128 as write_complex128,
    write_complex64 as write_complex64,
    write_dau_pack16 as write_dau_pack16,
    write_double as write_double,
    write_float as write_float,
    write_id as write_id,
    write_int as write_int,
    write_string as write_string,
)
from ..annotations import Annotations as Annotations
from ..channels.channels import (
    InterpolationMixin as InterpolationMixin,
    ReferenceMixin as ReferenceMixin,
    UpdateChannelsMixin as UpdateChannelsMixin,
)
from ..event import concatenate_events as concatenate_events, find_events as find_events
from ..filter import (
    FilterMixin as FilterMixin,
    notch_filter as notch_filter,
    resample as resample,
)
from ..parallel import parallel_func as parallel_func
from ..time_frequency.spectrum import (
    Spectrum as Spectrum,
    SpectrumMixin as SpectrumMixin,
)
from ..utils import (
    SizeMixin as SizeMixin,
    TimeMixin as TimeMixin,
    check_fname as check_fname,
    copy_doc as copy_doc,
    copy_function_doc_to_method_doc as copy_function_doc_to_method_doc,
    fill_doc as fill_doc,
    logger as logger,
    repr_html as repr_html,
    sizeof_fmt as sizeof_fmt,
    warn as warn,
)
from ..viz import plot_raw as plot_raw
from _typeshed import Incomplete
from dataclasses import dataclass

class BaseRaw(
    ProjMixin,
    ContainsMixin,
    UpdateChannelsMixin,
    ReferenceMixin,
    SetChannelsMixin,
    InterpolationMixin,
    TimeMixin,
    SizeMixin,
    FilterMixin,
    SpectrumMixin,
):
    """## 🧠 Base class for Raw data.

    -----
    ### 🛠️ Parameters


    #### `info : mne.Info`
        The `mne.Info` object with information about the sensors and methods of measurement.
    #### `preload : bool | str | ndarray`
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory). If preload is an
        ndarray, the data are taken from that array. If False, data are not
        read until save.
    #### `first_samps : iterable`
        Iterable of the first sample number from each raw file. For unsplit raw
        files this should be a length-one list or tuple.
    #### `last_samps : iterable | None`
        Iterable of the last sample number from each raw file. For unsplit raw
        files this should be a length-one list or tuple. If None, then preload
        must be an ndarray.
    #### `filenames : tuple`
        Tuple of length one (for unsplit raw files) or length > 1 (for split
        raw files).
    #### `raw_extras : list of dict`
        The data necessary for on-demand reads for the given reader format.
        Should be the same length as ``filenames``. Will have the entry
        ``raw_extras['orig_nchan']`` added to it for convenience.
    #### `orig_format : str`
        The data format of the original raw file (e.g., ``'double'``).
    #### `dtype : dtype | None`
        The dtype of the raw data. If preload is an ndarray, its dtype must
        match what is passed here.
    #### `buffer_size_sec : float`
        The buffer size in seconds that should be written by default using
        `mne.io.Raw.save`.
    #### `orig_units : dict | None`
        Dictionary mapping channel names to their units as specified in
        the header file. Example: {'FC1': 'nV'}.

        ✨ Added in vesion 0.17

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### 👉 See Also

    mne.io.Raw : Documentation of attributes and methods.

    -----
    ### 📖 Notes

    This class is public to allow for stable type-checking in user
    code (i.e., ``isinstance(my_raw_object, BaseRaw)``) but should not be used
    as a constructor for `Raw` objects (use instead one of the subclass
    constructors, or one of the ``mne.io.read_raw_*`` functions).

    Subclasses must provide the following methods:

        * _read_segment_file(self, data, idx, fi, start, stop, cals, mult)
          (only needed for types that support on-demand disk reads)
    """

    preload: bool
    info: Incomplete
    buffer_size_sec: Incomplete
    orig_format: Incomplete

    def __init__(
        self,
        info,
        preload: bool = False,
        first_samps=(0,),
        last_samps=None,
        filenames=(None,),
        raw_extras=(None,),
        orig_format: str = "double",
        dtype=...,
        buffer_size_sec: float = 1.0,
        orig_units=None,
        *,
        verbose=None,
    ) -> None: ...
    def apply_gradient_compensation(self, grade, verbose=None):
        """## 🧠 Apply CTF gradient compensation.

        ### ⛔️ Warning The compensation matrices are stored with single
                     precision, so repeatedly switching between different
                     of compensation (e.g., 0->1->3->2) can increase
                     numerical noise, especially if data are saved to
                     disk in between changing grades. It is thus best to
                     only use a single gradient compensation level in
                     final analyses.

        -----
        ### 🛠️ Parameters

        #### `grade : int`
            CTF gradient compensation level.

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns

        #### `raw : instance of Raw`
            The modified Raw instance. Works in-place.
        """
        ...
    def load_data(self, verbose=None):
        """## 🧠 Load raw data.

        -----
        ### 🛠️ Parameters


        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns

        #### `raw : instance of Raw`
            The raw object with data.

        -----
        ### 📖 Notes

        This function will load raw data if it was not already preloaded.
        If data were already preloaded, it will do nothing.

        ✨ Added in vesion 0.10.0
        """
        ...
    @property
    def first_samp(self):
        """## 🧠 The first data sample.

        See :term:`first_samp`.
        """
        ...
    @property
    def first_time(self):
        """## 🧠 The first time point (including first_samp but not meas_date)."""
        ...
    @property
    def last_samp(self):
        """## 🧠 The last data sample."""
        ...
    def time_as_index(self, times, use_rounding: bool = False, origin=None):
        """## 🧠 Convert time to indices.

        -----
        ### 🛠️ Parameters

        #### `times : list-like | float | int`
            List of numbers or a number representing points in time.
        #### `use_rounding : bool`
            If True, use rounding (instead of truncation) when converting
            times to indices. This can help avoid non-unique indices.
        #### `origin : datetime | float | int | None`
            Time reference for times. If None, ``times`` are assumed to be
            relative to :term:`first_samp`.

            ✨ Added in vesion 0.17.0

        -----
        ### ⏎ Returns

        #### `index : ndarray`
            Indices relative to :term:`first_samp` corresponding to the times
            supplied.
        """
        ...
    @property
    def annotations(self):
        """## 🧠 `mne.Annotations` for marking segments of data."""
        ...
    @property
    def filenames(self):
        """## 🧠 The filenames used."""
        ...
    def set_annotations(
        self,
        annotations,
        emit_warning: bool = True,
        on_missing: str = "raise",
        *,
        verbose=None,
    ):
        """## 🧠 Setter for annotations.

        This setter checks if they are inside the data range.

        -----
        ### 🛠️ Parameters

        #### `annotations : instance of mne.Annotations | None`
            Annotations to set. If None, the annotations is defined
            but empty.

        #### `emit_warning : bool`
            Whether to emit warnings when cropping or omitting annotations.
            The default is True.

        #### `on_missing : 'raise' | 'warn' | 'ignore'`
            Can be ``'raise'`` (default) to raise an error, ``'warn'`` to emit a
            warning, or ``'ignore'`` to ignore when entries in ch_names are not present in the raw instance.

            ✨ Added in vesion 0.23.0

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns

        #### `self : instance of Raw`
            The raw object with annotations.
        """
        ...
    def __del__(self) -> None: ...
    def __enter__(self):
        """## 🧠 Entering with block."""
        ...
    def __exit__(
        self,
        exception_type: type[BaseException] | None,
        exception_val: BaseException | None,
        trace: types.TracebackType | None,
    ):
        """## 🧠 Exit with block."""
        ...
    def __getitem__(self, item):
        """## 🧠 Get raw data and times.

        -----
        ### 🛠️ Parameters

        #### `item : tuple or array-like`
            See below for use cases.

        -----
        ### ⏎ Returns

        #### `data : ndarray, shape (n_channels, n_times)`
            The raw data.
        #### `times : ndarray, shape (n_times,)`
            The times associated with the data.

        -----
        ### 🖥️ Examples

        Generally raw data is accessed as::

            >>> data, times = raw[picks, time_slice]  # doctest: +SKIP

        To get all data, you can thus do either of::

            >>> data, times = raw[:]  # doctest: +SKIP

        Which will be equivalent to:

            >>> data, times = raw[:, :]  # doctest: +SKIP

        To get only the good MEG data from 10-20 seconds, you could do::

            >>> picks = mne.pick_types(raw.info, meg=True, exclude='bads')  # doctest: +SKIP
            >>> t_idx = raw.time_as_index([10., 20.])  # doctest: +SKIP
            >>> data, times = raw[picks, t_idx[0]:t_idx[1]]  # doctest: +SKIP

        """
        ...
    def __setitem__(self, item, value) -> None:
        """## 🧠 Set raw data content."""
        ...
    def get_data(
        self,
        picks=None,
        start: int = 0,
        stop=None,
        reject_by_annotation=None,
        return_times: bool = False,
        units=None,
        *,
        tmin=None,
        tmax=None,
        verbose=None,
    ):
        """## 🧠 Get data in the given range.

        -----
        ### 🛠️ Parameters

        #### `picks : str | array-like | slice | None`
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel *type* strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick all channels. Note that channels in
            ``info['bads']`` *will be included* if their names or indices are
            explicitly provided.
        #### `start : int`
            The first sample to include. Defaults to 0.
        #### `stop : int | None`
            End sample (first not to include). If None (default), the end of
            the data is  used.
        #### `reject_by_annotation : None | 'omit' | 'NaN'`
            Whether to reject by annotation. If None (default), no rejection is
            done. If 'omit', segments annotated with description starting with
            'bad' are omitted. If 'NaN', the bad samples are filled with NaNs.
        #### `return_times : bool`
            Whether to return times as well. Defaults to False.

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
        #### `tmin : int | float | None`
            Start time of data to get in seconds. The ``tmin`` parameter is
            ignored if the ``start`` parameter is bigger than 0.

            ✨ Added in vesion 0.24.0
        #### `tmax : int | float | None`
            End time of data to get in seconds. The ``tmax`` parameter is
            ignored if the ``stop`` parameter is defined.

            ✨ Added in vesion 0.24.0

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns

        #### `data : ndarray, shape (n_channels, n_times)`
            Copy of the data in the given range.
        #### `times : ndarray, shape (n_times,)`
            Times associated with the data samples. Only returned if
            return_times=True.

        -----
        ### 📖 Notes

        ✨ Added in vesion 0.14.0
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
        """## 🧠 Apply a function to a subset of channels.

        The function ``fun`` is applied to the channels defined in ``picks``.
        The raw object's data is modified in-place. If the function returns a different
        data type (e.g. :py:obj:`numpy.complex128`) it must be specified
        using the ``dtype`` parameter, which causes the data type of **all** the data
        to change (even if the function is only applied to channels in ``picks``). The object has to have the data loaded e.g. with ``preload=True`` or ``self.load_data()``.

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
            operate on an array of shape ``(n_times,)``  if ``channel_wise=True`` and ``(len(picks), n_times)`` otherwise.
            The function must return an `numpy.ndarray` shaped like its input.
        #### `picks : str | array-like | slice | None`
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel *type* strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick all data channels (excluding reference
            MEG channels). Note that channels in ``info['bads']`` *will be included* if
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

        #### `channel_wise : bool`
            Whether to apply the function to each channel individually. If ``False``,
            the function will be applied to all channels at once. Default ``True``.

            ✨ Added in vesion 0.18

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        **kwargs : dict
            Additional keyword arguments to pass to ``fun``.

        -----
        ### ⏎ Returns

        #### `self : instance of Raw`
            The raw object with transformed data.
        """
        ...
    def filter(
        self,
        l_freq,
        h_freq,
        picks=None,
        filter_length: str = "auto",
        l_trans_bandwidth: str = "auto",
        h_trans_bandwidth: str = "auto",
        n_jobs=None,
        method: str = "fir",
        iir_params=None,
        phase: str = "zero",
        fir_window: str = "hamming",
        fir_design: str = "firwin",
        skip_by_annotation=("edge", "bad_acq_skip"),
        pad: str = "reflect_limited",
        verbose=None,
    ):
        """## 🧠 Filter a subset of channels.

        -----
        ### 🛠️ Parameters


        #### `l_freq : float | None`
            For FIR filters, the lower pass-band edge; for IIR filters, the lower
            cutoff frequency. If None the data are only low-passed.

        #### `h_freq : float | None`
            For FIR filters, the upper pass-band edge; for IIR filters, the upper
            cutoff frequency. If None the data are only high-passed.
        #### `picks : str | array-like | slice | None`
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel *type* strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick all data channels. Note that channels
            in ``info['bads']`` *will be included* if their names or indices are
            explicitly provided.

        #### `filter_length : str | int`
            Length of the FIR filter to use (if applicable):

            * **'auto' (default)**: The filter length is chosen based
              on the size of the transition regions (6.6 times the reciprocal
              of the shortest transition band for fir_window='hamming'
              and fir_design="firwin2", and half that for "firwin").
            * **str**: A human-readable time in
              units of "s" or "ms" (e.g., "10s" or "5500ms") will be
              converted to that number of samples if ``phase="zero"``, or
              the shortest power-of-two length at least that duration for
              ``phase="zero-double"``.
            * **int**: Specified length in samples. For fir_design="firwin",
              this should not be used.

        #### `l_trans_bandwidth : float | str`
            Width of the transition band at the low cut-off frequency in Hz
            (high pass or cutoff 1 in bandpass). Can be "auto"
            (default) to use a multiple of ``l_freq``::

                min(max(l_freq * 0.25, 2), l_freq)

            Only used for ``method='fir'``.

        #### `h_trans_bandwidth : float | str`
            Width of the transition band at the high cut-off frequency in Hz
            (low pass or cutoff 2 in bandpass). Can be "auto"
            (default in 0.14) to use a multiple of ``h_freq``::

                min(max(h_freq * 0.25, 2.), info['sfreq'] / 2. - h_freq)

            Only used for ``method='fir'``.

        #### `n_jobs : int | str`
            Number of jobs to run in parallel. Can be ``'cuda'`` if ``cupy``
            is installed properly and ``method='fir'``.

        #### `method : str`
            ``'fir'`` will use overlap-add FIR filtering, ``'iir'`` will use IIR
            forward-backward filtering (via `scipy.signal.filtfilt`).

        #### `iir_params : dict | None`
            Dictionary of parameters to use for IIR filtering.
            If ``iir_params=None`` and ``method="iir"``, 4th order Butterworth will be used.
            For more information, see `mne.filter.construct_iir_filter`.

        #### `phase : str`
            Phase of the filter.
            When ``method='fir'``, symmetric linear-phase FIR filters are constructed,
            and if ``phase='zero'`` (default), the delay of this filter is compensated
            for, making it non-causal. If ``phase='zero-double'``,
            then this filter is applied twice, once forward, and once backward
            (also making it non-causal). If ``'minimum'``, then a minimum-phase filter
            will be constructed and applied, which is causal but has weaker stop-band
            suppression.
            When ``method='iir'``, ``phase='zero'`` (default) or
            ``phase='zero-double'`` constructs and applies IIR filter twice, once
            forward, and once backward (making it non-causal) using
            `scipy.signal.filtfilt`.
            If ``phase='forward'``, it constructs and applies forward IIR filter using
            `scipy.signal.lfilter`.

            ✨ Added in vesion 0.13

        #### `fir_window : str`
            The window to use in FIR design, can be "hamming" (default),
            "hann" (default in 0.13), or "blackman".

            ✨ Added in vesion 0.15

        #### `fir_design : str`
            Can be "firwin" (default) to use `scipy.signal.firwin`,
            or "firwin2" to use `scipy.signal.firwin2`. "firwin" uses
            a time-domain design technique that generally gives improved
            attenuation using fewer samples than "firwin2".

            ✨ Added in vesion 0.15

        #### `skip_by_annotation : str | list of str`
            If a string (or list of str), any annotation segment that begins
            with the given string will not be included in filtering, and
            segments on either side of the given excluded annotated segment
            will be filtered separately (i.e., as independent signals).
            The default (``('edge', 'bad_acq_skip')`` will separately filter
            any segments that were concatenated by `mne.concatenate_raws`
            or `mne.io.Raw.append`, or separated during acquisition.
            To disable, provide an empty list. Only used if ``inst`` is raw.

            ✨ Added in vesion 0.16.

        #### `pad : str`
            The type of padding to use. Supports all `numpy.pad` ``mode``
            options. Can also be ``"reflect_limited"``, which pads with a
            reflected version of each vector mirrored on the first and last values
            of the vector, followed by zeros.

            Only used for ``method='fir'``.

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns

        #### `inst : instance of Epochs, Evoked, or Raw`
            The filtered data.

        -----
        ### 👉 See Also

        mne.filter.create_filter
        mne.Evoked.savgol_filter
        mne.io.Raw.notch_filter
        mne.io.Raw.resample
        mne.filter.create_filter
        mne.filter.filter_data
        mne.filter.construct_iir_filter

        -----
        ### 📖 Notes

        Applies a zero-phase low-pass, high-pass, band-pass, or band-stop
        filter to the channels selected by ``picks``.
        The data are modified inplace.

        The object has to have the data loaded e.g. with ``preload=True``
        or ``self.load_data()``.

        ``l_freq`` and ``h_freq`` are the frequencies below which and above
        which, respectively, to filter out of the data. Thus the uses are:

            * ``l_freq < h_freq``: band-pass filter
            * ``l_freq > h_freq``: band-stop filter
            * ``l_freq is not None and h_freq is None``: high-pass filter
            * ``l_freq is None and h_freq is not None``: low-pass filter

        ``self.info['lowpass']`` and ``self.info['highpass']`` are only
        updated with picks=None.

        ### 💡 Note If n_jobs > 1, more memory is required as
                  ``len(picks) * n_times`` additional time points need to
                  be temporarily stored in memory.

        For more information, see the tutorials
        `disc-filtering` and `tut-filter-resample` and
        `mne.filter.create_filter`.

        ✨ Added in vesion 0.15
        """
        ...
    def notch_filter(
        self,
        freqs,
        picks=None,
        filter_length: str = "auto",
        notch_widths=None,
        trans_bandwidth: float = 1.0,
        n_jobs=None,
        method: str = "fir",
        iir_params=None,
        mt_bandwidth=None,
        p_value: float = 0.05,
        phase: str = "zero",
        fir_window: str = "hamming",
        fir_design: str = "firwin",
        pad: str = "reflect_limited",
        skip_by_annotation=("edge", "bad_acq_skip"),
        verbose=None,
    ):
        """## 🧠 Notch filter a subset of channels.

        -----
        ### 🛠️ Parameters

        #### `freqs : float | array of float | None`
            Specific frequencies to filter out from data, e.g.,
            ``np.arange(60, 241, 60)`` in the US or ``np.arange(50, 251, 50)``
            in Europe. ``None`` can only be used with the mode
            ``'spectrum_fit'``, where an F test is used to find sinusoidal
            components.
        #### `picks : str | array-like | slice | None`
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel *type* strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick all data channels. Note that channels
            in ``info['bads']`` *will be included* if their names or indices are
            explicitly provided.

        #### `filter_length : str | int`
            Length of the FIR filter to use (if applicable):

            * **'auto' (default)**: The filter length is chosen based
              on the size of the transition regions (6.6 times the reciprocal
              of the shortest transition band for fir_window='hamming'
              and fir_design="firwin2", and half that for "firwin").
            * **str**: A human-readable time in
              units of "s" or "ms" (e.g., "10s" or "5500ms") will be
              converted to that number of samples if ``phase="zero"``, or
              the shortest power-of-two length at least that duration for
              ``phase="zero-double"``.
            * **int**: Specified length in samples. For fir_design="firwin",
              this should not be used.

            When ``method=='spectrum_fit'``, this sets the effective window duration
            over which fits are computed. See `mne.filter.create_filter`
            for options. Longer window lengths will give more stable frequency
            estimates, but require (potentially much) more processing and are not able
            to adapt as well to non-stationarities.

            The default in 0.21 is None, but this will change to ``'10s'`` in 0.22.
        #### `notch_widths : float | array of float | None`
            Width of each stop band (centred at each freq in freqs) in Hz.
            If None, ``freqs / 200`` is used.
        #### `trans_bandwidth : float`
            Width of the transition band in Hz.
            Only used for ``method='fir'`` and ``method='iir'``.

        #### `n_jobs : int | str`
            Number of jobs to run in parallel. Can be ``'cuda'`` if ``cupy``
            is installed properly and ``method='fir'``.

        #### `method : str`
            ``'fir'`` will use overlap-add FIR filtering, ``'iir'`` will use IIR
            forward-backward filtering (via `scipy.signal.filtfilt`).

        #### `iir_params : dict | None`
            Dictionary of parameters to use for IIR filtering.
            If ``iir_params=None`` and ``method="iir"``, 4th order Butterworth will be used.
            For more information, see `mne.filter.construct_iir_filter`.
        #### `mt_bandwidth : float | None`
            The bandwidth of the multitaper windowing function in Hz.
            Only used in 'spectrum_fit' mode.
        #### `p_value : float`
            P-value to use in F-test thresholding to determine significant
            sinusoidal components to remove when ``method='spectrum_fit'`` and
            ``freqs=None``. Note that this will be Bonferroni corrected for the
            number of frequencies, so large p-values may be justified.

        #### `phase : str`
            Phase of the filter.
            When ``method='fir'``, symmetric linear-phase FIR filters are constructed,
            and if ``phase='zero'`` (default), the delay of this filter is compensated
            for, making it non-causal. If ``phase='zero-double'``,
            then this filter is applied twice, once forward, and once backward
            (also making it non-causal). If ``'minimum'``, then a minimum-phase filter
            will be constructed and applied, which is causal but has weaker stop-band
            suppression.
            When ``method='iir'``, ``phase='zero'`` (default) or
            ``phase='zero-double'`` constructs and applies IIR filter twice, once
            forward, and once backward (making it non-causal) using
            `scipy.signal.filtfilt`.
            If ``phase='forward'``, it constructs and applies forward IIR filter using
            `scipy.signal.lfilter`.

            ✨ Added in vesion 0.13

        #### `fir_window : str`
            The window to use in FIR design, can be "hamming" (default),
            "hann" (default in 0.13), or "blackman".

            ✨ Added in vesion 0.15

        #### `fir_design : str`
            Can be "firwin" (default) to use `scipy.signal.firwin`,
            or "firwin2" to use `scipy.signal.firwin2`. "firwin" uses
            a time-domain design technique that generally gives improved
            attenuation using fewer samples than "firwin2".

            ✨ Added in vesion 0.15

        #### `pad : str`
            The type of padding to use. Supports all `numpy.pad` ``mode``
            options. Can also be ``"reflect_limited"``, which pads with a
            reflected version of each vector mirrored on the first and last values
            of the vector, followed by zeros.

            Only used for ``method='fir'``.
            The default is ``'reflect_limited'``.

            ✨ Added in vesion 0.15

        #### `skip_by_annotation : str | list of str`
            If a string (or list of str), any annotation segment that begins
            with the given string will not be included in filtering, and
            segments on either side of the given excluded annotated segment
            will be filtered separately (i.e., as independent signals).
            The default (``('edge', 'bad_acq_skip')`` will separately filter
            any segments that were concatenated by `mne.concatenate_raws`
            or `mne.io.Raw.append`, or separated during acquisition.
            To disable, provide an empty list. Only used if ``inst`` is raw.

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns

        #### `raw : instance of Raw`
            The raw instance with filtered data.

        -----
        ### 👉 See Also

        mne.filter.notch_filter
        mne.io.Raw.filter

        -----
        ### 📖 Notes

        Applies a zero-phase notch filter to the channels selected by
        "picks". By default the data of the Raw object is modified inplace.

        The Raw object has to have the data loaded e.g. with ``preload=True``
        or ``self.load_data()``.

        ### 💡 Note If n_jobs > 1, more memory is required as
                  ``len(picks) * n_times`` additional time points need to
                  be temporarily stored in memory.

        For details, see `mne.filter.notch_filter`.
        """
        ...
    def resample(
        self,
        sfreq,
        npad: str = "auto",
        window: str = "boxcar",
        stim_picks=None,
        n_jobs=None,
        events=None,
        pad: str = "reflect_limited",
        verbose=None,
    ):
        """## 🧠 Resample all channels.

        If appropriate, an anti-aliasing filter is applied before resampling.
        See `resampling-and-decimating` for more information.

        ### ⛔️ Warning The intended purpose of this function is primarily to
                     speed up computations (e.g., projection calculation) when
                     precise timing of events is not required, as downsampling
                     raw data effectively jitters trigger timings. It is
                     generally recommended not to epoch downsampled data,
                     but instead epoch and then downsample, as epoching
                     downsampled data jitters triggers.
                     For more, see
                     `this illustrative gist
                     <https://gist.github.com/larsoner/01642cb3789992fbca59>`_.

                     If resampling the continuous data is desired, it is
                     recommended to construct events using the original data.
                     The event onsets can be jointly resampled with the raw
                     data using the 'events' parameter (a resampled copy is
                     returned).

        -----
        ### 🛠️ Parameters

        #### `sfreq : float`
            New sample rate to use.

        #### `npad : int | str`
            Amount to pad the start and end of the data.
            Can also be ``"auto"`` to use a padding that will result in
            a power-of-two size (can be much faster).

        #### `window : str | tuple`
            Frequency-domain window to use in resampling.
            See `scipy.signal.resample`.
        #### `stim_picks : list of int | None`
            Stim channels. These channels are simply subsampled or
            supersampled (without applying any filtering). This reduces
            resampling artifacts in stim channels, but may lead to missing
            triggers. If None, stim channels are automatically chosen using
            `mne.pick_types`.

        #### `n_jobs : int | str`
            Number of jobs to run in parallel. Can be ``'cuda'`` if ``cupy``
            is installed properly.
        #### `events : 2D array, shape (n_events, 3) | None`
            An optional event matrix. When specified, the onsets of the events
            are resampled jointly with the data. NB: The input events are not
            modified, but a new array is returned with the raw instead.

        #### `pad : str`
            The type of padding to use. Supports all `numpy.pad` ``mode``
            options. Can also be ``"reflect_limited"``, which pads with a
            reflected version of each vector mirrored on the first and last values
            of the vector, followed by zeros.
            The default is ``'reflect_limited'``.

            ✨ Added in vesion 0.15

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns

        #### `raw : instance of Raw`
            The resampled version of the raw object.
        #### `events : array, shape (n_events, 3) | None`
            If events are jointly resampled, these are returned with the raw.

        -----
        ### 👉 See Also

        mne.io.Raw.filter
        mne.Epochs.resample

        -----
        ### 📖 Notes

        For some data, it may be more accurate to use ``npad=0`` to reduce
        artifacts. This is dataset dependent -- check your data!

        For optimum performance and to make use of ``n_jobs > 1``, the raw
        object has to have the data loaded e.g. with ``preload=True`` or
        ``self.load_data()``, but this increases memory requirements. The
        resulting raw object will have the data loaded into memory.
        """
        ...
    def crop(
        self, tmin: float = 0.0, tmax=None, include_tmax: bool = True, *, verbose=None
    ):
        """## 🧠 Crop raw data file.

        Limit the data from the raw file to go between specific times. Note
        that the new ``tmin`` is assumed to be ``t=0`` for all subsequently
        called functions (e.g., `mne.io.Raw.time_as_index`, or
        `mne.Epochs`). New :term:`first_samp` and :term:`last_samp`
        are set accordingly.

        Thus function operates in-place on the instance.
        Use `mne.io.Raw.copy` if operation on a copy is desired.

        -----
        ### 🛠️ Parameters


        #### `tmin : float`
            Start time of the raw data to use in seconds (must be >= 0).

        #### `tmax : float`
            End time of the raw data to use in seconds (cannot exceed data duration).

        #### `include_tmax : bool`
            If True (default), include tmax. If False, exclude tmax (similar to how
            Python indexing typically works).

            ✨ Added in vesion 0.19

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns

        #### `raw : instance of Raw`
            The cropped raw object, modified in-place.
        """
        ...
    def crop_by_annotations(self, annotations=None, *, verbose=None):
        """## 🧠 Get crops of raw data file for selected annotations.

        -----
        ### 🛠️ Parameters

        #### `annotations : instance of Annotations | None`
            The annotations to use for cropping the raw file. If None,
            the annotations from the instance are used.

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns

        #### `raws : list`
            The cropped raw objects.
        """
        ...
    def save(
        self,
        fname,
        picks=None,
        tmin: int = 0,
        tmax=None,
        buffer_size_sec=None,
        drop_small_buffer: bool = False,
        proj: bool = False,
        fmt: str = "single",
        overwrite: bool = False,
        split_size: str = "2GB",
        split_naming: str = "neuromag",
        verbose=None,
    ) -> None:
        """## 🧠 Save raw data to file.

        -----
        ### 🛠️ Parameters

        #### `fname : path-like`
            File name of the new dataset. This has to be a new filename
            unless data have been preloaded. Filenames should end with
            ``raw.fif`` (common raw data), ``raw_sss.fif``
            (Maxwell-filtered continuous data),
            ``raw_tsss.fif`` (temporally signal-space-separated data),
            ``_meg.fif`` (common MEG data), ``_eeg.fif`` (common EEG data),
            or ``_ieeg.fif`` (common intracranial EEG data). You may also
            append an additional ``.gz`` suffix to enable gzip compression.
        #### `picks : str | array-like | slice | None`
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel *type* strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick all channels. Note that channels in
            ``info['bads']`` *will be included* if their names or indices are
            explicitly provided.

        #### `tmin : float`
            Start time of the raw data to use in seconds (must be >= 0).

        #### `tmax : float`
            End time of the raw data to use in seconds (cannot exceed data duration).
        #### `buffer_size_sec : float | None`
            Size of data chunks in seconds. If None (default), the buffer
            size of the original file is used.
        #### `drop_small_buffer : bool`
            Drop or not the last buffer. It is required by maxfilter (SSS)
            that only accepts raw files with buffers of the same size.
        #### `proj : bool`
            If True the data is saved with the projections applied (active).

            ### 💡 Note If ``apply_proj()`` was used to apply the projections,
                      the projectons will be active even if ``proj`` is False.
        #### `fmt : 'single' | 'double' | 'int' | 'short'`
            Format to use to save raw data. Valid options are 'double',
            'single', 'int', and 'short' for 64- or 32-bit float, or 32- or
            16-bit integers, respectively. It is **strongly** recommended to
            use 'single', as this is backward-compatible, and is standard for
            maintaining precision. Note that using 'short' or 'int' may result
            in loss of precision, complex data cannot be saved as 'short',
            and neither complex data types nor real data stored as 'double'
            can be loaded with the MNE command-line tools. See raw.orig_format
            to determine the format the original data were stored in.

        #### `overwrite : bool`
            If True (default False), overwrite the destination file if it
            exists.
            To overwrite original file (the same one that was loaded),
            data must be preloaded upon reading.
        #### `split_size : str | int`
            Large raw files are automatically split into multiple pieces. This
            parameter specifies the maximum size of each piece. If the
            parameter is an integer, it specifies the size in Bytes. It is
            also possible to pass a human-readable string, e.g., 100MB.

            ### 💡 Note Due to FIFF file limitations, the maximum split
                      size is 2GB.

        #### `split_naming : 'neuromag' | 'bids'`
            When splitting files, append a filename partition with the appropriate
            naming schema: for ``'neuromag'``, a split file ``fname.fif`` will be named
            ``fname.fif``, ``fname-1.fif``, ``fname-2.fif`` etc.; while for ``'bids'``,
            it will be named ``fname_split-01.fif``, ``fname_split-02.fif``, etc.

            ✨ Added in vesion 0.17

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### 📖 Notes

        If Raw is a concatenation of several raw files, **be warned** that
        only the measurement information from the first raw file is stored.
        This likely means that certain operations with external tools may not
        work properly on a saved concatenated file (e.g., probably some
        or all forms of SSS). It is recommended not to concatenate and
        then save raw files for this reason.

        Samples annotated ``BAD_ACQ_SKIP`` are not stored in order to optimize
        memory. Whatever values, they will be loaded as 0s when reading file.
        """
        ...
    def export(
        self,
        fname,
        fmt: str = "auto",
        physical_range: str = "auto",
        add_ch_type: bool = False,
        *,
        overwrite: bool = False,
        verbose=None,
    ) -> None:
        """## 🧠 Export Raw to external formats.

        Supported formats:
            - BrainVision (``.vhdr``, ``.vmrk``, ``.eeg``, uses `pybv <https://github.com/bids-standard/pybv>`_)
            - EEGLAB (``.set``, uses `eeglabio`)
            - EDF (``.edf``, uses `edfio <https://github.com/the-siesta-group/edfio>`_)

        ### ⛔️ Warning
            Since we are exporting to external formats, there's no guarantee that all
            the info will be preserved in the external format. See Notes for details.

        -----
        ### 🛠️ Parameters


        #### `fname : str`
            Name of the output file.

        #### `fmt : 'auto' | 'brainvision' | 'edf' | 'eeglab'`
            Format of the export. Defaults to ``'auto'``, which will infer the format
            from the filename extension. See supported formats above for more
            information.

        #### `physical_range : str | tuple`
            The physical range of the data. If 'auto' (default), then
            it will infer the physical min and max from the data itself,
            taking the minimum and maximum values per channel type.
            If it is a 2-tuple of minimum and maximum limit, then those
            physical ranges will be used. Only used for exporting EDF files.

        #### `add_ch_type : bool`
            Whether to incorporate the channel type into the signal label (e.g. whether
            to store channel "Fz" as "EEG Fz"). Only used for EDF format. Default is
            ``False``.

        #### `overwrite : bool`
            If True (default False), overwrite the destination file if it
            exists.

            ✨ Added in vesion 0.24.1

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### 📖 Notes

        ✨ Added in vesion 0.24

        Export to external format may not preserve all the information from the
        instance. To save in native MNE format (``.fif``) without information loss,
        use `mne.io.Raw.save` instead.
        Export does not apply projector(s). Unapplied projector(s) will be lost.
        Consider applying projector(s) before exporting with
        `mne.io.Raw.apply_proj`.

        For EEGLAB exports, channel locations are expanded to full EEGLAB format.
        For more details see `eeglabio.utils.cart_to_eeglab`.

        For EDF exports, only channels measured in Volts are allowed; in MNE-Python
        this means channel types 'eeg', 'ecog', 'seeg', 'emg', 'eog', 'ecg', 'dbs',
        'bio', and 'misc'. 'stim' channels are dropped. Although this function
        supports storing channel types in the signal label (e.g. ``EEG Fz`` or
        ``MISC E``), other software may not support this (optional) feature of
        the EDF standard.

        If ``add_ch_type`` is True, then channel types are written based on what
        they are currently set in MNE-Python. One should double check that all
        their channels are set correctly. You can call
        :attr:`raw.set_channel_types <mne.io.Raw.set_channel_types>` to set
        channel types.

        In addition, EDF does not support storing a montage. You will need
        to store the montage separately and call :attr:`raw.set_montage()
        <mne.io.Raw.set_montage>`.
        """
        ...
    def plot(
        self,
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
        """## 🧠 Plot raw data.

        -----
        ### 🛠️ Parameters

        #### `events : array | None`
            Events to show with vertical bars.
        #### `duration : float`
            Time window (s) to plot. The lesser of this value and the duration
            of the raw file will be used.
        #### `start : float`
            Initial time to show (can be changed dynamically once plotted). If
            show_first_samp is True, then it is taken relative to
            ``raw.first_samp``.
        #### `n_channels : int`
            Number of channels to plot at once. Defaults to 20. The lesser of
            ``n_channels`` and ``len(raw.ch_names)`` will be shown.
            Has no effect if ``order`` is 'position', 'selection' or 'butterfly'.
        #### `bgcolor : color object`
            Color of the background.
        #### `color : dict | color object | None`
            Color for the data traces. If None, defaults to::

                dict(mag='darkblue', grad='b', eeg='k', eog='k', ecg='m',
                     emg='k', ref_meg='steelblue', misc='k', stim='k',
                     resp='k', chpi='k')

        #### `bad_color : color object`
            Color to make bad channels.

        #### `event_color : color object | dict | None`
            Color(s) to use for :term:`events`. To show all :term:`events` in the same
            color, pass any matplotlib-compatible color. To color events differently,
            pass a `dict` that maps event names or integer event numbers to colors
            (must include entries for *all* events, or include a "fallback" entry with
            key ``-1``). If ``None``, colors are chosen from the current Matplotlib
            color cycle.
            Defaults to ``'cyan'``.

        #### `scalings : 'auto' | dict | None`
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
        #### `remove_dc : bool`
            If True remove DC component when plotting data.
        #### `order : array of int | None`
            Order in which to plot data. If the array is shorter than the number of
            channels, only the given channels are plotted. If None (default), all
            channels are plotted. If ``group_by`` is ``'position'`` or
            ``'selection'``, the ``order`` parameter is used only for selecting the
            channels to be plotted.
        #### `show_options : bool`
            If True, a dialog for options related to projection is shown.
        #### `title : str | None`
            The title of the window. If None, and either the filename of the
            raw object or '<unknown>' will be displayed as title.
        #### `show : bool`
            Show figure if True.
        #### `block : bool`
            Whether to halt program execution until the figure is closed.
            Useful for setting bad channels on the fly by clicking on a line.
            May not work on all systems / platforms.
            (Only Qt) If you run from a script, this needs to
            be ``True`` or a Qt-eventloop needs to be started somewhere
            else in the script (e.g. if you want to implement the browser
            inside another Qt-Application).
        #### `highpass : float | None`
            Highpass to apply when displaying data.
        #### `lowpass : float | None`
            Lowpass to apply when displaying data.
            If highpass > lowpass, a bandstop rather than bandpass filter
            will be applied.
        #### `filtorder : int`
            Filtering order. 0 will use FIR filtering with MNE defaults.
            Other values will construct an IIR filter of the given order
            and apply it with `scipy.signal.filtfilt` (making the effective
            order twice ``filtorder``). Filtering may produce some edge artifacts
            (at the left and right edges) of the signals during display.

            🎭 Changed in version 0.18
               Support for ``filtorder=0`` to use FIR filtering.
        #### `clipping : str | float | None`
            If None, channels are allowed to exceed their designated bounds in
            the plot. If "clamp", then values are clamped to the appropriate
            range for display, creating step-like artifacts. If "transparent",
            then excessive values are not shown, creating gaps in the traces.
            If float, clipping occurs for values beyond the ``clipping`` multiple
            of their dedicated range, so ``clipping=1.`` is an alias for
            ``clipping='transparent'``.

            🎭 Changed in version 0.21
               Support for float, and default changed from None to 1.5.
        #### `show_first_samp : bool`
            If True, show time axis relative to the ``raw.first_samp``.
        #### `proj : bool`
            Whether to apply projectors prior to plotting (default is ``True``).
            Individual projectors can be enabled/disabled interactively (see
            Notes). This argument only affects the plot; use ``raw.apply_proj()``
            to modify the data stored in the Raw object.

        #### `group_by : str`
            How to group channels. ``'type'`` groups by channel type,
            ``'original'`` plots in the order of ch_names, ``'selection'`` uses
            Elekta's channel groupings (only works for Neuromag data),
            ``'position'`` groups the channels by the positions of the sensors.
            ``'selection'`` and ``'position'`` modes allow custom selections by
            using a lasso selector on the topomap. In butterfly mode, ``'type'``
            and ``'original'`` group the channels by type, whereas ``'selection'``
            and ``'position'`` use regional grouping. ``'type'`` and ``'original'``
            modes are ignored when ``order`` is not ``None``. Defaults to ``'type'``.
        #### `butterfly : bool`
            Whether to start in butterfly mode. Defaults to False.
        #### `decim : int | 'auto'`
            Amount to decimate the data during display for speed purposes.
            You should only decimate if the data are sufficiently low-passed,
            otherwise aliasing can occur. The 'auto' mode (default) uses
            the decimation that results in a sampling rate least three times
            larger than ``min(info['lowpass'], lowpass)`` (e.g., a 40 Hz lowpass
            will result in at least a 120 Hz displayed sample rate).
        #### `noise_cov : instance of Covariance | str | None`
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
        #### `event_id : dict | None`
            Event IDs used to show at event markers (default None shows
            the event numbers).

            ✨ Added in vesion 0.16.0

        #### `show_scrollbars : bool`
            Whether to show scrollbars when the plot is initialized. Can be toggled
            after initialization by pressing :kbd:`z` ("zen mode") while the plot
            window is focused. Default is ``True``.

            ✨ Added in vesion 0.19.0

        #### `show_scalebars : bool`
            Whether to show scale bars when the plot is initialized. Can be toggled
            after initialization by pressing :kbd:`s` while the plot window is focused.
            Default is ``True``.

            ✨ Added in vesion 0.20.0

        #### `time_format : 'float' | 'clock'`
            Style of time labels on the horizontal axis. If ``'float'``, labels will be
            number of seconds from the start of the recording. If ``'clock'``,
            labels will show "clock time" (hours/minutes/seconds) inferred from
            ``raw.info['meas_date']``. Default is ``'float'``.

            ✨ Added in vesion 0.24

        #### `precompute : bool | str`
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

        #### `use_opengl : bool | None`
            Whether to use OpenGL when rendering the plot (requires ``pyopengl``).
            May increase performance, but effect is dependent on system CPU and
            graphics hardware. Only works if using the Qt backend. Default is
            None, which will use False unless the user configuration variable
            ``MNE_BROWSER_USE_OPENGL`` is set to ``'true'``,
            see `mne.set_config`.

            ✨ Added in vesion 0.24

        #### `theme : str | path-like`
            Can be "auto", "light", or "dark" or a path-like to a
            custom stylesheet. For Dark-Mode and automatic Dark-Mode-Detection,
            `qdarkstyle` and
            `darkdetect <https://github.com/albertosottile/darkdetect>`__,
            respectively, are required.    If None (default), the config option MNE_BROWSER_THEME will be used,
            defaulting to "auto" if it's not found.
            Only supported by the ``'qt'`` backend.

            ✨ Added in vesion 1.0

        #### `overview_mode : str | None`
            Can be "channels", "empty", or "hidden" to set the overview bar mode
            for the ``'qt'`` backend. If None (default), the config option
            ``MNE_BROWSER_OVERVIEW_MODE`` will be used, defaulting to "channels"
            if it's not found.

            ✨ Added in vesion 1.1

        #### `splash : bool`
            If True (default), a splash screen is shown during the application startup. Only
            applicable to the ``qt`` backend.

            ✨ Added in vesion 1.6

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns


        #### `fig : matplotlib.figure.Figure | mne_qt_browser.figure.MNEQtBrowser`
            Browser instance.

        -----
        ### 📖 Notes

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
    @property
    def ch_names(self):
        """## 🧠 Channel names."""
        ...
    @property
    def times(self):
        """## 🧠 Time points."""
        ...
    @property
    def n_times(self):
        """## 🧠 Number of time points."""
        ...
    def __len__(self) -> int:
        """## 🧠 Return the number of time points.

        -----
        ### ⏎ Returns

        #### `len : int`
            The number of time points.

        -----
        ### 🖥️ Examples

        This can be used as::

            >>> len(raw)  # doctest: +SKIP
            1000
        """
        ...
    def load_bad_channels(
        self, bad_file=None, force: bool = False, verbose=None
    ) -> None:
        """## 🧠 Mark channels as bad from a text file.

        This function operates mostly in the style of the C function
        ``mne_mark_bad_channels``. Each line in the text file will be
        interpreted as a name of a bad channel.

        -----
        ### 🛠️ Parameters

        #### `bad_file : path-like | None`
            File name of the text file containing bad channels.
            If ``None`` (default), bad channels are cleared, but this
            is more easily done directly with ``raw.info['bads'] = []``.
        #### `force : bool`
            Whether or not to force bad channel marking (of those
            that exist) if channels are not found, instead of
            raising an error. Defaults to ``False``.

        #### `verbose : bool | str | int | None`
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.
        """
        ...
    def append(self, raws, preload=None) -> None:
        """## 🧠 Concatenate raw instances as if they were continuous.

        ### 💡 Note Boundaries of the raw files are annotated bad. If you wish to
                  use the data as continuous recording, you can remove the
                  boundary annotations after concatenation (see
                  `mne.Annotations.delete`).

        -----
        ### 🛠️ Parameters

        #### `raws : list, or Raw instance`
            List of Raw instances to concatenate to the current instance
            (in order), or a single raw instance to concatenate.

        #### `preload : bool, str, or None (default None)`
            Preload data into memory for data manipulation and faster indexing.
            If True, the data will be preloaded into memory (fast, requires
            large amount of memory). If preload is a string, preload is the
            file name of a memory-mapped file which is used to store the data
            on the hard drive (slower, requires less memory). If preload is
            None, preload=True or False is inferred using the preload status
            of the instances passed in.
        """
        ...
    def close(self) -> None:
        """## 🧠 Clean up the object.

        Does nothing for objects that close their file descriptors.
        Things like Raw will override this method.
        """
        ...
    def copy(self):
        """## 🧠 Return copy of Raw instance.

        -----
        ### ⏎ Returns

        #### `inst : instance of Raw`
            A copy of the instance.
        """
        ...
    def add_events(self, events, stim_channel=None, replace: bool = False) -> None:
        """## 🧠 Add events to stim channel.

        -----
        ### 🛠️ Parameters

        #### `events : ndarray, shape (n_events, 3)`
            Events to add. The first column specifies the sample number of
            each event, the second column is ignored, and the third column
            provides the event value. If events already exist in the Raw
            instance at the given sample numbers, the event values will be
            added together.
        #### `stim_channel : str | None`
            Name of the stim channel to add to. If None, the config variable
            'MNE_STIM_CHANNEL' is used. If this is not found, it will default
            to ``'STI 014'``.
        #### `replace : bool`
            If True the old events on the stim channel are removed before
            adding the new ones.

        -----
        ### 📖 Notes

        Data must be preloaded in order to add events.
        """
        ...
    def compute_psd(
        self,
        method: str = "welch",
        fmin: int = 0,
        fmax=...,
        tmin=None,
        tmax=None,
        picks=None,
        exclude=(),
        proj: bool = False,
        remove_dc: bool = True,
        reject_by_annotation: bool = True,
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
            Default is ``'welch'``.
        #### `fmin, fmax : float`
            The lower- and upper-bound on frequencies of interest. Default is ``fmin=0, fmax=np.inf`` (spans all frequencies present in the data).
        #### `tmin, tmax : float | None`
            First and last times to include, in seconds. ``None`` uses the first or
            last time present in the data. Default is ``tmin=None, tmax=None`` (all
            times).
        #### `picks : str | array-like | slice | None`
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel *type* strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick good data channels (excluding reference
            MEG channels). Note that channels in ``info['bads']`` *will be included* if
            their names or indices are explicitly provided.
        #### `exclude : list of str | 'bads'`
            Channel names to exclude. If ``'bads'``, channels
            in ``info['bads']`` are excluded; pass an empty list to
            include all channels (including "bad" channels, if any).
        #### `proj : bool`
            Whether to apply SSP projection vectors before spectral estimation.
            Default is ``False``.

        #### `remove_dc : bool`
            If ``True``, the mean is subtracted from each segment before computing
            its spectrum.
        #### `reject_by_annotation : bool`
            Whether to omit bad spans of data before spectral estimation. If
            ``True``, spans with annotations whose description begins with
            ``bad`` will be omitted.
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
    def to_data_frame(
        self,
        picks=None,
        index=None,
        scalings=None,
        copy: bool = True,
        start=None,
        stop=None,
        long_format: bool = False,
        time_format=None,
        *,
        verbose=None,
    ):
        """## 🧠 Export data in tabular structure as a pandas DataFrame.

        Channels are converted to columns in the DataFrame. By default, an
        additional column "time" is added, unless ``index`` is not ``None``
        (in which case time values form the DataFrame's index).

        -----
        ### 🛠️ Parameters

        #### `picks : str | array-like | slice | None`
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel *type* strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick all channels. Note that channels in
            ``info['bads']`` *will be included* if their names or indices are
            explicitly provided.

        #### `index : 'time' | None`
            Kind of index to use for the DataFrame. If ``None``, a sequential
            integer index (`pandas.RangeIndex`) will be used. If ``'time'``, a
            ``pandas.Index``, `pandas.DatetimeIndex`, or `pandas.TimedeltaIndex` will be used
            (depending on the value of ``time_format``).
            Defaults to ``None``.

        #### `scalings : dict | None`
            Scaling factor applied to the channels picked. If ``None``, defaults to
            ``dict(eeg=1e6, mag=1e15, grad=1e13)`` — i.e., converts EEG to µV,
            magnetometers to fT, and gradiometers to fT/cm.

        #### `copy : bool`
            If ``True``, data will be copied. Otherwise data may be modified in place.
            Defaults to ``True``.
        #### `start : int | None`
            Starting sample index for creating the DataFrame from a temporal
            span of the Raw object. ``None`` (the default) uses the first
            sample.
        #### `stop : int | None`
            Ending sample index for creating the DataFrame from a temporal span
            of the Raw object. ``None`` (the default) uses the last sample.

        #### `long_format : bool`
            If True, the DataFrame is returned in long format where each row is one
            observation of the signal at a unique combination of time point and channel.
            For convenience, a ``ch_type`` column is added to facilitate subsetting the resulting DataFrame. Defaults to ``False``.

        #### `time_format : str | None`
            Desired time format. If ``None``, no conversion is applied, and time values
            remain as float values in seconds. If ``'ms'``, time values will be rounded
            to the nearest millisecond and converted to integers. If ``'timedelta'``,
            time values will be converted to `pandas.Timedelta` values. If ``'datetime'``, time values will be converted to `pandas.Timestamp` values, relative to ``raw.info['meas_date']`` and offset by ``raw.first_samp``.
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
    def describe(self, data_frame: bool = False):
        """## 🧠 Describe channels (name, type, descriptive statistics).

        -----
        ### 🛠️ Parameters

        #### `data_frame : bool`
            If True, return results in a pandas.DataFrame. If False, only print
            results. Columns 'ch', 'type', and 'unit' indicate channel index,
            channel type, and unit of the remaining five columns. These columns
            are 'min' (minimum), 'Q1' (first quartile or 25% percentile),
            'median', 'Q3' (third quartile or 75% percentile), and 'max'
            (maximum).

        -----
        ### ⏎ Returns

        #### `result : None | pandas.DataFrame`
            If data_frame=False, returns None. If data_frame=True, returns
            results in a pandas.DataFrame (requires pandas).
        """
        ...

class _ReadSegmentFileProtector:
    """## 🧠 Ensure only _filenames, _raw_extras, and _read_segment_file are used."""

    def __init__(self, raw) -> None: ...

class _RawShell:
    """## 🧠 Create a temporary raw object."""

    first_samp: Incomplete
    last_samp: Incomplete

    def __init__(self) -> None: ...
    @property
    def n_times(self): ...
    @property
    def annotations(self): ...
    def set_annotations(self, annotations) -> None: ...

MAX_N_SPLITS: int

class _ReservedFilename:
    fname: Incomplete
    remove: bool

    def __init__(self, fname) -> None: ...
    def __enter__(self): ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...

@dataclass(frozen=True)
class _RawFidWriterCfg:
    buffer_size: int
    split_size: int
    drop_small_buffer: bool
    fmt: str
    reset_range: bool = ...
    data_type: int = ...

    def __post_init__(self) -> None: ...
    def __init__(self, buffer_size, split_size, drop_small_buffer, fmt) -> None: ...

class _RawFidWriter:
    raw: Incomplete
    picks: Incomplete
    info: Incomplete
    projector: Incomplete
    cfg: Incomplete

    def __init__(self, raw, info, picks, projector, start, stop, cfg) -> None: ...
    start: Incomplete

    def write(self, fid, part_idx, prev_fname, next_fname): ...

def concatenate_raws(
    raws, preload=None, events_list=None, *, on_mismatch: str = "raise", verbose=None
):
    """## 🧠 Concatenate `mne.io.Raw` instances as if they were continuous.

    ### 💡 Note ``raws[0]`` is modified in-place to achieve the concatenation.
              Boundaries of the raw files are annotated bad. If you wish to use
              the data as continuous recording, you can remove the boundary
              annotations after concatenation (see
              `mne.Annotations.delete`).

    -----
    ### 🛠️ Parameters

    #### `raws : list`
        List of `mne.io.Raw` instances to concatenate (in order).

    #### `preload : bool, str, or None (default None)`
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory). If preload is
        None, preload=True or False is inferred using the preload status
        of the instances passed in.
    #### `events_list : None | list`
        The events to concatenate. Defaults to ``None``.

    #### `on_mismatch : 'raise' | 'warn' | 'ignore'`
        Can be ``'raise'`` (default) to raise an error, ``'warn'`` to emit a
        warning, or ``'ignore'`` to ignore when the device-to-head transformation differs between
        instances.

        ✨ Added in vesion 0.24

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `raw : instance of Raw`
        The result of the concatenation (first Raw instance passed in).
    #### `events : ndarray of int, shape (n_events, 3)`
        The events. Only returned if ``event_list`` is not None.
    """
    ...

def match_channel_orders(raws, copy: bool = True):
    """## 🧠 Ensure consistent channel order across raws.

    -----
    ### 🛠️ Parameters

    #### `raws : list`
        List of `mne.io.Raw` instances to order.

    #### `copy : bool`
        If ``True``, data will be copied. Otherwise data may be modified in place.
        Defaults to ``True``.

    -----
    ### ⏎ Returns

    list of Raw
        List of Raws with matched channel orders.
    """
    ...
