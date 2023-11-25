from ..utils import logger as logger

def oversampled_temporal_projection(
    raw, duration: float = 10.0, picks=None, verbose=None
):
    """Denoise MEG channels using leave-one-out temporal projection.

    Parameters
    ----------
    raw : instance of Raw
        Raw data to denoise.
    duration : float | str
        The window duration (in seconds; default 10.) to use. Can also
        be "min" to use as short a window as possible.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick all data channels. Note that channels
        in ``info['bads']`` *will be included* if their names or indices are
        explicitly provided.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    raw_clean : instance of Raw
        The cleaned data.

    Notes
    -----
    This algorithm is computationally expensive, and can be several times
    slower than realtime for conventional M/EEG datasets. It uses a
    leave-one-out procedure with parallel temporal projection to remove
    individual sensor noise under the assumption that sampled fields
    (e.g., MEG and EEG) are oversampled by the sensor array
    :footcite:`LarsonTaulu2018`.

    OTP can improve sensor noise levels (especially under visual
    inspection) and repair some bad channels. This noise reduction is known
    to interact with :func:`tSSS <mne.preprocessing.maxwell_filter>` such
    that increasing the ``st_correlation`` value will likely be necessary.

    Channels marked as bad will not be used to reconstruct good channels,
    but good channels will be used to process the bad channels. Depending
    on the type of noise present in the bad channels, this might make
    them usable again.

    Use of this algorithm is covered by a provisional patent.

    .. versionadded:: 0.16

    References
    ----------
    .. footbibliography::
    """
