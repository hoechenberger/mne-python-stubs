from _typeshed import Incomplete

class TransformerMixin:
    """Fit to data, then transform it.

        Fits transformer to ``X`` and ``y`` with optional parameters
        ``fit_params``, and returns a transformed version of ``X``.

        Parameters
        ----------
        X : array, shape (n_samples, n_features)
            Training set.
        y : array, shape (n_samples,)
            Target values or class labels.
        **fit_params : dict
            Additional fitting parameters passed to the ``fit`` method..

        Returns
        -------
        X_new : array, shape (n_samples, n_features_new)
            Transformed array.
        """

    def fit_transform(self, X, y: Incomplete | None=..., **fit_params):
        """Fit to data, then transform it.

        Fits transformer to ``X`` and ``y`` with optional parameters
        ``fit_params``, and returns a transformed version of ``X``.

        Parameters
        ----------
        X : array, shape (n_samples, n_features)
            Training set.
        y : array, shape (n_samples,)
            Target values or class labels.
        **fit_params : dict
            Additional fitting parameters passed to the ``fit`` method..

        Returns
        -------
        X_new : array, shape (n_samples, n_features_new)
            Transformed array.
        """

class EstimatorMixin:
    """Set parameters (mimics sklearn API).

        Parameters
        ----------
        **params : dict
            Extra parameters.

        Returns
        -------
        inst : object
            The instance.
        """

    def get_params(self, deep: bool=...) -> None:
        """Get the estimator params.

        Parameters
        ----------
        deep : bool
            Deep.
        """

    def set_params(self, **params):
        """Set parameters (mimics sklearn API).

        Parameters
        ----------
        **params : dict
            Extra parameters.

        Returns
        -------
        inst : object
            The instance.
        """