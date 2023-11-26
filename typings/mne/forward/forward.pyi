from .._fiff.constants import FIFF as FIFF
from .._fiff.matrix import write_named_matrix as write_named_matrix
from .._fiff.meas_info import Info as Info, write_info as write_info
from .._fiff.open import fiff_open as fiff_open
from .._fiff.pick import (
    pick_channels as pick_channels,
    pick_channels_forward as pick_channels_forward,
    pick_info as pick_info,
    pick_types as pick_types,
)
from .._fiff.tag import find_tag as find_tag, read_tag as read_tag
from .._fiff.tree import dir_tree_find as dir_tree_find
from .._fiff.write import (
    end_block as end_block,
    start_and_end_file as start_and_end_file,
    start_block as start_block,
    write_coord_trans as write_coord_trans,
    write_id as write_id,
    write_int as write_int,
    write_string as write_string,
)
from ..epochs import BaseEpochs as BaseEpochs
from ..evoked import Evoked as Evoked, EvokedArray as EvokedArray
from ..io import BaseRaw as BaseRaw, RawArray as RawArray
from ..label import Label as Label
from ..source_space._source_space import (
    find_source_space_hemi as find_source_space_hemi,
)
from ..transforms import (
    invert_transform as invert_transform,
    transform_surface_to as transform_surface_to,
    write_trans as write_trans,
)
from ..utils import (
    check_fname as check_fname,
    fill_doc as fill_doc,
    get_subjects_dir as get_subjects_dir,
    has_mne_c as has_mne_c,
    logger as logger,
    repr_html as repr_html,
    run_subprocess as run_subprocess,
    warn as warn,
)

class Forward(dict):
    """### Forward class to represent info from forward solution.

    Like `mne.Info`, this data structure behaves like a dictionary.
    It contains all metadata necessary for a forward solution.

    ### ⛔️ Warning
        This class should not be modified or created by users.
        Forward objects should be obtained using
        `mne.make_forward_solution` or `mne.read_forward_solution`.

    ### 📊 Attributes
    ----------
    ch_names : list of str
        A convenience wrapper accessible as ``fwd.ch_names`` which wraps
        ``fwd['info']['ch_names']``.

    ### 👉 See Also
    --------
    mne.make_forward_solution
    mne.read_forward_solution

    ### 📖 Notes
    -----
    Forward data is accessible via string keys using standard
    `python:dict` access (e.g., ``fwd['nsource'] == 4096``):

        source_ori : int
            The source orientation, either ``FIFF.FIFFV_MNE_FIXED_ORI`` or
            ``FIFF.FIFFV_MNE_FREE_ORI``.
        coord_frame : int
            The coordinate frame of the forward solution, usually
            ``FIFF.FIFFV_COORD_HEAD``.
        nsource : int
            The number of source locations.
        nchan : int
            The number of channels.
        sol : dict
            The forward solution, with entries:

            ``'data'`` : ndarray, shape (n_channels, nsource * n_ori)
                The forward solution data. The shape will be
                ``(n_channels, nsource)`` for a fixed-orientation forward and
                ``(n_channels, nsource * 3)`` for a free-orientation forward.
            ``'row_names'`` : list of str
                The channel names.
        mri_head_t : instance of Transform
            The mri ↔ head transformation that was used.
        info : instance of `mne.Info`
            The measurement information (with contents reduced compared to that
            of the original data).
        src : instance of `mne.SourceSpaces`
            The source space used during forward computation. This can differ
            from the original source space as:

            1. Source points are removed due to proximity to (or existing
               outside)
               the inner skull surface.
            2. The source space will be converted to the ``coord_frame`` of the
               forward solution, which typically means it gets converted from
               MRI to head coordinates.
        source_rr : ndarray, shape (n_sources, 3)
            The source locations.
        source_nn : ndarray, shape (n_sources, 3)
            The source normals. Will be all +Z (``(0, 0, 1.)``) for volume
            source spaces. For surface source spaces, these are normal to the
            cortical surface.
        surf_ori : int
            Whether ``sol`` is surface-oriented with the surface normal in the
            Z component (``FIFF.FIFFV_MNE_FIXED_ORI``) or +Z in the given
            ``coord_frame`` in the Z component (``FIFF.FIFFV_MNE_FREE_ORI``).

    Forward objects also have some attributes that are accessible via ``.``
    access, like ``fwd.ch_names``.
    """

    def copy(self):
        """### Copy the Forward instance."""
        ...
    def save(self, fname, *, overwrite: bool = False, verbose=None) -> None:
        """### Save the forward solution.

        ### 🛠️ Parameters
        ----------

        fname : path-like
            File name to save the forward solution to. It should end with
            ``-fwd.fif`` or ``-fwd.fif.gz`` to save to FIF, or ``-fwd.h5`` to save to
            HDF5.

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
    @property
    def ch_names(self): ...
    def pick_channels(self, ch_names, ordered: bool = False):
        """### Pick channels from this forward operator.

        ### 🛠️ Parameters
        ----------
        ch_names : list of str
            List of channels to include.
        ordered : bool
            If true (default False), treat ``include`` as an ordered list
            rather than a set.

        ### ⏎ Returns
        -------
        fwd : instance of Forward.
            The modified forward model.

        ### 📖 Notes
        -----
        Operates in-place.

        ✨ Added in vesion 0.20.0
        """
        ...

def read_forward_solution(fname, include=(), exclude=(), *, ordered=None, verbose=None):
    """### Read a forward solution a.k.a. lead field.

    ### 🛠️ Parameters
    ----------
    fname : path-like
        The file name, which should end with ``-fwd.fif``, ``-fwd.fif.gz``,
        ``_fwd.fif``, ``_fwd.fif.gz``, ``-fwd.h5``, or ``_fwd.h5``.
    include : list, optional
        List of names of channels to include. If empty all channels
        are included.
    exclude : list, optional
        List of names of channels to exclude. If empty include all channels.

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

    ### ⏎ Returns
    -------
    fwd : instance of Forward
        The forward solution.

    ### 👉 See Also
    --------
    write_forward_solution, make_forward_solution

    ### 📖 Notes
    -----
    Forward solutions, which are derived from an original forward solution with
    free orientation, are always stored on disk as forward solution with free
    orientation in X/Y/Z RAS coordinates. To apply any transformation to the
    forward operator (surface orientation, fixed orientation) please apply
    `convert_forward_solution` after reading the forward solution with
    `read_forward_solution`.

    Forward solutions, which are derived from an original forward solution with
    fixed orientation, are stored on disk as forward solution with fixed
    surface-based orientations. Please note that the transformation to
    surface-based, fixed orientation cannot be reverted after loading the
    forward solution with `read_forward_solution`.
    """
    ...

def convert_forward_solution(
    fwd,
    surf_ori: bool = False,
    force_fixed: bool = False,
    copy: bool = True,
    use_cps: bool = True,
    *,
    verbose=None,
):
    """### Convert forward solution between different source orientations.

    ### 🛠️ Parameters
    ----------
    fwd : Forward
        The forward solution to modify.
    surf_ori : bool, optional (default False)
        Use surface-based source coordinate system? Note that force_fixed=True
        implies surf_ori=True.
    force_fixed : bool, optional (default False)
        If True, force fixed source orientation mode.
    copy : bool
        Whether to return a new instance or modify in place.

    use_cps : bool
        Whether to use cortical patch statistics to define normal orientations for
        surfaces (default True).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    fwd : Forward
        The modified forward solution.
    """
    ...

def write_forward_solution(fname, fwd, overwrite: bool = False, verbose=None) -> None:
    """### Write forward solution to a file.

    ### 🛠️ Parameters
    ----------

    fname : path-like
        File name to save the forward solution to. It should end with
        ``-fwd.fif`` or ``-fwd.fif.gz`` to save to FIF, or ``-fwd.h5`` to save to
        HDF5.
    fwd : Forward
        Forward solution.

    overwrite : bool
        If True (default False), overwrite the destination file if it
        exists.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### 👉 See Also
    --------
    read_forward_solution

    ### 📖 Notes
    -----
    Forward solutions, which are derived from an original forward solution with
    free orientation, are always stored on disk as forward solution with free
    orientation in X/Y/Z RAS coordinates. Transformations (surface orientation,
    fixed orientation) will be reverted. To reapply any transformation to the
    forward operator please apply `convert_forward_solution` after
    reading the forward solution with `read_forward_solution`.

    Forward solutions, which are derived from an original forward solution with
    fixed orientation, are stored on disk as forward solution with fixed
    surface-based orientations. Please note that the transformation to
    surface-based, fixed orientation cannot be reverted after loading the
    forward solution with `read_forward_solution`.
    """
    ...

def is_fixed_orient(forward, orig: bool = False):
    """### Check if the forward operator is fixed orientation.

    ### 🛠️ Parameters
    ----------
    forward : instance of Forward
        The forward.
    orig : bool
        If True, consider the original source orientation.
        If False (default), consider the current source orientation.

    ### ⏎ Returns
    -------
    fixed_ori : bool
        Whether or not it is fixed orientation.
    """
    ...

def write_forward_meas_info(fid, info) -> None:
    """### Write measurement info stored in forward solution.

    ### 🛠️ Parameters
    ----------
    fid : file id
        The file id

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    """
    ...

def compute_orient_prior(forward, loose: str = "auto", verbose=None):
    """### Compute orientation prior.

    ### 🛠️ Parameters
    ----------
    forward : instance of Forward
        Forward operator.

    loose : float | 'auto' | dict
        Value that weights the source variances of the dipole components
        that are parallel (tangential) to the cortical surface. Can be:

        - float between 0 and 1 (inclusive)
            If 0, then the solution is computed with fixed orientation.
            If 1, it corresponds to free orientations.
        - ``'auto'`` (default)
            Uses 0.2 for surface source spaces (unless ``fixed`` is True) and
            1.0 for other source spaces (volume or mixed).
        - dict
            Mapping from the key for a given source space type (surface, volume,
            discrete) to the loose value. Useful mostly for mixed source spaces.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    orient_prior : ndarray, shape (n_sources,)
        Orientation priors.

    ### 👉 See Also
    --------
    compute_depth_prior
    """
    ...

def compute_depth_prior(
    forward,
    info,
    exp: float = 0.8,
    limit: float = 10.0,
    limit_depth_chs: bool = False,
    combine_xyz: str = "spectral",
    noise_cov=None,
    rank=None,
    verbose=None,
):
    """### Compute depth prior for depth weighting.

    ### 🛠️ Parameters
    ----------
    forward : instance of Forward
        The forward solution.

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    exp : float
        Exponent for the depth weighting, must be between 0 and 1.
    limit : float | None
        The upper bound on depth weighting.
        Can be None to be bounded by the largest finite prior.
    limit_depth_chs : bool | 'whiten'
        How to deal with multiple channel types in depth weighting.
        The default is True, which whitens based on the source sensitivity
        of the highest-SNR channel type. See Notes for details.

        🎭 Changed in version 0.18
           Added the "whiten" option.
    combine_xyz : 'spectral' | 'fro'
        When a loose (or free) orientation is used, how the depth weighting
        for each triplet should be calculated.
        If 'spectral', use the squared spectral norm of Gk.
        If 'fro', use the squared Frobenius norm of Gk.

        ✨ Added in vesion 0.18
    noise_cov : instance of Covariance | None
        The noise covariance to use to whiten the gain matrix when
        ``limit_depth_chs='whiten'``.

        ✨ Added in vesion 0.18

    rank : None | 'info' | 'full' | dict
        This controls the rank computation that can be read from the
        measurement info or estimated from the data. When a noise covariance
        is used for whitening, this should reflect the rank of that covariance,
        otherwise amplification of noise components can occur in whitening (e.g.,
        often during source localization).

        :data:`python:None`
            The rank will be estimated from the data after proper scaling of
            different channel types.
        ``'info'``
            The rank is inferred from ``info``. If data have been processed
            with Maxwell filtering, the Maxwell filtering header is used.
            Otherwise, the channel counts themselves are used.
            In both cases, the number of projectors is subtracted from
            the (effective) number of channels in the data.
            For example, if Maxwell filtering reduces the rank to 68, with
            two projectors the returned value will be 66.
        ``'full'``
            The rank is assumed to be full, i.e. equal to the
            number of good channels. If a `mne.Covariance` is passed, this can
            make sense if it has been (possibly improperly) regularized without
            taking into account the true data rank.
        `dict`
            Calculate the rank only for a subset of channel types, and explicitly
            specify the rank for the remaining channel types. This can be
            extremely useful if you already **know** the rank of (part of) your
            data, for instance in case you have calculated it earlier.

            This parameter must be a dictionary whose **keys** correspond to
            channel types in the data (e.g. ``'meg'``, ``'mag'``, ``'grad'``,
            ``'eeg'``), and whose **values** are integers representing the
            respective ranks. For example, ``{'mag': 90, 'eeg': 45}`` will assume
            a rank of ``90`` and ``45`` for magnetometer data and EEG data,
            respectively.

            The ranks for all channel types present in the data, but
            **not** specified in the dictionary will be estimated empirically.
            That is, if you passed a dataset containing magnetometer, gradiometer,
            and EEG data together with the dictionary from the previous example,
            only the gradiometer rank would be determined, while the specified
            magnetometer and EEG ranks would be taken for granted.

        The default is ``None``.

        ✨ Added in vesion 0.18

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    depth_prior : ndarray, shape (n_vertices,)
        The depth prior.

    ### 👉 See Also
    --------
    compute_orient_prior

    ### 📖 Notes
    -----
    The defaults used by the minimum norm code and sparse solvers differ.
    In particular, the values for MNE are::

        compute_depth_prior(..., limit=10., limit_depth_chs=True,
                            combine_xyz='spectral')

    In sparse solvers and LCMV, the values are::

        compute_depth_prior(..., limit=None, limit_depth_chs='whiten',
                            combine_xyz='fro')

    The ``limit_depth_chs`` argument can take the following values:

    * :data:`python:True` (default)
          Use only grad channels in depth weighting (equivalent to MNE C
          minimum-norm code). If grad channels aren't present, only mag
          channels will be used (if no mag, then eeg). This makes the depth
          prior dependent only on the sensor geometry (and relationship
          to the sources).
    * ``'whiten'``
          Compute a whitener and apply it to the gain matrix before computing
          the depth prior. In this case ``noise_cov`` must not be None.
          Whitening the gain matrix makes the depth prior
          depend on both sensor geometry and the data of interest captured
          by the noise covariance (e.g., projections, SNR).

          ✨ Added in vesion 0.18
    * :data:`python:False`
          Use all channels. Not recommended since the depth weighting will be
          biased toward whichever channel type has the largest values in
          SI units (such as EEG being orders of magnitude larger than MEG).
    """
    ...

def apply_forward(
    fwd,
    stc,
    info,
    start=None,
    stop=None,
    use_cps: bool = True,
    on_missing: str = "raise",
    verbose=None,
):
    """### Project source space currents to sensor space using a forward operator.

    The sensor space data is computed for all channels present in fwd. Use
    pick_channels_forward or pick_types_forward to restrict the solution to a
    subset of channels.

    The function returns an Evoked object, which is constructed from
    evoked_template. The evoked_template should be from the same MEG system on
    which the original data was acquired. An exception will be raised if the
    forward operator contains channels that are not present in the template.

    ### 🛠️ Parameters
    ----------
    fwd : Forward
        Forward operator to use.
    stc : SourceEstimate
        The source estimate from which the sensor space data is computed.

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    start : int, optional
        Index of first time sample (index not time is seconds).
    stop : int, optional
        Index of first time sample not to include (index not time is seconds).

    use_cps : bool
        Whether to use cortical patch statistics to define normal orientations for
        surfaces (default True).

        ✨ Added in vesion 0.15

    on_missing : 'raise' | 'warn' | 'ignore'
        Can be ``'raise'`` (default) to raise an error, ``'warn'`` to emit a
        warning, or ``'ignore'`` to ignore when ``stc`` has vertices that are not in ``fwd``.
        Default is "raise".

        ✨ Added in vesion 0.18

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    evoked : Evoked
        Evoked object with computed sensor space data.

    ### 👉 See Also
    --------
    apply_forward_raw: Compute sensor space data and return a Raw object.
    """
    ...

def apply_forward_raw(
    fwd,
    stc,
    info,
    start=None,
    stop=None,
    on_missing: str = "raise",
    use_cps: bool = True,
    verbose=None,
):
    """### Project source space currents to sensor space using a forward operator.

    The sensor space data is computed for all channels present in fwd. Use
    pick_channels_forward or pick_types_forward to restrict the solution to a
    subset of channels.

    The function returns a Raw object, which is constructed using provided
    info. The info object should be from the same MEG system on which the
    original data was acquired. An exception will be raised if the forward
    operator contains channels that are not present in the info.

    ### 🛠️ Parameters
    ----------
    fwd : Forward
        Forward operator to use.
    stc : SourceEstimate
        The source estimate from which the sensor space data is computed.

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    start : int, optional
        Index of first time sample (index not time is seconds).
    stop : int, optional
        Index of first time sample not to include (index not time is seconds).

    on_missing : 'raise' | 'warn' | 'ignore'
        Can be ``'raise'`` (default) to raise an error, ``'warn'`` to emit a
        warning, or ``'ignore'`` to ignore when ``stc`` has vertices that are not in ``fwd``.
        Default is "raise".

        ✨ Added in vesion 0.18

    use_cps : bool
        Whether to use cortical patch statistics to define normal orientations for
        surfaces (default True).

        ✨ Added in vesion 0.21

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    raw : Raw object
        Raw object with computed sensor space data.

    ### 👉 See Also
    --------
    apply_forward: Compute sensor space data and return an Evoked object.
    """
    ...

def restrict_forward_to_stc(fwd, stc, on_missing: str = "ignore"):
    """### Restrict forward operator to active sources in a source estimate.

    ### 🛠️ Parameters
    ----------
    fwd : instance of Forward
        Forward operator.
    stc : instance of SourceEstimate
        Source estimate.

    on_missing : 'raise' | 'warn' | 'ignore'
        Can be ``'raise'`` (default) to raise an error, ``'warn'`` to emit a
        warning, or ``'ignore'`` to ignore when ``stc`` has vertices that are not in ``fwd``.
        Default is "ignore".

        ✨ Added in vesion 0.18

    ### ⏎ Returns
    -------
    fwd_out : instance of Forward
        Restricted forward operator.

    ### 👉 See Also
    --------
    restrict_forward_to_label
    """
    ...

def restrict_forward_to_label(fwd, labels):
    """### Restrict forward operator to labels.

    ### 🛠️ Parameters
    ----------
    fwd : Forward
        Forward operator.
    labels : instance of Label | list
        Label object or list of label objects.

    ### ⏎ Returns
    -------
    fwd_out : dict
        Restricted forward operator.

    ### 👉 See Also
    --------
    restrict_forward_to_stc
    """
    ...

def average_forward_solutions(fwds, weights=None, verbose=None):
    """### Average forward solutions.

    ### 🛠️ Parameters
    ----------
    fwds : list of Forward
        Forward solutions to average. Each entry (dict) should be a
        forward solution.
    weights : array | None
        Weights to apply to each forward solution in averaging. If None,
        forward solutions will be equally weighted. Weights must be
        non-negative, and will be adjusted to sum to one.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    fwd : Forward
        The averaged forward solution.
    """
    ...
