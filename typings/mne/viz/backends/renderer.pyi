from ...utils import fill_doc as fill_doc, get_config as get_config, logger as logger
from ..utils import safe_event as safe_event
from ._utils import VALID_3D_BACKENDS as VALID_3D_BACKENDS
from _typeshed import Incomplete
from collections.abc import Generator

MNE_3D_BACKEND: Incomplete
MNE_3D_BACKEND_TESTING: bool
backend: Incomplete

def set_3d_backend(backend_name, verbose=None):
    """Set the 3D backend for MNE.

    The backend will be set as specified and operations will use
    that backend.

    Parameters
    ----------
    backend_name : str
        The 3d backend to select. See Notes for the capabilities of each
        backend (``'pyvistaqt'`` and ``'notebook'``).

        .. versionchanged:: 0.24
           The ``'pyvista'`` backend was renamed ``'pyvistaqt'``.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    old_backend_name : str | None
        The old backend that was in use.

    Notes
    -----
    To use PyVista, set ``backend_name`` to ``pyvistaqt`` but the value
    ``pyvista`` is still supported for backward compatibility.

    This table shows the capabilities of each backend ("✓" for full support,
    and "-" for partial support):

    .. table::
       :widths: auto

       +--------------------------------------+-----------+----------+
       | **3D function:**                     | pyvistaqt | notebook |
       +======================================+===========+==========+
       | :func:`plot_vector_source_estimates` | ✓         | ✓        |
       +--------------------------------------+-----------+----------+
       | :func:`plot_source_estimates`        | ✓         | ✓        |
       +--------------------------------------+-----------+----------+
       | :func:`plot_alignment`               | ✓         | ✓        |
       +--------------------------------------+-----------+----------+
       | :func:`plot_sparse_source_estimates` | ✓         | ✓        |
       +--------------------------------------+-----------+----------+
       | :func:`plot_evoked_field`            | ✓         | ✓        |
       +--------------------------------------+-----------+----------+
       | :func:`snapshot_brain_montage`       | ✓         | ✓        |
       +--------------------------------------+-----------+----------+
       | :func:`link_brains`                  | ✓         |          |
       +--------------------------------------+-----------+----------+
       +--------------------------------------+-----------+----------+
       | **Feature:**                                                |
       +--------------------------------------+-----------+----------+
       | Large data                           | ✓         | ✓        |
       +--------------------------------------+-----------+----------+
       | Opacity/transparency                 | ✓         | ✓        |
       +--------------------------------------+-----------+----------+
       | Support geometric glyph              | ✓         | ✓        |
       +--------------------------------------+-----------+----------+
       | Smooth shading                       | ✓         | ✓        |
       +--------------------------------------+-----------+----------+
       | Subplotting                          | ✓         | ✓        |
       +--------------------------------------+-----------+----------+
       | Inline plot in Jupyter Notebook      |           | ✓        |
       +--------------------------------------+-----------+----------+
       | Inline plot in JupyterLab            |           | ✓        |
       +--------------------------------------+-----------+----------+
       | Inline plot in Google Colab          |           |          |
       +--------------------------------------+-----------+----------+
       | Toolbar                              | ✓         | ✓        |
       +--------------------------------------+-----------+----------+
    """

def get_3d_backend():
    """Return the 3D backend currently used.

    Returns
    -------
    backend_used : str | None
        The 3d backend currently in use. If no backend is found,
        returns ``None``.

        .. versionchanged:: 0.24
           The ``'pyvista'`` backend has been renamed ``'pyvistaqt'``, so
           ``'pyvista'`` is no longer returned by this function.
    """

def use_3d_backend(backend_name) -> Generator[None, None, None]:
    """Create a 3d visualization context using the designated backend.

    See :func:`mne.viz.set_3d_backend` for more details on the available
    3d backends and their capabilities.

    Parameters
    ----------
    backend_name : {'pyvistaqt', 'notebook'}
        The 3d backend to use in the context.
    """

def set_3d_view(
    figure,
    azimuth=None,
    elevation=None,
    focalpoint=None,
    distance=None,
    roll=None,
    *,
    reset_camera=None,
) -> None:
    """Configure the view of the given scene.

    Parameters
    ----------
    figure : object
        The scene which is modified.

    azimuth : float
        The azimuthal angle of the camera rendering the view in degrees.

    elevation : float
        The The zenith angle of the camera rendering the view in degrees.

    focalpoint : tuple, shape (3,) | str | None
        The focal point of the camera rendering the view: (x, y, z) in
        plot units (either m or mm). When ``"auto"``, it is set to the center of
        mass of the visible bounds.

    distance : float | "auto" | None
        The distance from the camera rendering the view to the focalpoint
        in plot units (either m or mm). If "auto", the bounds of visible objects will be
        used to set a reasonable distance.

        .. versionchanged:: 1.6
           ``None`` will no longer change the distance, use ``"auto"`` instead.

    roll : float | None
        The roll of the camera rendering the view in degrees.
    reset_camera : bool
       Deprecated, use ``distance="auto"`` instead.
    """

def set_3d_title(figure, title, size: int = 40) -> None:
    """Configure the title of the given scene.

    Parameters
    ----------
    figure : object
        The scene which is modified.
    title : str
        The title of the scene.
    size : int
        The size of the title.
    """

def create_3d_figure(
    size,
    bgcolor=(0, 0, 0),
    smooth_shading=None,
    handle=None,
    *,
    scene: bool = True,
    show: bool = False,
):
    """Return an empty figure based on the current 3d backend.

    .. warning:: Proceed with caution when the renderer object is
                 returned (with ``scene=False``) because the _Renderer
                 API is not necessarily stable enough for production,
                 it's still actively in development.

    Parameters
    ----------
    size : tuple
        The dimensions of the 3d figure (width, height).
    bgcolor : tuple
        The color of the background.
    smooth_shading : bool | None
        Whether to enable smooth shading. If ``None``, uses the config value
        ``MNE_3D_OPTION_SMOOTH_SHADING``. Defaults to ``None``.
    handle : int | None
        The figure identifier.
    scene : bool
        If True (default), the returned object is the Figure3D. If False,
        an advanced, undocumented Renderer object is returned (the API is not
        stable or documented, so this is not recommended).
    show : bool
        If True, show the renderer immediately.

        .. versionadded:: 1.0

    Returns
    -------
    figure : instance of Figure3D or ``Renderer``
        The requested empty figure or renderer, depending on ``scene``.
    """

def close_3d_figure(figure) -> None:
    """Close the given scene.

    Parameters
    ----------
    figure : object
        The scene which needs to be closed.
    """

def close_all_3d_figures() -> None:
    """Close all the scenes of the current 3d backend."""

def get_brain_class():
    """Return the proper Brain class based on the current 3d backend.

    Returns
    -------
    brain : object
        The Brain class corresponding to the current 3d backend.
    """

class _TimeInteraction:
    """Mixin enabling time interaction controls."""
