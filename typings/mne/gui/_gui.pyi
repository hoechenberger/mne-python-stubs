from ..utils import get_config as get_config

def coregistration(
    *,
    width=None,
    height=None,
    inst=None,
    subject=None,
    subjects_dir=None,
    head_opacity=None,
    head_high_res=None,
    trans=None,
    orient_to_surface=None,
    scale_by_distance=None,
    mark_inside=None,
    interaction=None,
    fullscreen=None,
    show: bool = True,
    block: bool = False,
    verbose=None,
):
    """Coregister an MRI with a subject's head shape.

    The GUI can be launched through the command line interface:

    .. code-block::  bash

        $ mne coreg

    or using a python interpreter as shown in `tut-source-alignment`.

    Parameters
    ----------
    width : int | None
        Specify the width for window (in logical pixels).
        Default is None, which uses ``MNE_COREG_WINDOW_WIDTH`` config value
        (which defaults to 800).
    height : int | None
        Specify a height for window (in logical pixels).
        Default is None, which uses ``MNE_COREG_WINDOW_WIDTH`` config value
        (which defaults to 400).
    inst : None | str
        Path to an instance file containing the digitizer data. Compatible for
        Raw, Epochs, and Evoked files.
    subject : None | str
        Name of the mri subject.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    head_opacity : float | None
        The opacity of the head surface in the range [0., 1.].
        Default is None, which uses ``MNE_COREG_HEAD_OPACITY`` config value
        (which defaults to 1.).
    head_high_res : bool | None
        Use a high resolution head surface.
        Default is None, which uses ``MNE_COREG_HEAD_HIGH_RES`` config value
        (which defaults to True).
    trans : path-like | None
        The transform file to use.
    orient_to_surface : bool | None
        If True (default), orient EEG electrode and head shape points
        to the head surface.

        ✨ Added in version 0.16
    scale_by_distance : bool | None
        If True (default), scale the digitization points by their
        distance from the scalp surface.

        ✨ Added in version 0.16
    mark_inside : bool | None
        If True (default), mark points inside the head surface in a
        different color.

        ✨ Added in version 0.16

    interaction : 'trackball' | 'terrain' | None
        How interactions with the scene via an input device (e.g., mouse or
        trackpad) modify the camera position. If ``'terrain'``, one axis is
        fixed, enabling "turntable-style" rotations. If ``'trackball'``,
        movement along all axes is possible, which provides more freedom of
        movement, but you may incidentally perform unintentional rotations along
        some axes.
        If ``None``, the setting stored in the MNE-Python configuration file is
        used.
        Defaults to ``'terrain'``.

        ✨ Added in version 0.16
        🎭 Changed in version 1.0
           Default interaction mode if ``None`` and no config setting found
           changed from ``'trackball'`` to ``'terrain'``.

    fullscreen : bool
        Whether to start in fullscreen (``True``) or windowed mode
        (``False``).
        Default is None, which uses ``MNE_COREG_FULLSCREEN`` config value
        (which defaults to False).

        ✨ Added in version 1.1
    show : bool
        Show the GUI if True.
    block : bool
        Whether to halt program execution until the figure is closed.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    frame : instance of CoregistrationUI
        The coregistration frame.

    Notes
    -----
    Many parameters (e.g., ``head_opacity``) take None as a parameter,
    which means that the default will be read from the MNE-Python
    configuration file (which gets saved when exiting).

    Step by step instructions for the coregistrations are shown below:

    .. youtube:: ALV5qqMHLlQ
    """
    ...

class _GUIScraper:
    """Scrape GUI outputs."""

    def __call__(self, block, block_vars, gallery_conf): ...
