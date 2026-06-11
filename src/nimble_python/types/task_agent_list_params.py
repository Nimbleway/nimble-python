# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["TaskAgentListParams"]


class TaskAgentListParams(TypedDict, total=False):
    effort: Optional[str]

    limit: int

    offset: int

    use_case: Optional[str]
