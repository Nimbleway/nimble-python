# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["TaskAgentRunParams", "Sources", "SourcesAllow", "SourcesBlock"]


class TaskAgentRunParams(TypedDict, total=False):
    input: Required[str]

    enable_events: bool

    output_schema: Optional[Dict[str, object]]

    sources: Optional[Sources]


class SourcesAllow(TypedDict, total=False):
    domains: Required[SequenceNotStr[str]]

    title: Required[str]

    order: int


class SourcesBlock(TypedDict, total=False):
    domains: Required[SequenceNotStr[str]]

    title: Required[str]

    order: int


class Sources(TypedDict, total=False):
    allow: Iterable[SourcesAllow]

    avoid: Optional[str]

    block: Iterable[SourcesBlock]

    prioritize: Optional[str]
