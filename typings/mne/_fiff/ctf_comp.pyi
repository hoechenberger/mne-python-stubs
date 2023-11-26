from ..utils import logger as logger
from .constants import FIFF as FIFF
from .matrix import write_named_matrix as write_named_matrix
from .tag import read_tag as read_tag
from .tree import dir_tree_find as dir_tree_find
from .write import (
    end_block as end_block,
    start_block as start_block,
    write_int as write_int,
)

def read_ctf_comp(fid, node, chs, verbose=None):
    """Read the CTF software compensation data from the given node.

    Parameters
    ----------
    fid : file
        The file descriptor.
    node : dict
        The node in the FIF tree.
    chs : list
        The list of channels from info['chs'] to match with
        compensators that are read.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    compdata : list
        The compensation data
    """
    ...

def write_ctf_comp(fid, comps) -> None:
    """Write the CTF compensation data into a fif file.

    Parameters
    ----------
    fid : file
        The open FIF file descriptor

    comps : list
        The compensation data to write
    """
    ...
