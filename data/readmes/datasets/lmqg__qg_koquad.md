---
license: cc-by-4.0
pretty_name: KorQuAD for question generation
language: ko
multilinguality: monolingual
size_categories: 10K<n<100K
source_datasets: squad_es
task_categories:
- text-generation
task_ids:
- language-modeling
tags:
- question-generation
---

# Dataset Card for "lmqg/qg_korquad"

## Dataset Description
- **Repository:** [https://github.com/asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation)
- **Paper:** [https://arxiv.org/abs/2210.03992](https://arxiv.org/abs/2210.03992)
- **Point of Contact:** [Asahi Ushio](http://asahiushio.com/)

### Dataset Summary
This is a subset of [QG-Bench](https://github.com/asahi417/lm-question-generation/blob/master/QG_BENCH.md#datasets), a unified question generation benchmark proposed in
 ["Generative Language Models for Paragraph-Level Question Generation: A Unified Benchmark and Evaluation, EMNLP 2022 main conference"](https://arxiv.org/abs/2210.03992).
This is a modified version of [KorQuAD](https://huggingface.co/datasets/squad_kor_v1) for question generation (QG) task.
Since the original dataset only contains training/validation set, we manually sample test set from training set, which
has no overlap in terms of the paragraph with the training set.

### Supported Tasks and Leaderboards
* `question-generation`: The dataset is assumed to be used to train a model for question generation.
  Success on this task is typically measured by achieving a high BLEU4/METEOR/ROUGE-L/BERTScore/MoverScore (see our paper for more in detail).
  
### Languages
Korean (ko)

## Dataset Structure
An example of 'train' looks as follows.
```
{
  "question": "함수해석학이 주목하는 탐구는?",
  "paragraph": "변화에 대한 이해와 묘사는 자연과학에 있어서 일반적인 주제이며, 미적분학은 변화를 탐구하는 강력한 도구로서 발전되었다. 함수는 변화하는 양을 묘사함에 있어서 중추적인 개념으로써 떠오르게 된다. 실수와 실변수로 구성된 함수의 엄밀한 탐구가 실해석학이라는 분야로 알려지게 되었고, 복소수에 대한 이와 같은 탐구분야는 복소해석학이라고 한다. 함수해석학은 함수의 공간(특히 무한차원)의 탐구에 주목한다. 함수해석학의 많은 응용분야 중 하나가 양자역학이다. 많은 문제들이 자연스럽게 양과 그 양의 변화율의 관계로 귀착되고, 이러한 문제들이 미분방정식으로 다루어진다. 자연의 많은 현상들이 동역학계로 기술될 수 있다. 혼돈 이론은 이러한 예측 불가능한 현상을 탐구하는 데 상당한 기여를 한다.",
  "answer": "함수의 공간(특히 무한차원)의 탐구",
  "sentence": "함수해석학은 함수의 공간(특히 무한차원)의 탐구 에 주목한다.",
  "paragraph_sentence": '변화에 대한 이해와 묘사는 자연과학에 있어서 일반적인 주제이며, 미적분학은 변화를 탐구하는 강력한 도구로서 발전되었다. 함수는 변화하는 양을 묘사함에 있어서 중추적인 개념으로써 떠오르게 된다. 실수와 실변수로 구성된 함수의 엄밀한 탐구가 실해석학이라는 분야로 알려지게 되었고, 복소수에 대한 이와 같은 탐구 분야는 복소해석학이라고 한다. <hl> 함수해석학은 함수의 공간(특히 무한차원)의 탐구 에 주목한다. <hl> 함수해석학의 많은 응용분야 중 하나가 양자역학이다. 많은 문제들이 자연스럽게 양과 그 양의 변화율의 관계로 귀착되고, 이러한 문제들이 미분방정식으로 다루어진다. 자연의 많은 현상들이 동역학계로 기술될 수 있다. 혼돈 이론은 이러한 예측 불가능한 현상을 탐구하는 데 상당한 기여를 한다.',
  "paragraph_answer": '변화에 대한 이해와 묘사는 자연과학에 있어서 일반적인 주제이며, 미적분학은 변화를 탐구하는 강력한 도구로서 발전되었다. 함수는 변화하는 양을 묘사함에 있어서 중추적인 개념으로써 떠오르게 된다. 실수와 실변수로 구성된 함수의 엄밀한 탐구가 실해석학이라는 분야로 알려지게 되었고, 복소수에 대한 이와 같은 탐구 분야는 복소해석학이라고 한다. 함수해석학은 <hl> 함수의 공간(특히 무한차원)의 탐구 <hl>에 주목한다. 함수해석학의 많은 응용분야 중 하나가 양자역학이다. 많은 문제들이 자연스럽게 양과 그 양의 변화율의 관계로 귀착되고, 이러한 문제들이 미분방정식으로 다루어진다. 자연의 많은 현상들이 동역학계로 기술될 수 있다. 혼돈 이론은 이러한 예측 불가능한 현상을 탐구하는 데 상당한 기여를 한다.',
  "sentence_answer": "함수해석학은 <hl> 함수의 공간(특히 무한차원)의 탐구 <hl> 에 주목한다."
}
```

The data fields are the same among all splits.
- `question`: a `string` feature. 
- `paragraph`: a `string` feature.
- `answer`: a `string` feature.
- `sentence`: a `string` feature.
- `paragraph_answer`: a `string` feature, which is same as the paragraph but the answer is highlighted by a special token `<hl>`.
- `paragraph_sentence`: a `string` feature, which is same as the paragraph but a sentence containing the answer is highlighted by a special token `<hl>`.
- `sentence_answer`: a `string` feature, which is same as the sentence but the answer is highlighted by a special token `<hl>`.

Each of `paragraph_answer`, `paragraph_sentence`, and `sentence_answer` feature is assumed to be used to train a question generation model,
but with different information. The `paragraph_answer` and `sentence_answer` features are for answer-aware question generation and 
`paragraph_sentence` feature is for sentence-aware question generation.

## Data Splits

|train|validation|test |
|----:|---------:|----:|
|54556|     5766 |5766 |


## Citation Information

```
@inproceedings{ushio-etal-2022-generative,
    title = "{G}enerative {L}anguage {M}odels for {P}aragraph-{L}evel {Q}uestion {G}eneration: {A} {U}nified {B}enchmark and {E}valuation",
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