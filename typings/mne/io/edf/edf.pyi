from ..._fiff.constants import FIFF as FIFF
from ...annotations import Annotations as Annotations
from ...filter import resample as resample
from ...utils import fill_doc as fill_doc, logger as logger, warn as warn
from ..base import BaseRaw as BaseRaw
from _typeshed import Incomplete

CH_TYPE_MAPPING: Incomplete

class RawEDF(BaseRaw):
    """Raw object from EDF, EDF+ or BDF file.

    Parameters
    ----------
    input_fname : path-like
        Path to the EDF, EDF+ or BDF file.
    eog : list or tuple
        Names of channels or list of indices that should be designated EOG
        channels. Values should correspond to the electrodes in the file.
        Default is None.
    misc : list or tuple
        Names of channels or list of indices that should be designated MISC
        channels. Values should correspond to the electrodes in the file.
        Default is None.
    stim_channel : ``'auto'`` | str | list of str | int | list of int
        Defaults to ``'auto'``, which means that channels named ``'status'`` or
        ``'trigger'`` (case insensitive) are set to STIM. If str (or list of
        str), all channels matching the name(s) are set to STIM. If int (or
        list of ints), the channels corresponding to the indices are set to
        STIM.
    exclude : list of str
        Channel names to exclude. This can help when reading data with
        different sampling rates to avoid unnecessary resampling.
    infer_types : bool
        If True, try to infer channel types from channel labels. If a channel
        label starts with a known type (such as 'EEG') followed by a space and
        a name (such as 'Fp1'), the channel type will be set accordingly, and
        the channel will be renamed to the original label without the prefix.
        For unknown prefixes, the type will be 'EEG' and the name will not be
        modified. If False, do not infer types and assume all channels are of
        type 'EEG'.

        .. versionadded:: 0.24.1
    include : list of str | str
        Channel names to be included. A str is interpreted as a regular
        expression. 'exclude' must be empty if include is assigned.

        .. versionadded:: 1.1

    preload : bool or str (default False)
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).

    units : dict | str
        The units of the channels as stored in the file. This argument
        is useful only if the units are missing from the original file.
        If a dict, it must map a channel name to its unit, and if str
        it is assumed that all channels have the same units.

    encoding : str
        Encoding of annotations channel(s). Default is "utf8" (the only correct
        encoding according to the EDF+ standard).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    mne.io.Raw : Documentation of attributes and methods.
    mne.io.read_raw_edf : Recommended way to read EDF/EDF+ files.
    mne.io.read_raw_bdf : Recommended way to read BDF files.

    Notes
    -----

    :class:`mne.io.Raw` only stores signals with matching sampling frequencies.
    Therefore, if mixed sampling frequency signals are requested, all signals
    are upsampled to the highest loaded sampling frequency. In this case, using
    preload=True is recommended, as otherwise, edge artifacts appear when
    slices of the signal are requested.

    Biosemi devices trigger codes are encoded in 16-bit format, whereas system
    codes (CMS in/out-of range, battery low, etc.) are coded in bits 16-23 of
    the status channel (see http://www.biosemi.com/faq/trigger_signals.htm).
    To retrieve correct event values (bits 1-16), one could do:

        >>> events = mne.find_events(...)  # doctest:+SKIP
        >>> events[:, 2] &= (2**16 - 1)  # doctest:+SKIP

    The above operation can be carried out directly in :func:`mne.find_events`
    using the ``mask`` and ``mask_type`` parameters (see
    :func:`mne.find_events` for more details).

    It is also possible to retrieve system codes, but no particular effort has
    been made to decode these in MNE. In case it is necessary, for instance to
    check the CMS bit, the following operation can be carried out:

        >>> cms_bit = 20  # doctest:+SKIP
        >>> cms_high = (events[:, 2] & (1 << cms_bit)) != 0  # doctest:+SKIP

    It is worth noting that in some special cases, it may be necessary to shift
    event values in order to retrieve correct event triggers. This depends on
    the triggering device used to perform the synchronization. For instance, in
    some files events need to be shifted by 8 bits:

        >>> events[:, 2] >>= 8  # doctest:+SKIP

    TAL channels called 'EDF Annotations' or 'BDF Annotations' are parsed and
    extracted annotations are stored in raw.annotations. Use
    :func:`mne.events_from_annotations` to obtain events from these
    annotations.

    If channels named 'status' or 'trigger' are present, they are considered as
    STIM channels by default. Use func:`mne.find_events` to parse events
    encoded in such analog stim channels.
    """

    def __init__(
        self,
        input_fname,
        eog=...,
        misc=...,
        stim_channel: str = ...,
        exclude=...,
        infer_types: bool = ...,
        preload: bool = ...,
        include=...,
        units=...,
        encoding: str = ...,
        *,
        verbose=...,
    ) -> None: ...

class RawGDF(BaseRaw):
    """Raw object from GDF file.

    Parameters
    ----------
    input_fname : path-like
        Path to the GDF file.
    eog : list or tuple
        Names of channels or list of indices that should be designated EOG
        channels. Values should correspond to the electrodes in the file.
        Default is None.
    misc : list or tuple
        Names of channels or list of indices that should be designated MISC
        channels. Values should correspond to the electrodes in the file.
        Default is None.
    stim_channel : ``'auto'`` | str | list of str | int | list of int
        Defaults to 'auto', which means that channels named 'status' or
        'trigger' (case insensitive) are set to STIM. If str (or list of str),
        all channels matching the name(s) are set to STIM. If int (or list of
        ints), channels corresponding to the indices are set to STIM.
    exclude : list of str
        Channel names to exclude. This can help when reading data with
        different sampling rates to avoid unnecessary resampling.

        .. versionadded:: 0.24.1
    include : list of str | str
        Channel names to be included. A str is interpreted as a regular
        expression. 'exclude' must be empty if include is assigned.

        .. versionadded:: 1.1

    preload : bool or str (default False)
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    mne.io.Raw : Documentation of attributes and methods.
    mne.io.read_raw_gdf : Recommended way to read GDF files.

    Notes
    -----
    If channels named 'status' or 'trigger' are present, they are considered as
    STIM channels by default. Use func:`mne.find_events` to parse events
    encoded in such analog stim channels.
    """

    def __init__(
        self,
        input_fname,
        eog=...,
        misc=...,
        stim_channel: str = ...,
        exclude=...,
        preload: bool = ...,
        include=...,
        verbose=...,
    ) -> None: ...

INT8: str
UINT8: str
INT16: str
UINT16: str
INT32: str
UINT32: str
INT64: str
UINT64: str
FLOAT32: str
FLOAT64: str
GDFTYPE_NP: Incomplete
GDFTYPE_BYTE: Incomplete

def read_raw_edf(
    input_fname,
    eog=...,
    misc=...,
    stim_channel: str = ...,
    exclude=...,
    infer_types: bool = ...,
    include=...,
    preload: bool = ...,
    units=...,
    encoding: str = ...,
    *,
    verbose=...,
):
    """Reader function for EDF and EDF+ files.

    Parameters
    ----------
    input_fname : path-like
        Path to the EDF or EDF+ file.
    eog : list or tuple
        Names of channels or list of indices that should be designated EOG
        channels. Values should correspond to the electrodes in the file.
        Default is None.
    misc : list or tuple
        Names of channels or list of indices that should be designated MISC
        channels. Values should correspond to the electrodes in the file.
        Default is None.
    stim_channel : ``'auto'`` | str | list of str | int | list of int
        Defaults to ``'auto'``, which means that channels named ``'status'`` or
        ``'trigger'`` (case insensitive) are set to STIM. If str (or list of
        str), all channels matching the name(s) are set to STIM. If int (or
        list of ints), channels corresponding to the indices are set to STIM.
    exclude : list of str | str
        Channel names to exclude. This can help when reading data with
        different sampling rates to avoid unnecessary resampling. A str is
        interpreted as a regular expression.
    infer_types : bool
        If True, try to infer channel types from channel labels. If a channel
        label starts with a known type (such as 'EEG') followed by a space and
        a name (such as 'Fp1'), the channel type will be set accordingly, and
        the channel will be renamed to the original label without the prefix.
        For unknown prefixes, the type will be 'EEG' and the name will not be
        modified. If False, do not infer types and assume all channels are of
        type 'EEG'.

        .. versionadded:: 0.24.1
    include : list of str | str
        Channel names to be included. A str is interpreted as a regular
        expression. 'exclude' must be empty if include is assigned.

        .. versionadded:: 1.1

    preload : bool or str (default False)
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).

    units : dict | str
        The units of the channels as stored in the file. This argument
        is useful only if the units are missing from the original file.
        If a dict, it must map a channel name to its unit, and if str
        it is assumed that all channels have the same units.

    encoding : str
        Encoding of annotations channel(s). Default is "utf8" (the only correct
        encoding according to the EDF+ standard).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    raw : instance of RawEDF
        The raw instance.
        See :class:`mne.io.Raw` for documentation of attributes and methods.

    See Also
    --------
    mne.io.read_raw_bdf : Reader function for BDF files.
    mne.io.read_raw_gdf : Reader function for GDF files.
    mne.export.export_raw : Export function for EDF files.
    mne.io.Raw : Documentation of attributes and methods of RawEDF.

    Notes
    -----

    :class:`mne.io.Raw` only stores signals with matching sampling frequencies.
    Therefore, if mixed sampling frequency signals are requested, all signals
    are upsampled to the highest loaded sampling frequency. In this case, using
    preload=True is recommended, as otherwise, edge artifacts appear when
    slices of the signal are requested.

    It is worth noting that in some special cases, it may be necessary to shift
    event values in order to retrieve correct event triggers. This depends on
    the triggering device used to perform the synchronization. For instance, in
    some files events need to be shifted by 8 bits:

        >>> events[:, 2] >>= 8  # doctest:+SKIP

    TAL channels called 'EDF Annotations' are parsed and extracted annotations
    are stored in raw.annotations. Use :func:`mne.events_from_annotations` to
    obtain events from these annotations.

    If channels named 'status' or 'trigger' are present, they are considered as
    STIM channels by default. Use func:`mne.find_events` to parse events
    encoded in such analog stim channels.

    The EDF specification allows optional storage of channel types in the
    prefix of the signal label for each channel. For example, ``EEG Fz``
    implies that ``Fz`` is an EEG channel and ``MISC E`` would imply ``E`` is
    a MISC channel. However, there is no standard way of specifying all
    channel types. MNE-Python will try to infer the channel type, when such a
    string exists, defaulting to EEG, when there is no prefix or the prefix is
    not recognized.

    The following prefix strings are mapped to MNE internal types:

        - 'EEG': 'eeg'
        - 'SEEG': 'seeg'
        - 'ECOG': 'ecog'
        - 'DBS': 'dbs'
        - 'EOG': 'eog'
        - 'ECG': 'ecg'
        - 'EMG': 'emg'
        - 'BIO': 'bio'
        - 'RESP': 'resp'
        - 'MISC': 'misc'
        - 'SAO2': 'bio'

    The EDF specification allows storage of subseconds in measurement date.
    However, this reader currently sets subseconds to 0 by default.
    """

def read_raw_bdf(
    input_fname,
    eog=...,
    misc=...,
    stim_channel: str = ...,
    exclude=...,
    infer_types: bool = ...,
    include=...,
    preload: bool = ...,
    units=...,
    encoding: str = ...,
    *,
    verbose=...,
):
    """Reader function for BDF files.

    Parameters
    ----------
    input_fname : path-like
        Path to the BDF file.
    eog : list or tuple
        Names of channels or list of indices that should be designated EOG
        channels. Values should correspond to the electrodes in the file.
        Default is None.
    misc : list or tuple
        Names of channels or list of indices that should be designated MISC
        channels. Values should correspond to the electrodes in the file.
        Default is None.
    stim_channel : ``'auto'`` | str | list of str | int | list of int
        Defaults to ``'auto'``, which means that channels named ``'status'`` or
        ``'trigger'`` (case insensitive) are set to STIM. If str (or list of
        str), all channels matching the name(s) are set to STIM. If int (or
        list of ints), channels corresponding to the indices are set to STIM.
    exclude : list of str | str
        Channel names to exclude. This can help when reading data with
        different sampling rates to avoid unnecessary resampling. A str is
        interpreted as a regular expression.
    infer_types : bool
        If True, try to infer channel types from channel labels. If a channel
        label starts with a known type (such as 'EEG') followed by a space and
        a name (such as 'Fp1'), the channel type will be set accordingly, and
        the channel will be renamed to the original label without the prefix.
        For unknown prefixes, the type will be 'EEG' and the name will not be
        modified. If False, do not infer types and assume all channels are of
        type 'EEG'.

        .. versionadded:: 0.24.1
    include : list of str | str
        Channel names to be included. A str is interpreted as a regular
        expression. 'exclude' must be empty if include is assigned.

        .. versionadded:: 1.1

    preload : bool or str (default False)
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).

    units : dict | str
        The units of the channels as stored in the file. This argument
        is useful only if the units are missing from the original file.
        If a dict, it must map a channel name to its unit, and if str
        it is assumed that all channels have the same units.

    encoding : str
        Encoding of annotations channel(s). Default is "utf8" (the only correct
        encoding according to the EDF+ standard).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    raw : instance of RawEDF
        The raw instance.
        See :class:`mne.io.Raw` for documentation of attributes and methods.

    See Also
    --------
    mne.io.read_raw_edf : Reader function for EDF and EDF+ files.
    mne.io.read_raw_gdf : Reader function for GDF files.
    mne.io.Raw : Documentation of attributes and methods of RawEDF.

    Notes
    -----
    :class:`mne.io.Raw` only stores signals with matching sampling frequencies.
    Therefore, if mixed sampling frequency signals are requested, all signals
    are upsampled to the highest loaded sampling frequency. In this case, using
    preload=True is recommended, as otherwise, edge artifacts appear when
    slices of the signal are requested.

    Biosemi devices trigger codes are encoded in 16-bit format, whereas system
    codes (CMS in/out-of range, battery low, etc.) are coded in bits 16-23 of
    the status channel (see http://www.biosemi.com/faq/trigger_signals.htm).
    To retrieve correct event values (bits 1-16), one could do:

        >>> events = mne.find_events(...)  # doctest:+SKIP
        >>> events[:, 2] &= (2**16 - 1)  # doctest:+SKIP

    The above operation can be carried out directly in :func:`mne.find_events`
    using the ``mask`` and ``mask_type`` parameters (see
    :func:`mne.find_events` for more details).

    It is also possible to retrieve system codes, but no particular effort has
    been made to decode these in MNE. In case it is necessary, for instance to
    check the CMS bit, the following operation can be carried out:

        >>> cms_bit = 20  # doctest:+SKIP
        >>> cms_high = (events[:, 2] & (1 << cms_bit)) != 0  # doctest:+SKIP

    It is worth noting that in some special cases, it may be necessary to shift
    event values in order to retrieve correct event triggers. This depends on
    the triggering device used to perform the synchronization. For instance, in
    some files events need to be shifted by 8 bits:

        >>> events[:, 2] >>= 8  # doctest:+SKIP

    TAL channels called 'BDF Annotations' are parsed and extracted annotations
    are stored in raw.annotations. Use :func:`mne.events_from_annotations` to
    obtain events from these annotations.

    If channels named 'status' or 'trigger' are present, they are considered as
    STIM channels by default. Use func:`mne.find_events` to parse events
    encoded in such analog stim channels.
    """

def read_raw_gdf(
    input_fname,
    eog=...,
    misc=...,
    stim_channel: str = ...,
    exclude=...,
    include=...,
    preload: bool = ...,
    verbose=...,
):
    """Reader function for GDF files.

    Parameters
    ----------
    input_fname : path-like
        Path to the GDF file.
    eog : list or tuple
        Names of channels or list of indices that should be designated EOG
        channels. Values should correspond to the electrodes in the file.
        Default is None.
    misc : list or tuple
        Names of channels or list of indices that should be designated MISC
        channels. Values should correspond to the electrodes in the file.
        Default is None.
    stim_channel : ``'auto'`` | str | list of str | int | list of int
        Defaults to ``'auto'``, which means that channels named ``'status'`` or
        ``'trigger'`` (case insensitive) are set to STIM. If str (or list of
        str), all channels matching the name(s) are set to STIM. If int (or
        list of ints), channels corresponding to the indices are set to STIM.
    exclude : list of str | str
        Channel names to exclude. This can help when reading data with
        different sampling rates to avoid unnecessary resampling. A str is
        interpreted as a regular expression.
    include : list of str | str
        Channel names to be included. A str is interpreted as a regular
        expression. 'exclude' must be empty if include is assigned.

    preload : bool or str (default False)
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    raw : instance of RawGDF
        The raw instance.
        See :class:`mne.io.Raw` for documentation of attributes and methods.

    See Also
    --------
    mne.io.read_raw_edf : Reader function for EDF and EDF+ files.
    mne.io.read_raw_bdf : Reader function for BDF files.
    mne.io.Raw : Documentation of attributes and methods of RawGDF.

    Notes
    -----
    If channels named 'status' or 'trigger' are present, they are considered as
    STIM channels by default. Use func:`mne.find_events` to parse events
    encoded in such analog stim channels.
    """
