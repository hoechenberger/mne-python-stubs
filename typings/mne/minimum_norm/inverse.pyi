from .._fiff.constants import FIFF as FIFF
from .._fiff.matrix import write_named_matrix as write_named_matrix
from .._fiff.open import fiff_open as fiff_open
from .._fiff.pick import (
    channel_type as channel_type,
    pick_channels as pick_channels,
    pick_info as pick_info,
    pick_types as pick_types,
)
from .._fiff.proj import make_projector as make_projector
from .._fiff.tag import find_tag as find_tag
from .._fiff.tree import dir_tree_find as dir_tree_find
from .._fiff.write import (
    end_block as end_block,
    start_and_end_file as start_and_end_file,
    start_block as start_block,
    write_coord_trans as write_coord_trans,
    write_float as write_float,
    write_float_matrix as write_float_matrix,
    write_int as write_int,
    write_string as write_string,
)
from ..cov import (
    Covariance as Covariance,
    compute_whitener as compute_whitener,
    prepare_noise_cov as prepare_noise_cov,
)
from ..epochs import BaseEpochs as BaseEpochs, EpochsArray as EpochsArray
from ..evoked import Evoked as Evoked, EvokedArray as EvokedArray
from ..forward import (
    compute_depth_prior as compute_depth_prior,
    compute_orient_prior as compute_orient_prior,
    convert_forward_solution as convert_forward_solution,
    is_fixed_orient as is_fixed_orient,
)
from ..forward.forward import write_forward_meas_info as write_forward_meas_info
from ..io import BaseRaw as BaseRaw
from ..source_space._source_space import (
    find_source_space_hemi as find_source_space_hemi,
    label_src_vertno_sel as label_src_vertno_sel,
)
from ..transforms import transform_surface_to as transform_surface_to
from ..utils import (
    check_fname as check_fname,
    logger as logger,
    repr_html as repr_html,
    warn as warn,
)
from _typeshed import Incomplete

INVERSE_METHODS: Incomplete

class InverseOperator(dict):
    """### InverseOperator class to represent info from inverse operator."""

    def copy(self):
        """### Return a copy of the InverseOperator."""
        ...
    @property
    def ch_names(self):
        """### Name of channels attached to the inverse operator."""
        ...
    @property
    def info(self):
        """### `mne.Info` attached to the inverse operator."""
        ...

def read_inverse_operator(fname, *, verbose=None):
    """### Read the inverse operator decomposition from a FIF file.

    ### 🛠️ Parameters
    ----------
    fname : path-like
        The name of the FIF file, which ends with ``-inv.fif`` or
        ``-inv.fif.gz``.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    inv : instance of InverseOperator
        The inverse operator.

    See Also
    --------
    write_inverse_operator, make_inverse_operator
    """
    ...

def write_inverse_operator(
    fname, inv, *, overwrite: bool = False, verbose=None
) -> None:
    """### Write an inverse operator to a FIF file.

    ### 🛠️ Parameters
    ----------
    fname : path-like
        The name of the FIF file, which ends with ``-inv.fif`` or
        ``-inv.fif.gz``.
    inv : dict
        The inverse operator.

    overwrite : bool
        If True (default False), overwrite the destination file if it
        exists.

        ✨ Added in vesion 1.0

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    read_inverse_operator
    """
    ...

def combine_xyz(vec, square: bool = False):
    """### Compute the three Cartesian components of a vector or matrix together.

    ### 🛠️ Parameters
    ----------
    vec : 2d array of shape [3 n x p]
        Input [ x1 y1 z1 ... x_n y_n z_n ] where x1 ... z_n
        can be vectors

    ### ⏎ Returns
    -------
    comb : array
        Output vector [sqrt(x1^2+y1^2+z1^2), ..., sqrt(x_n^2+y_n^2+z_n^2)]
    """
    ...

def prepare_inverse_operator(
    orig,
    nave,
    lambda2,
    method: str = "dSPM",
    method_params=None,
    copy: bool = True,
    verbose=None,
):
    """### Prepare an inverse operator for actually computing the inverse.

    ### 🛠️ Parameters
    ----------
    orig : dict
        The inverse operator structure read from a file.
    nave : int
        Number of averages (scales the noise covariance).
    lambda2 : float
        The regularization factor. Recommended to be 1 / SNR**2.
    method : "MNE" | "dSPM" | "sLORETA" | "eLORETA"
        Use minimum norm, dSPM (default), sLORETA, or eLORETA.
    method_params : dict | None
        Additional options for eLORETA. See Notes of `apply_inverse`.

        ✨ Added in vesion 0.16
    copy : bool | str
        If True (default), copy the inverse. False will not copy.
        Can be "non-src" to avoid copying the source space, which typically
        is not modified and can be large in memory.

        ✨ Added in vesion 0.21

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    inv : instance of InverseOperator
        Prepared inverse operator.
    """
    ...

def apply_inverse(
    evoked,
    inverse_operator,
    lambda2=0.1111111111111111,
    method: str = "dSPM",
    pick_ori=None,
    prepared: bool = False,
    label=None,
    method_params=None,
    return_residual: bool = False,
    use_cps: bool = True,
    verbose=None,
):
    """### Apply inverse operator to evoked data.

    ### 🛠️ Parameters
    ----------
    evoked : Evoked object
        Evoked data.
    inverse_operator : instance of InverseOperator
        Inverse operator.
    lambda2 : float
        The regularization parameter.
    method : "MNE" | "dSPM" | "sLORETA" | "eLORETA"
        Use minimum norm :footcite:`HamalainenIlmoniemi1994`,
        dSPM (default) :footcite:`DaleEtAl2000`,
        sLORETA :footcite:`Pascual-Marqui2002`, or
        eLORETA :footcite:`Pascual-Marqui2011`.

    pick_ori : None | "normal" | "vector"

        Options:

        - ``None``
            Pooling is performed by taking the norm of loose/free
            orientations. In case of a fixed source space no norm is computed
            leading to signed source activity.
        - ``"normal"``
            Only the normal to the cortical surface is kept. This is only
            implemented when working with loose orientations.

        - ``"vector"``
            No pooling of the orientations is done, and the vector result
            will be returned in the form of a `mne.VectorSourceEstimate`
            object.
    prepared : bool
        If True, do not call `prepare_inverse_operator`.
    label : Label | None
        Restricts the source estimates to a given label. If None,
        source estimates will be computed for the entire source space.
    method_params : dict | None
        Additional options for eLORETA. See Notes for details.

        ✨ Added in vesion 0.16
    return_residual : bool
        If True (default False), return the residual evoked data.
        Cannot be used with ``method=='eLORETA'``.

        ✨ Added in vesion 0.17

    use_cps : bool
        Whether to use cortical patch statistics to define normal orientations for
        surfaces (default True).

        Only used when the inverse is free orientation (``loose=1.``),
        not in surface orientation, and ``pick_ori='normal'``.

        ✨ Added in vesion 0.20

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    stc : SourceEstimate | VectorSourceEstimate | VolSourceEstimate
        The source estimates.
    residual : instance of Evoked
        The residual evoked data, only returned if return_residual is True.

    See Also
    --------
    apply_inverse_raw : Apply inverse operator to raw object.
    apply_inverse_epochs : Apply inverse operator to epochs object.
    apply_inverse_tfr_epochs : Apply inverse operator to epochs tfr object.
    apply_inverse_cov : Apply inverse operator to covariance object.

    ### 📖 Notes
    -----
    Currently only the ``method='eLORETA'`` has additional options.
    It performs an iterative fit with a convergence criterion, so you can
    pass a ``method_params`` `dict` with string keys mapping to values
    for:

        'eps' : float
            The convergence epsilon (default 1e-6).
        'max_iter' : int
            The maximum number of iterations (default 20).
            If less regularization is applied, more iterations may be
            necessary.
        'force_equal' : bool
            Force all eLORETA weights for each direction for a given
            location equal. The default is None, which means ``True`` for
            loose-orientation inverses and ``False`` for free- and
            fixed-orientation inverses. See below.

    The eLORETA paper :footcite:`Pascual-Marqui2011` defines how to compute
    inverses for fixed- and
    free-orientation inverses. In the free orientation case, the X/Y/Z
    orientation triplet for each location is effectively multiplied by a
    3x3 weight matrix. This is the behavior obtained with
    ``force_equal=False`` parameter.

    However, other noise normalization methods (dSPM, sLORETA) multiply all
    orientations for a given location by a single value.
    Using ``force_equal=True`` mimics this behavior by modifying the iterative
    algorithm to choose uniform weights (equivalent to a 3x3 diagonal matrix
    with equal entries).

    It is necessary to use ``force_equal=True``
    with loose orientation inverses (e.g., ``loose=0.2``), otherwise the
    solution resembles a free-orientation inverse (``loose=1.0``).
    It is thus recommended to use ``force_equal=True`` for loose orientation
    and ``force_equal=False`` for free orientation inverses. This is the
    behavior used when the parameter ``force_equal=None`` (default behavior).

    References
    ----------
    .. footbibliography::
    """
    ...

def apply_inverse_raw(
    raw,
    inverse_operator,
    lambda2,
    method: str = "dSPM",
    label=None,
    start=None,
    stop=None,
    nave: int = 1,
    time_func=None,
    pick_ori=None,
    buffer_size=None,
    prepared: bool = False,
    method_params=None,
    use_cps: bool = True,
    verbose=None,
):
    """### Apply inverse operator to Raw data.

    ### 🛠️ Parameters
    ----------
    raw : Raw object
        Raw data.
    inverse_operator : dict
        Inverse operator.
    lambda2 : float
        The regularization parameter.
    method : "MNE" | "dSPM" | "sLORETA" | "eLORETA"
        Use minimum norm, dSPM (default), sLORETA, or eLORETA.
    label : Label | None
        Restricts the source estimates to a given label. If None,
        source estimates will be computed for the entire source space.
    start : int
        Index of first time sample (index not time is seconds).
    stop : int
        Index of first time sample not to include (index not time is seconds).
    nave : int
        Number of averages used to regularize the solution.
        Set to 1 on raw data.
    time_func : callable
        Linear function applied to sensor space time series.

    pick_ori : None | "normal" | "vector"

        Options:

        - ``None``
            Pooling is performed by taking the norm of loose/free
            orientations. In case of a fixed source space no norm is computed
            leading to signed source activity.
        - ``"normal"``
            Only the normal to the cortical surface is kept. This is only
            implemented when working with loose orientations.

        - ``"vector"``
            No pooling of the orientations is done, and the vector result
            will be returned in the form of a `mne.VectorSourceEstimate`
            object.
    buffer_size : int (or None)
        If not None, the computation of the inverse and the combination of the
        current components is performed in segments of length buffer_size
        samples. While slightly slower, this is useful for long datasets as it
        reduces the memory requirements by approx. a factor of 3 (assuming
        buffer_size << data length).
        Note that this setting has no effect for fixed-orientation inverse
        operators.
    prepared : bool
        If True, do not call `prepare_inverse_operator`.
    method_params : dict | None
        Additional options for eLORETA. See Notes of `apply_inverse`.

        ✨ Added in vesion 0.16

    use_cps : bool
        Whether to use cortical patch statistics to define normal orientations for
        surfaces (default True).

        Only used when the inverse is free orientation (``loose=1.``),
        not in surface orientation, and ``pick_ori='normal'``.

        ✨ Added in vesion 0.20

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    stc : SourceEstimate | VectorSourceEstimate | VolSourceEstimate
        The source estimates.

    See Also
    --------
    apply_inverse : Apply inverse operator to evoked object.
    apply_inverse_epochs : Apply inverse operator to epochs object.
    apply_inverse_tfr_epochs : Apply inverse operator to epochs tfr object.
    apply_inverse_cov : Apply inverse operator to covariance object.
    """
    ...

def apply_inverse_epochs(
    epochs,
    inverse_operator,
    lambda2,
    method: str = "dSPM",
    label=None,
    nave: int = 1,
    pick_ori=None,
    return_generator: bool = False,
    prepared: bool = False,
    method_params=None,
    use_cps: bool = True,
    verbose=None,
):
    """### Apply inverse operator to Epochs.

    ### 🛠️ Parameters
    ----------
    epochs : Epochs object
        Single trial epochs.
    inverse_operator : dict
        Inverse operator.
    lambda2 : float
        The regularization parameter.
    method : "MNE" | "dSPM" | "sLORETA" | "eLORETA"
        Use minimum norm, dSPM (default), sLORETA, or eLORETA.
    label : Label | None
        Restricts the source estimates to a given label. If None,
        source estimates will be computed for the entire source space.
    nave : int
        Number of averages used to regularize the solution.
        Set to 1 on single Epoch by default.

    pick_ori : None | "normal" | "vector"

        Options:

        - ``None``
            Pooling is performed by taking the norm of loose/free
            orientations. In case of a fixed source space no norm is computed
            leading to signed source activity.
        - ``"normal"``
            Only the normal to the cortical surface is kept. This is only
            implemented when working with loose orientations.

        - ``"vector"``
            No pooling of the orientations is done, and the vector result
            will be returned in the form of a `mne.VectorSourceEstimate`
            object.
    return_generator : bool
        Return a generator object instead of a list. This allows iterating
        over the stcs without having to keep them all in memory.
    prepared : bool
        If True, do not call `prepare_inverse_operator`.
    method_params : dict | None
        Additional options for eLORETA. See Notes of `apply_inverse`.

        ✨ Added in vesion 0.16

    use_cps : bool
        Whether to use cortical patch statistics to define normal orientations for
        surfaces (default True).

        Only used when the inverse is free orientation (``loose=1.``),
        not in surface orientation, and ``pick_ori='normal'``.

        ✨ Added in vesion 0.20

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    stcs : list of (SourceEstimate | VectorSourceEstimate | VolSourceEstimate)
        The source estimates for all epochs.

    See Also
    --------
    apply_inverse_raw : Apply inverse operator to raw object.
    apply_inverse : Apply inverse operator to evoked object.
    apply_inverse_tfr_epochs : Apply inverse operator to epochs tfr object.
    apply_inverse_cov : Apply inverse operator to a covariance object.
    """
    ...

def apply_inverse_tfr_epochs(
    epochs_tfr,
    inverse_operator,
    lambda2,
    method: str = "dSPM",
    label=None,
    nave: int = 1,
    pick_ori=None,
    return_generator: bool = False,
    prepared: bool = False,
    method_params=None,
    use_cps: bool = True,
    verbose=None,
):
    """### Apply inverse operator to EpochsTFR.

    ### 🛠️ Parameters
    ----------
    epochs_tfr : EpochsTFR object
        Single trial, phase-amplitude (complex-valued), time-frequency epochs.
    inverse_operator : list of dict | dict
        The inverse operator for each frequency or a single inverse operator
        to use for all frequencies.
    lambda2 : float
        The regularization parameter.
    method : "MNE" | "dSPM" | "sLORETA" | "eLORETA"
        Use minimum norm, dSPM (default), sLORETA, or eLORETA.
    label : Label | None
        Restricts the source estimates to a given label. If None,
        source estimates will be computed for the entire source space.
    nave : int
        Number of averages used to regularize the solution.
        Set to 1 on single Epoch by default.

    pick_ori : None | "normal" | "vector"

        Options:

        - ``None``
            Pooling is performed by taking the norm of loose/free
            orientations. In case of a fixed source space no norm is computed
            leading to signed source activity.
        - ``"normal"``
            Only the normal to the cortical surface is kept. This is only
            implemented when working with loose orientations.

        - ``"vector"``
            No pooling of the orientations is done, and the vector result
            will be returned in the form of a `mne.VectorSourceEstimate`
            object.
    return_generator : bool
        Return a generator object instead of a list. This allows iterating
        over the stcs without having to keep them all in memory.
    prepared : bool
        If True, do not call `prepare_inverse_operator`.
    method_params : dict | None
        Additional options for eLORETA. See Notes of `apply_inverse`.

    use_cps : bool
        Whether to use cortical patch statistics to define normal orientations for
        surfaces (default True).

        Only used when the inverse is free orientation (``loose=1.``),
        not in surface orientation, and ``pick_ori='normal'``.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    stcs : list of list of (SourceEstimate | VectorSourceEstimate | VolSourceEstimate)
        The source estimates for all frequencies (outside list) and for
        all epochs (inside list).

    See Also
    --------
    apply_inverse_raw : Apply inverse operator to raw object.
    apply_inverse : Apply inverse operator to evoked object.
    apply_inverse_epochs : Apply inverse operator to epochs object.
    apply_inverse_cov : Apply inverse operator to a covariance object.
    """
    ...

def apply_inverse_cov(
    cov,
    info,
    inverse_operator,
    nave: int = 1,
    lambda2=0.1111111111111111,
    method: str = "dSPM",
    pick_ori=None,
    prepared: bool = False,
    label=None,
    method_params=None,
    use_cps: bool = True,
    verbose=None,
):
    """### Apply inverse operator to covariance data.

    ### 🛠️ Parameters
    ----------
    cov : instance of Covariance
        Covariance data, computed on the time segment for which to compute
        source power.

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement. Used specify the channels to include.
    inverse_operator : instance of InverseOperator
        Inverse operator.
    nave : int
        Number of averages used to regularize the solution.
    lambda2 : float
        The regularization parameter.
    method : "MNE" | "dSPM" | "sLORETA" | "eLORETA"
        Use minimum norm, dSPM (default), sLORETA, or eLORETA.

    pick_ori : None | "normal"

        Options:

        - ``None``
            Pooling is performed by taking the norm of loose/free
            orientations. In case of a fixed source space no norm is computed
            leading to signed source activity.
        - ``"normal"``
            Only the normal to the cortical surface is kept. This is only
            implemented when working with loose orientations.
    prepared : bool
        If True, do not call `prepare_inverse_operator`.
    label : Label | None
        Restricts the source estimates to a given label. If None,
        source estimates will be computed for the entire source space.
    method_params : dict | None
        Additional options for eLORETA. See Notes for details.

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
    stc : SourceEstimate | VectorSourceEstimate | VolSourceEstimate
        The source estimates.

    See Also
    --------
    apply_inverse : Apply inverse operator to evoked object.
    apply_inverse_raw : Apply inverse operator to raw object.
    apply_inverse_epochs : Apply inverse operator to epochs object.
    apply_inverse_tfr_epochs : Apply inverse operator to epochs tfr object.

    ### 📖 Notes
    -----
    ✨ Added in vesion 0.20

    This code is based on the original research code from
    :footcite:`Sabbagh2020` and has been useful to correct for individual field
    spread using source localization in the context of predictive modeling.

    References
    ----------
    .. footbibliography::
    """
    ...

def make_inverse_operator(
    info,
    forward,
    noise_cov,
    loose: str = "auto",
    depth: float = 0.8,
    fixed: str = "auto",
    rank=None,
    use_cps: bool = True,
    verbose=None,
):
    """### Assemble inverse operator.

    ### 🛠️ Parameters
    ----------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
        Specifies the channels to include. Bad channels (in ``info['bads']``)
        are not used.
    forward : instance of Forward
        Forward operator. See `mne.make_forward_solution` to create the operator.
    noise_cov : instance of Covariance
        The noise covariance matrix. See `mne.compute_raw_covariance` and
        `mne.compute_covariance` to compute the noise covariance matrix on
        `mne.io.Raw` and `mne.Epochs` respectively.

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

    depth : None | float | dict
        How to weight (or normalize) the forward using a depth prior.
        If float (default 0.8), it acts as the depth weighting exponent (``exp``)
        to use None is equivalent to 0, meaning no depth weighting is performed.
        It can also be a `dict` containing keyword arguments to pass to
        `mne.forward.compute_depth_prior` (see docstring for details and
        defaults). This is effectively ignored when ``method='eLORETA'``.

        🎭 Changed in version 0.20
           Depth bias ignored for ``method='eLORETA'``.
    fixed : bool | 'auto'
        Use fixed source orientations normal to the cortical mantle. If True,
        the loose parameter must be ``"auto"`` or ``0``. If ``'auto'``, the loose value
        is used.

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
    inv : instance of InverseOperator
        Inverse operator.

    ### 📖 Notes
    -----
    For different sets of options (**loose**, **depth**, **fixed**) to work,
    the forward operator must have been loaded using a certain configuration
    (i.e., with **force_fixed** and **surf_ori** set appropriately). For
    example, given the desired inverse type (with representative choices
    of **loose** = 0.2 and **depth** = 0.8 shown in the table in various
    places, as these are the defaults for those parameters):

        +---------------------+-----------+-----------+-----------+-----------------+--------------+
        | Inverse desired                             | Forward parameters allowed                 |
        +=====================+===========+===========+===========+=================+==============+
        |                     | **loose** | **depth** | **fixed** | **force_fixed** | **surf_ori** |
        +---------------------+-----------+-----------+-----------+-----------------+--------------+
        | | Loose constraint, | 0.2       | 0.8       | False     | False           | True         |
        | | Depth weighted    |           |           |           |                 |              |
        +---------------------+-----------+-----------+-----------+-----------------+--------------+
        | | Loose constraint  | 0.2       | None      | False     | False           | True         |
        +---------------------+-----------+-----------+-----------+-----------------+--------------+
        | | Free orientation, | 1.0       | 0.8       | False     | False           | True         |
        | | Depth weighted    |           |           |           |                 |              |
        +---------------------+-----------+-----------+-----------+-----------------+--------------+
        | | Free orientation  | 1.0       | None      | False     | False           | True | False |
        +---------------------+-----------+-----------+-----------+-----------------+--------------+
        | | Fixed constraint, | 0.0       | 0.8       | True      | False           | True         |
        | | Depth weighted    |           |           |           |                 |              |
        +---------------------+-----------+-----------+-----------+-----------------+--------------+
        | | Fixed constraint  | 0.0       | None      | True      | True            | True         |
        +---------------------+-----------+-----------+-----------+-----------------+--------------+

    Also note that, if the source space (as stored in the forward solution)
    has patch statistics computed, these are used to improve the depth
    weighting. Thus slightly different results are to be expected with
    and without this information.

    For depth weighting, 0.8 is generally good for MEG, and between 2 and 5
    is good for EEG, see :footcite:t:`LinEtAl2006a`.

    References
    ----------
    .. footbibliography::
    """
    ...

def compute_rank_inverse(inv):
    """### Compute the rank of a linear inverse operator (MNE, dSPM, etc.).

    ### 🛠️ Parameters
    ----------
    inv : instance of InverseOperator
        The inverse operator.

    ### ⏎ Returns
    -------
    rank : int
        The rank of the inverse operator.
    """
    ...

def estimate_snr(evoked, inv, verbose=None):
    """### Estimate the SNR as a function of time for evoked data.

    ### 🛠️ Parameters
    ----------
    evoked : instance of Evoked
        Evoked instance.
    inv : instance of InverseOperator
        The inverse operator.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    snr : ndarray, shape (n_times,)
        The SNR estimated from the whitened data (i.e., GFP of whitened data).
    snr_est : ndarray, shape (n_times,)
        The SNR estimated using the mismatch between the unregularized
        solution and the regularized solution.

    ### 📖 Notes
    -----
    ``snr_est`` is estimated by using different amounts of inverse
    regularization and checking the mismatch between predicted and
    measured whitened data.

    In more detail, given our whitened inverse obtained from SVD:

    .. math::

        \\tilde{M} = R^\\frac{1}{2}V\\Gamma U^T

    The values in the diagonal matrix :math:`\\Gamma` are expressed in terms
    of the chosen regularization :math:`\\lambda^2 \\sim 1/\\rm{SNR}^2`
    and singular values :math:`\\lambda_k` as:

    .. math::

        \\gamma_k = \\frac{1}{\\lambda_k}\\frac{\\lambda_k^2}{\\lambda_k^2 + \\lambda^2}

    We also know that our predicted data is given by:

    .. math::

        \\hat{x}(t) = G\\hat{j}(t)=C^\\frac{1}{2}U\\Pi w(t)

    And thus our predicted whitened data is just:

    .. math::

        \\hat{w}(t) = U\\Pi w(t)

    Where :math:`\\Pi` is diagonal with entries entries:

    .. math::

        \\lambda_k\\gamma_k = \\frac{\\lambda_k^2}{\\lambda_k^2 + \\lambda^2}

    If we use no regularization, note that :math:`\\Pi` is just the
    identity matrix. Here we test the squared magnitude of the difference
    between unregularized solution and regularized solutions, choosing the
    biggest regularization that achieves a :math:`\\chi^2`-test significance
    of 0.001.

    ✨ Added in vesion 0.9.0
    """
    ...
