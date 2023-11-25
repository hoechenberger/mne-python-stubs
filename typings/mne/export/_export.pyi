from ..utils import logger as logger, warn as warn
from ._egimff import export_evokeds_mff as export_evokeds_mff

def export_raw(
    fname,
    raw,
    fmt: str = ...,
    physical_range: str = ...,
    add_ch_type: bool = ...,
    *,
    overwrite: bool = ...,
    verbose=...,
) -> None:
    """Export Raw to external formats.

    Supported formats:
        - BrainVision (``.vhdr``, ``.vmrk``, ``.eeg``, uses `pybv <https://github.com/bids-standard/pybv>`_)
        - EEGLAB (``.set``, uses :mod:`eeglabio`)
        - EDF (``.edf``, uses `edfio <https://github.com/the-siesta-group/edfio>`_)

    .. warning::
        Since we are exporting to external formats, there's no guarantee that all
        the info will be preserved in the external format. See Notes for details.

    Parameters
    ----------

    fname : str
        Name of the output file.
    raw : instance of Raw
        The raw instance to export.

    fmt : 'auto' | 'brainvision' | 'edf' | 'eeglab'
        Format of the export. Defaults to ``'auto'``, which will infer the format
        from the filename extension. See supported formats above for more
        information.

    physical_range : str | tuple
        The physical range of the data. If 'auto' (default), then
        it will infer the physical min and max from the data itself,
        taking the minimum and maximum values per channel type.
        If it is a 2-tuple of minimum and maximum limit, then those
        physical ranges will be used. Only used for exporting EDF files.

    add_ch_type : bool
        Whether to incorporate the channel type into the signal label (e.g. whether
        to store channel "Fz" as "EEG Fz"). Only used for EDF format. Default is
        ``False``.

    overwrite : bool
        If True (default False), overwrite the destination file if it
        exists.

        .. versionadded:: 0.24.1

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Notes
    -----
    .. versionadded:: 0.24

    Export to external format may not preserve all the information from the
    instance. To save in native MNE format (``.fif``) without information loss,
    use :meth:`mne.io.Raw.save` instead.
    Export does not apply projector(s). Unapplied projector(s) will be lost.
    Consider applying projector(s) before exporting with
    :meth:`mne.io.Raw.apply_proj`.

    For EEGLAB exports, channel locations are expanded to full EEGLAB format.
    For more details see :func:`eeglabio.utils.cart_to_eeglab`.

    For EDF exports, only channels measured in Volts are allowed; in MNE-Python
    this means channel types 'eeg', 'ecog', 'seeg', 'emg', 'eog', 'ecg', 'dbs',
    'bio', and 'misc'. 'stim' channels are dropped. Although this function
    supports storing channel types in the signal label (e.g. ``EEG Fz`` or
    ``MISC E``), other software may not support this (optional) feature of
    the EDF standard.

    If ``add_ch_type`` is True, then channel types are written based on what
    they are currently set in MNE-Python. One should double check that all
    their channels are set correctly. You can call
    :attr:`raw.set_channel_types <mne.io.Raw.set_channel_types>` to set
    channel types.

    In addition, EDF does not support storing a montage. You will need
    to store the montage separately and call :attr:`raw.set_montage()
    <mne.io.Raw.set_montage>`.
    """

def export_epochs(
    fname, epochs, fmt: str = ..., *, overwrite: bool = ..., verbose=...
) -> None:
    """Export Epochs to external formats.

    Supported formats:
        - EEGLAB (``.set``, uses :mod:`eeglabio`)

    .. warning::
        Since we are exporting to external formats, there's no guarantee that all
        the info will be preserved in the external format. See Notes for details.

    Parameters
    ----------

    fname : str
        Name of the output file.
    epochs : instance of Epochs
        The epochs to export.

    fmt : 'auto' | 'eeglab'
        Format of the export. Defaults to ``'auto'``, which will infer the format
        from the filename extension. See supported formats above for more
        information.

    overwrite : bool
        If True (default False), overwrite the destination file if it
        exists.

        .. versionadded:: 0.24.1

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Notes
    -----
    .. versionadded:: 0.24

    Export to external format may not preserve all the information from the
    instance. To save in native MNE format (``.fif``) without information loss,
    use :meth:`mne.Epochs.save` instead.
    Export does not apply projector(s). Unapplied projector(s) will be lost.
    Consider applying projector(s) before exporting with
    :meth:`mne.Epochs.apply_proj`.

    For EEGLAB exports, channel locations are expanded to full EEGLAB format.
    For more details see :func:`eeglabio.utils.cart_to_eeglab`.
    """

def export_evokeds(
    fname, evoked, fmt: str = ..., *, overwrite: bool = ..., verbose=...
) -> None:
    """Export evoked dataset to external formats.

    This function is a wrapper for format-specific export functions. The export
    function is selected based on the inferred file format. For additional
    options, use the format-specific functions.

    Supported formats:
        - MFF (``.mff``, uses :func:`mne.export.export_evokeds_mff`)

    .. warning::
        Since we are exporting to external formats, there's no guarantee that all
        the info will be preserved in the external format. See Notes for details.

    Parameters
    ----------

    fname : str
        Name of the output file.
    evoked : Evoked instance, or list of Evoked instances
        The evoked dataset, or list of evoked datasets, to export to one file.
        Note that the measurement info from the first evoked instance is used,
        so be sure that information matches.

    fmt : 'auto' | 'mff'
        Format of the export. Defaults to ``'auto'``, which will infer the format
        from the filename extension. See supported formats above for more
        information.

    overwrite : bool
        If True (default False), overwrite the destination file if it
        exists.

        .. versionadded:: 0.24.1

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    mne.write_evokeds
    mne.export.export_evokeds_mff

    Notes
    -----
    .. versionadded:: 0.24

    Export to external format may not preserve all the information from the
    instance. To save in native MNE format (``.fif``) without information loss,
    use :meth:`mne.Evoked.save` instead.
    Export does not apply projector(s). Unapplied projector(s) will be lost.
    Consider applying projector(s) before exporting with
    :meth:`mne.Evoked.apply_proj`.
    """
