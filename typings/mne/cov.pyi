from . import viz as viz
from ._fiff.constants import FIFF as FIFF
from ._fiff.meas_info import create_info as create_info
from ._fiff.pick import (
    pick_channels as pick_channels,
    pick_channels_cov as pick_channels_cov,
    pick_info as pick_info,
    pick_types as pick_types,
)
from ._fiff.tag import find_tag as find_tag
from ._fiff.tree import dir_tree_find as dir_tree_find
from .defaults import DEFAULTS as DEFAULTS
from .epochs import Epochs as Epochs
from .event import make_fixed_length_events as make_fixed_length_events
from .evoked import EvokedArray as EvokedArray
from .fixes import (
    BaseEstimator as BaseEstimator,
    EmpiricalCovariance as EmpiricalCovariance,
    empirical_covariance as empirical_covariance,
    log_likelihood as log_likelihood,
)
from .rank import compute_rank as compute_rank
from .utils import (
    check_fname as check_fname,
    check_version as check_version,
    copy_function_doc_to_method_doc as copy_function_doc_to_method_doc,
    eigh as eigh,
    fill_doc as fill_doc,
    logger as logger,
    warn as warn,
)
from _typeshed import Incomplete

class Covariance(dict):
    """Pick channels from this covariance matrix.

    Parameters
    ----------
    ch_names : list of str
        List of channels to keep. All other channels are dropped.

    ordered : bool
        If True (default False), ensure that the order of the channels in
        the modified instance matches the order of ``ch_names``.

        .. versionadded:: 0.20.0
        .. versionchanged:: 1.5
            The default changed from False in 1.4 to True in 1.5.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    cov : instance of Covariance.
        The modified covariance matrix.

    Notes
    -----
    Operates in-place.

    .. versionadded:: 0.20.0
    """

    def __init__(
        self,
        data,
        names,
        bads,
        projs,
        nfree,
        eig=...,
        eigvec=...,
        method=...,
        loglik=...,
        *,
        verbose=...,
    ) -> None:
        """Init of covariance."""
    @property
    def data(self):
        """Numpy array of Noise covariance matrix."""
    @property
    def ch_names(self):
        """Channel names."""
    @property
    def nfree(self):
        """Number of degrees of freedom."""
    def save(self, fname, *, overwrite: bool = ..., verbose=...) -> None:
        """Save covariance matrix in a FIF file.

        Parameters
        ----------
        fname : path-like
            Output filename.

        overwrite : bool
            If True (default False), overwrite the destination file if it
            exists.

            .. versionadded:: 1.0

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.
        """
    def copy(self):
        """Copy the Covariance object.

        Returns
        -------
        cov : instance of Covariance
            The copied object.
        """
    def as_diag(self):
        """Set covariance to be processed as being diagonal.

        Returns
        -------
        cov : dict
            The covariance.

        Notes
        -----
        This function allows creation of inverse operators
        equivalent to using the old "--diagnoise" mne option.

        This function operates in place.
        """
    def __add__(self, cov):
        """Add Covariance taking into account number of degrees of freedom."""
    def __iadd__(self, cov):
        """Add Covariance taking into account number of degrees of freedom."""
    def plot(
        self,
        info,
        exclude=...,
        colorbar: bool = ...,
        proj: bool = ...,
        show_svd: bool = ...,
        show: bool = ...,
        verbose=...,
    ):
        """Plot Covariance data.

        Parameters
        ----------
        info : mne.Info
            The :class:`mne.Info` object with information about the sensors and methods of measurement.
        exclude : list of str | str
            List of channels to exclude. If empty do not exclude any channel.
            If 'bads', exclude info['bads'].
        colorbar : bool
            Show colorbar or not.
        proj : bool
            Apply projections or not.
        show_svd : bool
            Plot also singular values of the noise covariance for each sensor
            type. We show square roots ie. standard deviations.
        show : bool
            Show figure if True.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        fig_cov : instance of matplotlib.figure.Figure
            The covariance plot.
        fig_svd : instance of matplotlib.figure.Figure | None
            The SVD spectra plot of the covariance.

        See Also
        --------
        mne.compute_rank

        Notes
        -----
        For each channel type, the rank is estimated using
        :func:`mne.compute_rank`.

        .. versionchanged:: 0.19
           Approximate ranks for each channel type are shown with red dashed lines.
        """
    def plot_topomap(
        self,
        info,
        ch_type=...,
        *,
        scalings=...,
        proj: bool = ...,
        noise_cov=...,
        sensors: bool = ...,
        show_names: bool = ...,
        mask=...,
        mask_params=...,
        contours: int = ...,
        outlines: str = ...,
        sphere=...,
        image_interp=...,
        extrapolate=...,
        border=...,
        res: int = ...,
        size: int = ...,
        cmap=...,
        vlim=...,
        cnorm=...,
        colorbar: bool = ...,
        cbar_fmt: str = ...,
        units=...,
        axes=...,
        show: bool = ...,
        verbose=...,
    ):
        """Plot a topomap of the covariance diagonal.

        Parameters
        ----------

        info : mne.Info
            The :class:`mne.Info` object with information about the sensors and methods of measurement.
        ch_type : 'mag' | 'grad' | 'planar1' | 'planar2' | 'eeg' | None
            The channel type to plot. For ``'grad'``, the gradiometers are
            collected in pairs and the RMS for each pair is plotted. If
            ``None`` the first available channel type from order shown above is used. Defaults to ``None``.

            .. versionadded:: 0.21

        scalings : dict | float | None
            The scalings of the channel types to be applied for plotting.
            If None, defaults to ``dict(eeg=1e6, grad=1e13, mag=1e15)``.

        proj : bool | 'interactive' | 'reconstruct'
            If true SSP projections are applied before display. If 'interactive',
            a check box for reversible selection of SSP projection vectors will
            be shown. If 'reconstruct', projection vectors will be applied and then
            M/EEG data will be reconstructed via field mapping to reduce the signal
            bias caused by projection.

            .. versionchanged:: 0.21
               Support for 'reconstruct' was added.
        noise_cov : instance of Covariance | None
            If not None, whiten the instance with ``noise_cov`` before
            plotting.

        sensors : bool | str
            Whether to add markers for sensor locations. If :class:`str`, should be a
            valid matplotlib format string (e.g., ``'r+'`` for red plusses, see the
            Notes section of :meth:matplotlib.axes.Axes.plot`). If ``True`` (the
            default), black circles will be used.

        show_names : bool | callable
            If ``True``, show channel names next to each sensor marker. If callable,
            channel names will be formatted using the callable; e.g., to
            delete the prefix 'MEG ' from all channel names, pass the function
            ``lambda x: x.replace('MEG ', '')``. If ``mask`` is not ``None``, only
            non-masked sensor names will be shown.

        mask : ndarray of bool, shape (n_channels,) | None
            Array indicating channel(s) to highlight with a distinct
            plotting style. Array elements set to ``True`` will be plotted
            with the parameters given in ``mask_params``. Defaults to ``None``,
            equivalent to an array of all ``False`` elements.

        mask_params : dict | None
            Additional plotting parameters for plotting significant sensors.
            Default (None) equals::

                dict(marker='o', markerfacecolor='w', markeredgecolor='k',
                        linewidth=0, markersize=4)

        contours : int | array-like
            The number of contour lines to draw. If ``0``, no contours will be drawn.
            If a positive integer, that number of contour levels are chosen using the
            matplotlib tick locator (may sometimes be inaccurate, use array for
            accuracy). If array-like, the array values are used as the contour levels.
            The values should be in µV for EEG, fT for magnetometers and fT/m for
            gradiometers. If ``colorbar=True``, the colorbar will have ticks
            corresponding to the contour levels. Default is ``6``.

        outlines : 'head' | dict | None
            The outlines to be drawn. If 'head', the default head scheme will be
            drawn. If dict, each key refers to a tuple of x and y positions, the values
            in 'mask_pos' will serve as image mask.
            Alternatively, a matplotlib patch object can be passed for advanced
            masking options, either directly or as a function that returns patches
            (required for multi-axis plots). If None, nothing will be drawn.
            Defaults to 'head'.
        sphere : float | array-like | instance of ConductorModel | None  | 'auto' | 'eeglab'
            The sphere parameters to use for the head outline. Can be array-like of
            shape (4,) to give the X/Y/Z origin and radius in meters, or a single float
            to give just the radius (origin assumed 0, 0, 0). Can also be an instance
            of a spherical :class:mne.bem.ConductorModel` to use the origin and
            radius from that object. If ``'auto'`` the sphere is fit to digitization
            points. If ``'eeglab'`` the head circle is defined by EEG electrodes
            ``'Fpz'``, ``'Oz'``, ``'T7'``, and ``'T8'`` (if ``'Fpz'`` is not present,
            it will be approximated from the coordinates of ``'Oz'``). ``None`` (the
            default) is equivalent to ``'auto'`` when enough extra digitization points
            are available, and (0, 0, 0, 0.095) otherwise.

            .. versionadded:: 0.20
            .. versionchanged:: 1.1 Added ``'eeglab'`` option.

        image_interp : str
            The image interpolation to be used. Options are ``'cubic'`` (default)
            to use :class:`scipy.interpolate.CloughTocher2DInterpolator`,
            ``'nearest'`` to use :class:`scipy.spatial.Voronoi` or
            ``'linear'`` to use :class:`scipy.interpolate.LinearNDInterpolator`.

        extrapolate : str
            Options:

            - ``'box'``
                Extrapolate to four points placed to form a square encompassing all
                data points, where each side of the square is three times the range
                of the data in the respective dimension.
            - ``'local'`` (default for MEG sensors)
                Extrapolate only to nearby points (approximately to points closer than
                median inter-electrode distance). This will also set the
                mask to be polygonal based on the convex hull of the sensors.
            - ``'head'`` (default for non-MEG sensors)
                Extrapolate out to the edges of the clipping circle. This will be on
                the head circle when the sensors are contained within the head circle,
                but it can extend beyond the head when sensors are plotted outside
                the head circle.

            .. versionchanged:: 0.21

               - The default was changed to ``'local'`` for MEG sensors.
               - ``'local'`` was changed to use a convex hull mask
               - ``'head'`` was changed to extrapolate out to the clipping circle.

        border : float | 'mean'
            Value to extrapolate to on the topomap borders. If ``'mean'`` (default),
            then each extrapolated point has the average value of its neighbours.

            .. versionadded:: 0.20

        res : int
            The resolution of the topomap image (number of pixels along each side).

        size : float
            Side length of each subplot in inches.

        cmap : matplotlib colormap | (colormap, bool) | 'interactive' | None
            Colormap to use. If :class:`tuple`, the first value indicates the colormap
            to use and the second value is a boolean defining interactivity. In
            interactive mode the colors are adjustable by clicking and dragging the
            colorbar with left and right mouse button. Left mouse button moves the
            scale up and down and right mouse button adjusts the range. Hitting
            space bar resets the range. Up and down arrows can be used to change
            the colormap. If ``None``, ``'Reds'`` is used for data that is either
            all-positive or all-negative, and ``'RdBu_r'`` is used otherwise.
            ``'interactive'`` is equivalent to ``(None, True)``. Defaults to ``None``.

            .. warning::  Interactive mode works smoothly only for a small amount
                of topomaps. Interactive mode is disabled by default for more than
                2 topomaps.

        vlim : tuple of length 2
            Colormap limits to use. If a :class:`tuple` of floats, specifies the
            lower and upper bounds of the colormap (in that order); providing
            ``None`` for either entry will set the corresponding boundary at the
            min/max of the data. Defaults to ``(None, None)``.

            .. versionadded:: 1.2

        cnorm : matplotlib.colors.Normalize | None
            How to normalize the colormap. If ``None``, standard linear normalization
            is performed. If not ``None``, ``vmin`` and ``vmax`` will be ignored.
            See :ref:`Matplotlib docs <matplotlib:colormapnorms>`
            for more details on colormap normalization, and
            :ref:`the ERDs example<cnorm-example>` for an example of its use.

            .. versionadded:: 1.2

        colorbar : bool
            Plot a colorbar in the rightmost column of the figure.
        cbar_fmt : str
            Formatting string for colorbar tick labels. See :ref:`formatspec` for
            details.

        units : dict | str | None
            The units to use for the colorbar label. Ignored if ``colorbar=False``.
            If ``None`` and ``scalings=None`` the unit is automatically determined, otherwise the label will be "AU" indicating arbitrary units.
            Default is ``None``.
        axes : instance of Axes | list of Axes | None
            The axes to plot to. If ``None``, a new :class:matplotlib.figure.Figure`
            will be created with the correct number of axes. If :class:matplotlib.axes.Axes` are provided (either as a single instance or a :class:`list` of axes), the number of axes provided must be length 1.Default is ``None``.
        show : bool
            Show the figure if ``True``.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        fig : instance of Figure
            The matplotlib figure.

        Notes
        -----
        .. versionadded:: 0.21
        """
    def pick_channels(self, ch_names, ordered=..., *, verbose=...):
        """Pick channels from this covariance matrix.

        Parameters
        ----------
        ch_names : list of str
            List of channels to keep. All other channels are dropped.

        ordered : bool
            If True (default False), ensure that the order of the channels in
            the modified instance matches the order of ``ch_names``.

            .. versionadded:: 0.20.0
            .. versionchanged:: 1.5
                The default changed from False in 1.4 to True in 1.5.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        cov : instance of Covariance.
            The modified covariance matrix.

        Notes
        -----
        Operates in-place.

        .. versionadded:: 0.20.0
        """

def read_cov(fname, verbose=...):
    """Read a noise covariance from a FIF file.

    Parameters
    ----------
    fname : path-like
        The path-like of file containing the covariance matrix. It should end
        with ``-cov.fif`` or ``-cov.fif.gz``.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    cov : Covariance
        The noise covariance matrix.

    See Also
    --------
    write_cov, compute_covariance, compute_raw_covariance
    """

def make_ad_hoc_cov(info, std=..., *, verbose=...):
    """Create an ad hoc noise covariance.

    Parameters
    ----------

    info : mne.Info
        The :class:`mne.Info` object with information about the sensors and methods of measurement.
    std : dict of float | None
        Standard_deviation of the diagonal elements. If dict, keys should be
        ``'grad'`` for gradiometers, ``'mag'`` for magnetometers and ``'eeg'``
        for EEG channels. If None, default values will be used (see Notes).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    cov : instance of Covariance
        The ad hoc diagonal noise covariance for the M/EEG data channels.

    Notes
    -----
    The default noise values are 5 fT/cm, 20 fT, and 0.2 µV for gradiometers,
    magnetometers, and EEG channels respectively.

    .. versionadded:: 0.9.0
    """

def compute_raw_covariance(
    raw,
    tmin: int = ...,
    tmax=...,
    tstep: float = ...,
    reject=...,
    flat=...,
    picks=...,
    method: str = ...,
    method_params=...,
    cv: int = ...,
    scalings=...,
    n_jobs=...,
    return_estimators: bool = ...,
    reject_by_annotation: bool = ...,
    rank=...,
    verbose=...,
):
    """Estimate noise covariance matrix from a continuous segment of raw data.

    It is typically useful to estimate a noise covariance from empty room
    data or time intervals before starting the stimulation.

    .. note:: To estimate the noise covariance from epoched data, use
              :func:`mne.compute_covariance` instead.

    Parameters
    ----------
    raw : instance of Raw
        Raw data.
    tmin : float
        Beginning of time interval in seconds. Defaults to 0.
    tmax : float | None (default None)
        End of time interval in seconds. If None (default), use the end of the
        recording.
    tstep : float (default 0.2)
        Length of data chunks for artifact rejection in seconds.
        Can also be None to use a single epoch of (tmax - tmin)
        duration. This can use a lot of memory for large ``Raw``
        instances.
    reject : dict | None (default None)
        Rejection parameters based on peak-to-peak amplitude.
        Valid keys are 'grad' | 'mag' | 'eeg' | 'eog' | 'ecg'.
        If reject is None then no rejection is done. Example::

            reject = dict(grad=4000e-13, # T / m (gradiometers)
                          mag=4e-12, # T (magnetometers)
                          eeg=40e-6, # V (EEG channels)
                          eog=250e-6 # V (EOG channels)
                          )

    flat : dict | None (default None)
        Rejection parameters based on flatness of signal.
        Valid keys are 'grad' | 'mag' | 'eeg' | 'eog' | 'ecg', and values
        are floats that set the minimum acceptable peak-to-peak amplitude.
        If flat is None then no rejection is done.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick good data channels (excluding reference
        MEG channels). Note that channels in ``info['bads']`` *will be included* if
        their names or indices are explicitly provided.
    method : str | list | None (default 'empirical')
        The method used for covariance estimation.
        See :func:`mne.compute_covariance`.

        .. versionadded:: 0.12
    method_params : dict | None (default None)
        Additional parameters to the estimation procedure.
        See :func:`mne.compute_covariance`.

        .. versionadded:: 0.12
    cv : int | sklearn.model_selection object (default 3)
        The cross validation method. Defaults to 3, which will
        internally trigger by default :class:`sklearn.model_selection.KFold`
        with 3 splits.

        .. versionadded:: 0.12
    scalings : dict | None (default None)
        Defaults to ``dict(mag=1e15, grad=1e13, eeg=1e6)``.
        These defaults will scale magnetometers and gradiometers
        at the same unit.

        .. versionadded:: 0.12
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the :mod:`joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a :class:`joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.

        .. versionadded:: 0.12
    return_estimators : bool (default False)
        Whether to return all estimators or the best. Only considered if
        method equals 'auto' or is a list of str. Defaults to False.

        .. versionadded:: 0.12

    reject_by_annotation : bool
        Whether to reject based on annotations. If ``True`` (default), epochs
        overlapping with segments whose description begins with ``'bad'`` are
        rejected. If ``False``, no rejection based on annotations is performed.

        .. versionadded:: 0.14

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

        The default is ``None``.

        .. versionadded:: 0.17

        .. versionadded:: 0.18
           Support for 'info' mode.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    cov : instance of Covariance | list
        The computed covariance. If method equals 'auto' or is a list of str
        and return_estimators equals True, a list of covariance estimators is
        returned (sorted by log-likelihood, from high to low, i.e. from best
        to worst).

    See Also
    --------
    compute_covariance : Estimate noise covariance matrix from epoched data.

    Notes
    -----
    This function will:

    1. Partition the data into evenly spaced, equal-length epochs.
    2. Load them into memory.
    3. Subtract the mean across all time points and epochs for each channel.
    4. Process the :class:`Epochs` by :func:`compute_covariance`.

    This will produce a slightly different result compared to using
    :func:`make_fixed_length_events`, :class:`Epochs`, and
    :func:`compute_covariance` directly, since that would (with the recommended
    baseline correction) subtract the mean across time *for each epoch*
    (instead of across epochs) for each channel.
    """

def compute_covariance(
    epochs,
    keep_sample_mean: bool = ...,
    tmin=...,
    tmax=...,
    projs=...,
    method: str = ...,
    method_params=...,
    cv: int = ...,
    scalings=...,
    n_jobs=...,
    return_estimators: bool = ...,
    on_mismatch: str = ...,
    rank=...,
    verbose=...,
):
    """Estimate noise covariance matrix from epochs.

    The noise covariance is typically estimated on pre-stimulus periods
    when the stimulus onset is defined from events.

    If the covariance is computed for multiple event types (events
    with different IDs), the following two options can be used and combined:

        1. either an Epochs object for each event type is created and
           a list of Epochs is passed to this function.
        2. an Epochs object is created for multiple events and passed
           to this function.

    .. note:: To estimate the noise covariance from non-epoched raw data, such
              as an empty-room recording, use
              :func:`mne.compute_raw_covariance` instead.

    Parameters
    ----------
    epochs : instance of Epochs, or list of Epochs
        The epochs.
    keep_sample_mean : bool (default True)
        If False, the average response over epochs is computed for
        each event type and subtracted during the covariance
        computation. This is useful if the evoked response from a
        previous stimulus extends into the baseline period of the next.
        Note. This option is only implemented for method='empirical'.
    tmin : float | None (default None)
        Start time for baseline. If None start at first sample.
    tmax : float | None (default None)
        End time for baseline. If None end at last sample.
    projs : list of Projection | None (default None)
        List of projectors to use in covariance calculation, or None
        to indicate that the projectors from the epochs should be
        inherited. If None, then projectors from all epochs must match.
    method : str | list | None (default 'empirical')
        The method used for covariance estimation. If 'empirical' (default),
        the sample covariance will be computed. A list can be passed to
        perform estimates using multiple methods.
        If 'auto' or a list of methods, the best estimator will be determined
        based on log-likelihood and cross-validation on unseen data as
        described in :footcite:`EngemannGramfort2015`. Valid methods are
        'empirical', 'diagonal_fixed', 'shrunk', 'oas', 'ledoit_wolf',
        'factor_analysis', 'shrinkage', and 'pca' (see Notes). If ``'auto'``,
        it expands to::

             ['shrunk', 'diagonal_fixed', 'empirical', 'factor_analysis']

        ``'factor_analysis'`` is removed when ``rank`` is not 'full'.
        The ``'auto'`` mode is not recommended if there are many
        segments of data, since computation can take a long time.

        .. versionadded:: 0.9.0
    method_params : dict | None (default None)
        Additional parameters to the estimation procedure. Only considered if
        method is not None. Keys must correspond to the value(s) of ``method``.
        If None (default), expands to the following (with the addition of
        ``{'store_precision': False, 'assume_centered': True} for all methods
        except ``'factor_analysis'`` and ``'pca'``)::

            {'diagonal_fixed': {'grad': 0.1, 'mag': 0.1, 'eeg': 0.1, ...},
             'shrinkage': {'shrikage': 0.1},
             'shrunk': {'shrinkage': np.logspace(-4, 0, 30)},
             'pca': {'iter_n_components': None},
             'factor_analysis': {'iter_n_components': None}}

    cv : int | sklearn.model_selection object (default 3)
        The cross validation method. Defaults to 3, which will
        internally trigger by default :class:`sklearn.model_selection.KFold`
        with 3 splits.
    scalings : dict | None (default None)
        Defaults to ``dict(mag=1e15, grad=1e13, eeg=1e6)``.
        These defaults will scale data to roughly the same order of
        magnitude.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the :mod:`joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a :class:`joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.
    return_estimators : bool (default False)
        Whether to return all estimators or the best. Only considered if
        method equals 'auto' or is a list of str. Defaults to False.
    on_mismatch : str
        What to do when the MEG<->Head transformations do not match between
        epochs. If "raise" (default) an error is raised, if "warn" then a
        warning is emitted, if "ignore" then nothing is printed. Having
        mismatched transforms can in some cases lead to unexpected or
        unstable results in covariance calculation, e.g. when data
        have been processed with Maxwell filtering but not transformed
        to the same head position.

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

        The default is ``None``.

        .. versionadded:: 0.17

        .. versionadded:: 0.18
           Support for 'info' mode.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    cov : instance of Covariance | list
        The computed covariance. If method equals ``'auto'`` or is a list of str
        and ``return_estimators=True``, a list of covariance estimators is
        returned (sorted by log-likelihood, from high to low, i.e. from best
        to worst).

    See Also
    --------
    compute_raw_covariance : Estimate noise covariance from raw data, such as
        empty-room recordings.

    Notes
    -----
    Baseline correction or sufficient high-passing should be used
    when creating the :class:`Epochs` to ensure that the data are zero mean,
    otherwise the computed covariance matrix will be inaccurate.

    Valid ``method`` strings are:

    * ``'empirical'``
        The empirical or sample covariance (default)
    * ``'diagonal_fixed'``
        A diagonal regularization based on channel types as in
        :func:`mne.cov.regularize`.
    * ``'shrinkage'``
        Fixed shrinkage.

      .. versionadded:: 0.16
    * ``'ledoit_wolf'``
        The Ledoit-Wolf estimator, which uses an
        empirical formula for the optimal shrinkage value :footcite:`LedoitWolf2004`.
    * ``'oas'``
        The OAS estimator :footcite:`ChenEtAl2010`, which uses a different
        empricial formula for the optimal shrinkage value.

      .. versionadded:: 0.16
    * ``'shrunk'``
        Like 'ledoit_wolf', but with cross-validation for optimal alpha.
    * ``'pca'``
        Probabilistic PCA with low rank :footcite:`TippingBishop1999`.
    * ``'factor_analysis'``
        Factor analysis with low rank :footcite:`Barber2012`.

    ``'ledoit_wolf'`` and ``'pca'`` are similar to ``'shrunk'`` and
    ``'factor_analysis'``, respectively, except that they use
    cross validation (which is useful when samples are correlated, which
    is often the case for M/EEG data). The former two are not included in
    the ``'auto'`` mode to avoid redundancy.

    For multiple event types, it is also possible to create a
    single :class:`Epochs` object with events obtained using
    :func:`mne.merge_events`. However, the resulting covariance matrix
    will only be correct if ``keep_sample_mean is True``.

    The covariance can be unstable if the number of samples is small.
    In that case it is common to regularize the covariance estimate.
    The ``method`` parameter allows to regularize the covariance in an
    automated way. It also allows to select between different alternative
    estimation algorithms which themselves achieve regularization.
    Details are described in :footcite:t:`EngemannGramfort2015`.

    For more information on the advanced estimation methods, see
    :ref:`the sklearn manual <sklearn:covariance>`.

    References
    ----------
    .. footbibliography::
    """

class _RegCovariance(BaseEstimator):
    """Delegate call to modified EmpiricalCovariance instance."""

    info: Incomplete
    grad: Incomplete
    mag: Incomplete
    eeg: Incomplete
    seeg: Incomplete
    dbs: Incomplete
    ecog: Incomplete
    hbo: Incomplete
    hbr: Incomplete
    fnirs_cw_amplitude: Incomplete
    fnirs_fd_ac_amplitude: Incomplete
    fnirs_fd_phase: Incomplete
    fnirs_od: Incomplete
    csd: Incomplete
    store_precision: Incomplete
    assume_centered: Incomplete

    def __init__(
        self,
        info,
        grad: float = ...,
        mag: float = ...,
        eeg: float = ...,
        seeg: float = ...,
        ecog: float = ...,
        hbo: float = ...,
        hbr: float = ...,
        fnirs_cw_amplitude: float = ...,
        fnirs_fd_ac_amplitude: float = ...,
        fnirs_fd_phase: float = ...,
        fnirs_od: float = ...,
        csd: float = ...,
        dbs: float = ...,
        store_precision: bool = ...,
        assume_centered: bool = ...,
    ) -> None: ...
    estimator_: Incomplete
    covariance_: Incomplete

    def fit(self, X):
        """Fit covariance model with classical diagonal regularization."""
    def score(self, X_test, y=...):
        """Delegate call to modified EmpiricalCovariance instance."""
    def get_precision(self):
        """Delegate call to modified EmpiricalCovariance instance."""

class _ShrunkCovariance(BaseEstimator):
    """Delegate to modified EmpiricalCovariance instance."""

    store_precision: Incomplete
    assume_centered: Incomplete
    shrinkage: Incomplete

    def __init__(
        self, store_precision, assume_centered, shrinkage: float = ...
    ) -> None: ...
    estimator_: Incomplete
    zero_cross_cov_: Incomplete

    def fit(self, X):
        """Fit covariance model with oracle shrinkage regularization."""
    def score(self, X_test, y=...):
        """Delegate to modified EmpiricalCovariance instance."""
    def get_precision(self):
        """Delegate to modified EmpiricalCovariance instance."""

def write_cov(fname, cov, *, overwrite: bool = ..., verbose=...) -> None:
    """Write a noise covariance matrix.

    Parameters
    ----------
    fname : path-like
        The name of the file. It should end with ``-cov.fif`` or
        ``-cov.fif.gz``.
    cov : Covariance
        The noise covariance matrix.

    overwrite : bool
        If True (default False), overwrite the destination file if it
        exists.

        .. versionadded:: 1.0

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    read_cov
    """

def prepare_noise_cov(
    noise_cov,
    info,
    ch_names=...,
    rank=...,
    scalings=...,
    on_rank_mismatch: str = ...,
    verbose=...,
):
    """Prepare noise covariance matrix.

    Parameters
    ----------
    noise_cov : instance of Covariance
        The noise covariance to process.

    info : mne.Info
        The :class:`mne.Info` object with information about the sensors and methods of measurement. (Used to get channel types and bad channels).
    ch_names : list | None
        The channel names to be considered. Can be None to use
        ``info['ch_names']``.

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

        The default is ``None``.

        .. versionadded:: 0.18
           Support for 'info' mode.
    scalings : dict | None
        Data will be rescaled before rank estimation to improve accuracy.
        If dict, it will override the following dict (default if None)::

            dict(mag=1e12, grad=1e11, eeg=1e5)

    on_rank_mismatch : str
        If an explicit MEG value is passed, what to do when it does not match
        an empirically computed rank (only used for covariances).
        Can be 'raise' to raise an error, 'warn' (default) to emit a warning, or
        'ignore' to ignore.

        .. versionadded:: 0.23

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    cov : instance of Covariance
        A copy of the covariance with the good channels subselected
        and parameters updated.
    """

def regularize(
    cov,
    info,
    mag: float = ...,
    grad: float = ...,
    eeg: float = ...,
    exclude: str = ...,
    proj: bool = ...,
    seeg: float = ...,
    ecog: float = ...,
    hbo: float = ...,
    hbr: float = ...,
    fnirs_cw_amplitude: float = ...,
    fnirs_fd_ac_amplitude: float = ...,
    fnirs_fd_phase: float = ...,
    fnirs_od: float = ...,
    csd: float = ...,
    dbs: float = ...,
    rank=...,
    scalings=...,
    verbose=...,
):
    """Regularize noise covariance matrix.

    This method works by adding a constant to the diagonal for each
    channel type separately. Special care is taken to keep the
    rank of the data constant.

    .. note:: This function is kept for reasons of backward-compatibility.
              Please consider explicitly using the ``method`` parameter in
              :func:`mne.compute_covariance` to directly combine estimation
              with regularization in a data-driven fashion. See the
              :ref:`FAQ <faq_how_should_i_regularize>` for more information.

    Parameters
    ----------
    cov : Covariance
        The noise covariance matrix.

    info : mne.Info
        The :class:`mne.Info` object with information about the sensors and methods of measurement. (Used to get channel types and bad channels).
    mag : float (default 0.1)
        Regularization factor for MEG magnetometers.
    grad : float (default 0.1)
        Regularization factor for MEG gradiometers. Must be the same as
        ``mag`` if data have been processed with SSS.
    eeg : float (default 0.1)
        Regularization factor for EEG.
    exclude : list | 'bads' (default 'bads')
        List of channels to mark as bad. If 'bads', bads channels
        are extracted from both info['bads'] and cov['bads'].
    proj : bool (default True)
        Apply projections to keep rank of data.
    seeg : float (default 0.1)
        Regularization factor for sEEG signals.
    ecog : float (default 0.1)
        Regularization factor for ECoG signals.
    hbo : float (default 0.1)
        Regularization factor for HBO signals.
    hbr : float (default 0.1)
        Regularization factor for HBR signals.
    fnirs_cw_amplitude : float (default 0.1)
        Regularization factor for fNIRS CW raw signals.
    fnirs_fd_ac_amplitude : float (default 0.1)
        Regularization factor for fNIRS FD AC raw signals.
    fnirs_fd_phase : float (default 0.1)
        Regularization factor for fNIRS raw phase signals.
    fnirs_od : float (default 0.1)
        Regularization factor for fNIRS optical density signals.
    csd : float (default 0.1)
        Regularization factor for EEG-CSD signals.
    dbs : float (default 0.1)
        Regularization factor for DBS signals.

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

        The default is ``None``.

        .. versionadded:: 0.17

        .. versionadded:: 0.18
           Support for 'info' mode.
    scalings : dict | None
        Data will be rescaled before rank estimation to improve accuracy.
        See :func:`mne.compute_covariance`.

        .. versionadded:: 0.17

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    reg_cov : Covariance
        The regularized covariance matrix.

    See Also
    --------
    mne.compute_covariance
    """

def compute_whitener(
    noise_cov,
    info=...,
    picks=...,
    rank=...,
    scalings=...,
    return_rank: bool = ...,
    pca: bool = ...,
    return_colorer: bool = ...,
    on_rank_mismatch: str = ...,
    verbose=...,
):
    """Compute whitening matrix.

    Parameters
    ----------
    noise_cov : Covariance
        The noise covariance.

    info : mne.Info | None
        The :class:`mne.Info` object with information about the sensors and methods of measurement. Can be None if ``noise_cov`` has already been
        prepared with :func:`prepare_noise_cov`.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick good data channels (excluding reference
        MEG channels). Note that channels in ``info['bads']`` *will be included* if
        their names or indices are explicitly provided.

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

        The default is ``None``.

        .. versionadded:: 0.18
           Support for 'info' mode.
    scalings : dict | None
        The rescaling method to be applied. See documentation of
        ``prepare_noise_cov`` for details.
    return_rank : bool
        If True, return the rank used to compute the whitener.

        .. versionadded:: 0.15
    pca : bool | str
        Space to project the data into. Options:

        :data:`python:True`
            Whitener will be shape (n_nonzero, n_channels).
        ``'white'``
            Whitener will be shape (n_channels, n_channels), potentially rank
            deficient, and have the first ``n_channels - n_nonzero`` rows and
            columns set to zero.
        :data:`python:False` (default)
            Whitener will be shape (n_channels, n_channels), potentially rank
            deficient, and rotated back to the space of the original data.

        .. versionadded:: 0.18
    return_colorer : bool
        If True, return the colorer as well.

    on_rank_mismatch : str
        If an explicit MEG value is passed, what to do when it does not match
        an empirically computed rank (only used for covariances).
        Can be 'raise' to raise an error, 'warn' (default) to emit a warning, or
        'ignore' to ignore.

        .. versionadded:: 0.23

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    W : ndarray, shape (n_channels, n_channels) or (n_nonzero, n_channels)
        The whitening matrix.
    ch_names : list
        The channel names.
    rank : int
        Rank reduction of the whitener. Returned only if return_rank is True.
    colorer : ndarray, shape (n_channels, n_channels) or (n_channels, n_nonzero)
        The coloring matrix.
    """

def whiten_evoked(
    evoked, noise_cov, picks=..., diag=..., rank=..., scalings=..., verbose=...
):
    """Whiten evoked data using given noise covariance.

    Parameters
    ----------
    evoked : instance of Evoked
        The evoked data.
    noise_cov : instance of Covariance
        The noise covariance.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick good data channels. Note that channels
        in ``info['bads']`` *will be included* if their names or indices are
        explicitly provided.
    diag : bool (default False)
        If True, whiten using only the diagonal of the covariance.

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

        The default is ``None``.

        .. versionadded:: 0.18
           Support for 'info' mode.
    scalings : dict | None (default None)
        To achieve reliable rank estimation on multiple sensors,
        sensors have to be rescaled. This parameter controls the
        rescaling. If dict, it will override the
        following default dict (default if None):

            dict(mag=1e12, grad=1e11, eeg=1e5)

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    evoked_white : instance of Evoked
        The whitened evoked data.
    """
