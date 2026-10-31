---
pretty_name: OSS Documentation Collection
language:
  - cn
  - de
  - en
  - es
  - fa
  - ja
  - ko
  - pt
tags:
  - documentation
  - software-engineering
  - open-source
  - programming
task_categories:
  - text-retrieval
  - text-generation
---

# OSS Documentation Collection

A daily snapshot of selected open-source software documentation collected by oss-docs-collect.

## Dataset

- Documents: 1783
- Repositories: 14
- Generated: 2026-10-28T22:20:24.360Z
- Format: JSONL

## Schema

- id: stable document identifier
- repo: source repository
- path: source path
- title: extracted document title
- content: Markdown/MDX source
- language: configured document language
- license: source license
- license_url: license reference when configured
- source_url: source project URL
- github_url: exact source file at the collected commit when available
- commit: source repository commit
- collected_at: collection timestamp

## Licensing

This dataset contains documentation from multiple projects. Each document retains the license declared for its source project. Check the individual source license before redistribution or downstream use.
