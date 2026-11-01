---
license: other
language:
- ko
- en
task_categories:
- text-generation
private: true
---

# Keural Web Dataset

Internal training corpus collected via compliant crawling.

## Intended Use
- Internal AI model training
- Dataset backup

## Schema
- `section`: type of web content (web, news, blogs)
- `title`: title of the web page
- `url`: URL link of web page
- `text`: raw text content of web page
- `language`: language of web page (KO / EN)
- `query`: query used to crawl the web page
- `engine`: search engine used to find the page (Google / Naver)
- `page_num`: search engine results page number
