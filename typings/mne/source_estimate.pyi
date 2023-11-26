from ._fiff.constants import FIFF as FIFF
from ._fiff.meas_info import Info as Info
from ._fiff.pick import pick_types as pick_types
from ._freesurfer import read_freesurfer_lut as read_freesurfer_lut
from .baseline import rescale as rescale
from .cov import Covariance as Covariance
from .filter import resample as resample
from .source_space._source_space import SourceSpaces as SourceSpaces
from .surface import mesh_edges as mesh_edges, read_surface as read_surface
from .transforms import apply_trans as apply_trans
from .utils import (
    TimeMixin as TimeMixin,
    copy_function_doc_to_method_doc as copy_function_doc_to_method_doc,
    fill_doc as fill_doc,
    get_subjects_dir as get_subjects_dir,
    logger as logger,
    object_size as object_size,
    sizeof_fmt as sizeof_fmt,
    warn as warn,
)
from .viz import (
    plot_source_estimates as plot_source_estimates,
    plot_vector_source_estimates as plot_vector_source_estimates,
    plot_volume_source_estimates as plot_volume_source_estimates,
)
from _typeshed import Incomplete

def read_source_estimate(fname, subject=None):
    """Read a source estimate object.

    Parameters
    ----------
    fname : path-like
        Path to (a) source-estimate file(s).
    subject : str | None
        Name of the subject the source estimate(s) is (are) from.
        It is good practice to set this attribute to avoid combining
        incompatible labels and SourceEstimates (e.g., ones from other
        subjects). Note that due to file specification limitations, the
        subject name isn't saved to or loaded from files written to disk.

    Returns
    -------
    stc : SourceEstimate | VectorSourceEstimate | VolSourceEstimate | MixedSourceEstimate
        The source estimate object loaded from file.

    Notes
    -----
     - for volume source estimates, ``fname`` should provide the path to a
       single file named ``'*-vl.stc``` or ``'*-vol.stc'``
     - for surface source estimates, ``fname`` should either provide the
       path to the file corresponding to a single hemisphere (``'*-lh.stc'``,
       ``'*-rh.stc'``) or only specify the asterisk part in these patterns. In
       any case, the function expects files for both hemisphere with names
       following this pattern.
     - for vector surface source estimates, only HDF5 files are supported.
     - for mixed source estimates, only HDF5 files are supported.
     - for single time point ``.w`` files, ``fname`` should follow the same
       pattern as for surface estimates, except that files are named
       ``'*-lh.w'`` and ``'*-rh.w'``.
    """
    ...

class _BaseSourceEstimate(TimeMixin):
    vertices: Incomplete
    subject: Incomplete

    def __init__(
        self, data, vertices, tmin, tstep, subject=None, verbose=None
    ) -> None: ...
    def get_peak(
        self,
        tmin=None,
        tmax=None,
        mode: str = "abs",
        vert_as_index: bool = False,
        time_as_index: bool = False,
    ):
        """Get location and latency of peak amplitude.

        Parameters
        ----------

        tmin : float | None
            The minimum point in time to be considered for peak getting.
        tmax : float | None
            The maximum point in time to be considered for peak getting.
        mode : {'pos', 'neg', 'abs'}
            How to deal with the sign of the data. If 'pos' only positive
            values will be considered. If 'neg' only negative values will
            be considered. If 'abs' absolute values will be considered.
            Defaults to 'abs'.
        vert_as_index : bool
            Whether to return the vertex index (True) instead of of its ID
            (False, default).
        time_as_index : bool
            Whether to return the time index (True) instead of the latency
            (False, default).

        Returns
        -------
        pos : int
            The vertex exhibiting the maximum response, either ID or index.
        latency : float
            The latency in seconds.
        """
        ...
    def extract_label_time_course(
        self, labels, src, mode: str = "auto", allow_empty: bool = False, verbose=None
    ):
        """Extract label time courses for lists of labels.

        This function will extract one time course for each label. The way the
        time courses are extracted depends on the mode parameter.

        Parameters
        ----------

        labels : Label | BiHemiLabel | list | tuple | str
            If using a surface or mixed source space, this should be the
            :class:mne.Label`'s for which to extract the time course.
            If working with whole-brain volume source estimates, this must be one of:

            - a string path to a FreeSurfer atlas for the subject (e.g., their
              'aparc.a2009s+aseg.mgz') to extract time courses for all volumes in the
              atlas
            - a two-element list or tuple, the first element being a path to an atlas,
              and the second being a list or dict of ``volume_labels`` to extract
              (see :func:`mne.setup_volume_source_space` for details).

            .. versionchanged:: 0.21.0
               Support for volume source estimates.

        src : instance of SourceSpaces
            The source spaces for the source time courses.

        mode : str
            Extraction mode, see Notes.

        allow_empty : bool | str
            ``False`` (default) will emit an error if there are labels that have no
            vertices in the source estimate. ``True`` and ``'ignore'`` will return
            all-zero time courses for labels that do not have any vertices in the
            source estimate, and True will emit a warning while and "ignore" will
            just log a message.

            .. versionchanged:: 0.21.0
               Support for "ignore".

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------

        label_tc : array | list (or generator) of array, shape (n_labels[, n_orient], n_times)
            Extracted time course for each label and source estimate.

        See Also
        --------
        extract_label_time_course : Extract time courses for multiple STCs.

        Notes
        -----

        Valid values for ``mode`` are:

        - ``'max'``
            Maximum value across vertices at each time point within each label.
        - ``'mean'``
            Average across vertices at each time point within each label. Ignores
            orientation of sources for standard source estimates, which varies
            across the cortical surface, which can lead to cancellation.
            Vector source estimates are always in XYZ / RAS orientation, and are thus
            already geometrically aligned.
        - ``'mean_flip'``
            Finds the dominant direction of source space normal vector orientations
            within each label, applies a sign-flip to time series at vertices whose
            orientation is more than 180° different from the dominant direction, and
            then averages across vertices at each time point within each label.
        - ``'pca_flip'``
            Applies singular value decomposition to the time courses within each label,
            and uses the first right-singular vector as the representative label time
            course. This signal is scaled so that its power matches the average
            (per-vertex) power within the label, and sign-flipped by multiplying by
            ``np.sign(u @ flip)``, where ``u`` is the first left-singular vector and
            ``flip`` is the same sign-flip vector used when ``mode='mean_flip'``. This
            sign-flip ensures that extracting time courses from the same label in
            similar STCs does not result in 180° direction/phase changes.
        - ``'auto'`` (default)
            Uses ``'mean_flip'`` when a standard source estimate is applied, and
            ``'mean'`` when a vector source estimate is supplied.
        - ``None``
            No aggregation is performed, and an array of shape ``(n_vertices, n_times)`` is
            returned.

            .. versionadded:: 0.21
               Support for ``'auto'``, vector, and volume source estimates.

        The only modes that work for vector and volume source estimates are ``'mean'``,
        ``'max'``, and ``'auto'``.
        """
        ...
    def apply_baseline(self, baseline=(None, 0), *, verbose=None):
        """Baseline correct source estimate data.

        Parameters
        ----------

        baseline : None | tuple of length 2
            The time interval to consider as "baseline" when applying baseline
            correction. If ``None``, do not apply baseline correction.
            If a tuple ``(a, b)``, the interval is between ``a`` and ``b``
            (in seconds), including the endpoints.
            If ``a`` is ``None``, the **beginning** of the data is used; and if ``b``
            is ``None``, it is set to the **end** of the interval.
            If ``(None, None)``, the entire time interval is used.

            .. note:: The baseline ``(a, b)`` includes both endpoints, i.e. all
                        timepoints ``t`` such that ``a <= t <= b``.

            Correction is applied **to each source individually** in the following
            way:

            1. Calculate the mean signal of the baseline period.
            2. Subtract this mean from the **entire** source estimate data.

            .. note:: Baseline correction is appropriate when signal and noise are
                      approximately additive, and the noise level can be estimated from
                      the baseline interval. This can be the case for non-normalized
                      source activities (e.g. signed and unsigned MNE), but it is not
                      the case for normalized estimates (e.g. signal-to-noise ratios,
                      dSPM, sLORETA).

            Defaults to ``(None, 0)``, i.e. beginning of the the data until
            time point zero.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        stc : instance of SourceEstimate
            The baseline-corrected source estimate object.

        Notes
        -----
        Baseline correction can be done multiple times.
        """
        ...
    def save(
        self, fname, ftype: str = "h5", *, overwrite: bool = False, verbose=None
    ) -> None:
        """Save the full source estimate to an HDF5 file.

        Parameters
        ----------
        fname : path-like
            The file name to write the source estimate to, should end in
            ``'-stc.h5'``.
        ftype : str
            File format to use. Currently, the only allowed values is ``"h5"``.

        overwrite : bool
            If True (default False), overwrite the destination file if it
            exists.

            .. versionadded:: 1.0

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.
        """
        ...
    def plot(
        self,
        subject=None,
        surface: str = "inflated",
        hemi: str = "lh",
        colormap: str = "auto",
        time_label: str = "auto",
        smoothing_steps: int = 10,
        transparent: bool = True,
        alpha: float = 1.0,
        time_viewer: str = "auto",
        subjects_dir=None,
        figure=None,
        views: str = "auto",
        colorbar: bool = True,
        clim: str = "auto",
        cortex: str = "classic",
        size: int = 800,
        background: str = "black",
        foreground=None,
        initial_time=None,
        time_unit: str = "s",
        backend: str = "auto",
        spacing: str = "oct6",
        title=None,
        show_traces: str = "auto",
        src=None,
        volume_options: float = 1.0,
        view_layout: str = "vertical",
        add_data_kwargs=None,
        brain_kwargs=None,
        verbose=None,
    ):
        """Plot SourceEstimate.

        Parameters
        ----------
        subject : str | None
            The FreeSurfer subject name.
            If ``None``, ``stc.subject`` will be used.
        surface : str
            The type of surface (inflated, white etc.).
        hemi : str
            Hemisphere id (ie ``'lh'``, ``'rh'``, ``'both'``, or ``'split'``). In
            the case of ``'both'``, both hemispheres are shown in the same window.
            In the case of ``'split'`` hemispheres are displayed side-by-side
            in different viewing panes.

        colormap : str | np.ndarray of float, shape(n_colors, 3 | 4)
            Name of colormap to use or a custom look up table. If array, must
            be (n x 3) or (n x 4) array for with RGB or RGBA values between
            0 and 255.
            The default ('auto') uses ``'hot'`` for one-sided data and
            'mne' for two-sided data.

        time_label : str | callable | None
            Format of the time label (a format string, a function that maps
            floating point time values to strings, or None for no label). The
            default is ``'auto'``, which will use ``time=%0.2f ms`` if there
            is more than one time point.
        smoothing_steps : int
            The amount of smoothing.

        transparent : bool | None
            If True: use a linear transparency between fmin and fmid
            and make values below fmin fully transparent (symmetrically for
            divergent colormaps). None will choose automatically based on colormap
            type.
        alpha : float
            Alpha value to apply globally to the overlay. Has no effect with mpl
            backend.
        time_viewer : bool | str
            Display time viewer GUI. Can also be 'auto', which will mean True
            for the PyVista backend and False otherwise.

            .. versionchanged:: 0.20.0
               "auto" mode added.

        subjects_dir : path-like | None
            The path to the directory containing the FreeSurfer subjects
            reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
            variable.
        figure : instance of Figure3D | instance of matplotlib.figure.Figure | list | int | None
            If None, a new figure will be created. If multiple views or a
            split view is requested, this must be a list of the appropriate
            length. If int is provided it will be used to identify the PyVista
            figure by it's id or create a new figure with the given id. If an
            instance of matplotlib figure, mpl backend is used for plotting.

        views : str | list
            View to use. Using multiple views (list) is not supported for mpl
            backend. See :meth:`Brain.show_view <mne.viz.Brain.show_view>` for
            valid string options.

            When plotting a standard SourceEstimate (not volume, mixed, or vector)
            and using the PyVista backend, ``views='flat'`` is also supported to
            plot cortex as a flatmap.

            Using multiple views (list) is not supported by the matplotlib backend.

            .. versionchanged:: 0.21.0
               Support for flatmaps.
        colorbar : bool
            If True, display colorbar on scene.

        clim : str | dict
            Colorbar properties specification. If 'auto', set clim automatically
            based on data percentiles. If dict, should contain:

                ``kind`` : 'value' | 'percent'
                    Flag to specify type of limits.
                ``lims`` : list | np.ndarray | tuple of float, 3 elements
                    Lower, middle, and upper bounds for colormap.
                ``pos_lims`` : list | np.ndarray | tuple of float, 3 elements
                    Lower, middle, and upper bound for colormap. Positive values
                    will be mirrored directly across zero during colormap
                    construction to obtain negative control points.

            .. note:: Only one of ``lims`` or ``pos_lims`` should be provided.
                      Only sequential colormaps should be used with ``lims``, and
                      only divergent colormaps should be used with ``pos_lims``.
        cortex : str | tuple
            Specifies how binarized curvature values are rendered.
            Either the name of a preset Brain cortex colorscheme (one of
            ``'classic'``, ``'bone'``, ``'low_contrast'``, or ``'high_contrast'``),
            or the name of a colormap, or a tuple with values
            ``(colormap, min, max, reverse)`` to fully specify the curvature
            colors. Has no effect with the matplotlib backend.
        size : float or tuple of float
            The size of the window, in pixels. can be one number to specify
            a square window, or the (width, height) of a rectangular window.
            Has no effect with mpl backend.
        background : matplotlib color
            Color of the background of the display window.
        foreground : matplotlib color | None
            Color of the foreground of the display window. Has no effect with mpl
            backend. None will choose white or black based on the background color.
        initial_time : float | None
            The time to display on the plot initially. ``None`` to display the
            first time sample (default).
        time_unit : ``'s'`` | ``'ms'``
            Whether time is represented in seconds ("s", default) or
            milliseconds ("ms").
        backend : ``'auto'`` | ``'pyvistaqt'`` | ``'matplotlib'``
            Which backend to use. If ``'auto'`` (default), tries to plot with
            pyvistaqt, but resorts to matplotlib if no 3d backend is available.

            .. versionadded:: 0.15.0
        spacing : str
            Only affects the matplotlib backend.
            The spacing to use for the source space. Can be ``'ico#'`` for a
            recursively subdivided icosahedron, ``'oct#'`` for a recursively
            subdivided octahedron, or ``'all'`` for all points. In general, you can
            speed up the plotting by selecting a sparser source space.
            Defaults  to 'oct6'.

            .. versionadded:: 0.15.0
        title : str | None
            Title for the figure. If None, the subject name will be used.

            .. versionadded:: 0.17.0

        show_traces : bool | str | float
            If True, enable interactive picking of a point on the surface of the
            brain and plot its time course.
            This feature is only available with the PyVista 3d backend, and requires
            ``time_viewer=True``. Defaults to 'auto', which will use True if and
            only if ``time_viewer=True``, the backend is PyVista, and there is more
            than one time point. If float (between zero and one), it specifies what
            proportion of the total window should be devoted to traces (True is
            equivalent to 0.25, i.e., it will occupy the bottom 1/4 of the figure).

            .. versionadded:: 0.20.0

        src : instance of SourceSpaces | None
            The source space corresponding to the source estimate. Only necessary
            if the STC is a volume or mixed source estimate.
        volume_options : float | dict | None
            Options for volumetric source estimate plotting, with key/value pairs:

            - ``'resolution'`` : float | None
                Resolution (in mm) of volume rendering. Smaller (e.g., 1.) looks
                better at the cost of speed. None (default) uses the volume source
                space resolution, which is often something like 7 or 5 mm,
                without resampling.
            - ``'blending'`` : str
                Can be "mip" (default) for :term:`maximum intensity projection` or
                "composite" for composite blending using alpha values.
            - ``'alpha'`` : float | None
                Alpha for the volumetric rendering. Defaults are 0.4 for vector source
                estimates and 1.0 for scalar source estimates.
            - ``'surface_alpha'`` : float | None
                Alpha for the surface enclosing the volume(s). None (default) will use
                half the volume alpha. Set to zero to avoid plotting the surface.
            - ``'silhouette_alpha'`` : float | None
                Alpha for a silhouette along the outside of the volume. None (default)
                will use ``0.25 * surface_alpha``.
            - ``'silhouette_linewidth'`` : float
                The line width to use for the silhouette. Default is 2.

            A float input (default 1.) or None will be used for the ``'resolution'``
            entry.

        view_layout : str
            Can be "vertical" (default) or "horizontal". When using "horizontal" mode,
            the PyVista backend must be used and hemi cannot be "split".

        add_data_kwargs : dict | None
            Additional arguments to brain.add_data (e.g.,
            ``dict(time_label_size=10)``).

        brain_kwargs : dict | None
            Additional arguments to the :class:`mne.viz.Brain` constructor (e.g.,
            ``dict(silhouette=True)``).

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        figure : instance of mne.viz.Brain | matplotlib.figure.Figure
            An instance of :class:`mne.viz.Brain` or matplotlib figure.

        Notes
        -----
        Flatmaps are available by default for ``fsaverage`` but not for other
        subjects reconstructed by FreeSurfer. We recommend using
        :func:`mne.compute_source_morph` to morph source estimates to ``fsaverage``
        for flatmap plotting. If you want to construct your own flatmap for a given
        subject, these links might help:

        - https://surfer.nmr.mgh.harvard.edu/fswiki/FreeSurferOccipitalFlattenedPatch
        - https://openwetware.org/wiki/Beauchamp:FreeSurfer
        """
        ...
    @property
    def sfreq(self):
        """Sample rate of the data."""
        ...
    def crop(self, tmin=None, tmax=None, include_tmax: bool = True):
        """Restrict SourceEstimate to a time interval.

        Parameters
        ----------
        tmin : float | None
            The first time point in seconds. If None the first present is used.
        tmax : float | None
            The last time point in seconds. If None the last present is used.

        include_tmax : bool
            If True (default), include tmax. If False, exclude tmax (similar to how
            Python indexing typically works).

            .. versionadded:: 0.19

        Returns
        -------
        stc : instance of SourceEstimate
            The cropped source estimate.
        """
        ...
    def resample(
        self,
        sfreq,
        npad: str = "auto",
        window: str = "boxcar",
        n_jobs=None,
        verbose=None,
    ):
        """Resample data.

        If appropriate, an anti-aliasing filter is applied before resampling.
        See :ref:`resampling-and-decimating` for more information.

        Parameters
        ----------
        sfreq : float
            New sample rate to use.
        npad : int | str
            Amount to pad the start and end of the data.
            Can also be "auto" to use a padding that will result in
            a power-of-two size (can be much faster).
        window : str | tuple
            Window to use in resampling. See :func:`scipy.signal.resample`.
        n_jobs : int | None
            The number of jobs to run in parallel. If ``-1``, it is set
            to the number of CPU cores. Requires the :mod:`joblib` package.
            ``None`` (default) is a marker for 'unset' that will be interpreted
            as ``n_jobs=1`` (sequential execution) unless the call is performed under
            a :class:`joblib:joblib.parallel_config` context manager that sets another
            value for ``n_jobs``.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        stc : instance of SourceEstimate
            The resampled source estimate.

        Notes
        -----
        For some data, it may be more accurate to use npad=0 to reduce
        artifacts. This is dataset dependent -- check your data!

        Note that the sample rate of the original data is inferred from tstep.
        """
        ...
    @property
    def data(self):
        """Numpy array of source estimate data."""
        ...
    @data.setter
    def data(self, value) -> None:
        """Numpy array of source estimate data."""
        ...
    @property
    def shape(self):
        """Shape of the data."""
        ...
    @property
    def tmin(self):
        """The first timestamp."""
        ...
    @tmin.setter
    def tmin(self, value) -> None:
        """The first timestamp."""
        ...
    @property
    def tstep(self):
        """The change in time between two consecutive samples (1 / sfreq)."""
        ...
    @tstep.setter
    def tstep(self, value) -> None:
        """The change in time between two consecutive samples (1 / sfreq)."""
        ...
    @property
    def times(self):
        """A timestamp for each sample."""
        ...
    @times.setter
    def times(self, value) -> None:
        """A timestamp for each sample."""
        ...
    def __add__(self, a):
        """Add source estimates."""
        ...
    def __iadd__(self, a): ...
    def mean(self):
        """Make a summary stc file with mean over time points.

        Returns
        -------
        stc : SourceEstimate | VectorSourceEstimate
            The modified stc.
        """
        ...
    def sum(self):
        """Make a summary stc file with sum over time points.

        Returns
        -------
        stc : SourceEstimate | VectorSourceEstimate
            The modified stc.
        """
        ...
    def __sub__(self, a):
        """Subtract source estimates."""
        ...
    def __isub__(self, a): ...
    def __truediv__(self, a): ...
    def __div__(self, a):
        """Divide source estimates."""
        ...
    def __itruediv__(self, a): ...
    def __idiv__(self, a): ...
    def __mul__(self, a):
        """Multiply source estimates."""
        ...
    def __imul__(self, a): ...
    def __pow__(self, a): ...
    def __ipow__(self, a): ...
    def __radd__(self, a): ...
    def __rsub__(self, a): ...
    def __rmul__(self, a): ...
    def __rdiv__(self, a): ...
    def __neg__(self):
        """Negate the source estimate."""
        ...
    def __pos__(self): ...
    def __abs__(self):
        """Compute the absolute value of the data.

        Returns
        -------
        stc : instance of _BaseSourceEstimate
            A version of the source estimate, where the data attribute is set
            to abs(self.data).
        """
        ...
    def sqrt(self):
        """Take the square root.

        Returns
        -------
        stc : instance of SourceEstimate
            A copy of the SourceEstimate with sqrt(data).
        """
        ...
    def copy(self):
        """Return copy of source estimate instance.

        Returns
        -------
        stc : instance of SourceEstimate
            A copy of the source estimate.
        """
        ...
    def bin(self, width, tstart=None, tstop=None, func=...):
        """Return a source estimate object with data summarized over time bins.

        Time bins of ``width`` seconds. This method is intended for
        visualization only. No filter is applied to the data before binning,
        making the method inappropriate as a tool for downsampling data.

        Parameters
        ----------
        width : scalar
            Width of the individual bins in seconds.
        tstart : scalar | None
            Time point where the first bin starts. The default is the first
            time point of the stc.
        tstop : scalar | None
            Last possible time point contained in a bin (if the last bin would
            be shorter than width it is dropped). The default is the last time
            point of the stc.
        func : callable
            Function that is applied to summarize the data. Needs to accept a
            numpy.array as first input and an ``axis`` keyword argument.

        Returns
        -------
        stc : SourceEstimate | VectorSourceEstimate
            The binned source estimate.
        """
        ...
    def transform_data(self, func, idx=None, tmin_idx=None, tmax_idx=None):
        """Get data after a linear (time) transform has been applied.

        The transform is applied to each source time course independently.

        Parameters
        ----------
        func : callable
            The transform to be applied, including parameters (see, e.g.,
            :func:`functools.partial`). The first parameter of the function is
            the input data. The first return value is the transformed data,
            remaining outputs are ignored. The first dimension of the
            transformed data has to be the same as the first dimension of the
            input data.
        idx : array | None
            Indicices of source time courses for which to compute transform.
            If None, all time courses are used.
        tmin_idx : int | None
            Index of first time point to include. If None, the index of the
            first time point is used.
        tmax_idx : int | None
            Index of the first time point not to include. If None, time points
            up to (and including) the last time point are included.

        Returns
        -------
        data_t : ndarray
            The transformed data.

        Notes
        -----
        Applying transforms can be significantly faster if the
        SourceEstimate object was created using "(kernel, sens_data)", for
        the "data" parameter as the transform is applied in sensor space.
        Inverse methods, e.g., "apply_inverse_epochs", or "apply_lcmv_epochs"
        do this automatically (if possible).
        """
        ...
    def transform(self, func, idx=None, tmin=None, tmax=None, copy: bool = False):
        """Apply linear transform.

        The transform is applied to each source time course independently.

        Parameters
        ----------
        func : callable
            The transform to be applied, including parameters (see, e.g.,
            :func:`functools.partial`). The first parameter of the function is
            the input data. The first two dimensions of the transformed data
            should be (i) vertices and (ii) time.  See Notes for details.
        idx : array | None
            Indices of source time courses for which to compute transform.
            If None, all time courses are used.
        tmin : float | int | None
            First time point to include (ms). If None, self.tmin is used.
        tmax : float | int | None
            Last time point to include (ms). If None, self.tmax is used.
        copy : bool
            If True, return a new instance of SourceEstimate instead of
            modifying the input inplace.

        Returns
        -------
        stcs : SourceEstimate | VectorSourceEstimate | list
            The transformed stc or, in the case of transforms which yield
            N-dimensional output (where N > 2), a list of stcs. For a list,
            copy must be True.

        Notes
        -----
        Transforms which yield 3D
        output (e.g. time-frequency transforms) are valid, so long as the
        first two dimensions are vertices and time.  In this case, the
        copy parameter must be True and a list of
        SourceEstimates, rather than a single instance of SourceEstimate,
        will be returned, one for each index of the 3rd dimension of the
        transformed data.  In the case of transforms yielding 2D output
        (e.g. filtering), the user has the option of modifying the input
        inplace (copy = False) or returning a new instance of
        SourceEstimate (copy = True) with the transformed data.

        Applying transforms can be significantly faster if the
        SourceEstimate object was created using "(kernel, sens_data)", for
        the "data" parameter as the transform is applied in sensor space.
        Inverse methods, e.g., "apply_inverse_epochs", or "apply_lcmv_epochs"
        do this automatically (if possible).
        """
        ...
    def to_data_frame(
        self,
        index=None,
        scalings=None,
        long_format: bool = False,
        time_format=None,
        *,
        verbose=None,
    ):
        """Export data in tabular structure as a pandas DataFrame.

        Vertices are converted to columns in the DataFrame. By default,
        an additional column "time" is added, unless ``index='time'``
        (in which case time values form the DataFrame's index).

        Parameters
        ----------

        index : 'time' | None
            Kind of index to use for the DataFrame. If ``None``, a sequential
            integer index (:class:`pandas.RangeIndex`) will be used. If ``'time'``, a
            ``pandas.Index`` or :class:`pandas.TimedeltaIndex` will be used
            (depending on the value of ``time_format``).
            Defaults to ``None``.

        scalings : dict | None
            Scaling factor applied to the channels picked. If ``None``, defaults to
            ``dict(eeg=1e6, mag=1e15, grad=1e13)`` — i.e., converts EEG to µV,
            magnetometers to fT, and gradiometers to fT/cm.

        long_format : bool
            If True, the DataFrame is returned in long format where each row is one
            observation of the signal at a unique combination of time point and vertex.
            Defaults to ``False``.

        time_format : str | None
            Desired time format. If ``None``, no conversion is applied, and time values
            remain as float values in seconds. If ``'ms'``, time values will be rounded
            to the nearest millisecond and converted to integers. If ``'timedelta'``,
            time values will be converted to :class:`pandas.Timedelta` values.
            Default is ``None``.

            .. versionadded:: 0.20

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------

        df : instance of pandas.DataFrame
            A dataframe suitable for usage with other statistical/plotting/analysis
            packages.
        """
        ...

class _BaseSurfaceSourceEstimate(_BaseSourceEstimate):
    """Abstract base class for surface source estimates.

    Parameters
    ----------
    data : array
        The data in source space.
    vertices : list of array, shape (2,)
        Vertex numbers corresponding to the data. The first element of the list
        contains vertices of left hemisphere and the second element contains
        vertices of right hemisphere.

    tmin : scalar
        Time point of the first sample in data.

    tstep : scalar
        Time step between successive samples in data.

    subject : str
        The FreeSurfer subject name. While not necessary, it is safer to set the
        subject parameter to avoid analysis errors.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Attributes
    ----------
    subject : str | None
        The subject name.
    times : array of shape (n_times,)
        The time vector.
    vertices : list of array, shape (2,)
        Vertex numbers corresponding to the data. The first element of the list
        contains vertices of left hemisphere and the second element contains
        vertices of right hemisphere.
    data : array
        The data in source space.
    shape : tuple
        The shape of the data. A tuple of int (n_dipoles, n_times).
    """

    @property
    def lh_data(self):
        """Left hemisphere data."""
        ...
    @property
    def rh_data(self):
        """Right hemisphere data."""
        ...
    @property
    def lh_vertno(self):
        """Left hemisphere vertno."""
        ...
    @property
    def rh_vertno(self):
        """Right hemisphere vertno."""
        ...
    def in_label(self, label):
        """Get a source estimate object restricted to a label.

        SourceEstimate contains the time course of
        activation of all sources inside the label.

        Parameters
        ----------
        label : Label | BiHemiLabel
            The label (as created for example by mne.read_label). If the label
            does not match any sources in the SourceEstimate, a ValueError is
            raised.

        Returns
        -------
        stc : SourceEstimate | VectorSourceEstimate
            The source estimate restricted to the given label.
        """
        ...
    data: Incomplete

    def expand(self, vertices):
        """Expand SourceEstimate to include more vertices.

        This will add rows to stc.data (zero-filled) and modify stc.vertices
        to include all vertices in stc.vertices and the input vertices.

        Parameters
        ----------
        vertices : list of array
            New vertices to add. Can also contain old values.

        Returns
        -------
        stc : SourceEstimate | VectorSourceEstimate
            The modified stc (note: method operates inplace).
        """
        ...
    def to_original_src(
        self, src_orig, subject_orig=None, subjects_dir=None, verbose=None
    ):
        """Get a source estimate from morphed source to the original subject.

        Parameters
        ----------
        src_orig : instance of SourceSpaces
            The original source spaces that were morphed to the current
            subject.
        subject_orig : str | None
            The original subject. For most source spaces this shouldn't need
            to be provided, since it is stored in the source space itself.

        subjects_dir : path-like | None
            The path to the directory containing the FreeSurfer subjects
            reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
            variable.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        stc : SourceEstimate | VectorSourceEstimate
            The transformed source estimate.

        See Also
        --------
        morph_source_spaces

        Notes
        -----
        .. versionadded:: 0.10.0
        """
        ...
    def get_peak(
        self,
        hemi=None,
        tmin=None,
        tmax=None,
        mode: str = "abs",
        vert_as_index: bool = False,
        time_as_index: bool = False,
    ):
        """Get location and latency of peak amplitude.

        Parameters
        ----------
        hemi : {'lh', 'rh', None}
            The hemi to be considered. If None, the entire source space is
            considered.

        tmin : float | None
            The minimum point in time to be considered for peak getting.
        tmax : float | None
            The maximum point in time to be considered for peak getting.
        mode : {'pos', 'neg', 'abs'}
            How to deal with the sign of the data. If 'pos' only positive
            values will be considered. If 'neg' only negative values will
            be considered. If 'abs' absolute values will be considered.
            Defaults to 'abs'.
        vert_as_index : bool
            Whether to return the vertex index (True) instead of of its ID
            (False, default).
        time_as_index : bool
            Whether to return the time index (True) instead of the latency
            (False, default).

        Returns
        -------
        pos : int
            The vertex exhibiting the maximum response, either ID or index.
        latency : float | int
            The time point of the maximum response, either latency in seconds
            or index.
        """
        ...

class SourceEstimate(_BaseSurfaceSourceEstimate):
    """Container for surface source estimates.

    Parameters
    ----------
    data : array of shape (n_dipoles, n_times) | tuple, shape (2,)
        The data in source space. When it is a single array, the
        left hemisphere is stored in data[:len(vertices[0])] and the right
        hemisphere is stored in data[-len(vertices[1]):].
        When data is a tuple, it contains two arrays:

        - "kernel" shape (n_vertices, n_sensors) and
        - "sens_data" shape (n_sensors, n_times).

        In this case, the source space data corresponds to
        ``np.dot(kernel, sens_data)``.
    vertices : list of array, shape (2,)
        Vertex numbers corresponding to the data. The first element of the list
        contains vertices of left hemisphere and the second element contains
        vertices of right hemisphere.

    tmin : scalar
        Time point of the first sample in data.

    tstep : scalar
        Time step between successive samples in data.

    subject : str
        The FreeSurfer subject name. While not necessary, it is safer to set the
        subject parameter to avoid analysis errors.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Attributes
    ----------
    subject : str | None
        The subject name.
    times : array of shape (n_times,)
        The time vector.
    vertices : list of array, shape (2,)
        The indices of the dipoles in the left and right source space.
    data : array of shape (n_dipoles, n_times)
        The data in source space.
    shape : tuple
        The shape of the data. A tuple of int (n_dipoles, n_times).

    See Also
    --------
    VectorSourceEstimate : A container for vector surface source estimates.
    VolSourceEstimate : A container for volume source estimates.
    VolVectorSourceEstimate : A container for volume vector source estimates.
    MixedSourceEstimate : A container for mixed surface + volume source
                          estimates.
    """

    def save(
        self, fname, ftype: str = "stc", *, overwrite: bool = False, verbose=None
    ) -> None:
        """Save the source estimates to a file.

        Parameters
        ----------
        fname : path-like
            The stem of the file name. The file names used for surface source
            spaces are obtained by adding ``"-lh.stc"`` and ``"-rh.stc"`` (or
            ``"-lh.w"`` and ``"-rh.w"``) to the stem provided, for the left and
            the right hemisphere, respectively.
        ftype : str
            File format to use. Allowed values are ``"stc"`` (default),
            ``"w"``, and ``"h5"``. The ``"w"`` format only supports a single
            time point.

        overwrite : bool
            If True (default False), overwrite the destination file if it
            exists.

            .. versionadded:: 1.0

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.
        """
        ...
    def estimate_snr(self, info, fwd, cov, verbose=None):
        """Compute time-varying SNR in the source space.

        This function should only be used with source estimates with units
        nanoAmperes (i.e., MNE-like solutions, *not* dSPM or sLORETA).
        See also :footcite:`GoldenholzEtAl2009`.

        .. warning:: This function currently only works properly for fixed
                     orientation.

        Parameters
        ----------

        info : mne.Info
            The :class:`mne.Info` object with information about the sensors and methods of measurement.
        fwd : instance of Forward
            The forward solution used to create the source estimate.
        cov : instance of Covariance
            The noise covariance used to estimate the resting cortical
            activations. Should be an evoked covariance, not empty room.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        snr_stc : instance of SourceEstimate
            The source estimate with the SNR computed.

        Notes
        -----
        We define the SNR in decibels for each source location at each
        time point as:

        .. math::

            {\\rm SNR} = 10\\log_10[\\frac{a^2}{N}\\sum_k\\frac{b_k^2}{s_k^2}]

        where :math:`\\\\b_k` is the signal on sensor :math:`k` provided by the
        forward model for a source with unit amplitude, :math:`a` is the
        source amplitude, :math:`N` is the number of sensors, and
        :math:`s_k^2` is the noise variance on sensor :math:`k`.

        References
        ----------
        .. footbibliography::
        """
        ...
    def center_of_mass(
        self,
        subject=None,
        hemi=None,
        restrict_vertices: bool = False,
        subjects_dir=None,
        surf: str = "sphere",
    ):
        """Compute the center of mass of activity.

        This function computes the spatial center of mass on the surface
        as well as the temporal center of mass as in :footcite:`LarsonLee2013`.

        .. note:: All activity must occur in a single hemisphere, otherwise
                  an error is raised. The "mass" of each point in space for
                  computing the spatial center of mass is computed by summing
                  across time, and vice-versa for each point in time in
                  computing the temporal center of mass. This is useful for
                  quantifying spatio-temporal cluster locations, especially
                  when combined with :func:`mne.vertex_to_mni`.

        Parameters
        ----------
        subject : str | None
            The subject the stc is defined for.
        hemi : int, or None
            Calculate the center of mass for the left (0) or right (1)
            hemisphere. If None, one of the hemispheres must be all zeroes,
            and the center of mass will be calculated for the other
            hemisphere (useful for getting COM for clusters).
        restrict_vertices : bool | array of int | instance of SourceSpaces
            If True, returned vertex will be one from stc. Otherwise, it could
            be any vertex from surf. If an array of int, the returned vertex
            will come from that array. If instance of SourceSpaces (as of
            0.13), the returned vertex will be from the given source space.
            For most accuruate estimates, do not restrict vertices.

        subjects_dir : path-like | None
            The path to the directory containing the FreeSurfer subjects
            reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
            variable.
        surf : str
            The surface to use for Euclidean distance center of mass
            finding. The default here is "sphere", which finds the center
            of mass on the spherical surface to help avoid potential issues
            with cortical folding.

        Returns
        -------
        vertex : int
            Vertex of the spatial center of mass for the inferred hemisphere,
            with each vertex weighted by the sum of the stc across time. For a
            boolean stc, then, this would be weighted purely by the duration
            each vertex was active.
        hemi : int
            Hemisphere the vertex was taken from.
        t : float
            Time of the temporal center of mass (weighted by the sum across
            source vertices).

        See Also
        --------
        mne.Label.center_of_mass
        mne.vertex_to_mni

        References
        ----------
        .. footbibliography::
        """
        ...

class _BaseVectorSourceEstimate(_BaseSourceEstimate):
    def __init__(
        self, data, vertices=None, tmin=None, tstep=None, subject=None, verbose=None
    ) -> None: ...
    def magnitude(self):
        """Compute magnitude of activity without directionality.

        Returns
        -------
        stc : instance of SourceEstimate
            The source estimate without directionality information.
        """
        ...
    def project(self, directions, src=None, use_cps: bool = True):
        """Project the data for each vertex in a given direction.

        Parameters
        ----------
        directions : ndarray, shape (n_vertices, 3) | str
            Can be:

            - ``'normal'``
                Project onto the source space normals.
            - ``'pca'``
                SVD will be used to project onto the direction of maximal
                power for each source.
            - :class:numpy.ndarray`, shape (n_vertices, 3)
                Projection directions for each source.
        src : instance of SourceSpaces | None
            The source spaces corresponding to the source estimate.
            Not used when ``directions`` is an array, optional when
            ``directions='pca'``.

        use_cps : bool
            Whether to use cortical patch statistics to define normal orientations for
            surfaces (default True).
            Should be the same value that was used when the forward model
            was computed (typically True).

        Returns
        -------
        stc : instance of SourceEstimate
            The projected source estimate.
        directions : ndarray, shape (n_vertices, 3)
            The directions that were computed (or just used).

        Notes
        -----
        When using SVD, there is a sign ambiguity for the direction of maximal
        power. When ``src is None``, the direction is chosen that makes the
        resulting time waveform sum positive (i.e., have positive amplitudes).
        When ``src`` is provided, the directions are flipped in the direction
        of the source normals, i.e., outward from cortex for surface source
        spaces and in the +Z / superior direction for volume source spaces.

        .. versionadded:: 0.21
        """
        ...
    def plot(
        self,
        subject=None,
        hemi: str = "lh",
        colormap: str = "hot",
        time_label: str = "auto",
        smoothing_steps: int = 10,
        transparent: bool = True,
        brain_alpha: float = 0.4,
        overlay_alpha=None,
        vector_alpha: float = 1.0,
        scale_factor=None,
        time_viewer: str = "auto",
        subjects_dir=None,
        figure=None,
        views: str = "lateral",
        colorbar: bool = True,
        clim: str = "auto",
        cortex: str = "classic",
        size: int = 800,
        background: str = "black",
        foreground=None,
        initial_time=None,
        time_unit: str = "s",
        show_traces: str = "auto",
        src=None,
        volume_options: float = 1.0,
        view_layout: str = "vertical",
        add_data_kwargs=None,
        brain_kwargs=None,
        verbose=None,
    ):
        """Plot VectorSourceEstimate with PyVista.

        A "glass brain" is drawn and all dipoles defined in the source estimate
        are shown using arrows, depicting the direction and magnitude of the
        current moment at the dipole. Additionally, an overlay is plotted on top of
        the cortex with the magnitude of the current.

        Parameters
        ----------
        subject : str | None
            The FreeSurfer subject name.
            If ``None``, ``stc.subject`` will be used.
        hemi : str, 'lh' | 'rh' | 'split' | 'both'
            The hemisphere to display.

        colormap : str | np.ndarray of float, shape(n_colors, 3 | 4)
            Name of colormap to use or a custom look up table. If array, must
            be (n x 3) or (n x 4) array for with RGB or RGBA values between
            0 and 255.
            This should be a sequential colormap.

        time_label : str | callable | None
            Format of the time label (a format string, a function that maps
            floating point time values to strings, or None for no label). The
            default is ``'auto'``, which will use ``time=%0.2f ms`` if there
            is more than one time point.
        smoothing_steps : int
            The amount of smoothing.

        transparent : bool | None
            If True: use a linear transparency between fmin and fmid
            and make values below fmin fully transparent (symmetrically for
            divergent colormaps). None will choose automatically based on colormap
            type.
        brain_alpha : float
            Alpha value to apply globally to the surface meshes. Defaults to 0.4.
        overlay_alpha : float
            Alpha value to apply globally to the overlay. Defaults to
            ``brain_alpha``.
        vector_alpha : float
            Alpha value to apply globally to the vector glyphs. Defaults to 1.
        scale_factor : float | None
            Scaling factor for the vector glyphs. By default, an attempt is made to
            automatically determine a sane value.
        time_viewer : bool | str
            Display time viewer GUI. Can be "auto", which is True for the PyVista
            backend and False otherwise.

            .. versionchanged:: 0.20
               Added "auto" option and default.
        subjects_dir : str
            The path to the freesurfer subjects reconstructions.
            It corresponds to Freesurfer environment variable SUBJECTS_DIR.
        figure : instance of Figure3D | list | int | None
            If None, a new figure will be created. If multiple views or a
            split view is requested, this must be a list of the appropriate
            length. If int is provided it will be used to identify the PyVista
            figure by it's id or create a new figure with the given id.

        views : str | list
            View to use. Using multiple views (list) is not supported for mpl
            backend. See :meth:`Brain.show_view <mne.viz.Brain.show_view>` for
            valid string options.
        colorbar : bool
            If True, display colorbar on scene.

        clim : str | dict
            Colorbar properties specification. If 'auto', set clim automatically
            based on data percentiles. If dict, should contain:

                ``kind`` : 'value' | 'percent'
                    Flag to specify type of limits.
                ``lims`` : list | np.ndarray | tuple of float, 3 elements
                    Lower, middle, and upper bound for colormap.

            Unlike :meth:`stc.plot <mne.SourceEstimate.plot>`, it cannot use
            ``pos_lims``, as the surface plot must show the magnitude.
        cortex : str or tuple
            Specifies how binarized curvature values are rendered.
            either the name of a preset Brain cortex colorscheme (one of
            'classic', 'bone', 'low_contrast', or 'high_contrast'), or the
            name of a colormap, or a tuple with values (colormap, min,
            max, reverse) to fully specify the curvature colors.
        size : float or tuple of float
            The size of the window, in pixels. can be one number to specify
            a square window, or the (width, height) of a rectangular window.
        background : matplotlib color
            Color of the background of the display window.
        foreground : matplotlib color | None
            Color of the foreground of the display window.
            None will choose black or white based on the background color.
        initial_time : float | None
            The time to display on the plot initially. ``None`` to display the
            first time sample (default).
        time_unit : 's' | 'ms'
            Whether time is represented in seconds ("s", default) or
            milliseconds ("ms").

        show_traces : bool | str | float
            If True, enable interactive picking of a point on the surface of the
            brain and plot its time course.
            This feature is only available with the PyVista 3d backend, and requires
            ``time_viewer=True``. Defaults to 'auto', which will use True if and
            only if ``time_viewer=True``, the backend is PyVista, and there is more
            than one time point. If float (between zero and one), it specifies what
            proportion of the total window should be devoted to traces (True is
            equivalent to 0.25, i.e., it will occupy the bottom 1/4 of the figure).

            .. versionadded:: 0.20.0

        src : instance of SourceSpaces | None
            The source space corresponding to the source estimate. Only necessary
            if the STC is a volume or mixed source estimate.
        volume_options : float | dict | None
            Options for volumetric source estimate plotting, with key/value pairs:

            - ``'resolution'`` : float | None
                Resolution (in mm) of volume rendering. Smaller (e.g., 1.) looks
                better at the cost of speed. None (default) uses the volume source
                space resolution, which is often something like 7 or 5 mm,
                without resampling.
            - ``'blending'`` : str
                Can be "mip" (default) for :term:`maximum intensity projection` or
                "composite" for composite blending using alpha values.
            - ``'alpha'`` : float | None
                Alpha for the volumetric rendering. Defaults are 0.4 for vector source
                estimates and 1.0 for scalar source estimates.
            - ``'surface_alpha'`` : float | None
                Alpha for the surface enclosing the volume(s). None (default) will use
                half the volume alpha. Set to zero to avoid plotting the surface.
            - ``'silhouette_alpha'`` : float | None
                Alpha for a silhouette along the outside of the volume. None (default)
                will use ``0.25 * surface_alpha``.
            - ``'silhouette_linewidth'`` : float
                The line width to use for the silhouette. Default is 2.

            A float input (default 1.) or None will be used for the ``'resolution'``
            entry.

        view_layout : str
            Can be "vertical" (default) or "horizontal". When using "horizontal" mode,
            the PyVista backend must be used and hemi cannot be "split".

        add_data_kwargs : dict | None
            Additional arguments to brain.add_data (e.g.,
            ``dict(time_label_size=10)``).

        brain_kwargs : dict | None
            Additional arguments to the :class:`mne.viz.Brain` constructor (e.g.,
            ``dict(silhouette=True)``).

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        brain : mne.viz.Brain
            A instance of :class:`mne.viz.Brain`.

        Notes
        -----
        .. versionadded:: 0.15

        If the current magnitude overlay is not desired, set ``overlay_alpha=0``
        and ``smoothing_steps=1``.
        """
        ...

class _BaseVolSourceEstimate(_BaseSourceEstimate):
    def plot_3d(
        self,
        subject=None,
        surface: str = "white",
        hemi: str = "both",
        colormap: str = "auto",
        time_label: str = "auto",
        smoothing_steps: int = 10,
        transparent: bool = True,
        alpha: float = 0.1,
        time_viewer: str = "auto",
        subjects_dir=None,
        figure=None,
        views: str = "axial",
        colorbar: bool = True,
        clim: str = "auto",
        cortex: str = "classic",
        size: int = 800,
        background: str = "black",
        foreground=None,
        initial_time=None,
        time_unit: str = "s",
        backend: str = "auto",
        spacing: str = "oct6",
        title=None,
        show_traces: str = "auto",
        src=None,
        volume_options: float = 1.0,
        view_layout: str = "vertical",
        add_data_kwargs=None,
        brain_kwargs=None,
        verbose=None,
    ):
        """Plot SourceEstimate.

        Parameters
        ----------
        subject : str | None
            The FreeSurfer subject name.
            If ``None``, ``stc.subject`` will be used.
        surface : str
            The type of surface (inflated, white etc.).
        hemi : str
            Hemisphere id (ie ``'lh'``, ``'rh'``, ``'both'``, or ``'split'``). In
            the case of ``'both'``, both hemispheres are shown in the same window.
            In the case of ``'split'`` hemispheres are displayed side-by-side
            in different viewing panes.

        colormap : str | np.ndarray of float, shape(n_colors, 3 | 4)
            Name of colormap to use or a custom look up table. If array, must
            be (n x 3) or (n x 4) array for with RGB or RGBA values between
            0 and 255.
            The default ('auto') uses ``'hot'`` for one-sided data and
            'mne' for two-sided data.

        time_label : str | callable | None
            Format of the time label (a format string, a function that maps
            floating point time values to strings, or None for no label). The
            default is ``'auto'``, which will use ``time=%0.2f ms`` if there
            is more than one time point.
        smoothing_steps : int
            The amount of smoothing.

        transparent : bool | None
            If True: use a linear transparency between fmin and fmid
            and make values below fmin fully transparent (symmetrically for
            divergent colormaps). None will choose automatically based on colormap
            type.
        alpha : float
            Alpha value to apply globally to the overlay. Has no effect with mpl
            backend.
        time_viewer : bool | str
            Display time viewer GUI. Can also be 'auto', which will mean True
            for the PyVista backend and False otherwise.

            .. versionchanged:: 0.20.0
               "auto" mode added.

        subjects_dir : path-like | None
            The path to the directory containing the FreeSurfer subjects
            reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
            variable.
        figure : instance of Figure3D | instance of matplotlib.figure.Figure | list | int | None
            If None, a new figure will be created. If multiple views or a
            split view is requested, this must be a list of the appropriate
            length. If int is provided it will be used to identify the PyVista
            figure by it's id or create a new figure with the given id. If an
            instance of matplotlib figure, mpl backend is used for plotting.

        views : str | list
            View to use. Using multiple views (list) is not supported for mpl
            backend. See :meth:`Brain.show_view <mne.viz.Brain.show_view>` for
            valid string options.

            When plotting a standard SourceEstimate (not volume, mixed, or vector)
            and using the PyVista backend, ``views='flat'`` is also supported to
            plot cortex as a flatmap.

            Using multiple views (list) is not supported by the matplotlib backend.

            .. versionchanged:: 0.21.0
               Support for flatmaps.
        colorbar : bool
            If True, display colorbar on scene.

        clim : str | dict
            Colorbar properties specification. If 'auto', set clim automatically
            based on data percentiles. If dict, should contain:

                ``kind`` : 'value' | 'percent'
                    Flag to specify type of limits.
                ``lims`` : list | np.ndarray | tuple of float, 3 elements
                    Lower, middle, and upper bounds for colormap.
                ``pos_lims`` : list | np.ndarray | tuple of float, 3 elements
                    Lower, middle, and upper bound for colormap. Positive values
                    will be mirrored directly across zero during colormap
                    construction to obtain negative control points.

            .. note:: Only one of ``lims`` or ``pos_lims`` should be provided.
                      Only sequential colormaps should be used with ``lims``, and
                      only divergent colormaps should be used with ``pos_lims``.
        cortex : str | tuple
            Specifies how binarized curvature values are rendered.
            Either the name of a preset Brain cortex colorscheme (one of
            ``'classic'``, ``'bone'``, ``'low_contrast'``, or ``'high_contrast'``),
            or the name of a colormap, or a tuple with values
            ``(colormap, min, max, reverse)`` to fully specify the curvature
            colors. Has no effect with the matplotlib backend.
        size : float or tuple of float
            The size of the window, in pixels. can be one number to specify
            a square window, or the (width, height) of a rectangular window.
            Has no effect with mpl backend.
        background : matplotlib color
            Color of the background of the display window.
        foreground : matplotlib color | None
            Color of the foreground of the display window. Has no effect with mpl
            backend. None will choose white or black based on the background color.
        initial_time : float | None
            The time to display on the plot initially. ``None`` to display the
            first time sample (default).
        time_unit : ``'s'`` | ``'ms'``
            Whether time is represented in seconds ("s", default) or
            milliseconds ("ms").
        backend : ``'auto'`` | ``'pyvistaqt'`` | ``'matplotlib'``
            Which backend to use. If ``'auto'`` (default), tries to plot with
            pyvistaqt, but resorts to matplotlib if no 3d backend is available.

            .. versionadded:: 0.15.0
        spacing : str
            Only affects the matplotlib backend.
            The spacing to use for the source space. Can be ``'ico#'`` for a
            recursively subdivided icosahedron, ``'oct#'`` for a recursively
            subdivided octahedron, or ``'all'`` for all points. In general, you can
            speed up the plotting by selecting a sparser source space.
            Defaults  to 'oct6'.

            .. versionadded:: 0.15.0
        title : str | None
            Title for the figure. If None, the subject name will be used.

            .. versionadded:: 0.17.0

        show_traces : bool | str | float
            If True, enable interactive picking of a point on the surface of the
            brain and plot its time course.
            This feature is only available with the PyVista 3d backend, and requires
            ``time_viewer=True``. Defaults to 'auto', which will use True if and
            only if ``time_viewer=True``, the backend is PyVista, and there is more
            than one time point. If float (between zero and one), it specifies what
            proportion of the total window should be devoted to traces (True is
            equivalent to 0.25, i.e., it will occupy the bottom 1/4 of the figure).

            .. versionadded:: 0.20.0

        src : instance of SourceSpaces | None
            The source space corresponding to the source estimate. Only necessary
            if the STC is a volume or mixed source estimate.
        volume_options : float | dict | None
            Options for volumetric source estimate plotting, with key/value pairs:

            - ``'resolution'`` : float | None
                Resolution (in mm) of volume rendering. Smaller (e.g., 1.) looks
                better at the cost of speed. None (default) uses the volume source
                space resolution, which is often something like 7 or 5 mm,
                without resampling.
            - ``'blending'`` : str
                Can be "mip" (default) for :term:`maximum intensity projection` or
                "composite" for composite blending using alpha values.
            - ``'alpha'`` : float | None
                Alpha for the volumetric rendering. Defaults are 0.4 for vector source
                estimates and 1.0 for scalar source estimates.
            - ``'surface_alpha'`` : float | None
                Alpha for the surface enclosing the volume(s). None (default) will use
                half the volume alpha. Set to zero to avoid plotting the surface.
            - ``'silhouette_alpha'`` : float | None
                Alpha for a silhouette along the outside of the volume. None (default)
                will use ``0.25 * surface_alpha``.
            - ``'silhouette_linewidth'`` : float
                The line width to use for the silhouette. Default is 2.

            A float input (default 1.) or None will be used for the ``'resolution'``
            entry.

        view_layout : str
            Can be "vertical" (default) or "horizontal". When using "horizontal" mode,
            the PyVista backend must be used and hemi cannot be "split".

        add_data_kwargs : dict | None
            Additional arguments to brain.add_data (e.g.,
            ``dict(time_label_size=10)``).

        brain_kwargs : dict | None
            Additional arguments to the :class:`mne.viz.Brain` constructor (e.g.,
            ``dict(silhouette=True)``).

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        figure : instance of mne.viz.Brain | matplotlib.figure.Figure
            An instance of :class:`mne.viz.Brain` or matplotlib figure.

        Notes
        -----
        Flatmaps are available by default for ``fsaverage`` but not for other
        subjects reconstructed by FreeSurfer. We recommend using
        :func:`mne.compute_source_morph` to morph source estimates to ``fsaverage``
        for flatmap plotting. If you want to construct your own flatmap for a given
        subject, these links might help:

        - https://surfer.nmr.mgh.harvard.edu/fswiki/FreeSurferOccipitalFlattenedPatch
        - https://openwetware.org/wiki/Beauchamp:FreeSurfer
        """
        ...
    def plot(
        self,
        src,
        subject=None,
        subjects_dir=None,
        mode: str = "stat_map",
        bg_img: str = "T1.mgz",
        colorbar: bool = True,
        colormap: str = "auto",
        clim: str = "auto",
        transparent: str = "auto",
        show: bool = True,
        initial_time=None,
        initial_pos=None,
        verbose=None,
    ):
        """Plot Nutmeg style volumetric source estimates using nilearn.

        Parameters
        ----------
        src : instance of SourceSpaces | instance of SourceMorph
            The source space. Can also be a SourceMorph to morph the STC to
            a new subject (see Examples).

            .. versionchanged:: 0.18
               Support for :class:nibabel.spatialimages.SpatialImage`.

        subject : str | None
            The FreeSurfer subject name.
            If ``None``, ``stc.subject`` will be used.

        subjects_dir : path-like | None
            The path to the directory containing the FreeSurfer subjects
            reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
            variable.
        mode : ``'stat_map'`` | ``'glass_brain'``
            The plotting mode to use. For ``'glass_brain'``, activation absolute values are
            displayed after being transformed to a standard MNI brain.
        bg_img : instance of SpatialImage | str
            The background image used in the nilearn plotting function.
            Can also be a string to use the ``bg_img`` file in the subject's
            MRI directory (default is ``'T1.mgz'``).
            Not used in "glass brain" plotting.
        colorbar : bool, optional
            If True, display a colorbar on the right of the plots.

        colormap : str | np.ndarray of float, shape(n_colors, 3 | 4)
            Name of colormap to use or a custom look up table. If array, must
            be (n x 3) or (n x 4) array for with RGB or RGBA values between
            0 and 255.

        clim : str | dict
            Colorbar properties specification. If 'auto', set clim automatically
            based on data percentiles. If dict, should contain:

                ``kind`` : 'value' | 'percent'
                    Flag to specify type of limits.
                ``lims`` : list | np.ndarray | tuple of float, 3 elements
                    Lower, middle, and upper bounds for colormap.
                ``pos_lims`` : list | np.ndarray | tuple of float, 3 elements
                    Lower, middle, and upper bound for colormap. Positive values
                    will be mirrored directly across zero during colormap
                    construction to obtain negative control points.

            .. note:: Only one of ``lims`` or ``pos_lims`` should be provided.
                      Only sequential colormaps should be used with ``lims``, and
                      only divergent colormaps should be used with ``pos_lims``.

        transparent : bool | None
            If True: use a linear transparency between fmin and fmid
            and make values below fmin fully transparent (symmetrically for
            divergent colormaps). None will choose automatically based on colormap
            type.
        show : bool
            Show figures if True. Defaults to True.
        initial_time : float | None
            The initial time to plot. Can be None (default) to use the time point
            with the maximal absolute value activation across all voxels
            or the ``initial_pos`` voxel (if ``initial_pos is None`` or not,
            respectively).

            .. versionadded:: 0.19
        initial_pos : ndarray, shape (3,) | None
            The initial position to use (in m). Can be None (default) to use the
            voxel with the maximum absolute value activation across all time points
            or at ``initial_time`` (if ``initial_time is None`` or not,
            respectively).

            .. versionadded:: 0.19

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        fig : instance of Figure
            The figure.

        Notes
        -----
        Click on any of the anatomical slices to explore the time series.
        Clicking on any time point will bring up the corresponding anatomical map.

        The left and right arrow keys can be used to navigate in time.
        To move in time by larger steps, use shift+left and shift+right.

        In ``'glass_brain'`` mode, values are transformed to the standard MNI
        brain using the FreeSurfer Talairach transformation
        ``$SUBJECTS_DIR/$SUBJECT/mri/transforms/talairach.xfm``.

        .. versionadded:: 0.17

        .. versionchanged:: 0.19
           MRI volumes are automatically transformed to MNI space in
           ``'glass_brain'`` mode.

        Examples
        --------
        Passing a :class:`mne.SourceMorph` as the ``src``
        parameter can be useful for plotting in a different subject's space
        (here, a ``'sample'`` STC in ``'fsaverage'``'s space)::

        >>> morph = mne.compute_source_morph(src_sample, subject_to='fsaverage')  # doctest: +SKIP
        >>> fig = stc_vol_sample.plot(morph)  # doctest: +SKIP
        """
        ...
    def extract_label_time_course(
        self,
        labels,
        src,
        mode: str = "auto",
        allow_empty: bool = False,
        *,
        mri_resolution: bool = True,
        verbose=None,
    ):
        """Extract label time courses for lists of labels.

        This function will extract one time course for each label. The way the
        time courses are extracted depends on the mode parameter.

        Parameters
        ----------

        labels : Label | BiHemiLabel | list | tuple | str
            If using a surface or mixed source space, this should be the
            :class:mne.Label`'s for which to extract the time course.
            If working with whole-brain volume source estimates, this must be one of:

            - a string path to a FreeSurfer atlas for the subject (e.g., their
              'aparc.a2009s+aseg.mgz') to extract time courses for all volumes in the
              atlas
            - a two-element list or tuple, the first element being a path to an atlas,
              and the second being a list or dict of ``volume_labels`` to extract
              (see :func:`mne.setup_volume_source_space` for details).

            .. versionchanged:: 0.21.0
               Support for volume source estimates.

        src : instance of SourceSpaces
            The source spaces for the source time courses.

        mode : str
            Extraction mode, see Notes.

        allow_empty : bool | str
            ``False`` (default) will emit an error if there are labels that have no
            vertices in the source estimate. ``True`` and ``'ignore'`` will return
            all-zero time courses for labels that do not have any vertices in the
            source estimate, and True will emit a warning while and "ignore" will
            just log a message.

            .. versionchanged:: 0.21.0
               Support for "ignore".

        mri_resolution : bool
            If True (default), the volume source space will be upsampled to the
            original MRI resolution via trilinear interpolation before the atlas values
            are extracted. This ensnures that each atlas label will contain source
            activations. When False, only the original source space points are used,
            and some atlas labels thus may not contain any source space vertices.

            .. versionadded:: 0.21.0

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------

        label_tc : array | list (or generator) of array, shape (n_labels[, n_orient], n_times)
            Extracted time course for each label and source estimate.

        See Also
        --------
        extract_label_time_course : Extract time courses for multiple STCs.

        Notes
        -----

        Valid values for ``mode`` are:

        - ``'max'``
            Maximum value across vertices at each time point within each label.
        - ``'mean'``
            Average across vertices at each time point within each label. Ignores
            orientation of sources for standard source estimates, which varies
            across the cortical surface, which can lead to cancellation.
            Vector source estimates are always in XYZ / RAS orientation, and are thus
            already geometrically aligned.
        - ``'mean_flip'``
            Finds the dominant direction of source space normal vector orientations
            within each label, applies a sign-flip to time series at vertices whose
            orientation is more than 180° different from the dominant direction, and
            then averages across vertices at each time point within each label.
        - ``'pca_flip'``
            Applies singular value decomposition to the time courses within each label,
            and uses the first right-singular vector as the representative label time
            course. This signal is scaled so that its power matches the average
            (per-vertex) power within the label, and sign-flipped by multiplying by
            ``np.sign(u @ flip)``, where ``u`` is the first left-singular vector and
            ``flip`` is the same sign-flip vector used when ``mode='mean_flip'``. This
            sign-flip ensures that extracting time courses from the same label in
            similar STCs does not result in 180° direction/phase changes.
        - ``'auto'`` (default)
            Uses ``'mean_flip'`` when a standard source estimate is applied, and
            ``'mean'`` when a vector source estimate is supplied.
        - ``None``
            No aggregation is performed, and an array of shape ``(n_vertices, n_times)`` is
            returned.

            .. versionadded:: 0.21
               Support for ``'auto'``, vector, and volume source estimates.

        The only modes that work for vector and volume source estimates are ``'mean'``,
        ``'max'``, and ``'auto'``.
        """
        ...
    def in_label(self, label, mri, src, *, verbose=None):
        """Get a source estimate object restricted to a label.

        SourceEstimate contains the time course of
        activation of all sources inside the label.

        Parameters
        ----------
        label : str | int
            The label to use. Can be the name of a label if using a standard
            FreeSurfer atlas, or an integer value to extract from the ``mri``.
        mri : str
            Path to the atlas to use.
        src : instance of SourceSpaces
            The volumetric source space. It must be a single, whole-brain
            volume.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        stc : VolSourceEstimate | VolVectorSourceEstimate
            The source estimate restricted to the given label.

        Notes
        -----
        .. versionadded:: 0.21.0
        """
        ...
    def save_as_volume(
        self,
        fname,
        src,
        dest: str = "mri",
        mri_resolution: bool = False,
        format: str = "nifti1",
        *,
        overwrite: bool = False,
        verbose=None,
    ) -> None:
        """Save a volume source estimate in a NIfTI file.

        Parameters
        ----------
        fname : path-like
            The name of the generated nifti file.
        src : list
            The list of source spaces (should all be of type volume).
        dest : ``'mri'`` | ``'surf'``
            If ``'mri'`` the volume is defined in the coordinate system of
            the original T1 image. If ``'surf'`` the coordinate system
            of the FreeSurfer surface is used (Surface RAS).
        mri_resolution : bool
            It True the image is saved in MRI resolution.

            .. warning: If you have many time points the file produced can be
                        huge. The default is ``mri_resolution=False``.
        format : str
            Either ``'nifti1'`` (default) or ``'nifti2'``.

            .. versionadded:: 0.17

        overwrite : bool
            If True (default False), overwrite the destination file if it
            exists.

            .. versionadded:: 1.0

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

            .. versionadded:: 1.0

        Returns
        -------
        img : instance Nifti1Image
            The image object.

        Notes
        -----
        .. versionadded:: 0.9.0
        """
        ...
    def as_volume(
        self,
        src,
        dest: str = "mri",
        mri_resolution: bool = False,
        format: str = "nifti1",
    ):
        """Export volume source estimate as a nifti object.

        Parameters
        ----------
        src : instance of SourceSpaces
            The source spaces (should all be of type volume, or part of a
            mixed source space).
        dest : ``'mri'`` | ``'surf'``
            If ``'mri'`` the volume is defined in the coordinate system of
            the original T1 image. If 'surf' the coordinate system
            of the FreeSurfer surface is used (Surface RAS).
        mri_resolution : bool
            It True the image is saved in MRI resolution.

            .. warning: If you have many time points the file produced can be
                        huge. The default is ``mri_resolution=False``.
        format : str
            Either 'nifti1' (default) or 'nifti2'.

        Returns
        -------
        img : instance of Nifti1Image
            The image object.

        Notes
        -----
        .. versionadded:: 0.9.0
        """
        ...

class VolSourceEstimate(_BaseVolSourceEstimate):
    """Container for volume source estimates.

    Parameters
    ----------
    data : array of shape (n_dipoles, n_times) | tuple, shape (2,)
        The data in source space. The data can either be a single array or
        a tuple with two arrays: "kernel" shape (n_vertices, n_sensors) and
        "sens_data" shape (n_sensors, n_times). In this case, the source
        space data corresponds to ``np.dot(kernel, sens_data)``.

    vertices : list of array of int
        The indices of the dipoles in the source space. Should be a single
        array of shape (n_dipoles,) unless there are subvolumes.

    tmin : scalar
        Time point of the first sample in data.

    tstep : scalar
        Time step between successive samples in data.

    subject : str
        The FreeSurfer subject name. While not necessary, it is safer to set the
        subject parameter to avoid analysis errors.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Attributes
    ----------
    subject : str | None
        The subject name.
    times : array of shape (n_times,)
        The time vector.

    vertices : list of array of int
        The indices of the dipoles in the source space. Should be a single
        array of shape (n_dipoles,) unless there are subvolumes.
    data : array of shape (n_dipoles, n_times)
        The data in source space.
    shape : tuple
        The shape of the data. A tuple of int (n_dipoles, n_times).

    See Also
    --------
    SourceEstimate : A container for surface source estimates.
    VectorSourceEstimate : A container for vector surface source estimates.
    VolVectorSourceEstimate : A container for volume vector source estimates.
    MixedSourceEstimate : A container for mixed surface + volume source
                          estimates.

    Notes
    -----
    .. versionadded:: 0.9.0
    """

    def save(
        self, fname, ftype: str = "stc", *, overwrite: bool = False, verbose=None
    ) -> None:
        """Save the source estimates to a file.

        Parameters
        ----------
        fname : path-like
            The stem of the file name. The stem is extended with ``"-vl.stc"``
            or ``"-vl.w"``.
        ftype : str
            File format to use. Allowed values are ``"stc"`` (default),
            ``"w"``, and ``"h5"``. The ``"w"`` format only supports a single
            time point.

        overwrite : bool
            If True (default False), overwrite the destination file if it
            exists.

            .. versionadded:: 1.0

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.
        """
        ...

class VolVectorSourceEstimate(_BaseVolSourceEstimate, _BaseVectorSourceEstimate):
    """Container for volume source estimates.

    Parameters
    ----------
    data : array of shape (n_dipoles, 3, n_times)
        The data in source space. Each dipole contains three vectors that
        denote the dipole strength in X, Y and Z directions over time.

    vertices : list of array of int
        The indices of the dipoles in the source space. Should be a single
        array of shape (n_dipoles,) unless there are subvolumes.

    tmin : scalar
        Time point of the first sample in data.

    tstep : scalar
        Time step between successive samples in data.

    subject : str
        The FreeSurfer subject name. While not necessary, it is safer to set the
        subject parameter to avoid analysis errors.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Attributes
    ----------
    subject : str | None
        The subject name.
    times : array of shape (n_times,)
        The time vector.

    vertices : list of array of int
        The indices of the dipoles in the source space. Should be a single
        array of shape (n_dipoles,) unless there are subvolumes.
    data : array of shape (n_dipoles, n_times)
        The data in source space.
    shape : tuple
        The shape of the data. A tuple of int (n_dipoles, n_times).

    See Also
    --------
    SourceEstimate : A container for surface source estimates.
    VectorSourceEstimate : A container for vector surface source estimates.
    VolSourceEstimate : A container for volume source estimates.
    MixedSourceEstimate : A container for mixed surface + volume source
                          estimates.

    Notes
    -----
    .. versionadded:: 0.9.0
    """

    def plot_3d(
        self,
        subject=None,
        hemi: str = "both",
        colormap: str = "hot",
        time_label: str = "auto",
        smoothing_steps: int = 10,
        transparent: bool = True,
        brain_alpha: float = 0.4,
        overlay_alpha=None,
        vector_alpha: float = 1.0,
        scale_factor=None,
        time_viewer: str = "auto",
        subjects_dir=None,
        figure=None,
        views: str = "axial",
        colorbar: bool = True,
        clim: str = "auto",
        cortex: str = "classic",
        size: int = 800,
        background: str = "black",
        foreground=None,
        initial_time=None,
        time_unit: str = "s",
        show_traces: str = "auto",
        src=None,
        volume_options: float = 1.0,
        view_layout: str = "vertical",
        add_data_kwargs=None,
        brain_kwargs=None,
        verbose=None,
    ):
        """Plot VectorSourceEstimate with PyVista.

        A "glass brain" is drawn and all dipoles defined in the source estimate
        are shown using arrows, depicting the direction and magnitude of the
        current moment at the dipole. Additionally, an overlay is plotted on top of
        the cortex with the magnitude of the current.

        Parameters
        ----------
        subject : str | None
            The FreeSurfer subject name.
            If ``None``, ``stc.subject`` will be used.
        hemi : str, 'lh' | 'rh' | 'split' | 'both'
            The hemisphere to display.

        colormap : str | np.ndarray of float, shape(n_colors, 3 | 4)
            Name of colormap to use or a custom look up table. If array, must
            be (n x 3) or (n x 4) array for with RGB or RGBA values between
            0 and 255.
            This should be a sequential colormap.

        time_label : str | callable | None
            Format of the time label (a format string, a function that maps
            floating point time values to strings, or None for no label). The
            default is ``'auto'``, which will use ``time=%0.2f ms`` if there
            is more than one time point.
        smoothing_steps : int
            The amount of smoothing.

        transparent : bool | None
            If True: use a linear transparency between fmin and fmid
            and make values below fmin fully transparent (symmetrically for
            divergent colormaps). None will choose automatically based on colormap
            type.
        brain_alpha : float
            Alpha value to apply globally to the surface meshes. Defaults to 0.4.
        overlay_alpha : float
            Alpha value to apply globally to the overlay. Defaults to
            ``brain_alpha``.
        vector_alpha : float
            Alpha value to apply globally to the vector glyphs. Defaults to 1.
        scale_factor : float | None
            Scaling factor for the vector glyphs. By default, an attempt is made to
            automatically determine a sane value.
        time_viewer : bool | str
            Display time viewer GUI. Can be "auto", which is True for the PyVista
            backend and False otherwise.

            .. versionchanged:: 0.20
               Added "auto" option and default.
        subjects_dir : str
            The path to the freesurfer subjects reconstructions.
            It corresponds to Freesurfer environment variable SUBJECTS_DIR.
        figure : instance of Figure3D | list | int | None
            If None, a new figure will be created. If multiple views or a
            split view is requested, this must be a list of the appropriate
            length. If int is provided it will be used to identify the PyVista
            figure by it's id or create a new figure with the given id.

        views : str | list
            View to use. Using multiple views (list) is not supported for mpl
            backend. See :meth:`Brain.show_view <mne.viz.Brain.show_view>` for
            valid string options.
        colorbar : bool
            If True, display colorbar on scene.

        clim : str | dict
            Colorbar properties specification. If 'auto', set clim automatically
            based on data percentiles. If dict, should contain:

                ``kind`` : 'value' | 'percent'
                    Flag to specify type of limits.
                ``lims`` : list | np.ndarray | tuple of float, 3 elements
                    Lower, middle, and upper bound for colormap.

            Unlike :meth:`stc.plot <mne.SourceEstimate.plot>`, it cannot use
            ``pos_lims``, as the surface plot must show the magnitude.
        cortex : str or tuple
            Specifies how binarized curvature values are rendered.
            either the name of a preset Brain cortex colorscheme (one of
            'classic', 'bone', 'low_contrast', or 'high_contrast'), or the
            name of a colormap, or a tuple with values (colormap, min,
            max, reverse) to fully specify the curvature colors.
        size : float or tuple of float
            The size of the window, in pixels. can be one number to specify
            a square window, or the (width, height) of a rectangular window.
        background : matplotlib color
            Color of the background of the display window.
        foreground : matplotlib color | None
            Color of the foreground of the display window.
            None will choose black or white based on the background color.
        initial_time : float | None
            The time to display on the plot initially. ``None`` to display the
            first time sample (default).
        time_unit : 's' | 'ms'
            Whether time is represented in seconds ("s", default) or
            milliseconds ("ms").

        show_traces : bool | str | float
            If True, enable interactive picking of a point on the surface of the
            brain and plot its time course.
            This feature is only available with the PyVista 3d backend, and requires
            ``time_viewer=True``. Defaults to 'auto', which will use True if and
            only if ``time_viewer=True``, the backend is PyVista, and there is more
            than one time point. If float (between zero and one), it specifies what
            proportion of the total window should be devoted to traces (True is
            equivalent to 0.25, i.e., it will occupy the bottom 1/4 of the figure).

            .. versionadded:: 0.20.0

        src : instance of SourceSpaces | None
            The source space corresponding to the source estimate. Only necessary
            if the STC is a volume or mixed source estimate.
        volume_options : float | dict | None
            Options for volumetric source estimate plotting, with key/value pairs:

            - ``'resolution'`` : float | None
                Resolution (in mm) of volume rendering. Smaller (e.g., 1.) looks
                better at the cost of speed. None (default) uses the volume source
                space resolution, which is often something like 7 or 5 mm,
                without resampling.
            - ``'blending'`` : str
                Can be "mip" (default) for :term:`maximum intensity projection` or
                "composite" for composite blending using alpha values.
            - ``'alpha'`` : float | None
                Alpha for the volumetric rendering. Defaults are 0.4 for vector source
                estimates and 1.0 for scalar source estimates.
            - ``'surface_alpha'`` : float | None
                Alpha for the surface enclosing the volume(s). None (default) will use
                half the volume alpha. Set to zero to avoid plotting the surface.
            - ``'silhouette_alpha'`` : float | None
                Alpha for a silhouette along the outside of the volume. None (default)
                will use ``0.25 * surface_alpha``.
            - ``'silhouette_linewidth'`` : float
                The line width to use for the silhouette. Default is 2.

            A float input (default 1.) or None will be used for the ``'resolution'``
            entry.

        view_layout : str
            Can be "vertical" (default) or "horizontal". When using "horizontal" mode,
            the PyVista backend must be used and hemi cannot be "split".

        add_data_kwargs : dict | None
            Additional arguments to brain.add_data (e.g.,
            ``dict(time_label_size=10)``).

        brain_kwargs : dict | None
            Additional arguments to the :class:`mne.viz.Brain` constructor (e.g.,
            ``dict(silhouette=True)``).

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        brain : mne.viz.Brain
            A instance of :class:`mne.viz.Brain`.

        Notes
        -----
        .. versionadded:: 0.15

        If the current magnitude overlay is not desired, set ``overlay_alpha=0``
        and ``smoothing_steps=1``.
        """
        ...

class VectorSourceEstimate(_BaseVectorSourceEstimate, _BaseSurfaceSourceEstimate):
    """Container for vector surface source estimates.

    For each vertex, the magnitude of the current is defined in the X, Y and Z
    directions.

    Parameters
    ----------
    data : array of shape (n_dipoles, 3, n_times)
        The data in source space. Each dipole contains three vectors that
        denote the dipole strength in X, Y and Z directions over time.
    vertices : list of array, shape (2,)
        Vertex numbers corresponding to the data. The first element of the list
        contains vertices of left hemisphere and the second element contains
        vertices of right hemisphere.

    tmin : scalar
        Time point of the first sample in data.

    tstep : scalar
        Time step between successive samples in data.

    subject : str
        The FreeSurfer subject name. While not necessary, it is safer to set the
        subject parameter to avoid analysis errors.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Attributes
    ----------
    subject : str | None
        The subject name.
    times : array of shape (n_times,)
        The time vector.
    shape : tuple
        The shape of the data. A tuple of int (n_dipoles, n_times).

    See Also
    --------
    SourceEstimate : A container for surface source estimates.
    VolSourceEstimate : A container for volume source estimates.
    MixedSourceEstimate : A container for mixed surface + volume source
                          estimates.

    Notes
    -----
    .. versionadded:: 0.15
    """

    ...

class _BaseMixedSourceEstimate(_BaseSourceEstimate):
    def __init__(
        self, data, vertices=None, tmin=None, tstep=None, subject=None, verbose=None
    ) -> None: ...
    def surface(self):
        """Return the cortical surface source estimate.

        Returns
        -------
        stc : instance of SourceEstimate or VectorSourceEstimate
            The surface source estimate.
        """
        ...
    def volume(self):
        """Return the volume surface source estimate.

        Returns
        -------
        stc : instance of VolSourceEstimate or VolVectorSourceEstimate
            The volume source estimate.
        """
        ...

class MixedSourceEstimate(_BaseMixedSourceEstimate):
    """Container for mixed surface and volume source estimates.

    Parameters
    ----------
    data : array of shape (n_dipoles, n_times) | tuple, shape (2,)
        The data in source space. The data can either be a single array or
        a tuple with two arrays: "kernel" shape (n_vertices, n_sensors) and
        "sens_data" shape (n_sensors, n_times). In this case, the source
        space data corresponds to ``np.dot(kernel, sens_data)``.
    vertices : list of array
        Vertex numbers corresponding to the data. The list contains arrays
        with one array per source space.

    tmin : scalar
        Time point of the first sample in data.

    tstep : scalar
        Time step between successive samples in data.

    subject : str
        The FreeSurfer subject name. While not necessary, it is safer to set the
        subject parameter to avoid analysis errors.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Attributes
    ----------
    subject : str | None
        The subject name.
    times : array of shape (n_times,)
        The time vector.
    vertices : list of array
        Vertex numbers corresponding to the data. The list contains arrays
        with one array per source space.
    data : array of shape (n_dipoles, n_times)
        The data in source space.
    shape : tuple
        The shape of the data. A tuple of int (n_dipoles, n_times).

    See Also
    --------
    SourceEstimate : A container for surface source estimates.
    VectorSourceEstimate : A container for vector surface source estimates.
    VolSourceEstimate : A container for volume source estimates.
    VolVectorSourceEstimate : A container for Volume vector source estimates.

    Notes
    -----
    .. versionadded:: 0.9.0
    """

    ...

class MixedVectorSourceEstimate(_BaseVectorSourceEstimate, _BaseMixedSourceEstimate):
    """Container for volume source estimates.

    Parameters
    ----------
    data : array, shape (n_dipoles, 3, n_times)
        The data in source space. Each dipole contains three vectors that
        denote the dipole strength in X, Y and Z directions over time.
    vertices : list of array, shape (n_src,)
        Vertex numbers corresponding to the data.

    tmin : scalar
        Time point of the first sample in data.

    tstep : scalar
        Time step between successive samples in data.

    subject : str
        The FreeSurfer subject name. While not necessary, it is safer to set the
        subject parameter to avoid analysis errors.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Attributes
    ----------
    subject : str | None
        The subject name.
    times : array, shape (n_times,)
        The time vector.
    vertices : array of shape (n_dipoles,)
        The indices of the dipoles in the source space.
    data : array of shape (n_dipoles, n_times)
        The data in source space.
    shape : tuple
        The shape of the data. A tuple of int (n_dipoles, n_times).

    See Also
    --------
    MixedSourceEstimate : A container for mixed surface + volume source
                          estimates.

    Notes
    -----
    .. versionadded:: 0.21.0
    """

    ...

def spatio_temporal_src_adjacency(src, n_times, dist=None, verbose=None):
    """Compute adjacency for a source space activation over time.

    Parameters
    ----------
    src : instance of SourceSpaces
        The source space. It can be a surface source space or a
        volume source space.
    n_times : int
        Number of time instants.
    dist : float, or None
        Maximal geodesic distance (in m) between vertices in the
        source space to consider neighbors. If None, immediate neighbors
        are extracted from an ico surface.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    adjacency : ~scipy.sparse.coo_matrix
        The adjacency matrix describing the spatio-temporal
        graph structure. If N is the number of vertices in the
        source space, the N first nodes in the graph are the
        vertices are time 1, the nodes from 2 to 2N are the vertices
        during time 2, etc.
    """
    ...

def grade_to_tris(grade, verbose=None):
    """Get tris defined for a certain grade.

    Parameters
    ----------
    grade : int
        Grade of an icosahedral mesh.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    tris : list
        2-element list containing Nx3 arrays of tris, suitable for use in
        spatio_temporal_tris_adjacency.
    """
    ...

def spatio_temporal_tris_adjacency(
    tris, n_times, remap_vertices: bool = False, verbose=None
):
    """Compute adjacency from triangles and time instants.

    Parameters
    ----------
    tris : array
        N x 3 array defining triangles.
    n_times : int
        Number of time points.
    remap_vertices : bool
        Reassign vertex indices based on unique values. Useful
        to process a subset of triangles. Defaults to False.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    adjacency : ~scipy.sparse.coo_matrix
        The adjacency matrix describing the spatio-temporal
        graph structure. If N is the number of vertices in the
        source space, the N first nodes in the graph are the
        vertices are time 1, the nodes from 2 to 2N are the vertices
        during time 2, etc.
    """
    ...

def spatio_temporal_dist_adjacency(src, n_times, dist, verbose=None):
    """Compute adjacency from distances in a source space and time instants.

    Parameters
    ----------
    src : instance of SourceSpaces
        The source space must have distances between vertices computed, such
        that src['dist'] exists and is useful. This can be obtained
        with a call to :func:`mne.setup_source_space` with the
        ``add_dist=True`` option.
    n_times : int
        Number of time points.
    dist : float
        Maximal geodesic distance (in m) between vertices in the
        source space to consider neighbors.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    adjacency : ~scipy.sparse.coo_matrix
        The adjacency matrix describing the spatio-temporal
        graph structure. If N is the number of vertices in the
        source space, the N first nodes in the graph are the
        vertices are time 1, the nodes from 2 to 2N are the vertices
        during time 2, etc.
    """
    ...

def spatial_src_adjacency(src, dist=None, verbose=None):
    """Compute adjacency for a source space activation.

    Parameters
    ----------
    src : instance of SourceSpaces
        The source space. It can be a surface source space or a
        volume source space.
    dist : float, or None
        Maximal geodesic distance (in m) between vertices in the
        source space to consider neighbors. If None, immediate neighbors
        are extracted from an ico surface.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    adjacency : ~scipy.sparse.coo_matrix
        The adjacency matrix describing the spatial graph structure.
    """
    ...

def spatial_tris_adjacency(tris, remap_vertices: bool = False, verbose=None):
    """Compute adjacency from triangles.

    Parameters
    ----------
    tris : array
        N x 3 array defining triangles.
    remap_vertices : bool
        Reassign vertex indices based on unique values. Useful
        to process a subset of triangles. Defaults to False.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    adjacency : ~scipy.sparse.coo_matrix
        The adjacency matrix describing the spatial graph structure.
    """
    ...

def spatial_dist_adjacency(src, dist, verbose=None):
    """Compute adjacency from distances in a source space.

    Parameters
    ----------
    src : instance of SourceSpaces
        The source space must have distances between vertices computed, such
        that src['dist'] exists and is useful. This can be obtained
        with a call to :func:`mne.setup_source_space` with the
        ``add_dist=True`` option.
    dist : float
        Maximal geodesic distance (in m) between vertices in the
        source space to consider neighbors.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    adjacency : ~scipy.sparse.coo_matrix
        The adjacency matrix describing the spatial graph structure.
    """
    ...

def spatial_inter_hemi_adjacency(src, dist, verbose=None):
    """Get vertices on each hemisphere that are close to the other hemisphere.

    Parameters
    ----------
    src : instance of SourceSpaces
        The source space. Must be surface type.
    dist : float
        Maximal Euclidean distance (in m) between vertices in one hemisphere
        compared to the other to consider neighbors.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    adjacency : ~scipy.sparse.coo_matrix
        The adjacency matrix describing the spatial graph structure.
        Typically this should be combined (addititively) with another
        existing intra-hemispheric adjacency matrix, e.g. computed
        using geodesic distances.
    """
    ...

def extract_label_time_course(
    stcs,
    labels,
    src,
    mode: str = "auto",
    allow_empty: bool = False,
    return_generator: bool = False,
    *,
    mri_resolution: bool = True,
    verbose=None,
):
    """Extract label time course for lists of labels and source estimates.

    This function will extract one time course for each label and source
    estimate. The way the time courses are extracted depends on the mode
    parameter (see Notes).

    Parameters
    ----------
    stcs : SourceEstimate | list (or generator) of SourceEstimate
        The source estimates from which to extract the time course.

    labels : Label | BiHemiLabel | list | tuple | str
        If using a surface or mixed source space, this should be the
        :class:mne.Label`'s for which to extract the time course.
        If working with whole-brain volume source estimates, this must be one of:

        - a string path to a FreeSurfer atlas for the subject (e.g., their
          'aparc.a2009s+aseg.mgz') to extract time courses for all volumes in the
          atlas
        - a two-element list or tuple, the first element being a path to an atlas,
          and the second being a list or dict of ``volume_labels`` to extract
          (see :func:`mne.setup_volume_source_space` for details).

        .. versionchanged:: 0.21.0
           Support for volume source estimates.

    src : instance of SourceSpaces
        The source spaces for the source time courses.

    mode : str
        Extraction mode, see Notes.

    allow_empty : bool | str
        ``False`` (default) will emit an error if there are labels that have no
        vertices in the source estimate. ``True`` and ``'ignore'`` will return
        all-zero time courses for labels that do not have any vertices in the
        source estimate, and True will emit a warning while and "ignore" will
        just log a message.

        .. versionchanged:: 0.21.0
           Support for "ignore".
    return_generator : bool
        If True, a generator instead of a list is returned.

    mri_resolution : bool
        If True (default), the volume source space will be upsampled to the
        original MRI resolution via trilinear interpolation before the atlas values
        are extracted. This ensnures that each atlas label will contain source
        activations. When False, only the original source space points are used,
        and some atlas labels thus may not contain any source space vertices.

        .. versionadded:: 0.21.0

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------

    label_tc : array | list (or generator) of array, shape (n_labels[, n_orient], n_times)
        Extracted time course for each label and source estimate.

    Notes
    -----

    Valid values for ``mode`` are:

    - ``'max'``
        Maximum value across vertices at each time point within each label.
    - ``'mean'``
        Average across vertices at each time point within each label. Ignores
        orientation of sources for standard source estimates, which varies
        across the cortical surface, which can lead to cancellation.
        Vector source estimates are always in XYZ / RAS orientation, and are thus
        already geometrically aligned.
    - ``'mean_flip'``
        Finds the dominant direction of source space normal vector orientations
        within each label, applies a sign-flip to time series at vertices whose
        orientation is more than 180° different from the dominant direction, and
        then averages across vertices at each time point within each label.
    - ``'pca_flip'``
        Applies singular value decomposition to the time courses within each label,
        and uses the first right-singular vector as the representative label time
        course. This signal is scaled so that its power matches the average
        (per-vertex) power within the label, and sign-flipped by multiplying by
        ``np.sign(u @ flip)``, where ``u`` is the first left-singular vector and
        ``flip`` is the same sign-flip vector used when ``mode='mean_flip'``. This
        sign-flip ensures that extracting time courses from the same label in
        similar STCs does not result in 180° direction/phase changes.
    - ``'auto'`` (default)
        Uses ``'mean_flip'`` when a standard source estimate is applied, and
        ``'mean'`` when a vector source estimate is supplied.
    - ``None``
        No aggregation is performed, and an array of shape ``(n_vertices, n_times)`` is
        returned.

        .. versionadded:: 0.21
           Support for ``'auto'``, vector, and volume source estimates.

    The only modes that work for vector and volume source estimates are ``'mean'``,
    ``'max'``, and ``'auto'``.

    If encountering a ``ValueError`` due to mismatch between number of
    source points in the subject source space and computed ``stc`` object set
    ``src`` argument to ``fwd['src']`` or ``inv['src']`` to ensure the source
    space is the one actually used by the inverse to compute the source
    time courses.
    """
    ...

def stc_near_sensors(
    evoked,
    trans,
    subject,
    distance: float = 0.01,
    mode: str = "sum",
    project: bool = True,
    subjects_dir=None,
    src=None,
    picks=None,
    surface: str = "pial",
    verbose=None,
):
    """Create a STC from ECoG, sEEG and DBS sensor data.

    Parameters
    ----------
    evoked : instance of Evoked
        The evoked data. Must contain ECoG, sEEG or DBS channels.

    trans : path-like | dict | instance of Transform | ``"fsaverage"`` | None
        If str, the path to the head<->MRI transform ``*-trans.fif`` file produced
        during coregistration. Can also be ``'fsaverage'`` to use the built-in
        fsaverage transformation.
        If trans is None, an identity matrix is assumed.

        .. versionchanged:: 0.19
            Support for 'fsaverage' argument.
    subject : str
        The subject name.
    distance : float
        Distance (m) defining the activation "ball" of the sensor.
    mode : str
        Can be ``"sum"`` to do a linear sum of weights, ``"weighted"`` to make
        this a weighted sum, ``"nearest"`` to use only the weight of the
        nearest sensor, or ``"single"`` to do a distance-weight of the nearest
        sensor. Default is ``"sum"``. See Notes.

        .. versionchanged:: 0.24
           Added "weighted" option.
    project : bool
        If True, project the sensors to the nearest ``'pial`` surface
        vertex before computing distances. Only used when doing a
        surface projection.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    src : instance of SourceSpaces
        The source space.

        .. warning:: If a surface source space is used, make sure that
                     ``surface='pial'`` was used during construction,
                     or that you set ``surface='pial'`` here.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick good sEEG, ECoG, and DBS channels.

        .. versionadded:: 0.24
    surface : str | None
        The surface to use if ``src=None``. Default is the pial surface.
        If None, the source space surface will be used.

        .. versionadded:: 0.24.1

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    stc : instance of SourceEstimate
        The surface source estimate. If src is None, a surface source
        estimate will be produced, and the number of vertices will equal
        the number of pial-surface vertices that were close enough to
        the sensors to take on a non-zero volue. If src is not None,
        a surface, volume, or mixed source estimate will be produced
        (depending on the kind of source space passed) and the
        vertices will match those of src (i.e., there may be me
        many all-zero values in stc.data).

    Notes
    -----
    For surface projections, this function projects the ECoG sensors to
    the pial surface (if ``project``), then the activation at each pial
    surface vertex is given by the mode:

    - ``'sum'``
        Activation is the sum across each sensor weighted by the fractional
        ``distance`` from each sensor. A sensor with zero distance gets weight
        1 and a sensor at ``distance`` meters away (or larger) gets weight 0.
        If ``distance`` is less than half the distance between any two
        sensors, this will be the same as ``'single'``.
    - ``'single'``
        Same as ``'sum'`` except that only the nearest sensor is used,
        rather than summing across sensors within the ``distance`` radius.
        As ``'nearest'`` for vertices with distance zero to the projected
        sensor.
    - ``'nearest'``
        The value is given by the value of the nearest sensor, up to a
        ``distance`` (beyond which it is zero).
    - ``'weighted'``
        The value is given by the same as ``sum`` but the total weight for
        each vertex is 1. (i.e., it's a weighted sum based on proximity).

    If creating a Volume STC, ``src`` must be passed in, and this
    function will project sEEG and DBS sensors to nearby surrounding vertices.
    Then the activation at each volume vertex is given by the mode
    in the same way as ECoG surface projections.

    .. versionadded:: 0.22
    """
    ...
