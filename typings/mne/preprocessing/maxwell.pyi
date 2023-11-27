from .. import __version__ as __version__
from .._fiff.compensator import make_compensator as make_compensator
from .._fiff.constants import FIFF as FIFF, FWD as FWD
from .._fiff.meas_info import Info as Info
from .._fiff.pick import pick_info as pick_info, pick_types as pick_types
from .._fiff.proj import Projection as Projection
from .._fiff.write import DATE_NONE as DATE_NONE
from ..channels.channels import fix_mag_coil_types as fix_mag_coil_types
from ..fixes import bincount as bincount
from ..io import BaseRaw as BaseRaw, RawArray as RawArray
from ..transforms import (
    Transform as Transform,
    apply_trans as apply_trans,
    quat_to_rot as quat_to_rot,
    rot_to_quat as rot_to_quat,
)
from ..utils import logger as logger, use_log_level as use_log_level, warn as warn
from _typeshed import Incomplete

def maxwell_filter_prepare_emptyroom(
    raw_er,
    *,
    raw,
    bads: str = "from_raw",
    annotations: str = "from_raw",
    meas_date: str = "keep",
    emit_warning: bool = False,
    verbose=None,
):
    """## Prepare an empty-room recording for Maxwell filtering.

    Empty-room data by default lacks certain properties that are required to
    ensure running `mne.preprocessing.maxwell_filter` will process the
    empty-room recording the same way as the experimental data. This function
    preconditions an empty-room raw data instance accordingly so it can be used
    for Maxwell filtering. Please see the ``Notes`` section for details.

    -----
    ### 🛠️ Parameters

    #### `raw_er : instance of Raw`
        The empty-room recording. It will not be modified.
    #### `raw : instance of Raw`
        The experimental recording, typically this will be the reference run
        used for Maxwell filtering.
    #### `bads : 'from_raw' | 'union' | 'keep'`
        How to populate the list of bad channel names to be injected into
        the empty-room recording. If ``'from_raw'`` (default) the list of bad
        channels will be overwritten with that of ``raw``. If ``'union'``, will
        use the union of bad channels in ``raw`` and ``raw_er``. Note that
        this may lead to additional bad channels in the empty-room in
        comparison to the experimental recording. If ``'keep'``, don't alter
        the existing list of bad channels.

        ### 💡 Note
           Non-MEG channels are silently dropped from the list of bads.
    #### `annotations : 'from_raw' | 'union' | 'keep'`
        Whether to copy the annotations over from ``raw`` (default),
        use the union of the annotations, or to keep them unchanged.
    #### `meas_date : 'keep' | 'from_raw'`
        Whether to transfer the measurement date from ``raw`` or to keep
        it as is (default). If you intend to manually transfer annotations
        from ``raw`` `after` running this function, you should set this to
        ``'from_raw'``.

    #### `emit_warning : bool`
        Whether to emit warnings when cropping or omitting annotations.
        Unlike `raw.set_annotations <mne.io.Raw.set_annotations>`, the
        default here is ``False``, as empty-room recordings are often shorter
        than raw.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `raw_er_prepared : instance of Raw`
        A copy of the passed empty-room recording, ready for Maxwell filtering.

    -----
    ### 📖 Notes

    This function will:

    * Compile the list of bad channels according to the ``bads`` parameter.
    * Inject the device-to-head transformation matrix from the experimental
      recording into the empty-room recording.
    * Set the following properties of the empty-room recording to match the
      experimental recording:

      * Montage
      * ``raw.first_time`` and ``raw.first_samp``

    * Adjust annotations according to the ``annotations`` parameter.
    * Adjust the measurement date according to the ``meas_date`` parameter.

    ✨ Added in version 1.1
    """
    ...

def maxwell_filter(
    raw,
    origin: str = "auto",
    int_order: int = 8,
    ext_order: int = 3,
    calibration=None,
    cross_talk=None,
    st_duration=None,
    st_correlation: float = 0.98,
    coord_frame: str = "head",
    destination=None,
    regularize: str = "in",
    ignore_ref: bool = False,
    bad_condition: str = "error",
    head_pos=None,
    st_fixed: bool = True,
    st_only: bool = False,
    mag_scale: float = 100.0,
    skip_by_annotation=("edge", "bad_acq_skip"),
    extended_proj=(),
    verbose=None,
):
    """## Maxwell filter data using multipole moments.

    -----
    ### 🛠️ Parameters

    #### `raw : instance of Raw`
        Data to be filtered.

        ### ⛔️ Warning It is critical to mark bad channels in
                     ``raw.info['bads']`` prior to processing in order to
                     prevent artifact spreading. Manual inspection and use
                     of `find_bad_channels_maxwell` is recommended.

    #### `origin : array-like, shape (3,) | str`
        Origin of internal and external multipolar moment space in meters.
        The default is ``'auto'``, which means ``(0., 0., 0.)`` when
        ``coord_frame='meg'``, and a head-digitization-based
        origin fit using `mne.bem.fit_sphere_to_headshape`
        when ``coord_frame='head'``. If automatic fitting fails (e.g., due
        to having too few digitization points),
        consider separately calling the fitting function with different
        options or specifying the origin manually.

    #### `int_order : int`
        Order of internal component of spherical expansion.

    #### `ext_order : int`
        Order of external component of spherical expansion.

    #### `calibration : str | None`
        Path to the ``'.dat'`` file with fine calibration coefficients.
        File can have 1D or 3D gradiometer imbalance correction.
        This file is machine/site-specific.

    #### `cross_talk : str | None`
        Path to the FIF file with cross-talk correction information.
    #### `st_duration : float | None`
        If not None, apply spatiotemporal SSS with specified buffer duration
        (in seconds). MaxFilter™'s default is 10.0 seconds in v2.2.
        Spatiotemporal SSS acts as implicitly as a high-pass filter where the
        cut-off frequency is 1/st_duration Hz. For this (and other) reasons,
        longer buffers are generally better as long as your system can handle
        the higher memory usage. To ensure that each window is processed
        identically, choose a buffer length that divides evenly into your data.
        Any data at the trailing edge that doesn't fit evenly into a whole
        buffer window will be lumped into the previous buffer.
    #### `st_correlation : float`
        Correlation limit between inner and outer subspaces used to reject
        overlapping intersecting inner/outer signals during spatiotemporal SSS.

    #### `coord_frame : str`
        The coordinate frame that the ``origin`` is specified in, either
        ``'meg'`` or ``'head'``. For empty-room recordings that do not have
        a head<->meg transform ``info['dev_head_t']``, the MEG coordinate
        frame should be used.

    #### `destination : path-like | array-like, shape (3,) | None`
        The destination location for the head. Can be ``None``, which
        will not change the head position, or a path to a FIF file
        containing a MEG device<->head transformation, or a 3-element array
        giving the coordinates to translate to (with no rotations).
        For example, ``destination=(0, 0, 0.04)`` would translate the bases
        as ``--trans default`` would in MaxFilter™ (i.e., to the default
        head location).

    #### `regularize : str | None`
        Basis regularization type, must be ``"in"`` or None.
        ``"in"`` is the same algorithm as the ``-regularize in`` option in
        MaxFilter™.

    #### `ignore_ref : bool`
        If True, do not include reference channels in compensation. This
        option should be True for KIT files, since Maxwell filtering
        with reference channels is not currently supported.

    #### `bad_condition : str`
        How to deal with ill-conditioned SSS matrices. Can be ``"error"``
        (default), ``"warning"``, ``"info"``, or ``"ignore"``.

    #### `head_pos : array | None`
        If array, movement compensation will be performed.
        The array should be of shape (N, 10), holding the position
        parameters as returned by e.g. ``read_head_pos``.

        ✨ Added in version 0.12

    #### `st_fixed : bool`
        If True (default), do tSSS using the median head position during the
        ``st_duration`` window. This is the default behavior of MaxFilter
        and has been most extensively tested.

        ✨ Added in version 0.12
    #### `st_only : bool`
        If True, only tSSS (temporal) projection of MEG data will be
        performed on the output data. The non-tSSS parameters (e.g.,
        ``int_order``, ``calibration``, ``head_pos``, etc.) will still be
        used to form the SSS bases used to calculate temporal projectors,
        but the output MEG data will *only* have temporal projections
        performed. Noise reduction from SSS basis multiplication,
        cross-talk cancellation, movement compensation, and so forth
        will not be applied to the data. This is useful, for example, when
        evoked movement compensation will be performed with
        `mne.epochs.average_movements`.

        ✨ Added in version 0.12

    #### `mag_scale : float | str`
        The magenetometer scale-factor used to bring the magnetometers
        to approximately the same order of magnitude as the gradiometers
        (default 100.), as they have different units (T vs T/m).
        Can be ``'auto'`` to use the reciprocal of the physical distance
        between the gradiometer pickup loops (e.g., 0.0168 m yields
        59.5 for VectorView).

        ✨ Added in version 0.13

    #### `skip_by_annotation : str | list of str`
        If a string (or list of str), any annotation segment that begins
        with the given string will not be included in filtering, and
        segments on either side of the given excluded annotated segment
        will be filtered separately (i.e., as independent signals).
        The default ``('edge', 'bad_acq_skip')`` will separately filter
        any segments that were concatenated by `mne.concatenate_raws`
        or `mne.io.Raw.append`, or separated during acquisition.
        To disable, provide an empty list.

        ✨ Added in version 0.17

    #### `extended_proj : list`
        The empty-room projection vectors used to extend the external
        SSS basis (i.e., use eSSS).

        ✨ Added in version 0.21

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `raw_sss : instance of Raw`
        The raw data with Maxwell filtering applied.

    -----
    ### 👉 See Also

    mne.preprocessing.annotate_amplitude
    mne.preprocessing.find_bad_channels_maxwell
    mne.chpi.filter_chpi
    mne.chpi.read_head_pos
    mne.epochs.average_movements

    -----
    ### 📖 Notes

    ✨ Added in version 0.11

    Some of this code was adapted and relicensed (with BSD form) with
    permission from Jussi Nurminen. These algorithms are based on work
    from :footcite:`TauluKajola2005` and :footcite:`TauluSimola2006`.
    It will likely use multiple CPU cores, see the `FAQ <faq_cpu>`
    for more information.

    ### ⛔️ Warning Maxwell filtering in MNE is not designed or certified
                 for clinical use.

    Compared to the MEGIN MaxFilter™ software, the MNE Maxwell filtering
    routines currently provide the following features:

    .. table::
       :widths: auto

       +-----------------------------------------------------------------------------+-----+-----------+
       | Feature                                                                     | MNE | MaxFilter |
       +=============================================================================+=====+===========+
       | Maxwell filtering software shielding                                        | ✓   | ✓         |
       +-----------------------------------------------------------------------------+-----+-----------+
       | Bad channel reconstruction                                                  | ✓   | ✓         |
       +-----------------------------------------------------------------------------+-----+-----------+
       | Cross-talk cancellation                                                     | ✓   | ✓         |
       +-----------------------------------------------------------------------------+-----+-----------+
       | Fine calibration correction (1D)                                            | ✓   | ✓         |
       +-----------------------------------------------------------------------------+-----+-----------+
       | Fine calibration correction (3D)                                            | ✓   |           |
       +-----------------------------------------------------------------------------+-----+-----------+
       | Spatio-temporal SSS (tSSS)                                                  | ✓   | ✓         |
       +-----------------------------------------------------------------------------+-----+-----------+
       | Coordinate frame translation                                                | ✓   | ✓         |
       +-----------------------------------------------------------------------------+-----+-----------+
       | Regularization using information theory                                     | ✓   | ✓         |
       +-----------------------------------------------------------------------------+-----+-----------+
       | Movement compensation (raw)                                                 | ✓   | ✓         |
       +-----------------------------------------------------------------------------+-----+-----------+
       | Movement compensation (`epochs <mne.epochs.average_movements>`)       | ✓   |           |
       +-----------------------------------------------------------------------------+-----+-----------+
       | `cHPI subtraction <mne.chpi.filter_chpi>`                             | ✓   | ✓         |
       +-----------------------------------------------------------------------------+-----+-----------+
       | Double floating point precision                                             | ✓   |           |
       +-----------------------------------------------------------------------------+-----+-----------+
       | Seamless processing of split (``-1.fif``) and concatenated files            | ✓   |           |
       +-----------------------------------------------------------------------------+-----+-----------+
       | Automatic bad channel detection (`find_bad_channels_maxwell`)        | ✓   | ✓         |
       +-----------------------------------------------------------------------------+-----+-----------+
       | Head position estimation (`mne.chpi.compute_head_pos`)               | ✓   | ✓         |
       +-----------------------------------------------------------------------------+-----+-----------+
       | Certified for clinical use                                                  |     | ✓         |
       +-----------------------------------------------------------------------------+-----+-----------+
       | Extended external basis (eSSS)                                              | ✓   |           |
       +-----------------------------------------------------------------------------+-----+-----------+

    Epoch-based movement compensation is described in :footcite:`TauluKajola2005`.

    Use of Maxwell filtering routines with non-Neuromag systems is currently
    `experimental`. Worse results for non-Neuromag systems are expected due
    to (at least):

    * Missing fine-calibration and cross-talk cancellation data for
      other systems.
    * Processing with reference sensors has not been vetted.
    * Regularization of components may not work well for all systems.
    * Coil integration has not been optimized using Abramowitz/Stegun
      definitions.

    ### 💡 Note Various Maxwell filtering algorithm components are covered by
              patents owned by MEGIN. These patents include, but may not be
              limited to:

              - US2006031038 (Signal Space Separation)
              - US6876196 (Head position determination)
              - WO2005067789 (DC fields)
              - WO2005078467 (MaxShield)
              - WO2006114473 (Temporal Signal Space Separation)

              These patents likely preclude the use of Maxwell filtering code
              in commercial applications. Consult a lawyer if necessary.

    Currently, in order to perform Maxwell filtering, the raw data must not
    have any projectors applied. During Maxwell filtering, the spatial
    structure of the data is modified, so projectors are discarded (unless
    in ``st_only=True`` mode).

    References
    ----------
    .. footbibliography::
    """
    ...

check_disable: Incomplete

def find_bad_channels_maxwell(
    raw,
    limit: float = 7.0,
    duration: float = 5.0,
    min_count: int = 5,
    return_scores: bool = False,
    origin: str = "auto",
    int_order: int = 8,
    ext_order: int = 3,
    calibration=None,
    cross_talk=None,
    coord_frame: str = "head",
    regularize: str = "in",
    ignore_ref: bool = False,
    bad_condition: str = "error",
    head_pos=None,
    mag_scale: float = 100.0,
    skip_by_annotation=("edge", "bad_acq_skip"),
    h_freq: float = 40.0,
    extended_proj=(),
    verbose=None,
):
    """## Find bad channels using Maxwell filtering.

    -----
    ### 🛠️ Parameters

    #### `raw : instance of Raw`
        Raw data to process.
    #### `limit : float`
        Detection limit for noisy segments (default is 7.). Smaller values will
        find more bad channels at increased risk of including good ones. This
        value can be interpreted as the standard score of differences between
        the original and Maxwell-filtered data. See the ``Notes`` section for
        details.

        ### 💡 Note This setting only concerns *noisy* channel detection.
                  The limit for *flat* channel detection currently cannot be
                  controlled by the user. Flat channel detection is always run
                  before noisy channel detection.
    #### `duration : float`
        Duration of the segments into which to slice the data for processing,
        in seconds. Default is 5.
    #### `min_count : int`
        Minimum number of times a channel must show up as bad in a chunk.
        Default is 5.
    #### `return_scores : bool`
        If ``True``, return a dictionary with scoring information for each
        evaluated segment of the data. Default is ``False``.

        ### ⛔️ Warning This feature is experimental and may change in a future
                     version of MNE-Python without prior notice. Please
                     report any problems and enhancement proposals to the
                     developers.

        ✨ Added in version 0.21

    #### `origin : array-like, shape (3,) | str`
        Origin of internal and external multipolar moment space in meters.
        The default is ``'auto'``, which means ``(0., 0., 0.)`` when
        ``coord_frame='meg'``, and a head-digitization-based
        origin fit using `mne.bem.fit_sphere_to_headshape`
        when ``coord_frame='head'``. If automatic fitting fails (e.g., due
        to having too few digitization points),
        consider separately calling the fitting function with different
        options or specifying the origin manually.

    #### `int_order : int`
        Order of internal component of spherical expansion.

    #### `ext_order : int`
        Order of external component of spherical expansion.

    #### `calibration : str | None`
        Path to the ``'.dat'`` file with fine calibration coefficients.
        File can have 1D or 3D gradiometer imbalance correction.
        This file is machine/site-specific.

    #### `cross_talk : str | None`
        Path to the FIF file with cross-talk correction information.

    #### `coord_frame : str`
        The coordinate frame that the ``origin`` is specified in, either
        ``'meg'`` or ``'head'``. For empty-room recordings that do not have
        a head<->meg transform ``info['dev_head_t']``, the MEG coordinate
        frame should be used.

    #### `regularize : str | None`
        Basis regularization type, must be ``"in"`` or None.
        ``"in"`` is the same algorithm as the ``-regularize in`` option in
        MaxFilter™.

    #### `ignore_ref : bool`
        If True, do not include reference channels in compensation. This
        option should be True for KIT files, since Maxwell filtering
        with reference channels is not currently supported.

    #### `bad_condition : str`
        How to deal with ill-conditioned SSS matrices. Can be ``"error"``
        (default), ``"warning"``, ``"info"``, or ``"ignore"``.

    #### `head_pos : array | None`
        If array, movement compensation will be performed.
        The array should be of shape (N, 10), holding the position
        parameters as returned by e.g. ``read_head_pos``.

    #### `mag_scale : float | str`
        The magenetometer scale-factor used to bring the magnetometers
        to approximately the same order of magnitude as the gradiometers
        (default 100.), as they have different units (T vs T/m).
        Can be ``'auto'`` to use the reciprocal of the physical distance
        between the gradiometer pickup loops (e.g., 0.0168 m yields
        59.5 for VectorView).

    #### `skip_by_annotation : str | list of str`
        If a string (or list of str), any annotation segment that begins
        with the given string will not be included in filtering, and
        segments on either side of the given excluded annotated segment
        will be filtered separately (i.e., as independent signals).
        The default ``('edge', 'bad_acq_skip')`` will separately filter
        any segments that were concatenated by `mne.concatenate_raws`
        or `mne.io.Raw.append`, or separated during acquisition.
        To disable, provide an empty list.
    #### `h_freq : float | None`
        The cutoff frequency (in Hz) of the low-pass filter that will be
        applied before processing the data. This defaults to ``40.``, which
        should provide similar results to MaxFilter. If you do not wish to
        apply a filter, set this to ``None``.

    #### `extended_proj : list`
        The empty-room projection vectors used to extend the external
        SSS basis (i.e., use eSSS).

        ✨ Added in version 0.21

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `noisy_chs : list`
        List of bad MEG channels that were automatically detected as being
        noisy among the good MEG channels.
    #### `flat_chs : list`
        List of MEG channels that were detected as being flat in at least
        ``min_count`` segments.
    #### `scores : dict`
        A dictionary with information produced by the scoring algorithms.
        Only returned when ``return_scores`` is ``True``. It contains the
        following keys:

        - ``ch_names`` : ndarray, shape (n_meg,)
            The names of the MEG channels. Their order corresponds to the
            order of rows in the ``scores`` and ``limits`` arrays.
        - ``ch_types`` : ndarray, shape (n_meg,)
            The types of the MEG channels in ``ch_names`` (``'mag'``,
            ``'grad'``).
        - ``bins`` : ndarray, shape (n_windows, 2)
            The inclusive window boundaries (start and stop; in seconds) used
            to calculate the scores.
        - ``scores_flat`` : ndarray, shape (n_meg, n_windows)
            The scores for testing whether MEG channels are flat. These values
            correspond to the standard deviation of a segment.
            See the ``Notes`` section for details.
        - ``limits_flat`` : ndarray, shape (n_meg, 1)
            The score thresholds (in standard deviation) above which a segment
            was classified as "flat".
        - ``scores_noisy`` : ndarray, shape (n_meg, n_windows)
            The scores for testing whether MEG channels are noisy. These values
            correspond to the standard score of a segment.
            See the ``Notes`` section for details.
        - ``limits_noisy`` : ndarray, shape (n_meg, 1)
            The score thresholds (in standard scores) above which a segment was
            classified as "noisy".

        ### 💡 Note The scores and limits for channels marked as ``bad`` in the
                  input data will be set to ``np.nan``.

    -----
    ### 👉 See Also

    annotate_amplitude
    maxwell_filter

    -----
    ### 📖 Notes

    All arguments after ``raw``, ``limit``, ``duration``, ``min_count``, and
    ``return_scores`` are the same as `maxwell_filter`, except that the
    following are not allowed in this function because they are unused:
    ``st_duration``, ``st_correlation``, ``destination``, ``st_fixed``, and
    ``st_only``.

    This algorithm, for a given chunk of data:

    1. Runs SSS on the data, without removing external components.
    2. Excludes channels as *flat* that have had low variability
       (standard deviation < 0.01 fT or fT/cm in a 30 ms window) in the given
       or any previous chunk.
    3. For each channel :math:`k`, computes the *range* or peak-to-peak
       :math:`d_k` of the difference between the reconstructed and original
       data.
    4. Computes the average :math:`\\mu_d` and standard deviation
       :math:`\\sigma_d` of the differences (after scaling magnetometer data
       to roughly match the scale of the gradiometer data using ``mag_scale``).
    5. Marks channels as bad for the chunk when
       :math:`d_k > \\mu_d + \\textrm{limit} \\times \\sigma_d`. Note that this
       expression can be easily transformed into
       :math:`(d_k - \\mu_d) / \\sigma_d > \\textrm{limit}`, which is equivalent
       to :math:`z(d_k) > \\textrm{limit}`, with :math:`z(d_k)` being the
       standard or z-score of the difference.

    Data are processed in chunks of the given ``duration``, and channels that
    are bad for at least ``min_count`` chunks are returned.

    Channels marked as *flat* in step 2 are excluded from all subsequent steps
    of noisy channel detection.

    This algorithm gives results similar to, but not identical with,
    MaxFilter. Differences arise because MaxFilter processes on a
    buffer-by-buffer basis (using buffer-size-dependent downsampling logic),
    uses different filtering characteristics, and possibly other factors.
    Channels that are near the ``limit`` for a given ``min_count`` are
    particularly susceptible to being different between the two
    implementations.

    ✨ Added in version 0.20
    """
    ...

def compute_maxwell_basis(
    info,
    origin: str = "auto",
    int_order: int = 8,
    ext_order: int = 3,
    calibration=None,
    coord_frame: str = "head",
    regularize: str = "in",
    ignore_ref: bool = True,
    bad_condition: str = "error",
    mag_scale: float = 100.0,
    extended_proj=(),
    verbose=None,
):
    """## Compute the SSS basis for a given measurement info structure.

    -----
    ### 🛠️ Parameters


    #### `info : mne.Info`
        The `mne.Info` object with information about the sensors and methods of measurement.

    #### `origin : array-like, shape (3,) | str`
        Origin of internal and external multipolar moment space in meters.
        The default is ``'auto'``, which means ``(0., 0., 0.)`` when
        ``coord_frame='meg'``, and a head-digitization-based
        origin fit using `mne.bem.fit_sphere_to_headshape`
        when ``coord_frame='head'``. If automatic fitting fails (e.g., due
        to having too few digitization points),
        consider separately calling the fitting function with different
        options or specifying the origin manually.

    #### `int_order : int`
        Order of internal component of spherical expansion.

    #### `ext_order : int`
        Order of external component of spherical expansion.

    #### `calibration : str | None`
        Path to the ``'.dat'`` file with fine calibration coefficients.
        File can have 1D or 3D gradiometer imbalance correction.
        This file is machine/site-specific.

    #### `coord_frame : str`
        The coordinate frame that the ``origin`` is specified in, either
        ``'meg'`` or ``'head'``. For empty-room recordings that do not have
        a head<->meg transform ``info['dev_head_t']``, the MEG coordinate
        frame should be used.

    #### `regularize : str | None`
        Basis regularization type, must be ``"in"`` or None.
        ``"in"`` is the same algorithm as the ``-regularize in`` option in
        MaxFilter™.

    #### `ignore_ref : bool`
        If True, do not include reference channels in compensation. This
        option should be True for KIT files, since Maxwell filtering
        with reference channels is not currently supported.

    #### `bad_condition : str`
        How to deal with ill-conditioned SSS matrices. Can be ``"error"``
        (default), ``"warning"``, ``"info"``, or ``"ignore"``.

    #### `mag_scale : float | str`
        The magenetometer scale-factor used to bring the magnetometers
        to approximately the same order of magnitude as the gradiometers
        (default 100.), as they have different units (T vs T/m).
        Can be ``'auto'`` to use the reciprocal of the physical distance
        between the gradiometer pickup loops (e.g., 0.0168 m yields
        59.5 for VectorView).

    #### `extended_proj : list`
        The empty-room projection vectors used to extend the external
        SSS basis (i.e., use eSSS).

        ✨ Added in version 0.21

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    S : ndarray, shape (n_meg, n_moments)
        The basis that can be used to reconstruct the data.
    pS : ndarray, shape (n_moments, n_good_meg)
        The (stabilized) pseudoinverse of the S array.
    #### `reg_moments : ndarray, shape (n_moments,)`
        The moments that were kept after regularization.
    #### `n_use_in : int`
        The number of kept moments that were in the internal space.

    -----
    ### 📖 Notes

    This outputs variants of :math:`\\mathbf{S}` and :math:`\\mathbf{S^\\dagger}`
    from equations 27 and 37 of :footcite:`TauluKajola2005` with the coil scale
    for magnetometers already factored in so that the resulting denoising
    transform of the data to obtain :math:`\\hat{\\phi}_{in}` from equation
    38 would be::

        phi_in = S[:, :n_use_in] @ pS[:n_use_in] @ data_meg_good

    ✨ Added in version 0.23

    References
    ----------
    .. footbibliography::
    """
    ...
