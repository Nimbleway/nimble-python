# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["JobUpdateParams", "Destination", "Inputs", "Schedule"]


class JobUpdateParams(TypedDict, total=False):
    description: Optional[str]

    destination: Optional[Destination]

    display_name: Optional[str]

    inputs: Optional[Inputs]

    schedule: Optional[Schedule]


class Destination(TypedDict, total=False):
    path: Required[str]

    type: Required[Literal["file", "s3"]]

    format: Literal["jsonl", "csv", "parquet"]


class Inputs(TypedDict, total=False):
    type: Required[Literal["s3", "inline", "file"]]

    data: Optional[Iterable[Dict[str, object]]]

    file_path: Optional[str]


class Schedule(TypedDict, total=False):
    cron: Required[str]

    enabled: Required[bool]
