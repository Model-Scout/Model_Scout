---
pretty_name: VOKU Archive
language:
- ko
license: cc-by-4.0
size_categories:
- 10K<n<100K
tags:
- archives
- korean
- ocr
- historical-documents
- pseudonymization
configs:
- config_name: pages
  default: true
  data_files:
  - split: corpus
    path: data/pages/*.parquet
---

# VOKU Archive

VOKU Archive brings **66,010 pages of student-produced campus radio cue sheets and scripts from 1988–2019** into a form that people can read, search, and study. VOKU (Voice of Kyonggi University) is a student-run university broadcasting station whose work also includes video production and stage and live event production and operation. This collection covers the radio materials within that wider activity.

A former station member made this digital archive independently so that documents created by earlier members would remain readable instead of being left in storage. Alongside redaction, pseudonym tokens were inserted to preserve, where possible, repeated participation by the same producer and collaboration within episodes. The tokens are part of the prepared public images; they were not names written in the historical scripts.

This is a selected surviving archive, not a reconstruction of every broadcast during those years. It contains preparation documents, which do not establish that everything written was performed on air. Scope, exclusions, and known exceptions are collected in the [release notes](RELEASE_NOTES.md#known-exceptions-and-interpretive-limits).

## What is provided

| Material | Content and use |
|---|---|
| Final WebP images | 66,010 pages showing the prepared public version of the documents. Use these to check what is actually displayed. |
| Fresh OCR | Machine-recognized Korean text, lines, confidence values, and coordinates read from those final images. Useful for search, navigation, and subsequent processing; not a human-corrected transcription. |
| Public token annotations | 91,776 records on 25,162 pages, connecting displayed pseudonym tokens to their placement boxes and associated recorded name-removal boxes. |
| Metadata and schemas | Page, episode, and program-unit identifiers; Korean and editorial English titles; image hashes; file locations; field definitions; and validation records. |

The same corpus is supplied as **32 yearly TAR files** for ordinary files and **54 Parquet shards** for page-level access. The TAR files contain 5,330 episode OCR JSON files and 5,330 corresponding annotation JSON files. These are two access forms for the same pages, not separate corpora. [Detailed counts and checks](RELEASE_NOTES.md).

## A page from the archive

![A cue sheet for 여행에 미치다, showing its program heading, production-role tokens, approval area, and music rundown](assets/voku_2017_1_crazy_about_travel_02_page01.webp)

**여행에 미치다 / Crazy About Travel**, 2017, first semester, source episode bundle `02`, page `01`. The English title is an editorial translation. This preview is a byte-identical copy of `images/2017/voku_2017_1_crazy_about_travel_02_page01.webp` inside [the 2017 TAR](archives/voku_2017.tar), not the workflow's synthetic-identifier demo.

Read the program heading, planned broadcast information, production-role line, and music rundown as parts of the document. The role line contains the inserted tokens `물빛수첩`, `물빛결빛`, and `노을노래`. Its annotation page has three token records. The blurred approval area illustrates why token annotations are not a map of every redacted region. [How to read a token record](DATA_GUIDE.md#token-annotations).

## Open one episode

Download [archives/voku_2017.tar](archives/voku_2017.tar). With a working directory containing `archives/`, the following standard-library Python reads one episode directly from the TAR; no conversion or extraction is needed.

```python
import json
import tarfile

document_id = "voku_2017_1_crazy_about_travel_02"
with tarfile.open("archives/voku_2017.tar", "r:") as archive:
    ocr = json.load(archive.extractfile(f"ocr/2017/{document_id}.json"))
    annotation = json.load(
        archive.extractfile(f"annotation/2017/{document_id}.json")
    )
    page = next(p for p in ocr["pages"] if p["page"] == 1)
    marks = next(p for p in annotation["pages"]
                 if p["page_id"] == page["page_id"])
    print(page["page_id"], page["width"], page["height"])
    print(page["text"])
    print(marks["annotations"])
    webp_bytes = archive.extractfile(page["image"]).read()
```

The selected page is `1191 × 1684` pixels. A WebP-capable image viewer can open it after ordinary TAR extraction. The [data guide](DATA_GUIDE.md) explains the JSON fields and provides a short Parquet example.

## Find and interpret data

- [Page index](metadata/pages.jsonl): locate each image, its yearly archive and Parquet shard, and its two episode JSON files.
- [Episode index](metadata/episodes.jsonl): group pages into source bundles and find episode JSON hashes.
- [Data guide](DATA_GUIDE.md): identifiers, title policy, OCR coordinates, and token annotation semantics.
- [Release notes](RELEASE_NOTES.md): counts, recorded validation, preserved exceptions, and the single `corpus` split.
- [Rights and credits](RIGHTS_AND_CREDITS.md): CC BY 4.0 scope, attribution as **VOKU Archive**, and the creator's separate credit.

## Production history

The separate [**VOKU Archive Workflow** repository on GitHub](https://github.com/NewTypeCola/VOKU-Archive-Workflow) documents the judgments, review, corrections, and production history behind the images. Its synthetic-identifier demo illustrates processing and is not this dataset's example data. The dataset can be used through the documents above without first reading that history.

## Why I decided to publish

I decided to make these materials publicly available after considering their historical value, the purpose of publication, and the privacy safeguards I implemented and the reviews I conducted. The project was not intended to generate revenue; its purpose was to enable the community and future generations to read and use records created by generations of members. The safeguards and review process are documented in the separately published workflow.

Although reaching everyone connected with these historical records individually was difficult in practice, I sought to make the materials’ existence and public availability known within practical limits. I informed alumni that the archive had been made publicly available online and explained how the materials had been processed and distributed. I also created and shared VOKU On so they could access and read the materials. Returning these records to the community that created them was part of this work.

Based on these preparations, I concluded that making the records publicly available with these safeguards in place, so that people could read and use them again, was consistent with the purpose of preservation. Following publication, I will continue to respond responsibly to specific feedback or concerns raised by those directly connected with the materials.

## Reuse

VOKU Archive is made available under CC BY 4.0 within the scope described in [Rights and credits](RIGHTS_AND_CREDITS.md). The designated attribution name is VOKU Archive. The unmodified license text is in [LICENSE](LICENSE).
