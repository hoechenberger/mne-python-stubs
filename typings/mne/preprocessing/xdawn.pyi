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

    n_components: Incomplete
    signal_cov: Incomplete
    reg: Incomplete
    method_params: Incomplete

    def __init__(
        self, n_components: int = ..., reg=..., signal_cov=..., method_params=...
    ) -> None:
        """Init."""
    classes_: Incomplete

    def fit(self, X, y=...):
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

class Xdawn(_XdawnTransformer):
    """Not implemented, see Xdawn.apply() instead."""

    correct_overlap: Incomplete

    def __init__(
        self,
        n_components: int = ...,
        signal_cov=...,
        correct_overlap: str = ...,
        reg=...,
    ) -> None:
        """Init."""
    event_id_: Incomplete
    correct_overlap_: Incomplete

    def fit(self, epochs, y=...):
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
    def apply(self, inst, event_id=..., include=..., exclude=...):
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
    def inverse_transform(self) -> None:
        """Not implemented, see Xdawn.apply() instead."""
