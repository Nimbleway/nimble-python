# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "TemplateRunResponse",
    "Data",
    "DataBrowserActions",
    "DataBrowserActionsResult",
    "DataNetworkCapture",
    "DataNetworkCaptureFilter",
    "DataNetworkCaptureFilterURL",
    "DataNetworkCaptureResult",
    "DataNetworkCaptureResultRequest",
    "DataNetworkCaptureResultResponse",
    "DataParsing",
    "DataParsingParsingSuccessResult",
    "DataParsingParsingErrorResult",
    "DataRedirect",
    "Metadata",
    "Debug",
    "Pagination",
    "PaginationNextPageParams",
    "PaginationUnionMember1",
]


class DataBrowserActionsResult(BaseModel):
    duration: float

    name: Literal[
        "goto",
        "wait",
        "wait_for_element",
        "wait_for_navigation",
        "click",
        "fill",
        "press",
        "scroll",
        "auto_scroll",
        "screenshot",
        "get_cookies",
        "eval",
        "fetch",
    ]

    status: Literal["no-run", "in-progress", "done", "error", "skipped"]

    error: Optional[str] = None

    result: Optional[object] = None


class DataBrowserActions(BaseModel):
    """Browser actions execution results.

    Present only when browser_actions were specified in the request.
    """

    results: List[DataBrowserActionsResult]

    success: bool

    total_duration: float


class DataNetworkCaptureFilterURL(BaseModel):
    type: Literal["exact", "contains"]

    value: str


class DataNetworkCaptureFilter(BaseModel):
    validation: bool

    wait_for_requests_count: float

    method: Optional[Literal["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]] = None

    resource_type: Union[
        Literal[
            "document",
            "stylesheet",
            "image",
            "media",
            "font",
            "script",
            "texttrack",
            "xhr",
            "fetch",
            "prefetch",
            "eventsource",
            "websocket",
            "manifest",
            "signedexchange",
            "ping",
            "cspviolationreport",
            "preflight",
            "other",
            "fedcm",
        ],
        List[
            Literal[
                "document",
                "stylesheet",
                "image",
                "media",
                "font",
                "script",
                "texttrack",
                "xhr",
                "fetch",
                "prefetch",
                "eventsource",
                "websocket",
                "manifest",
                "signedexchange",
                "ping",
                "cspviolationreport",
                "preflight",
                "other",
                "fedcm",
            ]
        ],
        None,
    ] = None
    """Resource type for network capture filtering"""

    status_code: Union[float, List[float], None] = None

    url: Optional[DataNetworkCaptureFilterURL] = None

    wait_for_requests_count_timeout: Optional[float] = None


class DataNetworkCaptureResultRequest(BaseModel):
    headers: Dict[str, str]

    method: str

    resource_type: Literal[
        "document",
        "stylesheet",
        "image",
        "media",
        "font",
        "script",
        "texttrack",
        "xhr",
        "fetch",
        "prefetch",
        "eventsource",
        "websocket",
        "manifest",
        "signedexchange",
        "ping",
        "cspviolationreport",
        "preflight",
        "other",
        "fedcm",
    ]
    """Resource type for network capture filtering"""

    url: str

    body: Optional[str] = None


class DataNetworkCaptureResultResponse(BaseModel):
    body: str

    headers: Dict[str, str]

    serialization: Literal["none", "base64"]

    status: float

    status_text: str


class DataNetworkCaptureResult(BaseModel):
    request: DataNetworkCaptureResultRequest

    response: DataNetworkCaptureResultResponse


class DataNetworkCapture(BaseModel):
    filter: DataNetworkCaptureFilter

    results: List[DataNetworkCaptureResult]

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)


class DataParsingParsingSuccessResult(BaseModel):
    entities: Dict[str, object]

    status: Literal["success"]


class DataParsingParsingErrorResult(BaseModel):
    error: str

    status: Literal["error"]


DataParsing: TypeAlias = Union[DataParsingParsingSuccessResult, DataParsingParsingErrorResult, Dict[str, object]]


class DataRedirect(BaseModel):
    status_code: float

    url: str


class Data(BaseModel):
    browser_actions: Optional[DataBrowserActions] = None
    """Browser actions execution results.

    Present only when browser_actions were specified in the request.
    """

    cookies: Optional[List[object]] = None
    """The cookies collected from browser actions during the task."""

    eval: Optional[List[object]] = None
    """The evaluation results from browser actions during the task."""

    fetch: Optional[List[object]] = None
    """The http requests from browser actions made during the task."""

    headers: Optional[Dict[str, str]] = None
    """The headers received during the task."""

    html: Optional[str] = None
    """The HTML content of the page."""

    links: Optional[List[str]] = None
    """List of all unique URLs found on the page."""

    markdown: Optional[str] = None
    """The Markdown version of the HTML content."""

    network_capture: Optional[List[DataNetworkCapture]] = None
    """The network capture data collected during the task."""

    pages_html: Optional[List[str]] = None
    """Individual HTML content of each pagination page, before merging."""

    parsing: Optional[DataParsing] = None
    """The parsing results extracted from the HTML & network content."""

    redirects: Optional[List[DataRedirect]] = None
    """The list of redirects that occurred during the task."""

    screenshots: Optional[List[object]] = None
    """
    Screenshots taken during the task, from browser actions, or the screenshot
    format.
    """


class Metadata(BaseModel):
    agent: Optional[str] = None
    """The name of the agent used for the query."""

    driver: Optional[str] = None
    """The driver used for the task."""

    localization_id: Optional[str] = None
    """The localization identifier for the query."""

    query_duration: Optional[float] = None
    """The duration in milliseconds of the query processing."""

    query_time: Optional[str] = None
    """The time when the query was received."""

    response_parameters: Optional[object] = None
    """Additional response parameters."""

    tag: Optional[str] = None
    """A tag associated with the query."""


class Debug(BaseModel):
    performance_metrics: Optional[Dict[str, float]] = None
    """Performance metrics collected during the task."""

    proxy_total_bytes_usage: Optional[float] = None
    """Total bytes used by the proxy during the task."""

    transformed_output: Optional[object] = None
    """The transformed output after applying any transformations."""

    userbrowser: Optional[object] = None
    """The userbrowser instance using during the task."""


class PaginationNextPageParams(BaseModel):
    next_page_params: Dict[str, object]


class PaginationUnionMember1(BaseModel):
    next_page_params: Dict[str, object]


Pagination: TypeAlias = Union[PaginationNextPageParams, List[PaginationUnionMember1]]


class TemplateRunResponse(BaseModel):
    data: Data

    metadata: Metadata

    status: Literal["success", "skipped", "fatal", "error", "postponed", "ignored", "rejected", "blocked"]
    """The status of the task."""

    task_id: str
    """Unique identifier for the task."""

    url: str
    """The final URL."""

    debug: Optional[Debug] = None

    pagination: Optional[Pagination] = None
    """Pagination information if applicable."""

    status_code: Optional[float] = None
    """The HTTP status code of the task."""

    warnings: Optional[List[str]] = None
    """List of warnings generated during the task."""
