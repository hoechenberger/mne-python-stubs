from ._logging import verbose as verbose, warn as warn
from .numerics import object_hash as object_hash, object_size as object_size
from _typeshed import Incomplete
logger: Incomplete

class SizeMixin:
    """Hash the object.

        Returns
        -------
        hash : int
            The hash
        """

    def __eq__(self, other):
        """Compare self to other.

        Parameters
        ----------
        other : object
            The object to compare to.

        Returns
        -------
        eq : bool
            True if the two objects are equal.
        """

    def __hash__(self):
        """Hash the object.

        Returns
        -------
        hash : int
            The hash
        """

class GetEpochsMixin:
    """Get the metadata."""

    def __getitem__(self, item):
        """Return an Epochs object with a copied subset of epochs.

        Parameters
        ----------
        item : slice, array-like, str, or list
            See below for use cases.

        Returns
        -------
        epochs : instance of Epochs
            See below for use cases.

        Notes
        -----
        Epochs can be accessed as ``epochs[...]`` in several ways:

        1. **Integer or slice:** ``epochs[idx]`` will return an `~mne.Epochs`
           object with a subset of epochs chosen by index (supports single
           index and Python-style slicing).

        2. **String:** ``epochs['name']`` will return an `~mne.Epochs` object
           comprising only the epochs labeled ``'name'`` (i.e., epochs created
           around events with the label ``'name'``).

           If there are no epochs labeled ``'name'`` but there are epochs
           labeled with /-separated tags (e.g. ``'name/left'``,
           ``'name/right'``), then ``epochs['name']`` will select the epochs
           with labels that contain that tag (e.g., ``epochs['left']`` selects
           epochs labeled ``'audio/left'`` and ``'visual/left'``, but not
           ``'audio_left'``).

           If multiple tags are provided *as a single string* (e.g.,
           ``epochs['name_1/name_2']``), this selects epochs containing *all*
           provided tags. For example, ``epochs['audio/left']`` selects
           ``'audio/left'`` and ``'audio/quiet/left'``, but not
           ``'audio/right'``. Note that tag-based selection is insensitive to
           order: tags like ``'audio/left'`` and ``'left/audio'`` will be
           treated the same way when selecting via tag.

        3. **List of strings:** ``epochs[['name_1', 'name_2', ... ]]`` will
           return an `~mne.Epochs` object comprising epochs that match *any* of
           the provided names (i.e., the list of names is treated as an
           inclusive-or condition). If *none* of the provided names match any
           epoch labels, a ``KeyError`` will be raised.

           If epoch labels are /-separated tags, then providing multiple tags
           *as separate list entries* will likewise act as an inclusive-or
           filter. For example, ``epochs[['audio', 'left']]`` would select
           ``'audio/left'``, ``'audio/right'``, and ``'visual/left'``, but not
           ``'visual/right'``.

        4. **Pandas query:** ``epochs['pandas query']`` will return an
           `~mne.Epochs` object with a subset of epochs (and matching
           metadata) selected by the query called with
           ``self.metadata.eval``, e.g.::

               epochs["col_a > 2 and col_b == 'foo'"]

           would return all epochs whose associated ``col_a`` metadata was
           greater than two, and whose ``col_b`` metadata was the string 'foo'.
           Query-based indexing only works if Pandas is installed and
           ``self.metadata`` is a :class:`pandas.DataFrame`.

           .. versionadded:: 0.16
        """

    def __len__(self) -> int:
        """Return the number of epochs.

        Returns
        -------
        n_epochs : int
            The number of remaining epochs.

        Notes
        -----
        This function only works if bad epochs have been dropped.

        Examples
        --------
        This can be used as::

            >>> epochs.drop_bad()  # doctest: +SKIP
            >>> len(epochs)  # doctest: +SKIP
            43
            >>> len(epochs.events)  # doctest: +SKIP
            43
        """

    def __iter__(self):
        """Facilitate iteration over epochs.

        This method resets the object iteration state to the first epoch.

        Notes
        -----
        This enables the use of this Python pattern::

            >>> for epoch in epochs:  # doctest: +SKIP
            >>>     print(epoch)  # doctest: +SKIP

        Where ``epoch`` is given by successive outputs of
        :meth:`mne.Epochs.next`.
        """

    def __next__(self, return_event_id: bool=...):
        """Iterate over epoch data.

        Parameters
        ----------
        return_event_id : bool
            If True, return both the epoch data and an event_id.

        Returns
        -------
        epoch : array of shape (n_channels, n_times)
            The epoch data.
        event_id : int
            The event id. Only returned if ``return_event_id`` is ``True``.
        """
    next = __next__

    @property
    def metadata(self):
        """Get the metadata."""

    @metadata.setter
    def metadata(self, metadata, verbose: Incomplete | None=...) -> None:
        """Get the metadata."""

class TimeMixin:
    """Time vector in seconds."""

    def time_as_index(self, times, use_rounding: bool=...):
        """Convert time to indices.

        Parameters
        ----------
        times : list-like | float | int
            List of numbers or a number representing points in time.
        use_rounding : bool
            If True, use rounding (instead of truncation) when converting
            times to indices. This can help avoid non-unique indices.

        Returns
        -------
        index : ndarray
            Indices corresponding to the times supplied.
        """

    @property
    def times(self):
        """Time vector in seconds."""

class ExtendedTimeMixin(TimeMixin):
    """Shift time scale in epoched or evoked data.

        Parameters
        ----------
        tshift : float
            The (absolute or relative) time shift in seconds. If ``relative``
            is True, positive tshift increases the time value associated with
            each sample, while negative tshift decreases it.
        relative : bool
            If True, increase or decrease time values by ``tshift`` seconds.
            Otherwise, shift the time values such that the time of the first
            sample equals ``tshift``.

        Returns
        -------
        epochs : MNE-object
            The modified instance.

        Notes
        -----
        This method allows you to shift the *time* values associated with each
        data sample by an arbitrary amount. It does *not* resample the signal
        or change the *data* values in any way.
        """

    @property
    def tmin(self):
        """First time point."""

    @property
    def tmax(self):
        """Last time point."""

    def crop(self, tmin: Incomplete | None=..., tmax: Incomplete | None=..., include_tmax: bool=..., verbose: Incomplete | None=...):
        """Crop data to a given time interval.

        Parameters
        ----------
        tmin : float | None
            Start time of selection in seconds.
        tmax : float | None
            End time of selection in seconds.
        
        include_tmax : bool
            If True (default), include tmax. If False, exclude tmax (similar to how
            Python indexing typically works).
        
            .. versionadded:: 0.19
        
        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        inst : instance of Raw, Epochs, Evoked, AverageTFR, or SourceEstimate
            The cropped time-series object, modified in-place.

        Notes
        -----
        
        Unlike Python slices, MNE time intervals by default include **both**
        their end points; ``crop(tmin, tmax)`` returns the interval
        ``tmin <= t <= tmax``. Pass ``include_tmax=False`` to specify the half-open
        interval ``tmin <= t < tmax`` instead.
        """

    def decimate(self, decim, offset: int=..., *, verbose: Incomplete | None=...):
        """Decimate the time-series data.

        Parameters
        ----------
        
        decim : int
            Factor by which to subsample the data.
        
            .. warning:: Low-pass filtering is not performed, this simply selects
                         every Nth sample (where N is the value passed to
                         ``decim``), i.e., it compresses the signal (see Notes).
                         If the data are not properly filtered, aliasing artifacts
                         may occur.
        
        offset : int
            Apply an offset to where the decimation starts relative to the
            sample corresponding to t=0. The offset is in samples at the
            current sampling rate.
        
            .. versionadded:: 0.12
        
        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        inst : MNE-object
            The decimated object.

        See Also
        --------
        mne.Epochs.resample
        mne.io.Raw.resample

        Notes
        -----
        
        For historical reasons, ``decim`` / "decimation" refers to simply subselecting
        samples from a given signal. This contrasts with the broader signal processing
        literature, where decimation is defined as (quoting
        :footcite:`OppenheimEtAl1999`, p. 172; which cites
        :footcite:`CrochiereRabiner1983`):
        
            "... a general system for downsampling by a factor of M is the one shown
            in Figure 4.23. Such a system is called a decimator, and downsampling
            by lowpass filtering followed by compression [i.e, subselecting samples]
            has been termed decimation (Crochiere and Rabiner, 1983)."
        
        Hence "decimation" in MNE is what is considered "compression" in the signal
        processing community.
        
        Decimation can be done multiple times. For example,
        ``inst.decimate(2).decimate(2)`` will be the same as
        ``inst.decimate(4)``.

        If ``decim`` is 1, this method does not copy the underlying data.

        .. versionadded:: 0.10.0

        References
        ----------
        .. footbibliography::
        """

    def shift_time(self, tshift, relative: bool=...):
        """Shift time scale in epoched or evoked data.

        Parameters
        ----------
        tshift : float
            The (absolute or relative) time shift in seconds. If ``relative``
            is True, positive tshift increases the time value associated with
            each sample, while negative tshift decreases it.
        relative : bool
            If True, increase or decrease time values by ``tshift`` seconds.
            Otherwise, shift the time values such that the time of the first
            sample equals ``tshift``.

        Returns
        -------
        epochs : MNE-object
            The modified instance.

        Notes
        -----
        This method allows you to shift the *time* values associated with each
        data sample by an arbitrary amount. It does *not* resample the signal
        or change the *data* values in any way.
        """