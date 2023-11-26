def parse_config(fname):
    """Parse a config file (like .ave and .cov files).

    Parameters
    ----------
    fname : path-like
        Config file name.

    Returns
    -------
    conditions : list of dict
        Each condition is indexed by the event type.
        A condition contains as keys::

            tmin, tmax, name, grad_reject, mag_reject,
            eeg_reject, eog_reject
    """
    ...

def read_reject_parameters(fname):
    """Read rejection parameters from .cov or .ave config file.

    Parameters
    ----------
    fname : path-like
        Filename to read.

    Returns
    -------
    params : dict
        The rejection parameters.
    """
    ...

def read_flat_parameters(fname):
    """Read flat channel rejection parameters from .cov or .ave config file."""
    ...
