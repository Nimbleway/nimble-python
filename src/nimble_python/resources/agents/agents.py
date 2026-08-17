# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
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
from ...types import agent_run_params, agent_list_params, agent_create_params, agent_update_params
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
from ...types.agent_get_response import AgentGetResponse
from ...types.agent_run_response import AgentRunResponse
from ...types.agent_list_response import AgentListResponse
from ...types.agent_create_response import AgentCreateResponse
from ...types.agent_update_response import AgentUpdateResponse

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def templates(self) -> TemplatesResource:
        return TemplatesResource(self._client)

    @cached_property
    def runs(self) -> RunsResource:
        return RunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Nimbleway/nimble-python#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Nimbleway/nimble-python#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        agent_name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        effort: Literal["low", "medium", "high", "x-high", "5x-high", "max"] | Omit = omit,
        goals: SequenceNotStr[str] | Omit = omit,
        icon: Optional[str] | Omit = omit,
        is_active: bool | Omit = omit,
        output_schema: Optional[Dict[str, object]] | Omit = omit,
        skill: Optional[str] | Omit = omit,
        sources: agent_create_params.Sources | Omit = omit,
        suggested_questions: SequenceNotStr[str] | Omit = omit,
        template: Optional[str] | Omit = omit,
        use_case: Optional[Literal["research", "enrichment", "dataset_building"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentCreateResponse:
        """Create a Web Search Agent.

        Either pass `template` to materialize a pre-built
        template (its fields, goals, sources, and suggested questions are copied), or
        define the agent from scratch with `display_name`, `goals`, `sources`, and an
        optional `output_schema` for structured results.

        Args:
          agent_name: Stable agent name.

          description: Agent description shown to users.

          display_name: Human-friendly agent name shown to users.

          effort: Default effort level for this agent's runs.

          goals: Ordered goals for the agent to follow.

          icon: Icon identifier used when presenting the agent.

          is_active: Whether the agent can be used to start new runs.

          output_schema: JSON schema describing the structured output the agent should produce.

          skill: Skill or operating context for the agent.

          sources: Source guidance for the agent.

          suggested_questions: Suggested prompts users can run with this agent.

          template: Template name to materialize this instance from. When set, the scalar fields and
              child rows are copied from the template.

          use_case: Primary use case supported by the agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/agents",
            body=maybe_transform(
                {
                    "agent_name": agent_name,
                    "description": description,
                    "display_name": display_name,
                    "effort": effort,
                    "goals": goals,
                    "icon": icon,
                    "is_active": is_active,
                    "output_schema": output_schema,
                    "skill": skill,
                    "sources": sources,
                    "suggested_questions": suggested_questions,
                    "template": template,
                    "use_case": use_case,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentCreateResponse,
        )

    def update(
        self,
        agent_id: str,
        *,
        body: Iterable[agent_update_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentUpdateResponse:
        """
        Update an agent with a
        [JSON Patch](https://datatracker.ietf.org/doc/html/rfc6902) document — an array
        of `{op, path, value}` operations applied to the agent, e.g.
        `[{"op": "replace", "path": "/display_name", "value": "My agent"}]`. Returns the
        updated agent.

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
            path_template("/v2/agents/{agent_id}", agent_id=agent_id),
            body=maybe_transform(body, Iterable[agent_update_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentUpdateResponse,
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
    ) -> AgentListResponse:
        """List the active Web Search Agents in your account.

        Results are scoped to the
        workspace resolved from your token (or the optional `workspace_id` query
        parameter) and paginated with `offset`/`limit`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/agents",
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
                    agent_list_params.AgentListParams,
                ),
            ),
            cast_to=AgentListResponse,
        )

    def delete(
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
        """Deactivate an agent.

        This is a soft delete: the agent can no longer start new
        runs, but its existing runs and their results remain retrievable.

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
            path_template("/v2/agents/{agent_id}", agent_id=agent_id),
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
    ) -> AgentGetResponse:
        """
        Retrieve a single Web Search Agent by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            path_template("/v2/agents/{agent_id}", agent_id=agent_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGetResponse,
        )

    def run(
        self,
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
        sources: Optional[agent_run_params.Sources] | Omit = omit,
        use_case: Optional[Literal["research", "enrichment", "dataset_building"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRunResponse:
        """Creates a minimal persistent Web Search Agent and starts a run for it.

        The
        response includes `web_search_agent_id` for later agent and run queries.

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
        return self._post(
            "/v2/agents/runs",
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
                agent_run_params.AgentRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRunResponse,
        )


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def templates(self) -> AsyncTemplatesResource:
        return AsyncTemplatesResource(self._client)

    @cached_property
    def runs(self) -> AsyncRunsResource:
        return AsyncRunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Nimbleway/nimble-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Nimbleway/nimble-python#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        agent_name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        effort: Literal["low", "medium", "high", "x-high", "5x-high", "max"] | Omit = omit,
        goals: SequenceNotStr[str] | Omit = omit,
        icon: Optional[str] | Omit = omit,
        is_active: bool | Omit = omit,
        output_schema: Optional[Dict[str, object]] | Omit = omit,
        skill: Optional[str] | Omit = omit,
        sources: agent_create_params.Sources | Omit = omit,
        suggested_questions: SequenceNotStr[str] | Omit = omit,
        template: Optional[str] | Omit = omit,
        use_case: Optional[Literal["research", "enrichment", "dataset_building"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentCreateResponse:
        """Create a Web Search Agent.

        Either pass `template` to materialize a pre-built
        template (its fields, goals, sources, and suggested questions are copied), or
        define the agent from scratch with `display_name`, `goals`, `sources`, and an
        optional `output_schema` for structured results.

        Args:
          agent_name: Stable agent name.

          description: Agent description shown to users.

          display_name: Human-friendly agent name shown to users.

          effort: Default effort level for this agent's runs.

          goals: Ordered goals for the agent to follow.

          icon: Icon identifier used when presenting the agent.

          is_active: Whether the agent can be used to start new runs.

          output_schema: JSON schema describing the structured output the agent should produce.

          skill: Skill or operating context for the agent.

          sources: Source guidance for the agent.

          suggested_questions: Suggested prompts users can run with this agent.

          template: Template name to materialize this instance from. When set, the scalar fields and
              child rows are copied from the template.

          use_case: Primary use case supported by the agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/agents",
            body=await async_maybe_transform(
                {
                    "agent_name": agent_name,
                    "description": description,
                    "display_name": display_name,
                    "effort": effort,
                    "goals": goals,
                    "icon": icon,
                    "is_active": is_active,
                    "output_schema": output_schema,
                    "skill": skill,
                    "sources": sources,
                    "suggested_questions": suggested_questions,
                    "template": template,
                    "use_case": use_case,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentCreateResponse,
        )

    async def update(
        self,
        agent_id: str,
        *,
        body: Iterable[agent_update_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentUpdateResponse:
        """
        Update an agent with a
        [JSON Patch](https://datatracker.ietf.org/doc/html/rfc6902) document — an array
        of `{op, path, value}` operations applied to the agent, e.g.
        `[{"op": "replace", "path": "/display_name", "value": "My agent"}]`. Returns the
        updated agent.

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
            path_template("/v2/agents/{agent_id}", agent_id=agent_id),
            body=await async_maybe_transform(body, Iterable[agent_update_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentUpdateResponse,
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
    ) -> AgentListResponse:
        """List the active Web Search Agents in your account.

        Results are scoped to the
        workspace resolved from your token (or the optional `workspace_id` query
        parameter) and paginated with `offset`/`limit`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/agents",
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
                    agent_list_params.AgentListParams,
                ),
            ),
            cast_to=AgentListResponse,
        )

    async def delete(
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
        """Deactivate an agent.

        This is a soft delete: the agent can no longer start new
        runs, but its existing runs and their results remain retrievable.

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
            path_template("/v2/agents/{agent_id}", agent_id=agent_id),
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
    ) -> AgentGetResponse:
        """
        Retrieve a single Web Search Agent by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            path_template("/v2/agents/{agent_id}", agent_id=agent_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGetResponse,
        )

    async def run(
        self,
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
        sources: Optional[agent_run_params.Sources] | Omit = omit,
        use_case: Optional[Literal["research", "enrichment", "dataset_building"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRunResponse:
        """Creates a minimal persistent Web Search Agent and starts a run for it.

        The
        response includes `web_search_agent_id` for later agent and run queries.

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
        return await self._post(
            "/v2/agents/runs",
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
                agent_run_params.AgentRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRunResponse,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_raw_response_wrapper(
            agents.create,
        )
        self.update = to_raw_response_wrapper(
            agents.update,
        )
        self.list = to_raw_response_wrapper(
            agents.list,
        )
        self.delete = to_raw_response_wrapper(
            agents.delete,
        )
        self.get = to_raw_response_wrapper(
            agents.get,
        )
        self.run = to_raw_response_wrapper(
            agents.run,
        )

    @cached_property
    def templates(self) -> TemplatesResourceWithRawResponse:
        return TemplatesResourceWithRawResponse(self._agents.templates)

    @cached_property
    def runs(self) -> RunsResourceWithRawResponse:
        return RunsResourceWithRawResponse(self._agents.runs)


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_raw_response_wrapper(
            agents.create,
        )
        self.update = async_to_raw_response_wrapper(
            agents.update,
        )
        self.list = async_to_raw_response_wrapper(
            agents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            agents.delete,
        )
        self.get = async_to_raw_response_wrapper(
            agents.get,
        )
        self.run = async_to_raw_response_wrapper(
            agents.run,
        )

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithRawResponse:
        return AsyncTemplatesResourceWithRawResponse(self._agents.templates)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithRawResponse:
        return AsyncRunsResourceWithRawResponse(self._agents.runs)


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_streamed_response_wrapper(
            agents.create,
        )
        self.update = to_streamed_response_wrapper(
            agents.update,
        )
        self.list = to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = to_streamed_response_wrapper(
            agents.delete,
        )
        self.get = to_streamed_response_wrapper(
            agents.get,
        )
        self.run = to_streamed_response_wrapper(
            agents.run,
        )

    @cached_property
    def templates(self) -> TemplatesResourceWithStreamingResponse:
        return TemplatesResourceWithStreamingResponse(self._agents.templates)

    @cached_property
    def runs(self) -> RunsResourceWithStreamingResponse:
        return RunsResourceWithStreamingResponse(self._agents.runs)


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_streamed_response_wrapper(
            agents.create,
        )
        self.update = async_to_streamed_response_wrapper(
            agents.update,
        )
        self.list = async_to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            agents.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            agents.get,
        )
        self.run = async_to_streamed_response_wrapper(
            agents.run,
        )

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithStreamingResponse:
        return AsyncTemplatesResourceWithStreamingResponse(self._agents.templates)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithStreamingResponse:
        return AsyncRunsResourceWithStreamingResponse(self._agents.runs)
