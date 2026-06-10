# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["MediaRunParams", "Storage"]


class MediaRunParams(TypedDict, total=False):
    url: Required[str]

    country: str

    expected_mime_types: SequenceNotStr[str]

    locale: str

    storage: Storage


class Storage(TypedDict, total=False):
    url: Required[str]

    object_name: str

    type: Literal["s3", "gcs", "do", "oci"]
