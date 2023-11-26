from .._fiff.pick import pick_types as pick_types
from ..defaults import DEFAULTS as DEFAULTS
from ..utils import fill_doc as fill_doc
from .ui_events import (
    ColormapRange as ColormapRange,
    Contours as Contours,
    TimeChange as TimeChange,
    disable_ui_events as disable_ui_events,
    publish as publish,
    subscribe as subscribe,
)
from .utils import mne_analyze_colormap as mne_analyze_colormap
from _typeshed import Incomplete

class EvokedField:
    """### Plot MEG/EEG fields on head surface and helmet in 3D.

    ### 🛠️ Parameters
    ----------
    evoked : instance of mne.Evoked
        The evoked object.
    surf_maps : list
        The surface mapping information obtained with make_field_map.
    time : float | None
        The time point at which the field map shall be displayed. If None,
        the average peak latency (across sensor types) is used.
    time_label : str | None
        How to print info about the time instant visualized.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.
    fig : instance of Figure3D | None
        If None (default), a new figure will be created, otherwise it will
        plot into the given figure.

        ✨ Added in vesion 0.20
    vmax : float | dict | None
        Maximum intensity. Can be a dictionary with two entries ``"eeg"`` and ``"meg"``
        to specify separate values for EEG and MEG fields respectively. Can be
        ``None`` to use the maximum value of the data.

        ✨ Added in vesion 0.21
        ✨ Added in vesion 1.4
            ``vmax`` can be a dictionary to specify separate values for EEG and
            MEG fields.
    n_contours : int
        The number of contours.

        ✨ Added in vesion 0.21
    show_density : bool
        Whether to draw the field density as an overlay on top of the helmet/head
        surface. Defaults to ``True``.
    alpha : float | dict | None
        Opacity of the meshes (between 0 and 1). Can be a dictionary with two
        entries ``"eeg"`` and ``"meg"`` to specify separate values for EEG and
        MEG fields respectively. Can be ``None`` to use 1.0 when a single field
        map is shown, or ``dict(eeg=1.0, meg=0.5)`` when both field maps are shown.

        ✨ Added in vesion 1.4

    interpolation : str | None
        Interpolation method (`scipy.interpolate.interp1d` parameter).
        Must be one of ``'linear'``, ``'nearest'``, ``'zero'``, ``'slinear'``,
        ``'quadratic'`` or ``'cubic'``.

        ✨ Added in vesion 1.6

    interaction : 'trackball' | 'terrain'
        How interactions with the scene via an input device (e.g., mouse or
        trackpad) modify the camera position. If ``'terrain'``, one axis is
        fixed, enabling "turntable-style" rotations. If ``'trackball'``,
        movement along all axes is possible, which provides more freedom of
        movement, but you may incidentally perform unintentional rotations along
        some axes.
        Defaults to ``'terrain'``.

        ✨ Added in vesion 1.1
    time_viewer : bool | str
        Display time viewer GUI. Can also be ``"auto"``, which will mean
        ``True`` if there is more than one time point and ``False`` otherwise.

        ✨ Added in vesion 1.6

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### 📖 Notes
    -----
    The figure will publish and subscribe to the following UI events:

    * `mne.viz.ui_events.TimeChange`
    * `mne.viz.ui_events.Contours`, ``kind="field_strength_meg" | "field_strength_eeg"``
    * `mne.viz.ui_events.ColormapRange`, ``kind="field_strength_meg" | "field_strength_eeg"``
    """

    plotter: Incomplete
    interaction: Incomplete
    time_viewer: Incomplete

    def __init__(
        self,
        evoked,
        surf_maps,
        *,
        time=None,
        time_label: str = "t = %0.0f ms",
        n_jobs=None,
        fig=None,
        vmax=None,
        n_contours: int = 21,
        show_density: bool = True,
        alpha=None,
        interpolation: str = "nearest",
        interaction: str = "terrain",
        time_viewer: str = "auto",
        verbose=None,
    ) -> None: ...
    def set_time(self, time) -> None:
        """### Set the time to display (in seconds).

        ### 🛠️ Parameters
        ----------
        time : float
            The time to show, in seconds.
        """
        ...
    def set_contours(self, n_contours) -> None:
        """### Adjust the number of contour lines to use when drawing the fieldlines.

        ### 🛠️ Parameters
        ----------
        n_contours : int
            The number of contour lines to use.
        """
        ...
    def set_vmax(self, vmax, type: str = "meg") -> None:
        """### Change the color range of the density maps.

        ### 🛠️ Parameters
        ----------
        vmax : float
            The new maximum value of the color range.
        type : 'meg' | 'eeg'
            Which field map to apply the new color range to.
        """
        ...
