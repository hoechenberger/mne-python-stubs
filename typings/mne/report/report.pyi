from .._fiff.meas_info import Info as Info, read_info as read_info
from ..cov import Covariance as Covariance, read_cov as read_cov
from ..epochs import BaseEpochs as BaseEpochs, read_epochs as read_epochs
from ..event import read_events as read_events
from ..evoked import Evoked as Evoked, read_evokeds as read_evokeds
from ..forward import Forward as Forward, read_forward_solution as read_forward_solution
from ..io import BaseRaw as BaseRaw, read_raw as read_raw
from ..minimum_norm import (
    InverseOperator as InverseOperator,
    read_inverse_operator as read_inverse_operator,
)
from ..parallel import parallel_func as parallel_func
from ..preprocessing.ica import read_ica as read_ica
from ..proj import read_proj as read_proj
from ..source_estimate import (
    SourceEstimate as SourceEstimate,
    read_source_estimate as read_source_estimate,
)
from ..surface import dig_mri_distances as dig_mri_distances
from ..transforms import Transform as Transform, read_trans as read_trans
from ..utils import (
    check_version as check_version,
    fill_doc as fill_doc,
    get_subjects_dir as get_subjects_dir,
    logger as logger,
    sys_info as sys_info,
    use_log_level as use_log_level,
    warn as warn,
)
from ..viz import (
    Figure3D as Figure3D,
    create_3d_figure as create_3d_figure,
    get_3d_backend as get_3d_backend,
    plot_alignment as plot_alignment,
    plot_compare_evokeds as plot_compare_evokeds,
    plot_cov as plot_cov,
    plot_events as plot_events,
    plot_projs_topomap as plot_projs_topomap,
    set_3d_view as set_3d_view,
    use_browser_backend as use_browser_backend,
)
from ..viz._brain.view import views_dicts as views_dicts
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Optional, Tuple

SUPPORTED_READ_RAW_EXTENSIONS: Incomplete
RAW_EXTENSIONS: Incomplete
VALID_EXTENSIONS: Incomplete
CONTENT_ORDER: Incomplete
html_include_dir: Incomplete
template_dir: Incomplete
JAVASCRIPT: Incomplete
CSS: Incomplete
MAX_IMG_RES: int
MAX_IMG_WIDTH: int

@dataclass
class _ContentElement:
    name: str
    section: Optional[str]
    dom_id: str
    tags: Tuple[str]
    html: str

    def __init__(self, name, section, dom_id, tags, html) -> None: ...

def open_report(fname, **params):
    """### Read a saved report or, if it doesn't exist yet, create a new one.

    The returned report can be used as a context manager, in which case any
    changes to the report are saved when exiting the context block.

    -----
    ### 🛠️ Parameters

    fname : path-like
        The file containing the report, stored in the HDF5 format. If the file
        does not exist yet, a new report is created that will be saved to the
        specified file.
    **params : kwargs
        When creating a new report, any named parameters other than ``fname``
        are passed to the ``__init__`` function of the `Report` object. When
        reading an existing report, the parameters are checked with the
        loaded report and an exception is raised when they don't match.

    -----
    ### ⏎ Returns

    report : instance of Report
        The report.
    """
    ...

mne_logo_path: Incomplete
mne_logo: Incomplete

class Report:
    """### Object for rendering HTML.

    -----
    ### 🛠️ Parameters

    info_fname : None | str
        Name of the file containing the info dictionary.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    subject : str | None
        Subject name.
    title : str
        Title of the report.
    cov_fname : None | str
        Name of the file containing the noise covariance.

    baseline : None | tuple of length 2
        The time interval to consider as "baseline" when applying baseline
        correction. If ``None``, do not apply baseline correction.
        If a tuple ``(a, b)``, the interval is between ``a`` and ``b``
        (in seconds), including the endpoints.
        If ``a`` is ``None``, the **beginning** of the data is used; and if ``b``
        is ``None``, it is set to the **end** of the interval.
        If ``(None, None)``, the entire time interval is used.

        ### 💡 Note The baseline ``(a, b)`` includes both endpoints, i.e. all
                    timepoints ``t`` such that ``a <= t <= b``.

        Correction is applied in the following way **to each channel:**

        1. Calculate the mean signal of the baseline period.
        2. Subtract this mean from the **entire** time period.

        For `mne.Epochs`, this algorithm is run **on each epoch individually.**
        Defaults to ``None``, i.e. no baseline correction.
    image_format : 'png' | 'svg' | 'webp' | 'auto'
        Default image format to use (default is ``'auto'``, which will use
        ``'webp'`` if available and ``'png'`` otherwise).
        ``'svg'`` uses vector graphics, so fidelity is higher but can increase
        file size and browser image rendering time as well.
        ``'webp'`` format requires matplotlib >= 3.6.

        ✨ Added in vesion 0.15
        🎭 Changed in version 1.3
           Added support for ``'webp'`` format, removed support for GIF, and
           set the default to ``'auto'``.
    raw_psd : bool | dict
        If True, include PSD plots for raw files. Can be False (default) to
        omit, True to plot, or a dict to pass as ``kwargs`` to
        `mne.time_frequency.Spectrum.plot`.

        ✨ Added in vesion 0.17
        🎭 Changed in version 1.4
           kwargs are sent to ``spectrum.plot`` instead of ``raw.plot_psd``.
    projs : bool
        Whether to include topographic plots of SSP projectors, if present in
        the data. Defaults to ``False``.

        ✨ Added in vesion 0.21

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### 📊 Attributes

    info_fname : None | str
        Name of the file containing the info dictionary.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    subject : str | None
        Subject name.
    title : str
        Title of the report.
    cov_fname : None | str
        Name of the file containing the noise covariance.

    baseline : None | tuple of length 2
        The time interval to consider as "baseline" when applying baseline
        correction. If ``None``, do not apply baseline correction.
        If a tuple ``(a, b)``, the interval is between ``a`` and ``b``
        (in seconds), including the endpoints.
        If ``a`` is ``None``, the **beginning** of the data is used; and if ``b``
        is ``None``, it is set to the **end** of the interval.
        If ``(None, None)``, the entire time interval is used.

        ### 💡 Note The baseline ``(a, b)`` includes both endpoints, i.e. all
                    timepoints ``t`` such that ``a <= t <= b``.

        Correction is applied in the following way **to each channel:**

        1. Calculate the mean signal of the baseline period.
        2. Subtract this mean from the **entire** time period.

        For `mne.Epochs`, this algorithm is run **on each epoch individually.**
        Defaults to ``None``, i.e. no baseline correction.
    image_format : str
        Default image format to use.

        ✨ Added in vesion 0.15
    raw_psd : bool | dict
        If True, include PSD plots for raw files. Can be False (default) to
        omit, True to plot, or a dict to pass as ``kwargs`` to
        `mne.time_frequency.Spectrum.plot`.

        ✨ Added in vesion 0.17
        🎭 Changed in version 1.4
           kwargs are sent to ``spectrum.plot`` instead of ``raw.plot_psd``.
    projs : bool
        Whether to include topographic plots of SSP projectors, if present in
        the data. Defaults to ``False``.

        ✨ Added in vesion 0.21

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.
    html : list of str
        Contains items of html-page.
    include : list of str
        Dictionary containing elements included in head.
    fnames : list of str
        List of file names rendered.
    sections : list of str
        List of sections.
    lang : str
        language setting for the HTML file.

    -----
    ### 📖 Notes

    See `tut-report` for an introduction to using ``mne.Report``.

    ✨ Added in vesion 0.8.0
    """

    info_fname: Incomplete
    cov_fname: Incomplete
    baseline: Incomplete
    subjects_dir: Incomplete
    subject: Incomplete
    title: Incomplete
    image_format: Incomplete
    projs: Incomplete
    include: Incomplete
    lang: str
    raw_psd: Incomplete
    fname: Incomplete
    data_path: Incomplete

    def __init__(
        self,
        info_fname=None,
        subjects_dir=None,
        subject=None,
        title=None,
        cov_fname=None,
        baseline=None,
        image_format: str = "auto",
        raw_psd: bool = False,
        projs: bool = False,
        *,
        verbose=None,
    ) -> None: ...
    def __len__(self) -> int:
        """### Return the number of files processed by the report.

        -----
        ### ⏎ Returns

        n_files : int
            The number of files processed.
        """
        ...
    @property
    def html(self):
        """### A list of HTML representations for all content elements."""
        ...
    @property
    def tags(self):
        """### All tags currently used in the report."""
        ...
    def add_custom_css(self, css) -> None:
        """### Add custom CSS to the report.

        -----
        ### 🛠️ Parameters

        css : str
            Style definitions to add to the report. The content of this string
            will be embedded between HTML ``<style>`` and ``</style>`` tags.

        -----
        ### 📖 Notes

        ✨ Added in vesion 0.23
        """
        ...
    def add_custom_js(self, js) -> None:
        """### Add custom JavaScript to the report.

        -----
        ### 🛠️ Parameters

        js : str
            JavaScript code to add to the report. The content of this string
            will be embedded between HTML ``<script>`` and ``</script>`` tags.

        -----
        ### 📖 Notes

        ✨ Added in vesion 0.23
        """
        ...
    def add_epochs(
        self,
        epochs,
        title,
        *,
        psd: bool = True,
        projs=None,
        topomap_kwargs=None,
        drop_log_ignore=("IGNORED",),
        tags=("epochs",),
        replace: bool = False,
    ) -> None:
        """### Add `mne.Epochs` to the report.

        -----
        ### 🛠️ Parameters

        epochs : path-like | instance of Epochs
            The epochs to add to the report.
        title : str
            The title to add.
        psd : bool | float
            If a float, the duration of data to use for creation of PSD plots,
            in seconds. PSD will be calculated on as many epochs as required to
            cover at least this duration. Epochs will be picked across the
            entire time range in equally-spaced distance.

            ### 💡 Note
              In rare edge cases, we may not be able to create a grid of
              equally-spaced epochs that cover the entire requested time range.
              In these situations, a warning will be emitted, informing you
              about the duration that's actually being used.

            If ``True``, add PSD plots based on all ``epochs``. If ``False``,
            do not add PSD plots.

        projs : bool | None
            Whether to add SSP projector plots if projectors are present in
            the data. If ``None``, use ``projs`` from `mne.Report` creation.

        topomap_kwargs : dict | None
            Keyword arguments to pass to the topomap-generating functions.
        drop_log_ignore : array-like of str
            The drop reasons to ignore when creating the drop log bar plot.
            All epochs for which a drop reason listed here appears in
            ``epochs.drop_log`` will be excluded from the drop log plot.

        tags : array-like of str | str
            Tags to add for later interactive filtering. Must not contain spaces.

        replace : bool
            If ``True``, content already present that has the same ``title`` and
            ``section`` will be replaced. Defaults to ``False``, which will cause
            duplicate entries in the table of contents if an entry for ``title``
            already exists.

        -----
        ### 📖 Notes

        ✨ Added in vesion 0.24.0
        """
        ...
    def add_evokeds(
        self,
        evokeds,
        *,
        titles=None,
        noise_cov=None,
        projs=None,
        n_time_points=None,
        tags=("evoked",),
        replace: bool = False,
        topomap_kwargs=None,
        n_jobs=None,
    ) -> None:
        """### Add `mne.Evoked` objects to the report.

        -----
        ### 🛠️ Parameters

        evokeds : path-like | instance of Evoked | list of Evoked
            The evoked data to add to the report. Multiple `mne.Evoked`
            objects – as returned from `mne.read_evokeds` – can be passed as
            a list.
        titles : str | list of str | None
            The titles corresponding to the evoked data. If ``None``, the
            content of ``evoked.comment`` from each evoked will be used as
            title.
        noise_cov : path-like | instance of Covariance | None
            A noise covariance matrix. If provided, will be used to whiten
            the ``evokeds``. If ``None``, will fall back to the ``cov_fname``
            provided upon report creation.

        projs : bool | None
            Whether to add SSP projector plots if projectors are present in
            the data. If ``None``, use ``projs`` from `mne.Report` creation.
        n_time_points : int | None
            The number of equidistant time points to render. If ``None``,
            will render each `mne.Evoked` at 21 time points, unless the data
            contains fewer time points, in which case all will be rendered.

        tags : array-like of str | str
            Tags to add for later interactive filtering. Must not contain spaces.

        replace : bool
            If ``True``, content already present that has the same ``title`` and
            ``section`` will be replaced. Defaults to ``False``, which will cause
            duplicate entries in the table of contents if an entry for ``title``
            already exists.

        topomap_kwargs : dict | None
            Keyword arguments to pass to the topomap-generating functions.
        n_jobs : int | None
            The number of jobs to run in parallel. If ``-1``, it is set
            to the number of CPU cores. Requires the `joblib` package.
            ``None`` (default) is a marker for 'unset' that will be interpreted
            as ``n_jobs=1`` (sequential execution) unless the call is performed under
            a `joblib:joblib.parallel_config` context manager that sets another
            value for ``n_jobs``.

        -----
        ### 📖 Notes

        ✨ Added in vesion 0.24.0
        """
        ...
    def add_raw(
        self,
        raw,
        title,
        *,
        psd=None,
        projs=None,
        butterfly: bool = True,
        scalings=None,
        tags=("raw",),
        replace: bool = False,
        topomap_kwargs=None,
    ) -> None:
        """### Add `mne.io.Raw` objects to the report.

        -----
        ### 🛠️ Parameters

        raw : path-like | instance of Raw
            The data to add to the report.
        title : str
            The title corresponding to the ``raw`` object.
        psd : bool | None
            Whether to add PSD plots. Overrides the ``raw_psd`` parameter
            passed when initializing the `mne.Report`. If ``None``, use
            ``raw_psd`` from `mne.Report` creation.

        projs : bool | None
            Whether to add SSP projector plots if projectors are present in
            the data. If ``None``, use ``projs`` from `mne.Report` creation.
        butterfly : bool | int
            Whether to add butterfly plots of the data. Can be useful to
            spot problematic channels. If ``True``, 10 equally-spaced 1-second
            segments will be plotted. If an integer, specifies the number of
            1-second segments to plot. Larger numbers may take a considerable
            amount of time if the data contains many sensors. You can disable
            butterfly plots altogether by passing ``False``.

        scalings : 'auto' | dict | None
            Scaling factors for the traces. If a dictionary where any
            value is ``'auto'``, the scaling factor is set to match the 99.5th
            percentile of the respective data. If ``'auto'``, all scalings (for all
            channel types) are set to ``'auto'``. If any values are ``'auto'`` and the
            data is not preloaded, a subset up to 100 MB will be loaded. If ``None``,
            defaults to::

                dict(mag=1e-12, grad=4e-11, eeg=20e-6, eog=150e-6, ecg=5e-4,
                     emg=1e-3, ref_meg=1e-12, misc=1e-3, stim=1,
                     resp=1, chpi=1e-4, whitened=1e2)

            ### 💡 Note
                A particular scaling value ``s`` corresponds to half of the visualized
                signal range around zero (i.e. from ``0`` to ``+s`` or from ``0`` to
                ``-s``). For example, the default scaling of ``20e-6`` (20µV) for EEG
                signals means that the visualized range will be 40 µV (20 µV in the
                positive direction and 20 µV in the negative direction).

        tags : array-like of str | str
            Tags to add for later interactive filtering. Must not contain spaces.

        replace : bool
            If ``True``, content already present that has the same ``title`` and
            ``section`` will be replaced. Defaults to ``False``, which will cause
            duplicate entries in the table of contents if an entry for ``title``
            already exists.

        topomap_kwargs : dict | None
            Keyword arguments to pass to the topomap-generating functions.

        -----
        ### 📖 Notes

        ✨ Added in vesion 0.24.0
        """
        ...
    def add_stc(
        self,
        stc,
        title,
        *,
        subject=None,
        subjects_dir=None,
        n_time_points=None,
        tags=("source-estimate",),
        replace: bool = False,
        stc_plot_kwargs=None,
    ) -> None:
        """### Add a `mne.SourceEstimate` (STC) to the report.

        -----
        ### 🛠️ Parameters

        stc : path-like | instance of SourceEstimate
            The `mne.SourceEstimate` to add to the report.
        title : str
            The title to add.
        subject : str | None
            The name of the FreeSurfer subject the STC belongs to. The name is
            not stored with the STC data and therefore needs to be specified.
            If ``None``, will use the value of ``subject`` passed on report
            creation.
        subjects_dir : path-like | None
            The FreeSurfer ``SUBJECTS_DIR``.
        n_time_points : int | None
            The number of equidistant time points to render. If ``None``,
            will render ``stc`` at 51 time points, unless the data
            contains fewer time points, in which case all will be rendered.

        tags : array-like of str | str
            Tags to add for later interactive filtering. Must not contain spaces.

        replace : bool
            If ``True``, content already present that has the same ``title`` and
            ``section`` will be replaced. Defaults to ``False``, which will cause
            duplicate entries in the table of contents if an entry for ``title``
            already exists.

        stc_plot_kwargs : dict
            Dictionary of keyword arguments to pass to
            `mne.SourceEstimate.plot`. Only used when plotting in 3D
            mode.

        -----
        ### 📖 Notes

        ✨ Added in vesion 0.24.0
        """
        ...
    def add_forward(
        self,
        forward,
        title,
        *,
        subject=None,
        subjects_dir=None,
        tags=("forward-solution",),
        replace: bool = False,
    ) -> None:
        """### Add a forward solution.

        -----
        ### 🛠️ Parameters

        forward : instance of Forward | path-like
            The forward solution to add to the report.
        title : str
            The title corresponding to forward solution.
        subject : str | None
            The name of the FreeSurfer subject ``forward`` belongs to. If
            provided, the sensitivity maps of the forward solution will
            be visualized. If ``None``, will use the value of ``subject``
            passed on report creation. If supplied, also pass ``subjects_dir``.
        subjects_dir : path-like | None
            The FreeSurfer ``SUBJECTS_DIR``.

        tags : array-like of str | str
            Tags to add for later interactive filtering. Must not contain spaces.

        replace : bool
            If ``True``, content already present that has the same ``title`` and
            ``section`` will be replaced. Defaults to ``False``, which will cause
            duplicate entries in the table of contents if an entry for ``title``
            already exists.

        -----
        ### 📖 Notes

        ✨ Added in vesion 0.24.0
        """
        ...
    def add_inverse_operator(
        self,
        inverse_operator,
        title,
        *,
        subject=None,
        subjects_dir=None,
        trans=None,
        tags=("inverse-operator",),
        replace: bool = False,
    ) -> None:
        """### Add an inverse operator.

        -----
        ### 🛠️ Parameters

        inverse_operator : instance of InverseOperator | path-like
            The inverse operator to add to the report.
        title : str
            The title corresponding to the inverse operator object.
        subject : str | None
            The name of the FreeSurfer subject ``inverse_op`` belongs to. If
            provided, the source space the inverse solution is based on will
            be visualized. If ``None``, will use the value of ``subject``
            passed on report creation. If supplied, also pass ``subjects_dir``
            and ``trans``.
        subjects_dir : path-like | None
            The FreeSurfer ``SUBJECTS_DIR``.
        trans : path-like | instance of Transform | None
            The ``head -> MRI`` transformation for ``subject``.

        tags : array-like of str | str
            Tags to add for later interactive filtering. Must not contain spaces.

        replace : bool
            If ``True``, content already present that has the same ``title`` and
            ``section`` will be replaced. Defaults to ``False``, which will cause
            duplicate entries in the table of contents if an entry for ``title``
            already exists.

        -----
        ### 📖 Notes

        ✨ Added in vesion 0.24.0
        """
        ...
    def add_trans(
        self,
        trans,
        *,
        info,
        title,
        subject=None,
        subjects_dir=None,
        alpha=None,
        tags=("coregistration",),
        replace: bool = False,
    ) -> None:
        """### Add a coregistration visualization to the report.

        -----
        ### 🛠️ Parameters

        trans : path-like | instance of Transform
            The ``head -> MRI`` transformation to render.
        info : path-like | instance of Info
            The `mne.Info` corresponding to ``trans``.
        title : str
            The title to add.
        subject : str | None
            The name of the FreeSurfer subject the ``trans```` belong to. The
            name is not stored with the ``trans`` and therefore needs to be
            specified. If ``None``, will use the value of ``subject`` passed on
            report creation.
        subjects_dir : path-like | None
            The FreeSurfer ``SUBJECTS_DIR``.
        alpha : float | None
            The level of opacity to apply to the head surface. If a float, must
            be between 0 and 1 (inclusive), where 1 means fully opaque. If
            ``None``, will use the MNE-Python default value.

        tags : array-like of str | str
            Tags to add for later interactive filtering. Must not contain spaces.

        replace : bool
            If ``True``, content already present that has the same ``title`` and
            ``section`` will be replaced. Defaults to ``False``, which will cause
            duplicate entries in the table of contents if an entry for ``title``
            already exists.

        -----
        ### 📖 Notes

        ✨ Added in vesion 0.24.0
        """
        ...
    def add_covariance(
        self, cov, *, info, title, tags=("covariance",), replace: bool = False
    ) -> None:
        """### Add covariance to the report.

        -----
        ### 🛠️ Parameters

        cov : path-like | instance of Covariance
            The `mne.Covariance` to add to the report.
        info : path-like | instance of Info
            The `mne.Info` corresponding to ``cov``.
        title : str
            The title corresponding to the `mne.Covariance` object.

        tags : array-like of str | str
            Tags to add for later interactive filtering. Must not contain spaces.

        replace : bool
            If ``True``, content already present that has the same ``title`` and
            ``section`` will be replaced. Defaults to ``False``, which will cause
            duplicate entries in the table of contents if an entry for ``title``
            already exists.

        -----
        ### 📖 Notes

        ✨ Added in vesion 0.24.0
        """
        ...
    def add_events(
        self,
        events,
        title,
        *,
        event_id=None,
        sfreq,
        first_samp: int = 0,
        tags=("events",),
        replace: bool = False,
    ) -> None:
        """### Add events to the report.

        -----
        ### 🛠️ Parameters

        events : path-like | array, shape (n_events, 3)
            An MNE-Python events array.
        title : str
            The title corresponding to the events.
        event_id : dict
            A dictionary mapping event names (keys) to event codes (values).
        sfreq : float
            The sampling frequency used while recording.
        first_samp : int
            The first sample point in the recording. This corresponds to
            ``raw.first_samp`` on files created with Elekta/Neuromag systems.

        tags : array-like of str | str
            Tags to add for later interactive filtering. Must not contain spaces.

        replace : bool
            If ``True``, content already present that has the same ``title`` and
            ``section`` will be replaced. Defaults to ``False``, which will cause
            duplicate entries in the table of contents if an entry for ``title``
            already exists.

        -----
        ### 📖 Notes

        ✨ Added in vesion 0.24.0
        """
        ...
    def add_projs(
        self,
        *,
        info,
        projs=None,
        title,
        topomap_kwargs=None,
        tags=("ssp",),
        replace: bool = False,
    ) -> None:
        """### Render (SSP) projection vectors.

        -----
        ### 🛠️ Parameters

        info : instance of Info | path-like
            An `mne.Info` structure or the path of a file containing one. This
            is required to create the topographic plots.
        projs : iterable of mne.Projection | path-like | None
            The projection vectors to add to the report. Can be the path to a
            file that will be loaded via `mne.read_proj`. If ``None``, the
            projectors are taken from ``info['projs']``.
        title : str
            The title corresponding to the `mne.Projection` object.

        topomap_kwargs : dict | None
            Keyword arguments to pass to the topomap-generating functions.

        tags : array-like of str | str
            Tags to add for later interactive filtering. Must not contain spaces.

        replace : bool
            If ``True``, content already present that has the same ``title`` and
            ``section`` will be replaced. Defaults to ``False``, which will cause
            duplicate entries in the table of contents if an entry for ``title``
            already exists.

        -----
        ### 📖 Notes

        ✨ Added in vesion 0.24.0
        """
        ...
    def add_ica(
        self,
        ica,
        title,
        *,
        inst,
        picks=None,
        ecg_evoked=None,
        eog_evoked=None,
        ecg_scores=None,
        eog_scores=None,
        n_jobs=None,
        tags=("ica",),
        replace: bool = False,
    ) -> None:
        """### Add (a fitted) `mne.preprocessing.ICA` to the report.

        -----
        ### 🛠️ Parameters

        ica : path-like | instance of mne.preprocessing.ICA
            The fitted ICA to add.
        title : str
            The title to add.
        inst : path-like | mne.io.Raw | mne.Epochs | None
            The data to use for visualization of the effects of ICA cleaning.
            To only plot the ICA component topographies, explicitly pass
            ``None``.

        picks : int | list of int | slice | None
            Indices of the independent components (ICs) to visualize.
            If an integer, represents the index of the IC to pick.
            Multiple ICs can be selected using a list of int or a slice.
            The indices are 0-indexed, so ``picks=1`` will pick the second
            IC: ``ICA001``. ``None`` will pick all independent components in the order
            fitted. This only affects the behavior of the component
            topography and properties plots.
        ecg_evoked, eog_evoked : path-line | mne.Evoked | None
            Evoked signal based on ECG and EOG epochs, respectively. If passed,
            will be used to visualize the effects of artifact rejection.
        ecg_scores, eog_scores : array of float | list of array of float | None
            The scores produced by `mne.preprocessing.ICA.find_bads_ecg`
            and `mne.preprocessing.ICA.find_bads_eog`, respectively.
            If passed, will be used to visualize the scoring for each ICA
            component.
        n_jobs : int | None
            The number of jobs to run in parallel. If ``-1``, it is set
            to the number of CPU cores. Requires the `joblib` package.
            ``None`` (default) is a marker for 'unset' that will be interpreted
            as ``n_jobs=1`` (sequential execution) unless the call is performed under
            a `joblib:joblib.parallel_config` context manager that sets another
            value for ``n_jobs``.

        tags : array-like of str | str
            Tags to add for later interactive filtering. Must not contain spaces.

        replace : bool
            If ``True``, content already present that has the same ``title`` and
            ``section`` will be replaced. Defaults to ``False``, which will cause
            duplicate entries in the table of contents if an entry for ``title``
            already exists.

        -----
        ### 📖 Notes

        ✨ Added in vesion 0.24.0
        """
        ...
    def remove(self, *, title=None, tags=None, remove_all: bool = False):
        """### Remove elements from the report.

        The element to remove is searched for by its title. Optionally, tags
        may be specified as well to narrow down the search to elements that
        have the supplied tags.

        -----
        ### 🛠️ Parameters

        title : str
            The title of the element(s) to remove.

            ✨ Added in vesion 0.24.0
        tags : array-like of str | str | None
             If supplied, restrict the operation to elements with the supplied
             tags.

            ✨ Added in vesion 0.24.0
        remove_all : bool
            Controls the behavior if multiple elements match the search
            criteria. If ``False`` (default) only the element last added to the
            report will be removed. If ``True``, all matches will be removed.

            ✨ Added in vesion 0.24.0

        -----
        ### ⏎ Returns

        removed_index : int | tuple of int | None
            The indices of the elements that were removed, or ``None`` if no
            element matched the search criteria. A tuple will always be
            returned if ``remove_all`` was set to ``True`` and at least one
            element was removed.

            🎭 Changed in version 0.24.0
               Returns tuple if ``remove_all`` is ``True``.
        """
        ...
    def add_code(
        self,
        code,
        title,
        *,
        language: str = "python",
        tags=("code",),
        replace: bool = False,
    ) -> None:
        """### Add a code snippet (e.g., an analysis script) to the report.

        -----
        ### 🛠️ Parameters

        code : str | pathlib.Path
            The code to add to the report as a string, or the path to a file
            as a `pathlib.Path` object.

            ### 💡 Note Paths must be passed as `pathlib.Path` object, since
                      strings will be treated as literal code.
        title : str
            The title corresponding to the code.
        language : str
            The programming language of ``code``. This will be used for syntax
            highlighting. Can be ``'auto'`` to try to auto-detect the language.

        tags : array-like of str | str
            Tags to add for later interactive filtering. Must not contain spaces.

        replace : bool
            If ``True``, content already present that has the same ``title`` and
            ``section`` will be replaced. Defaults to ``False``, which will cause
            duplicate entries in the table of contents if an entry for ``title``
            already exists.

        -----
        ### 📖 Notes

        ✨ Added in vesion 0.24.0
        """
        ...
    def add_sys_info(
        self, title, *, tags=("mne-sysinfo",), replace: bool = False
    ) -> None:
        """### Add a MNE-Python system information to the report.

        This is a convenience method that captures the output of
        `mne.sys_info` and adds it to the report.

        -----
        ### 🛠️ Parameters

        title : str
            The title to assign.

        tags : array-like of str | str
            Tags to add for later interactive filtering. Must not contain spaces.

        replace : bool
            If ``True``, content already present that has the same ``title`` and
            ``section`` will be replaced. Defaults to ``False``, which will cause
            duplicate entries in the table of contents if an entry for ``title``
            already exists.

        -----
        ### 📖 Notes

        ✨ Added in vesion 0.24.0
        """
        ...
    def add_figure(
        self,
        fig,
        title,
        *,
        caption=None,
        image_format=None,
        tags=("custom-figure",),
        section=None,
        replace: bool = False,
    ) -> None:
        """### Add figures to the report.

        -----
        ### 🛠️ Parameters

        fig : matplotlib.figure.Figure | Figure3D | array | array-like of matplotlib.figure.Figure | array-like of Figure3D | array-like of array
            One or more figures to add to the report. All figures must be an
            instance of `matplotlib.figure.Figure`,
            `mne.viz.Figure3D`, or `numpy.ndarray`. If
            multiple figures are passed, they will be added as "slides"
            that can be navigated using buttons and a slider element.
        title : str
            The title corresponding to the figure(s).
        caption : str | array-like of str | None
            The caption(s) to add to the figure(s).

        image_format : 'png' | 'svg' | 'gif' | None
            The image format to be used for the report, can be ``'png'``,
            ``'svg'``, or ``'gif'``.
            None (default) will use the default specified during `mne.Report`
            instantiation.

        tags : array-like of str | str
            Tags to add for later interactive filtering. Must not contain spaces.

        section : str | None
            The name of the section (or content block) to add the content to. This
            feature is useful for grouping multiple related content elements
            together under a single, collapsible section. Each content element will
            retain its own title and functionality, but not appear separately in the
            table of contents. Hence, using sections is a way to declutter the table
            of contents, and to easy navigation of the report.

            ✨ Added in vesion 1.1

        replace : bool
            If ``True``, content already present that has the same ``title`` and
            ``section`` will be replaced. Defaults to ``False``, which will cause
            duplicate entries in the table of contents if an entry for ``title``
            already exists.

        -----
        ### 📖 Notes

        ✨ Added in vesion 0.24.0
        """
        ...
    def add_image(
        self,
        image,
        title,
        *,
        caption=None,
        tags=("custom-image",),
        section=None,
        replace: bool = False,
    ) -> None:
        """### Add an image (e.g., PNG or JPEG pictures) to the report.

        -----
        ### 🛠️ Parameters

        image : path-like
            The image to add.
        title : str
            Title corresponding to the images.
        caption : str | None
            If not ``None``, the caption to add to the image.

        tags : array-like of str | str
            Tags to add for later interactive filtering. Must not contain spaces.

        section : str | None
            The name of the section (or content block) to add the content to. This
            feature is useful for grouping multiple related content elements
            together under a single, collapsible section. Each content element will
            retain its own title and functionality, but not appear separately in the
            table of contents. Hence, using sections is a way to declutter the table
            of contents, and to easy navigation of the report.

            ✨ Added in vesion 1.1

        replace : bool
            If ``True``, content already present that has the same ``title`` and
            ``section`` will be replaced. Defaults to ``False``, which will cause
            duplicate entries in the table of contents if an entry for ``title``
            already exists.

        -----
        ### 📖 Notes

        ✨ Added in vesion 0.24.0
        """
        ...
    def add_html(
        self, html, title, *, tags=("custom-html",), section=None, replace: bool = False
    ) -> None:
        """### Add HTML content to the report.

        -----
        ### 🛠️ Parameters

        html : str
            The HTML content to add.
        title : str
            The title corresponding to ``html``.

        tags : array-like of str | str
            Tags to add for later interactive filtering. Must not contain spaces.

        section : str | None
            The name of the section (or content block) to add the content to. This
            feature is useful for grouping multiple related content elements
            together under a single, collapsible section. Each content element will
            retain its own title and functionality, but not appear separately in the
            table of contents. Hence, using sections is a way to declutter the table
            of contents, and to easy navigation of the report.

            ✨ Added in vesion 1.1

            ✨ Added in vesion 1.3

        replace : bool
            If ``True``, content already present that has the same ``title`` and
            ``section`` will be replaced. Defaults to ``False``, which will cause
            duplicate entries in the table of contents if an entry for ``title``
            already exists.

        -----
        ### 📖 Notes

        ✨ Added in vesion 0.24.0
        """
        ...
    def add_bem(
        self,
        subject,
        title,
        *,
        subjects_dir=None,
        decim: int = 2,
        width: int = 512,
        n_jobs=None,
        tags=("bem",),
        replace: bool = False,
    ) -> None:
        """### Render a visualization of the boundary element model (BEM) surfaces.

        -----
        ### 🛠️ Parameters

        subject : str
            The FreeSurfer subject name.
        title : str
            The title corresponding to the BEM image.

        subjects_dir : path-like | None
            The path to the directory containing the FreeSurfer subjects
            reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
            variable.
        decim : int
            Use this decimation factor for generating MRI/BEM images
            (since it can be time consuming).
        width : int
            The width of the MRI images (in pixels). Larger values will have
            clearer surface lines, but will create larger HTML files.
            Typically a factor of 2 more than the number of MRI voxels along
            each dimension (typically 512, default) is reasonable.
        n_jobs : int | None
            The number of jobs to run in parallel. If ``-1``, it is set
            to the number of CPU cores. Requires the `joblib` package.
            ``None`` (default) is a marker for 'unset' that will be interpreted
            as ``n_jobs=1`` (sequential execution) unless the call is performed under
            a `joblib:joblib.parallel_config` context manager that sets another
            value for ``n_jobs``.

        tags : array-like of str | str
            Tags to add for later interactive filtering. Must not contain spaces.

        replace : bool
            If ``True``, content already present that has the same ``title`` and
            ``section`` will be replaced. Defaults to ``False``, which will cause
            duplicate entries in the table of contents if an entry for ``title``
            already exists.

        -----
        ### 📖 Notes

        ✨ Added in vesion 0.24.0
        """
        ...
    def parse_folder(
        self,
        data_path,
        pattern=None,
        n_jobs=None,
        mri_decim: int = 2,
        sort_content: bool = True,
        *,
        on_error: str = "warn",
        image_format=None,
        render_bem: bool = True,
        n_time_points_evokeds=None,
        n_time_points_stcs=None,
        raw_butterfly: bool = True,
        stc_plot_kwargs=None,
        topomap_kwargs=None,
        verbose=None,
    ) -> None:
        """### Render all the files in the folder.

        -----
        ### 🛠️ Parameters

        data_path : str
            Path to the folder containing data whose HTML report will be
            created.
        pattern : None | str | list of str
            Filename pattern(s) to include in the report.
            For example, ``[\\*raw.fif, \\*ave.fif]`` will include `mne.io.Raw`
            as well as `mne.Evoked` files. If ``None``, include all supported
            file formats.

            🎭 Changed in version 0.23
               Include supported non-FIFF files by default.
        n_jobs : int | None
            The number of jobs to run in parallel. If ``-1``, it is set
            to the number of CPU cores. Requires the `joblib` package.
            ``None`` (default) is a marker for 'unset' that will be interpreted
            as ``n_jobs=1`` (sequential execution) unless the call is performed under
            a `joblib:joblib.parallel_config` context manager that sets another
            value for ``n_jobs``.
        mri_decim : int
            Use this decimation factor for generating MRI/BEM images
            (since it can be time consuming).
        sort_content : bool
            If ``True``, sort the content based on tags in the order:
            raw -> events -> epochs -> evoked -> covariance -> coregistration
            -> bem -> forward-solution -> inverse-operator -> source-estimate.

            ✨ Added in vesion 0.24.0
        on_error : str
            What to do if a file cannot be rendered. Can be 'ignore',
            'warn' (default), or 'raise'.

        image_format : 'png' | 'svg' | 'gif' | None
            The image format to be used for the report, can be ``'png'``,
            ``'svg'``, or ``'gif'``.
            None (default) will use the default specified during `mne.Report`
            instantiation.

            ✨ Added in vesion 0.15
        render_bem : bool
            If True (default), try to render the BEM.

            ✨ Added in vesion 0.16
        n_time_points_evokeds, n_time_points_stcs : int | None
            The number of equidistant time points to render for `mne.Evoked`
            and `mne.SourceEstimate` data, respectively. If ``None``,
            will render each `mne.Evoked` at 21 and each `mne.SourceEstimate`
            at 51 time points, unless the respective data contains fewer time
            points, in which call all will be rendered.

            ✨ Added in vesion 0.24.0
        raw_butterfly : bool
            Whether to render butterfly plots for (decimated) `mne.io.Raw`
            data.

            ✨ Added in vesion 0.24.0

        stc_plot_kwargs : dict
            Dictionary of keyword arguments to pass to
            `mne.SourceEstimate.plot`. Only used when plotting in 3D
            mode.

            ✨ Added in vesion 0.24.0

        topomap_kwargs : dict | None
            Keyword arguments to pass to the topomap-generating functions.

            ✨ Added in vesion 0.24.0

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.
        """
        ...
    def save(
        self,
        fname=None,
        open_browser: bool = True,
        overwrite: bool = False,
        sort_content: bool = False,
        *,
        verbose=None,
    ):
        """### Save the report and optionally open it in browser.

        -----
        ### 🛠️ Parameters

        fname : path-like | None
            Output filename. If the name ends with ``.h5`` or ``.hdf5``, the
            report is saved in HDF5 format, so it can later be loaded again
            with `open_report`. For any other suffix, the report will be
            saved in HTML format. If ``None`` and `Report.parse_folder`
            was **not** called, the report is saved as ``report.html`` in the
            current working directory. If ``None`` and
            `Report.parse_folder` **was** used, the report is saved as
            ``report.html`` inside the ``data_path`` supplied to
            `Report.parse_folder`.
        open_browser : bool
            Whether to open the rendered HTML report in the default web browser
            after saving. This is ignored when writing an HDF5 file.

        overwrite : bool
            If True (default False), overwrite the destination file if it
            exists.
        sort_content : bool
            If ``True``, sort the content based on tags before saving in the
            order:
            raw -> events -> epochs -> evoked -> covariance -> coregistration
            -> bem -> forward-solution -> inverse-operator -> source-estimate.

            ✨ Added in vesion 0.24.0

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the `logging documentation <tut-logging>` and
            `mne.verbose` for details. Should only be passed as a keyword
            argument.

        -----
        ### ⏎ Returns

        fname : str
            The file name to which the report was saved.
        """
        ...
    def __enter__(self):
        """### Do nothing when entering the context block."""
        ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None:
        """### Save the report when leaving the context block."""
        ...

class _ReportScraper:
    """### Scrape Report outputs.

    Only works properly if conf.py is configured properly and the file
    is written to the same directory as the example script.
    """

    app: Incomplete
    files: Incomplete

    def __init__(self) -> None: ...
    def __call__(self, block, block_vars, gallery_conf): ...
    def copyfiles(self, *args, **kwargs) -> None: ...
