# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = ["WaitForElementAction", "WaitForElement", "WaitForElementUnionMember2"]


class WaitForElementUnionMember2(TypedDict, total=False):
    selector: Required[Union[str, SequenceNotStr[str]]]
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

    timeout: float
    """Timeout in milliseconds.

    Set to 0 for infinite timeout (no timeout). Default: 15000ms.
    """

    visible: bool


WaitForElement: TypeAlias = Union[str, SequenceNotStr[str], WaitForElementUnionMember2]


class WaitForElementAction(TypedDict, total=False):
    """Wait for an element to appear or reach a specific state"""

    wait_for_element: Required[WaitForElement]
