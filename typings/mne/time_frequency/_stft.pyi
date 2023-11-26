from ..utils import logger as logger

def stft(x, wsize, tstep=None, verbose=None):
    """STFT Short-Term Fourier Transform using a sine window.

    The transformation is designed to be a tight frame that can be
    perfectly inverted. It only returns the positive frequencies.

    Parameters
    ----------
    x : array, shape (n_signals, n_times)
        Containing multi-channels signal.
    wsize : int
        Length of the STFT window in samples (must be a multiple of 4).
    tstep : int
        Step between successive windows in samples (must be a multiple of 2,
        a divider of wsize and smaller than wsize/2) (default: wsize/2).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    X : array, shape (n_signals, wsize // 2 + 1, n_step)
        STFT coefficients for positive frequencies with
        ``n_step = ceil(T / tstep)``.

    See Also
    --------
    istft
    stftfreq
    """
    ...

def istft(X, tstep=None, Tx=None):
    """ISTFT Inverse Short-Term Fourier Transform using a sine window.

    Parameters
    ----------
    X : array, shape (..., wsize / 2 + 1, n_step)
        The STFT coefficients for positive frequencies.
    tstep : int
        Step between successive windows in samples (must be a multiple of 2,
        a divider of wsize and smaller than wsize/2) (default: wsize/2).
    Tx : int
        Length of returned signal. If None Tx = n_step * tstep.

    Returns
    -------
    x : array, shape (Tx,)
        Array containing the inverse STFT signal.

    See Also
    --------
    stft
    """
    ...

def stftfreq(wsize, sfreq=None):
    """Compute frequencies of stft transformation.

    Parameters
    ----------
    wsize : int
        Size of stft window.
    sfreq : float
        Sampling frequency. If None the frequencies are given between 0 and pi
        otherwise it's given in Hz.

    Returns
    -------
    freqs : array
        The positive frequencies returned by stft.

    See Also
    --------
    stft
    istft
    """
    ...

def stft_norm2(X):
    """Compute L2 norm of STFT transform.

    It takes into account that stft only return positive frequencies.
    As we use tight frame this quantity is conserved by the stft.

    Parameters
    ----------
    X : 3D complex array
        The STFT transforms

    Returns
    -------
    norms2 : array
        The squared L2 norm of every row of X.
    """
    ...

def stft_norm1(X):
    """Compute L1 norm of STFT transform.

    It takes into account that stft only return positive frequencies.

    Parameters
    ----------
    X : 3D complex array
        The STFT transforms

    Returns
    -------
    norms : array
        The L1 norm of every row of X.
    """
    ...
