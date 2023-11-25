from ._compute_beamformer import (
    Beamformer as Beamformer,
    read_beamformer as read_beamformer,
)
from ._dics import (
    apply_dics as apply_dics,
    apply_dics_csd as apply_dics_csd,
    apply_dics_epochs as apply_dics_epochs,
    apply_dics_tfr_epochs as apply_dics_tfr_epochs,
    make_dics as make_dics,
)
from ._lcmv import (
    apply_lcmv as apply_lcmv,
    apply_lcmv_cov as apply_lcmv_cov,
    apply_lcmv_epochs as apply_lcmv_epochs,
    apply_lcmv_raw as apply_lcmv_raw,
    make_lcmv as make_lcmv,
)
from ._rap_music import rap_music as rap_music, trap_music as trap_music
from .resolution_matrix import (
    make_lcmv_resolution_matrix as make_lcmv_resolution_matrix,
)
