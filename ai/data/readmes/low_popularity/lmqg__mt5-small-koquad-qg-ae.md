
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
- answer extraction
widget:
- text: "generate question: 1990년 영화 《 <hl> 남부군 <hl> 》에서 단역으로 영화배우 첫 데뷔에 이어 같은 해 KBS 드라마 《지구인》에서 단역으로 출연하였고 이듬해 MBC 《여명의 눈동자》를 통해 단역으로 출연하였다."
  example_title: "Question Generation Example 1" 
- text: "generate question: 백신이 없기때문에 예방책은 <hl> 살충제 <hl> 를 사용하면서 서식 장소(찻찬 받침, 배수로, 고인 물의 열린 저장소, 버려진 타이어 등)의 수를 줄임으로써 매개체를 통제할 수 있다."
  example_title: "Question Generation Example 2" 
- text: "generate question: <hl> 원테이크 촬영 <hl> 이기 때문에 한 사람이 실수를 하면 처음부터 다시 찍어야 하는 상황이 발생한다."
  example_title: "Question Generation Example 3" 
- text: "extract answers: 또한 스피어스는 많은 새로운 여성 아티스트들에게 영향을 끼쳤는데, 대표적으로 데미 로바토, 케이티 페리, 크리스티니아 드바지, 레이디 가가, 리틀 부츠, 셀레나 고메즈 & 더씬, 픽시 로트 이 있다. 2007년 비욘세 놀스는 Total Request Live와의 인터뷰에서 '나는 브리트니를 사랑하고 팬이에요. 특히 새 앨범 Blackout을 좋아해요'라고 말했다. 린제이 로한은 '언제나 브리트니 스피어스에게 영감을 받는다. 학창시절 그녀처럼 타블로이드에 오르기를 꿈꿔왔다'고 말하며 롤 모델로 꼽았다. 스피어스는 현대 음악가들에게 음악적 영감으로 언급되기도 했다. <hl> 마일리 사이러스는 자신의 히트곡 Party in the U.S.A. 가 브리트니에게 영감과 영향을 받은 곡이라고 밝혔다. <hl> 베리 매닐로우의 앨범 15 Minutes 역시 브리트니에게 영감을 얻었다고 언급되었다."
  example_title: "Answer Extraction Example 1" 
- text: "extract answers: 지난 22일 아프리카TV는 BJ 철구가 서비스 정지 처분을 받았음을 밝혔다. 서비스 정지 처분을 사유는 철구가 10대 청소년에게 유해한 장면을 방송으로 내보냈기 때문이었다. 문제가 된 장면은 BJ 철구가 미성년자는 시청할 수 없게 하는 19세 시청 가능 설정을 하지 않은 채 흡연하는 모습을 여과 없이 드러낸 장면이다. 아프리카TV는 청소년 보호 정책의 '청소년들이 해로운 환경으로부터 보호받을 수 있도록 조치한다'라고 조항을 근거로 철구에게 서비스 정지 처분을 내렸다. 흡연 이외에 음주 방송 등도 19세 시청 가능 설정을 해야만 방송할 수 있다. <hl> 게다가 철구의 방송 정지 처분은 이번에 처음이 아니라 16번 째기 때문에 더욱더 논란이 되고 있다. <hl>"
  example_title: "Answer Extraction Example 2" 
model-index:
- name: lmqg/mt5-small-koquad-qg-ae
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
      value: 10.91
    - name: ROUGE-L (Question Generation)
      type: rouge_l_question_generation
      value: 25.83
    - name: METEOR (Question Generation)
      type: meteor_question_generation
      value: 27.52
    - name: BERTScore (Question Generation)
      type: bertscore_question_generation
      value: 83.4
    - name: MoverScore (Question Generation)
      type: moverscore_question_generation
      value: 82.54
    - name: QAAlignedF1Score-BERTScore (Question & Answer Generation (with Gold Answer))
      type: qa_aligned_f1_score_bertscore_question_answer_generation_with_gold_answer
      value: 80.36
    - name: QAAlignedRecall-BERTScore (Question & Answer Generation (with Gold Answer))
      type: qa_aligned_recall_bertscore_question_answer_generation_with_gold_answer
      value: 83.72
    - name: QAAlignedPrecision-BERTScore (Question & Answer Generation (with Gold Answer))
      type: qa_aligned_precision_bertscore_question_answer_generation_with_gold_answer
      value: 77.34
    - name: QAAlignedF1Score-MoverScore (Question & Answer Generation (with Gold Answer))
      type: qa_aligned_f1_score_moverscore_question_answer_generation_with_gold_answer
      value: 82.55
    - name: QAAlignedRecall-MoverScore (Question & Answer Generation (with Gold Answer))
      type: qa_aligned_recall_moverscore_question_answer_generation_with_gold_answer
      value: 86.69
    - name: QAAlignedPrecision-MoverScore (Question & Answer Generation (with Gold Answer))
      type: qa_aligned_precision_moverscore_question_answer_generation_with_gold_answer
      value: 78.93
    - name: BLEU4 (Answer Extraction)
      type: bleu4_answer_extraction
      value: 38.2
    - name: ROUGE-L (Answer Extraction)
      type: rouge_l_answer_extraction
      value: 82.32
    - name: METEOR (Answer Extraction)
      type: meteor_answer_extraction
      value: 59.91
    - name: BERTScore (Answer Extraction)
      type: bertscore_answer_extraction
      value: 95.65
    - name: MoverScore (Answer Extraction)
      type: moverscore_answer_extraction
      value: 94.61
    - name: AnswerF1Score (Answer Extraction)
      type: answer_f1_score__answer_extraction
      value: 86.98
    - name: AnswerExactMatch (Answer Extraction)
      type: answer_exact_match_answer_extraction
      value: 80.78
---

# Model Card of `lmqg/mt5-small-koquad-qg-ae`
This model is fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) for question generation and answer extraction jointly on the [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) (dataset_name: default) via [`lmqg`](https://github.com/asahi417/lm-question-generation).


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
model = TransformersQG(language="ko", model="lmqg/mt5-small-koquad-qg-ae")

# model prediction
question_answer_pairs = model.generate_qa("1990년 영화 《 남부군 》에서 단역으로 영화배우 첫 데뷔에 이어 같은 해 KBS 드라마 《지구인》에서 단역으로 출연하였고 이듬해 MBC 《여명의 눈동자》를 통해 단역으로 출연하였다.")

```

- With `transformers`
```python
from transformers import pipeline

pipe = pipeline("text2text-generation", "lmqg/mt5-small-koquad-qg-ae")

# answer extraction
answer = pipe("generate question: 1990년 영화 《 <hl> 남부군 <hl> 》에서 단역으로 영화배우 첫 데뷔에 이어 같은 해 KBS 드라마 《지구인》에서 단역으로 출연하였고 이듬해 MBC 《여명의 눈동자》를 통해 단역으로 출연하였다.")

# question generation
question = pipe("extract answers: 또한 스피어스는 많은 새로운 여성 아티스트들에게 영향을 끼쳤는데, 대표적으로 데미 로바토, 케이티 페리, 크리스티니아 드바지, 레이디 가가, 리틀 부츠, 셀레나 고메즈 & 더씬, 픽시 로트 이 있다. 2007년 비욘세 놀스는 Total Request Live와의 인터뷰에서 '나는 브리트니를 사랑하고 팬이에요. 특히 새 앨범 Blackout을 좋아해요'라고 말했다. 린제이 로한은 '언제나 브리트니 스피어스에게 영감을 받는다. 학창시절 그녀처럼 타블로이드에 오르기를 꿈꿔왔다'고 말하며 롤 모델로 꼽았다. 스피어스는 현대 음악가들에게 음악적 영감으로 언급되기도 했다. <hl> 마일리 사이러스는 자신의 히트곡 Party in the U.S.A. 가 브리트니에게 영감과 영향을 받은 곡이라고 밝혔다. <hl> 베리 매닐로우의 앨범 15 Minutes 역시 브리트니에게 영감을 얻었다고 언급되었다.")

```

## Evaluation


- ***Metric (Question Generation)***: [raw metric file](https://huggingface.co/lmqg/mt5-small-koquad-qg-ae/raw/main/eval/metric.first.sentence.paragraph_answer.question.lmqg_qg_koquad.default.json) 

|            |   Score | Type    | Dataset                                                          |
|:-----------|--------:|:--------|:-----------------------------------------------------------------|
| BERTScore  |   83.4  | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| Bleu_1     |   25.91 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| Bleu_2     |   19.09 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| Bleu_3     |   14.37 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| Bleu_4     |   10.91 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| METEOR     |   27.52 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| MoverScore |   82.54 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| ROUGE_L    |   25.83 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |


- ***Metric (Question & Answer Generation)***:  [raw metric file](https://huggingface.co/lmqg/mt5-small-koquad-qg-ae/raw/main/eval/metric.first.answer.paragraph.questions_answers.lmqg_qg_koquad.default.json)

|                                 |   Score | Type    | Dataset                                                          |
|:--------------------------------|--------:|:--------|:-----------------------------------------------------------------|
| QAAlignedF1Score (BERTScore)    |   80.36 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| QAAlignedF1Score (MoverScore)   |   82.55 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| QAAlignedPrecision (BERTScore)  |   77.34 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| QAAlignedPrecision (MoverScore) |   78.93 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| QAAlignedRecall (BERTScore)     |   83.72 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| QAAlignedRecall (MoverScore)    |   86.69 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |


- ***Metric (Answer Extraction)***: [raw metric file](https://huggingface.co/lmqg/mt5-small-koquad-qg-ae/raw/main/eval/metric.first.answer.paragraph_sentence.answer.lmqg_qg_koquad.default.json)

|                  |   Score | Type    | Dataset                                                          |
|:-----------------|--------:|:--------|:-----------------------------------------------------------------|
| AnswerExactMatch |   80.78 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| AnswerF1Score    |   86.98 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| BERTScore        |   95.65 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| Bleu_1           |   75.14 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| Bleu_2           |   66.16 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| Bleu_3           |   53.61 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| Bleu_4           |   38.2  | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| METEOR           |   59.91 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| MoverScore       |   94.61 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |
| ROUGE_L          |   82.32 | default | [lmqg/qg_koquad](https://huggingface.co/datasets/lmqg/qg_koquad) |



## Training hyperparameters

The following hyperparameters were used during fine-tuning:
 - dataset_path: lmqg/qg_koquad
 - dataset_name: default
 - input_types: ['paragraph_answer', 'paragraph_sentence']
 - output_types: ['question', 'answer']
 - prefix_types: ['qg', 'ae']
 - model: google/mt5-small
 - max_length: 512
 - max_length_output: 32
 - epoch: 6
 - batch: 16
 - lr: 0.001
 - fp16: False
 - random_seed: 1
 - gradient_accumulation_steps: 4
 - label_smoothing: 0.15

The full configuration can be found at [fine-tuning config file](https://huggingface.co/lmqg/mt5-small-koquad-qg-ae/raw/main/trainer_config.json).

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
