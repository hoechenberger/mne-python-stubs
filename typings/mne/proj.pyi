from ._fiff.constants import FIFF as FIFF
from ._fiff.open import fiff_open as fiff_open
from ._fiff.pick import (
    pick_types as pick_types,
    pick_types_forward as pick_types_forward,
)
from ._fiff.proj import (
    Projection as Projection,
    make_eeg_average_ref_proj as make_eeg_average_ref_proj,
    make_projector as make_projector,
)
from ._fiff.write import start_and_end_file as start_and_end_file
from .epochs import Epochs as Epochs
from .event import make_fixed_length_events as make_fixed_length_events
from .forward import (
    convert_forward_solution as convert_forward_solution,
    is_fixed_orient as is_fixed_orient,
)
from .parallel import parallel_func as parallel_func
from .utils import check_fname as check_fname, logger as logger

def read_proj(fname, verbose=None):
    """## Read projections from a FIF file.

    -----
    ### 🛠️ Parameters

    #### `fname : path-like`
        The name of file containing the projections vectors. It should end with
        ``-proj.fif`` or ``-proj.fif.gz``.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `projs : list of Projection`
        The list of projection vectors.

    -----
    ### 👉 See Also

    write_proj
    """
    ...

def write_proj(fname, projs, *, overwrite: bool = False, verbose=None) -> None:
    """## Write projections to a FIF file.

    -----
    ### 🛠️ Parameters

    #### `fname : path-like`
        The name of file containing the projections vectors. It should end with
        ``-proj.fif`` or ``-proj.fif.gz``.
    #### `projs : list of Projection`
        The list of projection vectors.

    #### `overwrite : bool`
        If True (default False), overwrite the destination file if it
        exists.

        ✨ Added in version 1.0

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

        ✨ Added in version 1.0

    -----
    ### 👉 See Also

    read_proj
    """
    ...

def compute_proj_epochs(
    epochs,
    n_grad: int = 2,
    n_mag: int = 2,
    n_eeg: int = 2,
    n_jobs=None,
    desc_prefix=None,
    meg: str = "separate",
    verbose=None,
):
    """## Compute SSP (signal-space projection) vectors on epoched data.

    This function aims to find those SSP vectors that
    will project out the ``n`` most prominent signals from the data for each
    specified sensor type. Consequently, if the provided input data contains high
    levels of noise, the produced SSP vectors can then be used to eliminate that
    noise from the data.

    -----
    ### 🛠️ Parameters

    #### `epochs : instance of Epochs`
        The epochs containing the artifact.

    #### `n_grad : int | float between ``0`` and ``1```
        Number of vectors for gradiometers. Either an integer or a float between 0 and 1
        to select the number of vectors to explain the cumulative variance greater than
        ``n_grad``.
    #### `n_mag : int | float between ``0`` and ``1```
        Number of vectors for magnetometers. Either an integer or a float between 0 and
        1 to select the number of vectors to explain the cumulative variance greater
        than ``n_mag``.
    #### `n_eeg : int | float between ``0`` and ``1```
        Number of vectors for EEG channels. Either an integer or a float between 0 and 1
        to select the number of vectors to explain the cumulative variance greater than
        ``n_eeg``.
    #### `n_jobs : int | None`
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.
        Number of jobs to use to compute covariance.
    #### `desc_prefix : str | None`
        The description prefix to use. If None, one will be created based on
        the event_id, tmin, and tmax.
    #### `meg : str`
        Can be ``'separate'`` (default) or ``'combined'`` to compute projectors
        for magnetometers and gradiometers separately or jointly.
        If ``'combined'``, ``n_mag == n_grad`` is required and the number of
        projectors computed for MEG will be ``n_mag``.

        ✨ Added in version 0.18

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    projs: list of Projection
        List of projection vectors.

    -----
    ### 👉 See Also

    compute_proj_raw, compute_proj_evoked
    """
    ...

def compute_proj_evoked(
    evoked,
    n_grad: int = 2,
    n_mag: int = 2,
    n_eeg: int = 2,
    desc_prefix=None,
    meg: str = "separate",
    verbose=None,
):
    """## Compute SSP (signal-space projection) vectors on evoked data.

    This function aims to find those SSP vectors that
    will project out the ``n`` most prominent signals from the data for each
    specified sensor type. Consequently, if the provided input data contains high
    levels of noise, the produced SSP vectors can then be used to eliminate that
    noise from the data.

    -----
    ### 🛠️ Parameters

    #### `evoked : instance of Evoked`
        The Evoked obtained by averaging the artifact.

    #### `n_grad : int | float between ``0`` and ``1```
        Number of vectors for gradiometers. Either an integer or a float between 0 and 1
        to select the number of vectors to explain the cumulative variance greater than
        ``n_grad``.
    #### `n_mag : int | float between ``0`` and ``1```
        Number of vectors for magnetometers. Either an integer or a float between 0 and
        1 to select the number of vectors to explain the cumulative variance greater
        than ``n_mag``.
    #### `n_eeg : int | float between ``0`` and ``1```
        Number of vectors for EEG channels. Either an integer or a float between 0 and 1
        to select the number of vectors to explain the cumulative variance greater than
        ``n_eeg``.
    #### `desc_prefix : str | None`
        The description prefix to use. If None, one will be created based on
        tmin and tmax.

        ✨ Added in version 0.17
    #### `meg : str`
        Can be ``'separate'`` (default) or ``'combined'`` to compute projectors
        for magnetometers and gradiometers separately or jointly.
        If ``'combined'``, ``n_mag == n_grad`` is required and the number of
        projectors computed for MEG will be ``n_mag``.

        ✨ Added in version 0.18

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `projs : list of Projection`
        List of projection vectors.

    -----
    ### 👉 See Also

    compute_proj_raw, compute_proj_epochs
    """
    ...

def compute_proj_raw(
    raw,
    start: int = 0,
    stop=None,
    duration: int = 1,
    n_grad: int = 2,
    n_mag: int = 2,
    n_eeg: int = 0,
    reject=None,
    flat=None,
    n_jobs=None,
    meg: str = "separate",
    verbose=None,
):
    """## Compute SSP (signal-space projection) vectors on continuous data.

    This function aims to find those SSP vectors that
    will project out the ``n`` most prominent signals from the data for each
    specified sensor type. Consequently, if the provided input data contains high
    levels of noise, the produced SSP vectors can then be used to eliminate that
    noise from the data.

    -----
    ### 🛠️ Parameters

    #### `raw : instance of Raw`
        A raw object to use the data from.
    #### `start : float`
        Time (in seconds) to start computing SSP.
    #### `stop : float | None`
        Time (in seconds) to stop computing SSP. None will go to the end of the file.
    #### `duration : float | None`
        Duration (in seconds) to chunk data into for SSP
        If duration is ``None``, data will not be chunked.

    #### `n_grad : int | float between ``0`` and ``1```
        Number of vectors for gradiometers. Either an integer or a float between 0 and 1
        to select the number of vectors to explain the cumulative variance greater than
        ``n_grad``.
    #### `n_mag : int | float between ``0`` and ``1```
        Number of vectors for magnetometers. Either an integer or a float between 0 and
        1 to select the number of vectors to explain the cumulative variance greater
        than ``n_mag``.
    #### `n_eeg : int | float between ``0`` and ``1```
        Number of vectors for EEG channels. Either an integer or a float between 0 and 1
        to select the number of vectors to explain the cumulative variance greater than
        ``n_eeg``.
    #### `reject : dict | None`
        Epoch PTP rejection threshold used if ``duration != None``. See `mne.Epochs`.
    #### `flat : dict | None`
        Epoch flatness rejection threshold used if ``duration != None``. See
        `mne.Epochs`.
    #### `n_jobs : int | None`
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.
        Number of jobs to use to compute covariance.
    #### `meg : str`
        Can be ``'separate'`` (default) or ``'combined'`` to compute projectors
        for magnetometers and gradiometers separately or jointly.
        If ``'combined'``, ``n_mag == n_grad`` is required and the number of
        projectors computed for MEG will be ``n_mag``.

        ✨ Added in version 0.18

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    projs: list of Projection
        List of projection vectors.

    -----
    ### 👉 See Also

    compute_proj_epochs, compute_proj_evoked
    """
    ...

def sensitivity_map(
    fwd,
    projs=None,
    ch_type: str = "grad",
    mode: str = "fixed",
    exclude=(),
    *,
    verbose=None,
):
    """## Compute sensitivity map.

    Such maps are used to know how much sources are visible by a type
    of sensor, and how much projections shadow some sources.

    -----
    ### 🛠️ Parameters

    #### `fwd : Forward`
        The forward operator.
    #### `projs : list`
        List of projection vectors.
    #### `ch_type : ``'grad'`` | ``'mag'`` | ``'eeg'```
        The type of sensors to use.
    #### `mode : str`
        The type of sensitivity map computed. See manual. Should be ``'free'``,
        ``'fixed'``, ``'ratio'``, ``'radiality'``, ``'angle'``,
        ``'remaining'``, or ``'dampening'`` corresponding to the argument
        ``--map 1, 2, 3, 4, 5, 6, 7`` of the command ``mne_sensitivity_map``.
    #### `exclude : list of str | str`
        List of channels to exclude. If empty do not exclude any (default).
        If ``'bads'``, exclude channels in ``fwd['info']['bads']``.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `stc : SourceEstimate | VolSourceEstimate`
        The sensitivity map as a SourceEstimate or VolSourceEstimate instance
        for visualization.

    -----
    ### 📖 Notes

    When mode is ``'fixed'`` or ``'free'``, the sensitivity map is normalized
    by its maximum value.
    """
    ...
