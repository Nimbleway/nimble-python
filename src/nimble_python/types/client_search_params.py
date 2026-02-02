# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ClientSearchParams"]


class ClientSearchParams(TypedDict, total=False):
    query: Required[str]
    """Search query string"""

    content_type: Optional[SequenceNotStr[str]]
    """Filter by content type (only supported with focus=general).

    Supports semantic groups ('documents', 'spreadsheets', 'presentations') and
    specific formats ('pdf', 'docx', 'xlsx', etc.)
    """

    country: str

    deep_search: bool
    """If True, fetches and extracts full page content for each search result.

    If False, returns only metadata (title, snippet, URL)
    """

    end_date: Optional[str]
    """Filter results before this date (format: YYYY-MM-DD or YYYY)"""

    exclude_domains: Optional[SequenceNotStr[str]]
    """List of domains to exclude from search results. Maximum 50 domains."""

    include_answer: bool
    """
    Generate LLM answer summary based on search result snippets (works with both
    deep_search=True and False)
    """

    include_domains: Optional[SequenceNotStr[str]]
    """List of domains to include in search results. Maximum 50 domains."""

    locale: str

    max_subagents: int
    """
    Maximum number of subagents to execute in parallel for WSA focus modes
    (shopping, social, geo). Ignored for traditional SERP focus modes. Default: 3,
    Range: 1-5.
    """

    num_results: int
    """Maximum number of results to return (actual count may be less)"""

    parsing_type: Literal["plain_text", "markdown", "simplified_html"]
    """Output format: plain_text, markdown, or simplified_html"""

    search_engine: Optional[Literal["google_search", "google_sge", "bing_search", "yandex_search"]]
    """
    Enum representing the search engines supported by Nimble ⚠️ DEPRECATED: This
    parameter is ignored. Use 'focus' parameter instead.
    """

    start_date: Optional[str]
    """Filter results after this date (format: YYYY-MM-DD or YYYY)"""

    time_range: Optional[Literal["hour", "day", "week", "month", "year"]]
    """Time range filters passed to Webit SERP API as 'time' parameter."""

    topic: Literal["general", "news", "location", "coding", "academic", "geo", "shopping", "social"]
    """Search focus/specialization (general, news, or location)"""
