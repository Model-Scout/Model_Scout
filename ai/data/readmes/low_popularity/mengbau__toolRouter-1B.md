---
base_model: meta-llama/Llama-3.2-1B-Instruct
language:
  - ko
  - en
library_name: peft
pipeline_tag: text-generation
tags:
  - function-calling
  - tool-use
  - korean
  - qlora
---

# toolRouter-1B

한국어 우선 **툴콜 라우터** — 사용자 발화를 받아 항상 툴콜 하나로 응답하는 라우팅 모델입니다. **Llama-3.2-1B-Instruct** 위에 얹는 QLoRA 어댑터(~45MB)로, 4bit 로드 시 VRAM 약 2.5GB, GGUF Q4 변환 시 약 1GB로 구동됩니다.

- 자유 텍스트를 생성하지 않습니다. 모든 출력은 `<tool_call>{"name": ..., "arguments": {...}}</tool_call>` 형식입니다.
- 일반 대화·상식 응답은 `reply(text=...)`, 처리 불가 요청은 `escalate(query=원문)` 툴로 표현합니다.
- 인자는 사용자 문장의 표현을 원문 그대로 추출하도록 학습됐습니다 (한국어 인자의 영어 번역·요약·지어냄 억제).
- 처음 보는 툴 스키마(zero-shot toolset)에서도 동작하도록 학습됐습니다.
- 멀티턴이 필요하면 [recallResolver-1B](https://huggingface.co/kimjg/recallResolver-1B)와 짝으로 쓰세요 — 같은 베이스를 공유해 어댑터 전환만으로 함께 동작하며, 모델을 따로 띄우는 것 대비 VRAM이 절반입니다 — 실측: llama.cpp 베이스 Q4 + LoRA 2개 한 서버 = **1.5GB**, 머지 Q4 서버 2개 = 2.8GB (각 2048 ctx, 추론 버퍼 포함).

## 최신 버전 — 2026-09.2 (recall 지원)

한국어 실사용 문체 6,000문장 직접 작성 데이터로 강화하고, **과거 대화 참조 감지(`recall`)**를 추가한 버전입니다.

| 평가 | 수치 |
|---|---|
| 한국어 평가셋 396 (decision / tool / args) | 97.2 / 95.7 / 83.8 |
| held-out 1,100 (decision / tool / args) | 99.5 / 99.2 / 97.0 |
| BFCL v3 single-turn (simple / multiple / irrelevance / overall) | 86.0 / 85.5 / 80.0 / **84.2** |
| recall 판정 (경계 케이스 포함 120) | 재현 86.7% / 정밀 91.2% / 함정 방어 52/55 |

## 사용법

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

base = "meta-llama/Llama-3.2-1B-Instruct"
model = AutoModelForCausalLM.from_pretrained(base, device_map="auto")
model = PeftModel.from_pretrained(model, "kimjg/toolRouter-1B")
tokenizer = AutoTokenizer.from_pretrained("kimjg/toolRouter-1B")
```

채팅 템플릿은 저장소의 `chat_template.jinja`에 포함돼 있습니다. greedy 디코딩을 권장하며, 프로덕션에서는 xgrammar 등 JSON 스키마 문법 강제(constrained decoding)를 함께 쓰면 파싱·스키마 통과율 100%를 보장할 수 있습니다.

## 툴 지정 방법

시스템 프롬프트에 툴 스키마를 **한 줄에 하나씩 compact JSON**으로 나열합니다. 학습 때 사용한 템플릿 그대로 쓰는 것을 권장합니다:

```text
너는 게임 공략 도우미의 툴콜 라우터다. 사용자의 요청을 읽고 아래 툴 중 정확히 하나를 호출하는 것으로만 응답한다. 자유 텍스트를 출력하지 않는다.
- 일반 대화나 직접 답할 수 있는 질문은 reply 툴을 호출한다.
- 목록에 있는 툴로 처리할 수 없거나 범위를 벗어난 요청은 escalate 툴을 호출한다.
- 툴 인자는 사용자의 요청에서 추출한다. 요청에 없는 값을 지어내지 않는다.
응답 형식은 반드시 다음과 같다:
<tool_call>{"name": "<툴 이름>", "arguments": {<인자>}}</tool_call>
사용 가능한 툴 목록:
<tools>
{tools_json}
</tools>
```

`{tools_json}` 자리에 들어가는 툴 스키마 형식 (OpenAI function 스키마와 동일한 `parameters` 구조):

```json
{"name": "get_weather", "description": "지역의 현재 날씨를 조회한다", "parameters": {"type": "object", "properties": {"location": {"type": "string", "description": "도시 이름"}, "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}}, "required": ["location"]}}
{"name": "reply", "description": "툴이 필요 없는 질문에 직접 답한다", "parameters": {"type": "object", "properties": {"text": {"type": "string"}}, "required": ["text"]}}
{"name": "escalate", "description": "처리할 수 없는 요청을 상위로 넘긴다", "parameters": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}}
```

`reply`와 `escalate`는 항상 목록에 포함해야 합니다. 나머지 툴은 자유롭게 교체할 수 있고, 학습 때 본 적 없는 툴셋도 동작합니다(zero-shot). 툴 설명은 영어·한국어 모두 지원합니다.

## 기본 툴 3종 (라우터의 프로토콜)

이 라우터는 "모든 응답이 툴콜"이라는 규약 위에서 동작하며, 도메인 툴 외에 다음 기본 툴로 모든 발화를 커버합니다:

| 기본 툴 | 언제 나오나 | 인자 | 서버가 할 일 |
|---|---|---|---|
| `reply` | 툴이 필요 없는 인사·잡담·상식 질문 ("고마워!", "안녕") | `text`: 짧은 한국어 답변 | text를 그대로 사용자에게 |
| `escalate` | 목록의 툴로 처리 불가한 요청 — 다른 도메인, 복합 작업, 필수 인자를 알 수 없음, 긴 글쓰기 등 | `query`: **사용자 요청 원문 그대로** | 상위 모델·담당자에게 전달 |
| `recall` | 발화가 과거 대화의 값을 가리킬 때 ("그거 재고 얼마 남았어?", "아까 그 도시 내일 날씨는?") | `needs`: 찾아야 할 값의 한국어 설명 | [recallResolver-1B](https://huggingface.co/kimjg/recallResolver-1B)로 히스토리에서 값을 찾아 발화를 보강 후 라우터 재호출 |

설계 의도: 라우터는 자유 텍스트를 생성하지 않으므로 "대답한다/넘긴다/과거를 찾는다"까지 전부 툴콜로 표현됩니다. 덕분에 다운스트림은 분기 처리만 하면 되고, 출력 문법 강제(constrained decoding)를 전체 응답에 적용할 수 있습니다.

**reply 운용 팁**: `reply.text`를 그대로 쓸 수도 있지만(지연 최소), reply를 **"대화 트랙" 신호로만 쓰고 발화를 별도 챗 모델로 넘기는** 구성도 분기 한 줄이면 됩니다. 페르소나 있는 본격 챗봇과 붙일 때 유용합니다:

```python
call = route(utterance)
if call["name"] == "reply":
    return chat_model(persona, utterance)  # text는 버리고 큰 모델이 대화
```

> **recall 연동 팁** (recallResolver-1B와의 end-to-end 검증에서 확정한 서버 규칙): ①리졸버가 값을 찾으면 그 값의 출처 인자 스키마 설명을 라벨로 발화를 보강해 재라우팅 — `"{발화} ({라벨}: {값})"` ②라우터의 needs로 리졸버가 못 찾으면 해당 기록의 인자 설명들로 재질의 ③needs와 값 라벨의 유형이 안 맞으면 자동 주입 대신 사용자에게 확인. 재호출이 또 recall이면 escalate(루프 가드). recall을 쓰지 않으려면 툴 목록에서 빼면 됩니다 — 그러면 과거 참조 발화는 escalate로 나옵니다.

동작 예:

```text
user: 우산 챙겨야 하나, 대전인데
assistant: <tool_call>{"name": "get_weather", "arguments": {"location": "대전"}}</tool_call>

user: 고마워!
assistant: <tool_call>{"name": "reply", "arguments": {"text": "별말씀을요, 또 필요하면 불러 주세요!"}}</tool_call>

user: 이 사진에서 글자 좀 읽어줘
assistant: <tool_call>{"name": "escalate", "arguments": {"query": "이 사진에서 글자 좀 읽어줘"}}</tool_call>
```

## GGUF (llama.cpp)

어댑터를 머지해 양자화한 단일 파일도 제공합니다. 손실은 자체 평가셋 실측치입니다:

| 파일 | 크기 | 한국어 평가셋 (decision/tool/args) | 권장 용도 |
|---|---|---|---|
| `toolRouter-1B-Q8_0.gguf` | 1.3GB | 96.5 / 95.0 / 83.4 (원본 대비 ~-0.8%p) | 품질 우선 |
| `toolRouter-1B-Q4_K_M.gguf` | 0.8GB | 95.5 / 94.2 / 83.4 (~-1.6%p) | 최소 VRAM |

```bash
llama-server -m toolRouter-1B-Q8_0.gguf -ngl 99 -c 2048
```

채팅 템플릿이 GGUF에 포함돼 있습니다. greedy(temperature 0) 권장, 출력은 `<tool_call>...</tool_call>` 형식 그대로입니다. recall 판정은 양자화에 다소 민감하니(경계 케이스 -4~5%p) recall을 쓰는 파이프라인이면 Q8을 권합니다.

## 제한

- 단일 턴 라우팅 전용입니다 (멀티턴 문맥 참조는 미지원).
- 세계지식 추론이 필요한 인자 보정(예: 도시명→통화코드), 상대 날짜 해석은 다운스트림에서 처리하세요. 상대 날짜는 시스템 프롬프트에 현재 날짜를 제공하면 개선됩니다.
- base 모델의 Llama 3.2 Community License를 따릅니다.
