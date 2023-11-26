from ..utils import (
    check_fname as check_fname,
    fill_doc as fill_doc,
    logger as logger,
    object_diff as object_diff,
    repr_html as repr_html,
    warn as warn,
)
from ._digitization import DigPoint as DigPoint, write_dig as write_dig
from .compensator import get_current_comp as get_current_comp
from .constants import FIFF as FIFF
from .ctf_comp import write_ctf_comp as write_ctf_comp
from .open import fiff_open as fiff_open
from .pick import (
    channel_type as channel_type,
    get_channel_type_constants as get_channel_type_constants,
    pick_types as pick_types,
)
from .proj import Projection as Projection
from .tag import find_tag as find_tag, read_tag as read_tag
from .tree import dir_tree_find as dir_tree_find
from .write import (
    DATE_NONE as DATE_NONE,
    end_block as end_block,
    start_and_end_file as start_and_end_file,
    start_block as start_block,
    write_ch_info as write_ch_info,
    write_coord_trans as write_coord_trans,
    write_dig_points as write_dig_points,
    write_float as write_float,
    write_float_matrix as write_float_matrix,
    write_id as write_id,
    write_int as write_int,
    write_julian as write_julian,
    write_name_list_sanitized as write_name_list_sanitized,
    write_string as write_string,
)
from _typeshed import Incomplete

b = bytes

class MontageMixin:
    """### Mixin for Montage getting and setting."""

    def get_montage(self):
        """### Get a DigMontage from instance.

        -----
        ### ⏎ Returns


        montage : None | str | DigMontage
            A montage containing channel positions. If a string or
            `mne.channels.DigMontage` is
            specified, the existing channel information will be updated with the
            channel positions from the montage. Valid strings are the names of the
            built-in montages that ship with MNE-Python; you can list those via
            `mne.channels.get_builtin_montages`.
            If ``None`` (default), the channel positions will be removed from the
            `mne.Info`.
        """
        ...
    def set_montage(
        self,
        montage,
        match_case: bool = True,
        match_alias: bool = False,
        on_missing: str = "raise",
        verbose=None,
    ):
        """### Set EEG/sEEG/ECoG/DBS/fNIRS channel positions and digitization points.

        -----
        ### 🛠️ Parameters


        montage : None | str | DigMontage
            A montage containing channel positions. If a string or
            `mne.channels.DigMontage` is
            specified, the existing channel information will be updated with the
            channel positions from the montage. Valid strings are the names of the
            built-in montages that ship with MNE-Python; you can list those via
            `mne.channels.get_builtin_montages`.
            If ``None`` (default), the channel positions will be removed from the
            `mne.Info`.

        match_case : bool
            If True (default), channel name matching will be case sensitive.

            ✨ Added in vesion 0.20

        match_alias : bool | dict
            Whether to use a lookup table to match unrecognized channel location names
            to their known aliases. If True, uses the mapping in
            ``mne.io.constants.CHANNEL_LOC_ALIASES``. If a `dict` is passed, it
            will be used instead, and should map from non-standard channel names to
            names in the specified ``montage``. Default is ``False``.

            ✨ Added in vesion 0.23

        on_missing : 'raise' | 'warn' | 'ignore'
            Can be ``'raise'`` (default) to raise an error, ``'warn'`` to emit a
            warning, or ``'ignore'`` to ignore when channels have missing coordinates.

            ✨ Added in vesion 0.20.1

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns

        inst : instance of Raw | Epochs | Evoked
            The instance, modified in-place.

        -----
        ### 👉 See Also

        mne.channels.make_standard_montage
        mne.channels.make_dig_montage
        mne.channels.read_custom_montage

        -----
        ### 📖 Notes

        ### ⛔️ Warning
            Only EEG/sEEG/ECoG/DBS/fNIRS channels can have their positions set using
            a montage. Other channel types (e.g., MEG channels) should have
            their positions defined properly using their data reading
            functions.
        ### ⛔️ Warning
            Applying a montage will only set locations of channels that exist
            at the time it is applied. This means when
            `re-referencing <tut-set-eeg-ref>`
            make sure to apply the montage only after calling
            `mne.add_reference_channels`
        """
        ...

channel_type_constants: Incomplete

class SetChannelsMixin(MontageMixin):
    """### Mixin class for Raw, Evoked, Epochs."""

    def set_channel_types(self, mapping, *, on_unit_change: str = "warn", verbose=None):
        """### Specify the sensor types of channels.

        -----
        ### 🛠️ Parameters

        mapping : dict
            A dictionary mapping channel names to sensor types, e.g.,
            ``{'EEG061': 'eog'}``.
        on_unit_change : ``'raise'`` | ``'warn'`` | ``'ignore'``
            What to do if the measurement unit of a channel is changed
            automatically to match the new sensor type.

            ✨ Added in vesion 1.4

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns

        inst : instance of Raw | Epochs | Evoked
            The instance (modified in place).

            🎭 Changed in version 0.20
               Return the instance.

        -----
        ### 📖 Notes

        The following sensor types are accepted:

            ecg, eeg, emg, eog, exci, ias, misc, resp, seeg, dbs, stim, syst,
            ecog, hbo, hbr, fnirs_cw_amplitude, fnirs_fd_ac_amplitude,
            fnirs_fd_phase, fnirs_od, eyetrack_pos, eyetrack_pupil,
            temperature, gsr

        ✨ Added in vesion 0.9.0
        """
        ...
    def rename_channels(self, mapping, allow_duplicates: bool = False, *, verbose=None):
        """### Rename channels.

        -----
        ### 🛠️ Parameters


        mapping : dict | callable
            A dictionary mapping the old channel to a new channel name
            e.g. ``{'EEG061' : 'EEG161'}``. Can also be a callable function
            that takes and returns a string.

            🎭 Changed in version 0.10.0
               Support for a callable function.
        allow_duplicates : bool
            If True (default False), allow duplicates, which will automatically
            be renamed with ``-N`` at the end.

            ✨ Added in vesion 0.22.0

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns

        inst : instance of Raw | Epochs | Evoked
            The instance (modified in place).

            🎭 Changed in version 0.20
               Return the instance.

        -----
        ### 📖 Notes

        ✨ Added in vesion 0.9.0
        """
        ...
    def plot_sensors(
        self,
        kind: str = "topomap",
        ch_type=None,
        title=None,
        show_names: bool = False,
        ch_groups=None,
        to_sphere: bool = True,
        axes=None,
        block: bool = False,
        show: bool = True,
        sphere=None,
        *,
        verbose=None,
    ):
        """### Plot sensor positions.

        -----
        ### 🛠️ Parameters

        kind : str
            Whether to plot the sensors as 3d, topomap or as an interactive
            sensor selection dialog. Available options 'topomap', '3d',
            'select'. If 'select', a set of channels can be selected
            interactively by using lasso selector or clicking while holding
            control key. The selected channels are returned along with the
            figure instance. Defaults to 'topomap'.
        ch_type : None | str
            The channel type to plot. Available options ``'mag'``, ``'grad'``,
            ``'eeg'``, ``'seeg'``, ``'dbs'``, ``'ecog'``, ``'all'``. If ``'all'``, all
            the available mag, grad, eeg, seeg, dbs, and ecog channels are plotted. If
            None (default), then channels are chosen in the order given above.
        title : str | None
            Title for the figure. If None (default), equals to ``'Sensor
            positions (%s)' % ch_type``.
        show_names : bool | array of str
            Whether to display all channel names. If an array, only the channel
            names in the array are shown. Defaults to False.
        ch_groups : 'position' | array of shape (n_ch_groups, n_picks) | None
            Channel groups for coloring the sensors. If None (default), default
            coloring scheme is used. If 'position', the sensors are divided
            into 8 regions. See ``order`` kwarg of `mne.viz.plot_raw`. If
            array, the channels are divided by picks given in the array.

            ✨ Added in vesion 0.13.0
        to_sphere : bool
            Whether to project the 3d locations to a sphere. When False, the
            sensor array appears similar as to looking downwards straight above
            the subject's head. Has no effect when kind='3d'. Defaults to True.

            ✨ Added in vesion 0.14.0
        axes : instance of Axes | instance of Axes3D | None
            Axes to draw the sensors to. If ``kind='3d'``, axes must be an
            instance of Axes3D. If None (default), a new axes will be created.

            ✨ Added in vesion 0.13.0
        block : bool
            Whether to halt program execution until the figure is closed.
            Defaults to False.

            ✨ Added in vesion 0.13.0
        show : bool
            Show figure if True. Defaults to True.
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

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns

        fig : instance of Figure
            Figure containing the sensor topography.
        selection : list
            A list of selected channels. Only returned if ``kind=='select'``.

        -----
        ### 👉 See Also

        mne.viz.plot_layout

        -----
        ### 📖 Notes

        This function plots the sensor locations from the info structure using
        matplotlib. For drawing the sensors using PyVista see
        `mne.viz.plot_alignment`.

        ✨ Added in vesion 0.12.0
        """
        ...
    def anonymize(self, daysback=None, keep_his: bool = False, verbose=None):
        """### Anonymize measurement information in place.

        -----
        ### 🛠️ Parameters


        daysback : int | None
            Number of days to subtract from all dates.
            If ``None`` (default), the acquisition date, ``info['meas_date']``,
            will be set to ``January 1ˢᵗ, 2000``. This parameter is ignored if
            ``info['meas_date']`` is ``None`` (i.e., no acquisition date has been set).

        keep_his : bool
            If ``True``, ``his_id`` of ``subject_info`` will **not** be overwritten.
            Defaults to ``False``.

            ### ⛔️ Warning This could mean that ``info`` is not fully
                         anonymized. Use with caution.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns

        inst : instance of Raw | Epochs | Evoked
            The modified instance.

        -----
        ### 📖 Notes


        Removes potentially identifying information if it exists in ``info``.
        Specifically for each of the following we use:

        - meas_date, file_id, meas_id
                A default value, or as specified by ``daysback``.
        - subject_info
                Default values, except for 'birthday' which is adjusted
                to maintain the subject age.
        - experimenter, proj_name, description
                Default strings.
        - utc_offset
                ``None``.
        - proj_id
                Zeros.
        - proc_history
                Dates use the ``meas_date`` logic, and experimenter a default string.
        - helium_info, device_info
                Dates use the ``meas_date`` logic, meta info uses defaults.

        If ``info['meas_date']`` is ``None``, it will remain ``None`` during processing
        the above fields.

        Operates in place.

        ✨ Added in vesion 0.13.0
        """
        ...
    def set_meas_date(self, meas_date):
        """### Set the measurement start date.

        -----
        ### 🛠️ Parameters

        meas_date : datetime | float | tuple | None
            The new measurement date.
            If datetime object, it must be timezone-aware and in UTC.
            A tuple of (seconds, microseconds) or float (alias for
            ``(meas_date, 0)``) can also be passed and a datetime
            object will be automatically created. If None, will remove
            the time reference.

        -----
        ### ⏎ Returns

        inst : instance of Raw | Epochs | Evoked
            The modified raw instance. Operates in place.

        -----
        ### 👉 See Also

        mne.io.Raw.anonymize

        -----
        ### 📖 Notes

        If you want to remove all time references in the file, call
        `mne.io.anonymize_info(inst.info) <mne.io.anonymize_info>`
        after calling ``inst.set_meas_date(None)``.

        ✨ Added in vesion 0.20
        """
        ...

class ContainsMixin:
    """### Mixin class for Raw, Evoked, Epochs and Info."""

    def __contains__(self, ch_type) -> bool:
        """### Check channel type membership.

        -----
        ### 🛠️ Parameters

        ch_type : str
            Channel type to check for. Can be e.g. ``'meg'``, ``'eeg'``,
            ``'stim'``, etc.

        -----
        ### ⏎ Returns

        in : bool
            Whether or not the instance contains the given channel type.

        -----
        ### 🖥️ Examples

        Channel type membership can be tested as::

            >>> 'meg' in inst  # doctest: +SKIP
            True
            >>> 'seeg' in inst  # doctest: +SKIP
            False

        """
        ...
    @property
    def compensation_grade(self):
        """### The current gradient compensation grade."""
        ...
    def get_channel_types(
        self, picks=None, unique: bool = False, only_data_chs: bool = False
    ):
        """### Get a list of channel type for each channel.

        -----
        ### 🛠️ Parameters

        picks : str | array-like | slice | None
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel *type* strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick all channels. Note that channels in
            ``info['bads']`` *will be included* if their names or indices are
            explicitly provided.
        unique : bool
            Whether to return only unique channel types. Default is ``False``.
        only_data_chs : bool
            Whether to ignore non-data channels. Default is ``False``.

        -----
        ### ⏎ Returns

        channel_types : list
            The channel types.
        """
        ...

class MNEBadsList(list):
    """### Subclass of bads that checks inplace operations."""

    def __init__(self, *, bads, info) -> None: ...
    def extend(self, iterable): ...
    def append(self, x): ...
    def __iadd__(self, x): ...

class Info(dict, SetChannelsMixin, MontageMixin, ContainsMixin):
    """### Measurement information.

    This data structure behaves like a dictionary. It contains all metadata
    that is available for a recording. However, its keys are restricted to
    those provided by the
    `FIF format specification <https://github.com/mne-tools/fiff-constants>`__,
    so new entries should not be manually added.

    ### 💡 Note
        This class should not be instantiated directly via
        ``mne.Info(...)``. Instead, use `mne.create_info` to create
        measurement information from scratch.

    ### ⛔️ Warning
        The only entries that should be manually changed by the user are:
        ``info['bads']``, ``info['description']``, ``info['device_info']``
        ``info['dev_head_t']``, ``info['experimenter']``,
        ``info['helium_info']``, ``info['line_freq']``, ``info['temp']``,
        and ``info['subject_info']``.

        All other entries should be considered read-only, though they can be
        modified by various MNE-Python functions or methods (which have
        safeguards to ensure all fields remain in sync).

    -----
    ### 🛠️ Parameters

    *args : list
        Arguments.
    **kwargs : dict
        Keyword arguments.

    -----
    ### 📊 Attributes

    acq_pars : str | None
        MEG system acquisition parameters.
        See `mne.AcqParserFIF` for details.
    acq_stim : str | None
        MEG system stimulus parameters.
    bads : list of str
        List of bad (noisy/broken) channels, by name. These channels will by
        default be ignored by many processing steps.
    ch_names : list of str
        The names of the channels.
    chs : list of dict
        A list of channel information dictionaries, one per channel.
        See Notes for more information.
    command_line : str
        Contains the command and arguments used to create the source space
        (used for source estimation).
    comps : list of dict
        CTF software gradient compensation data.
        See Notes for more information.
    ctf_head_t : Transform | None
        The transformation from 4D/CTF head coordinates to Neuromag head
        coordinates. This is only present in 4D/CTF data.
    custom_ref_applied : int
        Whether a custom (=other than average) reference has been applied to
        the EEG data. This flag is checked by some algorithms that require an
        average reference to be set.
    description : str | None
        String description of the recording.
    dev_ctf_t : Transform | None
        The transformation from device coordinates to 4D/CTF head coordinates.
        This is only present in 4D/CTF data.
    dev_head_t : Transform | None
        The device to head transformation.
    device_info : dict | None
        Information about the acquisition device. See Notes for details.

        ✨ Added in vesion 0.19
    dig : list of dict | None
        The Polhemus digitization data in head coordinates.
        See Notes for more information.
    events : list of dict
        Event list, sometimes extracted from the stim channels by Neuromag
        systems. In general this should not be used and
        `mne.find_events` should be used for event processing.
        See Notes for more information.
    experimenter : str | None
        Name of the person that ran the experiment.
    file_id : dict | None
        The FIF globally unique ID. See Notes for more information.
    gantry_angle : float | None
        Tilt angle of the gantry in degrees.
    helium_info : dict | None
        Information about the device helium. See Notes for details.

        ✨ Added in vesion 0.19
    highpass : float
        Highpass corner frequency in Hertz. Zero indicates a DC recording.
    hpi_meas : list of dict
        HPI measurements that were taken at the start of the recording
        (e.g. coil frequencies).
        See Notes for details.
    hpi_results : list of dict
        Head position indicator (HPI) digitization points and fit information
        (e.g., the resulting transform).
        See Notes for details.
    hpi_subsystem : dict | None
        Information about the HPI subsystem that was used (e.g., event
        channel used for cHPI measurements).
        See Notes for details.
    kit_system_id : int
        Identifies the KIT system.
    line_freq : float | None
        Frequency of the power line in Hertz.
    lowpass : float
        Lowpass corner frequency in Hertz.
        It is automatically set to half the sampling rate if there is
        otherwise no low-pass applied to the data.
    maxshield : bool
        True if active shielding (IAS) was active during recording.
    meas_date : datetime
        The time (UTC) of the recording.

        🎭 Changed in version 0.20
           This is stored as a `python:datetime.datetime` object
           instead of a tuple of seconds/microseconds.
    meas_file : str | None
        Raw measurement file (used for source estimation).
    meas_id : dict | None
        The ID assigned to this measurement by the acquisition system or
        during file conversion. Follows the same format as ``file_id``.
    mri_file : str | None
        File containing the MRI to head transformation (used for source
        estimation).
    mri_head_t : dict | None
        Transformation from MRI to head coordinates (used for source
        estimation).
    mri_id : dict | None
        MRI unique ID (used for source estimation).
    nchan : int
        Number of channels.
    proc_history : list of dict
        The MaxFilter processing history.
        See Notes for details.
    proj_id : int | None
        ID number of the project the experiment belongs to.
    proj_name : str | None
        Name of the project the experiment belongs to.
    projs : list of Projection
        List of SSP operators that operate on the data.
        See `mne.Projection` for details.
    sfreq : float
        Sampling frequency in Hertz.
    subject_info : dict | None
        Information about the subject.
        See Notes for details.
    temp : object | None
        Can be used to store temporary objects in an Info instance. It will not
        survive an I/O roundtrip.

        ✨ Added in vesion 0.24
    utc_offset : str
        "UTC offset of related meas_date (sHH:MM).

        ✨ Added in vesion 0.19
    working_dir : str
        Working directory used when the source space was created (used for
        source estimation).
    xplotter_layout : str
        Layout of the Xplotter (Neuromag system only).

    -----
    ### 👉 See Also

    mne.create_info

    -----
    ### 📖 Notes

    The following parameters have a nested structure.

    * ``chs`` list of dict:

        cal : float
            The calibration factor to bring the channels to physical
            units. Used in product with ``range`` to scale the data read
            from disk.
        ch_name : str
            The channel name.
        coil_type : int
            Coil type, e.g. ``FIFFV_COIL_MEG``.
        coord_frame : int
            The coordinate frame used, e.g. ``FIFFV_COORD_HEAD``.
        kind : int
            The kind of channel, e.g. ``FIFFV_EEG_CH``.
        loc : array, shape (12,)
            Channel location information. The first three elements ``[:3]`` always store
            the nominal channel position. The remaining 9 elements store different
            information based on the channel type:

            MEG
                Remaining 9 elements ``[3:]``, contain the EX, EY, and EZ normal
                triplets (columns) of the coil rotation/orientation matrix.
            EEG
                Elements ``[3:6]`` contain the reference channel position.
            Eyetrack
                Element ``[3]`` contains information about which eye was tracked
                (-1 for left, 1 for right), and element ``[4]`` contains information
                about the the axis of coordinate data (-1 for x-coordinate data, 1 for
                y-coordinate data).
            Dipole
                Elements ``[3:6]`` contain dipole orientation information.
        logno : int
            Logical channel number, conventions in the usage of this
            number vary.
        range : float
            The hardware-oriented part of the calibration factor.
            This should be only applied to the continuous raw data.
            Used in product with ``cal`` to scale data read from disk.
        scanno : int
            Scanning order number, starting from 1.
        unit : int
            The unit to use, e.g. ``FIFF_UNIT_T_M``.
        unit_mul : int
            Unit multipliers, most commonly ``FIFF_UNITM_NONE``.

    * ``comps`` list of dict:

        ctfkind : int
            CTF compensation grade.
        colcals : ndarray
            Column calibrations.
        mat : dict
            A named matrix dictionary (with entries "data", "col_names", etc.)
            containing the compensation matrix.
        rowcals : ndarray
            Row calibrations.
        save_calibrated : bool
            Were the compensation data saved in calibrated form.

    * ``device_info`` dict:

        type : str
            Device type.
        model : str
            Device model.
        serial : str
            Device serial.
        site : str
            Device site.

    * ``dig`` list of dict:

        kind : int
            The kind of channel,
            e.g. ``FIFFV_POINT_EEG``, ``FIFFV_POINT_CARDINAL``.
        r : array, shape (3,)
            3D position in m. and coord_frame.
        ident : int
            Number specifying the identity of the point.
            e.g. ``FIFFV_POINT_NASION`` if kind is ``FIFFV_POINT_CARDINAL``, or
            42 if kind is ``FIFFV_POINT_EEG``.
        coord_frame : int
            The coordinate frame used, e.g. ``FIFFV_COORD_HEAD``.

    * ``events`` list of dict:

        channels : list of int
            Channel indices for the events.
        list : ndarray, shape (n_events * 3,)
            Events in triplets as number of samples, before, after.

    * ``file_id`` dict:

        version : int
            FIF format version, i.e. ``FIFFC_VERSION``.
        machid : ndarray, shape (2,)
            Unique machine ID, usually derived from the MAC address.
        secs : int
            Time in seconds.
        usecs : int
            Time in microseconds.

    * ``helium_info`` dict:

        he_level_raw : float
            Helium level (%) before position correction.
        helium_level : float
            Helium level (%) after position correction.
        orig_file_guid : str
            Original file GUID.
        meas_date : tuple of int
            The helium level meas date.

    * ``hpi_meas`` list of dict:

        creator : str
            Program that did the measurement.
        sfreq : float
            Sample rate.
        nchan : int
            Number of channels used.
        nave : int
            Number of averages used.
        ncoil : int
            Number of coils used.
        first_samp : int
            First sample used.
        last_samp : int
            Last sample used.
        hpi_coils : list of dict
            Coils, containing:

                number: int
                    Coil number
                epoch : ndarray
                    Buffer containing one epoch and channel.
                slopes : ndarray, shape (n_channels,)
                    HPI data.
                corr_coeff : ndarray, shape (n_channels,)
                    HPI curve fit correlations.
                coil_freq : float
                    HPI coil excitation frequency

    * ``hpi_results`` list of dict:

        dig_points : list
            Digitization points (see ``dig`` definition) for the HPI coils.
        order : ndarray, shape (ncoil,)
            The determined digitization order.
        used : ndarray, shape (nused,)
            The indices of the used coils.
        moments : ndarray, shape (ncoil, 3)
            The coil moments.
        goodness : ndarray, shape (ncoil,)
            The goodness of fits.
        good_limit : float
            The goodness of fit limit.
        dist_limit : float
            The distance limit.
        accept : int
            Whether or not the fit was accepted.
        coord_trans : instance of Transform
            The resulting MEG<->head transformation.

    * ``hpi_subsystem`` dict:

        ncoil : int
            The number of coils.
        event_channel : str
            The event channel used to encode cHPI status (e.g., STI201).
        hpi_coils : list of ndarray
            List of length ``ncoil``, each 4-element ndarray contains the
            event bits used on the event channel to indicate cHPI status
            (using the first element of these arrays is typically
            sufficient).

    * ``mri_id`` dict:

        version : int
            FIF format version, i.e. ``FIFFC_VERSION``.
        machid : ndarray, shape (2,)
            Unique machine ID, usually derived from the MAC address.
        secs : int
            Time in seconds.
        usecs : int
            Time in microseconds.

    * ``proc_history`` list of dict:

        block_id : dict
            See ``id`` above.
        date : ndarray, shape (2,)
            2-element tuple of seconds and microseconds.
        experimenter : str
            Name of the person who ran the program.
        creator : str
            Program that did the processing.
        max_info : dict
            Maxwel filtering info, can contain:

                sss_info : dict
                    SSS processing information.
                max_st
                    tSSS processing information.
                sss_ctc : dict
                    Cross-talk processing information.
                sss_cal : dict
                    Fine-calibration information.
        smartshield : dict
            MaxShield information. This dictionary is (always?) empty,
            but its presence implies that MaxShield was used during
            acquisition.

    * ``subject_info`` dict:

        id : int
            Integer subject identifier.
        his_id : str
            String subject identifier.
        last_name : str
            Last name.
        first_name : str
            First name.
        middle_name : str
            Middle name.
        birthday : tuple of int
            Birthday in (year, month, day) format.
        sex : int
            Subject sex (0=unknown, 1=male, 2=female).
        hand : int
            Handedness (1=right, 2=left, 3=ambidextrous).
        weight : float
            Weight in kilograms.
        height : float
            Height in meters.
    """

    def __init__(self, *args, **kwargs) -> None: ...
    def __setitem__(self, key, val) -> None:
        """### Attribute setter."""
        ...
    def update(self, other=None, **kwargs) -> None:
        """### Update method using __setitem__()."""
        ...
    def copy(self):
        """### Copy the instance.

        -----
        ### ⏎ Returns

        info : instance of Info
            The copied info.
        """
        ...
    def normalize_proj(self) -> None:
        """### (Re-)Normalize projection vectors after subselection.

        Applying projection after sub-selecting a set of channels that
        were originally used to compute the original projection vectors
        can be dangerous (e.g., if few channels remain, most power was
        in channels that are no longer picked, etc.). By default, mne
        will emit a warning when this is done.

        This function will re-normalize projectors to use only the
        remaining channels, thus avoiding that warning. Only use this
        function if you're confident that the projection vectors still
        adequately capture the original signal of interest.
        """
        ...
    def __deepcopy__(self, memodict):
        """### Make a deepcopy."""
        ...
    @property
    def ch_names(self): ...
    def save(self, fname) -> None:
        """### Write measurement info in fif file.

        -----
        ### 🛠️ Parameters

        fname : path-like
            The name of the file. Should end by ``'-info.fif'``.
        """
        ...

def read_fiducials(fname, verbose=None):
    """### Read fiducials from a fiff file.

    -----
    ### 🛠️ Parameters

    fname : path-like
        The filename to read.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    pts : list of dict
        List of digitizer points (each point in a dict).
    coord_frame : int
        The coordinate frame of the points (one of
        ``mne.io.constants.FIFF.FIFFV_COORD_...``).
    """
    ...

def write_fiducials(
    fname, pts, coord_frame: str = "unknown", *, overwrite: bool = False, verbose=None
) -> None:
    """### Write fiducials to a fiff file.

    -----
    ### 🛠️ Parameters

    fname : path-like
        Destination file name.
    pts : iterator of dict
        Iterator through digitizer points. Each point is a dictionary with
        the keys 'kind', 'ident' and 'r'.
    coord_frame : str | int
        The coordinate frame of the points. If a string, must be one of
        ``'meg'``, ``'mri'``, ``'mri_voxel'``, ``'head'``,
        ``'mri_tal'``, ``'ras'``, ``'fs_tal'``, ``'ctf_head'``,
        ``'ctf_meg'``, and ``'unknown'``
        If an integer, must be one of the constants defined as
        ``mne.io.constants.FIFF.FIFFV_COORD_...``.

    overwrite : bool
        If True (default False), overwrite the destination file if it
        exists.

        ✨ Added in vesion 1.0

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.
    """
    ...

def read_info(fname, verbose=None):
    """### Read measurement info from a file.

    -----
    ### 🛠️ Parameters

    fname : path-like
        File name.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns


    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    """
    ...

def read_bad_channels(fid, node):
    """### Read bad channels.

    -----
    ### 🛠️ Parameters

    fid : file
        The file descriptor.
    node : dict
        The node of the FIF tree that contains info on the bad channels.

    -----
    ### ⏎ Returns

    bads : list
        A list of bad channel's names.
    """
    ...

def read_meas_info(fid, tree, clean_bads: bool = False, verbose=None):
    """### Read the measurement info.

    -----
    ### 🛠️ Parameters

    fid : file
        Open file descriptor.
    tree : tree
        FIF tree structure.
    clean_bads : bool
        If True, clean info['bads'] before running consistency check.
        Should only be needed for old files where we did not check bads
        before saving.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns


    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    meas : dict
        Node in tree that contains the info.
    """
    ...

def write_meas_info(fid, info, data_type=None, reset_range: bool = True) -> None:
    """### Write measurement info into a file id (from a fif file).

    -----
    ### 🛠️ Parameters

    fid : file
        Open file descriptor.

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    data_type : int
        The data_type in case it is necessary. Should be 4 (FIFFT_FLOAT),
        5 (FIFFT_DOUBLE), or 16 (FIFFT_DAU_PACK16) for
        raw data.
    reset_range : bool
        If True, info['chs'][k]['range'] will be set to unity.

    -----
    ### 📖 Notes

    Tags are written in a particular order for compatibility with maxfilter.
    """
    ...

def write_info(fname, info, data_type=None, reset_range: bool = True) -> None:
    """### Write measurement info in fif file.

    -----
    ### 🛠️ Parameters

    fname : path-like
        The name of the file. Should end by ``-info.fif``.

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    data_type : int
        The data_type in case it is necessary. Should be 4 (FIFFT_FLOAT),
        5 (FIFFT_DOUBLE), or 16 (FIFFT_DAU_PACK16) for
        raw data.
    reset_range : bool
        If True, info['chs'][k]['range'] will be set to unity.
    """
    ...

def create_info(ch_names, sfreq, ch_types: str = "misc", verbose=None):
    """### Create a basic Info instance suitable for use with create_raw.

    -----
    ### 🛠️ Parameters

    ch_names : list of str | int
        Channel names. If an int, a list of channel names will be created
        from ``range(ch_names)``.
    sfreq : float
        Sample rate of the data.
    ch_types : list of str | str
        Channel types, default is ``'misc'`` which is not a
        :term:`data channel <data channels>`.
        Currently supported fields are 'ecg', 'bio', 'stim', 'eog', 'misc',
        'seeg', 'dbs', 'ecog', 'mag', 'eeg', 'ref_meg', 'grad', 'emg', 'hbr'
        'eyetrack' or 'hbo'.
        If str, then all channels are assumed to be of the same type.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns


    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.

    -----
    ### 📖 Notes

    The info dictionary will be sparsely populated to enable functionality
    within the rest of the package. Advanced functionality such as source
    localization can only be obtained through substantial, proper
    modifications of the info structure (not recommended).

    Note that the MEG device-to-head transform ``info['dev_head_t']`` will
    be initialized to the identity transform.

    Proper units of measure:

    * V: eeg, eog, seeg, dbs, emg, ecg, bio, ecog
    * T: mag
    * T/m: grad
    * M: hbo, hbr
    * Am: dipole
    * AU: misc
    """
    ...

RAW_INFO_FIELDS: Incomplete

def anonymize_info(info, daysback=None, keep_his: bool = False, verbose=None):
    """### Anonymize measurement information in place.

    ### ⛔️ Warning If ``info`` is part of an object like
                 `raw.info <mne.io.Raw>`, you should directly use
                 the method `raw.anonymize() <mne.io.Raw.anonymize>`
                 to ensure that all parts of the data are anonymized and
                 stay synchronized (e.g.,
                 `raw.annotations <mne.Annotations>`).

    -----
    ### 🛠️ Parameters


    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.

    daysback : int | None
        Number of days to subtract from all dates.
        If ``None`` (default), the acquisition date, ``info['meas_date']``,
        will be set to ``January 1ˢᵗ, 2000``. This parameter is ignored if
        ``info['meas_date']`` is ``None`` (i.e., no acquisition date has been set).

    keep_his : bool
        If ``True``, ``his_id`` of ``subject_info`` will **not** be overwritten.
        Defaults to ``False``.

        ### ⛔️ Warning This could mean that ``info`` is not fully
                     anonymized. Use with caution.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    info : instance of Info
        The anonymized measurement information.

    -----
    ### 📖 Notes


    Removes potentially identifying information if it exists in ``info``.
    Specifically for each of the following we use:

    - meas_date, file_id, meas_id
            A default value, or as specified by ``daysback``.
    - subject_info
            Default values, except for 'birthday' which is adjusted
            to maintain the subject age.
    - experimenter, proj_name, description
            Default strings.
    - utc_offset
            ``None``.
    - proj_id
            Zeros.
    - proc_history
            Dates use the ``meas_date`` logic, and experimenter a default string.
    - helium_info, device_info
            Dates use the ``meas_date`` logic, meta info uses defaults.

    If ``info['meas_date']`` is ``None``, it will remain ``None`` during processing
    the above fields.

    Operates in place.
    """
    ...
