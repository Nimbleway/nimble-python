# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from ...._models import BaseModel

__all__ = ["ArtifactPreviewResponse"]


class ArtifactPreviewResponse(BaseModel):
    """A tabular preview of an artifact's contents."""

    columns: List[str]
    """Column names in the preview."""

    row_count: int
    """Total number of rows in the artifact."""

    rows: List[Dict[str, object]]
    """Sample rows from the artifact."""
