from ...utils import get_subjects_dir as get_subjects_dir

def fetch_infant_template(age, subjects_dir=..., *, verbose=...):
    """## 🧠 Fetch and update an infant MRI template.

    -----
    ### 🛠️ Parameters

    #### `age : str`
        Age to download. Can be one of ``{'2wk', '1mo', '2mo', '3mo', '4.5mo',
        '6mo', '7.5mo', '9mo', '10.5mo', '12mo', '15mo', '18mo', '2yr'}``.
    #### `subjects_dir : str | None`
        The path to download the template data to.

    #### `verbose : bool | str | int | None`
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the `logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    -----
    ### ⏎ Returns

    #### `subject : str`
        The standard subject name, e.g. ``ANTS4-5Month3T``.

    -----
    ### 📖 Notes

    If you use these templates in your work, please cite
    :footcite:`OReillyEtAl2021` and :footcite:`RichardsEtAl2016`.

    ✨ Added in vesion 0.23

    References
    ----------
    .. footbibliography::
    """
    ...
