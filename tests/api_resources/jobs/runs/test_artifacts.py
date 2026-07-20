# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from nimble_python import Nimble, AsyncNimble
from nimble_python.types.jobs.runs import (
    ArtifactGetResponse,
    ArtifactListResponse,
    ArtifactPreviewResponse,
    ArtifactDownloadURLResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArtifacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Nimble) -> None:
        artifact = client.jobs.runs.artifacts.list(
            "run_id",
        )
        assert_matches_type(ArtifactListResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Nimble) -> None:
        response = client.jobs.runs.artifacts.with_raw_response.list(
            "run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = response.parse()
        assert_matches_type(ArtifactListResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Nimble) -> None:
        with client.jobs.runs.artifacts.with_streaming_response.list(
            "run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = response.parse()
            assert_matches_type(ArtifactListResponse, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Nimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.jobs.runs.artifacts.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_download_url(self, client: Nimble) -> None:
        artifact = client.jobs.runs.artifacts.download_url(
            artifact_id=0,
            run_id="run_id",
        )
        assert_matches_type(ArtifactDownloadURLResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_download_url(self, client: Nimble) -> None:
        response = client.jobs.runs.artifacts.with_raw_response.download_url(
            artifact_id=0,
            run_id="run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = response.parse()
        assert_matches_type(ArtifactDownloadURLResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_download_url(self, client: Nimble) -> None:
        with client.jobs.runs.artifacts.with_streaming_response.download_url(
            artifact_id=0,
            run_id="run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = response.parse()
            assert_matches_type(ArtifactDownloadURLResponse, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_download_url(self, client: Nimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.jobs.runs.artifacts.with_raw_response.download_url(
                artifact_id=0,
                run_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Nimble) -> None:
        artifact = client.jobs.runs.artifacts.get(
            artifact_id=0,
            run_id="run_id",
        )
        assert_matches_type(ArtifactGetResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Nimble) -> None:
        response = client.jobs.runs.artifacts.with_raw_response.get(
            artifact_id=0,
            run_id="run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = response.parse()
        assert_matches_type(ArtifactGetResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Nimble) -> None:
        with client.jobs.runs.artifacts.with_streaming_response.get(
            artifact_id=0,
            run_id="run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = response.parse()
            assert_matches_type(ArtifactGetResponse, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Nimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.jobs.runs.artifacts.with_raw_response.get(
                artifact_id=0,
                run_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_preview(self, client: Nimble) -> None:
        artifact = client.jobs.runs.artifacts.preview(
            artifact_id=0,
            run_id="run_id",
        )
        assert_matches_type(ArtifactPreviewResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_preview(self, client: Nimble) -> None:
        response = client.jobs.runs.artifacts.with_raw_response.preview(
            artifact_id=0,
            run_id="run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = response.parse()
        assert_matches_type(ArtifactPreviewResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_preview(self, client: Nimble) -> None:
        with client.jobs.runs.artifacts.with_streaming_response.preview(
            artifact_id=0,
            run_id="run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = response.parse()
            assert_matches_type(ArtifactPreviewResponse, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_preview(self, client: Nimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.jobs.runs.artifacts.with_raw_response.preview(
                artifact_id=0,
                run_id="",
            )


class TestAsyncArtifacts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncNimble) -> None:
        artifact = await async_client.jobs.runs.artifacts.list(
            "run_id",
        )
        assert_matches_type(ArtifactListResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNimble) -> None:
        response = await async_client.jobs.runs.artifacts.with_raw_response.list(
            "run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = await response.parse()
        assert_matches_type(ArtifactListResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNimble) -> None:
        async with async_client.jobs.runs.artifacts.with_streaming_response.list(
            "run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = await response.parse()
            assert_matches_type(ArtifactListResponse, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncNimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.jobs.runs.artifacts.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_download_url(self, async_client: AsyncNimble) -> None:
        artifact = await async_client.jobs.runs.artifacts.download_url(
            artifact_id=0,
            run_id="run_id",
        )
        assert_matches_type(ArtifactDownloadURLResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_download_url(self, async_client: AsyncNimble) -> None:
        response = await async_client.jobs.runs.artifacts.with_raw_response.download_url(
            artifact_id=0,
            run_id="run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = await response.parse()
        assert_matches_type(ArtifactDownloadURLResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_download_url(self, async_client: AsyncNimble) -> None:
        async with async_client.jobs.runs.artifacts.with_streaming_response.download_url(
            artifact_id=0,
            run_id="run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = await response.parse()
            assert_matches_type(ArtifactDownloadURLResponse, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_download_url(self, async_client: AsyncNimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.jobs.runs.artifacts.with_raw_response.download_url(
                artifact_id=0,
                run_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncNimble) -> None:
        artifact = await async_client.jobs.runs.artifacts.get(
            artifact_id=0,
            run_id="run_id",
        )
        assert_matches_type(ArtifactGetResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncNimble) -> None:
        response = await async_client.jobs.runs.artifacts.with_raw_response.get(
            artifact_id=0,
            run_id="run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = await response.parse()
        assert_matches_type(ArtifactGetResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncNimble) -> None:
        async with async_client.jobs.runs.artifacts.with_streaming_response.get(
            artifact_id=0,
            run_id="run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = await response.parse()
            assert_matches_type(ArtifactGetResponse, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncNimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.jobs.runs.artifacts.with_raw_response.get(
                artifact_id=0,
                run_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_preview(self, async_client: AsyncNimble) -> None:
        artifact = await async_client.jobs.runs.artifacts.preview(
            artifact_id=0,
            run_id="run_id",
        )
        assert_matches_type(ArtifactPreviewResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_preview(self, async_client: AsyncNimble) -> None:
        response = await async_client.jobs.runs.artifacts.with_raw_response.preview(
            artifact_id=0,
            run_id="run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = await response.parse()
        assert_matches_type(ArtifactPreviewResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_preview(self, async_client: AsyncNimble) -> None:
        async with async_client.jobs.runs.artifacts.with_streaming_response.preview(
            artifact_id=0,
            run_id="run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = await response.parse()
            assert_matches_type(ArtifactPreviewResponse, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_preview(self, async_client: AsyncNimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.jobs.runs.artifacts.with_raw_response.preview(
                artifact_id=0,
                run_id="",
            )
