# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared_params.eval_action import EvalAction
from .shared_params.fill_action import FillAction
from .shared_params.goto_action import GotoAction
from .shared_params.wait_action import WaitAction
from .shared_params.click_action import ClickAction
from .shared_params.fetch_action import FetchAction
from .shared_params.press_action import PressAction
from .shared_params.scroll_action import ScrollAction
from .shared_params.screenshot_action import ScreenshotAction
from .shared_params.auto_scroll_action import AutoScrollAction
from .shared_params.get_cookies_action import GetCookiesAction
from .shared_params.wait_for_element_action import WaitForElementAction
from .shared_params.wait_for_navigation_action import WaitForNavigationAction

__all__ = [
    "ExtractAsyncParams",
    "Browser",
    "BrowserUnionMember1",
    "BrowserAction",
    "CookiesUnionMember0",
    "NetworkCapture",
    "NetworkCaptureURL",
    "Session",
]


class ExtractAsyncParams(TypedDict, total=False):
    url: Required[str]
    """Target URL to scrape"""

    auto_driver_configuration: Dict[str, int]
    """
    Custom flow for the optimization engine: maps candidate names to the number of
    attempts to spend on each candidate before advancing (0 skips it). Key order
    defines the flow order. Providing it opts the request into 'auto' driver
    selection.
    """

    body: object
    """Request body for POST, PUT, PATCH methods"""

    browser: Browser
    """Browser type to emulate"""

    browser_actions: Iterable[BrowserAction]
    """Array of browser automation actions to execute sequentially"""

    callback_url: str
    """URL to call back when async operation completes"""

    city: str
    """City for geolocation"""

    consent_header: bool
    """Whether to automatically handle cookie consent headers"""

    cookies: Union[Iterable[CookiesUnionMember0], str]
    """Browser cookies as array of cookie objects"""

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

    device: Literal["desktop", "mobile", "tablet"]
    """Device type for browser emulation"""

    driver: Literal["auto", "vx6", "vx8", "vx8-pro", "vx10", "vx10-pro", "vx12", "vx12-pro", "media-vx6", "fast-vx6"]
    """Browser driver to use"""

    expected_status_codes: Iterable[int]
    """Expected HTTP status codes for successful requests"""

    formats: List[Literal["html", "markdown", "screenshot", "headers", "links"]]
    """List of acceptable response formats in order of preference"""

    headers: Dict[str, Union[str, SequenceNotStr[str], None]]
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

    markdown_backend: Literal["full_page", "main_content"]
    """Selects which markdown conversion strategy to use.

    "full_page" converts the entire HTML page. "main_content" uses Mozilla
    Readability to extract the main article content before converting.
    """

    method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"]
    """HTTP method for the request"""

    network_capture: Iterable[NetworkCapture]
    """Filters for capturing network traffic"""

    os: Literal["windows", "mac os", "linux", "android", "ios"]
    """Operating system to emulate"""

    parse: bool
    """Whether to parse the response content"""

    parser: Union[Dict[str, object], str]
    """Custom parser configuration as a key-value map"""

    realtime_total_timeout: float
    """Overall deadline in milliseconds for a realtime request.

    Clamped to the account total timeout — it can shorten the deadline but never
    extend it. Has no effect on async requests.
    """

    referrer_type: Literal["random", "no-referer", "same-origin", "google", "bing", "facebook", "twitter", "instagram"]
    """Referrer policy for the request"""

    render: Union[bool, Literal["auto"]]
    """Whether to render JavaScript content using a browser"""

    request_timeout: float
    """Request timeout in milliseconds"""

    session: Session

    skill: Union[str, SequenceNotStr[str]]
    """Skills or capabilities required for the request"""

    state: Literal[
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
    """US state for geolocation (only valid when country is US)"""

    storage_compress: bool
    """Whether to compress stored data"""

    storage_object_name: str
    """Custom name for the stored object"""

    storage_type: str
    """Type of storage to use for results"""

    storage_url: str
    """URL for storage location"""

    tag: str
    """User-defined tag for request identification"""


class BrowserUnionMember1(TypedDict, total=False):
    name: Required[Literal["chrome", "firefox"]]

    version: str
    """Specific browser version to emulate"""


Browser: TypeAlias = Union[Literal["chrome", "firefox"], BrowserUnionMember1]

BrowserAction: TypeAlias = Union[
    AutoScrollAction,
    ClickAction,
    EvalAction,
    FetchAction,
    FillAction,
    GetCookiesAction,
    GotoAction,
    PressAction,
    ScreenshotAction,
    ScrollAction,
    WaitAction,
    WaitForElementAction,
    WaitForNavigationAction,
]


class CookiesUnionMember0(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    creation: Optional[str]

    domain: Optional[str]

    expires: str

    extensions: Optional[SequenceNotStr[str]]

    host_only: Annotated[Optional[bool], PropertyInfo(alias="hostOnly")]

    http_only: Annotated[Optional[bool], PropertyInfo(alias="httpOnly")]

    last_accessed: Annotated[Optional[str], PropertyInfo(alias="lastAccessed")]

    max_age: Annotated[Union[Literal["Infinity", "-Infinity"], float, None], PropertyInfo(alias="maxAge")]

    name: str

    path: Optional[str]

    path_is_default: Annotated[Optional[bool], PropertyInfo(alias="pathIsDefault")]

    same_site: Annotated[Literal["strict", "lax", "none"], PropertyInfo(alias="sameSite")]

    secure: bool

    value: str


class NetworkCaptureURL(TypedDict, total=False):
    value: Required[str]

    type: Literal["exact", "contains"]


class NetworkCapture(TypedDict, total=False):
    method: Literal["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]

    resource_type: Union[str, SequenceNotStr[str]]
    """Resource type for network capture filtering"""

    status_code: Union[float, Iterable[float]]

    url: NetworkCaptureURL

    validation: bool

    wait_for_requests_count: float

    wait_for_requests_count_timeout: float


class Session(TypedDict, total=False):
    id: str

    prefetch_userbrowser: bool

    renew_on_blocked: bool

    retry: bool

    timeout: float
