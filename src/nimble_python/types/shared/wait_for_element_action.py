# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["WaitForElementAction", "WaitForElement", "WaitForElementUnionMember2"]


class WaitForElementUnionMember2(BaseModel):
    selector: Union[str, List[str]]
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

    timeout: Optional[float] = None
    """Timeout in milliseconds.

    Set to 0 for infinite timeout (no timeout). Default: 15000ms.
    """

    visible: Optional[bool] = None


WaitForElement: TypeAlias = Union[str, List[str], WaitForElementUnionMember2]


class WaitForElementAction(BaseModel):
    """Wait for an element to appear or reach a specific state"""

    wait_for_element: WaitForElement
