from .._fiff.pick import (
    channel_indices_by_type as channel_indices_by_type,
    pick_types as pick_types,
)
from ..utils import Bunch as Bunch, check_version as check_version, logger as logger
from ._figure import BrowserBase as BrowserBase
from .utils import (
    DraggableLine as DraggableLine,
    plot_sensors as plot_sensors,
    plt_show as plt_show,
)
from _typeshed import Incomplete
from matplotlib.figure import Figure

name: str
BACKEND: Incomplete
ANNOTATION_FIG_PAD: float
ANNOTATION_FIG_MIN_H: float
ANNOTATION_FIG_W: float
ANNOTATION_FIG_CHECKBOX_COLUMN_W: float

class MNEFigure(Figure):
    """## 🧠 Base class for 2D figures & dialogs; wraps matplotlib.figure.Figure."""

    mne: Incomplete

    def __init__(self, **kwargs) -> None: ...

class MNEAnnotationFigure(MNEFigure):
    """## 🧠 Interactive dialog figure for annotations."""

    ...

class MNESelectionFigure(MNEFigure):
    """## 🧠 Interactive dialog figure for channel selections."""

    ...

class MNEBrowseFigure(BrowserBase, MNEFigure):
    """## 🧠 Interactive figure with scrollbars, for data browsing."""

    backend_name: str

    def __init__(
        self, inst, figsize, ica=None, xlabel: str = "Time (s)", **kwargs
    ) -> None: ...

class MNELineFigure(MNEFigure):
    """## 🧠 Interactive figure for non-scrolling line plots."""

    def __init__(
        self, inst, n_axes, figsize, *, layout: str = "constrained", **kwargs
    ) -> None: ...
