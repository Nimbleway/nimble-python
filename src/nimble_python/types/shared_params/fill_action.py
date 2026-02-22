# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = ["FillAction", "Fill", "FillType", "FillPaste"]


class FillType(TypedDict, total=False):
    selector: Required[Union[str, SequenceNotStr[str]]]
    """CSS selector or array of alternative selectors.

    Use an array when you have multiple possible selectors for the same element.
    """

    value: Required[str]

    click_on_element: bool

    delay: Union[float, str]
    """Duration value that accepts various formats.

    Supports: number (ms), string ("1000"), or string with unit ("2s", "500ms",
    "2m", "1h")
    """

    mode: Literal["type"]

    mouse_movement_strategy: Literal["linear", "ghost-cursor", "windmouse"]

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

    timeout: float
    """Timeout in milliseconds.

    Set to 0 for infinite timeout (no timeout). Default: 15000ms.
    """

    typing_interval: Union[float, str]
    """Duration value that accepts various formats.

    Supports: number (ms), string ("1000"), or string with unit ("2s", "500ms",
    "2m", "1h")
    """

    typing_strategy: Literal["simple", "distribution"]

    visible: bool


class FillPaste(TypedDict, total=False):
    mode: Required[Literal["paste"]]

    selector: Required[Union[str, SequenceNotStr[str]]]
    """CSS selector or array of alternative selectors.

    Use an array when you have multiple possible selectors for the same element.
    """

    value: Required[str]

    click_on_element: bool

    delay: Union[float, str]
    """Duration value that accepts various formats.

    Supports: number (ms), string ("1000"), or string with unit ("2s", "500ms",
    "2m", "1h")
    """

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

    timeout: float
    """Timeout in milliseconds.

    Set to 0 for infinite timeout (no timeout). Default: 15000ms.
    """

    visible: bool


Fill: TypeAlias = Union[FillType, FillPaste]


class FillAction(TypedDict, total=False):
    """Fill text into an input field"""

    fill: Required[Fill]
    """Fill options with mode-specific fields.

    Use "type" mode for behavioral typing simulation, or "paste" mode for instant
    paste.
    """
