from ..defaults import HEAD_SIZE_DEFAULT as HEAD_SIZE_DEFAULT
from ._bunch import BunchConst as BunchConst
from _typeshed import Incomplete

docdict: Incomplete
mem: str
comb: str
st: Incomplete
tf: Incomplete
nogroups: Incomplete
groups: Incomplete
applyfun_summary: str
applyfun_preload: str
chwise: str
applyfun_fun_base: str
datetime: str
multiindex: str
raw: Incomplete
epo: Incomplete
evk: Incomplete
ch_type: str
stc: Incomplete
spe: Incomplete
reminder: Incomplete
reminder_nostr: Incomplete
noref: Incomplete
picks_base: Incomplete
picks_base_notypes: Incomplete
f_test: Incomplete
t_test: Incomplete
docdict_indented: Incomplete

def fill_doc(f):
    """## Fill a docstring with docdict entries.

    -----
    ### 🛠️ Parameters

    #### `f : callable`
        The function to fill the docstring of. Will be modified in place.

    -----
    ### ⏎ Returns

    #### `f : callable`
        The function, potentially with an updated ``__doc__``.
    """
    ...

def copy_doc(source):
    """## Copy the docstring from another function (decorator).

    The docstring of the source function is prepepended to the docstring of the
    function wrapped by this decorator.

    This is useful when inheriting from a class and overloading a method. This
    decorator can be used to copy the docstring of the original method.

    -----
    ### 🛠️ Parameters

    #### `source : function`
        Function to copy the docstring from

    -----
    ### ⏎ Returns

    #### `wrapper : function`
        The decorated function

    -----
    ### 🖥️ Examples

    >>> class A:
    ...     def m1():
    ...         '''Docstring for m1'''
    ...         pass
    >>> class B (A):
    ...     @copy_doc(A.m1)
    ...     def m1():
    ...         ''' this gets appended'''
    ...         pass
    >>> print(B.m1.__doc__)
    Docstring for m1 this gets appended
    """
    ...

def copy_function_doc_to_method_doc(source):
    """## Use the docstring from a function as docstring for a method.

    The docstring of the source function is prepepended to the docstring of the
    function wrapped by this decorator. Additionally, the first parameter
    specified in the docstring of the source function is removed in the new
    docstring.

    This decorator is useful when implementing a method that just calls a
    function.  This pattern is prevalent in for example the plotting functions
    of MNE.

    -----
    ### 🛠️ Parameters

    #### `source : function`
        Function to copy the docstring from.

    -----
    ### ⏎ Returns

    #### `wrapper : function`
        The decorated method.

    -----
    ### 📖 Notes

    The parsing performed is very basic and will break easily on docstrings
    that are not formatted exactly according to the ``numpydoc`` standard.
    Always inspect the resulting docstring when using this decorator.

    -----
    ### 🖥️ Examples

    >>> def plot_function(object, a, b):
    ...     '''Docstring for plotting function.
    ...
    ...     Parameters
    ...     ----------
    ...     object : instance of object
    ...         The object to plot
    ...     a : int
    ...         Some parameter
    ...     b : int
    ...         Some parameter
    ...     '''
    ...     pass
    ...
    >>> class A:
    ...     @copy_function_doc_to_method_doc(plot_function)
    ...     def plot(self, a, b):
    ...         '''
    ...         Notes
    ...         -----
    ...         ✨ Added in version 0.13.0
    ...         '''
    ...         plot_function(self, a, b)
    >>> print(A.plot.__doc__)
    Docstring for plotting function.
    <BLANKLINE>
        -----
        ### 🛠️ Parameters

        #### `a : int`
            Some parameter
        #### `b : int`
            Some parameter
    <BLANKLINE>
            -----
            ### 📖 Notes

            ✨ Added in version 0.13.0
    <BLANKLINE>
    """
    ...

def copy_base_doc_to_subclass_doc(subclass):
    """## Use the docstring from a parent class methods in derived class.

    The docstring of a parent class method is prepended to the
    docstring of the method of the class wrapped by this decorator.

    -----
    ### 🛠️ Parameters

    #### `subclass : wrapped class`
        Class to copy the docstring to.

    -----
    ### ⏎ Returns

    #### `subclass : Derived class`
        The decorated class with copied docstrings.
    """
    ...

def linkcode_resolve(domain, info):
    """## Determine the URL corresponding to a Python object.

    -----
    ### 🛠️ Parameters

    #### `domain : str`
        Only useful when 'py'.
    #### `info : dict`
        With keys "module" and "fullname".

    -----
    ### ⏎ Returns

    #### `url : str`
        The code URL.

    -----
    ### 📖 Notes

    This has been adapted to deal with our "verbose" decorator.

    Adapted from SciPy (doc/source/conf.py).
    """
    ...

def open_docs(kind=None, version=None) -> None:
    """## Launch a new web browser tab with the MNE documentation.

    -----
    ### 🛠️ Parameters

    #### `kind : str | None`
        Can be "api" (default), "tutorials", or "examples".
        The default can be changed by setting the configuration value
        MNE_DOCS_KIND.
    #### `version : str | None`
        Can be "stable" (default) or "dev".
        The default can be changed by setting the configuration value
        MNE_DOCS_VERSION.
    """
    ...

class _decorator:
    """## Inject code or modify the docstring of a class, method, or function."""

    kind: Incomplete
    extra: Incomplete
    msg: Incomplete

    def __init__(self, extra) -> None: ...
    def __call__(self, obj):
        """## Call.

        -----
        ### 🛠️ Parameters

        #### `obj : object`
            Object to call.

        -----
        ### ⏎ Returns

        #### `obj : object`
            The modified object.
        """
        ...

class deprecated(_decorator):
    """## Mark a function, class, or method as deprecated (decorator).

    Originally adapted from sklearn and
    http://wiki.python.org/moin/PythonDecoratorLibrary, then modified to make
    arguments populate properly following our verbose decorator methods based
    on decorator.

    -----
    ### 🛠️ Parameters

    #### `extra : str`
        Extra information beyond just saying the class/function/method is
        deprecated. Should be a complete sentence (trailing period will be
        added automatically). Will be included in FutureWarning messages
        and in a sphinx warning box in the docstring.
    """

    ...

def deprecated_alias(dep_name, func, removed_in=None) -> None:
    """## Inject a deprecated alias into the namespace."""
    ...

class legacy(_decorator):
    """## Mark a function, class, or method as legacy (decorator).

    -----
    ### 🛠️ Parameters

    #### `alt : str`
        Description of the alternate, preferred way to achieve a comparable
        result.
    #### `extra : str`
        Extra information beyond just saying the class/function/method is
        legacy. Should be a complete sentence (trailing period will be
        added automatically). Will be included in logger.info messages
        and in a sphinx warning box in the docstring.
    """

    def __init__(self, alt, extra: str = "") -> None: ...
