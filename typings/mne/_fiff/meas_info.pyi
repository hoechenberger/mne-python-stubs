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
    """Set EEG/sEEG/ECoG/DBS/fNIRS channel positions and digitization points.

    Parameters
    ----------

    montage : None | str | DigMontage
        A montage containing channel positions. If a string or
        :class:mne.channels.DigMontage` is
        specified, the existing channel information will be updated with the
        channel positions from the montage. Valid strings are the names of the
        built-in montages that ship with MNE-Python; you can list those via
        :func:`mne.channels.get_builtin_montages`.
        If ``None`` (default), the channel positions will be removed from the
        :class:mne.Info`.

    match_case : bool
        If True (default), channel name matching will be case sensitive.

        .. versionadded:: 0.20

    match_alias : bool | dict
        Whether to use a lookup table to match unrecognized channel location names
        to their known aliases. If True, uses the mapping in
        ``mne.io.constants.CHANNEL_LOC_ALIASES``. If a :class:`dict` is passed, it
        will be used instead, and should map from non-standard channel names to
        names in the specified ``montage``. Default is ``False``.

        .. versionadded:: 0.23

    on_missing : 'raise' | 'warn' | 'ignore'
        Can be ``'raise'`` (default) to raise an error, ``'warn'`` to emit a
        warning, or ``'ignore'`` to ignore when channels have missing coordinates.

        .. versionadded:: 0.20.1

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    inst : instance of Raw | Epochs | Evoked
        The instance, modified in-place.

    See Also
    --------
    mne.channels.make_standard_montage
    mne.channels.make_dig_montage
    mne.channels.read_custom_montage

    Notes
    -----
    .. warning::
        Only EEG/sEEG/ECoG/DBS/fNIRS channels can have their positions set using
        a montage. Other channel types (e.g., MEG channels) should have
        their positions defined properly using their data reading
        functions.
    .. warning::
        Applying a montage will only set locations of channels that exist
        at the time it is applied. This means when
        :ref:`re-referencing <tut-set-eeg-ref>`
        make sure to apply the montage only after calling
        :func:`mne.add_reference_channels`
    """

    def get_montage(self):
        """Get a DigMontage from instance.

        Returns
        -------

        montage : None | str | DigMontage
            A montage containing channel positions. If a string or
            :class:mne.channels.DigMontage` is
            specified, the existing channel information will be updated with the
            channel positions from the montage. Valid strings are the names of the
            built-in montages that ship with MNE-Python; you can list those via
            :func:`mne.channels.get_builtin_montages`.
            If ``None`` (default), the channel positions will be removed from the
            :class:mne.Info`.
        """
    def set_montage(
        self,
        montage,
        match_case: bool = ...,
        match_alias: bool = ...,
        on_missing: str = ...,
        verbose=...,
    ):
        """Set EEG/sEEG/ECoG/DBS/fNIRS channel positions and digitization points.

        Parameters
        ----------

        montage : None | str | DigMontage
            A montage containing channel positions. If a string or
            :class:mne.channels.DigMontage` is
            specified, the existing channel information will be updated with the
            channel positions from the montage. Valid strings are the names of the
            built-in montages that ship with MNE-Python; you can list those via
            :func:`mne.channels.get_builtin_montages`.
            If ``None`` (default), the channel positions will be removed from the
            :class:mne.Info`.

        match_case : bool
            If True (default), channel name matching will be case sensitive.

            .. versionadded:: 0.20

        match_alias : bool | dict
            Whether to use a lookup table to match unrecognized channel location names
            to their known aliases. If True, uses the mapping in
            ``mne.io.constants.CHANNEL_LOC_ALIASES``. If a :class:`dict` is passed, it
            will be used instead, and should map from non-standard channel names to
            names in the specified ``montage``. Default is ``False``.

            .. versionadded:: 0.23

        on_missing : 'raise' | 'warn' | 'ignore'
            Can be ``'raise'`` (default) to raise an error, ``'warn'`` to emit a
            warning, or ``'ignore'`` to ignore when channels have missing coordinates.

            .. versionadded:: 0.20.1

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        inst : instance of Raw | Epochs | Evoked
            The instance, modified in-place.

        See Also
        --------
        mne.channels.make_standard_montage
        mne.channels.make_dig_montage
        mne.channels.read_custom_montage

        Notes
        -----
        .. warning::
            Only EEG/sEEG/ECoG/DBS/fNIRS channels can have their positions set using
            a montage. Other channel types (e.g., MEG channels) should have
            their positions defined properly using their data reading
            functions.
        .. warning::
            Applying a montage will only set locations of channels that exist
            at the time it is applied. This means when
            :ref:`re-referencing <tut-set-eeg-ref>`
            make sure to apply the montage only after calling
            :func:`mne.add_reference_channels`
        """

channel_type_constants: Incomplete

class SetChannelsMixin(MontageMixin):
    """Set the measurement start date.

    Parameters
    ----------
    meas_date : datetime | float | tuple | None
        The new measurement date.
        If datetime object, it must be timezone-aware and in UTC.
        A tuple of (seconds, microseconds) or float (alias for
        ``(meas_date, 0)``) can also be passed and a datetime
        object will be automatically created. If None, will remove
        the time reference.

    Returns
    -------
    inst : instance of Raw | Epochs | Evoked
        The modified raw instance. Operates in place.

    See Also
    --------
    mne.io.Raw.anonymize

    Notes
    -----
    If you want to remove all time references in the file, call
    :func:`mne.io.anonymize_info(inst.info) <mne.io.anonymize_info>`
    after calling ``inst.set_meas_date(None)``.

    .. versionadded:: 0.20
    """

    def set_channel_types(self, mapping, *, on_unit_change: str = ..., verbose=...):
        """Specify the sensor types of channels.

        Parameters
        ----------
        mapping : dict
            A dictionary mapping channel names to sensor types, e.g.,
            ``{'EEG061': 'eog'}``.
        on_unit_change : ``'raise'`` | ``'warn'`` | ``'ignore'``
            What to do if the measurement unit of a channel is changed
            automatically to match the new sensor type.

            .. versionadded:: 1.4

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        inst : instance of Raw | Epochs | Evoked
            The instance (modified in place).

            .. versionchanged:: 0.20
               Return the instance.

        Notes
        -----
        The following sensor types are accepted:

            ecg, eeg, emg, eog, exci, ias, misc, resp, seeg, dbs, stim, syst,
            ecog, hbo, hbr, fnirs_cw_amplitude, fnirs_fd_ac_amplitude,
            fnirs_fd_phase, fnirs_od, eyetrack_pos, eyetrack_pupil,
            temperature, gsr

        .. versionadded:: 0.9.0
        """
    def rename_channels(self, mapping, allow_duplicates: bool = ..., *, verbose=...):
        """Rename channels.

        Parameters
        ----------

        mapping : dict | callable
            A dictionary mapping the old channel to a new channel name
            e.g. ``{'EEG061' : 'EEG161'}``. Can also be a callable function
            that takes and returns a string.

            .. versionchanged:: 0.10.0
               Support for a callable function.
        allow_duplicates : bool
            If True (default False), allow duplicates, which will automatically
            be renamed with ``-N`` at the end.

            .. versionadded:: 0.22.0

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        inst : instance of Raw | Epochs | Evoked
            The instance (modified in place).

            .. versionchanged:: 0.20
               Return the instance.

        Notes
        -----
        .. versionadded:: 0.9.0
        """
    def plot_sensors(
        self,
        kind: str = ...,
        ch_type=...,
        title=...,
        show_names: bool = ...,
        ch_groups=...,
        to_sphere: bool = ...,
        axes=...,
        block: bool = ...,
        show: bool = ...,
        sphere=...,
        *,
        verbose=...,
    ):
        """Plot sensor positions.

        Parameters
        ----------
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
            into 8 regions. See ``order`` kwarg of :func:`mne.viz.plot_raw`. If
            array, the channels are divided by picks given in the array.

            .. versionadded:: 0.13.0
        to_sphere : bool
            Whether to project the 3d locations to a sphere. When False, the
            sensor array appears similar as to looking downwards straight above
            the subject's head. Has no effect when kind='3d'. Defaults to True.

            .. versionadded:: 0.14.0
        axes : instance of Axes | instance of Axes3D | None
            Axes to draw the sensors to. If ``kind='3d'``, axes must be an
            instance of Axes3D. If None (default), a new axes will be created.

            .. versionadded:: 0.13.0
        block : bool
            Whether to halt program execution until the figure is closed.
            Defaults to False.

            .. versionadded:: 0.13.0
        show : bool
            Show figure if True. Defaults to True.
        sphere : float | array-like | instance of ConductorModel | None  | 'auto' | 'eeglab'
            The sphere parameters to use for the head outline. Can be array-like of
            shape (4,) to give the X/Y/Z origin and radius in meters, or a single float
            to give just the radius (origin assumed 0, 0, 0). Can also be an instance
            of a spherical :class:mne.bem.ConductorModel` to use the origin and
            radius from that object. If ``'auto'`` the sphere is fit to digitization
            points. If ``'eeglab'`` the head circle is defined by EEG electrodes
            ``'Fpz'``, ``'Oz'``, ``'T7'``, and ``'T8'`` (if ``'Fpz'`` is not present,
            it will be approximated from the coordinates of ``'Oz'``). ``None`` (the
            default) is equivalent to ``'auto'`` when enough extra digitization points
            are available, and (0, 0, 0, 0.095) otherwise.

            .. versionadded:: 0.20
            .. versionchanged:: 1.1 Added ``'eeglab'`` option.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        fig : instance of Figure
            Figure containing the sensor topography.
        selection : list
            A list of selected channels. Only returned if ``kind=='select'``.

        See Also
        --------
        mne.viz.plot_layout

        Notes
        -----
        This function plots the sensor locations from the info structure using
        matplotlib. For drawing the sensors using PyVista see
        :func:`mne.viz.plot_alignment`.

        .. versionadded:: 0.12.0
        """
    def anonymize(self, daysback=..., keep_his: bool = ..., verbose=...):
        """Anonymize measurement information in place.

        Parameters
        ----------

        daysback : int | None
            Number of days to subtract from all dates.
            If ``None`` (default), the acquisition date, ``info['meas_date']``,
            will be set to ``January 1ˢᵗ, 2000``. This parameter is ignored if
            ``info['meas_date']`` is ``None`` (i.e., no acquisition date has been set).

        keep_his : bool
            If ``True``, ``his_id`` of ``subject_info`` will **not** be overwritten.
            Defaults to ``False``.

            .. warning:: This could mean that ``info`` is not fully
                         anonymized. Use with caution.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        inst : instance of Raw | Epochs | Evoked
            The modified instance.

        Notes
        -----

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

        .. versionadded:: 0.13.0
        """
    def set_meas_date(self, meas_date):
        """Set the measurement start date.

        Parameters
        ----------
        meas_date : datetime | float | tuple | None
            The new measurement date.
            If datetime object, it must be timezone-aware and in UTC.
            A tuple of (seconds, microseconds) or float (alias for
            ``(meas_date, 0)``) can also be passed and a datetime
            object will be automatically created. If None, will remove
            the time reference.

        Returns
        -------
        inst : instance of Raw | Epochs | Evoked
            The modified raw instance. Operates in place.

        See Also
        --------
        mne.io.Raw.anonymize

        Notes
        -----
        If you want to remove all time references in the file, call
        :func:`mne.io.anonymize_info(inst.info) <mne.io.anonymize_info>`
        after calling ``inst.set_meas_date(None)``.

        .. versionadded:: 0.20
        """

class ContainsMixin:
    """Get a list of channel type for each channel.

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
    unique : bool
        Whether to return only unique channel types. Default is ``False``.
    only_data_chs : bool
        Whether to ignore non-data channels. Default is ``False``.

    Returns
    -------
    channel_types : list
        The channel types.
    """

    def __contains__(self, ch_type) -> bool:
        """Check channel type membership.

        Parameters
        ----------
        ch_type : str
            Channel type to check for. Can be e.g. ``'meg'``, ``'eeg'``,
            ``'stim'``, etc.

        Returns
        -------
        in : bool
            Whether or not the instance contains the given channel type.

        Examples
        --------
        Channel type membership can be tested as::

            >>> 'meg' in inst  # doctest: +SKIP
            True
            >>> 'seeg' in inst  # doctest: +SKIP
            False

        """
    @property
    def compensation_grade(self):
        """The current gradient compensation grade."""
    def get_channel_types(
        self, picks=..., unique: bool = ..., only_data_chs: bool = ...
    ):
        """Get a list of channel type for each channel.

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
        unique : bool
            Whether to return only unique channel types. Default is ``False``.
        only_data_chs : bool
            Whether to ignore non-data channels. Default is ``False``.

        Returns
        -------
        channel_types : list
            The channel types.
        """

class MNEBadsList(list):
    """Subclass of bads that checks inplace operations."""

    def __init__(self, *, bads, info) -> None: ...
    def extend(self, iterable): ...
    def append(self, x): ...
    def __iadd__(self, x): ...

class Info(dict, SetChannelsMixin, MontageMixin, ContainsMixin):
    """Write measurement info in fif file.

    Parameters
    ----------
    fname : path-like
        The name of the file. Should end by ``'-info.fif'``.
    """

    def __init__(self, *args, **kwargs) -> None: ...
    def __setitem__(self, key, val) -> None:
        """Attribute setter."""
    def update(self, other=..., **kwargs) -> None:
        """Update method using __setitem__()."""
    def copy(self):
        """Copy the instance.

        Returns
        -------
        info : instance of Info
            The copied info.
        """
    def normalize_proj(self) -> None:
        """(Re-)Normalize projection vectors after subselection.

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
    def __deepcopy__(self, memodict):
        """Make a deepcopy."""
    @property
    def ch_names(self): ...
    def save(self, fname) -> None:
        """Write measurement info in fif file.

        Parameters
        ----------
        fname : path-like
            The name of the file. Should end by ``'-info.fif'``.
        """

def read_fiducials(fname, verbose=...):
    """Read fiducials from a fiff file.

    Parameters
    ----------
    fname : path-like
        The filename to read.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    pts : list of dict
        List of digitizer points (each point in a dict).
    coord_frame : int
        The coordinate frame of the points (one of
        ``mne.io.constants.FIFF.FIFFV_COORD_...``).
    """

def write_fiducials(
    fname, pts, coord_frame: str = ..., *, overwrite: bool = ..., verbose=...
) -> None:
    """Write fiducials to a fiff file.

    Parameters
    ----------
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

        .. versionadded:: 1.0

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.
    """

def read_info(fname, verbose=...):
    """Read measurement info from a file.

    Parameters
    ----------
    fname : path-like
        File name.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------

    info : mne.Info
        The :class:`mne.Info` object with information about the sensors and methods of measurement.
    """

def read_bad_channels(fid, node):
    """Read bad channels.

    Parameters
    ----------
    fid : file
        The file descriptor.
    node : dict
        The node of the FIF tree that contains info on the bad channels.

    Returns
    -------
    bads : list
        A list of bad channel's names.
    """

def read_meas_info(fid, tree, clean_bads: bool = ..., verbose=...):
    """Read the measurement info.

    Parameters
    ----------
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
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------

    info : mne.Info
        The :class:`mne.Info` object with information about the sensors and methods of measurement.
    meas : dict
        Node in tree that contains the info.
    """

def write_meas_info(fid, info, data_type=..., reset_range: bool = ...) -> None:
    """Write measurement info into a file id (from a fif file).

    Parameters
    ----------
    fid : file
        Open file descriptor.

    info : mne.Info
        The :class:`mne.Info` object with information about the sensors and methods of measurement.
    data_type : int
        The data_type in case it is necessary. Should be 4 (FIFFT_FLOAT),
        5 (FIFFT_DOUBLE), or 16 (FIFFT_DAU_PACK16) for
        raw data.
    reset_range : bool
        If True, info['chs'][k]['range'] will be set to unity.

    Notes
    -----
    Tags are written in a particular order for compatibility with maxfilter.
    """

def write_info(fname, info, data_type=..., reset_range: bool = ...) -> None:
    """Write measurement info in fif file.

    Parameters
    ----------
    fname : path-like
        The name of the file. Should end by ``-info.fif``.

    info : mne.Info
        The :class:`mne.Info` object with information about the sensors and methods of measurement.
    data_type : int
        The data_type in case it is necessary. Should be 4 (FIFFT_FLOAT),
        5 (FIFFT_DOUBLE), or 16 (FIFFT_DAU_PACK16) for
        raw data.
    reset_range : bool
        If True, info['chs'][k]['range'] will be set to unity.
    """

def create_info(ch_names, sfreq, ch_types: str = ..., verbose=...):
    """Create a basic Info instance suitable for use with create_raw.

    Parameters
    ----------
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
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------

    info : mne.Info
        The :class:`mne.Info` object with information about the sensors and methods of measurement.

    Notes
    -----
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

RAW_INFO_FIELDS: Incomplete

def anonymize_info(info, daysback=..., keep_his: bool = ..., verbose=...):
    """Anonymize measurement information in place.

    .. warning:: If ``info`` is part of an object like
                 :class:`raw.info <mne.io.Raw>`, you should directly use
                 the method :meth:`raw.anonymize() <mne.io.Raw.anonymize>`
                 to ensure that all parts of the data are anonymized and
                 stay synchronized (e.g.,
                 :class:`raw.annotations <mne.Annotations>`).

    Parameters
    ----------

    info : mne.Info
        The :class:`mne.Info` object with information about the sensors and methods of measurement.

    daysback : int | None
        Number of days to subtract from all dates.
        If ``None`` (default), the acquisition date, ``info['meas_date']``,
        will be set to ``January 1ˢᵗ, 2000``. This parameter is ignored if
        ``info['meas_date']`` is ``None`` (i.e., no acquisition date has been set).

    keep_his : bool
        If ``True``, ``his_id`` of ``subject_info`` will **not** be overwritten.
        Defaults to ``False``.

        .. warning:: This could mean that ``info`` is not fully
                     anonymized. Use with caution.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    info : instance of Info
        The anonymized measurement information.

    Notes
    -----

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
