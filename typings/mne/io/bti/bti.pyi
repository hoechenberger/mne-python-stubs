from ..._fiff.constants import FIFF as FIFF
from ..._fiff.utils import read_str as read_str
from ...transforms import Transform as Transform, combine_transforms as combine_transforms, invert_transform as invert_transform
from ...utils import logger as logger, path_like as path_like, verbose as verbose
from ..base import BaseRaw as BaseRaw
from .constants import BTI as BTI
from .read import read_char as read_char, read_dev_header as read_dev_header, read_double as read_double, read_double_matrix as read_double_matrix, read_float as read_float, read_float_matrix as read_float_matrix, read_int16 as read_int16, read_int16_matrix as read_int16_matrix, read_int32 as read_int32, read_int64 as read_int64, read_transform as read_transform, read_uint16 as read_uint16, read_uint32 as read_uint32
from _typeshed import Incomplete
FIFF_INFO_DIG_FIELDS: Incomplete
FIFF_INFO_DIG_DEFAULTS: Incomplete
BTI_WH2500_REF_MAG: Incomplete
BTI_WH2500_REF_GRAD: Incomplete
dtypes: Incomplete
DTYPES: Incomplete

class _bytes_io_mock_context:
    """Make a context for BytesIO."""
    target: Incomplete

    def __init__(self, target) -> None:
        ...

    def __enter__(self):
        ...

    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, tb: types.TracebackType | None) -> None:
        ...

class RawBTi(BaseRaw):
    """Raw object from 4D Neuroimaging MagnesWH3600 data.

    Parameters
    ----------
    pdf_fname : path-like
        Path to the processed data file (PDF).
    config_fname : path-like
        Path to system config file.
    head_shape_fname : path-like | None
        Path to the head shape file.
    rotation_x : float
        Degrees to tilt x-axis for sensor frame misalignment. Ignored
        if convert is True.
    translation : array-like, shape (3,)
        The translation to place the origin of coordinate system
        to the center of the head. Ignored if convert is True.
    convert : bool
        Convert to Neuromag coordinates or not.
    rename_channels : bool
        Whether to keep original 4D channel labels or not. Defaults to True.
    sort_by_ch_name : bool
        Reorder channels according to channel label. 4D channels don't have
        monotonically increasing numbers in their labels. Defaults to True.
    ecg_ch : str | None
        The 4D name of the ECG channel. If None, the channel will be treated
        as regular EEG channel.
    eog_ch : tuple of str | None
        The 4D names of the EOG channels. If None, the channels will be treated
        as regular EEG channels.
    %(preload)s

        .. versionadded:: 0.11

    %(verbose)s
    """

    def __init__(self, pdf_fname, config_fname: str=..., head_shape_fname: str=..., rotation_x: float=..., translation=..., convert: bool=..., rename_channels: bool=..., sort_by_ch_name: bool=..., ecg_ch: str=..., eog_ch=..., preload: bool=..., verbose: Incomplete | None=...) -> None:
        ...

def read_raw_bti(pdf_fname, config_fname: str=..., head_shape_fname: str=..., rotation_x: float=..., translation=..., convert: bool=..., rename_channels: bool=..., sort_by_ch_name: bool=..., ecg_ch: str=..., eog_ch=..., preload: bool=..., verbose: Incomplete | None=...):
    """Raw object from 4D Neuroimaging MagnesWH3600 data.

    .. note::
        1. Currently direct inclusion of reference channel weights
           is not supported. Please use ``mne_create_comp_data`` to include
           the weights or use the low level functions from this module to
           include them by yourself.
        2. The informed guess for the 4D name is E31 for the ECG channel and
           E63, E63 for the EOG channels. Please check and adjust if those
           channels are present in your dataset but 'ECG 01' and 'EOG 01',
           'EOG 02' don't appear in the channel names of the raw object.

    Parameters
    ----------
    pdf_fname : path-like
        Path to the processed data file (PDF).
    config_fname : path-like
        Path to system config file.
    head_shape_fname : path-like | None
        Path to the head shape file.
    rotation_x : float
        Degrees to tilt x-axis for sensor frame misalignment. Ignored
        if convert is True.
    translation : array-like, shape (3,)
        The translation to place the origin of coordinate system
        to the center of the head. Ignored if convert is True.
    convert : bool
        Convert to Neuromag coordinates or not.
    rename_channels : bool
        Whether to keep original 4D channel labels or not. Defaults to True.
    sort_by_ch_name : bool
        Reorder channels according to channel label. 4D channels don't have
        monotonically increasing numbers in their labels. Defaults to True.
    ecg_ch : str | None
        The 4D name of the ECG channel. If None, the channel will be treated
        as regular EEG channel.
    eog_ch : tuple of str | None
        The 4D names of the EOG channels. If None, the channels will be treated
        as regular EEG channels.
    
    preload : bool or str (default False)
        Preload data into memory for data manipulation and faster indexing.
        If True, the data will be preloaded into memory (fast, requires
        large amount of memory). If preload is a string, preload is the
        file name of a memory-mapped file which is used to store the data
        on the hard drive (slower, requires less memory).

        .. versionadded:: 0.11
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    raw : instance of RawBTi
        A Raw object containing BTI data.
        See :class:`mne.io.Raw` for documentation of attributes and methods.

    See Also
    --------
    mne.io.Raw : Documentation of attributes and methods of RawBTi.
    """