from ...channels import DigMontage as DigMontage, make_dig_montage as make_dig_montage
from ...transforms import Transform as Transform, apply_trans as apply_trans
from ...utils import warn as warn

def warp_montage(montage, moving, static, reg_affine, sdr_morph, verbose=...):
    """Warp a montage to a template with image volumes using SDR.

    .. note:: This is likely only applicable for channels inside the brain
              (intracranial electrodes).

    Parameters
    ----------
    montage : instance of mne.channels.DigMontage
        The montage object containing the channels.

    moving : instance of SpatialImage
        The image to morph ("from" volume).

    static : instance of SpatialImage
        The image to align with ("to" volume).

    reg_affine : ndarray of float, shape (4, 4)
        The affine that registers one volume to another.

    sdr_morph : instance of dipy.align.DiffeomorphicMap
        The class that applies the the symmetric diffeomorphic registration
        (SDR) morph.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    montage_warped : mne.channels.DigMontage
        The modified montage object containing the channels.
    """

def make_montage_volume(
    montage,
    base_image,
    thresh: float = ...,
    max_peak_dist: int = ...,
    voxels_max: int = ...,
    use_min: bool = ...,
    verbose=...,
):
    """Make a volume from intracranial electrode contact locations.

    Find areas of the input volume with intensity greater than
    a threshold surrounding local extrema near the channel location.
    Monotonicity from the peak is enforced to prevent channels
    bleeding into each other.

    Parameters
    ----------
    montage : instance of mne.channels.DigMontage
        The montage object containing the channels.
    base_image : path-like | nibabel.spatialimages.SpatialImage
        Path to a volumetric scan (e.g. CT) of the subject. Can be in any
        format readable by nibabel. Can also be a nibabel image object.
        Local extrema (max or min) should be nearby montage channel locations.
    thresh : float
        The threshold relative to the peak to determine the size
        of the sensors on the volume.
    max_peak_dist : int
        The number of voxels away from the channel location to
        look in the ``image``. This will depend on the accuracy of
        the channel locations, the default (one voxel in all directions)
        will work only with localizations that are that accurate.
    voxels_max : int
        The maximum number of voxels for each channel.
    use_min : bool
        Whether to hypointensities in the volume as channel locations.
        Default False uses hyperintensities.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    elec_image : nibabel.spatialimages.SpatialImage
        An image in Freesurfer surface RAS space with voxel values
        corresponding to the index of the channel. The background
        is 0s and this index starts at 1.
    """
