from ._fiff.constants import FIFF as FIFF
from ._fiff.open import fiff_open as fiff_open
from ._fiff.tag import read_tag as read_tag
from ._fiff.tree import dir_tree_find as dir_tree_find
from ._fiff.write import (
    end_block as end_block,
    start_and_end_file as start_and_end_file,
    start_block as start_block,
    write_double as write_double,
    write_float as write_float,
    write_name_list_sanitized as write_name_list_sanitized,
    write_string as write_string,
)
from .utils import (
    check_fname as check_fname,
    fill_doc as fill_doc,
    int_like as int_like,
    logger as logger,
    warn as warn,
)
from _typeshed import Incomplete

class Annotations:
    """Rename annotation description(s). Operates inplace.

    Parameters
    ----------
    mapping : dict
        A dictionary mapping the old description to a new description,
        e.g. {'1.0' : 'Control', '2.0' : 'Stimulus'}.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    self : mne.Annotations
        The modified Annotations object.

    Notes
    -----
    .. versionadded:: 0.24.0
    """

    def __init__(
        self, onset, duration, description, orig_time=..., ch_names=...
    ) -> None: ...
    @property
    def orig_time(self):
        """The time base of the Annotations."""
    def __eq__(self, other):
        """Compare to another Annotations instance."""
    def __len__(self) -> int:
        """Return the number of annotations.

        Returns
        -------
        n_annot : int
            The number of annotations.
        """
    def __add__(self, other):
        """Add (concatencate) two Annotation objects."""
    def __iadd__(self, other):
        """Add (concatencate) two Annotation objects in-place.

        Both annotations must have the same orig_time
        """
    def __iter__(self):
        """Iterate over the annotations."""
    def __getitem__(self, key, *, with_ch_names=...):
        """Propagate indexing and slicing to the underlying numpy structure."""
    onset: Incomplete
    duration: Incomplete
    description: Incomplete
    ch_names: Incomplete

    def append(self, onset, duration, description, ch_names=...):
        """Add an annotated segment. Operates inplace.

        Parameters
        ----------
        onset : float | array-like
            Annotation time onset from the beginning of the recording in
            seconds.
        duration : float | array-like
            Duration of the annotation in seconds.
        description : str | array-like
            Description for the annotation. To reject epochs, use description
            starting with keyword 'bad'.

        ch_names : list | None
            List of lists of channel names associated with the annotations.
            Empty entries are assumed to be associated with no specific channel,
            i.e., with all channels or with the time slice itself. None (default) is
            the same as passing all empty lists. For example, this creates three
            annotations, associating the first with the time interval itself, the
            second with two channels, and the third with a single channel::

                Annotations(onset=[0, 3, 10], duration=[1, 0.25, 0.5],
                            description=['Start', 'BAD_flux', 'BAD_noise'],
                            ch_names=[[], ['MEG0111', 'MEG2563'], ['MEG1443']])

            .. versionadded:: 0.23

        Returns
        -------
        self : mne.Annotations
            The modified Annotations object.

        Notes
        -----
        The array-like support for arguments allows this to be used similarly
        to not only ``list.append``, but also
        `list.extend <https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types>`__.
        """
    def copy(self):
        """Return a copy of the Annotations.

        Returns
        -------
        inst : instance of Annotations
            A copy of the object.
        """
    def delete(self, idx) -> None:
        """Remove an annotation. Operates inplace.

        Parameters
        ----------
        idx : int | array-like of int
            Index of the annotation to remove. Can be array-like to
            remove multiple indices.
        """
    def to_data_frame(self):
        """Export annotations in tabular structure as a pandas DataFrame.

        Returns
        -------
        result : pandas.DataFrame
            Returns a pandas DataFrame with onset, duration, and
            description columns. A column named ch_names is added if any
            annotations are channel-specific.
        """
    def count(self):
        """Count annotations.

        Returns
        -------
        counts : dict
            A dictionary containing unique annotation descriptions as keys with their
            counts as values.
        """
    def save(self, fname, *, overwrite: bool = ..., verbose=...) -> None:
        """Save annotations to FIF, CSV or TXT.

        Typically annotations get saved in the FIF file for raw data
        (e.g., as ``raw.annotations``), but this offers the possibility
        to also save them to disk separately in different file formats
        which are easier to share between packages.

        Parameters
        ----------
        fname : path-like
            The filename to use.

        overwrite : bool
            If True (default False), overwrite the destination file if it
            exists.

            .. versionadded:: 0.23

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Notes
        -----
        The format of the information stored in the saved annotation objects
        depends on the chosen file format. :file:`.csv` files store the onset
        as timestamps (e.g., ``2002-12-03 19:01:56.676071``),
        whereas :file:`.txt` files store onset as seconds since start of the
        recording (e.g., ``45.95597082905339``).
        """
    def crop(
        self,
        tmin=...,
        tmax=...,
        emit_warning: bool = ...,
        use_orig_time: bool = ...,
        verbose=...,
    ):
        """Remove all annotation that are outside of [tmin, tmax].

        The method operates inplace.

        Parameters
        ----------
        tmin : float | datetime | None
            Start time of selection in seconds.
        tmax : float | datetime | None
            End time of selection in seconds.
        emit_warning : bool
            Whether to emit warnings when limiting or omitting annotations.
            Defaults to False.
        use_orig_time : bool
            Whether to use orig_time as an offset.
            Defaults to True.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        self : instance of Annotations
            The cropped Annotations object.
        """
    def set_durations(self, mapping, verbose=...):
        """Set annotation duration(s). Operates inplace.

        Parameters
        ----------
        mapping : dict | float
            A dictionary mapping the annotation description to a duration in
            seconds e.g. ``{'ShortStimulus' : 3, 'LongStimulus' : 12}``.
            Alternatively, if a number is provided, then all annotations
            durations are set to the single provided value.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        self : mne.Annotations
            The modified Annotations object.

        Notes
        -----
        .. versionadded:: 0.24.0
        """
    def rename(self, mapping, verbose=...):
        """Rename annotation description(s). Operates inplace.

        Parameters
        ----------
        mapping : dict
            A dictionary mapping the old description to a new description,
            e.g. {'1.0' : 'Control', '2.0' : 'Stimulus'}.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        self : mne.Annotations
            The modified Annotations object.

        Notes
        -----
        .. versionadded:: 0.24.0
        """

class EpochAnnotationsMixin:
    """Add raw annotations into the Epochs metadata data frame.

    Adds three columns to the ``metadata`` consisting of a list
    in each row:
    - ``annot_onset``: the onset of each Annotation within
    the Epoch relative to the start time of the Epoch (in seconds).
    - ``annot_duration``: the duration of each Annotation
    within the Epoch in seconds.
    - ``annot_description``: the free-form text description of each
    Annotation.

    Parameters
    ----------
    overwrite : bool
        Whether to overwrite existing columns in metadata or not.
        Default is False.

    Returns
    -------
    self : instance of Epochs
        The modified instance (instance is also modified inplace).

    Notes
    -----
    .. versionadded:: 1.0
    """

    @property
    def annotations(self): ...
    def set_annotations(self, annotations, on_missing: str = ..., *, verbose=...):
        """Setter for Epoch annotations from Raw.

        This method does not handle offsetting the times based
        on first_samp or measurement dates, since that is expected
        to occur in Raw.set_annotations().

        Parameters
        ----------
        annotations : instance of mne.Annotations | None
            Annotations to set.

        on_missing : 'raise' | 'warn' | 'ignore'
            Can be ``'raise'`` (default) to raise an error, ``'warn'`` to emit a
            warning, or ``'ignore'`` to ignore when entries in ch_names are not present in the raw instance.

            .. versionadded:: 0.23.0

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        self : instance of Epochs
            The epochs object with annotations.

        Notes
        -----
        Annotation onsets and offsets are stored as time in seconds (not as
        sample numbers).

        If you have an ``-epo.fif`` file saved to disk created before 1.0,
        annotations can be added correctly only if no decimation or
        resampling was performed. We thus suggest to regenerate your
        :class:`mne.Epochs` from raw and re-save to disk with 1.0+ if you
        want to safely work with :class:mne.Annotations` in epochs.

        Since this method does not handle offsetting the times based
        on first_samp or measurement dates, the recommended way to add
        Annotations is::

            raw.set_annotations(annotations)
            annotations = raw.annotations
            epochs.set_annotations(annotations)

        .. versionadded:: 1.0
        """
    def get_annotations_per_epoch(self):
        """Get a list of annotations that occur during each epoch.

        Returns
        -------
        epoch_annots : list
            A list of lists (with length equal to number of epochs) where each
            inner list contains any annotations that overlap the corresponding
            epoch. Annotations are stored as a :class:`tuple` of onset,
            duration, description (not as a :class:mne.Annotations` object),
            where the onset is now relative to time=0 of the epoch, rather than
            time=0 of the original continuous (raw) data.
        """
    metadata: Incomplete

    def add_annotations_to_metadata(self, overwrite: bool = ...):
        """Add raw annotations into the Epochs metadata data frame.

        Adds three columns to the ``metadata`` consisting of a list
        in each row:
        - ``annot_onset``: the onset of each Annotation within
        the Epoch relative to the start time of the Epoch (in seconds).
        - ``annot_duration``: the duration of each Annotation
        within the Epoch in seconds.
        - ``annot_description``: the free-form text description of each
        Annotation.

        Parameters
        ----------
        overwrite : bool
            Whether to overwrite existing columns in metadata or not.
            Default is False.

        Returns
        -------
        self : instance of Epochs
            The modified instance (instance is also modified inplace).

        Notes
        -----
        .. versionadded:: 1.0
        """

def read_annotations(fname, sfreq: str = ..., uint16_codec=..., encoding: str = ...):
    """Read annotations from a file.

    This function reads a ``.fif``, ``.fif.gz``, ``.vmrk``, ``.amrk``,
    ``.edf``, ``.txt``, ``.csv``, ``.cnt``, ``.cef``, or ``.set`` file and
    makes an :class:`mne.Annotations` object.

    Parameters
    ----------
    fname : path-like
        The filename.
    sfreq : float | ``'auto'``
        The sampling frequency in the file. This parameter is necessary for
        \\*.vmrk, \\*.amrk, and \\*.cef files as Annotations are expressed in
        seconds and \\*.vmrk/\\*.amrk/\\*.cef files are in samples. For any other
        file format, ``sfreq`` is omitted. If set to 'auto' then the ``sfreq``
        is taken from the respective info file of the same name with according
        file extension (\\*.vhdr/\\*.ahdr for brainvision; \\*.dap for Curry 7;
        \\*.cdt.dpa for Curry 8). So data.vmrk/amrk looks for sfreq in
        data.vhdr/ahdr, data.cef looks in data.dap and data.cdt.cef looks in
        data.cdt.dpa.
    uint16_codec : str | None
        This parameter is only used in EEGLAB (\\*.set) and omitted otherwise.
        If your \\*.set file contains non-ascii characters, sometimes reading
        it may fail and give rise to error message stating that "buffer is
        too small". ``uint16_codec`` allows to specify what codec (for example:
        ``'latin1'`` or ``'utf-8'``) should be used when reading character
        arrays and can therefore help you solve this problem.

    encoding : str
        Encoding of annotations channel(s). Default is "utf8" (the only correct
        encoding according to the EDF+ standard).
        Only used when reading EDF annotations.

    Returns
    -------
    annot : instance of Annotations | None
        The annotations.

    Notes
    -----
    The annotations stored in a ``.csv`` require the onset columns to be
    timestamps. If you have onsets as floats (in seconds), you should use the
    ``.txt`` extension.
    """

def events_from_annotations(
    raw,
    event_id: str = ...,
    regexp: str = ...,
    use_rounding: bool = ...,
    chunk_duration=...,
    verbose=...,
):
    """Get :term:`events` and ``event_id`` from an Annotations object.

    Parameters
    ----------
    raw : instance of Raw
        The raw data for which Annotations are defined.
    event_id : dict | callable | None | ``'auto'``
        Can be:

        - **dict**: map descriptions (keys) to integer event codes (values).
          Only the descriptions present will be mapped, others will be ignored.
        - **callable**: must take a string input and return an integer event
          code, or return ``None`` to ignore the event.
        - **None**: Map descriptions to unique integer values based on their
          ``sorted`` order.
        - **'auto' (default)**: prefer a raw-format-specific parser:

          - Brainvision: map stimulus events to their integer part; response
            events to integer part + 1000; optic events to integer part + 2000;
            'SyncStatus/Sync On' to 99998; 'New Segment/' to 99999;
            all others like ``None`` with an offset of 10000.
          - Other raw formats: Behaves like None.

          .. versionadded:: 0.18
    regexp : str | None
        Regular expression used to filter the annotations whose
        descriptions is a match. The default ignores descriptions beginning
        ``'bad'`` or ``'edge'`` (case-insensitive).

        .. versionchanged:: 0.18
           Default ignores bad and edge descriptions.
    use_rounding : bool
        If True, use rounding (instead of truncation) when converting
        times to indices. This can help avoid non-unique indices.
    chunk_duration : float | None
        Chunk duration in seconds. If ``chunk_duration`` is set to None
        (default), generated events correspond to the annotation onsets.
        If not, :func:`mne.events_from_annotations` returns as many events as
        they fit within the annotation duration spaced according to
        ``chunk_duration``. As a consequence annotations with duration shorter
        than ``chunk_duration`` will not contribute events.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------

    events : array of int, shape (n_events, 3)
        The array of :term:`events`. The first column contains the event time in
        samples, with :term:`first_samp` included. The third column contains the
        event id.
    event_id : dict
        The event_id variable that can be passed to :class:mne.Epochs`.

    See Also
    --------
    mne.annotations_from_events

    Notes
    -----
    For data formats that store integer events as strings (e.g., NeuroScan
    ``.cnt`` files), passing the Python built-in function :class:`int` as the
    ``event_id`` parameter will do what most users probably want in those
    circumstances: return an ``event_id`` dictionary that maps event ``'1'`` to
    integer event code ``1``, ``'2'`` to ``2``, etc.
    """

def annotations_from_events(
    events, sfreq, event_desc=..., first_samp: int = ..., orig_time=..., verbose=...
):
    """Convert an event array to an Annotations object.

    Parameters
    ----------
    events : ndarray, shape (n_events, 3)
        The events.
    sfreq : float
        Sampling frequency.
    event_desc : dict | array-like | callable | None
        Events description. Can be:

        - **dict**: map integer event codes (keys) to descriptions (values).
          Only the descriptions present will be mapped, others will be ignored.
        - **array-like**: list, or 1d array of integers event codes to include.
          Only the event codes present will be mapped, others will be ignored.
          Event codes will be passed as string descriptions.
        - **callable**: must take a integer event code as input and return a
          string description or None to ignore it.
        - **None**: Use integer event codes as descriptions.
    first_samp : int
        The first data sample (default=0). See :attr:`mne.io.Raw.first_samp`
        docstring.
    orig_time : float | str | datetime | tuple of int | None
        Determines the starting time of annotation acquisition. If None
        (default), starting time is determined from beginning of raw data
        acquisition. For details, see :meth:`mne.Annotations` docstring.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    annot : instance of Annotations
        The annotations.

    See Also
    --------
    mne.events_from_annotations

    Notes
    -----
    Annotations returned by this function will all have zero (null) duration.

    Creating events from annotations via the function
    `mne.events_from_annotations` takes in event mappings with
    key→value pairs as description→ID, whereas `mne.annotations_from_events`
    takes in event mappings with key→value pairs as ID→description.
    If you need to use these together, you can invert the mapping by doing::

        event_desc = {v: k for k, v in event_id.items()}
    """

def count_annotations(annotations):
    """Count annotations.

    Parameters
    ----------
    annotations : mne.Annotations
        The annotations instance.

    Returns
    -------
    counts : dict
        A dictionary containing unique annotation descriptions as keys with their
        counts as values.

    Examples
    --------
        >>> annotations = mne.Annotations([0, 1, 2], [1, 2, 1], ["T0", "T1", "T0"])
        >>> count_annotations(annotations)
        {'T0': 2, 'T1': 1}
    """