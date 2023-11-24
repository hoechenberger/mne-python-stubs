from ...surface import complete_surface_info as complete_surface_info, read_curvature as read_curvature, read_surface as read_surface
from ...utils import get_subjects_dir as get_subjects_dir
from _typeshed import Incomplete

class _Surface:
    """Load in curvature values from the ?h.curv file."""
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

    def __init__(self, subject, hemi, surf, subjects_dir: Incomplete | None=..., offset: Incomplete | None=..., units: str=..., x_dir: Incomplete | None=...) -> None:
        ...
    orig_faces: Incomplete

    def load_geometry(self) -> None:
        """Load geometry of the surface.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

    def __len__(self) -> int:
        """Return number of vertices."""

    @property
    def x(self):
        ...

    @property
    def y(self):
        ...

    @property
    def z(self):
        ...

    def load_curvature(self) -> None:
        """Load in curvature values from the ?h.curv file."""