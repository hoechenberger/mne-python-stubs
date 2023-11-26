from ..._fiff.constants import FIFF as FIFF
from ..._fiff.utils import read_str as read_str
from ...annotations import Annotations as Annotations
from ...utils import fill_doc as fill_doc, warn as warn
from ..base import BaseRaw as BaseRaw
from ._utils import CNTEventType3 as CNTEventType3

def read_raw_cnt(
    input_fname,
    eog=(),
    misc=(),
    ecg=(),
    emg=(),
    data_format: str = "auto",
    date_format: str = "mm/dd/yy",
    *,
    header: str = "auto",
    preload: bool = False,
    verbose=None,
):
    """Read CNT data as raw object.

    .. Note::
        2d spatial coordinates (x, y) for EEG channels are read from the file
        header and fit to a sphere to compute corresponding z-coordinates.
        If channels assigned as EEG channels have locations
        far away from the head (i.e. x and y coordinates don't fit to a
        sphere), all the channel locations will be distorted
        (all channels that are not assigned with keywords ``eog``, ``ecg``,
        ``emg`` and ``misc`` are assigned as EEG channels). If you are not
        sure that the channel locations in the header are correct, it is
        probably safer to replace them with :meth:`mne.io.Raw.set_montage`.
        Montages can be created/imported with:

        - Standard montages with :func:`mne.channels.make_standard_montage`
        - Montages for `Compumedics systems
          <https://compumedicsneuroscan.com>`__ with
          :func:`mne.channels.read_dig_dat`
        - Other reader functions are listed under *See Also* at
          :class:`mne.channels.DigMontage`

    Parameters
    ----------
    input_fname : path-like
        Path to the data file.
    eog : list | tuple | ``'auto'`` | ``'header'``
        Names of channels or list of indices that should be designated
        EOG channels. If 'header', VEOG and HEOG channels assigned in the file
        header are used. If ``'auto'``, channel names containing ``'EOG'`` are
        used. Defaults to empty tuple.
    misc : list | tuple
        Names of channels or list of indices that should be designated
        MISC channels. Defaults to empty tuple.
    ecg : list | tuple | ``'auto'``
        Names of channels or list of indices that should be designated
        ECG channels. If ``'auto'``, the channel names containing ``'ECG'`` are
        used. Defaults to empty tuple.
    emg : list | tuple
        Names of channels or list of indices that should be designated
        EMG channels. If 'auto', the channel names containing 'EMG' are used.
        Defaults to empty tuple.
    data_format : ``'auto'`` | ``'int16'`` | ``'int32'``
        Defines the data format the data is read in. If ``'auto'``, it is
        determined from the file header using ``numsamples`` field.
        Defaults to ``'auto'``.
    date_format : ``'mm/dd/yy'`` | ``'dd/mm/yy'``
        Format of date in the header. Defaults to ``'mm/dd/yy'``.
    header : ``'auto'`` | ``'new'`` | ``'old'``
        Defines the header format. Used to describe how bad channels
        are formatted. If auto, reads using old and new header and
        if either contain a bad channel make channel bad.
        Defaults to ``'auto'``.

        .. versionadded:: 1.6

    preload : bool or str (default False)
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    raw : instance of RawCNT.
        The raw data.
        See :class:`mne.io.Raw` for documentation of attributes and methods.

    See Also
    --------
    mne.io.Raw : Documentation of attributes and methods of RawCNT.

    Notes
    -----
    .. versionadded:: 0.12
    """
    ...

class RawCNT(BaseRaw):
    """Raw object from Neuroscan CNT file.

    .. Note::
        The channel positions are read from the file header. Channels that are
        not assigned with keywords ``eog``, ``ecg``, ``emg`` and ``misc`` are
        assigned as eeg channels. All the eeg channel locations are fit to a
        sphere when computing the z-coordinates for the channels. If channels
        assigned as eeg channels have locations far away from the head (i.e.
        x and y coordinates don't fit to a sphere), all the channel locations
        will be distorted. If you are not sure that the channel locations in
        the header are correct, it is probably safer to use a (standard)
        montage. See :func:`mne.channels.make_standard_montage`

    Parameters
    ----------
    input_fname : path-like
        Path to the CNT file.
    eog : list | tuple
        Names of channels or list of indices that should be designated
        EOG channels. If ``'auto'``, the channel names beginning with
        ``EOG`` are used. Defaults to empty tuple.
    misc : list | tuple
        Names of channels or list of indices that should be designated
        MISC channels. Defaults to empty tuple.
    ecg : list | tuple
        Names of channels or list of indices that should be designated
        ECG channels. If ``'auto'``, the channel names beginning with
        ``ECG`` are used. Defaults to empty tuple.
    emg : list | tuple
        Names of channels or list of indices that should be designated
        EMG channels. If ``'auto'``, the channel names beginning with
        ``EMG`` are used. Defaults to empty tuple.
    data_format : ``'auto'`` | ``'int16'`` | ``'int32'``
        Defines the data format the data is read in. If ``'auto'``, it is
        determined from the file header using ``numsamples`` field.
        Defaults to ``'auto'``.
    date_format : ``'mm/dd/yy'`` | ``'dd/mm/yy'``
        Format of date in the header. Defaults to ``'mm/dd/yy'``.
    header : ``'auto'`` | ``'new'`` | ``'old'``
        Defines the header format. Used to describe how bad channels
        are formatted. If auto, reads using old and new header and
        if either contain a bad channel make channel bad.
        Defaults to ``'auto'``.

    preload : bool or str (default False)
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).
    stim_channel : bool | None
        Add a stim channel from the events. Defaults to None to trigger a
        future warning.

        .. warning:: This defaults to True in 0.18 but will change to False in
                     0.19 (when no stim channel synthesis will be allowed)
                     and be removed in 0.20; migrate code to use
                     :func:`mne.events_from_annotations` instead.

        .. versionadded:: 0.18

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    mne.io.Raw : Documentation of attributes and methods.
    """

    def __init__(
        self,
        input_fname,
        eog=(),
        misc=(),
        ecg=(),
        emg=(),
        data_format: str = "auto",
        date_format: str = "mm/dd/yy",
        *,
        header: str = "auto",
        preload: bool = False,
        verbose=None,
    ) -> None: ...
