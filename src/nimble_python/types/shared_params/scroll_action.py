# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ScrollAction", "Scroll", "ScrollUnionMember2"]


class ScrollUnionMember2(TypedDict, total=False):
    container: Union[str, SequenceNotStr[str]]
    """CSS selector or array of alternative selectors.

    Use an array when you have multiple possible selectors for the same element.
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

    to: Union[str, SequenceNotStr[str]]
    """CSS selector or array of alternative selectors.

    Use an array when you have multiple possible selectors for the same element.
    """

    visible: bool

    x: float

    y: float


Scroll: TypeAlias = Union[float, str, ScrollUnionMember2]


class ScrollAction(TypedDict, total=False):
    """Scroll the page or an element"""

    scroll: Required[Scroll]
