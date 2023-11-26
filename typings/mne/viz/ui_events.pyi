from ..utils import fill_doc as fill_doc, logger as logger, warn as warn
from _typeshed import Incomplete
from collections.abc import Generator
from dataclasses import dataclass
from matplotlib.colors import Colormap
from typing import List, Optional, Union

class UIEvent:
    """### Abstract base class for all events.

    -----
    ### 📊 Attributes


    name : str
        The name of the event (same as its class name but in snake_case).
    source : matplotlib.figure.Figure | Figure3D
        The figure that published the event.
    """

    source: Incomplete

    @property
    def name(self):
        """### The name of the event, which is the class name in snake case."""
        ...

class FigureClosing(UIEvent):
    """### Indicates that the user has requested to close a figure.

    -----
    ### 📊 Attributes


    name : str
        The name of the event (same as its class name but in snake_case).
    source : matplotlib.figure.Figure | Figure3D
        The figure that published the event.
    """

    ...

@dataclass
class TimeChange(UIEvent):
    """Indicates that the user has selected a time.

    -----
    ### 🛠️ Parameters

    time : float
        The new time in seconds.

    -----
    ### 📊 Attributes

    %(ui_event_name_source)s
    time : float
        The new time in seconds.
    """

    time: float

    def __init__(self, time) -> None: ...

@dataclass
class PlaybackSpeed(UIEvent):
    """Indicates that the user has selected a different playback speed for videos.

    -----
    ### 🛠️ Parameters

    speed : float
        The new speed in seconds per frame.

    -----
    ### 📊 Attributes

    %(ui_event_name_source)s
    speed : float
        The new speed in seconds per frame.
    """

    speed: float

    def __init__(self, speed) -> None: ...

@dataclass
class ColormapRange(UIEvent):
    """Indicates that the user has updated the bounds of the colormap.

    -----
    ### 🛠️ Parameters

    kind : str
        Kind of colormap being updated. The Notes section of the drawing
        routine publishing this event should mention the possible kinds.
    ch_type : str
       Type of sensor the data originates from.
    %(fmin_fmid_fmax)s
    %(alpha)s
    cmap : str
        The colormap to use. Either string or matplotlib.colors.Colormap
        instance.

    -----
    ### 📊 Attributes

    kind : str
        Kind of colormap being updated. The Notes section of the drawing
        routine publishing this event should mention the possible kinds.
    ch_type : str
        Type of sensor the data originates from.
    unit : str
        The unit of the values.
    %(ui_event_name_source)s
    %(fmin_fmid_fmax)s
    %(alpha)s
    cmap : str
        The colormap to use. Either string or matplotlib.colors.Colormap
        instance.
    """

    kind: str
    ch_type: Optional[str] = ...
    fmin: Optional[float] = ...
    fmid: Optional[float] = ...
    fmax: Optional[float] = ...
    alpha: Optional[bool] = ...
    cmap: Optional[Union[Colormap, str]] = ...

    def __init__(self, kind, ch_type, fmin, fmid, fmax, alpha, cmap) -> None: ...

@dataclass
class VertexSelect(UIEvent):
    """Indicates that the user has selected a vertex.

    -----
    ### 🛠️ Parameters

    hemi : str
        The hemisphere the vertex was selected on.
        Can be ``"lh"``, ``"rh"``, or ``"vol"``.
    vertex_id : int
        The vertex number (in the high resolution mesh) that was selected.

    -----
    ### 📊 Attributes

    %(ui_event_name_source)s
    hemi : str
        The hemisphere the vertex was selected on.
        Can be ``"lh"``, ``"rh"``, or ``"vol"``.
    vertex_id : int
        The vertex number (in the high resolution mesh) that was selected.
    """

    hemi: str
    vertex_id: int

    def __init__(self, hemi, vertex_id) -> None: ...

@dataclass
class Contours(UIEvent):
    """Indicates that the user has changed the contour lines.

    -----
    ### 🛠️ Parameters

    kind : str
        The kind of contours lines being changed. The Notes section of the
        drawing routine publishing this event should mention the possible
        kinds.
    contours : list of float
        The new values at which contour lines need to be drawn.

    -----
    ### 📊 Attributes

    %(ui_event_name_source)s
    kind : str
        The kind of contours lines being changed. The Notes section of the
        drawing routine publishing this event should mention the possible
        kinds.
    contours : list of float
        The new values at which contour lines need to be drawn.
    """

    kind: str
    contours: List[str]

    def __init__(self, kind, contours) -> None: ...

def publish(fig, event, *, verbose=None) -> None:
    """### Publish an event to all subscribers of the figure's channel.

    The figure's event channel and all linked event channels are searched for
    subscribers to the given event. Each subscriber had provided a callback
    function when subscribing, so we call that.

    -----
    ### 🛠️ Parameters

    fig : matplotlib.figure.Figure | Figure3D
        The figure that publishes the event.
    event : UIEvent
        Event to publish.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.
    """
    ...

def subscribe(fig, event_name, callback, *, verbose=None) -> None:
    """### Subscribe to an event on a figure's event channel.

    -----
    ### 🛠️ Parameters

    fig : matplotlib.figure.Figure | Figure3D
        The figure of which event channel to subscribe.
    event_name : str
        The name of the event to listen for.
    callback : callable
        The function that should be called whenever the event is published.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.
    """
    ...

def unsubscribe(fig, event_names, callback=None, *, verbose=None) -> None:
    """### Unsubscribe from an event on a figure's event channel.

    -----
    ### 🛠️ Parameters

    fig : matplotlib.figure.Figure | Figure3D
        The figure of which event channel to unsubscribe from.
    event_names : str | list of str
        Select which events to stop subscribing to. Can be a single string
        event name, a list of event names or ``"all"`` which will unsubscribe
        from all events.
    callback : callable | None
        The callback function that should be unsubscribed, leaving all other
        callback functions that may be subscribed untouched. By default
        (``None``) all callback functions are unsubscribed from the event.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.
    """
    ...

def link(*figs, include_events=None, exclude_events=None, verbose=None) -> None:
    """### Link the event channels of two figures together.

    When event channels are linked, any events that are published on one
    channel are simultaneously published on the other channel. Links are
    bi-directional.

    -----
    ### 🛠️ Parameters

    *figs : tuple of matplotlib.figure.Figure | tuple of Figure3D
        The figures whose event channel will be linked.
    include_events : list of str | None
        Select which events to publish across figures. By default (``None``),
        both figures will receive all of each other's events. Passing a list of
        event names will restrict the events being shared across the figures to
        only the given ones.
    exclude_events : list of str | None
        Select which events not to publish across figures. By default (``None``),
        no events are excluded.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.
    """
    ...

def unlink(fig, *, verbose=None) -> None:
    """### Remove all links involving the event channel of the given figure.

    -----
    ### 🛠️ Parameters

    fig : matplotlib.figure.Figure | Figure3D
        The figure whose event channel should be unlinked from all other event
        channels.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.
    """
    ...

def disable_ui_events(fig) -> Generator[None, None, None]:
    """### Temporarily disable generation of UI events. Use as context manager.

    -----
    ### 🛠️ Parameters

    fig : matplotlib.figure.Figure | Figure3D
        The figure whose UI event generation should be temporarily disabled.
    """
    ...
