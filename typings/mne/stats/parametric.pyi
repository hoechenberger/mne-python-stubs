def ttest_1samp_no_p(X, sigma: int = 0, method: str = "relative"):
    """### Perform one-sample t-test.

    This is a modified version of `scipy.stats.ttest_1samp` that avoids
    a (relatively) time-consuming p-value calculation, and can adjust
    for implausibly small variance values :footcite:`RidgwayEtAl2012`.

    ### 🛠️ Parameters
    ----------
    X : array
        Array to return t-values for.
    sigma : float
        The variance estimate will be given by ``var + sigma * max(var)`` or
        ``var + sigma``, depending on "method". By default this is 0 (no
        adjustment). See Notes for details.
    method : str
        If 'relative', the minimum variance estimate will be sigma * max(var),
        if 'absolute' the minimum variance estimate will be sigma.

    ### ⏎ Returns
    -------
    t : array
        T-values, potentially adjusted using the hat method.

    ### 📖 Notes
    -----
    To use the "hat" adjustment method :footcite:`RidgwayEtAl2012`, a value
    of ``sigma=1e-3`` may be a reasonable choice.

    References
    ----------
    .. footbibliography::
    """
    ...

def ttest_ind_no_p(a, b, equal_var: bool = True, sigma: float = 0.0):
    """### Independent samples t-test without p calculation.

    This is a modified version of `scipy.stats.ttest_ind`. It operates
    along the first axis. The ``sigma`` parameter provides an optional "hat"
    adjustment (see `ttest_1samp_no_p` and :footcite:`RidgwayEtAl2012`).

    ### 🛠️ Parameters
    ----------
    a : array-like
        The first array.
    b : array-like
        The second array.
    equal_var : bool
        Assume equal variance. See `scipy.stats.ttest_ind`.
    sigma : float
        The regularization. See `ttest_1samp_no_p`.

    ### ⏎ Returns
    -------
    t : array
        T values.

    References
    ----------
    .. footbibliography::
    """
    ...

def f_oneway(*args):
    """### Perform a 1-way ANOVA.

    The one-way ANOVA tests the null hypothesis that 2 or more groups have
    the same population mean. The test is applied to samples from two or
    more groups, possibly with differing sizes :footcite:`Lowry2014`.

    This is a modified version of `scipy.stats.f_oneway` that avoids
    computing the associated p-value.

    ### 🛠️ Parameters
    ----------
    *args : array_like
        The sample measurements should be given as arguments.

    ### ⏎ Returns
    -------
    F-value : float
        The computed F-value of the test.

    ### 📖 Notes
    -----
    The ANOVA test has important assumptions that must be satisfied in order
    for the associated p-value to be valid.

    1. The samples are independent
    2. Each sample is from a normally distributed population
    3. The population standard deviations of the groups are all equal. This
       property is known as homoscedasticity.

    If these assumptions are not true for a given set of data, it may still be
    possible to use the Kruskal-Wallis H-test (`scipy.stats.kruskal`)
    although with some loss of power.

    The algorithm is from Heiman :footcite:`Heiman2002`, pp.394-7.

    References
    ----------
    .. footbibliography::
    """
    ...

def f_threshold_mway_rm(
    n_subjects, factor_levels, effects: str = "A*B", pvalue: float = 0.05
):
    """### Compute F-value thresholds for a two-way ANOVA.

    ### 🛠️ Parameters
    ----------
    n_subjects : int
        The number of subjects to be analyzed.
    factor_levels : list-like
        The number of levels per factor.
    effects : str
        A string denoting the effect to be returned. The following
        mapping is currently supported:

            * ``'A'``: main effect of A
            * ``'B'``: main effect of B
            * ``'A:B'``: interaction effect
            * ``'A+B'``: both main effects
            * ``'A*B'``: all three effects

    pvalue : float
        The p-value to be thresholded.

    ### ⏎ Returns
    -------
    F_threshold : list | float
        List of F-values for each effect if the number of effects
        requested > 2, else float.

    ### 👉 See Also
    --------
    f_oneway
    f_mway_rm

    ### 📖 Notes
    -----
    ✨ Added in vesion 0.10
    """
    ...

def f_mway_rm(
    data,
    factor_levels,
    effects: str = "all",
    correction: bool = False,
    return_pvals: bool = True,
):
    """### Compute M-way repeated measures ANOVA for fully balanced designs.

    ### 🛠️ Parameters
    ----------
    data : ndarray
        3D array where the first two dimensions are compliant
        with a subjects X conditions scheme where the first
        factor repeats slowest::

                        A1B1 A1B2 A2B1 A2B2
            subject 1   1.34 2.53 0.97 1.74
            subject ... .... .... .... ....
            subject k   2.45 7.90 3.09 4.76

        The last dimensions is thought to carry the observations
        for mass univariate analysis.
    factor_levels : list-like
        The number of levels per factor.
    effects : str | list
        A string denoting the effect to be returned. The following
        mapping is currently supported (example with 2 factors):

            * ``'A'``: main effect of A
            * ``'B'``: main effect of B
            * ``'A:B'``: interaction effect
            * ``'A+B'``: both main effects
            * ``'A*B'``: all three effects
            * ``'all'``: all effects (equals 'A*B' in a 2 way design)

        If list, effect names are used: ``['A', 'B', 'A:B']``.
    correction : bool
        The correction method to be employed if one factor has more than two
        levels. If True, sphericity correction using the Greenhouse-Geisser
        method will be applied.
    return_pvals : bool
        If True, return p-values corresponding to F-values.

    ### ⏎ Returns
    -------
    F_vals : ndarray
        An array of F-statistics with length corresponding to the number
        of effects estimated. The shape depends on the number of effects
        estimated.
    p_vals : ndarray
        If not requested via return_pvals, defaults to an empty array.

    ### 👉 See Also
    --------
    f_oneway
    f_threshold_mway_rm

    ### 📖 Notes
    -----
    ✨ Added in vesion 0.10
    """
    ...
