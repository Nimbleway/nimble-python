# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["AutoScrollAction", "AutoScroll", "AutoScrollUnionMember3"]


class AutoScrollUnionMember3(BaseModel):
    click_selector: Union[str, List[str], None] = None
    """CSS selector or array of alternative selectors.

    Use an array when you have multiple possible selectors for the same element.
    """

    container: Union[str, List[str], None] = None
    """CSS selector or array of alternative selectors.

    Use an array when you have multiple possible selectors for the same element.
    """

    delay_after_scroll: Union[float, str, None] = None
    """Duration value that accepts various formats.

    Supports: number (ms), string ("1000"), or string with unit ("2s", "500ms",
    "2m", "1h")
    """

    idle_timeout: Union[float, str, None] = None
    """Duration value that accepts various formats.

    Supports: number (ms), string ("1000"), or string with unit ("2s", "500ms",
    "2m", "1h")
    """

    loading_selector: Union[str, List[str], None] = None
    """CSS selector or array of alternative selectors.

    Use an array when you have multiple possible selectors for the same element.
    """

    max_duration: Union[float, str, None] = None
    """Duration value that accepts various formats.

    Supports: number (ms), string ("1000"), or string with unit ("2s", "500ms",
    "2m", "1h")
    """

    pause_on_selector: Union[str, List[str], None] = None
    """CSS selector or array of alternative selectors.

    Use an array when you have multiple possible selectors for the same element.
    """

    required: Union[Literal["true", "false"], bool, None] = None
    """Whether this action is required.

    If true, pipeline stops on failure. Accepts boolean or string "true"/"false".
    Default: true.
    """

    skip: Union[Literal["true", "false"], bool, None] = None
    """Whether to skip this action.

    Accepts boolean or string "true"/"false". Default: false.
    """

    step_size: Optional[float] = None


AutoScroll: TypeAlias = Union[bool, float, str, AutoScrollUnionMember3]


class AutoScrollAction(BaseModel):
    """Continuously scroll to load dynamic content"""

    auto_scroll: AutoScroll
