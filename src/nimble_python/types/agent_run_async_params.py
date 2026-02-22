# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["AgentRunAsyncParams"]


class AgentRunAsyncParams(TypedDict, total=False):
    agent: Required[str]

    params: Required[Dict[str, object]]

    callback_url: str
    """URL to call back when async operation completes"""

    localization: bool

    storage_compress: bool
    """Whether to compress stored data"""

    storage_object_name: str
    """Custom name for the stored object"""

    storage_type: str
    """Type of storage to use for results"""

    storage_url: str
    """URL for storage location"""
