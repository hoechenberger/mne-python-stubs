from ...utils import get_subjects_dir as get_subjects_dir
from _typeshed import Incomplete

PHANTOM_MANIFEST_PATH: Incomplete

def fetch_phantom(kind, subjects_dir=None, *, verbose=None):
    """### Fetch and update a phantom subject.

    ### 🛠️ Parameters
    ----------
    kind : str
        The kind of phantom to fetch. Can only be ``'otaniemi'`` (default).

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    ### ⏎ Returns
    -------
    subject_dir : str
        The resulting phantom subject directory.

    See Also
    --------
    mne.dipole.get_phantom_dipoles

    ### 📖 Notes
    -----
    This function is designed to provide a head surface and T1.mgz for
    the 32-dipole Otaniemi phantom. The VectorView/TRIUX phantom has the same
    basic outside geometry, but different internal dipole positions.

    Unlike most FreeSurfer subjects, the Otaniemi phantom scan was aligned
    to the "head" coordinate frame, so an identity head<->MRI :term:`trans`
    is appropriate.

    ✨ Added in vesion 0.24
    """
    ...
