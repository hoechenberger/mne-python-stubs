from ..utils import fill_doc as fill_doc
from .constants import FIFF as FIFF

def get_current_comp(info):
    """## Get the current compensation in effect in the data."""
    ...

def set_current_comp(info, comp) -> None:
    """## Set the current compensation in effect in the data."""
    ...

def make_compensator(info, from_, to, exclude_comp_chs: bool = False):
    """## Return compensation matrix eg. for CTF system.

    Create a compensation matrix to bring the data from one compensation
    state to another.

    -----
    ### 🛠️ Parameters


    #### `info : mne.Info`
        The `mne.Info` object with information about the sensors and methods of measurement.
    #### `from_ : int`
        Compensation in the input data.
    #### `to : int`
        Desired compensation in the output.
    #### `exclude_comp_chs : bool`
        Exclude compensation channels from the output.

    -----
    ### ⏎ Returns

    #### `comp : array | None.`
        The compensation matrix. Might be None if no compensation
        is needed (from == to).
    """
    ...
