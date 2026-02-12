# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from nimble_python import Nimble, AsyncNimble
from nimble_python.types import (
    MapResponse,
    AgentResponse,
    CrawlResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClient:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_agent_overload_1(self, client: Nimble) -> None:
        client_ = client.agent(
            params={"foo": "bar"},
            template="template",
        )
        assert_matches_type(AgentResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_agent_with_all_params_overload_1(self, client: Nimble) -> None:
        client_ = client.agent(
            params={"foo": "bar"},
            template="template",
            localization=True,
        )
        assert_matches_type(AgentResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_agent_overload_1(self, client: Nimble) -> None:
        response = client.with_raw_response.agent(
            params={"foo": "bar"},
            template="template",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(AgentResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_agent_overload_1(self, client: Nimble) -> None:
        with client.with_streaming_response.agent(
            params={"foo": "bar"},
            template="template",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(AgentResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_agent_overload_2(self, client: Nimble) -> None:
        client_ = client.agent(
            agent="agent",
            params={"foo": "bar"},
        )
        assert_matches_type(AgentResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_agent_with_all_params_overload_2(self, client: Nimble) -> None:
        client_ = client.agent(
            agent="agent",
            params={"foo": "bar"},
            localization=True,
        )
        assert_matches_type(AgentResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_agent_overload_2(self, client: Nimble) -> None:
        response = client.with_raw_response.agent(
            agent="agent",
            params={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(AgentResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_agent_overload_2(self, client: Nimble) -> None:
        with client.with_streaming_response.agent(
            agent="agent",
            params={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(AgentResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_crawl(self, client: Nimble) -> None:
        client_ = client.crawl(
            url="url",
        )
        assert_matches_type(CrawlResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_crawl_with_all_params(self, client: Nimble) -> None:
        client_ = client.crawl(
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
                "expected_status_codes": [200, 201],
                "formats": ["html"],
                "headers": {
                    "User-Agent": "CustomBot/1.0",
                    "Accept-Language": "en-US",
                },
                "http2": True,
                "ip6": False,
                "is_xhr": True,
                "locale": "en-US",
                "metadata": {
                    "account_name": "account_name",
                    "api_type": "api_type",
                    "crawl_depth": -9007199254740991,
                    "crawl_id": "crawl_id",
                    "definition_id": -9007199254740991,
                    "definition_name": "definition_name",
                    "endpoint": "endpoint",
                    "execution_id": "execution_id",
                    "flowit_task_id": "flowit_task_id",
                    "input_id": "input_id",
                    "is_public_wsa": True,
                    "is_sitemap": True,
                    "is_wsa": True,
                    "parser_id": "parser_id",
                    "pipeline_execution_id": -9007199254740991,
                    "query_template_id": "query_template_id",
                    "source": "source",
                    "template_id": -9007199254740991,
                    "template_name": "template_name",
                    "wsa_id": "wsa_id",
                    "wsa_name": "wsa_name",
                    "wsa_version": 0,
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
                "no_userbrowser": False,
                "os": "windows",
                "parse": True,
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
                    "connector_type": "puppeteer",
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
                    "render_type": "domcontentloaded",
                    "store_local_storage": True,
                    "timeout": 30000,
                    "typing_interval": 100,
                    "typing_strategy": "simple",
                    "userbrowser": True,
                    "wait_until": "networkidle2",
                    "with_performance_metrics": True,
                },
                "request_timeout": 30000,
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
                "url": "url",
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
        assert_matches_type(CrawlResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_crawl(self, client: Nimble) -> None:
        response = client.with_raw_response.crawl(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(CrawlResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_crawl(self, client: Nimble) -> None:
        with client.with_streaming_response.crawl(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(CrawlResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

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
    async def test_method_agent_overload_1(self, async_client: AsyncNimble) -> None:
        client = await async_client.agent(
            params={"foo": "bar"},
            template="template",
        )
        assert_matches_type(AgentResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_agent_with_all_params_overload_1(self, async_client: AsyncNimble) -> None:
        client = await async_client.agent(
            params={"foo": "bar"},
            template="template",
            localization=True,
        )
        assert_matches_type(AgentResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_agent_overload_1(self, async_client: AsyncNimble) -> None:
        response = await async_client.with_raw_response.agent(
            params={"foo": "bar"},
            template="template",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(AgentResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_agent_overload_1(self, async_client: AsyncNimble) -> None:
        async with async_client.with_streaming_response.agent(
            params={"foo": "bar"},
            template="template",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(AgentResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_agent_overload_2(self, async_client: AsyncNimble) -> None:
        client = await async_client.agent(
            agent="agent",
            params={"foo": "bar"},
        )
        assert_matches_type(AgentResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_agent_with_all_params_overload_2(self, async_client: AsyncNimble) -> None:
        client = await async_client.agent(
            agent="agent",
            params={"foo": "bar"},
            localization=True,
        )
        assert_matches_type(AgentResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_agent_overload_2(self, async_client: AsyncNimble) -> None:
        response = await async_client.with_raw_response.agent(
            agent="agent",
            params={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(AgentResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_agent_overload_2(self, async_client: AsyncNimble) -> None:
        async with async_client.with_streaming_response.agent(
            agent="agent",
            params={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(AgentResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_crawl(self, async_client: AsyncNimble) -> None:
        client = await async_client.crawl(
            url="url",
        )
        assert_matches_type(CrawlResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_crawl_with_all_params(self, async_client: AsyncNimble) -> None:
        client = await async_client.crawl(
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
                "expected_status_codes": [200, 201],
                "formats": ["html"],
                "headers": {
                    "User-Agent": "CustomBot/1.0",
                    "Accept-Language": "en-US",
                },
                "http2": True,
                "ip6": False,
                "is_xhr": True,
                "locale": "en-US",
                "metadata": {
                    "account_name": "account_name",
                    "api_type": "api_type",
                    "crawl_depth": -9007199254740991,
                    "crawl_id": "crawl_id",
                    "definition_id": -9007199254740991,
                    "definition_name": "definition_name",
                    "endpoint": "endpoint",
                    "execution_id": "execution_id",
                    "flowit_task_id": "flowit_task_id",
                    "input_id": "input_id",
                    "is_public_wsa": True,
                    "is_sitemap": True,
                    "is_wsa": True,
                    "parser_id": "parser_id",
                    "pipeline_execution_id": -9007199254740991,
                    "query_template_id": "query_template_id",
                    "source": "source",
                    "template_id": -9007199254740991,
                    "template_name": "template_name",
                    "wsa_id": "wsa_id",
                    "wsa_name": "wsa_name",
                    "wsa_version": 0,
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
                "no_userbrowser": False,
                "os": "windows",
                "parse": True,
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
                    "connector_type": "puppeteer",
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
                    "render_type": "domcontentloaded",
                    "store_local_storage": True,
                    "timeout": 30000,
                    "typing_interval": 100,
                    "typing_strategy": "simple",
                    "userbrowser": True,
                    "wait_until": "networkidle2",
                    "with_performance_metrics": True,
                },
                "request_timeout": 30000,
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
                "url": "url",
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
        assert_matches_type(CrawlResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_crawl(self, async_client: AsyncNimble) -> None:
        response = await async_client.with_raw_response.crawl(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(CrawlResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_crawl(self, async_client: AsyncNimble) -> None:
        async with async_client.with_streaming_response.crawl(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(CrawlResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

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
