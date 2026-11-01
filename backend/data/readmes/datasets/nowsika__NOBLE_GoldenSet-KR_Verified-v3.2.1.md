---
language:
- ko
pretty_name: NOBLE v3.2.1 GoldenSet (KR, Verified)
license: cc-by-nc-4.0
task_categories:
- text-generation
- text-classification
tags:
- korean
- dialogue
- safety
- evaluation
size_categories:
- n<1K
---

# NOBLE v3.2.1 GoldenSet (KR, Verified)

한국어 대화 샘플 63개(JSONL)로 구성된 골든셋(검수 통과)입니다.  
목표는 **짧고 읽히는 톤**, **맥락 고정**, **안전한 방향 제시**, **과부하 줄이기**입니다.

## Files
- `data/NOBLE_v3.2.1_GoldenSet_KR_Verified.jsonl` — 검수 통과(qa_ok=YES)만 모은 샘플
- [`SCENARIO_INDEX.md`](./SCENARIO_INDEX.md) — 질문(상황) 목록 + 태그

## Record format (one line = one JSON)
각 줄은 1개의 레코드이며, 주요 필드는 아래와 같습니다.

- `scenario` : 질문/상황(한 문장 요약)
- `tags` : 분류 태그(복수)
- `signals` : (선택) 위험/왜곡 신호 요약
- `model_response` : 응답 구성 요소
  - `reflection` : 상황 요약/감정 반사
  - `anchor` : 오늘 붙잡을 핵심 한 줄
  - `route_steps` : 지금 할 일(최대 3개)
  - `one_question` : 마지막 질문 1개
  - `closing` : 마무리 문장
- `qa` : 형식 점검 정보(메타포 도메인, 질문 수 등)
- `qa_ok` : `YES` / `NO` (이 파일은 `YES`만 포함)

## Verification (auto QC)
이 샘플은 자동 점검을 통과한 레코드만 포함합니다.
- 금지 표현(내부 용어/호칭 등) 탐지
- 과부하 방지(행동 제안 상한)
- 질문 수 제한: **마지막 질문 1개 기준**

## Generation note
All samples in this dataset were authored with **ChatGPT (model: GPT-5.2 Thinking)** and then verified via auto QC.

## Intended use
- 프롬프트/평가 입력으로 활용(한국어 응답 톤·구조 참고용)
- 고정 프롬프트 템플릿은 별도로 제공하지 않습니다. scenario를 입력으로 쓰고 출력 비교를 하면 됩니다.
- 모델 비교 평가(같은 입력에서 구조/안전성/일관성 비교)
- 데모/샘플용

## Roadmap
An English sample set will be released soon. 

## Notes / limitations
- 본 샘플은 “도움이 되는 말의 구조”를 보여주기 위한 예시입니다.
- 실제 서비스 적용 시에는 운영 정책, 지역별 긴급 도움 안내, 민감 주제 처리 기준을 별도로 준비하는 것을 권장합니다.

## How to Use (Usage)

from datasets import load_dataset
ds = load_dataset("nowsika/NOBLE_GoldenSet-KR_Verified-v3.2.1")
ds["train"][0]

## Citation
If you use this dataset, please cite:
- NOBLE v3.2.1 GoldenSet (KR, Verified), Young-hun Choe, 2025.

## License
This dataset is released under **CC BY-NC 4.0** (non-commercial).  
For commercial use or custom datasets, contact: **nowsika@gmail.com**

## Contact
- **nowsika@gmail.com**