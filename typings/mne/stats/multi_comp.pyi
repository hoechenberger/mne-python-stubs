def fdr_correction(pvals, alpha: float = 0.05, method: str = "indep"):
    """## P-value correction with False Discovery Rate (FDR).

    Correction for multiple comparison using FDR :footcite:`GenoveseEtAl2002`.

    This covers Benjamini/Hochberg for independent or positively correlated and
    Benjamini/Yekutieli for general or negatively correlated tests.

    -----
    ### 🛠️ Parameters

    #### `pvals : array_like`
        Set of p-values of the individual tests.
    #### `alpha : float`
        Error rate.
    #### `method : 'indep' | 'negcorr'`
        If 'indep' it implements Benjamini/Hochberg for independent or if
        'negcorr' it corresponds to Benjamini/Yekutieli.

    -----
    ### ⏎ Returns

    #### `reject : array, bool`
        True if a hypothesis is rejected, False if not.
    #### `pval_corrected : array`
        P-values adjusted for multiple hypothesis testing to limit FDR.

    References
    ----------
    .. footbibliography::
    """
    ...

def bonferroni_correction(pval, alpha: float = 0.05):
    """## P-value correction with Bonferroni method.

    -----
    ### 🛠️ Parameters

    #### `pval : array_like`
        Set of p-values of the individual tests.
    #### `alpha : float`
        Error rate.

    -----
    ### ⏎ Returns

    #### `reject : array, bool`
        True if a hypothesis is rejected, False if not.
    #### `pval_corrected : array`
        P-values adjusted for multiple hypothesis testing to limit FDR.
    """
    ...
