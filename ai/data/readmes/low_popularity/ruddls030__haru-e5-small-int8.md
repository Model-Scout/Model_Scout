---
license: mit
language: [ko]
library_name: transformers.js
pipeline_tag: feature-extraction
base_model: intfloat/multilingual-e5-small
tags: [sentence-similarity, onnx, harupet]
---

# haru-e5-small-int8

[HaruPet](https://haru.sarl) 데스크톱 펫의 'CPU 전용 대화'(내장 대화 모델을 못 쓰는 사용자용 답 고르기)에 쓰는 문장 임베딩 모델이에요.
[intfloat/multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small)을 하루 대화 질문↔답 쌍으로 파인튜닝했어요(MultipleNegativesRanking, 8에폭).
학습 데이터는 공개하지 않아요.

- `onnx/model_quantized.onnx`: int8 동적 양자화(채널별 uint8), 118MB. 앱이 쓰는 파일이에요.
- `onnx/model.onnx`: fp32, 470MB
- 384차원, mean pooling 후 정규화. 입력 앞에 `query: `(질문), `passage: `(기억·문서)를 붙여요.

```js
import { pipeline } from "@huggingface/transformers";
const ext = await pipeline("feature-extraction", "ruddls030/haru-e5-small-int8", { dtype: "q8" });
const v = await ext(["query: 오늘 너무 피곤해"], { pooling: "mean", normalize: true });
```

## 평가
| 모델 | 하루 실제 질문 R@1 | 하루 합성 질문 R@1 | Ko-StrategyQA nDCG@10 |
|---|---|---|---|
| multilingual-e5-small | 0.413 | 0.657 | 0.752 |
| KoSimCSE-roberta-multitask | 0.440 | 0.514 | 0.639 |
| **이 모델 (fp32)** | **0.593** | **0.714** | 0.715 |
| 이 모델 int8 (onnxruntime-web WASM) | 0.587 | – | – |

## CPU 전용 대화 묶음 (`cpu-chat/`)
하루·루나·모리·미나코 네 캐릭터가 이 모델 하나와 공용 질문 목록을 같이 써요. 사용자 말과 가장 비슷한 공용 질문을 고르고, 지금 캐릭터의 답을 보여 줘요.

- `cpu-chat/questions.f16`: 공용 질문 3,575개의 벡터. 3,575×384 float16, little-endian, 행 순서 = 답 순서, 정규화됨. 2.7MB
- `cpu-chat/answers.json`: `answers.{haru,luna,mori,minako}[i]` = i번째 질문에 대한 답, `fallback.<캐릭터>` = 되묻는 말 3개, `threshold` 0.6. 1.6MB

```js
const v = await ext(["query: " + msg], { pooling: "mean", normalize: true });
// questions.f16 의 각 행과 내적 → 최고 점수 i
// 점수 >= threshold ? answers[char][i] : fallback[char] 중 하나
```

CPU(WASM, 1스레드)에서 답 하나 고르는 데 약 16ms, 효율 코어만 쓰면 약 106ms 걸려요.
