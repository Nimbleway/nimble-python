# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from ...._models import BaseModel

__all__ = ["ArtifactPreviewResponse"]


class ArtifactPreviewResponse(BaseModel):
    columns: List[str]

    row_count: int

    rows: List[Dict[str, object]]
