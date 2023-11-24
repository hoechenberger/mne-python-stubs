from ..bem import fit_sphere_to_headshape as fit_sphere_to_headshape
from ..io import read_raw_fif as read_raw_fif
from ..utils import deprecated as deprecated, logger as logger, verbose as verbose, warn as warn
from _typeshed import Incomplete

def apply_maxfilter(in_fname, out_fname, origin: Incomplete | None=..., frame: str=..., bad: Incomplete | None=..., autobad: str=..., skip: Incomplete | None=..., force: bool=..., st: bool=..., st_buflen: float=..., st_corr: float=..., mv_trans: Incomplete | None=..., mv_comp: bool=..., mv_headpos: bool=..., mv_hp: Incomplete | None=..., mv_hpistep: Incomplete | None=..., mv_hpisubt: Incomplete | None=..., mv_hpicons: bool=..., linefreq: Incomplete | None=..., cal: Incomplete | None=..., ctc: Incomplete | None=..., mx_args: str=..., overwrite: bool=..., verbose: Incomplete | None=...):
    """.. warning:: DEPRECATED: apply_maxfilter will be removed in 1.7, use mne.preprocessing.maxwell_filter or the MEGIN command-line utility maxfilter and mne.bem.fit_sphere_to_headshape instead..

    Apply NeuroMag MaxFilter to raw data.

    Needs Maxfilter license, maxfilter has to be in PATH.

    Parameters
    ----------
    in_fname : path-like
        Input file name.
    out_fname : path-like
        Output file name.
    origin : array-like or str
        Head origin in mm. If None it will be estimated from headshape points.
    frame : ``'device'`` | ``'head'``
        Coordinate frame for head center.
    bad : str, list (or None)
        List of static bad channels. Can be a list with channel names, or a
        string with channels (names or logical channel numbers).
    autobad : str ('on', 'off', 'n')
        Sets automated bad channel detection on or off.
    skip : str or a list of float-tuples (or None)
        Skips raw data sequences, time intervals pairs in s,
        e.g.: 0 30 120 150.
    force : bool
        Ignore program warnings.
    st : bool
        Apply the time-domain MaxST extension.
    st_buflen : float
        MaxSt buffer length in s (disabled if st is False).
    st_corr : float
        MaxSt subspace correlation limit (disabled if st is False).
    mv_trans : str (filename or 'default') (or None)
        Transforms the data into the coil definitions of in_fname, or into the
        default frame (None: don't use option).
    mv_comp : bool (or 'inter')
        Estimates and compensates head movements in continuous raw data.
    mv_headpos : bool
        Estimates and stores head position parameters, but does not compensate
        movements (disabled if mv_comp is False).
    mv_hp : str (or None)
        Stores head position data in an ascii file
        (disabled if mv_comp is False).
    mv_hpistep : float (or None)
        Sets head position update interval in ms (disabled if mv_comp is
        False).
    mv_hpisubt : str ('amp', 'base', 'off') (or None)
        Subtracts hpi signals: sine amplitudes, amp + baseline, or switch off
        (disabled if mv_comp is False).
    mv_hpicons : bool
        Check initial consistency isotrak vs hpifit
        (disabled if mv_comp is False).
    linefreq : int (50, 60) (or None)
        Sets the basic line interference frequency (50 or 60 Hz)
        (None: do not use line filter).
    cal : str
        Path to calibration file.
    ctc : str
        Path to Cross-talk compensation file.
    mx_args : str
        Additional command line arguments to pass to MaxFilter.
    
    overwrite : bool
        If True (default False), overwrite the destination file if it
        exists.
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    origin: str
        Head origin in selected coordinate frame.
    """