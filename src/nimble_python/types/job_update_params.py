# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["JobUpdateParams", "Destination", "Inputs", "Schedule"]


class JobUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """New description."""

    destination: Optional[Destination]
    """Where a job writes its results."""

    display_name: Optional[str]
    """New display name."""

    inputs: Optional[Inputs]
    """Configuration for the input data a job processes."""

    schedule: Optional[Schedule]
    """Cron-based schedule controlling when a job runs automatically."""


class Destination(TypedDict, total=False):
    """Where a job writes its results."""

    path: Required[str]
    """Destination path the output is written to."""

    type: Required[Literal["file", "s3"]]
    """Destination kind: a local 'file' or an 's3' bucket."""

    format: Literal["jsonl", "csv", "parquet"]
    """Output file format."""


class Inputs(TypedDict, total=False):
    """Configuration for the input data a job processes."""

    type: Required[Literal["s3", "inline", "file"]]
    """
    How inputs are supplied: an 's3' bucket, 'inline' records, or an uploaded
    'file'.
    """

    data: Optional[Iterable[Dict[str, object]]]
    """Inline list of input records. Used when type is 'inline'."""

    file_path: Optional[str]
    """Path to the input file; must start with 's3' or 'file\\__'.

    Used for 's3'/'file' types.
    """

    node_data: Optional[Dict[str, Iterable[Dict[str, object]]]]
    """Inline input records keyed by source node id, e.g.

    {'source_a': [{...}]}. Used when type is 'inline' on a dynamic-workflow job,
    which has one source node per input file. Mutually exclusive with 'data'.
    """


class Schedule(TypedDict, total=False):
    """Cron-based schedule controlling when a job runs automatically."""

    cron: Required[str]
    """Cron expression defining when the job runs."""

    enabled: Required[bool]
    """Whether the schedule is currently active."""
