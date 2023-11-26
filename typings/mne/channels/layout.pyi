from .._fiff.constants import FIFF as FIFF
from .._fiff.meas_info import Info as Info
from .._fiff.pick import pick_types as pick_types
from ..utils import fill_doc as fill_doc, logger as logger, warn as warn
from ..viz.topomap import plot_layout as plot_layout
from _typeshed import Incomplete

class Layout:
    """Sensor layouts.

    Layouts are typically loaded from a file using
    :func:mne.channels.read_layout`. Only use this class directly if you're
    constructing a new layout.

    Parameters
    ----------
    box : tuple of length 4
        The box dimension (x_min, x_max, y_min, y_max).
    pos : array, shape=(n_channels, 4)
        The unit-normalized positions of the channels in 2d
        (x, y, width, height).
    names : list
        The channel names.
    ids : list
        The channel ids.
    kind : str
        The type of Layout (e.g. 'Vectorview-all').
    """

    box: Incomplete
    pos: Incomplete
    names: Incomplete
    ids: Incomplete
    kind: Incomplete

    def __init__(self, box, pos, names, ids, kind) -> None: ...
    def save(self, fname, overwrite: bool = False) -> None:
        """Save Layout to disk.

        Parameters
        ----------
        fname : path-like
            The file name (e.g. ``'my_layout.lout'``).
        overwrite : bool
            If True, overwrites the destination file if it exists.

        See Also
        --------
        read_layout
        """
        ...
    def plot(self, picks=None, show_axes: bool = False, show: bool = True):
        """Plot the sensor positions.

        Parameters
        ----------
        picks : list | slice | None
            Channels to include. Slices and lists of integers will be interpreted as channel indices.
            None (default) will pick all channels. Note that channels in ``info['bads']`` *will be included* if their indices are explicitly provided.
        show_axes : bool
            Show layout axes if True. Defaults to False.
        show : bool
            Show figure if True. Defaults to True.

        Returns
        -------
        fig : instance of matplotlib.figure.Figure
            Figure containing the sensor topography.

        Notes
        -----
        .. versionadded:: 0.12.0
        """
        ...

def read_layout(fname=None, *, scale: bool = True):
    """Read layout from a file.

    Parameters
    ----------
    fname : path-like | str
        Either the path to a ``.lout`` or ``.lay`` file or the name of a
        built-in layout. c.f. Notes for a list of the available built-in
        layouts.
    scale : bool
        Apply useful scaling for out the box plotting using ``layout.pos``.
        Defaults to True.

    Returns
    -------
    layout : instance of Layout
        The layout.

    See Also
    --------
    Layout.save

    Notes
    -----
    Valid ``fname`` arguments are:

    .. table::
       :widths: auto

       +----------------------+
       | Kind                 |
       +======================+
       | biosemi              |
       +----------------------+
       | CTF151               |
       +----------------------+
       | CTF275               |
       +----------------------+
       | CTF-275              |
       +----------------------+
       | EEG1005              |
       +----------------------+
       | EGI256               |
       +----------------------+
       | GeodesicHeadWeb-130  |
       +----------------------+
       | GeodesicHeadWeb-280  |
       +----------------------+
       | KIT-125              |
       +----------------------+
       | KIT-157              |
       +----------------------+
       | KIT-160              |
       +----------------------+
       | KIT-AD               |
       +----------------------+
       | KIT-AS-2008          |
       +----------------------+
       | KIT-UMD-3            |
       +----------------------+
       | magnesWH3600         |
       +----------------------+
       | Neuromag_122         |
       +----------------------+
       | Vectorview-all       |
       +----------------------+
       | Vectorview-grad      |
       +----------------------+
       | Vectorview-grad_norm |
       +----------------------+
       | Vectorview-mag       |
       +----------------------+
    """
    ...

def make_eeg_layout(
    info,
    radius: float = 0.5,
    width=None,
    height=None,
    exclude: str = "bads",
    csd: bool = False,
):
    """Create .lout file from EEG electrode digitization.

    Parameters
    ----------

    info : mne.Info
        The :class:`mne.Info` object with information about the sensors and methods of measurement.
    radius : float
        Viewport radius as a fraction of main figure height. Defaults to 0.5.
    width : float | None
        Width of sensor axes as a fraction of main figure height. By default,
        this will be the maximum width possible without axes overlapping.
    height : float | None
        Height of sensor axes as a fraction of main figure height. By default,
        this will be the maximum height possible without axes overlapping.
    exclude : list of str | str
        List of channels to exclude. If empty do not exclude any.
        If 'bads', exclude channels in info['bads'] (default).
    csd : bool
        Whether the channels contain current-source-density-transformed data.

    Returns
    -------
    layout : Layout
        The generated Layout.

    See Also
    --------
    make_grid_layout, generate_2d_layout
    """
    ...

def make_grid_layout(info, picks=None, n_col=None):
    """Generate .lout file for custom data, i.e., ICA sources.

    Parameters
    ----------

    info : mne.Info
        The :class:`mne.Info` object with information about the sensors and methods of measurement.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick all good misc channels.
    n_col : int | None
        Number of columns to generate. If None, a square grid will be produced.

    Returns
    -------
    layout : Layout
        The generated layout.

    See Also
    --------
    make_eeg_layout, generate_2d_layout
    """
    ...

def find_layout(info, ch_type=None, exclude: str = "bads"):
    """Choose a layout based on the channels in the info 'chs' field.

    Parameters
    ----------

    info : mne.Info
        The :class:`mne.Info` object with information about the sensors and methods of measurement.
    ch_type : {'mag', 'grad', 'meg', 'eeg'} | None
        The channel type for selecting single channel layouts.
        Defaults to None. Note, this argument will only be considered for
        VectorView type layout. Use ``'meg'`` to force using the full layout
        in situations where the info does only contain one sensor type.
    exclude : list of str | str
        List of channels to exclude. If empty do not exclude any.
        If 'bads', exclude channels in info['bads'] (default).

    Returns
    -------
    layout : Layout instance | None
        None if layout not found.
    """
    ...

def generate_2d_layout(
    xy,
    w: float = 0.07,
    h: float = 0.05,
    pad: float = 0.02,
    ch_names=None,
    ch_indices=None,
    name: str = "ecog",
    bg_image=None,
    normalize: bool = True,
):
    """Generate a custom 2D layout from xy points.

    Generates a 2-D layout for plotting with plot_topo methods and
    functions. XY points will be normalized between 0 and 1, where
    normalization extremes will be either the min/max of xy, or
    the width/height of bg_image.

    Parameters
    ----------
    xy : ndarray, shape (N, 2)
        The xy coordinates of sensor locations.
    w : float
        The width of each sensor's axis (between 0 and 1).
    h : float
        The height of each sensor's axis (between 0 and 1).
    pad : float
        Portion of the box to reserve for padding. The value can range between
        0.0 (boxes will touch, default) to 1.0 (boxes consist of only padding).
    ch_names : list
        The names of each channel. Must be a list of strings, with one
        string per channel.
    ch_indices : list
        Index of each channel - must be a collection of unique integers,
        one index per channel.
    name : str
        The name of this layout type.
    bg_image : path-like | ndarray
        The image over which sensor axes will be plotted. Either a path to an
        image file, or an array that can be plotted with plt.imshow. If
        provided, xy points will be normalized by the width/height of this
        image. If not, xy points will be normalized by their own min/max.
    normalize : bool
        Whether to normalize the coordinates to run from 0 to 1. Defaults to
        True.

    Returns
    -------
    layout : Layout
        A Layout object that can be plotted with plot_topo
        functions and methods.

    See Also
    --------
    make_eeg_layout, make_grid_layout

    Notes
    -----
    .. versionadded:: 0.9.0
    """
    ...
