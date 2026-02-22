# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["ScrollAction", "Scroll", "ScrollUnionMember2"]


class ScrollUnionMember2(BaseModel):
    container: Union[str, List[str], None] = None
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

    to: Union[str, List[str], None] = None
    """CSS selector or array of alternative selectors.

    Use an array when you have multiple possible selectors for the same element.
    """

    visible: Optional[bool] = None

    x: Optional[float] = None

    y: Optional[float] = None


Scroll: TypeAlias = Union[float, str, ScrollUnionMember2]


class ScrollAction(BaseModel):
    """Scroll the page or an element"""

    scroll: Scroll
