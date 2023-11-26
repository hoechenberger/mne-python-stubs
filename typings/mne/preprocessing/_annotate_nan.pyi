from ..annotations import Annotations as Annotations

def annotate_nan(raw, *, verbose=None):
    """Detect segments with NaN and return a new Annotations instance.

    Parameters
    ----------
    raw : instance of Raw
        Data to find segments with NaN values.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    annot : instance of Annotations
        New channel-specific annotations for the data.
    """
    ...
