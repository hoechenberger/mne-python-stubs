from ..fixes import rng_uniform as rng_uniform
from ..label import Label as Label
from ..source_estimate import (
    SourceEstimate as SourceEstimate,
    VolSourceEstimate as VolSourceEstimate,
)
from ..utils import (
    check_random_state as check_random_state,
    fill_doc as fill_doc,
    warn as warn,
)
from _typeshed import Incomplete

def select_source_in_label(
    src,
    label,
    random_state=None,
    location: str = "random",
    subject=None,
    subjects_dir=None,
    surf: str = "sphere",
):
    """Select source positions using a label.

    Parameters
    ----------
    src : list of dict
        The source space.
    label : Label
        The label.

    random_state : None | int | instance of ~numpy.random.RandomState
        A seed for the NumPy random number generator (RNG). If ``None`` (default),
        the seed will be  obtained from the operating system
        (see  `RandomState` for details), meaning it will most
        likely produce different output every time this function or method is run.
        To achieve reproducible results, pass a value here to explicitly initialize
        the RNG with a defined state.
    location : str
        The label location to choose. Can be 'random' (default) or 'center'
        to use `mne.Label.center_of_mass` (restricting to vertices
        both in the label and in the source space). Note that for 'center'
        mode the label values are used as weights.

        ✨ Added in version 0.13
    subject : str | None
        The subject the label is defined for.
        Only used with ``location='center'``.

        ✨ Added in version 0.13

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.

        ✨ Added in version 0.13
    surf : str
        The surface to use for Euclidean distance center of mass
        finding. The default here is "sphere", which finds the center
        of mass on the spherical surface to help avoid potential issues
        with cortical folding.

        ✨ Added in version 0.13

    Returns
    -------
    lh_vertno : list
        Selected source coefficients on the left hemisphere.
    rh_vertno : list
        Selected source coefficients on the right hemisphere.
    """
    ...

def simulate_sparse_stc(
    src,
    n_dipoles,
    times,
    data_fun=...,
    labels=None,
    random_state=None,
    location: str = "random",
    subject=None,
    subjects_dir=None,
    surf: str = "sphere",
):
    """Generate sparse (n_dipoles) sources time courses from data_fun.

    This function randomly selects ``n_dipoles`` vertices in the whole
    cortex or one single vertex (randomly in or in the center of) each
    label if ``labels is not None``. It uses ``data_fun`` to generate
    waveforms for each vertex.

    Parameters
    ----------
    src : instance of SourceSpaces
        The source space.
    n_dipoles : int
        Number of dipoles to simulate.
    times : array
        Time array.
    data_fun : callable
        Function to generate the waveforms. The default is a 100 nAm, 10 Hz
        sinusoid as ``1e-7 * np.sin(20 * pi * t)``. The function should take
        as input the array of time samples in seconds and return an array of
        the same length containing the time courses.
    labels : None | list of Label
        The labels. The default is None, otherwise its size must be n_dipoles.

    random_state : None | int | instance of ~numpy.random.RandomState
        A seed for the NumPy random number generator (RNG). If ``None`` (default),
        the seed will be  obtained from the operating system
        (see  `RandomState` for details), meaning it will most
        likely produce different output every time this function or method is run.
        To achieve reproducible results, pass a value here to explicitly initialize
        the RNG with a defined state.
    location : str
        The label location to choose. Can be ``'random'`` (default) or
        ``'center'`` to use `mne.Label.center_of_mass`. Note that for
        ``'center'`` mode the label values are used as weights.

        ✨ Added in version 0.13
    subject : str | None
        The subject the label is defined for.
        Only used with ``location='center'``.

        ✨ Added in version 0.13

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.

        ✨ Added in version 0.13
    surf : str
        The surface to use for Euclidean distance center of mass
        finding. The default here is "sphere", which finds the center
        of mass on the spherical surface to help avoid potential issues
        with cortical folding.

        ✨ Added in version 0.13

    Returns
    -------
    stc : SourceEstimate
        The generated source time courses.

    See Also
    --------
    simulate_raw
    simulate_evoked
    simulate_stc

    Notes
    -----
    ✨ Added in version 0.10.0
    """
    ...

def simulate_stc(
    src, labels, stc_data, tmin, tstep, value_fun=None, allow_overlap: bool = False
):
    """Simulate sources time courses from waveforms and labels.

    This function generates a source estimate with extended sources by
    filling the labels with the waveforms given in stc_data.

    Parameters
    ----------
    src : instance of SourceSpaces
        The source space.
    labels : list of Label
        The labels.
    stc_data : array, shape (n_labels, n_times)
        The waveforms.
    tmin : float
        The beginning of the timeseries.
    tstep : float
        The time step (1 / sampling frequency).
    value_fun : callable | None
        Function to apply to the label values to obtain the waveform
        scaling for each vertex in the label. If None (default), uniform
        scaling is used.
    allow_overlap : bool
        Allow overlapping labels or not. Default value is False.

        ✨ Added in version 0.18

    Returns
    -------
    stc : SourceEstimate
        The generated source time courses.

    See Also
    --------
    simulate_raw
    simulate_evoked
    simulate_sparse_stc
    """
    ...

class SourceSimulator:
    """Class to generate simulated Source Estimates.

    Parameters
    ----------
    src : instance of SourceSpaces
        Source space.
    tstep : float
        Time step between successive samples in data. Default is 0.001 s.
    duration : float | None
        Time interval during which the simulation takes place in seconds.
        If None, it is computed using existing events and waveform lengths.
    first_samp : int
        First sample from which the simulation takes place, as an integer.
        Comparable to the `first_samp` property of `Raw` objects.
        Default is 0.

    Attributes
    ----------
    duration : float
        The duration of the simulation in seconds.
    n_times : int
        The number of time samples of the simulation.
    """

    first_samp: Incomplete

    def __init__(
        self, src, tstep: float = 0.001, duration=None, first_samp: int = 0
    ) -> None: ...
    @property
    def duration(self):
        """Duration of the simulation in same units as tstep."""
        ...

    @property
    def n_times(self):
        """Number of time samples in the simulation."""
        ...

    @property
    def last_samp(self): ...
    def add_data(self, label, waveform, events) -> None:
        """Add data to the simulation.

        Data should be added in the form of a triplet of
        Label (Where) - Waveform(s) (What) - Event(s) (When)

        Parameters
        ----------
        label : instance of Label
            The label (as created for example by mne.read_label). If the label
            does not match any sources in the SourceEstimate, a ValueError is
            raised.
        waveform : array, shape (n_times,) or (n_events, n_times) | list
            The waveform(s) describing the activity on the label vertices.
            If list, it must have the same length as events.
        events : array of int, shape (n_events, 3)
            Events associated to the waveform(s) to specify when the activity
            should occur.
        """
        ...

    def get_stim_channel(self, start_sample: int = 0, stop_sample=None):
        """Get the stim channel from the provided data.

        Returns the stim channel data according to the simulation parameters
        which should be added through the add_data method. If both start_sample
        and stop_sample are not specified, the entire duration is used.

        Parameters
        ----------
        start_sample : int
            First sample in chunk. Default is the value of the ``first_samp``
            attribute.
        stop_sample : int | None
            The final sample of the returned stc. If None, then all samples
            from start_sample onward are returned.

        Returns
        -------
        stim_data : ndarray of int, shape (n_samples,)
            The stimulation channel data.
        """
        ...

    def get_stc(self, start_sample=None, stop_sample=None):
        """Simulate a SourceEstimate from the provided data.

        Returns a SourceEstimate object constructed according to the simulation
        parameters which should be added through function add_data. If both
        start_sample and stop_sample are not specified, the entire duration is
        used.

        Parameters
        ----------
        start_sample : int | None
            First sample in chunk. If ``None`` the value of the ``first_samp``
            attribute is used. Defaults to ``None``.
        stop_sample : int | None
            The final sample of the returned STC. If ``None``, then all samples
            past ``start_sample`` are returned.

        Returns
        -------
        stc : SourceEstimate object
            The generated source time courses.
        """
        ...

    def __iter__(self):
        """Iterate over 1 second STCs."""
        ...
