from ..._fiff._digitization import DigPoint as DigPoint
from ..._fiff.constants import FIFF as FIFF
from ...transforms import (
    Transform as Transform,
    apply_trans as apply_trans,
    get_ras_to_neuromag_trans as get_ras_to_neuromag_trans,
)
from ...utils import logger as logger, warn as warn
from ..base import BaseRaw as BaseRaw

def read_raw_artemis123(
    input_fname,
    preload: bool = False,
    verbose=None,
    pos_fname=None,
    add_head_trans: bool = True,
):
    """## 🧠 Read Artemis123 data as raw object.

    -----
    ### 🛠️ Parameters

    #### `input_fname : path-like`
        Path to the data file (extension ``.bin``). The header file with the
        same file name stem and an extension ``.txt`` is expected to be found
        in the same directory.

    #### `preload : bool or str (default False)`
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.
    #### `pos_fname : path-like | None`
        If not None, load digitized head points from this file.
    #### `add_head_trans : bool (default True)`
        If True attempt to perform initial head localization. Compute initial
        device to head coordinate transform using HPI coils. If no
        HPI coils are in info['dig'] hpi coils are assumed to be in canonical
        order of fiducial points (nas, rpa, lpa).

    -----
    ### ⏎ Returns

    #### `raw : instance of Raw`
        A Raw object containing the data.

    -----
    ### 👉 See Also

    mne.io.Raw : Documentation of attributes and methods.
    """
    ...

class RawArtemis123(BaseRaw):
    """## 🧠 Raw object from Artemis123 file.

    -----
    ### 🛠️ Parameters

    #### `input_fname : path-like`
        Path to the Artemis123 data file (ending in ``'.bin'``).
    %(preload)s
    %(verbose)s

    -----
    ### 👉 See Also

    mne.io.Raw : Documentation of attributes and methods.
    """

    def __init__(
        self,
        input_fname,
        preload: bool = False,
        verbose=None,
        pos_fname=None,
        add_head_trans: bool = True,
    ) -> None: ...
