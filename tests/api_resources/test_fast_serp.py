# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from nimble_python import Nimble, AsyncNimble
from nimble_python.types import FastSerpRunResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFastSerp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run(self, client: Nimble) -> None:
        fast_serp = client.fast_serp.run(
            search_engine="google_search",
        )
        assert_matches_type(FastSerpRunResponse, fast_serp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: Nimble) -> None:
        fast_serp = client.fast_serp.run(
            search_engine="google_search",
            country="US",
            device="desktop",
            domain="com",
            locale="en",
            location="New York, New York, United States",
            num_results=10,
            page=1,
            parse=True,
            query="nimble web data",
            render=False,
            resolve_url=True,
            show_hidden_results=False,
        )
        assert_matches_type(FastSerpRunResponse, fast_serp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: Nimble) -> None:
        response = client.fast_serp.with_raw_response.run(
            search_engine="google_search",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fast_serp = response.parse()
        assert_matches_type(FastSerpRunResponse, fast_serp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: Nimble) -> None:
        with client.fast_serp.with_streaming_response.run(
            search_engine="google_search",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fast_serp = response.parse()
            assert_matches_type(FastSerpRunResponse, fast_serp, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFastSerp:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncNimble) -> None:
        fast_serp = await async_client.fast_serp.run(
            search_engine="google_search",
        )
        assert_matches_type(FastSerpRunResponse, fast_serp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncNimble) -> None:
        fast_serp = await async_client.fast_serp.run(
            search_engine="google_search",
            country="US",
            device="desktop",
            domain="com",
            locale="en",
            location="New York, New York, United States",
            num_results=10,
            page=1,
            parse=True,
            query="nimble web data",
            render=False,
            resolve_url=True,
            show_hidden_results=False,
        )
        assert_matches_type(FastSerpRunResponse, fast_serp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncNimble) -> None:
        response = await async_client.fast_serp.with_raw_response.run(
            search_engine="google_search",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fast_serp = await response.parse()
        assert_matches_type(FastSerpRunResponse, fast_serp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncNimble) -> None:
        async with async_client.fast_serp.with_streaming_response.run(
            search_engine="google_search",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fast_serp = await response.parse()
            assert_matches_type(FastSerpRunResponse, fast_serp, path=["response"])

        assert cast(Any, response.is_closed) is True
