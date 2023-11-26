from .._fiff.meas_info import create_info as create_info
from ..utils import logger as logger
from .utils import plot_sensors as plot_sensors

def plot_montage(
    montage,
    scale_factor: int = 20,
    show_names: bool = True,
    kind: str = "topomap",
    show: bool = True,
    sphere=None,
    *,
    axes=None,
    verbose=None,
):
    """Plot a montage.

    Parameters
    ----------
    montage : instance of DigMontage
        The montage to visualize.
    scale_factor : float
        Determines the size of the points.
    show_names : bool | list
        Whether to display all channel names. If a list, only the channel
        names in the list are shown. Defaults to True.
    kind : str
        Whether to plot the montage as '3d' or 'topomap' (default).
    show : bool
        Show figure if True.
    sphere : float | array-like | instance of ConductorModel | None  | 'auto' | 'eeglab'
        The sphere parameters to use for the head outline. Can be array-like of
        shape (4,) to give the X/Y/Z origin and radius in meters, or a single float
        to give just the radius (origin assumed 0, 0, 0). Can also be an instance
        of a spherical :class:mne.bem.ConductorModel` to use the origin and
        radius from that object. If ``'auto'`` the sphere is fit to digitization
        points. If ``'eeglab'`` the head circle is defined by EEG electrodes
        ``'Fpz'``, ``'Oz'``, ``'T7'``, and ``'T8'`` (if ``'Fpz'`` is not present,
        it will be approximated from the coordinates of ``'Oz'``). ``None`` (the
        default) is equivalent to ``'auto'`` when enough extra digitization points
        are available, and (0, 0, 0, 0.095) otherwise.

        .. versionadded:: 0.20
        .. versionchanged:: 1.1 Added ``'eeglab'`` option.

    axes : instance of Axes | instance of Axes3D | None
        Axes to draw the sensors to. If ``kind='3d'``, axes must be an instance
        of Axes3D. If None (default), a new axes will be created.

        .. versionadded:: 1.4

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    fig : instance of matplotlib.figure.Figure
        The figure object.
    """
    ...
