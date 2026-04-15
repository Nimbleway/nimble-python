# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AgentRunParams"]


class AgentRunParams(TypedDict, total=False):
    agent: Required[str]

    params: Required[Dict[str, object]]

    formats: List[Literal["html", "markdown", "screenshot", "headers", "links"]]
    """Response formats to include. All disabled by default."""

    localization: bool
