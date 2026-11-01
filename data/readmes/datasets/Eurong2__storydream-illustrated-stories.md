---
language:
- ko
- en
task_categories:
- image-to-text
- text-to-image
tags:
- storytelling
- children-stories
- illustrations
- graded-readers
size_categories:
- 10K<n<100K
---

# StoryDream — Illustrated Graded Stories (KO / EN)

11,680 illustrated story pages across 50 story/language combinations, each page
pairing an image with its story text. Every story is available at three reading
levels and split into three narrative parts.

## Structure

```
{language}/{story_id}/level_{level}/{part_type}/page_{page_num}.jpg
metadata.csv
```

- `language` — `ko` or `en`
- `story_id` — original story id (25 stories per language)
- `level` — `1`, `2`, `3` (reading difficulty; 1 is easiest)
- `part_type` — `intro`, `body`, `conclusion`
- `page_num` — 1-based page number, restarting within each part

## Fields in `metadata.csv`

| column | description |
|---|---|
| `file_name` | image path, relative to the repo root |
| `language` | `ko` or `en` |
| `story_id` | original story id |
| `title` | story title |
| `level` | reading level `1`–`3` |
| `part_type` | `intro` / `body` / `conclusion` |
| `page_num` | page number within the part |
| `text` | story text for this page |
| `text_version` | see *Korean text versions* below |
| `borrowed_image` | `true` if the image was carried over from the previous page |

## Loading

```python
from datasets import load_dataset

ds = load_dataset("imagefolder", data_dir="path/to/repo", split="train")
print(ds[0]["image"], ds[0]["text"])
```

## Known caveats

Read these before training on the pairs.

**Korean text versions.** The source spreadsheet contained *two* different
Korean texts for every `(story, level, part)` slot, both pointing at the same
image. The two are not paraphrases — they narrate different beats of the story,
so at most one of them matches what is actually drawn. This release keeps the
second version (`text_version = v2`) for all 2,602 Korean pages that have one.
The image–text alignment on the Korean split should therefore be treated as
unverified.

**145 Korean pages have no text.** These slots existed only in the discarded
first version, so the image is included with an empty `text` and
`text_version = none`.

**34 pages reuse the previous page's image.** The source data had no image for
these pages, so the preceding page's image was carried forward. They are marked
with `borrowed_image = true`. Five of them borrowed across a part boundary
(the blank page was page 1 of its part), so their image belongs to the end of
the previous part.

**English split.** All 8,933 English rows were unique with no version conflict;
`text_version` is empty for them.

## Provenance

Texts are level-adapted retellings of classic public-domain stories
(e.g. *Alice's Adventures in Wonderland*, *The Frog Prince*); illustrations were
generated for this dataset.
