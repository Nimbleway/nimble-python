# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import fast_serp_run_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.fast_serp_run_response import FastSerpRunResponse

__all__ = ["FastSerpResource", "AsyncFastSerpResource"]


class FastSerpResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FastSerpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Nimbleway/nimble-python#accessing-raw-response-data-eg-headers
        """
        return FastSerpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FastSerpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Nimbleway/nimble-python#with_streaming_response
        """
        return FastSerpResourceWithStreamingResponse(self)

    def run(
        self,
        *,
        search_engine: Literal[
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
        ],
        country: str | Omit = omit,
        device: Literal["desktop", "mobile"] | Omit = omit,
        domain: str | Omit = omit,
        locale: str | Omit = omit,
        location: str | Omit = omit,
        num_results: int | Omit = omit,
        page: int | Omit = omit,
        parse: bool | Omit = omit,
        query: str | Omit = omit,
        render: bool | Omit = omit,
        resolve_url: bool | Omit = omit,
        show_hidden_results: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FastSerpRunResponse:
        """
        Fast SERP

        Args:
          search_engine: The search engine to query.

          country: ISO Alpha-2 country code used to access the target search engine (e.g. US, DE,
              GB).

          device: Device type used for the search request.

          domain: Top-level domain for the search engine (e.g. "com", "co.uk", "de").

          locale: Locale used for the search request.

          location: Geo-location for the search (canonical Google location name).

          num_results: Number of results to return (1–100).

          page: The result page number for pagination.

          parse: When true, the SERP response is parsed into structured JSON.

          query: The search keyword or phrase to query.

          render: Whether to render the page in a browser before extracting.

          resolve_url: When true, search result links that point at a search-engine redirector are
              resolved to their final destination URLs. Best-effort within a time budget:
              links that cannot be resolved in time are returned unchanged.

          show_hidden_results: When true, disables Google result filtering (filter=0) so omitted/duplicate and
              highly similar pages are also returned. Applies to Google search engines.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/fast-serp",
            body=maybe_transform(
                {
                    "search_engine": search_engine,
                    "country": country,
                    "device": device,
                    "domain": domain,
                    "locale": locale,
                    "location": location,
                    "num_results": num_results,
                    "page": page,
                    "parse": parse,
                    "query": query,
                    "render": render,
                    "resolve_url": resolve_url,
                    "show_hidden_results": show_hidden_results,
                },
                fast_serp_run_params.FastSerpRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FastSerpRunResponse,
        )


class AsyncFastSerpResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFastSerpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Nimbleway/nimble-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFastSerpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFastSerpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Nimbleway/nimble-python#with_streaming_response
        """
        return AsyncFastSerpResourceWithStreamingResponse(self)

    async def run(
        self,
        *,
        search_engine: Literal[
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
        ],
        country: str | Omit = omit,
        device: Literal["desktop", "mobile"] | Omit = omit,
        domain: str | Omit = omit,
        locale: str | Omit = omit,
        location: str | Omit = omit,
        num_results: int | Omit = omit,
        page: int | Omit = omit,
        parse: bool | Omit = omit,
        query: str | Omit = omit,
        render: bool | Omit = omit,
        resolve_url: bool | Omit = omit,
        show_hidden_results: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FastSerpRunResponse:
        """
        Fast SERP

        Args:
          search_engine: The search engine to query.

          country: ISO Alpha-2 country code used to access the target search engine (e.g. US, DE,
              GB).

          device: Device type used for the search request.

          domain: Top-level domain for the search engine (e.g. "com", "co.uk", "de").

          locale: Locale used for the search request.

          location: Geo-location for the search (canonical Google location name).

          num_results: Number of results to return (1–100).

          page: The result page number for pagination.

          parse: When true, the SERP response is parsed into structured JSON.

          query: The search keyword or phrase to query.

          render: Whether to render the page in a browser before extracting.

          resolve_url: When true, search result links that point at a search-engine redirector are
              resolved to their final destination URLs. Best-effort within a time budget:
              links that cannot be resolved in time are returned unchanged.

          show_hidden_results: When true, disables Google result filtering (filter=0) so omitted/duplicate and
              highly similar pages are also returned. Applies to Google search engines.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/fast-serp",
            body=await async_maybe_transform(
                {
                    "search_engine": search_engine,
                    "country": country,
                    "device": device,
                    "domain": domain,
                    "locale": locale,
                    "location": location,
                    "num_results": num_results,
                    "page": page,
                    "parse": parse,
                    "query": query,
                    "render": render,
                    "resolve_url": resolve_url,
                    "show_hidden_results": show_hidden_results,
                },
                fast_serp_run_params.FastSerpRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FastSerpRunResponse,
        )


class FastSerpResourceWithRawResponse:
    def __init__(self, fast_serp: FastSerpResource) -> None:
        self._fast_serp = fast_serp

        self.run = to_raw_response_wrapper(
            fast_serp.run,
        )


class AsyncFastSerpResourceWithRawResponse:
    def __init__(self, fast_serp: AsyncFastSerpResource) -> None:
        self._fast_serp = fast_serp

        self.run = async_to_raw_response_wrapper(
            fast_serp.run,
        )


class FastSerpResourceWithStreamingResponse:
    def __init__(self, fast_serp: FastSerpResource) -> None:
        self._fast_serp = fast_serp

        self.run = to_streamed_response_wrapper(
            fast_serp.run,
        )


class AsyncFastSerpResourceWithStreamingResponse:
    def __init__(self, fast_serp: AsyncFastSerpResource) -> None:
        self._fast_serp = fast_serp

        self.run = async_to_streamed_response_wrapper(
            fast_serp.run,
        )
