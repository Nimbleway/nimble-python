# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TemplateAsyncParams"]


class TemplateAsyncParams(TypedDict, total=False):
    params: Required[Dict[str, object]]

    template: Required[str]

    callback_url: str
    """URL to call back when async operation completes"""

    formats: List[Literal["html", "markdown", "screenshot", "headers", "links"]]
    """Response formats to include. All disabled by default."""

    localization: bool

    storage_compress: bool
    """Whether to compress stored data"""

    storage_object_name: str
    """Custom name for the stored object"""

    storage_type: str
    """Type of storage to use for results"""

    storage_url: str
    """URL for storage location"""
