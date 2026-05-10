# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from nimble_python import Nimble, AsyncNimble
from nimble_python.types import DomainKnowledgeGetDriverResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDomainKnowledge:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_driver(self, client: Nimble) -> None:
        domain_knowledge = client.domain_knowledge.get_driver()
        assert_matches_type(DomainKnowledgeGetDriverResponse, domain_knowledge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_driver_with_all_params(self, client: Nimble) -> None:
        domain_knowledge = client.domain_knowledge.get_driver(
            agent="nimble-ecommerce",
            url="amazon.com",
        )
        assert_matches_type(DomainKnowledgeGetDriverResponse, domain_knowledge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_driver(self, client: Nimble) -> None:
        response = client.domain_knowledge.with_raw_response.get_driver()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain_knowledge = response.parse()
        assert_matches_type(DomainKnowledgeGetDriverResponse, domain_knowledge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_driver(self, client: Nimble) -> None:
        with client.domain_knowledge.with_streaming_response.get_driver() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain_knowledge = response.parse()
            assert_matches_type(DomainKnowledgeGetDriverResponse, domain_knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDomainKnowledge:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_driver(self, async_client: AsyncNimble) -> None:
        domain_knowledge = await async_client.domain_knowledge.get_driver()
        assert_matches_type(DomainKnowledgeGetDriverResponse, domain_knowledge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_driver_with_all_params(self, async_client: AsyncNimble) -> None:
        domain_knowledge = await async_client.domain_knowledge.get_driver(
            agent="nimble-ecommerce",
            url="amazon.com",
        )
        assert_matches_type(DomainKnowledgeGetDriverResponse, domain_knowledge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_driver(self, async_client: AsyncNimble) -> None:
        response = await async_client.domain_knowledge.with_raw_response.get_driver()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain_knowledge = await response.parse()
        assert_matches_type(DomainKnowledgeGetDriverResponse, domain_knowledge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_driver(self, async_client: AsyncNimble) -> None:
        async with async_client.domain_knowledge.with_streaming_response.get_driver() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain_knowledge = await response.parse()
            assert_matches_type(DomainKnowledgeGetDriverResponse, domain_knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True
