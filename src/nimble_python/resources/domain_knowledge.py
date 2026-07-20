# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import domain_knowledge_get_driver_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.domain_knowledge_get_driver_response import DomainKnowledgeGetDriverResponse

__all__ = ["DomainKnowledgeResource", "AsyncDomainKnowledgeResource"]


class DomainKnowledgeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DomainKnowledgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Nimbleway/nimble-python#accessing-raw-response-data-eg-headers
        """
        return DomainKnowledgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainKnowledgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Nimbleway/nimble-python#with_streaming_response
        """
        return DomainKnowledgeResourceWithStreamingResponse(self)

    def get_driver(
        self,
        *,
        agent: str | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainKnowledgeGetDriverResponse:
        """Resolves the suggested driver for a given URL or agent name.

        Exactly one of
        `url` or `agent` must be provided.

        Args:
          agent: Agent name to resolve driver for (e.g. nimble-ecommerce).

          url: Target domain to resolve driver for (e.g. amazon.com).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/domain-knowledge/driver",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent": agent,
                        "url": url,
                    },
                    domain_knowledge_get_driver_params.DomainKnowledgeGetDriverParams,
                ),
            ),
            cast_to=DomainKnowledgeGetDriverResponse,
        )


class AsyncDomainKnowledgeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDomainKnowledgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Nimbleway/nimble-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDomainKnowledgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainKnowledgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Nimbleway/nimble-python#with_streaming_response
        """
        return AsyncDomainKnowledgeResourceWithStreamingResponse(self)

    async def get_driver(
        self,
        *,
        agent: str | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainKnowledgeGetDriverResponse:
        """Resolves the suggested driver for a given URL or agent name.

        Exactly one of
        `url` or `agent` must be provided.

        Args:
          agent: Agent name to resolve driver for (e.g. nimble-ecommerce).

          url: Target domain to resolve driver for (e.g. amazon.com).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/domain-knowledge/driver",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agent": agent,
                        "url": url,
                    },
                    domain_knowledge_get_driver_params.DomainKnowledgeGetDriverParams,
                ),
            ),
            cast_to=DomainKnowledgeGetDriverResponse,
        )


class DomainKnowledgeResourceWithRawResponse:
    def __init__(self, domain_knowledge: DomainKnowledgeResource) -> None:
        self._domain_knowledge = domain_knowledge

        self.get_driver = to_raw_response_wrapper(
            domain_knowledge.get_driver,
        )


class AsyncDomainKnowledgeResourceWithRawResponse:
    def __init__(self, domain_knowledge: AsyncDomainKnowledgeResource) -> None:
        self._domain_knowledge = domain_knowledge

        self.get_driver = async_to_raw_response_wrapper(
            domain_knowledge.get_driver,
        )


class DomainKnowledgeResourceWithStreamingResponse:
    def __init__(self, domain_knowledge: DomainKnowledgeResource) -> None:
        self._domain_knowledge = domain_knowledge

        self.get_driver = to_streamed_response_wrapper(
            domain_knowledge.get_driver,
        )


class AsyncDomainKnowledgeResourceWithStreamingResponse:
    def __init__(self, domain_knowledge: AsyncDomainKnowledgeResource) -> None:
        self._domain_knowledge = domain_knowledge

        self.get_driver = async_to_streamed_response_wrapper(
            domain_knowledge.get_driver,
        )
