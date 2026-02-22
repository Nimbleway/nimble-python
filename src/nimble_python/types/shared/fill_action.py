# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = ["FillAction", "Fill", "FillType", "FillPaste"]


class FillType(BaseModel):
    selector: Union[str, List[str]]
    """CSS selector or array of alternative selectors.

    Use an array when you have multiple possible selectors for the same element.
    """

    value: str

    click_on_element: Optional[bool] = None

    delay: Union[float, str, None] = None
    """Duration value that accepts various formats.

    Supports: number (ms), string ("1000"), or string with unit ("2s", "500ms",
    "2m", "1h")
    """

    mode: Optional[Literal["type"]] = None

    mouse_movement_strategy: Optional[Literal["linear", "ghost-cursor", "windmouse"]] = None

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

    timeout: Optional[float] = None
    """Timeout in milliseconds.

    Set to 0 for infinite timeout (no timeout). Default: 15000ms.
    """

    typing_interval: Union[float, str, None] = None
    """Duration value that accepts various formats.

    Supports: number (ms), string ("1000"), or string with unit ("2s", "500ms",
    "2m", "1h")
    """

    typing_strategy: Optional[Literal["simple", "distribution"]] = None

    visible: Optional[bool] = None


class FillPaste(BaseModel):
    mode: Literal["paste"]

    selector: Union[str, List[str]]
    """CSS selector or array of alternative selectors.

    Use an array when you have multiple possible selectors for the same element.
    """

    value: str

    click_on_element: Optional[bool] = None

    delay: Union[float, str, None] = None
    """Duration value that accepts various formats.

    Supports: number (ms), string ("1000"), or string with unit ("2s", "500ms",
    "2m", "1h")
    """

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

    timeout: Optional[float] = None
    """Timeout in milliseconds.

    Set to 0 for infinite timeout (no timeout). Default: 15000ms.
    """

    visible: Optional[bool] = None


Fill: TypeAlias = Annotated[Union[FillType, FillPaste], PropertyInfo(discriminator="mode")]


class FillAction(BaseModel):
    """Fill text into an input field"""

    fill: Fill
    """Fill options with mode-specific fields.

    Use "type" mode for behavioral typing simulation, or "paste" mode for instant
    paste.
    """
