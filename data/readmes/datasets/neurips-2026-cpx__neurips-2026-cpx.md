---
pretty_name: neurips-2026-cpx
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

# neurips-2026-cpx — Korean OSCE history-taking dialogues with a GPT-4o virtual standardized patient

49 text-based history-taking dialogue sessions between 17 senior Korean
medical-student participants (Years 3–4 of a 6-year curriculum) and a
GPT-4o-driven virtual standardized patient (VSP). Released as the
empirical evaluation dataset accompanying our NeurIPS 2026 submission.

- **Sessions**: 49
- **Participants**: 17 (anonymised to `R001`–`R017`)
- **Total QA turns**: 1,763
- **Language**: Korean
- **Domain**: OSCE-style history-taking
- **VSP model**: `gpt-4o-2024-11-20`, temperature 0.5, seed 42
- **Collection window**: 2025-08 to 2026-05

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
| `participant_occupation` | string | `Year 5` / `Year 6` of the 6-year Korean medical curriculum, or `N/A`. |
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

The dataset contains **no** real participant names and **no** email
addresses — those were dropped at build time and the mapping was
destroyed (see [`docs/anonymisation.md`](docs/anonymisation.md)).
Per-participant aggregates (mean score, session count, turn count)
can be computed from `sessions.parquet` directly:

```python
import pyarrow.parquet as pq
import pandas as pd
df = pq.read_table("data/sessions.parquet").to_pandas()
per_session = df.drop_duplicates("session_id")[
    ["participant_id", "participant_occupation", "session_total_score"]
]
agg = per_session.groupby("participant_id").agg(
    occupation=("participant_occupation", "first"),
    avg_score=("session_total_score", "mean"),
    included_session_count=("session_total_score", "count"),
)
```

## Usage

```python
from datasets import load_dataset

ds = load_dataset("neurips-2026-cpx/neurips-2026-cpx", split="sessions")
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
pneumonia = ds.filter(lambda r: r["scenario_disease"] == "폐렴")
```

## Reproducibility

The persona-injection prompt template that drives the VSP is released in
[`docs/persona_injection_prompt.md`](docs/persona_injection_prompt.md).
The data-generation pipeline that produced the 27 underlying clinical
scenarios is open-sourced separately on GitHub; see the *Citation*
section.

All three GPT endpoints used in the broader study are configured with
`seed=42` for best-effort reproducibility (per OpenAI's
[seed semantics](https://platform.openai.com/docs/guides/text-generation/reproducible-outputs)):

| Endpoint | Model | Temperature | Role |
|---|---|---|---|
| (i) clinical-scenario script generation | `gpt-4.1` | 0.2 | Scenario authoring |
| (ii) automated platform evaluation | `gpt-4o-2024-11-20` | 0.0 | Per-session grader |
| (iii) patient role-play (this dataset) | `gpt-4o-2024-11-20` | 0.5 | VSP answer generation |

## Responsible AI metadata

All eight RAI fields below are also present in machine-readable form
under the [`rai:` extension](http://mlcommons.org/croissant/RAI/) of the
accompanying [`croissant.json`](croissant.json).

### 1. Data limitations
Sample of 49 dialogue sessions from 17 senior medical-student
participants enrolled at Korean medical schools (Years 3–4 of a 6-year
curriculum); results may not generalize to other educational levels or
contexts. All dialogues are text-based via web interface, lacking the
verbal and non-verbal cues of in-person OSCE. Korean-language origin.

### 2. Suspected biases
Korean-language origin; participants are medical students rather than
practicing clinicians; dialogues are text-based rather than spoken.
Clinical-scenario distribution is skewed toward common
internal-medicine presentations (27 scenarios).

### 3. Personal / sensitive information
All participants' identities anonymized to `R001`–`R017`; no clinical
PHI; scenarios are synthetic OSCE cases authored by the research team.
Within-text mentions of real names are deterministically substituted
during release; the original mapping was destroyed after anonymization
(see [`docs/anonymisation.md`](docs/anonymisation.md)).

### 4. Construct validity / use cases
The dataset measures fidelity of LLM-based virtual standardized
patients in text-based OSCE-style history-taking. Validity established
for: LLM-VSP research, OSCE training methodology, and multi-rater
evaluation methodology. Validity **NOT** established for: clinical
decision-making, diagnosis, evaluation in non-Korean contexts, or
standalone medical training without supervision.

### 5. Social impact
- **Positive**: enables cost-effective, reproducible OSCE practice for
  medical students and supports research on LLM-based clinical
  dialogue agents.
- **Negative**: overreliance on LLM patient simulation could displace
  human standardized-patient programs, and high LLM scores could be
  misread as clinical competence rather than role-play fidelity.
- **Mitigations**: explicit unsuitable-use-case statements,
  IRB-approved consent, and full participant anonymization.

### 6. Synthetic data
- `has_synthetic_data`: **true**
- All VSP-side answers (approximately 1,763 turns across 49 sessions)
  are generated by GPT-4o via a persona-injection prompt that fixes
  scenario-specific patient identity, clinical state, history, and
  conversational style. Student-side questions are human-typed in real
  time. The persona-injection prompt template is released alongside
  the dataset (see
  [`docs/persona_injection_prompt.md`](docs/persona_injection_prompt.md)).

### 7. Source datasets (`was_derived_from`)
27 clinical scenarios authored within the deployed VSP platform by the
research team; no external public dataset was used.

### 8. Provenance (`was_generated_by`)
- **Preprocessing**: participant identifiers (names, email addresses)
  replaced with study IDs (`R001`–`R017`); within-text occurrences of
  real names substituted deterministically; the original mapping was
  destroyed after anonymization.
- **Collection**: dialogues were generated through a web-based VSP
  platform using three GPT-family endpoints, all configured with
  `seed=42` for best-effort reproducibility (per OpenAI's seed
  semantics):
  - (i) clinical-scenario script generation by GPT-4.1
    (`temperature=0.2`),
  - (ii) automated platform evaluation by GPT-4o
    (`gpt-4o-2024-11-20`, `temperature=0`),
  - (iii) patient role-play by GPT-4o (`gpt-4o-2024-11-20`,
    `temperature=0.5`) with a persona-injection prompt fixing
    scenario-specific patient identity, clinical state, history, and
    conversational style.
  The VSP-side answers released in this dataset are produced by
  endpoint (iii). Medical students conducted text-based real-time
  history-taking encounters across 27 OSCE scenarios over 2025-08 to
  2026-05.
- **Annotation**: each session is structured with `session_id`,
  `participant_id`, clinical scenario, turn number, student question,
  and VSP response; participant-level statistics (occupation, average
  score, completed-session count, total turn count) are derivable
  from this single table.

## Ethics

See [`docs/ethics.md`](docs/ethics.md). Highlights: IRB-approved consent,
synthetic-only patient personas, no PHI, deterministic anonymisation
verified at build time.

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
The build script in `scripts/` is released under MIT (see the GitHub
repo).

OpenAI is the upstream provider of `gpt-4o` and `gpt-4.1`. Output of
those models is governed by OpenAI's
[Usage Policies](https://openai.com/policies/usage-policies) and
[Sharing & Publication Policy](https://openai.com/policies/sharing-publication-policy)
in addition to this dataset's license.

## Citation

```bibtex
@inproceedings{anonymous2026cpx,
  title  = {<paper title>},
  author = {<authors>},
  booktitle = {NeurIPS},
  year   = {2026}
}
```

The accompanying code and prompts are released anonymously at
`https://anonymous.4open.science/r/osce-pipeline-1FF7/`.
