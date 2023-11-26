import abc
from ..ui_events import TimeChange as TimeChange, publish as publish
from _typeshed import Incomplete
from abc import ABC, abstractmethod

class Figure3D(ABC):
    """### Class that refers to a 3D figure.

    ### 💡 Note
        This class should not be instantiated directly via
        ``mne.viz.Figure3D(...)``. Instead, use
        `mne.viz.create_3d_figure`.

    ### 👉 See Also
    --------
    mne.viz.create_3d_figure
    """

    @property
    def plotter(self):
        """### The native 3D plotting widget.

        ### ⏎ Returns
        -------
        plotter : instance of pyvista.Plotter
            The plotter. Useful for interacting with the native 3D library.
        """
        ...

class _AbstractRenderer(ABC, metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def __init__(
        self,
        fig=None,
        size=(600, 600),
        bgcolor=(0.0, 0.0, 0.0),
        name=None,
        show: bool = False,
        shape=(1, 1),
        splash: bool = False,
    ):
        """### Set up the scene."""
        ...
    @classmethod
    @abc.abstractmethod
    def subplot(self, x, y):
        """### Set the active subplot."""
        ...
    @classmethod
    @abc.abstractmethod
    def scene(self):
        """### Return scene handle."""
        ...
    @classmethod
    @abc.abstractmethod
    def set_interaction(self, interaction):
        """### Set interaction mode."""
        ...
    @classmethod
    @abc.abstractmethod
    def legend(
        self,
        labels,
        border: bool = False,
        size: float = 0.1,
        face: str = "triangle",
        loc: str = "upper left",
    ):
        """### Add a legend to the scene.

        ### 🛠️ Parameters
        ----------
        labels : list of tuples
            Each entry must contain two strings, (label, color),
            where ``label`` is the name of the item to add, and
            ``color`` is the color of the label to add.
        border : bool
            Controls if there will be a border around the legend.
            The default is False.
        size : float
            The size of the entire figure window.
        loc : str
            The location of the legend.
        face : str
            Face shape of legend face.  One of the following:

            * None: ``None``
            * Line: ``"-"`` or ``"line"``
            * Triangle: ``"^"`` or ``'triangle'``
            * Circle: ``"o"`` or ``'circle'``
            * Rectangle: ``"r"`` or ``'rectangle'``
        """
        ...
    @classmethod
    @abc.abstractmethod
    def mesh(
        self,
        x,
        y,
        z,
        triangles,
        color,
        opacity: float = 1.0,
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
    ):
        """### Add a mesh in the scene.

        ### 🛠️ Parameters
        ----------
        x : array, shape (n_vertices,)
           The array containing the X component of the vertices.
        y : array, shape (n_vertices,)
           The array containing the Y component of the vertices.
        z : array, shape (n_vertices,)
           The array containing the Z component of the vertices.
        triangles : array, shape (n_polygons, 3)
           The array containing the indices of the polygons.
        color : tuple | str
            The color of the mesh as a tuple (red, green, blue) of float
            values between 0 and 1 or a valid color name (i.e. 'white'
            or 'w').
        opacity : float
            The opacity of the mesh.
        shading : bool
            If True, enable the mesh shading.
        backface_culling : bool
            If True, enable backface culling on the mesh.
        scalars : ndarray, shape (n_vertices,)
            The scalar valued associated to the vertices.
        vmin : float | None
            vmin is used to scale the colormap.
            If None, the min of the data will be used
        vmax : float | None
            vmax is used to scale the colormap.
            If None, the max of the data will be used
        colormap :
            The colormap to use.
        interpolate_before_map :
            Enabling makes for a smoother scalars display. Default is True.
            When False, OpenGL will interpolate the mapped colors which can
            result is showing colors that are not present in the color map.
        representation : str
            The representation of the mesh: either 'surface' or 'wireframe'.
        line_width : int
            The width of the lines when representation='wireframe'.
        normals : array, shape (n_vertices, 3)
            The array containing the normal of each vertex.
        polygon_offset : float
            If not None, the factor used to resolve coincident topology.
        kwargs : args
            The arguments to pass to triangular_mesh

        ### ⏎ Returns
        -------
        surface :
            Handle of the mesh in the scene.
        """
        ...
    @classmethod
    @abc.abstractmethod
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
    ):
        """### Add a contour in the scene.

        ### 🛠️ Parameters
        ----------
        surface : surface object
            The mesh to use as support for contour.
        scalars : ndarray, shape (n_vertices,)
            The scalar valued associated to the vertices.
        contours : int | list
             Specifying a list of values will only give the requested contours.
        width : float
            The width of the lines or radius of the tubes.
        opacity : float
            The opacity of the contour.
        vmin : float | None
            vmin is used to scale the colormap.
            If None, the min of the data will be used
        vmax : float | None
            vmax is used to scale the colormap.
            If None, the max of the data will be used
        colormap :
            The colormap to use.
        normalized_colormap : bool
            Specify if the values of the colormap are between 0 and 1.
        kind : 'line' | 'tube'
            The type of the primitives to use to display the contours.
        color :
            The color of the mesh as a tuple (red, green, blue) of float
            values between 0 and 1 or a valid color name (i.e. 'white'
            or 'w').
        """
        ...
    @classmethod
    @abc.abstractmethod
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
    ):
        """### Add a surface in the scene.

        ### 🛠️ Parameters
        ----------
        surface : surface object
            The information describing the surface.
        color : tuple | str
            The color of the surface as a tuple (red, green, blue) of float
            values between 0 and 1 or a valid color name (i.e. 'white'
            or 'w').
        opacity : float
            The opacity of the surface.
        vmin : float | None
            vmin is used to scale the colormap.
            If None, the min of the data will be used
        vmax : float | None
            vmax is used to scale the colormap.
            If None, the max of the data will be used
        colormap :
            The colormap to use.
        scalars : ndarray, shape (n_vertices,)
            The scalar valued associated to the vertices.
        backface_culling : bool
            If True, enable backface culling on the surface.
        polygon_offset : float
            If not None, the factor used to resolve coincident topology.
        """
        ...
    @classmethod
    @abc.abstractmethod
    def sphere(
        self,
        center,
        color,
        scale,
        opacity: float = 1.0,
        resolution: int = 8,
        backface_culling: bool = False,
        radius=None,
    ):
        """### Add sphere in the scene.

        ### 🛠️ Parameters
        ----------
        center : ndarray, shape(n_center, 3)
            The list of centers to use for the sphere(s).
        color : tuple | str
            The color of the sphere as a tuple (red, green, blue) of float
            values between 0 and 1 or a valid color name (i.e. 'white'
            or 'w').
        scale : float
            The scaling applied to the spheres. The given value specifies
            the maximum size in drawing units.
        opacity : float
            The opacity of the sphere(s).
        resolution : int
            The resolution of the sphere created. This is the number
            of divisions along theta and phi.
        backface_culling : bool
            If True, enable backface culling on the sphere(s).
        radius : float | None
            Replace the glyph scaling by a fixed radius value for each
            sphere.
        """
        ...
    @classmethod
    @abc.abstractmethod
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
    ):
        """### Add tube in the scene.

        ### 🛠️ Parameters
        ----------
        origin : array, shape(n_lines, 3)
            The coordinates of the first end of the tube(s).
        destination : array, shape(n_lines, 3)
            The coordinates of the other end of the tube(s).
        radius : float
            The radius of the tube(s).
        color : tuple | str
            The color of the tube as a tuple (red, green, blue) of float
            values between 0 and 1 or a valid color name (i.e. 'white'
            or 'w').
        scalars : array, shape (n_quivers,) | None
            The optional scalar data to use.
        vmin : float | None
            vmin is used to scale the colormap.
            If None, the min of the data will be used
        vmax : float | None
            vmax is used to scale the colormap.
            If None, the max of the data will be used
        colormap :
            The colormap to use.
        opacity : float
            The opacity of the tube(s).
        backface_culling : bool
            If True, enable backface culling on the tube(s).
        reverse_lut : bool
            If True, reverse the lookup table.

        ### ⏎ Returns
        -------
        actor :
            The actor in the scene.
        surface :
            Handle of the tube in the scene.
        """
        ...
    @classmethod
    @abc.abstractmethod
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
        backface_culling: bool = False,
        colormap=None,
        vmin=None,
        vmax=None,
        line_width: float = 2.0,
        name=None,
    ):
        """### Add quiver3d in the scene.

        ### 🛠️ Parameters
        ----------
        x : array, shape (n_quivers,)
            The X component of the position of the quiver.
        y : array, shape (n_quivers,)
            The Y component of the position of the quiver.
        z : array, shape (n_quivers,)
            The Z component of the position of the quiver.
        u : array, shape (n_quivers,)
            The last X component of the quiver.
        v : array, shape (n_quivers,)
            The last Y component of the quiver.
        w : array, shape (n_quivers,)
            The last Z component of the quiver.
        color : tuple | str
            The color of the quiver as a tuple (red, green, blue) of float
            values between 0 and 1 or a valid color name (i.e. 'white'
            or 'w').
        scale : float
            The scaling applied to the glyphs. The size of the glyph
            is by default calculated from the inter-glyph spacing.
            The given value specifies the maximum glyph size in drawing units.
        mode : 'arrow', 'cone' or 'cylinder'
            The type of the quiver.
        resolution : int
            The resolution of the glyph created. Depending on the type of
            glyph, it represents the number of divisions in its geometric
            representation.
        glyph_height : float
            The height of the glyph used with the quiver.
        glyph_center : tuple
            The center of the glyph used with the quiver: (x, y, z).
        glyph_resolution : float
            The resolution of the glyph used with the quiver.
        opacity : float
            The opacity of the quiver.
        scale_mode : 'vector', 'scalar' or 'none'
            The scaling mode for the glyph.
        scalars : array, shape (n_quivers,) | None
            The optional scalar data to use.
        backface_culling : bool
            If True, enable backface culling on the quiver.
        colormap :
            The colormap to use.
        vmin : float | None
            vmin is used to scale the colormap.
            If None, the min of the data will be used
        vmax : float | None
            vmax is used to scale the colormap.
            If None, the max of the data will be used
        line_width : float
            The width of the 2d arrows.

        ### ⏎ Returns
        -------
        actor :
            The actor in the scene.
        surface :
            Handle of the quiver in the scene.
        """
        ...
    @classmethod
    @abc.abstractmethod
    def text2d(self, x_window, y_window, text, size: int = 14, color: str = "white"):
        """### Add 2d text in the scene.

        ### 🛠️ Parameters
        ----------
        x : float
            The X component to use as position of the text in the
            window coordinates system (window_width, window_height).
        y : float
            The Y component to use as position of the text in the
            window coordinates system (window_width, window_height).
        text : str
            The content of the text.
        size : int
            The size of the font.
        color : tuple | str
            The color of the text as a tuple (red, green, blue) of float
            values between 0 and 1 or a valid color name (i.e. 'white'
            or 'w').
        """
        ...
    @classmethod
    @abc.abstractmethod
    def text3d(self, x, y, z, text, width, color: str = "white"):
        """### Add 2d text in the scene.

        ### 🛠️ Parameters
        ----------
        x : float
            The X component to use as position of the text.
        y : float
            The Y component to use as position of the text.
        z : float
            The Z component to use as position of the text.
        text : str
            The content of the text.
        width : float
            The width of the text.
        color : tuple | str
            The color of the text as a tuple (red, green, blue) of float
            values between 0 and 1 or a valid color name (i.e. 'white'
            or 'w').
        """
        ...
    @classmethod
    @abc.abstractmethod
    def scalarbar(
        self, source, color: str = "white", title=None, n_labels: int = 4, bgcolor=None
    ):
        """### Add a scalar bar in the scene.

        ### 🛠️ Parameters
        ----------
        source :
            The object of the scene used for the colormap.
        color :
            The color of the label text.
        title : str | None
            The title of the scalar bar.
        n_labels : int | None
            The number of labels to display on the scalar bar.
        bgcolor :
            The color of the background when there is transparency.
        """
        ...
    @classmethod
    @abc.abstractmethod
    def show(self):
        """### Render the scene."""
        ...
    @classmethod
    @abc.abstractmethod
    def close(self):
        """### Close the scene."""
        ...
    @classmethod
    @abc.abstractmethod
    def set_camera(
        self,
        azimuth=None,
        elevation=None,
        distance=None,
        focalpoint=None,
        roll=None,
        *,
        reset_camera=None,
    ):
        """### Configure the camera of the scene.

        ### 🛠️ Parameters
        ----------
        azimuth : float
            The azimuthal angle of the camera.
        elevation : float
            The zenith angle of the camera.
        distance : float
            The distance to the focal point.
        focalpoint : tuple
            The focal point of the camera: (x, y, z).
        roll : float
            The rotation of the camera along its axis.
        reset_camera : bool
           Deprecated, used ``distance="auto"`` instead.
        """
        ...
    @classmethod
    @abc.abstractmethod
    def reset_camera(self):
        """### Reset the camera properties."""
        ...
    @classmethod
    @abc.abstractmethod
    def screenshot(self, mode: str = "rgb", filename=None):
        """### Take a screenshot of the scene.

        ### 🛠️ Parameters
        ----------
        mode : str
            Either 'rgb' or 'rgba' for values to return.
            Default is 'rgb'.
        filename : str | None
            If not None, save the figure to the disk.
        """
        ...
    @classmethod
    @abc.abstractmethod
    def project(self, xyz, ch_names):
        """### Convert 3d points to a 2d perspective.

        ### 🛠️ Parameters
        ----------
        xyz : array, shape(n_points, 3)
            The points to project.
        ch_names : array, shape(_n_points,)
            Names of the channels.
        """
        ...
    @classmethod
    @abc.abstractmethod
    def remove_mesh(self, mesh_data):
        """### Remove the given mesh from the scene.

        ### 🛠️ Parameters
        ----------
        mesh_data : tuple | Surface
            The mesh to remove.
        """
        ...

class _AbstractWidget(ABC, metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def __init__(self): ...

class _AbstractLabel(_AbstractWidget, metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def __init__(self, value, center: bool = False, selectable: bool = False): ...

class _AbstractText(_AbstractWidget, metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def __init__(self, value=None, placeholder=None, callback=None): ...

class _AbstractButton(_AbstractWidget, metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def __init__(self, value, callback, icon=None): ...

class _AbstractSlider(_AbstractWidget, metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def __init__(self, value, rng, callback, horizontal: bool = True): ...

class _AbstractProgressBar(_AbstractWidget, metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def __init__(self, count): ...

class _AbstractCheckBox(_AbstractWidget, metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def __init__(self, value, callback): ...

class _AbstractSpinBox(_AbstractWidget, metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def __init__(self, value, rng, callback, step=None): ...

class _AbstractComboBox(_AbstractWidget, metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def __init__(self, value, items, callback): ...

class _AbstractRadioButtons(_AbstractWidget, metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def __init__(self, value, items, callback): ...

class _AbstractGroupBox(_AbstractWidget, metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def __init__(self, name, items): ...

class _AbstractFileButton(_AbstractWidget, metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def __init__(
        self,
        callback,
        content_filter=None,
        initial_directory=None,
        save: bool = False,
        is_directory: bool = False,
        icon: str = "folder",
        window=None,
    ): ...

class _AbstractPlayMenu(_AbstractWidget, metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def __init__(self, value, rng, callback): ...

class _AbstractPopup(_AbstractWidget, metaclass=abc.ABCMeta):
    @abstractmethod
    def __init__(
        self,
        title,
        text,
        info_text=None,
        callback=None,
        icon: str = "Warning",
        buttons=None,
        window=None,
    ): ...

class _AbstractBoxLayout(ABC, metaclass=abc.ABCMeta): ...

class _AbstractHBoxLayout(_AbstractBoxLayout, metaclass=abc.ABCMeta):
    @abstractmethod
    def __init__(self, height=None, scroll=None): ...

class _AbstractVBoxLayout(_AbstractBoxLayout, metaclass=abc.ABCMeta):
    @abstractmethod
    def __init__(self, width=None, scroll=None): ...

class _AbstractGridLayout(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def __init__(self, height=None, width=None, scroll=None): ...

class _AbstractAppWindow(ABC, metaclass=abc.ABCMeta):
    def __init__(self, size=None, fullscreen: bool = False) -> None: ...

class _AbstractCanvas(ABC, metaclass=abc.ABCMeta):
    def __init__(self, width=None, height=None, dpi=None) -> None:
        """### Initialize the matplotlib Canvas."""
        ...
    def show(self) -> None:
        """### Show the canvas."""
        ...
    def close(self) -> None:
        """### Close the canvas."""
        ...
    def update(self) -> None:
        """### Update the canvas."""
        ...
    manager: Incomplete

    def clear(self) -> None:
        """### Clear internal variables."""
        ...

class _AbstractToolBar(ABC, metaclass=abc.ABCMeta): ...
class _AbstractDock(ABC, metaclass=abc.ABCMeta): ...
class _AbstractMenuBar(ABC, metaclass=abc.ABCMeta): ...
class _AbstractStatusBar(ABC, metaclass=abc.ABCMeta): ...
class _AbstractPlayback(ABC, metaclass=abc.ABCMeta): ...
class _AbstractKeyPress(ABC, metaclass=abc.ABCMeta): ...
class _AbstractDialog(ABC, metaclass=abc.ABCMeta): ...
class _AbstractLayout(ABC, metaclass=abc.ABCMeta): ...

class _AbstractWidgetList(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def set_enabled(self, state): ...
    @abstractmethod
    def get_value(self, idx): ...
    @abstractmethod
    def set_value(self, idx, value): ...

class _AbstractWdgt(ABC, metaclass=abc.ABCMeta):
    def __init__(self, widget) -> None: ...
    @property
    def widget(self): ...
    @abstractmethod
    def set_value(self, value): ...
    @abstractmethod
    def get_value(self): ...
    @abstractmethod
    def set_range(self, rng): ...
    @abstractmethod
    def show(self): ...
    @abstractmethod
    def hide(self): ...
    @abstractmethod
    def set_enabled(self, state): ...
    @abstractmethod
    def is_enabled(self): ...
    @abstractmethod
    def update(self, repaint: bool = True): ...
    @abstractmethod
    def get_tooltip(self): ...
    @abstractmethod
    def set_tooltip(self, tooltip: str): ...
    @abstractmethod
    def set_style(self, style): ...

class _AbstractAction(ABC, metaclass=abc.ABCMeta):
    def __init__(self, action) -> None: ...
    @abstractmethod
    def trigger(self): ...
    @abstractmethod
    def set_icon(self): ...
    @abstractmethod
    def set_shortcut(self): ...

class _AbstractMplInterface(ABC, metaclass=abc.ABCMeta): ...

class _AbstractMplCanvas(ABC):
    fig: Incomplete
    axes: Incomplete
    manager: Incomplete

    def __init__(self, width, height, dpi) -> None:
        """### Initialize the MplCanvas."""
        ...
    def plot(self, x, y, label, update: bool = True, **kwargs):
        """### Plot a curve."""
        ...
    def plot_time_line(self, x, label, update: bool = True, **kwargs):
        """### Plot the vertical line."""
        ...
    def update_plot(self) -> None:
        """### Update the plot."""
        ...
    def set_color(self, bg_color, fg_color) -> None:
        """### Set the widget colors."""
        ...
    def show(self) -> None:
        """### Show the canvas."""
        ...
    def close(self) -> None:
        """### Close the canvas."""
        ...
    canvas: Incomplete

    def clear(self) -> None:
        """### Clear internal variables."""
        ...
    def on_resize(self, event) -> None:
        """### Handle resize events."""
        ...

class _AbstractBrainMplCanvas(_AbstractMplCanvas):
    brain: Incomplete

    def __init__(self, brain, width, height, dpi) -> None:
        """### Initialize the MplCanvas."""
        ...
    def update_plot(self) -> None:
        """### Update the plot."""
        ...
    def on_button_press(self, event) -> None:
        """### Handle button presses."""
        ...
    on_motion_notify = on_button_press

    def clear(self) -> None:
        """### Clear internal variables."""
        ...

class _AbstractWindow(ABC, metaclass=abc.ABCMeta): ...
