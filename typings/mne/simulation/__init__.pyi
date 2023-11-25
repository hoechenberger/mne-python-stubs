from . import metrics as metrics
from .evoked import add_noise as add_noise, simulate_evoked as simulate_evoked
from .raw import (
    add_chpi as add_chpi,
    add_ecg as add_ecg,
    add_eog as add_eog,
    simulate_raw as simulate_raw,
)
from .source import (
    SourceSimulator as SourceSimulator,
    select_source_in_label as select_source_in_label,
    simulate_sparse_stc as simulate_sparse_stc,
    simulate_stc as simulate_stc,
)
