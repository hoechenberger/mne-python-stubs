from ._logging import logger as logger
from .config import get_config as get_config
from _typeshed import Incomplete
from threading import Thread

class ProgressBar:
    """## 🧠 Generate a command-line progressbar.

    -----
    ### 🛠️ Parameters

    #### `iterable : iterable | int | None`
        The iterable to use. Can also be an int for backward compatibility
        (acts like ``max_value``).
    #### `initial_value : int`
        Initial value of process, useful when resuming process from a specific
        value, defaults to 0.
    #### `mesg : str`
        Message to include at end of progress bar.
    #### `max_total_width : int | str`
        Maximum total message width. Can use "auto" (default) to try to set
        a sane value based on the current terminal width.
    #### `max_value : int | None`
        The max value. If None, the length of ``iterable`` will be used.
    #### `which_tqdm : str | None`
        Which tqdm module to use. Can be "tqdm", "tqdm.notebook", or "off".
        Defaults to ``None``, which uses the value of the MNE_TQDM environment
        variable, or ``"tqdm.auto"`` if that is not set.
    **kwargs : dict
        Additional keyword arguments for tqdm.
    """

    iterable: Incomplete
    max_value: Incomplete

    def __init__(
        self,
        iterable=None,
        initial_value: int = 0,
        mesg=None,
        max_total_width: str = "auto",
        max_value=None,
        *,
        which_tqdm=None,
        **kwargs,
    ) -> None: ...
    def update(self, cur_value) -> None:
        """### Update progressbar with current value of process.

        -----
        ### 🛠️ Parameters

        #### `cur_value : number`
            Current value of process.  Should be <= max_value (but this is not
            enforced).  The percent of the progressbar will be computed as
            ``(cur_value / max_value) * 100``.
        """
        ...
    def update_with_increment_value(self, increment_value) -> None:
        """### Update progressbar with an increment.

        -----
        ### 🛠️ Parameters

        #### `increment_value : int`
            Value of the increment of process.  The percent of the progressbar
            will be computed as
            ``(self.cur_value + increment_value / max_value) * 100``.
        """
        ...
    def __iter__(self):
        """### Iterate to auto-increment the pbar with 1."""
        ...
    def subset(self, idx):
        """### Make a joblib-friendly index subset updater.

        -----
        ### 🛠️ Parameters

        #### `idx : ndarray`
            List of indices for this subset.

        -----
        ### ⏎ Returns

        #### `updater : instance of PBSubsetUpdater`
            Class with a ``.update(ii)`` method.
        """
        ...
    def __enter__(self): ...
    def __exit__(
        self,
        type_: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
    def __del__(self) -> None:
        """### Ensure output completes."""
        ...

class _UpdateThread(Thread):
    def __init__(self, pb) -> None: ...
    def run(self) -> None: ...

class _PBSubsetUpdater:
    mmap: Incomplete
    idx: Incomplete

    def __init__(self, pb, idx) -> None: ...
    def update(self, ii) -> None: ...
