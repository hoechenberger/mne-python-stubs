from .._fiff.constants import FIFF as FIFF
from .._fiff.pick import pick_info as pick_info, pick_types as pick_types
from .._fiff.proj import make_projector as make_projector
from ..cov import make_ad_hoc_cov as make_ad_hoc_cov
from ..epochs import BaseEpochs as BaseEpochs, EpochsArray as EpochsArray
from ..evoked import Evoked as Evoked, EvokedArray as EvokedArray
from ..surface import (
    get_head_surf as get_head_surf,
    get_meg_helmet_surf as get_meg_helmet_surf,
)
from ..transforms import transform_surface_to as transform_surface_to
from ..utils import logger as logger

def make_field_map(
    evoked,
    trans: str = "auto",
    subject=None,
    subjects_dir=None,
    ch_type=None,
    mode: str = "fast",
    meg_surf: str = "helmet",
    origin=(0.0, 0.0, 0.04),
    n_jobs=None,
    *,
    head_source=("bem", "head"),
    verbose=None,
):
    """Compute surface maps used for field display in 3D.

    Parameters
    ----------
    evoked : Evoked | Epochs | Raw
        The measurement file. Need to have info attribute.

    trans : path-like | dict | instance of Transform | ``"fsaverage"`` | None
        If str, the path to the head<->MRI transform ``*-trans.fif`` file produced
        during coregistration. Can also be ``'fsaverage'`` to use the built-in
        fsaverage transformation.
        If trans is None, an identity matrix is assumed. ``"auto"`` (default) will load trans from the FreeSurfer
        directory specified by ``subject`` and ``subjects_dir`` parameters.

        🎭 Changed in version 0.19
            Support for ``'fsaverage'`` argument.
    subject : str | None
        The subject name corresponding to FreeSurfer environment
        variable SUBJECT. If None, map for EEG data will not be available.
    subjects_dir : path-like
        The path to the freesurfer subjects reconstructions.
        It corresponds to Freesurfer environment variable SUBJECTS_DIR.
    ch_type : None | ``'eeg'`` | ``'meg'``
        If None, a map for each available channel type will be returned.
        Else only the specified type will be used.
    mode : ``'accurate'`` | ``'fast'``
        Either ``'accurate'`` or ``'fast'``, determines the quality of the
        Legendre polynomial expansion used. ``'fast'`` should be sufficient
        for most applications.
    meg_surf : 'helmet' | 'head'
        Should be ``'helmet'`` or ``'head'`` to specify in which surface
        to compute the MEG field map. The default value is ``'helmet'``.
    origin : array-like, shape (3,) | 'auto'
        Origin of the sphere in the head coordinate frame and in meters.
        Can be ``'auto'``, which means a head-digitization-based origin
        fit. Default is ``(0., 0., 0.04)``.

        ✨ Added in version 0.11
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.

    head_source : str | list of str
        Head source(s) to use. See the ``source`` option of
        `mne.get_head_surf` for more information.

        ✨ Added in version 1.1

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    surf_maps : list
        The surface maps to be used for field plots. The list contains
        separate ones for MEG and EEG (if both MEG and EEG are present).
    """
    ...
