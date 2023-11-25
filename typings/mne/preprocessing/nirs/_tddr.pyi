from ...io import BaseRaw as BaseRaw


def temporal_derivative_distribution_repair(raw, *, verbose=...):
    """Apply temporal derivative distribution repair to data.

    Applies temporal derivative distribution repair (TDDR) to data
    :footcite:`FishburnEtAl2019`. This approach removes baseline shift
    and spike artifacts without the need for any user-supplied parameters.

    Parameters
    ----------
    raw : instance of Raw
        The raw data.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    raw : instance of Raw
         Data with TDDR applied.

    Notes
    -----
    TDDR was initially designed to be used on optical density fNIRS data but
    has been enabled to be applied on hemoglobin concentration fNIRS data as
    well in MNE. We recommend applying the algorithm to optical density fNIRS
    data as intended by the original author wherever possible.

    There is a shorter alias ``mne.preprocessing.nirs.tddr`` that can be used
    instead of this function (e.g. if line length is an issue).

    References
    ----------
    .. footbibliography::
    """

tddr = temporal_derivative_distribution_repair
