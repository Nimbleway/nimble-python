# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from nimble_python import Nimble, AsyncNimble
from nimble_python.types.task_agent import RunGetResponse, RunListResponse, RunGetResultResponse

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Nimble) -> None:
        with pytest.warns(DeprecationWarning):
            run = client.task_agent.runs.list(
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(RunListResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Nimble) -> None:
        with pytest.warns(DeprecationWarning):
            run = client.task_agent.runs.list(
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                limit=1,
                offset=0,
            )

        assert_matches_type(RunListResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Nimble) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.task_agent.runs.with_raw_response.list(
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunListResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Nimble) -> None:
        with pytest.warns(DeprecationWarning):
            with client.task_agent.runs.with_streaming_response.list(
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                run = response.parse()
                assert_matches_type(RunListResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Nimble) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
                client.task_agent.runs.with_raw_response.list(
                    agent_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Nimble) -> None:
        with pytest.warns(DeprecationWarning):
            run = client.task_agent.runs.cancel(
                run_id="run_id",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert run is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Nimble) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.task_agent.runs.with_raw_response.cancel(
                run_id="run_id",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert run is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Nimble) -> None:
        with pytest.warns(DeprecationWarning):
            with client.task_agent.runs.with_streaming_response.cancel(
                run_id="run_id",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                run = response.parse()
                assert run is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: Nimble) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
                client.task_agent.runs.with_raw_response.cancel(
                    run_id="run_id",
                    agent_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
                client.task_agent.runs.with_raw_response.cancel(
                    run_id="",
                    agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Nimble) -> None:
        with pytest.warns(DeprecationWarning):
            run = client.task_agent.runs.get(
                run_id="run_id",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(RunGetResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Nimble) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.task_agent.runs.with_raw_response.get(
                run_id="run_id",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunGetResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Nimble) -> None:
        with pytest.warns(DeprecationWarning):
            with client.task_agent.runs.with_streaming_response.get(
                run_id="run_id",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                run = response.parse()
                assert_matches_type(RunGetResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Nimble) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
                client.task_agent.runs.with_raw_response.get(
                    run_id="run_id",
                    agent_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
                client.task_agent.runs.with_raw_response.get(
                    run_id="",
                    agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_result(self, client: Nimble) -> None:
        with pytest.warns(DeprecationWarning):
            run = client.task_agent.runs.get_result(
                run_id="run_id",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(RunGetResultResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_result(self, client: Nimble) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.task_agent.runs.with_raw_response.get_result(
                run_id="run_id",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunGetResultResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_result(self, client: Nimble) -> None:
        with pytest.warns(DeprecationWarning):
            with client.task_agent.runs.with_streaming_response.get_result(
                run_id="run_id",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                run = response.parse()
                assert_matches_type(RunGetResultResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_result(self, client: Nimble) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
                client.task_agent.runs.with_raw_response.get_result(
                    run_id="run_id",
                    agent_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
                client.task_agent.runs.with_raw_response.get_result(
                    run_id="",
                    agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_events(self, client: Nimble) -> None:
        with pytest.warns(DeprecationWarning):
            run = client.task_agent.runs.stream_events(
                run_id="run_id",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(object, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream_events(self, client: Nimble) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.task_agent.runs.with_raw_response.stream_events(
                run_id="run_id",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(object, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream_events(self, client: Nimble) -> None:
        with pytest.warns(DeprecationWarning):
            with client.task_agent.runs.with_streaming_response.stream_events(
                run_id="run_id",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                run = response.parse()
                assert_matches_type(object, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_stream_events(self, client: Nimble) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
                client.task_agent.runs.with_raw_response.stream_events(
                    run_id="run_id",
                    agent_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
                client.task_agent.runs.with_raw_response.stream_events(
                    run_id="",
                    agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncNimble) -> None:
        with pytest.warns(DeprecationWarning):
            run = await async_client.task_agent.runs.list(
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(RunListResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncNimble) -> None:
        with pytest.warns(DeprecationWarning):
            run = await async_client.task_agent.runs.list(
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                limit=1,
                offset=0,
            )

        assert_matches_type(RunListResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNimble) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.task_agent.runs.with_raw_response.list(
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunListResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNimble) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.task_agent.runs.with_streaming_response.list(
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                run = await response.parse()
                assert_matches_type(RunListResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncNimble) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
                await async_client.task_agent.runs.with_raw_response.list(
                    agent_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncNimble) -> None:
        with pytest.warns(DeprecationWarning):
            run = await async_client.task_agent.runs.cancel(
                run_id="run_id",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert run is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncNimble) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.task_agent.runs.with_raw_response.cancel(
                run_id="run_id",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert run is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncNimble) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.task_agent.runs.with_streaming_response.cancel(
                run_id="run_id",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                run = await response.parse()
                assert run is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncNimble) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
                await async_client.task_agent.runs.with_raw_response.cancel(
                    run_id="run_id",
                    agent_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
                await async_client.task_agent.runs.with_raw_response.cancel(
                    run_id="",
                    agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncNimble) -> None:
        with pytest.warns(DeprecationWarning):
            run = await async_client.task_agent.runs.get(
                run_id="run_id",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(RunGetResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncNimble) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.task_agent.runs.with_raw_response.get(
                run_id="run_id",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunGetResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncNimble) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.task_agent.runs.with_streaming_response.get(
                run_id="run_id",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                run = await response.parse()
                assert_matches_type(RunGetResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncNimble) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
                await async_client.task_agent.runs.with_raw_response.get(
                    run_id="run_id",
                    agent_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
                await async_client.task_agent.runs.with_raw_response.get(
                    run_id="",
                    agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_result(self, async_client: AsyncNimble) -> None:
        with pytest.warns(DeprecationWarning):
            run = await async_client.task_agent.runs.get_result(
                run_id="run_id",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(RunGetResultResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_result(self, async_client: AsyncNimble) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.task_agent.runs.with_raw_response.get_result(
                run_id="run_id",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunGetResultResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_result(self, async_client: AsyncNimble) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.task_agent.runs.with_streaming_response.get_result(
                run_id="run_id",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                run = await response.parse()
                assert_matches_type(RunGetResultResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_result(self, async_client: AsyncNimble) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
                await async_client.task_agent.runs.with_raw_response.get_result(
                    run_id="run_id",
                    agent_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
                await async_client.task_agent.runs.with_raw_response.get_result(
                    run_id="",
                    agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_events(self, async_client: AsyncNimble) -> None:
        with pytest.warns(DeprecationWarning):
            run = await async_client.task_agent.runs.stream_events(
                run_id="run_id",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(object, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream_events(self, async_client: AsyncNimble) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.task_agent.runs.with_raw_response.stream_events(
                run_id="run_id",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(object, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream_events(self, async_client: AsyncNimble) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.task_agent.runs.with_streaming_response.stream_events(
                run_id="run_id",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                run = await response.parse()
                assert_matches_type(object, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_stream_events(self, async_client: AsyncNimble) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
                await async_client.task_agent.runs.with_raw_response.stream_events(
                    run_id="run_id",
                    agent_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
                await async_client.task_agent.runs.with_raw_response.stream_events(
                    run_id="",
                    agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                )
