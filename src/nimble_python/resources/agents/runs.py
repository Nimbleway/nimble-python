# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Union, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ..._base_client import make_request_options
from ...types.agents import run_list_params, run_create_params
from ...types.agents.run_get_response import RunGetResponse
from ...types.agents.run_list_response import RunListResponse
from ...types.agents.run_create_response import RunCreateResponse
from ...types.agents.run_result_response import RunResultResponse

__all__ = ["RunsResource", "AsyncRunsResource"]


class RunsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Nimbleway/nimble-python#accessing-raw-response-data-eg-headers
        """
        return RunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Nimbleway/nimble-python#with_streaming_response
        """
        return RunsResourceWithStreamingResponse(self)

    def create(
        self,
        agent_id: str,
        *,
        input: str,
        agent_name: Optional[str] | Omit = omit,
        effort: Optional[Literal["low", "medium", "high", "x-high", "5x-high", "max"]] | Omit = omit,
        enable_events: bool | Omit = omit,
        input_data: Union[Iterable[Dict[str, object]], Dict[str, object], None] | Omit = omit,
        origin: Literal["api"] | Omit = omit,
        output_schema: Optional[Dict[str, object]] | Omit = omit,
        previous_interaction_id: Optional[str] | Omit = omit,
        skill: Optional[str] | Omit = omit,
        sources: Optional[run_create_params.Sources] | Omit = omit,
        use_case: Optional[Literal["research", "enrichment", "dataset_building"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunCreateResponse:
        """Start an agent run.

        The run executes asynchronously: the response returns
        immediately with status `queued`, then poll `GET .../runs/{run_id}` until
        `completed` and fetch the output from `GET .../runs/{run_id}/result` — or set
        `enable_events: true` and follow `GET .../runs/{run_id}/events` for live
        progress.

        To enrich existing records instead of researching from scratch, pass them in
        `input_data`; this requires an `output_schema` (on the request or the agent).

        Args:
          input: User prompt or task instructions for the run.

          agent_name: Stable agent name. On this no-agent-id route, an unseen name creates a new
              agent; an existing name reuses it. Ignored on the /{agent_id}/runs route.

          effort: Canonical effort tier names for the research graph.

          enable_events: Whether to stream run events when supported.

          input_data: Existing records to ENRICH: a list of partial rows, or a single object,
              mirroring output_schema's shape.

          origin: Origin of public API runs. Public requests are always API-originated.

          output_schema: JSON schema overriding the agent's default structured output for this run.

          previous_interaction_id: Previous interaction identifier used to continue a conversation.

          skill: Skill override for this run. One-time only, except when this run creates a new
              agent via agent_name, in which case it becomes the new agent's stored skill.

          sources: Source guidance overriding the agent default.

          use_case: Only settable when this run creates a new agent (via agent_name, or when no
              agent is resolved), in which case it becomes the new agent's stored use_case.
              For a run against an existing agent, this must match the agent's own use_case —
              passing the same value is accepted as a no-op, a different value is rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            path_template("/v2/agents/{agent_id}/runs", agent_id=agent_id),
            body=maybe_transform(
                {
                    "input": input,
                    "agent_name": agent_name,
                    "effort": effort,
                    "enable_events": enable_events,
                    "input_data": input_data,
                    "origin": origin,
                    "output_schema": output_schema,
                    "previous_interaction_id": previous_interaction_id,
                    "skill": skill,
                    "sources": sources,
                    "use_case": use_case,
                },
                run_create_params.RunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunCreateResponse,
        )

    def list(
        self,
        agent_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunListResponse:
        """
        List the runs of an agent, newest first, paginated with `offset`/`limit`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            path_template("/v2/agents/{agent_id}/runs", agent_id=agent_id),
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
                    run_list_params.RunListParams,
                ),
            ),
            cast_to=RunListResponse,
        )

    def get(
        self,
        run_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunGetResponse:
        """Retrieve a run's current state.

        Poll this endpoint after creating a run: the run
        is finished once `status` is `completed`, `failed`, or `cancelled`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            path_template("/v2/agents/{agent_id}/runs/{run_id}", agent_id=agent_id, run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunGetResponse,
        )

    def result(
        self,
        run_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunResultResponse:
        """Fetch the output of a completed run.

        The `output` is `type: "text"` (a prose
        answer) or `type: "json"` (structured data matching the output schema), plus
        `trust` metadata with per-claim citations for the answer.

        While the run is still `queued` or `running` this endpoint returns `409`; if the
        run `failed` or was `cancelled` it returns `422` with the run and error details.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return cast(
            RunResultResponse,
            self._get(
                path_template("/v2/agents/{agent_id}/runs/{run_id}/result", agent_id=agent_id, run_id=run_id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, RunResultResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def stream_events(
        self,
        run_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[object]:
        """
        Stream a run's progress as
        [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)
        (`text/event-stream`). Create the run with `enable_events: true` to have events
        published. A keep-alive comment is sent every 15 seconds.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._get(
            path_template("/v2/agents/{agent_id}/runs/{run_id}/events", agent_id=agent_id, run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
            stream=True,
            stream_cls=Stream[object],
        )


class AsyncRunsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Nimbleway/nimble-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Nimbleway/nimble-python#with_streaming_response
        """
        return AsyncRunsResourceWithStreamingResponse(self)

    async def create(
        self,
        agent_id: str,
        *,
        input: str,
        agent_name: Optional[str] | Omit = omit,
        effort: Optional[Literal["low", "medium", "high", "x-high", "5x-high", "max"]] | Omit = omit,
        enable_events: bool | Omit = omit,
        input_data: Union[Iterable[Dict[str, object]], Dict[str, object], None] | Omit = omit,
        origin: Literal["api"] | Omit = omit,
        output_schema: Optional[Dict[str, object]] | Omit = omit,
        previous_interaction_id: Optional[str] | Omit = omit,
        skill: Optional[str] | Omit = omit,
        sources: Optional[run_create_params.Sources] | Omit = omit,
        use_case: Optional[Literal["research", "enrichment", "dataset_building"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunCreateResponse:
        """Start an agent run.

        The run executes asynchronously: the response returns
        immediately with status `queued`, then poll `GET .../runs/{run_id}` until
        `completed` and fetch the output from `GET .../runs/{run_id}/result` — or set
        `enable_events: true` and follow `GET .../runs/{run_id}/events` for live
        progress.

        To enrich existing records instead of researching from scratch, pass them in
        `input_data`; this requires an `output_schema` (on the request or the agent).

        Args:
          input: User prompt or task instructions for the run.

          agent_name: Stable agent name. On this no-agent-id route, an unseen name creates a new
              agent; an existing name reuses it. Ignored on the /{agent_id}/runs route.

          effort: Canonical effort tier names for the research graph.

          enable_events: Whether to stream run events when supported.

          input_data: Existing records to ENRICH: a list of partial rows, or a single object,
              mirroring output_schema's shape.

          origin: Origin of public API runs. Public requests are always API-originated.

          output_schema: JSON schema overriding the agent's default structured output for this run.

          previous_interaction_id: Previous interaction identifier used to continue a conversation.

          skill: Skill override for this run. One-time only, except when this run creates a new
              agent via agent_name, in which case it becomes the new agent's stored skill.

          sources: Source guidance overriding the agent default.

          use_case: Only settable when this run creates a new agent (via agent_name, or when no
              agent is resolved), in which case it becomes the new agent's stored use_case.
              For a run against an existing agent, this must match the agent's own use_case —
              passing the same value is accepted as a no-op, a different value is rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            path_template("/v2/agents/{agent_id}/runs", agent_id=agent_id),
            body=await async_maybe_transform(
                {
                    "input": input,
                    "agent_name": agent_name,
                    "effort": effort,
                    "enable_events": enable_events,
                    "input_data": input_data,
                    "origin": origin,
                    "output_schema": output_schema,
                    "previous_interaction_id": previous_interaction_id,
                    "skill": skill,
                    "sources": sources,
                    "use_case": use_case,
                },
                run_create_params.RunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunCreateResponse,
        )

    async def list(
        self,
        agent_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunListResponse:
        """
        List the runs of an agent, newest first, paginated with `offset`/`limit`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            path_template("/v2/agents/{agent_id}/runs", agent_id=agent_id),
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
                    run_list_params.RunListParams,
                ),
            ),
            cast_to=RunListResponse,
        )

    async def get(
        self,
        run_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunGetResponse:
        """Retrieve a run's current state.

        Poll this endpoint after creating a run: the run
        is finished once `status` is `completed`, `failed`, or `cancelled`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            path_template("/v2/agents/{agent_id}/runs/{run_id}", agent_id=agent_id, run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunGetResponse,
        )

    async def result(
        self,
        run_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunResultResponse:
        """Fetch the output of a completed run.

        The `output` is `type: "text"` (a prose
        answer) or `type: "json"` (structured data matching the output schema), plus
        `trust` metadata with per-claim citations for the answer.

        While the run is still `queued` or `running` this endpoint returns `409`; if the
        run `failed` or was `cancelled` it returns `422` with the run and error details.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return cast(
            RunResultResponse,
            await self._get(
                path_template("/v2/agents/{agent_id}/runs/{run_id}/result", agent_id=agent_id, run_id=run_id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, RunResultResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def stream_events(
        self,
        run_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[object]:
        """
        Stream a run's progress as
        [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)
        (`text/event-stream`). Create the run with `enable_events: true` to have events
        published. A keep-alive comment is sent every 15 seconds.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._get(
            path_template("/v2/agents/{agent_id}/runs/{run_id}/events", agent_id=agent_id, run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
            stream=True,
            stream_cls=AsyncStream[object],
        )


class RunsResourceWithRawResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.create = to_raw_response_wrapper(
            runs.create,
        )
        self.list = to_raw_response_wrapper(
            runs.list,
        )
        self.get = to_raw_response_wrapper(
            runs.get,
        )
        self.result = to_raw_response_wrapper(
            runs.result,
        )
        self.stream_events = to_raw_response_wrapper(
            runs.stream_events,
        )


class AsyncRunsResourceWithRawResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.create = async_to_raw_response_wrapper(
            runs.create,
        )
        self.list = async_to_raw_response_wrapper(
            runs.list,
        )
        self.get = async_to_raw_response_wrapper(
            runs.get,
        )
        self.result = async_to_raw_response_wrapper(
            runs.result,
        )
        self.stream_events = async_to_raw_response_wrapper(
            runs.stream_events,
        )


class RunsResourceWithStreamingResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.create = to_streamed_response_wrapper(
            runs.create,
        )
        self.list = to_streamed_response_wrapper(
            runs.list,
        )
        self.get = to_streamed_response_wrapper(
            runs.get,
        )
        self.result = to_streamed_response_wrapper(
            runs.result,
        )
        self.stream_events = to_streamed_response_wrapper(
            runs.stream_events,
        )


class AsyncRunsResourceWithStreamingResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.create = async_to_streamed_response_wrapper(
            runs.create,
        )
        self.list = async_to_streamed_response_wrapper(
            runs.list,
        )
        self.get = async_to_streamed_response_wrapper(
            runs.get,
        )
        self.result = async_to_streamed_response_wrapper(
            runs.result,
        )
        self.stream_events = async_to_streamed_response_wrapper(
            runs.stream_events,
        )
