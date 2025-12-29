# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nimbleway import Nimbleway, AsyncNimbleway
from tests.utils import assert_matches_type
from nimbleway.types import ExtractCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExtract:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Nimbleway) -> None:
        extract = client.extract.create(
            url="https://example.com/page",
        )
        assert_matches_type(ExtractCreateResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Nimbleway) -> None:
        extract = client.extract.create(
            url="https://example.com/page",
            aggregate="json",
            async_timeout=60000,
            base_domain="example.com",
            batch_callback_url="https://example.com/webhook/batch-callback",
            browser="chrome",
            browser_version="120.0.0",
            callback_url="https://example.com/webhook/callback",
            city="Los Angeles",
            client_timeout=25000,
            consent_header="true",
            cookies=[
                {
                    "creation": "creation",
                    "domain": "domain",
                    "expires": "string",
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
            },
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
            headless=True,
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
                    "resource_type": "string",
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
                "_911proxy": 1,
                "always": 1,
                "brightdata": 70,
                "brightup": 1,
                "direct911proxy": 1,
                "froxy": 1,
                "ipfoxy": 1,
                "local": 1,
                "nimble_isp": 1,
                "nimble_isp_mobile": 1,
                "oculusproxies": 1,
                "oxylabs": 30,
                "packetstream": 1,
                "proxit": 1,
                "proxit_preprod": 1,
                "proxit_linux": 1,
                "proxit_macos": 1,
                "proxit_rental": 1,
                "proxit_windows": 1,
                "rayobyte": 1,
                "smartproxy": 1,
                "thesocialproxy": 1,
                "thesocialproxy2": 1,
            },
            query_template={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "api_type": "WEB",
                "pagination": {"next_page_params": {}},
                "params": {"foo": "bar"},
            },
            raw_headers=True,
            referrer_type="random",
            render=True,
            render_flow=[
                {"wait": {"delay": 2000}},
                {
                    "click": {
                        "selector": "#load-more",
                        "timeout": 5000,
                    }
                },
            ],
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
            requests=[{}],
            return_response_headers_as_header=True,
            save_userbrowser=False,
            session_id="session_id",
            session_prefetch_userbrowser=True,
            session_retry=True,
            session_timeout=1,
            skill="dynamic-content",
            skip_ubct=False,
            state="CA",
            storage_compress=True,
            storage_object_name="result-2024-01-15.json",
            storage_type="s3",
            storage_url="s3://bucket-name/path/to/object",
            tag="campaign-2024-q1",
            template={
                "name": "x",
                "params": {},
            },
            transform={},
            type="generic",
            user_context="order-id-12345",
            userbrowser_creation_template_rendered={
                "id": "id",
                "allowed_parameter_names": ["x"],
                "render_flow_rendered": [{"foo": {}}],
            },
            with_proxy_usage=True,
        )
        assert_matches_type(ExtractCreateResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Nimbleway) -> None:
        response = client.extract.with_raw_response.create(
            url="https://example.com/page",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractCreateResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Nimbleway) -> None:
        with client.extract.with_streaming_response.create(
            url="https://example.com/page",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractCreateResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExtract:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncNimbleway) -> None:
        extract = await async_client.extract.create(
            url="https://example.com/page",
        )
        assert_matches_type(ExtractCreateResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncNimbleway) -> None:
        extract = await async_client.extract.create(
            url="https://example.com/page",
            aggregate="json",
            async_timeout=60000,
            base_domain="example.com",
            batch_callback_url="https://example.com/webhook/batch-callback",
            browser="chrome",
            browser_version="120.0.0",
            callback_url="https://example.com/webhook/callback",
            city="Los Angeles",
            client_timeout=25000,
            consent_header="true",
            cookies=[
                {
                    "creation": "creation",
                    "domain": "domain",
                    "expires": "string",
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
            },
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
            headless=True,
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
                    "resource_type": "string",
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
                "_911proxy": 1,
                "always": 1,
                "brightdata": 70,
                "brightup": 1,
                "direct911proxy": 1,
                "froxy": 1,
                "ipfoxy": 1,
                "local": 1,
                "nimble_isp": 1,
                "nimble_isp_mobile": 1,
                "oculusproxies": 1,
                "oxylabs": 30,
                "packetstream": 1,
                "proxit": 1,
                "proxit_preprod": 1,
                "proxit_linux": 1,
                "proxit_macos": 1,
                "proxit_rental": 1,
                "proxit_windows": 1,
                "rayobyte": 1,
                "smartproxy": 1,
                "thesocialproxy": 1,
                "thesocialproxy2": 1,
            },
            query_template={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "api_type": "WEB",
                "pagination": {"next_page_params": {}},
                "params": {"foo": "bar"},
            },
            raw_headers=True,
            referrer_type="random",
            render=True,
            render_flow=[
                {"wait": {"delay": 2000}},
                {
                    "click": {
                        "selector": "#load-more",
                        "timeout": 5000,
                    }
                },
            ],
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
            requests=[{}],
            return_response_headers_as_header=True,
            save_userbrowser=False,
            session_id="session_id",
            session_prefetch_userbrowser=True,
            session_retry=True,
            session_timeout=1,
            skill="dynamic-content",
            skip_ubct=False,
            state="CA",
            storage_compress=True,
            storage_object_name="result-2024-01-15.json",
            storage_type="s3",
            storage_url="s3://bucket-name/path/to/object",
            tag="campaign-2024-q1",
            template={
                "name": "x",
                "params": {},
            },
            transform={},
            type="generic",
            user_context="order-id-12345",
            userbrowser_creation_template_rendered={
                "id": "id",
                "allowed_parameter_names": ["x"],
                "render_flow_rendered": [{"foo": {}}],
            },
            with_proxy_usage=True,
        )
        assert_matches_type(ExtractCreateResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncNimbleway) -> None:
        response = await async_client.extract.with_raw_response.create(
            url="https://example.com/page",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractCreateResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncNimbleway) -> None:
        async with async_client.extract.with_streaming_response.create(
            url="https://example.com/page",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractCreateResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True
