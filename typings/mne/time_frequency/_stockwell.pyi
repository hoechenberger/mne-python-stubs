from .._fiff.pick import pick_info as pick_info
from ..parallel import parallel_func as parallel_func
from ..utils import fill_doc as fill_doc, logger as logger
from .tfr import AverageTFR as AverageTFR

def tfr_array_stockwell(
    data,
    sfreq,
    fmin=None,
    fmax=None,
    n_fft=None,
    width: float = 1.0,
    decim: int = 1,
    return_itc: bool = False,
    n_jobs=None,
):
    """Compute power and intertrial coherence using Stockwell (S) transform.

    Same computation as `tfr_stockwell`, but operates on
    `NumPy arrays <numpy.ndarray>` instead of `Epochs` objects.

    See `Stockwell2007,MoukademEtAl2014,WheatEtAl2010,JonesEtAl2006`
    for more information.

    Parameters
    ----------
    data : ndarray, shape (n_epochs, n_channels, n_times)
        The signal to transform.
    sfreq : float
        The sampling frequency.
    fmin : None, float
        The minimum frequency to include. If None defaults to the minimum fft
        frequency greater than zero.
    fmax : None, float
        The maximum frequency to include. If None defaults to the maximum fft.
    n_fft : int | None
        The length of the windows used for FFT. If None, it defaults to the
        next power of 2 larger than the signal length.
    width : float
        The width of the Gaussian window. If < 1, increased temporal
        resolution, if > 1, increased frequency resolution. Defaults to 1.
        (classical S-Transform).
    decim : int
        The decimation factor on the time axis. To reduce memory usage.
    return_itc : bool
        Return intertrial coherence (ITC) as well as averaged power.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.

    Returns
    -------
    st_power : ndarray
        The multitaper power of the Stockwell transformed data.
        The last two dimensions are frequency and time.
    itc : ndarray
        The intertrial coherence. Only returned if return_itc is True.
    freqs : ndarray
        The frequencies.

    See Also
    --------
    mne.time_frequency.tfr_stockwell
    mne.time_frequency.tfr_multitaper
    mne.time_frequency.tfr_array_multitaper
    mne.time_frequency.tfr_morlet
    mne.time_frequency.tfr_array_morlet

    References
    ----------
    .. footbibliography::
    """
    ...

def tfr_stockwell(
    inst,
    fmin=None,
    fmax=None,
    n_fft=None,
    width: float = 1.0,
    decim: int = 1,
    return_itc: bool = False,
    n_jobs=None,
    verbose=None,
):
    """Compute Time-Frequency Representation (TFR) using Stockwell Transform.

    Same computation as `tfr_array_stockwell`, but operates
    on `Epochs` objects instead of `NumPy arrays <numpy.ndarray>`.

    See `Stockwell2007,MoukademEtAl2014,WheatEtAl2010,JonesEtAl2006`
    for more information.

    Parameters
    ----------
    inst : Epochs | Evoked
        The epochs or evoked object.
    fmin : None, float
        The minimum frequency to include. If None defaults to the minimum fft
        frequency greater than zero.
    fmax : None, float
        The maximum frequency to include. If None defaults to the maximum fft.
    n_fft : int | None
        The length of the windows used for FFT. If None, it defaults to the
        next power of 2 larger than the signal length.
    width : float
        The width of the Gaussian window. If < 1, increased temporal
        resolution, if > 1, increased frequency resolution. Defaults to 1.
        (classical S-Transform).
    decim : int
        The decimation factor on the time axis. To reduce memory usage.
    return_itc : bool
        Return intertrial coherence (ITC) as well as averaged power.
    n_jobs : int
        The number of jobs to run in parallel (over channels).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    power : AverageTFR
        The averaged power.
    itc : AverageTFR
        The intertrial coherence. Only returned if return_itc is True.

    See Also
    --------
    mne.time_frequency.tfr_array_stockwell
    mne.time_frequency.tfr_multitaper
    mne.time_frequency.tfr_array_multitaper
    mne.time_frequency.tfr_morlet
    mne.time_frequency.tfr_array_morlet

    Notes
    -----
    ✨ Added in version 0.9.0

    References
    ----------
    .. footbibliography::
    """
    ...
