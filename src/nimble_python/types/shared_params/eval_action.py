# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["EvalAction", "Eval", "EvalUnionMember1"]


class EvalUnionMember1(TypedDict, total=False):
    code: Required[str]

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


Eval: TypeAlias = Union[str, EvalUnionMember1]


class EvalAction(TypedDict, total=False):
    """Execute JavaScript code in page context"""

    eval: Required[Eval]
