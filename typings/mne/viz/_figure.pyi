import abc
from ..utils import get_config as get_config, logger as logger, set_config as set_config
from .backends._utils import VALID_BROWSE_BACKENDS as VALID_BROWSE_BACKENDS
from _typeshed import Incomplete
from abc import ABC
from collections.abc import Generator

MNE_BROWSER_BACKEND: Incomplete
backend: Incomplete

class BrowserParams:
    """Container object for 2D browser parameters."""

    close_key: str

    def __init__(self, **kwargs) -> None: ...

class BrowserBase(ABC, metaclass=abc.ABCMeta):
    """A base class containing for the 2D browser.

    This class contains all backend-independent attributes and methods.
    """

    backend_name: Incomplete
    mne: Incomplete

    def __init__(self, **kwargs) -> None: ...
    def fake_keypress(self, key, fig=None):
        """Pass a fake keypress to the figure.

        Parameters
        ----------
        key : str
            The key to fake (e.g., ``'a'``).
        fig : instance of Figure
            The figure to pass the keypress to.
        """
        ...

def set_browser_backend(backend_name, verbose=None):
    """Set the 2D browser backend for MNE.

    The backend will be set as specified and operations will use
    that backend.

    Parameters
    ----------
    backend_name : str
        The 2D browser backend to select. See Notes for the capabilities
        of each backend (``'qt'``, ``'matplotlib'``). The ``'qt'`` browser
        requires `mne-qt-browser
        <https://github.com/mne-tools/mne-qt-browser>`__.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    old_backend_name : str | None
        The old backend that was in use.

    Notes
    -----
    This table shows the capabilities of each backend ("✓" for full support,
    and "-" for partial support):

    .. table::
       :widths: auto

       +--------------------------------------+------------+----+
       | **2D browser function:**             | matplotlib | qt |
       +======================================+============+====+
       | `plot_raw`                     | ✓          | ✓  |
       +--------------------------------------+------------+----+
       | `plot_epochs`                  | ✓          | ✓  |
       +--------------------------------------+------------+----+
       | `plot_ica_sources`             | ✓          | ✓  |
       +--------------------------------------+------------+----+
       +--------------------------------------+------------+----+
       | **Feature:**                                           |
       +--------------------------------------+------------+----+
       | Show Events                          | ✓          | ✓  |
       +--------------------------------------+------------+----+
       | Add/Edit/Remove Annotations          | ✓          | ✓  |
       +--------------------------------------+------------+----+
       | Toggle Projections                   | ✓          | ✓  |
       +--------------------------------------+------------+----+
       | Butterfly Mode                       | ✓          | ✓  |
       +--------------------------------------+------------+----+
       | Selection Mode                       | ✓          | ✓  |
       +--------------------------------------+------------+----+
       | Smooth Scrolling                     |            | ✓  |
       +--------------------------------------+------------+----+
       | Overview-Bar (with Z-Score-Mode)     |            | ✓  |
       +--------------------------------------+------------+----+

    ✨ Added in version 0.24
    """
    ...

def get_browser_backend():
    """Return the 2D backend currently used.

    Returns
    -------
    backend_used : str | None
        The 2D browser backend currently in use. If no backend is found,
        returns ``None``.
    """
    ...

def use_browser_backend(backend_name) -> Generator[Incomplete, None, None]:
    """Create a 2D browser visualization context using the designated backend.

    See `mne.viz.set_browser_backend` for more details on the available
    2D browser backends and their capabilities.

    Parameters
    ----------
    backend_name : {'qt', 'matplotlib'}
        The 2D browser backend to use in the context.
    """
    ...
