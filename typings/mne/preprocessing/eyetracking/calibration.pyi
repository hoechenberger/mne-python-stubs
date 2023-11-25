from ...utils import fill_doc as fill_doc, logger as logger
from ...viz.utils import plt_show as plt_show

class Calibration(dict):
    """Visualize calibration.

    Parameters
    ----------
    show_offsets : bool
        Whether to display the offset (in visual degrees) of each calibration
        point or not. Defaults to ``True``.
    axes : instance of matplotlib.axes.Axes | None
        Axes to draw the calibration positions to. If ``None`` (default), a new axes
        will be created.
    show : bool
        Whether to show the figure or not. Defaults to ``True``.

    Returns
    -------
    fig : instance of matplotlib.figure.Figure
        The resulting figure object for the calibration plot.
    """

    def __init__(
        self,
        *,
        onset,
        model,
        eye,
        avg_error,
        max_error,
        positions,
        offsets,
        gaze,
        screen_size=...,
        screen_distance=...,
        screen_resolution=...,
    ) -> None: ...
    def copy(self):
        """Copy the instance.

        Returns
        -------
        cal : instance of Calibration
            The copied Calibration.
        """
    def plot(self, show_offsets: bool = ..., axes=..., show: bool = ...):
        """Visualize calibration.

        Parameters
        ----------
        show_offsets : bool
            Whether to display the offset (in visual degrees) of each calibration
            point or not. Defaults to ``True``.
        axes : instance of matplotlib.axes.Axes | None
            Axes to draw the calibration positions to. If ``None`` (default), a new axes
            will be created.
        show : bool
            Whether to show the figure or not. Defaults to ``True``.

        Returns
        -------
        fig : instance of matplotlib.figure.Figure
            The resulting figure object for the calibration plot.
        """

def read_eyelink_calibration(
    fname, screen_size=..., screen_distance=..., screen_resolution=...
):
    """Return info on calibrations collected in an eyelink file.

    Parameters
    ----------
    fname : path-like
        Path to the eyelink file (.asc).
    screen_size : array-like of shape ``(2,)``
        The width and height (in meters) of the screen that the eyetracking
        data was collected with. For example ``(.531, .298)`` for a monitor with
        a display area of 531 x 298 mm. Defaults to ``None``.
    screen_distance : float
        The distance (in meters) from the participant's eyes to the screen.
        Defaults to ``None``.
    screen_resolution : array-like of shape ``(2,)``
        The resolution (in pixels) of the screen that the eyetracking data
        was collected with. For example, ``(1920, 1080)`` for a 1920x1080
        resolution display. Defaults to ``None``.

    Returns
    -------
    calibrations : list
        A list of :class:mne.preprocessing.eyetracking.Calibration` instances, one for
        each eye of every calibration that was performed during the recording session.
    """
