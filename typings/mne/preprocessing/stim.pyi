from ..epochs import BaseEpochs as BaseEpochs
from ..event import find_events as find_events
from ..evoked import Evoked as Evoked
from ..io import BaseRaw as BaseRaw
from ..utils import fill_doc as fill_doc

def fix_stim_artifact(
    inst,
    events=None,
    event_id=None,
    tmin: float = 0.0,
    tmax: float = 0.01,
    mode: str = "linear",
    stim_channel=None,
    picks=None,
):
    """## 🧠 Eliminate stimulation's artifacts from instance.

    ### 💡 Note This function operates in-place, consider passing
              ``inst.copy()`` if this is not desired.

    -----
    ### 🛠️ Parameters

    #### `inst : instance of Raw or Epochs or Evoked`
        The data.
    #### `events : array, shape (n_events, 3)`
        The list of events. Required only when inst is Raw.
    #### `event_id : int`
        The id of the events generating the stimulation artifacts.
        If None, read all events. Required only when inst is Raw.
    #### `tmin : float`
        Start time of the interpolation window in seconds.
    #### `tmax : float`
        End time of the interpolation window in seconds.
    #### `mode : 'linear' | 'window'`
        Way to fill the artifacted time interval.
        'linear' does linear interpolation
        'window' applies a (1 - hanning) window.
    #### `stim_channel : str | None`
        Stim channel to use.
    #### `picks : str | array-like | slice | None`
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel `type` strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel `name` strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick all data channels. Note that channels
        in ``info['bads']`` `will be included` if their names or indices are
        explicitly provided.

    -----
    ### ⏎ Returns

    #### `inst : instance of Raw or Evoked or Epochs`
        Instance with modified data.
    """
    ...
