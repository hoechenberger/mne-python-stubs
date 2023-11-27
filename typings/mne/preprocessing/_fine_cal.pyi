from .._fiff.pick import pick_info as pick_info, pick_types as pick_types
from ..io import BaseRaw as BaseRaw
from ..utils import check_fname as check_fname, logger as logger

def compute_fine_calibration(
    raw,
    n_imbalance: int = 3,
    t_window: float = 10.0,
    ext_order: int = 2,
    origin=(0.0, 0.0, 0.0),
    cross_talk=None,
    calibration=None,
    verbose=None,
):
    """## Compute fine calibration from empty-room data.

    -----
    ### 🛠️ Parameters

    #### `raw : instance of Raw`
        The raw data to use. Should be from an empty-room recording,
        and all channels should be good.
    #### `n_imbalance : int`
        Can be 1 or 3 (default), indicating the number of gradiometer
        imbalance components. Only used if gradiometers are present.
    #### `t_window : float`
        Time window to use for surface normal rotation in seconds.
        Default is 10.

    #### `ext_order : int`
        Order of external component of spherical expansion.
        Default is 2, which is lower than the default (3) for
        `mne.preprocessing.maxwell_filter` because it tends to yield
        more stable parameter estimates.

    #### `origin : array-like, shape (3,) | str`
        Origin of internal and external multipolar moment space in meters.
        The default is ``'auto'``, which means ``(0., 0., 0.)`` when
        ``coord_frame='meg'``, and a head-digitization-based
        origin fit using `mne.bem.fit_sphere_to_headshape`
        when ``coord_frame='head'``. If automatic fitting fails (e.g., due
        to having too few digitization points),
        consider separately calling the fitting function with different
        options or specifying the origin manually.

    #### `cross_talk : str | None`
        Path to the FIF file with cross-talk correction information.
    #### `calibration : dict | None`
        Dictionary with existing calibration. If provided, the magnetometer
        imbalances and adjusted normals will be used and only the gradiometer
        imbalances will be estimated (see step 2 in Notes below).

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `calibration : dict`
        Fine calibration data.
    #### `count : int`
        The number of good segments used to compute the magnetometer
        parameters.

    -----
    ### 👉 See Also

    mne.preprocessing.maxwell_filter

    -----
    ### 📖 Notes

    This algorithm proceeds in two steps, both optimizing the fit between the
    data and a reconstruction of the data based only on an external multipole
    expansion:

    1. Estimate magnetometer normal directions and scale factors. All
       coils (mag and matching grad) are rotated by the adjusted normal
       direction.
    2. Estimate gradiometer imbalance factors. These add point magnetometers
       in just the gradiometer difference direction or in all three directions
       (depending on ``n_imbalance``).

    Magnetometer normal and coefficient estimation (1) is typically the most
    time consuming step. Gradiometer imbalance parameters (2) can be
    iteratively reestimated (for example, first using ``n_imbalance=1`` then
    subsequently ``n_imbalance=3``) by passing the previous ``calibration``
    output to the ``calibration`` input in the second call.

    MaxFilter processes at most 120 seconds of data, so consider cropping
    your raw instance prior to processing. It also checks to make sure that
    there were some minimal usable ``count`` number of segments (default 5)
    that were included in the estimate.

    ✨ Added in version 0.21
    """
    ...

def read_fine_calibration(fname):
    """## Read fine calibration information from a ``.dat`` file.

    The fine calibration typically includes improved sensor locations,
    calibration coefficients, and gradiometer imbalance information.

    -----
    ### 🛠️ Parameters

    #### `fname : path-like`
        The filename.

    -----
    ### ⏎ Returns

    #### `calibration : dict`
        Fine calibration information. Key-value pairs are:

        - ``ch_names``
             List of str of the channel names.
        - ``locs``
             Coil location and orientation parameters.
        - ``imb_cals``
             For magnetometers, the calibration coefficients.
             For gradiometers, one or three imbalance parameters.
    """
    ...

def write_fine_calibration(fname, calibration) -> None:
    """## Write fine calibration information to a ``.dat`` file.

    -----
    ### 🛠️ Parameters

    #### `fname : path-like`
        The filename to write out.
    #### `calibration : dict`
        Fine calibration information.
    """
    ...
