from ._fiff.constants import FIFF as FIFF
from ._fiff.open import fiff_open as fiff_open
from ._fiff.pick import pick_channels as pick_channels
from ._fiff.tag import read_tag as read_tag
from ._fiff.tree import dir_tree_find as dir_tree_find
from ._fiff.write import (
    end_block as end_block,
    start_and_end_file as start_and_end_file,
    start_block as start_block,
    write_int as write_int,
)
from .utils import (
    check_fname as check_fname,
    fill_doc as fill_doc,
    logger as logger,
    warn as warn,
)
from _typeshed import Incomplete

def pick_events(events, include=None, exclude=None, step: bool = False):
    """Select some :term:`events`.

    Parameters
    ----------

    events : array of int, shape (n_events, 3)
        The array of :term:`events`. The first column contains the event time in
        samples, with :term:`first_samp` included. The third column contains the
        event id.
    include : int | list | None
        A event id to include or a list of them.
        If None all events are included.
    exclude : int | list | None
        A event id to exclude or a list of them.
        If None no event is excluded. If include is not None
        the exclude parameter is ignored.
    step : bool
        If True (default is False), events have a step format according
        to the argument output='step' in the function find_events().
        In this case, the two last columns are considered in inclusion/
        exclusion criteria.

    Returns
    -------
    events : array, shape (n_events, 3)
        The list of events.
    """
    ...

def define_target_events(
    events, reference_id, target_id, sfreq, tmin, tmax, new_id=None, fill_na=None
):
    """Define new events by co-occurrence of existing events.

    This function can be used to evaluate events depending on the
    temporal lag to another event. For example, this can be used to
    analyze evoked responses which were followed by a button press within
    a defined time window.

    Parameters
    ----------
    events : ndarray
        Array as returned by mne.find_events.
    reference_id : int
        The reference event. The event defining the epoch of interest.
    target_id : int
        The target event. The event co-occurring in within a certain time
        window around the reference event.
    sfreq : float
        The sampling frequency of the data.
    tmin : float
        The lower limit in seconds from the target event.
    tmax : float
        The upper limit border in seconds from the target event.
    new_id : int
        New ID for the new event.
    fill_na : int | None
        Fill event to be inserted if target is not available within the time
        window specified. If None, the 'null' events will be dropped.

    Returns
    -------
    new_events : ndarray
        The new defined events.
    lag : ndarray
        Time lag between reference and target in milliseconds.
    """
    ...

def read_events(
    filename,
    include=None,
    exclude=None,
    mask=None,
    mask_type: str = "and",
    return_event_id: bool = False,
    verbose=None,
):
    """Read :term:`events` from fif or text file.

    See :ref:`tut-events-vs-annotations` and :ref:`tut-event-arrays`
    for more information about events.

    Parameters
    ----------
    filename : path-like
        Name of the input file.
        If the extension is ``.fif``, events are read assuming
        the file is in FIF format, otherwise (e.g., ``.eve``,
        ``.lst``, ``.txt``) events are read as coming from text.
        Note that new format event files do not contain
        the ``"time"`` column (used to be the second column).
    include : int | list | None
        A event id to include or a list of them.
        If None all events are included.
    exclude : int | list | None
        A event id to exclude or a list of them.
        If None no event is excluded. If include is not None
        the exclude parameter is ignored.
    mask : int | None
        The value of the digital mask to apply to the stim channel values.
        If None (default), no masking is performed.
    mask_type : ``'and'`` | ``'not_and'``
        The type of operation between the mask and the trigger.
        Choose 'and' (default) for MNE-C masking behavior.

        .. versionadded:: 0.13
    return_event_id : bool
        If True, ``event_id`` will be returned. This is only possible for
        ``-annot.fif`` files produced with MNE-C ``mne_browse_raw``.

        .. versionadded:: 0.20

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------

    events : array of int, shape (n_events, 3)
        The array of :term:`events`. The first column contains the event time in
        samples, with :term:`first_samp` included. The third column contains the
        event id.
    event_id : dict
        Dictionary of ``{str: int}`` mappings of event IDs.

    See Also
    --------
    find_events, write_events

    Notes
    -----
    This function will discard the offset line (i.e., first line with zero
    event number) if it is present in a text file.

    For more information on ``mask`` and ``mask_type``, see
    :func:`mne.find_events`.
    """
    ...

def write_events(filename, events, *, overwrite: bool = False, verbose=None) -> None:
    """Write :term:`events` to file.

    Parameters
    ----------
    filename : path-like
        Name of the output file.
        If the extension is ``.fif``, events are written in
        binary FIF format, otherwise (e.g., ``.eve``,
        ``.lst``, ``.txt``) events are written as plain text.
        Note that new format event files do not contain
        the ``"time"`` column (used to be the second column).

    events : array of int, shape (n_events, 3)
        The array of :term:`events`. The first column contains the event time in
        samples, with :term:`first_samp` included. The third column contains the
        event id.

    overwrite : bool
        If True (default False), overwrite the destination file if it
        exists.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    read_events
    """
    ...

def find_stim_steps(
    raw, pad_start=None, pad_stop=None, merge: int = 0, stim_channel=None
):
    """Find all steps in data from a stim channel.

    Parameters
    ----------
    raw : Raw object
        The raw data.
    pad_start : None | int
        Values to assume outside of the stim channel (e.g., if pad_start=0 and
        the stim channel starts with value 5, an event of [0, 0, 5] will be
        inserted at the beginning). With None, no steps will be inserted.
    pad_stop : None | int
        Values to assume outside of the stim channel, see ``pad_start``.
    merge : int
        Merge steps occurring in neighboring samples. The integer value
        indicates over how many samples events should be merged, and the sign
        indicates in which direction they should be merged (negative means
        towards the earlier event, positive towards the later event).
    stim_channel : None | str | list of str
        Name of the stim channel or all the stim channels
        affected by the trigger. If None, the config variables
        'MNE_STIM_CHANNEL', 'MNE_STIM_CHANNEL_1', 'MNE_STIM_CHANNEL_2',
        etc. are read. If these are not found, it will default to
        'STI101' or 'STI 014', whichever is present.

    Returns
    -------
    steps : array, shape = (n_samples, 3)
        For each step in the stim channel the values [sample, v_from, v_to].
        The first column contains the event time in samples (the first sample
        with the new value). The second column contains the stim channel value
        before the step, and the third column contains value after the step.

    See Also
    --------
    find_events : More sophisticated options for finding events in a Raw file.
    """
    ...

def find_events(
    raw,
    stim_channel=None,
    output: str = "onset",
    consecutive: str = "increasing",
    min_duration: int = 0,
    shortest_event: int = 2,
    mask=None,
    uint_cast: bool = False,
    mask_type: str = "and",
    initial_event: bool = False,
    verbose=None,
):
    """Find :term:`events` from raw file.

    See :ref:`tut-events-vs-annotations` and :ref:`tut-event-arrays`
    for more information about events.

    Parameters
    ----------
    raw : Raw object
        The raw data.
    stim_channel : None | str | list of str
        Name of the stim channel or all the stim channels
        affected by triggers. If None, the config variables
        'MNE_STIM_CHANNEL', 'MNE_STIM_CHANNEL_1', 'MNE_STIM_CHANNEL_2',
        etc. are read. If these are not found, it will fall back to
        'STI 014' if present, then fall back to the first channel of type
        'stim', if present. If multiple channels are provided
        then the returned events are the union of all the events
        extracted from individual stim channels.
    output : 'onset' | 'offset' | 'step'
        Whether to report when events start, when events end, or both.
    consecutive : bool | 'increasing'
        If True, consider instances where the value of the events
        channel changes without first returning to zero as multiple
        events. If False, report only instances where the value of the
        events channel changes from/to zero. If 'increasing', report
        adjacent events only when the second event code is greater than
        the first.
    min_duration : float
        The minimum duration of a change in the events channel required
        to consider it as an event (in seconds).
    shortest_event : int
        Minimum number of samples an event must last (default is 2). If the
        duration is less than this an exception will be raised.
    mask : int | None
        The value of the digital mask to apply to the stim channel values.
        If None (default), no masking is performed.
    uint_cast : bool
        If True (default False), do a cast to ``uint16`` on the channel
        data. This can be used to fix a bug with STI101 and STI014 in
        Neuromag acquisition setups that use channel STI016 (channel 16
        turns data into e.g. -32768), similar to ``mne_fix_stim14 --32``
        in MNE-C.

        .. versionadded:: 0.12
    mask_type : 'and' | 'not_and'
        The type of operation between the mask and the trigger.
        Choose 'and' (default) for MNE-C masking behavior.

        .. versionadded:: 0.13
    initial_event : bool
        If True (default False), an event is created if the stim channel has a
        value different from 0 as its first sample. This is useful if an event
        at t=0s is present.

        .. versionadded:: 0.16

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------

    events : array of int, shape (n_events, 3)
        The array of :term:`events`. The first column contains the event time in
        samples, with :term:`first_samp` included. The third column contains the
        event id.

    See Also
    --------
    find_stim_steps : Find all the steps in the stim channel.
    read_events : Read events from disk.
    write_events : Write events to disk.

    Notes
    -----
    .. warning:: If you are working with downsampled data, events computed
                 before decimation are no longer valid. Please recompute
                 your events after decimation, but note this reduces the
                 precision of event timing.

    Examples
    --------
    Consider data with a stim channel that looks like::

        [0, 32, 32, 33, 32, 0]

    By default, find_events returns all samples at which the value of the
    stim channel increases::

        >>> print(find_events(raw)) # doctest: +SKIP
        [[ 1  0 32]
         [ 3 32 33]]

    If consecutive is False, find_events only returns the samples at which
    the stim channel changes from zero to a non-zero value::

        >>> print(find_events(raw, consecutive=False)) # doctest: +SKIP
        [[ 1  0 32]]

    If consecutive is True, find_events returns samples at which the
    event changes, regardless of whether it first returns to zero::

        >>> print(find_events(raw, consecutive=True)) # doctest: +SKIP
        [[ 1  0 32]
         [ 3 32 33]
         [ 4 33 32]]

    If output is 'offset', find_events returns the last sample of each event
    instead of the first one::

        >>> print(find_events(raw, consecutive=True, # doctest: +SKIP
        ...                   output='offset'))
        [[ 2 33 32]
         [ 3 32 33]
         [ 4  0 32]]

    If output is 'step', find_events returns the samples at which an event
    starts or ends::

        >>> print(find_events(raw, consecutive=True, # doctest: +SKIP
        ...                   output='step'))
        [[ 1  0 32]
         [ 3 32 33]
         [ 4 33 32]
         [ 5 32  0]]

    To ignore spurious events, it is also possible to specify a minimum
    event duration. Assuming our events channel has a sample rate of
    1000 Hz::

        >>> print(find_events(raw, consecutive=True, # doctest: +SKIP
        ...                   min_duration=0.002))
        [[ 1  0 32]]

    For the digital mask, if mask_type is set to 'and' it will take the
    binary representation of the digital mask, e.g. 5 -> '00000101', and will
    allow the values to pass where mask is one, e.g.::

              7 '0000111' <- trigger value
             37 '0100101' <- mask
         ----------------
              5 '0000101'

    For the digital mask, if mask_type is set to 'not_and' it will take the
    binary representation of the digital mask, e.g. 5 -> '00000101', and will
    block the values where mask is one, e.g.::

              7 '0000111' <- trigger value
             37 '0100101' <- mask
         ----------------
              2 '0000010'
    """
    ...

def merge_events(events, ids, new_id, replace_events: bool = True):
    """Merge a set of :term:`events`.

    Parameters
    ----------
    events : array, shape (n_events_in, 3)
        Events.
    ids : array of int
        The ids of events to merge.
    new_id : int
        The new id.
    replace_events : bool
        If True (default), old event ids are replaced. Otherwise,
        new events will be added to the old event list.

    Returns
    -------
    new_events : array, shape (n_events_out, 3)
        The new events.

    Notes
    -----
    Rather than merging events you can use hierarchical event_id
    in Epochs. For example, here::

        >>> event_id = {'auditory/left': 1, 'auditory/right': 2}

    And the condition 'auditory' would correspond to either 1 or 2.

    Examples
    --------
    Here is quick example of the behavior::

        >>> events = [[134, 0, 1], [341, 0, 2], [502, 0, 3]]
        >>> merge_events(events, [1, 2], 12, replace_events=True)
        array([[134,   0,  12],
               [341,   0,  12],
               [502,   0,   3]])
        >>> merge_events(events, [1, 2], 12, replace_events=False)
        array([[134,   0,   1],
               [134,   0,  12],
               [341,   0,   2],
               [341,   0,  12],
               [502,   0,   3]])
    """
    ...

def shift_time_events(events, ids, tshift, sfreq):
    """Shift a set of :term:`events`.

    Parameters
    ----------

    events : array of int, shape (n_events, 3)
        The array of :term:`events`. The first column contains the event time in
        samples, with :term:`first_samp` included. The third column contains the
        event id.
    ids : ndarray of int | None
        The ids of events to shift.
    tshift : float
        Time-shift event. Use positive value tshift for forward shifting
        the event and negative value for backward shift.
    sfreq : float
        The sampling frequency of the data.

    Returns
    -------
    new_events : array of int, shape (n_new_events, 3)
        The new events.
    """
    ...

def make_fixed_length_events(
    raw,
    id: int = 1,
    start: int = 0,
    stop=None,
    duration: float = 1.0,
    first_samp: bool = True,
    overlap: float = 0.0,
):
    """Make a set of :term:`events` separated by a fixed duration.

    Parameters
    ----------
    raw : instance of Raw
        A raw object to use the data from.
    id : int
        The id to use (default 1).
    start : float
        Time of first event (in seconds).
    stop : float | None
        Maximum time of last event (in seconds). If None, events extend to the
        end of the recording.
    duration : float
        The duration to separate events by (in seconds).
    first_samp : bool
        If True (default), times will have :term:`first_samp` added to them, as
        in :func:`mne.find_events`. This behavior is not desirable if the
        returned events will be combined with event times that already
        have :term:`first_samp` added to them, e.g. event times that come
        from :func:`mne.find_events`.
    overlap : float
        The overlap between events (in seconds).
        Must be ``0 <= overlap < duration``.

        .. versionadded:: 0.18

    Returns
    -------

    events : array of int, shape (n_events, 3)
        The array of :term:`events`. The first column contains the event time in
        samples, with :term:`first_samp` included. The third column contains the
        event id.
    """
    ...

def concatenate_events(events, first_samps, last_samps):
    """Concatenate event lists to be compatible with concatenate_raws.

    This is useful, for example, if you processed and/or changed
    events in raw files separately before combining them using
    :func:`mne.concatenate_raws`.

    Parameters
    ----------
    events : list of array
        List of :term:`events` arrays, typically each extracted from a
        corresponding raw file that is being concatenated.
    first_samps : list or array of int
        First sample numbers of the raw files concatenated.
    last_samps : list or array of int
        Last sample numbers of the raw files concatenated.

    Returns
    -------
    events : array
        The concatenated events.

    See Also
    --------
    mne.concatenate_raws
    """
    ...

class AcqParserFIF:
    """Parser for Elekta data acquisition settings.

    This class parses parameters (e.g. events and averaging categories) that
    are defined in the Elekta TRIUX/VectorView data acquisition software (DACQ)
    and stored in ``info['acq_pars']``. It can be used to reaverage raw data
    according to DACQ settings and modify original averaging settings if
    necessary.

    Parameters
    ----------

    info : mne.Info
        The :class:`mne.Info` object with information about the sensors and methods of measurement. This is where the DACQ parameters will be taken from.

    Attributes
    ----------
    categories : list
        List of averaging categories marked active in DACQ.
    events : list
        List of events that are in use (referenced by some averaging category).
    reject : dict
        Rejection criteria from DACQ that can be used with mne.Epochs.
        Note that mne does not support all DACQ rejection criteria
        (e.g. spike, slope).
    flat : dict
        Flatness rejection criteria from DACQ that can be used with mne.Epochs.
    acq_dict : dict
        All DACQ parameters.

    See Also
    --------
    mne.io.Raw.acqparser : Access the parser through a Raw attribute.

    Notes
    -----
    Any averaging category (also non-active ones) can be accessed by indexing
    as ``acqparserfif['category_name']``.
    """

    acq_dict: Incomplete
    compat: bool
    stimsource: Incomplete
    reject: Incomplete
    flat: Incomplete

    def __init__(self, info) -> None: ...
    def __getitem__(self, item):
        """Return an averaging category, or list of categories.

        Parameters
        ----------
        item : str | list of str
            Name of the category (comment field in DACQ).

        Returns
        -------
        conds : dict | list of dict
            Each dict should have the following keys:

            comment: str
                The comment field in DACQ.
            state : bool
                Whether the category was marked enabled in DACQ.
            index : int
                The index of the category in DACQ. Indices start from 1.
            event : int
                DACQ index of the reference event (trigger event, zero time for
                the corresponding epochs). Note that the event indices start
                from 1.
            start : float
                Start time of epoch relative to the reference event.
            end : float
                End time of epoch relative to the reference event.
            reqevent : int
                Index of the required (conditional) event.
            reqwhen : int
                Whether the required event is required before (1) or after (2)
                the reference event.
            reqwithin : float
                The time range within which the required event must occur,
                before or after the reference event.
            display : bool
                Whether the category was displayed online in DACQ.
            nave : int
                Desired number of averages. DACQ stops collecting averages once
                this number is reached.
            subave : int
                Whether to compute normal and alternating subaverages, and
                how many epochs to include. See the Elekta data acquisition
                manual for details. Currently the class does not offer any
                facility for computing subaverages, but it can be done manually
                by the user after collecting the epochs.

        """
        ...
    def __len__(self) -> int:
        """Return number of averaging categories marked active in DACQ.

        Returns
        -------
        n_cat : int
            The number of categories.
        """
        ...
    @property
    def categories(self):
        """Return list of averaging categories ordered by DACQ index.

        Only returns categories marked active in DACQ.
        """
        ...
    @property
    def events(self):
        """Return events ordered by DACQ index.

        Only returns events that are in use (referred to by a category).
        """
        ...
    def get_condition(
        self,
        raw,
        condition=None,
        stim_channel=None,
        mask=None,
        uint_cast=None,
        mask_type: str = "and",
        delayed_lookup: bool = True,
    ):
        """Get averaging parameters for a condition (averaging category).

        Output is designed to be used with the Epochs class to extract the
        corresponding epochs.

        Parameters
        ----------
        raw : Raw object
            An instance of Raw.
        condition : None | str | dict | list of dict
            Condition or a list of conditions. Conditions can be strings
            (DACQ comment field, e.g. 'Auditory left') or category dicts
            (e.g. acqp['Auditory left'], where acqp is an instance of
            AcqParserFIF). If None, get all conditions marked active in
            DACQ.
        stim_channel : None | str | list of str
            Name of the stim channel or all the stim channels
            affected by the trigger. If None, the config variables
            'MNE_STIM_CHANNEL', 'MNE_STIM_CHANNEL_1', 'MNE_STIM_CHANNEL_2',
            etc. are read. If these are not found, it will fall back to
            'STI101' or 'STI 014' if present, then fall back to the first
            channel of type 'stim', if present.
        mask : int | None
            The value of the digital mask to apply to the stim channel values.
            If None (default), no masking is performed.
        uint_cast : bool
            If True (default False), do a cast to ``uint16`` on the channel
            data. This can be used to fix a bug with STI101 and STI014 in
            Neuromag acquisition setups that use channel STI016 (channel 16
            turns data into e.g. -32768), similar to ``mne_fix_stim14 --32``
            in MNE-C.
        mask_type : 'and' | 'not_and'
            The type of operation between the mask and the trigger.
            Choose 'and' for MNE-C masking behavior.
        delayed_lookup : bool
            If True, use the 'delayed lookup' procedure implemented in Elekta
            software. When a trigger transition occurs, the lookup of
            the new trigger value will not happen immediately at the following
            sample, but with a 1-sample delay. This allows a slight
            asynchrony between trigger onsets, when they are intended to be
            synchronous. If you have accurate hardware and want to detect
            transitions with a resolution of one sample, use
            delayed_lookup=False.

        Returns
        -------
        conds_data : dict or list of dict
            Each dict has the following keys:

            events : array, shape (n_epochs_out, 3)
                List of zero time points (t0) for the epochs matching the
                condition. Use as the ``events`` parameter to Epochs. Note
                that these are not (necessarily) actual events.
            event_id : dict
                Name of condition and index compatible with ``events``.
                Should be passed as the ``event_id`` parameter to Epochs.
            tmin : float
                Epoch starting time relative to t0. Use as the ``tmin``
                parameter to Epochs.
            tmax : float
                Epoch ending time relative to t0. Use as the ``tmax``
                parameter to Epochs.
        """
        ...

def match_event_names(event_names, keys, *, on_missing: str = "raise"):
    """Search a collection of event names for matching (sub-)groups of events.

    This function is particularly helpful when using grouped event names
    (i.e., event names containing forward slashes ``/``). Please see the
    Examples section below for a working example.

    Parameters
    ----------
    event_names : array-like of str | dict
        Either a collection of event names, or the ``event_id`` dictionary
        mapping event names to event codes.
    keys : array-like of str | str
        One or multiple event names or groups to search for in ``event_names``.
    on_missing : 'raise' | 'warn' | 'ignore'
        How to handle situations when none of the ``keys`` can be found in
        ``event_names``. If ``'warn'`` or ``'ignore'``, an empty list will be
        returned.

    Returns
    -------
    matches : list of str
        All event names that match any of the ``keys`` provided.

    Notes
    -----
    .. versionadded:: 1.0

    Examples
    --------
    Assuming the following grouped event names in the data, you could easily
    query for all ``auditory`` and ``left`` event names::

        >>> event_names = [
        ...     'auditory/left',
        ...     'auditory/right',
        ...     'visual/left',
        ...     'visual/right'
        ... ]
        >>> match_event_names(
        ...     event_names=event_names,
        ...     keys=['auditory', 'left']
        ... )
        ['auditory/left', 'auditory/right', 'visual/left']
    """
    ...

def count_events(events, ids=None):
    """Count events.

    Parameters
    ----------
    events : ndarray, shape (N, 3)
        The events array (consisting of N events).
    ids : array-like of int | None
        If ``None``, count all event types present in the input. If array-like
        of int, count only those event types given by ``ids``.

    Returns
    -------
    counts : dict
        A dictionary containing the event types as keys with their counts as
        values.

    Examples
    --------
        >>> events = np.array([[0, 0, 1], [0, 0, 1], [0, 0, 5]])
        >>> count_events(events)
        {1: 2, 5: 1}
        >>> count_events(events, ids=[1, 5])
        {1: 2, 5: 1}
        >>> count_events(events, ids=[1, 11])
        {1: 2, 11: 0}
    """
    ...
