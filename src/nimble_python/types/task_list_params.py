# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TaskListParams"]


class TaskListParams(TypedDict, total=False):
    cursor: str
    """Cursor for pagination. Use the next_cursor from the previous response."""

    limit: int
    """Number of tasks to return per page."""
