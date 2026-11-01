---
language:
- ko
license: cc-by-nc-sa-4.0
tags:
- dialogue
- conversation
- evaluation
annotations_creators:
- found
- machine-generated
pretty_name: KoDialogBench
size_categories:
- 10K<n<100K
source_datasets:
- daily_dialog
- empathetic_dialogues
- bavard/personachat_truecased
- socialdial
- aihub/k-sns
- aihub/k-tdd
- aihub/k-ed
- aihub/k-ds
task_categories:
- multiple-choice
configs:
- config_name: dc_topic_k-sns
  data_files:
  - split: test
    path: dialogue_comprehension/topic/k-sns/test.jsonl
- config_name: dc_topic_k-tdd
  data_files:
  - split: test
    path: dialogue_comprehension/topic/k-tdd/test.jsonl
- config_name: dc_topic_socialdial
  data_files:
  - split: test
    path: dialogue_comprehension/topic/socialdial/test.jsonl
- config_name: dc_emotion_k-ed
  data_files:
  - split: test
    path: dialogue_comprehension/emotion/k-ed/test.jsonl
- config_name: dc_emotion_dailydialog
  data_files:
  - split: test
    path: dialogue_comprehension/emotion/dailydialog/test.jsonl
- config_name: dc_emotion_empathetic
  data_files:
  - split: test
    path: dialogue_comprehension/emotion/empathetic_dialogues/test.jsonl
- config_name: dc_relation_socialdial-distance
  data_files:
  - split: test
    path: dialogue_comprehension/relation/socialdial_distance/test.jsonl
- config_name: dc_relation_socialdial-relation
  data_files:
  - split: test
    path: dialogue_comprehension/relation/socialdial_relation/test.jsonl
- config_name: dc_location_socialdial
  data_files:
  - split: test
    path: dialogue_comprehension/location/socialdial/test.jsonl
- config_name: dc_dialog_act_k-tdd
  data_files:
  - split: test
    path: dialogue_comprehension/dialog_act/k-tdd/test.jsonl
- config_name: dc_dialog_act_dailydialog
  data_files:
  - split: test
    path: dialogue_comprehension/dialog_act/dailydialog/test.jsonl
- config_name: dc_fact_k-ds
  data_files:
  - split: test
    path: dialogue_comprehension/fact/k-ds/test.jsonl
- config_name: dc_fact_personachat
  data_files:
  - split: test
    path: dialogue_comprehension/fact/personachat/test.jsonl
- config_name: dc_fact_empathetic
  data_files:
  - split: test
    path: dialogue_comprehension/fact/empathetic_dialogues/test.jsonl
- config_name: rs_k-sns
  data_files:
  - split: test
    path: response_selection/k-sns/test.jsonl
- config_name: rs_k-tdd
  data_files:
  - split: test
    path: response_selection/k-tdd/test.jsonl
- config_name: rs_k-ed
  data_files:
  - split: test
    path: response_selection/k-ed/test.jsonl
- config_name: rs_personachat
  data_files:
  - split: test
    path: response_selection/personachat/test.jsonl
- config_name: rs_dailydialog
  data_files:
  - split: test
    path: response_selection/dailydialog/test.jsonl
- config_name: rs_empathetic
  data_files:
  - split: test
    path: response_selection/empathetic_dialogues/test.jsonl
- config_name: rs_socialdial
  data_files:
  - split: test
    path: response_selection/socialdial/test.jsonl
---

⚠️NOTE: We can't release the datasets originated from AI Hub (K-SNS, K-TDD, K-ED, K-DS) for now, according to the [Terms of Use](https://www.aihub.or.kr/intrcn/guid/usagepolicy.do?currMenu=151&topMenu=105).
We're in consultation with the relevant organizations and will make these public in the appropriate form soon.

# Dataset Card for KoDialogBench

For most of detailed information, please refer to the following:
- **Paper:** [KoDialogBench: Evaluating Conversational Understanding of
Language Models with Korean Dialogue Benchmark](https://arxiv.org/abs/2402.17377)
- **Repository:** [GitHub](https://github.com/sb-jang/kodialogbench)

## Dataset Details

### Dataset Description

KoDialogBench is a benchmark designed to assess the conversational capabilities of language models in Korean language.
To this end, we collected native Korean dialogues on daily topics from public sources (e.g., AI Hub), or translated dialogues from other languages such as English and Chinese.
We then structured these conversations into diverse test datasets, spanning from dialogue comprehension to response selection tasks.
This benchmark consists of 21 test sets, encompassing various aspects of open-domain colloquial dialogues (e.g., topic, emotion, dialog act).

### Data Sources

We collected native Korean dialogues from AI Hub:
- [K-SNS](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=114) stands for Korean SNS (한국어 SNS)
- [K-TDD](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=543) stands for Thematic Daily Dialogues (주제별 텍스트 일상 대화 데이터)
- [K-ED](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=86) stands for Emotional Dialogues (감성 대화 말뭉치)
- [K-DS](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=117) stands for Dialogue Summary (한국어 대화 요약)

We translated public datasets from other languages:
- [DailyDialog](https://huggingface.co/datasets/daily_dialog) from "[DailyDialog: A Manually Labelled Multi-turn Dialogue Dataset](https://aclanthology.org/I17-1099/)"
- [Empathetic Dialogues](https://huggingface.co/datasets/empathetic_dialogues) from "[Towards Empathetic Open-domain Conversation Models: A New Benchmark and Dataset](https://aclanthology.org/P19-1534/)"
- [PersonaChat](https://huggingface.co/datasets/bavard/personachat_truecased) from "[Personalizing Dialogue Agents: I have a dog, do you have pets too?](https://aclanthology.org/P18-1205/)"
- [SocialDial](https://github.com/zhanhl316/SocialDial/blob/main/human_dialogue_data.json) from "[SocialDial: A Benchmark for Socially-Aware Dialogue Systems](https://dl.acm.org/doi/10.1145/3539618.3591877)"

### Data Creation

We utilized diverse meta information such as dialogue topic and speaker's emotion which was already annotated in the original datasets to formulate dialogue-related multiple-choice questions.
To prevent label imbalance, we sampled the equal number of examples from each class.

### Statistics

The dataset has 82,962 examples in total.

| Task                   | Subtask                   | Source                | # Options | # Examples |
|------------------------|---------------------------|-----------------------|-----------|------------|
| Dialogue Comprehension | Topic Classification      | K-SNS                 | 6         | 1200       |
| Dialogue Comprehension | Topic Classification      | K-TDD                 | 19        | 1900       |
| Dialogue Comprehension | Topic Classification      | SocialDial            | 4         | 400        |
| Dialogue Comprehension | Emotion Recognition       | K-ED                  | 6         | 1200       |
| Dialogue Comprehension | Emotion Recognition       | DailyDialog           | 5         | 470        |
| Dialogue Comprehension | Emotion Recognition       | Empathetic Dialogues  | 2         | 2000       |
| Dialogue Comprehension | Relation Classification   | SocialDial (Distance) | 4         | 524        |
| Dialogue Comprehension | Relation Classification   | SocialDial (Relation) | 3         | 330        |
| Dialogue Comprehension | Location Classification   | SocialDial            | 4         | 376        |
| Dialogue Comprehension | Dialog Act Classification | K-TDD                 | 4         | 520        |
| Dialogue Comprehension | Dialog Act Classification | DailyDialog           | 4         | 1000       |
| Dialogue Comprehension | Fact Identification       | K-DS                  | 4         | 1200       |
| Dialogue Comprehension | Fact Identification       | PersonaChat           | 4         | 1000       |
| Dialogue Comprehension | Fact Identification       | Empathetic Dialogues  | 4         | 2394       |
| Response Selection     |                           | K-SNS                 | 5         | 10295      |
| Response Selection     |                           | K-TDD                 | 5         | 10616      |
| Response Selection     |                           | K-ED                  | 5         | 17818      |
| Response Selection     |                           | PersonaChat           | 5         | 7801       |
| Response Selection     |                           | DailyDialog           | 5         | 6740       |
| Response Selection     |                           | Empathetic Dialogues  | 5         | 7941       |
| Response Selection     |                           | SocialDial            | 5         | 7237       |



## Limitations

Our benchmark may suffer from a chronic problem of benchmark contamination.
Due to the scarcity of Korean language resources, there is a possibility that the held-out sources utilized to construct the benchmark might overlap with training data used for some language models.

## Ethics Statement

Our benchmark dataset is designed to assess capabilities related to various situations and aspects of conversations in Korean language.
To achieve this, we utilized conversational content from publicly available datasets from various sources, either without modification or with translation if necessary.
During this process, there is a possibility that harmful content or inappropriate biases existing in the original data may have been conveyed, or may have arisen due to limitations of translation tools.
We reject any form of violence, discrimination, or offensive language, and our benchmark dataset and experimental results does not represent such values.
If any harmful content or privacy infringement is identified within the dataset, we kindly request immediate notification to the authors.
In the event of such cases being reported, we will apply the highest ethical standards and take appropriate actions.

## Citation

**BibTeX:**

```bibtex
@misc{jang2024kodialogbench,
      title={KoDialogBench: Evaluating Conversational Understanding of Language Models with Korean Dialogue Benchmark}, 
      author={Seongbo Jang and Seonghyeon Lee and Hwanjo Yu},
      year={2024},
      eprint={2402.17377},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

## Point of Contact

[Seongbo Jang](mailto:jang.sb@postech.ac.kr)