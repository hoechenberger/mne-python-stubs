from .._fiff.constants import FIFF as FIFF
from .._fiff.pick import pick_types as pick_types
from ..bem import fit_sphere_to_headshape as fit_sphere_to_headshape
from ..epochs import (
    BaseEpochs as BaseEpochs,
    make_fixed_length_epochs as make_fixed_length_epochs,
)
from ..evoked import Evoked as Evoked
from ..io import BaseRaw as BaseRaw
from ..utils import logger as logger

def compute_current_source_density(
    inst,
    sphere: str = "auto",
    lambda2: float = 1e-05,
    stiffness: int = 4,
    n_legendre_terms: int = 50,
    copy: bool = True,
    *,
    verbose=None,
):
    """Get the current source density (CSD) transformation.

    Transformation based on spherical spline surface Laplacian
    :footcite:`PerrinEtAl1987,PerrinEtAl1989,Cohen2014,KayserTenke2015`.

    This function can be used to re-reference the signal using a Laplacian
    (LAP) "reference-free" transformation.

    Parameters
    ----------
    inst : instance of Raw, Epochs or Evoked
        The data to be transformed.
    sphere : array-like, shape (4,) | str
        The sphere, head-model of the form (x, y, z, r) where x, y, z
        is the center of the sphere and r is the radius in meters.
        Can also be "auto" to use a digitization-based fit.
    lambda2 : float
        Regularization parameter, produces smoothness. Defaults to 1e-5.
    stiffness : float
        Stiffness of the spline.
    n_legendre_terms : int
        Number of Legendre terms to evaluate.
    copy : bool
        Whether to overwrite instance data or create a copy.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    inst_csd : instance of Raw, Epochs or Evoked
        The transformed data. Output type will match input type.

    Notes
    -----
    .. versionadded:: 0.20

    References
    ----------
    .. footbibliography::
    """

def compute_bridged_electrodes(
    inst,
    lm_cutoff: int = 16,
    epoch_threshold: float = 0.5,
    l_freq: float = 0.5,
    h_freq: int = 30,
    epoch_duration: int = 2,
    bw_method=None,
    verbose=None,
):
    """Compute bridged EEG electrodes using the intrinsic Hjorth algorithm.

    First, an electrical distance matrix is computed by taking the pairwise
    variance between electrodes. Local minimums in this matrix below
    ``lm_cutoff`` are indicative of bridging between a pair of electrodes.
    Pairs of electrodes are marked as bridged as long as their electrical
    distance is below ``lm_cutoff`` on more than the ``epoch_threshold``
    proportion of epochs.

    Based on :footcite:`TenkeKayser2001,GreischarEtAl2004,DelormeMakeig2004`
    and the `EEGLAB implementation
    <https://psychophysiology.cpmc.columbia.edu/software/eBridge/index.html>`_.

    Parameters
    ----------
    inst : instance of Raw, Epochs or Evoked
        The data to compute electrode bridging on.
    lm_cutoff : float
        The distance in :math:`{\\mu}V^2` cutoff below which to
        search for a local minimum (lm) indicative of bridging.
        EEGLAB defaults to 5 :math:`{\\mu}V^2`. MNE defaults to
        16 :math:`{\\mu}V^2` to be conservative based on the distributions in
        :footcite:t:`GreischarEtAl2004`.
    epoch_threshold : float
        The proportion of epochs with electrical distance less than
        ``lm_cutoff`` in order to consider the channel bridged.
        The default is 0.5.
    l_freq : float
        The low cutoff frequency to use. Default is 0.5 Hz.
    h_freq : float
        The high cutoff frequency to use. Default is 30 Hz.
    epoch_duration : float
        The time in seconds to divide the raw into fixed-length epochs
        to check for consistent bridging. Only used if ``inst`` is
        :class:`mne.io.BaseRaw`. The default is 2 seconds.
    bw_method : None
        ``bw_method`` to pass to :class:`scipy.stats.gaussian_kde`.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    bridged_idx : list of tuple
        The indices of channels marked as bridged with each bridged
        pair stored as a tuple.
    ed_matrix : ndarray of float, shape (n_epochs, n_channels, n_channels)
        The electrical distance matrix for each pair of EEG electrodes.

    Notes
    -----
    .. versionadded:: 1.1

    References
    ----------
    .. footbibliography::
    """
