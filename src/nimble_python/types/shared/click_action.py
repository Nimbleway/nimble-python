# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["ClickAction", "Click", "ClickUnionMember2"]


class ClickUnionMember2(BaseModel):
    selector: Union[str, List[str]]
    """CSS selector or array of alternative selectors.

    Use an array when you have multiple possible selectors for the same element.
    """

    count: Optional[float] = None

    delay: Union[float, str, None] = None
    """Duration value that accepts various formats.

    Supports: number (ms), string ("1000"), or string with unit ("2s", "500ms",
    "2m", "1h")
    """

    offset_x: Optional[int] = None

    offset_y: Optional[int] = None

    required: Union[Literal["true", "false"], bool, None] = None
    """Whether this action is required.

    If true, pipeline stops on failure. Accepts boolean or string "true"/"false".
    Default: true.
    """

    scroll: Optional[bool] = None

    skip: Union[Literal["true", "false"], bool, None] = None
    """Whether to skip this action.

    Accepts boolean or string "true"/"false". Default: false.
    """

    steps: Optional[float] = None

    strategy: Optional[Literal["linear", "ghost-cursor", "windmouse"]] = None

    timeout: Optional[float] = None
    """Timeout in milliseconds.

    Set to 0 for infinite timeout (no timeout). Default: 15000ms.
    """

    visible: Optional[bool] = None


Click: TypeAlias = Union[str, List[str], ClickUnionMember2]


class ClickAction(BaseModel):
    """Click on an element by selector"""

    click: Click
