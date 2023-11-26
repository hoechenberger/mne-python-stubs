from ..utils import fill_doc as fill_doc, logger as logger, warn as warn
from .constants import FIFF as FIFF

def get_channel_type_constants(include_defaults: bool = False):
    """## 🧠 Return all known channel types, and associated FIFF constants.

    -----
    ### 🛠️ Parameters

    #### `include_defaults : bool`
        Whether to include default values for "unit" and "coil_type" for all
        entries (see Notes). Defaults are generally based on values normally
        present for a VectorView MEG system. Defaults to ``False``.

    -----
    ### ⏎ Returns

    #### `channel_types : dict`
        The keys are channel type strings, and the values are dictionaries of
        FIFF constants for "kind", and possibly "unit" and "coil_type".

    -----
    ### 📖 Notes

    Values which might vary within a channel type across real data
    recordings are excluded unless ``include_defaults=True``. For example,
    "ref_meg" channels may have coil type
    ``FIFFV_COIL_MAGNES_OFFDIAG_REF_GRAD``, ``FIFFV_COIL_VV_MAG_T3``, etc
    (depending on the recording system), so no "coil_type" entry is given
    for "ref_meg" unless ``include_defaults`` is requested.
    """
    ...

def channel_type(info, idx):
    """## 🧠 Get channel type.

    -----
    ### 🛠️ Parameters


    #### `info : mne.Info`
        The `mne.Info` object with information about the sensors and methods of measurement.
    #### `idx : int`
        Index of channel.

    -----
    ### ⏎ Returns

    #### `type : str`
        Type of channel. Will be one of::

            {'grad', 'mag', 'eeg', 'csd', 'stim', 'eog', 'emg', 'ecg',
             'ref_meg', 'resp', 'exci', 'ias', 'syst', 'misc', 'seeg', 'dbs',
              'bio', 'chpi', 'dipole', 'gof', 'ecog', 'hbo', 'hbr',
              'temperature', 'gsr', 'eyetrack'}
    """
    ...

def pick_channels(ch_names, include, exclude=[], ordered=None, *, verbose=None):
    """## 🧠 Pick channels by names.

    Returns the indices of ``ch_names`` in ``include`` but not in ``exclude``.

    -----
    ### 🛠️ Parameters

    #### `ch_names : list of str`
        List of channels.
    #### `include : list of str`
        List of channels to include (if empty include all available).

        ### 💡 Note This is to be treated as a set. The order of this list
           is not used or maintained in ``sel``.

    #### `exclude : list of str`
        List of channels to exclude (if empty do not exclude any channel).
        Defaults to [].

    #### `ordered : bool`
        If True (default False), ensure that the order of the channels in
        the modified instance matches the order of ``ch_names``.

        ✨ Added in vesion 0.20.0
        🎭 Changed in version 1.5
            The default changed from False in 1.4 to True in 1.5.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `sel : array of int`
        Indices of good channels.

    -----
    ### 👉 See Also

    pick_channels_regexp, pick_types
    """
    ...

def pick_channels_regexp(ch_names, regexp):
    """## 🧠 Pick channels using regular expression.

    Returns the indices of the good channels in ch_names.

    -----
    ### 🛠️ Parameters

    #### `ch_names : list of str`
        List of channels.

    #### `regexp : str`
        The regular expression. See python standard module for regular
        expressions.

    -----
    ### ⏎ Returns

    #### `sel : array of int`
        Indices of good channels.

    -----
    ### 👉 See Also

    pick_channels

    -----
    ### 🖥️ Examples

    >>> pick_channels_regexp(['MEG 2331', 'MEG 2332', 'MEG 2333'], 'MEG ...1')
    [0]
    >>> pick_channels_regexp(['MEG 2331', 'MEG 2332', 'MEG 2333'], 'MEG *')
    [0, 1, 2]
    """
    ...

def pick_types(
    info,
    meg: bool = False,
    eeg: bool = False,
    stim: bool = False,
    eog: bool = False,
    ecg: bool = False,
    emg: bool = False,
    ref_meg: str = "auto",
    *,
    misc: bool = False,
    resp: bool = False,
    chpi: bool = False,
    exci: bool = False,
    ias: bool = False,
    syst: bool = False,
    seeg: bool = False,
    dipole: bool = False,
    gof: bool = False,
    bio: bool = False,
    ecog: bool = False,
    fnirs: bool = False,
    csd: bool = False,
    dbs: bool = False,
    temperature: bool = False,
    gsr: bool = False,
    eyetrack: bool = False,
    include=(),
    exclude: str = "bads",
    selection=None,
):
    """## 🧠 Pick channels by type and names.

    -----
    ### 🛠️ Parameters


    #### `info : mne.Info`
        The `mne.Info` object with information about the sensors and methods of measurement.

    #### `meg : bool | str`
        If True include MEG channels. If string it can be 'mag', 'grad',
        'planar1' or 'planar2' to select only magnetometers, all
        gradiometers, or a specific type of gradiometer.
    #### `eeg : bool`
        If True include EEG channels.
    #### `stim : bool`
        If True include stimulus channels.
    #### `eog : bool`
        If True include EOG channels.
    #### `ecg : bool`
        If True include ECG channels.
    #### `emg : bool`
        If True include EMG channels.
    #### `ref_meg : bool | str`
        If True include CTF / 4D reference channels. If 'auto', reference
        channels are included if compensations are present and ``meg`` is
        not False. Can also be the string options for the ``meg``
        parameter.
    #### `misc : bool`
        If True include miscellaneous analog channels.
    #### `resp : bool`
        If ``True`` include respiratory channels.
    #### `chpi : bool`
        If True include continuous HPI coil channels.
    #### `exci : bool`
        Flux excitation channel used to be a stimulus channel.
    #### `ias : bool`
        Internal Active Shielding data (maybe on Triux only).
    #### `syst : bool`
        System status channel information (on Triux systems only).
    #### `seeg : bool`
        Stereotactic EEG channels.
    #### `dipole : bool`
        Dipole time course channels.
    #### `gof : bool`
        Dipole goodness of fit channels.
    #### `bio : bool`
        Bio channels.
    #### `ecog : bool`
        Electrocorticography channels.
    #### `fnirs : bool | str`
        Functional near-infrared spectroscopy channels. If True include all
        fNIRS channels. If False (default) include none. If string it can
        be 'hbo' (to include channels measuring oxyhemoglobin) or 'hbr' (to
        include channels measuring deoxyhemoglobin).
    #### `csd : bool`
        EEG-CSD channels.
    #### `dbs : bool`
        Deep brain stimulation channels.
    #### `temperature : bool`
        Temperature channels.
    #### `gsr : bool`
        Galvanic skin response channels.
    #### `eyetrack : bool | str`
        Eyetracking channels. If True include all eyetracking channels. If False
        (default) include none. If string it can be 'eyegaze' (to include
        eye position channels) or 'pupil' (to include pupil-size
        channels).
    #### `include : list of str`
        List of additional channels to include. If empty do not include
        any.
    #### `exclude : list of str | str`
        List of channels to exclude. If 'bads' (default), exclude channels
        in ``info['bads']``.
    #### `selection : list of str`
        Restrict sensor channels (MEG, EEG, etc.) to this list of channel names.

    -----
    ### ⏎ Returns

    #### `sel : array of int`
        Indices of good channels.
    """
    ...

def pick_info(info, sel=(), copy: bool = True, verbose=None):
    """## 🧠 Restrict an info structure to a selection of channels.

    -----
    ### 🛠️ Parameters


    #### `info : mne.Info`
        The `mne.Info` object with information about the sensors and methods of measurement.
    #### `sel : list of int | None`
        Indices of channels to include. If None, all channels
        are included.
    #### `copy : bool`
        If copy is False, info is modified inplace.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `res : dict`
        Info structure restricted to a selection of channels.
    """
    ...

def pick_channels_forward(
    orig, include=[], exclude=[], ordered=None, copy: bool = True, *, verbose=None
):
    """## 🧠 Pick channels from forward operator.

    -----
    ### 🛠️ Parameters

    #### `orig : dict`
        A forward solution.
    #### `include : list of str`
        List of channels to include (if empty, include all available).
        Defaults to [].
    #### `exclude : list of str | 'bads'`
        Channels to exclude (if empty, do not exclude any). Defaults to [].
        If 'bads', then exclude bad channels in orig.

    #### `ordered : bool`
        If True (default False), ensure that the order of the channels in
        the modified instance matches the order of ``ch_names``.

        ✨ Added in vesion 0.20.0
        🎭 Changed in version 1.5
            The default changed from False in 1.4 to True in 1.5.
    #### `copy : bool`
        If True (default), make a copy.

        ✨ Added in vesion 0.19

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `res : dict`
        Forward solution restricted to selected channels. If include and
        exclude are empty it returns orig without copy.
    """
    ...

def pick_types_forward(
    orig,
    meg: bool = False,
    eeg: bool = False,
    ref_meg: bool = True,
    seeg: bool = False,
    ecog: bool = False,
    dbs: bool = False,
    include=[],
    exclude=[],
):
    """## 🧠 Pick by channel type and names from a forward operator.

    -----
    ### 🛠️ Parameters

    #### `orig : dict`
        A forward solution.
    #### `meg : bool | str`
        If True include MEG channels. If string it can be 'mag', 'grad',
        'planar1' or 'planar2' to select only magnetometers, all gradiometers,
        or a specific type of gradiometer.
    #### `eeg : bool`
        If True include EEG channels.
    #### `ref_meg : bool`
        If True include CTF / 4D reference channels.
    #### `seeg : bool`
        If True include stereotactic EEG channels.
    #### `ecog : bool`
        If True include electrocorticography channels.
    #### `dbs : bool`
        If True include deep brain stimulation channels.
    #### `include : list of str`
        List of additional channels to include. If empty do not include any.
    #### `exclude : list of str | str`
        List of channels to exclude. If empty do not exclude any (default).
        If 'bads', exclude channels in orig['info']['bads'].

    -----
    ### ⏎ Returns

    #### `res : dict`
        Forward solution restricted to selected channel types.
    """
    ...

def channel_indices_by_type(info, picks=None):
    """## 🧠 Get indices of channels by type.

    -----
    ### 🛠️ Parameters


    #### `info : mne.Info`
        The `mne.Info` object with information about the sensors and methods of measurement.
    #### `picks : str | array-like | slice | None`
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick all channels. Note that channels in
        ``info['bads']`` *will be included* if their names or indices are
        explicitly provided.

    -----
    ### ⏎ Returns

    #### `idx_by_type : dict`
        A dictionary that maps each channel type to a (possibly empty) list of
        channel indices.
    """
    ...

def pick_channels_cov(
    orig,
    include=[],
    exclude: str = "bads",
    ordered=None,
    copy: bool = True,
    *,
    verbose=None,
):
    """## 🧠 Pick channels from covariance matrix.

    -----
    ### 🛠️ Parameters

    #### `orig : Covariance`
        A covariance.
    #### `include : list of str, (optional)`
        List of channels to include (if empty, include all available).
    #### `exclude : list of str, (optional) | 'bads'`
        Channels to exclude (if empty, do not exclude any). Defaults to 'bads'.

    #### `ordered : bool`
        If True (default False), ensure that the order of the channels in
        the modified instance matches the order of ``ch_names``.

        ✨ Added in vesion 0.20.0
        🎭 Changed in version 1.5
            The default changed from False in 1.4 to True in 1.5.
    #### `copy : bool`
        If True (the default), return a copy of the covariance matrix with the
        modified channels. If False, channels are modified in-place.

        ✨ Added in vesion 0.20.0

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `res : dict`
        Covariance solution restricted to selected channels.
    """
    ...
