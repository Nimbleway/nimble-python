# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal

import httpx

from .runs import (
    RunsResource,
    AsyncRunsResource,
    RunsResourceWithRawResponse,
    AsyncRunsResourceWithRawResponse,
    RunsResourceWithStreamingResponse,
    AsyncRunsResourceWithStreamingResponse,
)
from ...types import task_agent_run_params, task_agent_list_params, task_agent_create_params, task_agent_update_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .templates import (
    TemplatesResource,
    AsyncTemplatesResource,
    TemplatesResourceWithRawResponse,
    AsyncTemplatesResourceWithRawResponse,
    TemplatesResourceWithStreamingResponse,
    AsyncTemplatesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.task_agent_get_response import TaskAgentGetResponse
from ...types.task_agent_run_response import TaskAgentRunResponse
from ...types.task_agent_list_response import TaskAgentListResponse
from ...types.task_agent_create_response import TaskAgentCreateResponse
from ...types.task_agent_update_response import TaskAgentUpdateResponse

__all__ = ["TaskAgentResource", "AsyncTaskAgentResource"]


class TaskAgentResource(SyncAPIResource):
    @cached_property
    def templates(self) -> TemplatesResource:
        return TemplatesResource(self._client)

    @cached_property
    def runs(self) -> RunsResource:
        return RunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TaskAgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Nimbleway/nimble-python#accessing-raw-response-data-eg-headers
        """
        return TaskAgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TaskAgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Nimbleway/nimble-python#with_streaming_response
        """
        return TaskAgentResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        agent_name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        domain_expertise: Optional[str] | Omit = omit,
        effort: Literal["low", "medium", "high", "x-high", "max"] | Omit = omit,
        goals: SequenceNotStr[str] | Omit = omit,
        icon: Optional[str] | Omit = omit,
        is_active: bool | Omit = omit,
        output_schema: Optional[Dict[str, object]] | Omit = omit,
        sources: task_agent_create_params.Sources | Omit = omit,
        suggested_questions: SequenceNotStr[str] | Omit = omit,
        template: Optional[str] | Omit = omit,
        use_case: Optional[Literal["research", "enrichment", "dataset_building"]] | Omit = omit,
        workspace_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskAgentCreateResponse:
        """
        Create a Web Search Agent instance.

        `account_id` is JWT-derived and never read from the request body.

        Args:
          effort: Canonical effort tier names for the research graph.

          sources: Source preferences for a web search agent instance.

          template: Template name to materialize this instance from. When set, the scalar fields and
              child rows are copied from the template.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/task-agents",
            body=maybe_transform(
                {
                    "agent_name": agent_name,
                    "description": description,
                    "display_name": display_name,
                    "domain_expertise": domain_expertise,
                    "effort": effort,
                    "goals": goals,
                    "icon": icon,
                    "is_active": is_active,
                    "output_schema": output_schema,
                    "sources": sources,
                    "suggested_questions": suggested_questions,
                    "template": template,
                    "use_case": use_case,
                    "workspace_id": workspace_id,
                },
                task_agent_create_params.TaskAgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskAgentCreateResponse,
        )

    def update(
        self,
        agent_id: str,
        *,
        body: Iterable[task_agent_update_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskAgentUpdateResponse:
        """
        Update Agent

        Args:
          body: A JSON Patch document per RFC 6902 — a JSON array of patch operations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._patch(
            path_template("/v1/task-agents/{agent_id}", agent_id=agent_id),
            body=maybe_transform(body, Iterable[task_agent_update_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskAgentUpdateResponse,
        )

    def list(
        self,
        *,
        filter_effort: Optional[Literal["low", "medium", "high", "x-high", "max"]] | Omit = omit,
        filter_use_case: Optional[Literal["research", "enrichment", "dataset_building"]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        workspace_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskAgentListResponse:
        """
        List Web Search Agent instances.

        Callers are strictly scoped to their (account, workspace). If `workspace_id` is
        omitted, the user's default workspace is used.

        Args:
          filter_effort: Canonical effort tier names for the research graph.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/task-agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_effort": filter_effort,
                        "filter_use_case": filter_use_case,
                        "limit": limit,
                        "offset": offset,
                        "workspace_id": workspace_id,
                    },
                    task_agent_list_params.TaskAgentListParams,
                ),
            ),
            cast_to=TaskAgentListResponse,
        )

    def deactivate(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deactivate Agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/task-agents/{agent_id}", agent_id=agent_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskAgentGetResponse:
        """
        Get Agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            path_template("/v1/task-agents/{agent_id}", agent_id=agent_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskAgentGetResponse,
        )

    def run(
        self,
        agent_id: str,
        *,
        input: str,
        effort: Optional[Literal["low", "medium", "high", "x-high", "max"]] | Omit = omit,
        enable_events: bool | Omit = omit,
        output_schema: Optional[Dict[str, object]] | Omit = omit,
        previous_interaction_id: Optional[str] | Omit = omit,
        sources: Optional[task_agent_run_params.Sources] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskAgentRunResponse:
        """
        Create a research run for a Web Search Agent instance.

        Args:
          effort: Canonical effort tier names for the research graph.

          sources: Source preferences for a web search agent instance.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            path_template("/v1/task-agents/{agent_id}/runs", agent_id=agent_id),
            body=maybe_transform(
                {
                    "input": input,
                    "effort": effort,
                    "enable_events": enable_events,
                    "output_schema": output_schema,
                    "previous_interaction_id": previous_interaction_id,
                    "sources": sources,
                },
                task_agent_run_params.TaskAgentRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskAgentRunResponse,
        )


class AsyncTaskAgentResource(AsyncAPIResource):
    @cached_property
    def templates(self) -> AsyncTemplatesResource:
        return AsyncTemplatesResource(self._client)

    @cached_property
    def runs(self) -> AsyncRunsResource:
        return AsyncRunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTaskAgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Nimbleway/nimble-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTaskAgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTaskAgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Nimbleway/nimble-python#with_streaming_response
        """
        return AsyncTaskAgentResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        agent_name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        domain_expertise: Optional[str] | Omit = omit,
        effort: Literal["low", "medium", "high", "x-high", "max"] | Omit = omit,
        goals: SequenceNotStr[str] | Omit = omit,
        icon: Optional[str] | Omit = omit,
        is_active: bool | Omit = omit,
        output_schema: Optional[Dict[str, object]] | Omit = omit,
        sources: task_agent_create_params.Sources | Omit = omit,
        suggested_questions: SequenceNotStr[str] | Omit = omit,
        template: Optional[str] | Omit = omit,
        use_case: Optional[Literal["research", "enrichment", "dataset_building"]] | Omit = omit,
        workspace_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskAgentCreateResponse:
        """
        Create a Web Search Agent instance.

        `account_id` is JWT-derived and never read from the request body.

        Args:
          effort: Canonical effort tier names for the research graph.

          sources: Source preferences for a web search agent instance.

          template: Template name to materialize this instance from. When set, the scalar fields and
              child rows are copied from the template.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/task-agents",
            body=await async_maybe_transform(
                {
                    "agent_name": agent_name,
                    "description": description,
                    "display_name": display_name,
                    "domain_expertise": domain_expertise,
                    "effort": effort,
                    "goals": goals,
                    "icon": icon,
                    "is_active": is_active,
                    "output_schema": output_schema,
                    "sources": sources,
                    "suggested_questions": suggested_questions,
                    "template": template,
                    "use_case": use_case,
                    "workspace_id": workspace_id,
                },
                task_agent_create_params.TaskAgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskAgentCreateResponse,
        )

    async def update(
        self,
        agent_id: str,
        *,
        body: Iterable[task_agent_update_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskAgentUpdateResponse:
        """
        Update Agent

        Args:
          body: A JSON Patch document per RFC 6902 — a JSON array of patch operations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._patch(
            path_template("/v1/task-agents/{agent_id}", agent_id=agent_id),
            body=await async_maybe_transform(body, Iterable[task_agent_update_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskAgentUpdateResponse,
        )

    async def list(
        self,
        *,
        filter_effort: Optional[Literal["low", "medium", "high", "x-high", "max"]] | Omit = omit,
        filter_use_case: Optional[Literal["research", "enrichment", "dataset_building"]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        workspace_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskAgentListResponse:
        """
        List Web Search Agent instances.

        Callers are strictly scoped to their (account, workspace). If `workspace_id` is
        omitted, the user's default workspace is used.

        Args:
          filter_effort: Canonical effort tier names for the research graph.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/task-agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter_effort": filter_effort,
                        "filter_use_case": filter_use_case,
                        "limit": limit,
                        "offset": offset,
                        "workspace_id": workspace_id,
                    },
                    task_agent_list_params.TaskAgentListParams,
                ),
            ),
            cast_to=TaskAgentListResponse,
        )

    async def deactivate(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deactivate Agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/task-agents/{agent_id}", agent_id=agent_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskAgentGetResponse:
        """
        Get Agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            path_template("/v1/task-agents/{agent_id}", agent_id=agent_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskAgentGetResponse,
        )

    async def run(
        self,
        agent_id: str,
        *,
        input: str,
        effort: Optional[Literal["low", "medium", "high", "x-high", "max"]] | Omit = omit,
        enable_events: bool | Omit = omit,
        output_schema: Optional[Dict[str, object]] | Omit = omit,
        previous_interaction_id: Optional[str] | Omit = omit,
        sources: Optional[task_agent_run_params.Sources] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskAgentRunResponse:
        """
        Create a research run for a Web Search Agent instance.

        Args:
          effort: Canonical effort tier names for the research graph.

          sources: Source preferences for a web search agent instance.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            path_template("/v1/task-agents/{agent_id}/runs", agent_id=agent_id),
            body=await async_maybe_transform(
                {
                    "input": input,
                    "effort": effort,
                    "enable_events": enable_events,
                    "output_schema": output_schema,
                    "previous_interaction_id": previous_interaction_id,
                    "sources": sources,
                },
                task_agent_run_params.TaskAgentRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskAgentRunResponse,
        )


class TaskAgentResourceWithRawResponse:
    def __init__(self, task_agent: TaskAgentResource) -> None:
        self._task_agent = task_agent

        self.create = to_raw_response_wrapper(
            task_agent.create,
        )
        self.update = to_raw_response_wrapper(
            task_agent.update,
        )
        self.list = to_raw_response_wrapper(
            task_agent.list,
        )
        self.deactivate = to_raw_response_wrapper(
            task_agent.deactivate,
        )
        self.get = to_raw_response_wrapper(
            task_agent.get,
        )
        self.run = to_raw_response_wrapper(
            task_agent.run,
        )

    @cached_property
    def templates(self) -> TemplatesResourceWithRawResponse:
        return TemplatesResourceWithRawResponse(self._task_agent.templates)

    @cached_property
    def runs(self) -> RunsResourceWithRawResponse:
        return RunsResourceWithRawResponse(self._task_agent.runs)


class AsyncTaskAgentResourceWithRawResponse:
    def __init__(self, task_agent: AsyncTaskAgentResource) -> None:
        self._task_agent = task_agent

        self.create = async_to_raw_response_wrapper(
            task_agent.create,
        )
        self.update = async_to_raw_response_wrapper(
            task_agent.update,
        )
        self.list = async_to_raw_response_wrapper(
            task_agent.list,
        )
        self.deactivate = async_to_raw_response_wrapper(
            task_agent.deactivate,
        )
        self.get = async_to_raw_response_wrapper(
            task_agent.get,
        )
        self.run = async_to_raw_response_wrapper(
            task_agent.run,
        )

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithRawResponse:
        return AsyncTemplatesResourceWithRawResponse(self._task_agent.templates)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithRawResponse:
        return AsyncRunsResourceWithRawResponse(self._task_agent.runs)


class TaskAgentResourceWithStreamingResponse:
    def __init__(self, task_agent: TaskAgentResource) -> None:
        self._task_agent = task_agent

        self.create = to_streamed_response_wrapper(
            task_agent.create,
        )
        self.update = to_streamed_response_wrapper(
            task_agent.update,
        )
        self.list = to_streamed_response_wrapper(
            task_agent.list,
        )
        self.deactivate = to_streamed_response_wrapper(
            task_agent.deactivate,
        )
        self.get = to_streamed_response_wrapper(
            task_agent.get,
        )
        self.run = to_streamed_response_wrapper(
            task_agent.run,
        )

    @cached_property
    def templates(self) -> TemplatesResourceWithStreamingResponse:
        return TemplatesResourceWithStreamingResponse(self._task_agent.templates)

    @cached_property
    def runs(self) -> RunsResourceWithStreamingResponse:
        return RunsResourceWithStreamingResponse(self._task_agent.runs)


class AsyncTaskAgentResourceWithStreamingResponse:
    def __init__(self, task_agent: AsyncTaskAgentResource) -> None:
        self._task_agent = task_agent

        self.create = async_to_streamed_response_wrapper(
            task_agent.create,
        )
        self.update = async_to_streamed_response_wrapper(
            task_agent.update,
        )
        self.list = async_to_streamed_response_wrapper(
            task_agent.list,
        )
        self.deactivate = async_to_streamed_response_wrapper(
            task_agent.deactivate,
        )
        self.get = async_to_streamed_response_wrapper(
            task_agent.get,
        )
        self.run = async_to_streamed_response_wrapper(
            task_agent.run,
        )

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithStreamingResponse:
        return AsyncTemplatesResourceWithStreamingResponse(self._task_agent.templates)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithStreamingResponse:
        return AsyncRunsResourceWithStreamingResponse(self._task_agent.runs)
