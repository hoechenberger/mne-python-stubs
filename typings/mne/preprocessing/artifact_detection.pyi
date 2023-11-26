from ..annotations import (
    Annotations as Annotations,
    annotations_from_events as annotations_from_events,
)
from ..filter import filter_data as filter_data
from ..io.base import BaseRaw as BaseRaw
from ..transforms import (
    Transform as Transform,
    apply_trans as apply_trans,
    quat_to_rot as quat_to_rot,
)
from ..utils import logger as logger

def annotate_muscle_zscore(
    raw,
    threshold: int = 4,
    ch_type=None,
    min_length_good: float = 0.1,
    filter_freq=(110, 140),
    n_jobs=None,
    verbose=None,
):
    """### Create annotations for segments that likely contain muscle artifacts.

    Detects data segments containing activity in the frequency range given by
    ``filter_freq`` whose envelope magnitude exceeds the specified z-score
    threshold, when summed across channels and divided by ``sqrt(n_channels)``.
    False-positive transient peaks are prevented by low-pass filtering the
    resulting z-score time series at 4 Hz. Only operates on a single channel
    type, if ``ch_type`` is ``None`` it will select the first type in the list
    ``mag``, ``grad``, ``eeg``.
    See :footcite:`Muthukumaraswamy2013` for background on choosing
    ``filter_freq`` and ``threshold``.

    ### 🛠️ Parameters
    ----------
    raw : instance of Raw
        Data to estimate segments with muscle artifacts.
    threshold : float
        The threshold in z-scores for marking segments as containing muscle
        activity artifacts.
    ch_type : 'mag' | 'grad' | 'eeg' | None
        The type of sensors to use. If ``None`` it will take the first type in
        ``mag``, ``grad``, ``eeg``.
    min_length_good : float | None
        The shortest allowed duration of "good data" (in seconds) between
        adjacent annotations; shorter segments will be incorporated into the
        surrounding annotations.``None`` is equivalent to ``0``.
        Default is ``0.1``.
    filter_freq : array-like, shape (2,)
        The lower and upper frequencies of the band-pass filter.
        Default is ``(110, 140)``.
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

    ### ⏎ Returns
    -------
    annot : mne.Annotations
        Periods with muscle artifacts annotated as BAD_muscle.
    scores_muscle : array
        Z-score values averaged across channels for each sample.

    References
    ----------
    .. footbibliography::
    """
    ...

def annotate_movement(
    raw,
    pos,
    rotation_velocity_limit=None,
    translation_velocity_limit=None,
    mean_distance_limit=None,
    use_dev_head_trans: str = "average",
):
    """### Detect segments with movement.

    Detects segments periods further from rotation_velocity_limit,
    translation_velocity_limit and mean_distance_limit. It returns an
    annotation with the bad segments.

    ### 🛠️ Parameters
    ----------
    raw : instance of Raw
        Data to compute head position.
    pos : array, shape (N, 10)
        The position and quaternion parameters from cHPI fitting. Obtained
        with `mne.chpi` functions.
    rotation_velocity_limit : float
        Head rotation velocity limit in degrees per second.
    translation_velocity_limit : float
        Head translation velocity limit in meters per second.
    mean_distance_limit : float
        Head position limit from mean recording in meters.
    use_dev_head_trans : 'average' (default) | 'info'
        Identify the device to head transform used to define the
        fixed HPI locations for computing moving distances.
        If ``average`` the average device to head transform is
        computed using ``compute_average_dev_head_t``.
        If ``info``, ``raw.info['dev_head_t']`` is used.

    ### ⏎ Returns
    -------
    annot : mne.Annotations
        Periods with head motion.
    hpi_disp : array
        Head position over time with respect to the mean head pos.

    See Also
    --------
    compute_average_dev_head_t
    """
    ...

def compute_average_dev_head_t(raw, pos):
    """### Get new device to head transform based on good segments.

    Segments starting with "BAD" annotations are not included for calculating
    the mean head position.

    ### 🛠️ Parameters
    ----------
    raw : instance of Raw
        Data to compute head position.
    pos : array, shape (N, 10)
        The position and quaternion parameters from cHPI fitting.

    ### ⏎ Returns
    -------
    dev_head_t : instance of Transform
        New ``dev_head_t`` transformation using the averaged good head positions.
    """
    ...

def annotate_break(
    raw,
    events=None,
    min_break_duration: float = 15.0,
    t_start_after_previous: float = 5.0,
    t_stop_before_next: float = 5.0,
    ignore=("bad", "edge"),
    *,
    verbose=None,
):
    """### Create `mne.Annotations` for breaks in an ongoing recording.

    This function first searches for segments in the data that are not
    annotated or do not contain any events and are at least
    ``min_break_duration`` seconds long, and then proceeds to creating
    annotations for those break periods.

    ### 🛠️ Parameters
    ----------
    raw : instance of Raw
        The continuous data to analyze.
    events : None | array, shape (n_events, 3)
        If ``None`` (default), operate based solely on the annotations present
        in ``raw``. If an events array, ignore any annotations in the raw data,
        and operate based on these events only.
    min_break_duration : float
        The minimum time span in seconds between the offset of one and the
        onset of the subsequent annotation (if ``events`` is ``None``) or
        between two consecutive events (if ``events`` is an array) to consider
        this period a "break". Defaults to 15 seconds.

        ### 💡 Note This value defines the minimum duration of a break period in
                  the data, **not** the minimum duration of the generated
                  annotations! See also ``t_start_after_previous`` and
                  ``t_stop_before_next`` for details.

    t_start_after_previous, t_stop_before_next : float
        Specifies how far the to-be-created "break" annotation extends towards
        the two annotations or events spanning the break. This can be used to
        ensure e.g. that the break annotation doesn't start and end immediately
        with a stimulation event. If, for example, your data contains a break
        of 30 seconds between two stimuli, and ``t_start_after_previous`` is
        set to ``5`` and ``t_stop_before_next`` is set to ``3``, the break
        annotation will start 5 seconds after the first stimulus, and end 3
        seconds before the second stimulus, yielding an annotated break of
        ``30 - 5 - 3 = 22`` seconds. Both default to 5 seconds.

        ### 💡 Note The beginning and the end of the recording will be annotated
                  as breaks, too, if the period from recording start until the
                  first annotation or event (or from last annotation or event
                  until recording end) is at least ``min_break_duration``
                  seconds long.

    ignore : iterable of str
        Annotation descriptions starting with these strings will be ignored by
        the break-finding algorithm. The string comparison is case-insensitive,
        i.e., ``('bad',)`` and ``('BAD',)`` are equivalent. By default, all
        annotation descriptions starting with "bad" and annotations
        indicating "edges" (produced by data concatenation) will be
        ignored. Pass an empty list or tuple to take all existing annotations
        into account. If ``events`` is passed, this parameter has no effect.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    break_annotations : instance of Annotations
        The break annotations, each with the description ``'BAD_break'``. If
        no breaks could be found given the provided function parameters, an
        empty `mne.Annotations` object will be returned.

    ### 📖 Notes
    -----
    ✨ Added in vesion 0.24
    """
    ...
