from .._fiff.pick import pick_channels as pick_channels, pick_types as pick_types
from ..utils import verbose as verbose, warn as warn
from _typeshed import Incomplete

def export_evokeds_mff(fname, evoked, history: Incomplete | None=..., *, overwrite: bool=..., verbose: Incomplete | None=...) -> None:
    """Export evoked dataset to MFF.

    .. warning::
        Since we are exporting to external formats, there's no guarantee that all
        the info will be preserved in the external format. See Notes for details.

    Parameters
    ----------
    
    fname : str
        Name of the output file.
    evoked : list of Evoked instances
        List of evoked datasets to export to one file. Note that the
        measurement info from the first evoked instance is used, so be sure
        that information matches.
    history : None (default) | list of dict
        Optional list of history entries (dictionaries) to be written to
        history.xml. This must adhere to the format described in
        mffpy.xml_files.History.content. If None, no history.xml will be
        written.
    
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
    use :meth:`mne.Evoked.save` instead.
    Export does not apply projector(s). Unapplied projector(s) will be lost.
    Consider applying projector(s) before exporting with
    :meth:`mne.Evoked.apply_proj`.

    Only EEG channels are written to the output file.
    ``info['device_info']['type']`` must be a valid MFF recording device
    (e.g. 'HydroCel GSN 256 1.0'). This field is automatically populated when
    using MFF read functions.
    """