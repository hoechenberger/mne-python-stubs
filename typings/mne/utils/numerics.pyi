import numpy as np
from ..fixes import (
    has_numba as has_numba,
    jit as jit,
    stable_cumsum as stable_cumsum,
    svd_flip as svd_flip,
)
from ._logging import logger as logger, warn as warn
from .check import check_random_state as check_random_state
from .docs import fill_doc as fill_doc
from _typeshed import Incomplete
from collections.abc import Generator

def split_list(v, n, idx: bool = False) -> Generator[Incomplete, None, None]:
    """## Split list in n (approx) equal pieces, possibly giving indices."""
    ...

def array_split_idx(ary, indices_or_sections, axis: int = 0, n_per_split: int = 1):
    """## Do what numpy.array_split does, but add indices."""
    ...

def create_chunks(sequence, size):
    """## Generate chunks from a sequence.

    -----
    ### 🛠️ Parameters

    #### `sequence : iterable`
        Any iterable object
    #### `size : int`
        The chunksize to be returned
    """
    ...

def sum_squared(X):
    """## Compute norm of an array.

    -----
    ### 🛠️ Parameters

    X : array
        Data whose norm must be found.

    -----
    ### ⏎ Returns

    #### `value : float`
        Sum of squares of the input array X.
    """
    ...

def compute_corr(x, y):
    """## Compute pearson correlations between a vector and a matrix."""
    ...

def random_permutation(n_samples, random_state=None):
    """## Emulate the randperm matlab function.

    It returns a vector containing a random permutation of the
    integers between 0 and n_samples-1. It returns the same random numbers
    than randperm matlab function whenever the random_state is the same
    as the matlab's random seed.

    This function is useful for comparing against matlab scripts
    which use the randperm function.

    Note: the randperm(n_samples) matlab function generates a random
    sequence between 1 and n_samples, whereas
    random_permutation(n_samples, random_state) function generates
    a random sequence between 0 and n_samples-1, that is:
    randperm(n_samples) = random_permutation(n_samples, random_state) - 1

    -----
    ### 🛠️ Parameters

    #### `n_samples : int`
        End point of the sequence to be permuted (excluded, i.e., the end point
        is equal to n_samples-1)

    #### `random_state : None | int | instance of ~numpy.random.RandomState`
        A seed for the NumPy random number generator (RNG). If ``None`` (default),
        the seed will be  obtained from the operating system
        (see  `numpy.random.RandomState` for details), meaning it will most
        likely produce different output every time this function or method is run.
        To achieve reproducible results, pass a value here to explicitly initialize
        the RNG with a defined state.

    -----
    ### ⏎ Returns

    #### `randperm : ndarray, int`
        Randomly permuted sequence between 0 and n-1.
    """
    ...

def hashfunc(fname, block_size: int = 1048576, hash_type: str = "md5"):
    """## Calculate the hash for a file.

    -----
    ### 🛠️ Parameters

    #### `fname : str`
        Filename.
    #### `block_size : int`
        Block size to use when reading.

    -----
    ### ⏎ Returns

    #### `hash_ : str`
        The hexadecimal digest of the hash.
    """
    ...

def create_slices(start, stop, step=None, length: int = 1):
    """## Generate slices of time indexes.

    -----
    ### 🛠️ Parameters

    #### `start : int`
        Index where first slice should start.
    #### `stop : int`
        Index where last slice should maximally end.
    #### `length : int`
        Number of time sample included in a given slice.
    step: int | None
        Number of time samples separating two slices.
        If step = None, step = length.

    -----
    ### ⏎ Returns

    #### `slices : list`
        List of slice objects.
    """
    ...

def grand_average(all_inst, interpolate_bads: bool = True, drop_bads: bool = True):
    """## Make grand average of a list of Evoked or AverageTFR data.

    For `mne.Evoked` data, the function interpolates bad channels based
    on the ``interpolate_bads`` parameter. If ``interpolate_bads`` is True,
    the grand average file will contain good channels and the bad channels
    interpolated from the good MEG/EEG channels.
    For `mne.time_frequency.AverageTFR` data, the function takes the
    subset of channels not marked as bad in any of the instances.

    The ``grand_average.nave`` attribute will be equal to the number
    of evoked datasets used to calculate the grand average.

    ### 💡 Note A grand average evoked should not be used for source
              localization.

    -----
    ### 🛠️ Parameters

    #### `all_inst : list of Evoked or AverageTFR`
        The evoked datasets.
    #### `interpolate_bads : bool`
        If True, bad MEG and EEG channels are interpolated. Ignored for
        AverageTFR.
    #### `drop_bads : bool`
        If True, drop all bad channels marked as bad in any data set.
        If neither interpolate_bads nor drop_bads is True, in the output file,
        every channel marked as bad in at least one of the input files will be
        marked as bad, but no interpolation or dropping will be performed.

    -----
    ### ⏎ Returns

    #### `grand_average : Evoked | AverageTFR`
        The grand average data. Same type as input.

    -----
    ### 📖 Notes

    ✨ Added in version 0.11.0
    """
    ...

class _HashableNdarray(np.ndarray):
    def __hash__(self): ...
    def __eq__(self, other): ...

def object_hash(x, h=None):
    """## Hash a reasonable python object.

    -----
    ### 🛠️ Parameters

    #### `x : object`
        Object to hash. Can be anything comprised of nested versions of:
        {dict, list, tuple, ndarray, str, bytes, float, int, None}.
    #### `h : hashlib HASH object | None`
        Optional, object to add the hash to. None creates an MD5 hash.

    -----
    ### ⏎ Returns

    #### `digest : int`
        The digest resulting from the hash.
    """
    ...

def object_size(x, memo=None):
    """## Estimate the size of a reasonable python object.

    -----
    ### 🛠️ Parameters

    #### `x : object`
        Object to approximate the size of.
        Can be anything comprised of nested versions of:
        {dict, list, tuple, ndarray, str, bytes, float, int, None}.
    #### `memo : dict | None`
        The memodict.

    -----
    ### ⏎ Returns

    #### `size : int`
        The estimated size in bytes of the object.
    """
    ...

def object_diff(a, b, pre: str = "", *, allclose: bool = False):
    """## Compute all differences between two python variables.

    -----
    ### 🛠️ Parameters

    #### `a : object`
        Currently supported: class, dict, list, tuple, ndarray,
        int, str, bytes, float, StringIO, BytesIO.
    #### `b : object`
        Must be same type as ``a``.
    #### `pre : str`
        String to prepend to each line.
    #### `allclose : bool`
        If True (default False), use assert_allclose.

    -----
    ### ⏎ Returns

    #### `diffs : str`
        A string representation of the differences.
    """
    ...

class _PCA:
    """## Principal component analysis (PCA)."""

    n_components: Incomplete
    whiten: Incomplete

    def __init__(self, n_components=None, whiten: bool = False) -> None: ...
    def fit_transform(self, X, y=None): ...

class _ReuseCycle:
    """## Cycle over a variable, preferring to reuse earlier indices.

    Requires the values in ``x`` to be hashable and unique. This holds
    nicely for matplotlib's color cycle, which gives HTML hex color strings.
    """

    indices: Incomplete
    popped: Incomplete
    x: Incomplete

    def __init__(self, x) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    def restore(self, val) -> None: ...
