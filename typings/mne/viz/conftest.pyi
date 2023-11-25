from _typeshed import Incomplete
from mne import (
    Epochs as Epochs,
    EvokedArray as EvokedArray,
    create_info as create_info,
    events_from_annotations as events_from_annotations,
)
from mne.channels import make_standard_montage as make_standard_montage
from mne.datasets.testing import data_path as data_path
from mne.io import read_raw_nirx as read_raw_nirx
from mne.preprocessing.nirs import (
    beer_lambert_law as beer_lambert_law,
    optical_density as optical_density,
)

fname_nirx: Incomplete

def fnirs_evoked():
    """Create an fnirs evoked structure."""

def fnirs_epochs():
    """Create an fnirs epoch structure."""
