# -*- coding: utf-8 -*-
"""Collection of exceptions raised by requests-toolbelt."""


class StreamingError(Exception):
    """Used in :mod:`requests_toolbelt.downloadutils.stream`."""
    pass


class VersionMismatchError(Exception):
    """Used to indicate a version mismatch in the version of requests required.

    The feature in use requires a newer version of Requests to function
    appropriately but the version installed is not sufficient.
    """
    pass


class RequestsVersionTooOld(Warning):
    """Used to indiciate that the Requests version is too old.

    If the version of Requests is too old to support a feature, we will issue
    this warning to the user.
    """
    pass


class IgnoringCertificateValidation(Warning):
    """Used to indiciate that the user has tried to specify certificate
    validation but it will be ignored (validation will remain off).

    In :class:`requests_toolbelt.adapters.appengine.InsecureAppEngineAdapter`.
    """
    pass
