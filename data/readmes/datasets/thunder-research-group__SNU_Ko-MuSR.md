---
dataset_info:
- config_name: murder_mysteries
  features:
  - name: narrative
    dtype: string
  - name: question
    dtype: string
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  - name: answer_choice
    dtype: string
  - name: narrative_before_edit
    dtype: string
  splits:
  - name: test
    num_bytes: 2879131
    num_examples: 250
  download_size: 1491327
  dataset_size: 2879131
- config_name: object_placements
  features:
  - name: narrative
    dtype: string
  - name: question
    dtype: string
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  - name: answer_choice
    dtype: string
  - name: narrative_before_edit
    dtype: string
  splits:
  - name: test
    num_bytes: 1242870
    num_examples: 250
  download_size: 128275
  dataset_size: 1242870
- config_name: team_allocation
  features:
  - name: narrative
    dtype: string
  - name: question
    dtype: string
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  - name: answer_choice
    dtype: string
  - name: narrative_before_edit
    dtype: string
  splits:
  - name: test
    num_bytes: 1436040
    num_examples: 250
  download_size: 703719
  dataset_size: 1436040
configs:
- config_name: murder_mysteries
  data_files:
  - split: test
    path: murder_mysteries/test-*
- config_name: object_placements
  data_files:
  - split: test
    path: object_placements/test-*
- config_name: team_allocation
  data_files:
  - split: test
    path: team_allocation/test-*
license: mit
language:
- ko
preety_name: Ko-MuSR
---
# Dataset Card for SNU Ko-MuSR

## Dataset Summary

SNU Ko-MuSR is a Korean adaptation of [MuSR](https://huggingface.co/datasets/TAUR-Lab/MuSR), a benchmark designed to assess multistep reasoning abilities of large language models.
It evaluates a model's ability to extract facts from long narratives, perform multi-step soft reasoning and deduce the conclusion according to the task settings.

The benchmark consists of three subtasks: `murder mysteries`, `object placements` and `team allocations`, according to the MuSR benchmark. 

1.	Murder Mysteries – Determining the culprit based on evidence of means, motive, and opportunity.
2.	Object Placements – Tracking beliefs and locations of objects through observed and unobserved movements.
3.	Team Allocations – Forming optimal team compositions considering skills, personalities, and interpersonal dynamics.

## Supported Tasks and Benchmarks

**Task**: Multistep Soft Reasoning

SNU Ko-MuSR evaluates a language models' ability to:
- extract facts from long narratives
- perform multi-step soft reasoning
- deduce the conlusion according to the task settings

## Languages

ko(Korean)

> We utilize LM-Evaluation-Harness for evaluating this task. See [our repository](https://github.com/mcrl/Ko-MuSR) for task configuration yaml files.


## Dataset Structure
### Data Instance Example

```json
{
  "narrative": "금요일 아침, 교육기관의... 제작 팀과 플랫폼 개발 팀 중, 각자의 능력이 가장 빛날 자리는 어디일까?",
  "question": "이 이야기를 바탕으로, 두 가지 업무가 모두 효율적으로 수행되도록 사람을 어떻게 배정하시겠습니까?",
  "choices": '["콘텐츠 제작 팀: 동욱 - 플랫폼 개발 팀: 수현, 지민", "콘텐츠 제작 팀: 지민 - 플랫폼 개발 팀: 동욱, 수현", "콘텐츠 제작 팀: 수현 - 플랫폼 개발 팀: 동욱, 지민"]',
  "answer": 2,
  "answer_choice": "콘텐츠 제작 팀: 수현 - 플랫폼 개발 팀: 동욱, 지민",
  "narrative_before_edit": "금요일 아침, 교육기관의... 제작 팀과 플랫폼 개발 팀 중, 각자의 능력이 가장 빛날 자리는 어디일까?",
}
```

### Data Fields

- `narrative`: The narrative from which the model should obtain answer
- `question`: The question the model should solve
- `choices`: The list of answer choices
- `answer`: The index of the answer, starting from 0
- `answer_choice`: The content of the answer choice
- `narrative_before_edit`: The content of the initial version of machine generated narrative. This version contains the synthesized text without minor edit stages.

### Data Configuration Names
-  murder_mysteries
-  object_placements
-  team_allocation

### Data Splits
- Single evaluation set(`test` set)
- See yaml configuration files for few-shot example splits

## Dataset Creation

Following the [MuSR pipeline](https://github.com/Zayne-sprague/MuSR), we synthesize the narrative with three steps:

1.	Sampling stage: Seeds such as names, objects, or settings are drawn from predefined domains (e.g., crime scenes, workplaces).
2.	Reasoning tree expansion: An LLM expands a logical reasoning tree by adding fact nodes and commonsense knowledge nodes, ensuring internal coherence.
3.	Narrative generation: Another model converts the reasoning tree into a natural, human-readable story that implicitly embeds all reasoning facts.

This process guarantees consistency between the story and its underlying reasoning logic.

SNU Ko-MuSR adapts the synthesis pipeline of the original MuSR benchmark (Sprague et al., 2024) to the Korean language and culture. The objective is to construct a contamination-free, narrative-based benchmark that evaluates multistep soft reasoning in Korean while preserving the logical rigor and task structure of MuSR. Like MuSR, Ko-MuSR comprises three reasoning domains — Murder Mysteries, Object Placements, and Team Allocations — each requiring multi-step reasoning over long-form narratives.

We employed OpenAI’s GPT-4o and o1 models for both reasoning-tree expansion and narrative generation. After synthesis, human annotators examined each instance to confirm that (i) the correct answer could be inferred unambiguously from the narrative, (ii) the story remained coherent and natural in Korean, and (iii) no trivial or stylistically inconsistent expressions appeared. To ensure solvability, we additionally recruited independent participants with no prior exposure to the dataset. Their feedback led to the removal of ambiguous or logically inconsistent examples, guaranteeing that all remaining examples were valid, solvable, and logically consistent.

While following MuSR’s overall structure, Ko-MuSR introduces several key modifications to ensure cultural and linguistic fidelity:
•	Korean-specific domain seeds were generated using GPT-4o for Object Placement and Team Allocation tasks. For Murder Mysteries, culturally coherent Korean names and crime-scene settings were created.
•	All prompts for reasoning-tree construction and narrative generation were fully translated into Korean, preserving logical consistency while avoiding English keywords that could trivialize reasoning.
These adaptations ensure that Ko-MuSR retains the reasoning depth of MuSR while producing natural Korean narratives.


## Additional Information

### Licensing

This dataset is licensed under the MIT License

### Citation

To be added

### Contact Information

If you find something wrong or have question about the dataset, contact snullm@aces.snu.ac.kr.