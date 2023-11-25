from .morph_map import read_morph_map as read_morph_map
from .parallel import parallel_func as parallel_func
from .source_estimate import (
    SourceEstimate as SourceEstimate,
    VolSourceEstimate as VolSourceEstimate,
    extract_label_time_course as extract_label_time_course,
    spatial_src_adjacency as spatial_src_adjacency,
)
from .source_space._source_space import (
    SourceSpaces as SourceSpaces,
    add_source_space_distances as add_source_space_distances,
)
from .surface import (
    complete_surface_info as complete_surface_info,
    fast_cross_3d as fast_cross_3d,
    mesh_dist as mesh_dist,
    mesh_edges as mesh_edges,
    read_surface as read_surface,
)
from .utils import (
    check_random_state as check_random_state,
    fill_doc as fill_doc,
    get_subjects_dir as get_subjects_dir,
    logger as logger,
    warn as warn,
)
from _typeshed import Incomplete

class Label:
    """Compute the surface area of a label.

    Parameters
    ----------

    subject : str | None
        Subject which this label belongs to. Should only be specified if it is not
        specified in the label.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    surface : str
        The surface along which to do the computations, defaults to ``'white'``
        (the gray-white matter boundary).

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    area : float
        The area (in m²) of the label.

    Notes
    -----
    ..versionadded:: 0.24
    """

    vertices: Incomplete
    pos: Incomplete
    values: Incomplete
    hemi: Incomplete
    comment: Incomplete
    subject: Incomplete
    color: Incomplete
    name: Incomplete
    filename: Incomplete

    def __init__(
        self,
        vertices=...,
        pos=...,
        values=...,
        hemi=...,
        comment: str = ...,
        name=...,
        filename=...,
        subject=...,
        color=...,
        *,
        verbose=...,
    ) -> None: ...
    def __len__(self) -> int:
        """Return the number of vertices.

        Returns
        -------
        n_vertices : int
            The number of vertices.
        """
    def __add__(self, other):
        """Add Labels."""
    def __sub__(self, other):
        """Subtract Labels."""
    def save(self, filename) -> None:
        """Write to disk as FreeSurfer \\*.label file.

        Parameters
        ----------
        filename : path-like
            Path to label file to produce.

        Notes
        -----
        Note that due to file specification limitations, the Label's subject
        and color attributes are not saved to disk.
        """
    def copy(self):
        """Copy the label instance.

        Returns
        -------
        label : instance of Label
            The copied label.
        """
    def fill(self, src, name=...):
        """Fill the surface between sources for a source space label.

        Parameters
        ----------
        src : SourceSpaces
            Source space in which the label was defined. If a source space is
            provided, the label is expanded to fill in surface vertices that
            lie between the vertices included in the source space. For the
            added vertices, ``pos`` is filled in with positions from the
            source space, and ``values`` is filled in from the closest source
            space vertex.
        name : None | str
            Name for the new Label (default is self.name).

        Returns
        -------
        label : Label
            The label covering the same vertices in source space but also
            including intermediate surface vertices.

        See Also
        --------
        Label.restrict
        Label.smooth
        """
    def restrict(self, src, name=...):
        """Restrict a label to a source space.

        Parameters
        ----------
        src : instance of SourceSpaces
            The source spaces to use to restrict the label.
        name : None | str
            Name for the new Label (default is self.name).

        Returns
        -------
        label : instance of Label
            The Label restricted to the set of source space vertices.

        See Also
        --------
        Label.fill

        Notes
        -----
        .. versionadded:: 0.20
        """
    def smooth(
        self,
        subject=...,
        smooth: int = ...,
        grade=...,
        subjects_dir=...,
        n_jobs=...,
        verbose=...,
    ):
        """Smooth the label.

        Useful for filling in labels made in a
        decimated source space for display.

        Parameters
        ----------

        subject : str | None
            Subject which this label belongs to. Should only be specified if it is not
            specified in the label.
        smooth : int
            Number of iterations for the smoothing of the surface data.
            Cannot be None here since not all vertices are used. For a
            grade of 5 (e.g., fsaverage), a smoothing of 2 will fill a
            label.
        grade : int, list of shape (2,), array, or None
            Resolution of the icosahedral mesh (typically 5). If None, all
            vertices will be used (potentially filling the surface). If a list,
            values will be morphed to the set of vertices specified in grade[0]
            and grade[1], assuming that these are vertices for the left and
            right hemispheres. Note that specifying the vertices (e.g.,
            grade=[np.arange(10242), np.arange(10242)] for fsaverage on a
            standard grade 5 source space) can be substantially faster than
            computing vertex locations. If one array is used, it is assumed
            that all vertices belong to the hemisphere of the label. To create
            a label filling the surface, use None.

        subjects_dir : path-like | None
            The path to the directory containing the FreeSurfer subjects
            reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
            variable.
        n_jobs : int | None
            The number of jobs to run in parallel. If ``-1``, it is set
            to the number of CPU cores. Requires the :mod:`joblib` package.
            ``None`` (default) is a marker for 'unset' that will be interpreted
            as ``n_jobs=1`` (sequential execution) unless the call is performed under
            a :class:`joblib:joblib.parallel_config` context manager that sets another
            value for ``n_jobs``.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        label : instance of Label
            The smoothed label.

        Notes
        -----
        This function will set label.pos to be all zeros. If the positions
        on the new surface are required, consider using mne.read_surface
        with ``label.vertices``.
        """
    def morph(
        self,
        subject_from=...,
        subject_to=...,
        smooth: int = ...,
        grade=...,
        subjects_dir=...,
        n_jobs=...,
        verbose=...,
    ):
        """Morph the label.

        Useful for transforming a label from one subject to another.

        Parameters
        ----------
        subject_from : str | None
            The name of the subject of the current label. If None, the
            initial subject will be taken from self.subject.
        subject_to : str
            The name of the subject to morph the label to. This will
            be put in label.subject of the output label file.
        smooth : int
            Number of iterations for the smoothing of the surface data.
            Cannot be None here since not all vertices are used.
        grade : int, list of shape (2,), array, or None
            Resolution of the icosahedral mesh (typically 5). If None, all
            vertices will be used (potentially filling the surface). If a list,
            values will be morphed to the set of vertices specified in grade[0]
            and grade[1], assuming that these are vertices for the left and
            right hemispheres. Note that specifying the vertices (e.g.,
            ``grade=[np.arange(10242), np.arange(10242)]`` for fsaverage on a
            standard grade 5 source space) can be substantially faster than
            computing vertex locations. If one array is used, it is assumed
            that all vertices belong to the hemisphere of the label. To create
            a label filling the surface, use None.

        subjects_dir : path-like | None
            The path to the directory containing the FreeSurfer subjects
            reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
            variable.
        n_jobs : int | None
            The number of jobs to run in parallel. If ``-1``, it is set
            to the number of CPU cores. Requires the :mod:`joblib` package.
            ``None`` (default) is a marker for 'unset' that will be interpreted
            as ``n_jobs=1`` (sequential execution) unless the call is performed under
            a :class:`joblib:joblib.parallel_config` context manager that sets another
            value for ``n_jobs``.

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        label : instance of Label
            The morphed label.

        See Also
        --------
        mne.morph_labels : Morph a set of labels.

        Notes
        -----
        This function will set label.pos to be all zeros. If the positions
        on the new surface are required, consider using `mne.read_surface`
        with ``label.vertices``.
        """
    def split(
        self, parts: int = ..., subject=..., subjects_dir=..., freesurfer: bool = ...
    ):
        """Split the Label into two or more parts.

        Parameters
        ----------
        parts : int >= 2 | tuple of str | str
            Number of labels to create (default is 2), or tuple of strings
            specifying label names for new labels (from posterior to anterior),
            or 'contiguous' to split the label into connected components.
            If a number or 'contiguous' is specified, names of the new labels
            will be the input label's name with div1, div2 etc. appended.

        subject : str | None
            Subject which this label belongs to. Should only be specified if it is not
            specified in the label.

        subjects_dir : path-like | None
            The path to the directory containing the FreeSurfer subjects
            reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
            variable.
        freesurfer : bool
            By default (``False``) ``split_label`` uses an algorithm that is
            slightly optimized for performance and numerical precision. Set
            ``freesurfer`` to ``True`` in order to replicate label splits from
            FreeSurfer's ``mris_divide_parcellation``.

        Returns
        -------
        labels : list of Label, shape (n_parts,)
            The labels, starting from the lowest to the highest end of the
            projection axis.

        Notes
        -----
        If using 'contiguous' split, you must ensure that the label being split
        uses the same triangular resolution as the surface mesh files in
        ``subjects_dir`` Also, some small fringe labels may be returned that
        are close (but not connected) to the large components.

        The spatial split finds the label's principal eigen-axis on the
        spherical surface, projects all label vertex coordinates onto this
        axis, and divides them at regular spatial intervals.
        """
    def get_vertices_used(self, vertices=...):
        """Get the source space's vertices inside the label.

        Parameters
        ----------
        vertices : ndarray of int, shape (n_vertices,) | None
            The set of vertices to compare the label to. If None, equals to
            ``np.arange(10242)``. Defaults to None.

        Returns
        -------
        label_verts : ndarray of in, shape (n_label_vertices,)
            The vertices of the label corresponding used by the data.
        """
    def get_tris(self, tris, vertices=...):
        """Get the source space's triangles inside the label.

        Parameters
        ----------
        tris : ndarray of int, shape (n_tris, 3)
            The set of triangles corresponding to the vertices in a
            source space.
        vertices : ndarray of int, shape (n_vertices,) | None
            The set of vertices to compare the label to. If None, equals to
            ``np.arange(10242)``. Defaults to None.

        Returns
        -------
        label_tris : ndarray of int, shape (n_tris, 3)
            The subset of tris used by the label.
        """
    def center_of_mass(
        self,
        subject=...,
        restrict_vertices: bool = ...,
        subjects_dir=...,
        surf: str = ...,
    ):
        """Compute the center of mass of the label.

        This function computes the spatial center of mass on the surface
        as in :footcite:`LarsonLee2013`.

        Parameters
        ----------

        subject : str | None
            Subject which this label belongs to. Should only be specified if it is not
            specified in the label.
        restrict_vertices : bool | array of int | instance of SourceSpaces
            If True, returned vertex will be one from the label. Otherwise,
            it could be any vertex from surf. If an array of int, the
            returned vertex will come from that array. If instance of
            SourceSpaces (as of 0.13), the returned vertex will be from
            the given source space. For most accuruate estimates, do not
            restrict vertices.

        subjects_dir : path-like | None
            The path to the directory containing the FreeSurfer subjects
            reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
            variable.
        surf : str
            The surface to use for Euclidean distance center of mass
            finding. The default here is "sphere", which finds the center
            of mass on the spherical surface to help avoid potential issues
            with cortical folding.

        Returns
        -------
        vertex : int
            Vertex of the spatial center of mass for the inferred hemisphere,
            with each vertex weighted by its label value.

        See Also
        --------
        SourceEstimate.center_of_mass
        vertex_to_mni

        Notes
        -----
        .. versionadded:: 0.13

        References
        ----------
        .. footbibliography::
        """
    def distances_to_outside(
        self, subject=..., subjects_dir=..., surface: str = ..., *, verbose=...
    ):
        """Compute the distance from each vertex to outside the label.

        Parameters
        ----------

        subject : str | None
            Subject which this label belongs to. Should only be specified if it is not
            specified in the label.

        subjects_dir : path-like | None
            The path to the directory containing the FreeSurfer subjects
            reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
            variable.
        surface : str
            The surface along which to do the computations, defaults to ``'white'``
            (the gray-white matter boundary).

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        dist : ndarray, shape (n_vertices,)
            The distance from each vertex in ``self.vertices`` to exit the
            label.
        outside_vertices : ndarray, shape (n_vertices,)
            For each vertex in the label, the nearest vertex outside the
            label.

        Notes
        -----
        Distances are computed along the cortical surface.

        .. versionadded:: 0.24
        """
    def compute_area(
        self, subject=..., subjects_dir=..., surface: str = ..., *, verbose=...
    ):
        """Compute the surface area of a label.

        Parameters
        ----------

        subject : str | None
            Subject which this label belongs to. Should only be specified if it is not
            specified in the label.

        subjects_dir : path-like | None
            The path to the directory containing the FreeSurfer subjects
            reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
            variable.
        surface : str
            The surface along which to do the computations, defaults to ``'white'``
            (the gray-white matter boundary).

        verbose : bool | str | int | None
            Control verbosity of the logging output. If ``None``, use the default
            verbosity level. See the :ref:`logging documentation <tut-logging>` and
            :func:`mne.verbose` for details. Should only be passed as a keyword
            argument.

        Returns
        -------
        area : float
            The area (in m²) of the label.

        Notes
        -----
        ..versionadded:: 0.24
        """

class BiHemiLabel:
    """Subtract labels."""

    lh: Incomplete
    rh: Incomplete
    name: Incomplete
    subject: Incomplete
    color: Incomplete
    hemi: str

    def __init__(self, lh, rh, name=..., color=...) -> None: ...
    def __len__(self) -> int:
        """Return the number of vertices.

        Returns
        -------
        n_vertices : int
            The number of vertices.
        """
    def __add__(self, other):
        """Add labels."""
    def __sub__(self, other):
        """Subtract labels."""

def read_label(filename, subject=..., color=..., *, verbose=...):
    """Read FreeSurfer Label file.

    Parameters
    ----------
    filename : str
        Path to label file.

    subject : str | None
        Subject which this label belongs to. Should only be specified if it is not
        specified in the label.
        It is good practice to set this attribute to avoid combining
        incompatible labels and SourceEstimates (e.g., ones from other
        subjects). Note that due to file specification limitations, the
        subject name isn't saved to or loaded from files written to disk.
    color : None | matplotlib color
        Default label color and alpha (e.g., ``(1., 0., 0., 1.)`` for red).
        Note that due to file specification limitations, the color isn't saved
        to or loaded from files written to disk.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    label : Label
        Instance of Label object with attributes:

            - ``comment``: comment from the first line of the label file
            - ``vertices``: vertex indices (0 based, column 1)
            - ``pos``: locations in meters (columns 2 - 4 divided by 1000)
            - ``values``: values at the vertices (column 5)

    See Also
    --------
    read_labels_from_annot
    write_labels_to_annot
    """

def write_label(filename, label, verbose=...) -> None:
    """Write a FreeSurfer label.

    Parameters
    ----------
    filename : str
        Path to label file to produce.
    label : Label
        The label object to save.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    write_labels_to_annot

    Notes
    -----
    Note that due to file specification limitations, the Label's subject and
    color attributes are not saved to disk.
    """

def split_label(
    label, parts: int = ..., subject=..., subjects_dir=..., freesurfer: bool = ...
):
    """Split a Label into two or more parts.

    Parameters
    ----------
    label : Label | str
        Label which is to be split (Label object or path to a label file).
    parts : int >= 2 | tuple of str
        A sequence of strings specifying label names for the new labels (from
        posterior to anterior), or the number of new labels to create (default
        is 2). If a number is specified, names of the new labels will be the
        input label's name with div1, div2 etc. appended.

    subject : str | None
        Subject which this label belongs to. Should only be specified if it is not
        specified in the label.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    freesurfer : bool
        By default (``False``) ``split_label`` uses an algorithm that is
        slightly optimized for performance and numerical precision. Set
        ``freesurfer`` to ``True`` in order to replicate label splits from
        FreeSurfer's ``mris_divide_parcellation``.

    Returns
    -------
    labels : list of Label, shape (n_parts,)
        The labels, starting from the lowest to the highest end of the
        projection axis.

    Notes
    -----
    Works by finding the label's principal eigen-axis on the spherical surface,
    projecting all label vertex coordinates onto this axis and dividing them at
    regular spatial intervals.
    """

def label_sign_flip(label, src):
    """Compute sign for label averaging.

    Parameters
    ----------
    label : Label | BiHemiLabel
        A label.
    src : SourceSpaces
        The source space over which the label is defined.

    Returns
    -------
    flip : array
        Sign flip vector (contains 1 or -1).
    """

def stc_to_label(
    stc,
    src=...,
    smooth: bool = ...,
    connected: bool = ...,
    subjects_dir=...,
    verbose=...,
):
    """Compute a label from the non-zero sources in an stc object.

    Parameters
    ----------
    stc : SourceEstimate
        The source estimates.
    src : SourceSpaces | str | None
        The source space over which the source estimates are defined.
        If it's a string it should the subject name (e.g. fsaverage).
        Can be None if stc.subject is not None.
    smooth : bool
        Fill in vertices on the cortical surface that are not in the source
        space based on the closest source space vertex (requires
        src to be a SourceSpace).
    connected : bool
        If True a list of connected labels will be returned in each
        hemisphere. The labels are ordered in decreasing order depending
        of the maximum value in the stc.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    labels : list of Label | list of list of Label
        The generated labels. If connected is False, it returns
        a list of Labels (one per hemisphere). If no Label is available
        in a hemisphere, None is returned. If connected is True,
        it returns for each hemisphere a list of connected labels
        ordered in decreasing order depending of the maximum value in the stc.
        If no Label is available in an hemisphere, an empty list is returned.
    """

def grow_labels(
    subject,
    seeds,
    extents,
    hemis,
    subjects_dir=...,
    n_jobs=...,
    overlap: bool = ...,
    names=...,
    surface: str = ...,
    colors=...,
):
    """Generate circular labels in source space with region growing.

    This function generates a number of labels in source space by growing
    regions starting from the vertices defined in "seeds". For each seed, a
    label is generated containing all vertices within a maximum geodesic
    distance on the white matter surface from the seed.

    Parameters
    ----------

    subject : str
        The FreeSurfer subject name.
    seeds : int | list
        Seed, or list of seeds. Each seed can be either a vertex number or
        a list of vertex numbers.
    extents : array | float
        Extents (radius in mm) of the labels.
    hemis : array | int
        Hemispheres to use for the labels (0: left, 1: right).

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the :mod:`joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a :class:`joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.
        Likely only useful if tens or hundreds of labels are being expanded
        simultaneously. Does not apply with ``overlap=False``.
    overlap : bool
        Produce overlapping labels. If True (default), the resulting labels
        can be overlapping. If False, each label will be grown one step at a
        time, and occupied territory will not be invaded.
    names : None | list of str
        Assign names to the new labels (list needs to have the same length as
        seeds).
    surface : str
        The surface along which to do the computations, defaults to ``'white'``
        (the gray-white matter boundary).
    colors : array, shape (n, 4) or (, 4) | None
        How to assign colors to each label. If None then unique colors will be
        chosen automatically (default), otherwise colors will be broadcast
        from the array. The first three values will be interpreted as RGB
        colors and the fourth column as the alpha value (commonly 1).

    Returns
    -------
    labels : list of Label
        The labels' ``comment`` attribute contains information on the seed
        vertex and extent; the ``values``  attribute contains distance from the
        seed in millimeters.

    Notes
    -----
    "extents" and "hemis" can either be arrays with the same length as
    seeds, which allows using a different extent and hemisphere for
    label, or integers, in which case the same extent and hemisphere is
    used for each label.
    """

def random_parcellation(
    subject, n_parcel, hemi, subjects_dir=..., surface: str = ..., random_state=...
):
    """Generate random cortex parcellation by growing labels.

    This function generates a number of labels which don't intersect and
    cover the whole surface. Regions are growing around randomly chosen
    seeds.

    Parameters
    ----------

    subject : str
        The FreeSurfer subject name.
    n_parcel : int
        Total number of cortical parcels.
    hemi : str
        Hemisphere id (ie ``'lh'``, ``'rh'``, ``'both'``). In the case
        of ``'both'``, both hemispheres are processed with ``(n_parcel // 2)``
        parcels per hemisphere.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    surface : str
        The surface along which to do the computations, defaults to ``'white'``
        (the gray-white matter boundary).

    random_state : None | int | instance of ~numpy.random.RandomState
        A seed for the NumPy random number generator (RNG). If ``None`` (default),
        the seed will be  obtained from the operating system
        (see  :class:numpy.random.RandomState` for details), meaning it will most
        likely produce different output every time this function or method is run.
        To achieve reproducible results, pass a value here to explicitly initialize
        the RNG with a defined state.

    Returns
    -------
    labels : list of Label
        Random cortex parcellation.
    """

def read_labels_from_annot(
    subject,
    parc: str = ...,
    hemi: str = ...,
    surf_name: str = ...,
    annot_fname=...,
    regexp=...,
    subjects_dir=...,
    sort: bool = ...,
    verbose=...,
):
    """Read labels from a FreeSurfer annotation file.

    Note: Only cortical labels will be returned.

    Parameters
    ----------

    subject : str
        The FreeSurfer subject name.
    parc : str
        The parcellation to use, e.g., ``'aparc'`` or ``'aparc.a2009s'``.
    hemi : str
        The hemisphere from which to read the parcellation, can be ``'lh'``,
        ``'rh'``, or ``'both'``.
    surf_name : str
        Surface used to obtain vertex locations, e.g., ``'white'``, ``'pial'``.
    annot_fname : path-like | None
        Filename of the ``.annot`` file. If not None, only this file is read
        and the arguments ``parc`` and ``hemi`` are ignored.
    regexp : str
        Regular expression or substring to select particular labels from the
        parcellation. E.g. ``'superior'`` will return all labels in which this
        substring is contained.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    sort : bool
        If true, labels will be sorted by name before being returned.

        .. versionadded:: 0.21.0

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    labels : list of Label
        The labels, sorted by label name (ascending).

    See Also
    --------
    write_labels_to_annot
    morph_labels
    """

def morph_labels(
    labels,
    subject_to,
    subject_from=...,
    subjects_dir=...,
    surf_name: str = ...,
    verbose=...,
):
    """Morph a set of labels.

    This is useful when morphing a set of non-overlapping labels (such as those
    obtained with :func:`read_labels_from_annot`) from one subject to
    another.

    Parameters
    ----------
    labels : list
        The labels to morph.
    subject_to : str
        The subject to morph labels to.
    subject_from : str | None
        The subject to morph labels from. Can be None if the labels
        have the ``.subject`` property defined.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    surf_name : str
        Surface used to obtain vertex locations, e.g., ``'white'``, ``'pial'``.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    labels : list
        The morphed labels.

    See Also
    --------
    read_labels_from_annot
    mne.Label.morph

    Notes
    -----
    This does not use the same algorithm as Freesurfer, so the results
    morphing (e.g., from ``'fsaverage'`` to your subject) might not match
    what Freesurfer produces during ``recon-all``.

    .. versionadded:: 0.18
    """

def labels_to_stc(
    labels, values, tmin: int = ..., tstep: int = ..., subject=..., src=..., verbose=...
):
    """Convert a set of labels and values to a STC.

    This function is meant to work like the opposite of
    `extract_label_time_course`.

    Parameters
    ----------

    labels : Label | BiHemiLabel | list | tuple | str
        If using a surface or mixed source space, this should be the
        :class:mne.Label`'s for which to extract the time course.
        If working with whole-brain volume source estimates, this must be one of:

        - a string path to a FreeSurfer atlas for the subject (e.g., their
          'aparc.a2009s+aseg.mgz') to extract time courses for all volumes in the
          atlas
        - a two-element list or tuple, the first element being a path to an atlas,
          and the second being a list or dict of ``volume_labels`` to extract
          (see :func:`mne.setup_volume_source_space` for details).

        .. versionchanged:: 0.21.0
           Support for volume source estimates.
    values : ndarray, shape (n_labels, ...)
        The values in each label. Can be 1D or 2D.
    tmin : float
        The tmin to use for the STC.
    tstep : float
        The tstep to use for the STC.

    subject : str
        The FreeSurfer subject name.

    src : instance of SourceSpaces
        The source spaces for the source time courses.
        Can be omitted if using a surface source space, in which case
        the label vertices will determine the output STC vertices.
        Required if using a volumetric source space.

        .. versionadded:: 0.22

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    stc : instance of SourceEstimate | instance of VolSourceEstimate
        The values-in-labels converted to a STC.

    See Also
    --------
    extract_label_time_course

    Notes
    -----
    Vertices that appear in more than one label will be averaged.

    .. versionadded:: 0.18
    """

def write_labels_to_annot(
    labels,
    subject=...,
    parc=...,
    overwrite: bool = ...,
    subjects_dir=...,
    annot_fname=...,
    colormap: str = ...,
    hemi: str = ...,
    sort: bool = ...,
    table_name=...,
    verbose=...,
):
    """Create a FreeSurfer annotation from a list of labels.

    Parameters
    ----------
    labels : list with instances of mne.Label
        The labels to create a parcellation from.

    subject : str
        The FreeSurfer subject name.
    parc : str | None
        The parcellation name to use.
    overwrite : bool
        Overwrite files if they already exist.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    annot_fname : str | None
        Filename of the ``.annot file``. If not None, only this file is written
        and the arguments ``parc`` and ``subject`` are ignored.
    colormap : str
        Colormap to use to generate label colors for labels that do not
        have a color specified.
    hemi : ``'both'`` | ``'lh'`` | ``'rh'``
        The hemisphere(s) for which to write \\*.annot files (only applies if
        annot_fname is not specified; default is 'both').
    sort : bool
        If True (default), labels will be sorted by name before writing.

        .. versionadded:: 0.21.0
    table_name : str
        The table name to use for the colortable.

        .. versionadded:: 0.21.0

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        :func:`mne.verbose` for details. Should only be passed as a keyword
        argument.

    See Also
    --------
    read_labels_from_annot

    Notes
    -----
    Vertices that are not covered by any of the labels are assigned to a label
    named ``"unknown"``.
    """

def select_sources(
    subject,
    label,
    location: str = ...,
    extent: float = ...,
    grow_outside: bool = ...,
    subjects_dir=...,
    name=...,
    random_state=...,
    surf: str = ...,
):
    """Select sources from a label.

    Parameters
    ----------

    subject : str
        The FreeSurfer subject name.
    label : instance of Label | str
        Define where the seed will be chosen. If str, can be 'lh' or 'rh',
        which correspond to left or right hemisphere, respectively.
    location : 'random' | 'center' | int
        Location to grow label from. If the location is an int, it represents
        the vertex number in the corresponding label. If it is a str, it can be
        either 'random' or 'center'.
    extent : float
        Extents (radius in mm) of the labels, i.e. maximum geodesic distance
        on the white matter surface from the seed. If 0, the resulting label
        will contain only one vertex.
    grow_outside : bool
        Let the region grow outside the original label where location was
        defined.

    subjects_dir : path-like | None
        The path to the directory containing the FreeSurfer subjects
        reconstructions. If ``None``, defaults to the ``SUBJECTS_DIR`` environment
        variable.
    name : None | str
        Assign name to the new label.

    random_state : None | int | instance of ~numpy.random.RandomState
        A seed for the NumPy random number generator (RNG). If ``None`` (default),
        the seed will be  obtained from the operating system
        (see  :class:numpy.random.RandomState` for details), meaning it will most
        likely produce different output every time this function or method is run.
        To achieve reproducible results, pass a value here to explicitly initialize
        the RNG with a defined state.
    surf : str
        The surface used to simulated the label, defaults to the white surface.

    Returns
    -------
    label : instance of Label
        The label that contains the selected sources.

    Notes
    -----
    This function selects a region of interest on the cortical surface based
    on a label (or a hemisphere). The sources are selected by growing a region
    around a seed which is selected randomly, is the center of the label, or
    is a specific vertex. The selected vertices can extend beyond the initial
    provided label. This can be prevented by setting grow_outside to False.

    The selected sources are returned in the form of a new Label object. The
    values of the label contain the distance from the seed in millimeters.

    .. versionadded:: 0.18
    """
