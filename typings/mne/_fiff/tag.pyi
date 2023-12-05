from ..utils import warn as warn
from .constants import FIFF as FIFF
from _typeshed import Incomplete

class Tag:
    """Tag in FIF tree structure.

    Parameters
    ----------
    kind : int
        Kind of Tag.
    type_ : int
        Type of Tag.
    size : int
        Size in bytes.
    int : next
        Position of next Tag.
    pos : int
        Position of Tag is the original file.
    """

    kind: Incomplete
    type: Incomplete
    size: Incomplete
    next: Incomplete
    pos: Incomplete
    data: Incomplete

    def __init__(self, kind, type_, size, next, pos=None) -> None: ...
    def __eq__(self, tag): ...

def read_tag_info(fid):
    """Read Tag info (or header)."""
    ...

def read_tag(fid, pos=None, shape=None, rlims=None):
    """Read a Tag from a file at a given position.

    Parameters
    ----------
    fid : file
        The open FIF file descriptor.
    pos : int
        The position of the Tag in the file.
    shape : tuple | None
        If tuple, the shape of the stored matrix. Only to be used with
        data stored as a vector (not implemented for matrices yet).
    rlims : tuple | None
        If tuple, the first (inclusive) and last (exclusive) rows to retrieve.
        Note that data are assumed to be stored row-major in the file. Only to
        be used with data stored as a vector (not implemented for matrices
        yet).

    Returns
    -------
    tag : Tag
        The Tag read.
    """
    ...

def find_tag(fid, node, findkind):
    """Find Tag in an open FIF file descriptor.

    Parameters
    ----------
    fid : file-like
        Open file.
    node : dict
        Node to search.
    findkind : int
        Tag kind to find.

    Returns
    -------
    tag : instance of Tag
        The first tag found.
    """
    ...

def has_tag(node, kind):
    """Check if the node contains a Tag of a given kind."""
    ...
