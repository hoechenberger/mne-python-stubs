from .utils import logger as logger
from _typeshed import Incomplete
from collections.abc import Generator

class _Interp2:
    """### Interpolate between two points.

    -----
    ### 🛠️ Parameters

    control_points : array, shape (n_changes,)
        The control points (indices) to use.
    values : callable | array, shape (n_changes, ...)
        Callable that takes the control point and returns a list of
        arrays that must be interpolated.
    interp : str
        Can be 'zero', 'linear', 'hann', or 'cos2' (same as hann).

    -----
    ### 📖 Notes

    This will process data using overlapping windows of potentially
    different sizes to achieve a constant output value using different
    2-point interpolation schemes. For example, for linear interpolation,
    and window sizes of 6 and 17, this would look like::

        1 _     _
          |\\   / '-.           .-'
          | \\ /     '-.     .-'
          |  x         |-.-|
          | / \\     .-'     '-.
          |/   \\_.-'           '-.
        0 +----|----|----|----|---
          0    5   10   15   20   25

    """

    control_points: Incomplete
    values: Incomplete
    n_last: Incomplete

    def __init__(self, control_points, values, interp: str = "hann") -> None: ...
    def feed_generator(self, n_pts) -> Generator[Incomplete, None, None]:
        """### Feed data and get interpolators as a generator."""
        ...
    def feed(self, n_pts):
        """### Feed data and get interpolated values."""
        ...

class _COLA:
    """### Constant overlap-add processing helper.

    -----
    ### 🛠️ Parameters

    process : callable
        A function that takes a chunk of input data with shape
        ``(n_channels, n_samples)`` and processes it.
    store : callable | ndarray
        A function that takes a completed chunk of output data.
        Can also be an ``ndarray``, in which case it is treated as the
        output data in which to store the results.
    n_total : int
        The total number of samples.
    n_samples : int
        The number of samples per window.
    n_overlap : int
        The overlap between windows.
    window : str
        The window to use. Default is "hann".
    tol : float
        The tolerance for COLA checking.

    -----
    ### 📖 Notes

    This will process data using overlapping windows to achieve a constant
    output value. For example, for ``n_total=27``, ``n_samples=10``,
    ``n_overlap=5`` and ``window='triang'``::

        1 _____               _______
          |    \\   /\\   /\\   /
          |     \\ /  \\ /  \\ /
          |      x    x    x
          |     / \\  / \\  / \\
          |    /   \\/   \\/   \\
        0 +----|----|----|----|----|-
          0    5   10   15   20   25

    This produces four windows: the first three are the requested length
    (10 samples) and the last one is longer (12 samples). The first and last
    window are asymmetric.
    """

    starts: Incomplete
    stops: Incomplete

    def __init__(
        self,
        process,
        store,
        n_total,
        n_samples,
        n_overlap,
        sfreq,
        window: str = "hann",
        tol: float = 1e-10,
        *,
        verbose=None,
    ) -> None: ...
    def feed(self, *datas, verbose=None, **kwargs) -> None:
        """### Pass in a chunk of data."""
        ...

class _Storer:
    """### Store data in chunks."""

    outs: Incomplete
    idx: int
    picks: Incomplete

    def __init__(self, *outs, picks=None) -> None: ...
    def __call__(self, *outs) -> None: ...
