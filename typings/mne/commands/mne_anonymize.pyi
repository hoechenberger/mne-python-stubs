from _typeshed import Incomplete

ANONYMIZE_FILE_PREFIX: str

def mne_anonymize(fif_fname, out_fname, keep_his, daysback, overwrite) -> None:
    """Call *anonymize_info* on fif file and save.

    Parameters
    ----------
    fif_fname : path-like
        Raw fif File
    out_fname : path-like | None
        Output file name
        relative paths are saved relative to parent dir of fif_fname
        None will save to parent dir of fif_fname with default prefix
    daysback : int | None
        Number of days to subtract from all dates.
        If None will default to move date of service to Jan 1 2000
    keep_his : bool
        If True his_id of subject_info will NOT be overwritten.
        defaults to False
    overwrite : bool
        Overwrite output file if it already exists
    """

def run() -> None:
    """Run *mne_anonymize* command."""

is_main: Incomplete
