from .._fiff.constants import FIFF as FIFF
from .._fiff.meas_info import Info as Info
from .._fiff.pick import (
    pick_channels as pick_channels,
    pick_channels_forward as pick_channels_forward,
    pick_info as pick_info,
    pick_types as pick_types,
)
from ..bem import (
    fit_sphere_to_headshape as fit_sphere_to_headshape,
    make_sphere_model as make_sphere_model,
    read_bem_solution as read_bem_solution,
)
from ..chpi import (
    get_chpi_info as get_chpi_info,
    head_pos_to_trans_rot_t as head_pos_to_trans_rot_t,
    read_head_pos as read_head_pos,
)
from ..cov import (
    Covariance as Covariance,
    make_ad_hoc_cov as make_ad_hoc_cov,
    read_cov as read_cov,
)
from ..forward import (
    convert_forward_solution as convert_forward_solution,
    restrict_forward_to_stc as restrict_forward_to_stc,
)
from ..io import BaseRaw as BaseRaw, RawArray as RawArray
from ..source_space._source_space import (
    setup_volume_source_space as setup_volume_source_space,
)
from ..transforms import transform_surface_to as transform_surface_to
from ..utils import check_random_state as check_random_state, logger as logger
from .source import SourceSimulator as SourceSimulator
from _typeshed import Incomplete

def simulate_raw(
    info,
    stc=None,
    trans=None,
    src=None,
    bem=None,
    head_pos=None,
    mindist: float = 1.0,
    interp: str = "cos2",
    n_jobs=None,
    use_cps: bool = True,
    forward=None,
    first_samp: int = 0,
    max_iter: int = 10000,
    verbose=None,
):
    """Simulate raw data.

    Head movements can optionally be simulated using the ``head_pos``
    parameter.

    Parameters
    ----------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement. Used for simulation.

        🎭 Changed in version 0.18
           Support for `mne.Info`.
    stc : iterable | SourceEstimate | SourceSimulator
        The source estimates to use to simulate data. Each must have the same
        sample rate as the raw data, and the vertices of all stcs in the
        iterable must match. Each entry in the iterable can also be a tuple of
        ``(SourceEstimate, ndarray)`` to allow specifying the stim channel
        (e.g., STI001) data accompany the source estimate.
        See Notes for details.

        🎭 Changed in version 0.18
           Support for tuple, iterable of tuple or `mne.SourceEstimate`,
           or `mne.simulation.SourceSimulator`.
    trans : dict | str | None
        Either a transformation filename (usually made using mne_analyze)
        or an info dict (usually opened using read_trans()).
        If string, an ending of ``.fif`` or ``.fif.gz`` will be assumed to
        be in FIF format, any other ending will be assumed to be a text
        file with a 4x4 transformation matrix (like the ``--trans`` MNE-C
        option). If trans is None, an identity transform will be used.
    src : path-like | instance of SourceSpaces | None
        Source space corresponding to the stc. If string, should be a source
        space filename. Can also be an instance of loaded or generated
        SourceSpaces. Can be None if ``forward`` is provided.
    bem : path-like | dict | None
        BEM solution  corresponding to the stc. If string, should be a BEM
        solution filename (e.g., "sample-5120-5120-5120-bem-sol.fif").
        Can be None if ``forward`` is provided.

    head_pos : None | path-like | dict | tuple | array
        Path to the position estimates file. Should be in the format of
        the files produced by MaxFilter. If dict, keys should
        be the time points and entries should be 4x4 ``dev_head_t``
        matrices. If None, the original head position (from
        ``info['dev_head_t']``) will be used. If tuple, should have the
        same format as data returned by ``head_pos_to_trans_rot_t``.
        If array, should be of the form returned by
        `mne.chpi.read_head_pos`.
        See for example :footcite:`LarsonTaulu2017`.
    mindist : float
        Minimum distance between sources and the inner skull boundary
        to use during forward calculation.

    interp : str
        Either ``'hann'``, ``'cos2'`` (default), ``'linear'``, or ``'zero'``, the type of
        forward-solution interpolation to use between forward solutions
        at different head positions.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.

    use_cps : bool
        Whether to use cortical patch statistics to define normal orientations for
        surfaces (default True).
    forward : instance of Forward | None
        The forward operator to use. If None (default) it will be computed
        using ``bem``, ``trans``, and ``src``. If not None,
        ``bem``, ``trans``, and ``src`` are ignored.

        ✨ Added in version 0.17
    first_samp : int
        The first_samp property in the output Raw instance.

        ✨ Added in version 0.18
    max_iter : int
        The maximum number of STC iterations to allow.
        This is a sanity parameter to prevent accidental blowups.

        ✨ Added in version 0.18

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    raw : instance of Raw
        The simulated raw file.

    See Also
    --------
    mne.chpi.read_head_pos
    add_chpi
    add_noise
    add_ecg
    add_eog
    simulate_evoked
    simulate_stc
    simulate_sparse_stc

    Notes
    -----
    **Stim channel encoding**

    By default, the stimulus channel will have the head position number
    (starting at 1) stored in the trigger channel (if available) at the
    t=0 point in each repetition of the ``stc``. If ``stc`` is a tuple of
    ``(SourceEstimate, ndarray)`` the array values will be placed in the
    stim channel aligned with the `mne.SourceEstimate`.

    **Data simulation**

    In the most advanced case where ``stc`` is an iterable of tuples the output
    will be concatenated in time as:

    .. table:: Data alignment and stim channel encoding

       +---------+--------------------------+--------------------------+---------+
       | Channel | Data                                                          |
       +=========+==========================+==========================+=========+
       | M/EEG   | ``fwd @ stc[0][0].data`` | ``fwd @ stc[1][0].data`` | ``...`` |
       +---------+--------------------------+--------------------------+---------+
       | STIM    | ``stc[0][1]``            | ``stc[1][1]``            | ``...`` |
       +---------+--------------------------+--------------------------+---------+
       |         | *time →*                                                      |
       +---------+--------------------------+--------------------------+---------+

    ✨ Added in version 0.10.0

    References
    ----------
    .. footbibliography::
    """
    ...

def add_eog(
    raw,
    head_pos=None,
    interp: str = "cos2",
    n_jobs=None,
    random_state=None,
    verbose=None,
):
    """Add blink noise to raw data.

    Parameters
    ----------
    raw : instance of Raw
        The raw instance to modify.

    head_pos : None | path-like | dict | tuple | array
        Path to the position estimates file. Should be in the format of
        the files produced by MaxFilter. If dict, keys should
        be the time points and entries should be 4x4 ``dev_head_t``
        matrices. If None, the original head position (from
        ``info['dev_head_t']``) will be used. If tuple, should have the
        same format as data returned by ``head_pos_to_trans_rot_t``.
        If array, should be of the form returned by
        `mne.chpi.read_head_pos`.

    interp : str
        Either ``'hann'``, ``'cos2'`` (default), ``'linear'``, or ``'zero'``, the type of
        forward-solution interpolation to use between forward solutions
        at different head positions.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.

    random_state : None | int | instance of ~numpy.random.RandomState
        A seed for the NumPy random number generator (RNG). If ``None`` (default),
        the seed will be  obtained from the operating system
        (see  `numpy.random.RandomState` for details), meaning it will most
        likely produce different output every time this function or method is run.
        To achieve reproducible results, pass a value here to explicitly initialize
        the RNG with a defined state.
        The random generator state used for blink, ECG, and sensor noise
        randomization.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    raw : instance of Raw
        The instance, modified in place.

    See Also
    --------
    add_chpi
    add_ecg
    add_noise
    simulate_raw

    Notes
    -----
    The blink artifacts are generated by:

    1. Random activation times are drawn from an inhomogeneous poisson
       process whose blink rate oscillates between 4.5 blinks/minute
       and 17 blinks/minute based on the low (reading) and high (resting)
       blink rates from :footcite:`BentivoglioEtAl1997`.
    2. The activation kernel is a 250 ms Hanning window.
    3. Two activated dipoles are located in the z=0 plane (in head
       coordinates) at ±30 degrees away from the y axis (nasion).
    4. Activations affect MEG and EEG channels.

    The scale-factor of the activation function was chosen based on
    visual inspection to yield amplitudes generally consistent with those
    seen in experimental data. Noisy versions of the activation will be
    stored in the first EOG channel in the raw instance, if it exists.

    References
    ----------
    .. footbibliography::
    """
    ...

def add_ecg(
    raw,
    head_pos=None,
    interp: str = "cos2",
    n_jobs=None,
    random_state=None,
    verbose=None,
):
    """Add ECG noise to raw data.

    Parameters
    ----------
    raw : instance of Raw
        The raw instance to modify.

    head_pos : None | path-like | dict | tuple | array
        Path to the position estimates file. Should be in the format of
        the files produced by MaxFilter. If dict, keys should
        be the time points and entries should be 4x4 ``dev_head_t``
        matrices. If None, the original head position (from
        ``info['dev_head_t']``) will be used. If tuple, should have the
        same format as data returned by ``head_pos_to_trans_rot_t``.
        If array, should be of the form returned by
        `mne.chpi.read_head_pos`.

    interp : str
        Either ``'hann'``, ``'cos2'`` (default), ``'linear'``, or ``'zero'``, the type of
        forward-solution interpolation to use between forward solutions
        at different head positions.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.

    random_state : None | int | instance of ~numpy.random.RandomState
        A seed for the NumPy random number generator (RNG). If ``None`` (default),
        the seed will be  obtained from the operating system
        (see  `numpy.random.RandomState` for details), meaning it will most
        likely produce different output every time this function or method is run.
        To achieve reproducible results, pass a value here to explicitly initialize
        the RNG with a defined state.
        The random generator state used for blink, ECG, and sensor noise
        randomization.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    raw : instance of Raw
        The instance, modified in place.

    See Also
    --------
    add_chpi
    add_eog
    add_noise
    simulate_raw

    Notes
    -----
    The ECG artifacts are generated by:

    1. Random inter-beat intervals are drawn from a uniform distribution
       of times corresponding to 40 and 80 beats per minute.
    2. The activation function is the sum of three Hanning windows with
       varying durations and scales to make a more complex waveform.
    3. The activated dipole is located one (estimated) head radius to
       the left (-x) of head center and three head radii below (+z)
       head center; this dipole is oriented in the +x direction.
    4. Activations only affect MEG channels.

    The scale-factor of the activation function was chosen based on
    visual inspection to yield amplitudes generally consistent with those
    seen in experimental data. Noisy versions of the activation will be
    stored in the first EOG channel in the raw instance, if it exists.

    ✨ Added in version 0.18
    """
    ...

def add_chpi(raw, head_pos=None, interp: str = "cos2", n_jobs=None, verbose=None):
    """Add cHPI activations to raw data.

    Parameters
    ----------
    raw : instance of Raw
        The raw instance to be modified.

    head_pos : None | path-like | dict | tuple | array
        Path to the position estimates file. Should be in the format of
        the files produced by MaxFilter. If dict, keys should
        be the time points and entries should be 4x4 ``dev_head_t``
        matrices. If None, the original head position (from
        ``info['dev_head_t']``) will be used. If tuple, should have the
        same format as data returned by ``head_pos_to_trans_rot_t``.
        If array, should be of the form returned by
        `mne.chpi.read_head_pos`.

    interp : str
        Either ``'hann'``, ``'cos2'`` (default), ``'linear'``, or ``'zero'``, the type of
        forward-solution interpolation to use between forward solutions
        at different head positions.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    raw : instance of Raw
        The instance, modified in place.

    Notes
    -----
    ✨ Added in version 0.18
    """
    ...

class _HPIForwards:
    offsets: Incomplete
    dev_head_ts: Incomplete
    hpi_rrs: Incomplete
    hpi_nns: Incomplete
    megcoils: Incomplete
    idx: int

    def __init__(self, offsets, dev_head_ts, megcoils, hpi_rrs, hpi_nns) -> None: ...
    def __call__(self, offset): ...

class _SimForwards:
    idx: int
    offsets: Incomplete
    use_cps: Incomplete
    iter: Incomplete

    def __init__(
        self,
        dev_head_ts,
        offsets,
        info,
        trans,
        src,
        bem,
        mindist,
        n_jobs,
        meeg_picks,
        forward=None,
        use_cps: bool = True,
    ) -> None: ...
    src: Incomplete

    def __call__(self, offset): ...
