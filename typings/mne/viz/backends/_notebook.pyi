from ...utils import check_version as check_version
from ._abstract import _AbstractAction, _AbstractAppWindow, _AbstractBrainMplCanvas, _AbstractButton, _AbstractCanvas, _AbstractCheckBox, _AbstractComboBox, _AbstractDialog, _AbstractDock, _AbstractFileButton, _AbstractGridLayout, _AbstractGroupBox, _AbstractHBoxLayout, _AbstractKeyPress, _AbstractLabel, _AbstractLayout, _AbstractMenuBar, _AbstractMplCanvas, _AbstractMplInterface, _AbstractPlayMenu, _AbstractPlayback, _AbstractPopup, _AbstractProgressBar, _AbstractRadioButtons, _AbstractSlider, _AbstractSpinBox, _AbstractStatusBar, _AbstractText, _AbstractToolBar, _AbstractVBoxLayout, _AbstractWdgt, _AbstractWidget, _AbstractWidgetList, _AbstractWindow
from ._pyvista import Plotter as Plotter, _PyVistaRenderer
from .renderer import _TimeInteraction
from _typeshed import Incomplete
from ipywidgets import Accordion, Button, Checkbox, Dropdown, GridBox, HBox, IntProgress, IntSlider, IntText, Label, RadioButtons, Text, VBox, Widget

class _BaseWidget(Incomplete, Incomplete):
    ...

class _Widget(Widget, _AbstractWidget, metaclass=_BaseWidget):
    tooltip: Incomplete

    def __init__(self) -> None:
        ...

class _Label(_Widget, _AbstractLabel, Label, metaclass=_BaseWidget):

    def __init__(self, value, center: bool=..., selectable: bool=...) -> None:
        ...

class _Text(_AbstractText, _Widget, Text, metaclass=_BaseWidget):

    def __init__(self, value: Incomplete | None=..., placeholder: Incomplete | None=..., callback: Incomplete | None=...) -> None:
        ...

class _Button(_Widget, _AbstractButton, Button, metaclass=_BaseWidget):
    icon: Incomplete

    def __init__(self, value, callback, icon: Incomplete | None=...) -> None:
        ...

class _Slider(_Widget, _AbstractSlider, IntSlider, metaclass=_BaseWidget):

    def __init__(self, value, rng, callback, horizontal: bool=...) -> None:
        ...
    min: Incomplete
    max: Incomplete

    def set_range(self, rng) -> None:
        ...

class _ProgressBar(_AbstractProgressBar, _Widget, IntProgress, metaclass=_BaseWidget):

    def __init__(self, count) -> None:
        ...

class _CheckBox(_Widget, _AbstractCheckBox, Checkbox, metaclass=_BaseWidget):

    def __init__(self, value, callback) -> None:
        ...

class _SpinBox(_Widget, _AbstractSpinBox, IntText, metaclass=_BaseWidget):
    step: Incomplete

    def __init__(self, value, rng, callback, step: Incomplete | None=...) -> None:
        ...

class _ComboBox(_AbstractComboBox, _Widget, Dropdown, metaclass=_BaseWidget):

    def __init__(self, value, items, callback) -> None:
        ...

class _RadioButtons(_AbstractRadioButtons, _Widget, RadioButtons, metaclass=_BaseWidget):

    def __init__(self, value, items, callback) -> None:
        ...

class _GroupBox(_AbstractGroupBox, _Widget, Accordion, metaclass=_BaseWidget):
    selected_index: int

    def __init__(self, name, items) -> None:
        ...

class _FilePicker:

    def __init__(self, rows: int=..., directory_only: bool=..., ignore_dotfiles: bool=...) -> None:
        ...

    def show(self) -> None:
        ...

    def hide(self) -> None:
        ...

    def set_directory_only(self, state) -> None:
        ...

    def set_ignore_dotfiles(self, state) -> None:
        ...

    def connect(self, callback) -> None:
        ...

class _FileButton(_AbstractFileButton, _Widget, Button, metaclass=_BaseWidget):
    icon: Incomplete

    def __init__(self, callback, content_filter: Incomplete | None=..., initial_directory: Incomplete | None=..., save: bool=..., is_directory: bool=..., icon: str=..., window: Incomplete | None=...) -> None:
        ...

class _PlayMenu(_AbstractPlayMenu, _Widget, VBox, metaclass=_BaseWidget):
    children: Incomplete

    def __init__(self, value, rng, callback) -> None:
        ...

class _Popup(_AbstractPopup, _Widget, VBox, metaclass=_BaseWidget):
    children: Incomplete
    icon: Incomplete

    def __init__(self, title, text, info_text: Incomplete | None=..., callback: Incomplete | None=..., icon: str=..., buttons: Incomplete | None=..., window: Incomplete | None=...) -> None:
        ...

class _BoxLayout:
    ...

class _HBoxLayout(_AbstractHBoxLayout, _BoxLayout, _Widget, HBox, metaclass=_BaseWidget):

    def __init__(self, height: Incomplete | None=..., scroll: Incomplete | None=...) -> None:
        ...

class _VBoxLayout(_AbstractVBoxLayout, _BoxLayout, _Widget, VBox, metaclass=_BaseWidget):

    def __init__(self, width: Incomplete | None=..., scroll: Incomplete | None=...) -> None:
        ...

class _GridLayout(_AbstractGridLayout, _Widget, GridBox, metaclass=_BaseWidget):

    def __init__(self, height: Incomplete | None=..., width: Incomplete | None=...) -> None:
        ...

class _Canvas(_AbstractCanvas, _Widget, HBox, metaclass=_BaseWidget):
    children: Incomplete

    def __init__(self, width, height, dpi) -> None:
        ...

class _AppWindow(_AbstractAppWindow, _Widget, VBox, metaclass=_BaseWidget):

    def __init__(self, size: Incomplete | None=..., fullscreen: bool=...) -> None:
        ...

class _3DRenderer(_PyVistaRenderer):

    def __init__(self, *args, **kwargs) -> None:
        ...

    def show(self) -> None:
        ...

class _FilePckr:

    def __init__(self, rows: int=..., directory_only: bool=..., ignore_dotfiles: bool=...) -> None:
        ...

    def show(self) -> None:
        ...

    def hide(self) -> None:
        ...

    def set_directory_only(self, state) -> None:
        ...

    def set_ignore_dotfiles(self, state) -> None:
        ...

    def connect(self, callback) -> None:
        ...

class _IpyKeyPress(_AbstractKeyPress):
    ...

class _IpyDialog(_AbstractDialog):
    ...

class _IpyLayout(_AbstractLayout):
    ...

class _IpyDock(_AbstractDock, _IpyLayout):
    ...

class _IpyToolBar(_AbstractToolBar, _IpyLayout):
    ...

class _IpyMenuBar(_AbstractMenuBar):
    ...

class _IpyStatusBar(_AbstractStatusBar, _IpyLayout):
    ...

class _IpyPlayback(_AbstractPlayback):
    ...

class _IpyMplInterface(_AbstractMplInterface):
    ...

class _IpyMplCanvas(_AbstractMplCanvas, _IpyMplInterface):

    def __init__(self, width, height, dpi) -> None:
        ...

class _IpyBrainMplCanvas(_AbstractBrainMplCanvas, _IpyMplInterface):

    def __init__(self, brain, width, height, dpi) -> None:
        ...

class _IpyWindow(_AbstractWindow):
    ...

class _IpyWidgetList(_AbstractWidgetList):

    def __init__(self, src) -> None:
        ...

    def set_enabled(self, state) -> None:
        ...

    def get_value(self, idx):
        ...

    def set_value(self, idx, value) -> None:
        ...

class _IpyWidget(_AbstractWdgt):

    def set_value(self, value) -> None:
        ...

    def get_value(self):
        ...

    def set_range(self, rng) -> None:
        ...

    def show(self) -> None:
        ...

    def hide(self) -> None:
        ...

    def set_enabled(self, state) -> None:
        ...

    def is_enabled(self):
        ...

    def update(self, repaint: bool=...) -> None:
        ...

    def get_tooltip(self):
        ...

    def set_tooltip(self, tooltip) -> None:
        ...

    def set_style(self, style) -> None:
        ...

class _IpyAction(_AbstractAction):

    def trigger(self) -> None:
        ...

    def set_icon(self, icon) -> None:
        ...

    def set_shortcut(self, shortcut) -> None:
        ...

class _Renderer(_PyVistaRenderer, _IpyDock, _IpyToolBar, _IpyMenuBar, _IpyStatusBar, _IpyWindow, _IpyPlayback, _IpyDialog, _IpyKeyPress, _TimeInteraction):

    def __init__(self, *args, **kwargs) -> None:
        ...

    def show(self):
        ...