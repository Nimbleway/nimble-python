# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["JobListResponse", "Item", "ItemDestination", "ItemInputs", "ItemSchedule"]


class ItemDestination(BaseModel):
    path: str

    type: Literal["file", "s3"]

    format: Optional[Literal["jsonl", "csv", "parquet"]] = None


class ItemInputs(BaseModel):
    type: Literal["s3", "inline", "file"]

    data: Optional[List[Dict[str, object]]] = None

    file_path: Optional[str] = None


class ItemSchedule(BaseModel):
    cron: str

    enabled: bool


class Item(BaseModel):
    id: str

    name: str

    agent_name: Optional[str] = None

    created_at: Optional[datetime] = None

    description: Optional[str] = None

    destination: Optional[ItemDestination] = None

    display_name: Optional[str] = None

    inputs: Optional[ItemInputs] = None

    last_run_at: Optional[datetime] = None

    last_run_status: Optional[Literal["PENDING", "RUNNING", "SUCCESS", "FAILED", "CANCELLED", "TIMEOUT", "WARNING"]] = (
        None
    )

    schedule: Optional[ItemSchedule] = None

    updated_at: Optional[datetime] = None


class JobListResponse(BaseModel):
    items: List[Item]

    page: int

    per_page: int

    total: int
