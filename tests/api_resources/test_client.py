# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from nimble_python import Nimble, AsyncNimble
from nimble_python.types import MapResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClient:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_map(self, client: Nimble) -> None:
        client_ = client.map(
            url="url",
        )
        assert_matches_type(MapResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_map_with_all_params(self, client: Nimble) -> None:
        client_ = client.map(
            url="url",
            country="US",
            domain_filter="all",
            limit=1000,
            locale="en-US",
            sitemap="include",
        )
        assert_matches_type(MapResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_map(self, client: Nimble) -> None:
        response = client.with_raw_response.map(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(MapResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_map(self, client: Nimble) -> None:
        with client.with_streaming_response.map(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(MapResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClient:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_map(self, async_client: AsyncNimble) -> None:
        client = await async_client.map(
            url="url",
        )
        assert_matches_type(MapResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_map_with_all_params(self, async_client: AsyncNimble) -> None:
        client = await async_client.map(
            url="url",
            country="US",
            domain_filter="all",
            limit=1000,
            locale="en-US",
            sitemap="include",
        )
        assert_matches_type(MapResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_map(self, async_client: AsyncNimble) -> None:
        response = await async_client.with_raw_response.map(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(MapResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_map(self, async_client: AsyncNimble) -> None:
        async with async_client.with_streaming_response.map(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(MapResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True
