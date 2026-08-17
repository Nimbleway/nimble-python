# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from nimble_python import Nimble, AsyncNimble
from nimble_python.types import (
    ExtractRunResponse,
    ExtractAsyncResponse,
    ExtractBatchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExtract:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_async(self, client: Nimble) -> None:
        extract = client.extract.async_(
            url="url",
        )
        assert_matches_type(ExtractAsyncResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_async_with_all_params(self, client: Nimble) -> None:
        extract = client.extract.async_(
            url="url",
            auto_driver_configuration={
                "vx10": 2,
                "vx10-pro": 0,
                "vx6-fast": 1,
                "vx6-stealth": 1,
                "vx8": 5,
                "vx8-pro": 5,
            },
            body={"key": "value"},
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
            realtime_total_timeout=15000,
            referrer_type="random",
            render=True,
            request_timeout=30000,
            session={
                "id": "id",
                "prefetch_userbrowser": True,
                "renew_on_blocked": True,
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
        assert_matches_type(ExtractAsyncResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_async(self, client: Nimble) -> None:
        response = client.extract.with_raw_response.async_(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractAsyncResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_async(self, client: Nimble) -> None:
        with client.extract.with_streaming_response.async_(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractAsyncResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch(self, client: Nimble) -> None:
        extract = client.extract.batch(
            inputs=[{}],
        )
        assert_matches_type(ExtractBatchResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch_with_all_params(self, client: Nimble) -> None:
        extract = client.extract.batch(
            inputs=[
                {
                    "auto_driver_configuration": {
                        "vx10": 2,
                        "vx10-pro": 0,
                        "vx6-fast": 1,
                        "vx6-stealth": 1,
                        "vx8": 5,
                        "vx8-pro": 5,
                    },
                    "body": {"key": "value"},
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
                    "realtime_total_timeout": 15000,
                    "referrer_type": "random",
                    "render": False,
                    "request_timeout": 30000,
                    "session": {
                        "id": "id",
                        "prefetch_userbrowser": True,
                        "renew_on_blocked": True,
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
                "auto_driver_configuration": {
                    "vx10": 2,
                    "vx10-pro": 0,
                    "vx6-fast": 1,
                    "vx6-stealth": 1,
                    "vx8": 5,
                    "vx8-pro": 5,
                },
                "body": {"key": "value"},
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
                "realtime_total_timeout": 15000,
                "referrer_type": "random",
                "render": False,
                "request_timeout": 30000,
                "session": {
                    "id": "id",
                    "prefetch_userbrowser": True,
                    "renew_on_blocked": True,
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
        assert_matches_type(ExtractBatchResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_batch(self, client: Nimble) -> None:
        response = client.extract.with_raw_response.batch(
            inputs=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractBatchResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_batch(self, client: Nimble) -> None:
        with client.extract.with_streaming_response.batch(
            inputs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractBatchResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run(self, client: Nimble) -> None:
        extract = client.extract.run(
            url="url",
        )
        assert_matches_type(ExtractRunResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: Nimble) -> None:
        extract = client.extract.run(
            url="url",
            auto_driver_configuration={
                "vx10": 2,
                "vx10-pro": 0,
                "vx6-fast": 1,
                "vx6-stealth": 1,
                "vx8": 5,
                "vx8-pro": 5,
            },
            body={"key": "value"},
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
            realtime_total_timeout=15000,
            referrer_type="random",
            render=True,
            request_timeout=30000,
            session={
                "id": "id",
                "prefetch_userbrowser": True,
                "renew_on_blocked": True,
                "retry": True,
                "timeout": 1,
            },
            skill="dynamic-content",
            state="CA",
            tag="campaign-2024-q1",
        )
        assert_matches_type(ExtractRunResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: Nimble) -> None:
        response = client.extract.with_raw_response.run(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractRunResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: Nimble) -> None:
        with client.extract.with_streaming_response.run(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractRunResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExtract:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_async(self, async_client: AsyncNimble) -> None:
        extract = await async_client.extract.async_(
            url="url",
        )
        assert_matches_type(ExtractAsyncResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_async_with_all_params(self, async_client: AsyncNimble) -> None:
        extract = await async_client.extract.async_(
            url="url",
            auto_driver_configuration={
                "vx10": 2,
                "vx10-pro": 0,
                "vx6-fast": 1,
                "vx6-stealth": 1,
                "vx8": 5,
                "vx8-pro": 5,
            },
            body={"key": "value"},
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
            realtime_total_timeout=15000,
            referrer_type="random",
            render=True,
            request_timeout=30000,
            session={
                "id": "id",
                "prefetch_userbrowser": True,
                "renew_on_blocked": True,
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
        assert_matches_type(ExtractAsyncResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_async(self, async_client: AsyncNimble) -> None:
        response = await async_client.extract.with_raw_response.async_(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractAsyncResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_async(self, async_client: AsyncNimble) -> None:
        async with async_client.extract.with_streaming_response.async_(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractAsyncResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch(self, async_client: AsyncNimble) -> None:
        extract = await async_client.extract.batch(
            inputs=[{}],
        )
        assert_matches_type(ExtractBatchResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch_with_all_params(self, async_client: AsyncNimble) -> None:
        extract = await async_client.extract.batch(
            inputs=[
                {
                    "auto_driver_configuration": {
                        "vx10": 2,
                        "vx10-pro": 0,
                        "vx6-fast": 1,
                        "vx6-stealth": 1,
                        "vx8": 5,
                        "vx8-pro": 5,
                    },
                    "body": {"key": "value"},
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
                    "realtime_total_timeout": 15000,
                    "referrer_type": "random",
                    "render": False,
                    "request_timeout": 30000,
                    "session": {
                        "id": "id",
                        "prefetch_userbrowser": True,
                        "renew_on_blocked": True,
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
                "auto_driver_configuration": {
                    "vx10": 2,
                    "vx10-pro": 0,
                    "vx6-fast": 1,
                    "vx6-stealth": 1,
                    "vx8": 5,
                    "vx8-pro": 5,
                },
                "body": {"key": "value"},
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
                "realtime_total_timeout": 15000,
                "referrer_type": "random",
                "render": False,
                "request_timeout": 30000,
                "session": {
                    "id": "id",
                    "prefetch_userbrowser": True,
                    "renew_on_blocked": True,
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
        assert_matches_type(ExtractBatchResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_batch(self, async_client: AsyncNimble) -> None:
        response = await async_client.extract.with_raw_response.batch(
            inputs=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractBatchResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_batch(self, async_client: AsyncNimble) -> None:
        async with async_client.extract.with_streaming_response.batch(
            inputs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractBatchResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncNimble) -> None:
        extract = await async_client.extract.run(
            url="url",
        )
        assert_matches_type(ExtractRunResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncNimble) -> None:
        extract = await async_client.extract.run(
            url="url",
            auto_driver_configuration={
                "vx10": 2,
                "vx10-pro": 0,
                "vx6-fast": 1,
                "vx6-stealth": 1,
                "vx8": 5,
                "vx8-pro": 5,
            },
            body={"key": "value"},
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
            realtime_total_timeout=15000,
            referrer_type="random",
            render=True,
            request_timeout=30000,
            session={
                "id": "id",
                "prefetch_userbrowser": True,
                "renew_on_blocked": True,
                "retry": True,
                "timeout": 1,
            },
            skill="dynamic-content",
            state="CA",
            tag="campaign-2024-q1",
        )
        assert_matches_type(ExtractRunResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncNimble) -> None:
        response = await async_client.extract.with_raw_response.run(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractRunResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncNimble) -> None:
        async with async_client.extract.with_streaming_response.run(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractRunResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True
