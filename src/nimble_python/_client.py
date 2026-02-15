# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from .types import client_map_params
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
from .types.map_response import MapResponse

if TYPE_CHECKING:
    from .resources import crawl, agents, extract
    from .resources.crawl import CrawlResource, AsyncCrawlResource
    from .resources.agents import AgentsResource, AsyncAgentsResource
    from .resources.extract import ExtractResource, AsyncExtractResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Nimble", "AsyncNimble", "Client", "AsyncClient"]


class Nimble(SyncAPIClient):
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
        """Construct a new synchronous Nimble client instance.

        This automatically infers the `api_key` argument from the `NIMBLE_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("NIMBLE_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("NIMBLE_BASE_URL")
        if base_url is None:
            base_url = f"https://sdk.nimbleway.com"

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
    def extract(self) -> ExtractResource:
        from .resources.extract import ExtractResource

        return ExtractResource(self)

    @cached_property
    def agents(self) -> AgentsResource:
        from .resources.agents import AgentsResource

        return AgentsResource(self)

    @cached_property
    def crawl(self) -> CrawlResource:
        from .resources.crawl import CrawlResource

        return CrawlResource(self)

    @cached_property
    def with_raw_response(self) -> NimbleWithRawResponse:
        return NimbleWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NimbleWithStreamedResponse:
        return NimbleWithStreamedResponse(self)

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

    def map(
        self,
        *,
        url: str,
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
        ]
        | Omit = omit,
        domain_filter: Literal["domain", "subdomain", "all"] | Omit = omit,
        limit: int | Omit = omit,
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
        sitemap: Literal["skip", "include", "only"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MapResponse:
        """
        Create map task

        Args:
          url: Url to map.

          country: Country code for geolocation and proxy selection

          domain_filter: Includes subdomains of the main domain in the mapping process.

          limit: Maximum number of links to return.

          locale: Locale for browser language and region settings

          sitemap: Sitemap and other methods will be used together to find URLs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/v1/map",
            body=maybe_transform(
                {
                    "url": url,
                    "country": country,
                    "domain_filter": domain_filter,
                    "limit": limit,
                    "locale": locale,
                    "sitemap": sitemap,
                },
                client_map_params.ClientMapParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MapResponse,
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


class AsyncNimble(AsyncAPIClient):
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
        """Construct a new async AsyncNimble client instance.

        This automatically infers the `api_key` argument from the `NIMBLE_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("NIMBLE_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("NIMBLE_BASE_URL")
        if base_url is None:
            base_url = f"https://sdk.nimbleway.com"

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
    def extract(self) -> AsyncExtractResource:
        from .resources.extract import AsyncExtractResource

        return AsyncExtractResource(self)

    @cached_property
    def agents(self) -> AsyncAgentsResource:
        from .resources.agents import AsyncAgentsResource

        return AsyncAgentsResource(self)

    @cached_property
    def crawl(self) -> AsyncCrawlResource:
        from .resources.crawl import AsyncCrawlResource

        return AsyncCrawlResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncNimbleWithRawResponse:
        return AsyncNimbleWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNimbleWithStreamedResponse:
        return AsyncNimbleWithStreamedResponse(self)

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

    async def map(
        self,
        *,
        url: str,
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
        ]
        | Omit = omit,
        domain_filter: Literal["domain", "subdomain", "all"] | Omit = omit,
        limit: int | Omit = omit,
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
        sitemap: Literal["skip", "include", "only"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MapResponse:
        """
        Create map task

        Args:
          url: Url to map.

          country: Country code for geolocation and proxy selection

          domain_filter: Includes subdomains of the main domain in the mapping process.

          limit: Maximum number of links to return.

          locale: Locale for browser language and region settings

          sitemap: Sitemap and other methods will be used together to find URLs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/v1/map",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "country": country,
                    "domain_filter": domain_filter,
                    "limit": limit,
                    "locale": locale,
                    "sitemap": sitemap,
                },
                client_map_params.ClientMapParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MapResponse,
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


class NimbleWithRawResponse:
    _client: Nimble

    def __init__(self, client: Nimble) -> None:
        self._client = client

        self.map = to_raw_response_wrapper(
            client.map,
        )

    @cached_property
    def extract(self) -> extract.ExtractResourceWithRawResponse:
        from .resources.extract import ExtractResourceWithRawResponse

        return ExtractResourceWithRawResponse(self._client.extract)

    @cached_property
    def agents(self) -> agents.AgentsResourceWithRawResponse:
        from .resources.agents import AgentsResourceWithRawResponse

        return AgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def crawl(self) -> crawl.CrawlResourceWithRawResponse:
        from .resources.crawl import CrawlResourceWithRawResponse

        return CrawlResourceWithRawResponse(self._client.crawl)


class AsyncNimbleWithRawResponse:
    _client: AsyncNimble

    def __init__(self, client: AsyncNimble) -> None:
        self._client = client

        self.map = async_to_raw_response_wrapper(
            client.map,
        )

    @cached_property
    def extract(self) -> extract.AsyncExtractResourceWithRawResponse:
        from .resources.extract import AsyncExtractResourceWithRawResponse

        return AsyncExtractResourceWithRawResponse(self._client.extract)

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithRawResponse:
        from .resources.agents import AsyncAgentsResourceWithRawResponse

        return AsyncAgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def crawl(self) -> crawl.AsyncCrawlResourceWithRawResponse:
        from .resources.crawl import AsyncCrawlResourceWithRawResponse

        return AsyncCrawlResourceWithRawResponse(self._client.crawl)


class NimbleWithStreamedResponse:
    _client: Nimble

    def __init__(self, client: Nimble) -> None:
        self._client = client

        self.map = to_streamed_response_wrapper(
            client.map,
        )

    @cached_property
    def extract(self) -> extract.ExtractResourceWithStreamingResponse:
        from .resources.extract import ExtractResourceWithStreamingResponse

        return ExtractResourceWithStreamingResponse(self._client.extract)

    @cached_property
    def agents(self) -> agents.AgentsResourceWithStreamingResponse:
        from .resources.agents import AgentsResourceWithStreamingResponse

        return AgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def crawl(self) -> crawl.CrawlResourceWithStreamingResponse:
        from .resources.crawl import CrawlResourceWithStreamingResponse

        return CrawlResourceWithStreamingResponse(self._client.crawl)


class AsyncNimbleWithStreamedResponse:
    _client: AsyncNimble

    def __init__(self, client: AsyncNimble) -> None:
        self._client = client

        self.map = async_to_streamed_response_wrapper(
            client.map,
        )

    @cached_property
    def extract(self) -> extract.AsyncExtractResourceWithStreamingResponse:
        from .resources.extract import AsyncExtractResourceWithStreamingResponse

        return AsyncExtractResourceWithStreamingResponse(self._client.extract)

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithStreamingResponse:
        from .resources.agents import AsyncAgentsResourceWithStreamingResponse

        return AsyncAgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def crawl(self) -> crawl.AsyncCrawlResourceWithStreamingResponse:
        from .resources.crawl import AsyncCrawlResourceWithStreamingResponse

        return AsyncCrawlResourceWithStreamingResponse(self._client.crawl)


Client = Nimble

AsyncClient = AsyncNimble
