from ..._fiff.constants import FIFF as FIFF
from ...utils import logger as logger, warn as warn
from ..base import BaseRaw as BaseRaw
from _typeshed import Incomplete

def read_raw_egi(
    input_fname,
    eog=None,
    misc=None,
    include=None,
    exclude=None,
    preload: bool = False,
    channel_naming: str = "E%d",
    verbose=None,
):
    """## Read EGI simple binary as raw object.

    ### 💡 Note This function attempts to create a synthetic trigger channel.
              See the Notes section below.

    -----
    ### 🛠️ Parameters

    #### `input_fname : path-like`
        Path to the raw file. Files with an extension ``.mff`` are
        automatically considered to be EGI's native MFF format files.
    #### `eog : list or tuple`
        Names of channels or list of indices that should be designated
        EOG channels. Default is None.
    #### `misc : list or tuple`
        Names of channels or list of indices that should be designated
        MISC channels. Default is None.
    #### `include : None | list`
       The event channels to be ignored when creating the synthetic
       trigger. Defaults to None.
       Note. Overrides ``exclude`` parameter.
    #### `exclude : None | list`
       The event channels to be ignored when creating the synthetic
       trigger. Defaults to None. If None, channels that have more than
       one event and the ``sync`` and ``TREV`` channels will be
       ignored.

    #### `preload : bool or str (default False)`
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).

        ✨ Added in version 0.11
    #### `channel_naming : str`
        Channel naming convention for the data channels. Defaults to ``'E%d'``
        (resulting in channel names ``'E1'``, ``'E2'``, ``'E3'``...). The
        effective default prior to 0.14.0 was ``'EEG %03d'``.

         ✨ Added in version 0.14.0

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `raw : instance of RawEGI`
        A Raw object containing EGI data.
        See `mne.io.Raw` for documentation of attributes and methods.

    -----
    ### 👉 See Also

    mne.io.Raw : Documentation of attributes and methods of RawEGI.

    -----
    ### 📖 Notes

    The trigger channel names are based on the arbitrary user dependent event
    codes used. However this function will attempt to generate a **synthetic
    trigger channel** named ``STI 014`` in accordance with the general
    Neuromag / MNE naming pattern.

    The event_id assignment equals ``np.arange(n_events) + 1``. The resulting
    ``event_id`` mapping is stored as attribute to the resulting raw object but
    will be ignored when saving to a fiff. Note. The trigger channel is
    artificially constructed based on timestamps received by the Netstation.
    As a consequence, triggers have only short durations.

    This step will fail if events are not mutually exclusive.
    """
    ...

class RawEGI(BaseRaw):
    """## Raw object from EGI simple binary file."""

    event_id: Incomplete

    def __init__(
        self,
        input_fname,
        eog=None,
        misc=None,
        include=None,
        exclude=None,
        preload: bool = False,
        channel_naming: str = "E%d",
        verbose=None,
    ) -> None: ...
