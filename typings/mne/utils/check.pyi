from ..defaults import HEAD_SIZE_DEFAULT as HEAD_SIZE_DEFAULT
from ._logging import logger as logger, warn as warn
from _typeshed import Incomplete

def check_fname(fname, filetype, endings, endings_err=()) -> None:
    """### Enforce MNE filename conventions.

    ### 🛠️ Parameters
    ----------
    fname : str
        Name of the file.
    filetype : str
        Type of file. e.g., ICA, Epochs etc.
    endings : tuple
        Acceptable endings for the filename.
    endings_err : tuple
        Obligatory possible endings for the filename.
    """
    ...

def check_version(
    library,
    min_version: str = "0.0",
    *,
    strip: bool = True,
    return_version: bool = False,
):
    """### Check minimum library version required.

    ### 🛠️ Parameters
    ----------
    library : str
        The library name to import. Must have a ``__version__`` property.
    min_version : str
        The minimum version string. Anything that matches
        ``'(\\d+ | [a-z]+ | \\.)'``. Can also be empty to skip version
        check (just check for library presence).
    strip : bool
        If True (default), then PEP440 development markers like ``.devN``
        will be stripped from the version. This makes it so that
        ``check_version('mne', '1.1')`` will be ``True`` even when on version
        ``'1.1.dev0'`` (prerelease/dev version). This option is provided for
        backward compatibility with the behavior of ``LooseVersion``, and
        diverges from how modern parsing in ``packaging.version.parse`` works.

        ✨ Added in vesion 1.0
    return_version : bool
        If True (default False), also return the version (can be None if the
        library is missing).

        ✨ Added in vesion 1.0

    ### ⏎ Returns
    -------
    ok : bool
        True if the library exists with at least the specified version.
    version : str | None
        The version. Only returned when ``return_version=True``.
    """
    ...

def check_random_state(seed):
    """### Turn seed into a numpy.random.mtrand.RandomState instance.

    If seed is None, return the RandomState singleton used by np.random.mtrand.
    If seed is an int, return a new RandomState instance seeded with seed.
    If seed is already a RandomState instance, return it.
    Otherwise raise ValueError.
    """
    ...

class _IntLike:
    @classmethod
    def __instancecheck__(cls, other): ...

int_like: Incomplete
path_like: Incomplete

class _Callable:
    @classmethod
    def __instancecheck__(cls, other): ...
