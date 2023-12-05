from ..defaults import DEFAULTS as DEFAULTS
from ..fixes import pinv as pinv
from ..utils import fill_doc as fill_doc, logger as logger, warn as warn
from .constants import FIFF as FIFF
from .pick import (
    pick_channels as pick_channels,
    pick_channels_forward as pick_channels_forward,
    pick_types as pick_types,
)
from .proj import (
    make_eeg_average_ref_proj as make_eeg_average_ref_proj,
    setup_proj as setup_proj,
)

def add_reference_channels(inst, ref_channels, copy: bool = True):
    """Add reference channels to data that consists of all zeros.

    Adds reference channels to data that were not included during recording.
    This is useful when you need to re-reference your data to different
    channels. These added channels will consist of all zeros.

    Parameters
    ----------
    inst : instance of Raw | Epochs | Evoked
        Instance of Raw or Epochs with EEG channels and reference channel(s).

    ref_channels : str | list of str
        Name of the electrode(s) which served as the reference in the
        recording. If a name is provided, a corresponding channel is added
        and its data is set to 0. This is useful for later re-referencing.
    copy : bool
        Specifies whether the data will be copied (True) or modified in-place
        (False). Defaults to True.

    Returns
    -------
    inst : instance of Raw | Epochs | Evoked
        Data with added EEG reference channels.

    Notes
    -----
    ⛔️
        When `re-referencing <tut-set-eeg-ref>`,
        make sure to apply the montage using `mne.io.Raw.set_montage`
        only after calling this function. Applying a montage will only set
        locations of channels that exist at the time it is applied.
    """
    ...

def set_eeg_reference(
    inst,
    ref_channels: str = "average",
    copy: bool = True,
    projection: bool = False,
    ch_type: str = "auto",
    forward=None,
    *,
    joint: bool = False,
    verbose=None,
):
    """Specify which reference to use for EEG data.

    Use this function to explicitly specify the desired reference for EEG.
    This can be either an existing electrode or a new virtual channel.
    This function will re-reference the data according to the desired
    reference.

    Note that it is also possible to re-reference the signal using a
    Laplacian (LAP) "reference-free" transformation using the
    `.compute_current_source_density` function.

    Parameters
    ----------
    inst : instance of Raw | Epochs | Evoked
        Instance of Raw or Epochs with EEG channels and reference channel(s).

    ref_channels : list of str | str
        Can be:

        - The name(s) of the channel(s) used to construct the reference.
        - ``'average'`` to apply an average reference (default)
        - ``'REST'`` to use the Reference Electrode Standardization Technique
          infinity reference :footcite:`Yao2001`.
        - An empty list, in which case MNE will not attempt any re-referencing of
          the data
    copy : bool
        Specifies whether the data will be copied (True) or modified in-place
        (False). Defaults to True.

    projection : bool
        If ``ref_channels='average'`` this argument specifies if the
        average reference should be computed as a projection (True) or not
        (False; default). If ``projection=True``, the average reference is
        added as a projection and is not applied to the data (it can be
        applied afterwards with the ``apply_proj`` method). If
        ``projection=False``, the average reference is directly applied to
        the data. If ``ref_channels`` is not ``'average'``, ``projection``
        must be set to ``False`` (the default in this case).

    ch_type : list of str | str
        The name of the channel type to apply the reference to.
        Valid channel types are ``'auto'``, ``'eeg'``, ``'ecog'``, ``'seeg'``,
        ``'dbs'``. If ``'auto'``, the first channel type of eeg, ecog, seeg or dbs
        that is found (in that order) will be selected.

        ✨ Added in version 0.19
        🎭 Changed in version 1.2
           ``list-of-str`` is now supported with ``projection=True``.

    forward : instance of Forward | None
        Forward solution to use. Only used with ``ref_channels='REST'``.

        ✨ Added in version 0.21

    joint : bool
        How to handle list-of-str ``ch_type``. If False (default), one projector
        is created per channel type. If True, one projector is created across
        all channel types. This is only used when ``projection=True``.

        ✨ Added in version 1.2

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    inst : instance of Raw | Epochs | Evoked
        Data with EEG channels re-referenced. If ``ref_channels='average'`` and
        ``projection=True`` a projection will be added instead of directly
        re-referencing the data.
    ref_data : array
        Array of reference data subtracted from EEG channels. This will be
        ``None`` if ``projection=True`` or ``ref_channels='REST'``.

    See Also
    --------
    mne.set_bipolar_reference : Convenience function for creating bipolar
                            references.

    Notes
    -----
    Some common referencing schemes and the corresponding value for the
    ``ref_channels`` parameter:

    - Average reference:
        A new virtual reference electrode is created by averaging the current
        EEG signal by setting ``ref_channels='average'``. Bad EEG channels are
        automatically excluded if they are properly set in ``info['bads']``.

    - A single electrode:
        Set ``ref_channels`` to a list containing the name of the channel that
        will act as the new reference, for example ``ref_channels=['Cz']``.

    - The mean of multiple electrodes:
        A new virtual reference electrode is created by computing the average
        of the current EEG signal recorded from two or more selected channels.
        Set ``ref_channels`` to a list of channel names, indicating which
        channels to use. For example, to apply an average mastoid reference,
        when using the 10-20 naming scheme, set ``ref_channels=['M1', 'M2']``.

    - REST
        The given EEG electrodes are referenced to a point at infinity using the
        lead fields in ``forward``, which helps standardize the signals.

    1. If a reference is requested that is not the average reference, this
       function removes any pre-existing average reference projections.

    2. During source localization, the EEG signal should have an average
       reference.

    3. In order to apply a reference, the data must be preloaded. This is not
       necessary if ``ref_channels='average'`` and ``projection=True``.

    4. For an average or REST reference, bad EEG channels are automatically
       excluded if they are properly set in ``info['bads']``.

    ✨ Added in version 0.9.0

    References
    ----------
    .. footbibliography::
    """
    ...

def set_bipolar_reference(
    inst,
    anode,
    cathode,
    ch_name=None,
    ch_info=None,
    drop_refs: bool = True,
    copy: bool = True,
    on_bad: str = "warn",
    verbose=None,
):
    """Re-reference selected channels using a bipolar referencing scheme.

    A bipolar reference takes the difference between two channels (the anode
    minus the cathode) and adds it as a new virtual channel. The original
    channels will be dropped by default.

    Multiple anodes and cathodes can be specified, in which case multiple
    virtual channels will be created. The 1st cathode will be subtracted
    from the 1st anode, the 2nd cathode from the 2nd anode, etc.

    By default, the virtual channels will be annotated with channel-info and
    -location of the anodes and coil types will be set to EEG_BIPOLAR.

    Parameters
    ----------
    inst : instance of Raw | Epochs | Evoked
        Data containing the unreferenced channels.
    anode : str | list of str
        The name(s) of the channel(s) to use as anode in the bipolar reference.
    cathode : str | list of str
        The name(s) of the channel(s) to use as cathode in the bipolar
        reference.
    ch_name : str | list of str | None
        The channel name(s) for the virtual channel(s) containing the resulting
        signal. By default, bipolar channels are named after the anode and
        cathode, but it is recommended to supply a more meaningful name.
    ch_info : dict | list of dict | None
        This parameter can be used to supply a dictionary (or a dictionary for
        each bipolar channel) containing channel information to merge in,
        overwriting the default values. Defaults to None.
    drop_refs : bool
        Whether to drop the anode/cathode channels from the instance.
    copy : bool
        Whether to operate on a copy of the data (True) or modify it in-place
        (False). Defaults to True.
    on_bad : str
        If a bipolar channel is created from a bad anode or a bad cathode, mne
        warns if on_bad="warns", raises ValueError if on_bad="raise", and does
        nothing if on_bad="ignore". For "warn" and "ignore", the new bipolar
        channel will be marked as bad. Defaults to on_bad="warns".

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    inst : instance of Raw | Epochs | Evoked
        Data with the specified channels re-referenced.

    See Also
    --------
    set_eeg_reference : Convenience function for creating an EEG reference.

    Notes
    -----
    1. If the anodes contain any EEG channels, this function removes
       any pre-existing average reference projections.

    2. During source localization, the EEG signal should have an average
       reference.

    3. The data must be preloaded.

    ✨ Added in version 0.9.0
    """
    ...
