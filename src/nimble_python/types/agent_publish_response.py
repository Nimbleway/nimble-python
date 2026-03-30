# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AgentPublishResponse"]


class AgentPublishResponse(BaseModel):
    agent_name: str

    published_version_id: str
