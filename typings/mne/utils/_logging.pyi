import logging
from .docs import fill_doc as fill_doc
from _typeshed import Incomplete
from collections.abc import Generator
from io import StringIO

logger: Incomplete

class _FrameFilter(logging.Filter):
    add_frames: int

    def __init__(self) -> None: ...
    def filter(self, record): ...

def verbose(function: _FuncT) -> _FuncT:
    """### Verbose decorator to allow functions to override log-level.

    ### 🛠️ Parameters
    ----------
    function : callable
        Function to be decorated by setting the verbosity level.

    ### ⏎ Returns
    -------
    dec : callable
        The decorated function.

    ### 👉 See Also
    --------
    set_log_level
    set_config

    ### 📖 Notes
    -----
    This decorator is used to set the verbose level during a function or method
    call, such as `mne.compute_covariance`. The `verbose` keyword
    argument can be 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL', True (an
    alias for 'INFO'), or False (an alias for 'WARNING'). To set the global
    verbosity level for all functions, use `mne.set_log_level`.

    This function also serves as a docstring filler.

    Examples
    --------
    You can use the ``verbose`` argument to set the verbose level on the fly::

        >>> import mne
        >>> cov = mne.compute_raw_covariance(raw, verbose='WARNING')  # doctest: +SKIP
        >>> cov = mne.compute_raw_covariance(raw, verbose='INFO')  # doctest: +SKIP
        Using up to 49 segments
        Number of samples used : 5880
        [done]
    """
    ...

class use_log_level:
    """### Context manager for logging level.

    ### 🛠️ Parameters
    ----------

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    add_frames : int | None
        If int, enable (>=1) or disable (0) the printing of stack frame
        information using formatting. Default (None) does not change the
        formatting. This can add overhead so is meant only for debugging.

    ### 👉 See Also
    --------
    mne.verbose

    ### 📖 Notes
    -----
    See the `logging documentation <tut-logging>` for details.

    Examples
    --------
    >>> from mne import use_log_level
    >>> from mne.utils import logger
    >>> with use_log_level(False):
    ...     # Most MNE logger messages are "info" level, False makes them not
    ...     # print:
    ...     logger.info('This message will not be printed')
    >>> with use_log_level(True):
    ...     # Using verbose=True in functions, methods, or this context manager
    ...     # will ensure they are printed
    ...     logger.info('This message will be printed!')
    This message will be printed!
    """

    def __init__(self, verbose=None, *, add_frames=None) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args) -> None: ...

def set_log_level(verbose=None, return_old_level: bool = False, add_frames=None):
    """### Set the logging level.

    ### 🛠️ Parameters
    ----------
    verbose : bool, str, int, or None
        The verbosity of messages to print. If a str, it can be either DEBUG,
        INFO, WARNING, ERROR, or CRITICAL. Note that these are for
        convenience and are equivalent to passing in logging.DEBUG, etc.
        For bool, True is the same as 'INFO', False is the same as 'WARNING'.
        If None, the environment variable MNE_LOGGING_LEVEL is read, and if
        it doesn't exist, defaults to INFO.
    return_old_level : bool
        If True, return the old verbosity level.

    add_frames : int | None
        If int, enable (>=1) or disable (0) the printing of stack frame
        information using formatting. Default (None) does not change the
        formatting. This can add overhead so is meant only for debugging.

    ### ⏎ Returns
    -------
    old_level : int
        The old level. Only returned if ``return_old_level`` is True.
    """
    ...

def set_log_file(
    fname=None, output_format: str = "%(message)s", overwrite=None
) -> None:
    """### Set the log to print to a file.

    ### 🛠️ Parameters
    ----------
    fname : path-like | None
        Filename of the log to print to. If None, stdout is used.
        To suppress log outputs, use set_log_level('WARNING').
    output_format : str
        Format of the output messages. See the following for examples:

            https://docs.python.org/dev/howto/logging.html

        e.g., "%(asctime)s - %(levelname)s - %(message)s".
    overwrite : bool | None
        Overwrite the log file (if it exists). Otherwise, statements
        will be appended to the log (default). None is the same as False,
        but additionally raises a warning to notify the user that log
        entries will be appended.
    """
    ...

class ClosingStringIO(StringIO):
    """### StringIO that closes after getvalue()."""

    def getvalue(self, close: bool = True):
        """### Get the value."""
        ...

class catch_logging:
    """### Store logging.

    This will remove all other logging handlers, and return the handler to
    stdout when complete.
    """

    verbose: Incomplete

    def __init__(self, verbose=None) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...

class WrapStdOut:
    """### Dynamically wrap to sys.stdout.

    This makes packages that monkey-patch sys.stdout (e.g.doctest,
    sphinx-gallery) work properly.
    """

    def __getattr__(self, name): ...

def warn(
    message, category=..., module: str = "mne", ignore_namespaces=("mne",)
) -> None:
    """### Emit a warning with trace outside the mne namespace.

    This function takes arguments like warnings.warn, and sends messages
    using both ``warnings.warn`` and ``logger.warn``. Warnings can be
    generated deep within nested function calls. In order to provide a
    more helpful warning, this function traverses the stack until it
    reaches a frame outside the ``mne`` namespace that caused the error.

    ### 🛠️ Parameters
    ----------
    message : str
        Warning message.
    category : instance of Warning
        The warning class. Defaults to ``RuntimeWarning``.
    module : str
        The name of the module emitting the warning.
    ignore_namespaces : list of str
        Namespaces to ignore when traversing the stack.

        ✨ Added in vesion 0.24
    """
    ...

def filter_out_warnings(warn_record, category=None, match=None) -> None:
    """### Remove particular records from ``warn_record``.

    This helper takes a list of `warnings.WarningMessage` objects,
    and remove those matching category and/or text.

    ### 🛠️ Parameters
    ----------
    category: WarningMessage type | None
       class of the message to filter out

    match : str | None
        text or regex that matches the error message to filter out
    """
    ...

def wrapped_stdout(
    indent: str = "", cull_newlines: bool = False
) -> Generator[None, None, None]:
    """### Wrap stdout writes to logger.info, with an optional indent prefix.

    ### 🛠️ Parameters
    ----------
    indent : str
        The indentation to add.
    cull_newlines : bool
        If True, cull any new/blank lines at the end.
    """
    ...
