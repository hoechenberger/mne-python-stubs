def ctps(data, is_raw: bool = True):
    """### Compute cross-trial-phase-statistics [1].

    Note. It is assumed that the sources are already
    appropriately filtered

    -----
    ### 🛠️ Parameters

    data: ndarray, shape (n_epochs, n_channels, n_times)
        Any kind of data of dimensions trials, traces, features.
    is_raw : bool
        If True it is assumed that data haven't been transformed to Hilbert
        space and phase angles haven't been normalized. Defaults to True.

    -----
    ### ⏎ Returns

    ks_dynamics : ndarray, shape (n_sources, n_times)
        The kuiper statistics.
    pk_dynamics : ndarray, shape (n_sources, n_times)
        The normalized kuiper index for ICA sources and
        time slices.
    phase_angles : ndarray, shape (n_epochs, n_sources, n_times) | None
        The phase values for epochs, sources and time slices. If ``is_raw``
        is False, None is returned.

    References
    ----------
    [1] Dammers, J., Schiek, M., Boers, F., Silex, C., Zvyagintsev,
        M., Pietrzyk, U., Mathiak, K., 2008. Integration of amplitude
        and phase statistics for complete artifact removal in independent
        components of neuromagnetic recordings. Biomedical
        Engineering, IEEE Transactions on 55 (10), 2353-2362.
    """
    ...

def kuiper(data, dtype=...):
    """### Kuiper's test of uniform distribution.

    -----
    ### 🛠️ Parameters

    data : ndarray, shape (n_sources,) | (n_sources, n_times)
           Empirical distribution.
    dtype : str | obj
        The data type to be used.

    -----
    ### ⏎ Returns

    ks : ndarray
        Kuiper's statistic.
    pk : ndarray
        Normalized probability of Kuiper's statistic [0, 1].
    """
    ...
