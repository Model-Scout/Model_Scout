---
license: mit
language:
  - ko
task_categories:
  - question-answering
pretty_name: SNU Ko-MuSR — Narrative Merged into Question
configs:
  - config_name: murder_mysteries
    data_files:
      - split: test
        path: murder_mysteries/test.parquet
  - config_name: object_placements
    data_files:
      - split: test
        path: object_placements/test.parquet
  - config_name: team_allocation
    data_files:
      - split: test
        path: team_allocation/test.parquet
---

# SNU_Ko-MuSR — narrative merged into question

Source: [thunder-research-group/SNU_Ko-MuSR](https://huggingface.co/datasets/thunder-research-group/SNU_Ko-MuSR)

This is a field-layout transformation of the source dataset. Users should
review and comply with the source dataset's access conditions.

For every row in each `test` split, the output applies:

```text
question = narrative.strip() + "\n\n" + question.strip()
```

The original `narrative` column is removed. `choices`, `answer`,
`answer_choice`, and `narrative_before_edit` are preserved.

## Files

- `murder_mysteries/test.parquet` — 250 rows
- `object_placements/test.parquet` — 250 rows
- `team_allocation/test.parquet` — 250 rows
- `manifest.json` — row counts, columns, and relative file paths
