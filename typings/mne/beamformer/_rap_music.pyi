from .._fiff.pick import (
    pick_channels_forward as pick_channels_forward,
    pick_info as pick_info,
)
from ..forward import (
    convert_forward_solution as convert_forward_solution,
    is_fixed_orient as is_fixed_orient,
)
from ..utils import fill_doc as fill_doc, logger as logger

def rap_music(
    evoked,
    forward,
    noise_cov,
    n_dipoles: int = 5,
    return_residual: bool = False,
    *,
    verbose=None,
):
    """## 🧠 RAP-MUSIC source localization method.

    Compute Recursively Applied and Projected MUltiple SIgnal Classification
    (RAP-MUSIC) :footcite:`MosherLeahy1999,MosherLeahy1996` on evoked data.

    ### 💡 Note The goodness of fit (GOF) of all the returned dipoles is the
              same and corresponds to the GOF of the full set of dipoles.

    -----
    ### 🛠️ Parameters

    #### `evoked : instance of Evoked`
        Evoked data to localize.
    #### `forward : instance of Forward`
        Forward operator.
    #### `noise_cov : instance of Covariance`
        The noise covariance.
    #### `n_dipoles : int`
        The number of dipoles to look for. The default value is 5.
    #### `return_residual : bool`
        If True, the residual is returned as an Evoked instance.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `dipoles : list of instance of Dipole`
        The dipole fits.
    #### `residual : instance of Evoked`
        The residual a.k.a. data not explained by the dipoles.
        Only returned if return_residual is True.

    -----
    ### 👉 See Also

    mne.fit_dipole
    mne.beamformer.trap_music

    -----
    ### 📖 Notes

    ✨ Added in vesion 0.9.0

    References
    ----------
    .. footbibliography::
    """
    ...

def trap_music(
    evoked,
    forward,
    noise_cov,
    n_dipoles: int = 5,
    return_residual: bool = False,
    *,
    verbose=None,
):
    """## 🧠 TRAP-MUSIC source localization method.

    Compute Truncated Recursively Applied and Projected MUltiple SIgnal Classification
    (TRAP-MUSIC) :footcite:`Makela2018` on evoked data.

    ### 💡 Note The goodness of fit (GOF) of all the returned dipoles is the
              same and corresponds to the GOF of the full set of dipoles.

    -----
    ### 🛠️ Parameters

    #### `evoked : instance of Evoked`
        Evoked data to localize.
    #### `forward : instance of Forward`
        Forward operator.
    #### `noise_cov : instance of Covariance`
        The noise covariance.
    #### `n_dipoles : int`
        The number of dipoles to look for. The default value is 5.
    #### `return_residual : bool`
        If True, the residual is returned as an Evoked instance.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `dipoles : list of instance of Dipole`
        The dipole fits.
    #### `residual : instance of Evoked`
        The residual a.k.a. data not explained by the dipoles.
        Only returned if return_residual is True.

    -----
    ### 👉 See Also

    mne.fit_dipole
    mne.beamformer.rap_music

    -----
    ### 📖 Notes

    ✨ Added in vesion 1.4

    References
    ----------
    .. footbibliography::
    """
    ...
