---
language:
- en
- ko
license: other
pretty_name: Algocean FABLE5 Traces
task_categories:
- text-generation
tags:
- fable5
- traces
- sft
- tool-use
- agentic
- langgraph
size_categories:
- 10K<n<100K
---

# algocean-fable5-traces

FABLE5 계열 trace를 LangGraph/SFT 학습용 JSONL로 전처리한 데이터셋입니다.

## 파일

- `train.jsonl`: 30,265 rows
- `eval.jsonl`: 512 rows
- `manifest.json`: 전처리 설정, 소스별 카운트, 분할 정보

## 구성

이 데이터는 Crownelius 원본과 kelexine 원본을 합친 뒤, 중복 제거, 필터링, train/eval 분할을 거쳐 만들었습니다.

- Crownelius selected: 26,938
- kelexine selected: 3,839
- total selected: 30,777
- train/eval split: 30,265 / 512
- duplicate/seen skipped: 1,721

## 크기

원본 로컬 데이터 폴더는 약 360 MiB입니다.

- Crownelius 원본 Parquet: 307,137,038 bytes, 약 293 MiB
- kelexine 원본 JSONL: 69,836,598 bytes, 약 67 MiB

전처리 후 JSONL 학습 입력은 압축 Parquet가 prompt/completion 형태로 풀리면서 더 커졌습니다.

- `train.jsonl`: 772,240,628 bytes, 약 736 MiB
- `eval.jsonl`: 13,699,262 bytes, 약 13 MiB

## 왜 360 MiB에서 750 MiB로 커졌나

원본은 압축된 저장 포맷이고, 전처리본은 토크나이저가 바로 읽을 수 있게 풀어쓴 텍스트 JSONL입니다.

1. Crownelius 원본은 Parquet 압축본입니다. Parquet는 columnar + 압축 포맷이라 반복 문자열, 컬럼명, 구조가 작게 저장됩니다. JSONL로 풀면 이 압축 이점이 사라집니다.
2. 학습용 JSONL은 row마다 `prompt`, `completion`, `source`, `source_weight`, `kind` 같은 키를 반복해서 씁니다.
3. 원본 tool trace를 LangGraph 학습 포맷으로 펼쳤습니다. 예를 들어 `Bash`, `Read`, `Edit`, `WebSearch` 같은 tool call을 `<tool_call>`, `<function=run_shell>`, `<parameter=cmd>` 형태의 텍스트로 변환했습니다.
4. `messages`, `context`, `completion`도 `USER:`, `ASSISTANT:`, `<think>`, `<tool_call>` 형태의 SFT 텍스트로 풀었습니다.

정리하면, 데이터가 새로 늘어난 것이 아니라 압축된 원본을 비압축 JSONL + tool-call 학습 텍스트로 펼쳐서 약 2.1배 커진 것입니다.

복사 시점에 원본 `data/fable_mix_langgraph`와 이 폴더의 3개 파일 SHA-256이 모두 일치했습니다.
