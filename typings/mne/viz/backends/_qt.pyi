from ...utils import get_config as get_config
from ..utils import safe_event as safe_event
from ._abstract import (
    _AbstractAction,
    _AbstractAppWindow,
    _AbstractBrainMplCanvas,
    _AbstractButton,
    _AbstractCanvas,
    _AbstractCheckBox,
    _AbstractComboBox,
    _AbstractDialog,
    _AbstractDock,
    _AbstractFileButton,
    _AbstractGridLayout,
    _AbstractGroupBox,
    _AbstractHBoxLayout,
    _AbstractKeyPress,
    _AbstractLabel,
    _AbstractLayout,
    _AbstractMenuBar,
    _AbstractMplCanvas,
    _AbstractMplInterface,
    _AbstractPlayMenu,
    _AbstractPlayback,
    _AbstractPopup,
    _AbstractProgressBar,
    _AbstractRadioButtons,
    _AbstractSlider,
    _AbstractSpinBox,
    _AbstractStatusBar,
    _AbstractText,
    _AbstractToolBar,
    _AbstractVBoxLayout,
    _AbstractWdgt,
    _AbstractWidget,
    _AbstractWidgetList,
    _AbstractWindow,
)
from ._pyvista import _PyVistaRenderer
from .renderer import _TimeInteraction
from _typeshed import Incomplete
from matplotlib.backends.backend_qtagg import FigureCanvas
from pyvistaqt.plotting import MainWindow
from qtpy import API_NAME as API_NAME
from qtpy.QtCore import QObject
from qtpy.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QSlider,
    QVBoxLayout,
    QWidget,
)

class _BaseWidget(Incomplete, Incomplete): ...

class _Widget(_AbstractWidget, QWidget, metaclass=_BaseWidget):
    tooltip: Incomplete

    def __init__(self) -> None: ...

class _Label(QLabel, _AbstractLabel, _Widget, metaclass=_BaseWidget):
    def __init__(
        self, value, center: bool = False, selectable: bool = False
    ) -> None: ...

class _Text(QLineEdit, _AbstractText, _Widget, metaclass=_BaseWidget):
    def __init__(self, value=None, placeholder=None, callback=None) -> None: ...

class _Button(QPushButton, _AbstractButton, _Widget, metaclass=_BaseWidget):
    def __init__(self, value, callback, icon=None) -> None: ...

class _Slider(QSlider, _AbstractSlider, _Widget, metaclass=_BaseWidget):
    def __init__(self, value, rng, callback, horizontal: bool = True) -> None: ...

class _ProgressBar(QProgressBar, _AbstractProgressBar, _Widget, metaclass=_BaseWidget):
    def __init__(self, count) -> None: ...

class _CheckBox(QCheckBox, _AbstractCheckBox, _Widget, metaclass=_BaseWidget):
    def __init__(self, value, callback) -> None: ...

class _SpinBox(QDoubleSpinBox, _AbstractSpinBox, _Widget, metaclass=_BaseWidget):
    def __init__(self, value, rng, callback, step=None) -> None: ...

class _ComboBox(QComboBox, _AbstractComboBox, _Widget, metaclass=_BaseWidget):
    def __init__(self, value, items, callback) -> None: ...

class _RadioButtons(QVBoxLayout, _AbstractRadioButtons, _Widget, metaclass=_BaseWidget):
    def __init__(self, value, items, callback) -> None: ...

class _GroupBox(QGroupBox, _AbstractGroupBox, _Widget, metaclass=_BaseWidget):
    def __init__(self, name, items) -> None: ...

class _FileButton(_Button, _AbstractFileButton, _Widget, metaclass=_BaseWidget):
    def __init__(
        self,
        callback,
        content_filter=None,
        initial_directory=None,
        save: bool = False,
        is_directory: bool = False,
        icon: str = "folder",
        window=None,
    ) -> None: ...

class _PlayMenu(QVBoxLayout, _AbstractPlayMenu, _Widget, metaclass=_BaseWidget):
    def __init__(self, value, rng, callback) -> None: ...

class _Popup(QMessageBox, _AbstractPopup, _Widget, metaclass=_BaseWidget):
    def __init__(
        self,
        title,
        text,
        info_text=None,
        callback=None,
        icon: str = "warning",
        buttons=None,
        window=None,
    ) -> None: ...

class _ScrollArea(QScrollArea):
    def __init__(self, width, height, widget) -> None: ...

class _HBoxLayout(QHBoxLayout, _AbstractHBoxLayout, _Widget, metaclass=_BaseWidget):
    def __init__(self, height=None, scroll=None) -> None: ...

class _VBoxLayout(QVBoxLayout, _AbstractVBoxLayout, _Widget, metaclass=_BaseWidget):
    def __init__(self, width=None, scroll=None) -> None: ...

class _GridLayout(QGridLayout, _AbstractGridLayout, _Widget, metaclass=_BaseWidget):
    def __init__(self, height=None, width=None) -> None: ...

class _BaseCanvas(Incomplete, Incomplete): ...

class _Canvas(FigureCanvas, _AbstractCanvas, metaclass=_BaseCanvas):
    fig: Incomplete
    ax: Incomplete

    def __init__(self, width, height, dpi) -> None: ...

class _MNEMainWindow(MainWindow):
    def __init__(self, parent=None, title=None, size=None) -> None: ...

class _AppWindow(_AbstractAppWindow, _MNEMainWindow, _Widget, metaclass=_BaseWidget):
    closeEvent: Incomplete

    def __init__(self, size=None, fullscreen: bool = False) -> None: ...

class _3DRenderer(_PyVistaRenderer):
    def __init__(self, *args, **kwargs) -> None: ...
    def show(self) -> None: ...

class _QtKeyPress(_AbstractKeyPress): ...

class _QtDialog(_AbstractDialog):
    supported_button_names: Incomplete
    supported_icon_names: Incomplete

class _QtLayout(_AbstractLayout): ...
class _QtDock(_AbstractDock, _QtLayout): ...

class QFloatSlider(QSlider):
    """## Slider that handles float values."""

    floatValueChanged: Incomplete

    def __init__(self, ori, parent=None) -> None:
        """## Initialize the slider."""
        ...
    def minimum(self):
        """## Get the minimum."""
        ...
    def setMinimum(self, value) -> None:
        """## Set the minimum."""
        ...
    def maximum(self):
        """## Get the maximum."""
        ...
    def setMaximum(self, value) -> None:
        """## Set the maximum."""
        ...
    def value(self):
        """## Get the current value."""
        ...
    def setValue(self, value) -> None:
        """## Set the current value."""
        ...
    def mousePressEvent(self, event) -> None:
        """## Add snap-to-location handling."""
        ...

class _QtToolBar(_AbstractToolBar, _QtLayout): ...
class _QtMenuBar(_AbstractMenuBar): ...
class _QtStatusBar(_AbstractStatusBar, _QtLayout): ...
class _QtPlayback(_AbstractPlayback): ...
class _QtMplInterface(_AbstractMplInterface): ...

class _QtMplCanvas(_AbstractMplCanvas, _QtMplInterface):
    def __init__(self, width, height, dpi) -> None: ...

class _QtBrainMplCanvas(_AbstractBrainMplCanvas, _QtMplInterface):
    def __init__(self, brain, width, height, dpi) -> None: ...

class _QtWindow(_AbstractWindow): ...

class _QtWidgetList(_AbstractWidgetList):
    def __init__(self, src) -> None: ...
    def set_enabled(self, state) -> None: ...
    def get_value(self, idx): ...
    def set_value(self, idx, value) -> None: ...

class _QtWidget(_AbstractWdgt):
    def set_value(self, value) -> None: ...
    def get_value(self): ...
    def set_range(self, rng) -> None: ...
    def show(self) -> None: ...
    def hide(self) -> None: ...
    def set_enabled(self, state) -> None: ...
    def is_enabled(self): ...
    def update(self, repaint: bool = True) -> None: ...
    def get_tooltip(self): ...
    def set_tooltip(self, tooltip) -> None: ...
    def set_style(self, style) -> None: ...

class _QtDialogCommunicator(QObject):
    signal_show: Incomplete

    def __init__(self, parent=None) -> None: ...

class _QtDialogWidget(_QtWidget):
    def __init__(self, widget, modal) -> None: ...
    def trigger(self, button) -> None: ...
    def show(self, thread: bool = False) -> None: ...

class _QtAction(_AbstractAction):
    def trigger(self) -> None: ...
    def set_icon(self, icon) -> None: ...
    def set_shortcut(self, shortcut) -> None: ...

class _Renderer(
    _PyVistaRenderer,
    _QtDock,
    _QtToolBar,
    _QtMenuBar,
    _QtStatusBar,
    _QtWindow,
    _QtPlayback,
    _QtDialog,
    _QtKeyPress,
    _TimeInteraction,
):
    def __init__(self, *args, **kwargs) -> None: ...
    def show(self) -> None: ...
