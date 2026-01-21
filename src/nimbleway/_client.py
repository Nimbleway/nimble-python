# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Union, Mapping, Iterable
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from .types import client_extract_params, client_extract_template_params
from ._types import (
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    SequenceNotStr,
    omit,
    not_given,
)
from ._utils import (
    is_given,
    maybe_transform,
    get_async_library,
    async_maybe_transform,
)
from ._compat import cached_property
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .types.extract_response import ExtractResponse
from .types.extract_template_response import ExtractTemplateResponse

if TYPE_CHECKING:
    from .resources import crawl
    from .resources.crawl import CrawlResource, AsyncCrawlResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Nimbleway",
    "AsyncNimbleway",
    "Client",
    "AsyncClient",
]


class Nimbleway(SyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Nimbleway client instance.

        This automatically infers the `api_key` argument from the `NIMBLEWAY_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("NIMBLEWAY_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("NIMBLEWAY_BASE_URL")
        if base_url is None:
            base_url = f"https://gateway.staging.webit.live"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def crawl(self) -> CrawlResource:
        from .resources.crawl import CrawlResource

        return CrawlResource(self)

    @cached_property
    def with_raw_response(self) -> NimblewayWithRawResponse:
        return NimblewayWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NimblewayWithStreamedResponse:
        return NimblewayWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def extract(
        self,
        *,
        debug_options: client_extract_params.DebugOptions,
        url: str,
        browser: client_extract_params.Browser | Omit = omit,
        city: str | Omit = omit,
        client_timeout: float | Omit = omit,
        consent_header: bool | Omit = omit,
        cookies: Union[Iterable[client_extract_params.CookiesUnionMember0], str] | Omit = omit,
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
        | Omit = omit,
        device: Literal["desktop", "mobile", "tablet"] | Omit = omit,
        disable_ip_check: bool | Omit = omit,
        driver: Literal["vx6", "vx8", "vx8-pro", "vx10", "vx10-pro", "vx12", "vx12-pro"] | Omit = omit,
        dynamic_parser: Dict[str, object] | Omit = omit,
        expected_status_codes: Iterable[int] | Omit = omit,
        export_userbrowser: bool | Omit = omit,
        format: Literal["json", "html", "csv", "raw", "json-lines", "markdown"] | Omit = omit,
        headers: Dict[str, Union[str, SequenceNotStr[str], None]] | Omit = omit,
        http2: bool | Omit = omit,
        ip6: bool | Omit = omit,
        is_xhr: bool | Omit = omit,
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
        | Omit = omit,
        markdown: bool | Omit = omit,
        metadata: client_extract_params.Metadata | Omit = omit,
        method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"] | Omit = omit,
        native_mode: Literal["requester", "apm", "direct"] | Omit = omit,
        network_capture: Iterable[client_extract_params.NetworkCapture] | Omit = omit,
        no_html: bool | Omit = omit,
        no_userbrowser: bool | Omit = omit,
        os: Literal["windows", "mac os", "linux", "android", "ios"] | Omit = omit,
        parse: bool | Omit = omit,
        parse_options: client_extract_params.ParseOptions | Omit = omit,
        parser: Union[Dict[str, object], str] | Omit = omit,
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
        | Omit = omit,
        proxy_providers: Dict[str, float] | Omit = omit,
        query_template: client_extract_params.QueryTemplate | Omit = omit,
        raw_headers: bool | Omit = omit,
        referrer_type: Literal[
            "random", "no-referer", "same-origin", "google", "bing", "facebook", "twitter", "instagram"
        ]
        | Omit = omit,
        render: bool | Omit = omit,
        render_flow: Iterable[Dict[str, object]] | Omit = omit,
        render_options: client_extract_params.RenderOptions | Omit = omit,
        request_timeout: float | Omit = omit,
        return_response_headers_as_header: bool | Omit = omit,
        save_userbrowser: bool | Omit = omit,
        session: client_extract_params.Session | Omit = omit,
        skill: Union[str, SequenceNotStr[str]] | Omit = omit,
        skip_ubct: bool | Omit = omit,
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
        | Omit = omit,
        tag: str | Omit = omit,
        template: client_extract_params.Template | Omit = omit,
        type: str | Omit = omit,
        userbrowser_creation_template_rendered: client_extract_params.UserbrowserCreationTemplateRendered | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractResponse:
        """
        Webit v2 Realtime extract Endpoint

        Args:
          debug_options: Debug and troubleshooting options for the request

          url: Target URL to scrape

          browser: Browser type to emulate

          city: City for geolocation

          client_timeout: Client-side timeout in milliseconds

          consent_header: Whether to automatically handle cookie consent headers

          cookies: Browser cookies as array of cookie objects

          country: Country code for geolocation and proxy selection

          device: Device type for browser emulation

          disable_ip_check: Whether to disable IP address validation

          driver: Browser driver to use

          dynamic_parser: Custom parser configuration as a key-value map

          expected_status_codes: Expected HTTP status codes for successful requests

          export_userbrowser: Whether to export the userbrowser session

          format: Response format

          headers: Custom HTTP headers to include in the request

          http2: Whether to use HTTP/2 protocol

          ip6: Whether to use IPv6 for the request

          is_xhr: Whether to emulate XMLHttpRequest behavior

          locale: Locale for browser language and region settings

          markdown: Whether to return response in Markdown format

          metadata: Structured metadata about the request execution context

          method: HTTP method for the request

          native_mode: Native execution mode

          network_capture: Filters for capturing network traffic

          no_html: Whether to exclude HTML from the response

          no_userbrowser: Whether to disable browser-based rendering

          os: Operating system to emulate

          parse: Whether to parse the response content

          parse_options: Configuration options for parsing behavior

          parser: Custom parser configuration as a key-value map

          proxy_provider: Proxy provider to use for the request

          proxy_providers: Weighted distribution of proxy providers

          query_template: Query template configuration for structured data extraction

          raw_headers: Whether to return raw HTTP headers in response

          referrer_type: Referrer policy for the request

          render: Whether to render JavaScript content using a browser

          render_flow: Array of actions to perform during browser rendering

          request_timeout: Request timeout in milliseconds

          return_response_headers_as_header: Whether to return response headers in HTTP headers

          save_userbrowser: Whether to save the userbrowser session for reuse

          skill: Skills or capabilities required for the request

          skip_ubct: Whether to skip userbrowser creation template processing

          state: US state for geolocation (only valid when country is US)

          tag: User-defined tag for request identification

          template: Userbrowser creation template configuration

          type: Type of query or scraping template

          userbrowser_creation_template_rendered: Pre-rendered userbrowser creation template configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/v1/extract",
            body=maybe_transform(
                {
                    "debug_options": debug_options,
                    "url": url,
                    "browser": browser,
                    "city": city,
                    "client_timeout": client_timeout,
                    "consent_header": consent_header,
                    "cookies": cookies,
                    "country": country,
                    "device": device,
                    "disable_ip_check": disable_ip_check,
                    "driver": driver,
                    "dynamic_parser": dynamic_parser,
                    "expected_status_codes": expected_status_codes,
                    "export_userbrowser": export_userbrowser,
                    "format": format,
                    "headers": headers,
                    "http2": http2,
                    "ip6": ip6,
                    "is_xhr": is_xhr,
                    "locale": locale,
                    "markdown": markdown,
                    "metadata": metadata,
                    "method": method,
                    "native_mode": native_mode,
                    "network_capture": network_capture,
                    "no_html": no_html,
                    "no_userbrowser": no_userbrowser,
                    "os": os,
                    "parse": parse,
                    "parse_options": parse_options,
                    "parser": parser,
                    "proxy_provider": proxy_provider,
                    "proxy_providers": proxy_providers,
                    "query_template": query_template,
                    "raw_headers": raw_headers,
                    "referrer_type": referrer_type,
                    "render": render,
                    "render_flow": render_flow,
                    "render_options": render_options,
                    "request_timeout": request_timeout,
                    "return_response_headers_as_header": return_response_headers_as_header,
                    "save_userbrowser": save_userbrowser,
                    "session": session,
                    "skill": skill,
                    "skip_ubct": skip_ubct,
                    "state": state,
                    "tag": tag,
                    "template": template,
                    "type": type,
                    "userbrowser_creation_template_rendered": userbrowser_creation_template_rendered,
                },
                client_extract_params.ClientExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractResponse,
        )

    def extract_template(
        self,
        *,
        params: Dict[str, object],
        template: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractTemplateResponse:
        """
        Execute WSA Template Realtime Endpoint

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/v1/extract-template",
            body=maybe_transform(
                {
                    "params": params,
                    "template": template,
                },
                client_extract_template_params.ClientExtractTemplateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractTemplateResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncNimbleway(AsyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncNimbleway client instance.

        This automatically infers the `api_key` argument from the `NIMBLEWAY_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("NIMBLEWAY_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("NIMBLEWAY_BASE_URL")
        if base_url is None:
            base_url = f"https://gateway.staging.webit.live"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def crawl(self) -> AsyncCrawlResource:
        from .resources.crawl import AsyncCrawlResource

        return AsyncCrawlResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncNimblewayWithRawResponse:
        return AsyncNimblewayWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNimblewayWithStreamedResponse:
        return AsyncNimblewayWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def extract(
        self,
        *,
        debug_options: client_extract_params.DebugOptions,
        url: str,
        browser: client_extract_params.Browser | Omit = omit,
        city: str | Omit = omit,
        client_timeout: float | Omit = omit,
        consent_header: bool | Omit = omit,
        cookies: Union[Iterable[client_extract_params.CookiesUnionMember0], str] | Omit = omit,
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
        | Omit = omit,
        device: Literal["desktop", "mobile", "tablet"] | Omit = omit,
        disable_ip_check: bool | Omit = omit,
        driver: Literal["vx6", "vx8", "vx8-pro", "vx10", "vx10-pro", "vx12", "vx12-pro"] | Omit = omit,
        dynamic_parser: Dict[str, object] | Omit = omit,
        expected_status_codes: Iterable[int] | Omit = omit,
        export_userbrowser: bool | Omit = omit,
        format: Literal["json", "html", "csv", "raw", "json-lines", "markdown"] | Omit = omit,
        headers: Dict[str, Union[str, SequenceNotStr[str], None]] | Omit = omit,
        http2: bool | Omit = omit,
        ip6: bool | Omit = omit,
        is_xhr: bool | Omit = omit,
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
        | Omit = omit,
        markdown: bool | Omit = omit,
        metadata: client_extract_params.Metadata | Omit = omit,
        method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"] | Omit = omit,
        native_mode: Literal["requester", "apm", "direct"] | Omit = omit,
        network_capture: Iterable[client_extract_params.NetworkCapture] | Omit = omit,
        no_html: bool | Omit = omit,
        no_userbrowser: bool | Omit = omit,
        os: Literal["windows", "mac os", "linux", "android", "ios"] | Omit = omit,
        parse: bool | Omit = omit,
        parse_options: client_extract_params.ParseOptions | Omit = omit,
        parser: Union[Dict[str, object], str] | Omit = omit,
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
        | Omit = omit,
        proxy_providers: Dict[str, float] | Omit = omit,
        query_template: client_extract_params.QueryTemplate | Omit = omit,
        raw_headers: bool | Omit = omit,
        referrer_type: Literal[
            "random", "no-referer", "same-origin", "google", "bing", "facebook", "twitter", "instagram"
        ]
        | Omit = omit,
        render: bool | Omit = omit,
        render_flow: Iterable[Dict[str, object]] | Omit = omit,
        render_options: client_extract_params.RenderOptions | Omit = omit,
        request_timeout: float | Omit = omit,
        return_response_headers_as_header: bool | Omit = omit,
        save_userbrowser: bool | Omit = omit,
        session: client_extract_params.Session | Omit = omit,
        skill: Union[str, SequenceNotStr[str]] | Omit = omit,
        skip_ubct: bool | Omit = omit,
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
        | Omit = omit,
        tag: str | Omit = omit,
        template: client_extract_params.Template | Omit = omit,
        type: str | Omit = omit,
        userbrowser_creation_template_rendered: client_extract_params.UserbrowserCreationTemplateRendered | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractResponse:
        """
        Webit v2 Realtime extract Endpoint

        Args:
          debug_options: Debug and troubleshooting options for the request

          url: Target URL to scrape

          browser: Browser type to emulate

          city: City for geolocation

          client_timeout: Client-side timeout in milliseconds

          consent_header: Whether to automatically handle cookie consent headers

          cookies: Browser cookies as array of cookie objects

          country: Country code for geolocation and proxy selection

          device: Device type for browser emulation

          disable_ip_check: Whether to disable IP address validation

          driver: Browser driver to use

          dynamic_parser: Custom parser configuration as a key-value map

          expected_status_codes: Expected HTTP status codes for successful requests

          export_userbrowser: Whether to export the userbrowser session

          format: Response format

          headers: Custom HTTP headers to include in the request

          http2: Whether to use HTTP/2 protocol

          ip6: Whether to use IPv6 for the request

          is_xhr: Whether to emulate XMLHttpRequest behavior

          locale: Locale for browser language and region settings

          markdown: Whether to return response in Markdown format

          metadata: Structured metadata about the request execution context

          method: HTTP method for the request

          native_mode: Native execution mode

          network_capture: Filters for capturing network traffic

          no_html: Whether to exclude HTML from the response

          no_userbrowser: Whether to disable browser-based rendering

          os: Operating system to emulate

          parse: Whether to parse the response content

          parse_options: Configuration options for parsing behavior

          parser: Custom parser configuration as a key-value map

          proxy_provider: Proxy provider to use for the request

          proxy_providers: Weighted distribution of proxy providers

          query_template: Query template configuration for structured data extraction

          raw_headers: Whether to return raw HTTP headers in response

          referrer_type: Referrer policy for the request

          render: Whether to render JavaScript content using a browser

          render_flow: Array of actions to perform during browser rendering

          request_timeout: Request timeout in milliseconds

          return_response_headers_as_header: Whether to return response headers in HTTP headers

          save_userbrowser: Whether to save the userbrowser session for reuse

          skill: Skills or capabilities required for the request

          skip_ubct: Whether to skip userbrowser creation template processing

          state: US state for geolocation (only valid when country is US)

          tag: User-defined tag for request identification

          template: Userbrowser creation template configuration

          type: Type of query or scraping template

          userbrowser_creation_template_rendered: Pre-rendered userbrowser creation template configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/v1/extract",
            body=await async_maybe_transform(
                {
                    "debug_options": debug_options,
                    "url": url,
                    "browser": browser,
                    "city": city,
                    "client_timeout": client_timeout,
                    "consent_header": consent_header,
                    "cookies": cookies,
                    "country": country,
                    "device": device,
                    "disable_ip_check": disable_ip_check,
                    "driver": driver,
                    "dynamic_parser": dynamic_parser,
                    "expected_status_codes": expected_status_codes,
                    "export_userbrowser": export_userbrowser,
                    "format": format,
                    "headers": headers,
                    "http2": http2,
                    "ip6": ip6,
                    "is_xhr": is_xhr,
                    "locale": locale,
                    "markdown": markdown,
                    "metadata": metadata,
                    "method": method,
                    "native_mode": native_mode,
                    "network_capture": network_capture,
                    "no_html": no_html,
                    "no_userbrowser": no_userbrowser,
                    "os": os,
                    "parse": parse,
                    "parse_options": parse_options,
                    "parser": parser,
                    "proxy_provider": proxy_provider,
                    "proxy_providers": proxy_providers,
                    "query_template": query_template,
                    "raw_headers": raw_headers,
                    "referrer_type": referrer_type,
                    "render": render,
                    "render_flow": render_flow,
                    "render_options": render_options,
                    "request_timeout": request_timeout,
                    "return_response_headers_as_header": return_response_headers_as_header,
                    "save_userbrowser": save_userbrowser,
                    "session": session,
                    "skill": skill,
                    "skip_ubct": skip_ubct,
                    "state": state,
                    "tag": tag,
                    "template": template,
                    "type": type,
                    "userbrowser_creation_template_rendered": userbrowser_creation_template_rendered,
                },
                client_extract_params.ClientExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractResponse,
        )

    async def extract_template(
        self,
        *,
        params: Dict[str, object],
        template: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractTemplateResponse:
        """
        Execute WSA Template Realtime Endpoint

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/v1/extract-template",
            body=await async_maybe_transform(
                {
                    "params": params,
                    "template": template,
                },
                client_extract_template_params.ClientExtractTemplateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractTemplateResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class NimblewayWithRawResponse:
    _client: Nimbleway

    def __init__(self, client: Nimbleway) -> None:
        self._client = client

        self.extract = to_raw_response_wrapper(
            client.extract,
        )
        self.extract_template = to_raw_response_wrapper(
            client.extract_template,
        )

    @cached_property
    def crawl(self) -> crawl.CrawlResourceWithRawResponse:
        from .resources.crawl import CrawlResourceWithRawResponse

        return CrawlResourceWithRawResponse(self._client.crawl)


class AsyncNimblewayWithRawResponse:
    _client: AsyncNimbleway

    def __init__(self, client: AsyncNimbleway) -> None:
        self._client = client

        self.extract = async_to_raw_response_wrapper(
            client.extract,
        )
        self.extract_template = async_to_raw_response_wrapper(
            client.extract_template,
        )

    @cached_property
    def crawl(self) -> crawl.AsyncCrawlResourceWithRawResponse:
        from .resources.crawl import AsyncCrawlResourceWithRawResponse

        return AsyncCrawlResourceWithRawResponse(self._client.crawl)


class NimblewayWithStreamedResponse:
    _client: Nimbleway

    def __init__(self, client: Nimbleway) -> None:
        self._client = client

        self.extract = to_streamed_response_wrapper(
            client.extract,
        )
        self.extract_template = to_streamed_response_wrapper(
            client.extract_template,
        )

    @cached_property
    def crawl(self) -> crawl.CrawlResourceWithStreamingResponse:
        from .resources.crawl import CrawlResourceWithStreamingResponse

        return CrawlResourceWithStreamingResponse(self._client.crawl)


class AsyncNimblewayWithStreamedResponse:
    _client: AsyncNimbleway

    def __init__(self, client: AsyncNimbleway) -> None:
        self._client = client

        self.extract = async_to_streamed_response_wrapper(
            client.extract,
        )
        self.extract_template = async_to_streamed_response_wrapper(
            client.extract_template,
        )

    @cached_property
    def crawl(self) -> crawl.AsyncCrawlResourceWithStreamingResponse:
        from .resources.crawl import AsyncCrawlResourceWithStreamingResponse

        return AsyncCrawlResourceWithStreamingResponse(self._client.crawl)


Client = Nimbleway

AsyncClient = AsyncNimbleway
