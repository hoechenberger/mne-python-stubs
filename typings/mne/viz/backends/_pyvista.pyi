import abc
from ...transforms import apply_trans as apply_trans
from ...utils import warn as warn
from ._abstract import Figure3D as Figure3D, _AbstractRenderer
from ._utils import ALLOWED_QUIVER_MODES as ALLOWED_QUIVER_MODES
from _typeshed import Incomplete
from pyvistaqt import BackgroundPlotter

class PyVistaFigure(Figure3D):
    """PyVista-based 3D Figure.

    💡 This class should not be instantiated directly via
              ``mne.viz.PyVistaFigure(...)``. Instead, use
              `mne.viz.create_3d_figure`.

    See Also
    --------
    mne.viz.create_3d_figure
    """

    def __init__(self) -> None: ...

class _Projection:
    """Class storing projection information.

    Attributes
    ----------
    xy : array
        Result of 2d projection of 3d data.
    pts : None
        Scene sensors handle.
    """

    xy: Incomplete
    pts: Incomplete
    plotter: Incomplete

    def __init__(self, *, xy, pts, plotter) -> None:
        """Store input projection information into attributes."""
        ...

    def visible(self, state) -> None:
        """Modify visibility attribute of the sensors."""
        ...

class _PyVistaRenderer(_AbstractRenderer, metaclass=abc.ABCMeta):
    """Class managing rendering scene.

    Attributes
    ----------
    plotter: Plotter
        Main PyVista access point.
    name: str
        Name of the window.
    """

    font_family: str
    tube_n_sides: int
    antialias: Incomplete
    depth_peeling: Incomplete
    multi_samples: Incomplete
    smooth_shading: Incomplete
    figure: Incomplete
    plotter: Incomplete

    def __init__(
        self,
        fig=None,
        size=(600, 600),
        bgcolor: str = "black",
        name: str = "PyVista Scene",
        show: bool = False,
        shape=(1, 1),
        notebook=None,
        smooth_shading: bool = True,
        splash: bool = False,
        multi_samples=None,
    ) -> None: ...
    def subplot(self, x, y) -> None: ...
    def scene(self): ...
    def update_lighting(self) -> None: ...
    def set_interaction(self, interaction) -> None: ...
    def legend(
        self,
        labels,
        border: bool = False,
        size: float = 0.1,
        face: str = "triangle",
        loc: str = "upper left",
    ): ...
    def polydata(
        self,
        mesh,
        color=None,
        opacity: float = 1.0,
        normals=None,
        backface_culling: bool = False,
        scalars=None,
        colormap=None,
        vmin=None,
        vmax=None,
        interpolate_before_map: bool = True,
        representation: str = "surface",
        line_width: float = 1.0,
        polygon_offset=None,
        **kwargs,
    ): ...
    def mesh(
        self,
        x,
        y,
        z,
        triangles,
        color,
        opacity: float = 1.0,
        *,
        backface_culling: bool = False,
        scalars=None,
        colormap=None,
        vmin=None,
        vmax=None,
        interpolate_before_map: bool = True,
        representation: str = "surface",
        line_width: float = 1.0,
        normals=None,
        polygon_offset=None,
        **kwargs,
    ): ...
    def contour(
        self,
        surface,
        scalars,
        contours,
        width: float = 1.0,
        opacity: float = 1.0,
        vmin=None,
        vmax=None,
        colormap=None,
        normalized_colormap: bool = False,
        kind: str = "line",
        color=None,
    ): ...
    def surface(
        self,
        surface,
        color=None,
        opacity: float = 1.0,
        vmin=None,
        vmax=None,
        colormap=None,
        normalized_colormap: bool = False,
        scalars=None,
        backface_culling: bool = False,
        polygon_offset=None,
    ): ...
    def sphere(
        self,
        center,
        color,
        scale,
        opacity: float = 1.0,
        resolution: int = 8,
        backface_culling: bool = False,
        radius=None,
    ): ...
    def tube(
        self,
        origin,
        destination,
        radius: float = 0.001,
        color: str = "white",
        scalars=None,
        vmin=None,
        vmax=None,
        colormap: str = "RdBu",
        normalized_colormap: bool = False,
        reverse_lut: bool = False,
        opacity=None,
    ): ...
    def quiver3d(
        self,
        x,
        y,
        z,
        u,
        v,
        w,
        color,
        scale,
        mode,
        resolution: int = 8,
        glyph_height=None,
        glyph_center=None,
        glyph_resolution=None,
        opacity: float = 1.0,
        scale_mode: str = "none",
        scalars=None,
        colormap=None,
        backface_culling: bool = False,
        line_width: float = 2.0,
        name=None,
        glyph_width=None,
        glyph_depth=None,
        glyph_radius: float = 0.15,
        solid_transform=None,
        *,
        clim=None,
    ): ...
    def text2d(
        self,
        x_window,
        y_window,
        text,
        size: int = 14,
        color: str = "white",
        justification=None,
    ): ...
    def text3d(self, x, y, z, text, scale, color: str = "white"): ...
    def scalarbar(
        self,
        source,
        color: str = "white",
        title=None,
        n_labels: int = 4,
        bgcolor=None,
        **extra_kwargs,
    ): ...
    def show(self) -> None: ...
    def close(self) -> None: ...
    def get_camera(self, *, rigid=None): ...
    def set_camera(
        self,
        azimuth=None,
        elevation=None,
        distance=None,
        focalpoint=None,
        roll=None,
        *,
        rigid=None,
        update: bool = True,
    ) -> None: ...
    def screenshot(self, mode: str = "rgb", filename=None): ...
    def project(self, xyz, ch_names): ...
    def remove_mesh(self, mesh_data) -> None: ...

class _SafeBackgroundPlotter(BackgroundPlotter):
    def __del__(self) -> None:
        """Delete the qt plotter."""
        ...
