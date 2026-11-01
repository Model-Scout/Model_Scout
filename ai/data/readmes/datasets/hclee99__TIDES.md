---
pretty_name: TIDES
language:
- ko
- en
task_categories:
- text-classification
tags:
- dialogue
- multi-party
- longitudinal
- collaboration
- social-dynamics
- utterance-classification
---

# 🌊 TIDES: Longitudinal Bilingual Dataset for Modeling Multi-Party Social Dynamics

- **Paper:** Coming soon
- **Website:** https://tides.cstlab.org
- **Contact:** Heechan Lee [hclee99@kaist.ac.kr](mailto:heechan@kaist.ac.kr), Jeonggyu Kang [jeonggyumarkk@kaist.ac.kr](mailto:jeonggyumarkk@kaist.ac.kr), Joseph Seering [seering@kaist.ac.kr](mailto:seering@kaist.ac.kr)

🌊 TIDES is an **in-the-wild**, **longitudinal**, **multi-party** collaboration dialogue dataset collected by tracking Korean university student teams over the course of a semester. TIDES includes transcripts and chat logs from meetings conducted by participants as they worked on real course projects throughout the semester, along with satisfaction surveys. Rather than simply providing raw dialogue, we offer **emergent role, utterance type, and team development** annotation layers to capture **the development of social dynamics** in multi-party collaboration settings.

Speakers are anonymized (`PERSON_A`, `PERSON_B`, …). The corpus includes seven primarily Korean-speaking teams (`Team_1`, `Team_2`, `Team_3`, `Team_6`, `Team_7`, `Team_9`, and `Team_10`) and five primarily English-speaking teams (`Team_4`, `Team_5`, `Team_8`, `Team_11`, and `Team_12`). All transcripts provide English text (Some participants speak in Korean seldomly!); Korean-source teams additionally include the original utterances in `korean_text`.

| Scale | Count |
| --- | ---: |
| Teams | 12 (`Team_1` … `Team_12`) |
| Meeting transcript files | 104 |
| Utterance segments | ~75,971 |
| Chat exports | 11 teams (Team_3 has no chat file) |
| Approx. size | ~27 MB |

> Some meetings are split across multiple files (`…_Pt1.json`, `…_Pt2.json`, …). Metadata lists **meetings by date** (88 dated meetings), so the number of JSON files can exceed the number of metadata meeting entries.

---

## Directory layout

```
TIDES/
├── README.md
├── metadata/
│   ├── meeting_metadata.json      # per-team project blurb, meeting topics, speaker map
│   ├── satisfaction_metadata.json # per-meeting satisfaction survey aggregates
│   └── meeting_roles.csv          # per-participant role ratings per meeting
└── Team_N/
    ├── TeamN_YYYYMMDD.json        # meeting transcript (+ optional "_PtK" suffix)
    ├── TeamN_YYYYMMDD_PtK.json
    └── chat/
        └── TeamN_chat_anonymized.{txt,csv,xlsx}
```

---

## Meeting transcripts (`Team_N/*.json`)

Each file is a single JSON object:

```json
{
  "segments": [ /* ordered utterances */ ]
}
```

### Segment schema

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `start` | number | yes | Utterance start time (seconds) |
| `end` | number | yes | Utterance end time (seconds) |
| `speaker` | string | yes | Anonymized speaker id (`PERSON_A`, …) |
| `text` | string | yes | Utterance text (English) |
| `utterance_type` | string | yes | Dialogue-act / interaction label (see below) |
| `annotation_source` | string | yes | `"gemma"` (model) or `"human"` (gold) |
| `korean_text` | string | no | Original Korean utterance when retained |
| `qwen_utterance_type` | string | no | Secondary model (Qwen) label |

**Coverage notes**

- `annotation_source`: mostly `gemma` (~70k); `human` (~5.7k). Human segments usually omit `korean_text` and `qwen_utterance_type`.
- `korean_text`: present on a majority of segments, not all.
- `qwen_utterance_type`: present on most `gemma` segments; absent on typical `human` segments.

### Example segment

```json
{
      "start": 76.56,
      "end": 80.3,
      "speaker": "PERSON_B",
      "text": "It's a bit different from what we had in mind.",
      "utterance_type": "Linking Solutions",
      "annotation_source": "gemma",
      "korean_text": " 근데 저희가 생각하는 이미지랑 좀 다르세요.",
      "qwen_utterance_type": "Linking Problems"
}
```

### `utterance_type` vocabulary

Based on modified version of `act4teams-SHORT` (Klünder et al., 2020)

| Label | ~Count |
| --- | ---: |
| Giving Information | 26810 |
| Active listening | 9946 |
| Linking Solutions | 9260 |
| Naming Solutions | 4917 |
| Other / Neutral | 4703 |
| Structuring | 4643 |
| Proactivity | 3912 |
| Naming Problems | 3157 |
| Social / Humor | 2510 |
| Linking Problems | 2233 |
| Cooperation | 1812 |
| Knowledge Transfer | 878 |
| Task/Process Negative | 642 |
| Social Negative | 465 |
| Linking & Connecting | 83 |

---

## Metadata

### `metadata/meeting_metadata.json`

Top-level keys: `Team_1` … `Team_12`.

```text
Team_N:
  team_number: int
  project: string                    # short project / context description (may be Korean)
  speaker_id_to_pseudonym: {         # PERSON_* → English given-name pseudonym
    "PERSON_A": "Alex",
    ...
  }
  meetings: [
    {
      date: "YYYY-MM-DD",
      main_topics: [string, ...],    # participant- or annotator-written topic summaries
      participants: ["PERSON_A", ...],
      team_development_stage: string # optional; e.g. Forming, Storming, Norming, Performing, Adjourning
                                     # (occasionally a comma-combined value)
    },
    ...
  ]
```

**Team development stage (Based on Tuckman's stages of group development (1965))**: Forming, Storming, Norming, Performing, Adjourning.

### `metadata/satisfaction_metadata.json`

Top-level keys: `Team_1` … `Team_12`.

```text
Team_N:
  team_number: int
  meetings: [
    {
      date: "YYYY-MM-DD",
      satisfaction: [
        {
          question: string,   # bilingual prompt text
          average: number | null,
          scores: [number, ...]   # may be empty when not collected
        },
        ...
      ]
    },
    ...
  ]
```

### `metadata/meeting_roles.csv`

One row per participant × meeting.

| Column | Description |
| --- | --- |
| `Team_Number` | Team id (1–12) |
| `Meeting_Sequence` | Meeting index within the team |
| `Meeting_Date` | `YYYY-MM-DD` |
| `Participant_Name` | `PERSON_*` id |
| `Dominance_Average` | Dominance score |
| `Sociability_Average` | Sociability score |
| `Task_Orientation_Average` | Task-orientation score |
| `assigned_role` | Nearest role label (see below) |
| `role_distance` | Distance to assigned role centroid |

**`assigned_role` values (Based on `TRIAD model` (Driskell et al., 2017)):** Attention Seeker, Coordinator, Critic, Evaluator, Follower, Negative, Power Seeker, Problem Solver, Social, Task Completer, Task Motivator, Team Leader, Teamwork Support.


---

## Team chat (`Team_N/chat/`)

Asynchronous team messaging exports (KakaoTalk-style), with participant names replaced by English pseudonyms consistent with `speaker_id_to_pseudonym` where applicable.

| Team | File | Format |
| --- | --- | --- |
| 1, 2, 5, 6, 7, 8, 9 | `TeamN_chat_anonymized.txt` | Plain-text chat export |
| 10, 11, 12 | `TeamN_chat_anonymized.csv` | CSV |
| 4 | `TeamN_chat_anonymized.xlsx` | Excel |
| 3 | — | Missing in this release |

---

## Anonymization & ethics notes

- Meeting speakers use `PERSON_*` ids; metadata maps them to English pseudonyms for readability.
- Chat logs use the same pseudonym style; residual indirect identifiers may still exist in free text—review before redistribution if your release policy requires it.
- Survey free-text / topic fields may contain Korean descriptions of course projects.

---

## Citation

Add citation / license / paper link here before publishing to arXiv.
