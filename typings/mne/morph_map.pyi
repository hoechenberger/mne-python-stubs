from ._fiff.constants import FIFF as FIFF
from ._fiff.open import fiff_open as fiff_open
from ._fiff.tag import find_tag as find_tag
from ._fiff.tree import dir_tree_find as dir_tree_find
from ._fiff.write import (
    end_block as end_block,
    start_and_end_file as start_and_end_file,
    start_block as start_block,
    write_float_sparse_rcs as write_float_sparse_rcs,
    write_int as write_int,
    write_string as write_string,
)
from .surface import read_surface as read_surface
from .utils import get_subjects_dir as get_subjects_dir, logger as logger, warn as warn

def read_morph_map(
    subject_from, subject_to, subjects_dir=..., xhemi: bool = ..., verbose=...
):
    """Read morph map.

    Morph maps can be generated with mne_make_morph_maps. If one isn't
    available, it will be generated automatically and saved to the
    ``subjects_dir/morph_maps`` directory.

    Parameters
    ----------
    subject_from : str
        Name of the original subject as named in the ``SUBJECTS_DIR``.
    subject_to : str
        Name of the subject on which to morph as named in the ``SUBJECTS_DIR``.
    subjects_dir : path-like
        Path to ``SUBJECTS_DIR`` is not set in the environment.
    xhemi : bool
        Morph across hemisphere. Currently only implemented for
        ``subject_to == subject_from``. See notes of
        :func:`mne.compute_source_morph`.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    left_map, right_map : ~scipy.sparse.csr_matrix
        The morph maps for the 2 hemispheres.
    """
