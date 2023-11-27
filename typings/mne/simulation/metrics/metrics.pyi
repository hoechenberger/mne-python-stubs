from ...utils import fill_doc as fill_doc

def source_estimate_quantification(stc1, stc2, metric: str = "rms"):
    """## Calculate STC similarities across all sources and times.

    -----
    ### 🛠️ Parameters

    stc1 : SourceEstimate
        First source estimate for comparison.
    stc2 : SourceEstimate
        Second source estimate for comparison.
    #### `metric : str`
        Metric to calculate, ``'rms'`` or ``'cosine'``.

    -----
    ### ⏎ Returns

    #### `score : float | array`
        Calculated metric.

    -----
    ### 📖 Notes

    Metric calculation has multiple options:

        * rms: Root mean square of difference between stc data matrices.
        * cosine: Normalized correlation of all elements in stc data matrices.

    ✨ Added in version 0.10.0
    """
    ...

def cosine_score(stc_true, stc_est, per_sample: bool = True):
    """## Compute cosine similarity between 2 source estimates.

    -----
    ### 🛠️ Parameters


    #### `stc_true : instance of (Vol|Mixed)SourceEstimate`
        The source estimates containing correct values.

    #### `stc_est : instance of (Vol|Mixed)SourceEstimate`
        The source estimates containing estimated values
        e.g. obtained with a source imaging method.

    #### `per_sample : bool`
        If True the metric is computed for each sample
        separately. If False, the metric is spatio-temporal.

    -----
    ### ⏎ Returns


    #### `metric : float | array, shape (n_times,)`
        The metric. float if per_sample is False, else
        array with the values computed for each time point.

    -----
    ### 📖 Notes

    ✨ Added in version 1.2
    """
    ...

def region_localization_error(
    stc_true, stc_est, src, threshold: str = "90%", per_sample: bool = True
):
    """## Compute region localization error (RLE) between 2 source estimates.

    .. math::

        RLE = \\frac{1}{2Q}\\sum_{k \\in I} \\min_{l \\in \\hat{I}}{||r_k - r_l||} + \\frac{1}{2\\hat{Q}}\\sum_{l \\in \\hat{I}} \\min_{k \\in I}{||r_k - r_l||}

    where :math:`I` and :math:`\\hat{I}` denote respectively the original and
    estimated indexes of active sources, :math:`Q` and :math:`\\hat{Q}` are
    the numbers of original and estimated active sources.
    :math:`r_k` denotes the position of the k-th source dipole in space
    and :math:`||\\cdot||` is an Euclidean norm in :math:`\\mathbb{R}^3`.

    -----
    ### 🛠️ Parameters


    #### `stc_true : instance of (Vol|Mixed)SourceEstimate`
        The source estimates containing correct values.

    #### `stc_est : instance of (Vol|Mixed)SourceEstimate`
        The source estimates containing estimated values
        e.g. obtained with a source imaging method.
    #### `src : instance of SourceSpaces`
        The source space on which the source estimates are defined.
    #### `threshold : float | str`
        The threshold to apply to source estimates before computing
        the dipole localization error. If a string the threshold is
        a percentage and it should end with the percent character.

    #### `per_sample : bool`
        If True the metric is computed for each sample
        separately. If False, the metric is spatio-temporal.

    -----
    ### ⏎ Returns


    #### `metric : float | array, shape (n_times,)`
        The metric. float if per_sample is False, else
        array with the values computed for each time point.

    -----
    ### 📖 Notes

    Papers :footcite:`MaksymenkoEtAl2017` and :footcite:`BeckerEtAl2017`
    use term Dipole Localization Error (DLE) for the same formula. Paper
    :footcite:`YaoEtAl2005` uses term Error Distance (ED) for the same formula.
    To unify the terminology and to avoid confusion with other cases
    of using term DLE but for different metric :footcite:`MolinsEtAl2008`, we
    use term Region Localization Error (RLE).

    ✨ Added in version 1.2

    References
    ----------
    .. footbibliography::
    """
    ...

def roc_auc_score(stc_true, stc_est, per_sample: bool = True):
    """## Compute ROC AUC between 2 source estimates.

    ROC stands for receiver operating curve and AUC is Area under the curve.
    When computing this metric the stc_true must be thresholded
    as any non-zero value will be considered as a positive.

    The ROC-AUC metric is computed between amplitudes of the source
    estimates, i.e. after taking the absolute values.

    -----
    ### 🛠️ Parameters


    #### `stc_true : instance of (Vol|Mixed)SourceEstimate`
        The source estimates containing correct values.

    #### `stc_est : instance of (Vol|Mixed)SourceEstimate`
        The source estimates containing estimated values
        e.g. obtained with a source imaging method.

    #### `per_sample : bool`
        If True the metric is computed for each sample
        separately. If False, the metric is spatio-temporal.

    -----
    ### ⏎ Returns


    #### `metric : float | array, shape (n_times,)`
        The metric. float if per_sample is False, else
        array with the values computed for each time point.

    -----
    ### 📖 Notes

    ✨ Added in version 1.2
    """
    ...

def f1_score(stc_true, stc_est, threshold: str = "90%", per_sample: bool = True):
    """## Compute the F1 score, also known as balanced F-score or F-measure.

    The F1 score can be interpreted as a weighted average of the precision
    and recall, where an F1 score reaches its best value at 1 and worst score
    at 0. The relative contribution of precision and recall to the F1
    score are equal.
    The formula for the F1 score is::

        F1 = 2 * (precision * recall) / (precision + recall)

    Threshold is used first for data binarization.

    -----
    ### 🛠️ Parameters


    #### `stc_true : instance of (Vol|Mixed)SourceEstimate`
        The source estimates containing correct values.

    #### `stc_est : instance of (Vol|Mixed)SourceEstimate`
        The source estimates containing estimated values
        e.g. obtained with a source imaging method.
    #### `threshold : float | str`
        The threshold to apply to source estimates before computing
        the f1 score. If a string the threshold is
        a percentage and it should end with the percent character.

    #### `per_sample : bool`
        If True the metric is computed for each sample
        separately. If False, the metric is spatio-temporal.

    -----
    ### ⏎ Returns


    #### `metric : float | array, shape (n_times,)`
        The metric. float if per_sample is False, else
        array with the values computed for each time point.

    -----
    ### 📖 Notes

    ✨ Added in version 1.2
    """
    ...

def precision_score(stc_true, stc_est, threshold: str = "90%", per_sample: bool = True):
    """## Compute the precision.

    The precision is the ratio ``tp / (tp + fp)`` where ``tp`` is the number of
    true positives and ``fp`` the number of false positives. The precision is
    intuitively the ability of the classifier not to label as positive a sample
    that is negative.

    The best value is 1 and the worst value is 0.

    Threshold is used first for data binarization.

    -----
    ### 🛠️ Parameters


    #### `stc_true : instance of (Vol|Mixed)SourceEstimate`
        The source estimates containing correct values.

    #### `stc_est : instance of (Vol|Mixed)SourceEstimate`
        The source estimates containing estimated values
        e.g. obtained with a source imaging method.
    #### `threshold : float | str`
        The threshold to apply to source estimates before computing
        the precision. If a string the threshold is
        a percentage and it should end with the percent character.

    #### `per_sample : bool`
        If True the metric is computed for each sample
        separately. If False, the metric is spatio-temporal.

    -----
    ### ⏎ Returns


    #### `metric : float | array, shape (n_times,)`
        The metric. float if per_sample is False, else
        array with the values computed for each time point.

    -----
    ### 📖 Notes

    ✨ Added in version 1.2
    """
    ...

def recall_score(stc_true, stc_est, threshold: str = "90%", per_sample: bool = True):
    """## Compute the recall.

    The recall is the ratio ``tp / (tp + fn)`` where ``tp`` is the number of
    true positives and ``fn`` the number of false negatives. The recall is
    intuitively the ability of the classifier to find all the positive samples.

    The best value is 1 and the worst value is 0.

    Threshold is used first for data binarization.

    -----
    ### 🛠️ Parameters


    #### `stc_true : instance of (Vol|Mixed)SourceEstimate`
        The source estimates containing correct values.

    #### `stc_est : instance of (Vol|Mixed)SourceEstimate`
        The source estimates containing estimated values
        e.g. obtained with a source imaging method.
    #### `threshold : float | str`
        The threshold to apply to source estimates before computing
        the recall. If a string the threshold is
        a percentage and it should end with the percent character.

    #### `per_sample : bool`
        If True the metric is computed for each sample
        separately. If False, the metric is spatio-temporal.

    -----
    ### ⏎ Returns


    #### `metric : float | array, shape (n_times,)`
        The metric. float if per_sample is False, else
        array with the values computed for each time point.

    -----
    ### 📖 Notes

    ✨ Added in version 1.2
    """
    ...

def peak_position_error(
    stc_true, stc_est, src, threshold: str = "50%", per_sample: bool = True
):
    """## Compute the peak position error.

    The peak position error measures the distance between the center-of-mass
    of the estimated and the true source.

    .. math::

        PPE = \\| \\dfrac{\\sum_i|s_i|r_{i}}{\\sum_i|s_i|}
        - r_{true}\\|,

    where :math:`r_{true}` is a true dipole position,
    :math:`r_i` and :math:`|s_i|` denote respectively the position
    and amplitude of i-th dipole in source estimate.

    Threshold is used on estimated source for focusing the metric to strong
    amplitudes and omitting the low-amplitude values.

    -----
    ### 🛠️ Parameters


    #### `stc_true : instance of (Vol|Mixed)SourceEstimate`
        The source estimates containing correct values.

    #### `stc_est : instance of (Vol|Mixed)SourceEstimate`
        The source estimates containing estimated values
        e.g. obtained with a source imaging method.
    #### `src : instance of SourceSpaces`
        The source space on which the source estimates are defined.
    #### `threshold : float | str`
        The threshold to apply to source estimates before computing
        the recall. If a string the threshold is
        a percentage and it should end with the percent character.

    #### `per_sample : bool`
        If True the metric is computed for each sample
        separately. If False, the metric is spatio-temporal.

    -----
    ### ⏎ Returns


    #### `metric : float | array, shape (n_times,)`
        The metric. float if per_sample is False, else
        array with the values computed for each time point.

    -----
    ### 📖 Notes

    These metrics are documented in :footcite:`StenroosHauk2013` and
    :footcite:`LinEtAl2006a`.

    ✨ Added in version 1.2

    References
    ----------
    .. footbibliography::
    """
    ...

def spatial_deviation_error(
    stc_true, stc_est, src, threshold: str = "50%", per_sample: bool = True
):
    """## Compute the spatial deviation.

    The spatial deviation characterizes the spread of the estimate source
    around the true source.

    .. math::

        SD = \\dfrac{\\sum_i|s_i|\\|r_{i} - r_{true}\\|^2}{\\sum_i|s_i|}.

    where :math:`r_{true}` is a true dipole position,
    :math:`r_i` and :math:`|s_i|` denote respectively the position
    and amplitude of i-th dipole in source estimate.

    Threshold is used on estimated source for focusing the metric to strong
    amplitudes and omitting the low-amplitude values.

    -----
    ### 🛠️ Parameters


    #### `stc_true : instance of (Vol|Mixed)SourceEstimate`
        The source estimates containing correct values.

    #### `stc_est : instance of (Vol|Mixed)SourceEstimate`
        The source estimates containing estimated values
        e.g. obtained with a source imaging method.
    #### `src : instance of SourceSpaces`
        The source space on which the source estimates are defined.
    #### `threshold : float | str`
        The threshold to apply to source estimates before computing
        the recall. If a string the threshold is
        a percentage and it should end with the percent character.

    #### `per_sample : bool`
        If True the metric is computed for each sample
        separately. If False, the metric is spatio-temporal.

    -----
    ### ⏎ Returns


    #### `metric : float | array, shape (n_times,)`
        The metric. float if per_sample is False, else
        array with the values computed for each time point.

    -----
    ### 📖 Notes

    These metrics are documented in :footcite:`StenroosHauk2013` and
    :footcite:`LinEtAl2006a`.

    ✨ Added in version 1.2

    References
    ----------
    .. footbibliography::
    """
    ...
