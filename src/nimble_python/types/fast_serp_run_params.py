# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FastSerpRunParams"]


class FastSerpRunParams(TypedDict, total=False):
    search_engine: Required[
        Literal[
            "google_search",
            "google_sge",
            "google_aio",
            "google_maps_search",
            "google_maps_reviews",
            "google_maps_place",
            "google_news",
            "google_images",
            "bing_search",
            "yandex_search",
        ]
    ]
    """The search engine to query."""

    country: str
    """ISO Alpha-2 country code used to access the target search engine (e.g.

    US, DE, GB).
    """

    device: Literal["desktop", "mobile"]
    """Device type used for the search request."""

    domain: str
    """Top-level domain for the search engine (e.g. "com", "co.uk", "de")."""

    locale: str
    """Locale used for the search request."""

    location: str
    """Geo-location for the search (canonical Google location name)."""

    num_results: int
    """Number of results to return (1–100)."""

    page: int
    """The result page number for pagination."""

    parse: bool
    """When true, the SERP response is parsed into structured JSON."""

    query: str
    """The search keyword or phrase to query."""

    render: bool
    """Whether to render the page in a browser before extracting."""

    resolve_url: bool
    """
    When true, search result links that point at a search-engine redirector are
    resolved to their final destination URLs. Best-effort within a time budget:
    links that cannot be resolved in time are returned unchanged.
    """

    show_hidden_results: bool
    """
    When true, disables Google result filtering (filter=0) so omitted/duplicate and
    highly similar pages are also returned. Applies to Google search engines.
    """
