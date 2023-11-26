from ..._fiff.constants import FIFF as FIFF
from ..._fiff.pick import pick_types as pick_types
from ...epochs import BaseEpochs as BaseEpochs
from ...event import read_events as read_events
from ...transforms import als_ras_trans as als_ras_trans, apply_trans as apply_trans
from ...utils import fill_doc as fill_doc, logger as logger, warn as warn
from ..base import BaseRaw as BaseRaw
from .constants import KIT as KIT, LEGACY_AMP_PARAMS as LEGACY_AMP_PARAMS
from .coreg import read_mrk as read_mrk
from _typeshed import Incomplete

FLOAT64: str
UINT32: str
INT32: str

class UnsupportedKITFormat(ValueError):
    """### Our reader is not guaranteed to work with old files."""

    sqd_version: Incomplete

    def __init__(self, sqd_version, *args, **kwargs) -> None: ...

class RawKIT(BaseRaw):
    """### Raw object from KIT SQD file.

    ### 🛠️ Parameters
    ----------
    input_fname : path-like
        Path to the SQD file.

    mrk : path-like | array of shape (5, 3) | list | None
        Marker points representing the location of the marker coils with
        respect to the MEG sensors, or path to a marker file.
        If list, all of the markers will be averaged together.

    elp : path-like | array of shape (8, 3) | None
        Digitizer points representing the location of the fiducials and the
        marker coils with respect to the digitized head shape, or path to a
        file containing these points.

    hsp : path-like | array of shape (n_points, 3) | None
        Digitizer head shape points, or path to head shape file. If more than
        10,000 points are in the head shape, they are automatically decimated.

    stim : list of int | ``'<'`` | ``'>'`` | None
        Channel-value correspondence when converting KIT trigger channels to a
        Neuromag-style stim channel. For ``'<'``\\, the largest values are
        assigned to the first channel (default). For ``'>'``\\, the largest
        values are assigned to the last channel. Can also be specified as a
        list of trigger channel indexes. If None, no synthesized channel is
        generated.

    slope : ``'+'`` | ``'-'``
        How to interpret values on KIT trigger channels when synthesizing a
        Neuromag-style stim channel. With ``'+'``\\, a positive slope (low-to-high)
        is interpreted as an event. With ``'-'``\\, a negative slope (high-to-low)
        is interpreted as an event.

    stimthresh : float | None
        The threshold level for accepting voltage changes in KIT trigger
        channels as a trigger event. If None, stim must also be set to None.

    preload : bool or str (default False)
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).

    stim_code : ``'binary'`` | ``'channel'``
        How to decode trigger values from stim channels. ``'binary'`` read stim
        channel events as binary code, 'channel' encodes channel number.
    allow_unknown_format : bool
        Force reading old data that is not officially supported. Alternatively,
        read and re-save the data with the KIT MEG Laboratory application.

    standardize_names : bool
        If True, standardize MEG and EEG channel names to be
        ``'MEG ###'`` and ``'EEG ###'``. If False (default), native
        channel names in the file will be used when possible.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### 📖 Notes
    -----
    ``elp`` and ``hsp`` are usually the exported text files (*.txt) from the
    Polhemus FastScan system. ``hsp`` refers to the headshape surface points.
    ``elp`` refers to the points in head-space that corresponds to the HPI
    points.

    If ``mrk``\\, ``hsp`` or ``elp`` are :term:`array_like` inputs, then the
    numbers in xyz coordinates should be in units of meters.

    See Also
    --------
    mne.io.Raw : Documentation of attributes and methods.
    """

    preload: bool
    info: Incomplete

    def __init__(
        self,
        input_fname,
        mrk=None,
        elp=None,
        hsp=None,
        stim: str = ">",
        slope: str = "-",
        stimthresh: int = 1,
        preload: bool = False,
        stim_code: str = "binary",
        allow_unknown_format: bool = False,
        standardize_names=None,
        verbose=None,
    ) -> None: ...
    def read_stim_ch(self, buffer_size: float = 100000.0):
        """### Read events from data.

        Parameter
        ---------
        buffer_size : int
            The size of chunk to by which the data are scanned.

        ### ⏎ Returns
        -------
        events : array, [samples]
           The event vector (1 x samples).
        """
        ...

class EpochsKIT(BaseEpochs):
    """### Epochs Array object from KIT SQD file.

    ### 🛠️ Parameters
    ----------
    input_fname : path-like
        Path to the sqd file.
    events : array of int, shape (n_events, 3) | path-like
        The array of :term:`events`. The first column contains the event time
        in samples, with :term:`first_samp` included. The third column contains
        the event id. If a path, must yield a ``.txt`` file containing the
        events.
        If some events don't match the events of interest as specified by
        ``event_id``, they will be marked as ``IGNORED`` in the drop log.

    event_id : int | list of int | dict | None
        The id of the :term:`events` to consider. If dict, the keys can later be
        used to access associated :term:`events`. Example:
        dict(auditory=1, visual=3). If int, a dict will be created with the id as
        string. If a list, all :term:`events` with the IDs specified in the list
        are used. If None, all :term:`events` will be used and a dict is created
        with string integer names corresponding to the event id integers.
    tmin : float
        Start time before event.

    baseline : None | tuple of length 2
        The time interval to consider as "baseline" when applying baseline
        correction. If ``None``, do not apply baseline correction.
        If a tuple ``(a, b)``, the interval is between ``a`` and ``b``
        (in seconds), including the endpoints.
        If ``a`` is ``None``, the **beginning** of the data is used; and if ``b``
        is ``None``, it is set to the **end** of the interval.
        If ``(None, None)``, the entire time interval is used.

        ### 💡 Note The baseline ``(a, b)`` includes both endpoints, i.e. all
                    timepoints ``t`` such that ``a <= t <= b``.

        Correction is applied **to each epoch and channel individually** in the
        following way:

        1. Calculate the mean signal of the baseline period.
        2. Subtract this mean from the **entire** epoch.


    reject : dict | None
        Reject epochs based on **maximum** peak-to-peak signal amplitude (PTP),
        i.e. the absolute difference between the lowest and the highest signal
        value. In each individual epoch, the PTP is calculated for every channel.
        If the PTP of any one channel exceeds the rejection threshold, the
        respective epoch will be dropped.

        The dictionary keys correspond to the different channel types; valid
        **keys** can be any channel type present in the object.

        Example::

            reject = dict(grad=4000e-13,  # unit: T / m (gradiometers)
                          mag=4e-12,      # unit: T (magnetometers)
                          eeg=40e-6,      # unit: V (EEG channels)
                          eog=250e-6      # unit: V (EOG channels)
                          )

        ### 💡 Note Since rejection is based on a signal **difference**
                  calculated for each channel separately, applying baseline
                  correction does not affect the rejection procedure, as the
                  difference will be preserved.

        ### 💡 Note To constrain the time period used for estimation of signal
                  quality, pass the ``reject_tmin`` and ``reject_tmax`` parameters.

        If ``reject`` is ``None`` (default), no rejection is performed.

    flat : dict | None
        Reject epochs based on **minimum** peak-to-peak signal amplitude (PTP).
        Valid **keys** can be any channel type present in the object. The
        **values** are floats that set the minimum acceptable PTP. If the PTP
        is smaller than this threshold, the epoch will be dropped. If ``None``
        then no rejection is performed based on flatness of the signal.

        ### 💡 Note To constrain the time period used for estimation of signal
                  quality, pass the ``reject_tmin`` and ``reject_tmax`` parameters.

    reject_tmin, reject_tmax : float | None
        Start and end of the time window used to reject epochs based on
        peak-to-peak (PTP) amplitudes as specified via ``reject`` and ``flat``.
        The default ``None`` corresponds to the first and last time points of the
        epochs, respectively.

        ### 💡 Note This parameter controls the time period used in conjunction with
                  both, ``reject`` and ``flat``.

    mrk : path-like | array of shape (5, 3) | list | None
        Marker points representing the location of the marker coils with
        respect to the MEG sensors, or path to a marker file.
        If list, all of the markers will be averaged together.

    elp : path-like | array of shape (8, 3) | None
        Digitizer points representing the location of the fiducials and the
        marker coils with respect to the digitized head shape, or path to a
        file containing these points.

    hsp : path-like | array of shape (n_points, 3) | None
        Digitizer head shape points, or path to head shape file. If more than
        10,000 points are in the head shape, they are automatically decimated.
    allow_unknown_format : bool
        Force reading old data that is not officially supported. Alternatively,
        read and re-save the data with the KIT MEG Laboratory application.

    standardize_names : bool
        If True, standardize MEG and EEG channel names to be
        ``'MEG ###'`` and ``'EEG ###'``. If False (default), native
        channel names in the file will be used when possible.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### 📖 Notes
    -----
    ``elp`` and ``hsp`` are usually the exported text files (*.txt) from the
    Polhemus FastScan system. hsp refers to the headshape surface points. elp
    refers to the points in head-space that corresponds to the HPI points.
    Currently, '*.elp' and '*.hsp' files are NOT supported.

    See Also
    --------
    mne.Epochs : Documentation of attributes and methods.
    """

    info: Incomplete

    def __init__(
        self,
        input_fname,
        events,
        event_id=None,
        tmin: int = 0,
        baseline=None,
        reject=None,
        flat=None,
        reject_tmin=None,
        reject_tmax=None,
        mrk=None,
        elp=None,
        hsp=None,
        allow_unknown_format: bool = False,
        standardize_names=None,
        verbose=None,
    ) -> None: ...

def get_kit_info(rawfile, allow_unknown_format, standardize_names=None, verbose=None):
    """### Extract all the information from the sqd/con file.

    ### 🛠️ Parameters
    ----------
    rawfile : path-like
        KIT file to be read.
    allow_unknown_format : bool
        Force reading old data that is not officially supported. Alternatively,
        read and re-save the data with the KIT MEG Laboratory application.

    standardize_names : bool
        If True, standardize MEG and EEG channel names to be
        ``'MEG ###'`` and ``'EEG ###'``. If False (default), native
        channel names in the file will be used when possible.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement.
    sqd : dict
        A dict containing all the sqd parameter settings.
    """
    ...

def read_raw_kit(
    input_fname,
    mrk=None,
    elp=None,
    hsp=None,
    stim: str = ">",
    slope: str = "-",
    stimthresh: int = 1,
    preload: bool = False,
    stim_code: str = "binary",
    allow_unknown_format: bool = False,
    standardize_names: bool = False,
    verbose=None,
):
    """### Reader function for Ricoh/KIT conversion to FIF.

    ### 🛠️ Parameters
    ----------
    input_fname : path-like
        Path to the SQD file.

    mrk : path-like | array of shape (5, 3) | list | None
        Marker points representing the location of the marker coils with
        respect to the MEG sensors, or path to a marker file.
        If list, all of the markers will be averaged together.

    elp : path-like | array of shape (8, 3) | None
        Digitizer points representing the location of the fiducials and the
        marker coils with respect to the digitized head shape, or path to a
        file containing these points.

    hsp : path-like | array of shape (n_points, 3) | None
        Digitizer head shape points, or path to head shape file. If more than
        10,000 points are in the head shape, they are automatically decimated.

    stim : list of int | ``'<'`` | ``'>'`` | None
        Channel-value correspondence when converting KIT trigger channels to a
        Neuromag-style stim channel. For ``'<'``\\, the largest values are
        assigned to the first channel (default). For ``'>'``\\, the largest
        values are assigned to the last channel. Can also be specified as a
        list of trigger channel indexes. If None, no synthesized channel is
        generated.

    slope : ``'+'`` | ``'-'``
        How to interpret values on KIT trigger channels when synthesizing a
        Neuromag-style stim channel. With ``'+'``\\, a positive slope (low-to-high)
        is interpreted as an event. With ``'-'``\\, a negative slope (high-to-low)
        is interpreted as an event.

    stimthresh : float | None
        The threshold level for accepting voltage changes in KIT trigger
        channels as a trigger event. If None, stim must also be set to None.

    preload : bool or str (default False)
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).

    stim_code : ``'binary'`` | ``'channel'``
        How to decode trigger values from stim channels. ``'binary'`` read stim
        channel events as binary code, 'channel' encodes channel number.
    allow_unknown_format : bool
        Force reading old data that is not officially supported. Alternatively,
        read and re-save the data with the KIT MEG Laboratory application.

    standardize_names : bool
        If True, standardize MEG and EEG channel names to be
        ``'MEG ###'`` and ``'EEG ###'``. If False (default), native
        channel names in the file will be used when possible.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    raw : instance of RawKIT
        A Raw object containing KIT data.
        See `mne.io.Raw` for documentation of attributes and methods.

    See Also
    --------
    mne.io.Raw : Documentation of attributes and methods of RawKIT.

    ### 📖 Notes
    -----
    ``elp`` and ``hsp`` are usually the exported text files (\\*.txt) from the
    Polhemus FastScan system. ``hsp`` refers to the headshape surface points.
    ``elp`` refers to the points in head-space that corresponds to the HPI
    points.

    If ``mrk``\\, ``hsp`` or ``elp`` are :term:`array_like` inputs, then the
    numbers in xyz coordinates should be in units of meters.
    """
    ...

def read_epochs_kit(
    input_fname,
    events,
    event_id=None,
    mrk=None,
    elp=None,
    hsp=None,
    allow_unknown_format: bool = False,
    standardize_names: bool = False,
    verbose=None,
):
    """### Reader function for Ricoh/KIT epochs files.

    ### 🛠️ Parameters
    ----------
    input_fname : path-like
        Path to the SQD file.
    events : array of int, shape (n_events, 3) | path-like
        The array of :term:`events`. The first column contains the event time
        in samples, with :term:`first_samp` included. The third column contains
        the event id. If a path, must yield a ``.txt`` file containing the
        events.
        If some events don't match the events of interest as specified by
        ``event_id``, they will be marked as ``IGNORED`` in the drop log.

    event_id : int | list of int | dict | None
        The id of the :term:`events` to consider. If dict, the keys can later be
        used to access associated :term:`events`. Example:
        dict(auditory=1, visual=3). If int, a dict will be created with the id as
        string. If a list, all :term:`events` with the IDs specified in the list
        are used. If None, all :term:`events` will be used and a dict is created
        with string integer names corresponding to the event id integers.

    mrk : path-like | array of shape (5, 3) | list | None
        Marker points representing the location of the marker coils with
        respect to the MEG sensors, or path to a marker file.
        If list, all of the markers will be averaged together.

    elp : path-like | array of shape (8, 3) | None
        Digitizer points representing the location of the fiducials and the
        marker coils with respect to the digitized head shape, or path to a
        file containing these points.

    hsp : path-like | array of shape (n_points, 3) | None
        Digitizer head shape points, or path to head shape file. If more than
        10,000 points are in the head shape, they are automatically decimated.
    allow_unknown_format : bool
        Force reading old data that is not officially supported. Alternatively,
        read and re-save the data with the KIT MEG Laboratory application.

    standardize_names : bool
        If True, standardize MEG and EEG channel names to be
        ``'MEG ###'`` and ``'EEG ###'``. If False (default), native
        channel names in the file will be used when possible.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    epochs : instance of Epochs
        The epochs.

    ### 📖 Notes
    -----
    ✨ Added in vesion 0.9.0
    """
    ...
