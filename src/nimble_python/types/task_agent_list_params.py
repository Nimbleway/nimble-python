# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["TaskAgentListParams"]


class TaskAgentListParams(TypedDict, total=False):
    filter_effort: Optional[Literal["low", "medium", "high", "x-high", "max"]]
    """Canonical effort tier names for the research graph."""

    filter_use_case: Optional[Literal["research", "enrichment", "dataset_building"]]

    limit: int

    offset: int

    workspace_id: Optional[str]
