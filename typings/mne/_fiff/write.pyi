from ..utils import logger as logger
from .constants import FIFF as FIFF
from _typeshed import Incomplete
from collections.abc import Generator

DATE_NONE: Incomplete

def write_nop(fid, last: bool = False) -> None:
    """### Write a FIFF_NOP."""
    ...

INT32_MAX: int

def write_int(fid, kind, data) -> None:
    """### Write a 32-bit integer tag to a fif file."""
    ...

def write_double(fid, kind, data) -> None:
    """### Write a double-precision floating point tag to a fif file."""
    ...

def write_float(fid, kind, data) -> None:
    """### Write a single-precision floating point tag to a fif file."""
    ...

def write_dau_pack16(fid, kind, data) -> None:
    """### Write a dau_pack16 tag to a fif file."""
    ...

def write_complex64(fid, kind, data) -> None:
    """### Write a 64 bit complex floating point tag to a fif file."""
    ...

def write_complex128(fid, kind, data) -> None:
    """### Write a 128 bit complex floating point tag to a fif file."""
    ...

def write_julian(fid, kind, data) -> None:
    """### Write a Julian-formatted date to a FIF file."""
    ...

def write_string(fid, kind, data) -> None:
    """### Write a string tag."""
    ...

def write_name_list(fid, kind, data) -> None:
    """### Write a colon-separated list of names.

    -----
    ### 🛠️ Parameters

    data : list of strings
    """
    ...

def write_name_list_sanitized(fid, kind, lst, name) -> None:
    """### Write a sanitized, colon-separated list of names."""
    ...

def write_float_matrix(fid, kind, mat) -> None:
    """### Write a single-precision floating-point matrix tag."""
    ...

def write_double_matrix(fid, kind, mat) -> None:
    """### Write a double-precision floating-point matrix tag."""
    ...

def write_int_matrix(fid, kind, mat) -> None:
    """### Write integer 32 matrix tag."""
    ...

def write_complex_float_matrix(fid, kind, mat) -> None:
    """### Write complex 64 matrix tag."""
    ...

def write_complex_double_matrix(fid, kind, mat) -> None:
    """### Write complex 128 matrix tag."""
    ...

def get_machid():
    """### Get (mostly) unique machine ID.

    -----
    ### ⏎ Returns

    ids : array (length 2, int32)
        The machine identifier used in MNE.
    """
    ...

def get_new_file_id():
    """### Create a new file ID tag."""
    ...

def write_id(fid, kind, id_=None) -> None:
    """### Write fiff id."""
    ...

def start_block(fid, kind) -> None:
    """### Write a FIFF_BLOCK_START tag."""
    ...

def end_block(fid, kind) -> None:
    """### Write a FIFF_BLOCK_END tag."""
    ...

def start_file(fname, id_=None):
    """### Open a fif file for writing and writes the compulsory header tags.

    -----
    ### 🛠️ Parameters

    fname : path-like | fid
        The name of the file to open. It is recommended
        that the name ends with .fif or .fif.gz. Can also be an
        already opened file.
    id_ : dict | None
        ID to use for the FIFF_FILE_ID.
    """
    ...

def start_and_end_file(fname, id_=None) -> Generator[Incomplete, None, None]:
    """### Start and (if successfully written) close the file."""
    ...

def check_fiff_length(fid, close: bool = True) -> None:
    """### Ensure our file hasn't grown too large to work properly."""
    ...

def end_file(fid) -> None:
    """### Write the closing tags to a fif file and closes the file."""
    ...

def write_coord_trans(fid, trans) -> None:
    """### Write a coordinate transformation structure."""
    ...

def write_ch_info(fid, ch) -> None:
    """### Write a channel information record to a fif file."""
    ...

def write_dig_points(fid, dig, block: bool = False, coord_frame=None) -> None:
    """### Write a set of digitizer data points into a fif file."""
    ...

def write_float_sparse_rcs(fid, kind, mat):
    """### Write a single-precision sparse compressed row matrix tag."""
    ...

def write_float_sparse_ccs(fid, kind, mat):
    """### Write a single-precision sparse compressed column matrix tag."""
    ...

def write_float_sparse(fid, kind, mat, fmt: str = "auto") -> None:
    """### Write a single-precision floating-point sparse matrix tag."""
    ...
