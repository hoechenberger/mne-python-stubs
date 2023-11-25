from ..parallel import parallel_func as parallel_func
from ..utils import logger as logger, warn as warn

def dpss_windows(
    N, half_nbw, Kmax, *, sym: bool = True, norm=None, low_bias: bool = True
):
    """Compute Discrete Prolate Spheroidal Sequences.

    Will give of orders [0,Kmax-1] for a given frequency-spacing multiple
    NW and sequence length N.

    .. note:: Copied from NiTime.

    Parameters
    ----------
    N : int
        Sequence length.
    half_nbw : float
        Standardized half bandwidth corresponding to 2 * half_bw = BW*f0
        = BW*N/dt but with dt taken as 1.
    Kmax : int
        Number of DPSS windows to return is Kmax (orders 0 through Kmax-1).
    sym : bool
        Whether to generate a symmetric window (``True``, for filter design) or
        a periodic window (``False``, for spectral analysis). Default is
        ``True``.

        .. versionadded:: 1.3
    norm : 2 | ``'approximate'`` | ``'subsample'`` | None
        Window normalization method. If ``'approximate'`` or ``'subsample'``,
        windows are normalized by the maximum, and a correction scale-factor
        for even-length windows is applied either using
        ``N**2/(N**2+half_nbw)`` ("approximate") or a FFT-based subsample shift
        ("subsample"). ``2`` uses the L2 norm. ``None`` (the default) uses
        ``"approximate"`` when ``Kmax=None`` and ``2`` otherwise.

        .. versionadded:: 1.3
    low_bias : bool
        Keep only tapers with eigenvalues > 0.9.

    Returns
    -------
    v, e : tuple,
        The v array contains DPSS windows shaped (Kmax, N).
        e are the eigenvalues.

    Notes
    -----
    Tridiagonal form of DPSS calculation from :footcite:`Slepian1978`.

    References
    ----------
    .. footbibliography::
    """

def psd_array_multitaper(
    x,
    sfreq,
    fmin: float = 0.0,
    fmax=...,
    bandwidth=None,
    adaptive: bool = False,
    low_bias: bool = True,
    normalization: str = "length",
    remove_dc: bool = True,
    output: str = "power",
    n_jobs=None,
    *,
    max_iter: int = 150,
    verbose=None,
):
    """Compute power spectral density (PSD) using a multi-taper method.

    The power spectral density is computed with DPSS
    tapers :footcite:p:`Slepian1978`.

    Parameters
    ----------
    x : array, shape=(..., n_times)
        The data to compute PSD from.
    sfreq : float
        The sampling frequency.
    fmin, fmax : float
        The lower- and upper-bound on frequencies of interest. Default is ``fmin=0, fmax=np.inf`` (spans all frequencies present in the data).
    bandwidth : float
        Frequency bandwidth of the multi-taper window function in Hz. For a
        given frequency, frequencies at ``± bandwidth / 2`` are smoothed
        together. The default value is a bandwidth of
        ``8 * (sfreq / n_times)``.
    adaptive : bool
        Use adaptive weights to combine the tapered spectra into PSD
        (slow, use n_jobs >> 1 to speed up computation).
    low_bias : bool
        Only use tapers with more than 90% spectral concentration within
        bandwidth.
    normalization : 'full' | 'length'
        Normalization strategy. If "full", the PSD will be normalized by the
        sampling rate as well as the length of the signal (as in
        :ref:`Nitime <nitime:users-guide>`). Default is ``'length'``.

    remove_dc : bool
        If ``True``, the mean is subtracted from each segment before computing
        its spectrum.
    output : str
        The format of the returned ``psds`` array, ``'complex'`` or
        ``'power'``:

        * ``'power'`` : the power spectral density is returned.
        * ``'complex'`` : the complex fourier coefficients are returned per
          taper.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the :mod:`joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a :class:`joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.

    max_iter : int
        Maximum number of iterations to reach convergence when combining the
        tapered spectra with adaptive weights (see argument ``adaptive``). This
        argument has not effect if ``adaptive`` is set to ``False``.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    psds : ndarray, shape (..., n_freqs) or (..., n_tapers, n_freqs)
        The power spectral densities. All dimensions up to the last (or the
        last two if ``output='complex'``) will be the same as input.
    freqs : array
        The frequency points in Hz of the PSD.
    weights : ndarray
        The weights used for averaging across tapers. Only returned if
        ``output='complex'``.

    See Also
    --------
    csd_multitaper
    mne.io.Raw.compute_psd
    mne.Epochs.compute_psd
    mne.Evoked.compute_psd

    Notes
    -----
    .. versionadded:: 0.14.0

    References
    ----------
    .. footbibliography::
    """

def tfr_array_multitaper(
    epoch_data,
    sfreq,
    freqs,
    n_cycles: float = 7.0,
    zero_mean: bool = True,
    time_bandwidth: float = 4.0,
    use_fft: bool = True,
    decim: int = 1,
    output: str = "complex",
    n_jobs=None,
    *,
    verbose=None,
):
    """Compute Time-Frequency Representation (TFR) using DPSS tapers.

    Same computation as mne.time_frequency.tfr_multitaper`, but operates on
    :class:`NumPy arrays <numpy.ndarray>` instead of mne.Epochs` or
    mne.Evoked` objects.

    Parameters
    ----------
    epoch_data : array of shape (n_epochs, n_channels, n_times)
        The epochs.
    sfreq : float
        Sampling frequency of the data in Hz.

    freqs : array of float, shape (n_freqs,)
        The frequencies of interest in Hz.

    n_cycles : int | array of int, shape (n_freqs,)
        Number of cycles in the wavelet, either a fixed number or one per
        frequency. The number of cycles ``n_cycles`` and the frequencies of
        interest ``freqs`` define the temporal window length. See notes for
        additional information about the relationship between those arguments
        and about time and frequency smoothing.
    zero_mean : bool
        If True, make sure the wavelets have a mean of zero. Defaults to True.

    time_bandwidth : float ``≥ 2.0``
        Product between the temporal window length (in seconds) and the *full*
        frequency bandwidth (in Hz). This product can be seen as the surface of the
        window on the time/frequency plane and controls the frequency bandwidth
        (thus the frequency resolution) and the number of good tapers. See notes
        for additional information.
    use_fft : bool
        Use the FFT for convolutions or not. Defaults to True.

    decim : int | slice, default 1
        To reduce memory usage, decimation factor after time-frequency
        decomposition.

        - if `int`, returns ``tfr[..., ::decim]``.
        - if `slice`, returns ``tfr[..., decim]``.

        .. note::
            Decimation is done after convolutions and may create aliasing
            artifacts.
    output : str, default 'complex'

        * ``'complex'`` : single trial per taper complex values.
        * ``'power'`` : single trial power.
        * ``'phase'`` : single trial per taper phase.
        * ``'avg_power'`` : average of single trial power.
        * ``'itc'`` : inter-trial coherence.
        * ``'avg_power_itc'`` : average of single trial power and inter-trial
          coherence across trials.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the :mod:`joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a :class:`joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    out : array
        Time frequency transform of ``epoch_data``.

        - if ``output in ('complex',' 'phase')``, array of shape
          ``(n_epochs, n_chans, n_tapers, n_freqs, n_times)``
        - if ``output`` is ``'power'``, array of shape ``(n_epochs, n_chans,
          n_freqs, n_times)``
        - else, array of shape ``(n_chans, n_freqs, n_times)``

        If ``output`` is ``'avg_power_itc'``, the real values in ``out``
        contain the average power and the imaginary values contain the
        inter-trial coherence: :math:`out = power_{avg} + i * ITC`.

    See Also
    --------
    mne.time_frequency.tfr_multitaper
    mne.time_frequency.tfr_morlet
    mne.time_frequency.tfr_array_morlet
    mne.time_frequency.tfr_stockwell
    mne.time_frequency.tfr_array_stockwell

    Notes
    -----

    In spectrotemporal analysis (as with traditional fourier methods),
    the temporal and spectral resolution are interrelated: longer temporal windows
    allow more precise frequency estimates; shorter temporal windows "smear"
    frequency estimates while providing more precise timing information.

    Time-frequency representations are computed using a sliding temporal window.
    Either the temporal window has a fixed length independent of frequency, or the
    temporal window decreases in length with increased frequency.

    .. image:: https://www.fieldtriptoolbox.org/assets/img/tutorial/timefrequencyanalysis/figure1.png

    *Figure: Time and frequency smoothing. (a) For a fixed length temporal window
    the time and frequency smoothing remains fixed. (b) For temporal windows that
    decrease with frequency, the temporal smoothing decreases and the frequency
    smoothing increases with frequency.*
    Source: `FieldTrip tutorial: Time-frequency analysis using Hanning window,
    multitapers and wavelets <https://www.fieldtriptoolbox.org/tutorial/timefrequencyanalysis>`_.

    In MNE-Python, the multitaper temporal window length is defined by the arguments
    ``freqs`` and ``n_cycles``, respectively defining the frequencies of interest
    and the number of cycles: :math:`T = \\frac{\\mathtt{n\\_cycles}}{\\mathtt{freqs}}`

    A fixed number of cycles for all frequencies will yield a temporal window which
    decreases with frequency. For example, ``freqs=np.arange(1, 6, 2)`` and
    ``n_cycles=2`` yields ``T=array([2., 0.7, 0.4])``.

    To use a temporal window with fixed length, the number of cycles has to be
    defined based on the frequency. For example, ``freqs=np.arange(1, 6, 2)`` and
    ``n_cycles=freqs / 2`` yields ``T=array([0.5, 0.5, 0.5])``.

    In MNE-Python's multitaper functions, the frequency bandwidth is
    additionally affected by the parameter ``time_bandwidth``.
    The ``n_cycles`` parameter determines the temporal window length based on the
    frequencies of interest: :math:`T = \\frac{\\mathtt{n\\_cycles}}{\\mathtt{freqs}}`.
    The ``time_bandwidth`` parameter defines the "time-bandwidth product", which is
    the product of the temporal window length (in seconds) and the frequency
    bandwidth (in Hz). Thus once ``n_cycles`` has been set, frequency bandwidth is
    determined by :math:`\\frac{\\mathrm{time~bandwidth}}{\\mathrm{time~window}}`, and
    thus passing a larger ``time_bandwidth`` value will increase the frequency
    bandwidth (thereby decreasing the frequency *resolution*).

    The increased frequency bandwidth is reached by averaging spectral estimates
    obtained from multiple tapers. Thus, ``time_bandwidth`` also determines the
    number of tapers used. MNE-Python uses only "good" tapers (tapers with minimal
    leakage from far-away frequencies); the number of good tapers is
    ``floor(time_bandwidth - 1)``. This means there is another trade-off at play,
    between frequency resolution and the variance reduction that multitaper
    analysis provides. Striving for finer frequency resolution (by setting
    ``time_bandwidth`` low) means fewer tapers will be used, which undermines what
    is unique about multitaper methods — namely their ability to improve accuracy /
    reduce noise in the power estimates by using several (orthogonal) tapers.

    .. warning::

        In mne.time_frequency.tfr_array_multitaper` and
        mne.time_frequency.tfr_multitaper`, ``time_bandwidth`` defines the
        product of the temporal window length with the *full* frequency bandwidth
        For example, a full bandwidth of 4 Hz at a frequency of interest of 10 Hz
        will "smear" the frequency estimate between 8 Hz and 12 Hz.

        This is not the case for mne.time_frequency.psd_array_multitaper` where
        the argument ``bandwidth`` defines the *half* frequency bandwidth. In the
        example above, the half-frequency bandwidth is 2 Hz.

    .. versionadded:: 0.14.0
    """
