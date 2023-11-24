from mne.utils import get_subjects_dir as get_subjects_dir, run_subprocess as run_subprocess

def freeview_bem_surfaces(subject, subjects_dir, method) -> None:
    """View 3-Layers BEM model with Freeview.

    Parameters
    ----------
    subject : str
        Subject name
    subjects_dir : path-like
        Directory containing subjects data (Freesurfer SUBJECTS_DIR)
    method : str
        Can be ``'flash'`` or ``'watershed'``.
    """

def run() -> None:
    """Run command."""