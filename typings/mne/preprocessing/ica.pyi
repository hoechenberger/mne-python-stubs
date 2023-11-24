from .._fiff.meas_info import ContainsMixin
from _typeshed import Incomplete
from typing import NamedTuple

def get_score_funcs():
    """Get the score functions.

    Returns
    -------
    score_funcs : dict
        The score functions.
    """

class ICA(ContainsMixin):
    """Overlay of raw and cleaned signals given the unmixing matrix.

    This method helps visualizing signal quality and artifact rejection.

    Parameters
    ----------
    inst : instance of Raw or Evoked
        The signal to plot. If `~mne.io.Raw`, the raw data per channel type is displayed
        before and after cleaning. A second panel with the RMS for MEG sensors and the
        :term:`GFP` for EEG sensors is displayed. If `~mne.Evoked`, butterfly traces for
        signals before and after cleaning will be superimposed.
    exclude : array-like of int | None (default)
        The components marked for exclusion. If ``None`` (default), the components
        listed in ``ICA.exclude`` will be used.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as 
        channel indices. In lists, channel *type* strings (e.g., ``['meg', 
        'eeg']``) will pick channels of those types, channel *name* strings (e.g., 
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the 
        string values "all" to pick all channels, or "data" to pick :term:`data 
        channels`. None (default) will pick all channels that were included during fitting.
    start, stop : float | None
       The first and last time point (in seconds) of the data to plot. If
       ``inst`` is a `~mne.io.Raw` object, ``start=None`` and ``stop=None``
       will be translated into ``start=0.`` and ``stop=3.``, respectively. For
       `~mne.Evoked`, ``None`` refers to the beginning and end of the evoked
       signal.
    
    title : str | None
        The title of the generated figure. If ``None`` (default), no title is
        displayed.
    show : bool
        Show the figure if ``True``.
    
    n_pca_components : int | float | None
        The number of PCA components to be kept, either absolute (int)
        or fraction of the explained variance (float). If None (default),
        the ``ica.n_pca_components`` from initialization will be used in 0.22;
        in 0.23 all components will be used.

        .. versionadded:: 0.22
    
    on_baseline : str
        How to handle baseline-corrected epochs or evoked data.
        Can be ``'raise'`` to raise an error, ``'warn'`` (default) to emit a
        warning, ``'ignore'`` to ignore, or "reapply" to reapply the baseline
        after applying ICA.
    
        .. versionadded:: 1.2
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    fig : instance of Figure
        The figure.
    """
    noise_cov: Incomplete
    current_fit: str
    n_components: Incomplete
    n_pca_components: Incomplete
    ch_names: Incomplete
    random_state: Incomplete
    max_iter: Incomplete
    fit_params: Incomplete
    exclude: Incomplete
    info: Incomplete
    method: Incomplete
    labels_: Incomplete
    allow_ref_meg: Incomplete

    def __init__(self, n_components: Incomplete | None=..., *, noise_cov: Incomplete | None=..., random_state: Incomplete | None=..., method: str=..., fit_params: Incomplete | None=..., max_iter: str=..., allow_ref_meg: bool=..., verbose: Incomplete | None=...) -> None:
        ...

    def fit(self, inst, picks: Incomplete | None=..., start: Incomplete | None=..., stop: Incomplete | None=..., decim: Incomplete | None=..., reject: Incomplete | None=..., flat: Incomplete | None=..., tstep: float=..., reject_by_annotation: bool=..., verbose: Incomplete | None=...):
        """Run the ICA decomposition on raw data.

        Caveat! If supplying a noise covariance keep track of the projections
        available in the cov, the raw or the epochs object. For example,
        if you are interested in EOG or ECG artifacts, EOG and ECG projections
        should be temporally removed before fitting the ICA.

        Parameters
        ----------
        inst : instance of Raw or Epochs
            The data to be decomposed.
        picks : str | array-like | slice | None
            Channels to include. Slices and lists of integers will be interpreted as 
            channel indices. In lists, channel *type* strings (e.g., ``['meg', 
            'eeg']``) will pick channels of those types, channel *name* strings (e.g., 
            ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the 
            string values "all" to pick all channels, or "data" to pick :term:`data 
            channels`. None (default) will pick good data channels (excluding reference 
            MEG channels). Note that channels in ``info['bads']`` *will be included* if 
            their names or indices are explicitly provided.
            This selection remains throughout the initialized ICA solution.
        start, stop : int | float | None
            First and last sample to include. If float, data will be
            interpreted as time in seconds. If ``None``, data will be used from
            the first sample and to the last sample, respectively.

            .. note:: These parameters only have an effect if ``inst`` is
                      `~mne.io.Raw` data.
        decim : int | None
            Increment for selecting only each n-th sampling point. If ``None``,
            all samples  between ``start`` and ``stop`` (inclusive) are used.
        reject, flat : dict | None
            Rejection parameters based on peak-to-peak amplitude (PTP)
            in the continuous data. Signal periods exceeding the thresholds
            in ``reject`` or less than the thresholds in ``flat`` will be
            removed before fitting the ICA.

            .. note:: These parameters only have an effect if ``inst`` is
                      `~mne.io.Raw` data. For `~mne.Epochs`, perform PTP
                      rejection via :meth:`~mne.Epochs.drop_bad`.

            Valid keys are all channel types present in the data. Values must
            be integers or floats.

            If ``None``, no PTP-based rejection will be performed. Example::

                reject = dict(
                    grad=4000e-13, # T / m (gradiometers)
                    mag=4e-12, # T (magnetometers)
                    eeg=40e-6, # V (EEG channels)
                    eog=250e-6 # V (EOG channels)
                )
                flat = None  # no rejection based on flatness
        tstep : float
            Length of data chunks for artifact rejection in seconds.

            .. note:: This parameter only has an effect if ``inst`` is
                      `~mne.io.Raw` data.
        
        reject_by_annotation : bool
            Whether to omit bad segments from the data before fitting. If ``True``
            (default), annotated segments whose description begins with ``'bad'`` are
            omitted. If ``False``, no rejection based on annotations is performed.
        
            Has no effect if ``inst`` is not a :class:`mne.io.Raw` object.

            .. versionadded:: 0.14.0
        
        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        self : instance of ICA
            Returns the modified instance.
        """

    def get_components(self):
        """Get ICA topomap for components as numpy arrays.

        Returns
        -------
        components : array, shape (n_channels, n_components)
            The ICA components (maps).
        """

    def get_explained_variance_ratio(self, inst, *, components: Incomplete | None=..., ch_type: Incomplete | None=...):
        """Get the proportion of data variance explained by ICA components.

        Parameters
        ----------
        inst : mne.io.BaseRaw | mne.BaseEpochs | mne.Evoked
            The uncleaned data.
        components : array-like of int | int | None
            The component(s) for which to do the calculation. If more than one
            component is specified, explained variance will be calculated
            jointly across all supplied components. If ``None`` (default), uses
            all available components.
        ch_type : 'mag' | 'grad' | 'planar1' | 'planar2' | 'eeg' | array-like of str | None
            The channel type(s) to include in the calculation. If ``None``, all
            available channel types will be used.

        Returns
        -------
        dict (str, float)
            The fraction of variance in ``inst`` that can be explained by the
            ICA components, calculated separately for each channel type.
            Dictionary keys are the channel types, and corresponding explained
            variance ratios are the values.

        Notes
        -----
        A value similar to EEGLAB's ``pvaf`` (percent variance accounted for)
        will be calculated for the specified component(s).

        Since ICA components cannot be assumed to be aligned orthogonally, the
        sum of the proportion of variance explained by all components may not
        be equal to 1. In certain situations, the proportion of variance
        explained by a component may even be negative.

        .. versionadded:: 1.2
        """

    def get_sources(self, inst, add_channels: Incomplete | None=..., start: Incomplete | None=..., stop: Incomplete | None=...):
        """Estimate sources given the unmixing matrix.

        This method will return the sources in the container format passed.
        Typical usecases:

        1. pass Raw object to use `raw.plot <mne.io.Raw.plot>` for ICA sources
        2. pass Epochs object to compute trial-based statistics in ICA space
        3. pass Evoked object to investigate time-locking in ICA space

        Parameters
        ----------
        inst : instance of Raw, Epochs or Evoked
            Object to compute sources from and to represent sources in.
        add_channels : None | list of str
            Additional channels  to be added. Useful to e.g. compare sources
            with some reference. Defaults to None.
        start : int | float | None
            First sample to include. If float, data will be interpreted as
            time in seconds. If None, the entire data will be used.
        stop : int | float | None
            Last sample to not include. If float, data will be interpreted as
            time in seconds. If None, the entire data will be used.

        Returns
        -------
        sources : instance of Raw, Epochs or Evoked
            The ICA sources time series.
        """

    def score_sources(self, inst, target: Incomplete | None=..., score_func: str=..., start: Incomplete | None=..., stop: Incomplete | None=..., l_freq: Incomplete | None=..., h_freq: Incomplete | None=..., reject_by_annotation: bool=..., verbose: Incomplete | None=...):
        """Assign score to components based on statistic or metric.

        Parameters
        ----------
        inst : instance of Raw, Epochs or Evoked
            The object to reconstruct the sources from.
        target : array-like | str | None
            Signal to which the sources shall be compared. It has to be of
            the same shape as the sources. If str, a routine will try to find
            a matching channel name. If None, a score
            function expecting only one input-array argument must be used,
            for instance, scipy.stats.skew (default).
        score_func : callable | str
            Callable taking as arguments either two input arrays
            (e.g. Pearson correlation) or one input
            array (e. g. skewness) and returns a float. For convenience the
            most common score_funcs are available via string labels:
            Currently, all distance metrics from scipy.spatial and All
            functions from scipy.stats taking compatible input arguments are
            supported. These function have been modified to support iteration
            over the rows of a 2D array.
        start : int | float | None
            First sample to include. If float, data will be interpreted as
            time in seconds. If None, data will be used from the first sample.
        stop : int | float | None
            Last sample to not include. If float, data will be interpreted as
            time in seconds. If None, data will be used to the last sample.
        l_freq : float
            Low pass frequency.
        h_freq : float
            High pass frequency.
        
        reject_by_annotation : bool
            Whether to omit bad segments from the data before fitting. If ``True``
            (default), annotated segments whose description begins with ``'bad'`` are
            omitted. If ``False``, no rejection based on annotations is performed.

            .. versionadded:: 0.14.0
        
        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        scores : ndarray
            Scores for each source as returned from score_func.
        """

    def find_bads_ecg(self, inst, ch_name: Incomplete | None=..., threshold: str=..., start: Incomplete | None=..., stop: Incomplete | None=..., l_freq: int=..., h_freq: int=..., method: str=..., reject_by_annotation: bool=..., measure: str=..., verbose: Incomplete | None=...):
        """Detect ECG related components.

        Cross-trial phase statistics :footcite:`DammersEtAl2008` or Pearson
        correlation can be used for detection.

        .. note:: If no ECG channel is available, routine attempts to create
                  an artificial ECG based on cross-channel averaging.

        Parameters
        ----------
        inst : instance of Raw, Epochs or Evoked
            Object to compute sources from.
        ch_name : str
            The name of the channel to use for ECG peak detection.
            The argument is mandatory if the dataset contains no ECG
            channels.
        threshold : float | 'auto'
            Value above which a feature is classified as outlier. See Notes.

            .. versionchanged:: 0.21
        start : int | float | None
            First sample to include. If float, data will be interpreted as
            time in seconds. If None, data will be used from the first sample.
            When working with Epochs or Evoked objects, must be float or None.
        stop : int | float | None
            Last sample to not include. If float, data will be interpreted as
            time in seconds. If None, data will be used to the last sample.
            When working with Epochs or Evoked objects, must be float or None.
        l_freq : float
            Low pass frequency.
        h_freq : float
            High pass frequency.
        method : 'ctps' | 'correlation'
            The method used for detection. If ``'ctps'``, cross-trial phase
            statistics :footcite:`DammersEtAl2008` are used to detect
            ECG-related components. See Notes.
        
        reject_by_annotation : bool
            Whether to omit bad segments from the data before fitting. If ``True``
            (default), annotated segments whose description begins with ``'bad'`` are
            omitted. If ``False``, no rejection based on annotations is performed.

            .. versionadded:: 0.14.0
        
        measure : 'zscore' | 'correlation'
            Which method to use for finding outliers among the components:
        
            - ``'zscore'`` (default) is the iterative z-scoring method. This method
              computes the z-score of the component's scores and masks the components
              with a z-score above threshold. This process is repeated until no
              supra-threshold component remains.
            - ``'correlation'`` is an absolute raw correlation threshold ranging from 0
              to 1.
        
            .. versionadded:: 0.21
        
        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        ecg_idx : list of int
            The indices of ECG-related components.
        scores : np.ndarray of float, shape (``n_components_``)
            If method is 'ctps', the normalized Kuiper index scores. If method
            is 'correlation', the correlation scores.

        See Also
        --------
        find_bads_eog, find_bads_ref, find_bads_muscle

        Notes
        -----
        The ``threshold``, ``method``, and ``measure`` parameters interact in
        the following ways:

        - If ``method='ctps'``, ``threshold`` refers to the significance value
          of a Kuiper statistic, and ``threshold='auto'`` will compute the
          threshold automatically based on the sampling frequency.
        - If ``method='correlation'`` and ``measure='correlation'``,
          ``threshold`` refers to the Pearson correlation value, and
          ``threshold='auto'`` sets the threshold to 0.9.
        - If ``method='correlation'`` and ``measure='zscore'``, ``threshold``
          refers to the z-score value (i.e., standard deviations) used in the
          iterative z-scoring method, and ``threshold='auto'`` sets the
          threshold to 3.0.

        References
        ----------
        .. footbibliography::
        """

    def find_bads_ref(self, inst, ch_name: Incomplete | None=..., threshold: float=..., start: Incomplete | None=..., stop: Incomplete | None=..., l_freq: Incomplete | None=..., h_freq: Incomplete | None=..., reject_by_annotation: bool=..., method: str=..., measure: str=..., verbose: Incomplete | None=...):
        """Detect MEG reference related components using correlation.

        Parameters
        ----------
        inst : instance of Raw, Epochs or Evoked
            Object to compute sources from. Should contain at least one channel
            i.e. component derived from MEG reference channels.
        ch_name : list of str
            Which MEG reference components to use. If None, then all channels
            that begin with REF_ICA.
        threshold : float | str
            Value above which a feature is classified as outlier.

            - If ``measure`` is ``'zscore'``, defines the threshold on the
              z-score used in the iterative z-scoring method.
            - If ``measure`` is ``'correlation'``, defines the absolute
              threshold on the correlation between 0 and 1.
            - If ``'auto'``, defaults to 3.0 if ``measure`` is ``'zscore'`` and
              0.9 if ``measure`` is ``'correlation'``.

             .. warning::
                 If ``method`` is ``'together'``, the iterative z-score method
                 is always used.
        start : int | float | None
            First sample to include. If float, data will be interpreted as
            time in seconds. If None, data will be used from the first sample.
        stop : int | float | None
            Last sample to not include. If float, data will be interpreted as
            time in seconds. If None, data will be used to the last sample.
        l_freq : float
            Low pass frequency.
        h_freq : float
            High pass frequency.
        
        reject_by_annotation : bool
            Whether to omit bad segments from the data before fitting. If ``True``
            (default), annotated segments whose description begins with ``'bad'`` are
            omitted. If ``False``, no rejection based on annotations is performed.
        method : 'together' | 'separate'
            Method to use to identify reference channel related components.
            Defaults to ``'together'``. See notes.

            .. versionadded:: 0.21
        
        measure : 'zscore' | 'correlation'
            Which method to use for finding outliers among the components:
        
            - ``'zscore'`` (default) is the iterative z-scoring method. This method
              computes the z-score of the component's scores and masks the components
              with a z-score above threshold. This process is repeated until no
              supra-threshold component remains.
            - ``'correlation'`` is an absolute raw correlation threshold ranging from 0
              to 1.
        
            .. versionadded:: 0.21
        
        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        ref_idx : list of int
            The indices of MEG reference related components, sorted by score.
        scores : np.ndarray of float, shape (``n_components_``) | list of array
            The correlation scores.

        See Also
        --------
        find_bads_ecg, find_bads_eog, find_bads_muscle

        Notes
        -----
        ICA decomposition on MEG reference channels is used to assess external
        magnetic noise and remove it from the MEG. Two methods are supported:

        With the ``'together'`` method, only one ICA fit is used, which
        encompasses both MEG and reference channels together. Components which
        have particularly strong weights on the reference channels may be
        thresholded and marked for removal.

        With ``'separate'`` selected components from a separate ICA
        decomposition on the reference channels are used as a ground truth for
        identifying bad components in an ICA fit done on MEG channels only. The
        logic here is similar to an EOG/ECG, with reference components
        replacing the EOG/ECG channels. Recommended procedure is to perform ICA
        separately on reference channels, extract them using
        :meth:`~mne.preprocessing.ICA.get_sources`, and then append them to the
        inst using :meth:`~mne.io.Raw.add_channels`, preferably with the prefix
        ``REF_ICA`` so that they can be automatically detected.

        With ``'together'``, thresholding is based on adaptative z-scoring.

        With ``'separate'``:

        - If ``measure`` is ``'zscore'``, thresholding is based on adaptative
          z-scoring.
        - If ``measure`` is ``'correlation'``, threshold defines the absolute
          threshold on the correlation between 0 and 1.

        Validation and further documentation for this technique can be found
        in :footcite:`HannaEtAl2020`.

        .. versionadded:: 0.18

        References
        ----------
        .. footbibliography::
        """

    def find_bads_muscle(self, inst, threshold: float=..., start: Incomplete | None=..., stop: Incomplete | None=..., l_freq: int=..., h_freq: int=..., sphere: Incomplete | None=..., verbose: Incomplete | None=...):
        """Detect muscle related components.

        Detection is based on :footcite:`DharmapraniEtAl2016` which uses
        data from a subject who has been temporarily paralyzed
        :footcite:`WhithamEtAl2007`. The criteria are threefold:
        1) Positive log-log spectral slope from 7 to 45 Hz
        2) Peripheral component power (farthest away from the vertex)
        3) A single focal point measured by low spatial smoothness

        The threshold is relative to the slope, focal point and smoothness
        of a typical muscle-related ICA component. Note the high frequency
        of the power spectral density slope was 75 Hz in the reference but
        has been modified to 45 Hz as a default based on the criteria being
        more accurate in practice.

        Parameters
        ----------
        inst : instance of Raw, Epochs or Evoked
            Object to compute sources from.
        threshold : float | str
            Value above which a component should be marked as muscle-related,
            relative to a typical muscle component.
        start : int | float | None
            First sample to include. If float, data will be interpreted as
            time in seconds. If None, data will be used from the first sample.
        stop : int | float | None
            Last sample to not include. If float, data will be interpreted as
            time in seconds. If None, data will be used to the last sample.
        l_freq : float
            Low frequency for muscle-related power.
        h_freq : float
            High frequency for msucle related power.
        sphere : float | array-like | instance of ConductorModel | None  | 'auto' | 'eeglab'
            The sphere parameters to use for the head outline. Can be array-like of
            shape (4,) to give the X/Y/Z origin and radius in meters, or a single float
            to give just the radius (origin assumed 0, 0, 0). Can also be an instance
            of a spherical :class:`~mne.bem.ConductorModel` to use the origin and
            radius from that object. If ``'auto'`` the sphere is fit to digitization
            points. If ``'eeglab'`` the head circle is defined by EEG electrodes
            ``'Fpz'``, ``'Oz'``, ``'T7'``, and ``'T8'`` (if ``'Fpz'`` is not present,
            it will be approximated from the coordinates of ``'Oz'``). ``None`` (the
            default) is equivalent to ``'auto'`` when enough extra digitization points
            are available, and (0, 0, 0, 0.095) otherwise.
        
            .. versionadded:: 0.20
            .. versionchanged:: 1.1 Added ``'eeglab'`` option.
        
        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        muscle_idx : list of int
            The indices of EOG related components, sorted by score.
        scores : np.ndarray of float, shape (``n_components_``) | list of array
            The correlation scores.

        See Also
        --------
        find_bads_ecg, find_bads_eog, find_bads_ref

        Notes
        -----
        .. versionadded:: 1.1
        """

    def find_bads_eog(self, inst, ch_name: Incomplete | None=..., threshold: float=..., start: Incomplete | None=..., stop: Incomplete | None=..., l_freq: int=..., h_freq: int=..., reject_by_annotation: bool=..., measure: str=..., verbose: Incomplete | None=...):
        """Detect EOG related components using correlation.

        Detection is based on Pearson correlation between the
        filtered data and the filtered EOG channel.
        Thresholding is based on adaptive z-scoring. The above threshold
        components will be masked and the z-score will be recomputed
        until no supra-threshold component remains.

        Parameters
        ----------
        inst : instance of Raw, Epochs or Evoked
            Object to compute sources from.
        ch_name : str
            The name of the channel to use for EOG peak detection.
            The argument is mandatory if the dataset contains no EOG
            channels.
        threshold : float | str
            Value above which a feature is classified as outlier.

            - If ``measure`` is ``'zscore'``, defines the threshold on the
              z-score used in the iterative z-scoring method.
            - If ``measure`` is ``'correlation'``, defines the absolute
              threshold on the correlation between 0 and 1.
            - If ``'auto'``, defaults to 3.0 if ``measure`` is ``'zscore'`` and
              0.9 if ``measure`` is ``'correlation'``.
        start : int | float | None
            First sample to include. If float, data will be interpreted as
            time in seconds. If None, data will be used from the first sample.
        stop : int | float | None
            Last sample to not include. If float, data will be interpreted as
            time in seconds. If None, data will be used to the last sample.
        l_freq : float
            Low pass frequency.
        h_freq : float
            High pass frequency.
        
        reject_by_annotation : bool
            Whether to omit bad segments from the data before fitting. If ``True``
            (default), annotated segments whose description begins with ``'bad'`` are
            omitted. If ``False``, no rejection based on annotations is performed.

            .. versionadded:: 0.14.0
        
        measure : 'zscore' | 'correlation'
            Which method to use for finding outliers among the components:
        
            - ``'zscore'`` (default) is the iterative z-scoring method. This method
              computes the z-score of the component's scores and masks the components
              with a z-score above threshold. This process is repeated until no
              supra-threshold component remains.
            - ``'correlation'`` is an absolute raw correlation threshold ranging from 0
              to 1.
        
            .. versionadded:: 0.21
        
        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        eog_idx : list of int
            The indices of EOG related components, sorted by score.
        scores : np.ndarray of float, shape (``n_components_``) | list of array
            The correlation scores.

        See Also
        --------
        find_bads_ecg, find_bads_ref
        """

    def apply(self, inst, include: Incomplete | None=..., exclude: Incomplete | None=..., n_pca_components: Incomplete | None=..., start: Incomplete | None=..., stop: Incomplete | None=..., *, on_baseline: str=..., verbose: Incomplete | None=...):
        """Remove selected components from the signal.

        Given the unmixing matrix, transform the data,
        zero out all excluded components, and inverse-transform the data.
        This procedure will reconstruct M/EEG signals from which
        the dynamics described by the excluded components is subtracted.

        Parameters
        ----------
        inst : instance of Raw, Epochs or Evoked
            The data to be processed (i.e., cleaned). It will be modified
            in-place.
        include : array_like of int
            The indices referring to columns in the ummixing matrix. The
            components to be kept. If ``None`` (default), all components
            will be included (minus those defined in ``ica.exclude``
            and the ``exclude`` parameter, see below).
        exclude : array_like of int
            The indices referring to columns in the ummixing matrix. The
            components to be zeroed out. If ``None`` (default) or an
            empty list, only components from ``ica.exclude`` will be
            excluded. Else, the union of ``exclude`` and ``ica.exclude``
            will be excluded.
        
        n_pca_components : int | float | None
            The number of PCA components to be kept, either absolute (int)
            or fraction of the explained variance (float). If None (default),
            the ``ica.n_pca_components`` from initialization will be used in 0.22;
            in 0.23 all components will be used.
        start : int | float | None
            First sample to include. If float, data will be interpreted as
            time in seconds. If None, data will be used from the first sample.
        stop : int | float | None
            Last sample to not include. If float, data will be interpreted as
            time in seconds. If None, data will be used to the last sample.
        
        on_baseline : str
            How to handle baseline-corrected epochs or evoked data.
            Can be ``'raise'`` to raise an error, ``'warn'`` (default) to emit a
            warning, ``'ignore'`` to ignore, or "reapply" to reapply the baseline
            after applying ICA.
        
            .. versionadded:: 1.2
        
        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        out : instance of Raw, Epochs or Evoked
            The processed data.

        Notes
        -----
        .. note:: Applying ICA may introduce a DC shift. If you pass
                  baseline-corrected `~mne.Epochs` or `~mne.Evoked` data,
                  the baseline period of the cleaned data may not be of
                  zero mean anymore. If you require baseline-corrected
                  data, apply baseline correction again after cleaning
                  via ICA. A warning will be emitted to remind you of this
                  fact if you pass baseline-corrected data.

        .. versionchanged:: 0.23
            Warn if instance was baseline-corrected.
        """

    def save(self, fname, *, overwrite: bool=..., verbose: Incomplete | None=...):
        """Store ICA solution into a fiff file.

        Parameters
        ----------
        fname : path-like
            The absolute path of the file name to save the ICA solution into.
            The file name should end with ``-ica.fif`` or ``-ica.fif.gz``.
        
        overwrite : bool
            If True (default False), overwrite the destination file if it
            exists.

            .. versionadded:: 1.0
        
        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        ica : instance of ICA
            The object.

        See Also
        --------
        read_ica
        """

    def copy(self):
        """Copy the ICA object.

        Returns
        -------
        ica : instance of ICA
            The copied object.
        """

    def plot_components(self, picks: Incomplete | None=..., ch_type: Incomplete | None=..., *, inst: Incomplete | None=..., plot_std: bool=..., reject: str=..., sensors: bool=..., show_names: bool=..., contours: int=..., outlines: str=..., sphere: Incomplete | None=..., image_interp=..., extrapolate=..., border=..., res: int=..., size: int=..., cmap: str=..., vlim=..., cnorm: Incomplete | None=..., colorbar: bool=..., cbar_fmt: str=..., axes: Incomplete | None=..., title: Incomplete | None=..., nrows: str=..., ncols: str=..., show: bool=..., image_args: Incomplete | None=..., psd_args: Incomplete | None=..., verbose: Incomplete | None=...):
        """Project mixing matrix on interpolated sensor topography.

    Parameters
    ----------
    picks : int | list of int | slice | None
        Indices of the independent components (ICs) to visualize.
        If an integer, represents the index of the IC to pick.
        Multiple ICs can be selected using a list of int or a slice.
        The indices are 0-indexed, so ``picks=1`` will pick the second
        IC: ``ICA001``. ``None`` will pick all independent components in the order
        fitted.
    ch_type : 'mag' | 'grad' | 'planar1' | 'planar2' | 'eeg' | None
        The channel type to plot. For ``'grad'``, the gradiometers are
        collected in pairs and the RMS for each pair is plotted. If
        ``None`` the first available channel type from order shown above is used. Defaults to ``None``.
    inst : Raw | Epochs | None
        To be able to see component properties after clicking on component
        topomap you need to pass relevant data - instances of Raw or Epochs
        (for example the data that ICA was trained on). This takes effect
        only when running matplotlib in interactive mode.
    plot_std : bool | float
        Whether to plot standard deviation in ERP/ERF and spectrum plots.
        Defaults to True, which plots one standard deviation above/below.
        If set to float allows to control how many standard deviations are
        plotted. For example 2.5 will plot 2.5 standard deviation above/below.
    reject : ``'auto'`` | dict | None
        Allows to specify rejection parameters used to drop epochs
        (or segments if continuous signal is passed as inst).
        If None, no rejection is applied. The default is 'auto',
        which applies the rejection parameters used when fitting
        the ICA object.
    
    sensors : bool | str
        Whether to add markers for sensor locations. If :class:`str`, should be a
        valid matplotlib format string (e.g., ``'r+'`` for red plusses, see the
        Notes section of :meth:`~matplotlib.axes.Axes.plot`). If ``True`` (the
        default), black circles will be used.
    
    show_names : bool | callable
        If ``True``, show channel names next to each sensor marker. If callable,
        channel names will be formatted using the callable; e.g., to
        delete the prefix 'MEG ' from all channel names, pass the function
        ``lambda x: x.replace('MEG ', '')``. If ``mask`` is not ``None``, only
        non-masked sensor names will be shown.
    
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
        of a spherical :class:`~mne.bem.ConductorModel` to use the origin and
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

        .. versionadded:: 1.3
    
    border : float | 'mean'
        Value to extrapolate to on the topomap borders. If ``'mean'`` (default),
        then each extrapolated point has the average value of its neighbours.

        .. versionadded:: 1.3
    
    res : int
        The resolution of the topomap image (number of pixels along each side).
    
    size : float
        Side length of each subplot in inches.

        .. versionadded:: 1.3
    
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

        .. versionadded:: 1.3
    
    cnorm : matplotlib.colors.Normalize | None
        How to normalize the colormap. If ``None``, standard linear normalization
        is performed. If not ``None``, ``vmin`` and ``vmax`` will be ignored.
        See :ref:`Matplotlib docs <matplotlib:colormapnorms>`
        for more details on colormap normalization, and
        :ref:`the ERDs example<cnorm-example>` for an example of its use.

        .. versionadded:: 1.3
    
    colorbar : bool
        Plot a colorbar in the rightmost column of the figure.
    cbar_fmt : str
        Formatting string for colorbar tick labels. See :ref:`formatspec` for
        details.
    axes : Axes | array of Axes | None
        The subplot(s) to plot to. Either a single Axes or an iterable of Axes
        if more than one subplot is needed. The number of subplots must match
        the number of selected components. If None, new figures will be created
        with the number of subplots per figure controlled by ``nrows`` and
        ``ncols``.
    title : str | None
        The title of the generated figure. If ``None`` (default) and
        ``axes=None``, a default title of "ICA Components" will be used.
    
    nrows, ncols : int | 'auto'
        The number of rows and columns of topographies to plot. If both ``nrows``
        and ``ncols`` are ``'auto'``, will plot up to 20 components in a 5×4 grid,
        and return multiple figures if more than 20 components are requested.
        If one is ``'auto'`` and the other a scalar, a single figure is generated.
        If scalars are provided for both arguments, will plot up to ``nrows*ncols``
        components in a grid and return multiple figures as needed. Default is
        ``nrows='auto', ncols='auto'``.

        .. versionadded:: 1.3
    show : bool
        Show the figure if ``True``.
    image_args : dict | None
        Dictionary of arguments to pass to :func:`~mne.viz.plot_epochs_image`
        in interactive mode. Ignored if ``inst`` is not supplied. If ``None``,
        nothing is passed. Defaults to ``None``.
    psd_args : dict | None
        Dictionary of arguments to pass to :meth:`~mne.Epochs.compute_psd` in
        interactive  mode. Ignored if ``inst`` is not supplied. If ``None``,
        nothing is passed. Defaults to ``None``.
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    fig : instance of matplotlib.figure.Figure | list of matplotlib.figure.Figure
        The figure object(s).

    Notes
    -----
    When run in interactive mode, ``plot_ica_components`` allows to reject
    components by clicking on their title label. The state of each component
    is indicated by its label color (gray: rejected; black: retained). It is
    also possible to open component properties by clicking on the component
    topomap (this option is only available when the ``inst`` argument is
    supplied).
    """

    def plot_properties(self, inst, picks: Incomplete | None=..., axes: Incomplete | None=..., dB: bool=..., plot_std: bool=..., log_scale: bool=..., topomap_args: Incomplete | None=..., image_args: Incomplete | None=..., psd_args: Incomplete | None=..., figsize: Incomplete | None=..., show: bool=..., reject: str=..., reject_by_annotation: bool=..., *, verbose: Incomplete | None=...):
        """Display component properties.

    Properties include the topography, epochs image, ERP/ERF, power
    spectrum, and epoch variance.

    Parameters
    ----------
    inst : instance of Epochs or Raw
        The data to use in plotting properties.

        .. note::
           You can interactively cycle through topographic maps for different
           channel types by pressing :kbd:`T`.
    picks : int | list of int | slice | None
        Indices of the independent components (ICs) to visualize.
        If an integer, represents the index of the IC to pick.
        Multiple ICs can be selected using a list of int or a slice.
        The indices are 0-indexed, so ``picks=1`` will pick the second
        IC: ``ICA001``. ``None`` will pick the first 5 components.
    axes : list of Axes | None
        List of five matplotlib axes to use in plotting: [topomap_axis,
        image_axis, erp_axis, spectrum_axis, variance_axis]. If None a new
        figure with relevant axes is created. Defaults to None.
    dB : bool
        Whether to plot spectrum in dB. Defaults to True.
    plot_std : bool | float
        Whether to plot standard deviation/confidence intervals in ERP/ERF and
        spectrum plots.
        Defaults to True, which plots one standard deviation above/below for
        the spectrum. If set to float allows to control how many standard
        deviations are plotted for the spectrum. For example 2.5 will plot 2.5
        standard deviation above/below.
        For the ERP/ERF, by default, plot the 95 percent parametric confidence
        interval is calculated. To change this, use ``ci`` in ``ts_args`` in
        ``image_args`` (see below).
    log_scale : bool
        Whether to use a logarithmic frequency axis to plot the spectrum.
        Defaults to ``False``.

        .. note::
           You can interactively toggle this setting by pressing :kbd:`L`.

        .. versionadded:: 1.1
    topomap_args : dict | None
        Dictionary of arguments to ``plot_topomap``. If None, doesn't pass any
        additional arguments. Defaults to None.
    image_args : dict | None
        Dictionary of arguments to ``plot_epochs_image``. If None, doesn't pass
        any additional arguments. Defaults to None.
    psd_args : dict | None
        Dictionary of arguments to :meth:`~mne.Epochs.compute_psd`. If
        ``None``, doesn't pass any additional arguments. Defaults to ``None``.
    figsize : array-like, shape (2,) | None
        Allows to control size of the figure. If None, the figure size
        defaults to [7., 6.].
    show : bool
        Show figure if True.
    reject : 'auto' | dict | None
        Allows to specify rejection parameters used to drop epochs
        (or segments if continuous signal is passed as inst).
        If None, no rejection is applied. The default is 'auto',
        which applies the rejection parameters used when fitting
        the ICA object.
    
    reject_by_annotation : bool
        Whether to omit bad segments from the data before fitting. If ``True``
        (default), annotated segments whose description begins with ``'bad'`` are
        omitted. If ``False``, no rejection based on annotations is performed.
    
        Has no effect if ``inst`` is not a :class:`mne.io.Raw` object.

        .. versionadded:: 0.21.0
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    fig : list
        List of matplotlib figures.

    Notes
    -----
    .. versionadded:: 0.13
    """

    def plot_sources(self, inst, picks: Incomplete | None=..., start: Incomplete | None=..., stop: Incomplete | None=..., title: Incomplete | None=..., show: bool=..., block: bool=..., show_first_samp: bool=..., show_scrollbars: bool=..., time_format: str=..., precompute: Incomplete | None=..., use_opengl: Incomplete | None=..., *, theme: Incomplete | None=..., overview_mode: Incomplete | None=..., splash: bool=...):
        """Plot estimated latent sources given the unmixing matrix.

    Typical usecases:

    1. plot evolution of latent sources over time based on (Raw input)
    2. plot latent source around event related time windows (Epochs input)
    3. plot time-locking in ICA space (Evoked input)

    Parameters
    ----------
    inst : instance of Raw, Epochs or Evoked
        The object to plot the sources from.
    
    picks : int | list of int | slice | None
        Indices of the independent components (ICs) to visualize.
        If an integer, represents the index of the IC to pick.
        Multiple ICs can be selected using a list of int or a slice.
        The indices are 0-indexed, so ``picks=1`` will pick the second
        IC: ``ICA001``. ``None`` will pick all independent components in the order
        fitted.
    start, stop : float | int | None
       If ``inst`` is a `~mne.io.Raw` or an `~mne.Evoked` object, the first and
       last time point (in seconds) of the data to plot. If ``inst`` is a
       `~mne.io.Raw` object, ``start=None`` and ``stop=None`` will be
       translated into ``start=0.`` and ``stop=3.``, respectively. For
       `~mne.Evoked`, ``None`` refers to the beginning and end of the evoked
       signal. If ``inst`` is an `~mne.Epochs` object, specifies the index of
       the first and last epoch to show.
    title : str | None
        The window title. If None a default is provided.
    show : bool
        Show figure if True.
    block : bool
        Whether to halt program execution until the figure is closed.
        Useful for interactive selection of components in raw and epoch
        plotter. For evoked, this parameter has no effect. Defaults to False.
    show_first_samp : bool
        If True, show time axis relative to the ``raw.first_samp``.
    
    show_scrollbars : bool
        Whether to show scrollbars when the plot is initialized. Can be toggled
        after initialization by pressing :kbd:`z` ("zen mode") while the plot
        window is focused. Default is ``True``.
    
        .. versionadded:: 0.19.0
    
    time_format : 'float' | 'clock'
        Style of time labels on the horizontal axis. If ``'float'``, labels will be
        number of seconds from the start of the recording. If ``'clock'``,
        labels will show "clock time" (hours/minutes/seconds) inferred from
        ``raw.info['meas_date']``. Default is ``'float'``.
    
        .. versionadded:: 0.24
    
    precompute : bool | str
        Whether to load all data (not just the visible portion) into RAM and
        apply preprocessing (e.g., projectors) to the full data array in a separate
        processor thread, instead of window-by-window during scrolling. The default
        None uses the ``MNE_BROWSER_PRECOMPUTE`` variable, which defaults to
        ``'auto'``. ``'auto'`` compares available RAM space to the expected size of
        the precomputed data, and precomputes only if enough RAM is available.
        This is only used with the Qt backend.
    
        .. versionadded:: 0.24
        .. versionchanged:: 1.0
           Support for the MNE_BROWSER_PRECOMPUTE config variable.
    
    use_opengl : bool | None
        Whether to use OpenGL when rendering the plot (requires ``pyopengl``).
        May increase performance, but effect is dependent on system CPU and
        graphics hardware. Only works if using the Qt backend. Default is
        None, which will use False unless the user configuration variable
        ``MNE_BROWSER_USE_OPENGL`` is set to ``'true'``,
        see :func:`mne.set_config`.
    
        .. versionadded:: 0.24
    
    theme : str | path-like
        Can be "auto", "light", or "dark" or a path-like to a
        custom stylesheet. For Dark-Mode and automatic Dark-Mode-Detection,
        :mod:`qdarkstyle` and
        `darkdetect <https://github.com/albertosottile/darkdetect>`__,
        respectively, are required.    If None (default), the config option MNE_BROWSER_THEME will be used,
        defaulting to "auto" if it's not found.
        Only supported by the ``'qt'`` backend.

        .. versionadded:: 1.0
    
    overview_mode : str | None
        Can be "channels", "empty", or "hidden" to set the overview bar mode
        for the ``'qt'`` backend. If None (default), the config option
        ``MNE_BROWSER_OVERVIEW_MODE`` will be used, defaulting to "channels"
        if it's not found.

        .. versionadded:: 1.1
    
    splash : bool
        If True (default), a splash screen is shown during the application startup. Only
        applicable to the ``qt`` backend.

        .. versionadded:: 1.6

    Returns
    -------
    
    fig : matplotlib.figure.Figure | mne_qt_browser.figure.MNEQtBrowser
        Browser instance.

    Notes
    -----
    For raw and epoch instances, it is possible to select components for
    exclusion by clicking on the line. The selected components are added to
    ``ica.exclude`` on close.

    MNE-Python provides two different backends for browsing plots (i.e.,
    :meth:`raw.plot()<mne.io.Raw.plot>`, :meth:`epochs.plot()<mne.Epochs.plot>`,
    and :meth:`ica.plot_sources()<mne.preprocessing.ICA.plot_sources>`). One is
    based on :mod:`matplotlib`, and the other is based on
    :doc:`PyQtGraph<pyqtgraph:index>`. You can set the backend temporarily with the
    context manager :func:`mne.viz.use_browser_backend`, you can set it for the
    duration of a Python session using :func:`mne.viz.set_browser_backend`, and you
    can set the default for your computer via
    :func:`mne.set_config('MNE_BROWSER_BACKEND', 'matplotlib')<mne.set_config>`
    (or ``'qt'``).
    
    .. note:: For the PyQtGraph backend to run in IPython with ``block=False``
              you must run the magic command ``%gui qt5`` first.
    .. note:: To report issues with the PyQtGraph backend, please use the
              `issues <https://github.com/mne-tools/mne-qt-browser/issues>`_
              of ``mne-qt-browser``.

    .. versionadded:: 0.10.0
    """

    def plot_scores(self, scores, exclude: Incomplete | None=..., labels: Incomplete | None=..., axhline: Incomplete | None=..., title: str=..., figsize: Incomplete | None=..., n_cols: Incomplete | None=..., show: bool=...):
        """Plot scores related to detected components.

    Use this function to asses how well your score describes outlier
    sources and how well you were detecting them.

    Parameters
    ----------
    scores : array-like of float, shape (n_ica_components,) | list of array
        Scores based on arbitrary metric to characterize ICA components.
    exclude : array-like of int
        The components marked for exclusion. If None (default), ICA.exclude
        will be used.
    labels : str | list | 'ecg' | 'eog' | None
        The labels to consider for the axes tests. Defaults to None.
        If list, should match the outer shape of ``scores``.
        If 'ecg' or 'eog', the ``labels_`` attributes will be looked up.
        Note that '/' is used internally for sublabels specifying ECG and
        EOG channels.
    axhline : float
        Draw horizontal line to e.g. visualize rejection threshold.
    title : str
        The figure title.
    figsize : tuple of int | None
        The figure size. If None it gets set automatically.
    n_cols : int | None
        Scores are plotted in a grid. This parameter controls how
        many to plot side by side before starting a new row. By
        default, a number will be chosen to make the grid as square as
        possible.
    show : bool
        Show figure if True.

    Returns
    -------
    fig : instance of Figure
        The figure object.
    """

    def plot_overlay(self, inst, exclude: Incomplete | None=..., picks: Incomplete | None=..., start: Incomplete | None=..., stop: Incomplete | None=..., title: Incomplete | None=..., show: bool=..., n_pca_components: Incomplete | None=..., *, on_baseline: str=..., verbose: Incomplete | None=...):
        """Overlay of raw and cleaned signals given the unmixing matrix.

    This method helps visualizing signal quality and artifact rejection.

    Parameters
    ----------
    inst : instance of Raw or Evoked
        The signal to plot. If `~mne.io.Raw`, the raw data per channel type is displayed
        before and after cleaning. A second panel with the RMS for MEG sensors and the
        :term:`GFP` for EEG sensors is displayed. If `~mne.Evoked`, butterfly traces for
        signals before and after cleaning will be superimposed.
    exclude : array-like of int | None (default)
        The components marked for exclusion. If ``None`` (default), the components
        listed in ``ICA.exclude`` will be used.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as 
        channel indices. In lists, channel *type* strings (e.g., ``['meg', 
        'eeg']``) will pick channels of those types, channel *name* strings (e.g., 
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the 
        string values "all" to pick all channels, or "data" to pick :term:`data 
        channels`. None (default) will pick all channels that were included during fitting.
    start, stop : float | None
       The first and last time point (in seconds) of the data to plot. If
       ``inst`` is a `~mne.io.Raw` object, ``start=None`` and ``stop=None``
       will be translated into ``start=0.`` and ``stop=3.``, respectively. For
       `~mne.Evoked`, ``None`` refers to the beginning and end of the evoked
       signal.
    
    title : str | None
        The title of the generated figure. If ``None`` (default), no title is
        displayed.
    show : bool
        Show the figure if ``True``.
    
    n_pca_components : int | float | None
        The number of PCA components to be kept, either absolute (int)
        or fraction of the explained variance (float). If None (default),
        the ``ica.n_pca_components`` from initialization will be used in 0.22;
        in 0.23 all components will be used.

        .. versionadded:: 0.22
    
    on_baseline : str
        How to handle baseline-corrected epochs or evoked data.
        Can be ``'raise'`` to raise an error, ``'warn'`` (default) to emit a
        warning, ``'ignore'`` to ignore, or "reapply" to reapply the baseline
        after applying ICA.
    
        .. versionadded:: 1.2
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    fig : instance of Figure
        The figure.
    """

def ica_find_ecg_events(raw, ecg_source, event_id: int=..., tstart: float=..., l_freq: int=..., h_freq: int=..., qrs_threshold: str=..., verbose: Incomplete | None=...):
    """Find ECG peaks from one selected ICA source.

    Parameters
    ----------
    raw : instance of Raw
        Raw object to draw sources from.
    ecg_source : ndarray
        ICA source resembling ECG to find peaks from.
    event_id : int
        The index to assign to found events.
    tstart : float
        Start detection after tstart seconds. Useful when beginning
        of run is noisy.
    l_freq : float
        Low pass frequency.
    h_freq : float
        High pass frequency.
    qrs_threshold : float | str
        Between 0 and 1. qrs detection threshold. Can also be "auto" to
        automatically choose the threshold that generates a reasonable
        number of heartbeats (40-160 beats / min).
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    ecg_events : array
        Events.
    ch_ECG : string
        Name of channel used.
    average_pulse : float.
        Estimated average pulse.
    """

def ica_find_eog_events(raw, eog_source: Incomplete | None=..., event_id: int=..., l_freq: int=..., h_freq: int=..., verbose: Incomplete | None=...):
    """Locate EOG artifacts from one selected ICA source.

    Parameters
    ----------
    raw : instance of Raw
        The raw data.
    eog_source : ndarray
        ICA source resembling EOG to find peaks from.
    event_id : int
        The index to assign to found events.
    l_freq : float
        Low cut-off frequency in Hz.
    h_freq : float
        High cut-off frequency in Hz.
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    eog_events : array
        Events.
    """

def read_ica(fname, verbose: Incomplete | None=...):
    """Restore ICA solution from fif file.

    Parameters
    ----------
    fname : path-like
        Absolute path to fif file containing ICA matrices.
        The file name should end with -ica.fif or -ica.fif.gz.
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    ica : instance of ICA
        The ICA estimator.
    """

class _ica_node(NamedTuple):
    name: Incomplete
    target: Incomplete
    score_func: Incomplete
    criterion: Incomplete

def read_ica_eeglab(fname, *, montage_units: str=..., verbose: Incomplete | None=...):
    """Load ICA information saved in an EEGLAB .set file.

    Parameters
    ----------
    fname : path-like
        Complete path to a ``.set`` EEGLAB file that contains an ICA object.
    
    montage_units : str
        Units that channel positions are represented in. Defaults to "mm"
        (millimeters), but can be any prefix + "m" combination (including just
        "m" for meters).
    
        .. versionadded:: 1.3

        .. versionadded:: 1.6
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    ica : instance of ICA
        An ICA object based on the information contained in the input file.
    """