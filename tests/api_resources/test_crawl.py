# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nimbleway import Nimbleway, AsyncNimbleway
from tests.utils import assert_matches_type
from nimbleway.types import (
    CrawlListResponse,
    CrawlRootResponse,
    CrawlStatusResponse,
    CrawlTerminateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCrawl:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Nimbleway) -> None:
        crawl = client.crawl.list(
            status="pending",
        )
        assert_matches_type(CrawlListResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Nimbleway) -> None:
        crawl = client.crawl.list(
            status="pending",
            cursor="cursor",
            limit=10,
        )
        assert_matches_type(CrawlListResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Nimbleway) -> None:
        response = client.crawl.with_raw_response.list(
            status="pending",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = response.parse()
        assert_matches_type(CrawlListResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Nimbleway) -> None:
        with client.crawl.with_streaming_response.list(
            status="pending",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = response.parse()
            assert_matches_type(CrawlListResponse, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_root(self, client: Nimbleway) -> None:
        crawl = client.crawl.root(
            url="https://example.com",
        )
        assert_matches_type(CrawlRootResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_root_with_all_params(self, client: Nimbleway) -> None:
        crawl = client.crawl.root(
            url="https://example.com",
            allow_external_links=False,
            allow_subdomains=False,
            callback={
                "url": "https://example.com/webhook",
                "events": ["page"],
                "headers": {"X-Custom-Header": "bar"},
                "metadata": {"crawlId": "bar"},
            },
            crawl_entire_domain=False,
            exclude_paths=["/exclude-this-path", "/and-this-path"],
            extract_options={
                "debug_options": {
                    "collect_har": True,
                    "no_retry_mode": True,
                    "record_screen": True,
                    "redact": True,
                    "show_cursor": True,
                    "solve_captcha": True,
                    "trace": True,
                    "upload_engine_logs": True,
                    "verbose": True,
                    "with_proxy_usage": True,
                },
                "url": "https://example.com/page",
                "browser": "chrome",
                "city": "Los Angeles",
                "client_timeout": 25000,
                "consent_header": True,
                "cookies": [
                    {
                        "creation": "creation",
                        "domain": "domain",
                        "expires": "expires",
                        "extensions": ["string"],
                        "host_only": True,
                        "http_only": True,
                        "last_accessed": "lastAccessed",
                        "max_age": "Infinity",
                        "name": "name",
                        "path": "path",
                        "path_is_default": True,
                        "same_site": "strict",
                        "secure": True,
                        "value": "value",
                    }
                ],
                "country": "US",
                "device": "desktop",
                "disable_ip_check": False,
                "driver": "vx8",
                "dynamic_parser": {"myParser": "bar"},
                "expected_status_codes": [200, 201],
                "export_userbrowser": False,
                "format": "json",
                "headers": {
                    "User-Agent": "CustomBot/1.0",
                    "Accept-Language": "en-US",
                },
                "http2": True,
                "ip6": False,
                "is_xhr": True,
                "locale": "en-US",
                "markdown": False,
                "metadata": {
                    "account_name": "acme-corp",
                    "definition_id": 456,
                    "definition_name": "product-scraper",
                    "endpoint": "/api/v2/scrape",
                    "execution_id": "exec-abc123",
                    "flowit_task_id": "task-xyz789",
                    "input_id": "input-123",
                    "pipeline_execution_id": 12345,
                    "query_template_id": "template-qry-001",
                    "source": "web-app",
                    "template_id": 789,
                    "template_name": "e-commerce-template",
                },
                "method": "GET",
                "native_mode": "requester",
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
                "no_html": False,
                "no_userbrowser": False,
                "os": "windows",
                "parse": True,
                "parse_options": {"merge_dynamic": True},
                "parser": {"myParser": "bar"},
                "proxy_provider": "brightdata",
                "proxy_providers": {
                    "brightdata": 70,
                    "oxylabs": 30,
                },
                "query_template": {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "api_type": "WEB",
                    "pagination": {"next_page_params": {"foo": "bar"}},
                    "params": {"foo": "bar"},
                },
                "raw_headers": True,
                "referrer_type": "random",
                "render": True,
                "render_flow": [{"wait": "bar"}, {"click": "bar"}],
                "render_options": {
                    "adblock": True,
                    "blocked_domains": ["ads.example.com", "tracker.com"],
                    "browser_engine": "chrome",
                    "cache": False,
                    "connector_type": "webit-cdp",
                    "disabled_resources": ["image", "stylesheet"],
                    "enable_2captcha": True,
                    "extensions": ["extension-id-1", "extension-id-2"],
                    "fingerprint_id": "fp-abc123",
                    "hackium_configuration": {
                        "collect_logs": True,
                        "do_not_fix_math_salt": True,
                        "enable_document_element_spoof": True,
                        "enable_document_has_focus": True,
                        "enable_fake_navigation_history": True,
                        "enable_key_ordering": True,
                        "enable_sniffer": True,
                        "enable_verbose_logs": True,
                    },
                    "headless": True,
                    "include_iframes": True,
                    "load_local_storage": True,
                    "local_storage_keys_to_load": ["authToken", "userId"],
                    "mouse_strategy": "linear",
                    "no_accept_encoding": True,
                    "override_permissions": True,
                    "random_header_order": True,
                    "render_type": "load",
                    "store_local_storage": True,
                    "timeout": 30000,
                    "typing_interval": 100,
                    "typing_strategy": "simple",
                    "userbrowser": True,
                    "wait_until": "networkidle2",
                    "with_performance_metrics": True,
                },
                "request_timeout": 30000,
                "return_response_headers_as_header": True,
                "save_userbrowser": False,
                "session": {
                    "id": "id",
                    "prefetch_userbrowser": True,
                    "retry": True,
                    "timeout": 1,
                },
                "skill": "dynamic-content",
                "skip_ubct": False,
                "state": "CA",
                "tag": "campaign-2024-q1",
                "template": {
                    "name": "x",
                    "params": {"foo": "bar"},
                },
                "type": "generic",
                "userbrowser_creation_template_rendered": {
                    "id": "id",
                    "allowed_parameter_names": ["x"],
                    "render_flow_rendered": [{"foo": "bar"}],
                },
            },
            ignore_query_parameters=False,
            include_paths=["/include-this-path", "/and-this-path"],
            limit=100,
            max_discovery_depth=3,
            name="The best crawl ever",
            sitemap="include",
        )
        assert_matches_type(CrawlRootResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_root(self, client: Nimbleway) -> None:
        response = client.crawl.with_raw_response.root(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = response.parse()
        assert_matches_type(CrawlRootResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_root(self, client: Nimbleway) -> None:
        with client.crawl.with_streaming_response.root(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = response.parse()
            assert_matches_type(CrawlRootResponse, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_status(self, client: Nimbleway) -> None:
        crawl = client.crawl.status(
            "123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(CrawlStatusResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_status(self, client: Nimbleway) -> None:
        response = client.crawl.with_raw_response.status(
            "123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = response.parse()
        assert_matches_type(CrawlStatusResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_status(self, client: Nimbleway) -> None:
        with client.crawl.with_streaming_response.status(
            "123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = response.parse()
            assert_matches_type(CrawlStatusResponse, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_status(self, client: Nimbleway) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.crawl.with_raw_response.status(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_terminate(self, client: Nimbleway) -> None:
        crawl = client.crawl.terminate(
            "123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(CrawlTerminateResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_terminate(self, client: Nimbleway) -> None:
        response = client.crawl.with_raw_response.terminate(
            "123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = response.parse()
        assert_matches_type(CrawlTerminateResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_terminate(self, client: Nimbleway) -> None:
        with client.crawl.with_streaming_response.terminate(
            "123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = response.parse()
            assert_matches_type(CrawlTerminateResponse, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_terminate(self, client: Nimbleway) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.crawl.with_raw_response.terminate(
                "",
            )


class TestAsyncCrawl:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncNimbleway) -> None:
        crawl = await async_client.crawl.list(
            status="pending",
        )
        assert_matches_type(CrawlListResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncNimbleway) -> None:
        crawl = await async_client.crawl.list(
            status="pending",
            cursor="cursor",
            limit=10,
        )
        assert_matches_type(CrawlListResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNimbleway) -> None:
        response = await async_client.crawl.with_raw_response.list(
            status="pending",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = await response.parse()
        assert_matches_type(CrawlListResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNimbleway) -> None:
        async with async_client.crawl.with_streaming_response.list(
            status="pending",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = await response.parse()
            assert_matches_type(CrawlListResponse, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_root(self, async_client: AsyncNimbleway) -> None:
        crawl = await async_client.crawl.root(
            url="https://example.com",
        )
        assert_matches_type(CrawlRootResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_root_with_all_params(self, async_client: AsyncNimbleway) -> None:
        crawl = await async_client.crawl.root(
            url="https://example.com",
            allow_external_links=False,
            allow_subdomains=False,
            callback={
                "url": "https://example.com/webhook",
                "events": ["page"],
                "headers": {"X-Custom-Header": "bar"},
                "metadata": {"crawlId": "bar"},
            },
            crawl_entire_domain=False,
            exclude_paths=["/exclude-this-path", "/and-this-path"],
            extract_options={
                "debug_options": {
                    "collect_har": True,
                    "no_retry_mode": True,
                    "record_screen": True,
                    "redact": True,
                    "show_cursor": True,
                    "solve_captcha": True,
                    "trace": True,
                    "upload_engine_logs": True,
                    "verbose": True,
                    "with_proxy_usage": True,
                },
                "url": "https://example.com/page",
                "browser": "chrome",
                "city": "Los Angeles",
                "client_timeout": 25000,
                "consent_header": True,
                "cookies": [
                    {
                        "creation": "creation",
                        "domain": "domain",
                        "expires": "expires",
                        "extensions": ["string"],
                        "host_only": True,
                        "http_only": True,
                        "last_accessed": "lastAccessed",
                        "max_age": "Infinity",
                        "name": "name",
                        "path": "path",
                        "path_is_default": True,
                        "same_site": "strict",
                        "secure": True,
                        "value": "value",
                    }
                ],
                "country": "US",
                "device": "desktop",
                "disable_ip_check": False,
                "driver": "vx8",
                "dynamic_parser": {"myParser": "bar"},
                "expected_status_codes": [200, 201],
                "export_userbrowser": False,
                "format": "json",
                "headers": {
                    "User-Agent": "CustomBot/1.0",
                    "Accept-Language": "en-US",
                },
                "http2": True,
                "ip6": False,
                "is_xhr": True,
                "locale": "en-US",
                "markdown": False,
                "metadata": {
                    "account_name": "acme-corp",
                    "definition_id": 456,
                    "definition_name": "product-scraper",
                    "endpoint": "/api/v2/scrape",
                    "execution_id": "exec-abc123",
                    "flowit_task_id": "task-xyz789",
                    "input_id": "input-123",
                    "pipeline_execution_id": 12345,
                    "query_template_id": "template-qry-001",
                    "source": "web-app",
                    "template_id": 789,
                    "template_name": "e-commerce-template",
                },
                "method": "GET",
                "native_mode": "requester",
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
                "no_html": False,
                "no_userbrowser": False,
                "os": "windows",
                "parse": True,
                "parse_options": {"merge_dynamic": True},
                "parser": {"myParser": "bar"},
                "proxy_provider": "brightdata",
                "proxy_providers": {
                    "brightdata": 70,
                    "oxylabs": 30,
                },
                "query_template": {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "api_type": "WEB",
                    "pagination": {"next_page_params": {"foo": "bar"}},
                    "params": {"foo": "bar"},
                },
                "raw_headers": True,
                "referrer_type": "random",
                "render": True,
                "render_flow": [{"wait": "bar"}, {"click": "bar"}],
                "render_options": {
                    "adblock": True,
                    "blocked_domains": ["ads.example.com", "tracker.com"],
                    "browser_engine": "chrome",
                    "cache": False,
                    "connector_type": "webit-cdp",
                    "disabled_resources": ["image", "stylesheet"],
                    "enable_2captcha": True,
                    "extensions": ["extension-id-1", "extension-id-2"],
                    "fingerprint_id": "fp-abc123",
                    "hackium_configuration": {
                        "collect_logs": True,
                        "do_not_fix_math_salt": True,
                        "enable_document_element_spoof": True,
                        "enable_document_has_focus": True,
                        "enable_fake_navigation_history": True,
                        "enable_key_ordering": True,
                        "enable_sniffer": True,
                        "enable_verbose_logs": True,
                    },
                    "headless": True,
                    "include_iframes": True,
                    "load_local_storage": True,
                    "local_storage_keys_to_load": ["authToken", "userId"],
                    "mouse_strategy": "linear",
                    "no_accept_encoding": True,
                    "override_permissions": True,
                    "random_header_order": True,
                    "render_type": "load",
                    "store_local_storage": True,
                    "timeout": 30000,
                    "typing_interval": 100,
                    "typing_strategy": "simple",
                    "userbrowser": True,
                    "wait_until": "networkidle2",
                    "with_performance_metrics": True,
                },
                "request_timeout": 30000,
                "return_response_headers_as_header": True,
                "save_userbrowser": False,
                "session": {
                    "id": "id",
                    "prefetch_userbrowser": True,
                    "retry": True,
                    "timeout": 1,
                },
                "skill": "dynamic-content",
                "skip_ubct": False,
                "state": "CA",
                "tag": "campaign-2024-q1",
                "template": {
                    "name": "x",
                    "params": {"foo": "bar"},
                },
                "type": "generic",
                "userbrowser_creation_template_rendered": {
                    "id": "id",
                    "allowed_parameter_names": ["x"],
                    "render_flow_rendered": [{"foo": "bar"}],
                },
            },
            ignore_query_parameters=False,
            include_paths=["/include-this-path", "/and-this-path"],
            limit=100,
            max_discovery_depth=3,
            name="The best crawl ever",
            sitemap="include",
        )
        assert_matches_type(CrawlRootResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_root(self, async_client: AsyncNimbleway) -> None:
        response = await async_client.crawl.with_raw_response.root(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = await response.parse()
        assert_matches_type(CrawlRootResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_root(self, async_client: AsyncNimbleway) -> None:
        async with async_client.crawl.with_streaming_response.root(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = await response.parse()
            assert_matches_type(CrawlRootResponse, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_status(self, async_client: AsyncNimbleway) -> None:
        crawl = await async_client.crawl.status(
            "123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(CrawlStatusResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_status(self, async_client: AsyncNimbleway) -> None:
        response = await async_client.crawl.with_raw_response.status(
            "123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = await response.parse()
        assert_matches_type(CrawlStatusResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncNimbleway) -> None:
        async with async_client.crawl.with_streaming_response.status(
            "123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = await response.parse()
            assert_matches_type(CrawlStatusResponse, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_status(self, async_client: AsyncNimbleway) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.crawl.with_raw_response.status(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_terminate(self, async_client: AsyncNimbleway) -> None:
        crawl = await async_client.crawl.terminate(
            "123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(CrawlTerminateResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_terminate(self, async_client: AsyncNimbleway) -> None:
        response = await async_client.crawl.with_raw_response.terminate(
            "123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = await response.parse()
        assert_matches_type(CrawlTerminateResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_terminate(self, async_client: AsyncNimbleway) -> None:
        async with async_client.crawl.with_streaming_response.terminate(
            "123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = await response.parse()
            assert_matches_type(CrawlTerminateResponse, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_terminate(self, async_client: AsyncNimbleway) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.crawl.with_raw_response.terminate(
                "",
            )
