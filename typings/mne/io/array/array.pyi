from ...utils import fill_doc as fill_doc, logger as logger
from ..base import BaseRaw as BaseRaw

class RawArray(BaseRaw):
    """Raw object from numpy array.

    Parameters
    ----------
    data : array, shape (n_channels, n_times)
        The channels' time series. See notes for proper units of measure.

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement. Consider using `mne.create_info` to populate
        this structure. This may be modified in place by the class.
    first_samp : int
        First sample offset used during recording (default 0).

        ✨ Added in version 0.12
    copy : {'data', 'info', 'both', 'auto', None}
        Determines what gets copied on instantiation. "auto" (default)
        will copy info, and copy "data" only if necessary to get to
        double floating point precision.

        ✨ Added in version 0.18

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    mne.EpochsArray
    mne.EvokedArray
    mne.create_info

    Notes
    -----
    Proper units of measure:

    * V: eeg, eog, seeg, dbs, emg, ecg, bio, ecog
    * T: mag
    * T/m: grad
    * M: hbo, hbr
    * Am: dipole
    * AU: misc
    """

    def __init__(
        self, data, info, first_samp: int = 0, copy: str = "auto", verbose=None
    ) -> None: ...
