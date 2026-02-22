# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ClickAction", "Click", "ClickUnionMember2"]


class ClickUnionMember2(TypedDict, total=False):
    selector: Required[Union[str, SequenceNotStr[str]]]
    """CSS selector or array of alternative selectors.

    Use an array when you have multiple possible selectors for the same element.
    """

    count: float

    delay: Union[float, str]
    """Duration value that accepts various formats.

    Supports: number (ms), string ("1000"), or string with unit ("2s", "500ms",
    "2m", "1h")
    """

    offset_x: int

    offset_y: int

    required: Union[Literal["true", "false"], bool]
    """Whether this action is required.

    If true, pipeline stops on failure. Accepts boolean or string "true"/"false".
    Default: true.
    """

    scroll: bool

    skip: Union[Literal["true", "false"], bool]
    """Whether to skip this action.

    Accepts boolean or string "true"/"false". Default: false.
    """

    steps: float

    strategy: Literal["linear", "ghost-cursor", "windmouse"]

    timeout: float
    """Timeout in milliseconds.

    Set to 0 for infinite timeout (no timeout). Default: 15000ms.
    """

    visible: bool


Click: TypeAlias = Union[str, SequenceNotStr[str], ClickUnionMember2]


class ClickAction(TypedDict, total=False):
    """Click on an element by selector"""

    click: Required[Click]
