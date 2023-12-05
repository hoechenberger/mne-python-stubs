from ..evoked import Evoked as Evoked

def cortical_signal_suppression(
    evoked,
    picks=None,
    mag_picks=None,
    grad_picks=None,
    n_proj: int = 6,
    *,
    verbose=None,
):
    """Apply cortical signal suppression (CSS) to evoked data.

    Parameters
    ----------
    evoked : instance of Evoked
        The evoked object to use for CSS. Must contain magnetometer,
        gradiometer, and EEG channels.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick good data channels. Note that channels
        in ``info['bads']`` *will be included* if their names or indices are
        explicitly provided.
    mag_picks : array-like of int
        Array of the magnetometer channel indices that will be used to find
        the reference data. If None (default), all magnetometers will
        be used.
    grad_picks : array-like of int
        Array of the gradiometer channel indices that will be used to find
        the reference data. If None (default), all gradiometers will
        be used.
    n_proj : int
        The number of projection vectors.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    evoked_subcortical : instance of Evoked
        The evoked object with cortical contributions to the EEG data
        suppressed.

    Notes
    -----
    This method removes the common signal subspace between the magnetometer
    data and the gradiometer data from the EEG data. This is done by a temporal
    projection using ``n_proj`` number of projection vectors. For reference,
    see :footcite:`Samuelsson2019`.

    References
    ----------
    .. footbibliography::
    """
    ...
