from ...utils import get_subjects_dir as get_subjects_dir, set_config as set_config
from _typeshed import Incomplete

FSAVERAGE_MANIFEST_PATH: Incomplete

def fetch_fsaverage(subjects_dir=..., *, verbose=...):
    """Fetch and update fsaverage.

    Parameters
    ----------
    subjects_dir : str | None
        The path to use as the subjects directory in the MNE-Python
        config file. None will use the existing config variable (i.e.,
        will not change anything), and if it does not exist, will use
        `/mne_data/MNE-fsaverage-data``.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    fs_dir : str
        The fsaverage directory.
        (essentially ``subjects_dir + '/fsaverage'``).

    Notes
    -----
    This function is designed to provide

    1. All modern (Freesurfer 6) fsaverage subject files
    2. All MNE fsaverage parcellations
    3. fsaverage head surface, fiducials, head<->MRI trans, 1- and 3-layer
       BEMs (and surfaces)

    This function will compare the contents of ``subjects_dir/fsaverage``
    to the ones provided in the remote zip file. If any are missing,
    the zip file is downloaded and files are updated. No files will
    be overwritten.

    .. versionadded:: 0.18
    """
