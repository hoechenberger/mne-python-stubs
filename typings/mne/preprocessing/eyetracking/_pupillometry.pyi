from ..._fiff.constants import FIFF as FIFF
from ...io import BaseRaw as BaseRaw
from ...utils import logger as logger, warn as warn

def interpolate_blinks(
    raw, buffer: float = 0.05, match: str = "BAD_blink", interpolate_gaze: bool = False
):
    """## Interpolate eyetracking signals during blinks.

    This function uses the timing of blink annotations to estimate missing
    data. Operates in place.

    -----
    ### 🛠️ Parameters

    #### `raw : instance of Raw`
        The raw data with at least one ``'pupil'`` or ``'eyegaze'`` channel.
    #### `buffer : float | array-like of float, shape ``(2,))```
        The time in seconds before and after a blink to consider invalid and
        include in the segment to be interpolated over. Default is ``0.05`` seconds
        (50 ms). If array-like, the first element is the time before the blink and the
        second element is the time after the blink to consider invalid, for example,
        ``(0.025, .1)``.
    #### `match : str | list of str`
        The description of annotations to interpolate over. If a list, the data within
        all annotations that match any of the strings in the list will be interpolated
        over. Defaults to ``'BAD_blink'``.
    #### `interpolate_gaze : bool`
        If False, only apply interpolation to ``'pupil channels'``. If True, interpolate
        over ``'eyegaze'`` channels as well. Defaults to False, because eye position can
        change in unpredictable ways during blinks.

    -----
    ### ⏎ Returns

    #### `self : instance of Raw`
        Returns the modified instance.

    -----
    ### 📖 Notes

    ✨ Added in version 1.5
    """
    ...
