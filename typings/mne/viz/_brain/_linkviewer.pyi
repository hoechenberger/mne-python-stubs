from ...utils import warn as warn
from ..ui_events import link as link
from _typeshed import Incomplete

class _LinkViewer:
    """Class to link multiple Brain objects."""
    brains: Incomplete
    leader: Incomplete

    def __init__(self, brains, time: bool=..., camera: bool=..., colorbar: bool=..., picking: bool=...) -> None:
        ...

    def set_fmin(self, value) -> None:
        ...

    def set_fmid(self, value) -> None:
        ...

    def set_fmax(self, value) -> None:
        ...

    def set_time_point(self, value) -> None:
        ...

    def set_playback_speed(self, value) -> None:
        ...

    def toggle_playback(self) -> None:
        ...

    def link_cameras(self) -> None:
        ...