# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["DomainKnowledgeGetDriverResponse"]


class DomainKnowledgeGetDriverResponse(BaseModel):
    antibots: List[str]
    """List of detected antibots for the domain"""

    description: str
    """Description of the driver"""

    driver: str
    """Resolved driver name"""

    agent: Optional[str] = None
    """The input agent name (present when agent query param was used)"""

    need_to_render: Optional[bool] = None
    """Whether the page needs to be rendered to be properly resolved."""

    url: Optional[str] = None
    """The input URL (present when url query param was used)"""
