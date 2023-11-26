from .._fiff.pick import pick_channels_cov as pick_channels_cov, pick_info as pick_info
from ..minimum_norm.inverse import combine_xyz as combine_xyz
from ..rank import compute_rank as compute_rank
from ..utils import logger as logger
from ._compute_beamformer import Beamformer as Beamformer

def make_lcmv(
    info,
    forward,
    data_cov,
    reg: float = 0.05,
    noise_cov=None,
    label=None,
    pick_ori=None,
    rank: str = "info",
    weight_norm: str = "unit-noise-gain-invariant",
    reduce_rank: bool = False,
    depth=None,
    inversion: str = "matrix",
    verbose=None,
):
    """Compute LCMV spatial filter.

    Parameters
    ----------

    info : mne.Info
        The :class:`mne.Info` object with information about the sensors and methods of measurement.
        Specifies the channels to include. Bad channels (in ``info['bads']``)
        are not used.
    forward : instance of Forward
        Forward operator.
    data_cov : instance of Covariance
        The data covariance.
    reg : float
        The regularization for the whitened data covariance.
    noise_cov : instance of Covariance
        The noise covariance. If provided, whitening will be done. Providing a
        noise covariance is mandatory if you mix sensor types, e.g.
        gradiometers with magnetometers or EEG with MEG.

        .. note::
            If ``noise_cov`` is ``None`` and ``weight_norm='unit-noise-gain'``,
            the unit noise is assumed to be 1 in SI units, e.g., 1 T for
            magnetometers, 1 V for EEG, so resulting amplitudes will be tiny.
            Consider using :func:`mne.make_ad_hoc_cov` to provide a
            ``noise_cov`` to set noise values that are more reasonable for
            neural data or using ``weight_norm='nai'`` for weight-normalized
            beamformer output that is scaled by a noise estimate.
    label : instance of Label
        Restricts the LCMV solution to a given label.

    pick_ori : None | str
        For forward solutions with fixed orientation, None (default) must be
        used and a scalar beamformer is computed. For free-orientation forward
        solutions, a vector beamformer is computed and:

        - ``None``
            Orientations are pooled after computing a vector beamformer (Default).
        - ``'normal'``
            Filters are computed for the orientation tangential to the
            cortical surface.
        - ``'max-power'``
            Filters are computed for the orientation that maximizes power.

        - ``'vector'``
            Keeps the currents for each direction separate

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
            number of good channels. If a mne.Covariance` is passed, this can
            make sense if it has been (possibly improperly) regularized without
            taking into account the true data rank.
        :class:`dict`
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

        The default is ``'info'``.

    weight_norm : str | None
        Can be:

        - ``None``
            The unit-gain LCMV beamformer :footcite:`SekiharaNagarajan2008` will be
            computed.
        - ``'unit-noise-gain'``
            The unit-noise gain minimum variance beamformer will be computed
            (Borgiotti-Kaplan beamformer) :footcite:`SekiharaNagarajan2008`,
            which is not rotation invariant when ``pick_ori='vector'``.
            This should be combined with
            :meth:`stc.project('pca') <mne.VectorSourceEstimate.project>` to follow
            the definition in :footcite:`SekiharaNagarajan2008`.
        - ``'nai'``
            The Neural Activity Index :footcite:`VanVeenEtAl1997` will be computed,
            which simply scales all values from ``'unit-noise-gain'`` by a fixed
            value.
        - ``'unit-noise-gain-invariant'``
            Compute a rotation-invariant normalization using the matrix square
            root. This differs from ``'unit-noise-gain'`` only when
            ``pick_ori='vector'``, creating a solution that:

            1. Is rotation invariant (``'unit-noise-gain'`` is not);
            2. Satisfies the first requirement from
               :footcite:`SekiharaNagarajan2008` that ``w @ w.conj().T == I``,
               whereas ``'unit-noise-gain'`` has non-zero off-diagonals; but
            3. Does not satisfy the second requirement that ``w @ G.T = θI``,
               which arguably does not make sense for a rotation-invariant
               solution.

        Defaults to ``'unit-noise-gain-invariant'``.

    reduce_rank : bool
        If True, the rank of the denominator of the beamformer formula (i.e.,
        during pseudo-inversion) will be reduced by one for each spatial location.
        Setting ``reduce_rank=True`` is typically necessary if you use a single
        sphere model with MEG data.

        .. versionchanged:: 0.20
            Support for reducing rank in all modes (previously only supported
            ``pick='max_power'`` with weight normalization).

    depth : None | float | dict
        How to weight (or normalize) the forward using a depth prior.
        If float (default 0.8), it acts as the depth weighting exponent (``exp``)
        to use None is equivalent to 0, meaning no depth weighting is performed.
        It can also be a :class:`dict` containing keyword arguments to pass to
        :func:`mne.forward.compute_depth_prior` (see docstring for details and
        defaults). This is effectively ignored when ``method='eLORETA'``.

        .. versionchanged:: 0.20
           Depth bias ignored for ``method='eLORETA'``.

        .. versionadded:: 0.18

    inversion : 'single' | 'matrix'
        This determines how the beamformer deals with source spaces in "free"
        orientation. Such source spaces define three orthogonal dipoles at each
        source point. When ``inversion='single'``, each dipole is considered
        as an individual source and the corresponding spatial filter is
        computed for each dipole separately. When ``inversion='matrix'``, all
        three dipoles at a source vertex are considered as a group and the
        spatial filters are computed jointly using a matrix inversion. While
        ``inversion='single'`` is more stable, ``inversion='matrix'`` is more
        precise. See section 5 of :footcite:`vanVlietEtAl2018`.
        Defaults to ``'matrix'``.

        .. versionadded:: 0.21

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    filters : instance of Beamformer
        Dictionary containing filter weights from LCMV beamformer.
        Contains the following keys:

            'kind' : str
                The type of beamformer, in this case 'LCMV'.
            'weights' : array
                The filter weights of the beamformer.
            'data_cov' : instance of Covariance
                The data covariance matrix used to compute the beamformer.
            'noise_cov' : instance of Covariance | None
                The noise covariance matrix used to compute the beamformer.
            'whitener' : None | ndarray, shape (n_channels, n_channels)
                Whitening matrix, provided if whitening was applied to the
                covariance matrix and leadfield during computation of the
                beamformer weights.
            'weight_norm' : str | None
                Type of weight normalization used to compute the filter
                weights.
            'pick-ori' : None | 'max-power' | 'normal' | 'vector'
                The orientation in which the beamformer filters were computed.
            'ch_names' : list of str
                Channels used to compute the beamformer.
            'proj' : array
                Projections used to compute the beamformer.
            'is_ssp' : bool
                If True, projections were applied prior to filter computation.
            'vertices' : list
                Vertices for which the filter weights were computed.
            'is_free_ori' : bool
                If True, the filter was computed with free source orientation.
            'n_sources' : int
                Number of source location for which the filter weight were
                computed.
            'src_type' : str
                Type of source space.
            'source_nn' : ndarray, shape (n_sources, 3)
                For each source location, the surface normal.
            'proj' : ndarray, shape (n_channels, n_channels)
                Projections used to compute the beamformer.
            'subject' : str
                The subject ID.
            'rank' : int
                The rank of the data covariance matrix used to compute the
                beamformer weights.
            'max-power-ori' : ndarray, shape (n_sources, 3) | None
                When pick_ori='max-power', this fields contains the estimated
                direction of maximum power at each source location.
            'inversion' : 'single' | 'matrix'
                Whether the spatial filters were computed for each dipole
                separately or jointly for all dipoles at each vertex using a
                matrix inversion.

    Notes
    -----
    The original reference is :footcite:`VanVeenEtAl1997`.

    To obtain the Sekihara unit-noise-gain vector beamformer, you should use
    ``weight_norm='unit-noise-gain', pick_ori='vector'`` followed by
    :meth:`vec_stc.project('pca', src) <mne.VectorSourceEstimate.project>`.

    .. versionchanged:: 0.21
       The computations were extensively reworked, and the default for
       ``weight_norm`` was set to ``'unit-noise-gain-invariant'``.

    References
    ----------
    .. footbibliography::
    """
    ...

def apply_lcmv(evoked, filters, *, verbose=None):
    """Apply Linearly Constrained Minimum Variance (LCMV) beamformer weights.

    Apply Linearly Constrained Minimum Variance (LCMV) beamformer weights
    on evoked data.

    Parameters
    ----------
    evoked : Evoked
        Evoked data to invert.
    filters : instance of Beamformer
        LCMV spatial filter (beamformer weights).
        Filter weights returned from :func:`make_lcmv`.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    stc : SourceEstimate | VolSourceEstimate | VectorSourceEstimate
        Source time courses.

    See Also
    --------
    make_lcmv, apply_lcmv_raw, apply_lcmv_epochs, apply_lcmv_cov

    Notes
    -----
    .. versionadded:: 0.18
    """
    ...

def apply_lcmv_epochs(epochs, filters, *, return_generator: bool = False, verbose=None):
    """Apply Linearly Constrained Minimum Variance (LCMV) beamformer weights.

    Apply Linearly Constrained Minimum Variance (LCMV) beamformer weights
    on single trial data.

    Parameters
    ----------
    epochs : Epochs
        Single trial epochs.
    filters : instance of Beamformer
        LCMV spatial filter (beamformer weights)
        Filter weights returned from :func:`make_lcmv`.
    return_generator : bool
         Return a generator object instead of a list. This allows iterating
         over the stcs without having to keep them all in memory.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    stc: list | generator of (SourceEstimate | VolSourceEstimate)
        The source estimates for all epochs.

    See Also
    --------
    make_lcmv, apply_lcmv_raw, apply_lcmv, apply_lcmv_cov
    """
    ...

def apply_lcmv_raw(raw, filters, start=None, stop=None, *, verbose=None):
    """Apply Linearly Constrained Minimum Variance (LCMV) beamformer weights.

    Apply Linearly Constrained Minimum Variance (LCMV) beamformer weights
    on raw data.

    Parameters
    ----------
    raw : mne.io.Raw
        Raw data to invert.
    filters : instance of Beamformer
        LCMV spatial filter (beamformer weights).
        Filter weights returned from :func:`make_lcmv`.
    start : int
        Index of first time sample (index not time is seconds).
    stop : int
        Index of first time sample not to include (index not time is seconds).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    stc : SourceEstimate | VolSourceEstimate
        Source time courses.

    See Also
    --------
    make_lcmv, apply_lcmv_epochs, apply_lcmv, apply_lcmv_cov
    """
    ...

def apply_lcmv_cov(data_cov, filters, verbose=None):
    """Apply Linearly Constrained  Minimum Variance (LCMV) beamformer weights.

    Apply Linearly Constrained Minimum Variance (LCMV) beamformer weights
    to a data covariance matrix to estimate source power.

    Parameters
    ----------
    data_cov : instance of Covariance
        Data covariance matrix.
    filters : instance of Beamformer
        LCMV spatial filter (beamformer weights).
        Filter weights returned from :func:`make_lcmv`.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    stc : SourceEstimate | VolSourceEstimate
        Source power.

    See Also
    --------
    make_lcmv, apply_lcmv, apply_lcmv_epochs, apply_lcmv_raw
    """
    ...
