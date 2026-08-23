# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from nimble_python import Nimble, AsyncNimble
from nimble_python.types import (
    SerpRunResponse,
    SerpRunAsyncResponse,
    SerpRunBatchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSerp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run(self, client: Nimble) -> None:
        serp = client.serp.run(
            search_engine="google_search",
        )
        assert_matches_type(SerpRunResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: Nimble) -> None:
        serp = client.serp.run(
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
        assert_matches_type(SerpRunResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: Nimble) -> None:
        response = client.serp.with_raw_response.run(
            search_engine="google_search",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        serp = response.parse()
        assert_matches_type(SerpRunResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: Nimble) -> None:
        with client.serp.with_streaming_response.run(
            search_engine="google_search",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            serp = response.parse()
            assert_matches_type(SerpRunResponse, serp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_async(self, client: Nimble) -> None:
        serp = client.serp.run_async(
            search_engine="google_search",
        )
        assert_matches_type(SerpRunAsyncResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_async_with_all_params(self, client: Nimble) -> None:
        serp = client.serp.run_async(
            search_engine="google_search",
            callback_url="https://example.com/webhook/callback",
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
            storage_compress=True,
            storage_object_name="result-2024-01-15.json",
            storage_type="s3",
            storage_url="s3://bucket-name/path/to/object",
        )
        assert_matches_type(SerpRunAsyncResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run_async(self, client: Nimble) -> None:
        response = client.serp.with_raw_response.run_async(
            search_engine="google_search",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        serp = response.parse()
        assert_matches_type(SerpRunAsyncResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run_async(self, client: Nimble) -> None:
        with client.serp.with_streaming_response.run_async(
            search_engine="google_search",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            serp = response.parse()
            assert_matches_type(SerpRunAsyncResponse, serp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_batch(self, client: Nimble) -> None:
        serp = client.serp.run_batch(
            inputs=[{}],
        )
        assert_matches_type(SerpRunBatchResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_batch_with_all_params(self, client: Nimble) -> None:
        serp = client.serp.run_batch(
            inputs=[
                {
                    "callback_url": "https://example.com/webhook/callback",
                    "country": "US",
                    "device": "desktop",
                    "domain": "com",
                    "locale": "en",
                    "location": "New York, New York, United States",
                    "num_results": 10,
                    "page": 1,
                    "parse": True,
                    "query": "nimble web data",
                    "render": False,
                    "resolve_url": True,
                    "search_engine": "google_search",
                    "show_hidden_results": False,
                    "storage_compress": True,
                    "storage_object_name": "result-2024-01-15.json",
                    "storage_type": "s3",
                    "storage_url": "s3://bucket-name/path/to/object",
                }
            ],
            shared_inputs={
                "callback_url": "https://example.com/webhook/callback",
                "country": "US",
                "device": "desktop",
                "domain": "com",
                "locale": "en",
                "location": "New York, New York, United States",
                "num_results": 10,
                "page": 1,
                "parse": True,
                "query": "nimble web data",
                "render": False,
                "resolve_url": True,
                "search_engine": "google_search",
                "show_hidden_results": False,
                "storage_compress": True,
                "storage_object_name": "result-2024-01-15.json",
                "storage_type": "s3",
                "storage_url": "s3://bucket-name/path/to/object",
            },
        )
        assert_matches_type(SerpRunBatchResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run_batch(self, client: Nimble) -> None:
        response = client.serp.with_raw_response.run_batch(
            inputs=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        serp = response.parse()
        assert_matches_type(SerpRunBatchResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run_batch(self, client: Nimble) -> None:
        with client.serp.with_streaming_response.run_batch(
            inputs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            serp = response.parse()
            assert_matches_type(SerpRunBatchResponse, serp, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSerp:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncNimble) -> None:
        serp = await async_client.serp.run(
            search_engine="google_search",
        )
        assert_matches_type(SerpRunResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncNimble) -> None:
        serp = await async_client.serp.run(
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
        assert_matches_type(SerpRunResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncNimble) -> None:
        response = await async_client.serp.with_raw_response.run(
            search_engine="google_search",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        serp = await response.parse()
        assert_matches_type(SerpRunResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncNimble) -> None:
        async with async_client.serp.with_streaming_response.run(
            search_engine="google_search",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            serp = await response.parse()
            assert_matches_type(SerpRunResponse, serp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_async(self, async_client: AsyncNimble) -> None:
        serp = await async_client.serp.run_async(
            search_engine="google_search",
        )
        assert_matches_type(SerpRunAsyncResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_async_with_all_params(self, async_client: AsyncNimble) -> None:
        serp = await async_client.serp.run_async(
            search_engine="google_search",
            callback_url="https://example.com/webhook/callback",
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
            storage_compress=True,
            storage_object_name="result-2024-01-15.json",
            storage_type="s3",
            storage_url="s3://bucket-name/path/to/object",
        )
        assert_matches_type(SerpRunAsyncResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run_async(self, async_client: AsyncNimble) -> None:
        response = await async_client.serp.with_raw_response.run_async(
            search_engine="google_search",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        serp = await response.parse()
        assert_matches_type(SerpRunAsyncResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run_async(self, async_client: AsyncNimble) -> None:
        async with async_client.serp.with_streaming_response.run_async(
            search_engine="google_search",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            serp = await response.parse()
            assert_matches_type(SerpRunAsyncResponse, serp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_batch(self, async_client: AsyncNimble) -> None:
        serp = await async_client.serp.run_batch(
            inputs=[{}],
        )
        assert_matches_type(SerpRunBatchResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_batch_with_all_params(self, async_client: AsyncNimble) -> None:
        serp = await async_client.serp.run_batch(
            inputs=[
                {
                    "callback_url": "https://example.com/webhook/callback",
                    "country": "US",
                    "device": "desktop",
                    "domain": "com",
                    "locale": "en",
                    "location": "New York, New York, United States",
                    "num_results": 10,
                    "page": 1,
                    "parse": True,
                    "query": "nimble web data",
                    "render": False,
                    "resolve_url": True,
                    "search_engine": "google_search",
                    "show_hidden_results": False,
                    "storage_compress": True,
                    "storage_object_name": "result-2024-01-15.json",
                    "storage_type": "s3",
                    "storage_url": "s3://bucket-name/path/to/object",
                }
            ],
            shared_inputs={
                "callback_url": "https://example.com/webhook/callback",
                "country": "US",
                "device": "desktop",
                "domain": "com",
                "locale": "en",
                "location": "New York, New York, United States",
                "num_results": 10,
                "page": 1,
                "parse": True,
                "query": "nimble web data",
                "render": False,
                "resolve_url": True,
                "search_engine": "google_search",
                "show_hidden_results": False,
                "storage_compress": True,
                "storage_object_name": "result-2024-01-15.json",
                "storage_type": "s3",
                "storage_url": "s3://bucket-name/path/to/object",
            },
        )
        assert_matches_type(SerpRunBatchResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run_batch(self, async_client: AsyncNimble) -> None:
        response = await async_client.serp.with_raw_response.run_batch(
            inputs=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        serp = await response.parse()
        assert_matches_type(SerpRunBatchResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run_batch(self, async_client: AsyncNimble) -> None:
        async with async_client.serp.with_streaming_response.run_batch(
            inputs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            serp = await response.parse()
            assert_matches_type(SerpRunBatchResponse, serp, path=["response"])

        assert cast(Any, response.is_closed) is True
