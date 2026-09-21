---
base_model: meta-llama/Llama-3.2-1B-Instruct
language:
  - ko
library_name: peft
pipeline_tag: text-generation
tags:
  - korean
  - dialogue
  - coreference
  - qlora
---

# recallResolver-1B

한국어 멀티턴 파이프라인의 **히스토리 값 추출기** — "그거 재고 얼마나 남았어?"처럼 과거 대화의 값을 가리키는 발화가 오면, 대화 기록에서 그 값을 찾아주는 1B 모델의 QLoRA 어댑터(~45MB)입니다.

[toolRouter-1B](https://huggingface.co/kimjg/toolRouter-1B)와 짝으로 설계됐습니다: 라우터가 과거 참조를 감지하면, recallResolver가 히스토리를 **교환 단위 하나씩** 받아 값을 추출하고, 서버가 그 값으로 발화를 보강해 라우터를 재호출합니다. 입력이 항상 "단위 1개 + 현재 발화 + needs"로 고정이라 **히스토리가 아무리 길어도 컨텍스트가 자라지 않습니다.**

## 입출력

```
system: (고정 지시 — 기록에서 needs에 해당하는 값을 그대로 추출, 없으면 false, 지어내기 금지)
user:
  [기록]
  user: SKU 44871 재고 몇 개 남았는지 봐줘
  call: {"name": "get_stock", "arguments": {"sku": "44871"}}
  result: {"ok": true, "sku": "44871", "qty": 120}
  [현재 요청] 그거 어느 구역에 보관돼 있는 거야?
  [needs] 상품 SKU 번호
assistant: {"found": true, "value": "44871"}
```

값이 기록에 없으면 `{"found": false}`. 출력은 xgrammar 등으로 JSON 형식을 강제하고, **value가 기록 텍스트에 글자 그대로 존재하는지 서버에서 검증**(verbatim 가드)하는 것을 권장합니다.

## 성능 (자체 평가셋 613건, 학습과 분리)

| 지표 | 수치 |
|---|---|
| found 판정 정확도 | 96.3% |
| value 정확일치 (found 중) | 94.2% |
| 오탐률 (없는데 찾았다고 함) | 2.5% |
| 형식(JSON 파싱) | 100% |

오탐은 4회의 hard-negative 채굴 반복으로 9.9% → 2.5%까지 압축했습니다. 남은 약점은 같은 계열 식별자의 하위 유형 혼동(주문 번호 ↔ 송장 번호)으로, 서버 측 되묻기 규칙으로 보완하는 것을 권장합니다.

## 사용법

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

base = "meta-llama/Llama-3.2-1B-Instruct"
model = AutoModelForCausalLM.from_pretrained(base, device_map="auto")
model = PeftModel.from_pretrained(model, "kimjg/recallResolver-1B")
tokenizer = AutoTokenizer.from_pretrained("kimjg/recallResolver-1B")
```

toolRouter-1B와 같은 베이스를 쓰므로, 베이스 한 벌에 어댑터 두 개를 얹고 `set_adapter`로 전환하면 두 모델이 **VRAM ~2.6GB(4bit)** 에서 함께 동작합니다.

## GGUF (llama.cpp)

머지·양자화한 단일 파일도 제공합니다: `recallResolver-1B-Q4_K_M.gguf` (0.8GB) / `recallResolver-1B-Q8_0.gguf` (1.3GB). 리졸버 기준 양자화 손실은 아직 실측 전입니다 — 같은 베이스·같은 방식의 toolRouter-1B 실측(Q8 ~-0.8%p, Q4 ~-1.6%p)이 참고치이며, 정밀도가 중요하면 Q8을 권합니다. 공유 베이스 구성(toolRouter-1B와 base GGUF 한 벌 + LoRA 2개)이 VRAM에 더 유리합니다(실측 1.5GB).

## 제한

- 추출 전용입니다 — 요약·계산·비교는 하지 않습니다 (그런 요청은 상위 모델로 escalate 권장).
- 결과(result)는 250자 내로 절단해 입력하세요. ID류 필드를 앞에 배치하면 잘림에 안전합니다.
- greedy 디코딩 권장. base 모델의 Llama 3.2 Community License를 따릅니다.
