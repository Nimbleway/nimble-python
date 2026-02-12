# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "CrawlListResponse",
    "Data",
    "DataCrawlOptions",
    "DataCrawlOptionsCallback",
    "DataCrawlOptionsCallbackUnionMember0",
    "DataTask",
    "Pagination",
]


class DataCrawlOptionsCallbackUnionMember0(BaseModel):
    url: str

    events: Optional[List[Literal["started", "page", "completed", "failed"]]] = None

    headers: Optional[Dict[str, str]] = None

    metadata: Optional[Dict[str, object]] = None


DataCrawlOptionsCallback: TypeAlias = Union[DataCrawlOptionsCallbackUnionMember0, str]


class DataCrawlOptions(BaseModel):
    allow_external_links: bool

    allow_subdomains: bool

    crawl_entire_domain: bool

    ignore_query_parameters: bool

    limit: int

    max_discovery_depth: int

    sitemap: Literal["skip", "include", "only"]

    callback: Optional[DataCrawlOptionsCallback] = None

    exclude_paths: Optional[List[str]] = None

    include_paths: Optional[List[str]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class DataTask(BaseModel):
    status: Literal["pending", "completed", "failed"]

    task_id: str

    created_at: Optional[str] = None

    updated_at: Optional[str] = None


class Data(BaseModel):
    """Crawl API response"""

    account_name: str

    crawl_id: str

    crawl_options: DataCrawlOptions

    created_at: Union[str, Dict[str, object]]

    status: Literal["queued", "running", "succeeded", "failed", "canceled"]

    updated_at: Union[str, Dict[str, object]]

    url: str

    completed: Optional[float] = None

    completed_at: Union[str, Dict[str, object], None] = None

    extract_options: Optional[Dict[str, object]] = None

    failed: Optional[float] = None

    name: Optional[str] = None

    pending: Optional[float] = None

    tasks: Optional[List[DataTask]] = None

    total: Optional[float] = None


class Pagination(BaseModel):
    has_next: bool

    next_cursor: Optional[str] = None

    total: Optional[float] = None


class CrawlListResponse(BaseModel):
    """Successful get crawl response"""

    data: List[Data]

    pagination: Pagination
