from .utils import (
    fill_doc as fill_doc,
    get_config as get_config,
    logger as logger,
    sizeof_fmt as sizeof_fmt,
    warn as warn,
)

def get_cuda_memory(kind: str = "available"):
    """Get the amount of free memory for CUDA operations.

    Parameters
    ----------
    kind : str
        Can be ``"available"`` or ``"total"``.

    Returns
    -------
    memory : str
        The amount of available or total memory as a human-readable string.
    """

def init_cuda(ignore_config: bool = False, verbose=None) -> None:
    """Initialize CUDA functionality.

    This function attempts to load the necessary interfaces
    (hardware connectivity) to run CUDA-based filtering. This
    function should only need to be run once per session.

    If the config var (set via mne.set_config or in ENV)
    MNE_USE_CUDA == 'true', this function will be executed when
    the first CUDA setup is performed. If this variable is not
    set, this function can be manually executed.

    Parameters
    ----------
    ignore_config : bool
        If True, ignore the config value MNE_USE_CUDA and force init.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.
    """

def set_cuda_device(device_id, verbose=None) -> None:
    """Set the CUDA device temporarily for the current session.

    Parameters
    ----------
    device_id : int
        Numeric ID of the CUDA-capable device you want MNE-Python to use.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.
    """
