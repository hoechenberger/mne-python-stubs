from ...utils import fill_doc as fill_doc, logger as logger
from ..base import BaseRaw as BaseRaw

def read_raw_eyelink(
    fname,
    *,
    create_annotations: bool = True,
    apply_offsets: bool = False,
    find_overlaps: bool = False,
    overlap_threshold: float = 0.05,
    verbose=None,
):
    """Reader for an Eyelink ``.asc`` file.

    Parameters
    ----------

    fname : path-like
        Path to the eyelink file (``.asc``).

    create_annotations : bool | list (default True)
        Whether to create `mne.Annotations` from occular events
        (blinks, fixations, saccades) and experiment messages. If a list, must
        contain one or more of ``['fixations', 'saccades',' blinks', messages']``.
        If True, creates `mne.Annotations` for both occular events and
        experiment messages.

    apply_offsets : bool (default False)
        Adjusts the onset time of the `mne.Annotations` created from Eyelink
        experiment messages, if offset values exist in the ASCII file. If False, any
        offset-like values will be prepended to the annotation description.

    find_overlaps : bool (default False)
        Combine left and right eye `mne.Annotations` (blinks, fixations,
        saccades) if their start times and their stop times are both not
        separated by more than overlap_threshold.

    overlap_threshold : float (default 0.05)
        Time in seconds. Threshold of allowable time-gap between both the start and
        stop times of the left and right eyes. If the gap is larger than the threshold,
        the `mne.Annotations` will be kept separate (i.e. ``"blink_L"``,
        ``"blink_R"``). If the gap is smaller than the threshold, the
        `mne.Annotations` will be merged and labeled as ``"blink_both"``.
        Defaults to ``0.05`` seconds (50 ms), meaning that if the blink start times of
        the left and right eyes are separated by less than 50 ms, and the blink stop
        times of the left and right eyes are separated by less than 50 ms, then the
        blink will be merged into a single `mne.Annotations`.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    raw : instance of RawEyelink
        A Raw object containing eyetracker data.

    See Also
    --------
    mne.io.Raw : Documentation of attribute and methods.

    Notes
    -----
    It is common for SR Research Eyelink eye trackers to only record data during trials.
    To avoid frequent data discontinuities and to ensure that the data is continuous
    so that it can be aligned with EEG and MEG data (if applicable), this reader will
    preserve the times between recording trials and annotate them with
    ``'BAD_ACQ_SKIP'``.
    """
    ...

class RawEyelink(BaseRaw):
    """Raw object from an XXX file.

    Parameters
    ----------

    fname : path-like
        Path to the eyelink file (``.asc``).

    create_annotations : bool | list (default True)
        Whether to create `mne.Annotations` from occular events
        (blinks, fixations, saccades) and experiment messages. If a list, must
        contain one or more of ``['fixations', 'saccades',' blinks', messages']``.
        If True, creates `mne.Annotations` for both occular events and
        experiment messages.

    apply_offsets : bool (default False)
        Adjusts the onset time of the `mne.Annotations` created from Eyelink
        experiment messages, if offset values exist in the ASCII file. If False, any
        offset-like values will be prepended to the annotation description.

    find_overlaps : bool (default False)
        Combine left and right eye `mne.Annotations` (blinks, fixations,
        saccades) if their start times and their stop times are both not
        separated by more than overlap_threshold.

    overlap_threshold : float (default 0.05)
        Time in seconds. Threshold of allowable time-gap between both the start and
        stop times of the left and right eyes. If the gap is larger than the threshold,
        the `mne.Annotations` will be kept separate (i.e. ``"blink_L"``,
        ``"blink_R"``). If the gap is smaller than the threshold, the
        `mne.Annotations` will be merged and labeled as ``"blink_both"``.
        Defaults to ``0.05`` seconds (50 ms), meaning that if the blink start times of
        the left and right eyes are separated by less than 50 ms, and the blink stop
        times of the left and right eyes are separated by less than 50 ms, then the
        blink will be merged into a single `mne.Annotations`.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    mne.io.Raw : Documentation of attribute and methods.
    """

    def __init__(
        self,
        fname,
        *,
        create_annotations: bool = True,
        apply_offsets: bool = False,
        find_overlaps: bool = False,
        overlap_threshold: float = 0.05,
        verbose=None,
    ) -> None: ...
