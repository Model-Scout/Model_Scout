---
license: cc0-1.0
language:
- en
- ja
- es
- de
- fr
- tr
- zh
- pt
- ar
- nl
- ko
- id
- it
- ru
- pl
- fa
- he
- th
- cs
- fi
- uk
- hi
task_categories:
- text-generation
- text-classification
tags:
- chatgpt
- conversation
- scrape
---
# DSULT-Core/ShareGPT-X Filtered Dataset

![image/png](CoverImage.png)

This dataset is a curated subset of [ShareGPT-X](https://huggingface.co/datasets/DSULT-Core/ShareGPT-X), which contains approximately 92,000 one-to-one conversations between humans and ChatGPT, collected from X.com (formerly Twitter). The corpus covers content from January 2024 through May 2025, built entirely from public "share" links posted by users on their timelines.

The file `ChatGPT-Simple_ShareGPT_Full.json` includes the longest sequences of alternating `human` and `gpt` messages within each conversation. Conversations containing certain content types were filtered out, such as:
- Messages with `file-service://` links
- ChatGPT API calls like `search()` and `msearch()`
- Human messages with HTTP(S) links
- Text containing the phrases "information about the original user was redacted" or "this code was redacted"
- Furthermore, URLs, e-mails, and phone numbers were redacted using regex patterns

## Data Format and Added Columns

The dataset preserves the original columns with two additional fields:
- `fasttext_language`: Language classification obtained using the FastText classifier `lid.176.bin` which is much more accurate than the original ChatGPT language annotations (`language`).
- `quality`: A quality score computed using the [agentlans/multilingual-e5-small-quality-v3](https://huggingface.co/agentlans/multilingual-e5-small-quality-v3) model.

The dataset contains entries in multiple languages, with the following counts for the most common ones:

| Language Code   | Number of Rows |
|-----------------|---------------:|
| en (English)    | 30,812         |
| ja (Japanese)   | 20,973         |
| es (Spanish)    | 2,389          |
| de (German)     | 1,510          |
| fr (French)     | 1,488          |
| tr (Turkish)    | 1,329          |
| zh (Chinese)    | 1,275          |
| pt (Portuguese) | 1,170          |
| nl (Dutch)      | 590            |
| ar (Arabic)     | 585            |

All other languages have fewer than 500 rows.

## Limitations
- Some personally identifiable information (PII) may remain, even though the users voluntarily shared their conversations and many secret types were redacted.
- Many conversations are excerpts from longer sessions and so may lose the users' original intended contexts.
- The dataset is unverified and may include fringe opinions, pseudo-intellectual content, and unreliable sources.
- ChatGPT’s responses often avoid directly challenging users’ biases, which can reinforce existing viewpoints.
- The dataset is further shaped by selection bias—both in the types of users who continue to use X and in what those users choose to share publicly.
- There is a notable lack of pop culture or entertainment topics, making the dataset less dynamic or engaging than expected (hence the choice of cover image).
- Conversations are predominantly in English and Japanese, limiting linguistic diversity.
- These limitations are consistent across all languages, not just English.

## Licence

This dataset is released under the Creative Commons Zero 1.0 Universal (CC0 1.0) licence, consistent with the original ShareGPT-X dataset.

Cover picture was modified from the original dataset's cover picture using Google Gemini Nano-Banana.