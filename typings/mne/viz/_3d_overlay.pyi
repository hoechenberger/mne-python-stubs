from ..utils import logger as logger
from _typeshed import Incomplete

class _Overlay:

    def __init__(self, scalars, colormap, rng, opacity, name) -> None:
        ...

    def to_colors(self):
        ...

class _LayeredMesh:

    def __init__(self, renderer, vertices, triangles, normals) -> None:
        ...

    def map(self) -> None:
        ...

    def add_overlay(self, scalars, colormap, rng, opacity, name) -> None:
        ...

    def remove_overlay(self, names) -> None:
        ...

    def update(self, colors: Incomplete | None=...) -> None:
        ...

    def update_overlay(self, name, scalars: Incomplete | None=..., colormap: Incomplete | None=..., opacity: Incomplete | None=..., rng: Incomplete | None=...) -> None:
        ...