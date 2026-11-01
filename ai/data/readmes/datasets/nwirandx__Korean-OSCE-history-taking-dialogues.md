---
pretty_name: Korean OSCE history-taking dialogues
license: cc-by-nc-sa-4.0
language:
  - ko
task_categories:
  - text-generation
  - question-answering
size_categories:
  - 1K<n<10K
tags:
  - medical
  - osce
  - history-taking
  - virtual-standardized-patient
  - korean
  - synthetic-dialogue
  - llm-evaluation
configs:
  - config_name: default
    data_files:
      - split: sessions
        path: data/sessions.parquet
---

# Korean OSCE history-taking dialogues with a GPT-4o virtual standardized patient

49 text-based history-taking dialogue sessions between 17 senior Korean
medical-student participants (Years 4–6 of a 6-year curriculum) and a
GPT-4o-driven virtual standardized patient (VSP). Released as the
empirical evaluation dataset accompanying *A Stratified Multi-Rater Evaluation of LLM-Based Virtual Standardized Patients with a Deployed Data-Generation Platform*
(NeurIPS 2026, Track on Evaluations and Datasets).

- **Sessions**: 49
- **Participants**: 17 (anonymised to `R001`–`R017`)
- **Total QA turns**: 1,763
- **Language**: Korean
- **Domain**: OSCE-style history-taking
- **VSP model**: `gpt-4o-2024-11-20`, temperature 0.5, seed 42
- **Collection window**: 2025-08 to 2026-05
- **Code**: [JINAILAB/OSCE-SimBench](https://github.com/JINAILAB/OSCE-SimBench) (scenario authoring, simulation, grading; Apache-2.0)

## Dataset structure

A single file under `data/`:

### `sessions.parquet` (1,763 rows)

One row per QA turn, joined with session-level metadata for
convenience. Every metadata column is in English; the original Korean
question/answer text is preserved alongside an English translation
(GPT-4o, `temperature=0`, `seed=42`).

| column | type | description |
|---|---|---|
| `session_id` | int32 | Stable session identifier (re-used across the parquet for joins). |
| `participant_id` | string | `R001`–`R017`. |
| `participant_occupation` | string | `Year 4` / `Year 5` / `Year 6` of the 6-year Korean medical curriculum (2 / 5 / 10 participants). |
| `scenario_disease` | string | Ground-truth diagnosis behind the persona (English). |
| `scenario_symptom` | string | Chief complaint the student is investigating (English). |
| `scenario_patient_name` | string | **Synthetic** patient name from the persona-injection prompt (Revised Romanization). |
| `session_status` | string | `completed` / other status flags. |
| `session_total_score` | float64 | Per-session score from the platform's automated grader (0–100). |
| `session_created_at` | string | UTC-naive timestamp of session creation. |
| `turn` | int32 | 1-indexed turn number within the session. |
| `question` | string | Student-typed question (Korean original). |
| `answer` | string | GPT-4o VSP response (Korean original). |
| `translated_question` | string | English translation of `question`. |
| `translated_answer` | string | English translation of `answer`. |

## Usage

```python
from datasets import load_dataset

ds = load_dataset("nwirandx/Korean-OSCE-history-taking-dialogues", split="sessions")
print(ds[0])
# {'session_id': 564, 'participant_id': 'R001', 'turn': 1, ...}

# Reconstruct a single session as an ordered transcript
session = ds.filter(lambda r: r["session_id"] == 564).sort("turn")
for row in session:
    print(f"Q: {row['question']}")
    print(f"A: {row['answer']}\n")
```

To filter by scenario:

```python
pneumonia = ds.filter(lambda r: r["scenario_disease"] == "Pneumonia")
```

## Reproducibility

The persona-injection prompt template that drives the VSP is released in
[`docs/persona_injection_prompt.md`](docs/persona_injection_prompt.md).
The data-generation pipeline that produced the 27 underlying clinical
scenarios is open-sourced at
[github.com/JINAILAB/OSCE-SimBench](https://github.com/JINAILAB/OSCE-SimBench).

All three GPT endpoints used in the broader study are configured with
`seed=42` for best-effort reproducibility (per OpenAI's
[seed semantics](https://platform.openai.com/docs/guides/text-generation/reproducible-outputs)):

| Endpoint | Model | Temperature | Role |
|---|---|---|---|
| (i) clinical-scenario script generation | `gpt-4.1` | 0.2 | Scenario authoring |
| (ii) automated platform evaluation | `gpt-4o-2024-11-20` | 0.0 | Per-session grader |
| (iii) patient role-play (this dataset) | `gpt-4o-2024-11-20` | 0.5 | VSP answer generation |

## Responsible AI and ethics

The eight Responsible AI fields (data limitations, biases, personal
information, use cases, social impact, synthetic data, source datasets,
and provenance) are provided in machine-readable form under the
[`rai:` extension](http://mlcommons.org/croissant/RAI/) of
[`croissant.json`](croissant.json). IRB approval, consent, and
anonymisation are described in [`docs/ethics.md`](docs/ethics.md) and
[`docs/anonymisation.md`](docs/anonymisation.md).

## Reproducing this release locally

The build script at `scripts/build_release.py` is read-only against the
source xlsx and idempotent. It runs the anonymisation, writes the
parquet files, calls OpenAI to translate every Q/A turn into English,
and emits `croissant.json` with the RAI extension fields:

```bash
python -m venv .venv && source .venv/bin/activate
pip install pyarrow openai python-dotenv
echo "OPENAI_API_KEY=sk-..." > ../.env
python scripts/build_release.py --input /path/to/jieumcpx_dataset.xlsx --out .
```

Translations are written through a local cache at
`data/.translation_cache.json` (gitignored), so re-runs only call the
API for sessions that haven't been translated yet. Pass
`--no-translate` to skip the OpenAI calls entirely (the
`translated_*` columns will be empty strings).

The script will fail loudly if any participant name or email survives
into the output parquet file.

## License

Dataset content (`data/*.parquet`, `docs/*`, `README.md`,
`croissant.json`) is released under
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
The build script in `scripts/` is released under Apache-2.0 (see the GitHub
repo).

OpenAI is the upstream provider of `gpt-4o` and `gpt-4.1`. Output of
those models is governed by OpenAI's
[Usage Policies](https://openai.com/policies/usage-policies) and
[Sharing & Publication Policy](https://openai.com/policies/sharing-publication-policy)
in addition to this dataset's license.

## Citation

```bibtex
@inproceedings{yi2026vsp,
  title     = {A Stratified Multi-Rater Evaluation of LLM-Based Virtual
               Standardized Patients with a Deployed Data-Generation Platform},
  author    = {Yi, Yongjin and Park, Jinyong and Kim, Sejoong},
  booktitle = {Advances in Neural Information Processing Systems
               (NeurIPS 2026), Track on Evaluations and Datasets},
  year      = {2026}
}
```

The accompanying code and prompts are released at
https://github.com/JINAILAB/OSCE-SimBench (Apache-2.0 licence).
