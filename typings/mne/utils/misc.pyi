from ._logging import logger as logger, warn as warn
from _typeshed import Incomplete
from collections.abc import Generator

class _DefaultEventParser:
    """### Parse none standard events."""

    event_ids: Incomplete

    def __init__(self) -> None: ...
    def __call__(self, description, offset: int = 1): ...

class _FormatDict(dict):
    """### Help pformat() work properly."""

    def __missing__(self, key): ...

def pformat(temp, **fmt):
    """### Format a template string partially.

    Examples
    --------
    >>> pformat("{a}_{b}", a='x')
    'x_{b}'
    """
    ...

def run_subprocess(command, return_code: bool = False, verbose=None, *args, **kwargs):
    """### Run command using subprocess.Popen.

    Run command and wait for command to complete. If the return code was zero
    then return, otherwise raise CalledProcessError.
    By default, this will also add stdout= and stderr=subproces.PIPE
    to the call to Popen to suppress printing to the terminal.

    ### 🛠️ Parameters
    ----------
    command : list of str | str
        Command to run as subprocess (see subprocess.Popen documentation).
    return_code : bool
        If True, return the return code instead of raising an error if it's
        non-zero.

        ✨ Added in vesion 0.20

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.
    *args, **kwargs : arguments
        Additional arguments to pass to subprocess.Popen.

    ### ⏎ Returns
    -------
    stdout : str
        Stdout returned by the process.
    stderr : str
        Stderr returned by the process.
    code : int
        The return code, only returned if ``return_code == True``.
    """
    ...

def running_subprocess(
    command, after: str = "wait", verbose=None, *args, **kwargs
) -> Generator[Incomplete, None, None]:
    """### Context manager to do something with a command running via Popen.

    ### 🛠️ Parameters
    ----------
    command : list of str | str
        Command to run as subprocess (see `python:subprocess.Popen`).
    after : str
        Can be:

        - "wait" to use `python:subprocess.Popen.wait`
        - "communicate" to use `python.subprocess.Popen.communicate`
        - "terminate" to use `python:subprocess.Popen.terminate`
        - "kill" to use `python:subprocess.Popen.kill`

    %(verbose)s
    *args, **kwargs : arguments
        Additional arguments to pass to subprocess.Popen.

    ### ⏎ Returns
    -------
    p : instance of Popen
        The process.
    """
    ...

def sizeof_fmt(num):
    """### Turn number of bytes into human-readable str.

    ### 🛠️ Parameters
    ----------
    num : int
        The number of bytes.

    ### ⏎ Returns
    -------
    size : str
        The size in human-readable format.
    """
    ...

def repr_html(f):
    """### Decorate _repr_html_ methods.

    If a _repr_html_ method is decorated with this decorator, the repr in a
    notebook will show HTML or plain text depending on the config value
    MNE_REPR_HTML (by default "true", which will render HTML).

    ### 🛠️ Parameters
    ----------
    f : function
        The function to decorate.

    ### ⏎ Returns
    -------
    wrapper : function
        The decorated function.
    """
    ...
