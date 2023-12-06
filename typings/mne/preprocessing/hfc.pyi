from .._fiff.pick import pick_info as pick_info
from .._fiff.proj import Projection as Projection

def compute_proj_hfc(
    info,
    order: int = 1,
    picks: str = "meg",
    exclude: str = "bads",
    *,
    accuracy: str = "accurate",
    verbose=None,
):
    """Generate projectors to perform homogeneous/harmonic correction to data.

    Remove evironmental fields from magentometer data by assuming it is
    explained as a homogeneous `TierneyEtAl2021` or harmonic field
    `TierneyEtAl2022`. Useful for arrays of OPMs.

    Parameters
    ----------

    info : mne.Info | None
        The `mne.Info` object with information about the sensors and methods of measurement.
    order : int
        The order of the spherical harmonic basis set to use. Set to 1 to use
        only the homogeneous field component (default), 2 to add gradients, 3
        to add quadrature terms etc.
    picks : str | array_like | slice | None
        Channels to include. Default of ``'meg'`` (same as None) will select
        all non-reference MEG channels. Use ``('meg', 'ref_meg')`` to include
        reference sensors as well.
    exclude : list | 'bads'
        List of channels to exclude from HFC, only used when picking
        based on types (e.g., exclude="bads" when picks="meg").
        Specify ``'bads'`` (the default) to exclude all channels marked as bad.
    accuracy : str
        Can be ``"point"``, ``"normal"`` or ``"accurate"`` (default), defines
        which level of coil definition accuracy is used to generate model.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------

    projs : list of Projection
        List of computed projection vectors.

    See Also
    --------
    mne.io.Raw.add_proj
    mne.io.Raw.apply_proj

    Notes
    -----
    To apply the projectors to a dataset, use
    ``inst.add_proj(projs).apply_proj()``.

    ✨ Added in version 1.4

    References
    ----------
    .. footbibliography::
    """
    ...
