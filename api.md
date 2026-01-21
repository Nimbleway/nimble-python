# Nimbleway

Types:

```python
from nimbleway.types import ExtractResponse, ExtractTemplateResponse
```

Methods:

- <code title="post /v1/extract">client.<a href="./src/nimbleway/_client.py">extract</a>(\*\*<a href="src/nimbleway/types/client_extract_params.py">params</a>) -> <a href="./src/nimbleway/types/extract_response.py">ExtractResponse</a></code>
- <code title="post /v1/extract-template">client.<a href="./src/nimbleway/_client.py">extract_template</a>(\*\*<a href="src/nimbleway/types/client_extract_template_params.py">params</a>) -> <a href="./src/nimbleway/types/extract_template_response.py">ExtractTemplateResponse</a></code>

# Crawl

Types:

```python
from nimbleway.types import (
    CrawlListResponse,
    CrawlRootResponse,
    CrawlStatusResponse,
    CrawlTerminateResponse,
)
```

Methods:

- <code title="get /v1/crawl?status={status}">client.crawl.<a href="./src/nimbleway/resources/crawl.py">list</a>(path_status, \*\*<a href="src/nimbleway/types/crawl_list_params.py">params</a>) -> <a href="./src/nimbleway/types/crawl_list_response.py">CrawlListResponse</a></code>
- <code title="post /v1/crawl">client.crawl.<a href="./src/nimbleway/resources/crawl.py">root</a>(\*\*<a href="src/nimbleway/types/crawl_root_params.py">params</a>) -> <a href="./src/nimbleway/types/crawl_root_response.py">CrawlRootResponse</a></code>
- <code title="get /v1/crawl/{id}">client.crawl.<a href="./src/nimbleway/resources/crawl.py">status</a>(id) -> <a href="./src/nimbleway/types/crawl_status_response.py">CrawlStatusResponse</a></code>
- <code title="delete /v1/crawl/{id}">client.crawl.<a href="./src/nimbleway/resources/crawl.py">terminate</a>(id) -> <a href="./src/nimbleway/types/crawl_terminate_response.py">CrawlTerminateResponse</a></code>
