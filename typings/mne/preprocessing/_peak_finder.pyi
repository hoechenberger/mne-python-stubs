from ..utils import logger as logger

def peak_finder(x0, thresh=None, extrema: int = 1, verbose=None):
    """Noise-tolerant fast peak-finding algorithm.

    Parameters
    ----------
    x0 : 1d array
        A real vector from the maxima will be found (required).
    thresh : float | None
        The amount above surrounding data for a peak to be
        identified. Larger values mean the algorithm is more selective in
        finding peaks. If ``None``, use the default of
        ``(max(x0) - min(x0)) / 4``.
    extrema : {-1, 1}
        1 if maxima are desired, -1 if minima are desired
        (default = maxima, 1).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    peak_loc : array
        The indices of the identified peaks in x0.
    peak_mag : array
        The magnitude of the identified peaks.

    Notes
    -----
    If repeated values are found the first is identified as the peak.
    Conversion from initial Matlab code from:
    Nathanael C. Yoder (ncyoder@purdue.edu)

    Examples
    --------
    >>> import numpy as np
    >>> from mne.preprocessing import peak_finder
    >>> t = np.arange(0, 3, 0.01)
    >>> x = np.sin(np.pi*t) - np.sin(0.5*np.pi*t)
    >>> peak_locs, peak_mags = peak_finder(x) # doctest: +SKIP
    >>> peak_locs # doctest: +SKIP
    array([36, 260]) # doctest: +SKIP
    >>> peak_mags # doctest: +SKIP
    array([0.36900026, 1.76007351]) # doctest: +SKIP
    """
    ...
