# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from nimble_python import Nimble, AsyncNimble
from nimble_python.types.extract.templates import VersionGetResponse, VersionListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Nimble) -> None:
        version = client.extract.templates.versions.list(
            extract_template_name="extract_template_name",
        )
        assert_matches_type(VersionListResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Nimble) -> None:
        version = client.extract.templates.versions.list(
            extract_template_name="extract_template_name",
            limit=1,
            offset=0,
        )
        assert_matches_type(VersionListResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Nimble) -> None:
        response = client.extract.templates.versions.with_raw_response.list(
            extract_template_name="extract_template_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionListResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Nimble) -> None:
        with client.extract.templates.versions.with_streaming_response.list(
            extract_template_name="extract_template_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionListResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Nimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extract_template_name` but received ''"):
            client.extract.templates.versions.with_raw_response.list(
                extract_template_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Nimble) -> None:
        version = client.extract.templates.versions.get(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            extract_template_name="extract_template_name",
        )
        assert_matches_type(VersionGetResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Nimble) -> None:
        response = client.extract.templates.versions.with_raw_response.get(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            extract_template_name="extract_template_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionGetResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Nimble) -> None:
        with client.extract.templates.versions.with_streaming_response.get(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            extract_template_name="extract_template_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionGetResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Nimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extract_template_name` but received ''"):
            client.extract.templates.versions.with_raw_response.get(
                version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                extract_template_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.extract.templates.versions.with_raw_response.get(
                version_id="",
                extract_template_name="extract_template_name",
            )


class TestAsyncVersions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncNimble) -> None:
        version = await async_client.extract.templates.versions.list(
            extract_template_name="extract_template_name",
        )
        assert_matches_type(VersionListResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncNimble) -> None:
        version = await async_client.extract.templates.versions.list(
            extract_template_name="extract_template_name",
            limit=1,
            offset=0,
        )
        assert_matches_type(VersionListResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNimble) -> None:
        response = await async_client.extract.templates.versions.with_raw_response.list(
            extract_template_name="extract_template_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(VersionListResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNimble) -> None:
        async with async_client.extract.templates.versions.with_streaming_response.list(
            extract_template_name="extract_template_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionListResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncNimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extract_template_name` but received ''"):
            await async_client.extract.templates.versions.with_raw_response.list(
                extract_template_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncNimble) -> None:
        version = await async_client.extract.templates.versions.get(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            extract_template_name="extract_template_name",
        )
        assert_matches_type(VersionGetResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncNimble) -> None:
        response = await async_client.extract.templates.versions.with_raw_response.get(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            extract_template_name="extract_template_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(VersionGetResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncNimble) -> None:
        async with async_client.extract.templates.versions.with_streaming_response.get(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            extract_template_name="extract_template_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionGetResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncNimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extract_template_name` but received ''"):
            await async_client.extract.templates.versions.with_raw_response.get(
                version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                extract_template_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.extract.templates.versions.with_raw_response.get(
                version_id="",
                extract_template_name="extract_template_name",
            )
