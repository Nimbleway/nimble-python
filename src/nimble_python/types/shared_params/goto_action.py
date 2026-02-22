# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["GotoAction", "Goto", "GotoUnionMember1"]


class GotoUnionMember1(TypedDict, total=False):
    url: Required[str]

    referer: str

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

    wait_until: Literal["load", "domcontentloaded", "networkidle0", "networkidle2"]


Goto: TypeAlias = Union[str, GotoUnionMember1]


class GotoAction(TypedDict, total=False):
    """Navigate to a URL"""

    goto: Required[Goto]
