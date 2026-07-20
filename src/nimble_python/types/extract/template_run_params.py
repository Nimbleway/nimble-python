# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TemplateRunParams"]


class TemplateRunParams(TypedDict, total=False):
    params: Required[Dict[str, object]]

    template: Required[str]

    formats: List[Literal["html", "markdown", "screenshot", "headers", "links"]]
    """Response formats to include. All disabled by default."""

    localization: bool
