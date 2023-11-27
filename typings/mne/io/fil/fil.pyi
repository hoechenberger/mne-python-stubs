from ..._fiff.constants import FIFF as FIFF
from ..._fiff.write import get_new_file_id as get_new_file_id
from ...transforms import (
    Transform as Transform,
    apply_trans as apply_trans,
    get_ras_to_neuromag_trans as get_ras_to_neuromag_trans,
)
from ...utils import fill_doc as fill_doc, warn as warn
from ..base import BaseRaw as BaseRaw

def read_raw_fil(
    binfile, precision: str = "single", preload: bool = False, *, verbose=None
):
    """## Raw object from FIL-OPMEG formatted data.

    -----
    ### 🛠️ Parameters

    #### `binfile : path-like`
        Path to the MEG data binary (ending in ``'_meg.bin'``).
    #### `precision : str, optional`
        How is the data represented? ``'single'`` if 32-bit or ``'double'`` if
        64-bit (default is single).

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

    -----
    ### ⏎ Returns

    #### `raw : instance of RawFIL`
        The raw data.
        See `mne.io.Raw` for documentation of attributes and methods.

    -----
    ### 👉 See Also

    mne.io.Raw : Documentation of attributes and methods of RawFIL.
    """
    ...

class RawFIL(BaseRaw):
    """## Raw object from FIL-OPMEG formatted data.

    -----
    ### 🛠️ Parameters

    #### `binfile : path-like`
        Path to the MEG data binary (ending in ``'_meg.bin'``).
    #### `precision : str, optional`
        How is the data represented? ``'single'`` if 32-bit or
        ``'double'`` if 64-bit (default is single).

    #### `preload : bool or str (default False)`
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).

    -----
    ### ⏎ Returns

    #### `raw : instance of RawFIL`
        The raw data.
        See `mne.io.Raw` for documentation of attributes and methods.

    -----
    ### 👉 See Also

    mne.io.Raw : Documentation of attributes and methods of RawFIL.
    """

    def __init__(
        self, binfile, precision: str = "single", preload: bool = False
    ) -> None: ...
