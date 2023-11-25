from .._fiff.constants import FIFF as FIFF
from .._fiff.meas_info import (
    read_fiducials as read_fiducials,
    read_info as read_info,
    write_fiducials as write_fiducials,
)
from .._fiff.open import dir_tree_find as dir_tree_find, fiff_open as fiff_open
from .._fiff.pick import pick_types as pick_types
from ..bem import (
    make_bem_solution as make_bem_solution,
    write_bem_solution as write_bem_solution,
)
from ..channels import read_dig_fif as read_dig_fif
from ..coreg import (
    Coregistration as Coregistration,
    bem_fname as bem_fname,
    fid_fname as fid_fname,
    scale_mri as scale_mri,
)
from ..defaults import DEFAULTS as DEFAULTS
from ..io._read_raw import read_raw as read_raw
from ..transforms import (
    read_trans as read_trans,
    rotation_angles as rotation_angles,
    write_trans as write_trans,
)
from ..utils import (
    check_fname as check_fname,
    fill_doc as fill_doc,
    get_subjects_dir as get_subjects_dir,
    logger as logger,
)
from ..viz.utils import safe_event as safe_event
from _typeshed import Incomplete
from traitlets import HasTraits

class _WorkerData:
    def __init__(self, name, params=None) -> None: ...

class CoregistrationUI(HasTraits):
    """Class for coregistration assisted by graphical interface.

    Parameters
    ----------
    info_file : None | str
        The FIFF file with digitizer data for coregistration.

    subject : str
        The FreeSurfer subject name.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.

    fiducials : list | dict | str
        The fiducials given in the MRI (surface RAS) coordinate
        system. If a dictionary is provided, it must contain the **keys**
        ``'lpa'``, ``'rpa'``, and ``'nasion'``, with **values** being the
        respective coordinates in meters.
        If a list, it must be a list of ``DigPoint`` instances as returned by the
        :func:`mne.io.read_fiducials` function.
        If ``'estimated'``, the fiducials are derived from the ``fsaverage``
        template. If ``'auto'`` (default), tries to find the fiducials
        in a file with the canonical name
        (``{subjects_dir}/{subject}/bem/{subject}-fiducials.fif``)
        and if absent, falls back to ``'estimated'``.
    head_resolution : bool
        If True, use a high-resolution head surface. Defaults to False.
    head_opacity : float
        The opacity of the head surface. Defaults to 0.8.
    hpi_coils : bool
        If True, display the HPI coils. Defaults to True.
    head_shape_points : bool
        If True, display the head shape points. Defaults to True.
    eeg_channels : bool
        If True, display the EEG channels. Defaults to True.
    meg_channels : bool
        If True, display the MEG channels. Defaults to False.
    fnirs_channels : bool
        If True, display the fNIRS channels. Defaults to True.
    orient_glyphs : bool
        If True, orient the sensors towards the head surface. Default to False.
    scale_by_distance : bool
        If True, scale the sensors based on their distance to the head surface.
        Defaults to True.
    mark_inside : bool
        If True, mark the head shape points that are inside the head surface
        with a different color. Defaults to True.
    sensor_opacity : float
        The opacity of the sensors between 0 and 1. Defaults to 1.0.
    trans : path-like
        The path to the Head<->MRI transform FIF file ("-trans.fif").
    size : tuple
        The dimensions (width, height) of the rendering view. The default is
        (800, 600).
    bgcolor : tuple | str
        The background color as a tuple (red, green, blue) of float
        values between 0 and 1 or a valid color name (i.e. 'white'
        or 'w'). Defaults to 'grey'.
    show : bool
        Display the window as soon as it is ready. Defaults to True.
    block : bool
        Whether to halt program execution until the GUI has been closed
        (``True``) or not (``False``, default).

    fullscreen : bool
        Whether to start in fullscreen (``True``) or windowed mode
        (``False``).
        The default is False.

        .. versionadded:: 1.1

    interaction : 'trackball' | 'terrain'
        How interactions with the scene via an input device (e.g., mouse or
        trackpad) modify the camera position. If ``'terrain'``, one axis is
        fixed, enabling "turntable-style" rotations. If ``'trackball'``,
        movement along all axes is possible, which provides more freedom of
        movement, but you may incidentally perform unintentional rotations along
        some axes.
        Defaults to ``'terrain'``.

        .. versionadded:: 1.0

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Attributes
    ----------
    coreg : mne.coreg.Coregistration
        The coregistration instance used by the graphical interface.
    """

    coreg: Incomplete

    def __init__(
        self,
        info_file,
        *,
        subject=None,
        subjects_dir=None,
        fiducials: str = "auto",
        head_resolution=None,
        head_opacity=None,
        hpi_coils=None,
        head_shape_points=None,
        eeg_channels=None,
        meg_channels=None,
        fnirs_channels=None,
        orient_glyphs=None,
        scale_by_distance=None,
        mark_inside=None,
        sensor_opacity=None,
        trans=None,
        size=None,
        bgcolor=None,
        show: bool = True,
        block: bool = False,
        fullscreen: bool = False,
        interaction: str = "terrain",
        verbose=None,
    ) -> None: ...
    def close(self) -> None:
        """Close interface and cleanup data structure."""
        ...
