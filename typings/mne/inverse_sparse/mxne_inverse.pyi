from .._fiff.proj import deactivate_proj as deactivate_proj
from ..dipole import Dipole as Dipole
from ..forward import is_fixed_orient as is_fixed_orient
from ..minimum_norm.inverse import combine_xyz as combine_xyz
from ..source_estimate import SourceEstimate as SourceEstimate
from ..utils import (
    check_random_state as check_random_state,
    logger as logger,
    sum_squared as sum_squared,
    warn as warn,
)
from .mxne_optim import (
    groups_norm2 as groups_norm2,
    iterative_mixed_norm_solver as iterative_mixed_norm_solver,
    iterative_tf_mixed_norm_solver as iterative_tf_mixed_norm_solver,
    mixed_norm_solver as mixed_norm_solver,
    norm_epsilon_inf as norm_epsilon_inf,
    norm_l2inf as norm_l2inf,
    tf_mixed_norm_solver as tf_mixed_norm_solver,
)

def make_stc_from_dipoles(dipoles, src, verbose=None):
    """Convert a list of spatio-temporal dipoles into a SourceEstimate.

    Parameters
    ----------
    dipoles : Dipole | list of instances of Dipole
        The dipoles to convert.
    src : instance of SourceSpaces
        The source space used to generate the forward operator.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    stc : SourceEstimate
        The source estimate.
    """
    ...

def mixed_norm(
    evoked,
    forward,
    noise_cov,
    alpha: str = "sure",
    loose: str = "auto",
    depth: float = 0.8,
    maxit: int = 3000,
    tol: float = 0.0001,
    active_set_size: int = 10,
    debias: bool = True,
    time_pca: bool = True,
    weights=None,
    weights_min: float = 0.0,
    solver: str = "auto",
    n_mxne_iter: int = 1,
    return_residual: bool = False,
    return_as_dipoles: bool = False,
    dgap_freq: int = 10,
    rank=None,
    pick_ori=None,
    sure_alpha_grid: str = "auto",
    random_state=None,
    verbose=None,
):
    """Mixed-norm estimate (MxNE) and iterative reweighted MxNE (irMxNE).

    Compute L1/L2 mixed-norm solution :footcite:`GramfortEtAl2012` or L0.5/L2
    :footcite:`StrohmeierEtAl2016` mixed-norm solution on evoked data.

    Parameters
    ----------
    evoked : instance of Evoked or list of instances of Evoked
        Evoked data to invert.
    forward : dict
        Forward operator.
    noise_cov : instance of Covariance
        Noise covariance to compute whitener.
    alpha : float | str
        Regularization parameter. If float it should be in the range [0, 100):
        0 means no regularization, 100 would give 0 active dipole.
        If ``'sure'`` (default), the SURE method from
        :footcite:`DeledalleEtAl2014` will be used.

        🎭 Changed in version 0.24
          The default was changed to ``'sure'``.

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
    maxit : int
        Maximum number of iterations.
    tol : float
        Tolerance parameter.
    active_set_size : int | None
        Size of active set increment. If None, no active set strategy is used.
    debias : bool
        Remove coefficient amplitude bias due to L1 penalty.
    time_pca : bool or int
        If True the rank of the concatenated epochs is reduced to
        its true dimension. If is 'int' the rank is limited to this value.
    weights : None | array | SourceEstimate
        Weight for penalty in mixed_norm. Can be None, a
        1d array with shape (n_sources,), or a SourceEstimate (e.g. obtained
        with wMNE, dSPM, or fMRI).
    weights_min : float
        Do not consider in the estimation sources for which weights
        is less than weights_min.
    solver : 'cd' | 'bcd' | 'auto'
        The algorithm to use for the optimization. 'cd' uses
        coordinate descent, and 'bcd' applies block coordinate descent.
        'cd' is only available for fixed orientation.
    n_mxne_iter : int
        The number of MxNE iterations. If > 1, iterative reweighting
        is applied.
    return_residual : bool
        If True, the residual is returned as an Evoked instance.
    return_as_dipoles : bool
        If True, the sources are returned as a list of Dipole instances.
    dgap_freq : int or np.inf
        The duality gap is evaluated every dgap_freq iterations. Ignored if
        solver is 'cd'.

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

        ✨ Added in version 0.18

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
    sure_alpha_grid : array | str
        If ``'auto'`` (default), the SURE is evaluated along 15 uniformly
        distributed alphas between alpha_max and 0.1 * alpha_max. If array, the
        grid is directly specified. Ignored if alpha is not "sure".

        ✨ Added in version 0.24
    random_state : int | None
        The random state used in a random number generator for delta and
        epsilon used for the SURE computation. Defaults to None.

        ✨ Added in version 0.24

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    stc : SourceEstimate | list of SourceEstimate
        Source time courses for each evoked data passed as input.
    residual : instance of Evoked
        The residual a.k.a. data not explained by the sources.
        Only returned if return_residual is True.

    See Also
    --------
    tf_mixed_norm

    References
    ----------
    .. footbibliography::
    """
    ...

def tf_mixed_norm(
    evoked,
    forward,
    noise_cov,
    loose: str = "auto",
    depth: float = 0.8,
    maxit: int = 3000,
    tol: float = 0.0001,
    weights=None,
    weights_min: float = 0.0,
    pca: bool = True,
    debias: bool = True,
    wsize: int = 64,
    tstep: int = 4,
    window: float = 0.02,
    return_residual: bool = False,
    return_as_dipoles: bool = False,
    alpha=None,
    l1_ratio=None,
    dgap_freq: int = 10,
    rank=None,
    pick_ori=None,
    n_tfmxne_iter: int = 1,
    verbose=None,
):
    """Time-Frequency Mixed-norm estimate (TF-MxNE).

    Compute L1/L2 + L1 mixed-norm solution on time-frequency
    dictionary. Works with evoked data
    :footcite:`GramfortEtAl2013b,GramfortEtAl2011`.

    Parameters
    ----------
    evoked : instance of Evoked
        Evoked data to invert.
    forward : dict
        Forward operator.
    noise_cov : instance of Covariance
        Noise covariance to compute whitener.

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
    maxit : int
        Maximum number of iterations.
    tol : float
        Tolerance parameter.
    weights : None | array | SourceEstimate
        Weight for penalty in mixed_norm. Can be None or
        1d array of length n_sources or a SourceEstimate e.g. obtained
        with wMNE or dSPM or fMRI.
    weights_min : float
        Do not consider in the estimation sources for which weights
        is less than weights_min.
    pca : bool
        If True the rank of the data is reduced to true dimension.
    debias : bool
        Remove coefficient amplitude bias due to L1 penalty.
    wsize : int or array-like
        Length of the STFT window in samples (must be a multiple of 4).
        If an array is passed, multiple TF dictionaries are used (each having
        its own wsize and tstep) and each entry of wsize must be a multiple
        of 4. See :footcite:`BekhtiEtAl2016`.
    tstep : int or array-like
        Step between successive windows in samples (must be a multiple of 2,
        a divider of wsize and smaller than wsize/2) (default: wsize/2).
        If an array is passed, multiple TF dictionaries are used (each having
        its own wsize and tstep), and each entry of tstep must be a multiple
        of 2 and divide the corresponding entry of wsize. See
        :footcite:`BekhtiEtAl2016`.
    window : float or (float, float)
        Length of time window used to take care of edge artifacts in seconds.
        It can be one float or float if the values are different for left
        and right window length.
    return_residual : bool
        If True, the residual is returned as an Evoked instance.
    return_as_dipoles : bool
        If True, the sources are returned as a list of Dipole instances.
    alpha : float in [0, 100) or None
        Overall regularization parameter.
        If alpha and l1_ratio are not None, alpha_space and alpha_time are
        overridden by alpha * alpha_max * (1. - l1_ratio) and alpha * alpha_max
        * l1_ratio. 0 means no regularization, 100 would give 0 active dipole.
    l1_ratio : float in [0, 1] or None
        Proportion of temporal regularization.
        If l1_ratio and alpha are not None, alpha_space and alpha_time are
        overridden by alpha * alpha_max * (1. - l1_ratio) and alpha * alpha_max
        * l1_ratio. 0 means no time regularization a.k.a. MxNE.
    dgap_freq : int or np.inf
        The duality gap is evaluated every dgap_freq iterations.

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

        ✨ Added in version 0.18

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
    n_tfmxne_iter : int
        Number of TF-MxNE iterations. If > 1, iterative reweighting is applied.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    stc : instance of SourceEstimate
        Source time courses.
    residual : instance of Evoked
        The residual a.k.a. data not explained by the sources.
        Only returned if return_residual is True.

    See Also
    --------
    mixed_norm

    References
    ----------
    .. footbibliography::
    """
    ...
