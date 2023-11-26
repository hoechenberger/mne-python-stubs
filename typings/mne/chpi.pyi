from ._fiff.constants import FIFF as FIFF
from ._fiff.meas_info import Info as Info
from ._fiff.pick import (
    pick_channels as pick_channels,
    pick_channels_regexp as pick_channels_regexp,
    pick_info as pick_info,
    pick_types as pick_types,
)
from ._fiff.proj import Projection as Projection, setup_proj as setup_proj
from .cov import (
    compute_whitener as compute_whitener,
    make_ad_hoc_cov as make_ad_hoc_cov,
)
from .event import find_events as find_events
from .fixes import jit as jit
from .io import BaseRaw as BaseRaw
from .io.kit.constants import KIT as KIT
from .transforms import (
    als_ras_trans as als_ras_trans,
    apply_trans as apply_trans,
    invert_transform as invert_transform,
    quat_to_rot as quat_to_rot,
    rot_to_quat as rot_to_quat,
)
from .utils import (
    ProgressBar as ProgressBar,
    logger as logger,
    use_log_level as use_log_level,
    warn as warn,
)

def read_head_pos(fname):
    """### Read MaxFilter-formatted head position parameters.

    ### 🛠️ Parameters
    ----------
    fname : path-like
        The filename to read. This can be produced by e.g.,
        ``maxfilter -headpos <name>.pos``.

    ### ⏎ Returns
    -------
    pos : array, shape (N, 10)
        The position and quaternion parameters from cHPI fitting.

    ### 👉 See Also
    --------
    write_head_pos
    head_pos_to_trans_rot_t

    ### 📖 Notes
    -----
    ✨ Added in vesion 0.12
    """
    ...

def write_head_pos(fname, pos) -> None:
    """### Write MaxFilter-formatted head position parameters.

    ### 🛠️ Parameters
    ----------
    fname : path-like
        The filename to write.
    pos : array, shape (N, 10)
        The position and quaternion parameters from cHPI fitting.

    ### 👉 See Also
    --------
    read_head_pos
    head_pos_to_trans_rot_t

    ### 📖 Notes
    -----
    ✨ Added in vesion 0.12
    """
    ...

def head_pos_to_trans_rot_t(quats):
    """### Convert Maxfilter-formatted head position quaternions.

    ### 🛠️ Parameters
    ----------
    quats : ndarray, shape (N, 10)
        MaxFilter-formatted position and quaternion parameters.

    ### ⏎ Returns
    -------
    translation : ndarray, shape (N, 3)
        Translations at each time point.
    rotation : ndarray, shape (N, 3, 3)
        Rotations at each time point.
    t : ndarray, shape (N,)
        The time points.

    ### 👉 See Also
    --------
    read_head_pos
    write_head_pos
    """
    ...

def extract_chpi_locs_ctf(raw, verbose=None):
    """### Extract cHPI locations from CTF data.

    ### 🛠️ Parameters
    ----------
    raw : instance of Raw
        Raw data with CTF cHPI information.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------

    chpi_locs : dict
        The time-varying cHPI coils locations, with entries
        "times", "rrs", "moments", and "gofs".

    ### 📖 Notes
    -----
    CTF continuous head monitoring stores the x,y,z location (m) of each chpi
    coil as separate channels in the dataset:

    - ``HLC001[123]\\\\*`` - nasion
    - ``HLC002[123]\\\\*`` - lpa
    - ``HLC003[123]\\\\*`` - rpa

    This extracts these positions for use with
    `mne.chpi.compute_head_pos`.

    ✨ Added in vesion 0.20
    """
    ...

def extract_chpi_locs_kit(raw, stim_channel: str = "MISC 064", *, verbose=None):
    """### Extract cHPI locations from KIT data.

    ### 🛠️ Parameters
    ----------
    raw : instance of RawKIT
        Raw data with KIT cHPI information.
    stim_channel : str
        The stimulus channel that encodes HPI measurement intervals.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------

    chpi_locs : dict
        The time-varying cHPI coils locations, with entries
        "times", "rrs", "moments", and "gofs".

    ### 📖 Notes
    -----
    ✨ Added in vesion 0.23
    """
    ...

def get_chpi_info(info, on_missing: str = "raise", verbose=None):
    """### Retrieve cHPI information from the data.

    ### 🛠️ Parameters
    ----------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.

    on_missing : 'raise' | 'warn' | 'ignore'
        Can be ``'raise'`` (default) to raise an error, ``'warn'`` to emit a
        warning, or ``'ignore'`` to ignore when no cHPI information can be found. If ``'ignore'`` or
        ``'warn'``, all return values will be empty arrays or ``None``. If
        ``'raise'``, an exception will be raised.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    hpi_freqs : array, shape (n_coils,)
        The frequency used for each individual cHPI coil.
    hpi_pick : int | None
        The index of the ``STIM`` channel containing information about when
        which cHPI coils were switched on.
    hpi_on : array, shape (n_coils,)
        The values coding for the "on" state of each individual cHPI coil.

    ### 📖 Notes
    -----
    ✨ Added in vesion 0.24
    """
    ...

def compute_head_pos(
    info,
    chpi_locs,
    dist_limit: float = 0.005,
    gof_limit: float = 0.98,
    adjust_dig: bool = False,
    verbose=None,
):
    """### Compute time-varying head positions.

    ### 🛠️ Parameters
    ----------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.

    chpi_locs : dict
        The time-varying cHPI coils locations, with entries
        "times", "rrs", "moments", and "gofs".
        Typically obtained by `mne.chpi.compute_chpi_locs` or
        `mne.chpi.extract_chpi_locs_ctf`.
    dist_limit : float
        Minimum distance (m) to accept for coil position fitting.
    gof_limit : float
        Minimum goodness of fit to accept for each coil.

    adjust_dig : bool
        If True, adjust the digitization locations used for fitting based on
        the positions localized at the start of the file.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    quats : ndarray, shape (n_pos, 10)
        The ``[t, q1, q2, q3, x, y, z, gof, err, v]`` for each fit.

    ### 👉 See Also
    --------
    compute_chpi_locs
    extract_chpi_locs_ctf
    read_head_pos
    write_head_pos

    ### 📖 Notes
    -----
    ✨ Added in vesion 0.20
    """
    ...

def compute_chpi_snr(
    raw,
    t_step_min: float = 0.01,
    t_window: str = "auto",
    ext_order: int = 1,
    tmin: int = 0,
    tmax=None,
    verbose=None,
):
    """### Compute time-varying estimates of cHPI SNR.

    ### 🛠️ Parameters
    ----------
    raw : instance of Raw
        Raw data with cHPI information.
    t_step_min : float
        Minimum time step to use.

    t_window : float
        Time window to use to estimate the amplitudes, default is
        0.2 (200 ms).

    ext_order : int
        The external order for SSS-like interfence suppression.
        The SSS bases are used as projection vectors during fitting.

        🎭 Changed in version 0.20
            Added ``ext_order=1`` by default, which should improve
            detection of true HPI signals.

    tmin : float
        Start time of the raw data to use in seconds (must be >= 0).

    tmax : float
        End time of the raw data to use in seconds (cannot exceed data duration).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    chpi_snrs : dict
        The time-varying cHPI SNR estimates, with entries "times", "freqs",
        "snr_mag", "power_mag", and "resid_mag" (and/or "snr_grad",
        "power_grad", and "resid_grad", depending on which channel types are
        present in ``raw``).

    ### 👉 See Also
    --------
    mne.chpi.compute_chpi_locs, mne.chpi.compute_chpi_amplitudes

    ### 📖 Notes
    -----
    ✨ Added in vesion 0.24
    """
    ...

def compute_chpi_amplitudes(
    raw,
    t_step_min: float = 0.01,
    t_window: str = "auto",
    ext_order: int = 1,
    tmin: int = 0,
    tmax=None,
    verbose=None,
):
    """### Compute time-varying cHPI amplitudes.

    ### 🛠️ Parameters
    ----------
    raw : instance of Raw
        Raw data with cHPI information.
    t_step_min : float
        Minimum time step to use.

    t_window : float
        Time window to use to estimate the amplitudes, default is
        0.2 (200 ms).

    ext_order : int
        The external order for SSS-like interfence suppression.
        The SSS bases are used as projection vectors during fitting.

        🎭 Changed in version 0.20
            Added ``ext_order=1`` by default, which should improve
            detection of true HPI signals.

    tmin : float
        Start time of the raw data to use in seconds (must be >= 0).

    tmax : float
        End time of the raw data to use in seconds (cannot exceed data duration).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------

    chpi_amplitudes : dict
        The time-varying cHPI coil amplitudes, with entries
        "times", "proj", and "slopes".

    ### 👉 See Also
    --------
    mne.chpi.compute_chpi_locs, mne.chpi.compute_chpi_snr

    ### 📖 Notes
    -----
    This function will:

    1. Get HPI frequencies,  HPI status channel, HPI status bits,
       and digitization order using ``_setup_hpi_amplitude_fitting``.
    2. Window data using ``t_window`` (half before and half after ``t``) and
       ``t_step_min``.
    3. Use a linear model (DC + linear slope + sin + cos terms) to fit
       sinusoidal amplitudes to MEG channels.
       It uses SVD to determine the phase/amplitude of the sinusoids.

    In "auto" mode, ``t_window`` will be set to the longer of:

    1. Five cycles of the lowest HPI or line frequency.
          Ensures that the frequency estimate is stable.
    2. The reciprocal of the smallest difference between HPI and line freqs.
          Ensures that neighboring frequencies can be disambiguated.

    The output is meant to be used with `mne.chpi.compute_chpi_locs`.

    ✨ Added in vesion 0.20
    """
    ...

def compute_chpi_locs(
    info,
    chpi_amplitudes,
    t_step_max: float = 1.0,
    too_close: str = "raise",
    adjust_dig: bool = False,
    verbose=None,
):
    """### Compute locations of each cHPI coils over time.

    ### 🛠️ Parameters
    ----------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.

    chpi_amplitudes : dict
        The time-varying cHPI coil amplitudes, with entries
        "times", "proj", and "slopes".
        Typically obtained by `mne.chpi.compute_chpi_amplitudes`.
    t_step_max : float
        Maximum time step to use.
    too_close : str
        How to handle HPI positions too close to the sensors,
        can be ``'raise'`` (default), ``'warning'``, or ``'info'``.

    adjust_dig : bool
        If True, adjust the digitization locations used for fitting based on
        the positions localized at the start of the file.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------

    chpi_locs : dict
        The time-varying cHPI coils locations, with entries
        "times", "rrs", "moments", and "gofs".

    ### 👉 See Also
    --------
    compute_chpi_amplitudes
    compute_head_pos
    read_head_pos
    write_head_pos
    extract_chpi_locs_ctf

    ### 📖 Notes
    -----
    This function is designed to take the output of
    `mne.chpi.compute_chpi_amplitudes` and:

    1. Get HPI coil locations (as digitized in ``info['dig']``) in head coords.
    2. If the amplitudes are 98% correlated with last position
       (and Δt < t_step_max), skip fitting.
    3. Fit magnetic dipoles using the amplitudes for each coil frequency.

    The number of fitted points ``n_pos`` will depend on the velocity of head
    movements as well as ``t_step_max`` (and ``t_step_min`` from
    `mne.chpi.compute_chpi_amplitudes`).

    ✨ Added in vesion 0.20
    """
    ...

def filter_chpi(
    raw,
    include_line: bool = True,
    t_step: float = 0.01,
    t_window: str = "auto",
    ext_order: int = 1,
    allow_line_only: bool = False,
    verbose=None,
):
    """### Remove cHPI and line noise from data.

    ### 💡 Note This function will only work properly if cHPI was on
              during the recording.

    ### 🛠️ Parameters
    ----------
    raw : instance of Raw
        Raw data with cHPI information. Must be preloaded. Operates in-place.
    include_line : bool
        If True, also filter line noise.
    t_step : float
        Time step to use for estimation, default is 0.01 (10 ms).

    t_window : float
        Time window to use to estimate the amplitudes, default is
        0.2 (200 ms).

    ext_order : int
        The external order for SSS-like interfence suppression.
        The SSS bases are used as projection vectors during fitting.

        🎭 Changed in version 0.20
            Added ``ext_order=1`` by default, which should improve
            detection of true HPI signals.
    allow_line_only : bool
        If True, allow filtering line noise only. The default is False,
        which only allows the function to run when cHPI information is present.

        ✨ Added in vesion 0.20

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    raw : instance of Raw
        The raw data.

    ### 📖 Notes
    -----
    cHPI signals are in general not stationary, because head movements act
    like amplitude modulators on cHPI signals. Thus it is recommended to
    use this procedure, which uses an iterative fitting method, to
    remove cHPI signals, as opposed to notch filtering.

    ✨ Added in vesion 0.12
    """
    ...

def get_active_chpi(raw, *, on_missing: str = "raise", verbose=None):
    """### Determine how many HPI coils were active for a time point.

    ### 🛠️ Parameters
    ----------
    raw : instance of Raw
        Raw data with cHPI information.

    on_missing : 'raise' | 'warn' | 'ignore'
        Can be ``'raise'`` (default) to raise an error, ``'warn'`` to emit a
        warning, or ``'ignore'`` to ignore when no cHPI information can be found. If ``'ignore'`` or
        ``'warn'``, all return values will be empty arrays or ``None``. If
        ``'raise'``, an exception will be raised.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    n_active : array, shape (n_times)
        The number of active cHPIs for every timepoint in raw.

    ### 📖 Notes
    -----
    ✨ Added in vesion 1.2
    """
    ...
