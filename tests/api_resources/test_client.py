# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from nimble_python import Nimble, AsyncNimble
from nimble_python.types import (
    MapResponse,
    SearchResponse,
    ExtractResponse,
    ExtractAsyncResponse,
    ExtractBatchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClient:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract(self, client: Nimble) -> None:
        client_ = client.extract(
            url="url",
        )
        assert_matches_type(ExtractResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_with_all_params(self, client: Nimble) -> None:
        client_ = client.extract(
            url="url",
            browser="chrome",
            browser_actions=[
                {"goto": "https://example.com/login"},
                {"wait_for_element": "#login-form"},
                {
                    "fill": {
                        "selector": "#username",
                        "value": "user@example.com",
                        "click_on_element": True,
                        "delay": 1000,
                        "mode": "type",
                        "mouse_movement_strategy": "linear",
                        "required": "true",
                        "scroll": True,
                        "skip": "true",
                        "timeout": 0,
                        "typing_interval": 1000,
                        "typing_strategy": "simple",
                        "visible": True,
                    }
                },
                {
                    "fill": {
                        "selector": "#password",
                        "value": "password123",
                        "click_on_element": True,
                        "delay": 1000,
                        "mode": "type",
                        "mouse_movement_strategy": "linear",
                        "required": "true",
                        "scroll": True,
                        "skip": "true",
                        "timeout": 0,
                        "typing_interval": 1000,
                        "typing_strategy": "simple",
                        "visible": True,
                    }
                },
                {"click": "#submit"},
                {
                    "screenshot": {
                        "format": "png",
                        "full_page": True,
                        "quality": 0,
                        "required": "true",
                        "skip": "true",
                    }
                },
            ],
            city="Los Angeles",
            consent_header=True,
            cookies="sessionId=abc123; userId=user456",
            country="US",
            device="desktop",
            driver="vx8",
            expected_status_codes=[200, 201],
            formats=["html"],
            headers={
                "Accept-Language": "en-US",
                "User-Agent": "CustomBot/1.0",
            },
            http2=True,
            is_xhr=True,
            locale="en-US",
            markdown_backend="full_page",
            method="GET",
            network_capture=[
                {
                    "method": "GET",
                    "resource_type": "document",
                    "status_code": 100,
                    "url": {
                        "value": "value",
                        "type": "exact",
                    },
                    "validation": True,
                    "wait_for_requests_count": 0,
                    "wait_for_requests_count_timeout": 1,
                }
            ],
            os="windows",
            parse=True,
            parser={"myParser": "bar"},
            referrer_type="random",
            render=True,
            request_timeout=30000,
            session={
                "id": "id",
                "prefetch_userbrowser": True,
                "retry": True,
                "timeout": 1,
            },
            skill="dynamic-content",
            state="CA",
            tag="campaign-2024-q1",
        )
        assert_matches_type(ExtractResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_extract(self, client: Nimble) -> None:
        response = client.with_raw_response.extract(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(ExtractResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_extract(self, client: Nimble) -> None:
        with client.with_streaming_response.extract(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(ExtractResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_async(self, client: Nimble) -> None:
        client_ = client.extract_async(
            url="url",
        )
        assert_matches_type(ExtractAsyncResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_async_with_all_params(self, client: Nimble) -> None:
        client_ = client.extract_async(
            url="url",
            browser="chrome",
            browser_actions=[
                {"goto": "https://example.com/login"},
                {"wait_for_element": "#login-form"},
                {
                    "fill": {
                        "selector": "#username",
                        "value": "user@example.com",
                        "click_on_element": True,
                        "delay": 1000,
                        "mode": "type",
                        "mouse_movement_strategy": "linear",
                        "required": "true",
                        "scroll": True,
                        "skip": "true",
                        "timeout": 0,
                        "typing_interval": 1000,
                        "typing_strategy": "simple",
                        "visible": True,
                    }
                },
                {
                    "fill": {
                        "selector": "#password",
                        "value": "password123",
                        "click_on_element": True,
                        "delay": 1000,
                        "mode": "type",
                        "mouse_movement_strategy": "linear",
                        "required": "true",
                        "scroll": True,
                        "skip": "true",
                        "timeout": 0,
                        "typing_interval": 1000,
                        "typing_strategy": "simple",
                        "visible": True,
                    }
                },
                {"click": "#submit"},
                {
                    "screenshot": {
                        "format": "png",
                        "full_page": True,
                        "quality": 0,
                        "required": "true",
                        "skip": "true",
                    }
                },
            ],
            callback_url="https://example.com/webhook/callback",
            city="Los Angeles",
            consent_header=True,
            cookies="sessionId=abc123; userId=user456",
            country="US",
            device="desktop",
            driver="vx8",
            expected_status_codes=[200, 201],
            formats=["html"],
            headers={
                "Accept-Language": "en-US",
                "User-Agent": "CustomBot/1.0",
            },
            http2=True,
            is_xhr=True,
            locale="en-US",
            markdown_backend="full_page",
            method="GET",
            network_capture=[
                {
                    "method": "GET",
                    "resource_type": "document",
                    "status_code": 100,
                    "url": {
                        "value": "value",
                        "type": "exact",
                    },
                    "validation": True,
                    "wait_for_requests_count": 0,
                    "wait_for_requests_count_timeout": 1,
                }
            ],
            os="windows",
            parse=True,
            parser={"myParser": "bar"},
            referrer_type="random",
            render=True,
            request_timeout=30000,
            session={
                "id": "id",
                "prefetch_userbrowser": True,
                "retry": True,
                "timeout": 1,
            },
            skill="dynamic-content",
            state="CA",
            storage_compress=True,
            storage_object_name="result-2024-01-15.json",
            storage_type="s3",
            storage_url="s3://bucket-name/path/to/object",
            tag="campaign-2024-q1",
        )
        assert_matches_type(ExtractAsyncResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_extract_async(self, client: Nimble) -> None:
        response = client.with_raw_response.extract_async(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(ExtractAsyncResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_extract_async(self, client: Nimble) -> None:
        with client.with_streaming_response.extract_async(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(ExtractAsyncResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_batch(self, client: Nimble) -> None:
        client_ = client.extract_batch(
            inputs=[{}],
        )
        assert_matches_type(ExtractBatchResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_batch_with_all_params(self, client: Nimble) -> None:
        client_ = client.extract_batch(
            inputs=[
                {
                    "browser": "chrome",
                    "browser_actions": [
                        {"goto": "https://example.com/login"},
                        {"wait_for_element": "#login-form"},
                        {
                            "fill": {
                                "selector": "#username",
                                "value": "user@example.com",
                                "click_on_element": True,
                                "delay": 1000,
                                "mode": "type",
                                "mouse_movement_strategy": "linear",
                                "required": "true",
                                "scroll": True,
                                "skip": "true",
                                "timeout": 0,
                                "typing_interval": 1000,
                                "typing_strategy": "simple",
                                "visible": True,
                            }
                        },
                        {
                            "fill": {
                                "selector": "#password",
                                "value": "password123",
                                "click_on_element": True,
                                "delay": 1000,
                                "mode": "type",
                                "mouse_movement_strategy": "linear",
                                "required": "true",
                                "scroll": True,
                                "skip": "true",
                                "timeout": 0,
                                "typing_interval": 1000,
                                "typing_strategy": "simple",
                                "visible": True,
                            }
                        },
                        {"click": "#submit"},
                        {
                            "screenshot": {
                                "format": "png",
                                "full_page": True,
                                "quality": 0,
                                "required": "true",
                                "skip": "true",
                            }
                        },
                    ],
                    "callback_url": "https://example.com/webhook/callback",
                    "city": "Los Angeles",
                    "consent_header": True,
                    "cookies": "sessionId=abc123; userId=user456",
                    "country": "US",
                    "device": "desktop",
                    "driver": "vx8",
                    "expected_status_codes": [200, 201],
                    "formats": ["html"],
                    "headers": {
                        "Accept-Language": "en-US",
                        "User-Agent": "CustomBot/1.0",
                    },
                    "http2": True,
                    "is_xhr": True,
                    "locale": "en-US",
                    "markdown_backend": "full_page",
                    "method": "GET",
                    "network_capture": [
                        {
                            "method": "GET",
                            "resource_type": "document",
                            "status_code": 100,
                            "url": {
                                "value": "value",
                                "type": "exact",
                            },
                            "validation": True,
                            "wait_for_requests_count": 0,
                            "wait_for_requests_count_timeout": 1,
                        }
                    ],
                    "os": "windows",
                    "parse": True,
                    "parser": {"myParser": "bar"},
                    "referrer_type": "random",
                    "render": True,
                    "request_timeout": 30000,
                    "session": {
                        "id": "id",
                        "prefetch_userbrowser": True,
                        "retry": True,
                        "timeout": 1,
                    },
                    "skill": "dynamic-content",
                    "state": "CA",
                    "storage_compress": True,
                    "storage_object_name": "result-2024-01-15.json",
                    "storage_type": "s3",
                    "storage_url": "s3://bucket-name/path/to/object",
                    "tag": "campaign-2024-q1",
                    "url": "url",
                }
            ],
            shared_inputs={
                "browser": "chrome",
                "browser_actions": [
                    {"goto": "https://example.com/login"},
                    {"wait_for_element": "#login-form"},
                    {
                        "fill": {
                            "selector": "#username",
                            "value": "user@example.com",
                            "click_on_element": True,
                            "delay": 1000,
                            "mode": "type",
                            "mouse_movement_strategy": "linear",
                            "required": "true",
                            "scroll": True,
                            "skip": "true",
                            "timeout": 0,
                            "typing_interval": 1000,
                            "typing_strategy": "simple",
                            "visible": True,
                        }
                    },
                    {
                        "fill": {
                            "selector": "#password",
                            "value": "password123",
                            "click_on_element": True,
                            "delay": 1000,
                            "mode": "type",
                            "mouse_movement_strategy": "linear",
                            "required": "true",
                            "scroll": True,
                            "skip": "true",
                            "timeout": 0,
                            "typing_interval": 1000,
                            "typing_strategy": "simple",
                            "visible": True,
                        }
                    },
                    {"click": "#submit"},
                    {
                        "screenshot": {
                            "format": "png",
                            "full_page": True,
                            "quality": 0,
                            "required": "true",
                            "skip": "true",
                        }
                    },
                ],
                "callback_url": "https://example.com/webhook/callback",
                "city": "Los Angeles",
                "consent_header": True,
                "cookies": "sessionId=abc123; userId=user456",
                "country": "US",
                "device": "desktop",
                "driver": "vx8",
                "expected_status_codes": [200, 201],
                "formats": ["html"],
                "headers": {
                    "Accept-Language": "en-US",
                    "User-Agent": "CustomBot/1.0",
                },
                "http2": True,
                "is_xhr": True,
                "locale": "en-US",
                "markdown_backend": "full_page",
                "method": "GET",
                "network_capture": [
                    {
                        "method": "GET",
                        "resource_type": "document",
                        "status_code": 100,
                        "url": {
                            "value": "value",
                            "type": "exact",
                        },
                        "validation": True,
                        "wait_for_requests_count": 0,
                        "wait_for_requests_count_timeout": 1,
                    }
                ],
                "os": "windows",
                "parse": True,
                "parser": {"myParser": "bar"},
                "referrer_type": "random",
                "render": True,
                "request_timeout": 30000,
                "session": {
                    "id": "id",
                    "prefetch_userbrowser": True,
                    "retry": True,
                    "timeout": 1,
                },
                "skill": "dynamic-content",
                "state": "CA",
                "storage_compress": True,
                "storage_object_name": "result-2024-01-15.json",
                "storage_type": "s3",
                "storage_url": "s3://bucket-name/path/to/object",
                "tag": "campaign-2024-q1",
                "url": "url",
            },
        )
        assert_matches_type(ExtractBatchResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_extract_batch(self, client: Nimble) -> None:
        response = client.with_raw_response.extract_batch(
            inputs=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(ExtractBatchResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_extract_batch(self, client: Nimble) -> None:
        with client.with_streaming_response.extract_batch(
            inputs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(ExtractBatchResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_map(self, client: Nimble) -> None:
        client_ = client.map(
            url="url",
        )
        assert_matches_type(MapResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_map(self, client: Nimble) -> None:
        response = client.with_raw_response.map(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(MapResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Nimble) -> None:
        client_ = client.search(
            query="x",
        )
        assert_matches_type(SearchResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Nimble) -> None:
        client_ = client.search(
            query="x",
            content_type=["string"],
            country="country",
            deep_search=True,
            end_date="end_date",
            exclude_domains=["string"],
            focus="string",
            include_answer=True,
            include_domains=["string"],
            locale="locale",
            max_results=1,
            max_subagents=1,
            output_format="plain_text",
            search_depth="lite",
            start_date="start_date",
            time_range="hour",
        )
        assert_matches_type(SearchResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Nimble) -> None:
        response = client.with_raw_response.search(
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(SearchResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Nimble) -> None:
        with client.with_streaming_response.search(
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(SearchResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClient:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract(self, async_client: AsyncNimble) -> None:
        client = await async_client.extract(
            url="url",
        )
        assert_matches_type(ExtractResponse, client, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_with_all_params(self, async_client: AsyncNimble) -> None:
        client = await async_client.extract(
            url="url",
            browser="chrome",
            browser_actions=[
                {"goto": "https://example.com/login"},
                {"wait_for_element": "#login-form"},
                {
                    "fill": {
                        "selector": "#username",
                        "value": "user@example.com",
                        "click_on_element": True,
                        "delay": 1000,
                        "mode": "type",
                        "mouse_movement_strategy": "linear",
                        "required": "true",
                        "scroll": True,
                        "skip": "true",
                        "timeout": 0,
                        "typing_interval": 1000,
                        "typing_strategy": "simple",
                        "visible": True,
                    }
                },
                {
                    "fill": {
                        "selector": "#password",
                        "value": "password123",
                        "click_on_element": True,
                        "delay": 1000,
                        "mode": "type",
                        "mouse_movement_strategy": "linear",
                        "required": "true",
                        "scroll": True,
                        "skip": "true",
                        "timeout": 0,
                        "typing_interval": 1000,
                        "typing_strategy": "simple",
                        "visible": True,
                    }
                },
                {"click": "#submit"},
                {
                    "screenshot": {
                        "format": "png",
                        "full_page": True,
                        "quality": 0,
                        "required": "true",
                        "skip": "true",
                    }
                },
            ],
            city="Los Angeles",
            consent_header=True,
            cookies="sessionId=abc123; userId=user456",
            country="US",
            device="desktop",
            driver="vx8",
            expected_status_codes=[200, 201],
            formats=["html"],
            headers={
                "Accept-Language": "en-US",
                "User-Agent": "CustomBot/1.0",
            },
            http2=True,
            is_xhr=True,
            locale="en-US",
            markdown_backend="full_page",
            method="GET",
            network_capture=[
                {
                    "method": "GET",
                    "resource_type": "document",
                    "status_code": 100,
                    "url": {
                        "value": "value",
                        "type": "exact",
                    },
                    "validation": True,
                    "wait_for_requests_count": 0,
                    "wait_for_requests_count_timeout": 1,
                }
            ],
            os="windows",
            parse=True,
            parser={"myParser": "bar"},
            referrer_type="random",
            render=True,
            request_timeout=30000,
            session={
                "id": "id",
                "prefetch_userbrowser": True,
                "retry": True,
                "timeout": 1,
            },
            skill="dynamic-content",
            state="CA",
            tag="campaign-2024-q1",
        )
        assert_matches_type(ExtractResponse, client, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_extract(self, async_client: AsyncNimble) -> None:
        response = await async_client.with_raw_response.extract(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(ExtractResponse, client, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_extract(self, async_client: AsyncNimble) -> None:
        async with async_client.with_streaming_response.extract(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(ExtractResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_async(self, async_client: AsyncNimble) -> None:
        client = await async_client.extract_async(
            url="url",
        )
        assert_matches_type(ExtractAsyncResponse, client, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_async_with_all_params(self, async_client: AsyncNimble) -> None:
        client = await async_client.extract_async(
            url="url",
            browser="chrome",
            browser_actions=[
                {"goto": "https://example.com/login"},
                {"wait_for_element": "#login-form"},
                {
                    "fill": {
                        "selector": "#username",
                        "value": "user@example.com",
                        "click_on_element": True,
                        "delay": 1000,
                        "mode": "type",
                        "mouse_movement_strategy": "linear",
                        "required": "true",
                        "scroll": True,
                        "skip": "true",
                        "timeout": 0,
                        "typing_interval": 1000,
                        "typing_strategy": "simple",
                        "visible": True,
                    }
                },
                {
                    "fill": {
                        "selector": "#password",
                        "value": "password123",
                        "click_on_element": True,
                        "delay": 1000,
                        "mode": "type",
                        "mouse_movement_strategy": "linear",
                        "required": "true",
                        "scroll": True,
                        "skip": "true",
                        "timeout": 0,
                        "typing_interval": 1000,
                        "typing_strategy": "simple",
                        "visible": True,
                    }
                },
                {"click": "#submit"},
                {
                    "screenshot": {
                        "format": "png",
                        "full_page": True,
                        "quality": 0,
                        "required": "true",
                        "skip": "true",
                    }
                },
            ],
            callback_url="https://example.com/webhook/callback",
            city="Los Angeles",
            consent_header=True,
            cookies="sessionId=abc123; userId=user456",
            country="US",
            device="desktop",
            driver="vx8",
            expected_status_codes=[200, 201],
            formats=["html"],
            headers={
                "Accept-Language": "en-US",
                "User-Agent": "CustomBot/1.0",
            },
            http2=True,
            is_xhr=True,
            locale="en-US",
            markdown_backend="full_page",
            method="GET",
            network_capture=[
                {
                    "method": "GET",
                    "resource_type": "document",
                    "status_code": 100,
                    "url": {
                        "value": "value",
                        "type": "exact",
                    },
                    "validation": True,
                    "wait_for_requests_count": 0,
                    "wait_for_requests_count_timeout": 1,
                }
            ],
            os="windows",
            parse=True,
            parser={"myParser": "bar"},
            referrer_type="random",
            render=True,
            request_timeout=30000,
            session={
                "id": "id",
                "prefetch_userbrowser": True,
                "retry": True,
                "timeout": 1,
            },
            skill="dynamic-content",
            state="CA",
            storage_compress=True,
            storage_object_name="result-2024-01-15.json",
            storage_type="s3",
            storage_url="s3://bucket-name/path/to/object",
            tag="campaign-2024-q1",
        )
        assert_matches_type(ExtractAsyncResponse, client, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_extract_async(self, async_client: AsyncNimble) -> None:
        response = await async_client.with_raw_response.extract_async(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(ExtractAsyncResponse, client, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_extract_async(self, async_client: AsyncNimble) -> None:
        async with async_client.with_streaming_response.extract_async(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(ExtractAsyncResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_batch(self, async_client: AsyncNimble) -> None:
        client = await async_client.extract_batch(
            inputs=[{}],
        )
        assert_matches_type(ExtractBatchResponse, client, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_batch_with_all_params(self, async_client: AsyncNimble) -> None:
        client = await async_client.extract_batch(
            inputs=[
                {
                    "browser": "chrome",
                    "browser_actions": [
                        {"goto": "https://example.com/login"},
                        {"wait_for_element": "#login-form"},
                        {
                            "fill": {
                                "selector": "#username",
                                "value": "user@example.com",
                                "click_on_element": True,
                                "delay": 1000,
                                "mode": "type",
                                "mouse_movement_strategy": "linear",
                                "required": "true",
                                "scroll": True,
                                "skip": "true",
                                "timeout": 0,
                                "typing_interval": 1000,
                                "typing_strategy": "simple",
                                "visible": True,
                            }
                        },
                        {
                            "fill": {
                                "selector": "#password",
                                "value": "password123",
                                "click_on_element": True,
                                "delay": 1000,
                                "mode": "type",
                                "mouse_movement_strategy": "linear",
                                "required": "true",
                                "scroll": True,
                                "skip": "true",
                                "timeout": 0,
                                "typing_interval": 1000,
                                "typing_strategy": "simple",
                                "visible": True,
                            }
                        },
                        {"click": "#submit"},
                        {
                            "screenshot": {
                                "format": "png",
                                "full_page": True,
                                "quality": 0,
                                "required": "true",
                                "skip": "true",
                            }
                        },
                    ],
                    "callback_url": "https://example.com/webhook/callback",
                    "city": "Los Angeles",
                    "consent_header": True,
                    "cookies": "sessionId=abc123; userId=user456",
                    "country": "US",
                    "device": "desktop",
                    "driver": "vx8",
                    "expected_status_codes": [200, 201],
                    "formats": ["html"],
                    "headers": {
                        "Accept-Language": "en-US",
                        "User-Agent": "CustomBot/1.0",
                    },
                    "http2": True,
                    "is_xhr": True,
                    "locale": "en-US",
                    "markdown_backend": "full_page",
                    "method": "GET",
                    "network_capture": [
                        {
                            "method": "GET",
                            "resource_type": "document",
                            "status_code": 100,
                            "url": {
                                "value": "value",
                                "type": "exact",
                            },
                            "validation": True,
                            "wait_for_requests_count": 0,
                            "wait_for_requests_count_timeout": 1,
                        }
                    ],
                    "os": "windows",
                    "parse": True,
                    "parser": {"myParser": "bar"},
                    "referrer_type": "random",
                    "render": True,
                    "request_timeout": 30000,
                    "session": {
                        "id": "id",
                        "prefetch_userbrowser": True,
                        "retry": True,
                        "timeout": 1,
                    },
                    "skill": "dynamic-content",
                    "state": "CA",
                    "storage_compress": True,
                    "storage_object_name": "result-2024-01-15.json",
                    "storage_type": "s3",
                    "storage_url": "s3://bucket-name/path/to/object",
                    "tag": "campaign-2024-q1",
                    "url": "url",
                }
            ],
            shared_inputs={
                "browser": "chrome",
                "browser_actions": [
                    {"goto": "https://example.com/login"},
                    {"wait_for_element": "#login-form"},
                    {
                        "fill": {
                            "selector": "#username",
                            "value": "user@example.com",
                            "click_on_element": True,
                            "delay": 1000,
                            "mode": "type",
                            "mouse_movement_strategy": "linear",
                            "required": "true",
                            "scroll": True,
                            "skip": "true",
                            "timeout": 0,
                            "typing_interval": 1000,
                            "typing_strategy": "simple",
                            "visible": True,
                        }
                    },
                    {
                        "fill": {
                            "selector": "#password",
                            "value": "password123",
                            "click_on_element": True,
                            "delay": 1000,
                            "mode": "type",
                            "mouse_movement_strategy": "linear",
                            "required": "true",
                            "scroll": True,
                            "skip": "true",
                            "timeout": 0,
                            "typing_interval": 1000,
                            "typing_strategy": "simple",
                            "visible": True,
                        }
                    },
                    {"click": "#submit"},
                    {
                        "screenshot": {
                            "format": "png",
                            "full_page": True,
                            "quality": 0,
                            "required": "true",
                            "skip": "true",
                        }
                    },
                ],
                "callback_url": "https://example.com/webhook/callback",
                "city": "Los Angeles",
                "consent_header": True,
                "cookies": "sessionId=abc123; userId=user456",
                "country": "US",
                "device": "desktop",
                "driver": "vx8",
                "expected_status_codes": [200, 201],
                "formats": ["html"],
                "headers": {
                    "Accept-Language": "en-US",
                    "User-Agent": "CustomBot/1.0",
                },
                "http2": True,
                "is_xhr": True,
                "locale": "en-US",
                "markdown_backend": "full_page",
                "method": "GET",
                "network_capture": [
                    {
                        "method": "GET",
                        "resource_type": "document",
                        "status_code": 100,
                        "url": {
                            "value": "value",
                            "type": "exact",
                        },
                        "validation": True,
                        "wait_for_requests_count": 0,
                        "wait_for_requests_count_timeout": 1,
                    }
                ],
                "os": "windows",
                "parse": True,
                "parser": {"myParser": "bar"},
                "referrer_type": "random",
                "render": True,
                "request_timeout": 30000,
                "session": {
                    "id": "id",
                    "prefetch_userbrowser": True,
                    "retry": True,
                    "timeout": 1,
                },
                "skill": "dynamic-content",
                "state": "CA",
                "storage_compress": True,
                "storage_object_name": "result-2024-01-15.json",
                "storage_type": "s3",
                "storage_url": "s3://bucket-name/path/to/object",
                "tag": "campaign-2024-q1",
                "url": "url",
            },
        )
        assert_matches_type(ExtractBatchResponse, client, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_extract_batch(self, async_client: AsyncNimble) -> None:
        response = await async_client.with_raw_response.extract_batch(
            inputs=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(ExtractBatchResponse, client, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_extract_batch(self, async_client: AsyncNimble) -> None:
        async with async_client.with_streaming_response.extract_batch(
            inputs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(ExtractBatchResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_map(self, async_client: AsyncNimble) -> None:
        client = await async_client.map(
            url="url",
        )
        assert_matches_type(MapResponse, client, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_map(self, async_client: AsyncNimble) -> None:
        response = await async_client.with_raw_response.map(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(MapResponse, client, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncNimble) -> None:
        client = await async_client.search(
            query="x",
        )
        assert_matches_type(SearchResponse, client, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncNimble) -> None:
        client = await async_client.search(
            query="x",
            content_type=["string"],
            country="country",
            deep_search=True,
            end_date="end_date",
            exclude_domains=["string"],
            focus="string",
            include_answer=True,
            include_domains=["string"],
            locale="locale",
            max_results=1,
            max_subagents=1,
            output_format="plain_text",
            search_depth="lite",
            start_date="start_date",
            time_range="hour",
        )
        assert_matches_type(SearchResponse, client, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncNimble) -> None:
        response = await async_client.with_raw_response.search(
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(SearchResponse, client, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncNimble) -> None:
        async with async_client.with_streaming_response.search(
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(SearchResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True
