# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["ScreenshotAction", "Screenshot", "ScreenshotUnionMember1"]


class ScreenshotUnionMember1(BaseModel):
    format: Optional[Literal["png", "jpeg", "webp"]] = None

    full_page: Optional[bool] = None

    quality: Optional[float] = None

    required: Union[Literal["true", "false"], bool, None] = None
    """Whether this action is required.

    If true, pipeline stops on failure. Accepts boolean or string "true"/"false".
    Default: true.
    """

    skip: Union[Literal["true", "false"], bool, None] = None
    """Whether to skip this action.

    Accepts boolean or string "true"/"false". Default: false.
    """


Screenshot: TypeAlias = Union[bool, ScreenshotUnionMember1]


class ScreenshotAction(BaseModel):
    """Capture a page screenshot"""

    screenshot: Screenshot
