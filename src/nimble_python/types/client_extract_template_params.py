# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ClientExtractTemplateParams"]


class ClientExtractTemplateParams(TypedDict, total=False):
    params: Required[Dict[str, object]]

    template: Required[str]
