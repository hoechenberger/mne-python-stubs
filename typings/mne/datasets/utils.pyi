from ..label import (
    Label as Label,
    read_labels_from_annot as read_labels_from_annot,
    write_labels_to_annot as write_labels_to_annot,
)
from ..utils import (
    get_config as get_config,
    get_subjects_dir as get_subjects_dir,
    logger as logger,
    set_config as set_config,
)
from ..utils.docs import docdict as docdict
from .config import MNE_DATASETS as MNE_DATASETS

def has_dataset(name):
    """Check for presence of a dataset.

    Parameters
    ----------
    name : str | dict
        The dataset to check. Strings refer to one of the supported datasets
        listed `here <datasets>`. A `dict` can be used to check for
        user-defined datasets (see the Notes section of `fetch_dataset`),
        and must contain keys ``dataset_name``, ``archive_name``, ``url``,
        ``folder_name``, ``hash``.

    Returns
    -------
    has : bool
        True if the dataset is present.
    """
    ...

def fetch_aparc_sub_parcellation(subjects_dir=None, verbose=None) -> None:
    """Fetch the modified subdivided aparc parcellation.

    This will download and install the subdivided aparc parcellation
    'KhanEtAl2018' files for
    FreeSurfer's fsaverage to the specified directory.

    Parameters
    ----------
    subjects_dir : path-like | None
        The subjects directory to use. The file will be placed in
        ``subjects_dir + '/fsaverage/label'``.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    References
    ----------
    .. footbibliography::
    """
    ...

def fetch_hcp_mmp_parcellation(
    subjects_dir=None, combine: bool = True, *, accept: bool = False, verbose=None
) -> None:
    """Fetch the HCP-MMP parcellation.

    This will download and install the HCP-MMP parcellation
    `GlasserEtAl2016` files for FreeSurfer's fsaverage
    `Mills2016` to the specified directory.

    Parameters
    ----------
    subjects_dir : path-like | None
        The subjects directory to use. The file will be placed in
        ``subjects_dir + '/fsaverage/label'``.
    combine : bool
        If True, also produce the combined/reduced set of 23 labels per
        hemisphere as ``HCPMMP1_combined.annot``
        `GlasserEtAl2016supp`.

    accept : bool
        If True (default False), accept the license terms of this dataset.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Notes
    -----
    Use of this parcellation is subject to terms of use on the
    `HCP-MMP webpage <https://balsa.wustl.edu/WN56>`_.

    References
    ----------
    .. footbibliography::
    """
    ...
