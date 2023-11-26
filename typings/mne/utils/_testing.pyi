from ._logging import ClosingStringIO as ClosingStringIO, warn as warn
from .check import check_version as check_version
from .misc import run_subprocess as run_subprocess
from .numerics import object_diff as object_diff
from _typeshed import Incomplete

class _TempDir(str):
    """## 🧠 Create and auto-destroy temp dir.

    This is designed to be used with testing modules. Instances should be
    defined inside test functions. Instances defined at module level can not
    guarantee proper destruction of the temporary directory.

    When used at module level, the current use of the __del__() method for
    cleanup can fail because the rmtree function may be cleaned up before this
    object (an alternative could be using the atexit module instead).
    """

    def __new__(self): ...
    def __init__(self) -> None: ...
    def __del__(self) -> None: ...

def requires_mne(func):
    """## 🧠 Decorate a function as requiring MNE."""
    ...

def requires_mne_mark():
    """## 🧠 Mark pytest tests that require MNE-C."""
    ...

def requires_openmeeg_mark():
    """## 🧠 Mark pytest tests that require OpenMEEG."""
    ...

def requires_freesurfer(arg):
    """## 🧠 Require Freesurfer."""
    ...

def requires_good_network(func): ...
def run_command_if_main() -> None:
    """## 🧠 Run a given command if it's __main__."""
    ...

class ArgvSetter:
    """## 🧠 Temporarily set sys.argv."""

    argv: Incomplete
    stdout: Incomplete
    stderr: Incomplete

    def __init__(
        self, args=(), disable_stdout: bool = True, disable_stderr: bool = True
    ) -> None: ...
    orig_argv: Incomplete
    orig_stdout: Incomplete
    orig_stderr: Incomplete

    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...

class SilenceStdout:
    """## 🧠 Silence stdout."""

    close: Incomplete

    def __init__(self, close: bool = True) -> None: ...
    stdout: Incomplete

    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...

def has_mne_c():
    """## 🧠 Check for MNE-C."""
    ...

def has_freesurfer():
    """## 🧠 Check for Freesurfer."""
    ...

def buggy_mkl_svd(function):
    """## 🧠 Decorate tests that make calls to SVD and intermittently fail."""
    ...

def assert_and_remove_boundary_annot(annotations, n: int = 1) -> None:
    """## 🧠 Assert that there are boundary annotations and remove them."""
    ...

def assert_object_equal(a, b) -> None:
    """## 🧠 Assert two objects are equal."""
    ...

def assert_meg_snr(
    actual,
    desired,
    min_tol,
    med_tol: float = 500.0,
    chpi_med_tol: float = 500.0,
    msg=None,
) -> None:
    """## 🧠 Assert channel SNR of a certain level.

    Mostly useful for operations like Maxwell filtering that modify
    MEG channels while leaving EEG and others intact.
    """
    ...

def assert_snr(actual, desired, tol) -> None:
    """## 🧠 Assert actual and desired arrays are within some SNR tolerance."""
    ...

def assert_stcs_equal(stc1, stc2) -> None:
    """## 🧠 Check that two STC are equal."""
    ...

def assert_dig_allclose(info_py, info_bin, limit=None) -> None:
    """## 🧠 Assert dig allclose."""
    ...
