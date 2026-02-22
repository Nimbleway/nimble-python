# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["WaitForNavigationAction", "WaitForNavigation", "WaitForNavigationUnionMember1"]


class WaitForNavigationUnionMember1(TypedDict, total=False):
    navigation: Required[Literal["load", "domcontentloaded", "networkidle0", "networkidle2"]]

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


WaitForNavigation: TypeAlias = Union[
    Literal["load", "domcontentloaded", "networkidle0", "networkidle2"], WaitForNavigationUnionMember1
]


class WaitForNavigationAction(TypedDict, total=False):
    """Wait for page navigation to complete"""

    wait_for_navigation: Required[WaitForNavigation]
