from _typeshed import Incomplete
from collections.abc import Generator
from mne import Epochs as Epochs, pick_types as pick_types, read_events as read_events
from mne.channels import read_layout as read_layout
from mne.coreg import create_default_subject as create_default_subject
from mne.datasets import testing as testing
from mne.fixes import has_numba as has_numba
from mne.io import read_raw_ctf as read_raw_ctf, read_raw_fif as read_raw_fif, read_raw_nirx as read_raw_nirx, read_raw_snirf as read_raw_snirf
from mne.stats import cluster_level as cluster_level
from mne.utils import Bunch as Bunch, numerics as numerics
from mne.viz._figure import use_browser_backend as use_browser_backend
test_path: Incomplete
s_path: Incomplete
fname_evoked: Incomplete
fname_cov: Incomplete
fname_fwd: Incomplete
fname_fwd_full: Incomplete
bem_path: Incomplete
fname_bem: Incomplete
fname_aseg: Incomplete
subjects_dir: Incomplete
fname_src: Incomplete
fname_trans: Incomplete
ctf_dir: Incomplete
fname_ctf_continuous: Incomplete
nirx_path: Incomplete
snirf_path: Incomplete
nirsport2: Incomplete
nirsport2_snirf: Incomplete
nirsport2_2021_9: Incomplete
nirsport2_20219_snirf: Incomplete
base_dir: Incomplete
fname_raw_io: Incomplete
fname_event_io: Incomplete
fname_cov_io: Incomplete
fname_evoked_io: Incomplete
event_id: Incomplete
tmin: Incomplete
tmax: Incomplete
vv_layout: Incomplete
collect_ignore: Incomplete

def pytest_configure(config) -> None:
    """Configure pytest options."""

def check_verbose(request) -> Generator[None, None, None]:
    """Set to the default logging level to ensure it's tested properly."""

def close_all() -> Generator[None, None, None]:
    """Close all matplotlib plots, regardless of test status."""

def add_mne(doctest_namespace) -> None:
    """Add mne to the namespace."""

def verbose_debug() -> Generator[None, None, None]:
    """Run a test with debug verbosity."""

def qt_config() -> None:
    """Configure the Qt backend for viz tests."""

def matplotlib_config() -> None:
    """Configure matplotlib for viz tests."""

def azure_windows():
    """Determine if running on Azure Windows."""

def raw_orig():
    """Get raw data without any change to it from mne.io.tests.data."""

def raw():
    """
    Get raw data and pick channels to reduce load for testing.

    (from mne.io.tests.data)
    """

def raw_ctf():
    """Get ctf raw data from mne.io.tests.data."""

def raw_spectrum(raw):
    """Get raw with power spectral density computed from mne.io.tests.data."""

def events():
    """Get events from mne.io.tests.data."""

def epochs():
    """
    Get minimal, pre-loaded epochs data suitable for most tests.

    (from mne.io.tests.data)
    """

def epochs_unloaded():
    """Get minimal, unloaded epochs data from mne.io.tests.data."""

def epochs_full():
    """Get full, preloaded epochs from mne.io.tests.data."""

def epochs_spectrum():
    """Get epochs with power spectral density computed from mne.io.tests.data."""

def epochs_empty():
    """Get empty epochs from mne.io.tests.data."""

def evoked(_evoked):
    """Get evoked data."""

def noise_cov():
    """Get a noise cov from the testing dataset."""

def noise_cov_io():
    """Get noise-covariance (from mne.io.tests.data)."""

def bias_params_free(evoked, noise_cov):
    """Provide inputs for free bias functions."""

def bias_params_fixed(evoked, noise_cov):
    """Provide inputs for fixed bias functions."""

def garbage_collect() -> Generator[None, None, None]:
    """Garbage collect on exit."""

def mpl_backend(garbage_collect) -> Generator[Incomplete, None, None]:
    """Use for epochs/ica when not implemented with pyqtgraph yet."""
pre_2_0_skip_modules: Incomplete
pre_2_0_skip_funcs: Incomplete

def pg_backend(request, garbage_collect) -> Generator[Incomplete, None, None]:
    """Use for pyqtgraph-specific test-functions."""

def browser_backend(request, garbage_collect, monkeypatch) -> Generator[Incomplete, None, None]:
    """Parametrizes the name of the browser backend."""

def renderer(request, options_3d, garbage_collect) -> Generator[Incomplete, None, None]:
    """Yield the 3D backends."""

def renderer_pyvistaqt(request, options_3d, garbage_collect) -> Generator[Incomplete, None, None]:
    """Yield the PyVista backend."""

def renderer_notebook(request, options_3d) -> Generator[Incomplete, None, None]:
    """Yield the 3D notebook renderer."""

def renderer_interactive_pyvistaqt(request, options_3d, qt_windows_closed) -> Generator[Incomplete, None, None]:
    """Yield the interactive PyVista backend."""

def renderer_interactive(request, options_3d) -> Generator[Incomplete, None, None]:
    """Yield the interactive 3D backends."""

def pixel_ratio():
    """Get the pixel ratio."""

def subjects_dir_tmp(tmp_path):
    """Copy MNE-testing-data subjects_dir to a temp dir for manipulation."""

def subjects_dir_tmp_few(tmp_path):
    """Copy fewer files to a tmp_path."""

def fwd_volume_small(_fwd_subvolume):
    """Provide a small volumetric source space."""

def all_src_types_inv_evoked(_all_src_types_inv_evoked):
    """All source types of inverses, allowing for possible modification."""

def mixed_fwd_cov_evoked(_evoked_cov_sphere, _all_src_types_fwd):
    """Compute inverses for all source types."""

def src_volume_labels():
    """Create a 7mm source space with labels."""

def download_is_error(monkeypatch) -> Generator[None, None, None]:
    """Prevent downloading by raising an error when it's attempted."""

def fake_retrieve(monkeypatch, download_is_error) -> Generator[Incomplete, None, None]:
    """Monkeypatch pooch.retrieve to avoid downloading (just touch files)."""

class _FakeFetch:
    call_args_list: Incomplete

    def __init__(self) -> None:
        ...

    @property
    def call_count(self):
        ...
    path: Incomplete

    def __call__(self, *args, **kwargs):
        ...

    def fetch(self, fname) -> None:
        ...

    def load_registry(self, registry) -> None:
        ...

def options_3d() -> Generator[None, None, None]:
    """Disable advanced 3d rendering."""

def protect_config() -> Generator[None, None, None]:
    """Protect ~/.mne."""

def brain_gc(request) -> Generator[None, None, None]:
    """Ensure that brain can be properly garbage collected."""

def pytest_sessionfinish(session, exitstatus):
    """Handle the end of the session."""

def pytest_terminal_summary(terminalreporter, exitstatus, config) -> None:
    """Print the module-level timings."""

def numba_conditional(monkeypatch, request) -> Generator[Incomplete, None, None]:
    """Test both code paths on machines that have Numba."""

def nbexec(_nbclient) -> Generator[Incomplete, None, None]:
    """Execute Python code in a notebook."""

def pytest_runtest_call(item) -> None:
    """Run notebook code written in Python."""

def nirx_snirf(request):
    """Return a (raw_nirx, raw_snirf) matched pair."""

def qt_windows_closed(request) -> Generator[None, None, None]:
    """Ensure that no new Qt windows are open after a test."""

def pytest_runtest_makereport(item, call) -> Generator[None, Incomplete, None]:
    """Stash the status of each item."""