# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "SearchResponse",
    "Result",
    "ResultMetadata",
    "ResultMetadataSerpMetadata",
    "ResultMetadataWsaMetadata",
    "AnswerCitation",
]


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
    with platform-specific data in additional_data and typed metadata.
    """

    content: str

    description: str

    metadata: ResultMetadata
    """Metadata for SERP-based search results (general, news, location)."""

    title: str

    url: str

    additional_data: Optional[Dict[str, object]] = None
    """Platform-specific fields (e.g., price, rating, publish_date).

    Omitted from response when no extra data.
    """


class AnswerCitation(BaseModel):
    """Citation model that maps citation markers to result indices."""

    marker: int
    """Citation marker number (e.g., 1 for [1])"""

    result_index: int
    """Zero-based index into the results array"""


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

    answer_citations: Optional[List[AnswerCitation]] = None
    """Citations mapping citation markers to result indices"""

    serp_data: Optional[Dict[str, object]] = None
    """Cleaned SERP entities (e.g.

    KnowledgeGraph, TopStory, RelatedSearch). Only present for focus='serp'.
    """
