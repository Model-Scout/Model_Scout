---
license: agpl-3.0
language:
- en
- zh
- ko
- es
- my
- ne
task_categories:
- visual-question-answering
- video-text-to-text
- text-generation
tags:
- multi-video
- event-understanding
- claim-generation
- grounded-citation
- magmar
- acl-2026
- ocr
- object-detection
- asr
- trace
pretty_name: TRACE — MAGMaR 2026 release
size_categories:
- n<1K
---

# TRACE — MAGMaR 2026 release

Companion dataset for **TRACE: Evidence Grounding-Guided Multi-Video Event
Understanding and Claim Generation** (ACL 2026 MAGMaR Workshop).

Paper: [arXiv:2605.16740](https://arxiv.org/abs/2605.16740).
Code: [pengyu965/TRACE](https://github.com/pengyu965/TRACE).

This release contains every artefact produced by the TRACE pipeline on the
MAGMaR 2026 Oracle Track test set: the official inputs, our Part-1
preprocessing outputs (ASR + OCR + object detection), our Part-2 LVLM
claim-generation outputs in two frame-selection variants, and our Part-3
cross-video aggregation outputs including the final MAGMaR submission
JSONLs for both aggregation methods.

The headline result reported in the paper —
Avg MiRAGE F1 = 0.811, InfoF1 = 0.869, CiteF1 = 0.753 on the 8-topic
validation subset (Table 4, row 4) — is the file
[`part3_aggregation/guided/submission/penkil_v2_method_a.jsonl`](part3_aggregation/guided/submission/penkil_v2_method_a.jsonl).

---

## Folder layout

```
TRACE-MAGMaR-2026/
├── inputs/                              official MAGMaR test inputs (shared across all variants)
├── videos.tar                           90 mp4s (3.8 GB) packed in a single tar for easy download
├── frames_annotated.tar.gz              YOLO + OCR annotated overlay JPGs (5.9 GB raw, ~5.5 GB compressed)
├── part1_preprocessing/                 YOLOv12 + HunyuanOCR + Whisper / Qwen3-Omni outputs (90 videos)
├── part2_claim_generation/              Qwen3-VL-30B-A3B-Instruct per-video claims
│   ├── uniform/                         100 uniform frames only        (= ✗ Additional Key Frames, Table 4)
│   └── guided/                          uniform + guidance-targeted    (= ✓ Additional Key Frames, Table 4)
└── part3_aggregation/                   Qwen3-Embedding-8B + Qwen3-30B-A3B-Instruct cross-video consolidation
    ├── uniform/                         on top of part2_claim_generation/uniform
    │   ├── per_query/                   stage 1: per-video → per-query pivot
    │   ├── clusters/                    stage 2: greedy single-link clusters at cosine τ = 0.9
    │   ├── stage3_io/
    │   │   ├── embed_sim/               Method A: embedding-similarity dedup + per-cluster LLM verify
    │   │   └── llm/                     Method B: pure-LLM clustering over flat claim list
    │   └── submission/
    │       ├── penkil_v1_method_a.jsonl   MAGMaR submission (uniform × Method A)
    │       └── penkil_v1_method_b.jsonl   MAGMaR submission (uniform × Method B)
    └── guided/                          on top of part2_claim_generation/guided
        └── submission/
            ├── penkil_v2_method_a.jsonl   headline paper result (guided × Method A, Avg F1 0.811)
            └── penkil_v2_method_b.jsonl   MAGMaR submission (guided × Method B)
```

The on-HF submission filenames (`penkil_v1_*`, `penkil_v2_*`) are kept
verbatim from our official MAGMaR 2026 submissions so they match what the
leaderboard records.

### Folder name ↔ paper term

| folder on HF | paper term (Table 4) |
|---|---|
| `part2_claim_generation/uniform/`     | Additional Key Frames ✗ |
| `part2_claim_generation/guided/`      | Additional Key Frames ✓ |
| `stage3_io/embed_sim/`                 | Method A — Embed-Sim |
| `stage3_io/llm/`                       | Method B — LLM clustering |

---

## Inputs (`inputs/`)

| File | Records | Description |
|---|---|---|
| `MAGMaR2026_queries.jsonl` | 19 | Official MAGMaR 2026 Oracle Track queries: `{query_id, query_type, language, title, persona_title, background, query}`. 10 unique `title`s (event topics); some topics carry multiple persona/query pairs. |
| `topic_video_mapping.json` | 10 topics → 92 video refs | Event title → list of video IDs. The MAGMaR oracle "which videos to read for each event" map. |
| `ground_truth.jsonl` | 8 | Per-query gold annotations (`metadata` + `references` + `responses`) for the WikiVideo-overlap validation subset of MAGMaR 2026. These are the 8 queries with publicly available gold claims; the remaining 11 are leaderboard-only. |

### Languages present in queries

- `english` (most queries)
- `chinese` (e.g. query #19, *2025_Shi_Yongxin_Scandal*)
- Korean, Japanese, Burmese, Nepali, Spanish all appear in OCR + ASR over individual videos.

---

## Videos (`videos.tar`)

90 `.mp4` files packed in a single uncompressed tarball (3.8 GB), one per
video listed in `inputs/topic_video_mapping.json`. After untarring you get
a `videos/` directory of bare `<video_id>.mp4` files — those filenames are
the keys used throughout the rest of this release.

```bash
tar -xf videos.tar          # produces videos/<video_id>.mp4
```

The MAGMaR 2026 organisers are the canonical source for these videos; we
redistribute them here so the full pipeline can be reproduced from this
dataset alone.

Two of the 92 mapping refs have no `.mp4` here — they were unavailable at
download time, which is also why their `part1_preprocessing/` records and
downstream claims are missing.

---

## Part 1 — Preprocessing (`part1_preprocessing/`)

90 of the 92 video refs in `topic_video_mapping.json` have complete Part-1
outputs; two videos were unavailable / failed download and are silently
dropped here. The missing list is logged in `*_stragglers.log` in the
source repo.

| File | Records | Description |
|---|---|---|
| `yolo.jsonl` | 90 | YOLOv12 (`yolo12x.pt`) per-frame object detections at 1 fps. Per-video: `{video_id, num_frames, fps, image_size, model, conf_threshold, frames: [{frame_idx, time_sec, num_detections, class_counts, detections: [{class_id, class_name, confidence, bbox_xyxy}]}]}`. |
| `ocr.jsonl` | 90 | HunyuanOCR (`tencent/HunyuanOCR`) per-frame scene-text detections at 1 fps. Per-frame: `{frame_idx, time_sec, num_detections, frame_languages, detections: [{text, src_lang (NLLB script tag), bbox_xyxy_norm, bbox_xyxy}]}`. |
| `asr_whisper.jsonl` | 90 | faster-whisper `large-v3`, two passes (transcribe + translate). Carries `language_detected`, `language_prob`, `duration`, `native` + `english` full transcripts, time-aligned `segments_native` + `segments_english`. Canonical ASR. |
| `asr_omni.jsonl` | 180 (VAD chunks) | Qwen3-Omni-30B-A3B-Thinking backup ASR with Silero-VAD chunking. Useful for queries where Whisper struggled. |
| `asr_factcards.jsonl` | 90 | Whisper + Omni merged side-by-side for the same video (one row per video, `{video_id, topic, language, whisper, omni}`). |
| `vad_chunks.json` | — | Silero-VAD chunk metadata (start/end seconds per chunk) used by `asr_omni`. |

Annotated frame JPGs (YOLO + OCR overlays drawn on the raw frames at 1 fps)
are shipped as the separate **`frames_annotated.tar.gz`** in this dataset
root. Untar it into a `frames_annotated/` directory containing
`yolo/<video_id>/frame_*.jpg` and `ocr/<video_id>/frame_*.jpg`:

```bash
tar -xzf frames_annotated.tar.gz   # produces frames_annotated/{yolo,ocr}/...
```

This is purely visualisation — the bounding boxes in `yolo.jsonl` and
`ocr.jsonl` are the canonical detection records.

---

## Part 2 — Claim generation (`part2_claim_generation/`)

Qwen3-VL-30B-A3B-Instruct per-video factual claims, conditioned on the
query/persona, the Part-2 Step-1 textual grounding summary (text-only
relevance filter — see TRACE repo), and the video itself.

Two frame-selection variants are shipped:

| variant | what the LVLM sees | row in paper Table 4 |
|---|---|---|
| `uniform/`  | 100 uniformly sampled frames only + the Step-1 textual summary | `Additional Key Frames ✗` |
| `guided/`   | 100 uniform frames + up to 30 guidance-targeted keyframes at evidentially relevant timestamps | `Additional Key Frames ✓` |

Each `<video_id>_results.json` shape:

```json
{
  "video_id": "1977786657936982016",
  "queries": [
    {
      "query_id": "10",
      "query":    "How did the 2025 Alaska typhoon affect coastal communities ...",
      "persona_title": "Emergency Management Specialist",
      "persona":       "<background text>",
      "generated_claims": [
        "The 2025 Alaska Typhoon caused severe coastal flooding and storm surge in Emmonak, AK ...",
        "..."
      ]
    }
  ]
}
```

`uniform/` covers 86 videos and `guided/` covers 87 (one video was
successfully processed only in the guided run due to LVLM batch failures
on the other).

---

## Part 3 — Cross-video aggregation (`part3_aggregation/`)

Stage 1 (split per-video → per-query) → Stage 2 (Qwen3-Embedding-8B greedy
single-link clustering at cosine τ = 0.9) → Stage 3 (Method A:
per-cluster LLM verify with Qwen3-30B-A3B-Instruct, or Method B: pure-LLM
clustering over the flat claim list) → Stage 4 (assemble MAGMaR submission
JSONL and run hard invariant checks) → Stage 5 (markdown diff report).

### What `stage3_io/` is

`stage3_io/` is a complete record of what the Stage-3 LLM was given and
what it produced, **per method, per query**. We ship it so every Method-A
and Method-B decision in the final submission is auditable:

- `stage3_io/<method>/input/query_<qid>.json` — the exact prompt context
  passed to the LLM for that (method, query) pair: cluster IDs, per-cluster
  member claims with their source `video_id`, and any other prompt fields
  the verifier was given. Re-running Stage 3 with this file reproduces the
  output.
- `stage3_io/<method>/output/query_<qid>.json` — what the LLM returned for
  that pair: `{query_id, method, n_input_claims, n_output_responses,
  responses: [{text, citations}]}`. This is what Stage 4 reads when
  assembling the submission JSONL.

For Method A (`embed_sim/`), the `input/` files come from Stage 2's
clusters — one prompt per query containing all clusters at once. For
Method B (`llm/`), the LLM does the clustering itself, so `input/` is the
flat claim list (with `video_id`s) and `output/` carries the LLM's own
cluster decisions plus the canonicalised text.

### File map

| file / subfolder | contents |
|---|---|
| `per_query/query_<qid>.json` | Stage 1 output: for one query, the per-video claim lists pivoted to a single record. |
| `clusters/query_<qid>_clusters.json` | Stage 2 output: greedy single-link clusters with `tau`, `n_claims`, `n_clusters`, `clusters: [{cluster_id, size, members: [{video_id, claim_idx, claim}]}, ...]`. |
| `stage3_io/<method>/input/query_<qid>.json`  | Stage 3 input: what the LLM saw for this (method, query). One JSON per query. |
| `stage3_io/<method>/output/query_<qid>.json` | Stage 3 output: what the LLM returned for this (method, query). One JSON per query, schema above. |
| `submission/penkil_v{1,2}_method_{a,b}.jsonl` | Stage 4: final MAGMaR submission JSONL in the official format. |
| `submission/diff_report.md` | Stage 5: per-query counts of input claims, output responses, citations, validator status (OK / FAIL). |

### MAGMaR submission JSONL shape (per line)

```json
{
  "metadata":   {"run_id": "penkil_v2_method_a", "query_id": "1",
                 "team_id": "123456", "task": "oracle"},
  "responses":  [{"text": "<verbatim claim>",  "citations": ["<vid1>", "<vid2>"]}, ...],
  "references": ["<vid1>", "<vid2>", ...]
}
```

Hard invariants enforced by Stage 4:
- every `response.text` is a verbatim copy of one input claim,
- citations are deduped `video_id`s drawn from that cluster's input,
- every video that contributed at least one claim appears in some response's citations,
- total citations across responses do not exceed total input claims.

---

## Headline results (from the paper)

MAGMaR 2026 Oracle Track validation set, 8 topics.

| Configuration | Avg F1 | InfoF1 | CiteF1 |
|---|---|---|---|
| Qwen3-VL-30B baseline (no grounding) | 0.705 | 0.800 | 0.609 |
| `uniform/` × Method B (LLM)          | 0.802 | 0.859 | 0.745 |
| `uniform/` × Method A (Embed-Sim)    | 0.808 | 0.868 | 0.748 |
| `guided/`  × Method B (LLM)          | 0.804 | 0.867 | 0.741 |
| **`guided/` × Method A (Embed-Sim)** | **0.811** | **0.869** | **0.753** |

The full-test-set leaderboard ranking is in the paper (Table 1); the
`submission/*.jsonl` files in this dataset are the exact artefacts
evaluated there.

---

## Reproducing every artefact

Every file under `part1_preprocessing/`, `part2_claim_generation/`, and
`part3_aggregation/` can be regenerated by running the TRACE pipeline on
the videos in `videos.tar` plus the queries in
`inputs/MAGMaR2026_queries.jsonl`. See the
[GitHub README](https://github.com/pengyu965/TRACE#-running-trace) for the
CLI.

```bash
tar -xf videos.tar                                 # produces videos/<video_id>.mp4
python -m pipeline.run --input MAGMaR2026_queries.jsonl \
                       --videos-dir videos/        # then point --videos-dir here
```

No further download is required to reproduce our results end-to-end.

---

## Citation

```bibtex
@inproceedings{yan2026trace,
  title     = {TRACE: Evidence Grounding-Guided Multi-Video Event Understanding and Claim Generation},
  author    = {Yan, Pengyu and Gorugantu, Akhil and Bhosale, Mahesh and Wasi, Abdul and Trivedi, Vishvesh and Doermann, David},
  booktitle = {Proceedings of the MAGMaR Workshop at ACL 2026},
  year      = {2026},
  note      = {Equal contribution: Pengyu Yan and Akhil Gorugantu}
}
```

Please also cite the upstream MAGMaR / WikiVideo / MultiVENT works, and
the underlying models (YOLOv12, HunyuanOCR, Whisper, Qwen3 family). Full
list in the GitHub README.

---

## License

This dataset is released under GNU AGPL-3.0, matching the TRACE code
release. The original video files and the MAGMaR 2026 official inputs
(`MAGMaR2026_queries.jsonl`, `topic_video_mapping.json`,
`ground_truth.jsonl`) remain under whatever terms the MAGMaR 2026
organisers distribute them under.
