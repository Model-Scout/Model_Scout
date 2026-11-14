---
library_name: transformers
pipeline_tag: text-generation
language: ko
license: mit
tags:
- haru
- cfrd
- custom-code
---

<img src="assets/haru.png" alt="Haru character" width="420" />


# Haru v2.0 (legacy)

> **Legacy release / 레거시 모델:** Haru v2 is preserved for research and reproducibility.
> **Haru v3 is the latest release. / 최신 버전은 Haru v3입니다.**

| Latest Haru v3 model | Parameters | Repository |
|---|---:|---|
| Student non-IT — plain story continuation | 13,688,705 | [haru_3-student-base](https://huggingface.co/alice-noa-chan/haru_3-student-base) |
| Student IT — experimental chat-formatted story instructions | 13,688,705 | [haru_3-student-chat](https://huggingface.co/alice-noa-chan/haru_3-student-chat) |
| Teacher non-IT | 30,997,377 | [haru_3-teacher-base](https://huggingface.co/alice-noa-chan/haru_3-teacher-base) |
| Teacher IT | 30,997,377 | [haru_3-teacher-chat](https://huggingface.co/alice-noa-chan/haru_3-teacher-chat) |

새로 사용할 때는 학생 non-IT 모델로 동화를 이어 쓰거나, 학생 IT 모델의
`apply_chat_template` 사용 예제를 참고하세요. 최신 저장소에는 FP32 가중치,
MIT 라이선스와 실행 예제가 포함되어 있습니다. IT는 실험 모델이며 이야기의
사실 유지와 새로운 지시 형식에 대한 일반화에는 한계가 있습니다.

See the [Haru collection](https://huggingface.co/collections/alice-noa-chan/haru-6abb683d0a8b9677162d7704)
and [current GitHub release](https://github.com/alice-noa-chan/haru/releases/tag/v3.0.2-students).

The original v2 architecture, weights and usage are documented below.

Haru is a compact Korean story continuation model built with the custom CFRD
causal architecture. It has 16,983,213 parameters and runs at
recurrent depth 6 only.

- [Source code](https://github.com/alice-noa-chan/haru)
- [Previous Haru release](https://huggingface.co/alice-noa-chan/haru_1.1)

## Usage

Review the included Python files before enabling remote custom code.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "alice-noa-chan/haru_2"
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(MODEL_ID, trust_remote_code=True)

inputs = tokenizer("작은 마을에 아침이 찾아왔어요.", return_tensors="pt")
output = model.generate(
    **inputs,
    max_new_tokens=120,
    do_sample=True,
    temperature=0.7,
    top_p=0.9,
    top_k=40,
    repetition_penalty=1.08,
    use_cache=False,
)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

## Model details

- Parameters: 16,983,213
- Context length: 512
- Recurrent depths supervised during training: none; AUX_EXIT_LOSS_WEIGHT is 0.0, so the depth 2 and 4 exits are untrained
- Exported checkpoint step: 32500
- Training tokens seen: 4,259,840,000

## Evaluation

| Recurrent depth | Validation loss | Perplexity |
|---:|---:|---:|
| 2 | 8.79562 | 6605.228 |
| 4 | 5.56061 | 259.982 |
| 6 | 3.38503 | 29.519 |

## Training data attribution

[Tiny-Ko-Stories](https://huggingface.co/datasets/psymon/Tiny-Ko-Stories)
by psymon, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
The dataset is not redistributed with this model.

## Limitations

- Haru is a continuation model, not an instruction-following assistant.
- Longer generations can repeat ideas or drift between entities.
- The model is not suitable for factual or safety-critical use.
- There is no inference cache yet, so generation recomputes the active context.

## License

Haru model weights and included code are released under the MIT License. The
training dataset remains under its separate CC BY 4.0 license.

## KoBEST

Scored with lm-eval on the five KoBEST tasks. The tasks mix two-way and
four-way formats, so the mean has no fixed floor: 0.450 is what a coin flip
scores. Read the "vs chance" column.

| Task | Haru v2.0 | Haru v1.1 | Chance | vs chance |
|---|---:|---:|---:|---:|
| kobest_boolq | 0.507 | 0.502 | 0.50 | +0.007 |
| kobest_copa | 0.529 | 0.500 | 0.50 | +0.029 |
| kobest_hellaswag | 0.314 | 0.224 | 0.25 | +0.064 |
| kobest_sentineg | 0.509 | 0.496 | 0.50 | +0.009 |
| kobest_wic | 0.488 | 0.488 | 0.50 | -0.012 |
| **mean** | **0.469** | 0.442 | 0.450 | **+0.019** |

v1.1 was at or below chance on every task. v2.0 is above chance on four of
five, and hellaswag at 0.314 against a 0.25 chance level is the first evidence
in this project of a task being learned rather than guessed.

### Against other sub-20M Korean models

Every row was scored locally through the same harness and task list rather
than quoted from a model card.

| Model | Parameters | Mean | vs chance |
|---|---:|---:|---:|
| **Haru v2.0** | **17.0M** | **0.469** | **+0.019** |
| minpeter/tiny-ko-20m-sft | 20.0M | 0.463 | +0.013 |
| minpeter/tiny-ko-20m-base | 20.0M | 0.457 | +0.007 |
| Haru v1.1 | 11.6M | 0.442 | -0.008 |

These are small margins on a benchmark whose chance mean is 0.450, and all four
models score below chance on wic. Sub-20M Korean models are all near the floor;
Haru v2.0 is a little further from it than the others tested.

## Recurrent depth

**v2.0 runs at depth 6 only.**

| Depth | v2.0 loss | v2.0 PPL |
|---:|---:|---:|
| 2 | 8.79562 | 6605.2 |
| 4 | 5.56061 | 260.0 |
| 6 | **3.38503** | **29.5** |

v1.1 degraded gracefully across depths 2, 4 and 6 because it reused three
physical cells and trained the intermediate exits with deep supervision. v2.0
unfolds the stack into six independent cells and sets the deep-supervision
weight to zero, so the shallow exits receive no training signal. Early exit was
a property of cell reuse plus deep supervision, and v2.0 dropped both.

## Training

17.0M parameters, 12,000-token BPE tokenizer, 512-token context. Trained on
4.26B tokens drawn from a 2.6B-token Korean corpus that was n-gram
decontaminated against all five KoBEST evaluation sets.

Training stopped at 4.26B of a planned 10.4B tokens: two KoBEST measurements
1.5B tokens apart moved the mean by +0.003, inside the harness's own noise, so
the remaining budget was not buying measurable accuracy.

## Limitations

- Repetition collapse is common after the first sentence or two.
- Entity tracking is unreliable; the model confuses referents in longer spans.
- It reproduces encyclopaedic surface form without the underlying facts.
- Not an instruction model, a factual assistant, or a safety-reviewed product.



Demo Spaces were retired at the owner's request. All model weights and revision history are preserved.

[Haru model collection](https://huggingface.co/collections/alice-noa-chan/haru-6abb683d0a8b9677162d7704)
