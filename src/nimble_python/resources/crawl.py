# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import crawl_run_params, crawl_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.crawl_run_response import CrawlRunResponse
from ..types.crawl_list_response import CrawlListResponse
from ..types.crawl_status_response import CrawlStatusResponse
from ..types.crawl_terminate_response import CrawlTerminateResponse

__all__ = ["CrawlResource", "AsyncCrawlResource"]


class CrawlResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CrawlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Nimbleway/nimble-python#accessing-raw-response-data-eg-headers
        """
        return CrawlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CrawlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Nimbleway/nimble-python#with_streaming_response
        """
        return CrawlResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["queued", "running", "succeeded", "failed", "canceled", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CrawlListResponse:
        """
        Crawl by Filter

        Args:
          cursor: Cursor for pagination.

          limit: Number of crawls to return per page.

          status: Filter crawls by their status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/crawl",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                    },
                    crawl_list_params.CrawlListParams,
                ),
            ),
            cast_to=CrawlListResponse,
        )

    def run(
        self,
        *,
        url: str,
        allow_external_links: bool | Omit = omit,
        allow_subdomains: bool | Omit = omit,
        callback: crawl_run_params.Callback | Omit = omit,
        crawl_entire_domain: bool | Omit = omit,
        exclude_paths: SequenceNotStr[str] | Omit = omit,
        extract_options: crawl_run_params.ExtractOptions | Omit = omit,
        ignore_query_parameters: bool | Omit = omit,
        include_paths: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        max_discovery_depth: int | Omit = omit,
        name: str | Omit = omit,
        sitemap: Literal["skip", "include", "only"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CrawlRunResponse:
        """
        Create crawl task

        Args:
          url: Url to crawl.

          allow_external_links: Allows the crawler to follow links to external websites.

          allow_subdomains: Allows the crawler to follow links to subdomains of the main domain.

          callback: Webhook configuration for receiving crawl results.

          crawl_entire_domain: Allows the crawler to follow internal links to sibling or parent URLs, not just
              child paths.

          exclude_paths: URL pathname regex patterns that exclude matching URLs from the crawl.

          ignore_query_parameters: Do not re-scrape the same path with different (or none) query parameters.

          include_paths: URL pathname regex patterns that include matching URLs in the crawl.

          limit: Maximum number of pages to crawl.

          max_discovery_depth: Maximum depth to crawl based on discovery order.

          name: Name of the crawl.

          sitemap: Sitemap and other methods will be used together to find URLs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/crawl",
            body=maybe_transform(
                {
                    "url": url,
                    "allow_external_links": allow_external_links,
                    "allow_subdomains": allow_subdomains,
                    "callback": callback,
                    "crawl_entire_domain": crawl_entire_domain,
                    "exclude_paths": exclude_paths,
                    "extract_options": extract_options,
                    "ignore_query_parameters": ignore_query_parameters,
                    "include_paths": include_paths,
                    "limit": limit,
                    "max_discovery_depth": max_discovery_depth,
                    "name": name,
                    "sitemap": sitemap,
                },
                crawl_run_params.CrawlRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CrawlRunResponse,
        )

    def status(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CrawlStatusResponse:
        """
        Get crawl data

        Args:
          id: The unique identifier of the crawl task.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v2/crawl/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CrawlStatusResponse,
        )

    def terminate(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CrawlTerminateResponse:
        """
        Cancel Crawl

        Args:
          id: The unique identifier of the crawl task.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/v2/crawl/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CrawlTerminateResponse,
        )


class AsyncCrawlResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCrawlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Nimbleway/nimble-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCrawlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCrawlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Nimbleway/nimble-python#with_streaming_response
        """
        return AsyncCrawlResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["queued", "running", "succeeded", "failed", "canceled", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CrawlListResponse:
        """
        Crawl by Filter

        Args:
          cursor: Cursor for pagination.

          limit: Number of crawls to return per page.

          status: Filter crawls by their status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/crawl",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                    },
                    crawl_list_params.CrawlListParams,
                ),
            ),
            cast_to=CrawlListResponse,
        )

    async def run(
        self,
        *,
        url: str,
        allow_external_links: bool | Omit = omit,
        allow_subdomains: bool | Omit = omit,
        callback: crawl_run_params.Callback | Omit = omit,
        crawl_entire_domain: bool | Omit = omit,
        exclude_paths: SequenceNotStr[str] | Omit = omit,
        extract_options: crawl_run_params.ExtractOptions | Omit = omit,
        ignore_query_parameters: bool | Omit = omit,
        include_paths: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        max_discovery_depth: int | Omit = omit,
        name: str | Omit = omit,
        sitemap: Literal["skip", "include", "only"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CrawlRunResponse:
        """
        Create crawl task

        Args:
          url: Url to crawl.

          allow_external_links: Allows the crawler to follow links to external websites.

          allow_subdomains: Allows the crawler to follow links to subdomains of the main domain.

          callback: Webhook configuration for receiving crawl results.

          crawl_entire_domain: Allows the crawler to follow internal links to sibling or parent URLs, not just
              child paths.

          exclude_paths: URL pathname regex patterns that exclude matching URLs from the crawl.

          ignore_query_parameters: Do not re-scrape the same path with different (or none) query parameters.

          include_paths: URL pathname regex patterns that include matching URLs in the crawl.

          limit: Maximum number of pages to crawl.

          max_discovery_depth: Maximum depth to crawl based on discovery order.

          name: Name of the crawl.

          sitemap: Sitemap and other methods will be used together to find URLs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/crawl",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "allow_external_links": allow_external_links,
                    "allow_subdomains": allow_subdomains,
                    "callback": callback,
                    "crawl_entire_domain": crawl_entire_domain,
                    "exclude_paths": exclude_paths,
                    "extract_options": extract_options,
                    "ignore_query_parameters": ignore_query_parameters,
                    "include_paths": include_paths,
                    "limit": limit,
                    "max_discovery_depth": max_discovery_depth,
                    "name": name,
                    "sitemap": sitemap,
                },
                crawl_run_params.CrawlRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CrawlRunResponse,
        )

    async def status(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CrawlStatusResponse:
        """
        Get crawl data

        Args:
          id: The unique identifier of the crawl task.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v2/crawl/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CrawlStatusResponse,
        )

    async def terminate(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CrawlTerminateResponse:
        """
        Cancel Crawl

        Args:
          id: The unique identifier of the crawl task.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/v2/crawl/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CrawlTerminateResponse,
        )


class CrawlResourceWithRawResponse:
    def __init__(self, crawl: CrawlResource) -> None:
        self._crawl = crawl

        self.list = to_raw_response_wrapper(
            crawl.list,
        )
        self.run = to_raw_response_wrapper(
            crawl.run,
        )
        self.status = to_raw_response_wrapper(
            crawl.status,
        )
        self.terminate = to_raw_response_wrapper(
            crawl.terminate,
        )


class AsyncCrawlResourceWithRawResponse:
    def __init__(self, crawl: AsyncCrawlResource) -> None:
        self._crawl = crawl

        self.list = async_to_raw_response_wrapper(
            crawl.list,
        )
        self.run = async_to_raw_response_wrapper(
            crawl.run,
        )
        self.status = async_to_raw_response_wrapper(
            crawl.status,
        )
        self.terminate = async_to_raw_response_wrapper(
            crawl.terminate,
        )


class CrawlResourceWithStreamingResponse:
    def __init__(self, crawl: CrawlResource) -> None:
        self._crawl = crawl

        self.list = to_streamed_response_wrapper(
            crawl.list,
        )
        self.run = to_streamed_response_wrapper(
            crawl.run,
        )
        self.status = to_streamed_response_wrapper(
            crawl.status,
        )
        self.terminate = to_streamed_response_wrapper(
            crawl.terminate,
        )


class AsyncCrawlResourceWithStreamingResponse:
    def __init__(self, crawl: AsyncCrawlResource) -> None:
        self._crawl = crawl

        self.list = async_to_streamed_response_wrapper(
            crawl.list,
        )
        self.run = async_to_streamed_response_wrapper(
            crawl.run,
        )
        self.status = async_to_streamed_response_wrapper(
            crawl.status,
        )
        self.terminate = async_to_streamed_response_wrapper(
            crawl.terminate,
        )
