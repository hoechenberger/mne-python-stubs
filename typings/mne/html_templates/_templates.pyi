class _RenderWrap:
    """Class that allows functools.partial-like wrapping of jinja2 Template.render()."""

    def __init__(self, template, **kwargs) -> None:
        ...

    def render(self, *args, **kwargs):
        ...