# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from nimble_python import Nimble, AsyncNimble
from nimble_python.types import MediaRunResponse, MediaRunAsyncResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMedia:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run(self, client: Nimble) -> None:
        media = client.media.run(
            url="https://example.com",
        )
        assert_matches_type(MediaRunResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: Nimble) -> None:
        media = client.media.run(
            url="https://example.com",
            country="country",
            expected_mime_types=["string"],
            locale="locale",
            storage={
                "url": "url",
                "object_name": "object_name",
                "type": "s3",
            },
        )
        assert_matches_type(MediaRunResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: Nimble) -> None:
        response = client.media.with_raw_response.run(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(MediaRunResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: Nimble) -> None:
        with client.media.with_streaming_response.run(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(MediaRunResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_async(self, client: Nimble) -> None:
        media = client.media.run_async(
            url="https://example.com",
        )
        assert_matches_type(MediaRunAsyncResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_async_with_all_params(self, client: Nimble) -> None:
        media = client.media.run_async(
            url="https://example.com",
            callback_url="https://example.com/webhook/callback",
            country="country",
            expected_mime_types=["string"],
            locale="locale",
            storage={
                "url": "url",
                "object_name": "object_name",
                "type": "s3",
            },
            storage_compress=True,
            storage_object_name="result-2024-01-15.json",
            storage_type="s3",
            storage_url="s3://bucket-name/path/to/object",
        )
        assert_matches_type(MediaRunAsyncResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run_async(self, client: Nimble) -> None:
        response = client.media.with_raw_response.run_async(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(MediaRunAsyncResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run_async(self, client: Nimble) -> None:
        with client.media.with_streaming_response.run_async(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(MediaRunAsyncResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMedia:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncNimble) -> None:
        media = await async_client.media.run(
            url="https://example.com",
        )
        assert_matches_type(MediaRunResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncNimble) -> None:
        media = await async_client.media.run(
            url="https://example.com",
            country="country",
            expected_mime_types=["string"],
            locale="locale",
            storage={
                "url": "url",
                "object_name": "object_name",
                "type": "s3",
            },
        )
        assert_matches_type(MediaRunResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncNimble) -> None:
        response = await async_client.media.with_raw_response.run(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(MediaRunResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncNimble) -> None:
        async with async_client.media.with_streaming_response.run(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(MediaRunResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_async(self, async_client: AsyncNimble) -> None:
        media = await async_client.media.run_async(
            url="https://example.com",
        )
        assert_matches_type(MediaRunAsyncResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_async_with_all_params(self, async_client: AsyncNimble) -> None:
        media = await async_client.media.run_async(
            url="https://example.com",
            callback_url="https://example.com/webhook/callback",
            country="country",
            expected_mime_types=["string"],
            locale="locale",
            storage={
                "url": "url",
                "object_name": "object_name",
                "type": "s3",
            },
            storage_compress=True,
            storage_object_name="result-2024-01-15.json",
            storage_type="s3",
            storage_url="s3://bucket-name/path/to/object",
        )
        assert_matches_type(MediaRunAsyncResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run_async(self, async_client: AsyncNimble) -> None:
        response = await async_client.media.with_raw_response.run_async(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(MediaRunAsyncResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run_async(self, async_client: AsyncNimble) -> None:
        async with async_client.media.with_streaming_response.run_async(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(MediaRunAsyncResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True
