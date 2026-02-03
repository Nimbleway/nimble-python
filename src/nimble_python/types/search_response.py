# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["SearchResponse", "Result", "ResultMetadata", "ResultMetadataSerpMetadata", "ResultMetadataWsaMetadata"]


class ResultMetadataSerpMetadata(BaseModel):
    """Metadata for SERP-based search results (general, news, location)."""

    country: str

    entity_type: str

    locale: str

    position: int

    driver: Optional[str] = None


class ResultMetadataWsaMetadata(BaseModel):
    """Metadata for WSA-based search results."""

    agent_name: str


ResultMetadata: TypeAlias = Union[ResultMetadataSerpMetadata, ResultMetadataWsaMetadata]


class Result(BaseModel):
    """Unified result model for all search types (SERP and WSA).

    This model provides a consistent structure for search results,
    with platform-specific data in extra_fields and typed metadata.
    """

    content: str

    description: str

    metadata: ResultMetadata
    """Metadata for SERP-based search results (general, news, location)."""

    title: str

    url: str

    extra_fields: Optional[Dict[str, object]] = None


class SearchResponse(BaseModel):
    """Response model from SearchService with results and optional LLM answer.

    Note: request_id is always a valid UUID generated internally by the middleware,
    so no validation is needed.
    """

    request_id: str
    """Unique identifier for this request (UUID)"""

    results: List[Result]

    total_results: int
    """Number of results returned"""

    answer: Optional[str] = None
