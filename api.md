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

- <code title="post /v2/map">client.<a href="./src/nimble_python/_client.py">map</a>(\*\*<a href="src/nimble_python/types/client_map_params.py">params</a>) -> <a href="./src/nimble_python/types/map_response.py">MapResponse</a></code>
- <code title="post /v2/search">client.<a href="./src/nimble_python/_client.py">search</a>(\*\*<a href="src/nimble_python/types/client_search_params.py">params</a>) -> <a href="./src/nimble_python/types/search_response.py">SearchResponse</a></code>

# Extract

Types:

```python
from nimble_python.types import ExtractAsyncResponse, ExtractBatchResponse, ExtractRunResponse
```

Methods:

- <code title="post /v2/extract/async">client.extract.<a href="./src/nimble_python/resources/extract/extract.py">async\_</a>(\*\*<a href="src/nimble_python/types/extract_async_params.py">params</a>) -> <a href="./src/nimble_python/types/extract_async_response.py">ExtractAsyncResponse</a></code>
- <code title="post /v2/extract/batch">client.extract.<a href="./src/nimble_python/resources/extract/extract.py">batch</a>(\*\*<a href="src/nimble_python/types/extract_batch_params.py">params</a>) -> <a href="./src/nimble_python/types/extract_batch_response.py">ExtractBatchResponse</a></code>
- <code title="post /v2/extract">client.extract.<a href="./src/nimble_python/resources/extract/extract.py">run</a>(\*\*<a href="src/nimble_python/types/extract_run_params.py">params</a>) -> <a href="./src/nimble_python/types/extract_run_response.py">ExtractRunResponse</a></code>

## Templates

Types:

```python
from nimble_python.types.extract import (
    TemplateUpdateResponse,
    TemplateListResponse,
    TemplateAsyncResponse,
    TemplateBatchResponse,
    TemplateGetResponse,
    TemplateRunResponse,
)
```

Methods:

- <code title="patch /v2/extract/templates/{extract_template_name}">client.extract.templates.<a href="./src/nimble_python/resources/extract/templates/templates.py">update</a>(extract_template_name, \*\*<a href="src/nimble_python/types/extract/template_update_params.py">params</a>) -> <a href="./src/nimble_python/types/extract/template_update_response.py">TemplateUpdateResponse</a></code>
- <code title="get /v2/extract/templates">client.extract.templates.<a href="./src/nimble_python/resources/extract/templates/templates.py">list</a>(\*\*<a href="src/nimble_python/types/extract/template_list_params.py">params</a>) -> <a href="./src/nimble_python/types/extract/template_list_response.py">TemplateListResponse</a></code>
- <code title="delete /v2/extract/templates/{extract_template_name}">client.extract.templates.<a href="./src/nimble_python/resources/extract/templates/templates.py">delete</a>(extract_template_name) -> None</code>
- <code title="post /v2/extract/templates/async">client.extract.templates.<a href="./src/nimble_python/resources/extract/templates/templates.py">async\_</a>(\*\*<a href="src/nimble_python/types/extract/template_async_params.py">params</a>) -> <a href="./src/nimble_python/types/extract/template_async_response.py">TemplateAsyncResponse</a></code>
- <code title="post /v2/extract/templates/batch">client.extract.templates.<a href="./src/nimble_python/resources/extract/templates/templates.py">batch</a>(\*\*<a href="src/nimble_python/types/extract/template_batch_params.py">params</a>) -> <a href="./src/nimble_python/types/extract/template_batch_response.py">TemplateBatchResponse</a></code>
- <code title="get /v2/extract/templates/{extract_template_name}">client.extract.templates.<a href="./src/nimble_python/resources/extract/templates/templates.py">get</a>(extract_template_name) -> <a href="./src/nimble_python/types/extract/template_get_response.py">TemplateGetResponse</a></code>
- <code title="post /v2/extract/templates/run">client.extract.templates.<a href="./src/nimble_python/resources/extract/templates/templates.py">run</a>(\*\*<a href="src/nimble_python/types/extract/template_run_params.py">params</a>) -> <a href="./src/nimble_python/types/extract/template_run_response.py">TemplateRunResponse</a></code>

### Generations

Types:

```python
from nimble_python.types.extract.templates import GenerationCreateResponse, GenerationGetResponse
```

Methods:

- <code title="post /v2/extract/templates/generations">client.extract.templates.generations.<a href="./src/nimble_python/resources/extract/templates/generations.py">create</a>(\*\*<a href="src/nimble_python/types/extract/templates/generation_create_params.py">params</a>) -> <a href="./src/nimble_python/types/extract/templates/generation_create_response.py">GenerationCreateResponse</a></code>
- <code title="get /v2/extract/templates/generations/{generation_id}">client.extract.templates.generations.<a href="./src/nimble_python/resources/extract/templates/generations.py">get</a>(generation_id) -> <a href="./src/nimble_python/types/extract/templates/generation_get_response.py">GenerationGetResponse</a></code>

### Versions

Types:

```python
from nimble_python.types.extract.templates import VersionListResponse, VersionGetResponse
```

Methods:

- <code title="get /v2/extract/templates/{extract_template_name}/versions">client.extract.templates.versions.<a href="./src/nimble_python/resources/extract/templates/versions.py">list</a>(extract_template_name, \*\*<a href="src/nimble_python/types/extract/templates/version_list_params.py">params</a>) -> <a href="./src/nimble_python/types/extract/templates/version_list_response.py">VersionListResponse</a></code>
- <code title="get /v2/extract/templates/{extract_template_name}/versions/{version_id}">client.extract.templates.versions.<a href="./src/nimble_python/resources/extract/templates/versions.py">get</a>(version_id, \*, extract_template_name) -> <a href="./src/nimble_python/types/extract/templates/version_get_response.py">VersionGetResponse</a></code>

# Agents

Types:

```python
from nimble_python.types import (
    AgentCreateResponse,
    AgentUpdateResponse,
    AgentListResponse,
    AgentGetResponse,
)
```

Methods:

- <code title="post /v2/agents">client.agents.<a href="./src/nimble_python/resources/agents/agents.py">create</a>(\*\*<a href="src/nimble_python/types/agent_create_params.py">params</a>) -> <a href="./src/nimble_python/types/agent_create_response.py">AgentCreateResponse</a></code>
- <code title="patch /v2/agents/{agent_id}">client.agents.<a href="./src/nimble_python/resources/agents/agents.py">update</a>(agent_id, \*\*<a href="src/nimble_python/types/agent_update_params.py">params</a>) -> <a href="./src/nimble_python/types/agent_update_response.py">AgentUpdateResponse</a></code>
- <code title="get /v2/agents">client.agents.<a href="./src/nimble_python/resources/agents/agents.py">list</a>(\*\*<a href="src/nimble_python/types/agent_list_params.py">params</a>) -> <a href="./src/nimble_python/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /v2/agents/{agent_id}">client.agents.<a href="./src/nimble_python/resources/agents/agents.py">delete</a>(agent_id) -> None</code>
- <code title="get /v2/agents/{agent_id}">client.agents.<a href="./src/nimble_python/resources/agents/agents.py">get</a>(agent_id) -> <a href="./src/nimble_python/types/agent_get_response.py">AgentGetResponse</a></code>

## Templates

Types:

```python
from nimble_python.types.agents import TemplateListResponse, TemplateGetResponse
```

Methods:

- <code title="get /v2/agents/templates">client.agents.templates.<a href="./src/nimble_python/resources/agents/templates.py">list</a>(\*\*<a href="src/nimble_python/types/agents/template_list_params.py">params</a>) -> <a href="./src/nimble_python/types/agents/template_list_response.py">TemplateListResponse</a></code>
- <code title="get /v2/agents/templates/{template_name}">client.agents.templates.<a href="./src/nimble_python/resources/agents/templates.py">get</a>(template_name) -> <a href="./src/nimble_python/types/agents/template_get_response.py">TemplateGetResponse</a></code>

## Runs

Types:

```python
from nimble_python.types.agents import (
    RunCreateResponse,
    RunListResponse,
    RunGetResponse,
    RunResultResponse,
)
```

Methods:

- <code title="post /v2/agents/{agent_id}/runs">client.agents.runs.<a href="./src/nimble_python/resources/agents/runs.py">create</a>(agent_id, \*\*<a href="src/nimble_python/types/agents/run_create_params.py">params</a>) -> <a href="./src/nimble_python/types/agents/run_create_response.py">RunCreateResponse</a></code>
- <code title="get /v2/agents/{agent_id}/runs">client.agents.runs.<a href="./src/nimble_python/resources/agents/runs.py">list</a>(agent_id, \*\*<a href="src/nimble_python/types/agents/run_list_params.py">params</a>) -> <a href="./src/nimble_python/types/agents/run_list_response.py">RunListResponse</a></code>
- <code title="get /v2/agents/{agent_id}/runs/{run_id}">client.agents.runs.<a href="./src/nimble_python/resources/agents/runs.py">get</a>(run_id, \*, agent_id) -> <a href="./src/nimble_python/types/agents/run_get_response.py">RunGetResponse</a></code>
- <code title="get /v2/agents/{agent_id}/runs/{run_id}/result">client.agents.runs.<a href="./src/nimble_python/resources/agents/runs.py">result</a>(run_id, \*, agent_id) -> <a href="./src/nimble_python/types/agents/run_result_response.py">RunResultResponse</a></code>
- <code title="get /v2/agents/{agent_id}/runs/{run_id}/events">client.agents.runs.<a href="./src/nimble_python/resources/agents/runs.py">stream_events</a>(run_id, \*, agent_id) -> None</code>

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

- <code title="get /v2/crawl">client.crawl.<a href="./src/nimble_python/resources/crawl.py">list</a>(\*\*<a href="src/nimble_python/types/crawl_list_params.py">params</a>) -> <a href="./src/nimble_python/types/crawl_list_response.py">CrawlListResponse</a></code>
- <code title="post /v2/crawl">client.crawl.<a href="./src/nimble_python/resources/crawl.py">run</a>(\*\*<a href="src/nimble_python/types/crawl_run_params.py">params</a>) -> <a href="./src/nimble_python/types/crawl_run_response.py">CrawlRunResponse</a></code>
- <code title="get /v2/crawl/{id}">client.crawl.<a href="./src/nimble_python/resources/crawl.py">status</a>(id) -> <a href="./src/nimble_python/types/crawl_status_response.py">CrawlStatusResponse</a></code>
- <code title="delete /v2/crawl/{id}">client.crawl.<a href="./src/nimble_python/resources/crawl.py">terminate</a>(id) -> <a href="./src/nimble_python/types/crawl_terminate_response.py">CrawlTerminateResponse</a></code>

# Tasks

Types:

```python
from nimble_python.types import TaskListResponse, TaskGetResponse, TaskResultsResponse
```

Methods:

- <code title="get /v2/tasks">client.tasks.<a href="./src/nimble_python/resources/tasks.py">list</a>(\*\*<a href="src/nimble_python/types/task_list_params.py">params</a>) -> <a href="./src/nimble_python/types/task_list_response.py">TaskListResponse</a></code>
- <code title="get /v2/tasks/{task_id}">client.tasks.<a href="./src/nimble_python/resources/tasks.py">get</a>(task_id) -> <a href="./src/nimble_python/types/task_get_response.py">TaskGetResponse</a></code>
- <code title="get /v2/tasks/{task_id}/results">client.tasks.<a href="./src/nimble_python/resources/tasks.py">results</a>(task_id) -> <a href="./src/nimble_python/types/task_results_response.py">TaskResultsResponse</a></code>

# Batches

Types:

```python
from nimble_python.types import BatchGetResponse, BatchProgressResponse
```

Methods:

- <code title="get /v2/batches">client.batches.<a href="./src/nimble_python/resources/batches.py">list</a>() -> None</code>
- <code title="get /v2/batches/{batch_id}">client.batches.<a href="./src/nimble_python/resources/batches.py">get</a>(batch_id) -> <a href="./src/nimble_python/types/batch_get_response.py">BatchGetResponse</a></code>
- <code title="get /v2/batches/{batch_id}/progress">client.batches.<a href="./src/nimble_python/resources/batches.py">progress</a>(batch_id) -> <a href="./src/nimble_python/types/batch_progress_response.py">BatchProgressResponse</a></code>

# DomainKnowledge

Types:

```python
from nimble_python.types import DomainKnowledgeGetDriverResponse
```

Methods:

- <code title="get /v2/domain-knowledge/driver">client.domain_knowledge.<a href="./src/nimble_python/resources/domain_knowledge.py">get_driver</a>(\*\*<a href="src/nimble_python/types/domain_knowledge_get_driver_params.py">params</a>) -> <a href="./src/nimble_python/types/domain_knowledge_get_driver_response.py">DomainKnowledgeGetDriverResponse</a></code>

# Media

Types:

```python
from nimble_python.types import MediaRunResponse, MediaRunAsyncResponse
```

Methods:

- <code title="post /v2/media">client.media.<a href="./src/nimble_python/resources/media.py">run</a>(\*\*<a href="src/nimble_python/types/media_run_params.py">params</a>) -> <a href="./src/nimble_python/types/media_run_response.py">MediaRunResponse</a></code>
- <code title="post /v2/media/async">client.media.<a href="./src/nimble_python/resources/media.py">run_async</a>(\*\*<a href="src/nimble_python/types/media_run_async_params.py">params</a>) -> <a href="./src/nimble_python/types/media_run_async_response.py">MediaRunAsyncResponse</a></code>

# Serp

Types:

```python
from nimble_python.types import SerpRunResponse, SerpRunAsyncResponse, SerpRunBatchResponse
```

Methods:

- <code title="post /v2/serp">client.serp.<a href="./src/nimble_python/resources/serp.py">run</a>(\*\*<a href="src/nimble_python/types/serp_run_params.py">params</a>) -> <a href="./src/nimble_python/types/serp_run_response.py">SerpRunResponse</a></code>
- <code title="post /v2/serp/async">client.serp.<a href="./src/nimble_python/resources/serp.py">run_async</a>(\*\*<a href="src/nimble_python/types/serp_run_async_params.py">params</a>) -> <a href="./src/nimble_python/types/serp_run_async_response.py">SerpRunAsyncResponse</a></code>
- <code title="post /v2/serp/batch">client.serp.<a href="./src/nimble_python/resources/serp.py">run_batch</a>(\*\*<a href="src/nimble_python/types/serp_run_batch_params.py">params</a>) -> <a href="./src/nimble_python/types/serp_run_batch_response.py">SerpRunBatchResponse</a></code>

# FastSerp

Types:

```python
from nimble_python.types import FastSerpRunResponse
```

Methods:

- <code title="post /v2/fast-serp">client.fast_serp.<a href="./src/nimble_python/resources/fast_serp.py">run</a>(\*\*<a href="src/nimble_python/types/fast_serp_run_params.py">params</a>) -> <a href="./src/nimble_python/types/fast_serp_run_response.py">FastSerpRunResponse</a></code>

# Jobs

Types:

```python
from nimble_python.types import (
    JobCreateResponse,
    JobUpdateResponse,
    JobListResponse,
    JobGetResponse,
)
```

Methods:

- <code title="post /v2/jobs">client.jobs.<a href="./src/nimble_python/resources/jobs/jobs.py">create</a>(\*\*<a href="src/nimble_python/types/job_create_params.py">params</a>) -> <a href="./src/nimble_python/types/job_create_response.py">JobCreateResponse</a></code>
- <code title="patch /v2/jobs/{job_id}">client.jobs.<a href="./src/nimble_python/resources/jobs/jobs.py">update</a>(job_id, \*\*<a href="src/nimble_python/types/job_update_params.py">params</a>) -> <a href="./src/nimble_python/types/job_update_response.py">JobUpdateResponse</a></code>
- <code title="get /v2/jobs">client.jobs.<a href="./src/nimble_python/resources/jobs/jobs.py">list</a>(\*\*<a href="src/nimble_python/types/job_list_params.py">params</a>) -> <a href="./src/nimble_python/types/job_list_response.py">JobListResponse</a></code>
- <code title="delete /v2/jobs/{job_id}">client.jobs.<a href="./src/nimble_python/resources/jobs/jobs.py">delete</a>(job_id) -> None</code>
- <code title="get /v2/jobs/{job_id}">client.jobs.<a href="./src/nimble_python/resources/jobs/jobs.py">get</a>(job_id) -> <a href="./src/nimble_python/types/job_get_response.py">JobGetResponse</a></code>

## Runs

Types:

```python
from nimble_python.types.jobs import (
    RunCreateResponse,
    RunListResponse,
    RunCancelResponse,
    RunGetResponse,
)
```

Methods:

- <code title="post /v2/jobs/{job_id}/runs">client.jobs.runs.<a href="./src/nimble_python/resources/jobs/runs/runs.py">create</a>(job_id) -> <a href="./src/nimble_python/types/jobs/run_create_response.py">RunCreateResponse</a></code>
- <code title="get /v2/jobs/{job_id}/runs">client.jobs.runs.<a href="./src/nimble_python/resources/jobs/runs/runs.py">list</a>(job_id, \*\*<a href="src/nimble_python/types/jobs/run_list_params.py">params</a>) -> <a href="./src/nimble_python/types/jobs/run_list_response.py">RunListResponse</a></code>
- <code title="post /v2/jobs/runs/{run_id}/cancel">client.jobs.runs.<a href="./src/nimble_python/resources/jobs/runs/runs.py">cancel</a>(run_id) -> <a href="./src/nimble_python/types/jobs/run_cancel_response.py">RunCancelResponse</a></code>
- <code title="get /v2/jobs/runs/{run_id}">client.jobs.runs.<a href="./src/nimble_python/resources/jobs/runs/runs.py">get</a>(run_id) -> <a href="./src/nimble_python/types/jobs/run_get_response.py">RunGetResponse</a></code>

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

- <code title="get /v2/jobs/runs/{run_id}/artifacts">client.jobs.runs.artifacts.<a href="./src/nimble_python/resources/jobs/runs/artifacts.py">list</a>(run_id) -> <a href="./src/nimble_python/types/jobs/runs/artifact_list_response.py">ArtifactListResponse</a></code>
- <code title="get /v2/jobs/runs/{run_id}/artifacts/{artifact_id}/download-url">client.jobs.runs.artifacts.<a href="./src/nimble_python/resources/jobs/runs/artifacts.py">download_url</a>(artifact_id, \*, run_id) -> <a href="./src/nimble_python/types/jobs/runs/artifact_download_url_response.py">ArtifactDownloadURLResponse</a></code>
- <code title="get /v2/jobs/runs/{run_id}/artifacts/{artifact_id}">client.jobs.runs.artifacts.<a href="./src/nimble_python/resources/jobs/runs/artifacts.py">get</a>(artifact_id, \*, run_id) -> <a href="./src/nimble_python/types/jobs/runs/artifact_get_response.py">ArtifactGetResponse</a></code>
- <code title="get /v2/jobs/runs/{run_id}/artifacts/{artifact_id}/preview">client.jobs.runs.artifacts.<a href="./src/nimble_python/resources/jobs/runs/artifacts.py">preview</a>(artifact_id, \*, run_id) -> <a href="./src/nimble_python/types/jobs/runs/artifact_preview_response.py">ArtifactPreviewResponse</a></code>
