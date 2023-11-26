from ..._fiff.constants import FIFF as FIFF
from ...annotations import (
    Annotations as Annotations,
    read_annotations as read_annotations,
)
from ...channels import make_dig_montage as make_dig_montage
from ...defaults import HEAD_SIZE_DEFAULT as HEAD_SIZE_DEFAULT
from ...utils import (
    _DefaultEventParser,
    fill_doc as fill_doc,
    logger as logger,
    warn as warn,
)
from ..base import BaseRaw as BaseRaw
from _typeshed import Incomplete

class RawBrainVision(BaseRaw):
    """### Raw object from Brain Vision EEG file.

    ### 🛠️ Parameters
    ----------
    vhdr_fname : path-like
        Path to the EEG header file.
    eog : list or tuple
        Names of channels or list of indices that should be designated
        EOG channels. Values should correspond to the header file.
        Default is ``('HEOGL', 'HEOGR', 'VEOGb')``.
    misc : list or tuple of str | ``'auto'``
        Names of channels or list of indices that should be designated
        MISC channels. Values should correspond to the electrodes
        in the header file. If ``'auto'``, units in header file are used for
        inferring misc channels. Default is ``'auto'``.
    scale : float
        The scaling factor for EEG data. Unless specified otherwise by
        header file, units are in microvolts. Default scale factor is 1.

    preload : bool or str (default False)
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### 📊 Attributes
    ----------
    impedances : dict
        A dictionary of all electrodes and their impedances.

    ### 👉 See Also
    --------
    mne.io.Raw : Documentation of attributes and methods.
    """

    impedances: Incomplete

    def __init__(
        self,
        vhdr_fname,
        eog=("HEOGL", "HEOGR", "VEOGb"),
        misc: str = "auto",
        scale: float = 1.0,
        preload: bool = False,
        verbose=None,
    ) -> None: ...

def read_raw_brainvision(
    vhdr_fname,
    eog=("HEOGL", "HEOGR", "VEOGb"),
    misc: str = "auto",
    scale: float = 1.0,
    preload: bool = False,
    verbose=None,
):
    """### Reader for Brain Vision EEG file.

    ### 🛠️ Parameters
    ----------
    vhdr_fname : path-like
        Path to the EEG header file.
    eog : list or tuple of str
        Names of channels or list of indices that should be designated
        EOG channels. Values should correspond to the header file
        Default is ``('HEOGL', 'HEOGR', 'VEOGb')``.
    misc : list or tuple of str | ``'auto'``
        Names of channels or list of indices that should be designated
        MISC channels. Values should correspond to the electrodes in the
        header file. If ``'auto'``, units in header file are used for inferring
        misc channels. Default is ``'auto'``.
    scale : float
        The scaling factor for EEG data. Unless specified otherwise by
        header file, units are in microvolts. Default scale factor is 1.

    preload : bool or str (default False)
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    raw : instance of RawBrainVision
        A Raw object containing BrainVision data.
        See `mne.io.Raw` for documentation of attributes and methods.

    ### 👉 See Also
    --------
    mne.io.Raw : Documentation of attributes and methods of RawBrainVision.
    """
    ...

class _BVEventParser(_DefaultEventParser):
    """### Parse standard brainvision events, accounting for non-standard ones."""

    def __call__(self, description):
        """### Parse BrainVision event codes (like `Stimulus/S 11`) to ints."""
        ...
