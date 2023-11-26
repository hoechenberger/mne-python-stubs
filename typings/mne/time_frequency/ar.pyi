from .._fiff.pick import pick_info as pick_info

def fit_iir_model_raw(
    raw, order: int = 2, picks=None, tmin=None, tmax=None, verbose=None
):
    """Fit an AR model to raw data and creates the corresponding IIR filter.

    The computed filter is fitted to data from all of the picked channels,
    with frequency response given by the standard IIR formula:

    .. math::

        H(e^{jw}) = \\frac{1}{a[0] + a[1]e^{-jw} + ... + a[n]e^{-jnw}}

    Parameters
    ----------
    raw : Raw object
        An instance of Raw.
    order : int
        Order of the FIR filter.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick good data channels. Note that channels
        in ``info['bads']`` *will be included* if their names or indices are
        explicitly provided.
    tmin : float
        The beginning of time interval in seconds.
    tmax : float
        The end of time interval in seconds.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    b : ndarray
        Numerator filter coefficients.
    a : ndarray
        Denominator filter coefficients.
    """
    ...
