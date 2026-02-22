# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["EvalAction", "Eval", "EvalUnionMember1"]


class EvalUnionMember1(BaseModel):
    code: str

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


Eval: TypeAlias = Union[str, EvalUnionMember1]


class EvalAction(BaseModel):
    """Execute JavaScript code in page context"""

    eval: Eval
