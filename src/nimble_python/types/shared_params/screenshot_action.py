# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ScreenshotAction", "Screenshot", "ScreenshotUnionMember1"]


class ScreenshotUnionMember1(TypedDict, total=False):
    format: Literal["png", "jpeg", "webp"]

    full_page: bool

    quality: float

    required: Union[Literal["true", "false"], bool]
    """Whether this action is required.

    If true, pipeline stops on failure. Accepts boolean or string "true"/"false".
    Default: true.
    """

    skip: Union[Literal["true", "false"], bool]
    """Whether to skip this action.

    Accepts boolean or string "true"/"false". Default: false.
    """


Screenshot: TypeAlias = Union[bool, ScreenshotUnionMember1]


class ScreenshotAction(TypedDict, total=False):
    """Capture a page screenshot"""

    screenshot: Required[Screenshot]
