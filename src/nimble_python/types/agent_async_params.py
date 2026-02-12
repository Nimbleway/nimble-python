# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["AgentAsyncParams", "ExtractTemplateBody", "AgentBody"]


class ExtractTemplateBody(TypedDict, total=False):
    params: Required[Dict[str, object]]

    template: Required[str]

    localization: bool


class AgentBody(TypedDict, total=False):
    agent: Required[str]

    params: Required[Dict[str, object]]

    localization: bool


AgentAsyncParams: TypeAlias = Union[ExtractTemplateBody, AgentBody]
