from .utils import logger as logger, verbose as verbose
from _typeshed import Incomplete
from collections.abc import Generator

class _Interp2:
    """Feed data and get interpolated values."""
    control_points: Incomplete
    values: Incomplete
    n_last: Incomplete

    def __init__(self, control_points, values, interp: str=...) -> None:
        ...

    def feed_generator(self, n_pts) -> Generator[Incomplete, None, None]:
        """Feed data and get interpolators as a generator."""

    def feed(self, n_pts):
        """Feed data and get interpolated values."""

class _COLA:
    """Pass in a chunk of data."""
    starts: Incomplete
    stops: Incomplete

    def __init__(self, process, store, n_total, n_samples, n_overlap, sfreq, window: str=..., tol: float=..., *, verbose: Incomplete | None=...) -> None:
        ...

    def feed(self, *datas, verbose: Incomplete | None=..., **kwargs) -> None:
        """Pass in a chunk of data."""

class _Storer:
    """Store data in chunks."""
    outs: Incomplete
    idx: int
    picks: Incomplete

    def __init__(self, *outs, picks: Incomplete | None=...) -> None:
        ...

    def __call__(self, *outs) -> None:
        ...