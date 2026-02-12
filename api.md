# Nimble

Types:

```python
from nimble_python.types import AgentResponse, CrawlResponse, MapResponse
```

Methods:

- <code title="post /v1/agent">client.<a href="./src/nimble_python/_client.py">agent</a>(\*\*<a href="src/nimble_python/types/client_agent_params.py">params</a>) -> <a href="./src/nimble_python/types/agent_response.py">AgentResponse</a></code>
- <code title="post /v1/crawl">client.<a href="./src/nimble_python/_client.py">crawl</a>(\*\*<a href="src/nimble_python/types/client_crawl_params.py">params</a>) -> <a href="./src/nimble_python/types/crawl_response.py">CrawlResponse</a></code>
- <code title="post /v1/map">client.<a href="./src/nimble_python/_client.py">map</a>(\*\*<a href="src/nimble_python/types/client_map_params.py">params</a>) -> <a href="./src/nimble_python/types/map_response.py">MapResponse</a></code>

# Agents

Types:

```python
from nimble_python.types import AgentListResponse, AgentAsyncResponse, AgentGetResponse
```

Methods:

- <code title="get /v1/agents">client.agents.<a href="./src/nimble_python/resources/agents.py">list</a>(\*\*<a href="src/nimble_python/types/agent_list_params.py">params</a>) -> <a href="./src/nimble_python/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="post /v1/agent/async">client.agents.<a href="./src/nimble_python/resources/agents.py">async\_</a>(\*\*<a href="src/nimble_python/types/agent_async_params.py">params</a>) -> <a href="./src/nimble_python/types/agent_async_response.py">AgentAsyncResponse</a></code>
- <code title="get /v1/agents/{template_name}">client.agents.<a href="./src/nimble_python/resources/agents.py">get</a>(template_name) -> <a href="./src/nimble_python/types/agent_get_response.py">AgentGetResponse</a></code>

# Extract

Types:

```python
from nimble_python.types import ExtractAsyncResponse, ExtractExtractResponse
```

Methods:

- <code title="post /v1/extract/async">client.extract.<a href="./src/nimble_python/resources/extract.py">async\_</a>(\*\*<a href="src/nimble_python/types/extract_async_params.py">params</a>) -> <a href="./src/nimble_python/types/extract_async_response.py">ExtractAsyncResponse</a></code>
- <code title="post /v1/extract">client.extract.<a href="./src/nimble_python/resources/extract.py">extract</a>(\*\*<a href="src/nimble_python/types/extract_extract_params.py">params</a>) -> <a href="./src/nimble_python/types/extract_extract_response.py">ExtractExtractResponse</a></code>

# Crawl

Types:

```python
from nimble_python.types import CrawlListResponse, CrawlStatusResponse, CrawlTerminateResponse
```

Methods:

- <code title="get /v1/crawl">client.crawl.<a href="./src/nimble_python/resources/crawl.py">list</a>(\*\*<a href="src/nimble_python/types/crawl_list_params.py">params</a>) -> <a href="./src/nimble_python/types/crawl_list_response.py">SyncCrawlPagination[CrawlListResponse]</a></code>
- <code title="get /v1/crawl/{id}">client.crawl.<a href="./src/nimble_python/resources/crawl.py">status</a>(id) -> <a href="./src/nimble_python/types/crawl_status_response.py">CrawlStatusResponse</a></code>
- <code title="delete /v1/crawl/{id}">client.crawl.<a href="./src/nimble_python/resources/crawl.py">terminate</a>(id) -> <a href="./src/nimble_python/types/crawl_terminate_response.py">CrawlTerminateResponse</a></code>

# Tasks

Types:

```python
from nimble_python.types import TaskListResponse, TaskGetResponse, TaskResultsResponse
```

Methods:

- <code title="get /v1/tasks">client.tasks.<a href="./src/nimble_python/resources/tasks.py">list</a>(\*\*<a href="src/nimble_python/types/task_list_params.py">params</a>) -> <a href="./src/nimble_python/types/task_list_response.py">SyncCrawlPagination[TaskListResponse]</a></code>
- <code title="get /v1/tasks/{task_id}">client.tasks.<a href="./src/nimble_python/resources/tasks.py">get</a>(task_id) -> <a href="./src/nimble_python/types/task_get_response.py">TaskGetResponse</a></code>
- <code title="get /v1/tasks/{task_id}/results">client.tasks.<a href="./src/nimble_python/resources/tasks.py">results</a>(task_id) -> <a href="./src/nimble_python/types/task_results_response.py">TaskResultsResponse</a></code>
