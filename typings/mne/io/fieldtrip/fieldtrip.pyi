from ...epochs import EpochsArray as EpochsArray
from ...evoked import EvokedArray as EvokedArray
from ..array.array import RawArray as RawArray

def read_raw_fieldtrip(fname, info, data_name: str = "data"):
    """Load continuous (raw) data from a FieldTrip preprocessing structure.

    This function expects to find single trial raw data (FT_DATATYPE_RAW) in
    the structure data_name is pointing at.

    .. warning:: FieldTrip does not normally store the original information
                 concerning channel location, orientation, type etc. It is
                 therefore **highly recommended** to provide the info field.
                 This can be obtained by reading the original raw data file
                 with MNE functions (without preload). The returned object
                 contains the necessary info field.

    Parameters
    ----------
    fname : path-like
        Path and filename of the ``.mat`` file containing the data.
    info : dict or None
        The info dict of the raw data file corresponding to the data to import.
        If this is set to None, limited information is extracted from the
        FieldTrip structure.
    data_name : str
        Name of heading dict/variable name under which the data was originally
        saved in MATLAB.

    Returns
    -------
    raw : instance of RawArray
        A Raw Object containing the loaded data.
        See :class:`mne.io.Raw` for documentation of attributes and methods.

    See Also
    --------
    mne.io.Raw : Documentation of attributes and methods of RawArray.
    """

def read_epochs_fieldtrip(
    fname, info, data_name: str = "data", trialinfo_column: int = 0
):
    """Load epoched data from a FieldTrip preprocessing structure.

    This function expects to find epoched data in the structure data_name is
    pointing at.

    .. warning:: Only epochs with the same amount of channels and samples are
                 supported!

    .. warning:: FieldTrip does not normally store the original information
                 concerning channel location, orientation, type etc. It is
                 therefore **highly recommended** to provide the info field.
                 This can be obtained by reading the original raw data file
                 with MNE functions (without preload). The returned object
                 contains the necessary info field.

    Parameters
    ----------
    fname : path-like
        Path and filename of the ``.mat`` file containing the data.
    info : dict or None
        The info dict of the raw data file corresponding to the data to import.
        If this is set to None, limited information is extracted from the
        FieldTrip structure.
    data_name : str
        Name of heading dict/ variable name under which the data was originally
        saved in MATLAB.
    trialinfo_column : int
        Column of the trialinfo matrix to use for the event codes.

    Returns
    -------
    epochs : instance of EpochsArray
        An EpochsArray containing the loaded data.
    """

def read_evoked_fieldtrip(fname, info, comment=None, data_name: str = "data"):
    """Load evoked data from a FieldTrip timelocked structure.

    This function expects to find timelocked data in the structure data_name is
    pointing at.

    .. warning:: FieldTrip does not normally store the original information
                 concerning channel location, orientation, type etc. It is
                 therefore **highly recommended** to provide the info field.
                 This can be obtained by reading the original raw data file
                 with MNE functions (without preload). The returned object
                 contains the necessary info field.

    Parameters
    ----------
    fname : path-like
        Path and filename of the ``.mat`` file containing the data.
    info : dict or None
        The info dict of the raw data file corresponding to the data to import.
        If this is set to None, limited information is extracted from the
        FieldTrip structure.
    comment : str
        Comment on dataset. Can be the condition.
    data_name : str
        Name of heading dict/ variable name under which the data was originally
        saved in MATLAB.

    Returns
    -------
    evoked : instance of EvokedArray
        An EvokedArray containing the loaded data.
    """
