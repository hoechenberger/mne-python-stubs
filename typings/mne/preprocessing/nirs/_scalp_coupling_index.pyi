from ...io import BaseRaw as BaseRaw

def scalp_coupling_index(
    raw,
    l_freq: float = 0.7,
    h_freq: float = 1.5,
    l_trans_bandwidth: float = 0.3,
    h_trans_bandwidth: float = 0.3,
    verbose: bool = False,
):
    """Calculate scalp coupling index.

    This function calculates the scalp coupling index
    :footcite:`pollonini2014auditory`. This is a measure of the quality of the
    connection between the optode and the scalp.

    Parameters
    ----------
    raw : instance of Raw
        The raw data.

    l_freq : float | None
        For FIR filters, the lower pass-band edge; for IIR filters, the lower
        cutoff frequency. If None the data are only low-passed.

    h_freq : float | None
        For FIR filters, the upper pass-band edge; for IIR filters, the upper
        cutoff frequency. If None the data are only high-passed.

    l_trans_bandwidth : float | str
        Width of the transition band at the low cut-off frequency in Hz
        (high pass or cutoff 1 in bandpass). Can be "auto"
        (default) to use a multiple of ``l_freq``::

            min(max(l_freq * 0.25, 2), l_freq)

        Only used for ``method='fir'``.

    h_trans_bandwidth : float | str
        Width of the transition band at the high cut-off frequency in Hz
        (low pass or cutoff 2 in bandpass). Can be "auto"
        (default in 0.14) to use a multiple of ``h_freq``::

            min(max(h_freq * 0.25, 2.), info['sfreq'] / 2. - h_freq)

        Only used for ``method='fir'``.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    sci : array of float
        Array containing scalp coupling index for each channel.

    References
    ----------
    .. footbibliography::
    """
