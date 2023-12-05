from _typeshed import Incomplete

class Bunch(dict):
    """Dictionary-like object that exposes its keys as attributes."""

    __dict__: Incomplete

    def __init__(self, **kwargs) -> None: ...

class BunchConst(Bunch):
    """Class to prevent us from re-defining constants (DRY)."""

    def __setitem__(self, key, val) -> None: ...

class BunchConstNamed(BunchConst):
    """Class to provide nice __repr__ for our integer constants.

    Only supports string keys and int or float values.
    """

    def __setattr__(self, attr, val) -> None: ...

class _Named:
    """Provide shared methods for giving named-representation subclasses."""

    def __new__(cls, name, val): ...
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...
    def __getnewargs__(self): ...

class NamedInt(_Named, int):
    """Int with a name in __repr__."""

    ...

class NamedFloat(_Named, float):
    """Float with a name in __repr__."""

    ...
