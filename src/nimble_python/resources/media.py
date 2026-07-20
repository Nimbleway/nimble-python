# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import media_run_params, media_run_async_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.media_run_response import MediaRunResponse
from ..types.media_run_async_response import MediaRunAsyncResponse

__all__ = ["MediaResource", "AsyncMediaResource"]


class MediaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MediaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Nimbleway/nimble-python#accessing-raw-response-data-eg-headers
        """
        return MediaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MediaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Nimbleway/nimble-python#with_streaming_response
        """
        return MediaResourceWithStreamingResponse(self)

    def run(
        self,
        *,
        url: str,
        country: str | Omit = omit,
        expected_mime_types: SequenceNotStr[str] | Omit = omit,
        locale: str | Omit = omit,
        storage: media_run_params.Storage | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaRunResponse:
        """Download media from a URL.

        Waits for the result before responding.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/media",
            body=maybe_transform(
                {
                    "url": url,
                    "country": country,
                    "expected_mime_types": expected_mime_types,
                    "locale": locale,
                    "storage": storage,
                },
                media_run_params.MediaRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaRunResponse,
        )

    def run_async(
        self,
        *,
        url: str,
        callback_url: str | Omit = omit,
        country: str | Omit = omit,
        expected_mime_types: SequenceNotStr[str] | Omit = omit,
        locale: str | Omit = omit,
        storage: media_run_async_params.Storage | Omit = omit,
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
    ) -> MediaRunAsyncResponse:
        """Download media from a URL asynchronously.

        Returns a task ID immediately.

        Args:
          callback_url: URL to call back when async operation completes

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
            "/v2/media/async",
            body=maybe_transform(
                {
                    "url": url,
                    "callback_url": callback_url,
                    "country": country,
                    "expected_mime_types": expected_mime_types,
                    "locale": locale,
                    "storage": storage,
                    "storage_compress": storage_compress,
                    "storage_object_name": storage_object_name,
                    "storage_type": storage_type,
                    "storage_url": storage_url,
                },
                media_run_async_params.MediaRunAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaRunAsyncResponse,
        )


class AsyncMediaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMediaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Nimbleway/nimble-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMediaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMediaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Nimbleway/nimble-python#with_streaming_response
        """
        return AsyncMediaResourceWithStreamingResponse(self)

    async def run(
        self,
        *,
        url: str,
        country: str | Omit = omit,
        expected_mime_types: SequenceNotStr[str] | Omit = omit,
        locale: str | Omit = omit,
        storage: media_run_params.Storage | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaRunResponse:
        """Download media from a URL.

        Waits for the result before responding.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/media",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "country": country,
                    "expected_mime_types": expected_mime_types,
                    "locale": locale,
                    "storage": storage,
                },
                media_run_params.MediaRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaRunResponse,
        )

    async def run_async(
        self,
        *,
        url: str,
        callback_url: str | Omit = omit,
        country: str | Omit = omit,
        expected_mime_types: SequenceNotStr[str] | Omit = omit,
        locale: str | Omit = omit,
        storage: media_run_async_params.Storage | Omit = omit,
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
    ) -> MediaRunAsyncResponse:
        """Download media from a URL asynchronously.

        Returns a task ID immediately.

        Args:
          callback_url: URL to call back when async operation completes

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
            "/v2/media/async",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "callback_url": callback_url,
                    "country": country,
                    "expected_mime_types": expected_mime_types,
                    "locale": locale,
                    "storage": storage,
                    "storage_compress": storage_compress,
                    "storage_object_name": storage_object_name,
                    "storage_type": storage_type,
                    "storage_url": storage_url,
                },
                media_run_async_params.MediaRunAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaRunAsyncResponse,
        )


class MediaResourceWithRawResponse:
    def __init__(self, media: MediaResource) -> None:
        self._media = media

        self.run = to_raw_response_wrapper(
            media.run,
        )
        self.run_async = to_raw_response_wrapper(
            media.run_async,
        )


class AsyncMediaResourceWithRawResponse:
    def __init__(self, media: AsyncMediaResource) -> None:
        self._media = media

        self.run = async_to_raw_response_wrapper(
            media.run,
        )
        self.run_async = async_to_raw_response_wrapper(
            media.run_async,
        )


class MediaResourceWithStreamingResponse:
    def __init__(self, media: MediaResource) -> None:
        self._media = media

        self.run = to_streamed_response_wrapper(
            media.run,
        )
        self.run_async = to_streamed_response_wrapper(
            media.run_async,
        )


class AsyncMediaResourceWithStreamingResponse:
    def __init__(self, media: AsyncMediaResource) -> None:
        self._media = media

        self.run = async_to_streamed_response_wrapper(
            media.run,
        )
        self.run_async = async_to_streamed_response_wrapper(
            media.run_async,
        )
