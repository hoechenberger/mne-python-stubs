from ..source_estimate import SourceEstimate as SourceEstimate
from ..utils import logger as logger

def resolution_metrics(
    resmat,
    src,
    function: str = "psf",
    metric: str = "peak_err",
    threshold: float = 0.5,
    verbose=None,
):
    """### Compute spatial resolution metrics for linear solvers.

    -----
    ### 🛠️ Parameters

    resmat : array, shape (n_orient * n_vertices, n_vertices)
        The resolution matrix.
        If not a square matrix and if the number of rows is a multiple of
        number of columns (e.g. free or loose orientations), then the Euclidean
        length per source location is computed (e.g. if inverse operator with
        free orientations was applied to forward solution with fixed
        orientations).
    src : instance of SourceSpaces
        Source space object from forward or inverse operator.
    function : 'psf' | 'ctf'
        Whether to compute metrics for columns (point-spread functions, PSFs)
        or rows (cross-talk functions, CTFs) of the resolution matrix.
    metric : str
        The resolution metric to compute. Allowed options are:

        Localization-based metrics:

        - ``'peak_err'`` Peak localization error (PLE), Euclidean distance
          between peak and true source location.
        - ``'cog_err'`` Centre-of-gravity localisation error (CoG), Euclidean
          distance between CoG and true source location.

        Spatial-extent-based metrics:

        - ``'sd_ext'`` Spatial deviation
          (e.g. :footcite:`MolinsEtAl2008,HaukEtAl2019`).
        - ``'maxrad_ext'`` Maximum radius to 50% of max amplitude.

        Amplitude-based metrics:

        - ``'peak_amp'`` Ratio between absolute maximum amplitudes of peaks
          per location and maximum peak across locations.
        - ``'sum_amp'`` Ratio between sums of absolute amplitudes.

    threshold : float
        Amplitude fraction threshold for spatial extent metric 'maxrad_ext'.
        Defaults to 0.5.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    resolution_metric : instance of SourceEstimate
        The resolution metric.

    -----
    ### 📖 Notes

    For details, see :footcite:`MolinsEtAl2008,HaukEtAl2019`.

    ✨ Added in vesion 0.20

    References
    ----------
    .. footbibliography::
    """
    ...
