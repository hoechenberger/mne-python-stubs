from .._fiff.pick import pick_types as pick_types
from ..defaults import DEFAULTS as DEFAULTS
from ..utils import fill_doc as fill_doc
from .ui_events import ColormapRange as ColormapRange, Contours as Contours, TimeChange as TimeChange, disable_ui_events as disable_ui_events, publish as publish, subscribe as subscribe
from .utils import mne_analyze_colormap as mne_analyze_colormap
from _typeshed import Incomplete

class EvokedField:
    """Change the color range of the density maps.

        Parameters
        ----------
        vmax : float
            The new maximum value of the color range.
        type : 'meg' | 'eeg'
            Which field map to apply the new color range to.
        """
    plotter: Incomplete
    interaction: Incomplete
    time_viewer: Incomplete

    def __init__(self, evoked, surf_maps, *, time: Incomplete | None=..., time_label: str=..., n_jobs: Incomplete | None=..., fig: Incomplete | None=..., vmax: Incomplete | None=..., n_contours: int=..., show_density: bool=..., alpha: Incomplete | None=..., interpolation: str=..., interaction: str=..., time_viewer: str=..., verbose: Incomplete | None=...) -> None:
        ...

    def set_time(self, time) -> None:
        """Set the time to display (in seconds).

        Parameters
        ----------
        time : float
            The time to show, in seconds.
        """

    def set_contours(self, n_contours) -> None:
        """Adjust the number of contour lines to use when drawing the fieldlines.

        Parameters
        ----------
        n_contours : int
            The number of contour lines to use.
        """

    def set_vmax(self, vmax, type: str=...) -> None:
        """Change the color range of the density maps.

        Parameters
        ----------
        vmax : float
            The new maximum value of the color range.
        type : 'meg' | 'eeg'
            Which field map to apply the new color range to.
        """