from .utils import (
    ProgressBar as ProgressBar,
    get_config as get_config,
    logger as logger,
    use_log_level as use_log_level,
    warn as warn,
)

def parallel_func(
    func,
    n_jobs,
    max_nbytes: str = "auto",
    pre_dispatch: str = "n_jobs",
    total=None,
    prefer=None,
    *,
    max_jobs=None,
    verbose=None,
):
    """Return parallel instance with delayed function.

    Util function to use joblib only if available

    Parameters
    ----------
    func : callable
        A function.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the :mod:`joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a :class:`joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.
    max_nbytes : int | str | None
        Threshold on the minimum size of arrays passed to the workers that
        triggers automated memory mapping. Can be an int in Bytes,
        or a human-readable string, e.g., '1M' for 1 megabyte.
        Use None to disable memmaping of large arrays. Use 'auto' to
        use the value set using :func:`mne.set_memmap_min_size`.
    pre_dispatch : int | str
        See :class:`joblib.Parallel`.
    total : int | None
        If int, use a progress bar to display the progress of dispatched
        jobs. This should only be used when directly iterating, not when
        using ``split_list`` or :func:`np.array_split`.
        If None (default), do not add a progress bar.
    prefer : str | None
        If str, can be ``"processes"`` or ``"threads"``.
        See :class:`joblib.Parallel`.

        .. versionadded:: 0.18
    max_jobs : int | None
        The upper limit of jobs to use. This is useful when you know ahead
        of a the maximum number of calls into :class:`joblib.Parallel` that
        you will possibly want or need, and the returned ``n_jobs`` should not
        exceed this value regardless of how many jobs the user requests.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument. INFO or DEBUG
        will print parallel status, others will not.

    Returns
    -------
    parallel: instance of joblib.Parallel or list
        The parallel object.
    my_func: callable
        ``func`` if not parallel or delayed(func).
    n_jobs: int
        Number of jobs >= 1.
    """
