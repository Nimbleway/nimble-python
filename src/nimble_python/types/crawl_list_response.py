# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "CrawlListResponse",
    "Data",
    "DataOptions",
    "DataOptionsCallback",
    "DataOptionsCallbackUnionMember0",
    "DataOptionsExtractOptions",
    "DataOptionsExtractOptionsParseOptions",
    "DataOptionsExtractOptionsSession",
    "DataOptionsExtractOptionsBrowser",
    "DataOptionsExtractOptionsBrowserUnionMember1",
    "DataOptionsExtractOptionsCookiesUnionMember0",
    "DataOptionsExtractOptionsMetadata",
    "DataOptionsExtractOptionsNetworkCapture",
    "DataOptionsExtractOptionsNetworkCaptureURL",
    "DataOptionsExtractOptionsQueryTemplate",
    "DataOptionsExtractOptionsQueryTemplatePagination",
    "DataOptionsExtractOptionsQueryTemplatePaginationNextPageParams",
    "DataOptionsExtractOptionsQueryTemplatePaginationUnionMember1",
    "DataOptionsExtractOptionsTemplate",
    "DataOptionsExtractOptionsUserbrowserCreationTemplateRendered",
    "Pagination",
]


class DataOptionsCallbackUnionMember0(BaseModel):
    url: str
    """Webhook URL to receive crawl results."""

    events: Optional[List[Literal["completed", "page", "failed", "started"]]] = None
    """Type of events that should be sent to the webhook URL. (default: all)"""

    headers: Optional[Dict[str, object]] = None
    """Headers to send to the webhook URL."""

    metadata: Optional[Dict[str, object]] = None
    """Custom metadata that will be included in all webhook payloads for this crawl."""


DataOptionsCallback: TypeAlias = Union[DataOptionsCallbackUnionMember0, str]


class DataOptionsExtractOptionsParseOptions(BaseModel):
    """Configuration options for parsing behavior"""

    merge_dynamic: Optional[bool] = None
    """Whether to merge dynamic parsing results with static results"""

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


class DataOptionsExtractOptionsSession(BaseModel):
    prefetch_userbrowser: bool

    retry: bool

    id: Optional[str] = None

    timeout: Optional[float] = None


class DataOptionsExtractOptionsBrowserUnionMember1(BaseModel):
    name: Literal["chrome", "firefox"]

    version: Optional[str] = None
    """Specific browser version to emulate"""


DataOptionsExtractOptionsBrowser: TypeAlias = Union[
    Literal["chrome", "firefox"], DataOptionsExtractOptionsBrowserUnionMember1
]


class DataOptionsExtractOptionsCookiesUnionMember0(BaseModel):
    creation: Optional[str] = None

    domain: Optional[str] = None

    expires: Optional[str] = None

    extensions: Optional[List[str]] = None

    host_only: Optional[bool] = FieldInfo(alias="hostOnly", default=None)

    http_only: Optional[bool] = FieldInfo(alias="httpOnly", default=None)

    last_accessed: Optional[str] = FieldInfo(alias="lastAccessed", default=None)

    max_age: Union[Literal["Infinity", "-Infinity"], float, None] = FieldInfo(alias="maxAge", default=None)

    name: Optional[str] = None

    path: Optional[str] = None

    path_is_default: Optional[bool] = FieldInfo(alias="pathIsDefault", default=None)

    same_site: Optional[Literal["strict", "lax", "none"]] = FieldInfo(alias="sameSite", default=None)

    secure: Optional[bool] = None

    value: Optional[str] = None

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


class DataOptionsExtractOptionsMetadata(BaseModel):
    """Structured metadata about the request execution context"""

    account_name: Optional[str] = None
    """Account name associated with the request"""

    definition_id: Optional[int] = None
    """Definition identifier"""

    definition_name: Optional[str] = None
    """Name of the definition"""

    endpoint: Optional[str] = None
    """API endpoint being called"""

    execution_id: Optional[str] = None
    """Unique identifier for this execution"""

    flowit_task_id: Optional[str] = None
    """FlowIt task identifier"""

    input_id: Optional[str] = None
    """Input data identifier"""

    pipeline_execution_id: Optional[int] = None
    """Identifier for the pipeline execution"""

    query_template_id: Optional[str] = None
    """Query template identifier"""

    source: Optional[str] = None
    """Source system or application making the request"""

    template_id: Optional[int] = None
    """Template identifier"""

    template_name: Optional[str] = None
    """Name of the template"""


class DataOptionsExtractOptionsNetworkCaptureURL(BaseModel):
    type: Literal["exact", "contains"]

    value: str


class DataOptionsExtractOptionsNetworkCapture(BaseModel):
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

    url: Optional[DataOptionsExtractOptionsNetworkCaptureURL] = None

    wait_for_requests_count_timeout: Optional[float] = None


class DataOptionsExtractOptionsQueryTemplatePaginationNextPageParams(BaseModel):
    next_page_params: Dict[str, object]


class DataOptionsExtractOptionsQueryTemplatePaginationUnionMember1(BaseModel):
    next_page_params: Dict[str, object]


DataOptionsExtractOptionsQueryTemplatePagination: TypeAlias = Union[
    DataOptionsExtractOptionsQueryTemplatePaginationNextPageParams,
    List[DataOptionsExtractOptionsQueryTemplatePaginationUnionMember1],
]


class DataOptionsExtractOptionsQueryTemplate(BaseModel):
    """Query template configuration for structured data extraction"""

    id: str

    api_type: Literal["WEB", "SERP", "SOCIAL"]

    pagination: Optional[DataOptionsExtractOptionsQueryTemplatePagination] = None

    params: Optional[Dict[str, object]] = None

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


class DataOptionsExtractOptionsTemplate(BaseModel):
    """Userbrowser creation template configuration"""

    name: str

    params: Optional[Dict[str, object]] = None


class DataOptionsExtractOptionsUserbrowserCreationTemplateRendered(BaseModel):
    """Pre-rendered userbrowser creation template configuration"""

    id: str

    allowed_parameter_names: List[str]

    render_flow_rendered: List[Dict[str, object]]


class DataOptionsExtractOptions(BaseModel):
    country: Literal[
        "AD",
        "AE",
        "AF",
        "AG",
        "AI",
        "AL",
        "AM",
        "AO",
        "AQ",
        "AR",
        "AS",
        "AT",
        "AU",
        "AW",
        "AX",
        "AZ",
        "BA",
        "BB",
        "BD",
        "BE",
        "BF",
        "BG",
        "BH",
        "BI",
        "BJ",
        "BL",
        "BM",
        "BN",
        "BO",
        "BQ",
        "BR",
        "BS",
        "BT",
        "BV",
        "BW",
        "BY",
        "BZ",
        "CA",
        "CC",
        "CD",
        "CF",
        "CG",
        "CH",
        "CI",
        "CK",
        "CL",
        "CM",
        "CN",
        "CO",
        "CR",
        "CU",
        "CV",
        "CW",
        "CX",
        "CY",
        "CZ",
        "DE",
        "DJ",
        "DK",
        "DM",
        "DO",
        "DZ",
        "EC",
        "EE",
        "EG",
        "EH",
        "ER",
        "ES",
        "ET",
        "FI",
        "FJ",
        "FK",
        "FM",
        "FO",
        "FR",
        "GA",
        "GB",
        "GD",
        "GE",
        "GF",
        "GG",
        "GH",
        "GI",
        "GL",
        "GM",
        "GN",
        "GP",
        "GQ",
        "GR",
        "GS",
        "GT",
        "GU",
        "GW",
        "GY",
        "HK",
        "HM",
        "HN",
        "HR",
        "HT",
        "HU",
        "ID",
        "IE",
        "IL",
        "IM",
        "IN",
        "IO",
        "IQ",
        "IR",
        "IS",
        "IT",
        "JE",
        "JM",
        "JO",
        "JP",
        "KE",
        "KG",
        "KH",
        "KI",
        "KM",
        "KN",
        "KP",
        "KR",
        "KW",
        "KY",
        "KZ",
        "LA",
        "LB",
        "LC",
        "LI",
        "LK",
        "LR",
        "LS",
        "LT",
        "LU",
        "LV",
        "LY",
        "MA",
        "MC",
        "MD",
        "ME",
        "MF",
        "MG",
        "MH",
        "MK",
        "ML",
        "MM",
        "MN",
        "MO",
        "MP",
        "MQ",
        "MR",
        "MS",
        "MT",
        "MU",
        "MV",
        "MW",
        "MX",
        "MY",
        "MZ",
        "NA",
        "NC",
        "NE",
        "NF",
        "NG",
        "NI",
        "NL",
        "NO",
        "NP",
        "NR",
        "NU",
        "NZ",
        "OM",
        "PA",
        "PE",
        "PF",
        "PG",
        "PH",
        "PK",
        "PL",
        "PM",
        "PN",
        "PR",
        "PS",
        "PT",
        "PW",
        "PY",
        "QA",
        "RE",
        "RO",
        "RS",
        "RU",
        "RW",
        "SA",
        "SB",
        "SC",
        "SD",
        "SE",
        "SG",
        "SH",
        "SI",
        "SJ",
        "SK",
        "SL",
        "SM",
        "SN",
        "SO",
        "SR",
        "SS",
        "ST",
        "SV",
        "SX",
        "SY",
        "SZ",
        "TC",
        "TD",
        "TF",
        "TG",
        "TH",
        "TJ",
        "TK",
        "TL",
        "TM",
        "TN",
        "TO",
        "TR",
        "TT",
        "TV",
        "TW",
        "TZ",
        "UA",
        "UG",
        "UM",
        "US",
        "UY",
        "UZ",
        "VA",
        "VC",
        "VE",
        "VG",
        "VI",
        "VN",
        "VU",
        "WF",
        "WS",
        "XK",
        "YE",
        "YT",
        "ZA",
        "ZM",
        "ZW",
        "ALL",
    ]
    """Country code for geolocation and proxy selection"""

    debug_options: Dict[str, object]
    """Debug and troubleshooting options for the request"""

    device: Literal["desktop", "mobile", "tablet"]
    """Device type for browser emulation"""

    export_userbrowser: bool
    """Whether to export the userbrowser session"""

    format: Literal["json", "html", "csv", "raw", "json-lines", "markdown"]
    """Response format"""

    headers: Dict[str, Union[str, List[str], None]]
    """Custom HTTP headers to include in the request"""

    http2: bool
    """Whether to use HTTP/2 protocol"""

    is_xhr: bool
    """Whether to emulate XMLHttpRequest behavior"""

    locale: Literal[
        "aa-DJ",
        "aa-ER",
        "aa-ET",
        "af",
        "af-NA",
        "af-ZA",
        "ak",
        "ak-GH",
        "am",
        "am-ET",
        "an-ES",
        "ar",
        "ar-AE",
        "ar-BH",
        "ar-DZ",
        "ar-EG",
        "ar-IN",
        "ar-IQ",
        "ar-JO",
        "ar-KW",
        "ar-LB",
        "ar-LY",
        "ar-MA",
        "ar-OM",
        "ar-QA",
        "ar-SA",
        "ar-SD",
        "ar-SY",
        "ar-TN",
        "ar-YE",
        "as",
        "as-IN",
        "asa",
        "asa-TZ",
        "ast-ES",
        "az",
        "az-AZ",
        "az-Cyrl",
        "az-Cyrl-AZ",
        "az-Latn",
        "az-Latn-AZ",
        "be",
        "be-BY",
        "bem",
        "bem-ZM",
        "ber-DZ",
        "ber-MA",
        "bez",
        "bez-TZ",
        "bg",
        "bg-BG",
        "bho-IN",
        "bm",
        "bm-ML",
        "bn",
        "bn-BD",
        "bn-IN",
        "bo",
        "bo-CN",
        "bo-IN",
        "br-FR",
        "brx-IN",
        "bs",
        "bs-BA",
        "byn-ER",
        "ca",
        "ca-AD",
        "ca-ES",
        "ca-FR",
        "ca-IT",
        "cgg",
        "cgg-UG",
        "chr",
        "chr-US",
        "crh-UA",
        "cs",
        "cs-CZ",
        "csb-PL",
        "cv-RU",
        "cy",
        "cy-GB",
        "da",
        "da-DK",
        "dav",
        "dav-KE",
        "de",
        "de-AT",
        "de-BE",
        "de-CH",
        "de-DE",
        "de-LI",
        "de-LU",
        "dv-MV",
        "dz-BT",
        "ebu",
        "ebu-KE",
        "ee",
        "ee-GH",
        "ee-TG",
        "el",
        "el-CY",
        "el-GR",
        "en",
        "en-AG",
        "en-AS",
        "en-AU",
        "en-BE",
        "en-BW",
        "en-BZ",
        "en-CA",
        "en-DK",
        "en-GB",
        "en-GU",
        "en-HK",
        "en-IE",
        "en-IN",
        "en-JM",
        "en-MH",
        "en-MP",
        "en-MT",
        "en-MU",
        "en-NA",
        "en-NG",
        "en-NZ",
        "en-PH",
        "en-PK",
        "en-SG",
        "en-TT",
        "en-UM",
        "en-US",
        "en-VI",
        "en-ZA",
        "en-ZM",
        "en-ZW",
        "eo",
        "es",
        "es-419",
        "es-AR",
        "es-BO",
        "es-CL",
        "es-CO",
        "es-CR",
        "es-CU",
        "es-DO",
        "es-EC",
        "es-ES",
        "es-GQ",
        "es-GT",
        "es-HN",
        "es-MX",
        "es-NI",
        "es-PA",
        "es-PE",
        "es-PR",
        "es-PY",
        "es-SV",
        "es-US",
        "es-UY",
        "es-VE",
        "et",
        "et-EE",
        "eu",
        "eu-ES",
        "fa",
        "fa-AF",
        "fa-IR",
        "ff",
        "ff-SN",
        "fi",
        "fi-FI",
        "fil",
        "fil-PH",
        "fo",
        "fo-FO",
        "fr",
        "fr-BE",
        "fr-BF",
        "fr-BI",
        "fr-BJ",
        "fr-BL",
        "fr-CA",
        "fr-CD",
        "fr-CF",
        "fr-CG",
        "fr-CH",
        "fr-CI",
        "fr-CM",
        "fr-DJ",
        "fr-FR",
        "fr-GA",
        "fr-GN",
        "fr-GP",
        "fr-GQ",
        "fr-KM",
        "fr-LU",
        "fr-MC",
        "fr-MF",
        "fr-MG",
        "fr-ML",
        "fr-MQ",
        "fr-NE",
        "fr-RE",
        "fr-RW",
        "fr-SN",
        "fr-TD",
        "fr-TG",
        "fur-IT",
        "fy-DE",
        "fy-NL",
        "ga",
        "ga-IE",
        "gd-GB",
        "gez-ER",
        "gez-ET",
        "gl",
        "gl-ES",
        "gsw",
        "gsw-CH",
        "gu",
        "gu-IN",
        "guz",
        "guz-KE",
        "gv",
        "gv-GB",
        "ha",
        "ha-Latn",
        "ha-Latn-GH",
        "ha-Latn-NE",
        "ha-Latn-NG",
        "ha-NG",
        "haw",
        "haw-US",
        "he",
        "he-IL",
        "hi",
        "hi-IN",
        "hne-IN",
        "hr",
        "hr-HR",
        "hsb-DE",
        "ht-HT",
        "hu",
        "hu-HU",
        "hy",
        "hy-AM",
        "id",
        "id-ID",
        "ig",
        "ig-NG",
        "ii",
        "ii-CN",
        "ik-CA",
        "is",
        "is-IS",
        "it",
        "it-CH",
        "it-IT",
        "iu-CA",
        "iw-IL",
        "ja",
        "ja-JP",
        "jmc",
        "jmc-TZ",
        "ka",
        "ka-GE",
        "kab",
        "kab-DZ",
        "kam",
        "kam-KE",
        "kde",
        "kde-TZ",
        "kea",
        "kea-CV",
        "khq",
        "khq-ML",
        "ki",
        "ki-KE",
        "kk",
        "kk-Cyrl",
        "kk-Cyrl-KZ",
        "kk-KZ",
        "kl",
        "kl-GL",
        "kln",
        "kln-KE",
        "km",
        "km-KH",
        "kn",
        "kn-IN",
        "ko",
        "ko-KR",
        "kok",
        "kok-IN",
        "ks-IN",
        "ku-TR",
        "kw",
        "kw-GB",
        "ky-KG",
        "lag",
        "lag-TZ",
        "lb-LU",
        "lg",
        "lg-UG",
        "li-BE",
        "li-NL",
        "lij-IT",
        "lo-LA",
        "lt",
        "lt-LT",
        "luo",
        "luo-KE",
        "luy",
        "luy-KE",
        "lv",
        "lv-LV",
        "mag-IN",
        "mai-IN",
        "mas",
        "mas-KE",
        "mas-TZ",
        "mer",
        "mer-KE",
        "mfe",
        "mfe-MU",
        "mg",
        "mg-MG",
        "mhr-RU",
        "mi-NZ",
        "mk",
        "mk-MK",
        "ml",
        "ml-IN",
        "mn-MN",
        "mr",
        "mr-IN",
        "ms",
        "ms-BN",
        "ms-MY",
        "mt",
        "mt-MT",
        "my",
        "my-MM",
        "nan-TW",
        "naq",
        "naq-NA",
        "nb",
        "nb-NO",
        "nd",
        "nd-ZW",
        "nds-DE",
        "nds-NL",
        "ne",
        "ne-IN",
        "ne-NP",
        "nl",
        "nl-AW",
        "nl-BE",
        "nl-NL",
        "nn",
        "nn-NO",
        "nr-ZA",
        "nso-ZA",
        "nyn",
        "nyn-UG",
        "oc-FR",
        "om",
        "om-ET",
        "om-KE",
        "or",
        "or-IN",
        "os-RU",
        "pa",
        "pa-Arab",
        "pa-Arab-PK",
        "pa-Guru",
        "pa-Guru-IN",
        "pa-IN",
        "pa-PK",
        "pap-AN",
        "pl",
        "pl-PL",
        "ps",
        "ps-AF",
        "pt",
        "pt-BR",
        "pt-GW",
        "pt-MZ",
        "pt-PT",
        "rm",
        "rm-CH",
        "ro",
        "ro-MD",
        "ro-RO",
        "rof",
        "rof-TZ",
        "ru",
        "ru-MD",
        "ru-RU",
        "ru-UA",
        "rw",
        "rw-RW",
        "rwk",
        "rwk-TZ",
        "sa-IN",
        "saq",
        "saq-KE",
        "sc-IT",
        "sd-IN",
        "se-NO",
        "seh",
        "seh-MZ",
        "ses",
        "ses-ML",
        "sg",
        "sg-CF",
        "shi",
        "shi-Latn",
        "shi-Latn-MA",
        "shi-Tfng",
        "shi-Tfng-MA",
        "shs-CA",
        "si",
        "si-LK",
        "sid-ET",
        "sk",
        "sk-SK",
        "sl",
        "sl-SI",
        "sn",
        "sn-ZW",
        "so",
        "so-DJ",
        "so-ET",
        "so-KE",
        "so-SO",
        "sq",
        "sq-AL",
        "sq-MK",
        "sr",
        "sr-Cyrl",
        "sr-Cyrl-BA",
        "sr-Cyrl-ME",
        "sr-Cyrl-RS",
        "sr-Latn",
        "sr-Latn-BA",
        "sr-Latn-ME",
        "sr-Latn-RS",
        "sr-ME",
        "sr-RS",
        "ss-ZA",
        "st-ZA",
        "sv",
        "sv-FI",
        "sv-SE",
        "sw",
        "sw-KE",
        "sw-TZ",
        "ta",
        "ta-IN",
        "ta-LK",
        "te",
        "te-IN",
        "teo",
        "teo-KE",
        "teo-UG",
        "tg-TJ",
        "th",
        "th-TH",
        "ti",
        "ti-ER",
        "ti-ET",
        "tig-ER",
        "tk-TM",
        "tl-PH",
        "tn-ZA",
        "to",
        "to-TO",
        "tr",
        "tr-CY",
        "tr-TR",
        "ts-ZA",
        "tt-RU",
        "tzm",
        "tzm-Latn",
        "tzm-Latn-MA",
        "ug-CN",
        "uk",
        "uk-UA",
        "unm-US",
        "ur",
        "ur-IN",
        "ur-PK",
        "uz",
        "uz-Arab",
        "uz-Arab-AF",
        "uz-Cyrl",
        "uz-Cyrl-UZ",
        "uz-Latn",
        "uz-Latn-UZ",
        "uz-UZ",
        "ve-ZA",
        "vi",
        "vi-VN",
        "vun",
        "vun-TZ",
        "wa-BE",
        "wae-CH",
        "wal-ET",
        "wo-SN",
        "xh-ZA",
        "xog",
        "xog-UG",
        "yi-US",
        "yo",
        "yo-NG",
        "yue-HK",
        "zh",
        "zh-CN",
        "zh-HK",
        "zh-Hans",
        "zh-Hans-CN",
        "zh-Hans-HK",
        "zh-Hans-MO",
        "zh-Hans-SG",
        "zh-Hant",
        "zh-Hant-HK",
        "zh-Hant-MO",
        "zh-Hant-TW",
        "zh-SG",
        "zh-TW",
        "zu",
        "zu-ZA",
        "auto",
    ]
    """Locale for browser language and region settings"""

    method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"]
    """HTTP method for the request"""

    no_html: bool
    """Whether to exclude HTML from the response"""

    parse: bool
    """Whether to parse the response content"""

    parse_options: DataOptionsExtractOptionsParseOptions
    """Configuration options for parsing behavior"""

    proxy_provider: Literal[
        "brightdata",
        "oxylabs",
        "smartproxy",
        "proxit",
        "proxit_preprod",
        "local",
        "rayobyte",
        "always",
        "oculusproxies",
        "froxy",
        "packetstream",
        "911proxy",
        "direct911proxy",
        "thesocialproxy",
        "thesocialproxy2",
        "nimble-isp",
        "nimble-isp-mobile",
        "proxit-linux",
        "proxit-macos",
        "proxit-windows",
        "proxit-rental",
        "ipfoxy",
        "brightup",
        "research",
    ]
    """Proxy provider to use for the request"""

    raw_headers: bool
    """Whether to return raw HTTP headers in response"""

    save_userbrowser: bool
    """Whether to save the userbrowser session for reuse"""

    session: DataOptionsExtractOptionsSession

    type: str
    """Type of query or scraping template"""

    url: str
    """Target URL to scrape"""

    browser: Optional[DataOptionsExtractOptionsBrowser] = None
    """Browser type to emulate"""

    city: Optional[str] = None
    """City for geolocation"""

    client_timeout: Optional[float] = None
    """Client-side timeout in milliseconds"""

    consent_header: Optional[bool] = None
    """Whether to automatically handle cookie consent headers"""

    cookies: Union[List[DataOptionsExtractOptionsCookiesUnionMember0], str, None] = None
    """Browser cookies as array of cookie objects"""

    disable_ip_check: Optional[bool] = None
    """Whether to disable IP address validation"""

    driver: Optional[Literal["vx6", "vx8", "vx8-pro", "vx10", "vx10-pro", "vx12", "vx12-pro"]] = None
    """Browser driver to use"""

    dynamic_parser: Optional[Dict[str, object]] = None
    """Custom parser configuration as a key-value map"""

    expected_status_codes: Optional[List[int]] = None
    """Expected HTTP status codes for successful requests"""

    ip6: Optional[bool] = None
    """Whether to use IPv6 for the request"""

    markdown: Optional[bool] = None
    """Whether to return response in Markdown format"""

    metadata: Optional[DataOptionsExtractOptionsMetadata] = None
    """Structured metadata about the request execution context"""

    native_mode: Optional[Literal["requester", "apm", "direct"]] = None
    """Native execution mode"""

    network_capture: Optional[List[DataOptionsExtractOptionsNetworkCapture]] = None
    """Filters for capturing network traffic"""

    no_userbrowser: Optional[bool] = None
    """Whether to disable browser-based rendering"""

    os: Optional[Literal["windows", "mac os", "linux", "android", "ios"]] = None
    """Operating system to emulate"""

    parser: Union[Dict[str, object], str, None] = None
    """Custom parser configuration as a key-value map"""

    proxy_providers: Optional[Dict[str, float]] = None
    """Weighted distribution of proxy providers"""

    query_template: Optional[DataOptionsExtractOptionsQueryTemplate] = None
    """Query template configuration for structured data extraction"""

    referrer_type: Optional[
        Literal["random", "no-referer", "same-origin", "google", "bing", "facebook", "twitter", "instagram"]
    ] = None
    """Referrer policy for the request"""

    render: Optional[bool] = None
    """Whether to render JavaScript content using a browser"""

    render_flow: Optional[List[Dict[str, object]]] = None
    """Array of actions to perform during browser rendering"""

    render_options: Optional[Dict[str, object]] = None

    request_timeout: Optional[float] = None
    """Request timeout in milliseconds"""

    return_response_headers_as_header: Optional[bool] = None
    """Whether to return response headers in HTTP headers"""

    skill: Union[str, List[str], None] = None
    """Skills or capabilities required for the request"""

    skip_ubct: Optional[bool] = None
    """Whether to skip userbrowser creation template processing"""

    state: Optional[
        Literal[
            "AL",
            "AK",
            "AS",
            "AZ",
            "AR",
            "CA",
            "CO",
            "CT",
            "DE",
            "DC",
            "FL",
            "GA",
            "GU",
            "HI",
            "ID",
            "IL",
            "IN",
            "IA",
            "KS",
            "KY",
            "LA",
            "ME",
            "MD",
            "MA",
            "MI",
            "MN",
            "MS",
            "MO",
            "MT",
            "NE",
            "NV",
            "NH",
            "NJ",
            "NM",
            "NY",
            "NC",
            "ND",
            "MP",
            "OH",
            "OK",
            "OR",
            "PA",
            "PR",
            "RI",
            "SC",
            "SD",
            "TN",
            "TX",
            "UT",
            "VT",
            "VA",
            "VI",
            "WA",
            "WV",
            "WI",
            "WY",
        ]
    ] = None
    """US state for geolocation (only valid when country is US)"""

    tag: Optional[str] = None
    """User-defined tag for request identification"""

    template: Optional[DataOptionsExtractOptionsTemplate] = None
    """Userbrowser creation template configuration"""

    userbrowser_creation_template_rendered: Optional[DataOptionsExtractOptionsUserbrowserCreationTemplateRendered] = (
        None
    )
    """Pre-rendered userbrowser creation template configuration"""


class DataOptions(BaseModel):
    allow_external_links: bool
    """Allows the crawler to follow links to external websites."""

    allow_subdomains: bool
    """Allows the crawler to follow links to subdomains of the main domain."""

    crawl_entire_domain: bool
    """
    Allows the crawler to follow internal links to sibling or parent URLs, not just
    child paths.
    """

    ignore_query_parameters: bool
    """Do not re-scrape the same path with different (or none) query parameters."""

    limit: int
    """Maximum number of pages to crawl."""

    max_discovery_depth: int
    """Maximum depth to crawl based on discovery order."""

    sitemap: Literal["skip", "include", "only"]
    """Sitemap and other methods will be used together to find URLs."""

    url: str
    """Url to crawl."""

    callback: Optional[DataOptionsCallback] = None
    """Webhook configuration for receiving crawl results."""

    exclude_paths: Optional[List[str]] = None
    """URL pathname regex patterns that exclude matching URLs from the crawl."""

    extract_options: Optional[DataOptionsExtractOptions] = None

    include_paths: Optional[List[str]] = None
    """URL pathname regex patterns that include matching URLs in the crawl."""

    name: Optional[str] = None
    """Name of the crawl."""


class Data(BaseModel):
    id: str

    account_name: str = FieldInfo(alias="accountName")

    options: DataOptions

    url: str


class Pagination(BaseModel):
    has_next: bool = FieldInfo(alias="hasNext")

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)

    total: float


class CrawlListResponse(BaseModel):
    """Successful get crawl response"""

    data: List[Data]

    pagination: Pagination
