# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["MediaRunAsyncParams", "Storage"]


class MediaRunAsyncParams(TypedDict, total=False):
    url: Required[str]

    callback_url: str
    """URL to call back when async operation completes"""

    country: str

    expected_mime_types: SequenceNotStr[str]

    locale: str

    storage: Storage

    storage_compress: bool
    """Whether to compress stored data"""

    storage_object_name: str
    """Custom name for the stored object"""

    storage_type: str
    """Type of storage to use for results"""

    storage_url: str
    """URL for storage location"""


class Storage(TypedDict, total=False):
    url: Required[str]

    object_name: str

    type: Literal["s3", "gcs", "do", "oci"]
