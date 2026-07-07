# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, overload

import httpx

from ..types import (
    agent_run_params,
    agent_list_params,
    agent_generate_params,
    agent_run_async_params,
    agent_run_batch_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.agent_get_response import AgentGetResponse
from ..types.agent_run_response import AgentRunResponse
from ..types.agent_list_response import AgentListResponse
from ..types.agent_generate_response import AgentGenerateResponse
from ..types.agent_run_async_response import AgentRunAsyncResponse
from ..types.agent_run_batch_response import AgentRunBatchResponse
from ..types.agent_get_generation_response import AgentGetGenerationResponse

__all__ = ["AgentResource", "AsyncAgentResource"]


class AgentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Nimbleway/nimble-python#accessing-raw-response-data-eg-headers
        """
        return AgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Nimbleway/nimble-python#with_streaming_response
        """
        return AgentResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | Omit = omit,
        managed_by: Optional[Literal["nimble", "community", "self_managed"]] | Omit = omit,
        offset: int | Omit = omit,
        privacy: Optional[Literal["public", "private", "all"]] | Omit = omit,
        search: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListResponse:
        """
        List Agent Templates

        Args:
          limit: Number of results per page

          managed_by: Filter templates by attribution

          offset: Pagination offset

          privacy: Filter by privacy level

          search: Search templates by name, domain, or vertical

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "managed_by": managed_by,
                        "offset": offset,
                        "privacy": privacy,
                        "search": search,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            cast_to=AgentListResponse,
        )

    @overload
    def generate(
        self,
        *,
        prompt: str,
        url: str,
        input_schema: Dict[str, object] | Omit = omit,
        metadata: Optional[agent_generate_params.CreateAgentGenerationRequestMetadata] | Omit = omit,
        name: Optional[str] | Omit = omit,
        output_schema: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGenerateResponse:
        """
        Create Agent Generation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def generate(
        self,
        *,
        from_agent: str,
        prompt: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGenerateResponse:
        """
        Create Agent Generation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["prompt", "url"], ["from_agent", "prompt"])
    def generate(
        self,
        *,
        prompt: str,
        url: str | Omit = omit,
        input_schema: Dict[str, object] | Omit = omit,
        metadata: Optional[agent_generate_params.CreateAgentGenerationRequestMetadata] | Omit = omit,
        name: Optional[str] | Omit = omit,
        output_schema: Dict[str, object] | Omit = omit,
        from_agent: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGenerateResponse:
        return self._post(
            "/v1/agents/generations",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "url": url,
                    "input_schema": input_schema,
                    "metadata": metadata,
                    "name": name,
                    "output_schema": output_schema,
                    "from_agent": from_agent,
                },
                agent_generate_params.AgentGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGenerateResponse,
        )

    def get(
        self,
        template_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGetResponse:
        """
        Get Agent Template

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_name:
            raise ValueError(f"Expected a non-empty value for `template_name` but received {template_name!r}")
        return self._get(
            path_template("/v1/agents/{template_name}", template_name=template_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGetResponse,
        )

    def get_generation(
        self,
        generation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGetGenerationResponse:
        """
        Get Agent Generation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not generation_id:
            raise ValueError(f"Expected a non-empty value for `generation_id` but received {generation_id!r}")
        return self._get(
            path_template("/v1/agents/generations/{generation_id}", generation_id=generation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGetGenerationResponse,
        )

    def run(
        self,
        *,
        agent: str,
        params: Dict[str, object],
        formats: List[Literal["html", "markdown", "screenshot", "headers", "links"]] | Omit = omit,
        localization: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRunResponse:
        """Execute WSA Realtime Endpoint

        Args:
          formats: Response formats to include.

        All disabled by default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/agents/run",
            body=maybe_transform(
                {
                    "agent": agent,
                    "params": params,
                    "formats": formats,
                    "localization": localization,
                },
                agent_run_params.AgentRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRunResponse,
        )

    def run_async(
        self,
        *,
        agent: str,
        params: Dict[str, object],
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
    ) -> AgentRunAsyncResponse:
        """
        Execute WSA Async Endpoint

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
            "/v1/agents/async",
            body=maybe_transform(
                {
                    "agent": agent,
                    "params": params,
                    "callback_url": callback_url,
                    "formats": formats,
                    "localization": localization,
                    "storage_compress": storage_compress,
                    "storage_object_name": storage_object_name,
                    "storage_type": storage_type,
                    "storage_url": storage_url,
                },
                agent_run_async_params.AgentRunAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRunAsyncResponse,
        )

    def run_batch(
        self,
        *,
        inputs: Iterable[agent_run_batch_params.Input],
        shared_inputs: agent_run_batch_params.SharedInputs,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRunBatchResponse:
        """
        Execute WSA Batch Endpoint

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/agents/batch",
            body=maybe_transform(
                {
                    "inputs": inputs,
                    "shared_inputs": shared_inputs,
                },
                agent_run_batch_params.AgentRunBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRunBatchResponse,
        )


class AsyncAgentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Nimbleway/nimble-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Nimbleway/nimble-python#with_streaming_response
        """
        return AsyncAgentResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        managed_by: Optional[Literal["nimble", "community", "self_managed"]] | Omit = omit,
        offset: int | Omit = omit,
        privacy: Optional[Literal["public", "private", "all"]] | Omit = omit,
        search: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListResponse:
        """
        List Agent Templates

        Args:
          limit: Number of results per page

          managed_by: Filter templates by attribution

          offset: Pagination offset

          privacy: Filter by privacy level

          search: Search templates by name, domain, or vertical

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "managed_by": managed_by,
                        "offset": offset,
                        "privacy": privacy,
                        "search": search,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            cast_to=AgentListResponse,
        )

    @overload
    async def generate(
        self,
        *,
        prompt: str,
        url: str,
        input_schema: Dict[str, object] | Omit = omit,
        metadata: Optional[agent_generate_params.CreateAgentGenerationRequestMetadata] | Omit = omit,
        name: Optional[str] | Omit = omit,
        output_schema: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGenerateResponse:
        """
        Create Agent Generation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def generate(
        self,
        *,
        from_agent: str,
        prompt: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGenerateResponse:
        """
        Create Agent Generation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["prompt", "url"], ["from_agent", "prompt"])
    async def generate(
        self,
        *,
        prompt: str,
        url: str | Omit = omit,
        input_schema: Dict[str, object] | Omit = omit,
        metadata: Optional[agent_generate_params.CreateAgentGenerationRequestMetadata] | Omit = omit,
        name: Optional[str] | Omit = omit,
        output_schema: Dict[str, object] | Omit = omit,
        from_agent: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGenerateResponse:
        return await self._post(
            "/v1/agents/generations",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "url": url,
                    "input_schema": input_schema,
                    "metadata": metadata,
                    "name": name,
                    "output_schema": output_schema,
                    "from_agent": from_agent,
                },
                agent_generate_params.AgentGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGenerateResponse,
        )

    async def get(
        self,
        template_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGetResponse:
        """
        Get Agent Template

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_name:
            raise ValueError(f"Expected a non-empty value for `template_name` but received {template_name!r}")
        return await self._get(
            path_template("/v1/agents/{template_name}", template_name=template_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGetResponse,
        )

    async def get_generation(
        self,
        generation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGetGenerationResponse:
        """
        Get Agent Generation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not generation_id:
            raise ValueError(f"Expected a non-empty value for `generation_id` but received {generation_id!r}")
        return await self._get(
            path_template("/v1/agents/generations/{generation_id}", generation_id=generation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGetGenerationResponse,
        )

    async def run(
        self,
        *,
        agent: str,
        params: Dict[str, object],
        formats: List[Literal["html", "markdown", "screenshot", "headers", "links"]] | Omit = omit,
        localization: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRunResponse:
        """Execute WSA Realtime Endpoint

        Args:
          formats: Response formats to include.

        All disabled by default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/agents/run",
            body=await async_maybe_transform(
                {
                    "agent": agent,
                    "params": params,
                    "formats": formats,
                    "localization": localization,
                },
                agent_run_params.AgentRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRunResponse,
        )

    async def run_async(
        self,
        *,
        agent: str,
        params: Dict[str, object],
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
    ) -> AgentRunAsyncResponse:
        """
        Execute WSA Async Endpoint

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
            "/v1/agents/async",
            body=await async_maybe_transform(
                {
                    "agent": agent,
                    "params": params,
                    "callback_url": callback_url,
                    "formats": formats,
                    "localization": localization,
                    "storage_compress": storage_compress,
                    "storage_object_name": storage_object_name,
                    "storage_type": storage_type,
                    "storage_url": storage_url,
                },
                agent_run_async_params.AgentRunAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRunAsyncResponse,
        )

    async def run_batch(
        self,
        *,
        inputs: Iterable[agent_run_batch_params.Input],
        shared_inputs: agent_run_batch_params.SharedInputs,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRunBatchResponse:
        """
        Execute WSA Batch Endpoint

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/agents/batch",
            body=await async_maybe_transform(
                {
                    "inputs": inputs,
                    "shared_inputs": shared_inputs,
                },
                agent_run_batch_params.AgentRunBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRunBatchResponse,
        )


class AgentResourceWithRawResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

        self.list = to_raw_response_wrapper(
            agent.list,
        )
        self.generate = to_raw_response_wrapper(
            agent.generate,
        )
        self.get = to_raw_response_wrapper(
            agent.get,
        )
        self.get_generation = to_raw_response_wrapper(
            agent.get_generation,
        )
        self.run = to_raw_response_wrapper(
            agent.run,
        )
        self.run_async = to_raw_response_wrapper(
            agent.run_async,
        )
        self.run_batch = to_raw_response_wrapper(
            agent.run_batch,
        )


class AsyncAgentResourceWithRawResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

        self.list = async_to_raw_response_wrapper(
            agent.list,
        )
        self.generate = async_to_raw_response_wrapper(
            agent.generate,
        )
        self.get = async_to_raw_response_wrapper(
            agent.get,
        )
        self.get_generation = async_to_raw_response_wrapper(
            agent.get_generation,
        )
        self.run = async_to_raw_response_wrapper(
            agent.run,
        )
        self.run_async = async_to_raw_response_wrapper(
            agent.run_async,
        )
        self.run_batch = async_to_raw_response_wrapper(
            agent.run_batch,
        )


class AgentResourceWithStreamingResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

        self.list = to_streamed_response_wrapper(
            agent.list,
        )
        self.generate = to_streamed_response_wrapper(
            agent.generate,
        )
        self.get = to_streamed_response_wrapper(
            agent.get,
        )
        self.get_generation = to_streamed_response_wrapper(
            agent.get_generation,
        )
        self.run = to_streamed_response_wrapper(
            agent.run,
        )
        self.run_async = to_streamed_response_wrapper(
            agent.run_async,
        )
        self.run_batch = to_streamed_response_wrapper(
            agent.run_batch,
        )


class AsyncAgentResourceWithStreamingResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

        self.list = async_to_streamed_response_wrapper(
            agent.list,
        )
        self.generate = async_to_streamed_response_wrapper(
            agent.generate,
        )
        self.get = async_to_streamed_response_wrapper(
            agent.get,
        )
        self.get_generation = async_to_streamed_response_wrapper(
            agent.get_generation,
        )
        self.run = async_to_streamed_response_wrapper(
            agent.run,
        )
        self.run_async = async_to_streamed_response_wrapper(
            agent.run_async,
        )
        self.run_batch = async_to_streamed_response_wrapper(
            agent.run_batch,
        )
