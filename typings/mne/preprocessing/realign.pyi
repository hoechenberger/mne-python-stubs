from ..io import BaseRaw as BaseRaw
from ..utils import logger as logger, warn as warn

def realign_raw(raw, other, t_raw, t_other, verbose=None) -> None:
    """Realign two simultaneous recordings.

    Due to clock drift, recordings at a given same sample rate made by two
    separate devices simultaneously can become out of sync over time. This
    function uses event times captured by both acquisition devices to resample
    ``other`` to match ``raw``.

    Parameters
    ----------
    raw : instance of Raw
        The first raw instance.
    other : instance of Raw
        The second raw instance. It will be resampled to match ``raw``.
    t_raw : array-like, shape (n_events,)
        The times of shared events in ``raw`` relative to ``raw.times[0]`` (0).
        Typically these could be events on some TTL channel such as::

            find_events(raw)[:, 0] / raw.info["sfreq"] - raw.first_time
    t_other : array-like, shape (n_events,)
        The times of shared events in ``other`` relative to ``other.times[0]``.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Notes
    -----
    This function operates inplace. It will:

    1. Estimate the zero-order (start offset) and first-order (clock drift)
       correction.
    2. Crop the start of ``raw`` or ``other``, depending on which started
       recording first.
    3. Resample ``other`` to match ``raw`` based on the clock drift.
    4. Realign the onsets and durations in ``other.annotations``.
    5. Crop the end of ``raw`` or ``other``, depending on which stopped
       recording first (and the clock drift rate).

    This function is primarily designed to work on recordings made at the same
    sample rate, but it can also operate on recordings made at different
    sample rates to resample and deal with clock drift simultaneously.

    .. versionadded:: 0.22
    """
