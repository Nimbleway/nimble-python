# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from nimble_python import Nimble, AsyncNimble
from nimble_python.types import (
    CrawlRunResponse,
    CrawlListResponse,
    CrawlStatusResponse,
    CrawlTerminateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCrawl:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Nimble) -> None:
        crawl = client.crawl.list()
        assert_matches_type(CrawlListResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Nimble) -> None:
        crawl = client.crawl.list(
            cursor="cursor",
            limit=10,
            status="queued",
        )
        assert_matches_type(CrawlListResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Nimble) -> None:
        response = client.crawl.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = response.parse()
        assert_matches_type(CrawlListResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Nimble) -> None:
        with client.crawl.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = response.parse()
            assert_matches_type(CrawlListResponse, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run(self, client: Nimble) -> None:
        crawl = client.crawl.run(
            url="url",
        )
        assert_matches_type(CrawlRunResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: Nimble) -> None:
        crawl = client.crawl.run(
            url="url",
            allow_external_links=False,
            allow_subdomains=False,
            callback={
                "url": "https://example.com",
                "events": ["started"],
                "headers": {"foo": "string"},
                "metadata": {"foo": "bar"},
            },
            crawl_entire_domain=False,
            exclude_paths=["/exclude-this-path", "/and-this-path"],
            extract_options={
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
                "render": True,
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
                "tag": "campaign-2024-q1",
                "url": "url",
            },
            ignore_query_parameters=False,
            include_paths=["/include-this-path", "/and-this-path"],
            limit=100,
            max_discovery_depth=3,
            name="The best crawl ever",
            sitemap="include",
        )
        assert_matches_type(CrawlRunResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: Nimble) -> None:
        response = client.crawl.with_raw_response.run(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = response.parse()
        assert_matches_type(CrawlRunResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: Nimble) -> None:
        with client.crawl.with_streaming_response.run(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = response.parse()
            assert_matches_type(CrawlRunResponse, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_status(self, client: Nimble) -> None:
        crawl = client.crawl.status(
            "123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(CrawlStatusResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_status(self, client: Nimble) -> None:
        response = client.crawl.with_raw_response.status(
            "123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = response.parse()
        assert_matches_type(CrawlStatusResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_status(self, client: Nimble) -> None:
        with client.crawl.with_streaming_response.status(
            "123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = response.parse()
            assert_matches_type(CrawlStatusResponse, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_status(self, client: Nimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.crawl.with_raw_response.status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_terminate(self, client: Nimble) -> None:
        crawl = client.crawl.terminate(
            "123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(CrawlTerminateResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_terminate(self, client: Nimble) -> None:
        response = client.crawl.with_raw_response.terminate(
            "123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = response.parse()
        assert_matches_type(CrawlTerminateResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_terminate(self, client: Nimble) -> None:
        with client.crawl.with_streaming_response.terminate(
            "123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = response.parse()
            assert_matches_type(CrawlTerminateResponse, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_terminate(self, client: Nimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.crawl.with_raw_response.terminate(
                "",
            )


class TestAsyncCrawl:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncNimble) -> None:
        crawl = await async_client.crawl.list()
        assert_matches_type(CrawlListResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncNimble) -> None:
        crawl = await async_client.crawl.list(
            cursor="cursor",
            limit=10,
            status="queued",
        )
        assert_matches_type(CrawlListResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNimble) -> None:
        response = await async_client.crawl.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = await response.parse()
        assert_matches_type(CrawlListResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNimble) -> None:
        async with async_client.crawl.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = await response.parse()
            assert_matches_type(CrawlListResponse, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncNimble) -> None:
        crawl = await async_client.crawl.run(
            url="url",
        )
        assert_matches_type(CrawlRunResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncNimble) -> None:
        crawl = await async_client.crawl.run(
            url="url",
            allow_external_links=False,
            allow_subdomains=False,
            callback={
                "url": "https://example.com",
                "events": ["started"],
                "headers": {"foo": "string"},
                "metadata": {"foo": "bar"},
            },
            crawl_entire_domain=False,
            exclude_paths=["/exclude-this-path", "/and-this-path"],
            extract_options={
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
                "render": True,
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
                "tag": "campaign-2024-q1",
                "url": "url",
            },
            ignore_query_parameters=False,
            include_paths=["/include-this-path", "/and-this-path"],
            limit=100,
            max_discovery_depth=3,
            name="The best crawl ever",
            sitemap="include",
        )
        assert_matches_type(CrawlRunResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncNimble) -> None:
        response = await async_client.crawl.with_raw_response.run(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = await response.parse()
        assert_matches_type(CrawlRunResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncNimble) -> None:
        async with async_client.crawl.with_streaming_response.run(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = await response.parse()
            assert_matches_type(CrawlRunResponse, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_status(self, async_client: AsyncNimble) -> None:
        crawl = await async_client.crawl.status(
            "123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(CrawlStatusResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_status(self, async_client: AsyncNimble) -> None:
        response = await async_client.crawl.with_raw_response.status(
            "123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = await response.parse()
        assert_matches_type(CrawlStatusResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncNimble) -> None:
        async with async_client.crawl.with_streaming_response.status(
            "123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = await response.parse()
            assert_matches_type(CrawlStatusResponse, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_status(self, async_client: AsyncNimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.crawl.with_raw_response.status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_terminate(self, async_client: AsyncNimble) -> None:
        crawl = await async_client.crawl.terminate(
            "123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(CrawlTerminateResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_terminate(self, async_client: AsyncNimble) -> None:
        response = await async_client.crawl.with_raw_response.terminate(
            "123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = await response.parse()
        assert_matches_type(CrawlTerminateResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_terminate(self, async_client: AsyncNimble) -> None:
        async with async_client.crawl.with_streaming_response.terminate(
            "123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = await response.parse()
            assert_matches_type(CrawlTerminateResponse, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_terminate(self, async_client: AsyncNimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.crawl.with_raw_response.terminate(
                "",
            )
