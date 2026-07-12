# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from nimble_python import Nimble, AsyncNimble
from nimble_python.types import (
    TaskAgentGetResponse,
    TaskAgentRunResponse,
    TaskAgentListResponse,
    TaskAgentCreateResponse,
    TaskAgentUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTaskAgent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Nimble) -> None:
        task_agent = client.task_agent.create()
        assert_matches_type(TaskAgentCreateResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Nimble) -> None:
        task_agent = client.task_agent.create(
            agent_name="agent_name",
            description="description",
            display_name="display_name",
            domain_expertise="domain_expertise",
            effort="low",
            goals=["string"],
            icon="icon",
            is_active=True,
            output_schema={"foo": "bar"},
            sources={
                "allow": [
                    {
                        "domains": ["string"],
                        "title": "title",
                        "order": 0,
                    }
                ],
                "avoid": "avoid",
                "block": [
                    {
                        "domains": ["string"],
                        "title": "title",
                        "order": 0,
                    }
                ],
                "prioritize": "prioritize",
            },
            suggested_questions=["string"],
            template="template",
            use_case="research",
            workspace_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TaskAgentCreateResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Nimble) -> None:
        response = client.task_agent.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_agent = response.parse()
        assert_matches_type(TaskAgentCreateResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Nimble) -> None:
        with client.task_agent.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_agent = response.parse()
            assert_matches_type(TaskAgentCreateResponse, task_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Nimble) -> None:
        task_agent = client.task_agent.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[
                {
                    "op": "add",
                    "path": "path",
                }
            ],
        )
        assert_matches_type(TaskAgentUpdateResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Nimble) -> None:
        response = client.task_agent.with_raw_response.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[
                {
                    "op": "add",
                    "path": "path",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_agent = response.parse()
        assert_matches_type(TaskAgentUpdateResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Nimble) -> None:
        with client.task_agent.with_streaming_response.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[
                {
                    "op": "add",
                    "path": "path",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_agent = response.parse()
            assert_matches_type(TaskAgentUpdateResponse, task_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Nimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.task_agent.with_raw_response.update(
                agent_id="",
                body=[
                    {
                        "op": "add",
                        "path": "path",
                    }
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Nimble) -> None:
        task_agent = client.task_agent.list()
        assert_matches_type(TaskAgentListResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Nimble) -> None:
        task_agent = client.task_agent.list(
            filter_effort="low",
            filter_use_case="research",
            limit=0,
            offset=0,
            workspace_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TaskAgentListResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Nimble) -> None:
        response = client.task_agent.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_agent = response.parse()
        assert_matches_type(TaskAgentListResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Nimble) -> None:
        with client.task_agent.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_agent = response.parse()
            assert_matches_type(TaskAgentListResponse, task_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deactivate(self, client: Nimble) -> None:
        task_agent = client.task_agent.deactivate(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert task_agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_deactivate(self, client: Nimble) -> None:
        response = client.task_agent.with_raw_response.deactivate(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_agent = response.parse()
        assert task_agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_deactivate(self, client: Nimble) -> None:
        with client.task_agent.with_streaming_response.deactivate(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_agent = response.parse()
            assert task_agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_deactivate(self, client: Nimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.task_agent.with_raw_response.deactivate(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Nimble) -> None:
        task_agent = client.task_agent.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TaskAgentGetResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Nimble) -> None:
        response = client.task_agent.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_agent = response.parse()
        assert_matches_type(TaskAgentGetResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Nimble) -> None:
        with client.task_agent.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_agent = response.parse()
            assert_matches_type(TaskAgentGetResponse, task_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Nimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.task_agent.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run(self, client: Nimble) -> None:
        task_agent = client.task_agent.run(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            input="input",
        )
        assert_matches_type(TaskAgentRunResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: Nimble) -> None:
        task_agent = client.task_agent.run(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            input="input",
            effort="low",
            enable_events=True,
            output_schema={"foo": "bar"},
            previous_interaction_id="previous_interaction_id",
            sources={
                "allow": [
                    {
                        "domains": ["string"],
                        "title": "title",
                        "order": 0,
                    }
                ],
                "avoid": "avoid",
                "block": [
                    {
                        "domains": ["string"],
                        "title": "title",
                        "order": 0,
                    }
                ],
                "prioritize": "prioritize",
            },
        )
        assert_matches_type(TaskAgentRunResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: Nimble) -> None:
        response = client.task_agent.with_raw_response.run(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            input="input",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_agent = response.parse()
        assert_matches_type(TaskAgentRunResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: Nimble) -> None:
        with client.task_agent.with_streaming_response.run(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            input="input",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_agent = response.parse()
            assert_matches_type(TaskAgentRunResponse, task_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_run(self, client: Nimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.task_agent.with_raw_response.run(
                agent_id="",
                input="input",
            )


class TestAsyncTaskAgent:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncNimble) -> None:
        task_agent = await async_client.task_agent.create()
        assert_matches_type(TaskAgentCreateResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncNimble) -> None:
        task_agent = await async_client.task_agent.create(
            agent_name="agent_name",
            description="description",
            display_name="display_name",
            domain_expertise="domain_expertise",
            effort="low",
            goals=["string"],
            icon="icon",
            is_active=True,
            output_schema={"foo": "bar"},
            sources={
                "allow": [
                    {
                        "domains": ["string"],
                        "title": "title",
                        "order": 0,
                    }
                ],
                "avoid": "avoid",
                "block": [
                    {
                        "domains": ["string"],
                        "title": "title",
                        "order": 0,
                    }
                ],
                "prioritize": "prioritize",
            },
            suggested_questions=["string"],
            template="template",
            use_case="research",
            workspace_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TaskAgentCreateResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncNimble) -> None:
        response = await async_client.task_agent.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_agent = await response.parse()
        assert_matches_type(TaskAgentCreateResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncNimble) -> None:
        async with async_client.task_agent.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_agent = await response.parse()
            assert_matches_type(TaskAgentCreateResponse, task_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncNimble) -> None:
        task_agent = await async_client.task_agent.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[
                {
                    "op": "add",
                    "path": "path",
                }
            ],
        )
        assert_matches_type(TaskAgentUpdateResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncNimble) -> None:
        response = await async_client.task_agent.with_raw_response.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[
                {
                    "op": "add",
                    "path": "path",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_agent = await response.parse()
        assert_matches_type(TaskAgentUpdateResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncNimble) -> None:
        async with async_client.task_agent.with_streaming_response.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[
                {
                    "op": "add",
                    "path": "path",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_agent = await response.parse()
            assert_matches_type(TaskAgentUpdateResponse, task_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncNimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.task_agent.with_raw_response.update(
                agent_id="",
                body=[
                    {
                        "op": "add",
                        "path": "path",
                    }
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncNimble) -> None:
        task_agent = await async_client.task_agent.list()
        assert_matches_type(TaskAgentListResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncNimble) -> None:
        task_agent = await async_client.task_agent.list(
            filter_effort="low",
            filter_use_case="research",
            limit=0,
            offset=0,
            workspace_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TaskAgentListResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNimble) -> None:
        response = await async_client.task_agent.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_agent = await response.parse()
        assert_matches_type(TaskAgentListResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNimble) -> None:
        async with async_client.task_agent.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_agent = await response.parse()
            assert_matches_type(TaskAgentListResponse, task_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deactivate(self, async_client: AsyncNimble) -> None:
        task_agent = await async_client.task_agent.deactivate(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert task_agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_deactivate(self, async_client: AsyncNimble) -> None:
        response = await async_client.task_agent.with_raw_response.deactivate(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_agent = await response.parse()
        assert task_agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_deactivate(self, async_client: AsyncNimble) -> None:
        async with async_client.task_agent.with_streaming_response.deactivate(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_agent = await response.parse()
            assert task_agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_deactivate(self, async_client: AsyncNimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.task_agent.with_raw_response.deactivate(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncNimble) -> None:
        task_agent = await async_client.task_agent.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TaskAgentGetResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncNimble) -> None:
        response = await async_client.task_agent.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_agent = await response.parse()
        assert_matches_type(TaskAgentGetResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncNimble) -> None:
        async with async_client.task_agent.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_agent = await response.parse()
            assert_matches_type(TaskAgentGetResponse, task_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncNimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.task_agent.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncNimble) -> None:
        task_agent = await async_client.task_agent.run(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            input="input",
        )
        assert_matches_type(TaskAgentRunResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncNimble) -> None:
        task_agent = await async_client.task_agent.run(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            input="input",
            effort="low",
            enable_events=True,
            output_schema={"foo": "bar"},
            previous_interaction_id="previous_interaction_id",
            sources={
                "allow": [
                    {
                        "domains": ["string"],
                        "title": "title",
                        "order": 0,
                    }
                ],
                "avoid": "avoid",
                "block": [
                    {
                        "domains": ["string"],
                        "title": "title",
                        "order": 0,
                    }
                ],
                "prioritize": "prioritize",
            },
        )
        assert_matches_type(TaskAgentRunResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncNimble) -> None:
        response = await async_client.task_agent.with_raw_response.run(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            input="input",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_agent = await response.parse()
        assert_matches_type(TaskAgentRunResponse, task_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncNimble) -> None:
        async with async_client.task_agent.with_streaming_response.run(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            input="input",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_agent = await response.parse()
            assert_matches_type(TaskAgentRunResponse, task_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_run(self, async_client: AsyncNimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.task_agent.with_raw_response.run(
                agent_id="",
                input="input",
            )
