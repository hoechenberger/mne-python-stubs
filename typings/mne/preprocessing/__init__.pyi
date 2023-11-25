from . import eyetracking as eyetracking, ieeg as ieeg, nirs as nirs
from ._annotate_amplitude import annotate_amplitude as annotate_amplitude
from ._annotate_nan import annotate_nan as annotate_nan
from ._csd import (
    compute_bridged_electrodes as compute_bridged_electrodes,
    compute_current_source_density as compute_current_source_density,
)
from ._css import cortical_signal_suppression as cortical_signal_suppression
from ._fine_cal import (
    compute_fine_calibration as compute_fine_calibration,
    read_fine_calibration as read_fine_calibration,
    write_fine_calibration as write_fine_calibration,
)
from ._peak_finder import peak_finder as peak_finder
from ._regress import (
    EOGRegression as EOGRegression,
    read_eog_regression as read_eog_regression,
    regress_artifact as regress_artifact,
)
from .artifact_detection import (
    annotate_break as annotate_break,
    annotate_movement as annotate_movement,
    annotate_muscle_zscore as annotate_muscle_zscore,
    compute_average_dev_head_t as compute_average_dev_head_t,
)
from .ecg import (
    create_ecg_epochs as create_ecg_epochs,
    find_ecg_events as find_ecg_events,
)
from .eog import (
    create_eog_epochs as create_eog_epochs,
    find_eog_events as find_eog_events,
)
from .hfc import compute_proj_hfc as compute_proj_hfc
from .ica import (
    ICA as ICA,
    corrmap as corrmap,
    get_score_funcs as get_score_funcs,
    ica_find_ecg_events as ica_find_ecg_events,
    ica_find_eog_events as ica_find_eog_events,
    read_ica as read_ica,
    read_ica_eeglab as read_ica_eeglab,
)
from .infomax_ import infomax as infomax
from .interpolate import (
    equalize_bads as equalize_bads,
    interpolate_bridged_electrodes as interpolate_bridged_electrodes,
)
from .maxfilter import apply_maxfilter as apply_maxfilter
from .maxwell import (
    compute_maxwell_basis as compute_maxwell_basis,
    find_bad_channels_maxwell as find_bad_channels_maxwell,
    maxwell_filter as maxwell_filter,
    maxwell_filter_prepare_emptyroom as maxwell_filter_prepare_emptyroom,
)
from .otp import oversampled_temporal_projection as oversampled_temporal_projection
from .realign import realign_raw as realign_raw
from .ssp import (
    compute_proj_ecg as compute_proj_ecg,
    compute_proj_eog as compute_proj_eog,
)
from .stim import fix_stim_artifact as fix_stim_artifact
from .xdawn import Xdawn as Xdawn
