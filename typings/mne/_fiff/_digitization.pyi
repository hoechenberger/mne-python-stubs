from ..utils import Bunch as Bunch, logger as logger, warn as warn
from .constants import FIFF as FIFF
from .tag import read_tag as read_tag
from .tree import dir_tree_find as dir_tree_find
from .write import (
    start_and_end_file as start_and_end_file,
    write_dig_points as write_dig_points,
)

class DigPoint(dict):
    """Compare two DigPoints.

    Two digpoints are equal if they are the same kind, share the same
    coordinate frame and position.
    """

    def __deepcopy__(self, memodict):
        """Make a deepcopy."""
    def __eq__(self, other):
        """Compare two DigPoints.

        Two digpoints are equal if they are the same kind, share the same
        coordinate frame and position.
        """

def write_dig(
    fname, pts, coord_frame=..., *, overwrite: bool = ..., verbose=...
) -> None:
    """Write digitization data to a FIF file.

    Parameters
    ----------
    fname : path-like
        Destination file name.
    pts : iterator of dict
        Iterator through digitizer points. Each point is a dictionary with
        the keys 'kind', 'ident' and 'r'.
    coord_frame : int | str | None
        If all the points have the same coordinate frame, specify the type
        here. Can be None (default) if the points could have varying
        coordinate frames.

    overwrite : bool
        If True (default False), overwrite the destination file if it
        exists.

        .. versionadded:: 1.0

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

        .. versionadded:: 1.0
    """
