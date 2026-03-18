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
from nimble_python.types import (
    ExtractResponse,
    ExtractAsyncResponse,
    ExtractBatchResponse,
    MapResponse,
    SearchResponse,
)
```

Methods:

- <code title="post /v1/extract">client.<a href="./src/nimble_python/_client.py">extract</a>(\*\*<a href="src/nimble_python/types/client_extract_params.py">params</a>) -> <a href="./src/nimble_python/types/extract_response.py">ExtractResponse</a></code>
- <code title="post /v1/extract/async">client.<a href="./src/nimble_python/_client.py">extract_async</a>(\*\*<a href="src/nimble_python/types/client_extract_async_params.py">params</a>) -> <a href="./src/nimble_python/types/extract_async_response.py">ExtractAsyncResponse</a></code>
- <code title="post /v1/extract/batch">client.<a href="./src/nimble_python/_client.py">extract_batch</a>(\*\*<a href="src/nimble_python/types/client_extract_batch_params.py">params</a>) -> <a href="./src/nimble_python/types/extract_batch_response.py">ExtractBatchResponse</a></code>
- <code title="post /v1/map">client.<a href="./src/nimble_python/_client.py">map</a>(\*\*<a href="src/nimble_python/types/client_map_params.py">params</a>) -> <a href="./src/nimble_python/types/map_response.py">MapResponse</a></code>
- <code title="post /v1/search">client.<a href="./src/nimble_python/_client.py">search</a>(\*\*<a href="src/nimble_python/types/client_search_params.py">params</a>) -> <a href="./src/nimble_python/types/search_response.py">SearchResponse</a></code>

# Agent

Types:

```python
from nimble_python.types import (
    AgentListResponse,
    AgentGetResponse,
    AgentRunResponse,
    AgentRunAsyncResponse,
)
```

Methods:

- <code title="get /v1/agents">client.agent.<a href="./src/nimble_python/resources/agent.py">list</a>(\*\*<a href="src/nimble_python/types/agent_list_params.py">params</a>) -> <a href="./src/nimble_python/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="get /v1/agents/{template_name}">client.agent.<a href="./src/nimble_python/resources/agent.py">get</a>(template_name) -> <a href="./src/nimble_python/types/agent_get_response.py">AgentGetResponse</a></code>
- <code title="post /v1/agents/run">client.agent.<a href="./src/nimble_python/resources/agent.py">run</a>(\*\*<a href="src/nimble_python/types/agent_run_params.py">params</a>) -> <a href="./src/nimble_python/types/agent_run_response.py">AgentRunResponse</a></code>
- <code title="post /v1/agents/async">client.agent.<a href="./src/nimble_python/resources/agent.py">run_async</a>(\*\*<a href="src/nimble_python/types/agent_run_async_params.py">params</a>) -> <a href="./src/nimble_python/types/agent_run_async_response.py">AgentRunAsyncResponse</a></code>

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

# Tasks

Types:

```python
from nimble_python.types import TaskListResponse, TaskGetResponse, TaskResultsResponse
```

Methods:

- <code title="get /v1/tasks">client.tasks.<a href="./src/nimble_python/resources/tasks.py">list</a>(\*\*<a href="src/nimble_python/types/task_list_params.py">params</a>) -> <a href="./src/nimble_python/types/task_list_response.py">TaskListResponse</a></code>
- <code title="get /v1/tasks/{task_id}">client.tasks.<a href="./src/nimble_python/resources/tasks.py">get</a>(task_id) -> <a href="./src/nimble_python/types/task_get_response.py">TaskGetResponse</a></code>
- <code title="get /v1/tasks/{task_id}/results">client.tasks.<a href="./src/nimble_python/resources/tasks.py">results</a>(task_id) -> <a href="./src/nimble_python/types/task_results_response.py">TaskResultsResponse</a></code>
