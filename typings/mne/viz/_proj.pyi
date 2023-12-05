from ..defaults import DEFAULTS as DEFAULTS
from ..utils import warn as warn
from .utils import plt_show as plt_show

def plot_projs_joint(
    projs,
    evoked,
    picks_trace=None,
    *,
    topomap_kwargs=None,
    show: bool = True,
    verbose=None,
):
    """Plot projectors and evoked jointly.

    Parameters
    ----------
    projs : list of Projection
        The projectors to plot.
    evoked : instance of Evoked
        The data to plot. Typically this is the evoked instance created from
        averaging the epochs used to create the projection.
    picks_trace : str | array-like | slice | None
        Channels to show alongside the projected time courses. Typically
        these are the ground-truth channels for an artifact (e.g., ``'eog'`` or
        ``'ecg'``). Slices and lists of integers will be interpreted as channel indices. In lists, channel *type* strings (e.g., ``['meg', 'eeg']``) will
        pick channels of those types, channel *name* strings (e.g., ``['MEG0111', 'MEG2623']``
        will pick the given channels.
        Can also be the string values "all" to pick
        all channels, or "data" to pick :term:`data channels`.
        None (default) will pick no channels.
    topomap_kwargs : dict | None
        Keyword arguments to pass to `mne.viz.plot_projs_topomap`.
    show : bool
        Show the figure if ``True``.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    fig : instance of matplotlib Figure
        The figure.

    Notes
    -----
    This function creates a figure with three columns:

    1. The left shows the evoked data traces before (black) and after (green)
       projection.
    2. The center shows the topomaps associated with each of the projectors.
    3. The right again shows the data traces (black), but this time with:

       1. The data projected onto each projector with a single normalization
          factor (solid lines). This is useful for seeing the relative power
          in each projection vector.
       2. The data projected onto each projector with individual normalization
          factors (dashed lines). This is useful for visualizing each time
          course regardless of its power.
       3. Additional data traces from ``picks_trace`` (solid yellow lines).
          This is useful for visualizing the "ground truth" of the time
          course, e.g. the measured EOG or ECG channel time courses.

    ✨ Added in version 1.1
    """
    ...
