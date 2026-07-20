# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TemplateBatchParams", "Input", "SharedInputs"]


class TemplateBatchParams(TypedDict, total=False):
    inputs: Required[Iterable[Input]]

    shared_inputs: Required[SharedInputs]


class Input(TypedDict, total=False):
    formats: List[Literal["html", "markdown", "screenshot", "headers", "links"]]
    """Response formats to include. All disabled by default."""

    localization: bool

    params: Dict[str, object]


class SharedInputs(TypedDict, total=False):
    template: Required[str]

    formats: List[Literal["html", "markdown", "screenshot", "headers", "links"]]
    """Response formats to include. All disabled by default."""

    localization: bool

    params: Dict[str, object]
