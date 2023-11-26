from .._fiff.constants import FIFF as FIFF
from .._fiff.meas_info import (
    Info as Info,
    MontageMixin as MontageMixin,
    create_info as create_info,
)
from .._fiff.pick import (
    channel_indices_by_type as channel_indices_by_type,
    channel_type as channel_type,
    pick_channels as pick_channels,
    pick_info as pick_info,
    pick_types as pick_types,
)
from .._fiff.proj import setup_proj as setup_proj
from .._fiff.reference import (
    add_reference_channels as add_reference_channels,
    set_eeg_reference as set_eeg_reference,
)
from ..defaults import HEAD_SIZE_DEFAULT as HEAD_SIZE_DEFAULT
from ..utils import (
    fill_doc as fill_doc,
    legacy as legacy,
    logger as logger,
    warn as warn,
)
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Union

def equalize_channels(instances, copy: bool = True, verbose=None):
    """### Equalize channel picks and ordering across multiple MNE-Python objects.

    First, all channels that are not common to each object are dropped. Then,
    using the first object in the list as a template, the channels of each
    object are re-ordered to match the template. The end result is that all
    given objects define the same channels, in the same order.

    ### 🛠️ Parameters
    ----------
    instances : list
        A list of MNE-Python objects to equalize the channels for. Objects can
        be of type Raw, Epochs, Evoked, AverageTFR, Forward, Covariance,
        CrossSpectralDensity or Info.
    copy : bool
        When dropping and/or re-ordering channels, an object will be copied
        when this parameter is set to ``True``. When set to ``False`` (the
        default) the dropping and re-ordering of channels happens in-place.

        ✨ Added in vesion 0.20.0

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    equalized_instances : list
        A list of MNE-Python objects that have the same channels defined in the
        same order.

    ### 📖 Notes
    -----
    This function operates inplace.
    """
    ...

def unify_bad_channels(insts):
    """### Unify bad channels across a list of instances.

    All instances must be of the same type and have matching channel names and channel
    order. The ``.info["bads"]`` of each instance will be set to the union of
    ``.info["bads"]`` across all instances.

    ### 🛠️ Parameters
    ----------
    insts : list
        List of instances (`mne.io.Raw`, `mne.Epochs`,
        `mne.Evoked`, `mne.time_frequency.Spectrum`,
        `mne.time_frequency.EpochsSpectrum`) across which to unify bad channels.

    ### ⏎ Returns
    -------
    insts : list
        List of instances with bad channels unified across instances.

    ### 👉 See Also
    --------
    mne.channels.equalize_channels
    mne.channels.rename_channels
    mne.channels.combine_channels

    ### 📖 Notes
    -----
    This function modifies the instances in-place.

    ✨ Added in vesion 1.6
    """
    ...

class ReferenceMixin(MontageMixin):
    """### Mixin class for Raw, Evoked, Epochs."""

    def set_eeg_reference(
        self,
        ref_channels: str = "average",
        projection: bool = False,
        ch_type: str = "auto",
        forward=None,
        *,
        joint: bool = False,
        verbose=None,
    ):
        """### Specify which reference to use for EEG data.

        Use this function to explicitly specify the desired reference for EEG.
        This can be either an existing electrode or a new virtual channel.
        This function will re-reference the data according to the desired
        reference.

        ### 🛠️ Parameters
        ----------

        ref_channels : list of str | str
            Can be:

            - The name(s) of the channel(s) used to construct the reference.
            - ``'average'`` to apply an average reference (default)
            - ``'REST'`` to use the Reference Electrode Standardization Technique
              infinity reference :footcite:`Yao2001`.
            - An empty list, in which case MNE will not attempt any re-referencing of
              the data

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

            ✨ Added in vesion 0.19
            🎭 Changed in version 1.2
               ``list-of-str`` is now supported with ``projection=True``.

        forward : instance of Forward | None
            Forward solution to use. Only used with ``ref_channels='REST'``.

            ✨ Added in vesion 0.21

        joint : bool
            How to handle list-of-str ``ch_type``. If False (default), one projector
            is created per channel type. If True, one projector is created across
            all channel types. This is only used when ``projection=True``.

            ✨ Added in vesion 1.2

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        ### ⏎ Returns
        -------
        inst : instance of Raw | Epochs | Evoked
            Data with EEG channels re-referenced. If ``ref_channels='average'``
            and ``projection=True`` a projection will be added instead of
            directly re-referencing the data.

        ### 👉 See Also
        --------
        mne.set_bipolar_reference : Convenience function for creating bipolar
                                references.

        ### 📖 Notes
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

        ✨ Added in vesion 0.9.0

        References
        ----------
        .. footbibliography::
        """
        ...

class UpdateChannelsMixin:
    """### Mixin class for Raw, Evoked, Epochs, Spectrum, AverageTFR."""

    def pick_types(
        self,
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
        verbose=None,
    ):
        """### ### ⛔️ Warning LEGACY: New code should use inst.pick(...).

        Pick some channels by type and names.

        ### 🛠️ Parameters
        ----------

        meg : bool | str
            If True include MEG channels. If string it can be 'mag', 'grad',
            'planar1' or 'planar2' to select only magnetometers, all
            gradiometers, or a specific type of gradiometer.
        eeg : bool
            If True include EEG channels.
        stim : bool
            If True include stimulus channels.
        eog : bool
            If True include EOG channels.
        ecg : bool
            If True include ECG channels.
        emg : bool
            If True include EMG channels.
        ref_meg : bool | str
            If True include CTF / 4D reference channels. If 'auto', reference
            channels are included if compensations are present and ``meg`` is
            not False. Can also be the string options for the ``meg``
            parameter.
        misc : bool
            If True include miscellaneous analog channels.
        resp : bool
            If ``True`` include respiratory channels.
        chpi : bool
            If True include continuous HPI coil channels.
        exci : bool
            Flux excitation channel used to be a stimulus channel.
        ias : bool
            Internal Active Shielding data (maybe on Triux only).
        syst : bool
            System status channel information (on Triux systems only).
        seeg : bool
            Stereotactic EEG channels.
        dipole : bool
            Dipole time course channels.
        gof : bool
            Dipole goodness of fit channels.
        bio : bool
            Bio channels.
        ecog : bool
            Electrocorticography channels.
        fnirs : bool | str
            Functional near-infrared spectroscopy channels. If True include all
            fNIRS channels. If False (default) include none. If string it can
            be 'hbo' (to include channels measuring oxyhemoglobin) or 'hbr' (to
            include channels measuring deoxyhemoglobin).
        csd : bool
            EEG-CSD channels.
        dbs : bool
            Deep brain stimulation channels.
        temperature : bool
            Temperature channels.
        gsr : bool
            Galvanic skin response channels.
        eyetrack : bool | str
            Eyetracking channels. If True include all eyetracking channels. If False
            (default) include none. If string it can be 'eyegaze' (to include
            eye position channels) or 'pupil' (to include pupil-size
            channels).
        include : list of str
            List of additional channels to include. If empty do not include
            any.
        exclude : list of str | str
            List of channels to exclude. If 'bads' (default), exclude channels
            in ``info['bads']``.
        selection : list of str
            Restrict sensor channels (MEG, EEG, etc.) to this list of channel names.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        ### ⏎ Returns
        -------
        inst : instance of Raw, Epochs, or Evoked
            The modified instance.

        ### 👉 See Also
        --------
        pick_channels

        ### 📖 Notes
        -----
        ✨ Added in vesion 0.9.0
        """
        ...
    def pick_channels(self, ch_names, ordered=None, *, verbose=None):
        """### ### ⛔️ Warning LEGACY: New code should use inst.pick(...).

        Pick some channels.

        ### 🛠️ Parameters
        ----------
        ch_names : list
            The list of channels to select.

        ordered : bool
            If True (default False), ensure that the order of the channels in
            the modified instance matches the order of ``ch_names``.

            ✨ Added in vesion 0.20.0
            🎭 Changed in version 1.5
                The default changed from False in 1.4 to True in 1.5.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

            ✨ Added in vesion 1.1

        ### ⏎ Returns
        -------
        inst : instance of Raw, Epochs, or Evoked
            The modified instance.

        ### 👉 See Also
        --------
        drop_channels
        pick_types
        reorder_channels

        ### 📖 Notes
        -----
        The channel names given are assumed to be a set, i.e. the order
        does not matter. The original order of the channels is preserved.
        You can use ``reorder_channels`` to set channel order if necessary.

        ✨ Added in vesion 0.9.0
        """
        ...
    def pick(self, picks, exclude=(), *, verbose=None):
        """### Pick a subset of channels.

        ### 🛠️ Parameters
        ----------
        picks : str | array-like | slice | None
            Channels to include. Slices and lists of integers will be interpreted as
            channel indices. In lists, channel *type* strings (e.g., ``['meg',
            'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
            string values "all" to pick all channels, or "data" to pick :term:`data
            channels`. None (default) will pick all channels. Note that channels in
            ``info['bads']`` *will be included* if their names or indices are
            explicitly provided.
        exclude : list | str
            Set of channels to exclude, only used when picking based on
            types (e.g., exclude="bads" when picks="meg").

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

            ✨ Added in vesion 0.24.0

        ### ⏎ Returns
        -------
        inst : instance of Raw, Epochs, or Evoked
            The modified instance.
        """
        ...
    def reorder_channels(self, ch_names):
        """### Reorder channels.

        ### 🛠️ Parameters
        ----------
        ch_names : list
            The desired channel order.

        ### ⏎ Returns
        -------
        inst : instance of Raw, Epochs, or Evoked
            The modified instance.

        ### 👉 See Also
        --------
        drop_channels
        pick_types
        pick_channels

        ### 📖 Notes
        -----
        Channel names must be unique. Channels that are not in ``ch_names``
        are dropped.

        ✨ Added in vesion 0.16.0
        """
        ...
    def drop_channels(self, ch_names, on_missing: str = "raise"):
        """### Drop channel(s).

        ### 🛠️ Parameters
        ----------
        ch_names : iterable or str
            Iterable (e.g. list) of channel name(s) or channel name to remove.

        on_missing : 'raise' | 'warn' | 'ignore'
            Can be ``'raise'`` (default) to raise an error, ``'warn'`` to emit a
            warning, or ``'ignore'`` to ignore when entries in ch_names are not present in the raw instance.

            ✨ Added in vesion 0.23.0

        ### ⏎ Returns
        -------
        inst : instance of Raw, Epochs, or Evoked
            The modified instance.

        ### 👉 See Also
        --------
        reorder_channels
        pick_channels
        pick_types

        ### 📖 Notes
        -----
        ✨ Added in vesion 0.9.0
        """
        ...
    info: Incomplete
    picks: Incomplete

    def add_channels(self, add_list, force_update_info: bool = False):
        """### Append new channels to the instance.

        ### 🛠️ Parameters
        ----------
        add_list : list
            A list of objects to append to self. Must contain all the same
            type as the current object.
        force_update_info : bool
            If True, force the info for objects to be appended to match the
            values in ``self``. This should generally only be used when adding
            stim channels for which important metadata won't be overwritten.

            ✨ Added in vesion 0.12

        ### ⏎ Returns
        -------
        inst : instance of Raw, Epochs, or Evoked
            The modified instance.

        ### 👉 See Also
        --------
        drop_channels

        ### 📖 Notes
        -----
        If ``self`` is a Raw instance that has been preloaded into a
        :obj:`numpy.memmap` instance, the memmap will be resized.
        """
        ...
    def add_reference_channels(self, ref_channels):
        """### Add reference channels to data that consists of all zeros.

        Adds reference channels to data that were not included during
        recording. This is useful when you need to re-reference your data
        to different channels. These added channels will consist of all zeros.

        ### 🛠️ Parameters
        ----------

        ref_channels : str | list of str
            Name of the electrode(s) which served as the reference in the
            recording. If a name is provided, a corresponding channel is added
            and its data is set to 0. This is useful for later re-referencing.

        ### ⏎ Returns
        -------
        inst : instance of Raw | Epochs | Evoked
               The modified instance.
        """
        ...

class InterpolationMixin:
    """### Mixin class for Raw, Evoked, Epochs."""

    def interpolate_bads(
        self,
        reset_bads: bool = True,
        mode: str = "accurate",
        origin: str = "auto",
        method=None,
        exclude=(),
        verbose=None,
    ):
        """### Interpolate bad MEG and EEG channels.

        Operates in place.

        ### 🛠️ Parameters
        ----------
        reset_bads : bool
            If True, remove the bads from info.
        mode : str
            Either ``'accurate'`` or ``'fast'``, determines the quality of the
            Legendre polynomial expansion used for interpolation of channels
            using the minimum-norm method.
        origin : array-like, shape (3,) | str
            Origin of the sphere in the head coordinate frame and in meters.
            Can be ``'auto'`` (default), which means a head-digitization-based
            origin fit.

            ✨ Added in vesion 0.17
        method : dict | str | None
            Method to use for each channel type.

            - ``"meg"`` channels support ``"MNE"`` (default) and ``"nan"``
            - ``"eeg"`` channels support ``"spline"`` (default), ``"MNE"`` and ``"nan"``
            - ``"fnirs"`` channels support ``"nearest"`` (default) and ``"nan"``

            None is an alias for::

                method=dict(meg="MNE", eeg="spline", fnirs="nearest")

            If a `str` is provided, the method will be applied to all channel
            types supported and available in the instance. The method ``"nan"`` will
            replace the channel data with ``np.nan``.

            ### ⛔️ Warning
                Be careful when using ``method="nan"``; the default value
                ``reset_bads=True`` may not be what you want.

            ✨ Added in vesion 0.21
        exclude : list | tuple
            The channels to exclude from interpolation. If excluded a bad
            channel will stay in bads.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        ### ⏎ Returns
        -------
        inst : instance of Raw, Epochs, or Evoked
            The modified instance.

        ### 📖 Notes
        -----
        The ``"MNE"`` method uses minimum-norm projection to a sphere and back.

        ✨ Added in vesion 0.9.0
        """
        ...

def rename_channels(
    info, mapping, allow_duplicates: bool = False, *, verbose=None
) -> None:
    """### Rename channels.

    ### 🛠️ Parameters
    ----------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement. Note: modified in place.

    mapping : dict | callable
        A dictionary mapping the old channel to a new channel name
        e.g. ``{'EEG061' : 'EEG161'}``. Can also be a callable function
        that takes and returns a string.

        🎭 Changed in version 0.10.0
           Support for a callable function.
    allow_duplicates : bool
        If True (default False), allow duplicates, which will automatically
        be renamed with ``-N`` at the end.

        ✨ Added in vesion 0.22.0

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.
    """
    ...

@dataclass
class _BuiltinChannelAdjacency:
    name: str
    description: str
    fname: str
    source_url: Union[str, None]

    def __init__(self, name, description, fname, source_url) -> None: ...

def get_builtin_ch_adjacencies(*, descriptions: bool = False):
    """### Get a list of all FieldTrip neighbor definitions shipping with MNE.

    The names of the these neighbor definitions can be passed to
    `read_ch_adjacency`.

    ### 🛠️ Parameters
    ----------
    descriptions : bool
        Whether to return not only the neighbor definition names, but also
        their corresponding descriptions. If ``True``, a list of tuples is
        returned, where the first tuple element is the neighbor definition name
        and the second is the description. If ``False`` (default), only the
        names are returned.

    ### ⏎ Returns
    -------
    neighbor_name : list of str | list of tuple
        If ``descriptions=False``, the names of all builtin FieldTrip neighbor
        definitions that can be loaded directly via `read_ch_adjacency`.

        If ``descriptions=True``, a list of tuples ``(name, description)``.

    ### 📖 Notes
    -----
    ✨ Added in vesion 1.1
    """
    ...

def read_ch_adjacency(fname, picks=None):
    """### Read a channel adjacency ("neighbors") file that ships with MNE.

    More information on these neighbor definitions can be found on the related
    `FieldTrip documentation pages
    <http://www.fieldtriptoolbox.org/template/neighbours/>`__.

    ### 🛠️ Parameters
    ----------
    fname : path-like | str
        The path to the file to load, or the name of a channel adjacency
        matrix that ships with MNE-Python.

        ### 💡 Note
            You can retrieve the names of all
            built-in channel adjacencies via
            `mne.channels.get_builtin_ch_adjacencies`.
    picks : list of int | list of str | slice | None
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *name* strings (e.g., ``['MEG0111',
        'MEG2623']`` will pick the given channels. None (default) will pick all
        channels. Note that channels in ``info['bads']`` *will be included* if
        their names or indices are explicitly provided.

    ### ⏎ Returns
    -------
    ch_adjacency : scipy.sparse.csr_matrix, shape (n_channels, n_channels)
        The adjacency matrix.
    ch_names : list
        The list of channel names present in adjacency matrix.

    ### 👉 See Also
    --------
    get_builtin_ch_adjacencies
    mne.viz.plot_ch_adjacency
    find_ch_adjacency
    mne.stats.combine_adjacency

    ### 📖 Notes
    -----
    If the neighbor definition you need is not shipped by MNE-Python,
    you may use `find_ch_adjacency` to compute the
    adjacency matrix based on your 2D sensor locations.

    Note that depending on your use case, you may need to additionally use
    `mne.stats.combine_adjacency` to prepare a final "adjacency"
    to pass to the eventual function.
    """
    ...

def find_ch_adjacency(info, ch_type):
    """### Find the adjacency matrix for the given channels.

    This function tries to infer the appropriate adjacency matrix template
    for the given channels. If a template is not found, the adjacency matrix
    is computed using Delaunay triangulation based on 2D sensor locations.

    ### 🛠️ Parameters
    ----------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    ch_type : str | None
        The channel type for computing the adjacency matrix. Currently
        supports ``'mag'``, ``'grad'``, ``'eeg'`` and ``None``.
        If ``None``, the info must contain only one channel type.

    ### ⏎ Returns
    -------
    ch_adjacency : scipy.sparse.csr_matrix, shape (n_channels, n_channels)
        The adjacency matrix.
    ch_names : list
        The list of channel names present in adjacency matrix.

    ### 👉 See Also
    --------
    mne.viz.plot_ch_adjacency
    mne.stats.combine_adjacency
    get_builtin_ch_adjacencies
    read_ch_adjacency

    ### 📖 Notes
    -----
    ✨ Added in vesion 0.15

    Automatic detection of an appropriate adjacency matrix template only
    works for MEG data at the moment. This means that the adjacency matrix
    is always computed for EEG data and never loaded from a template file. If
    you want to load a template for a given montage use
    `read_ch_adjacency` directly.

    ### ⛔️ Warning
        If Delaunay triangulation is used to calculate the adjacency matrix it
        may yield partially unexpected results (e.g., include unwanted edges
        between non-adjacent sensors). Therefore, it is recommended to check
        (and, if necessary, manually modify) the result by inspecting it
        via `mne.viz.plot_ch_adjacency`.

    Note that depending on your use case, you may need to additionally use
    `mne.stats.combine_adjacency` to prepare a final "adjacency"
    to pass to the eventual function.
    """
    ...

def fix_mag_coil_types(info, use_cal: bool = False) -> None:
    """### Fix magnetometer coil types.

    ### 🛠️ Parameters
    ----------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement. Corrections are done in-place.
    use_cal : bool
        If True, further refine the check for old coil types by checking
        ``info['chs'][ii]['cal']``.

    ### 📖 Notes
    -----
    This function changes magnetometer coil types 3022 (T1: SQ20483N) and
    3023 (T2: SQ20483-A) to 3024 (T3: SQ20950N) in the channel definition
    records in the info structure.

    Neuromag Vectorview systems can contain magnetometers with two
    different coil sizes (3022 and 3023 vs. 3024). The systems
    incorporating coils of type 3024 were introduced last and are used at
    the majority of MEG sites. At some sites with 3024 magnetometers,
    the data files have still defined the magnetometers to be of type
    3022 to ensure compatibility with older versions of Neuromag software.
    In the MNE software as well as in the present version of Neuromag
    software coil type 3024 is fully supported. Therefore, it is now safe
    to upgrade the data files to use the true coil type.

    ### 💡 Note The effect of the difference between the coil sizes on the
              current estimates computed by the MNE software is very small.
              Therefore the use of ``fix_mag_coil_types`` is not mandatory.
    """
    ...

def make_1020_channel_selections(
    info, midline: str = "z", *, return_ch_names: bool = False
):
    """### Map hemisphere names to corresponding EEG channel names or indices.

    This function uses a simple heuristic to separate channel names into three
    Region of Interest-based selections: ``Left``, ``Midline`` and ``Right``.

    The heuristic is that any of the channel names ending
    with odd numbers are filed under ``Left``; those ending with even numbers
    are filed under ``Right``; and those ending with the character(s) specified
    in ``midline`` are filed under ``Midline``. Other channels are ignored.

    This is appropriate for 10/20, 10/10, 10/05, …, sensor arrangements, but
    not for other naming conventions.

    ### 🛠️ Parameters
    ----------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement. If channel locations are present, the channel lists will
        be sorted from posterior to anterior; otherwise, the order specified in
        ``info["ch_names"]`` will be kept.
    midline : str
        Names ending in any of these characters are stored under the
        ``Midline`` key. Defaults to ``'z'``. Capitalization is ignored.
    return_ch_names : bool
        Whether to return channel names instead of channel indices.

        ✨ Added in vesion 1.4.0

    ### ⏎ Returns
    -------
    selections : dict
        A dictionary mapping from region of interest name to a list of channel
        indices (if ``return_ch_names=False``) or to a list of channel names
        (if ``return_ch_names=True``).
    """
    ...

def combine_channels(
    inst,
    groups,
    method: str = "mean",
    keep_stim: bool = False,
    drop_bad: bool = False,
    verbose=None,
):
    """### Combine channels based on specified channel grouping.

    ### 🛠️ Parameters
    ----------
    inst : instance of Raw, Epochs, or Evoked
        An MNE-Python object to combine the channels for. The object can be of
        type Raw, Epochs, or Evoked.
    groups : dict
        Specifies which channels are aggregated into a single channel, with
        aggregation method determined by the ``method`` parameter. One new
        pseudo-channel is made per dict entry; the dict values must be lists of
        picks (integer indices of ``ch_names``). For example::

            groups=dict(Left=[1, 2, 3, 4], Right=[5, 6, 7, 8])

        Note that within a dict entry all channels must have the same type.
    method : str | callable
        Which method to use to combine channels. If a `str`, must be one
        of 'mean', 'median', or 'std' (standard deviation). If callable, the
        callable must accept one positional input (data of shape ``(n_channels,
        n_times)``, or ``(n_epochs, n_channels, n_times)``) and return an
        `array <numpy.ndarray>` of shape ``(n_times,)``, or ``(n_epochs,
        n_times)``. For example with an instance of Raw or Evoked::

            method = lambda data: np.mean(data, axis=0)

        Another example with an instance of Epochs::

            method = lambda data: np.median(data, axis=1)

        Defaults to ``'mean'``.
    keep_stim : bool
        If ``True``, include stimulus channels in the resulting object.
        Defaults to ``False``.
    drop_bad : bool
        If ``True``, drop channels marked as bad before combining. Defaults to
        ``False``.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    combined_inst : instance of Raw, Epochs, or Evoked
        An MNE-Python object of the same type as the input ``inst``, containing
        one virtual channel for each group in ``groups`` (and, if ``keep_stim``
        is ``True``, also containing stimulus channels).
    """
    ...

def read_vectorview_selection(name, fname=None, info=None, verbose=None):
    """### Read Neuromag Vector View channel selection from a file.

    ### 🛠️ Parameters
    ----------
    name : str | list of str
        Name of the selection. If a list, the selections are combined.
        Supported selections are: ``'Vertex'``, ``'Left-temporal'``,
        ``'Right-temporal'``, ``'Left-parietal'``, ``'Right-parietal'``,
        ``'Left-occipital'``, ``'Right-occipital'``, ``'Left-frontal'`` and
        ``'Right-frontal'``. Selections can also be matched and combined by
        spcecifying common substrings. For example, ``name='temporal`` will
        produce a combination of ``'Left-temporal'`` and ``'Right-temporal'``.
    fname : path-like
        Filename of the selection file (if ``None``, built-in selections are
        used).

    info : mne.Info | None
        The `mne.Info` object with information about the sensors and methods of measurement. Used to determine which channel naming convention to use, e.g.
        ``'MEG 0111'`` (with space) for old Neuromag systems and ``'MEG0111'``
        (without space) for new ones.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    sel : list of str
        List with channel names in the selection.
    """
    ...
