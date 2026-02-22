# Shared Types

```python
from nimble_python.types import (
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
)
```

# Nimble

Types:

```python
from nimble_python.types import MapResponse, SearchResponse
```

Methods:

- <code title="post /v1/map">client.<a href="./src/nimble_python/_client.py">map</a>(\*\*<a href="src/nimble_python/types/client_map_params.py">params</a>) -> <a href="./src/nimble_python/types/map_response.py">MapResponse</a></code>
- <code title="post /v1/search">client.<a href="./src/nimble_python/_client.py">search</a>(\*\*<a href="src/nimble_python/types/client_search_params.py">params</a>) -> <a href="./src/nimble_python/types/search_response.py">SearchResponse</a></code>

# Extract

Types:

```python
from nimble_python.types import ExtractAsyncResponse, ExtractRunResponse
```

Methods:

- <code title="post /v1/extract/async">client.extract.<a href="./src/nimble_python/resources/extract.py">async\_</a>(\*\*<a href="src/nimble_python/types/extract_async_params.py">params</a>) -> <a href="./src/nimble_python/types/extract_async_response.py">ExtractAsyncResponse</a></code>
- <code title="post /v1/extract">client.extract.<a href="./src/nimble_python/resources/extract.py">run</a>(\*\*<a href="src/nimble_python/types/extract_run_params.py">params</a>) -> <a href="./src/nimble_python/types/extract_run_response.py">ExtractRunResponse</a></code>

# Agents

Types:

```python
from nimble_python.types import (
    AgentListResponse,
    AgentAsyncResponse,
    AgentGetResponse,
    AgentRunResponse,
)
```

Methods:

- <code title="get /v1/agents">client.agents.<a href="./src/nimble_python/resources/agents.py">list</a>(\*\*<a href="src/nimble_python/types/agent_list_params.py">params</a>) -> <a href="./src/nimble_python/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="post /v1/agents/async">client.agents.<a href="./src/nimble_python/resources/agents.py">async\_</a>(\*\*<a href="src/nimble_python/types/agent_async_params.py">params</a>) -> <a href="./src/nimble_python/types/agent_async_response.py">AgentAsyncResponse</a></code>
- <code title="get /v1/agents/{template_name}">client.agents.<a href="./src/nimble_python/resources/agents.py">get</a>(template_name) -> <a href="./src/nimble_python/types/agent_get_response.py">AgentGetResponse</a></code>
- <code title="post /v1/agents/run">client.agents.<a href="./src/nimble_python/resources/agents.py">run</a>(\*\*<a href="src/nimble_python/types/agent_run_params.py">params</a>) -> <a href="./src/nimble_python/types/agent_run_response.py">AgentRunResponse</a></code>

# Crawl

Types:

```python
from nimble_python.types import (
    CrawlListResponse,
    CrawlRunResponse,
    CrawlStatusResponse,
    CrawlTerminateResponse,
)
```

Methods:

- <code title="get /v1/crawl">client.crawl.<a href="./src/nimble_python/resources/crawl.py">list</a>(\*\*<a href="src/nimble_python/types/crawl_list_params.py">params</a>) -> <a href="./src/nimble_python/types/crawl_list_response.py">CrawlListResponse</a></code>
- <code title="post /v1/crawl">client.crawl.<a href="./src/nimble_python/resources/crawl.py">run</a>(\*\*<a href="src/nimble_python/types/crawl_run_params.py">params</a>) -> <a href="./src/nimble_python/types/crawl_run_response.py">CrawlRunResponse</a></code>
- <code title="get /v1/crawl/{id}">client.crawl.<a href="./src/nimble_python/resources/crawl.py">status</a>(id) -> <a href="./src/nimble_python/types/crawl_status_response.py">CrawlStatusResponse</a></code>
- <code title="delete /v1/crawl/{id}">client.crawl.<a href="./src/nimble_python/resources/crawl.py">terminate</a>(id) -> <a href="./src/nimble_python/types/crawl_terminate_response.py">CrawlTerminateResponse</a></code>
