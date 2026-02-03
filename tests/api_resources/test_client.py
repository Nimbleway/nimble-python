# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nimbleway import Nimbleway, AsyncNimbleway
from tests.utils import assert_matches_type
from nimbleway.types import (
    MapResponse,
    SearchResponse,
    ExtractResponse,
    ExtractTemplateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClient:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_extract(self, client: Nimbleway) -> None:
        client_ = client.extract(
            debug_options={},
            url="https://example.com/page",
        )
        assert_matches_type(ExtractResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_extract_with_all_params(self, client: Nimbleway) -> None:
        client_ = client.extract(
            debug_options={
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
            url="https://example.com/page",
            browser="chrome",
            city="Los Angeles",
            client_timeout=25000,
            consent_header=True,
            cookies=[
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
            country="US",
            device="desktop",
            disable_ip_check=False,
            driver="vx8",
            dynamic_parser={"myParser": "bar"},
            expected_status_codes=[200, 201],
            export_userbrowser=False,
            format="json",
            headers={
                "User-Agent": "CustomBot/1.0",
                "Accept-Language": "en-US",
            },
            http2=True,
            ip6=False,
            is_xhr=True,
            locale="en-US",
            markdown=False,
            metadata={
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
            method="GET",
            native_mode="requester",
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
            no_html=False,
            no_userbrowser=False,
            os="windows",
            parse=True,
            parse_options={"merge_dynamic": True},
            parser={"myParser": "bar"},
            proxy_provider="brightdata",
            proxy_providers={
                "brightdata": 70,
                "oxylabs": 30,
            },
            query_template={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "api_type": "WEB",
                "pagination": {"next_page_params": {"foo": "bar"}},
                "params": {"foo": "bar"},
            },
            raw_headers=True,
            referrer_type="random",
            render=True,
            render_flow=[{"wait": "bar"}, {"click": "bar"}],
            render_options={
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
            request_timeout=30000,
            return_response_headers_as_header=True,
            save_userbrowser=False,
            session={
                "id": "id",
                "prefetch_userbrowser": True,
                "retry": True,
                "timeout": 1,
            },
            skill="dynamic-content",
            skip_ubct=False,
            state="CA",
            tag="campaign-2024-q1",
            template={
                "name": "x",
                "params": {"foo": "bar"},
            },
            type="generic",
            userbrowser_creation_template_rendered={
                "id": "id",
                "allowed_parameter_names": ["x"],
                "render_flow_rendered": [{"foo": "bar"}],
            },
        )
        assert_matches_type(ExtractResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_extract(self, client: Nimbleway) -> None:
        response = client.with_raw_response.extract(
            debug_options={},
            url="https://example.com/page",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(ExtractResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_extract(self, client: Nimbleway) -> None:
        with client.with_streaming_response.extract(
            debug_options={},
            url="https://example.com/page",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(ExtractResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_extract_template(self, client: Nimbleway) -> None:
        client_ = client.extract_template(
            params={"foo": "bar"},
            template="template",
        )
        assert_matches_type(ExtractTemplateResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_extract_template(self, client: Nimbleway) -> None:
        response = client.with_raw_response.extract_template(
            params={"foo": "bar"},
            template="template",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(ExtractTemplateResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_extract_template(self, client: Nimbleway) -> None:
        with client.with_streaming_response.extract_template(
            params={"foo": "bar"},
            template="template",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(ExtractTemplateResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_map(self, client: Nimbleway) -> None:
        client_ = client.map(
            url="https://example.com",
        )
        assert_matches_type(MapResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_map_with_all_params(self, client: Nimbleway) -> None:
        client_ = client.map(
            url="https://example.com",
            country="US",
            domain_filter="all",
            limit=1000,
            locale="en-US",
            sitemap="include",
        )
        assert_matches_type(MapResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_map(self, client: Nimbleway) -> None:
        response = client.with_raw_response.map(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(MapResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_map(self, client: Nimbleway) -> None:
        with client.with_streaming_response.map(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(MapResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: Nimbleway) -> None:
        client_ = client.search(
            query="x",
        )
        assert_matches_type(SearchResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Nimbleway) -> None:
        client_ = client.search(
            query="x",
            content_type=["string"],
            country="country",
            deep_search=True,
            end_date="end_date",
            exclude_domains=["string"],
            include_answer=True,
            include_domains=["string"],
            locale="locale",
            max_subagents=1,
            num_results=1,
            parsing_type="plain_text",
            search_engine="google_search",
            start_date="start_date",
            time_range="hour",
            topic="general",
        )
        assert_matches_type(SearchResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Nimbleway) -> None:
        response = client.with_raw_response.search(
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(SearchResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Nimbleway) -> None:
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_extract(self, async_client: AsyncNimbleway) -> None:
        client = await async_client.extract(
            debug_options={},
            url="https://example.com/page",
        )
        assert_matches_type(ExtractResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_extract_with_all_params(self, async_client: AsyncNimbleway) -> None:
        client = await async_client.extract(
            debug_options={
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
            url="https://example.com/page",
            browser="chrome",
            city="Los Angeles",
            client_timeout=25000,
            consent_header=True,
            cookies=[
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
            country="US",
            device="desktop",
            disable_ip_check=False,
            driver="vx8",
            dynamic_parser={"myParser": "bar"},
            expected_status_codes=[200, 201],
            export_userbrowser=False,
            format="json",
            headers={
                "User-Agent": "CustomBot/1.0",
                "Accept-Language": "en-US",
            },
            http2=True,
            ip6=False,
            is_xhr=True,
            locale="en-US",
            markdown=False,
            metadata={
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
            method="GET",
            native_mode="requester",
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
            no_html=False,
            no_userbrowser=False,
            os="windows",
            parse=True,
            parse_options={"merge_dynamic": True},
            parser={"myParser": "bar"},
            proxy_provider="brightdata",
            proxy_providers={
                "brightdata": 70,
                "oxylabs": 30,
            },
            query_template={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "api_type": "WEB",
                "pagination": {"next_page_params": {"foo": "bar"}},
                "params": {"foo": "bar"},
            },
            raw_headers=True,
            referrer_type="random",
            render=True,
            render_flow=[{"wait": "bar"}, {"click": "bar"}],
            render_options={
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
            request_timeout=30000,
            return_response_headers_as_header=True,
            save_userbrowser=False,
            session={
                "id": "id",
                "prefetch_userbrowser": True,
                "retry": True,
                "timeout": 1,
            },
            skill="dynamic-content",
            skip_ubct=False,
            state="CA",
            tag="campaign-2024-q1",
            template={
                "name": "x",
                "params": {"foo": "bar"},
            },
            type="generic",
            userbrowser_creation_template_rendered={
                "id": "id",
                "allowed_parameter_names": ["x"],
                "render_flow_rendered": [{"foo": "bar"}],
            },
        )
        assert_matches_type(ExtractResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_extract(self, async_client: AsyncNimbleway) -> None:
        response = await async_client.with_raw_response.extract(
            debug_options={},
            url="https://example.com/page",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(ExtractResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_extract(self, async_client: AsyncNimbleway) -> None:
        async with async_client.with_streaming_response.extract(
            debug_options={},
            url="https://example.com/page",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(ExtractResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_extract_template(self, async_client: AsyncNimbleway) -> None:
        client = await async_client.extract_template(
            params={"foo": "bar"},
            template="template",
        )
        assert_matches_type(ExtractTemplateResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_extract_template(self, async_client: AsyncNimbleway) -> None:
        response = await async_client.with_raw_response.extract_template(
            params={"foo": "bar"},
            template="template",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(ExtractTemplateResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_extract_template(self, async_client: AsyncNimbleway) -> None:
        async with async_client.with_streaming_response.extract_template(
            params={"foo": "bar"},
            template="template",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(ExtractTemplateResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_map(self, async_client: AsyncNimbleway) -> None:
        client = await async_client.map(
            url="https://example.com",
        )
        assert_matches_type(MapResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_map_with_all_params(self, async_client: AsyncNimbleway) -> None:
        client = await async_client.map(
            url="https://example.com",
            country="US",
            domain_filter="all",
            limit=1000,
            locale="en-US",
            sitemap="include",
        )
        assert_matches_type(MapResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_map(self, async_client: AsyncNimbleway) -> None:
        response = await async_client.with_raw_response.map(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(MapResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_map(self, async_client: AsyncNimbleway) -> None:
        async with async_client.with_streaming_response.map(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(MapResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncNimbleway) -> None:
        client = await async_client.search(
            query="x",
        )
        assert_matches_type(SearchResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncNimbleway) -> None:
        client = await async_client.search(
            query="x",
            content_type=["string"],
            country="country",
            deep_search=True,
            end_date="end_date",
            exclude_domains=["string"],
            include_answer=True,
            include_domains=["string"],
            locale="locale",
            max_subagents=1,
            num_results=1,
            parsing_type="plain_text",
            search_engine="google_search",
            start_date="start_date",
            time_range="hour",
            topic="general",
        )
        assert_matches_type(SearchResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncNimbleway) -> None:
        response = await async_client.with_raw_response.search(
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(SearchResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncNimbleway) -> None:
        async with async_client.with_streaming_response.search(
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(SearchResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True
