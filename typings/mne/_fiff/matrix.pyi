from ..utils import logger as logger
from .constants import FIFF as FIFF
from .tag import find_tag as find_tag, has_tag as has_tag
from .write import (
    end_block as end_block,
    start_block as start_block,
    write_float_matrix as write_float_matrix,
    write_int as write_int,
    write_name_list as write_name_list,
)

def write_named_matrix(fid, kind, mat) -> None:
    """### Write named matrix from the given node.

    ### 🛠️ Parameters
    ----------
    fid : file
        The opened file descriptor.
    kind : int
        The kind of the matrix.
    matkind : int
        The type of matrix.
    """
    ...
