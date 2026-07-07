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
    AgentGenerateResponse,
    AgentGetResponse,
    AgentGetGenerationResponse,
    AgentRunResponse,
    AgentRunAsyncResponse,
    AgentRunBatchResponse,
)
```

Methods:

- <code title="get /v1/agents">client.agent.<a href="./src/nimble_python/resources/agent.py">list</a>(\*\*<a href="src/nimble_python/types/agent_list_params.py">params</a>) -> <a href="./src/nimble_python/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="post /v1/agents/generations">client.agent.<a href="./src/nimble_python/resources/agent.py">generate</a>(\*\*<a href="src/nimble_python/types/agent_generate_params.py">params</a>) -> <a href="./src/nimble_python/types/agent_generate_response.py">AgentGenerateResponse</a></code>
- <code title="get /v1/agents/{template_name}">client.agent.<a href="./src/nimble_python/resources/agent.py">get</a>(template_name) -> <a href="./src/nimble_python/types/agent_get_response.py">AgentGetResponse</a></code>
- <code title="get /v1/agents/generations/{generation_id}">client.agent.<a href="./src/nimble_python/resources/agent.py">get_generation</a>(generation_id) -> <a href="./src/nimble_python/types/agent_get_generation_response.py">AgentGetGenerationResponse</a></code>
- <code title="post /v1/agents/run">client.agent.<a href="./src/nimble_python/resources/agent.py">run</a>(\*\*<a href="src/nimble_python/types/agent_run_params.py">params</a>) -> <a href="./src/nimble_python/types/agent_run_response.py">AgentRunResponse</a></code>
- <code title="post /v1/agents/async">client.agent.<a href="./src/nimble_python/resources/agent.py">run_async</a>(\*\*<a href="src/nimble_python/types/agent_run_async_params.py">params</a>) -> <a href="./src/nimble_python/types/agent_run_async_response.py">AgentRunAsyncResponse</a></code>
- <code title="post /v1/agents/batch">client.agent.<a href="./src/nimble_python/resources/agent.py">run_batch</a>(\*\*<a href="src/nimble_python/types/agent_run_batch_params.py">params</a>) -> <a href="./src/nimble_python/types/agent_run_batch_response.py">AgentRunBatchResponse</a></code>

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

# Batches

Types:

```python
from nimble_python.types import BatchGetResponse, BatchProgressResponse
```

Methods:

- <code title="get /v1/batches">client.batches.<a href="./src/nimble_python/resources/batches.py">list</a>() -> None</code>
- <code title="get /v1/batches/{batch_id}">client.batches.<a href="./src/nimble_python/resources/batches.py">get</a>(batch_id) -> <a href="./src/nimble_python/types/batch_get_response.py">BatchGetResponse</a></code>
- <code title="get /v1/batches/{batch_id}/progress">client.batches.<a href="./src/nimble_python/resources/batches.py">progress</a>(batch_id) -> <a href="./src/nimble_python/types/batch_progress_response.py">BatchProgressResponse</a></code>

# DomainKnowledge

Types:

```python
from nimble_python.types import DomainKnowledgeGetDriverResponse
```

Methods:

- <code title="get /v1/domain-knowledge/driver">client.domain_knowledge.<a href="./src/nimble_python/resources/domain_knowledge.py">get_driver</a>(\*\*<a href="src/nimble_python/types/domain_knowledge_get_driver_params.py">params</a>) -> <a href="./src/nimble_python/types/domain_knowledge_get_driver_response.py">DomainKnowledgeGetDriverResponse</a></code>

# Media

Types:

```python
from nimble_python.types import MediaRunResponse, MediaRunAsyncResponse
```

Methods:

- <code title="post /v1/media">client.media.<a href="./src/nimble_python/resources/media.py">run</a>(\*\*<a href="src/nimble_python/types/media_run_params.py">params</a>) -> <a href="./src/nimble_python/types/media_run_response.py">MediaRunResponse</a></code>
- <code title="post /v1/media/async">client.media.<a href="./src/nimble_python/resources/media.py">run_async</a>(\*\*<a href="src/nimble_python/types/media_run_async_params.py">params</a>) -> <a href="./src/nimble_python/types/media_run_async_response.py">MediaRunAsyncResponse</a></code>

# Serp

Types:

```python
from nimble_python.types import SerpRunResponse, SerpRunAsyncResponse, SerpRunBatchResponse
```

Methods:

- <code title="post /v1/serp">client.serp.<a href="./src/nimble_python/resources/serp.py">run</a>(\*\*<a href="src/nimble_python/types/serp_run_params.py">params</a>) -> <a href="./src/nimble_python/types/serp_run_response.py">SerpRunResponse</a></code>
- <code title="post /v1/serp/async">client.serp.<a href="./src/nimble_python/resources/serp.py">run_async</a>(\*\*<a href="src/nimble_python/types/serp_run_async_params.py">params</a>) -> <a href="./src/nimble_python/types/serp_run_async_response.py">SerpRunAsyncResponse</a></code>
- <code title="post /v1/serp/batch">client.serp.<a href="./src/nimble_python/resources/serp.py">run_batch</a>(\*\*<a href="src/nimble_python/types/serp_run_batch_params.py">params</a>) -> <a href="./src/nimble_python/types/serp_run_batch_response.py">SerpRunBatchResponse</a></code>

# TaskAgent

Types:

```python
from nimble_python.types import (
    TaskAgentCreateResponse,
    TaskAgentUpdateResponse,
    TaskAgentListResponse,
    TaskAgentGetResponse,
    TaskAgentRunResponse,
)
```

Methods:

- <code title="post /v1/task-agents">client.task_agent.<a href="./src/nimble_python/resources/task_agent/task_agent.py">create</a>(\*\*<a href="src/nimble_python/types/task_agent_create_params.py">params</a>) -> <a href="./src/nimble_python/types/task_agent_create_response.py">TaskAgentCreateResponse</a></code>
- <code title="patch /v1/task-agents/{agent_id}">client.task_agent.<a href="./src/nimble_python/resources/task_agent/task_agent.py">update</a>(agent_id, \*\*<a href="src/nimble_python/types/task_agent_update_params.py">params</a>) -> <a href="./src/nimble_python/types/task_agent_update_response.py">TaskAgentUpdateResponse</a></code>
- <code title="get /v1/task-agents">client.task_agent.<a href="./src/nimble_python/resources/task_agent/task_agent.py">list</a>(\*\*<a href="src/nimble_python/types/task_agent_list_params.py">params</a>) -> <a href="./src/nimble_python/types/task_agent_list_response.py">TaskAgentListResponse</a></code>
- <code title="delete /v1/task-agents/{agent_id}">client.task_agent.<a href="./src/nimble_python/resources/task_agent/task_agent.py">deactivate</a>(agent_id) -> None</code>
- <code title="get /v1/task-agents/{agent_id}">client.task_agent.<a href="./src/nimble_python/resources/task_agent/task_agent.py">get</a>(agent_id) -> <a href="./src/nimble_python/types/task_agent_get_response.py">TaskAgentGetResponse</a></code>
- <code title="post /v1/task-agents/{agent_id}/runs">client.task_agent.<a href="./src/nimble_python/resources/task_agent/task_agent.py">run</a>(agent_id, \*\*<a href="src/nimble_python/types/task_agent_run_params.py">params</a>) -> <a href="./src/nimble_python/types/task_agent_run_response.py">TaskAgentRunResponse</a></code>

## Templates

Types:

```python
from nimble_python.types.task_agent import TemplateListResponse, TemplateGetResponse
```

Methods:

- <code title="get /v1/task-agents/templates">client.task_agent.templates.<a href="./src/nimble_python/resources/task_agent/templates.py">list</a>(\*\*<a href="src/nimble_python/types/task_agent/template_list_params.py">params</a>) -> <a href="./src/nimble_python/types/task_agent/template_list_response.py">TemplateListResponse</a></code>
- <code title="get /v1/task-agents/templates/{template_name}">client.task_agent.templates.<a href="./src/nimble_python/resources/task_agent/templates.py">get</a>(template_name) -> <a href="./src/nimble_python/types/task_agent/template_get_response.py">TemplateGetResponse</a></code>

## Runs

Types:

```python
from nimble_python.types.task_agent import RunListResponse, RunGetResponse, RunGetResultResponse
```

Methods:

- <code title="get /v1/task-agents/{agent_id}/runs">client.task_agent.runs.<a href="./src/nimble_python/resources/task_agent/runs.py">list</a>(agent_id, \*\*<a href="src/nimble_python/types/task_agent/run_list_params.py">params</a>) -> <a href="./src/nimble_python/types/task_agent/run_list_response.py">RunListResponse</a></code>
- <code title="post /v1/task-agents/{agent_id}/runs/{run_id}/cancel">client.task_agent.runs.<a href="./src/nimble_python/resources/task_agent/runs.py">cancel</a>(run_id, \*, agent_id) -> None</code>
- <code title="get /v1/task-agents/{agent_id}/runs/{run_id}">client.task_agent.runs.<a href="./src/nimble_python/resources/task_agent/runs.py">get</a>(run_id, \*, agent_id) -> <a href="./src/nimble_python/types/task_agent/run_get_response.py">RunGetResponse</a></code>
- <code title="get /v1/task-agents/{agent_id}/runs/{run_id}/result">client.task_agent.runs.<a href="./src/nimble_python/resources/task_agent/runs.py">get_result</a>(run_id, \*, agent_id) -> <a href="./src/nimble_python/types/task_agent/run_get_result_response.py">RunGetResultResponse</a></code>
- <code title="get /v1/task-agents/{agent_id}/runs/{run_id}/events">client.task_agent.runs.<a href="./src/nimble_python/resources/task_agent/runs.py">stream_events</a>(run_id, \*, agent_id) -> object</code>

# Jobs

Types:

```python
from nimble_python.types import (
    JobCreateResponse,
    JobUpdateResponse,
    JobListResponse,
    JobGetResponse,
    JobRunResponse,
)
```

Methods:

- <code title="post /v1/jobs">client.jobs.<a href="./src/nimble_python/resources/jobs/jobs.py">create</a>(\*\*<a href="src/nimble_python/types/job_create_params.py">params</a>) -> <a href="./src/nimble_python/types/job_create_response.py">JobCreateResponse</a></code>
- <code title="patch /v1/jobs/{job_id}">client.jobs.<a href="./src/nimble_python/resources/jobs/jobs.py">update</a>(job_id, \*\*<a href="src/nimble_python/types/job_update_params.py">params</a>) -> <a href="./src/nimble_python/types/job_update_response.py">JobUpdateResponse</a></code>
- <code title="get /v1/jobs">client.jobs.<a href="./src/nimble_python/resources/jobs/jobs.py">list</a>(\*\*<a href="src/nimble_python/types/job_list_params.py">params</a>) -> <a href="./src/nimble_python/types/job_list_response.py">JobListResponse</a></code>
- <code title="delete /v1/jobs/{job_id}">client.jobs.<a href="./src/nimble_python/resources/jobs/jobs.py">delete</a>(job_id) -> None</code>
- <code title="get /v1/jobs/{job_id}">client.jobs.<a href="./src/nimble_python/resources/jobs/jobs.py">get</a>(job_id) -> <a href="./src/nimble_python/types/job_get_response.py">JobGetResponse</a></code>
- <code title="post /v1/jobs/{job_id}/runs">client.jobs.<a href="./src/nimble_python/resources/jobs/jobs.py">run</a>(job_id) -> <a href="./src/nimble_python/types/job_run_response.py">JobRunResponse</a></code>

## Runs

Types:

```python
from nimble_python.types.jobs import RunListResponse, RunCancelResponse, RunGetResponse
```

Methods:

- <code title="get /v1/jobs/{job_id}/runs">client.jobs.runs.<a href="./src/nimble_python/resources/jobs/runs/runs.py">list</a>(job_id, \*\*<a href="src/nimble_python/types/jobs/run_list_params.py">params</a>) -> <a href="./src/nimble_python/types/jobs/run_list_response.py">RunListResponse</a></code>
- <code title="post /v1/jobs/runs/{run_id}/cancel">client.jobs.runs.<a href="./src/nimble_python/resources/jobs/runs/runs.py">cancel</a>(run_id) -> <a href="./src/nimble_python/types/jobs/run_cancel_response.py">RunCancelResponse</a></code>
- <code title="get /v1/jobs/runs/{run_id}">client.jobs.runs.<a href="./src/nimble_python/resources/jobs/runs/runs.py">get</a>(run_id) -> <a href="./src/nimble_python/types/jobs/run_get_response.py">RunGetResponse</a></code>

### Artifacts

Types:

```python
from nimble_python.types.jobs.runs import (
    ArtifactListResponse,
    ArtifactDownloadURLResponse,
    ArtifactGetResponse,
    ArtifactPreviewResponse,
)
```

Methods:

- <code title="get /v1/jobs/runs/{run_id}/artifacts">client.jobs.runs.artifacts.<a href="./src/nimble_python/resources/jobs/runs/artifacts.py">list</a>(run_id) -> <a href="./src/nimble_python/types/jobs/runs/artifact_list_response.py">ArtifactListResponse</a></code>
- <code title="get /v1/jobs/runs/{run_id}/artifacts/{artifact_id}/download-url">client.jobs.runs.artifacts.<a href="./src/nimble_python/resources/jobs/runs/artifacts.py">download_url</a>(artifact_id, \*, run_id) -> <a href="./src/nimble_python/types/jobs/runs/artifact_download_url_response.py">ArtifactDownloadURLResponse</a></code>
- <code title="get /v1/jobs/runs/{run_id}/artifacts/{artifact_id}">client.jobs.runs.artifacts.<a href="./src/nimble_python/resources/jobs/runs/artifacts.py">get</a>(artifact_id, \*, run_id) -> <a href="./src/nimble_python/types/jobs/runs/artifact_get_response.py">ArtifactGetResponse</a></code>
- <code title="get /v1/jobs/runs/{run_id}/artifacts/{artifact_id}/preview">client.jobs.runs.artifacts.<a href="./src/nimble_python/resources/jobs/runs/artifacts.py">preview</a>(artifact_id, \*, run_id) -> <a href="./src/nimble_python/types/jobs/runs/artifact_preview_response.py">ArtifactPreviewResponse</a></code>
