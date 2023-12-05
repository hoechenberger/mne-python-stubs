from .._fiff.meas_info import create_info as create_info
from ..epochs import BaseEpochs as BaseEpochs, EpochsArray as EpochsArray
from ..evoked import Evoked as Evoked, EvokedArray as EvokedArray
from ..io import BaseRaw as BaseRaw, RawArray as RawArray

def equalize_bads(insts, interp_thresh: float = 1.0, copy: bool = True):
    """Interpolate or mark bads consistently for a list of instances.

    Once called on a list of instances, the instances can be concatenated
    as they will have the same list of bad channels.

    Parameters
    ----------
    insts : list
        The list of instances (Evoked, Epochs or Raw) to consider
        for interpolation. Each instance should have marked channels.
    interp_thresh : float
        A float between 0 and 1 (default) that specifies the fraction of time
        a channel should be good to be eventually interpolated for certain
        instances. For example if 0.5, a channel which is good at least half
        of the time will be interpolated in the instances where it is marked
        as bad. If 1 then channels will never be interpolated and if 0 all bad
        channels will be systematically interpolated.
    copy : bool
        If True then the returned instances will be copies.

    Returns
    -------
    insts_bads : list
        The list of instances, with the same channel(s) marked as bad in all of
        them, possibly with some formerly bad channels interpolated.
    """
    ...

def interpolate_bridged_electrodes(inst, bridged_idx, bad_limit: int = 4):
    """Interpolate bridged electrode pairs.

    Because bridged electrodes contain brain signal, it's just that the
    signal is spatially smeared between the two electrodes, we can
    make a virtual channel midway between the bridged pairs and use
    that to aid in interpolation rather than completely discarding the
    data from the two channels.

    Parameters
    ----------
    inst : instance of Epochs, Evoked, or Raw
        The data object with channels that are to be interpolated.
    bridged_idx : list of tuple
        The indices of channels marked as bridged with each bridged
        pair stored as a tuple.
    bad_limit : int
        The maximum number of electrodes that can be bridged together
        (included) and interpolated. Above this number, an error will be
        raised.

        ✨ Added in version 1.2

    Returns
    -------
    inst : instance of Epochs, Evoked, or Raw
        The modified data object.

    See Also
    --------
    mne.preprocessing.compute_bridged_electrodes
    """
    ...
