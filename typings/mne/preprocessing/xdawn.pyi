from .._fiff.pick import pick_info as pick_info
from ..cov import Covariance as Covariance
from ..decoding import (
    BaseEstimator as BaseEstimator,
    TransformerMixin as TransformerMixin,
)
from ..epochs import BaseEpochs as BaseEpochs
from ..evoked import Evoked as Evoked, EvokedArray as EvokedArray
from ..io import BaseRaw as BaseRaw
from ..utils import logger as logger
from _typeshed import Incomplete

class _XdawnTransformer(BaseEstimator, TransformerMixin):
    """Implementation of the Xdawn Algorithm compatible with scikit-learn.

    Xdawn is a spatial filtering method designed to improve the signal
    to signal + noise ratio (SSNR) of the event related responses. Xdawn was
    originally designed for P300 evoked potential by enhancing the target
    response with respect to the non-target response. This implementation is a
    generalization to any type of event related response.

    💡 _XdawnTransformer does not correct for epochs overlap. To correct
              overlaps see ``Xdawn``.

    Parameters
    ----------
    n_components : int (default 2)
        The number of components to decompose the signals.
    reg : float | str | None (default None)
        If not None (same as ``'empirical'``, default), allow
        regularization for covariance estimation.
        If float, shrinkage is used (0 <= shrinkage <= 1).
        For str options, ``reg`` will be passed to ``method`` to
        `mne.compute_covariance`.
    signal_cov : None | Covariance | array, shape (n_channels, n_channels)
        The signal covariance used for whitening of the data.
        if None, the covariance is estimated from the epochs signal.
    method_params : dict | None
        Parameters to pass to `mne.compute_covariance`.

        ✨ Added in version 0.16

    Attributes
    ----------
    classes_ : array, shape (n_classes)
        The event indices of the classes.
    filters_ : array, shape (n_channels, n_channels)
        The Xdawn components used to decompose the data for each event type.
    patterns_ : array, shape (n_channels, n_channels)
        The Xdawn patterns used to restore the signals for each event type.
    """

    n_components: Incomplete
    signal_cov: Incomplete
    reg: Incomplete
    method_params: Incomplete

    def __init__(
        self, n_components: int = 2, reg=None, signal_cov=None, method_params=None
    ) -> None:
        """Init."""
        ...
    classes_: Incomplete

    def fit(self, X, y=None):
        """Fit Xdawn spatial filters.

        Parameters
        ----------
        X : array, shape (n_epochs, n_channels, n_samples)
            The target data.
        y : array, shape (n_epochs,) | None
            The target labels. If None, Xdawn fit on the average evoked.

        Returns
        -------
        self : Xdawn instance
            The Xdawn instance.
        """
        ...

    def transform(self, X):
        """Transform data with spatial filters.

        Parameters
        ----------
        X : array, shape (n_epochs, n_channels, n_samples)
            The target data.

        Returns
        -------
        X : array, shape (n_epochs, n_components * n_classes, n_samples)
            The transformed data.
        """
        ...

    def inverse_transform(self, X):
        """Remove selected components from the signal.

        Given the unmixing matrix, transform data, zero out components,
        and inverse transform the data. This procedure will reconstruct
        the signals from which the dynamics described by the excluded
        components is subtracted.

        Parameters
        ----------
        X : array, shape (n_epochs, n_components * n_classes, n_times)
            The transformed data.

        Returns
        -------
        X : array, shape (n_epochs, n_channels * n_classes, n_times)
            The inverse transform data.
        """
        ...

class Xdawn(_XdawnTransformer):
    """Implementation of the Xdawn Algorithm.

    Xdawn `RivetEtAl2009,RivetEtAl2011` is a spatial
    filtering method designed to improve the signal to signal + noise
    ratio (SSNR) of the ERP responses. Xdawn was originally designed for
    P300 evoked potential by enhancing the target response with respect
    to the non-target response. This implementation is a generalization
    to any type of ERP.

    Parameters
    ----------
    n_components : int, (default 2)
        The number of components to decompose the signals.
    signal_cov : None | Covariance | ndarray, shape (n_channels, n_channels)
        (default None). The signal covariance used for whitening of the data.
        if None, the covariance is estimated from the epochs signal.
    correct_overlap : 'auto' or bool (default 'auto')
        Compute the independent evoked responses per condition, while
        correcting for event overlaps if any. If 'auto', then
        overlapp_correction = True if the events do overlap.
    reg : float | str | None (default None)
        If not None (same as ``'empirical'``, default), allow
        regularization for covariance estimation.
        If float, shrinkage is used (0 <= shrinkage <= 1).
        For str options, ``reg`` will be passed as ``method`` to
        `mne.compute_covariance`.

    Attributes
    ----------
    filters_ : dict of ndarray
        If fit, the Xdawn components used to decompose the data for each event
        type, else empty. For each event type, the filters are in the rows of
        the corresponding array.
    patterns_ : dict of ndarray
        If fit, the Xdawn patterns used to restore the signals for each event
        type, else empty.
    evokeds_ : dict of Evoked
        If fit, the evoked response for each event type.
    event_id_ : dict
        The event id.
    correct_overlap_ : bool
        Whether overlap correction was applied.

    See Also
    --------
    mne.decoding.CSP, mne.decoding.SPoC

    Notes
    -----
    ✨ Added in version 0.10

    References
    ----------
    .. footbibliography::
    """

    correct_overlap: Incomplete

    def __init__(
        self,
        n_components: int = 2,
        signal_cov=None,
        correct_overlap: str = "auto",
        reg=None,
    ) -> None:
        """Init."""
        ...
    event_id_: Incomplete
    correct_overlap_: Incomplete

    def fit(self, epochs, y=None):
        """Fit Xdawn from epochs.

        Parameters
        ----------
        epochs : instance of Epochs
            An instance of Epoch on which Xdawn filters will be fitted.
        y : ndarray | None (default None)
            If None, used epochs.events[:, 2].

        Returns
        -------
        self : instance of Xdawn
            The Xdawn instance.
        """
        ...

    def transform(self, inst):
        """Apply Xdawn dim reduction.

        Parameters
        ----------
        inst : Epochs | Evoked | ndarray, shape ([n_epochs, ]n_channels, n_times)
            Data on which Xdawn filters will be applied.

        Returns
        -------
        X : ndarray, shape ([n_epochs, ]n_components * n_event_types, n_times)
            Spatially filtered signals.
        """
        ...

    def apply(self, inst, event_id=None, include=None, exclude=None):
        """Remove selected components from the signal.

        Given the unmixing matrix, transform data,
        zero out components, and inverse transform the data.
        This procedure will reconstruct the signals from which
        the dynamics described by the excluded components is subtracted.

        Parameters
        ----------
        inst : instance of Raw | Epochs | Evoked
            The data to be processed.
        event_id : dict | list of str | None (default None)
            The kind of event to apply. if None, a dict of inst will be return
            one for each type of event xdawn has been fitted.
        include : array_like of int | None (default None)
            The indices referring to columns in the ummixing matrix. The
            components to be kept. If None, the first n_components (as defined
            in the Xdawn constructor) will be kept.
        exclude : array_like of int | None (default None)
            The indices referring to columns in the ummixing matrix. The
            components to be zeroed out. If None, all the components except the
            first n_components will be exclude.

        Returns
        -------
        out : dict
            A dict of instance (from the same type as inst input) for each
            event type in event_id.
        """
        ...

    def inverse_transform(self) -> None:
        """Not implemented, see Xdawn.apply() instead."""
        ...
