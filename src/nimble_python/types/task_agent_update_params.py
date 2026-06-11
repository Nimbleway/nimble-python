# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TaskAgentUpdateParams", "Body"]


class TaskAgentUpdateParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    op: Required[Literal["replace"]]

    path: Required[str]

    value: Required[object]
