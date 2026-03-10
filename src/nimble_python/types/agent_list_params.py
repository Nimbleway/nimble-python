# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["AgentListParams"]


class AgentListParams(TypedDict, total=False):
    limit: int
    """Number of results per page"""

    managed_by: Optional[Literal["nimble", "community", "self_managed"]]
    """Filter templates by attribution"""

    offset: int
    """Pagination offset"""

    privacy: Optional[Literal["public", "private", "all"]]
    """Filter by privacy level"""

    search: Optional[str]
    """Search templates by name, domain, or vertical"""
