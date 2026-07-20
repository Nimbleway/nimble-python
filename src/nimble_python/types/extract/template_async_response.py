# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TemplateAsyncResponse"]


class TemplateAsyncResponse(BaseModel):
    status: Literal["success"]

    task: Dict[str, object]
