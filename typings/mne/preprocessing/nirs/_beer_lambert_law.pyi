from ..._fiff.constants import FIFF as FIFF
from ...io import BaseRaw as BaseRaw
from ...utils import warn as warn
from ..nirs import source_detector_distances as source_detector_distances

def beer_lambert_law(raw, ppf: float=...):
    """Convert NIRS optical density data to haemoglobin concentration.

    Parameters
    ----------
    raw : instance of Raw
        The optical density data.
    ppf : float
        The partial pathlength factor.

    Returns
    -------
    raw : instance of Raw
        The modified raw instance.
    """