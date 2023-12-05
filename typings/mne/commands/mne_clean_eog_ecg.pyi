def clean_ecg_eog(
    in_fif_fname,
    out_fif_fname=None,
    eog: bool = True,
    ecg: bool = True,
    ecg_proj_fname=None,
    eog_proj_fname=None,
    ecg_event_fname=None,
    eog_event_fname=None,
    in_path: str = ".",
    quiet: bool = False,
) -> None:
    """Clean ECG from raw fif file.

    Parameters
    ----------
    in_fif_fname : path-like
        Raw fif File
    eog_event_fname : str
        name of EOG event file required.
    eog : bool
        Reject or not EOG artifacts.
    ecg : bool
        Reject or not ECG artifacts.
    ecg_event_fname : str
        name of ECG event file required.
    in_path : str
        Path where all the files are.
    """
    ...

def run() -> None:
    """Run command."""
    ...
