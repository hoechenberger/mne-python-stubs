from .._fiff.pick import pick_info as pick_info
from ..cov import Covariance as Covariance, compute_whitener as compute_whitener
from ..epochs import BaseEpochs as BaseEpochs
from ..evoked import Evoked as Evoked
from ..forward import apply_forward as apply_forward
from ..io import BaseRaw as BaseRaw
from ..utils import check_random_state as check_random_state, logger as logger

def simulate_evoked(
    fwd,
    stc,
    info,
    cov=None,
    nave: int = 30,
    iir_filter=None,
    random_state=None,
    use_cps: bool = True,
    verbose=None,
):
    """### Generate noisy evoked data.

    ### 💡 Note No projections from ``info`` will be present in the
              output ``evoked``. You can use e.g.
              `evoked.add_proj <mne.Evoked.add_proj>` or
              `evoked.set_eeg_reference <mne.Evoked.set_eeg_reference>`
              to add them afterward as necessary.

    -----
    ### 🛠️ Parameters

    fwd : instance of Forward
        A forward solution.
    stc : SourceEstimate object
        The source time courses.

    info : mne.Info
        The `mne.Info` object with information about the sensors and methods of measurement. Used to generate the evoked.
    cov : Covariance object | None
        The noise covariance. If None, no noise is added.
    nave : int
        Number of averaged epochs (defaults to 30).

        ✨ Added in vesion 0.15.0
    iir_filter : None | array
        IIR filter coefficients (denominator) e.g. [1, -1, 0.2].

    random_state : None | int | instance of ~numpy.random.RandomState
        A seed for the NumPy random number generator (RNG). If ``None`` (default),
        the seed will be  obtained from the operating system
        (see  `numpy.random.RandomState` for details), meaning it will most
        likely produce different output every time this function or method is run.
        To achieve reproducible results, pass a value here to explicitly initialize
        the RNG with a defined state.

    use_cps : bool
        Whether to use cortical patch statistics to define normal orientations for
        surfaces (default True).

        ✨ Added in vesion 0.15

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    evoked : Evoked object
        The simulated evoked data.

    -----
    ### 👉 See Also

    simulate_raw
    simulate_stc
    simulate_sparse_stc

    -----
    ### 📖 Notes

    To make the equivalence between snr and nave, when the snr is given
    instead of nave::

        nave = (1 / 10 ** ((actual_snr - snr)) / 20) ** 2

    where actual_snr is the snr to the generated noise before scaling.

    ✨ Added in vesion 0.10.0
    """
    ...

def add_noise(inst, cov, iir_filter=None, random_state=None, verbose=None):
    """### Create noise as a multivariate Gaussian.

    The spatial covariance of the noise is given from the cov matrix.

    -----
    ### 🛠️ Parameters

    inst : instance of Evoked, Epochs, or Raw
        Instance to which to add noise.
    cov : instance of Covariance
        The noise covariance.
    iir_filter : None | array-like
        IIR filter coefficients (denominator).

    random_state : None | int | instance of ~numpy.random.RandomState
        A seed for the NumPy random number generator (RNG). If ``None`` (default),
        the seed will be  obtained from the operating system
        (see  `numpy.random.RandomState` for details), meaning it will most
        likely produce different output every time this function or method is run.
        To achieve reproducible results, pass a value here to explicitly initialize
        the RNG with a defined state.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    inst : instance of Evoked, Epochs, or Raw
        The instance, modified to have additional noise.

    -----
    ### 📖 Notes

    Only channels in both ``inst.info['ch_names']`` and
    ``cov['names']`` will have noise added to them.

    This function operates inplace on ``inst``.

    ✨ Added in vesion 0.18.0
    """
    ...
