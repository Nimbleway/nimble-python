# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Any, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.task_agent import run_list_params
from ...types.task_agent.run_get_response import RunGetResponse
from ...types.task_agent.run_list_response import RunListResponse
from ...types.task_agent.run_get_result_response import RunGetResultResponse

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

    @typing_extensions.deprecated("deprecated")
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
        List runs for this instance.

        `status` accepts a lowercase `TaskRunStatusValue` (e.g. "completed") or a
        comma-separated list of them (e.g. "queued,running").

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            path_template("/v1/task-agents/{agent_id}/runs", agent_id=agent_id),
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

    @typing_extensions.deprecated("deprecated")
    def cancel(
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
    ) -> None:
        """
        Cancel an in-progress or queued run.

        Verb is POST + `/cancel` action segment per the AGENTS-1666 spec (replaces the
        old `DELETE …/runs/{run_id}`).

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/v1/task-agents/{agent_id}/runs/{run_id}/cancel", agent_id=agent_id, run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
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
        """
        Fetch a run by id, scoped to the instance.

        A run resolves only when (run_id, agent_id) match — otherwise 404. This means a
        stale URL with a swapped agent_id won't leak runs across instances even if the
        run_id is real.

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
            path_template("/v1/task-agents/{agent_id}/runs/{run_id}", agent_id=agent_id, run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunGetResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def get_result(
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
    ) -> RunGetResultResponse:
        """
        Fetch the result for a terminal run on this instance.

        Mirrors the previous flat `GET /tasks/runs/:run_id/result` semantics:

        - 404 when the run doesn't belong to the agent.
        - 408 when the run is still active.
        - 422 (with TaskRunFailedResult body) when the run failed or was cancelled.
        - 200 (with TaskRunResult body) on success.

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
            RunGetResultResponse,
            self._get(
                path_template("/v1/task-agents/{agent_id}/runs/{run_id}/result", agent_id=agent_id, run_id=run_id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, RunGetResultResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @typing_extensions.deprecated("deprecated")
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
    ) -> None:
        """
        SSE stream of real-time progress events for a run on this instance.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/v1/task-agents/{agent_id}/runs/{run_id}/events", agent_id=agent_id, run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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

    @typing_extensions.deprecated("deprecated")
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
        List runs for this instance.

        `status` accepts a lowercase `TaskRunStatusValue` (e.g. "completed") or a
        comma-separated list of them (e.g. "queued,running").

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            path_template("/v1/task-agents/{agent_id}/runs", agent_id=agent_id),
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

    @typing_extensions.deprecated("deprecated")
    async def cancel(
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
    ) -> None:
        """
        Cancel an in-progress or queued run.

        Verb is POST + `/cancel` action segment per the AGENTS-1666 spec (replaces the
        old `DELETE …/runs/{run_id}`).

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/v1/task-agents/{agent_id}/runs/{run_id}/cancel", agent_id=agent_id, run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
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
        """
        Fetch a run by id, scoped to the instance.

        A run resolves only when (run_id, agent_id) match — otherwise 404. This means a
        stale URL with a swapped agent_id won't leak runs across instances even if the
        run_id is real.

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
            path_template("/v1/task-agents/{agent_id}/runs/{run_id}", agent_id=agent_id, run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunGetResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def get_result(
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
    ) -> RunGetResultResponse:
        """
        Fetch the result for a terminal run on this instance.

        Mirrors the previous flat `GET /tasks/runs/:run_id/result` semantics:

        - 404 when the run doesn't belong to the agent.
        - 408 when the run is still active.
        - 422 (with TaskRunFailedResult body) when the run failed or was cancelled.
        - 200 (with TaskRunResult body) on success.

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
            RunGetResultResponse,
            await self._get(
                path_template("/v1/task-agents/{agent_id}/runs/{run_id}/result", agent_id=agent_id, run_id=run_id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, RunGetResultResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @typing_extensions.deprecated("deprecated")
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
    ) -> None:
        """
        SSE stream of real-time progress events for a run on this instance.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/v1/task-agents/{agent_id}/runs/{run_id}/events", agent_id=agent_id, run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class RunsResourceWithRawResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                runs.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.cancel = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                runs.cancel,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                runs.get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_result = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                runs.get_result,  # pyright: ignore[reportDeprecated],
            )
        )
        self.stream_events = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                runs.stream_events,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncRunsResourceWithRawResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                runs.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.cancel = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                runs.cancel,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                runs.get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_result = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                runs.get_result,  # pyright: ignore[reportDeprecated],
            )
        )
        self.stream_events = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                runs.stream_events,  # pyright: ignore[reportDeprecated],
            )
        )


class RunsResourceWithStreamingResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                runs.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.cancel = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                runs.cancel,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                runs.get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_result = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                runs.get_result,  # pyright: ignore[reportDeprecated],
            )
        )
        self.stream_events = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                runs.stream_events,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncRunsResourceWithStreamingResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                runs.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.cancel = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                runs.cancel,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                runs.get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_result = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                runs.get_result,  # pyright: ignore[reportDeprecated],
            )
        )
        self.stream_events = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                runs.stream_events,  # pyright: ignore[reportDeprecated],
            )
        )
