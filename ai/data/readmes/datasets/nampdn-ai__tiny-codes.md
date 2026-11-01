---
license: mit
task_categories:
- text-generation
language:
- en
pretty_name: Tiny Codes
size_categories:
- 1M<n<10M
---
# Reasoning with Language and Code

This synthetic dataset is a collection of **1.6 millions short and clear code snippets** that can help LLM models learn how to reason with both natural and programming languages. The dataset covers a wide range of programming languages, such as Python, TypeScript, JavaScript, Ruby, Julia, Rust, C++, Bash, Java, C#, and Go. It also includes two database languages: Cypher (for graph databases) and SQL (for relational databases) in order to study the relationship of entities.

The main goal of this repository is to highlight the importance of **textbook (high education value)** using **code snippets**. All code snippets are carefully written and commented to ensure maximum readability and understandability. Moreover, the use of **if/else control flow** is emphasized to foster the development of effective reasoning skills in LLM models.

This repository is inspired by the paper [Textbooks Are All You Need](https://arxiv.org/abs/2306.11644) and [The Magic of IF](https://aclanthology.org/2023.findings-acl.574.pdf), which shows that LLM models can achieve state-of-the-art results on code-related tasks by training on high-quality data that resembles textbooks and exercises. This repository aims to provide such data for data analysts and ML engineers who want to enhance their knowledge of how LLM models can learn to reason with code. Anyone who wants to reproduce this dataset can use these prompts with other LLM models and compare their results, or you can forge a new prompt from related properties.

*Please note that this dataset is not intended for code-generation purposes, it's intended to boost the reasoning capability of model via logic code.*

I hope you find this dataset useful and informative!

## Tiny Series

Explore the possibilities and limitations of building Small Language Models with these tiny gems of data!

- [TinyStories](https://arxiv.org/abs/2305.07759): The paper that sparked my interest in the journey of the tiny-* series.
- [tiny-textbooks](https://huggingface.co/datasets/nampdn-ai/tiny-textbooks): 420k "things of internet" synthetic textbooks.
- [tiny-orca-textbooks](https://huggingface.co/datasets/nampdn-ai/tiny-orca-textbooks): Synthetic textbook to help model learn in-context on how it should perform task the right way.
- [tiny-webtext](https://huggingface.co/datasets/nampdn-ai/tiny-webtext): A 6GB (4.5M records) variety of diverse webtext enriched with critical thinking methods to make unbiased English dataset.
- [tiny-lessons](https://huggingface.co/datasets/nampdn-ai/tiny-lessons): Subset of [tiny-textbooks](https://huggingface.co/datasets/nampdn-ai/tiny-textbooks) dataset, various lessons about "things of internet" augmented in a bite-sized textbook Markdown format.
- [tiny-bridgedict](https://huggingface.co/datasets/nampdn-ai/tiny-bridgedict): A dataset that links and transfers knowledge between English, Vietnamese, Chinese in a tiny multilingual models.

### Others small HQ datasets with textbook-like quality
- [devdocs.io](https://huggingface.co/datasets/nampdn-ai/devdocs.io): FreeCodeCamp has provided 189k comprehensive API documentation across a wide range of tech stacks and programming languages.
- [sciphi-python-textbook](https://huggingface.co/datasets/emrgnt-cmplxty/sciphi-python-textbook)
- [textbook_quality_programming](https://huggingface.co/datasets/vikp/textbook_quality_programming)
- [sciphi-textbooks-are-all-you-need](https://huggingface.co/datasets/emrgnt-cmplxty/sciphi-textbooks-are-all-you-need)