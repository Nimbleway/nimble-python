# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["JobGetResponse", "Destination", "Inputs", "Schedule"]


class Destination(BaseModel):
    path: str

    type: Literal["file", "s3"]

    format: Optional[Literal["jsonl", "csv", "parquet"]] = None


class Inputs(BaseModel):
    type: Literal["s3", "inline", "file"]

    data: Optional[List[Dict[str, object]]] = None

    file_path: Optional[str] = None


class Schedule(BaseModel):
    cron: str

    enabled: bool


class JobGetResponse(BaseModel):
    id: str

    name: str

    agent_name: Optional[str] = None

    created_at: Optional[datetime] = None

    description: Optional[str] = None

    destination: Optional[Destination] = None

    display_name: Optional[str] = None

    inputs: Optional[Inputs] = None

    last_run_at: Optional[datetime] = None

    last_run_status: Optional[Literal["PENDING", "RUNNING", "SUCCESS", "FAILED", "CANCELLED", "TIMEOUT", "WARNING"]] = (
        None
    )

    schedule: Optional[Schedule] = None

    updated_at: Optional[datetime] = None
