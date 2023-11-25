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
    def __init__(self, name, params=...) -> None: ...

class CoregistrationUI(HasTraits):
    """Close interface and cleanup data structure."""

    coreg: Incomplete

    def __init__(
        self,
        info_file,
        *,
        subject=...,
        subjects_dir=...,
        fiducials: str = ...,
        head_resolution=...,
        head_opacity=...,
        hpi_coils=...,
        head_shape_points=...,
        eeg_channels=...,
        meg_channels=...,
        fnirs_channels=...,
        orient_glyphs=...,
        scale_by_distance=...,
        mark_inside=...,
        sensor_opacity=...,
        trans=...,
        size=...,
        bgcolor=...,
        show: bool = ...,
        block: bool = ...,
        fullscreen: bool = ...,
        interaction: str = ...,
        verbose=...,
    ) -> None: ...
    def close(self) -> None:
        """Close interface and cleanup data structure."""
