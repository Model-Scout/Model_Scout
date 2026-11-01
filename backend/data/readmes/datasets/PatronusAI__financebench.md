---
license: cc-by-nc-4.0
---
[FinanceBench](https://hf.co/papers/2311.11944) is a first-of-its-kind test suite for evaluating the performance of LLMs on open book financial question answering (QA). This is an open source sample of 150 annotated examples used in the evaluation and analysis of models assessed in the FinanceBench paper.

The PDFs linked in the dataset can be found here as well: [https://github.com/patronus-ai/financebench/tree/main/pdfs](https://github.com/patronus-ai/financebench/tree/main/pdfs)

The dataset comprises of questions about publicly traded companies, with corresponding answers and evidence strings. The questions in FinanceBench are ecologically valid and cover a diverse set of scenarios. They are intended to be clear-cut and straightforward to answer to serve as a minimum performance standard.

We test 16 state of the art model configurations (including GPT-4-Turbo, Llama2 and Claude2, with vector stores and long context prompts) on a sample of 150 cases from FinanceBench, and manually review their answers (n=2,400). The cases are available open-source.

We find that existing LLMs have clear limitations for financial QA. All models assessed exhibit weaknesses, such as hallucinations, that limit their suitability for use by enterprises.

To evaluate your models on the full dataset, or if you have questions about this work, you can email us at contact@patronus.ai