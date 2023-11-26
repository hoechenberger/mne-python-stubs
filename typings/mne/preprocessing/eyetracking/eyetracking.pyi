from ..._fiff.constants import FIFF as FIFF

def set_channel_types_eyetrack(inst, mapping):
    """Define sensor type for eyetrack channels.

    This function can set all eye tracking specific information:
    channel type, unit, eye (and x/y component; only for gaze channels)

    Supported channel types:
    ``'eyegaze'`` and ``'pupil'``

    Supported units:
    ``'au'``, ``'px'``, ``'deg'``, ``'rad'`` (for eyegaze)
    ``'au'``, ``'mm'``, ``'m'`` (for pupil)

    Parameters
    ----------
    inst : instance of Raw, Epochs, or Evoked
        The data instance.
    mapping : dict
        A dictionary mapping a channel to a list/tuple including
        channel type, unit, eye, [and x/y component] (all as str),  e.g.,
        ``{'l_x': ('eyegaze', 'deg', 'left', 'x')}`` or
        ``{'r_pupil': ('pupil', 'au', 'right')}``.

    Returns
    -------
    inst : instance of Raw | Epochs | Evoked
        The instance, modified in place.

    Notes
    -----
    ``inst.set_channel_types()`` to ``'eyegaze'`` or ``'pupil'``
    works as well, but cannot correctly set unit, eye and x/y component.

    Data will be stored in SI units:
    if your data comes in ``deg`` (visual angle) it will be converted to
    ``rad``, if it is in ``mm`` it will be converted to ``m``.
    """
    ...
