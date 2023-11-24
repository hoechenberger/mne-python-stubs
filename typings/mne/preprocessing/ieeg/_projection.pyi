from ...channels import make_dig_montage as make_dig_montage
from ...surface import fast_cross_3d as fast_cross_3d, read_surface as read_surface
from ...transforms import apply_trans as apply_trans, invert_transform as invert_transform
from ...utils import get_subjects_dir as get_subjects_dir, verbose as verbose
from _typeshed import Incomplete

def project_sensors_onto_brain(info, trans, subject, subjects_dir: Incomplete | None=..., picks: Incomplete | None=..., n_neighbors: int=..., copy: bool=..., verbose: Incomplete | None=...):
    """Project sensors onto the brain surface.

    Parameters
    ----------
    
    info : mne.Info
        The :class:`mne.Info` object with information about the sensors and methods of measurement.
    
    trans : str | dict | instance of Transform
        If str, the path to the head<->MRI transform ``*-trans.fif`` file produced
        during coregistration. Can also be ``'fsaverage'`` to use the built-in
        fsaverage transformation.
    
    subject : str
        The FreeSurfer subject name.
    
    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as 
        channel indices. In lists, channel *type* strings (e.g., ``['meg', 
        'eeg']``) will pick channels of those types, channel *name* strings (e.g., 
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the 
        string values "all" to pick all channels, or "data" to pick :term:`data 
        channels`. None (default) will pick only ``ecog`` channels.
    n_neighbors : int
        The number of neighbors to use to compute the normal vectors
        for the projection. Must be 2 or greater. More neighbors makes
        a normal vector with greater averaging which preserves the grid
        structure. Fewer neighbors has less averaging which better
        preserves contours in the grid.
    copy : bool
        If ``True``, return a new instance of ``info``, if ``False``
        ``info`` is modified in place.
    
    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    
    info : mne.Info
        The :class:`mne.Info` object with information about the sensors and methods of measurement.

    Notes
    -----
    This is useful in ECoG analysis for compensating for "brain shift"
    or shrinking of the brain away from the skull due to changes
    in pressure during the craniotomy.

    To use the brain surface, a BEM model must be created e.g. using
    :ref:`mne watershed_bem` using the T1 or :ref:`mne flash_bem`
    using a FLASH scan.
    """