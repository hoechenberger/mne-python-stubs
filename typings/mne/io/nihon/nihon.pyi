from ..._fiff.meas_info import create_info as create_info
from ...annotations import Annotations as Annotations
from ...utils import fill_doc as fill_doc, logger as logger, warn as warn
from ..base import BaseRaw as BaseRaw

def read_raw_nihon(fname, preload: bool = False, verbose=None):
    """## 🧠 Reader for an Nihon Kohden EEG file.

    -----
    ### 🛠️ Parameters

    #### `fname : path-like`
        Path to the Nihon Kohden data file (``.EEG``).
    #### `preload : bool`
        If True, all data are loaded at initialization.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `raw : instance of RawNihon`
        A Raw object containing Nihon Kohden data.
        See `mne.io.Raw` for documentation of attributes and methods.

    -----
    ### 👉 See Also

    mne.io.Raw : Documentation of attributes and methods of RawNihon.
    """
    ...

class RawNihon(BaseRaw):
    """## 🧠 Raw object from a Nihon Kohden EEG file.

    -----
    ### 🛠️ Parameters

    #### `fname : path-like`
        Path to the Nihon Kohden data ``.eeg`` file.
    #### `preload : bool`
        If True, all data are loaded at initialization.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### 👉 See Also

    mne.io.Raw : Documentation of attributes and methods.
    """

    def __init__(self, fname, preload: bool = False, verbose=None) -> None: ...
