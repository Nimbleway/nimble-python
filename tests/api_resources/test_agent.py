# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from nimble_python import Nimble, AsyncNimble
from nimble_python.types import (
    AgentGetResponse,
    AgentRunResponse,
    AgentListResponse,
    AgentRunAsyncResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Nimble) -> None:
        agent = client.agent.list()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Nimble) -> None:
        agent = client.agent.list(
            limit=1,
            managed_by="nimble",
            offset=0,
            privacy="public",
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Nimble) -> None:
        response = client.agent.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Nimble) -> None:
        with client.agent.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Nimble) -> None:
        agent = client.agent.get(
            "template_name",
        )
        assert_matches_type(AgentGetResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Nimble) -> None:
        response = client.agent.with_raw_response.get(
            "template_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentGetResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Nimble) -> None:
        with client.agent.with_streaming_response.get(
            "template_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentGetResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Nimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_name` but received ''"):
            client.agent.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run(self, client: Nimble) -> None:
        agent = client.agent.run(
            agent="agent",
            params={"foo": "bar"},
        )
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: Nimble) -> None:
        agent = client.agent.run(
            agent="agent",
            params={"foo": "bar"},
            localization=True,
        )
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: Nimble) -> None:
        response = client.agent.with_raw_response.run(
            agent="agent",
            params={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: Nimble) -> None:
        with client.agent.with_streaming_response.run(
            agent="agent",
            params={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentRunResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_async(self, client: Nimble) -> None:
        agent = client.agent.run_async(
            agent="agent",
            params={"foo": "bar"},
        )
        assert_matches_type(AgentRunAsyncResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_async_with_all_params(self, client: Nimble) -> None:
        agent = client.agent.run_async(
            agent="agent",
            params={"foo": "bar"},
            callback_url="https://example.com/webhook/callback",
            localization=True,
            storage_compress=True,
            storage_object_name="result-2024-01-15.json",
            storage_type="s3",
            storage_url="s3://bucket-name/path/to/object",
        )
        assert_matches_type(AgentRunAsyncResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run_async(self, client: Nimble) -> None:
        response = client.agent.with_raw_response.run_async(
            agent="agent",
            params={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRunAsyncResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run_async(self, client: Nimble) -> None:
        with client.agent.with_streaming_response.run_async(
            agent="agent",
            params={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentRunAsyncResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAgent:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncNimble) -> None:
        agent = await async_client.agent.list()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncNimble) -> None:
        agent = await async_client.agent.list(
            limit=1,
            managed_by="nimble",
            offset=0,
            privacy="public",
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNimble) -> None:
        response = await async_client.agent.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNimble) -> None:
        async with async_client.agent.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncNimble) -> None:
        agent = await async_client.agent.get(
            "template_name",
        )
        assert_matches_type(AgentGetResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncNimble) -> None:
        response = await async_client.agent.with_raw_response.get(
            "template_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentGetResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncNimble) -> None:
        async with async_client.agent.with_streaming_response.get(
            "template_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentGetResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncNimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_name` but received ''"):
            await async_client.agent.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncNimble) -> None:
        agent = await async_client.agent.run(
            agent="agent",
            params={"foo": "bar"},
        )
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncNimble) -> None:
        agent = await async_client.agent.run(
            agent="agent",
            params={"foo": "bar"},
            localization=True,
        )
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncNimble) -> None:
        response = await async_client.agent.with_raw_response.run(
            agent="agent",
            params={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncNimble) -> None:
        async with async_client.agent.with_streaming_response.run(
            agent="agent",
            params={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentRunResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_async(self, async_client: AsyncNimble) -> None:
        agent = await async_client.agent.run_async(
            agent="agent",
            params={"foo": "bar"},
        )
        assert_matches_type(AgentRunAsyncResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_async_with_all_params(self, async_client: AsyncNimble) -> None:
        agent = await async_client.agent.run_async(
            agent="agent",
            params={"foo": "bar"},
            callback_url="https://example.com/webhook/callback",
            localization=True,
            storage_compress=True,
            storage_object_name="result-2024-01-15.json",
            storage_type="s3",
            storage_url="s3://bucket-name/path/to/object",
        )
        assert_matches_type(AgentRunAsyncResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run_async(self, async_client: AsyncNimble) -> None:
        response = await async_client.agent.with_raw_response.run_async(
            agent="agent",
            params={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRunAsyncResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run_async(self, async_client: AsyncNimble) -> None:
        async with async_client.agent.with_streaming_response.run_async(
            agent="agent",
            params={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentRunAsyncResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True
