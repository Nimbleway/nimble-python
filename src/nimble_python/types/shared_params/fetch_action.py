# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["FetchAction", "Fetch", "FetchUnionMember1"]


class FetchUnionMember1(TypedDict, total=False):
    url: Required[str]

    body: str

    headers: Dict[str, str]

    method: Literal["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]

    required: Union[Literal["true", "false"], bool]
    """Whether this action is required.

    If true, pipeline stops on failure. Accepts boolean or string "true"/"false".
    Default: true.
    """

    skip: Union[Literal["true", "false"], bool]
    """Whether to skip this action.

    Accepts boolean or string "true"/"false". Default: false.
    """

    timeout: float
    """Timeout in milliseconds.

    Set to 0 for infinite timeout (no timeout). Default: 15000ms.
    """


Fetch: TypeAlias = Union[str, FetchUnionMember1]


class FetchAction(TypedDict, total=False):
    """Make an HTTP request in browser context"""

    fetch: Required[Fetch]
