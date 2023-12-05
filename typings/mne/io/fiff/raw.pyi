from ..._fiff.constants import FIFF as FIFF
from ..._fiff.meas_info import read_meas_info as read_meas_info
from ..._fiff.open import fiff_open as fiff_open
from ..._fiff.tag import read_tag as read_tag, read_tag_info as read_tag_info
from ..._fiff.tree import dir_tree_find as dir_tree_find
from ...annotations import Annotations as Annotations
from ...channels import fix_mag_coil_types as fix_mag_coil_types
from ...event import AcqParserFIF as AcqParserFIF
from ...utils import (
    check_fname as check_fname,
    fill_doc as fill_doc,
    logger as logger,
    warn as warn,
)
from ..base import BaseRaw as BaseRaw

class Raw(BaseRaw):
    """Raw data in FIF format.

    Parameters
    ----------
    fname : path-like | file-like
        The raw filename to load. For files that have automatically been split,
        the split part will be automatically loaded. Filenames not ending with
        ``raw.fif``, ``raw_sss.fif``, ``raw_tsss.fif``, ``_meg.fif``,
        ``_eeg.fif``,  or ``_ieeg.fif`` (with or without an optional additional
        ``.gz`` extension) will generate a warning. If a file-like object is
        provided, preloading must be used.

        🎭 Changed in version 0.18
           Support for file-like objects.
    allow_maxshield : bool | str (default False)
        If True, allow loading of data that has been recorded with internal
        active compensation (MaxShield). Data recorded with MaxShield should
        generally not be loaded directly, but should first be processed using
        SSS/tSSS to remove the compensation signals that may also affect brain
        activity. Can also be "yes" to load without eliciting a warning.

    preload : bool or str (default False)
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).

    on_split_missing : str
        Can be ``'raise'`` (default) to raise an error, ``'warn'`` to emit a
        warning, or ``'ignore'`` to ignore when split file is missing.

        ✨ Added in version 0.22

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Attributes
    ----------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    ch_names : list of string
        List of channels' names.
    n_times : int
        Total number of time points in the raw file.
    times :  ndarray
        Time vector in seconds. Starts from 0, independently of `first_samp`
        value. Time interval between consecutive time samples is equal to the
        inverse of the sampling frequency.
    preload : bool
        Indicates whether raw data are in memory.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.
    """

    preload: bool

    def __init__(
        self,
        fname,
        allow_maxshield: bool = False,
        preload: bool = False,
        on_split_missing: str = "raise",
        verbose=None,
    ) -> None: ...
    def fix_mag_coil_types(self):
        """Fix Elekta magnetometer coil types.

        Returns
        -------
        raw : instance of Raw
            The raw object. Operates in place.

        Notes
        -----
        This function changes magnetometer coil types 3022 (T1: SQ20483N) and
        3023 (T2: SQ20483-A) to 3024 (T3: SQ20950N) in the channel definition
        records in the info structure.

        Neuromag Vectorview systems can contain magnetometers with two
        different coil sizes (3022 and 3023 vs. 3024). The systems
        incorporating coils of type 3024 were introduced last and are used at
        the majority of MEG sites. At some sites with 3024 magnetometers,
        the data files have still defined the magnetometers to be of type
        3022 to ensure compatibility with older versions of Neuromag software.
        In the MNE software as well as in the present version of Neuromag
        software coil type 3024 is fully supported. Therefore, it is now safe
        to upgrade the data files to use the true coil type.

        💡 The effect of the difference between the coil sizes on the
                  current estimates computed by the MNE software is very small.
                  Therefore the use of mne_fix_mag_coil_types is not mandatory.
        """
        ...

    @property
    def acqparser(self):
        """The AcqParserFIF for the measurement info.

        See Also
        --------
        mne.AcqParserFIF
        """
        ...

def read_raw_fif(
    fname,
    allow_maxshield: bool = False,
    preload: bool = False,
    on_split_missing: str = "raise",
    verbose=None,
):
    """Reader function for Raw FIF data.

    Parameters
    ----------
    fname : path-like | file-like
        The raw filename to load. For files that have automatically been split,
        the split part will be automatically loaded. Filenames should end
        with raw.fif, raw.fif.gz, raw_sss.fif, raw_sss.fif.gz, raw_tsss.fif,
        raw_tsss.fif.gz, or _meg.fif. If a file-like object is provided,
        preloading must be used.

        🎭 Changed in version 0.18
           Support for file-like objects.
    allow_maxshield : bool | str (default False)
        If True, allow loading of data that has been recorded with internal
        active compensation (MaxShield). Data recorded with MaxShield should
        generally not be loaded directly, but should first be processed using
        SSS/tSSS to remove the compensation signals that may also affect brain
        activity. Can also be "yes" to load without eliciting a warning.

    preload : bool or str (default False)
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).

    on_split_missing : str
        Can be ``'raise'`` (default) to raise an error, ``'warn'`` to emit a
        warning, or ``'ignore'`` to ignore when split file is missing.

        ✨ Added in version 0.22

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    raw : instance of Raw
        A Raw object containing FIF data.

    Notes
    -----
    ✨ Added in version 0.9.0

    When reading a FIF file, note that the first N seconds annotated
    ``BAD_ACQ_SKIP`` are **skipped**. They are removed from ``raw.times`` and
    ``raw.n_times`` parameters but ``raw.first_samp`` and ``raw.first_time``
    are updated accordingly.
    """
    ...
