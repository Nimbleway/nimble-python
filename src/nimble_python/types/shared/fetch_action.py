# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["FetchAction", "Fetch", "FetchUnionMember1"]


class FetchUnionMember1(BaseModel):
    url: str

    body: Optional[str] = None

    headers: Optional[Dict[str, str]] = None

    method: Optional[Literal["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]] = None

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


Fetch: TypeAlias = Union[str, FetchUnionMember1]


class FetchAction(BaseModel):
    """Make an HTTP request in browser context"""

    fetch: Fetch
