from . import (
    _fake as _fake,
    brainstorm as brainstorm,
    eegbci as eegbci,
    epilepsy_ecog as epilepsy_ecog,
    erp_core as erp_core,
    eyelink as eyelink,
    fieldtrip_cmc as fieldtrip_cmc,
    fnirs_motor as fnirs_motor,
    hf_sef as hf_sef,
    kiloword as kiloword,
    limo as limo,
    misc as misc,
    mtrf as mtrf,
    multimodal as multimodal,
    opm as opm,
    phantom_4dbti as phantom_4dbti,
    phantom_kernel as phantom_kernel,
    phantom_kit as phantom_kit,
    refmeg_noise as refmeg_noise,
    sample as sample,
    sleep_physionet as sleep_physionet,
    somato as somato,
    spm_face as spm_face,
    ssvep as ssvep,
    testing as testing,
    ucl_opm_auditory as ucl_opm_auditory,
    visual_92_categories as visual_92_categories,
)
from ._fetch import fetch_dataset as fetch_dataset
from ._fsaverage.base import fetch_fsaverage as fetch_fsaverage
from ._infant.base import fetch_infant_template as fetch_infant_template
from ._phantom.base import fetch_phantom as fetch_phantom
from .utils import (
    _download_all_example_data as _download_all_example_data,
    fetch_aparc_sub_parcellation as fetch_aparc_sub_parcellation,
    fetch_hcp_mmp_parcellation as fetch_hcp_mmp_parcellation,
    has_dataset as has_dataset,
)
