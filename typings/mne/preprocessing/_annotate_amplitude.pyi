from ..annotations import Annotations as Annotations
from ..fixes import jit as jit
from ..io import BaseRaw as BaseRaw
from ..utils import logger as logger

def annotate_amplitude(
    raw,
    peak=None,
    flat=None,
    bad_percent: int = 5,
    min_duration: float = 0.005,
    picks=None,
    *,
    verbose=None,
):
    """Annotate raw data based on peak-to-peak amplitude.

    Creates annotations ``BAD_peak`` or ``BAD_flat`` for spans of data where
    consecutive samples exceed the threshold in ``peak`` or fall below the
    threshold in ``flat`` for more than ``min_duration``.
    Channels where more than ``bad_percent`` of the total recording length
    should be annotated with either ``BAD_peak`` or ``BAD_flat`` are returned
    in ``bads`` instead.
    Note that the annotations and the bads are not automatically added to the
    `mne.io.Raw` object; use `mne.io.Raw.set_annotations` and
    `info['bads'] <mne.Info>` to do so.

    Parameters
    ----------
    raw : instance of Raw
        The raw data.
    peak : float | dict | None
        Annotate segments based on **maximum** peak-to-peak signal amplitude
        (PTP). Valid **keys** can be any channel type present in the object.
        The **values** are floats that set the maximum acceptable PTP. If the
        PTP is larger than this threshold, the segment will be annotated.
        If float, the minimum acceptable PTP is applied to all channels.
    flat : float | dict | None
        Annotate segments based on **minimum** peak-to-peak signal amplitude
        (PTP). Valid **keys** can be any channel type present in the object.
        The **values** are floats that set the minimum acceptable PTP. If the
        PTP is smaller than this threshold, the segment will be annotated.
        If float, the minimum acceptable PTP is applied to all channels.
    bad_percent : float
        The percentage of the time a channel can be above or below thresholds.
        Below this percentage, `mne.Annotations` are created.
        Above this percentage, the channel involved is return in ``bads``. Note
        the returned ``bads`` are not automatically added to
        `info['bads'] <mne.Info>`.
        Defaults to ``5``, i.e. 5%.
    min_duration : float
        The minimum duration (s) required by consecutives samples to be above
        ``peak`` or below ``flat`` thresholds to be considered.
        to consider as above or below threshold.
        For some systems, adjacent time samples with exactly the same value are
        not totally uncommon. Defaults to ``0.005`` (5 ms).
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick good data channels. Note that channels
        in ``info['bads']`` *will be included* if their names or indices are
        explicitly provided.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    annotations : instance of Annotations
        The annotated bad segments.
    bads : list
        The channels detected as bad.

    Notes
    -----
    This function does not use a window to detect small peak-to-peak or large
    peak-to-peak amplitude changes as the ``reject`` and ``flat`` argument from
    `mne.Epochs` does. Instead, it looks at the difference between
    consecutive samples.

    - When used to detect segments below ``flat``, at least ``min_duration``
      seconds of consecutive samples must respect
      ``abs(a[i+1] - a[i]) ≤ flat``.
    - When used to detect segments above ``peak``, at least ``min_duration``
      seconds of consecutive samples must respect
      ``abs(a[i+1] - a[i]) ≥ peak``.

    Thus, this function does not detect every temporal event with large
    peak-to-peak amplitude, but only the ones where the peak-to-peak amplitude
    is supra-threshold between consecutive samples. For instance, segments
    experiencing a DC shift will not be picked up. Only the edges from the DC
    shift will be annotated (and those only if the edge transitions are longer
    than ``min_duration``).

    This function may perform faster if data is loaded in memory, as it
    loads data one channel type at a time (across all time points), which is
    typically not an efficient way to read raw data from disk.

    .. versionadded:: 1.0
    """
    ...
