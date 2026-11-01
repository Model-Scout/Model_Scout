---
license: cc-by-4.0
language:
  - en
  - ko
task_categories:
  - translation
tags:
  - machine-translation-evaluation
  - esa
  - wmt25
  - document-level
  - emnlp2026
size_categories:
  - 10K<n<100K
configs:
  - config_name: default
    data_files: esa-counterfactual-enko.jsonl
---

# ESA Counterfactual En-Ko

Data for "The Blindness of Document-Level Translation Evaluation"
(EMNLP 2026, Main Conference).

[paper](https://arxiv.org/abs/2609.05949) · [code](https://github.com/trotacodigos/esa-counterfactual)

Error Span Annotation (ESA) human judgments on WMT25 General MT English-Korean
outputs, collected under three context conditions. The same translation is
annotated in isolation, inside its own system's document, and inside a document
whose surrounding segments come from other systems. The first two are the
conventional segment and document levels. The third is counterfactual, supplying
document context of a quality the system never produced while leaving segment
order intact. This makes the effect of context on ESA scores measurable within
rater and within segment.

The official WMT25 human evaluation for English-Korean used MQM evaluation
criteria. This is a separate ESA collection over the same system outputs and is
not part of the WMT25 release.

## What this file contains

Annotations only. Source text and system translations are not redistributed
here. Each record carries a character span into the WMT25 document-level system
output, so the annotated string is recovered by joining against the WMT25
General MT release.

| | |
|---|---|
| Records | 18,294 |
| Documents | 23 |
| Systems | 10 (9 systems plus the reference) |
| Raters | 10 |
| Conditions | `seg`, `doc`, `mix` |


## Joining with WMT25

Download `wmt25-genmt.jsonl` from
[wmt-conference/wmt25-general-mt](https://github.com/wmt-conference/wmt25-general-mt),
then run the included script.

```bash
python rebuild_tgt.py --wmt wmt25-genmt.jsonl --out joined.jsonl
```

The join is `doc_id` plus `system`, and the annotated string is
`tgts[system][start:end]` where `[start, end)` is `tgt_char_span`. Every
rebuilt string is verified against `tgt_sha256`, computed over the NFC-normalized
UTF-8 encoding. A checksum failure means the WMT25 file has changed and the
offsets in that record no longer apply.

`system` is `"ref"` for the human reference, which is `refs.refA.ref` in the
WMT25 file. All other values match the WMT25 system names exactly.

## Fields

| Field | Type | Description |
|---|---|---|
| `doc_id` | string | WMT25 document ID, unmodified |
| `org_seg_id` | int | Paragraph index in the WMT25 document, 0-based |
| `new_seg_id` | int | Segment index in this dataset's segmentation, 0-based |
| `domain` | string | `literary`, `news`, or `social` |
| `system` | string | WMT25 system name, or `ref` |
| `condition` | string | `seg`, `doc`, or `mix` |
| `rater` | string | `rater1` through `rater10` |
| `tgt_char_span` | [int, int] | Half-open span into the WMT25 system output |
| `tgt_sha256` | string | SHA-256 of the annotated string, NFC, UTF-8 |
| `annotation.score` | int | ESA score, 0-100 |
| `annotation.error_spans` | list | Error spans, possibly empty |

### Segment IDs

Paragraphs are obtained by splitting `src_text` on blank lines. Long paragraphs
were divided before annotation, so one paragraph can correspond to several
records.

`org_seg_id` is the paragraph index and is the key for joining back to WMT25. It
is not unique within a document. `new_seg_id` is unique within a document and
runs consecutively over the post-division segmentation, which shifts every
segment after a divided paragraph.

| WMT25 paragraph | Divided into | `org_seg_id` | `new_seg_id` |
|---|---|---|---|
| 2 | 1 part | 2 | 2 |
| 3 | 2 parts | 3, 3 | 3, 4 |
| 4 | 1 part | 4 | 5 |

Segment order is identical across all three conditions. In `mix`, the segments
surrounding an annotated segment come from other systems, and which system
supplied each of them is not released.

### Error spans

`start_i` and `end_i` are character offsets into the annotated string, with
`end_i` inclusive, following the WMT25 ESA convention. Offsets are relative to
the string recovered by `tgt_char_span`, not to the full document.

Spans were remapped from the annotation interface onto WMT25 coordinates.
Whitespace at span edges was trimmed, since the two differ in whitespace runs at
some paragraph boundaries. Three classes of span were removed: 1,306 zero-content
spans placed past the end of the string, 370 spans covering only whitespace, and
whitespace-only edges of otherwise valid spans. Every remaining span was checked
to cover the same text after remapping.

`category` is absent by design. ESA collects severity without an error typology.

## Conditions

| Condition | Rater sees |
|---|---|
| `seg` | One segment, no surrounding document |
| `doc` | The full document, all segments from one system, in document order |
| `mix` | The full document, segments from different systems, in document order |

## License

The annotations, scores, span offsets, and segment identifiers in this file are
released under CC BY 4.0.

The underlying source texts and system outputs are not included and remain under
the WMT25 General MT terms, which permit use for research purposes and require
citation of the shared task findings paper along with any citation requirements
attached to the individual test sets. Anyone joining this dataset with the WMT25
release is bound by those terms.

## Citation

```bibtex
@misc{kim2026blindnessdocumentleveltranslationevaluation,
      title={The Blindness of Document-Level Translation Evaluation}, 
      author={Ahrii Kim and Vilém Zouhar and Chanjun Park and Seong-heum Kim},
      year={2026},
      eprint={2609.05949},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2609.05949}, 
}
```

Cite the WMT25 General MT findings paper as well.

```bibtex
@inproceedings{kocmi-etal-2025-findings,
    title = "Findings of the {WMT}25 General Machine Translation Shared Task: Time to Stop Evaluating on Easy Test Sets",
    author = "Kocmi, Tom  and
      Artemova, Ekaterina  and
      Avramidis, Eleftherios  and
      Bawden, Rachel  and
      Bojar, Ond{\v{r}}ej  and
      Dranch, Konstantin  and
      Dvorkovich, Anton  and
      Dukanov, Sergey  and
      Fishel, Mark  and
      Freitag, Markus  and
      Gowda, Thamme  and
      Grundkiewicz, Roman  and
      Haddow, Barry  and
      Karpinska, Marzena  and
      Koehn, Philipp  and
      Lakougna, Howard  and
      Lundin, Jessica  and
      Monz, Christof  and
      Murray, Kenton  and
      Nagata, Masaaki  and
      Perrella, Stefano  and
      Proietti, Lorenzo  and
      Popel, Martin  and
      Popovi{\'c}, Maja  and
      Riley, Parker  and
      Shmatova, Mariya  and
      Steingr{\'i}msson, Steinth{\'o}r  and
      Yankovskaya, Lisa  and
      Zouhar, Vil{\'e}m",
    editor = "Haddow, Barry  and
      Kocmi, Tom  and
      Koehn, Philipp  and
      Monz, Christof",
    booktitle = "Proceedings of the Tenth Conference on Machine Translation",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.wmt-1.22/",
    doi = "10.18653/v1/2025.wmt-1.22",
    pages = "355--413",
    ISBN = "979-8-89176-341-8"
}
```