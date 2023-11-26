from .._fiff._digitization import write_dig as write_dig
from .._fiff.constants import CHANNEL_LOC_ALIASES as CHANNEL_LOC_ALIASES, FIFF as FIFF
from .._fiff.meas_info import create_info as create_info
from .._fiff.open import fiff_open as fiff_open
from .._fiff.pick import channel_type as channel_type, pick_types as pick_types
from .._freesurfer import get_mni_fiducials as get_mni_fiducials
from ..defaults import HEAD_SIZE_DEFAULT as HEAD_SIZE_DEFAULT
from ..transforms import (
    Transform as Transform,
    apply_trans as apply_trans,
    get_ras_to_neuromag_trans as get_ras_to_neuromag_trans,
)
from ..utils import (
    copy_function_doc_to_method_doc as copy_function_doc_to_method_doc,
    fill_doc as fill_doc,
    warn as warn,
)
from ..utils.docs import docdict as docdict
from ..viz import plot_montage as plot_montage
from _typeshed import Incomplete
from dataclasses import dataclass

@dataclass
class _BuiltinStandardMontage:
    name: str
    description: str

    def __init__(self, name, description) -> None: ...

def get_builtin_montages(*, descriptions: bool = False):
    """### Get a list of all standard montages shipping with MNE-Python.

    The names of the montages can be passed to `make_standard_montage`.

    -----
    ### 🛠️ Parameters

    descriptions : bool
        Whether to return not only the montage names, but also their
        corresponding descriptions. If ``True``, a list of tuples is returned,
        where the first tuple element is the montage name and the second is
        the montage description. If ``False`` (default), only the names are
        returned.

        ✨ Added in vesion 1.1

    -----
    ### ⏎ Returns

    montages : list of str | list of tuple
        If ``descriptions=False``, the names of all builtin montages that can
        be used by `make_standard_montage`.

        If ``descriptions=True``, a list of tuples ``(name, description)``.
    """
    ...

def make_dig_montage(
    ch_pos=None,
    nasion=None,
    lpa=None,
    rpa=None,
    hsp=None,
    hpi=None,
    coord_frame: str = "unknown",
):
    """### Make montage from arrays.

    -----
    ### 🛠️ Parameters

    ch_pos : dict | None
        Dictionary of channel positions. Keys are channel names and values
        are 3D coordinates - array of shape (3,) - in native digitizer space
        in m.
    nasion : None | array, shape (3,)
        The position of the nasion fiducial point.
        This point is assumed to be in the native digitizer space in m.
    lpa : None | array, shape (3,)
        The position of the left periauricular fiducial point.
        This point is assumed to be in the native digitizer space in m.
    rpa : None | array, shape (3,)
        The position of the right periauricular fiducial point.
        This point is assumed to be in the native digitizer space in m.
    hsp : None | array, shape (n_points, 3)
        This corresponds to an array of positions of the headshape points in
        3d. These points are assumed to be in the native digitizer space in m.
    hpi : None | array, shape (n_hpi, 3)
        This corresponds to an array of HPI points in the native digitizer
        space. They only necessary if computation of a ``compute_dev_head_t``
        is True.
    coord_frame : str
        The coordinate frame of the points. Usually this is ``'unknown'``
        for native digitizer space.
        Other valid values are: ``'head'``, ``'meg'``, ``'mri'``,
        ``'mri_voxel'``, ``'mni_tal'``, ``'ras'``, ``'fs_tal'``,
        ``'ctf_head'``, and ``'ctf_meg'``.

        ### 💡 Note
            For custom montages without fiducials, this parameter must be set
            to ``'head'``.

    -----
    ### ⏎ Returns

    montage : instance of DigMontage
        The montage.

    -----
    ### 👉 See Also

    DigMontage
    read_dig_captrak
    read_dig_egi
    read_dig_fif
    read_dig_localite
    read_dig_polhemus_isotrak
    """
    ...

class DigMontage:
    """### Montage for digitized electrode and headshape position data.

    ### ⛔️ Warning Montages are typically created using one of the helper
                 functions in the ``See Also`` section below instead of
                 instantiating this class directly.

    -----
    ### 🛠️ Parameters

    dig : list of dict
        The object containing all the dig points.
    ch_names : list of str
        The names of the EEG channels.

    -----
    ### 👉 See Also

    read_dig_captrak
    read_dig_dat
    read_dig_egi
    read_dig_fif
    read_dig_hpts
    read_dig_localite
    read_dig_polhemus_isotrak
    make_dig_montage

    -----
    ### 📖 Notes

    ✨ Added in vesion 0.9.0
    """

    dig: Incomplete
    ch_names: Incomplete

    def __init__(self, *, dig=None, ch_names=None) -> None: ...
    def plot(
        self,
        scale_factor: int = 20,
        show_names: bool = True,
        kind: str = "topomap",
        show: bool = True,
        sphere=None,
        *,
        axes=None,
        verbose=None,
    ):
        """### Plot a montage.

        -----
        ### 🛠️ Parameters

        scale_factor : float
            Determines the size of the points.
        show_names : bool | list
            Whether to display all channel names. If a list, only the channel
            names in the list are shown. Defaults to True.
        kind : str
            Whether to plot the montage as '3d' or 'topomap' (default).
        show : bool
            Show figure if True.
        sphere : float | array-like | instance of ConductorModel | None  | 'auto' | 'eeglab'
            The sphere parameters to use for the head outline. Can be array-like of
            shape (4,) to give the X/Y/Z origin and radius in meters, or a single float
            to give just the radius (origin assumed 0, 0, 0). Can also be an instance
            of a spherical `mne.bem.ConductorModel` to use the origin and
            radius from that object. If ``'auto'`` the sphere is fit to digitization
            points. If ``'eeglab'`` the head circle is defined by EEG electrodes
            ``'Fpz'``, ``'Oz'``, ``'T7'``, and ``'T8'`` (if ``'Fpz'`` is not present,
            it will be approximated from the coordinates of ``'Oz'``). ``None`` (the
            default) is equivalent to ``'auto'`` when enough extra digitization points
            are available, and (0, 0, 0, 0.095) otherwise.

            ✨ Added in vesion 0.20
            🎭 Changed in version 1.1 Added ``'eeglab'`` option.

        axes : instance of Axes | instance of Axes3D | None
            Axes to draw the sensors to. If ``kind='3d'``, axes must be an instance
            of Axes3D. If None (default), a new axes will be created.

            ✨ Added in vesion 1.4

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns

        fig : instance of matplotlib.figure.Figure
            The figure object.
        """
        ...
    def rename_channels(self, mapping, allow_duplicates: bool = False) -> None:
        """### Rename the channels.

        -----
        ### 🛠️ Parameters


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

        -----
        ### ⏎ Returns

        inst : instance of DigMontage
            The instance. Operates in-place.
        """
        ...
    def save(self, fname, *, overwrite: bool = False, verbose=None) -> None:
        """### Save digitization points to FIF.

        -----
        ### 🛠️ Parameters

        fname : path-like
            The filename to use. Should end in .fif or .fif.gz.

        overwrite : bool
            If True (default False), overwrite the destination file if it
            exists.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.
        """
        ...
    def __iadd__(self, other):
        """### Add two DigMontages in place.

        -----
        ### 📖 Notes

        Two DigMontages can only be added if there are no duplicated ch_names
        and if fiducials are present they should share the same coordinate
        system and location values.
        """
        ...
    def copy(self):
        """### Copy the DigMontage object.

        -----
        ### ⏎ Returns

        dig : instance of DigMontage
            The copied DigMontage instance.
        """
        ...
    def __add__(self, other):
        """### Add two DigMontages."""
        ...
    def __eq__(self, other):
        """### Compare different DigMontage objects for equality.

        -----
        ### ⏎ Returns

        Boolean output from comparison of .dig
        """
        ...
    def get_positions(self):
        """### Get all channel and fiducial positions.

        -----
        ### ⏎ Returns

        positions : dict
            A dictionary of the positions for channels (``ch_pos``),
            coordinate frame (``coord_frame``), nasion (``nasion``),
            left preauricular point (``lpa``),
            right preauricular point (``rpa``),
            Head Shape Polhemus (``hsp``), and
            Head Position Indicator(``hpi``).
            E.g.::

                {
                    'ch_pos': {'EEG061': [0, 0, 0]},
                    'nasion': [0, 0, 1],
                    'coord_frame': 'mni_tal',
                    'lpa': [0, 1, 0],
                    'rpa': [1, 0, 0],
                    'hsp': None,
                    'hpi': None
                }
        """
        ...
    def apply_trans(self, trans, verbose=None) -> None:
        """### Apply a transformation matrix to the montage.

        -----
        ### 🛠️ Parameters

        trans : instance of mne.transforms.Transform
            The transformation matrix to be applied.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.
        """
        ...
    def add_estimated_fiducials(self, subject, subjects_dir=None, verbose=None):
        """### Estimate fiducials based on FreeSurfer ``fsaverage`` subject.

        This takes a montage with the ``mri`` coordinate frame,
        corresponding to the FreeSurfer RAS (xyz in the volume) T1w
        image of the specific subject. It will call
        `mne.coreg.get_mni_fiducials` to estimate LPA, RPA and
        Nasion fiducial points.

        -----
        ### 🛠️ Parameters


        subject : str
            The FreeSurfer subject name.

        subjects_dir : path-like | None
            The path to the directory containing the FreeSurfer subjects
            reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
            variable.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns

        inst : instance of DigMontage
            The instance, modified in-place.

        -----
        ### 👉 See Also

        `tut-source-alignment`

        -----
        ### 📖 Notes

        Since MNE uses the FIF data structure, it relies on the ``head``
        coordinate frame. Any coordinate frame can be transformed
        to ``head`` if the fiducials (i.e. LPA, RPA and Nasion) are
        defined. One can use this function to estimate those fiducials
        and then use ``mne.channels.compute_native_head_t(montage)``
        to get the head <-> MRI transform.
        """
        ...
    def add_mni_fiducials(self, subjects_dir=None, verbose=None):
        """### Add fiducials to a montage in MNI space.

        -----
        ### 🛠️ Parameters


        subjects_dir : path-like | None
            The path to the directory containing the FreeSurfer subjects
            reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
            variable.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns

        inst : instance of DigMontage
            The instance, modified in-place.

        -----
        ### 📖 Notes

        ``fsaverage`` is in MNI space and so its fiducials can be
        added to a montage in "mni_tal". MNI is an ACPC-aligned
        coordinate system (the posterior commissure is the origin)
        so since BIDS requires channel locations for ECoG, sEEG and
        DBS to be in ACPC space, this function can be used to allow
        those coordinate to be transformed to "head" space (origin
        between LPA and RPA).
        """
        ...
    def remove_fiducials(self, verbose=None):
        """### Remove the fiducial points from a montage.

        -----
        ### 🛠️ Parameters


        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns

        inst : instance of DigMontage
            The instance, modified in-place.

        -----
        ### 📖 Notes

        MNE will transform a montage to the internal "head" coordinate
        frame if the fiducials are present. Under most circumstances, this
        is ideal as it standardizes the coordinate frame for things like
        plotting. However, in some circumstances, such as saving a ``raw``
        with intracranial data to BIDS format, the coordinate frame
        should not be changed by removing fiducials.
        """
        ...

VALID_SCALES: Incomplete

def transform_to_head(montage):
    """### Transform a DigMontage object into head coordinate.

    -----
    ### 🛠️ Parameters

    montage : instance of DigMontage
        The montage.

    -----
    ### ⏎ Returns

    montage : instance of DigMontage
        The montage after transforming the points to head
        coordinate system.

    -----
    ### 📖 Notes

    This function requires that the LPA, RPA and Nasion fiducial
    points are available. If they are not, they will be added based by
    projecting the fiducials onto a sphere with radius equal to the average
    distance of each point to the origin (in the given coordinate frame).

    This function assumes that all fiducial points are in the same coordinate
    frame (e.g. 'unknown') and it will convert all the point in this coordinate
    system to Neuromag head coordinate system.

    🎭 Changed in version 1.2
       Fiducial points will be added automatically if the montage does not
       have them.
    """
    ...

def read_dig_dat(fname):
    """### Read electrode positions from a ``*.dat`` file.

    ### ⛔️ Warning
        This function was implemented based on ``*.dat`` files available from
        `Compumedics <https://compumedicsneuroscan.com>`__ and might not work
        as expected with novel files. If it does not read your files correctly
        please contact the MNE-Python developers.

    -----
    ### 🛠️ Parameters

    fname : path-like
        File from which to read electrode locations.

    -----
    ### ⏎ Returns

    montage : DigMontage
        The montage.

    -----
    ### 👉 See Also

    read_dig_captrak
    read_dig_dat
    read_dig_egi
    read_dig_fif
    read_dig_hpts
    read_dig_localite
    read_dig_polhemus_isotrak
    make_dig_montage

    -----
    ### 📖 Notes

    ``*.dat`` files are plain text files and can be inspected and amended with
    a plain text editor.
    """
    ...

def read_dig_fif(fname):
    """### Read digitized points from a .fif file.

    Note that electrode names are not present in the .fif file so
    they are here defined with the convention from VectorView
    systems (EEG001, EEG002, etc.)

    -----
    ### 🛠️ Parameters

    fname : path-like
        FIF file from which to read digitization locations.

    -----
    ### ⏎ Returns

    montage : instance of DigMontage
        The montage.

    -----
    ### 👉 See Also

    DigMontage
    read_dig_dat
    read_dig_egi
    read_dig_captrak
    read_dig_polhemus_isotrak
    read_dig_hpts
    read_dig_localite
    make_dig_montage
    """
    ...

def read_dig_hpts(fname, unit: str = "mm"):
    """### Read historical ``.hpts`` MNE-C files.

    -----
    ### 🛠️ Parameters

    fname : path-like
        The filepath of .hpts file.
    unit : ``'m'`` | ``'cm'`` | ``'mm'``
        Unit of the positions. Defaults to ``'mm'``.

    -----
    ### ⏎ Returns

    montage : instance of DigMontage
        The montage.

    -----
    ### 👉 See Also

    DigMontage
    read_dig_captrak
    read_dig_dat
    read_dig_egi
    read_dig_fif
    read_dig_localite
    read_dig_polhemus_isotrak
    make_dig_montage

    -----
    ### 📖 Notes

    The hpts format digitzer data file may contain comment lines starting
    with the pound sign (#) and data lines of the form::

         <*category*> <*identifier*> <*x/mm*> <*y/mm*> <*z/mm*>

    where:

    ``<*category*>``
        defines the type of points. Allowed categories are: ``hpi``,
        ``cardinal`` (fiducial), ``eeg``, and ``extra`` corresponding to
        head-position indicator coil locations, cardinal landmarks, EEG
        electrode locations, and additional head surface points,
        respectively.

    ``<*identifier*>``
        identifies the point. The identifiers are usually sequential
        numbers. For cardinal landmarks, 1 = left auricular point,
        2 = nasion, and 3 = right auricular point. For EEG electrodes,
        identifier = 0 signifies the reference electrode.

    ``<*x/mm*> , <*y/mm*> , <*z/mm*>``
        Location of the point, usually in the head coordinate system
        in millimeters. If your points are in [m] then unit parameter can
        be changed.

    For example::

        cardinal    2    -5.6729  -12.3873  -30.3671
        cardinal    1    -37.6782  -10.4957   91.5228
        cardinal    3    -131.3127    9.3976  -22.2363
        hpi    1    -30.4493  -11.8450   83.3601
        hpi    2    -122.5353    9.2232  -28.6828
        hpi    3    -6.8518  -47.0697  -37.0829
        hpi    4    7.3744  -50.6297  -12.1376
        hpi    5    -33.4264  -43.7352  -57.7756
        eeg    FP1  3.8676  -77.0439  -13.0212
        eeg    FP2  -31.9297  -70.6852  -57.4881
        eeg    F7  -6.1042  -68.2969   45.4939
        ...
    """
    ...

def read_dig_egi(fname):
    """### Read electrode locations from EGI system.

    -----
    ### 🛠️ Parameters

    fname : path-like
        EGI MFF XML coordinates file from which to read digitization locations.

    -----
    ### ⏎ Returns

    montage : instance of DigMontage
        The montage.

    -----
    ### 👉 See Also

    DigMontage
    read_dig_captrak
    read_dig_dat
    read_dig_fif
    read_dig_hpts
    read_dig_localite
    read_dig_polhemus_isotrak
    make_dig_montage
    """
    ...

def read_dig_captrak(fname):
    """### Read electrode locations from CapTrak Brain Products system.

    -----
    ### 🛠️ Parameters

    fname : path-like
        BrainVision CapTrak coordinates file from which to read EEG electrode
        locations. This is typically in XML format with the .bvct extension.

    -----
    ### ⏎ Returns

    montage : instance of DigMontage
        The montage.

    -----
    ### 👉 See Also

    DigMontage
    read_dig_dat
    read_dig_egi
    read_dig_fif
    read_dig_hpts
    read_dig_localite
    read_dig_polhemus_isotrak
    make_dig_montage
    """
    ...

def read_dig_localite(fname, nasion=None, lpa=None, rpa=None):
    """### Read Localite .csv file.

    -----
    ### 🛠️ Parameters

    fname : path-like
        File name.
    nasion : str | None
        Name of nasion fiducial point.
    lpa : str | None
        Name of left preauricular fiducial point.
    rpa : str | None
        Name of right preauricular fiducial point.

    -----
    ### ⏎ Returns

    montage : instance of DigMontage
        The montage.

    -----
    ### 👉 See Also

    DigMontage
    read_dig_captrak
    read_dig_dat
    read_dig_egi
    read_dig_fif
    read_dig_hpts
    read_dig_polhemus_isotrak
    make_dig_montage
    """
    ...

def read_dig_polhemus_isotrak(fname, ch_names=None, unit: str = "m"):
    """### Read Polhemus digitizer data from a file.

    -----
    ### 🛠️ Parameters

    fname : path-like
        The filepath of Polhemus ISOTrak formatted file.
        File extension is expected to be ``'.hsp'``, ``'.elp'`` or ``'.eeg'``.
    ch_names : None | list of str
        The names of the points. This will make the points
        considered as EEG channels. If None, channels will be assumed
        to be HPI if the extension is ``'.elp'``, and extra headshape
        points otherwise.
    unit : ``'m'`` | ``'cm'`` | ``'mm'``
        Unit of the digitizer file. Polhemus ISOTrak systems data is usually
        exported in meters. Defaults to ``'m'``.

    -----
    ### ⏎ Returns

    montage : instance of DigMontage
        The montage.

    -----
    ### 👉 See Also

    DigMontage
    make_dig_montage
    read_polhemus_fastscan
    read_dig_captrak
    read_dig_dat
    read_dig_egi
    read_dig_fif
    read_dig_localite
    """
    ...

def read_polhemus_fastscan(
    fname, unit: str = "mm", on_header_missing: str = "raise", *, verbose=None
):
    """### Read Polhemus FastSCAN digitizer data from a ``.txt`` file.

    -----
    ### 🛠️ Parameters

    fname : path-like
        The path of ``.txt`` Polhemus FastSCAN file.
    unit : ``'m'`` | ``'cm'`` | ``'mm'``
        Unit of the digitizer file. Polhemus FastSCAN systems data is usually
        exported in millimeters. Defaults to ``'mm'``.

    on_header_missing : str
        Can be ``'raise'`` (default) to raise an error, ``'warn'`` to emit a
        warning, or ``'ignore'`` to ignore when the FastSCAN header is missing.

        ✨ Added in vesion 0.22

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    points : array, shape (n_points, 3)
        The digitization points in digitizer coordinates.

    -----
    ### 👉 See Also

    read_dig_polhemus_isotrak
    make_dig_montage
    """
    ...

def read_custom_montage(fname, head_size=0.095, coord_frame=None):
    """### Read a montage from a file.

    -----
    ### 🛠️ Parameters

    fname : path-like
        File extension is expected to be:
        ``'.loc'`` or ``'.locs'`` or ``'.eloc'`` (for EEGLAB files),
        ``'.sfp'`` (BESA/EGI files), ``'.csd'``,
        ``'.elc'``, ``'.txt'``, ``'.csd'``, ``'.elp'`` (BESA spherical),
        ``'.bvef'`` (BrainVision files),
        ``'.csv'``, ``'.tsv'``, ``'.xyz'`` (XYZ coordinates).
    head_size : float | None
        The size of the head (radius, in [m]). If ``None``, returns the values
        read from the montage file with no modification. Defaults to 0.095m.
    coord_frame : str | None
        The coordinate frame of the points. Usually this is ``"unknown"``
        for native digitizer space. Defaults to None, which is ``"unknown"``
        for most readers but ``"head"`` for EEGLAB.

        ✨ Added in vesion 0.20

    -----
    ### ⏎ Returns

    montage : instance of DigMontage
        The montage.

    -----
    ### 👉 See Also

    make_dig_montage
    make_standard_montage

    -----
    ### 📖 Notes

    The function is a helper to read electrode positions you may have
    in various formats. Most of these format are weakly specified
    in terms of units, coordinate systems. It implies that setting
    a montage using a DigMontage produced by this function may
    be problematic. If you use a standard/template (eg. 10/20,
    10/10 or 10/05) we recommend you use `make_standard_montage`.
    If you can have positions in memory you can also use
    `make_dig_montage` that takes arrays as input.
    """
    ...

def compute_dev_head_t(montage):
    """### Compute device to head transform from a DigMontage.

    -----
    ### 🛠️ Parameters

    montage : DigMontage
        The `mne.channels.DigMontage` must contain the fiducials in head
        coordinate system and hpi points in both head and
        meg device coordinate system.

    -----
    ### ⏎ Returns

    dev_head_t : Transform
        A Device-to-Head transformation matrix.
    """
    ...

def compute_native_head_t(montage, *, on_missing: str = "warn", verbose=None):
    """### Compute the native-to-head transformation for a montage.

    This uses the fiducials in the native space to transform to compute the
    transform to the head coordinate frame.

    -----
    ### 🛠️ Parameters

    montage : instance of DigMontage
        The montage.

    on_missing : 'raise' | 'warn' | 'ignore'
        Can be ``'raise'`` (default) to raise an error, ``'warn'`` to emit a
        warning, or ``'ignore'`` to ignore when some necessary fiducial points are missing.

        ✨ Added in vesion 1.2

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    native_head_t : instance of Transform
        A native-to-head transformation matrix.
    """
    ...

def make_standard_montage(kind, head_size: str = "auto"):
    """### Read a generic (built-in) standard montage that ships with MNE-Python.

    -----
    ### 🛠️ Parameters

    kind : str
        The name of the montage to use.

        ### 💡 Note
            You can retrieve the names of all
            built-in montages via `mne.channels.get_builtin_montages`.
    head_size : float | None | str
        The head size (radius, in meters) to use for spherical montages.
        Can be None to not scale the read sizes. ``'auto'`` (default) will
        use 95mm for all montages except the ``'standard*'``, ``'mgh*'``, and
        ``'artinis*'``, which are already in fsaverage's MRI coordinates
        (same as MNI).

    -----
    ### ⏎ Returns

    montage : instance of DigMontage
        The montage.

    -----
    ### 👉 See Also

    get_builtin_montages
    make_dig_montage
    read_custom_montage

    -----
    ### 📖 Notes

    Individualized (digitized) electrode positions should be read in using
    `read_dig_captrak`, `read_dig_dat`, `read_dig_egi`,
    `read_dig_fif`, `read_dig_polhemus_isotrak`,
    `read_dig_hpts`, or manually made with `make_dig_montage`.

    ✨ Added in vesion 0.19.0
    """
    ...
