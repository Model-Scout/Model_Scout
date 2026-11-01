---
license: unknown
task_categories:
- text-generation
language:
- en
tags:
- synthetic
pretty_name: ChatGPT-4o Writing Prompts
size_categories:
- 1K<n<10K
configs:
- config_name: default
  data_files:
  - split: train
    path:
    - "chatgpt4o-writing-prompts-sharegpt.jsonl"
---

## ChatGPT-4o Writing Prompts
This is a dataset containing 3746 short stories, generated with OpenAI's `chatgpt-4o-latest` model and using Reddit's Writing Prompts subreddit as a source. Each sample is generally between 6000-8000 characters long.

These stories were thoroughly cleaned and then further enriched with a title and a series of applicable genres.  

Note that I did not touch the Markdown ChatGPT-4o produced by itself to enrich its output, as I very much enjoy the added flavour of it.  

**Two files are included:**
- A ShareGPT dataset, ready to be used for training.
- A "raw" version, containing prompt/title/genre/story columns.

If you find any errors, please let me know!