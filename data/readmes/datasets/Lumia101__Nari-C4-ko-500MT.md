---
license: cc-by-4.0
task_categories:
- text-generation
language:
- ko
size_categories:
- 100K<n<1M
---

# Lumia101/Nari-C4-ko-500MT

This dataset is a modified version of [C4 dataset(multilingual, ko subset)](https://huggingface.co/datasets/allenai/c4) made more useful for LLM training by applying additional filtering.

Since the number of tokens is only about 500M, it is recommended to mix it with other high-quality datasets.

# Additional filtering methods used

* **Phase 1**: Text normalization
* **Phase 2**: Remove HTML-filled junk documents
* **Phase 3**: Remove documents containing a lot of broken characters
* **Phase 4**: Remove documents containing harmful elements such as NSFW
* **Phase 5**: Remove documents with excessive email addresses, phone numbers, and links
* **Phase 6**: Remove documents with many repetitive phrases, low information content, or table-like structures.
* **Phase 7**: Extract only high-quality data using FastText

# Quality Statistics

**Chatacter length**

| | Nari-C4 | mC4(ko) | Fineweb-2(kor_Hang) |
|--------------|:--------|---------|---------------------|
| Sample count | 5000 | 5000 | 5000 |
| Average character length | 4046.53 | 3093.21 | 1318.49 |
| Median character length | 3033 | 1822 | 589 |
| Top 90% character length | 1757.70 | 187.90 | 263.00 |
| Top 75% character length | 2123.75 | 624.75 | 322.00 |
| Top 25% character length | 4894.75 | 3405.25 | 1393.00 |
| Top 10% character length | 6892.30 | 6074.70 | 2773.70 |
| Top 1% character length | 18446.7400 | 28362.29 | 10927.16 |

**Word count**

| | Nari-C4 | mC4(ko) | Fineweb-2(kor_Hang) |
|--------------|:--------|---------|---------------------|
| Average word count | 807.51 | 523.63 | 287.53 |
| Median word count | 641 | 341 | 128 |

**Letter ratio**

| | Nari-C4 | mC4(ko) | Fineweb-2(kor_Hang) |
|--------------|:--------|---------|---------------------|
| Average Korean ratio | 63.97 | 54.32 | 57.98 |
| Average Latin ratio | 3.98 | 11.76 | 11.75 |
| Average digit ratio | 4.97 | 6.55 | 2.87 |
| Average Symbol Ratio | 5.18 | 7.30 | 5.47 |

**Low quality documents**

| | Nari-C4 | mC4(ko) | Fineweb-2(kor_Hang) |
|--------------|:--------|---------|---------------------|
| Document with URL | 14.68 | 15.56 | 10.38 |
| Document with HTML | 0.96 | 12.12 | 5.78 |
| Document with Repeating Character | 3.98 | 5.9 | 3.28 |
| Document with Menu Keywords | 24.76 | 27.46 | 16.76 |