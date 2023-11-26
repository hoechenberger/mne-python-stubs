from .._fiff.meas_info import ContainsMixin as ContainsMixin, Info as Info
from .._fiff.pick import channel_type as channel_type, pick_info as pick_info
from ..baseline import rescale as rescale
from ..channels.channels import UpdateChannelsMixin as UpdateChannelsMixin
from ..filter import next_fast_len as next_fast_len
from ..parallel import parallel_func as parallel_func
from ..utils import (
    ExtendedTimeMixin as ExtendedTimeMixin,
    GetEpochsMixin as GetEpochsMixin,
    SizeMixin as SizeMixin,
    check_fname as check_fname,
    copy_function_doc_to_method_doc as copy_function_doc_to_method_doc,
    fill_doc as fill_doc,
    logger as logger,
    sizeof_fmt as sizeof_fmt,
    warn as warn,
)
from ..viz.topomap import (
    plot_tfr_topomap as plot_tfr_topomap,
    plot_topomap as plot_topomap,
)
from ..viz.utils import (
    add_background_image as add_background_image,
    figure_nobar as figure_nobar,
    plt_show as plt_show,
)
from .multitaper import dpss_windows as dpss_windows
from _typeshed import Incomplete

def morlet(sfreq, freqs, n_cycles: float = 7.0, sigma=None, zero_mean: bool = False):
    """### Compute Morlet wavelets for the given frequency range.

    ### 🛠️ Parameters
    ----------
    sfreq : float
        The sampling Frequency.
    freqs : float | array-like, shape (n_freqs,)
        Frequencies to compute Morlet wavelets for.
    n_cycles : float | array-like, shape (n_freqs,)
        Number of cycles. Can be a fixed number (float) or one per frequency
        (array-like).
    sigma : float, default None
        It controls the width of the wavelet ie its temporal
        resolution. If sigma is None the temporal resolution
        is adapted with the frequency like for all wavelet transform.
        The higher the frequency the shorter is the wavelet.
        If sigma is fixed the temporal resolution is fixed
        like for the short time Fourier transform and the number
        of oscillations increases with the frequency.
    zero_mean : bool, default False
        Make sure the wavelet has a mean of zero.

    ### ⏎ Returns
    -------
    Ws : list of ndarray | ndarray
        The wavelets time series. If ``freqs`` was a float, a single
        ndarray is returned instead of a list of ndarray.

    See Also
    --------
    mne.time_frequency.fwhm

    ### 📖 Notes
    -----

    The Morlet wavelets follow the formulation in :footcite:t:`Tallon-BaudryEtAl1997`.

    Convolution of a signal with a Morlet wavelet will impose temporal smoothing
    that is determined by the duration of the wavelet. In MNE-Python, the duration
    of the wavelet is determined by the ``sigma`` parameter, which gives the
    standard deviation of the wavelet's Gaussian envelope (our wavelets extend to
    ±5 standard deviations to ensure values very close to zero at the endpoints).
    Some authors (e.g., :footcite:t:`Cohen2019`) recommend specifying and reporting
    wavelet duration in terms of the full-width half-maximum (FWHM) of the
    wavelet's Gaussian envelope. The FWHM is related to ``sigma`` by the following
    identity: :math:`\\mathrm{FWHM} = \\sigma \\times 2 \\sqrt{2 \\ln{2}}` (or the
    equivalent in Python code: ``fwhm = sigma * 2 * np.sqrt(2 * np.log(2))``).
    If ``sigma`` is not provided, it is computed from ``n_cycles`` as
    :math:`\\frac{\\mathtt{n\\_cycles}}{2 \\pi f}` where :math:`f` is the frequency of
    the wavelet oscillation (given by ``freqs``). Thus when ``sigma=None`` the FWHM
    will be given by

    .. math::

        \\mathrm{FWHM} = \\frac{\\mathtt{n\\_cycles} \\times \\sqrt{2 \\ln{2}}}{\\pi \\times f}

    (cf. eq. 4 in :footcite:`Cohen2019`). To create wavelets with a chosen FWHM,
    one can compute::

        n_cycles = desired_fwhm * np.pi * np.array(freqs) / np.sqrt(2 * np.log(2))

    to get an array of values for ``n_cycles`` that yield the desired FWHM at each
    frequency in ``freqs``.  If you want different FWHM values at each frequency,
    do the same computation with ``desired_fwhm`` as an array of the same shape as
    ``freqs``.

    References
    ----------
    .. footbibliography::

    Examples
    --------
    Let's show a simple example of the relationship between ``n_cycles`` and
    the FWHM using `mne.time_frequency.fwhm`, as well as the equivalent
    call using `scipy.signal.morlet2`:

    .. plot::

        import numpy as np
        from scipy.signal import morlet2 as sp_morlet
        import matplotlib.pyplot as plt
        from mne.time_frequency import morlet, fwhm

        sfreq, freq, n_cycles = 1000., 10, 7  # i.e., 700 ms
        this_fwhm = fwhm(freq, n_cycles)
        wavelet = morlet(sfreq=sfreq, freqs=freq, n_cycles=n_cycles)
        M, w = len(wavelet), n_cycles # convert to SciPy convention
        s = w * sfreq / (2 * freq * np.pi)  # from SciPy docs
        wavelet_sp = sp_morlet(M, s, w) * np.sqrt(2)  # match our normalization

        _, ax = plt.subplots(layout="constrained")
        colors = {
            ('MNE', 'real'): '#66CCEE',
            ('SciPy', 'real'): '#4477AA',
            ('MNE', 'imag'): '#EE6677',
            ('SciPy', 'imag'): '#AA3377',
        }
        lw = dict(MNE=2, SciPy=4)
        zorder = dict(MNE=5, SciPy=4)
        t = np.arange(-M // 2 + 1, M // 2 + 1) / sfreq
        for name, w in (('MNE', wavelet), ('SciPy', wavelet_sp)):
            for kind in ('real', 'imag'):
                ax.plot(t, getattr(w, kind), label=f'{name} {kind}',
                        lw=lw[name], color=colors[(name, kind)],
                        zorder=zorder[name])
        ax.plot(t, np.abs(wavelet), label=f'MNE abs', color='k', lw=1., zorder=6)
        half_max = np.max(np.abs(wavelet)) / 2.
        ax.plot([-this_fwhm / 2., this_fwhm / 2.], [half_max, half_max],
                color='k', linestyle='-', label='FWHM', zorder=6)
        ax.legend(loc='upper right')
        ax.set(xlabel='Time (s)', ylabel='Amplitude')
    """
    ...

def fwhm(freq, n_cycles):
    """### Compute the full-width half maximum of a Morlet wavelet.

    Uses the formula from :footcite:t:`Cohen2019`.

    ### 🛠️ Parameters
    ----------
    freq : float
        The oscillation frequency of the wavelet.
    n_cycles : float
        The duration of the wavelet, expressed as the number of oscillation
        cycles.

    ### ⏎ Returns
    -------
    fwhm : float
        The full-width half maximum of the wavelet.

    ### 📖 Notes
    -----
     ✨ Added in vesion 1.3

    References
    ----------
    .. footbibliography::
    """
    ...

def cwt(X, Ws, use_fft: bool = True, mode: str = "same", decim: int = 1):
    """### Compute time-frequency decomposition with continuous wavelet transform.

    ### 🛠️ Parameters
    ----------
    X : array, shape (n_signals, n_times)
        The signals.
    Ws : list of array
        Wavelets time series.
    use_fft : bool
        Use FFT for convolutions. Defaults to True.
    mode : 'same' | 'valid' | 'full'
        Convention for convolution. 'full' is currently not implemented with
        ``use_fft=False``. Defaults to ``'same'``.

    decim : int | slice, default 1
        To reduce memory usage, decimation factor after time-frequency
        decomposition.

        - if `int`, returns ``tfr[..., ::decim]``.
        - if `slice`, returns ``tfr[..., decim]``.

        ### 💡 Note
            Decimation is done after convolutions and may create aliasing
            artifacts.

    ### ⏎ Returns
    -------
    tfr : array, shape (n_signals, n_freqs, n_times)
        The time-frequency decompositions.

    See Also
    --------
    mne.time_frequency.tfr_morlet : Compute time-frequency decomposition
                                    with Morlet wavelets.
    """
    ...

def tfr_morlet(
    inst,
    freqs,
    n_cycles,
    use_fft: bool = False,
    return_itc: bool = True,
    decim: int = 1,
    n_jobs=None,
    picks=None,
    zero_mean: bool = True,
    average: bool = True,
    output: str = "power",
    verbose=None,
):
    """### Compute Time-Frequency Representation (TFR) using Morlet wavelets.

    Same computation as `mne.time_frequency.tfr_array_morlet`, but
    operates on `mne.Epochs` or `mne.Evoked` objects instead of
    `NumPy arrays <numpy.ndarray>`.

    ### 🛠️ Parameters
    ----------
    inst : Epochs | Evoked
        The epochs or evoked object.

    freqs : array of float, shape (n_freqs,)
        The frequencies of interest in Hz.

    n_cycles : int | array of int, shape (n_freqs,)
        Number of cycles in the wavelet, either a fixed number or one per
        frequency. The number of cycles ``n_cycles`` and the frequencies of
        interest ``freqs`` define the temporal window length. See notes for
        additional information about the relationship between those arguments
        and about time and frequency smoothing.
    use_fft : bool, default False
        The fft based convolution or not.
    return_itc : bool, default True
        Return inter-trial coherence (ITC) as well as averaged power.
        Must be ``False`` for evoked data.

    decim : int | slice, default 1
        To reduce memory usage, decimation factor after time-frequency
        decomposition.

        - if `int`, returns ``tfr[..., ::decim]``.
        - if `slice`, returns ``tfr[..., decim]``.

        ### 💡 Note
            Decimation is done after convolutions and may create aliasing
            artifacts.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.
    picks : array-like of int | None, default None
        The indices of the channels to decompose. If None, all available
        good data channels are decomposed.
    zero_mean : bool, default True
        Make sure the wavelet has a mean of zero.

        ✨ Added in vesion 0.13.0

    average : bool, default True
        If ``False`` return an `EpochsTFR` containing separate TFRs for each
        epoch. If ``True`` return an `AverageTFR` containing the average of all
        TFRs across epochs.

        ### 💡 Note
            Using ``average=True`` is functionally equivalent to using
            ``average=False`` followed by ``EpochsTFR.average()``, but is
            more memory efficient.

        ✨ Added in vesion 0.13.0
    output : str
        Can be ``"power"`` (default) or ``"complex"``. If ``"complex"``, then
        ``average`` must be ``False``.

        ✨ Added in vesion 0.15.0

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    power : AverageTFR | EpochsTFR
        The averaged or single-trial power.
    itc : AverageTFR | EpochsTFR
        The inter-trial coherence (ITC). Only returned if return_itc
        is True.

    See Also
    --------
    mne.time_frequency.tfr_array_morlet
    mne.time_frequency.tfr_multitaper
    mne.time_frequency.tfr_array_multitaper
    mne.time_frequency.tfr_stockwell
    mne.time_frequency.tfr_array_stockwell

    ### 📖 Notes
    -----

    The Morlet wavelets follow the formulation in :footcite:t:`Tallon-BaudryEtAl1997`.

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

    In MNE-Python, the length of the Morlet wavelet is affected by the arguments
    ``freqs`` and ``n_cycles``, which define the frequencies of interest
    and the number of cycles, respectively. For the time-frequency representation,
    the length of the wavelet is defined such that both tails of
    the wavelet extend five standard deviations from the midpoint of its Gaussian
    envelope and that there is a sample at time zero.

    The length of the wavelet is thus :math:`10\\times\\mathtt{sfreq}\\cdot\\sigma-1`,
    which is equal to :math:`\\frac{5}{\\pi} \\cdot \\frac{\\mathtt{n\\_cycles} \\cdot
    \\mathtt{sfreq}}{\\mathtt{freqs}} - 1`, where
    :math:`\\sigma = \\frac{\\mathtt{n\\_cycles}}{2\\pi f}` corresponds to the standard
    deviation of the wavelet's Gaussian envelope. Note that the length of the
    wavelet must not exceed the length of your signal.

    For more information on the Morlet wavelet, see `mne.time_frequency.morlet`.

    See `mne.time_frequency.morlet` for more information about the
    Morlet wavelet.

    References
    ----------
    .. footbibliography::
    """
    ...

def tfr_array_morlet(
    epoch_data,
    sfreq,
    freqs,
    n_cycles: float = 7.0,
    zero_mean: bool = False,
    use_fft: bool = True,
    decim: int = 1,
    output: str = "complex",
    n_jobs=None,
    verbose=None,
):
    """### Compute Time-Frequency Representation (TFR) using Morlet wavelets.

    Same computation as `mne.time_frequency.tfr_morlet`, but operates on
    `NumPy arrays <numpy.ndarray>` instead of `mne.Epochs` objects.

    ### 🛠️ Parameters
    ----------
    epoch_data : array of shape (n_epochs, n_channels, n_times)
        The epochs.
    sfreq : float | int
        Sampling frequency of the data.

    freqs : array of float, shape (n_freqs,)
        The frequencies of interest in Hz.

    n_cycles : int | array of int, shape (n_freqs,)
        Number of cycles in the wavelet, either a fixed number or one per
        frequency. The number of cycles ``n_cycles`` and the frequencies of
        interest ``freqs`` define the temporal window length. See notes for
        additional information about the relationship between those arguments
        and about time and frequency smoothing.
    zero_mean : bool
        If True, make sure the wavelets have a mean of zero. default False.
    use_fft : bool
        Use the FFT for convolutions or not. default True.

    decim : int | slice, default 1
        To reduce memory usage, decimation factor after time-frequency
        decomposition.

        - if `int`, returns ``tfr[..., ::decim]``.
        - if `slice`, returns ``tfr[..., decim]``.

        ### 💡 Note
            Decimation is done after convolutions and may create aliasing
            artifacts.
    output : str, default ``'complex'``

        * ``'complex'`` : single trial complex.
        * ``'power'`` : single trial power.
        * ``'phase'`` : single trial phase.
        * ``'avg_power'`` : average of single trial power.
        * ``'itc'`` : inter-trial coherence.
        * ``'avg_power_itc'`` : average of single trial power and inter-trial
          coherence across trials.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.
        The number of epochs to process at the same time. The parallelization
        is implemented across channels. Default 1.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    out : array
        Time frequency transform of epoch_data.

        - if ``output in ('complex', 'phase', 'power')``, array of shape
          ``(n_epochs, n_chans, n_freqs, n_times)``
        - else, array of shape ``(n_chans, n_freqs, n_times)``

        If ``output`` is ``'avg_power_itc'``, the real values in ``out``
        contain the average power and the imaginary values contain the ITC:
        :math:`out = power_{avg} + i * itc`.

    See Also
    --------
    mne.time_frequency.tfr_morlet
    mne.time_frequency.tfr_multitaper
    mne.time_frequency.tfr_array_multitaper
    mne.time_frequency.tfr_stockwell
    mne.time_frequency.tfr_array_stockwell

    ### 📖 Notes
    -----

    The Morlet wavelets follow the formulation in :footcite:t:`Tallon-BaudryEtAl1997`.

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

    In MNE-Python, the length of the Morlet wavelet is affected by the arguments
    ``freqs`` and ``n_cycles``, which define the frequencies of interest
    and the number of cycles, respectively. For the time-frequency representation,
    the length of the wavelet is defined such that both tails of
    the wavelet extend five standard deviations from the midpoint of its Gaussian
    envelope and that there is a sample at time zero.

    The length of the wavelet is thus :math:`10\\times\\mathtt{sfreq}\\cdot\\sigma-1`,
    which is equal to :math:`\\frac{5}{\\pi} \\cdot \\frac{\\mathtt{n\\_cycles} \\cdot
    \\mathtt{sfreq}}{\\mathtt{freqs}} - 1`, where
    :math:`\\sigma = \\frac{\\mathtt{n\\_cycles}}{2\\pi f}` corresponds to the standard
    deviation of the wavelet's Gaussian envelope. Note that the length of the
    wavelet must not exceed the length of your signal.

    For more information on the Morlet wavelet, see `mne.time_frequency.morlet`.

    ✨ Added in vesion 0.14.0

    References
    ----------
    .. footbibliography::
    """
    ...

def tfr_multitaper(
    inst,
    freqs,
    n_cycles,
    time_bandwidth: float = 4.0,
    use_fft: bool = True,
    return_itc: bool = True,
    decim: int = 1,
    n_jobs=None,
    picks=None,
    average: bool = True,
    *,
    verbose=None,
):
    """### Compute Time-Frequency Representation (TFR) using DPSS tapers.

    Same computation as `mne.time_frequency.tfr_array_multitaper`, but
    operates on `mne.Epochs` or `mne.Evoked` objects instead of
    `NumPy arrays <numpy.ndarray>`.

    ### 🛠️ Parameters
    ----------
    inst : Epochs | Evoked
        The epochs or evoked object.

    freqs : array of float, shape (n_freqs,)
        The frequencies of interest in Hz.

    n_cycles : int | array of int, shape (n_freqs,)
        Number of cycles in the wavelet, either a fixed number or one per
        frequency. The number of cycles ``n_cycles`` and the frequencies of
        interest ``freqs`` define the temporal window length. See notes for
        additional information about the relationship between those arguments
        and about time and frequency smoothing.

    time_bandwidth : float ``≥ 2.0``
        Product between the temporal window length (in seconds) and the *full*
        frequency bandwidth (in Hz). This product can be seen as the surface of the
        window on the time/frequency plane and controls the frequency bandwidth
        (thus the frequency resolution) and the number of good tapers. See notes
        for additional information.
    use_fft : bool, default True
        The fft based convolution or not.
    return_itc : bool, default True
        Return inter-trial coherence (ITC) as well as averaged (or
        single-trial) power.

    decim : int | slice, default 1
        To reduce memory usage, decimation factor after time-frequency
        decomposition.

        - if `int`, returns ``tfr[..., ::decim]``.
        - if `slice`, returns ``tfr[..., decim]``.

        ### 💡 Note
            Decimation is done after convolutions and may create aliasing
            artifacts.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick good data channels. Note that channels
        in ``info['bads']`` *will be included* if their names or indices are
        explicitly provided.

    average : bool, default True
        If ``False`` return an `EpochsTFR` containing separate TFRs for each
        epoch. If ``True`` return an `AverageTFR` containing the average of all
        TFRs across epochs.

        ### 💡 Note
            Using ``average=True`` is functionally equivalent to using
            ``average=False`` followed by ``EpochsTFR.average()``, but is
            more memory efficient.

        ✨ Added in vesion 0.13.0

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    power : AverageTFR | EpochsTFR
        The averaged or single-trial power.
    itc : AverageTFR | EpochsTFR
        The inter-trial coherence (ITC). Only returned if return_itc
        is True.

    See Also
    --------
    mne.time_frequency.tfr_array_multitaper
    mne.time_frequency.tfr_stockwell
    mne.time_frequency.tfr_array_stockwell
    mne.time_frequency.tfr_morlet
    mne.time_frequency.tfr_array_morlet

    ### 📖 Notes
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

    ### ⛔️ Warning

        In `mne.time_frequency.tfr_array_multitaper` and
        `mne.time_frequency.tfr_multitaper`, ``time_bandwidth`` defines the
        product of the temporal window length with the *full* frequency bandwidth
        For example, a full bandwidth of 4 Hz at a frequency of interest of 10 Hz
        will "smear" the frequency estimate between 8 Hz and 12 Hz.

        This is not the case for `mne.time_frequency.psd_array_multitaper` where
        the argument ``bandwidth`` defines the *half* frequency bandwidth. In the
        example above, the half-frequency bandwidth is 2 Hz.

    ✨ Added in vesion 0.9.0
    """
    ...

class _BaseTFR(ContainsMixin, UpdateChannelsMixin, SizeMixin, ExtendedTimeMixin):
    """### Base TFR class."""

    baseline: Incomplete

    def __init__(self) -> None: ...
    @property
    def data(self): ...
    @data.setter
    def data(self, data) -> None: ...
    @property
    def ch_names(self):
        """### Channel names."""
        ...
    freqs: Incomplete

    def crop(
        self, tmin=None, tmax=None, fmin=None, fmax=None, include_tmax: bool = True
    ):
        """### Crop data to a given time interval in place.

        ### 🛠️ Parameters
        ----------
        tmin : float | None
            Start time of selection in seconds.
        tmax : float | None
            End time of selection in seconds.
        fmin : float | None
            Lowest frequency of selection in Hz.

            ✨ Added in vesion 0.18.0
        fmax : float | None
            Highest frequency of selection in Hz.

            ✨ Added in vesion 0.18.0

        include_tmax : bool
            If True (default), include tmax. If False, exclude tmax (similar to how
            Python indexing typically works).

            ✨ Added in vesion 0.19

        ### ⏎ Returns
        -------
        inst : instance of AverageTFR
            The modified instance.
        """
        ...
    def copy(self):
        """### Return a copy of the instance.

        ### ⏎ Returns
        -------
        copy : instance of EpochsTFR | instance of AverageTFR
            A copy of the instance.
        """
        ...
    def apply_baseline(self, baseline, mode: str = "mean", verbose=None):
        """### Baseline correct the data.

        ### 🛠️ Parameters
        ----------
        baseline : array-like, shape (2,)
            The time interval to apply rescaling / baseline correction.
            If None do not apply it. If baseline is (a, b)
            the interval is between "a (s)" and "b (s)".
            If a is None the beginning of the data is used
            and if b is None then b is set to the end of the interval.
            If baseline is equal to (None, None) all the time
            interval is used.
        mode : 'mean' | 'ratio' | 'logratio' | 'percent' | 'zscore' | 'zlogratio'
            Perform baseline correction by

            - subtracting the mean of baseline values ('mean')
            - dividing by the mean of baseline values ('ratio')
            - dividing by the mean of baseline values and taking the log
              ('logratio')
            - subtracting the mean of baseline values followed by dividing by
              the mean of baseline values ('percent')
            - subtracting the mean of baseline values and dividing by the
              standard deviation of baseline values ('zscore')
            - dividing by the mean of baseline values, taking the log, and
              dividing by the standard deviation of log baseline values
              ('zlogratio')

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        ### ⏎ Returns
        -------
        inst : instance of AverageTFR
            The modified instance.
        """
        ...
    def save(self, fname, overwrite: bool = False, *, verbose=None) -> None:
        """### Save TFR object to hdf5 file.

        ### 🛠️ Parameters
        ----------
        fname : path-like
            The file name, which should end with ``-tfr.h5``.

        overwrite : bool
            If True (default False), overwrite the destination file if it
            exists.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        See Also
        --------
        read_tfrs, write_tfrs
        """
        ...
    def to_data_frame(
        self,
        picks=None,
        index=None,
        long_format: bool = False,
        time_format=None,
        *,
        verbose=None,
    ):
        """### Export data in tabular structure as a pandas DataFrame.

        Channels are converted to columns in the DataFrame. By default,
        additional columns ``'time'``, ``'freq'``, ``'epoch'``, and
        ``'condition'`` (epoch event description) are added, unless ``index``
        is not ``None`` (in which case the columns specified in ``index`` will
        be used to form the DataFrame's index instead). ``'epoch'``, and
        ``'condition'`` are not supported for ``AverageTFR``.

        ### 🛠️ Parameters
        ----------
        picks : str | array-like | slice | None
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel *type* strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick all channels. Note that channels in
            ``info['bads']`` *will be included* if their names or indices are
            explicitly provided.

        index : str | list of str | None
            Kind of index to use for the DataFrame. If ``None``, a sequential
            integer index (`pandas.RangeIndex`) will be used. If ``'time'``, a
            ``pandas.Index`` or `pandas.TimedeltaIndex` will be used
            (depending on the value of ``time_format``). If a list of two or more string values, a `pandas.MultiIndex` will be created.
            Valid string values are ``'time'``, ``'freq'``, ``'epoch'``, and
            ``'condition'`` for ``EpochsTFR`` and ``'time'`` and ``'freq'``
            for ``AverageTFR``.
            Defaults to ``None``.

        long_format : bool
            If True, the DataFrame is returned in long format where each row is one
            observation of the signal at a unique combination of time point, channel, epoch number, and condition.
            For convenience, a ``ch_type`` column is added to facilitate subsetting the resulting DataFrame. Defaults to ``False``.

        time_format : str | None
            Desired time format. If ``None``, no conversion is applied, and time values
            remain as float values in seconds. If ``'ms'``, time values will be rounded
            to the nearest millisecond and converted to integers. If ``'timedelta'``,
            time values will be converted to `pandas.Timedelta` values.
            Default is ``None``.

            ✨ Added in vesion 0.23

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        ### ⏎ Returns
        -------

        df : instance of pandas.DataFrame
            A dataframe suitable for usage with other statistical/plotting/analysis
            packages.
        """
        ...

class AverageTFR(_BaseTFR):
    """### Container for Time-Frequency data.

    Can for example store induced power at sensor level or inter-trial
    coherence.

    ### 🛠️ Parameters
    ----------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    data : ndarray, shape (n_channels, n_freqs, n_times)
        The data.
    times : ndarray, shape (n_times,)
        The time values in seconds.
    freqs : ndarray, shape (n_freqs,)
        The frequencies in Hz.
    nave : int
        The number of averaged TFRs.
    comment : str | None, default None
        Comment on the data, e.g., the experimental condition.
    method : str | None, default None
        Comment on the method used to compute the data, e.g., morlet wavelet.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### 📊 Attributes
    ----------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    ch_names : list
        The names of the channels.
    nave : int
        Number of averaged epochs.
    data : ndarray, shape (n_channels, n_freqs, n_times)
        The data array.
    times : ndarray, shape (n_times,)
        The time values in seconds.
    freqs : ndarray, shape (n_freqs,)
        The frequencies in Hz.
    comment : str
        Comment on dataset. Can be the condition.
    method : str | None, default None
        Comment on the method used to compute the data, e.g., morlet wavelet.
    """

    info: Incomplete
    data: Incomplete
    freqs: Incomplete
    nave: Incomplete
    comment: Incomplete
    method: Incomplete
    preload: bool

    def __init__(
        self, info, data, times, freqs, nave, comment=None, method=None, verbose=None
    ) -> None: ...
    def plot(
        self,
        picks=None,
        baseline=None,
        mode: str = "mean",
        tmin=None,
        tmax=None,
        fmin=None,
        fmax=None,
        vmin=None,
        vmax=None,
        cmap: str = "RdBu_r",
        dB: bool = False,
        colorbar: bool = True,
        show: bool = True,
        title=None,
        axes=None,
        layout=None,
        yscale: str = "auto",
        mask=None,
        mask_style=None,
        mask_cmap: str = "Greys",
        mask_alpha: float = 0.1,
        combine=None,
        exclude=[],
        cnorm=None,
        verbose=None,
    ):
        """### Plot TFRs as a two-dimensional image(s).

        ### 🛠️ Parameters
        ----------
        picks : str | array-like | slice | None
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel *type* strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick good data channels. Note that channels
            in ``info['bads']`` *will be included* if their names or indices are
            explicitly provided.
        baseline : None (default) or tuple, shape (2,)
            The time interval to apply baseline correction.
            If None do not apply it. If baseline is (a, b)
            the interval is between "a (s)" and "b (s)".
            If a is None the beginning of the data is used
            and if b is None then b is set to the end of the interval.
            If baseline is equal to (None, None) all the time
            interval is used.
        mode : 'mean' | 'ratio' | 'logratio' | 'percent' | 'zscore' | 'zlogratio'
            Perform baseline correction by

            - subtracting the mean of baseline values ('mean') (default)
            - dividing by the mean of baseline values ('ratio')
            - dividing by the mean of baseline values and taking the log
              ('logratio')
            - subtracting the mean of baseline values followed by dividing by
              the mean of baseline values ('percent')
            - subtracting the mean of baseline values and dividing by the
              standard deviation of baseline values ('zscore')
            - dividing by the mean of baseline values, taking the log, and
              dividing by the standard deviation of log baseline values
              ('zlogratio')

        tmin : None | float
            The first time instant to display. If None the first time point
            available is used. Defaults to None.
        tmax : None | float
            The last time instant to display. If None the last time point
            available is used. Defaults to None.
        fmin : None | float
            The first frequency to display. If None the first frequency
            available is used. Defaults to None.
        fmax : None | float
            The last frequency to display. If None the last frequency
            available is used. Defaults to None.
        vmin : float | None
            The minimum value an the color scale. If vmin is None, the data
            minimum value is used. Defaults to None.
        vmax : float | None
            The maximum value an the color scale. If vmax is None, the data
            maximum value is used. Defaults to None.
        cmap : matplotlib colormap | 'interactive' | (colormap, bool)
            The colormap to use. If tuple, the first value indicates the
            colormap to use and the second value is a boolean defining
            interactivity. In interactive mode the colors are adjustable by
            clicking and dragging the colorbar with left and right mouse
            button. Left mouse button moves the scale up and down and right
            mouse button adjusts the range. Hitting space bar resets the range.
            Up and down arrows can be used to change the colormap. If
            'interactive', translates to ('RdBu_r', True). Defaults to
            'RdBu_r'.

            ### ⛔️ Warning Interactive mode works smoothly only for a small
                amount of images.

        dB : bool
            If True, 10*log10 is applied to the data to get dB.
            Defaults to False.
        colorbar : bool
            If true, colorbar will be added to the plot. Defaults to True.
        show : bool
            Call pyplot.show() at the end. Defaults to True.
        title : str | 'auto' | None
            String for ``title``. Defaults to None (blank/no title). If
            'auto', and ``combine`` is None, the title for each figure
            will be the channel name. If 'auto' and ``combine`` is not None,
            ``title`` states how many channels were combined into that figure
            and the method that was used for ``combine``. If str, that String
            will be the title for each figure.
        axes : instance of Axes | list | None
            The axes to plot to. If list, the list must be a list of Axes of
            the same length as ``picks``. If instance of Axes, there must be
            only one channel plotted. If ``combine`` is not None, ``axes``
            must either be an instance of Axes, or a list of length 1.
        layout : Layout | None
            Layout instance specifying sensor positions. Used for interactive
            plotting of topographies on rectangle selection. If possible, the
            correct layout is inferred from the data.
        yscale : 'auto' (default) | 'linear' | 'log'
            The scale of y (frequency) axis. 'linear' gives linear y axis,
            'log' leads to log-spaced y axis and 'auto' detects if frequencies
            are log-spaced and only then sets the y axis to 'log'.

            ✨ Added in vesion 0.14.0
        mask : ndarray | None
            An array of booleans of the same shape as the data. Entries of the
            data that correspond to False in the mask are plotted
            transparently. Useful for, e.g., masking for statistical
            significance.

            ✨ Added in vesion 0.16.0
        mask_style : None | 'both' | 'contour' | 'mask'
            If ``mask`` is not None: if ``'contour'``, a contour line is drawn
            around the masked areas (``True`` in ``mask``). If ``'mask'``,
            entries not ``True`` in ``mask`` are shown transparently. If
            ``'both'``, both a contour and transparency are used.
            If ``None``, defaults to ``'both'`` if ``mask`` is not None, and is
            ignored otherwise.

            ✨ Added in vesion 0.17
        mask_cmap : matplotlib colormap | (colormap, bool) | 'interactive'
            The colormap chosen for masked parts of the image (see below), if
            ``mask`` is not ``None``. If None, ``cmap`` is reused. Defaults to
            ``'Greys'``. Not interactive. Otherwise, as ``cmap``.

            ✨ Added in vesion 0.17
        mask_alpha : float
            A float between 0 and 1. If ``mask`` is not None, this sets the
            alpha level (degree of transparency) for the masked-out segments.
            I.e., if 0, masked-out segments are not visible at all.
            Defaults to 0.1.

            ✨ Added in vesion 0.16.0
        combine : 'mean' | 'rms' | callable | None
            Type of aggregation to perform across selected channels. If
            None, plot one figure per selected channel. If a function, it must
            operate on an array of shape ``(n_channels, n_freqs, n_times)`` and
            return an array of shape ``(n_freqs, n_times)``.

            🎭 Changed in version 1.3
               Added support for ``callable``.
        exclude : list of str | 'bads'
            Channels names to exclude from being shown. If 'bads', the
            bad channels are excluded. Defaults to an empty list.

        cnorm : matplotlib.colors.Normalize | None
            How to normalize the colormap. If ``None``, standard linear normalization
            is performed. If not ``None``, ``vmin`` and ``vmax`` will be ignored.
            See `Matplotlib docs <matplotlib:colormapnorms>`
            for more details on colormap normalization, and
            `the ERDs example<cnorm-example>` for an example of its use.

            ✨ Added in vesion 0.24

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        ### ⏎ Returns
        -------
        figs : list of instances of matplotlib.figure.Figure
            A list of figures containing the time-frequency power.
        """
        ...
    def plot_joint(
        self,
        timefreqs=None,
        picks=None,
        baseline=None,
        mode: str = "mean",
        tmin=None,
        tmax=None,
        fmin=None,
        fmax=None,
        vmin=None,
        vmax=None,
        cmap: str = "RdBu_r",
        dB: bool = False,
        colorbar: bool = True,
        show: bool = True,
        title=None,
        yscale: str = "auto",
        combine: str = "mean",
        exclude=[],
        topomap_args=None,
        image_args=None,
        verbose=None,
    ):
        """### Plot TFRs as a two-dimensional image with topomaps.

        ### 🛠️ Parameters
        ----------
        timefreqs : None | list of tuple | dict of tuple
            The time-frequency point(s) for which topomaps will be plotted.
            See Notes.
        picks : str | array-like | slice | None
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel *type* strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick good data channels. Note that channels
            in ``info['bads']`` *will be included* if their names or indices are
            explicitly provided.
        baseline : None (default) or tuple of length 2
            The time interval to apply baseline correction.
            If None do not apply it. If baseline is (a, b)
            the interval is between "a (s)" and "b (s)".
            If a is None, the beginning of the data is used.
            If b is None, then b is set to the end of the interval.
            If baseline is equal to (None, None), the  entire time
            interval is used.
        mode : None | str
            If str, must be one of 'ratio', 'zscore', 'mean', 'percent',
            'logratio' and 'zlogratio'.
            Do baseline correction with ratio (power is divided by mean
            power during baseline) or zscore (power is divided by standard
            deviation of power during baseline after subtracting the mean,
            power = [power - mean(power_baseline)] / std(power_baseline)),
            mean simply subtracts the mean power, percent is the same as
            applying ratio then mean, logratio is the same as mean but then
            rendered in log-scale, zlogratio is the same as zscore but data
            is rendered in log-scale first.
            If None no baseline correction is applied.
        tmin, tmax : float | None
            First and last times to include, in seconds. ``None`` uses the first or
            last time present in the data. Default is ``tmin=None, tmax=None`` (all
            times).
        fmin, fmax : float
            The lower- and upper-bound on frequencies of interest. Default is ``fmin=0, fmax=np.inf`` (spans all frequencies present in the data).
        vmin : float | None
            The minimum value of the color scale for the image (for
            topomaps, see ``topomap_args``). If vmin is None, the data
            absolute minimum value is used.
        vmax : float | None
            The maximum value of the color scale for the image (for
            topomaps, see ``topomap_args``). If vmax is None, the data
            absolute maximum value is used.
        cmap : matplotlib colormap
            The colormap to use.
        dB : bool
            If True, 10*log10 is applied to the data to get dB.
        colorbar : bool
            If true, colorbar will be added to the plot (relating to the
            topomaps). For user defined axes, the colorbar cannot be drawn.
            Defaults to True.
        show : bool
            Call pyplot.show() at the end.
        title : str | None
            String for title. Defaults to None (blank/no title).
        yscale : 'auto' (default) | 'linear' | 'log'
            The scale of y (frequency) axis. 'linear' gives linear y axis,
            'log' leads to log-spaced y axis and 'auto' detects if frequencies
            are log-spaced and only then sets the y axis to 'log'.
        combine : 'mean' | 'rms' | callable
            Type of aggregation to perform across selected channels. If a
            function, it must operate on an array of shape
            ``(n_channels, n_freqs, n_times)`` and return an array of shape
            ``(n_freqs, n_times)``.

            🎭 Changed in version 1.3
               Added support for ``callable``.
        exclude : list of str | 'bads'
            Channels names to exclude from being shown. If 'bads', the
            bad channels are excluded. Defaults to an empty list, i.e., ``[]``.
        topomap_args : None | dict
            A dict of ``kwargs`` that are forwarded to
            `mne.viz.plot_topomap` to style the topomaps. ``axes`` and
            ``show`` are ignored. If ``times`` is not in this dict, automatic
            peak detection is used. Beyond that, if ``None``, no customizable
            arguments will be passed.
            Defaults to ``None``.
        image_args : None | dict
            A dict of ``kwargs`` that are forwarded to `AverageTFR.plot`
            to style the image. ``axes`` and ``show`` are ignored. Beyond that,
            if ``None``, no customizable arguments will be passed.
            Defaults to ``None``.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        ### ⏎ Returns
        -------
        fig : matplotlib.figure.Figure
            The figure containing the topography.

        ### 📖 Notes
        -----
        ``timefreqs`` has three different modes: tuples, dicts, and auto.
        For (list of) tuple(s) mode, each tuple defines a pair
        (time, frequency) in s and Hz on the TFR plot. For example, to
        look at 10 Hz activity 1 second into the epoch and 3 Hz activity
        300 msec into the epoch, ::

            timefreqs=((1, 10), (.3, 3))

        If provided as a dictionary, (time, frequency) tuples are keys and
        (time_window, frequency_window) tuples are the values - indicating the
        width of the windows (centered on the time and frequency indicated by
        the key) to be averaged over. For example, ::

            timefreqs={(1, 10): (0.1, 2)}

        would translate into a window that spans 0.95 to 1.05 seconds, as
        well as 9 to 11 Hz. If None, a single topomap will be plotted at the
        absolute peak across the time-frequency representation.

        ✨ Added in vesion 0.16.0
        """
        ...
    def plot_topo(
        self,
        picks=None,
        baseline=None,
        mode: str = "mean",
        tmin=None,
        tmax=None,
        fmin=None,
        fmax=None,
        vmin=None,
        vmax=None,
        layout=None,
        cmap: str = "RdBu_r",
        title=None,
        dB: bool = False,
        colorbar: bool = True,
        layout_scale: float = 0.945,
        show: bool = True,
        border: str = "none",
        fig_facecolor: str = "k",
        fig_background=None,
        font_color: str = "w",
        yscale: str = "auto",
        verbose=None,
    ):
        """### Plot TFRs in a topography with images.

        ### 🛠️ Parameters
        ----------
        picks : str | array-like | slice | None
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel *type* strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick good data channels. Note that channels
            in ``info['bads']`` *will be included* if their names or indices are
            explicitly provided.
        baseline : None (default) or tuple of length 2
            The time interval to apply baseline correction.
            If None do not apply it. If baseline is (a, b)
            the interval is between "a (s)" and "b (s)".
            If a is None the beginning of the data is used
            and if b is None then b is set to the end of the interval.
            If baseline is equal to (None, None) all the time
            interval is used.
        mode : 'mean' | 'ratio' | 'logratio' | 'percent' | 'zscore' | 'zlogratio'
            Perform baseline correction by

            - subtracting the mean of baseline values ('mean')
            - dividing by the mean of baseline values ('ratio')
            - dividing by the mean of baseline values and taking the log
              ('logratio')
            - subtracting the mean of baseline values followed by dividing by
              the mean of baseline values ('percent')
            - subtracting the mean of baseline values and dividing by the
              standard deviation of baseline values ('zscore')
            - dividing by the mean of baseline values, taking the log, and
              dividing by the standard deviation of log baseline values
              ('zlogratio')

        tmin : None | float
            The first time instant to display. If None the first time point
            available is used.
        tmax : None | float
            The last time instant to display. If None the last time point
            available is used.
        fmin : None | float
            The first frequency to display. If None the first frequency
            available is used.
        fmax : None | float
            The last frequency to display. If None the last frequency
            available is used.
        vmin : float | None
            The minimum value of the color scale. If vmin is None, the data
            minimum value is used.
        vmax : float | None
            The maximum value of the color scale. If vmax is None, the data
            maximum value is used.
        layout : Layout | None
            Layout instance specifying sensor positions. If possible, the
            correct layout is inferred from the data.
        cmap : matplotlib colormap | str
            The colormap to use. Defaults to 'RdBu_r'.
        title : str
            Title of the figure.
        dB : bool
            If True, 10*log10 is applied to the data to get dB.
        colorbar : bool
            If true, colorbar will be added to the plot.
        layout_scale : float
            Scaling factor for adjusting the relative size of the layout
            on the canvas.
        show : bool
            Call pyplot.show() at the end.
        border : str
            Matplotlib borders style to be used for each sensor plot.
        fig_facecolor : color
            The figure face color. Defaults to black.
        fig_background : None | array
            A background image for the figure. This must be a valid input to
            `matplotlib.pyplot.imshow`. Defaults to None.
        font_color : color
            The color of tick labels in the colorbar. Defaults to white.
        yscale : 'auto' (default) | 'linear' | 'log'
            The scale of y (frequency) axis. 'linear' gives linear y axis,
            'log' leads to log-spaced y axis and 'auto' detects if frequencies
            are log-spaced and only then sets the y axis to 'log'.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        ### ⏎ Returns
        -------
        fig : matplotlib.figure.Figure
            The figure containing the topography.
        """
        ...
    def plot_topomap(
        self,
        tmin=None,
        tmax=None,
        fmin: float = 0.0,
        fmax=...,
        *,
        ch_type=None,
        baseline=None,
        mode: str = "mean",
        sensors: bool = True,
        show_names: bool = False,
        mask=None,
        mask_params=None,
        contours: int = 6,
        outlines: str = "head",
        sphere=None,
        image_interp="cubic",
        extrapolate="auto",
        border="mean",
        res: int = 64,
        size: int = 2,
        cmap=None,
        vlim=(None, None),
        cnorm=None,
        colorbar: bool = True,
        cbar_fmt: str = "%1.1e",
        units=None,
        axes=None,
        show: bool = True,
    ):
        """### Plot topographic maps of specific time-frequency intervals of TFR data.

        ### 🛠️ Parameters
        ----------
        tmin, tmax : float | None
            First and last times to include, in seconds. ``None`` uses the first or
            last time present in the data. Default is ``tmin=None, tmax=None`` (all
            times).
        fmin, fmax : float
            The lower- and upper-bound on frequencies of interest. Default is ``fmin=0, fmax=np.inf`` (spans all frequencies present in the data).
        ch_type : 'mag' | 'grad' | 'planar1' | 'planar2' | 'eeg' | None
            The channel type to plot. For ``'grad'``, the gradiometers are
            collected in pairs and the mean for each pair is plotted. If
            ``None`` the first available channel type from order shown above is used. Defaults to ``None``.
        baseline : tuple or list of length 2
            The time interval to apply rescaling / baseline correction. If None do
            not apply it. If baseline is (a, b) the interval is between "a (s)" and
            "b (s)". If a is None the beginning of the data is used and if b is
            None then b is set to the end of the interval. If baseline is equal to
            (None, None) the whole time interval is used.
        mode : 'mean' | 'ratio' | 'logratio' | 'percent' | 'zscore' | 'zlogratio' | None
            Perform baseline correction by

              - subtracting the mean baseline power ('mean')
              - dividing by the mean baseline power ('ratio')
              - dividing by the mean baseline power and taking the log ('logratio')
              - subtracting the mean baseline power followed by dividing by the
                mean baseline power ('percent')
              - subtracting the mean baseline power and dividing by the standard
                deviation of the baseline power ('zscore')
              - dividing by the mean baseline power, taking the log, and dividing
                by the standard deviation of the baseline power ('zlogratio')

            If None no baseline correction is applied.

        sensors : bool | str
            Whether to add markers for sensor locations. If `str`, should be a
            valid matplotlib format string (e.g., ``'r+'`` for red plusses, see the
            Notes section of `matplotlib.axes.Axes.plot`). If ``True`` (the
            default), black circles will be used.

        show_names : bool | callable
            If ``True``, show channel names next to each sensor marker. If callable,
            channel names will be formatted using the callable; e.g., to
            delete the prefix 'MEG ' from all channel names, pass the function
            ``lambda x: x.replace('MEG ', '')``. If ``mask`` is not ``None``, only
            non-masked sensor names will be shown.

        mask : ndarray of bool, shape (n_channels, n_times) | None
            Array indicating channel-time combinations to highlight with a distinct
            plotting style (useful for, e.g. marking which channels at which times a statistical test of the data reaches significance). Array elements set to ``True`` will be plotted
            with the parameters given in ``mask_params``. Defaults to ``None``,
            equivalent to an array of all ``False`` elements.

        mask_params : dict | None
            Additional plotting parameters for plotting significant sensors.
            Default (None) equals::

                dict(marker='o', markerfacecolor='w', markeredgecolor='k',
                        linewidth=0, markersize=4)

        contours : int | array-like
            The number of contour lines to draw. If ``0``, no contours will be drawn.
            If a positive integer, that number of contour levels are chosen using the
            matplotlib tick locator (may sometimes be inaccurate, use array for
            accuracy). If array-like, the array values are used as the contour levels.
            The values should be in µV for EEG, fT for magnetometers and fT/m for
            gradiometers. If ``colorbar=True``, the colorbar will have ticks
            corresponding to the contour levels. Default is ``6``.

        outlines : 'head' | dict | None
            The outlines to be drawn. If 'head', the default head scheme will be
            drawn. If dict, each key refers to a tuple of x and y positions, the values
            in 'mask_pos' will serve as image mask.
            Alternatively, a matplotlib patch object can be passed for advanced
            masking options, either directly or as a function that returns patches
            (required for multi-axis plots). If None, nothing will be drawn.
            Defaults to 'head'.
        sphere : float | array-like | instance of ConductorModel | None  | 'auto' | 'eeglab'
            The sphere parameters to use for the head outline. Can be array-like of
            shape (4,) to give the X/Y/Z origin and radius in meters, or a single float
            to give just the radius (origin assumed 0, 0, 0). Can also be an instance
            of a spherical `mne.bem.ConductorModel` to use the origin and
            radius from that object. If ``'auto'`` the sphere is fit to digitization
            points. If ``'eeglab'`` the head circle is defined by EEG electrodes
            ``'Fpz'``, ``'Oz'``, ``'T7'``, and ``'T8'`` (if ``'Fpz'`` is not present,
            it will be approximated from the coordinates of ``'Oz'``). ``None`` (the
            default) is equivalent to ``'auto'`` when enough extra digitization points
            are available, and (0, 0, 0, 0.095) otherwise.

            ✨ Added in vesion 0.20
            🎭 Changed in version 1.1 Added ``'eeglab'`` option.

        image_interp : str
            The image interpolation to be used. Options are ``'cubic'`` (default)
            to use `scipy.interpolate.CloughTocher2DInterpolator`,
            ``'nearest'`` to use `scipy.spatial.Voronoi` or
            ``'linear'`` to use `scipy.interpolate.LinearNDInterpolator`.

        extrapolate : str
            Options:

            - ``'box'``
                Extrapolate to four points placed to form a square encompassing all
                data points, where each side of the square is three times the range
                of the data in the respective dimension.
            - ``'local'`` (default for MEG sensors)
                Extrapolate only to nearby points (approximately to points closer than
                median inter-electrode distance). This will also set the
                mask to be polygonal based on the convex hull of the sensors.
            - ``'head'`` (default for non-MEG sensors)
                Extrapolate out to the edges of the clipping circle. This will be on
                the head circle when the sensors are contained within the head circle,
                but it can extend beyond the head when sensors are plotted outside
                the head circle.

            🎭 Changed in version 0.21

               - The default was changed to ``'local'`` for MEG sensors.
               - ``'local'`` was changed to use a convex hull mask
               - ``'head'`` was changed to extrapolate out to the clipping circle.

        border : float | 'mean'
            Value to extrapolate to on the topomap borders. If ``'mean'`` (default),
            then each extrapolated point has the average value of its neighbours.

            ✨ Added in vesion 0.20

        res : int
            The resolution of the topomap image (number of pixels along each side).

        size : float
            Side length of each subplot in inches.

        cmap : matplotlib colormap | (colormap, bool) | 'interactive' | None
            Colormap to use. If `tuple`, the first value indicates the colormap
            to use and the second value is a boolean defining interactivity. In
            interactive mode the colors are adjustable by clicking and dragging the
            colorbar with left and right mouse button. Left mouse button moves the
            scale up and down and right mouse button adjusts the range. Hitting
            space bar resets the range. Up and down arrows can be used to change
            the colormap. If ``None``, ``'Reds'`` is used for data that is either
            all-positive or all-negative, and ``'RdBu_r'`` is used otherwise.
            ``'interactive'`` is equivalent to ``(None, True)``. Defaults to ``None``.

            ### ⛔️ Warning  Interactive mode works smoothly only for a small amount
                of topomaps. Interactive mode is disabled by default for more than
                2 topomaps.

        vlim : tuple of length 2
            Colormap limits to use. If a `tuple` of floats, specifies the
            lower and upper bounds of the colormap (in that order); providing
            ``None`` for either entry will set the corresponding boundary at the
            min/max of the data. Defaults to ``(None, None)``.

            ✨ Added in vesion 1.2

        cnorm : matplotlib.colors.Normalize | None
            How to normalize the colormap. If ``None``, standard linear normalization
            is performed. If not ``None``, ``vmin`` and ``vmax`` will be ignored.
            See `Matplotlib docs <matplotlib:colormapnorms>`
            for more details on colormap normalization, and
            `the ERDs example<cnorm-example>` for an example of its use.

            ✨ Added in vesion 1.2

        colorbar : bool
            Plot a colorbar in the rightmost column of the figure.
        cbar_fmt : str
            Formatting string for colorbar tick labels. See `formatspec` for
            details.

        units : str | None
            The units to use for the colorbar label. Ignored if ``colorbar=False``.
            If ``None`` the label will be "AU" indicating arbitrary units.
            Default is ``None``.
        axes : instance of Axes | None
            The axes to plot to. If ``None``, a new `matplotlib.figure.Figure`
            will be created. Default is ``None``.
        show : bool
            Show the figure if ``True``.

        ### ⏎ Returns
        -------
        fig : matplotlib.figure.Figure
            The figure containing the topography.
        """
        ...
    def __add__(self, tfr):
        """### Add instances."""
        ...
    def __iadd__(self, tfr): ...
    def __sub__(self, tfr):
        """### Subtract instances."""
        ...
    def __isub__(self, tfr): ...
    def __truediv__(self, a):
        """### Divide instances."""
        ...
    def __itruediv__(self, a): ...
    def __mul__(self, a):
        """### Multiply source instances."""
        ...
    def __imul__(self, a): ...

class EpochsTFR(_BaseTFR, GetEpochsMixin):
    """### Container for Time-Frequency data on epochs.

    Can for example store induced power at sensor level.

    ### 🛠️ Parameters
    ----------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    data : ndarray, shape (n_epochs, n_channels, n_freqs, n_times)
        The data.
    times : ndarray, shape (n_times,)
        The time values in seconds.
    freqs : ndarray, shape (n_freqs,)
        The frequencies in Hz.
    comment : str | None, default None
        Comment on the data, e.g., the experimental condition.
    method : str | None, default None
        Comment on the method used to compute the data, e.g., morlet wavelet.
    events : ndarray, shape (n_events, 3) | None
        The events as stored in the Epochs class. If None (default), all event
        values are set to 1 and event time-samples are set to range(n_epochs).
    event_id : dict | None
        Example: dict(auditory=1, visual=3). They keys can be used to access
        associated events. If None, all events will be used and a dict is
        created with string integer names corresponding to the event id
        integers.
    selection : iterable | None
        Iterable of indices of selected epochs. If ``None``, will be
        automatically generated, corresponding to all non-zero events.

        ✨ Added in vesion 0.23
    drop_log : tuple | None
        Tuple of tuple of strings indicating which epochs have been marked to
        be ignored.

        ✨ Added in vesion 0.23
    metadata : instance of pandas.DataFrame | None
        A `pandas.DataFrame` containing pertinent information for each
        trial. See `mne.Epochs` for further details.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### 📊 Attributes
    ----------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    ch_names : list
        The names of the channels.
    data : ndarray, shape (n_epochs, n_channels, n_freqs, n_times)
        The data array.
    times : ndarray, shape (n_times,)
        The time values in seconds.
    freqs : ndarray, shape (n_freqs,)
        The frequencies in Hz.
    comment : string
        Comment on dataset. Can be the condition.
    method : str | None, default None
        Comment on the method used to compute the data, e.g., morlet wavelet.
    events : ndarray, shape (n_events, 3) | None
        Array containing sample information as event_id
    event_id : dict | None
        Names of conditions correspond to event_ids
    selection : array
        List of indices of selected events (not dropped or ignored etc.). For
        example, if the original event array had 4 events and the second event
        has been dropped, this attribute would be np.array([0, 2, 3]).
    drop_log : tuple of tuple
        A tuple of the same length as the event array used to initialize the
        ``EpochsTFR`` object. If the i-th original event is still part of the
        selection, drop_log[i] will be an empty tuple; otherwise it will be
        a tuple of the reasons the event is not longer in the selection, e.g.:

        - ``'IGNORED'``
            If it isn't part of the current subset defined by the user
        - ``'NO_DATA'`` or ``'TOO_SHORT'``
            If epoch didn't contain enough data names of channels that
            exceeded the amplitude threshold
        - ``'EQUALIZED_COUNTS'``
            See `mne.Epochs.equalize_event_counts`
        - ``'USER'``
            For user-defined reasons (see `mne.Epochs.drop`).

    metadata : pandas.DataFrame, shape (n_events, n_cols) | None
        DataFrame containing pertinent information for each trial

    ### 📖 Notes
    -----
    ✨ Added in vesion 0.13.0
    """

    info: Incomplete
    data: Incomplete
    freqs: Incomplete
    events: Incomplete
    event_id: Incomplete
    selection: Incomplete
    drop_log: Incomplete
    comment: Incomplete
    method: Incomplete
    preload: bool
    metadata: Incomplete

    def __init__(
        self,
        info,
        data,
        times,
        freqs,
        comment=None,
        method=None,
        events=None,
        event_id=None,
        selection=None,
        drop_log=None,
        metadata=None,
        verbose=None,
    ) -> None: ...
    def __abs__(self):
        """### Take the absolute value."""
        ...
    def average(self, method: str = "mean", dim: str = "epochs", copy: bool = False):
        """### Average the data across epochs.

        ### 🛠️ Parameters
        ----------
        method : str | callable
            How to combine the data. If "mean"/"median", the mean/median
            are returned. Otherwise, must be a callable which, when passed
            an array of shape (n_epochs, n_channels, n_freqs, n_time)
            returns an array of shape (n_channels, n_freqs, n_time).
            Note that due to file type limitations, the kind for all
            these will be "average".
        dim : 'epochs' | 'freqs' | 'times'
            The dimension along which to combine the data.
        copy : bool
            Whether to return a copy of the modified instance,
            or modify in place. Ignored when ``dim='epochs'``
            because a new instance must be returned.

        ### ⏎ Returns
        -------
        ave : instance of AverageTFR | EpochsTFR
            The averaged data.

        ### 📖 Notes
        -----
        Passing in ``np.median`` is considered unsafe when there is complex
        data because NumPy doesn't compute the marginal median. Numpy currently
        sorts the complex values by real part and return whatever value is
        computed. Use with caution. We use the marginal median in the
        complex case (i.e. the median of each component separately) if
        one passes in ``median``. See a discussion in scipy:

        https://github.com/scipy/scipy/pull/12676#issuecomment-783370228
        """
        ...

def combine_tfr(all_tfr, weights: str = "nave"):
    """### Merge AverageTFR data by weighted addition.

    Create a new AverageTFR instance, using a combination of the supplied
    instances as its data. By default, the mean (weighted by trials) is used.
    Subtraction can be performed by passing negative weights (e.g., [1, -1]).
    Data must have the same channels and the same time instants.

    ### 🛠️ Parameters
    ----------
    all_tfr : list of AverageTFR
        The tfr datasets.
    weights : list of float | str
        The weights to apply to the data of each AverageTFR instance.
        Can also be ``'nave'`` to weight according to tfr.nave,
        or ``'equal'`` to use equal weighting (each weighted as ``1/N``).

    ### ⏎ Returns
    -------
    tfr : AverageTFR
        The new TFR data.

    ### 📖 Notes
    -----
    ✨ Added in vesion 0.11.0
    """
    ...

def write_tfrs(fname, tfr, overwrite: bool = False, *, verbose=None) -> None:
    """### Write a TFR dataset to hdf5.

    ### 🛠️ Parameters
    ----------
    fname : path-like
        The file name, which should end with ``-tfr.h5``.
    tfr : AverageTFR | list of AverageTFR | EpochsTFR
        The TFR dataset, or list of TFR datasets, to save in one file.
        Note. If .comment is not None, a name will be generated on the fly,
        based on the order in which the TFR objects are passed.

    overwrite : bool
        If True (default False), overwrite the destination file if it
        exists.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    read_tfrs

    ### 📖 Notes
    -----
    ✨ Added in vesion 0.9.0
    """
    ...

def read_tfrs(fname, condition=None, *, verbose=None):
    """### Read TFR datasets from hdf5 file.

    ### 🛠️ Parameters
    ----------
    fname : path-like
        The file name, which should end with -tfr.h5 .
    condition : int or str | list of int or str | None
        The condition to load. If None, all conditions will be returned.
        Defaults to None.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    tfr : AverageTFR | list of AverageTFR | EpochsTFR
        Depending on ``condition`` either the TFR object or a list of multiple
        TFR objects.

    See Also
    --------
    write_tfrs

    ### 📖 Notes
    -----
    ✨ Added in vesion 0.9.0
    """
    ...
