from ...channels.montage import (
    read_custom_montage as read_custom_montage,
    read_dig_polhemus_isotrak as read_dig_polhemus_isotrak,
    read_polhemus_fastscan as read_polhemus_fastscan,
)
from ...transforms import (
    Transform as Transform,
    als_ras_trans as als_ras_trans,
    apply_trans as apply_trans,
    get_ras_to_neuromag_trans as get_ras_to_neuromag_trans,
)
from ...utils import warn as warn
from .constants import FIFF as FIFF, KIT as KIT

INT32: str
FLOAT64: str

def read_mrk(fname):
    """Marker Point Extraction in MEG space directly from sqd.

    Parameters
    ----------
    fname : path-like
        Absolute path to Marker file.
        File formats allowed: \\*.sqd, \\*.mrk, \\*.txt.

    Returns
    -------
    mrk_points : ndarray, shape (n_points, 3)
        Marker points in MEG space [m].
    """
    ...

def read_sns(fname):
    """Sensor coordinate extraction in MEG space.

    Parameters
    ----------
    fname : path-like
        Absolute path to sensor definition file.

    Returns
    -------
    locs : numpy.array, shape = (n_points, 3)
        Sensor coil location.
    """
    ...
