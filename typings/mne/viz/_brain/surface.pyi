from ...surface import (
    complete_surface_info as complete_surface_info,
    read_curvature as read_curvature,
    read_surface as read_surface,
)
from ...utils import get_subjects_dir as get_subjects_dir
from _typeshed import Incomplete

class _Surface:
    """## 🧠 Container for a brain surface.

    It is used for storing vertices, faces and morphometric data
    (curvature) of a hemisphere mesh.

    -----
    ### 🛠️ Parameters

    #### `subject : string`
        Name of subject
    #### `hemi : {'lh', 'rh'}`
        Which hemisphere to load
    #### `surf : string`
        Name of the surface to load (eg. inflated, orig ...).
    #### `subjects_dir : str | None`
        If not None, this directory will be used as the subjects directory
        instead of the value set using the SUBJECTS_DIR environment variable.
    #### `offset : float | None`
        If 0.0, the surface will be offset such that the medial
        wall is aligned with the origin. If None, no offset will
        be applied. If != 0.0, an additional offset will be used.
    #### `units : str`
        Can be 'm' or 'mm' (default).
    #### `x_dir : ndarray | None`
        The x direction to use for offset alignment.

    -----
    ### 📊 Attributes

    #### `bin_curv : numpy.ndarray`
        Curvature values stored as non-negative integers.
    #### `coords : numpy.ndarray`
        nvtx x 3 array of vertex (x, y, z) coordinates.
    #### `curv : numpy.ndarray`
        Vector representation of surface morpometry (curvature) values as
        loaded from a file.
    #### `grey_curv : numpy.ndarray`
        Normalized morphometry (curvature) data, used in order to get
        a gray cortex.
    #### `faces : numpy.ndarray`
        nfaces x 3 array of defining mesh triangles.
    #### `hemi : {'lh', 'rh'}`
        Which hemisphere to load.
    #### `nn : numpy.ndarray`
        Vertex normals for a triangulated surface.
    #### `offset : float | None`
        If float, align inside edge of each hemisphere to center + offset.
        If None, do not change coordinates (default).
    #### `subject : string`
        Name of subject.
    #### `surf : string`
        Name of the surface to load (eg. inflated, orig ...).
    #### `units : str`
        Can be 'm' or 'mm' (default).
    """

    units: Incomplete
    subject: Incomplete
    hemi: Incomplete
    surf: Incomplete
    offset: Incomplete
    bin_curv: Incomplete
    coords: Incomplete
    curv: Incomplete
    faces: Incomplete
    grey_curv: Incomplete
    nn: Incomplete
    labels: Incomplete
    x_dir: Incomplete
    data_path: Incomplete

    def __init__(
        self,
        subject,
        hemi,
        surf,
        subjects_dir=None,
        offset=None,
        units: str = "mm",
        x_dir=None,
    ) -> None: ...
    orig_faces: Incomplete

    def load_geometry(self) -> None:
        """## 🧠 Load geometry of the surface.

        -----
        ### 🛠️ Parameters

        None

        -----
        ### ⏎ Returns

        None
        """
        ...
    def __len__(self) -> int:
        """## 🧠 Return number of vertices."""
        ...
    @property
    def x(self): ...
    @property
    def y(self): ...
    @property
    def z(self): ...
    def load_curvature(self) -> None:
        """## 🧠 Load in curvature values from the ?h.curv file."""
        ...
