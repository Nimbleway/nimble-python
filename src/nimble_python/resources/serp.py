# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import serp_run_params, serp_run_async_params, serp_run_batch_params
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
from ..types.serp_run_response import SerpRunResponse
from ..types.serp_run_async_response import SerpRunAsyncResponse
from ..types.serp_run_batch_response import SerpRunBatchResponse

__all__ = ["SerpResource", "AsyncSerpResource"]


class SerpResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SerpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Nimbleway/nimble-python#accessing-raw-response-data-eg-headers
        """
        return SerpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SerpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Nimbleway/nimble-python#with_streaming_response
        """
        return SerpResourceWithStreamingResponse(self)

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
    ) -> SerpRunResponse:
        """
        SERP

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
            "/v2/serp",
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
                serp_run_params.SerpRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SerpRunResponse,
        )

    def run_async(
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
        callback_url: str | Omit = omit,
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
        storage_compress: bool | Omit = omit,
        storage_object_name: str | Omit = omit,
        storage_type: str | Omit = omit,
        storage_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SerpRunAsyncResponse:
        """
        SERP Async Endpoint

        Args:
          search_engine: The search engine to query.

          callback_url: URL to call back when async operation completes

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

          storage_compress: Whether to compress stored data

          storage_object_name: Custom name for the stored object

          storage_type: Type of storage to use for results

          storage_url: URL for storage location

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/serp/async",
            body=maybe_transform(
                {
                    "search_engine": search_engine,
                    "callback_url": callback_url,
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
                    "storage_compress": storage_compress,
                    "storage_object_name": storage_object_name,
                    "storage_type": storage_type,
                    "storage_url": storage_url,
                },
                serp_run_async_params.SerpRunAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SerpRunAsyncResponse,
        )

    def run_batch(
        self,
        *,
        inputs: Iterable[serp_run_batch_params.Input],
        shared_inputs: serp_run_batch_params.SharedInputs | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SerpRunBatchResponse:
        """SERP Batch Endpoint

        Args:
          inputs: Array of SERP requests.

        Each object can include search parameters and
              async/storage settings.

          shared_inputs: Shared parameters applied to the entire batch. Can include search parameters and
              async/storage settings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/serp/batch",
            body=maybe_transform(
                {
                    "inputs": inputs,
                    "shared_inputs": shared_inputs,
                },
                serp_run_batch_params.SerpRunBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SerpRunBatchResponse,
        )


class AsyncSerpResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSerpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Nimbleway/nimble-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSerpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSerpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Nimbleway/nimble-python#with_streaming_response
        """
        return AsyncSerpResourceWithStreamingResponse(self)

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
    ) -> SerpRunResponse:
        """
        SERP

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
            "/v2/serp",
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
                serp_run_params.SerpRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SerpRunResponse,
        )

    async def run_async(
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
        callback_url: str | Omit = omit,
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
        storage_compress: bool | Omit = omit,
        storage_object_name: str | Omit = omit,
        storage_type: str | Omit = omit,
        storage_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SerpRunAsyncResponse:
        """
        SERP Async Endpoint

        Args:
          search_engine: The search engine to query.

          callback_url: URL to call back when async operation completes

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

          storage_compress: Whether to compress stored data

          storage_object_name: Custom name for the stored object

          storage_type: Type of storage to use for results

          storage_url: URL for storage location

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/serp/async",
            body=await async_maybe_transform(
                {
                    "search_engine": search_engine,
                    "callback_url": callback_url,
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
                    "storage_compress": storage_compress,
                    "storage_object_name": storage_object_name,
                    "storage_type": storage_type,
                    "storage_url": storage_url,
                },
                serp_run_async_params.SerpRunAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SerpRunAsyncResponse,
        )

    async def run_batch(
        self,
        *,
        inputs: Iterable[serp_run_batch_params.Input],
        shared_inputs: serp_run_batch_params.SharedInputs | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SerpRunBatchResponse:
        """SERP Batch Endpoint

        Args:
          inputs: Array of SERP requests.

        Each object can include search parameters and
              async/storage settings.

          shared_inputs: Shared parameters applied to the entire batch. Can include search parameters and
              async/storage settings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/serp/batch",
            body=await async_maybe_transform(
                {
                    "inputs": inputs,
                    "shared_inputs": shared_inputs,
                },
                serp_run_batch_params.SerpRunBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SerpRunBatchResponse,
        )


class SerpResourceWithRawResponse:
    def __init__(self, serp: SerpResource) -> None:
        self._serp = serp

        self.run = to_raw_response_wrapper(
            serp.run,
        )
        self.run_async = to_raw_response_wrapper(
            serp.run_async,
        )
        self.run_batch = to_raw_response_wrapper(
            serp.run_batch,
        )


class AsyncSerpResourceWithRawResponse:
    def __init__(self, serp: AsyncSerpResource) -> None:
        self._serp = serp

        self.run = async_to_raw_response_wrapper(
            serp.run,
        )
        self.run_async = async_to_raw_response_wrapper(
            serp.run_async,
        )
        self.run_batch = async_to_raw_response_wrapper(
            serp.run_batch,
        )


class SerpResourceWithStreamingResponse:
    def __init__(self, serp: SerpResource) -> None:
        self._serp = serp

        self.run = to_streamed_response_wrapper(
            serp.run,
        )
        self.run_async = to_streamed_response_wrapper(
            serp.run_async,
        )
        self.run_batch = to_streamed_response_wrapper(
            serp.run_batch,
        )


class AsyncSerpResourceWithStreamingResponse:
    def __init__(self, serp: AsyncSerpResource) -> None:
        self._serp = serp

        self.run = async_to_streamed_response_wrapper(
            serp.run,
        )
        self.run_async = async_to_streamed_response_wrapper(
            serp.run_async,
        )
        self.run_batch = async_to_streamed_response_wrapper(
            serp.run_batch,
        )
