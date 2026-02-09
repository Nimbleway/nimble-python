# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["AgentListResponse", "AgentListResponseItem"]


class AgentListResponseItem(BaseModel):
    display_name: str

    is_public: bool

    name: str

    description: Optional[str] = None

    domain: Optional[str] = None

    entity_type: Optional[str] = None

    vertical: Optional[str] = None


AgentListResponse: TypeAlias = List[AgentListResponseItem]
