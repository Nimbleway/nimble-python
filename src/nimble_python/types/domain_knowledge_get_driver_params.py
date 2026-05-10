# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DomainKnowledgeGetDriverParams"]


class DomainKnowledgeGetDriverParams(TypedDict, total=False):
    agent: str
    """Agent name to resolve driver for (e.g. nimble-ecommerce)."""

    url: str
    """Target domain to resolve driver for (e.g. amazon.com)."""
