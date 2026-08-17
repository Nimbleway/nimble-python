# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
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
    """Country code for geo-targeted results (e.g., 'US', 'GB', 'IL')"""

    deep_search: Optional[bool]
    """Deprecated.

    Use search_depth instead. true maps to 'deep', false maps to 'lite'.
    """

    end_date: Optional[str]
    """Filter results before this date (format: YYYY-MM-DD or YYYY)"""

    exclude_domains: Optional[SequenceNotStr[str]]
    """List of domains to exclude from search results. Maximum 50 domains."""

    focus: Union[str, SequenceNotStr[str]]
    """
    Search focus mode (e.g., 'general', 'news', 'shopping') or a list of explicit
    subagent names (e.g., ['amazon_serp', 'target_serp'])
    """

    full_content: bool
    """Return richer per-result content on the fast path.

    With search_depth='fast', enables live crawling of both web and news sources so
    results carry full markdown content instead of snippets only. Higher recall and
    cost. Ignored for other search_depth values.
    """

    include_answer: bool
    """Generate an LLM-powered answer summary based on search result snippets."""

    include_domains: Optional[SequenceNotStr[str]]
    """List of domains to include in search results. Maximum 50 domains."""

    locale: str
    """Language/locale code (e.g., 'en', 'fr', 'de')"""

    max_results: int
    """Maximum number of results to return.

    Actual count may be lower depending on availability.
    """

    max_subagents: int
    """
    Maximum number of subagents to execute in parallel for WSA focus modes
    (shopping, social, geo). Ignored for SERP focus modes.
    """

    output_format: Literal["plain_text", "markdown", "simplified_html"]
    """Output format: plain_text, markdown, or simplified_html"""

    search_depth: Optional[Literal["lite", "fast", "deep"]]
    """Controls content richness and latency of search results.

    - lite: Token-efficient metadata for high-volume pipelines (title, URL,
      description only)
    - fast: Rich content (~2K chars) optimized for AI agents
    - deep: Full page content via Webit scraping for comprehensive analysis
    """

    start_date: Optional[str]
    """Filter results after this date (format: YYYY-MM-DD or YYYY)"""

    time_range: Optional[Literal["hour", "day", "week", "month", "year"]]
    """Time range filters passed to Webit SERP API as 'time' parameter."""
