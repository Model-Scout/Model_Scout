
---
license: cc-by-4.0
metrics:
- bleu4
- meteor
- rouge-l
- bertscore
- moverscore
language: ko
datasets:
- lmqg/qg_koquad
pipeline_tag: text2text-generation
tags:
- question generation
widget:
- text: "1990년 영화 《 <hl> 남부군 <hl> 》에서 단역으로 영화배우 첫 데뷔에 이어 같은 해 KBS 드라마 《지구인》에서 단역으로 출연하였고 이듬해 MBC 《여명의 눈동자》를 통해 단역으로 출연하였다."
  example_title: "Question Generation Example 1" 
- text: "백신이 없기때문에 예방책은 <hl> 살충제 <hl> 를 사용하면서 서식 장소(찻찬 받침, 배수로, 고인 물의 열린 저장소, 버려진 타이어 등)의 수를 줄임으로써 매개체를 통제할 수 있다."
  example_title: "Question Generation Example 2" 
- text: "<hl> 원테이크 촬영 <hl> 이기 때문에 한 사람이 실수를 하면 처음부터 다시 찍어야 하는 상황이 발생한다."
  example_title: "Question Generation Example 3" 
model-index:
- name: lmqg/mt5-small-koquad-qg
  results:
  - task:
      name: Text2text Generation
      type: text2text-generation
    dataset:
      name: lmqg/qg_koquad
      type: default
      args: default
    metrics:
    - name: BLEU4 (Question Generation)
      type: bleu4_question_generation
      value: 10.57
    - name: ROUGE-L (Question Generation)
      type: rouge_l_question_generation
      value: 25.64
    - name: METEOR (Question Generation)
      type: meteor_question_generation
      value: 27.52
    - name: BERTScore (Question Generation)
      type: bertscore_question_generation
      value: 82.89
    - name: MoverScore (Question Generation)
      type: moverscore_question_generation
      value: 82.49
    - name: QAAlignedF1Score-BERTScore (Question & Answer Generation (with Gold Answer)) [Gold Answer]
      type: qa_aligned_f1_score_bertscore_question_answer_generation_with_gold_answer_gold_answer
      value: 87.52
    - name: QAAlignedRecall-BERTScore (Question & Answer Generation (with Gold Answer)) [Gold Answer]
      type: qa_aligned_recall_bertscore_question_answer_generation_with_gold_answer_gold_answer
      value: 87.49
    - name: QAAlignedPrecision-BERTScore (Question & Answer Generation (with Gold Answer)) [Gold Answer]
      type: qa_aligned_precision_bertscore_question_answer_generation_with_gold_answer_gold_answer
      value: 87.57
    - name: QAAlignedF1Score-MoverScore (Question & Answer Generation (with Gold Answer)) [Gold Answer]
      type: qa_aligned_f1_score_moverscore_question_answer_generation_with_gold_answer_gold_answer
      value: 85.15
    - name: QAAlignedRecall-MoverScore (Question & Answer Generation (with Gold Answer)) [Gold Answer]
      type: qa_aligned_recall_moverscore_question_answer_generation_with_gold_answer_gold_answer
      value: 85.09
    - name: QAAlignedPrecision-MoverScore (Question & Answer Generation (with Gold Answer)) [Gold Answer]
      type: qa_aligned_precision_moverscore_question_answer_generation_with_gold_answer_gold_answer
      value: 85.23
    - name: QAAlignedF1Score-BERTScore (Question & Answer Generation) [Gold Answer]
      type: qa_aligned_f1_score_bertscore_question_answer_generation_gold_answer
      value: 80.52
    - name: QAAlignedRecall-BERTScore (Question & Answer Generation) [Gold Answer]
      type: qa_aligned_recall_bertscore_question_answer_generation_gold_answer
      value: 83.8
    - name: QAAlignedPrecision-BERTScore (Question & Answer Generation) [Gold Answer]
      type: qa_aligned_precision_bertscore_question_answer_generation_gold_answer
      value: 77.56
    - name: QAAlignedF1Score-MoverScore (Question & Answer Generation) [Gold Answer]
      type: qa_aligned_f1_score_moverscore_question_answer_generation_gold_answer
      value: 82.95
    - name: QAAlignedRecall-MoverScore (Question & Answer Generation) [Gold Answer]
      type: qa_aligned_recall_moverscore_question_answer_generation_gold_answer
      value: 87.02
    - name: QAAlignedPrecision-MoverScore (Question & Answer Generation) [Gold Answer]
      type: qa_aligned_precision_moverscore_question_answer_generation_gold_answer
      value: 79.39
---

# Model Card of `lmqg/mt5-small-koquad-qg`
This model is fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) for question generation task on the [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) (dataset_name: default) via [`lmqg`](https://github.com/asahi417/lm-question-generation).


### Overview
- **Language model:** [google/mt5-small](https://huggingface.co/google/mt5-small)   
- **Language:** ko  
- **Training data:** [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) (default)
- **Online Demo:** [https://autoqg.net/](https://autoqg.net/)
- **Repository:** [https://github.com/asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation)
- **Paper:** [https://arxiv.org/abs/2210.03992](https://arxiv.org/abs/2210.03992)

### Usage
- With [`lmqg`](https://github.com/asahi417/lm-question-generation#lmqg-language-model-for-question-generation-)
```python
from lmqg import TransformersQG

# initialize model
model = TransformersQG(language="ko", model="lmqg/mt5-small-koquad-qg")

# model prediction
questions = model.generate_q(list_context="1990년 영화 《 남부군 》에서 단역으로 영화배우 첫 데뷔에 이어 같은 해 KBS 드라마 《지구인》에서 단역으로 출연하였고 이듬해 MBC 《여명의 눈동자》를 통해 단역으로 출연하였다.", list_answer="남부군")

```

- With `transformers`
```python
from transformers import pipeline

pipe = pipeline("text2text-generation", "lmqg/mt5-small-koquad-qg")
output = pipe("1990년 영화 《 <hl> 남부군 <hl> 》에서 단역으로 영화배우 첫 데뷔에 이어 같은 해 KBS 드라마 《지구인》에서 단역으로 출연하였고 이듬해 MBC 《여명의 눈동자》를 통해 단역으로 출연하였다.")

```

## Evaluation


- ***Metric (Question Generation)***: [raw metric file](https://huggingface.co/lmqg/mt5-small-koquad-qg/raw/main/eval/metric.first.sentence.paragraph_answer.question.lmqg_qg_koquad.default.json) 

|            |   Score | Type    | Dataset                                                          |
|:-----------|--------:|:--------|:-----------------------------------------------------------------|
| BERTScore  |   82.89 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| Bleu_1     |   25.31 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| Bleu_2     |   18.59 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| Bleu_3     |   13.98 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| Bleu_4     |   10.57 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| METEOR     |   27.52 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| MoverScore |   82.49 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| ROUGE_L    |   25.64 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |


- ***Metric (Question & Answer Generation, Reference Answer)***: Each question is generated from *the gold answer*. [raw metric file](https://huggingface.co/lmqg/mt5-small-koquad-qg/raw/main/eval/metric.first.answer.paragraph.questions_answers.lmqg_qg_koquad.default.json)

|                                 |   Score | Type    | Dataset                                                          |
|:--------------------------------|--------:|:--------|:-----------------------------------------------------------------|
| QAAlignedF1Score (BERTScore)    |   87.52 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| QAAlignedF1Score (MoverScore)   |   85.15 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| QAAlignedPrecision (BERTScore)  |   87.57 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| QAAlignedPrecision (MoverScore) |   85.23 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| QAAlignedRecall (BERTScore)     |   87.49 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| QAAlignedRecall (MoverScore)    |   85.09 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |


- ***Metric (Question & Answer Generation, Pipeline Approach)***: Each question is generated on the answer generated by [`lmqg/mt5-small-koquad-ae`](https://huggingface.co/lmqg/mt5-small-koquad-ae). [raw metric file](https://huggingface.co/lmqg/mt5-small-koquad-qg/raw/main/eval_pipeline/metric.first.answer.paragraph.questions_answers.lmqg_qg_koquad.default.lmqg_mt5-small-koquad-ae.json)

|                                 |   Score | Type    | Dataset                                                          |
|:--------------------------------|--------:|:--------|:-----------------------------------------------------------------|
| QAAlignedF1Score (BERTScore)    |   80.52 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| QAAlignedF1Score (MoverScore)   |   82.95 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| QAAlignedPrecision (BERTScore)  |   77.56 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| QAAlignedPrecision (MoverScore) |   79.39 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| QAAlignedRecall (BERTScore)     |   83.8  | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| QAAlignedRecall (MoverScore)    |   87.02 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |



## Training hyperparameters

The following hyperparameters were used during fine-tuning:
 - dataset_path: lmqg/qg_koquad
 - dataset_name: default
 - input_types: ['paragraph_answer']
 - output_types: ['question']
 - prefix_types: None
 - model: google/mt5-small
 - max_length: 512
 - max_length_output: 32
 - epoch: 7
 - batch: 16
 - lr: 0.001
 - fp16: False
 - random_seed: 1
 - gradient_accumulation_steps: 4
 - label_smoothing: 0.15

The full configuration can be found at [fine-tuning config file](https://huggingface.co/lmqg/mt5-small-koquad-qg/raw/main/trainer_config.json).

## Citation
```
@inproceedings{ushio-etal-2022-generative,
    title = "{G}enerative {L}anguage {M}odels for {P}aragraph-{L}evel {Q}uestion {G}eneration",
    author = "Ushio, Asahi  and
        Alva-Manchego, Fernando  and
        Camacho-Collados, Jose",
    booktitle = "Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, U.A.E.",
    publisher = "Association for Computational Linguistics",
}

```
