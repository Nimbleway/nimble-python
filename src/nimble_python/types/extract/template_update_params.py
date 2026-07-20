# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TemplateUpdateParams", "Body"]


class TemplateUpdateParams(TypedDict, total=False):
    body: Required[Iterable[Body]]
    """A JSON Patch document per RFC 6902 — a JSON array of patch operations."""


_BodyReservedKeywords = TypedDict(
    "_BodyReservedKeywords",
    {
        "from": Optional[str],
    },
    total=False,
)


class Body(_BodyReservedKeywords, total=False):
    """A single JSON Patch operation per RFC 6902."""

    op: Required[Literal["add", "remove", "replace", "move", "copy", "test"]]

    path: Required[str]

    value: object
