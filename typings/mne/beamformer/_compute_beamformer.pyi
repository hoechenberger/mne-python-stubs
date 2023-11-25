from .._fiff.proj import Projection as Projection, make_projector as make_projector
from ..cov import Covariance as Covariance, make_ad_hoc_cov as make_ad_hoc_cov
from ..forward.forward import is_fixed_orient as is_fixed_orient
from ..source_space._source_space import label_src_vertno_sel as label_src_vertno_sel
from ..time_frequency.csd import CrossSpectralDensity as CrossSpectralDensity
from ..utils import check_fname as check_fname, logger as logger, warn as warn

class Beamformer(dict):
    """A computed beamformer.

    Notes
    -----
    .. versionadded:: 0.17
    """

    def copy(self):
        """Copy the beamformer.

        Returns
        -------
        beamformer : instance of Beamformer
            A deep copy of the beamformer.
        """
        ...
    def save(self, fname, overwrite: bool = False, verbose=None) -> None:
        """Save the beamformer filter.

        Parameters
        ----------
        fname : path-like
            The filename to use to write the HDF5 data.
            Should end in ``'-lcmv.h5'`` or ``'-dics.h5'``.

        overwrite : bool
            If True (default False), overwrite the destination file if it
            exists.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.
        """
        ...

def read_beamformer(fname):
    """Read a beamformer filter.

    Parameters
    ----------
    fname : path-like
        The filename of the HDF5 file.

    Returns
    -------
    filter : instance of Beamformer
        The beamformer filter.
    """
