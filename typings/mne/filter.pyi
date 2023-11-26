from .parallel import parallel_func as parallel_func
from .utils import logger as logger, sum_squared as sum_squared, warn as warn

def is_power2(num):
    """### Test if number is a power of 2.

    ### 🛠️ Parameters
    ----------
    num : int
        Number.

    ### ⏎ Returns
    -------
    b : bool
        True if is power of 2.

    Examples
    --------
    >>> is_power2(2 ** 3)
    True
    >>> is_power2(5)
    False
    """
    ...

def next_fast_len(target):
    """### Find the next fast size of input data to `fft`, for zero-padding, etc.

    SciPy's FFTPACK has efficient functions for radix {2, 3, 4, 5}, so this
    returns the next composite of the prime factors 2, 3, and 5 which is
    greater than or equal to `target`. (These are also known as 5-smooth
    numbers, regular numbers, or Hamming numbers.)

    ### 🛠️ Parameters
    ----------
    target : int
        Length to start searching from.  Must be a positive integer.

    ### ⏎ Returns
    -------
    out : int
        The first 5-smooth number greater than or equal to `target`.

    ### 📖 Notes
    -----
    Copied from SciPy with minor modifications.
    """
    ...

def estimate_ringing_samples(system, max_try: int = 100000):
    """### Estimate filter ringing.

    ### 🛠️ Parameters
    ----------
    system : tuple | ndarray
        A tuple of (b, a) or ndarray of second-order sections coefficients.
    max_try : int
        Approximate maximum number of samples to try.
        This will be changed to a multiple of 1000.

    ### ⏎ Returns
    -------
    n : int
        The approximate ringing.
    """
    ...

def construct_iir_filter(
    iir_params,
    f_pass=None,
    f_stop=None,
    sfreq=None,
    btype=None,
    return_copy: bool = True,
    *,
    phase: str = "zero",
    verbose=None,
):
    """### Use IIR parameters to get filtering coefficients.

    This function works like a wrapper for iirdesign and iirfilter in
    scipy.signal to make filter coefficients for IIR filtering. It also
    estimates the number of padding samples based on the filter ringing.
    It creates a new iir_params dict (or updates the one passed to the
    function) with the filter coefficients ('b' and 'a') and an estimate
    of the padding necessary ('padlen') so IIR filtering can be performed.

    ### 🛠️ Parameters
    ----------
    iir_params : dict
        Dictionary of parameters to use for IIR filtering.

            * If ``iir_params['sos']`` exists, it will be used as
              second-order sections to perform IIR filtering.

              ✨ Added in vesion 0.13

            * Otherwise, if ``iir_params['b']`` and ``iir_params['a']``
              exist, these will be used as coefficients to perform IIR
              filtering.
            * Otherwise, if ``iir_params['order']`` and
              ``iir_params['ftype']`` exist, these will be used with
              `scipy.signal.iirfilter` to make a filter.
              You should also supply ``iir_params['rs']`` and
              ``iir_params['rp']`` if using elliptic or Chebychev filters.
            * Otherwise, if ``iir_params['gpass']`` and
              ``iir_params['gstop']`` exist, these will be used with
              `scipy.signal.iirdesign` to design a filter.
            * ``iir_params['padlen']`` defines the number of samples to pad
              (and an estimate will be calculated if it is not given).
              See Notes for more details.
            * ``iir_params['output']`` defines the system output kind when
              designing filters, either "sos" or "ba". For 0.13 the
              default is 'ba' but will change to 'sos' in 0.14.

    f_pass : float or list of float
        Frequency for the pass-band. Low-pass and high-pass filters should
        be a float, band-pass should be a 2-element list of float.
    f_stop : float or list of float
        Stop-band frequency (same size as f_pass). Not used if 'order' is
        specified in iir_params.
    sfreq : float | None
        The sample rate.
    btype : str
        Type of filter. Should be 'lowpass', 'highpass', or 'bandpass'
        (or analogous string representations known to
        `scipy.signal.iirfilter`).
    return_copy : bool
        If False, the 'sos', 'b', 'a', and 'padlen' entries in
        ``iir_params`` will be set inplace (if they weren't already).
        Otherwise, a new ``iir_params`` instance will be created and
        returned with these entries.

    phase : str
        Phase of the filter.
        When ``method='fir'``, symmetric linear-phase FIR filters are constructed,
        and if ``phase='zero'`` (default), the delay of this filter is compensated
        for, making it non-causal. If ``phase='zero-double'``,
        then this filter is applied twice, once forward, and once backward
        (also making it non-causal). If ``'minimum'``, then a minimum-phase filter
        will be constructed and applied, which is causal but has weaker stop-band
        suppression.
        When ``method='iir'``, ``phase='zero'`` (default) or
        ``phase='zero-double'`` constructs and applies IIR filter twice, once
        forward, and once backward (making it non-causal) using
        `scipy.signal.filtfilt`.
        If ``phase='forward'``, it constructs and applies forward IIR filter using
        `scipy.signal.lfilter`.

        ✨ Added in vesion 0.13

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    iir_params : dict
        Updated iir_params dict, with the entries (set only if they didn't
        exist before) for 'sos' (or 'b', 'a'), and 'padlen' for
        IIR filtering.

    ### 👉 See Also
    --------
    mne.filter.filter_data
    mne.io.Raw.filter

    ### 📖 Notes
    -----
    This function triages calls to `scipy.signal.iirfilter` and
    `scipy.signal.iirdesign` based on the input arguments (see
    linked functions for more details).

    🎭 Changed in version 0.14
       Second-order sections are used in filter design by default (replacing
       ``output='ba'`` by ``output='sos'``) to help ensure filter stability
       and reduce numerical error.

    Examples
    --------
    iir_params can have several forms. Consider constructing a low-pass
    filter at 40 Hz with 1000 Hz sampling rate.

    In the most basic (2-parameter) form of iir_params, the order of the
    filter 'N' and the type of filtering 'ftype' are specified. To get
    coefficients for a 4th-order Butterworth filter, this would be:

    >>> iir_params = dict(order=4, ftype='butter', output='sos')  # doctest:+SKIP
    >>> iir_params = construct_iir_filter(iir_params, 40, None, 1000, 'low', return_copy=False)  # doctest:+SKIP
    >>> print((2 * len(iir_params['sos']), iir_params['padlen']))  # doctest:+SKIP
    (4, 82)

    Filters can also be constructed using filter design methods. To get a
    40 Hz Chebyshev type 1 lowpass with specific gain characteristics in the
    pass and stop bands (assuming the desired stop band is at 45 Hz), this
    would be a filter with much longer ringing:

    >>> iir_params = dict(ftype='cheby1', gpass=3, gstop=20, output='sos')  # doctest:+SKIP
    >>> iir_params = construct_iir_filter(iir_params, 40, 50, 1000, 'low')  # doctest:+SKIP
    >>> print((2 * len(iir_params['sos']), iir_params['padlen']))  # doctest:+SKIP
    (6, 439)

    Padding and/or filter coefficients can also be manually specified. For
    a 10-sample moving window with no padding during filtering, for example,
    one can just do:

    >>> iir_params = dict(b=np.ones((10)), a=[1, 0], padlen=0)  # doctest:+SKIP
    >>> iir_params = construct_iir_filter(iir_params, return_copy=False)  # doctest:+SKIP
    >>> print((iir_params['b'], iir_params['a'], iir_params['padlen']))  # doctest:+SKIP
    (array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]), [1, 0], 0)

    For more information, see the tutorials
    `disc-filtering` and `tut-filter-resample`.
    """
    ...

def filter_data(
    data,
    sfreq,
    l_freq,
    h_freq,
    picks=None,
    filter_length: str = "auto",
    l_trans_bandwidth: str = "auto",
    h_trans_bandwidth: str = "auto",
    n_jobs=None,
    method: str = "fir",
    iir_params=None,
    copy: bool = True,
    phase: str = "zero",
    fir_window: str = "hamming",
    fir_design: str = "firwin",
    pad: str = "reflect_limited",
    *,
    verbose=None,
):
    """### Filter a subset of channels.

    ### 🛠️ Parameters
    ----------
    data : ndarray, shape (..., n_times)
        The data to filter.
    sfreq : float
        The sample frequency in Hz.

    l_freq : float | None
        For FIR filters, the lower pass-band edge; for IIR filters, the lower
        cutoff frequency. If None the data are only low-passed.

    h_freq : float | None
        For FIR filters, the upper pass-band edge; for IIR filters, the upper
        cutoff frequency. If None the data are only high-passed.
    picks : list | slice | None
        Channels to include. Slices and lists of integers will be interpreted as channel indices.
        None (default) will pick all channels. Note that channels in ``info['bads']`` *will be included* if their indices are explicitly provided.
        Currently this is only supported for 2D (n_channels, n_times) and
        3D (n_epochs, n_channels, n_times) arrays.

    filter_length : str | int
        Length of the FIR filter to use (if applicable):

        * **'auto' (default)**: The filter length is chosen based
          on the size of the transition regions (6.6 times the reciprocal
          of the shortest transition band for fir_window='hamming'
          and fir_design="firwin2", and half that for "firwin").
        * **str**: A human-readable time in
          units of "s" or "ms" (e.g., "10s" or "5500ms") will be
          converted to that number of samples if ``phase="zero"``, or
          the shortest power-of-two length at least that duration for
          ``phase="zero-double"``.
        * **int**: Specified length in samples. For fir_design="firwin",
          this should not be used.

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

    n_jobs : int | str
        Number of jobs to run in parallel. Can be ``'cuda'`` if ``cupy``
        is installed properly and ``method='fir'``.

    method : str
        ``'fir'`` will use overlap-add FIR filtering, ``'iir'`` will use IIR
        forward-backward filtering (via `scipy.signal.filtfilt`).

    iir_params : dict | None
        Dictionary of parameters to use for IIR filtering.
        If ``iir_params=None`` and ``method="iir"``, 4th order Butterworth will be used.
        For more information, see `mne.filter.construct_iir_filter`.
    copy : bool
        If True, a copy of x, filtered, is returned. Otherwise, it operates
        on x in place.

    phase : str
        Phase of the filter.
        When ``method='fir'``, symmetric linear-phase FIR filters are constructed,
        and if ``phase='zero'`` (default), the delay of this filter is compensated
        for, making it non-causal. If ``phase='zero-double'``,
        then this filter is applied twice, once forward, and once backward
        (also making it non-causal). If ``'minimum'``, then a minimum-phase filter
        will be constructed and applied, which is causal but has weaker stop-band
        suppression.
        When ``method='iir'``, ``phase='zero'`` (default) or
        ``phase='zero-double'`` constructs and applies IIR filter twice, once
        forward, and once backward (making it non-causal) using
        `scipy.signal.filtfilt`.
        If ``phase='forward'``, it constructs and applies forward IIR filter using
        `scipy.signal.lfilter`.

        ✨ Added in vesion 0.13

    fir_window : str
        The window to use in FIR design, can be "hamming" (default),
        "hann" (default in 0.13), or "blackman".

        ✨ Added in vesion 0.15

    fir_design : str
        Can be "firwin" (default) to use `scipy.signal.firwin`,
        or "firwin2" to use `scipy.signal.firwin2`. "firwin" uses
        a time-domain design technique that generally gives improved
        attenuation using fewer samples than "firwin2".

        ✨ Added in vesion 0.15

    pad : str
        The type of padding to use. Supports all `numpy.pad` ``mode``
        options. Can also be ``"reflect_limited"``, which pads with a
        reflected version of each vector mirrored on the first and last values
        of the vector, followed by zeros.

        Only used for ``method='fir'``.
        The default is ``'reflect_limited'``.

        ✨ Added in vesion 0.15

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    data : ndarray, shape (..., n_times)
        The filtered data.

    ### 👉 See Also
    --------
    construct_iir_filter
    create_filter
    mne.io.Raw.filter
    notch_filter
    resample

    ### 📖 Notes
    -----
    Applies a zero-phase low-pass, high-pass, band-pass, or band-stop
    filter to the channels selected by ``picks``.

    ``l_freq`` and ``h_freq`` are the frequencies below which and above
    which, respectively, to filter out of the data. Thus the uses are:

        * ``l_freq < h_freq``: band-pass filter
        * ``l_freq > h_freq``: band-stop filter
        * ``l_freq is not None and h_freq is None``: high-pass filter
        * ``l_freq is None and h_freq is not None``: low-pass filter

    ### 💡 Note If n_jobs > 1, more memory is required as
              ``len(picks) * n_times`` additional time points need to
              be temporarily stored in memory.

    For more information, see the tutorials
    `disc-filtering` and `tut-filter-resample` and
    `mne.filter.create_filter`.
    """
    ...

def create_filter(
    data,
    sfreq,
    l_freq,
    h_freq,
    filter_length: str = "auto",
    l_trans_bandwidth: str = "auto",
    h_trans_bandwidth: str = "auto",
    method: str = "fir",
    iir_params=None,
    phase: str = "zero",
    fir_window: str = "hamming",
    fir_design: str = "firwin",
    verbose=None,
):
    """### Create a FIR or IIR filter.

    ``l_freq`` and ``h_freq`` are the frequencies below which and above
    which, respectively, to filter out of the data. Thus the uses are:

        * ``l_freq < h_freq``: band-pass filter
        * ``l_freq > h_freq``: band-stop filter
        * ``l_freq is not None and h_freq is None``: high-pass filter
        * ``l_freq is None and h_freq is not None``: low-pass filter

    ### 🛠️ Parameters
    ----------
    data : ndarray, shape (..., n_times) | None
        The data that will be filtered. This is used for sanity checking
        only. If None, no sanity checking related to the length of the signal
        relative to the filter order will be performed.
    sfreq : float
        The sample frequency in Hz.

    l_freq : float | None
        For FIR filters, the lower pass-band edge; for IIR filters, the lower
        cutoff frequency. If None the data are only low-passed.

    h_freq : float | None
        For FIR filters, the upper pass-band edge; for IIR filters, the upper
        cutoff frequency. If None the data are only high-passed.

    filter_length : str | int
        Length of the FIR filter to use (if applicable):

        * **'auto' (default)**: The filter length is chosen based
          on the size of the transition regions (6.6 times the reciprocal
          of the shortest transition band for fir_window='hamming'
          and fir_design="firwin2", and half that for "firwin").
        * **str**: A human-readable time in
          units of "s" or "ms" (e.g., "10s" or "5500ms") will be
          converted to that number of samples if ``phase="zero"``, or
          the shortest power-of-two length at least that duration for
          ``phase="zero-double"``.
        * **int**: Specified length in samples. For fir_design="firwin",
          this should not be used.

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

    method : str
        ``'fir'`` will use overlap-add FIR filtering, ``'iir'`` will use IIR
        forward-backward filtering (via `scipy.signal.filtfilt`).

    iir_params : dict | None
        Dictionary of parameters to use for IIR filtering.
        If ``iir_params=None`` and ``method="iir"``, 4th order Butterworth will be used.
        For more information, see `mne.filter.construct_iir_filter`.

    phase : str
        Phase of the filter.
        When ``method='fir'``, symmetric linear-phase FIR filters are constructed,
        and if ``phase='zero'`` (default), the delay of this filter is compensated
        for, making it non-causal. If ``phase='zero-double'``,
        then this filter is applied twice, once forward, and once backward
        (also making it non-causal). If ``'minimum'``, then a minimum-phase filter
        will be constructed and applied, which is causal but has weaker stop-band
        suppression.
        When ``method='iir'``, ``phase='zero'`` (default) or
        ``phase='zero-double'`` constructs and applies IIR filter twice, once
        forward, and once backward (making it non-causal) using
        `scipy.signal.filtfilt`.
        If ``phase='forward'``, it constructs and applies forward IIR filter using
        `scipy.signal.lfilter`.

        ✨ Added in vesion 0.13

    fir_window : str
        The window to use in FIR design, can be "hamming" (default),
        "hann" (default in 0.13), or "blackman".

        ✨ Added in vesion 0.15

    fir_design : str
        Can be "firwin" (default) to use `scipy.signal.firwin`,
        or "firwin2" to use `scipy.signal.firwin2`. "firwin" uses
        a time-domain design technique that generally gives improved
        attenuation using fewer samples than "firwin2".

        ✨ Added in vesion 0.15

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    filt : array or dict
        Will be an array of FIR coefficients for method='fir', and dict
        with IIR parameters for method='iir'.

    ### 👉 See Also
    --------
    filter_data

    ### 📖 Notes
    -----
    ### 💡 Note For FIR filters, the *cutoff frequency*, i.e. the -6 dB point,
              is in the middle of the transition band (when using phase='zero'
              and fir_design='firwin'). For IIR filters, the cutoff frequency
              is given by ``l_freq`` or ``h_freq`` directly, and
              ``l_trans_bandwidth`` and ``h_trans_bandwidth`` are ignored.

    **Band-pass filter**

    The frequency response is (approximately) given by::

       1-|               ----------
         |             /|         | \\
     |H| |            / |         |  \\
         |           /  |         |   \\
         |          /   |         |    \\
       0-|----------    |         |     --------------
         |         |    |         |     |            |
         0        Fs1  Fp1       Fp2   Fs2          Nyq

    Where:

        * Fs1 = Fp1 - l_trans_bandwidth in Hz
        * Fs2 = Fp2 + h_trans_bandwidth in Hz

    **Band-stop filter**

    The frequency response is (approximately) given by::

        1-|---------                   ----------
          |         \\                 /
      |H| |          \\               /
          |           \\             /
          |            \\           /
        0-|             -----------
          |        |    |         |    |        |
          0       Fp1  Fs1       Fs2  Fp2      Nyq

    Where ``Fs1 = Fp1 + l_trans_bandwidth`` and
    ``Fs2 = Fp2 - h_trans_bandwidth``.

    Multiple stop bands can be specified using arrays.

    **Low-pass filter**

    The frequency response is (approximately) given by::

        1-|------------------------
          |                        \\
      |H| |                         \\
          |                          \\
          |                           \\
        0-|                            ----------------
          |                       |    |              |
          0                      Fp  Fstop           Nyq

    Where ``Fstop = Fp + trans_bandwidth``.

    **High-pass filter**

    The frequency response is (approximately) given by::

        1-|             -----------------------
          |            /
      |H| |           /
          |          /
          |         /
        0-|---------
          |        |    |                     |
          0      Fstop  Fp                   Nyq

    Where ``Fstop = Fp - trans_bandwidth``.

    ✨ Added in vesion 0.14
    """
    ...

def notch_filter(
    x,
    Fs,
    freqs,
    filter_length: str = "auto",
    notch_widths=None,
    trans_bandwidth: int = 1,
    method: str = "fir",
    iir_params=None,
    mt_bandwidth=None,
    p_value: float = 0.05,
    picks=None,
    n_jobs=None,
    copy: bool = True,
    phase: str = "zero",
    fir_window: str = "hamming",
    fir_design: str = "firwin",
    pad: str = "reflect_limited",
    *,
    verbose=None,
):
    """### Notch filter for the signal x.

    Applies a zero-phase notch filter to the signal x, operating on the last
    dimension.

    ### 🛠️ Parameters
    ----------
    x : array
        Signal to filter.
    Fs : float
        Sampling rate in Hz.
    freqs : float | array of float | None
        Frequencies to notch filter in Hz, e.g. np.arange(60, 241, 60).
        Multiple stop-bands can only be used with method='fir'
        and method='spectrum_fit'. None can only be used with the mode
        'spectrum_fit', where an F test is used to find sinusoidal components.

    filter_length : str | int
        Length of the FIR filter to use (if applicable):

        * **'auto' (default)**: The filter length is chosen based
          on the size of the transition regions (6.6 times the reciprocal
          of the shortest transition band for fir_window='hamming'
          and fir_design="firwin2", and half that for "firwin").
        * **str**: A human-readable time in
          units of "s" or "ms" (e.g., "10s" or "5500ms") will be
          converted to that number of samples if ``phase="zero"``, or
          the shortest power-of-two length at least that duration for
          ``phase="zero-double"``.
        * **int**: Specified length in samples. For fir_design="firwin",
          this should not be used.

        When ``method=='spectrum_fit'``, this sets the effective window duration
        over which fits are computed. See `mne.filter.create_filter`
        for options. Longer window lengths will give more stable frequency
        estimates, but require (potentially much) more processing and are not able
        to adapt as well to non-stationarities.

        The default in 0.21 is None, but this will change to ``'10s'`` in 0.22.
    notch_widths : float | array of float | None
        Width of the stop band (centred at each freq in freqs) in Hz.
        If None, freqs / 200 is used.
    trans_bandwidth : float
        Width of the transition band in Hz.
        Only used for ``method='fir'`` and ``method='iir'``.

    method : str
        ``'fir'`` will use overlap-add FIR filtering, ``'iir'`` will use IIR
        forward-backward filtering (via `scipy.signal.filtfilt`).
        'spectrum_fit' will use multi-taper estimation of sinusoidal
        components. If freqs=None and method='spectrum_fit', significant
        sinusoidal components are detected using an F test, and noted by
        logging.

    iir_params : dict | None
        Dictionary of parameters to use for IIR filtering.
        If ``iir_params=None`` and ``method="iir"``, 4th order Butterworth will be used.
        For more information, see `mne.filter.construct_iir_filter`.
    mt_bandwidth : float | None
        The bandwidth of the multitaper windowing function in Hz.
        Only used in 'spectrum_fit' mode.
    p_value : float
        P-value to use in F-test thresholding to determine significant
        sinusoidal components to remove when method='spectrum_fit' and
        freqs=None. Note that this will be Bonferroni corrected for the
        number of frequencies, so large p-values may be justified.
    picks : list | slice | None
        Channels to include. Slices and lists of integers will be interpreted as channel indices.
        None (default) will pick all channels. Note that channels in ``info['bads']`` *will be included* if their indices are explicitly provided.
        Only supported for 2D (n_channels, n_times) and 3D
        (n_epochs, n_channels, n_times) data.

    n_jobs : int | str
        Number of jobs to run in parallel. Can be ``'cuda'`` if ``cupy``
        is installed properly and ``method='fir'``.
    copy : bool
        If True, a copy of x, filtered, is returned. Otherwise, it operates
        on x in place.

    phase : str
        Phase of the filter.
        When ``method='fir'``, symmetric linear-phase FIR filters are constructed,
        and if ``phase='zero'`` (default), the delay of this filter is compensated
        for, making it non-causal. If ``phase='zero-double'``,
        then this filter is applied twice, once forward, and once backward
        (also making it non-causal). If ``'minimum'``, then a minimum-phase filter
        will be constructed and applied, which is causal but has weaker stop-band
        suppression.
        When ``method='iir'``, ``phase='zero'`` (default) or
        ``phase='zero-double'`` constructs and applies IIR filter twice, once
        forward, and once backward (making it non-causal) using
        `scipy.signal.filtfilt`.
        If ``phase='forward'``, it constructs and applies forward IIR filter using
        `scipy.signal.lfilter`.

        ✨ Added in vesion 0.13

    fir_window : str
        The window to use in FIR design, can be "hamming" (default),
        "hann" (default in 0.13), or "blackman".

        ✨ Added in vesion 0.15

    fir_design : str
        Can be "firwin" (default) to use `scipy.signal.firwin`,
        or "firwin2" to use `scipy.signal.firwin2`. "firwin" uses
        a time-domain design technique that generally gives improved
        attenuation using fewer samples than "firwin2".

        ✨ Added in vesion 0.15

    pad : str
        The type of padding to use. Supports all `numpy.pad` ``mode``
        options. Can also be ``"reflect_limited"``, which pads with a
        reflected version of each vector mirrored on the first and last values
        of the vector, followed by zeros.

        Only used for ``method='fir'``.
        The default is ``'reflect_limited'``.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    xf : array
        The x array filtered.

    ### 👉 See Also
    --------
    filter_data
    resample

    ### 📖 Notes
    -----
    The frequency response is (approximately) given by::

        1-|----------         -----------
          |          \\       /
      |H| |           \\     /
          |            \\   /
          |             \\ /
        0-|              -
          |         |    |    |         |
          0        Fp1 freq  Fp2       Nyq

    For each freq in freqs, where ``Fp1 = freq - trans_bandwidth / 2`` and
    ``Fs2 = freq + trans_bandwidth / 2``.

    References
    ----------
    Multi-taper removal is inspired by code from the Chronux toolbox, see
    www.chronux.org and the book "Observed Brain Dynamics" by Partha Mitra
    & Hemant Bokil, Oxford University Press, New York, 2008. Please
    cite this in publications if method 'spectrum_fit' is used.
    """
    ...

def resample(
    x,
    up: float = 1.0,
    down: float = 1.0,
    npad: int = 100,
    axis: int = -1,
    window: str = "boxcar",
    n_jobs=None,
    pad: str = "reflect_limited",
    *,
    verbose=None,
):
    """### Resample an array.

    Operates along the last dimension of the array.

    ### 🛠️ Parameters
    ----------
    x : ndarray
        Signal to resample.
    up : float
        Factor to upsample by.
    down : float
        Factor to downsample by.

    npad : int | str
        Amount to pad the start and end of the data.
        Can also be ``"auto"`` to use a padding that will result in
        a power-of-two size (can be much faster).
    axis : int
        Axis along which to resample (default is the last axis).

    window : str | tuple
        Frequency-domain window to use in resampling.
        See `scipy.signal.resample`.

    n_jobs : int | str
        Number of jobs to run in parallel. Can be ``'cuda'`` if ``cupy``
        is installed properly.

    pad : str
        The type of padding to use. Supports all `numpy.pad` ``mode``
        options. Can also be ``"reflect_limited"``, which pads with a
        reflected version of each vector mirrored on the first and last values
        of the vector, followed by zeros.
        The default is ``'reflect_limited'``.

        ✨ Added in vesion 0.15

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    y : array
        The x array resampled.

    ### 📖 Notes
    -----
    This uses (hopefully) intelligent edge padding and frequency-domain
    windowing improve scipy.signal.resample's resampling method, which
    we have adapted for our use here. Choices of npad and window have
    important consequences, and the default choices should work well
    for most natural signals.

    Resampling arguments are broken into "up" and "down" components for future
    compatibility in case we decide to use an upfirdn implementation. The
    current implementation is functionally equivalent to passing
    up=up/down and down=1.
    """
    ...

def detrend(x, order: int = 1, axis: int = -1):
    """### Detrend the array x.

    ### 🛠️ Parameters
    ----------
    x : n-d array
        Signal to detrend.
    order : int
        Fit order. Currently must be '0' or '1'.
    axis : int
        Axis of the array to operate on.

    ### ⏎ Returns
    -------
    y : array
        The x array detrended.

    Examples
    --------
    As in `scipy.signal.detrend`::

        >>> randgen = np.random.RandomState(9)
        >>> npoints = int(1e3)
        >>> noise = randgen.randn(npoints)
        >>> x = 3 + 2*np.linspace(0, 1, npoints) + noise
        >>> bool((detrend(x) - noise).max() < 0.01)
        True
    """
    ...

class FilterMixin:
    """### Object for Epoch/Evoked filtering."""

    def savgol_filter(self, h_freq, verbose=None):
        """### Filter the data using Savitzky-Golay polynomial method.

        ### 🛠️ Parameters
        ----------
        h_freq : float
            Approximate high cut-off frequency in Hz. Note that this
            is not an exact cutoff, since Savitzky-Golay filtering
            :footcite:`SavitzkyGolay1964` is done using polynomial fits
            instead of FIR/IIR filtering. This parameter is thus used to
            determine the length of the window over which a 5th-order
            polynomial smoothing is used.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        ### ⏎ Returns
        -------
        inst : instance of Epochs or Evoked
            The object with the filtering applied.

        ### 👉 See Also
        --------
        mne.io.Raw.filter

        ### 📖 Notes
        -----
        For Savitzky-Golay low-pass approximation, see:

            https://gist.github.com/larsoner/bbac101d50176611136b

        ✨ Added in vesion 0.9.0

        References
        ----------
        .. footbibliography::

        Examples
        --------
        >>> import mne
        >>> from os import path as op
        >>> evoked_fname = op.join(mne.datasets.sample.data_path(), 'MEG', 'sample', 'sample_audvis-ave.fif')  # doctest:+SKIP
        >>> evoked = mne.read_evokeds(evoked_fname, baseline=(None, 0))[0]  # doctest:+SKIP
        >>> evoked.savgol_filter(10.)  # low-pass at around 10 Hz # doctest:+SKIP
        >>> evoked.plot()  # doctest:+SKIP
        """
        ...
    def filter(
        self,
        l_freq,
        h_freq,
        picks=None,
        filter_length: str = "auto",
        l_trans_bandwidth: str = "auto",
        h_trans_bandwidth: str = "auto",
        n_jobs=None,
        method: str = "fir",
        iir_params=None,
        phase: str = "zero",
        fir_window: str = "hamming",
        fir_design: str = "firwin",
        skip_by_annotation=("edge", "bad_acq_skip"),
        pad: str = "edge",
        *,
        verbose=None,
    ):
        """### Filter a subset of channels.

        ### 🛠️ Parameters
        ----------

        l_freq : float | None
            For FIR filters, the lower pass-band edge; for IIR filters, the lower
            cutoff frequency. If None the data are only low-passed.

        h_freq : float | None
            For FIR filters, the upper pass-band edge; for IIR filters, the upper
            cutoff frequency. If None the data are only high-passed.
        picks : str | array-like | slice | None
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel *type* strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick all data channels. Note that channels
            in ``info['bads']`` *will be included* if their names or indices are
            explicitly provided.

        filter_length : str | int
            Length of the FIR filter to use (if applicable):

            * **'auto' (default)**: The filter length is chosen based
              on the size of the transition regions (6.6 times the reciprocal
              of the shortest transition band for fir_window='hamming'
              and fir_design="firwin2", and half that for "firwin").
            * **str**: A human-readable time in
              units of "s" or "ms" (e.g., "10s" or "5500ms") will be
              converted to that number of samples if ``phase="zero"``, or
              the shortest power-of-two length at least that duration for
              ``phase="zero-double"``.
            * **int**: Specified length in samples. For fir_design="firwin",
              this should not be used.

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

        n_jobs : int | str
            Number of jobs to run in parallel. Can be ``'cuda'`` if ``cupy``
            is installed properly and ``method='fir'``.

        method : str
            ``'fir'`` will use overlap-add FIR filtering, ``'iir'`` will use IIR
            forward-backward filtering (via `scipy.signal.filtfilt`).

        iir_params : dict | None
            Dictionary of parameters to use for IIR filtering.
            If ``iir_params=None`` and ``method="iir"``, 4th order Butterworth will be used.
            For more information, see `mne.filter.construct_iir_filter`.

        phase : str
            Phase of the filter.
            When ``method='fir'``, symmetric linear-phase FIR filters are constructed,
            and if ``phase='zero'`` (default), the delay of this filter is compensated
            for, making it non-causal. If ``phase='zero-double'``,
            then this filter is applied twice, once forward, and once backward
            (also making it non-causal). If ``'minimum'``, then a minimum-phase filter
            will be constructed and applied, which is causal but has weaker stop-band
            suppression.
            When ``method='iir'``, ``phase='zero'`` (default) or
            ``phase='zero-double'`` constructs and applies IIR filter twice, once
            forward, and once backward (making it non-causal) using
            `scipy.signal.filtfilt`.
            If ``phase='forward'``, it constructs and applies forward IIR filter using
            `scipy.signal.lfilter`.

            ✨ Added in vesion 0.13

        fir_window : str
            The window to use in FIR design, can be "hamming" (default),
            "hann" (default in 0.13), or "blackman".

            ✨ Added in vesion 0.15

        fir_design : str
            Can be "firwin" (default) to use `scipy.signal.firwin`,
            or "firwin2" to use `scipy.signal.firwin2`. "firwin" uses
            a time-domain design technique that generally gives improved
            attenuation using fewer samples than "firwin2".

            ✨ Added in vesion 0.15

        skip_by_annotation : str | list of str
            If a string (or list of str), any annotation segment that begins
            with the given string will not be included in filtering, and
            segments on either side of the given excluded annotated segment
            will be filtered separately (i.e., as independent signals).
            The default (``('edge', 'bad_acq_skip')`` will separately filter
            any segments that were concatenated by `mne.concatenate_raws`
            or `mne.io.Raw.append`, or separated during acquisition.
            To disable, provide an empty list. Only used if ``inst`` is raw.

            ✨ Added in vesion 0.16.

        pad : str
            The type of padding to use. Supports all `numpy.pad` ``mode``
            options. Can also be ``"reflect_limited"``, which pads with a
            reflected version of each vector mirrored on the first and last values
            of the vector, followed by zeros.

            Only used for ``method='fir'``.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        ### ⏎ Returns
        -------
        inst : instance of Epochs, Evoked, or Raw
            The filtered data.

        ### 👉 See Also
        --------
        mne.filter.create_filter
        mne.Evoked.savgol_filter
        mne.io.Raw.notch_filter
        mne.io.Raw.resample
        mne.filter.create_filter
        mne.filter.filter_data
        mne.filter.construct_iir_filter

        ### 📖 Notes
        -----
        Applies a zero-phase low-pass, high-pass, band-pass, or band-stop
        filter to the channels selected by ``picks``.
        The data are modified inplace.

        The object has to have the data loaded e.g. with ``preload=True``
        or ``self.load_data()``.

        ``l_freq`` and ``h_freq`` are the frequencies below which and above
        which, respectively, to filter out of the data. Thus the uses are:

            * ``l_freq < h_freq``: band-pass filter
            * ``l_freq > h_freq``: band-stop filter
            * ``l_freq is not None and h_freq is None``: high-pass filter
            * ``l_freq is None and h_freq is not None``: low-pass filter

        ``self.info['lowpass']`` and ``self.info['highpass']`` are only
        updated with picks=None.

        ### 💡 Note If n_jobs > 1, more memory is required as
                  ``len(picks) * n_times`` additional time points need to
                  be temporarily stored in memory.

        For more information, see the tutorials
        `disc-filtering` and `tut-filter-resample` and
        `mne.filter.create_filter`.

        ✨ Added in vesion 0.15
        """
        ...
    def resample(
        self,
        sfreq,
        npad: str = "auto",
        window: str = "boxcar",
        n_jobs=None,
        pad: str = "edge",
        *,
        verbose=None,
    ):
        """### Resample data.

        If appropriate, an anti-aliasing filter is applied before resampling.
        See `resampling-and-decimating` for more information.

        ### 💡 Note Data must be loaded.

        ### 🛠️ Parameters
        ----------
        sfreq : float
            New sample rate to use.

        npad : int | str
            Amount to pad the start and end of the data.
            Can also be ``"auto"`` to use a padding that will result in
            a power-of-two size (can be much faster).

        window : str | tuple
            Frequency-domain window to use in resampling.
            See `scipy.signal.resample`.

        n_jobs : int | str
            Number of jobs to run in parallel. Can be ``'cuda'`` if ``cupy``
            is installed properly.

        pad : str
            The type of padding to use. Supports all `numpy.pad` ``mode``
            options. Can also be ``"reflect_limited"``, which pads with a
            reflected version of each vector mirrored on the first and last values
            of the vector, followed by zeros.
            The default is ``'edge'``, which pads with the edge values of each
            vector.

            ✨ Added in vesion 0.15

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        ### ⏎ Returns
        -------
        inst : instance of Epochs or Evoked
            The resampled object.

        ### 👉 See Also
        --------
        mne.io.Raw.resample

        ### 📖 Notes
        -----
        For some data, it may be more accurate to use npad=0 to reduce
        artifacts. This is dataset dependent -- check your data!
        """
        ...
    def apply_hilbert(
        self,
        picks=None,
        envelope: bool = False,
        n_jobs=None,
        n_fft: str = "auto",
        *,
        verbose=None,
    ):
        """### Compute analytic signal or envelope for a subset of channels.

        ### 🛠️ Parameters
        ----------
        picks : str | array-like | slice | None
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel *type* strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick all data channels (excluding reference
            MEG channels). Note that channels in ``info['bads']`` *will be included* if
            their names or indices are explicitly provided.
        envelope : bool
            Compute the envelope signal of each channel. Default False.
            See Notes.
        n_jobs : int | None
            The number of jobs to run in parallel. If ``-1``, it is set
            to the number of CPU cores. Requires the `joblib` package.
            ``None`` (default) is a marker for 'unset' that will be interpreted
            as ``n_jobs=1`` (sequential execution) unless the call is performed under
            a `joblib:joblib.parallel_config` context manager that sets another
            value for ``n_jobs``.
        n_fft : int | None | str
            Points to use in the FFT for Hilbert transformation. The signal
            will be padded with zeros before computing Hilbert, then cut back
            to original length. If None, n == self.n_times. If 'auto',
            the next highest fast FFT length will be use.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        ### ⏎ Returns
        -------
        self : instance of Raw, Epochs, or Evoked
            The raw object with transformed data.

        ### 📖 Notes
        -----
        **Parameters**

        If ``envelope=False``, the analytic signal for the channels defined in
        ``picks`` is computed and the data of the Raw object is converted to
        a complex representation (the analytic signal is complex valued).

        If ``envelope=True``, the absolute value of the analytic signal for the
        channels defined in ``picks`` is computed, resulting in the envelope
        signal.

        .. warning: Do not use ``envelope=True`` if you intend to compute
                    an inverse solution from the raw data. If you want to
                    compute the envelope in source space, use
                    ``envelope=False`` and compute the envelope after the
                    inverse solution has been obtained.

        If envelope=False, more memory is required since the original raw data
        as well as the analytic signal have temporarily to be stored in memory.
        If n_jobs > 1, more memory is required as ``len(picks) * n_times``
        additional time points need to be temporarily stored in memory.

        Also note that the ``n_fft`` parameter will allow you to pad the signal
        with zeros before performing the Hilbert transform. This padding
        is cut off, but it may result in a slightly different result
        (particularly around the edges). Use at your own risk.

        **Analytic signal**

        The analytic signal "x_a(t)" of "x(t)" is::

            x_a = F^{-1}(F(x) 2U) = x + i y

        where "F" is the Fourier transform, "U" the unit step function,
        and "y" the Hilbert transform of "x". One usage of the analytic
        signal is the computation of the envelope signal, which is given by
        "e(t) = abs(x_a(t))". Due to the linearity of Hilbert transform and the
        MNE inverse solution, the enevlope in source space can be obtained
        by computing the analytic signal in sensor space, applying the MNE
        inverse, and computing the envelope in source space.
        """
        ...

def design_mne_c_filter(
    sfreq,
    l_freq=None,
    h_freq: float = 40.0,
    l_trans_bandwidth=None,
    h_trans_bandwidth: float = 5.0,
    verbose=None,
):
    """### Create a FIR filter like that used by MNE-C.

    ### 🛠️ Parameters
    ----------
    sfreq : float
        The sample frequency.
    l_freq : float | None
        The low filter frequency in Hz, default None.
        Can be None to avoid high-passing.
    h_freq : float
        The high filter frequency in Hz, default 40.
        Can be None to avoid low-passing.
    l_trans_bandwidth : float | None
        Low transition bandwidthin Hz. Can be None (default) to use 3 samples.
    h_trans_bandwidth : float
        High transition bandwidth in Hz.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    h : ndarray, shape (8193,)
        The linear-phase (symmetric) FIR filter coefficients.

    ### 📖 Notes
    -----
    This function is provided mostly for reference purposes.

    MNE-C uses a frequency-domain filter design technique by creating a
    linear-phase filter of length 8193. In the frequency domain, the
    4197 frequencies are directly constructed, with zeroes in the stop-band
    and ones in the passband, with squared cosine ramps in between.
    """
    ...
