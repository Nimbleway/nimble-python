# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from nimble_python import Nimble, AsyncNimble
from nimble_python.types.extract.templates import (
    GenerationGetResponse,
    GenerationCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenerations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Nimble) -> None:
        generation = client.extract.templates.generations.create(
            prompt="prompt",
            url="url",
        )
        assert_matches_type(GenerationCreateResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Nimble) -> None:
        generation = client.extract.templates.generations.create(
            prompt="prompt",
            url="url",
            input_schema={"foo": "bar"},
            metadata={
                "description": "description",
                "display_name": "display_name",
                "tags": ["string"],
            },
            name="name",
            output_schema={"foo": "bar"},
        )
        assert_matches_type(GenerationCreateResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Nimble) -> None:
        response = client.extract.templates.generations.with_raw_response.create(
            prompt="prompt",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = response.parse()
        assert_matches_type(GenerationCreateResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Nimble) -> None:
        with client.extract.templates.generations.with_streaming_response.create(
            prompt="prompt",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = response.parse()
            assert_matches_type(GenerationCreateResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Nimble) -> None:
        generation = client.extract.templates.generations.create(
            from_extract_template="from_extract_template",
            prompt="prompt",
        )
        assert_matches_type(GenerationCreateResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Nimble) -> None:
        response = client.extract.templates.generations.with_raw_response.create(
            from_extract_template="from_extract_template",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = response.parse()
        assert_matches_type(GenerationCreateResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Nimble) -> None:
        with client.extract.templates.generations.with_streaming_response.create(
            from_extract_template="from_extract_template",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = response.parse()
            assert_matches_type(GenerationCreateResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Nimble) -> None:
        generation = client.extract.templates.generations.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GenerationGetResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Nimble) -> None:
        response = client.extract.templates.generations.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = response.parse()
        assert_matches_type(GenerationGetResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Nimble) -> None:
        with client.extract.templates.generations.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = response.parse()
            assert_matches_type(GenerationGetResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Nimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_id` but received ''"):
            client.extract.templates.generations.with_raw_response.get(
                "",
            )


class TestAsyncGenerations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncNimble) -> None:
        generation = await async_client.extract.templates.generations.create(
            prompt="prompt",
            url="url",
        )
        assert_matches_type(GenerationCreateResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncNimble) -> None:
        generation = await async_client.extract.templates.generations.create(
            prompt="prompt",
            url="url",
            input_schema={"foo": "bar"},
            metadata={
                "description": "description",
                "display_name": "display_name",
                "tags": ["string"],
            },
            name="name",
            output_schema={"foo": "bar"},
        )
        assert_matches_type(GenerationCreateResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncNimble) -> None:
        response = await async_client.extract.templates.generations.with_raw_response.create(
            prompt="prompt",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = await response.parse()
        assert_matches_type(GenerationCreateResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncNimble) -> None:
        async with async_client.extract.templates.generations.with_streaming_response.create(
            prompt="prompt",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = await response.parse()
            assert_matches_type(GenerationCreateResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncNimble) -> None:
        generation = await async_client.extract.templates.generations.create(
            from_extract_template="from_extract_template",
            prompt="prompt",
        )
        assert_matches_type(GenerationCreateResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncNimble) -> None:
        response = await async_client.extract.templates.generations.with_raw_response.create(
            from_extract_template="from_extract_template",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = await response.parse()
        assert_matches_type(GenerationCreateResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncNimble) -> None:
        async with async_client.extract.templates.generations.with_streaming_response.create(
            from_extract_template="from_extract_template",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = await response.parse()
            assert_matches_type(GenerationCreateResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncNimble) -> None:
        generation = await async_client.extract.templates.generations.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GenerationGetResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncNimble) -> None:
        response = await async_client.extract.templates.generations.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = await response.parse()
        assert_matches_type(GenerationGetResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncNimble) -> None:
        async with async_client.extract.templates.generations.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = await response.parse()
            assert_matches_type(GenerationGetResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncNimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_id` but received ''"):
            await async_client.extract.templates.generations.with_raw_response.get(
                "",
            )
