# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ClientAgentParams"]


class ClientAgentParams(TypedDict, total=False):
    agent: Required[str]

    params: Required[Dict[str, object]]

    localization: bool
