# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["WaitAction", "Wait", "WaitUnionMember2"]


class WaitUnionMember2(TypedDict, total=False):
    duration: Required[Union[float, str]]
    """Duration value that accepts various formats.

    Supports: number (ms), string ("1000"), or string with unit ("2s", "500ms",
    "2m", "1h")
    """

    required: Union[Literal["true", "false"], bool]
    """Whether this action is required.

    If true, pipeline stops on failure. Accepts boolean or string "true"/"false".
    Default: true.
    """

    skip: Union[Literal["true", "false"], bool]
    """Whether to skip this action.

    Accepts boolean or string "true"/"false". Default: false.
    """


Wait: TypeAlias = Union[float, str, WaitUnionMember2]


class WaitAction(TypedDict, total=False):
    """Wait for a specified duration"""

    wait: Required[Wait]
