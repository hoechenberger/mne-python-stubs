from ..utils import logger as logger, warn as warn
from .constants import FIFF as FIFF
from .tag import Tag as Tag, read_tag as read_tag, read_tag_info as read_tag_info
from .tree import dir_tree_find as dir_tree_find, make_dir_tree as make_dir_tree
from _typeshed import Incomplete

class _NoCloseRead:
    """### Create a wrapper that will not close when used as a context manager."""

    fid: Incomplete

    def __init__(self, fid) -> None: ...
    def __enter__(self): ...
    def __exit__(
        self,
        type_: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
    def close(self) -> None: ...
    def seek(self, offset, whence=0): ...
    def read(self, size: int = -1): ...

def fiff_open(fname, preload: bool = False, verbose=None):
    """### Open a FIF file.

    ### 🛠️ Parameters
    ----------
    fname : path-like | fid
        Name of the fif file, or an opened file (will seek back to 0).
    preload : bool
        If True, all data from the file is read into a memory buffer. This
        requires more memory, but can be faster for I/O operations that require
        frequent seeks.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    fid : file
        The file descriptor of the open file.
    tree : fif tree
        The tree is a complex structure filled with dictionaries,
        lists and tags.
    directory : list
        A list of tags.
    """
    ...

def show_fiff(
    fname,
    indent: str = "    ",
    read_limit=...,
    max_str: int = 30,
    output=...,
    tag=None,
    *,
    show_bytes: bool = False,
    verbose=None,
):
    """### Show FIFF information.

    This function is similar to mne_show_fiff.

    ### 🛠️ Parameters
    ----------
    fname : path-like
        Filename to evaluate.
    indent : str
        How to indent the lines.
    read_limit : int
        Max number of bytes of data to read from a tag. Can be np.inf
        to always read all data (helps test read completion).
    max_str : int
        Max number of characters of string representation to print for
        each tag's data.
    output : type
        Either str or list. str is a convenience output for printing.
    tag : int | None
        Provide information about this tag. If None (default), all information
        is shown.
    show_bytes : bool
        If True (default False), print the byte offsets of each tag.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    contents : str
        The contents of the file.
    """
    ...
