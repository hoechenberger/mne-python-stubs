from .._fiff.pick import (
    pick_channels as pick_channels,
    pick_channels_forward as pick_channels_forward,
    pick_info as pick_info,
)
from ..evoked import EvokedArray as EvokedArray
from ..utils import fill_doc as fill_doc, logger as logger
from ._lcmv import apply_lcmv as apply_lcmv

def make_lcmv_resolution_matrix(filters, forward, info):
    """Compute resolution matrix for LCMV beamformer.

    Parameters
    ----------
    filters : instance of Beamformer
         Dictionary containing filter weights from LCMV beamformer
         (see mne.beamformer.make_lcmv).
    forward : instance of Forward
        Forward Solution with leadfield matrix.

    info : mne.Info
        The :class:`mne.Info` object with information about the sensors and methods of measurement. Used to compute LCMV filters.

    Returns
    -------
    resmat : array, shape (n_dipoles_lcmv, n_dipoles_fwd)
        Resolution matrix (filter matrix multiplied to leadfield from
        forward solution). Numbers of rows (n_dipoles_lcmv) and columns
        (n_dipoles_fwd) may differ by a factor depending on orientation
        constraints of filter and forward solution, respectively (e.g. factor 3
        for free dipole orientation versus factor 1 for scalar beamformers).
    """
    ...
