import abc
from ...transforms import apply_trans as apply_trans
from ...utils import copy_base_doc_to_subclass_doc as copy_base_doc_to_subclass_doc, deprecated as deprecated, warn as warn
from ._abstract import Figure3D as Figure3D, _AbstractRenderer
from ._utils import ALLOWED_QUIVER_MODES as ALLOWED_QUIVER_MODES
from _typeshed import Incomplete
from pyvistaqt import BackgroundPlotter

class PyVistaFigure(Figure3D):
    """PyVista-based 3D Figure.

    .. note:: This class should not be instantiated directly via
              ``mne.viz.PyVistaFigure(...)``. Instead, use
              :func:`mne.viz.create_3d_figure`.

    See Also
    --------
    mne.viz.create_3d_figure
    """

    def __init__(self) -> None:
        ...

class _Projection:
    """Modify visibility attribute of the sensors."""
    xy: Incomplete
    pts: Incomplete
    plotter: Incomplete

    def __init__(self, *, xy, pts, plotter) -> None:
        """Store input projection information into attributes."""

    def visible(self, state) -> None:
        """Modify visibility attribute of the sensors."""

class _PyVistaRenderer(_AbstractRenderer, metaclass=abc.ABCMeta):
    """Remove the given mesh from the scene.

        Parameters
        ----------
        mesh_data : tuple | Surface
            The mesh to remove.
        """
    font_family: str
    tube_n_sides: int
    antialias: Incomplete
    depth_peeling: Incomplete
    smooth_shading: Incomplete
    figure: Incomplete
    plotter: Incomplete

    def __init__(self, fig: Incomplete | None=..., size=..., bgcolor: str=..., name: str=..., show: bool=..., shape=..., notebook: Incomplete | None=..., smooth_shading: bool=..., splash: bool=..., multi_samples: Incomplete | None=...) -> None:
        ...

    def subplot(self, x, y) -> None:
        """Set the active subplot."""

    def scene(self):
        """Return scene handle."""

    def update_lighting(self) -> None:
        ...

    def set_interaction(self, interaction) -> None:
        """Set interaction mode."""

    def legend(self, labels, border: bool=..., size: float=..., face: str=..., loc: str=...):
        """Add a legend to the scene.

        Parameters
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

    def polydata(self, mesh, color: Incomplete | None=..., opacity: float=..., normals: Incomplete | None=..., backface_culling: bool=..., scalars: Incomplete | None=..., colormap: Incomplete | None=..., vmin: Incomplete | None=..., vmax: Incomplete | None=..., interpolate_before_map: bool=..., representation: str=..., line_width: float=..., polygon_offset: Incomplete | None=..., **kwargs):
        ...

    def mesh(self, x, y, z, triangles, color, opacity: float=..., *, backface_culling: bool=..., scalars: Incomplete | None=..., colormap: Incomplete | None=..., vmin: Incomplete | None=..., vmax: Incomplete | None=..., interpolate_before_map: bool=..., representation: str=..., line_width: float=..., normals: Incomplete | None=..., polygon_offset: Incomplete | None=..., **kwargs):
        """Add a mesh in the scene.

        Parameters
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

        Returns
        -------
        surface :
            Handle of the mesh in the scene.
        """

    def contour(self, surface, scalars, contours, width: float=..., opacity: float=..., vmin: Incomplete | None=..., vmax: Incomplete | None=..., colormap: Incomplete | None=..., normalized_colormap: bool=..., kind: str=..., color: Incomplete | None=...):
        """Add a contour in the scene.

        Parameters
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

    def surface(self, surface, color: Incomplete | None=..., opacity: float=..., vmin: Incomplete | None=..., vmax: Incomplete | None=..., colormap: Incomplete | None=..., normalized_colormap: bool=..., scalars: Incomplete | None=..., backface_culling: bool=..., polygon_offset: Incomplete | None=...):
        """Add a surface in the scene.

        Parameters
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

    def sphere(self, center, color, scale, opacity: float=..., resolution: int=..., backface_culling: bool=..., radius: Incomplete | None=...):
        """Add sphere in the scene.

        Parameters
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

    def tube(self, origin, destination, radius: float=..., color: str=..., scalars: Incomplete | None=..., vmin: Incomplete | None=..., vmax: Incomplete | None=..., colormap: str=..., normalized_colormap: bool=..., reverse_lut: bool=..., opacity: Incomplete | None=...):
        """Add tube in the scene.

        Parameters
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

        Returns
        -------
        actor :
            The actor in the scene.
        surface :
            Handle of the tube in the scene.
        """

    def quiver3d(self, x, y, z, u, v, w, color, scale, mode, resolution: int=..., glyph_height: Incomplete | None=..., glyph_center: Incomplete | None=..., glyph_resolution: Incomplete | None=..., opacity: float=..., scale_mode: str=..., scalars: Incomplete | None=..., colormap: Incomplete | None=..., backface_culling: bool=..., line_width: float=..., name: Incomplete | None=..., glyph_width: Incomplete | None=..., glyph_depth: Incomplete | None=..., glyph_radius: float=..., solid_transform: Incomplete | None=..., *, clim: Incomplete | None=...):
        """Add quiver3d in the scene.

        Parameters
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

        Returns
        -------
        actor :
            The actor in the scene.
        surface :
            Handle of the quiver in the scene.
        """

    def text2d(self, x_window, y_window, text, size: int=..., color: str=..., justification: Incomplete | None=...):
        """Add 2d text in the scene.

        Parameters
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

    def text3d(self, x, y, z, text, scale, color: str=...):
        """Add 2d text in the scene.

        Parameters
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

    def scalarbar(self, source, color: str=..., title: Incomplete | None=..., n_labels: int=..., bgcolor: Incomplete | None=..., **extra_kwargs):
        """Add a scalar bar in the scene.

        Parameters
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

    def show(self) -> None:
        """Render the scene."""

    def close(self) -> None:
        """Close the scene."""

    def get_camera(self, *, rigid: Incomplete | None=...):
        ...

    def set_camera(self, azimuth: Incomplete | None=..., elevation: Incomplete | None=..., distance: Incomplete | None=..., focalpoint: Incomplete | None=..., roll: Incomplete | None=..., *, rigid: Incomplete | None=..., update: bool=..., reset_camera: Incomplete | None=...) -> None:
        """Configure the camera of the scene.

        Parameters
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

    def reset_camera(self) -> None:
        """Reset the camera properties.
.. warning:: DEPRECATED: reset_camera is deprecated and will be removed in 1.7, use set_camera(distance='auto') instead."""

    def screenshot(self, mode: str=..., filename: Incomplete | None=...):
        """Take a screenshot of the scene.

        Parameters
        ----------
        mode : str
            Either 'rgb' or 'rgba' for values to return.
            Default is 'rgb'.
        filename : str | None
            If not None, save the figure to the disk.
        """

    def project(self, xyz, ch_names):
        """Convert 3d points to a 2d perspective.

        Parameters
        ----------
        xyz : array, shape(n_points, 3)
            The points to project.
        ch_names : array, shape(_n_points,)
            Names of the channels.
        """

    def remove_mesh(self, mesh_data) -> None:
        """Remove the given mesh from the scene.

        Parameters
        ----------
        mesh_data : tuple | Surface
            The mesh to remove.
        """

class _SafeBackgroundPlotter(BackgroundPlotter):

    def __del__(self) -> None:
        """Delete the qt plotter."""