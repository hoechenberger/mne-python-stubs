from ..utils import (
    fill_doc as fill_doc,
    logger as logger,
    object_diff as object_diff,
    warn as warn,
)
from .constants import FIFF as FIFF
from .pick import pick_info as pick_info, pick_types as pick_types
from .tag import find_tag as find_tag
from .tree import dir_tree_find as dir_tree_find
from .write import (
    end_block as end_block,
    start_block as start_block,
    write_float as write_float,
    write_float_matrix as write_float_matrix,
    write_int as write_int,
    write_name_list_sanitized as write_name_list_sanitized,
    write_string as write_string,
)

class Projection(dict):
    """### Dictionary-like object holding a projection vector.

    Projection vectors are stored in a list in ``inst.info["projs"]``. Each projection
    vector has 5 keys: ``active``, ``data``, ``desc``, ``explained_var``, ``kind``.

    ### ⛔️ Warning This class is generally not meant to be instantiated
                 directly, use ``compute_proj_*`` functions instead.

    ### 🛠️ Parameters
    ----------
    data : dict
        The data dictionary.
    desc : str
        The projector description.
    kind : int
        The projector kind.
    active : bool
        Whether or not the projector has been applied.
    explained_var : float | None
        The proportion of explained variance.
    """

    def __init__(
        self,
        *,
        data,
        desc: str = "",
        kind=...,
        active: bool = False,
        explained_var=None,
    ) -> None: ...
    def __deepcopy__(self, memodict):
        """### Make a deepcopy."""
        ...
    def __eq__(self, other):
        """### Equality == method."""
        ...
    def __ne__(self, other):
        """### Different != method."""
        ...
    def plot_topomap(
        self,
        info,
        *,
        sensors: bool = True,
        show_names: bool = False,
        contours: int = 6,
        outlines: str = "head",
        sphere=None,
        image_interp="cubic",
        extrapolate="auto",
        border="mean",
        res: int = 64,
        size: int = 1,
        cmap=None,
        vlim=(None, None),
        cnorm=None,
        colorbar: bool = False,
        cbar_fmt: str = "%3.1f",
        units=None,
        axes=None,
        show: bool = True,
    ):
        """### Plot topographic maps of SSP projections.

        ### 🛠️ Parameters
        ----------

        info : mne.Info
            The `mne.Info` object with information about the sensors and methods of measurement. Used to determine the layout.

        sensors : bool | str
            Whether to add markers for sensor locations. If `str`, should be a
            valid matplotlib format string (e.g., ``'r+'`` for red plusses, see the
            Notes section of `matplotlib.axes.Axes.plot`). If ``True`` (the
            default), black circles will be used.

        show_names : bool | callable
            If ``True``, show channel names next to each sensor marker. If callable,
            channel names will be formatted using the callable; e.g., to
            delete the prefix 'MEG ' from all channel names, pass the function
            ``lambda x: x.replace('MEG ', '')``. If ``mask`` is not ``None``, only
            non-masked sensor names will be shown.

            ✨ Added in vesion 1.2

        contours : int | array-like
            The number of contour lines to draw. If ``0``, no contours will be drawn.
            If a positive integer, that number of contour levels are chosen using the
            matplotlib tick locator (may sometimes be inaccurate, use array for
            accuracy). If array-like, the array values are used as the contour levels.
            The values should be in µV for EEG, fT for magnetometers and fT/m for
            gradiometers. If ``colorbar=True``, the colorbar will have ticks
            corresponding to the contour levels. Default is ``6``.

        outlines : 'head' | dict | None
            The outlines to be drawn. If 'head', the default head scheme will be
            drawn. If dict, each key refers to a tuple of x and y positions, the values
            in 'mask_pos' will serve as image mask.
            Alternatively, a matplotlib patch object can be passed for advanced
            masking options, either directly or as a function that returns patches
            (required for multi-axis plots). If None, nothing will be drawn.
            Defaults to 'head'.
        sphere : float | array-like | instance of ConductorModel | None  | 'auto' | 'eeglab'
            The sphere parameters to use for the head outline. Can be array-like of
            shape (4,) to give the X/Y/Z origin and radius in meters, or a single float
            to give just the radius (origin assumed 0, 0, 0). Can also be an instance
            of a spherical `mne.bem.ConductorModel` to use the origin and
            radius from that object. If ``'auto'`` the sphere is fit to digitization
            points. If ``'eeglab'`` the head circle is defined by EEG electrodes
            ``'Fpz'``, ``'Oz'``, ``'T7'``, and ``'T8'`` (if ``'Fpz'`` is not present,
            it will be approximated from the coordinates of ``'Oz'``). ``None`` (the
            default) is equivalent to ``'auto'`` when enough extra digitization points
            are available, and (0, 0, 0, 0.095) otherwise.

            ✨ Added in vesion 0.20
            🎭 Changed in version 1.1 Added ``'eeglab'`` option.

        image_interp : str
            The image interpolation to be used. Options are ``'cubic'`` (default)
            to use `scipy.interpolate.CloughTocher2DInterpolator`,
            ``'nearest'`` to use `scipy.spatial.Voronoi` or
            ``'linear'`` to use `scipy.interpolate.LinearNDInterpolator`.

        extrapolate : str
            Options:

            - ``'box'``
                Extrapolate to four points placed to form a square encompassing all
                data points, where each side of the square is three times the range
                of the data in the respective dimension.
            - ``'local'`` (default for MEG sensors)
                Extrapolate only to nearby points (approximately to points closer than
                median inter-electrode distance). This will also set the
                mask to be polygonal based on the convex hull of the sensors.
            - ``'head'`` (default for non-MEG sensors)
                Extrapolate out to the edges of the clipping circle. This will be on
                the head circle when the sensors are contained within the head circle,
                but it can extend beyond the head when sensors are plotted outside
                the head circle.

            ✨ Added in vesion 1.2

        border : float | 'mean'
            Value to extrapolate to on the topomap borders. If ``'mean'`` (default),
            then each extrapolated point has the average value of its neighbours.

            ✨ Added in vesion 0.20

        res : int
            The resolution of the topomap image (number of pixels along each side).

        size : float
            Side length of each subplot in inches.

        cmap : matplotlib colormap | (colormap, bool) | 'interactive' | None
            Colormap to use. If `tuple`, the first value indicates the colormap
            to use and the second value is a boolean defining interactivity. In
            interactive mode the colors are adjustable by clicking and dragging the
            colorbar with left and right mouse button. Left mouse button moves the
            scale up and down and right mouse button adjusts the range. Hitting
            space bar resets the range. Up and down arrows can be used to change
            the colormap. If ``None``, ``'Reds'`` is used for data that is either
            all-positive or all-negative, and ``'RdBu_r'`` is used otherwise.
            ``'interactive'`` is equivalent to ``(None, True)``. Defaults to ``None``.

            ### ⛔️ Warning  Interactive mode works smoothly only for a small amount
                of topomaps. Interactive mode is disabled by default for more than
                2 topomaps.

        vlim : tuple of length 2 | 'joint'
            Colormap limits to use. If a `tuple` of floats, specifies the
            lower and upper bounds of the colormap (in that order); providing
            ``None`` for either entry will set the corresponding boundary at the
            min/max of the data (separately for each projector). Elements of the `tuple` may also be callable functions which take in a `NumPy array <numpy.ndarray>` and return a scalar. If ``vlim='joint'``, will compute the colormap limits jointly across all projectors of the same channel type, using the min/max of the data for that channel type. If vlim is ``'joint'``, ``info`` must not be ``None``. Defaults to ``(None, None)``.

        cnorm : matplotlib.colors.Normalize | None
            How to normalize the colormap. If ``None``, standard linear normalization
            is performed. If not ``None``, ``vmin`` and ``vmax`` will be ignored.
            See `Matplotlib docs <matplotlib:colormapnorms>`
            for more details on colormap normalization, and
            `the ERDs example<cnorm-example>` for an example of its use.

            ✨ Added in vesion 1.2

        colorbar : bool
            Plot a colorbar in the rightmost column of the figure.
        cbar_fmt : str
            Formatting string for colorbar tick labels. See `formatspec` for
            details.

            ✨ Added in vesion 1.2

        units : str | None
            The units to use for the colorbar label. Ignored if ``colorbar=False``.
            If ``None`` the label will be "AU" indicating arbitrary units.
            Default is ``None``.

            ✨ Added in vesion 1.2
        axes : instance of Axes | list of Axes | None
            The axes to plot to. If ``None``, a new `matplotlib.figure.Figure`
            will be created with the correct number of axes. If `matplotlib.axes.Axes` are provided (either as a single instance or a `list` of axes), the number of axes provided must match the number of projectors.Default is ``None``.
        show : bool
            Show the figure if ``True``.

        ### ⏎ Returns
        -------
        fig : instance of Figure
            Figure distributing one image per channel across sensor topography.

        ### 📖 Notes
        -----
        ✨ Added in vesion 0.15.0
        """
        ...

class ProjMixin:
    """### Mixin class for Raw, Evoked, Epochs.

    ### 📖 Notes
    -----
    This mixin adds a proj attribute as a property to data containers.
    It is True if at least one proj is present and all of them are active.
    The projs might not be applied yet if data are not preloaded. In
    this case it's the _projector attribute that does the job.
    If a private _data attribute is present then the projs applied
    to it are the ones marked as active.

    A proj parameter passed in constructor of raw or epochs calls
    apply_proj and hence after the .proj attribute is True.

    As soon as you've applied the projs it will stay active in the
    remaining pipeline.

    The suggested pipeline is proj=True in epochs (it's cheaper than for raw).

    When you use delayed SSP in Epochs, projs are applied when you call
    get_data() method. They are not applied to the evoked._data unless you call
    apply_proj(). The reason is that you want to reject with projs although
    it's not stored in proj mode.
    """

    @property
    def proj(self):
        """### Whether or not projections are active."""
        ...
    def add_proj(self, projs, remove_existing: bool = False, verbose=None):
        """### Add SSP projection vectors.

        ### 🛠️ Parameters
        ----------
        projs : list
            List with projection vectors.
        remove_existing : bool
            Remove the projection vectors currently in the file.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        ### ⏎ Returns
        -------
        self : instance of Raw | Epochs | Evoked
            The data container.
        """
        ...
    def apply_proj(self, verbose=None):
        """### Apply the signal space projection (SSP) operators to the data.

        ### 🛠️ Parameters
        ----------

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        ### ⏎ Returns
        -------
        self : instance of Raw | Epochs | Evoked
            The instance.

        ### 📖 Notes
        -----
        Once the projectors have been applied, they can no longer be
        removed. It is usually not recommended to apply the projectors at
        too early stages, as they are applied automatically later on
        (e.g. when computing inverse solutions).
        Hint: using the copy method individual projection vectors
        can be tested without affecting the original data.
        With evoked data, consider the following example::

            projs_a = mne.read_proj('proj_a.fif')
            projs_b = mne.read_proj('proj_b.fif')
            # add the first, copy, apply and see ...
            evoked.add_proj(a).copy().apply_proj().plot()
            # add the second, copy, apply and see ...
            evoked.add_proj(b).copy().apply_proj().plot()
            # drop the first and see again
            evoked.copy().del_proj(0).apply_proj().plot()
            evoked.apply_proj()  # finally keep both
        """
        ...
    def del_proj(self, idx: str = "all"):
        """### Remove SSP projection vector.

        ### 💡 Note The projection vector can only be removed if it is inactive
                  (has not been applied to the data).

        ### 🛠️ Parameters
        ----------
        idx : int | list of int | str
            Index of the projector to remove. Can also be "all" (default)
            to remove all projectors.

        ### ⏎ Returns
        -------
        self : instance of Raw | Epochs | Evoked
            The instance.
        """
        ...
    def plot_projs_topomap(
        self,
        ch_type=None,
        *,
        sensors: bool = True,
        show_names: bool = False,
        contours: int = 6,
        outlines: str = "head",
        sphere=None,
        image_interp="cubic",
        extrapolate="auto",
        border="mean",
        res: int = 64,
        size: int = 1,
        cmap=None,
        vlim=(None, None),
        cnorm=None,
        colorbar: bool = False,
        cbar_fmt: str = "%3.1f",
        units=None,
        axes=None,
        show: bool = True,
    ):
        """### Plot SSP vector.

        ### 🛠️ Parameters
        ----------
        ch_type : 'mag' | 'grad' | 'planar1' | 'planar2' | 'eeg' | None | list
            The channel type to plot. For ``'grad'``, the gradiometers are
            collected in pairs and the RMS for each pair is plotted. If
            ``None`` it will return all channel types present.. If a list of ch_types is provided, it will return multiple figures. Defaults to ``None``.

        sensors : bool | str
            Whether to add markers for sensor locations. If `str`, should be a
            valid matplotlib format string (e.g., ``'r+'`` for red plusses, see the
            Notes section of `matplotlib.axes.Axes.plot`). If ``True`` (the
            default), black circles will be used.

        show_names : bool | callable
            If ``True``, show channel names next to each sensor marker. If callable,
            channel names will be formatted using the callable; e.g., to
            delete the prefix 'MEG ' from all channel names, pass the function
            ``lambda x: x.replace('MEG ', '')``. If ``mask`` is not ``None``, only
            non-masked sensor names will be shown.

            ✨ Added in vesion 1.2

        contours : int | array-like
            The number of contour lines to draw. If ``0``, no contours will be drawn.
            If a positive integer, that number of contour levels are chosen using the
            matplotlib tick locator (may sometimes be inaccurate, use array for
            accuracy). If array-like, the array values are used as the contour levels.
            The values should be in µV for EEG, fT for magnetometers and fT/m for
            gradiometers. If ``colorbar=True``, the colorbar will have ticks
            corresponding to the contour levels. Default is ``6``.

        outlines : 'head' | dict | None
            The outlines to be drawn. If 'head', the default head scheme will be
            drawn. If dict, each key refers to a tuple of x and y positions, the values
            in 'mask_pos' will serve as image mask.
            Alternatively, a matplotlib patch object can be passed for advanced
            masking options, either directly or as a function that returns patches
            (required for multi-axis plots). If None, nothing will be drawn.
            Defaults to 'head'.
        sphere : float | array-like | instance of ConductorModel | None  | 'auto' | 'eeglab'
            The sphere parameters to use for the head outline. Can be array-like of
            shape (4,) to give the X/Y/Z origin and radius in meters, or a single float
            to give just the radius (origin assumed 0, 0, 0). Can also be an instance
            of a spherical `mne.bem.ConductorModel` to use the origin and
            radius from that object. If ``'auto'`` the sphere is fit to digitization
            points. If ``'eeglab'`` the head circle is defined by EEG electrodes
            ``'Fpz'``, ``'Oz'``, ``'T7'``, and ``'T8'`` (if ``'Fpz'`` is not present,
            it will be approximated from the coordinates of ``'Oz'``). ``None`` (the
            default) is equivalent to ``'auto'`` when enough extra digitization points
            are available, and (0, 0, 0, 0.095) otherwise.

            ✨ Added in vesion 0.20
            🎭 Changed in version 1.1 Added ``'eeglab'`` option.

        image_interp : str
            The image interpolation to be used. Options are ``'cubic'`` (default)
            to use `scipy.interpolate.CloughTocher2DInterpolator`,
            ``'nearest'`` to use `scipy.spatial.Voronoi` or
            ``'linear'`` to use `scipy.interpolate.LinearNDInterpolator`.

        extrapolate : str
            Options:

            - ``'box'``
                Extrapolate to four points placed to form a square encompassing all
                data points, where each side of the square is three times the range
                of the data in the respective dimension.
            - ``'local'`` (default for MEG sensors)
                Extrapolate only to nearby points (approximately to points closer than
                median inter-electrode distance). This will also set the
                mask to be polygonal based on the convex hull of the sensors.
            - ``'head'`` (default for non-MEG sensors)
                Extrapolate out to the edges of the clipping circle. This will be on
                the head circle when the sensors are contained within the head circle,
                but it can extend beyond the head when sensors are plotted outside
                the head circle.

            ✨ Added in vesion 0.20

            🎭 Changed in version 0.21

               - The default was changed to ``'local'`` for MEG sensors.
               - ``'local'`` was changed to use a convex hull mask
               - ``'head'`` was changed to extrapolate out to the clipping circle.

        border : float | 'mean'
            Value to extrapolate to on the topomap borders. If ``'mean'`` (default),
            then each extrapolated point has the average value of its neighbours.

            ✨ Added in vesion 0.20

        res : int
            The resolution of the topomap image (number of pixels along each side).

        size : float
            Side length of each subplot in inches.
            Only applies when plotting multiple topomaps at a time.

        cmap : matplotlib colormap | (colormap, bool) | 'interactive' | None
            Colormap to use. If `tuple`, the first value indicates the colormap
            to use and the second value is a boolean defining interactivity. In
            interactive mode the colors are adjustable by clicking and dragging the
            colorbar with left and right mouse button. Left mouse button moves the
            scale up and down and right mouse button adjusts the range. Hitting
            space bar resets the range. Up and down arrows can be used to change
            the colormap. If ``None``, ``'Reds'`` is used for data that is either
            all-positive or all-negative, and ``'RdBu_r'`` is used otherwise.
            ``'interactive'`` is equivalent to ``(None, True)``. Defaults to ``None``.

            ### ⛔️ Warning  Interactive mode works smoothly only for a small amount
                of topomaps. Interactive mode is disabled by default for more than
                2 topomaps.

        vlim : tuple of length 2 | 'joint'
            Colormap limits to use. If a `tuple` of floats, specifies the
            lower and upper bounds of the colormap (in that order); providing
            ``None`` for either entry will set the corresponding boundary at the
            min/max of the data (separately for each projector). Elements of the `tuple` may also be callable functions which take in a `NumPy array <numpy.ndarray>` and return a scalar. If ``vlim='joint'``, will compute the colormap limits jointly across all projectors of the same channel type, using the min/max of the data for that channel type. If vlim is ``'joint'``, ``info`` must not be ``None``. Defaults to ``(None, None)``.

        cnorm : matplotlib.colors.Normalize | None
            How to normalize the colormap. If ``None``, standard linear normalization
            is performed. If not ``None``, ``vmin`` and ``vmax`` will be ignored.
            See `Matplotlib docs <matplotlib:colormapnorms>`
            for more details on colormap normalization, and
            `the ERDs example<cnorm-example>` for an example of its use.

            ✨ Added in vesion 1.2

        colorbar : bool
            Plot a colorbar in the rightmost column of the figure.
        cbar_fmt : str
            Formatting string for colorbar tick labels. See `formatspec` for
            details.

            ✨ Added in vesion 1.2

        units : str | None
            The units to use for the colorbar label. Ignored if ``colorbar=False``.
            If ``None`` the label will be "AU" indicating arbitrary units.
            Default is ``None``.

            ✨ Added in vesion 1.2
        axes : instance of Axes | list of Axes | None
            The axes to plot to. If ``None``, a new `matplotlib.figure.Figure`
            will be created with the correct number of axes. If `matplotlib.axes.Axes` are provided (either as a single instance or a `list` of axes), the number of axes provided must match the number of projectors.Default is ``None``.
        show : bool
            Show the figure if ``True``.

        ### ⏎ Returns
        -------
        fig : instance of Figure
            Figure distributing one image per channel across sensor topography.
        """
        ...

def make_projector(projs, ch_names, bads=(), include_active: bool = True):
    """### Create an SSP operator from SSP projection vectors.

    ### 🛠️ Parameters
    ----------
    projs : list
        List of projection vectors.
    ch_names : list of str
        List of channels to include in the projection matrix.
    bads : list of str
        Some bad channels to exclude. If bad channels were marked
        in the raw file when projs were calculated using mne-python,
        they should not need to be included here as they will
        have been automatically omitted from the projectors.
    include_active : bool
        Also include projectors that are already active.

    ### ⏎ Returns
    -------
    proj : array of shape [n_channels, n_channels]
        The projection operator to apply to the data.
    nproj : int
        How many items in the projector.
    U : array
        The orthogonal basis of the projection vectors.
    """
    ...

def make_projector_info(info, include_active: bool = True):
    """### Make an SSP operator using the measurement info.

    Calls make_projector on good channels.

    ### 🛠️ Parameters
    ----------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    include_active : bool
        Also include projectors that are already active.

    ### ⏎ Returns
    -------
    proj : array of shape [n_channels, n_channels]
        The projection operator to apply to the data.
    nproj : int
        How many items in the projector.
    """
    ...

def activate_proj(projs, copy: bool = True, verbose=None):
    """### Set all projections to active.

    Useful before passing them to make_projector.

    ### 🛠️ Parameters
    ----------
    projs : list
        The projectors.
    copy : bool
        Modify projs in place or operate on a copy.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    projs : list
        The projectors.
    """
    ...

def deactivate_proj(projs, copy: bool = True, verbose=None):
    """### Set all projections to inactive.

    Useful before saving raw data without projectors applied.

    ### 🛠️ Parameters
    ----------
    projs : list
        The projectors.
    copy : bool
        Modify projs in place or operate on a copy.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    projs : list
        The projectors.
    """
    ...

def make_eeg_average_ref_proj(
    info, activate: bool = True, *, ch_type: str = "eeg", verbose=None
):
    """### Create an EEG average reference SSP projection vector.

    ### 🛠️ Parameters
    ----------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    activate : bool
        If True projections are activated.
    ch_type : str
        The channel type to use for reference projection.
        Valid types are ``'eeg'``, ``'ecog'``, ``'seeg'`` and ``'dbs'``.

        ✨ Added in vesion 1.2

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    proj: instance of Projection
        The SSP/PCA projector.
    """
    ...

def setup_proj(
    info,
    add_eeg_ref: bool = True,
    activate: bool = True,
    *,
    eeg_ref_ch_type: str = "eeg",
    verbose=None,
):
    """### Set up projection for Raw and Epochs.

    ### 🛠️ Parameters
    ----------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement. Warning: will be modified in-place.
    add_eeg_ref : bool
        If True, an EEG average reference will be added (unless one
        already exists).
    activate : bool
        If True projections are activated.
    eeg_ref_ch_type : str
        The channel type to use for reference projection.
        Valid types are 'eeg', 'ecog', 'seeg' and 'dbs'.

        ✨ Added in vesion 1.2

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    projector : array of shape [n_channels, n_channels]
        The projection operator to apply to the data.
    info : mne.Info
        The modified measurement info.
    """
    ...
