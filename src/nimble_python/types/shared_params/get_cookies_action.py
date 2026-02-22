# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["GetCookiesAction", "GetCookies", "GetCookiesUnionMember1"]


class GetCookiesUnionMember1Typed(TypedDict, total=False):
    required: Union[Literal["true", "false"], bool]
    """Whether this action is required.

    If true, pipeline stops on failure. Accepts boolean or string "true"/"false".
    Default: true.
    """

    skip: Union[Literal["true", "false"], bool]
    """Whether to skip this action.

    Accepts boolean or string "true"/"false". Default: false.
    """


GetCookiesUnionMember1: TypeAlias = Union[GetCookiesUnionMember1Typed, Dict[str, object]]

GetCookies: TypeAlias = Union[bool, GetCookiesUnionMember1]


class GetCookiesAction(TypedDict, total=False):
    """Retrieve browser cookies"""

    get_cookies: Required[GetCookies]
