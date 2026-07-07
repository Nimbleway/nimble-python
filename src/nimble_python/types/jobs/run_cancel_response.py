# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RunCancelResponse"]


class RunCancelResponse(BaseModel):
    """Result of cancelling a run."""

    id: str
    """Identifier of the cancelled run."""

    status: Literal["PENDING", "RUNNING", "SUCCESS", "FAILED", "CANCELLED", "TIMEOUT", "WARNING"]
    """Run status after cancellation."""
