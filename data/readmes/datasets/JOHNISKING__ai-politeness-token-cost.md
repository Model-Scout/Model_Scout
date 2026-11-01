---
license: cc-by-4.0
language:
- en
- ko
- ja
tags:
- politeness
- tokenization
- llm-cost
- multilingual
pretty_name: "Does being polite to AI cost more? Plain, polite and very polite prompts in Korean, Japanese and English"
size_categories:
- n<1K
configs:
- config_name: default
  data_files: ai-politeness-token-cost.csv
---

# Does being polite to AI cost more? Plain, polite and very polite prompts in Korean, Japanese and English

10 everyday requests at four politeness levels in Korean, Japanese and English sent to Claude Opus 5.5 and Haiku 5.5, with GPT token counts. The most polite version needs 114-162% more prompt tokens but cost only 0-4% more in total.

- Page with method, findings and limitations: https://tokensave.app/data/ai-politeness-token-cost
- Zenodo (DOI): https://doi.org/10.5281/zenodo.23489481 (record https://zenodo.org/records/23489482)
- GitHub: https://github.com/johnisking/token-cost-by-language

Measured 2026-10-20 by TokenSave. License CC BY 4.0. In raw logs the PC user name is replaced by USER.

## Citation

TokenSave (2026). Does being polite to AI cost more? Plain, polite and very polite prompts in Korean, Japanese and English [Data set]. Zenodo. https://doi.org/10.5281/zenodo.23489481
