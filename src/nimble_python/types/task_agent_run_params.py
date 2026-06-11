# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["TaskAgentRunParams"]


class TaskAgentRunParams(TypedDict, total=False):
    input: Required[str]

    enable_events: bool

    output_schema: Optional[Dict[str, object]]
