# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import overload

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, required_args, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.extract.templates import generation_create_params
from ....types.extract.templates.generation_get_response import GenerationGetResponse
from ....types.extract.templates.generation_create_response import GenerationCreateResponse

__all__ = ["GenerationsResource", "AsyncGenerationsResource"]


class GenerationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GenerationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Nimbleway/nimble-python#accessing-raw-response-data-eg-headers
        """
        return GenerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Nimbleway/nimble-python#with_streaming_response
        """
        return GenerationsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        prompt: str,
        url: str,
        input_schema: Dict[str, object] | Omit = omit,
        metadata: Optional[generation_create_params.CreateExtractTemplateGenerationRequestPublicV2Metadata]
        | Omit = omit,
        name: Optional[str] | Omit = omit,
        output_schema: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerationCreateResponse:
        """
        Create Extract Template Generation Public V2

        Args:
          prompt: Instructions for generating the extract template.

          url: Example URL used to generate the extract template.

          input_schema: Optional JSON schema describing expected input parameters.

          metadata: Metadata to attach to the generated extract template.

          name: Optional stable name for the generated extract template.

          output_schema: Optional JSON schema describing desired extracted output.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        from_extract_template: str,
        prompt: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerationCreateResponse:
        """
        Create Extract Template Generation Public V2

        Args:
          from_extract_template: Name of the source extract template to refine.

          prompt: Instructions for refining the extract template.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["prompt", "url"], ["from_extract_template", "prompt"])
    def create(
        self,
        *,
        prompt: str,
        url: str | Omit = omit,
        input_schema: Dict[str, object] | Omit = omit,
        metadata: Optional[generation_create_params.CreateExtractTemplateGenerationRequestPublicV2Metadata]
        | Omit = omit,
        name: Optional[str] | Omit = omit,
        output_schema: Dict[str, object] | Omit = omit,
        from_extract_template: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerationCreateResponse:
        return self._post(
            "/v2/extract/templates/generations",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "url": url,
                    "input_schema": input_schema,
                    "metadata": metadata,
                    "name": name,
                    "output_schema": output_schema,
                    "from_extract_template": from_extract_template,
                },
                generation_create_params.GenerationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationCreateResponse,
        )

    def get(
        self,
        generation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerationGetResponse:
        """
        Get Extract Template Generation Public V2

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not generation_id:
            raise ValueError(f"Expected a non-empty value for `generation_id` but received {generation_id!r}")
        return self._get(
            path_template("/v2/extract/templates/generations/{generation_id}", generation_id=generation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationGetResponse,
        )


class AsyncGenerationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGenerationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Nimbleway/nimble-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGenerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Nimbleway/nimble-python#with_streaming_response
        """
        return AsyncGenerationsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        prompt: str,
        url: str,
        input_schema: Dict[str, object] | Omit = omit,
        metadata: Optional[generation_create_params.CreateExtractTemplateGenerationRequestPublicV2Metadata]
        | Omit = omit,
        name: Optional[str] | Omit = omit,
        output_schema: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerationCreateResponse:
        """
        Create Extract Template Generation Public V2

        Args:
          prompt: Instructions for generating the extract template.

          url: Example URL used to generate the extract template.

          input_schema: Optional JSON schema describing expected input parameters.

          metadata: Metadata to attach to the generated extract template.

          name: Optional stable name for the generated extract template.

          output_schema: Optional JSON schema describing desired extracted output.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        from_extract_template: str,
        prompt: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerationCreateResponse:
        """
        Create Extract Template Generation Public V2

        Args:
          from_extract_template: Name of the source extract template to refine.

          prompt: Instructions for refining the extract template.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["prompt", "url"], ["from_extract_template", "prompt"])
    async def create(
        self,
        *,
        prompt: str,
        url: str | Omit = omit,
        input_schema: Dict[str, object] | Omit = omit,
        metadata: Optional[generation_create_params.CreateExtractTemplateGenerationRequestPublicV2Metadata]
        | Omit = omit,
        name: Optional[str] | Omit = omit,
        output_schema: Dict[str, object] | Omit = omit,
        from_extract_template: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerationCreateResponse:
        return await self._post(
            "/v2/extract/templates/generations",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "url": url,
                    "input_schema": input_schema,
                    "metadata": metadata,
                    "name": name,
                    "output_schema": output_schema,
                    "from_extract_template": from_extract_template,
                },
                generation_create_params.GenerationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationCreateResponse,
        )

    async def get(
        self,
        generation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerationGetResponse:
        """
        Get Extract Template Generation Public V2

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not generation_id:
            raise ValueError(f"Expected a non-empty value for `generation_id` but received {generation_id!r}")
        return await self._get(
            path_template("/v2/extract/templates/generations/{generation_id}", generation_id=generation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationGetResponse,
        )


class GenerationsResourceWithRawResponse:
    def __init__(self, generations: GenerationsResource) -> None:
        self._generations = generations

        self.create = to_raw_response_wrapper(
            generations.create,
        )
        self.get = to_raw_response_wrapper(
            generations.get,
        )


class AsyncGenerationsResourceWithRawResponse:
    def __init__(self, generations: AsyncGenerationsResource) -> None:
        self._generations = generations

        self.create = async_to_raw_response_wrapper(
            generations.create,
        )
        self.get = async_to_raw_response_wrapper(
            generations.get,
        )


class GenerationsResourceWithStreamingResponse:
    def __init__(self, generations: GenerationsResource) -> None:
        self._generations = generations

        self.create = to_streamed_response_wrapper(
            generations.create,
        )
        self.get = to_streamed_response_wrapper(
            generations.get,
        )


class AsyncGenerationsResourceWithStreamingResponse:
    def __init__(self, generations: AsyncGenerationsResource) -> None:
        self._generations = generations

        self.create = async_to_streamed_response_wrapper(
            generations.create,
        )
        self.get = async_to_streamed_response_wrapper(
            generations.get,
        )
