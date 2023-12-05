from ...utils import fill_doc as fill_doc, logger as logger
from ...viz.utils import plt_show as plt_show

class Calibration(dict):
    """Eye-tracking calibration info.

    This data structure behaves like a dictionary. It contains information regarding a
    calibration that was conducted during an eye-tracking recording.

    💡 Note
        When possible, a Calibration instance should be created with a helper function,
        such as `mne.preprocessing.eyetracking.read_eyelink_calibration`.

    Parameters
    ----------
    onset : float
        The onset of the calibration in seconds. If the calibration was
        performed before the recording started, the the onset can be
        negative.
    model : str
        A string, which is the model of the eye-tracking calibration that was applied.
        For example ``'H3'`` for a horizontal only 3-point calibration, or ``'HV3'``
        for a horizontal and vertical 3-point calibration.
    eye : str
        The eye that was calibrated. For example, ``'left'``, or ``'right'``.
    avg_error : float
        The average error in degrees between the calibration positions and the
        actual gaze position.
    max_error : float
        The maximum error in degrees that occurred between the calibration
        positions and the actual gaze position.
    positions : array-like of float, shape ``(n_calibration_points, 2)``
        The x and y coordinates of the calibration points.
    offsets : array-like of float, shape ``(n_calibration_points,)``
        The error in degrees between the calibration position and the actual
        gaze position for each calibration point.
    gaze : array-like of float, shape ``(n_calibration_points, 2)``
        The x and y coordinates of the actual gaze position for each calibration point.
    screen_size : array-like of shape ``(2,)``
        The width and height (in meters) of the screen that the eyetracking
        data was collected with. For example ``(.531, .298)`` for a monitor with
        a display area of 531 x 298 mm.
    screen_distance : float
        The distance (in meters) from the participant's eyes to the screen.
    screen_resolution : array-like of shape ``(2,)``
        The resolution (in pixels) of the screen that the eyetracking data
        was collected with. For example, ``(1920, 1080)`` for a 1920x1080
        resolution display.
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
        screen_size=None,
        screen_distance=None,
        screen_resolution=None,
    ) -> None: ...
    def copy(self):
        """Copy the instance.

        Returns
        -------
        cal : instance of Calibration
            The copied Calibration.
        """
        ...

    def plot(self, show_offsets: bool = True, axes=None, show: bool = True):
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
        ...

def read_eyelink_calibration(
    fname, screen_size=None, screen_distance=None, screen_resolution=None
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
        A list of `mne.preprocessing.eyetracking.Calibration` instances, one for
        each eye of every calibration that was performed during the recording session.
    """
    ...
