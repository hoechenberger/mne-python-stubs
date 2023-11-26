from .utils import plt_show as plt_show

def circular_layout(
    node_names,
    node_order,
    start_pos: int = 90,
    start_between: bool = True,
    group_boundaries=None,
    group_sep: int = 10,
):
    """## 🧠 Create layout arranging nodes on a circle.

    -----
    ### 🛠️ Parameters

    #### `node_names : list of str`
        Node names.
    #### `node_order : list of str`
        List with node names defining the order in which the nodes are
        arranged. Must have the elements as node_names but the order can be
        different. The nodes are arranged clockwise starting at "start_pos"
        degrees.
    #### `start_pos : float`
        Angle in degrees that defines where the first node is plotted.
    #### `start_between : bool`
        If True, the layout starts with the position between the nodes. This is
        the same as adding "180. / len(node_names)" to start_pos.
    #### `group_boundaries : None | array-like`
        List of of boundaries between groups at which point a "group_sep" will
        be inserted. E.g. "[0, len(node_names) / 2]" will create two groups.
    #### `group_sep : float`
        Group separation angle in degrees. See "group_boundaries".

    -----
    ### ⏎ Returns

    #### `node_angles : array, shape=(n_node_names,)`
        Node angles in degrees.
    """
    ...

def plot_channel_labels_circle(labels, colors=None, picks=None, **kwargs):
    """## 🧠 Plot labels for each channel in a circle plot.

    ### 💡 Note This primarily makes sense for sEEG channels where each
              channel can be assigned an anatomical label as the electrode
              passes through various brain areas.

    -----
    ### 🛠️ Parameters

    #### `labels : dict`
        Lists of labels (values) associated with each channel (keys).
    #### `colors : dict`
        The color (value) for each label (key).
    #### `picks : list | tuple`
        The channels to consider.
    **kwargs : kwargs
        Keyword arguments for
        `mne_connectivity.viz.plot_connectivity_circle`.

    -----
    ### ⏎ Returns

    #### `fig : instance of matplotlib.figure.Figure`
        The figure handle.
    #### `axes : instance of matplotlib.projections.polar.PolarAxes`
        The subplot handle.
    """
    ...
