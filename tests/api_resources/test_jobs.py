# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from nimble_python import Nimble, AsyncNimble
from nimble_python.types import (
    JobGetResponse,
    JobListResponse,
    JobCreateResponse,
    JobUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Nimble) -> None:
        job = client.jobs.create(
            extract_template_name="extract_template_name",
            name="name",
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Nimble) -> None:
        job = client.jobs.create(
            extract_template_name="extract_template_name",
            name="name",
            description="description",
            destination={
                "path": "path",
                "type": "file",
                "format": "jsonl",
            },
            display_name="display_name",
            inputs={
                "type": "s3",
                "data": [{"foo": "bar"}],
                "file_path": "file_path",
                "node_data": {"foo": [{"foo": "bar"}]},
            },
            schedule={
                "cron": "cron",
                "enabled": True,
            },
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Nimble) -> None:
        response = client.jobs.with_raw_response.create(
            extract_template_name="extract_template_name",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Nimble) -> None:
        with client.jobs.with_streaming_response.create(
            extract_template_name="extract_template_name",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobCreateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Nimble) -> None:
        job = client.jobs.update(
            job_id="job_id",
        )
        assert_matches_type(JobUpdateResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Nimble) -> None:
        job = client.jobs.update(
            job_id="job_id",
            description="description",
            destination={
                "path": "path",
                "type": "file",
                "format": "jsonl",
            },
            display_name="display_name",
            inputs={
                "type": "s3",
                "data": [{"foo": "bar"}],
                "file_path": "file_path",
                "node_data": {"foo": [{"foo": "bar"}]},
            },
            schedule={
                "cron": "cron",
                "enabled": True,
            },
        )
        assert_matches_type(JobUpdateResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Nimble) -> None:
        response = client.jobs.with_raw_response.update(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobUpdateResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Nimble) -> None:
        with client.jobs.with_streaming_response.update(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobUpdateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Nimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.jobs.with_raw_response.update(
                job_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Nimble) -> None:
        job = client.jobs.list()
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Nimble) -> None:
        job = client.jobs.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Nimble) -> None:
        response = client.jobs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Nimble) -> None:
        with client.jobs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobListResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Nimble) -> None:
        job = client.jobs.delete(
            "job_id",
        )
        assert job is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Nimble) -> None:
        response = client.jobs.with_raw_response.delete(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert job is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Nimble) -> None:
        with client.jobs.with_streaming_response.delete(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert job is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Nimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.jobs.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Nimble) -> None:
        job = client.jobs.get(
            "job_id",
        )
        assert_matches_type(JobGetResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Nimble) -> None:
        response = client.jobs.with_raw_response.get(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobGetResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Nimble) -> None:
        with client.jobs.with_streaming_response.get(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobGetResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Nimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.jobs.with_raw_response.get(
                "",
            )


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncNimble) -> None:
        job = await async_client.jobs.create(
            extract_template_name="extract_template_name",
            name="name",
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncNimble) -> None:
        job = await async_client.jobs.create(
            extract_template_name="extract_template_name",
            name="name",
            description="description",
            destination={
                "path": "path",
                "type": "file",
                "format": "jsonl",
            },
            display_name="display_name",
            inputs={
                "type": "s3",
                "data": [{"foo": "bar"}],
                "file_path": "file_path",
                "node_data": {"foo": [{"foo": "bar"}]},
            },
            schedule={
                "cron": "cron",
                "enabled": True,
            },
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncNimble) -> None:
        response = await async_client.jobs.with_raw_response.create(
            extract_template_name="extract_template_name",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncNimble) -> None:
        async with async_client.jobs.with_streaming_response.create(
            extract_template_name="extract_template_name",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobCreateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncNimble) -> None:
        job = await async_client.jobs.update(
            job_id="job_id",
        )
        assert_matches_type(JobUpdateResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncNimble) -> None:
        job = await async_client.jobs.update(
            job_id="job_id",
            description="description",
            destination={
                "path": "path",
                "type": "file",
                "format": "jsonl",
            },
            display_name="display_name",
            inputs={
                "type": "s3",
                "data": [{"foo": "bar"}],
                "file_path": "file_path",
                "node_data": {"foo": [{"foo": "bar"}]},
            },
            schedule={
                "cron": "cron",
                "enabled": True,
            },
        )
        assert_matches_type(JobUpdateResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncNimble) -> None:
        response = await async_client.jobs.with_raw_response.update(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobUpdateResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncNimble) -> None:
        async with async_client.jobs.with_streaming_response.update(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobUpdateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncNimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.jobs.with_raw_response.update(
                job_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncNimble) -> None:
        job = await async_client.jobs.list()
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncNimble) -> None:
        job = await async_client.jobs.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNimble) -> None:
        response = await async_client.jobs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNimble) -> None:
        async with async_client.jobs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobListResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncNimble) -> None:
        job = await async_client.jobs.delete(
            "job_id",
        )
        assert job is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncNimble) -> None:
        response = await async_client.jobs.with_raw_response.delete(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert job is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncNimble) -> None:
        async with async_client.jobs.with_streaming_response.delete(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert job is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncNimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.jobs.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncNimble) -> None:
        job = await async_client.jobs.get(
            "job_id",
        )
        assert_matches_type(JobGetResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncNimble) -> None:
        response = await async_client.jobs.with_raw_response.get(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobGetResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncNimble) -> None:
        async with async_client.jobs.with_streaming_response.get(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobGetResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncNimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.jobs.with_raw_response.get(
                "",
            )
