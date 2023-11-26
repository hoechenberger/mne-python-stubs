def create_lut(cmap, n_colors: int = 256, center=None):
    """### Return a colormap suitable for setting as a LUT."""
    ...

def scale_sequential_lut(lut_table, fmin, fmid, fmax):
    """### Scale a sequential colormap."""
    ...

def get_fill_colors(cols, n_fill):
    """### Get the fill colors for the middle of divergent colormaps."""
    ...

def calculate_lut(
    lut_table, alpha, fmin, fmid, fmax, center=None, transparent: bool = True
):
    """### Transparent color map calculation.

    A colormap may be sequential or divergent. When the colormap is
    divergent indicate this by providing a value for 'center'. The
    meanings of fmin, fmid and fmax are different for sequential and
    divergent colormaps. A sequential colormap is characterised by::

        [fmin, fmid, fmax]

    where fmin and fmax define the edges of the colormap and fmid
    will be the value mapped to the center of the originally chosen colormap.
    A divergent colormap is characterised by::

        [center-fmax, center-fmid, center-fmin, center,
            center+fmin, center+fmid, center+fmax]

    i.e., values between center-fmin and center+fmin will not be shown
    while center-fmid will map to the fmid of the first half of the
    original colormap and center-fmid to the fmid of the second half.

    -----
    ### 🛠️ Parameters

    lim_cmap : Colormap
        Color map obtained from _process_mapdata.
    alpha : float
        Alpha value to apply globally to the overlay. Has no effect with mpl
        backend.
    fmin : float
        Min value in colormap.
    fmid : float
        Intermediate value in colormap.
    fmax : float
        Max value in colormap.
    center : float or None
        If not None, center of a divergent colormap, changes the meaning of
        fmin, fmax and fmid.
    transparent : boolean
        if True: use a linear transparency between fmin and fmid and make
        values below fmin fully transparent (symmetrically for divergent
        colormaps)

    -----
    ### ⏎ Returns

    cmap : matplotlib.ListedColormap
        Color map with transparency channel.
    """
    ...
