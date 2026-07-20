# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal

import httpx

from .versions import (
    VersionsResource,
    AsyncVersionsResource,
    VersionsResourceWithRawResponse,
    AsyncVersionsResourceWithRawResponse,
    VersionsResourceWithStreamingResponse,
    AsyncVersionsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .generations import (
    GenerationsResource,
    AsyncGenerationsResource,
    GenerationsResourceWithRawResponse,
    AsyncGenerationsResourceWithRawResponse,
    GenerationsResourceWithStreamingResponse,
    AsyncGenerationsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.extract import (
    template_run_params,
    template_list_params,
    template_async_params,
    template_batch_params,
    template_update_params,
)
from ....types.extract.template_get_response import TemplateGetResponse
from ....types.extract.template_run_response import TemplateRunResponse
from ....types.extract.template_list_response import TemplateListResponse
from ....types.extract.template_async_response import TemplateAsyncResponse
from ....types.extract.template_batch_response import TemplateBatchResponse
from ....types.extract.template_update_response import TemplateUpdateResponse

__all__ = ["TemplatesResource", "AsyncTemplatesResource"]


class TemplatesResource(SyncAPIResource):
    @cached_property
    def generations(self) -> GenerationsResource:
        return GenerationsResource(self._client)

    @cached_property
    def versions(self) -> VersionsResource:
        return VersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Nimbleway/nimble-python#accessing-raw-response-data-eg-headers
        """
        return TemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Nimbleway/nimble-python#with_streaming_response
        """
        return TemplatesResourceWithStreamingResponse(self)

    def update(
        self,
        extract_template_name: str,
        *,
        body: Iterable[template_update_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateUpdateResponse:
        """
        Patch Extract Template Public V2

        Args:
          body: A JSON Patch document per RFC 6902 — a JSON array of patch operations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extract_template_name:
            raise ValueError(
                f"Expected a non-empty value for `extract_template_name` but received {extract_template_name!r}"
            )
        return self._patch(
            path_template("/v2/extract/templates/{extract_template_name}", extract_template_name=extract_template_name),
            body=maybe_transform(body, Iterable[template_update_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateUpdateResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateListResponse:
        """
        List Extract Templates Public V2

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/extract/templates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    template_list_params.TemplateListParams,
                ),
            ),
            cast_to=TemplateListResponse,
        )

    def delete(
        self,
        extract_template_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Extract Template Public V2

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extract_template_name:
            raise ValueError(
                f"Expected a non-empty value for `extract_template_name` but received {extract_template_name!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v2/extract/templates/{extract_template_name}", extract_template_name=extract_template_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def async_(
        self,
        *,
        params: Dict[str, object],
        template: str,
        callback_url: str | Omit = omit,
        formats: List[Literal["html", "markdown", "screenshot", "headers", "links"]] | Omit = omit,
        localization: bool | Omit = omit,
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
    ) -> TemplateAsyncResponse:
        """
        Execute Extraction Template Async Endpoint

        Args:
          callback_url: URL to call back when async operation completes

          formats: Response formats to include. All disabled by default.

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
            "/v2/extract/templates/async",
            body=maybe_transform(
                {
                    "params": params,
                    "template": template,
                    "callback_url": callback_url,
                    "formats": formats,
                    "localization": localization,
                    "storage_compress": storage_compress,
                    "storage_object_name": storage_object_name,
                    "storage_type": storage_type,
                    "storage_url": storage_url,
                },
                template_async_params.TemplateAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateAsyncResponse,
        )

    def batch(
        self,
        *,
        inputs: Iterable[template_batch_params.Input],
        shared_inputs: template_batch_params.SharedInputs,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateBatchResponse:
        """
        Execute Extraction Template Batch Endpoint

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/extract/templates/batch",
            body=maybe_transform(
                {
                    "inputs": inputs,
                    "shared_inputs": shared_inputs,
                },
                template_batch_params.TemplateBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateBatchResponse,
        )

    def get(
        self,
        extract_template_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateGetResponse:
        """
        Get Extract Template Public V2

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extract_template_name:
            raise ValueError(
                f"Expected a non-empty value for `extract_template_name` but received {extract_template_name!r}"
            )
        return self._get(
            path_template("/v2/extract/templates/{extract_template_name}", extract_template_name=extract_template_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateGetResponse,
        )

    def run(
        self,
        *,
        params: Dict[str, object],
        template: str,
        formats: List[Literal["html", "markdown", "screenshot", "headers", "links"]] | Omit = omit,
        localization: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateRunResponse:
        """
        Execute Extraction Template Realtime Endpoint

        Args:
          formats: Response formats to include. All disabled by default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/extract/templates/run",
            body=maybe_transform(
                {
                    "params": params,
                    "template": template,
                    "formats": formats,
                    "localization": localization,
                },
                template_run_params.TemplateRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateRunResponse,
        )


class AsyncTemplatesResource(AsyncAPIResource):
    @cached_property
    def generations(self) -> AsyncGenerationsResource:
        return AsyncGenerationsResource(self._client)

    @cached_property
    def versions(self) -> AsyncVersionsResource:
        return AsyncVersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Nimbleway/nimble-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Nimbleway/nimble-python#with_streaming_response
        """
        return AsyncTemplatesResourceWithStreamingResponse(self)

    async def update(
        self,
        extract_template_name: str,
        *,
        body: Iterable[template_update_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateUpdateResponse:
        """
        Patch Extract Template Public V2

        Args:
          body: A JSON Patch document per RFC 6902 — a JSON array of patch operations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extract_template_name:
            raise ValueError(
                f"Expected a non-empty value for `extract_template_name` but received {extract_template_name!r}"
            )
        return await self._patch(
            path_template("/v2/extract/templates/{extract_template_name}", extract_template_name=extract_template_name),
            body=await async_maybe_transform(body, Iterable[template_update_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateUpdateResponse,
        )

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateListResponse:
        """
        List Extract Templates Public V2

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/extract/templates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    template_list_params.TemplateListParams,
                ),
            ),
            cast_to=TemplateListResponse,
        )

    async def delete(
        self,
        extract_template_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Extract Template Public V2

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extract_template_name:
            raise ValueError(
                f"Expected a non-empty value for `extract_template_name` but received {extract_template_name!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v2/extract/templates/{extract_template_name}", extract_template_name=extract_template_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def async_(
        self,
        *,
        params: Dict[str, object],
        template: str,
        callback_url: str | Omit = omit,
        formats: List[Literal["html", "markdown", "screenshot", "headers", "links"]] | Omit = omit,
        localization: bool | Omit = omit,
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
    ) -> TemplateAsyncResponse:
        """
        Execute Extraction Template Async Endpoint

        Args:
          callback_url: URL to call back when async operation completes

          formats: Response formats to include. All disabled by default.

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
            "/v2/extract/templates/async",
            body=await async_maybe_transform(
                {
                    "params": params,
                    "template": template,
                    "callback_url": callback_url,
                    "formats": formats,
                    "localization": localization,
                    "storage_compress": storage_compress,
                    "storage_object_name": storage_object_name,
                    "storage_type": storage_type,
                    "storage_url": storage_url,
                },
                template_async_params.TemplateAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateAsyncResponse,
        )

    async def batch(
        self,
        *,
        inputs: Iterable[template_batch_params.Input],
        shared_inputs: template_batch_params.SharedInputs,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateBatchResponse:
        """
        Execute Extraction Template Batch Endpoint

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/extract/templates/batch",
            body=await async_maybe_transform(
                {
                    "inputs": inputs,
                    "shared_inputs": shared_inputs,
                },
                template_batch_params.TemplateBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateBatchResponse,
        )

    async def get(
        self,
        extract_template_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateGetResponse:
        """
        Get Extract Template Public V2

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extract_template_name:
            raise ValueError(
                f"Expected a non-empty value for `extract_template_name` but received {extract_template_name!r}"
            )
        return await self._get(
            path_template("/v2/extract/templates/{extract_template_name}", extract_template_name=extract_template_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateGetResponse,
        )

    async def run(
        self,
        *,
        params: Dict[str, object],
        template: str,
        formats: List[Literal["html", "markdown", "screenshot", "headers", "links"]] | Omit = omit,
        localization: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateRunResponse:
        """
        Execute Extraction Template Realtime Endpoint

        Args:
          formats: Response formats to include. All disabled by default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/extract/templates/run",
            body=await async_maybe_transform(
                {
                    "params": params,
                    "template": template,
                    "formats": formats,
                    "localization": localization,
                },
                template_run_params.TemplateRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateRunResponse,
        )


class TemplatesResourceWithRawResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.update = to_raw_response_wrapper(
            templates.update,
        )
        self.list = to_raw_response_wrapper(
            templates.list,
        )
        self.delete = to_raw_response_wrapper(
            templates.delete,
        )
        self.async_ = to_raw_response_wrapper(
            templates.async_,
        )
        self.batch = to_raw_response_wrapper(
            templates.batch,
        )
        self.get = to_raw_response_wrapper(
            templates.get,
        )
        self.run = to_raw_response_wrapper(
            templates.run,
        )

    @cached_property
    def generations(self) -> GenerationsResourceWithRawResponse:
        return GenerationsResourceWithRawResponse(self._templates.generations)

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        return VersionsResourceWithRawResponse(self._templates.versions)


class AsyncTemplatesResourceWithRawResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.update = async_to_raw_response_wrapper(
            templates.update,
        )
        self.list = async_to_raw_response_wrapper(
            templates.list,
        )
        self.delete = async_to_raw_response_wrapper(
            templates.delete,
        )
        self.async_ = async_to_raw_response_wrapper(
            templates.async_,
        )
        self.batch = async_to_raw_response_wrapper(
            templates.batch,
        )
        self.get = async_to_raw_response_wrapper(
            templates.get,
        )
        self.run = async_to_raw_response_wrapper(
            templates.run,
        )

    @cached_property
    def generations(self) -> AsyncGenerationsResourceWithRawResponse:
        return AsyncGenerationsResourceWithRawResponse(self._templates.generations)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        return AsyncVersionsResourceWithRawResponse(self._templates.versions)


class TemplatesResourceWithStreamingResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.update = to_streamed_response_wrapper(
            templates.update,
        )
        self.list = to_streamed_response_wrapper(
            templates.list,
        )
        self.delete = to_streamed_response_wrapper(
            templates.delete,
        )
        self.async_ = to_streamed_response_wrapper(
            templates.async_,
        )
        self.batch = to_streamed_response_wrapper(
            templates.batch,
        )
        self.get = to_streamed_response_wrapper(
            templates.get,
        )
        self.run = to_streamed_response_wrapper(
            templates.run,
        )

    @cached_property
    def generations(self) -> GenerationsResourceWithStreamingResponse:
        return GenerationsResourceWithStreamingResponse(self._templates.generations)

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        return VersionsResourceWithStreamingResponse(self._templates.versions)


class AsyncTemplatesResourceWithStreamingResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.update = async_to_streamed_response_wrapper(
            templates.update,
        )
        self.list = async_to_streamed_response_wrapper(
            templates.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            templates.delete,
        )
        self.async_ = async_to_streamed_response_wrapper(
            templates.async_,
        )
        self.batch = async_to_streamed_response_wrapper(
            templates.batch,
        )
        self.get = async_to_streamed_response_wrapper(
            templates.get,
        )
        self.run = async_to_streamed_response_wrapper(
            templates.run,
        )

    @cached_property
    def generations(self) -> AsyncGenerationsResourceWithStreamingResponse:
        return AsyncGenerationsResourceWithStreamingResponse(self._templates.generations)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self._templates.versions)
