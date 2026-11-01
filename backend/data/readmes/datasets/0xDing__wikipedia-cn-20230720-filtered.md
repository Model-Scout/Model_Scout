---
license: cc-by-sa-3.0
task_categories:
- text-generation
language:
- zh
tags:
- wikipedia
size_categories:
- 100K<n<1M
---

本数据集基于中文维基2023年7月20日的dump存档。作为一项以数据为中心的工作，本数据集仅保留了 `254,547条` 质量较高的词条内容。具体而言：
* 过滤了Template, Category, Wikipedia, File, Topic, Portal, MediaWiki, Draft, Help等特殊类型的词条
* 使用启发式的方法和自有的NLU模型过滤了一部分质量较低的词条
* 过滤了一部分内容较为敏感或存在争议性的词条。
* 进行了简繁转换和习惯用词转换，确保符合中国大陆地区的习惯用词。


This dataset is based on the Chinese Wikipedia dump archive from July 20th, 2023. As a data-centric effort, the dataset retains `254,574` high-quality entries. Specifically:
* Entries of special types such as Template, Category, Wikipedia, File, Topic, Portal, MediaWiki, Draft, and Help have been filtered out.
* A heuristic approach and proprietary NLU models have been used to filter out some low-quality entries.
* Entries with sensitive or controversial content have also been filtered out.
* To ensure compliance with language usage in mainland China, the dataset underwent conversions from simplified to traditional Chinese, as well as colloquial language conversions.
