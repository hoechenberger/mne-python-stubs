from .._fiff.compensator import (
    get_current_comp as get_current_comp,
    make_compensator as make_compensator,
)
from .._fiff.constants import FIFF as FIFF, FWD as FWD
from .._fiff.meas_info import Info as Info, read_info as read_info
from .._fiff.pick import pick_info as pick_info, pick_types as pick_types
from ..bem import (
    ConductorModel as ConductorModel,
    read_bem_solution as read_bem_solution,
)
from ..source_estimate import VolSourceEstimate as VolSourceEstimate
from ..transforms import (
    Transform as Transform,
    apply_trans as apply_trans,
    invert_transform as invert_transform,
    transform_surface_to as transform_surface_to,
)
from ..utils import logger as logger, warn as warn
from .forward import (
    Forward as Forward,
    convert_forward_solution as convert_forward_solution,
)
from collections.abc import Generator

def make_forward_solution(
    info,
    trans,
    src,
    bem,
    meg: bool = True,
    eeg: bool = True,
    *,
    mindist: float = 0.0,
    ignore_ref: bool = False,
    n_jobs=None,
    verbose=None,
):
    """Calculate a forward solution for a subject.

    Parameters
    ----------

    info : mne.Info | path-like
        The `mne.Info` object with information about the sensors and methods of measurement. If ``path-like``, it should be a `str` or
        `pathlib.Path` to a file with measurement information
        (e.g. `mne.io.Raw`).

    trans : path-like | dict | instance of Transform | ``"fsaverage"`` | None
        If str, the path to the head<->MRI transform ``*-trans.fif`` file produced
        during coregistration. Can also be ``'fsaverage'`` to use the built-in
        fsaverage transformation.
        If trans is None, an identity matrix is assumed.

        .. versionchanged:: 0.19
            Support for ``'fsaverage'`` argument.
    src : path-like | instance of SourceSpaces
        Either a path to a source space file or a loaded or generated
        `mne.SourceSpaces`.
    bem : path-like | ConductorModel
        Filename of the BEM (e.g., ``"sample-5120-5120-5120-bem-sol.fif"``) to
        use, or a loaded `mne.bem.ConductorModel`. See
        `mne.make_bem_model` and `mne.make_bem_solution` to create a
        `mne.bem.ConductorModel`.
    meg : bool
        If True (default), include MEG computations.
    eeg : bool
        If True (default), include EEG computations.
    mindist : float
        Minimum distance of sources from inner skull surface (in mm).
    ignore_ref : bool
        If True, do not include reference channels in compensation. This
        option should be True for KIT files, since forward computation
        with reference channels is not currently supported.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    fwd : instance of Forward
        The forward solution.

    See Also
    --------
    convert_forward_solution

    Notes
    -----
    The ``--grad`` option from MNE-C (to compute gradients) is not implemented
    here.

    To create a fixed-orientation forward solution, use this function
    followed by `mne.convert_forward_solution`.

    .. note::
        If the BEM solution was computed with :doc:`OpenMEEG <openmeeg:index>`
        in `mne.make_bem_solution`, then OpenMEEG will automatically
        be used to compute the forward solution.

    .. versionchanged:: 1.2
       Added support for OpenMEEG-based forward solution calculations.
    """
    ...

def make_forward_dipole(dipole, bem, info, trans=None, n_jobs=None, *, verbose=None):
    """Convert dipole object to source estimate and calculate forward operator.

    The instance of Dipole is converted to a discrete source space,
    which is then combined with a BEM or a sphere model and
    the sensor information in info to form a forward operator.

    The source estimate object (with the forward operator) can be projected to
    sensor-space using `mne.simulation.simulate_evoked`.

    .. note:: If the (unique) time points of the dipole object are unevenly
              spaced, the first output will be a list of single-timepoint
              source estimates.

    Parameters
    ----------

    dipole : instance of Dipole | list of Dipole
        Dipole object containing position, orientation and amplitude of
        one or more dipoles. Multiple simultaneous dipoles may be defined by
        assigning them identical times. Alternatively, multiple simultaneous
        dipoles may also be specified as a list of Dipole objects.

        .. versionchanged:: 1.1
            Added support for a list of `mne.Dipole` instances.
    bem : str | dict
        The BEM filename (str) or a loaded sphere model (dict).
    info : instance of Info
        The measurement information dictionary. It is sensor-information etc.,
        e.g., from a real data file.
    trans : str | None
        The head<->MRI transform filename. Must be provided unless BEM
        is a sphere model.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    fwd : instance of Forward
        The forward solution corresponding to the source estimate(s).
    stc : instance of VolSourceEstimate | list of VolSourceEstimate
        The dipoles converted to a discrete set of points and associated
        time courses. If the time points of the dipole are unevenly spaced,
        a list of single-timepoint source estimates are returned.

    See Also
    --------
    mne.simulation.simulate_evoked

    Notes
    -----
    .. versionadded:: 0.12.0
    """
    ...

def use_coil_def(fname) -> Generator[None, None, None]:
    """Use a custom coil definition file.

    Parameters
    ----------
    fname : path-like
        The filename of the coil definition file.

    Returns
    -------
    context : contextmanager
        The context for using the coil definition.

    Notes
    -----
    This is meant to be used a context manager such as:

    >>> with use_coil_def(my_fname):  # doctest:+SKIP
    ...     make_forward_solution(...)

    This allows using custom coil definitions with functions that require
    forward modeling.
    """
    ...
