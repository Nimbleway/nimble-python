# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from nimble_python import Nimble, AsyncNimble
from nimble_python.types.extract import (
    TemplateGetResponse,
    TemplateRunResponse,
    TemplateListResponse,
    TemplateAsyncResponse,
    TemplateBatchResponse,
    TemplateUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Nimble) -> None:
        template = client.extract.templates.update(
            extract_template_name="extract_template_name",
            body=[
                {
                    "op": "add",
                    "path": "path",
                }
            ],
        )
        assert_matches_type(TemplateUpdateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Nimble) -> None:
        response = client.extract.templates.with_raw_response.update(
            extract_template_name="extract_template_name",
            body=[
                {
                    "op": "add",
                    "path": "path",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateUpdateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Nimble) -> None:
        with client.extract.templates.with_streaming_response.update(
            extract_template_name="extract_template_name",
            body=[
                {
                    "op": "add",
                    "path": "path",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateUpdateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Nimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extract_template_name` but received ''"):
            client.extract.templates.with_raw_response.update(
                extract_template_name="",
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
        template = client.extract.templates.list()
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Nimble) -> None:
        template = client.extract.templates.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Nimble) -> None:
        response = client.extract.templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Nimble) -> None:
        with client.extract.templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateListResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Nimble) -> None:
        template = client.extract.templates.delete(
            "extract_template_name",
        )
        assert template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Nimble) -> None:
        response = client.extract.templates.with_raw_response.delete(
            "extract_template_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Nimble) -> None:
        with client.extract.templates.with_streaming_response.delete(
            "extract_template_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert template is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Nimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extract_template_name` but received ''"):
            client.extract.templates.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_async(self, client: Nimble) -> None:
        template = client.extract.templates.async_(
            params={"foo": "bar"},
            template="template",
        )
        assert_matches_type(TemplateAsyncResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_async_with_all_params(self, client: Nimble) -> None:
        template = client.extract.templates.async_(
            params={"foo": "bar"},
            template="template",
            callback_url="https://example.com/webhook/callback",
            formats=["html", "markdown"],
            localization=True,
            storage_compress=True,
            storage_object_name="result-2024-01-15.json",
            storage_type="s3",
            storage_url="s3://bucket-name/path/to/object",
        )
        assert_matches_type(TemplateAsyncResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_async(self, client: Nimble) -> None:
        response = client.extract.templates.with_raw_response.async_(
            params={"foo": "bar"},
            template="template",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateAsyncResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_async(self, client: Nimble) -> None:
        with client.extract.templates.with_streaming_response.async_(
            params={"foo": "bar"},
            template="template",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateAsyncResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch(self, client: Nimble) -> None:
        template = client.extract.templates.batch(
            inputs=[{}],
            shared_inputs={"template": "template"},
        )
        assert_matches_type(TemplateBatchResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch_with_all_params(self, client: Nimble) -> None:
        template = client.extract.templates.batch(
            inputs=[
                {
                    "formats": ["html", "markdown"],
                    "localization": True,
                    "params": {"foo": "bar"},
                }
            ],
            shared_inputs={
                "template": "template",
                "formats": ["html", "markdown"],
                "localization": True,
                "params": {"foo": "bar"},
            },
        )
        assert_matches_type(TemplateBatchResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_batch(self, client: Nimble) -> None:
        response = client.extract.templates.with_raw_response.batch(
            inputs=[{}],
            shared_inputs={"template": "template"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateBatchResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_batch(self, client: Nimble) -> None:
        with client.extract.templates.with_streaming_response.batch(
            inputs=[{}],
            shared_inputs={"template": "template"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateBatchResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Nimble) -> None:
        template = client.extract.templates.get(
            "extract_template_name",
        )
        assert_matches_type(TemplateGetResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Nimble) -> None:
        response = client.extract.templates.with_raw_response.get(
            "extract_template_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateGetResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Nimble) -> None:
        with client.extract.templates.with_streaming_response.get(
            "extract_template_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateGetResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Nimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extract_template_name` but received ''"):
            client.extract.templates.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run(self, client: Nimble) -> None:
        template = client.extract.templates.run(
            params={"foo": "bar"},
            template="template",
        )
        assert_matches_type(TemplateRunResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: Nimble) -> None:
        template = client.extract.templates.run(
            params={"foo": "bar"},
            template="template",
            formats=["html", "markdown"],
            localization=True,
        )
        assert_matches_type(TemplateRunResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: Nimble) -> None:
        response = client.extract.templates.with_raw_response.run(
            params={"foo": "bar"},
            template="template",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateRunResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: Nimble) -> None:
        with client.extract.templates.with_streaming_response.run(
            params={"foo": "bar"},
            template="template",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateRunResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTemplates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncNimble) -> None:
        template = await async_client.extract.templates.update(
            extract_template_name="extract_template_name",
            body=[
                {
                    "op": "add",
                    "path": "path",
                }
            ],
        )
        assert_matches_type(TemplateUpdateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncNimble) -> None:
        response = await async_client.extract.templates.with_raw_response.update(
            extract_template_name="extract_template_name",
            body=[
                {
                    "op": "add",
                    "path": "path",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateUpdateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncNimble) -> None:
        async with async_client.extract.templates.with_streaming_response.update(
            extract_template_name="extract_template_name",
            body=[
                {
                    "op": "add",
                    "path": "path",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateUpdateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncNimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extract_template_name` but received ''"):
            await async_client.extract.templates.with_raw_response.update(
                extract_template_name="",
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
        template = await async_client.extract.templates.list()
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncNimble) -> None:
        template = await async_client.extract.templates.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNimble) -> None:
        response = await async_client.extract.templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNimble) -> None:
        async with async_client.extract.templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateListResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncNimble) -> None:
        template = await async_client.extract.templates.delete(
            "extract_template_name",
        )
        assert template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncNimble) -> None:
        response = await async_client.extract.templates.with_raw_response.delete(
            "extract_template_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncNimble) -> None:
        async with async_client.extract.templates.with_streaming_response.delete(
            "extract_template_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert template is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncNimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extract_template_name` but received ''"):
            await async_client.extract.templates.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_async(self, async_client: AsyncNimble) -> None:
        template = await async_client.extract.templates.async_(
            params={"foo": "bar"},
            template="template",
        )
        assert_matches_type(TemplateAsyncResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_async_with_all_params(self, async_client: AsyncNimble) -> None:
        template = await async_client.extract.templates.async_(
            params={"foo": "bar"},
            template="template",
            callback_url="https://example.com/webhook/callback",
            formats=["html", "markdown"],
            localization=True,
            storage_compress=True,
            storage_object_name="result-2024-01-15.json",
            storage_type="s3",
            storage_url="s3://bucket-name/path/to/object",
        )
        assert_matches_type(TemplateAsyncResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_async(self, async_client: AsyncNimble) -> None:
        response = await async_client.extract.templates.with_raw_response.async_(
            params={"foo": "bar"},
            template="template",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateAsyncResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_async(self, async_client: AsyncNimble) -> None:
        async with async_client.extract.templates.with_streaming_response.async_(
            params={"foo": "bar"},
            template="template",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateAsyncResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch(self, async_client: AsyncNimble) -> None:
        template = await async_client.extract.templates.batch(
            inputs=[{}],
            shared_inputs={"template": "template"},
        )
        assert_matches_type(TemplateBatchResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch_with_all_params(self, async_client: AsyncNimble) -> None:
        template = await async_client.extract.templates.batch(
            inputs=[
                {
                    "formats": ["html", "markdown"],
                    "localization": True,
                    "params": {"foo": "bar"},
                }
            ],
            shared_inputs={
                "template": "template",
                "formats": ["html", "markdown"],
                "localization": True,
                "params": {"foo": "bar"},
            },
        )
        assert_matches_type(TemplateBatchResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_batch(self, async_client: AsyncNimble) -> None:
        response = await async_client.extract.templates.with_raw_response.batch(
            inputs=[{}],
            shared_inputs={"template": "template"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateBatchResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_batch(self, async_client: AsyncNimble) -> None:
        async with async_client.extract.templates.with_streaming_response.batch(
            inputs=[{}],
            shared_inputs={"template": "template"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateBatchResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncNimble) -> None:
        template = await async_client.extract.templates.get(
            "extract_template_name",
        )
        assert_matches_type(TemplateGetResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncNimble) -> None:
        response = await async_client.extract.templates.with_raw_response.get(
            "extract_template_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateGetResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncNimble) -> None:
        async with async_client.extract.templates.with_streaming_response.get(
            "extract_template_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateGetResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncNimble) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extract_template_name` but received ''"):
            await async_client.extract.templates.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncNimble) -> None:
        template = await async_client.extract.templates.run(
            params={"foo": "bar"},
            template="template",
        )
        assert_matches_type(TemplateRunResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncNimble) -> None:
        template = await async_client.extract.templates.run(
            params={"foo": "bar"},
            template="template",
            formats=["html", "markdown"],
            localization=True,
        )
        assert_matches_type(TemplateRunResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncNimble) -> None:
        response = await async_client.extract.templates.with_raw_response.run(
            params={"foo": "bar"},
            template="template",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateRunResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncNimble) -> None:
        async with async_client.extract.templates.with_streaming_response.run(
            params={"foo": "bar"},
            template="template",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateRunResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True
