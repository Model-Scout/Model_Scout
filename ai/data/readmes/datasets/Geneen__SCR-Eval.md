---
license: other
license_name: cc-by-per-source-film
license_link: LICENSE
language:
  - en
  - ko
configs:
  - config_name: expert_annotations
    default: true
    data_files:
      - split: train
        path: expert/*/*.csv
---

# SCR-Eval open-film release (scr_eval_open_films_v1)

Data accompanying *SCR-Eval: Evaluating Video Subtitle Translation with a Script-like
Context Representation* (EMNLP 2026, Industry Track).

## Contents

```
scr/{film}/scr.json                            schema scr@1 — source-side, human-reviewed
subtitles/{film}/{film}_en_source.vtt          English source subtitles
subtitles/{film}/{film}_ko_{provider}.vtt      Korean translations (4 providers)
sats/{film}/{provider}/sats.json              schema sats@1 — subtitle-to-source alignment
expert/{film}/P1.csv … P7.csv                  expert line annotations, one file per evaluator
tser/{film}/{condition}/{provider}/run_NNN.json schema tser@1 — per-run evaluation reports
LICENSE                                      licence terms and required attribution
MANIFEST.json                                file list with SHA-256 checksums
VIDEO_SOURCES.md                             source video links and file identifiers; videos not included
```

Films: Elephants Dream, Sprite Fright, Tears of Steel.

Providers (paper labels): `hand_written` (Human), `gemini_line` (LLM-Line),
`gemini_scene` (LLM-Scene), `google_translate` (Google NMT).

Conditions: `full` (scene segmentation plus SCR context), `scene_only` (scene
segmentation only), and `line_only` (individual source lines). Each film–provider–condition
combination has 10 evaluation runs.

The scene-based conditions use `scenes` and `scene_scores`; `line_only` uses `lines` and
`line_scores` keyed by `line_uid`. All conditions share the error anchors `scene_id`,
`source_line_uids`, and `ts_indices`.

## Expert annotations

Each `expert/{film}/{evaluator}.csv` contains one row per source line per provider.
Columns:
`film, provider, evaluator, line_uid, scene_id, source_text, translation, category, severity`.

Blank `category` and `severity` together indicate no error. `translation` contains the
aligned Korean subtitle shown to the evaluator; it is blank when no subtitle aligns with
the source line. Subtitle line breaks are collapsed to spaces in CSV and preserved in
the VTT files.

Free-text evaluator comments are not included.

## Citation

> Jongin Lee, Juyi Hwang, and Sehyun Kim. SCR-Eval: Evaluating Video Subtitle
> Translation with a Script-like Context Representation. In *Proceedings of the
> 2026 Conference on Empirical Methods in Natural Language Processing: Industry
> Track*, 2026.

Dataset page: <https://huggingface.co/datasets/Geneen/SCR-Eval>

Paper: <https://aclanthology.org/2026.emnlp-industry.80/>
