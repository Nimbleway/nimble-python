# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.jobs.runs.artifact_get_response import ArtifactGetResponse
from ....types.jobs.runs.artifact_list_response import ArtifactListResponse
from ....types.jobs.runs.artifact_preview_response import ArtifactPreviewResponse
from ....types.jobs.runs.artifact_download_url_response import ArtifactDownloadURLResponse

__all__ = ["ArtifactsResource", "AsyncArtifactsResource"]


class ArtifactsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ArtifactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Nimbleway/nimble-python#accessing-raw-response-data-eg-headers
        """
        return ArtifactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArtifactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Nimbleway/nimble-python#with_streaming_response
        """
        return ArtifactsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def list(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArtifactListResponse:
        """
        List Run Artifacts

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            path_template("/v1/jobs/runs/{run_id}/artifacts", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArtifactListResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def download_url(
        self,
        artifact_id: int,
        *,
        run_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArtifactDownloadURLResponse:
        """
        Get Run Artifact Download URL

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            path_template(
                "/v1/jobs/runs/{run_id}/artifacts/{artifact_id}/download-url", run_id=run_id, artifact_id=artifact_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArtifactDownloadURLResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def get(
        self,
        artifact_id: int,
        *,
        run_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArtifactGetResponse:
        """
        Get Run Artifact

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            path_template("/v1/jobs/runs/{run_id}/artifacts/{artifact_id}", run_id=run_id, artifact_id=artifact_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArtifactGetResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def preview(
        self,
        artifact_id: int,
        *,
        run_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArtifactPreviewResponse:
        """
        Preview Run Artifact

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            path_template(
                "/v1/jobs/runs/{run_id}/artifacts/{artifact_id}/preview", run_id=run_id, artifact_id=artifact_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArtifactPreviewResponse,
        )


class AsyncArtifactsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncArtifactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Nimbleway/nimble-python#accessing-raw-response-data-eg-headers
        """
        return AsyncArtifactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArtifactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Nimbleway/nimble-python#with_streaming_response
        """
        return AsyncArtifactsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def list(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArtifactListResponse:
        """
        List Run Artifacts

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            path_template("/v1/jobs/runs/{run_id}/artifacts", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArtifactListResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def download_url(
        self,
        artifact_id: int,
        *,
        run_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArtifactDownloadURLResponse:
        """
        Get Run Artifact Download URL

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            path_template(
                "/v1/jobs/runs/{run_id}/artifacts/{artifact_id}/download-url", run_id=run_id, artifact_id=artifact_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArtifactDownloadURLResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def get(
        self,
        artifact_id: int,
        *,
        run_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArtifactGetResponse:
        """
        Get Run Artifact

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            path_template("/v1/jobs/runs/{run_id}/artifacts/{artifact_id}", run_id=run_id, artifact_id=artifact_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArtifactGetResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def preview(
        self,
        artifact_id: int,
        *,
        run_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArtifactPreviewResponse:
        """
        Preview Run Artifact

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            path_template(
                "/v1/jobs/runs/{run_id}/artifacts/{artifact_id}/preview", run_id=run_id, artifact_id=artifact_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArtifactPreviewResponse,
        )


class ArtifactsResourceWithRawResponse:
    def __init__(self, artifacts: ArtifactsResource) -> None:
        self._artifacts = artifacts

        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                artifacts.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.download_url = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                artifacts.download_url,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                artifacts.get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.preview = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                artifacts.preview,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncArtifactsResourceWithRawResponse:
    def __init__(self, artifacts: AsyncArtifactsResource) -> None:
        self._artifacts = artifacts

        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                artifacts.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.download_url = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                artifacts.download_url,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                artifacts.get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.preview = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                artifacts.preview,  # pyright: ignore[reportDeprecated],
            )
        )


class ArtifactsResourceWithStreamingResponse:
    def __init__(self, artifacts: ArtifactsResource) -> None:
        self._artifacts = artifacts

        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                artifacts.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.download_url = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                artifacts.download_url,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                artifacts.get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.preview = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                artifacts.preview,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncArtifactsResourceWithStreamingResponse:
    def __init__(self, artifacts: AsyncArtifactsResource) -> None:
        self._artifacts = artifacts

        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                artifacts.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.download_url = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                artifacts.download_url,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                artifacts.get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.preview = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                artifacts.preview,  # pyright: ignore[reportDeprecated],
            )
        )
