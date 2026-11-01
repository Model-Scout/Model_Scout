---
license: mit
dataset_info:
  features:
  - name: prompt
    dtype: string
  - name: reference_answer
    dtype: string
  - name: reference_answer_fullscale
    dtype: string
  splits:
  - name: test
    num_bytes: 394522
    num_examples: 171
  download_size: 106019
  dataset_size: 394522
configs:
- config_name: default
  data_files:
  - split: test
    path: data/validation-*
language:
- ko
pretty_name: Ko-EQ-Bench
---

# Dataset Card for Ko-EQ-Bench

## Dataset Summary

Ko-EQ-Bench is a Korean adaptation of [EQ-Bench](https://huggingface.co/datasets/pbevan11/EQ-Bench), a benchmark designed to assess the emotional intelligence of large language models. 
It evaluates a model's ability to interpret emotions in dialogue by predicting the relative intensity of several possible emotional responses of a character.

The benchmark consists of fictional and realistic Korean dialogues featuring interpersonal conflict or tension, followed by a prompt instructing the model to score specific emotions on a 0–10 scale. 
Each question has a human-generated reference answer and a full-scale variant.

## Supported Tasks and Benchmarks
**Task**: Emotion Recognition and Intensity Prediction    

Ko-EQ-Bench evaluates a language model's ability to:
- Interpret nuanced emotional states from Korean dialogue
- Predict the intensity of multiple candidate emotions
- Follow formatting instructions with fidelity in Korean

## Languages
ko (Korean)

---

> Note: Evaluation code and task configurations for this benchmark are available in the [`evaluation_code`](https://github.com/mcrl/korean_benchmarks/tree/main/evaluation_code) directory of the [Korean Benchmark Suite GitHub repository](https://github.com/mcrl/korean_benchmarks). The evaluation setup is built on the Language Model Evaluation Harness and supports standardized model assessment.

## Dataset Structure

### Dataset Instance Example
```json
{
  "prompt": "여러분의 임무는 이 대화에서 인물이 보일 수 있는 감정 반응을 예측하는 것입니다.\n\n민준: 서윤 씨, 당신은 늘 이상적인 시각을 고수해왔죠. 하지만 이번 한 번만이라도 현실적으로 생각해 볼 수 있을까요?\n서윤: 현실적이라, 네가 말하는 현실성이란, 모든 걸 힘으로 밀어붙이는 걸 의미하잖아.\n민준: 그걸 우리는 ‘진보’라고 부릅니다, 서윤 씨. 세상은 그렇게 돌아가니까요.\n서윤: 적어도 내 세상에서는 아니야, 민준.\n민준: '내 세상'이요? 혹시 당신이 말하는 그... 성역을 뜻하나요?\n서윤: 성역이 아니라, 우리 부모님이 자연을 얼마나 사랑했는지 보여주는 증거야.\n민준: 그건 감성적인 얘기일 뿐이고, 감성으로는 우리 회사를 굴릴 수 없어요, 서윤 씨.\n서윤: 돈으로 벌목한 나무를 되살릴 수는 없잖아, 민준.\n민준: 이건 나무 한두 그루의 문제가 아니에요, 서윤 씨. 우리 회사의 생존이 달린 문제입니다.\n서윤: 그렇다면 이 땅을 고향으로 여기는 생명들의 생존은?\n민준: 환경은 늘 적응해왔어요. 이번에도 그럴 겁니다.\n서윤: 이번엔 다를 거야, 민준. 내가 그렇게 만들 거니까.\n민준: 서윤 씨, 당신에겐 선택의 여지가 없습니다. 팔지 않으면, 강제로 압류할 겁니다.\n[대화 끝]\n\n이 대화가 끝나면 서윤은 다음과 같이 느낄 것입니다.\n희망적\n위협받음\n연민\n반항적\n\n이러한 각 감정의 상대적 강도에 대해 0~10점 사이의 점수를 부여하세요.\n\n항목을 포함하여 다음 형식으로 출력해야 하며(물론 직접 점수를 매겨야 함), 추가 설명은 하지 않아야 합니다:\n\n희망적: <점수>\n위협받음: <점수>\n연민: <점수>\n반항적: <점수>\n\n[답변 끝]\n\n주의: 0점은 유효한 점수로, 해당 감정을 느끼지 않을 가능성이 높다는 의미입니다. 0점보다 큰 감정 점수를 하나 이상 받아야 합니다.\n\n답:",
  "reference_answer": {
    "emotion1": "희망적",
    "emotion2": "위협받음",
    "emotion3": "연민",
    "emotion4": "반항적",
    "emotion1_score": 0,
    "emotion2_score": 4,
    "emotion3_score": 0,
    "emotion4_score": 6
  },
  "reference_answer_fullscale": {
    "emotion1": "희망적",
    "emotion2": "위협받음",
    "emotion3": "연민",
    "emotion4": "반항적",
    "emotion1_score": "0",
    "emotion2_score": "8",
    "emotion3_score": "0",
    "emotion4_score": "9"
  }
}
```

### Data Fields
- `prompt`: Task description, character dialogue, and scoring instruction in Korean.
- `reference_answer`: Ground truth emotional intensity scores (compressed scale).
- `reference_answer_fullscale`: Full-scale scores used for finer evaluation.

### Data Splits
- Single evaluation set (`test` set)

---

## Dataset Creation
### Translation Process
The original EQ-Bench dataset was translated and localized to Korean through a four-stage pipeline:

#### 1. Initial Translation
- Used [DeepL API](https://www.deepl.com/ko/products/api) to translate English prompts and dialogues into Korean.

#### 2. Correction
Domain experts reviewed and corrected:
- Translation inconsistencies and errors in tone, formality, and phrasing.
- Awkward or unnatural Korean expressions.
- Emotion labeling discrepancies due to ambiguous mappings.
- Repetition of names or titles (overused honorifics like “서진 씨” were reduced for naturalness in Korean language).
- Ambiguous or idiomatic English phrases were reinterpreted in Korean context (e.g., "haunted" (literally, "귀신이 나오는") → "계속 떠오른다").
- Standardized frequently used prompt format and tone.

#### 3. Localization
Localized content with consideration of Korean culture:
- English names were replaced with Korean equivalents except where specific nationalities were part of the narrative.
- Adjusted honorifics and relationship expressions to match natural Korean social interaction norms.
- Carefully translated nuanced emotional expressions.
- Used a documented mapping table to unify emotion translations (see the [emotion list](https://huggingface.co/datasets/thunder-research-group/snu_eqbench/blob/main/emotions_list.csv) for more information).   
  - Emotions in English often have fine-grained distinctions not present in Korean; to ensure consistency, translations were standardized to one-to-one mappings where possible.
  - Context-dependent adjustments were made when needed (e.g., "Victimized" → "피해의식").

#### 4. Cross-review
- Independent reviewers re-checked the entire dataset to fix missed or subjective inconsistencies.

--- 

## Additional Information

### Licensing Information

This dataset is licensed under the MIT License.

### Citation Information

#### Our Citation Information
```
@inproceedings{
so2026constructing,
title={Constructing Korean Benchmark Suite for Reliable Evaluation of Foundation Models},
author={Yeonkyoung So and Jongmin Kim and Sungmok Jung and Gyuseong Lee and Sangho Kim and Jongyeon Park and Joonhak Lee and Seho Pyo and Gyeongje Cho and Seorin Kim and Jisoo Kim and Suyoung Park and Hyunji M. Park and Yelim Ahn and Yeongho Seo and Jaejin Lee},
booktitle={ICML 2026 Workshop on Combining Theory and Benchmarks: Towards A Virtuous Cycle to Understand and Guarantee Foundation Model Performance},
year={2026},
url={https://openreview.net/forum?id=oJ3rhISSqO}
}
```

#### Original Dataset Citation Information
```bibtex
@misc{paech2023eqbench,
	title={EQ-Bench: An Emotional Intelligence Benchmark for Large Language Models},
	author={Samuel J. Paech},
	year={2023},
	eprint={2312.06281},
	archivePrefix={arXiv},
	primaryClass={cs.CL}
}
```

### Contact Information

If you find something wrong or have question about the dataset, contact snullm@aces.snu.ac.kr.