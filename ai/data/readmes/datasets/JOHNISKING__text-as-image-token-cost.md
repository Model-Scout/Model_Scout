---
license: cc-by-4.0
language:
- en
- ko
- ja
pretty_name: Text as images to cut AI tokens (pxpipe on Claude)
tags:
- tokens
- pxpipe
- vision
- context-compression
- claude
- claude-code
size_categories:
- n<1K
task_categories:
- question-answering
configs:
- config_name: default
  data_files: text-as-image-token-cost.csv
---

# Text as images to cut AI tokens: an independent check of pxpipe on Claude

Measured 2026-10-21 by TokenSave. Page, method, findings and limitations: https://tokensave.app/data/text-as-image-token-cost

Six documents (English, Korean and Japanese prose, JavaScript source, a generated JSON response, a generated 230-line server log) were sent to Claude Haiku 5.5, Sonnet 5.5, Opus 5.5 and Fable 5.1 through Claude Code 2.1.295 as plain text, as pxpipe-proxy 0.15.0 output (page images + factsheet) and as images only. 2 runs each, 144 calls.

- Input tokens fell 64% to 81% versus plain text (Korean prose -77%, Japanese -73%, English -64%).
- As text, every model answered every item correctly.
- Through pxpipe, ids that were not in pxpipe's factsheet were read 0 of 80 times; Opus 5.5 got 44 of 60 planted numbers right.

One row per call: input tokens over a question-only baseline, and correct / wrong / null counts per item type (planted ids, planted numbers, other ids, other numbers).

Corpus, rendered pages, raw answers and scripts: https://github.com/johnisking/token-cost-by-language/tree/main/text-as-image

License: CC BY 4.0. Cite as: TokenSave (2026). Text as images to cut AI tokens: an independent check of pxpipe on Claude [Data set]. https://tokensave.app/data/text-as-image-token-cost
