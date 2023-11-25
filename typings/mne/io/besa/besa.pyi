from ..._fiff.meas_info import create_info as create_info
from ...evoked import EvokedArray as EvokedArray
from ...utils import fill_doc as fill_doc, logger as logger

def read_evoked_besa(fname, verbose=...):
    """Reader function for BESA ``.avr`` or ``.mul`` files.

    When a ``.elp`` sidecar file is present, it will be used to determine
    electrode information.

    Parameters
    ----------
    fname : path-like
        Path to the ``.avr`` or ``.mul`` file.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    ev : Evoked
        The evoked data in the .avr or .mul file.
    """
