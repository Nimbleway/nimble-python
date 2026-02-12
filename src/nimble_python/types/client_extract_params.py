# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "ClientExtractParams",
    "Browser",
    "BrowserUnionMember1",
    "BrowserAction",
    "BrowserActionAutoScrollAction",
    "BrowserActionAutoScrollActionAutoScroll",
    "BrowserActionAutoScrollActionAutoScrollUnionMember3",
    "BrowserActionClickAction",
    "BrowserActionClickActionClick",
    "BrowserActionClickActionClickUnionMember2",
    "BrowserActionEvalAction",
    "BrowserActionEvalActionEval",
    "BrowserActionEvalActionEvalUnionMember1",
    "BrowserActionFetchAction",
    "BrowserActionFetchActionFetch",
    "BrowserActionFetchActionFetchUnionMember1",
    "BrowserActionFillAction",
    "BrowserActionFillActionFill",
    "BrowserActionFillActionFillType",
    "BrowserActionFillActionFillPaste",
    "BrowserActionGetCookiesAction",
    "BrowserActionGetCookiesActionGetCookies",
    "BrowserActionGetCookiesActionGetCookiesUnionMember1",
    "BrowserActionGotoAction",
    "BrowserActionGotoActionGoto",
    "BrowserActionGotoActionGotoUnionMember1",
    "BrowserActionPressAction",
    "BrowserActionPressActionPress",
    "BrowserActionPressActionPressUnionMember1",
    "BrowserActionScreenshotAction",
    "BrowserActionScreenshotActionScreenshot",
    "BrowserActionScreenshotActionScreenshotUnionMember1",
    "BrowserActionScrollAction",
    "BrowserActionScrollActionScroll",
    "BrowserActionScrollActionScrollUnionMember2",
    "BrowserActionWaitAction",
    "BrowserActionWaitActionWait",
    "BrowserActionWaitActionWaitUnionMember2",
    "BrowserActionWaitForElementAction",
    "BrowserActionWaitForElementActionWaitForElement",
    "BrowserActionWaitForElementActionWaitForElementUnionMember2",
    "BrowserActionWaitForNavigationAction",
    "BrowserActionWaitForNavigationActionWaitForNavigation",
    "BrowserActionWaitForNavigationActionWaitForNavigationUnionMember1",
    "CookiesUnionMember0",
    "Metadata",
    "NetworkCapture",
    "NetworkCaptureURL",
    "QueryTemplate",
    "QueryTemplatePagination",
    "QueryTemplatePaginationNextPageParams",
    "QueryTemplatePaginationUnionMember1",
    "RenderOptions",
    "RenderOptionsHackiumConfiguration",
    "Session",
    "Template",
    "UserbrowserCreationTemplateRendered",
]


class ClientExtractParams(TypedDict, total=False):
    url: Required[str]
    """Target URL to scrape"""

    browser: Browser
    """Browser type to emulate"""

    browser_actions: Iterable[BrowserAction]
    """Array of browser automation actions to execute sequentially"""

    city: str
    """City for geolocation"""

    client_timeout: float
    """Client-side timeout in milliseconds"""

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

    disable_ip_check: bool
    """Whether to disable IP address validation"""

    driver: Literal["vx6", "vx8", "vx8-pro", "vx10", "vx10-pro", "vx12", "vx12-pro"]
    """Browser driver to use"""

    expected_status_codes: Iterable[int]
    """Expected HTTP status codes for successful requests"""

    formats: List[Literal["html", "markdown"]]
    """List of acceptable response formats in order of preference"""

    headers: Dict[str, Union[str, SequenceNotStr[str], None]]
    """Custom HTTP headers to include in the request"""

    http2: bool
    """Whether to use HTTP/2 protocol"""

    ip6: bool
    """Whether to use IPv6 for the request"""

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

    metadata: Metadata
    """Structured metadata about the request execution context"""

    method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"]
    """HTTP method for the request"""

    native_mode: Literal["requester", "apm", "direct"]
    """Native execution mode"""

    network_capture: Iterable[NetworkCapture]
    """Filters for capturing network traffic"""

    no_userbrowser: bool
    """Whether to disable browser-based rendering"""

    os: Literal["windows", "mac os", "linux", "android", "ios"]
    """Operating system to emulate"""

    parse: bool
    """Whether to parse the response content"""

    parser: Union[Dict[str, object], str]
    """Custom parser configuration as a key-value map"""

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

    proxy_providers: Dict[str, float]
    """Weighted distribution of proxy providers"""

    query_template: QueryTemplate
    """Query template configuration for structured data extraction"""

    raw_headers: bool
    """Whether to return raw HTTP headers in response"""

    referrer_type: Literal["random", "no-referer", "same-origin", "google", "bing", "facebook", "twitter", "instagram"]
    """Referrer policy for the request"""

    render: bool
    """Whether to render JavaScript content using a browser"""

    render_flow: Iterable[Dict[str, object]]
    """Array of actions to perform during browser rendering"""

    render_options: RenderOptions

    request_timeout: float
    """Request timeout in milliseconds"""

    save_userbrowser: bool
    """Whether to save the userbrowser session for reuse"""

    session: Session

    skill: Union[str, SequenceNotStr[str]]
    """Skills or capabilities required for the request"""

    skip_ubct: bool
    """Whether to skip userbrowser creation template processing"""

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

    tag: str
    """User-defined tag for request identification"""

    template: Template
    """Userbrowser creation template configuration"""

    type: str
    """Type of query or scraping template"""

    userbrowser_creation_template_rendered: UserbrowserCreationTemplateRendered
    """Pre-rendered userbrowser creation template configuration"""


class BrowserUnionMember1(TypedDict, total=False):
    name: Required[Literal["chrome", "firefox"]]

    version: str
    """Specific browser version to emulate"""


Browser: TypeAlias = Union[Literal["chrome", "firefox"], BrowserUnionMember1]


class BrowserActionAutoScrollActionAutoScrollUnionMember3(TypedDict, total=False):
    click_selector: Union[str, SequenceNotStr[str]]
    """CSS selector or array of alternative selectors.

    Use an array when you have multiple possible selectors for the same element.
    """

    container: Union[str, SequenceNotStr[str]]
    """CSS selector or array of alternative selectors.

    Use an array when you have multiple possible selectors for the same element.
    """

    delay_after_scroll: Union[float, str]
    """Duration value that accepts various formats.

    Supports: number (ms), string ("1000"), or string with unit ("2s", "500ms",
    "2m", "1h")
    """

    idle_timeout: Union[float, str]
    """Duration value that accepts various formats.

    Supports: number (ms), string ("1000"), or string with unit ("2s", "500ms",
    "2m", "1h")
    """

    loading_selector: Union[str, SequenceNotStr[str]]
    """CSS selector or array of alternative selectors.

    Use an array when you have multiple possible selectors for the same element.
    """

    max_duration: Union[float, str]
    """Duration value that accepts various formats.

    Supports: number (ms), string ("1000"), or string with unit ("2s", "500ms",
    "2m", "1h")
    """

    pause_on_selector: Union[str, SequenceNotStr[str]]
    """CSS selector or array of alternative selectors.

    Use an array when you have multiple possible selectors for the same element.
    """

    required: Union[Literal["true", "false"], bool]
    """Whether this action is required.

    If true, pipeline stops on failure. Accepts boolean or string "true"/"false".
    Default: true.
    """

    skip: Union[Literal["true", "false"], bool]
    """Whether to skip this action.

    Accepts boolean or string "true"/"false". Default: false.
    """

    step_size: float


BrowserActionAutoScrollActionAutoScroll: TypeAlias = Union[
    bool, float, str, BrowserActionAutoScrollActionAutoScrollUnionMember3
]


class BrowserActionAutoScrollAction(TypedDict, total=False):
    """Continuously scroll to load dynamic content"""

    auto_scroll: Required[BrowserActionAutoScrollActionAutoScroll]


class BrowserActionClickActionClickUnionMember2(TypedDict, total=False):
    selector: Required[Union[str, SequenceNotStr[str]]]
    """CSS selector or array of alternative selectors.

    Use an array when you have multiple possible selectors for the same element.
    """

    count: float

    delay: Union[float, str]
    """Duration value that accepts various formats.

    Supports: number (ms), string ("1000"), or string with unit ("2s", "500ms",
    "2m", "1h")
    """

    offset_x: int

    offset_y: int

    required: Union[Literal["true", "false"], bool]
    """Whether this action is required.

    If true, pipeline stops on failure. Accepts boolean or string "true"/"false".
    Default: true.
    """

    scroll: bool

    skip: Union[Literal["true", "false"], bool]
    """Whether to skip this action.

    Accepts boolean or string "true"/"false". Default: false.
    """

    steps: float

    strategy: Literal["linear", "ghost-cursor", "windmouse"]

    timeout: float
    """Timeout in milliseconds.

    Set to 0 for infinite timeout (no timeout). Default: 15000ms.
    """

    visible: bool


BrowserActionClickActionClick: TypeAlias = Union[str, SequenceNotStr[str], BrowserActionClickActionClickUnionMember2]


class BrowserActionClickAction(TypedDict, total=False):
    """Click on an element by selector"""

    click: Required[BrowserActionClickActionClick]


class BrowserActionEvalActionEvalUnionMember1(TypedDict, total=False):
    code: Required[str]

    required: Union[Literal["true", "false"], bool]
    """Whether this action is required.

    If true, pipeline stops on failure. Accepts boolean or string "true"/"false".
    Default: true.
    """

    skip: Union[Literal["true", "false"], bool]
    """Whether to skip this action.

    Accepts boolean or string "true"/"false". Default: false.
    """

    timeout: float
    """Timeout in milliseconds.

    Set to 0 for infinite timeout (no timeout). Default: 15000ms.
    """


BrowserActionEvalActionEval: TypeAlias = Union[str, BrowserActionEvalActionEvalUnionMember1]


class BrowserActionEvalAction(TypedDict, total=False):
    """Execute JavaScript code in page context"""

    eval: Required[BrowserActionEvalActionEval]


class BrowserActionFetchActionFetchUnionMember1(TypedDict, total=False):
    url: Required[str]

    body: str

    headers: Dict[str, str]

    method: Literal["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]

    required: Union[Literal["true", "false"], bool]
    """Whether this action is required.

    If true, pipeline stops on failure. Accepts boolean or string "true"/"false".
    Default: true.
    """

    skip: Union[Literal["true", "false"], bool]
    """Whether to skip this action.

    Accepts boolean or string "true"/"false". Default: false.
    """

    timeout: float
    """Timeout in milliseconds.

    Set to 0 for infinite timeout (no timeout). Default: 15000ms.
    """


BrowserActionFetchActionFetch: TypeAlias = Union[str, BrowserActionFetchActionFetchUnionMember1]


class BrowserActionFetchAction(TypedDict, total=False):
    """Make an HTTP request in browser context"""

    fetch: Required[BrowserActionFetchActionFetch]


class BrowserActionFillActionFillType(TypedDict, total=False):
    selector: Required[Union[str, SequenceNotStr[str]]]
    """CSS selector or array of alternative selectors.

    Use an array when you have multiple possible selectors for the same element.
    """

    value: Required[str]

    click_on_element: bool

    delay: Union[float, str]
    """Duration value that accepts various formats.

    Supports: number (ms), string ("1000"), or string with unit ("2s", "500ms",
    "2m", "1h")
    """

    mode: Literal["type"]

    mouse_movement_strategy: Literal["linear", "ghost-cursor", "windmouse"]

    required: Union[Literal["true", "false"], bool]
    """Whether this action is required.

    If true, pipeline stops on failure. Accepts boolean or string "true"/"false".
    Default: true.
    """

    scroll: bool

    skip: Union[Literal["true", "false"], bool]
    """Whether to skip this action.

    Accepts boolean or string "true"/"false". Default: false.
    """

    timeout: float
    """Timeout in milliseconds.

    Set to 0 for infinite timeout (no timeout). Default: 15000ms.
    """

    typing_interval: Union[float, str]
    """Duration value that accepts various formats.

    Supports: number (ms), string ("1000"), or string with unit ("2s", "500ms",
    "2m", "1h")
    """

    typing_strategy: Literal["simple", "distribution"]

    visible: bool


class BrowserActionFillActionFillPaste(TypedDict, total=False):
    mode: Required[Literal["paste"]]

    selector: Required[Union[str, SequenceNotStr[str]]]
    """CSS selector or array of alternative selectors.

    Use an array when you have multiple possible selectors for the same element.
    """

    value: Required[str]

    click_on_element: bool

    delay: Union[float, str]
    """Duration value that accepts various formats.

    Supports: number (ms), string ("1000"), or string with unit ("2s", "500ms",
    "2m", "1h")
    """

    required: Union[Literal["true", "false"], bool]
    """Whether this action is required.

    If true, pipeline stops on failure. Accepts boolean or string "true"/"false".
    Default: true.
    """

    scroll: bool

    skip: Union[Literal["true", "false"], bool]
    """Whether to skip this action.

    Accepts boolean or string "true"/"false". Default: false.
    """

    timeout: float
    """Timeout in milliseconds.

    Set to 0 for infinite timeout (no timeout). Default: 15000ms.
    """

    visible: bool


BrowserActionFillActionFill: TypeAlias = Union[BrowserActionFillActionFillType, BrowserActionFillActionFillPaste]


class BrowserActionFillAction(TypedDict, total=False):
    """Fill text into an input field"""

    fill: Required[BrowserActionFillActionFill]
    """Fill options with mode-specific fields.

    Use "type" mode for behavioral typing simulation, or "paste" mode for instant
    paste.
    """


class BrowserActionGetCookiesActionGetCookiesUnionMember1Typed(TypedDict, total=False):
    required: Union[Literal["true", "false"], bool]
    """Whether this action is required.

    If true, pipeline stops on failure. Accepts boolean or string "true"/"false".
    Default: true.
    """

    skip: Union[Literal["true", "false"], bool]
    """Whether to skip this action.

    Accepts boolean or string "true"/"false". Default: false.
    """


BrowserActionGetCookiesActionGetCookiesUnionMember1: TypeAlias = Union[
    BrowserActionGetCookiesActionGetCookiesUnionMember1Typed, Dict[str, object]
]

BrowserActionGetCookiesActionGetCookies: TypeAlias = Union[bool, BrowserActionGetCookiesActionGetCookiesUnionMember1]


class BrowserActionGetCookiesAction(TypedDict, total=False):
    """Retrieve browser cookies"""

    get_cookies: Required[BrowserActionGetCookiesActionGetCookies]


class BrowserActionGotoActionGotoUnionMember1(TypedDict, total=False):
    url: Required[str]

    referer: str

    required: Union[Literal["true", "false"], bool]
    """Whether this action is required.

    If true, pipeline stops on failure. Accepts boolean or string "true"/"false".
    Default: true.
    """

    skip: Union[Literal["true", "false"], bool]
    """Whether to skip this action.

    Accepts boolean or string "true"/"false". Default: false.
    """

    timeout: float
    """Timeout in milliseconds.

    Set to 0 for infinite timeout (no timeout). Default: 15000ms.
    """

    wait_until: Literal["load", "domcontentloaded", "networkidle0", "networkidle2"]


BrowserActionGotoActionGoto: TypeAlias = Union[str, BrowserActionGotoActionGotoUnionMember1]


class BrowserActionGotoAction(TypedDict, total=False):
    """Navigate to a URL"""

    goto: Required[BrowserActionGotoActionGoto]


class BrowserActionPressActionPressUnionMember1(TypedDict, total=False):
    key: Required[
        Literal[
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "Power",
            "Eject",
            "Abort",
            "Help",
            "Backspace",
            "Tab",
            "Numpad5",
            "NumpadEnter",
            "Enter",
            "\r",
            "\n",
            "ShiftLeft",
            "ShiftRight",
            "ControlLeft",
            "ControlRight",
            "AltLeft",
            "AltRight",
            "Pause",
            "CapsLock",
            "Escape",
            "Convert",
            "NonConvert",
            "Space",
            "Numpad9",
            "PageUp",
            "Numpad3",
            "PageDown",
            "End",
            "Numpad1",
            "Home",
            "Numpad7",
            "ArrowLeft",
            "Numpad4",
            "Numpad8",
            "ArrowUp",
            "ArrowRight",
            "Numpad6",
            "Numpad2",
            "ArrowDown",
            "Select",
            "Open",
            "PrintScreen",
            "Insert",
            "Numpad0",
            "Delete",
            "NumpadDecimal",
            "Digit0",
            "Digit1",
            "Digit2",
            "Digit3",
            "Digit4",
            "Digit5",
            "Digit6",
            "Digit7",
            "Digit8",
            "Digit9",
            "KeyA",
            "KeyB",
            "KeyC",
            "KeyD",
            "KeyE",
            "KeyF",
            "KeyG",
            "KeyH",
            "KeyI",
            "KeyJ",
            "KeyK",
            "KeyL",
            "KeyM",
            "KeyN",
            "KeyO",
            "KeyP",
            "KeyQ",
            "KeyR",
            "KeyS",
            "KeyT",
            "KeyU",
            "KeyV",
            "KeyW",
            "KeyX",
            "KeyY",
            "KeyZ",
            "MetaLeft",
            "MetaRight",
            "ContextMenu",
            "NumpadMultiply",
            "NumpadAdd",
            "NumpadSubtract",
            "NumpadDivide",
            "F1",
            "F2",
            "F3",
            "F4",
            "F5",
            "F6",
            "F7",
            "F8",
            "F9",
            "F10",
            "F11",
            "F12",
            "F13",
            "F14",
            "F15",
            "F16",
            "F17",
            "F18",
            "F19",
            "F20",
            "F21",
            "F22",
            "F23",
            "F24",
            "NumLock",
            "ScrollLock",
            "AudioVolumeMute",
            "AudioVolumeDown",
            "AudioVolumeUp",
            "MediaTrackNext",
            "MediaTrackPrevious",
            "MediaStop",
            "MediaPlayPause",
            "Semicolon",
            "Equal",
            "NumpadEqual",
            "Comma",
            "Minus",
            "Period",
            "Slash",
            "Backquote",
            "BracketLeft",
            "Backslash",
            "BracketRight",
            "Quote",
            "AltGraph",
            "Props",
            "Cancel",
            "Clear",
            "Shift",
            "Control",
            "Alt",
            "Accept",
            "ModeChange",
            " ",
            "Print",
            "Execute",
            " ",
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
            "Meta",
            "*",
            "+",
            "-",
            "/",
            ";",
            "=",
            ",",
            ".",
            "`",
            "[",
            "\\",
            "]",
            "'",
            "Attn",
            "CrSel",
            "ExSel",
            "EraseEof",
            "Play",
            "ZoomOut",
            ")",
            "!",
            "@",
            "#",
            "$",
            "%",
            "^",
            "&",
            "(",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
            ":",
            "<",
            "_",
            ">",
            "?",
            "~",
            "{",
            "|",
            "}",
            '"',
            "SoftLeft",
            "SoftRight",
            "Camera",
            "Call",
            "EndCall",
            "VolumeDown",
            "VolumeUp",
        ]
    ]

    delay: Union[float, str]
    """Duration value that accepts various formats.

    Supports: number (ms), string ("1000"), or string with unit ("2s", "500ms",
    "2m", "1h")
    """

    required: Union[Literal["true", "false"], bool]
    """Whether this action is required.

    If true, pipeline stops on failure. Accepts boolean or string "true"/"false".
    Default: true.
    """

    skip: Union[Literal["true", "false"], bool]
    """Whether to skip this action.

    Accepts boolean or string "true"/"false". Default: false.
    """


BrowserActionPressActionPress: TypeAlias = Union[str, BrowserActionPressActionPressUnionMember1]


class BrowserActionPressAction(TypedDict, total=False):
    """Press a keyboard key"""

    press: Required[BrowserActionPressActionPress]


class BrowserActionScreenshotActionScreenshotUnionMember1(TypedDict, total=False):
    format: Literal["png", "jpeg", "webp"]

    full_page: bool

    quality: float

    required: Union[Literal["true", "false"], bool]
    """Whether this action is required.

    If true, pipeline stops on failure. Accepts boolean or string "true"/"false".
    Default: true.
    """

    skip: Union[Literal["true", "false"], bool]
    """Whether to skip this action.

    Accepts boolean or string "true"/"false". Default: false.
    """


BrowserActionScreenshotActionScreenshot: TypeAlias = Union[bool, BrowserActionScreenshotActionScreenshotUnionMember1]


class BrowserActionScreenshotAction(TypedDict, total=False):
    """Capture a page screenshot"""

    screenshot: Required[BrowserActionScreenshotActionScreenshot]


class BrowserActionScrollActionScrollUnionMember2(TypedDict, total=False):
    container: Union[str, SequenceNotStr[str]]
    """CSS selector or array of alternative selectors.

    Use an array when you have multiple possible selectors for the same element.
    """

    required: Union[Literal["true", "false"], bool]
    """Whether this action is required.

    If true, pipeline stops on failure. Accepts boolean or string "true"/"false".
    Default: true.
    """

    skip: Union[Literal["true", "false"], bool]
    """Whether to skip this action.

    Accepts boolean or string "true"/"false". Default: false.
    """

    to: Union[str, SequenceNotStr[str]]
    """CSS selector or array of alternative selectors.

    Use an array when you have multiple possible selectors for the same element.
    """

    visible: bool

    x: float

    y: float


BrowserActionScrollActionScroll: TypeAlias = Union[float, str, BrowserActionScrollActionScrollUnionMember2]


class BrowserActionScrollAction(TypedDict, total=False):
    """Scroll the page or an element"""

    scroll: Required[BrowserActionScrollActionScroll]


class BrowserActionWaitActionWaitUnionMember2(TypedDict, total=False):
    duration: Required[Union[float, str]]
    """Duration value that accepts various formats.

    Supports: number (ms), string ("1000"), or string with unit ("2s", "500ms",
    "2m", "1h")
    """

    required: Union[Literal["true", "false"], bool]
    """Whether this action is required.

    If true, pipeline stops on failure. Accepts boolean or string "true"/"false".
    Default: true.
    """

    skip: Union[Literal["true", "false"], bool]
    """Whether to skip this action.

    Accepts boolean or string "true"/"false". Default: false.
    """


BrowserActionWaitActionWait: TypeAlias = Union[float, str, BrowserActionWaitActionWaitUnionMember2]


class BrowserActionWaitAction(TypedDict, total=False):
    """Wait for a specified duration"""

    wait: Required[BrowserActionWaitActionWait]


class BrowserActionWaitForElementActionWaitForElementUnionMember2(TypedDict, total=False):
    selector: Required[Union[str, SequenceNotStr[str]]]
    """CSS selector or array of alternative selectors.

    Use an array when you have multiple possible selectors for the same element.
    """

    required: Union[Literal["true", "false"], bool]
    """Whether this action is required.

    If true, pipeline stops on failure. Accepts boolean or string "true"/"false".
    Default: true.
    """

    skip: Union[Literal["true", "false"], bool]
    """Whether to skip this action.

    Accepts boolean or string "true"/"false". Default: false.
    """

    timeout: float
    """Timeout in milliseconds.

    Set to 0 for infinite timeout (no timeout). Default: 15000ms.
    """

    visible: bool


BrowserActionWaitForElementActionWaitForElement: TypeAlias = Union[
    str, SequenceNotStr[str], BrowserActionWaitForElementActionWaitForElementUnionMember2
]


class BrowserActionWaitForElementAction(TypedDict, total=False):
    """Wait for an element to appear or reach a specific state"""

    wait_for_element: Required[BrowserActionWaitForElementActionWaitForElement]


class BrowserActionWaitForNavigationActionWaitForNavigationUnionMember1(TypedDict, total=False):
    navigation: Required[Literal["load", "domcontentloaded", "networkidle0", "networkidle2"]]

    required: Union[Literal["true", "false"], bool]
    """Whether this action is required.

    If true, pipeline stops on failure. Accepts boolean or string "true"/"false".
    Default: true.
    """

    skip: Union[Literal["true", "false"], bool]
    """Whether to skip this action.

    Accepts boolean or string "true"/"false". Default: false.
    """

    timeout: float
    """Timeout in milliseconds.

    Set to 0 for infinite timeout (no timeout). Default: 15000ms.
    """


BrowserActionWaitForNavigationActionWaitForNavigation: TypeAlias = Union[
    Literal["load", "domcontentloaded", "networkidle0", "networkidle2"],
    BrowserActionWaitForNavigationActionWaitForNavigationUnionMember1,
]


class BrowserActionWaitForNavigationAction(TypedDict, total=False):
    """Wait for page navigation to complete"""

    wait_for_navigation: Required[BrowserActionWaitForNavigationActionWaitForNavigation]


BrowserAction: TypeAlias = Union[
    BrowserActionAutoScrollAction,
    BrowserActionClickAction,
    BrowserActionEvalAction,
    BrowserActionFetchAction,
    BrowserActionFillAction,
    BrowserActionGetCookiesAction,
    BrowserActionGotoAction,
    BrowserActionPressAction,
    BrowserActionScreenshotAction,
    BrowserActionScrollAction,
    BrowserActionWaitAction,
    BrowserActionWaitForElementAction,
    BrowserActionWaitForNavigationAction,
]


class CookiesUnionMember0Typed(TypedDict, total=False):
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


CookiesUnionMember0: TypeAlias = Union[CookiesUnionMember0Typed, Dict[str, object]]


class Metadata(TypedDict, total=False):
    """Structured metadata about the request execution context"""

    account_name: str

    api_type: str

    crawl_depth: int

    crawl_id: str

    definition_id: int

    definition_name: str

    endpoint: str

    execution_id: str

    flowit_task_id: str

    input_id: str

    is_public_wsa: bool

    is_sitemap: bool

    is_wsa: bool

    parser_id: str

    pipeline_execution_id: int

    query_template_id: str

    source: str

    template_id: int

    template_name: str

    wsa_id: str

    wsa_name: str

    wsa_version: float


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


class QueryTemplatePaginationNextPageParams(TypedDict, total=False):
    next_page_params: Required[Dict[str, object]]


class QueryTemplatePaginationUnionMember1(TypedDict, total=False):
    next_page_params: Required[Dict[str, object]]


QueryTemplatePagination: TypeAlias = Union[
    QueryTemplatePaginationNextPageParams, Iterable[QueryTemplatePaginationUnionMember1]
]


class QueryTemplateTyped(TypedDict, total=False):
    """Query template configuration for structured data extraction"""

    id: Required[str]

    api_type: Literal["WEB", "SERP", "SOCIAL"]

    pagination: QueryTemplatePagination

    params: Dict[str, object]


QueryTemplate: TypeAlias = Union[QueryTemplateTyped, Dict[str, object]]


class RenderOptionsHackiumConfiguration(TypedDict, total=False):
    """Configuration for Hackium browser modifications"""

    collect_logs: bool

    do_not_fix_math_salt: bool

    enable_document_element_spoof: bool

    enable_document_has_focus: bool

    enable_fake_navigation_history: bool

    enable_key_ordering: bool

    enable_sniffer: bool

    enable_verbose_logs: bool


class RenderOptions(TypedDict, total=False):
    adblock: bool
    """Whether to enable ad blocking"""

    blocked_domains: SequenceNotStr[str]
    """Domains to block from loading"""

    browser_engine: Union[Literal["chrome", "hackium", "firefox", "hackfox"], Dict[str, float]]
    """Browser engine to use, or weighted distribution of engines"""

    cache: bool
    """Whether to enable browser caching"""

    connector_type: Literal["puppeteer", "puppeteer-cdp", "puppeteer-bidi", "webit-cdp", "playwright"]
    """Type of browser connector to use"""

    disabled_resources: List[
        Literal[
            "other",
            "document",
            "stylesheet",
            "image",
            "media",
            "font",
            "script",
            "texttrack",
            "xhr",
            "fetch",
            "eventsource",
            "websocket",
            "manifest",
            "signedexchange",
            "ping",
            "cspviolationreport",
            "prefetch",
            "preflight",
            "fedcm",
        ]
    ]
    """Types of resources to block from loading"""

    enable_2captcha: bool
    """Whether to use 2Captcha service for solving captchas"""

    extensions: SequenceNotStr[str]
    """Browser extensions to load"""

    fingerprint_id: str
    """Fingerprint identifier for browser customization"""

    hackium_configuration: RenderOptionsHackiumConfiguration
    """Configuration for Hackium browser modifications"""

    headless: bool
    """Whether to run browser in headless mode"""

    include_iframes: bool
    """Whether to include iframe content in the result"""

    load_local_storage: bool
    """Whether to load previously stored localStorage data"""

    local_storage_keys_to_load: SequenceNotStr[str]
    """Specific localStorage keys to load"""

    mouse_strategy: Literal["linear", "ghost-cursor", "windmouse"]
    """Strategy for simulating mouse movements"""

    no_accept_encoding: bool
    """Disable content encoding to avoid cached responses"""

    override_permissions: bool
    """Whether to override default browser permissions"""

    random_header_order: bool
    """Whether to randomize HTTP header order"""

    render_type: Literal["domcontentloaded", "load", "idle0", "networkidle0", "idle2", "networkidle2", "navigate"]
    """Type of render completion to wait for"""

    store_local_storage: bool
    """Whether to store localStorage data for future sessions"""

    timeout: float
    """Maximum time in milliseconds to wait for page render"""

    typing_interval: float
    """Interval in milliseconds between key presses"""

    typing_strategy: Literal["simple", "distribution"]
    """Strategy for simulating keyboard typing"""

    userbrowser: bool
    """Whether to use a persistent browser session"""

    wait_until: Literal["load", "domcontentloaded", "idle0", "idle2", "networkidle0", "networkidle2", "navigate"]
    """Browser event to wait for before considering page loaded"""

    with_performance_metrics: bool
    """Whether to collect performance metrics during rendering"""


class Session(TypedDict, total=False):
    id: str

    prefetch_userbrowser: bool

    retry: bool

    timeout: float


class Template(TypedDict, total=False):
    """Userbrowser creation template configuration"""

    name: Required[str]

    params: Dict[str, object]


class UserbrowserCreationTemplateRendered(TypedDict, total=False):
    """Pre-rendered userbrowser creation template configuration"""

    id: Required[str]

    allowed_parameter_names: Required[SequenceNotStr[str]]

    render_flow_rendered: Required[Iterable[Dict[str, object]]]
