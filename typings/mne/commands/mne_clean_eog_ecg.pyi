from _typeshed import Incomplete

def clean_ecg_eog(in_fif_fname, out_fif_fname: Incomplete | None=..., eog: bool=..., ecg: bool=..., ecg_proj_fname: Incomplete | None=..., eog_proj_fname: Incomplete | None=..., ecg_event_fname: Incomplete | None=..., eog_event_fname: Incomplete | None=..., in_path: str=..., quiet: bool=...) -> None:
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

def run() -> None:
    """Run command."""