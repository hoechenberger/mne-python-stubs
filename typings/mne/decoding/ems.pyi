from .._fiff.pick import pick_info as pick_info, pick_types as pick_types
from ..parallel import parallel_func as parallel_func
from ..utils import logger as logger
from .mixin import (
    EstimatorMixin as EstimatorMixin,
    TransformerMixin as TransformerMixin,
)
from _typeshed import Incomplete

class EMS(TransformerMixin, EstimatorMixin):
    """Transformer to compute event-matched spatial filters.

    This version of EMS :footcite:`SchurgerEtAl2013` operates on the entire
    time course. No time
    window needs to be specified. The result is a spatial filter at each
    time point and a corresponding time course. Intuitively, the result
    gives the similarity between the filter at each time point and the
    data vector (sensors) at that time point.

    .. note:: EMS only works for binary classification.

    Attributes
    ----------
    filters_ : ndarray, shape (n_channels, n_times)
        The set of spatial filters.
    classes_ : ndarray, shape (n_classes,)
        The target classes.

    References
    ----------
    .. footbibliography::
    """

    classes_: Incomplete
    filters_: Incomplete

    def fit(self, X, y):
        """Fit the spatial filters.

        .. note : EMS is fitted on data normalized by channel type before the
                  fitting of the spatial filters.

        Parameters
        ----------
        X : array, shape (n_epochs, n_channels, n_times)
            The training data.
        y : array of int, shape (n_epochs)
            The target classes.

        Returns
        -------
        self : instance of EMS
            Returns self.
        """
        ...
    def transform(self, X):
        """Transform the data by the spatial filters.

        Parameters
        ----------
        X : array, shape (n_epochs, n_channels, n_times)
            The input data.

        Returns
        -------
        X : array, shape (n_epochs, n_times)
            The input data transformed by the spatial filters.
        """
        ...

def compute_ems(
    epochs, conditions=None, picks=None, n_jobs=None, cv=None, verbose=None
):
    """Compute event-matched spatial filter on epochs.

    This version of EMS :footcite:`SchurgerEtAl2013` operates on the entire
    time course. No time
    window needs to be specified. The result is a spatial filter at each
    time point and a corresponding time course. Intuitively, the result
    gives the similarity between the filter at each time point and the
    data vector (sensors) at that time point.

    .. note : EMS only works for binary classification.

    .. note : The present function applies a leave-one-out cross-validation,
              following Schurger et al's paper. However, we recommend using
              a stratified k-fold cross-validation. Indeed, leave-one-out tends
              to overfit and cannot be used to estimate the variance of the
              prediction within a given fold.

    .. note : Because of the leave-one-out, this function needs an equal
              number of epochs in each of the two conditions.

    Parameters
    ----------
    epochs : instance of mne.Epochs
        The epochs.
    conditions : list of str | None, default None
        If a list of strings, strings must match the epochs.event_id's key as
        well as the number of conditions supported by the objective_function.
        If None keys in epochs.event_id are used.
    picks : str | array-like | slice | None
        Channels to include. Slices and lists of integers will be interpreted as
        channel indices. In lists, channel *type* strings (e.g., ``['meg',
        'eeg']``) will pick channels of those types, channel *name* strings (e.g.,
        ``['MEG0111', 'MEG2623']`` will pick the given channels. Can also be the
        string values "all" to pick all channels, or "data" to pick :term:`data
        channels`. None (default) will pick good data channels. Note that channels
        in ``info['bads']`` *will be included* if their names or indices are
        explicitly provided.
    n_jobs : int | None
        The number of jobs to run in parallel. If ``-1``, it is set
        to the number of CPU cores. Requires the `joblib` package.
        ``None`` (default) is a marker for 'unset' that will be interpreted
        as ``n_jobs=1`` (sequential execution) unless the call is performed under
        a `joblib:joblib.parallel_config` context manager that sets another
        value for ``n_jobs``.
    cv : cross-validation object | str | None, default LeaveOneOut
        The cross-validation scheme.

    verbose : bool | str | int | None
        Control verbosity of the logging output. If ``None``, use the default
        verbosity level. See the :ref:`logging documentation <tut-logging>` and
        `mne.verbose` for details. Should only be passed as a keyword
        argument.

    Returns
    -------
    surrogate_trials : ndarray, shape (n_trials // 2, n_times)
        The trial surrogates.
    mean_spatial_filter : ndarray, shape (n_channels, n_times)
        The set of spatial filters.
    conditions : ndarray, shape (n_classes,)
        The conditions used. Values correspond to original event ids.

    References
    ----------
    .. footbibliography::
    """
    ...
