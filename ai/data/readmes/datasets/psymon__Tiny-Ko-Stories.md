---
license: cc-by-4.0
language:
  - ko
task_categories:
  - text-generation
pretty_name: Tiny-Ko-Stories
size_categories:
  - 1M<n<10M
tags:
  - korean
  - stories
  - language-modeling
  - children-stories
  - tinystories-inspired
  - synthetic-data
---

# Tiny-Ko-Stories

English version is available below.

Tiny-Ko-Stories는 TinyStories에서 영감을 받은 한국어 이야기 데이터셋입니다.

TinyStories는 제한된 고품질 데이터셋을 사용하면, 소형 모델이라도 추론 능력과 창의력을 발휘할 수 있음을 보였습니다.

우리가 확인하려는 것은 단순합니다.

> 이 현상이 한국어에서도 재현될까?

이를 확인하려면 번역 데이터셋만으로는 부족했습니다. 한국어다운 이름, 문장 리듬, 의성어와 의태어, 색채어, 작은 사건 구조를 포함하려면 처음부터 한국어로 만든 이야기가 필요했습니다. 그래서 Tiny-Ko-Stories는 영어 TinyStories를 번역하는 대신, 한국어로 짧은 이야기를 새로 생성하고 여러 단계의 검수를 거쳐 구성했습니다.

## 데이터셋 요약

| 항목 | 값 |
|---|---:|
| 레코드 수 | 2,003,542 |
| 형식 | JSONL |
| 공개 필드 | `text` |
| 평균 길이 | 346.41자 |
| 파일 크기 | 1,730,703,825 bytes |
| 언어 | 한국어 |
| 라이선스 | CC BY 4.0 |

각 줄에는 `text` 필드 하나만 들어 있습니다. 일부 이야기는 `text` 값 안에 단락 구분용 줄바꿈을 포함합니다.

```json
{"text": "하늘이는 비 오는 아침에 작은 우산을 들고 마당으로 나갔어요. ..."}
```

## 생성 방향

Tiny-Ko-Stories는 짧고 단순한 어린이 이야기 도메인에 맞춰 만들었습니다. 목표는 거창한 지식 모델이 아니라, 작은 모델이 배울 수 있는 또렷한 이야기 세계를 만드는 것이었습니다.

- 자연스러운 한국어 이름과 호칭
- 해요체 중심 문장
- 작은 문제와 해결
- 감정 변화
- 색채어와 의성어, 의태어
- 어린이에게 맞는 안전한 사건과 결말

## 생성 모델

최종 공개본은 여러 모델과 여러 단계의 품질 점검을 거쳐 만들었습니다. 주요 생성 모델은 Gemma 4 31B, GPT-5.5, Claude Opus 4.7/4.8입니다.

공개 파일에는 이야기 본문인 `text`만 남겼습니다. 생성에 사용한 내부 메타데이터는 포함하지 않습니다.

## 품질 관리

공개본은 다음 기준으로 정리했습니다.

- 빈 텍스트 제거
- 중복 텍스트 제거
- 지나치게 짧거나 긴 이야기 제거
- 부자연스러운 수식어, 어색한 이름 패턴 점검
- 어린이 이야기에 맞지 않는 주제, 표현 제거
- 최종 공개본은 생성용 메타데이터 없이 `text`만 유지

이 과정이 완벽한 품질을 보장하지는 않습니다. 합성 데이터셋인 만큼, 실제 사용 목적에 따라 추가 검토가 필요합니다.

## Split

공식 train/validation/test split은 포함하지 않았습니다. 사용 목적에 맞게 직접 나누는 것을 권장합니다.

## 권장 용도

- 소형 한국어 causal language model 학습
- 한국어 이야기 생성 연구
- 교육용 NLP 실험
- continuation LM 실험

## 권장하지 않는 용도

- 사실 질의응답 학습
- 안전성이 중요한 서비스에 바로 사용
- 사람 검수 없이 어린이에게 직접 제공

## 알려진 한계

- 합성 데이터셋입니다.
- 일부 이야기는 구조가 단순하거나 비슷한 교훈으로 끝날 수 있습니다.
- 드물게 어색한 이름, 대화, 인과관계가 남아 있을 수 있습니다.
- 어린이 이야기라는 좁은 도메인에 맞춘 코퍼스입니다.
- 범용 한국어 코퍼스로 사용하기에는 적합하지 않습니다.

## 라이선스

데이터셋은 **Creative Commons Attribution 4.0 International (CC BY 4.0)** 라이선스로 공개합니다. 자유롭게 사용하시되, 사용 시 알아볼 수 있는 형태로 **Tiny-Ko-Stories** 출처를 표기해 주세요.

더 자세한 개발 과정은 [여기](https://psymon-ai.github.io/posts/tiny-ko-stories-korean-native-story-dataset/)를 참고해주세요.

---

# Tiny-Ko-Stories

Tiny-Ko-Stories is a Korean story dataset inspired by TinyStories.

TinyStories showed that with a limited high-quality dataset, even small models can show reasoning ability and creativity.

The question behind this project is simple:

> Can the same phenomenon be reproduced in Korean?

A translated dataset was not enough for that question. To study Korean names, sentence rhythm, mimetic and ideophonic words, color expressions, and small story structures, we needed stories written in Korean from the start. Tiny-Ko-Stories was therefore built by generating short Korean stories directly and filtering them through multiple review stages, instead of translating the English TinyStories dataset.

## Dataset Summary

| Field | Value |
|---|---:|
| Records | 2,003,542 |
| Format | JSONL |
| Public field | `text` |
| Average length | 346.41 Korean characters |
| File size | 1,730,703,825 bytes |
| Language | Korean |
| License | CC BY 4.0 |

Each row contains only one `text` field. Some stories contain paragraph breaks inside the `text` value.

```json
{"text": "하늘이는 비 오는 아침에 작은 우산을 들고 마당으로 나갔어요. ..."}
```

## Generation Direction

Tiny-Ko-Stories focuses on short, simple child-friendly stories. The goal was not to build a general knowledge corpus, but to build a clear story world that small models can learn from.

- Natural Korean names and forms of address
- Polite Korean narration
- Small problem and resolution
- Emotional movement
- Korean color words, ideophones, and mimetic expressions
- Safe events and endings for a child-story corpus

## Generation Models

The final release was produced through multiple models and quality review passes. The main generation models were Gemma 4 31B, GPT-5.5, and Claude Opus 4.7/4.8.

The public file contains only the story `text`. It does not include internal generation metadata.

## Quality Control

The public release was checked for:

- empty text removal
- duplicate text removal
- length outliers
- awkward modifiers and awkward name patterns
- topics and expressions unsuitable for children's stories
- text-only export without generation metadata

This process does not guarantee perfect quality. As with any synthetic dataset, additional review may be needed depending on the use case.

## Split

The dataset does not include an official train/validation/test split. Users are encouraged to create their own splits.

## Intended Uses

- Training small Korean causal language models
- Research on Korean story generation
- Educational NLP experiments
- Continuation LM experiments

## Out-of-Scope Uses

- Factual question-answering training
- Direct use in safety-critical services
- Direct use as children's reading material without human review

## Known Limitations

- This is a synthetic dataset.
- Some stories may have simple structures or similar moral endings.
- Awkward names, dialogue, or causal links may remain in some samples.
- The corpus is focused on the narrow domain of child-friendly stories.
- It is not suitable as a general Korean corpus.

## License

The dataset is released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license. You may freely use it in any form, but please provide visible attribution to **Tiny-Ko-Stories**.
