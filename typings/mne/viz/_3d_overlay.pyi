from ..utils import logger as logger

class _Overlay:
    def __init__(self, scalars, colormap, rng, opacity, name) -> None: ...
    def to_colors(self): ...

class _LayeredMesh:
    def __init__(self, renderer, vertices, triangles, normals) -> None: ...
    def map(self) -> None: ...
    def add_overlay(self, scalars, colormap, rng, opacity, name) -> None: ...
    def remove_overlay(self, names) -> None: ...
    def update(self, colors=None) -> None: ...
    def update_overlay(
        self, name, scalars=None, colormap=None, opacity=None, rng=None
    ) -> None: ...
