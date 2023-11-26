from ..utils import logger as logger
from .constants import FIFF as FIFF
from .tag import Tag as Tag, read_tag as read_tag
from .write import (
    end_block as end_block,
    start_block as start_block,
    write_id as write_id,
)

def dir_tree_find(tree, kind):
    """### Find nodes of the given kind from a directory tree structure.

    ### 🛠️ Parameters
    ----------
    tree : dict
        Directory tree.
    kind : int
        Kind to find.

    ### ⏎ Returns
    -------
    nodes : list
        List of matching nodes.
    """
    ...

def make_dir_tree(fid, directory, start: int = 0, indent: int = 0, verbose=None):
    """### Create the directory tree structure."""
    ...

def copy_tree(fidin, in_id, nodes, fidout) -> None:
    """### Copy directory subtrees from fidin to fidout."""
    ...
