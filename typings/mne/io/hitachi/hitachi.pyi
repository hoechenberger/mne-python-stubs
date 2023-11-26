from ..._fiff.constants import FIFF as FIFF
from ..._fiff.meas_info import create_info as create_info
from ...utils import fill_doc as fill_doc, logger as logger, warn as warn
from ..base import BaseRaw as BaseRaw

def read_raw_hitachi(fname, preload: bool = False, verbose=None):
    """### Reader for a Hitachi fNIRS recording.

    -----
    ### 🛠️ Parameters


    fname : list | str
        Path(s) to the Hitachi CSV file(s). This should only be a list for
        multiple probes that were acquired simultaneously.

        🎭 Changed in version 1.2
            Added support for list-of-str.

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

    -----
    ### ⏎ Returns

    raw : instance of RawHitachi
        A Raw object containing Hitachi data.
        See `mne.io.Raw` for documentation of attributes and methods.

    -----
    ### 👉 See Also

    mne.io.Raw : Documentation of attributes and methods of RawHitachi.

    -----
    ### 📖 Notes


    Hitachi does not encode their channel positions, so you will need to
    create a suitable mapping using `mne.channels.make_standard_montage`
    or `mne.channels.make_dig_montage` like (for a 3x5/ETG-7000 example):

    >>> mon = mne.channels.make_standard_montage('standard_1020')
    >>> need = 'S1 D1 S2 D2 S3 D3 S4 D4 S5 D5 S6 D6 S7 D7 S8'.split()
    >>> have = 'F3 FC3 C3 CP3 P3 F5 FC5 C5 CP5 P5 F7 FT7 T7 TP7 P7'.split()
    >>> mon.rename_channels(dict(zip(have, need)))
    >>> raw.set_montage(mon)  # doctest: +SKIP

    The 3x3 (ETG-100) is laid out as two separate layouts::

        S1--D1--S2    S6--D6--S7
        |   |   |     |   |   |
        D2--S3--D3    D7--S8--D8
        |   |   |     |   |   |
        S4--D4--S5    S9--D9--S10

    The 3x5 (ETG-7000) is laid out as::

        S1--D1--S2--D2--S3
        |   |   |   |   |
        D3--S4--D4--S5--D5
        |   |   |   |   |
        S6--D6--S7--D7--S8

    The 4x4 (ETG-7000) is laid out as::

        S1--D1--S2--D2
        |   |   |   |
        D3--S3--D4--S4
        |   |   |   |
        S5--D5--S6--D6
        |   |   |   |
        D7--S7--D8--S8

    The 3x11 (ETG-4000) is laid out as::

        S1--D1--S2--D2--S3--D3--S4--D4--S5--D5--S6
        |   |   |   |   |   |   |   |   |   |   |
        D6--S7--D7--S8--D8--S9--D9--S10-D10-S11-D11
        |   |   |   |   |   |   |   |   |   |   |
        S12-D12-S13-D13-S14-D14-S16-D16-S17-D17-S18

    For each layout, the channels come from the (left-to-right) neighboring
    source-detector pairs in the first row, then between the first and second row,
    then the second row, etc.

    ✨ Added in vesion 0.24
    """
    ...

class RawHitachi(BaseRaw):
    """### Raw object from a Hitachi fNIRS file.

    -----
    ### 🛠️ Parameters


    fname : list | str
        Path(s) to the Hitachi CSV file(s). This should only be a list for
        multiple probes that were acquired simultaneously.

        🎭 Changed in version 1.2
            Added support for list-of-str.

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

    -----
    ### 👉 See Also

    mne.io.Raw : Documentation of attributes and methods.

    -----
    ### 📖 Notes


    Hitachi does not encode their channel positions, so you will need to
    create a suitable mapping using `mne.channels.make_standard_montage`
    or `mne.channels.make_dig_montage` like (for a 3x5/ETG-7000 example):

    >>> mon = mne.channels.make_standard_montage('standard_1020')
    >>> need = 'S1 D1 S2 D2 S3 D3 S4 D4 S5 D5 S6 D6 S7 D7 S8'.split()
    >>> have = 'F3 FC3 C3 CP3 P3 F5 FC5 C5 CP5 P5 F7 FT7 T7 TP7 P7'.split()
    >>> mon.rename_channels(dict(zip(have, need)))
    >>> raw.set_montage(mon)  # doctest: +SKIP

    The 3x3 (ETG-100) is laid out as two separate layouts::

        S1--D1--S2    S6--D6--S7
        |   |   |     |   |   |
        D2--S3--D3    D7--S8--D8
        |   |   |     |   |   |
        S4--D4--S5    S9--D9--S10

    The 3x5 (ETG-7000) is laid out as::

        S1--D1--S2--D2--S3
        |   |   |   |   |
        D3--S4--D4--S5--D5
        |   |   |   |   |
        S6--D6--S7--D7--S8

    The 4x4 (ETG-7000) is laid out as::

        S1--D1--S2--D2
        |   |   |   |
        D3--S3--D4--S4
        |   |   |   |
        S5--D5--S6--D6
        |   |   |   |
        D7--S7--D8--S8

    The 3x11 (ETG-4000) is laid out as::

        S1--D1--S2--D2--S3--D3--S4--D4--S5--D5--S6
        |   |   |   |   |   |   |   |   |   |   |
        D6--S7--D7--S8--D8--S9--D9--S10-D10-S11-D11
        |   |   |   |   |   |   |   |   |   |   |
        S12-D12-S13-D13-S14-D14-S16-D16-S17-D17-S18

    For each layout, the channels come from the (left-to-right) neighboring
    source-detector pairs in the first row, then between the first and second row,
    then the second row, etc.

    ✨ Added in vesion 0.24
    """

    def __init__(self, fname, preload: bool = False, *, verbose=None) -> None: ...
