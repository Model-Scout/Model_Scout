---
license: apache-2.0
language:
- en
- tr
- fr
- de
- es
- pt
- it
- ru
- zh
- ja
- ko
- ar
- hi
- nl
- pl
- sv
- uk
- cs
- ro
- hu
- el
- vi
- id
- fa
- da
- no
- sk
- sr
- bg
task_categories:
- text-generation
- translation
tags:
- tiny-stories
- child-safe-fiction
- multilingual
- synthetic-data
- literary-quality
- education
size_categories:
- 10K<n<100K
---

# Novelist: TinyStories Multilingual Edition

## Dataset Summary

The **TinyStories Multilingual Edition** is a high-fidelity synthetic dataset of short, child-safe fiction designed to stress-test literary consistency, emotional warmth, and multilingual fluency in small models. Derived from the broader **Novelist** ecosystem, this subset focuses on narrative simplicity paired with complex moral and social themes.

The dataset contains **15,688 high-quality stories** across **28 languages**. Each story is generated using a chain-of-thought planning process that ensures adherence to specific child-centric themes (like patience, sharing, and honesty) and is subsequently scored by a critic model for literary quality.

### Key Stats
- **Total Stories:** 15,688
- **Languages:** 28 (Global coverage)
- **Word Count:** ~2.5M words
- **Avg. Quality Score:** ~9.2 / 10
- **Themes:** 10 Core Developmental Themes

## Narrative Design

Unlike generic story generators, the Novelist TinyStories engine uses a **Blueprint-to-Prose** pipeline. Each story is anchored by:

1.  **Theme Logic:** A specific developmental challenge (e.g., "Finding courage to climb a ladder").
2.  **Sensory Anchors:** Tactile, auditory, or visual details that ground the scene (e.g., "The smell of warm bread", "Wet shoes on stone").
3.  **Body Language Cues:** Emotional states are communicated through observable actions rather than abstract labels.
4.  **Ending Warmth:** Every closure is audited to ensure it provides a "pressure seal" of safety and resolution.

### Core Themes

| Theme | Focus |
| --- | --- |
| **Sharing** | Resource management and empathy. |
| **Trying Again** | Resilience after small, child-scaled setbacks. |
| **Telling the Truth** | Accountability and repairing integrity. |
| **Helping a Friend** | Social solidarity and practical assistance. |
| **Being Patient** | Managing time and anticipation. |
| **Learning to Apologize** | Interpersonal repair and sincere communication. |
| **Asking for Help** | Overcoming the fear of vulnerability. |
| **Taking Turns** | Fairness and social negotiation. |
| **Finding Courage** | Small, brave steps in a large world. |
| **Kindness in Change** | Adjusting to disappointment with grace. |

## Data Structure

The dataset is shared as a `.jsonl` file where each line contains:

```json
{
  "language_code": "tr",
  "output": "Elif ve Ali bahçedeydi...",
  "score": 9.6
}
```

- `language_code`: The ISO 639-1 code for the story.
- `output`: The complete story text in the target language.
- `score`: The final quality score (0-10) assigned by the Judge model.

## Languages & Coverage

The dataset provides a balanced distribution across the following 28 languages:

| Group | Languages |
| --- | --- |
| **European** | English, French, German, Spanish, Portuguese, Italian, Dutch, Polish, Swedish, Danish, Norwegian, Slovak, Serbian, Bulgarian, Czech, Hungarian, Greek, Romanian, Russian, Ukrainian. |
| **Middle Eastern** | Turkish, Arabic, Persian. |
| **Asian** | Chinese, Japanese, Korean, Hindi, Vietnamese, Indonesian. |

## Generation Pipeline

Detailed in the `tinystories.py` engine, the generation follows three distinct phases:

1.  **Planning:** Selection of protagonist, setting, theme, and specific sensory anchors.
2.  **Multilingual Synthesis:** Parallel generation or high-fidelity branch translation depending on the locale.
3.  **Quality Auditing:** A scoring pass that evaluates "Ending Warmth", "Child Safety", and "Theme Consistency". Only stories scoring above the threshold (9+) are included.

## Intended Use

- **Small Model Pre-training:** Excellent for teaching coherence to <1B parameter models.
- **Multilingual Benchmarking:** Comparing literary quality across diverse script types.
- **Safe Data Augmentation:** Providing a guaranteed child-safe corpus for instruction tuning.

---
*Created as part of the Novelist Dataset Project.*
