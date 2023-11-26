from ..._fiff.pick import pick_types as pick_types
from ...utils import fill_doc as fill_doc

def source_detector_distances(info, picks=None):
    """### Determine the distance between NIRS source and detectors.

    -----
    ### 🛠️ Parameters


    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick all data channels. Note that channels
        in ``info['bads']`` *will be included* if their names or indices are
        explicitly provided.

    -----
    ### ⏎ Returns

    dists : array of float
        Array containing distances in meters.
        Of shape equal to number of channels, or shape of picks if supplied.
    """
    ...

def short_channels(info, threshold: float = 0.01):
    """### Determine which NIRS channels are short.

    Channels with a source to detector distance of less than
    ``threshold`` are reported as short. The default threshold is 0.01 m.

    -----
    ### 🛠️ Parameters


    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    threshold : float
        The threshold distance for what is considered short in meters.

    -----
    ### ⏎ Returns

    short : array of bool
        Array indicating which channels are short.
        Of shape equal to number of channels.
    """
    ...
