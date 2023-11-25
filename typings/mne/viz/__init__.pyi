from . import _scraper as _scraper, backends as backends, ui_events as ui_events
from ._3d import (
    link_brains as link_brains,
    plot_alignment as plot_alignment,
    plot_brain_colorbar as plot_brain_colorbar,
    plot_dipole_locations as plot_dipole_locations,
    plot_evoked_field as plot_evoked_field,
    plot_head_positions as plot_head_positions,
    plot_source_estimates as plot_source_estimates,
    plot_sparse_source_estimates as plot_sparse_source_estimates,
    plot_vector_source_estimates as plot_vector_source_estimates,
    plot_volume_source_estimates as plot_volume_source_estimates,
    set_3d_options as set_3d_options,
    snapshot_brain_montage as snapshot_brain_montage,
)
from ._brain import Brain as Brain
from ._figure import (
    get_browser_backend as get_browser_backend,
    set_browser_backend as set_browser_backend,
    use_browser_backend as use_browser_backend,
)
from ._proj import plot_projs_joint as plot_projs_joint
from .backends._abstract import Figure3D as Figure3D
from .backends.renderer import (
    close_3d_figure as close_3d_figure,
    close_all_3d_figures as close_all_3d_figures,
    create_3d_figure as create_3d_figure,
    get_3d_backend as get_3d_backend,
    get_brain_class as get_brain_class,
    set_3d_backend as set_3d_backend,
    set_3d_title as set_3d_title,
    set_3d_view as set_3d_view,
    use_3d_backend as use_3d_backend,
)
from .circle import (
    circular_layout as circular_layout,
    plot_channel_labels_circle as plot_channel_labels_circle,
)
from .epochs import (
    plot_drop_log as plot_drop_log,
    plot_epochs as plot_epochs,
    plot_epochs_image as plot_epochs_image,
    plot_epochs_psd as plot_epochs_psd,
)
from .evoked import (
    plot_compare_evokeds as plot_compare_evokeds,
    plot_evoked as plot_evoked,
    plot_evoked_image as plot_evoked_image,
    plot_evoked_joint as plot_evoked_joint,
    plot_evoked_topo as plot_evoked_topo,
    plot_evoked_white as plot_evoked_white,
    plot_snr_estimate as plot_snr_estimate,
)
from .evoked_field import EvokedField as EvokedField
from .ica import (
    _plot_sources as _plot_sources,
    plot_ica_overlay as plot_ica_overlay,
    plot_ica_properties as plot_ica_properties,
    plot_ica_scores as plot_ica_scores,
    plot_ica_sources as plot_ica_sources,
)
from .misc import (
    _get_presser as _get_presser,
    adjust_axes as adjust_axes,
    plot_bem as plot_bem,
    plot_chpi_snr as plot_chpi_snr,
    plot_cov as plot_cov,
    plot_csd as plot_csd,
    plot_dipole_amplitudes as plot_dipole_amplitudes,
    plot_events as plot_events,
    plot_filter as plot_filter,
    plot_ideal_filter as plot_ideal_filter,
    plot_source_spectrogram as plot_source_spectrogram,
)
from .montage import plot_montage as plot_montage
from .raw import (
    _RAW_CLIP_DEF as _RAW_CLIP_DEF,
    plot_raw as plot_raw,
    plot_raw_psd as plot_raw_psd,
    plot_raw_psd_topo as plot_raw_psd_topo,
)
from .topo import (
    iter_topography as iter_topography,
    plot_topo_image_epochs as plot_topo_image_epochs,
)
from .topomap import (
    plot_arrowmap as plot_arrowmap,
    plot_bridged_electrodes as plot_bridged_electrodes,
    plot_ch_adjacency as plot_ch_adjacency,
    plot_epochs_psd_topomap as plot_epochs_psd_topomap,
    plot_evoked_topomap as plot_evoked_topomap,
    plot_ica_components as plot_ica_components,
    plot_layout as plot_layout,
    plot_projs_topomap as plot_projs_topomap,
    plot_regression_weights as plot_regression_weights,
    plot_tfr_topomap as plot_tfr_topomap,
    plot_topomap as plot_topomap,
)
from .utils import (
    ClickableImage as ClickableImage,
    _get_plot_ch_type as _get_plot_ch_type,
    add_background_image as add_background_image,
    centers_to_edges as centers_to_edges,
    compare_fiff as compare_fiff,
    concatenate_images as concatenate_images,
    mne_analyze_colormap as mne_analyze_colormap,
    plot_sensors as plot_sensors,
)
