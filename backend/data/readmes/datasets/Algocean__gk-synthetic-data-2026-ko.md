---
license: other
language:
- ko
task_categories:
- text-generation
pretty_name: GK Synthetic Data 2026 KO
size_categories:
- 10K<n<100K
tags:
- sft
- korean
- synthetic
- distillation
- long-form
- year-2026
---

# gk-synthetic-data-2026-ko.jsonl

`gk-synthetic-data-2026-ko.jsonl`은 외부 teacher 모델의 고급 지식과 장문 설명 능력을 한국어 SFT용으로 증류한 데이터셋이다.

- 현재 행 수: 77,408
- 한 줄 용도: 2026년 기준 고급 지식과 장문 설명 능력을 보강하기 위한 한국어 합성 SFT 데이터셋
- 주 용도: kanana 기반 지식/추론/장문 응답 모델 SFT
- 형식: JSONL, 한 줄에 하나의 학습 예시
- 스키마: `{"messages":[{"role":"user","content":"..."},{"role":"assistant","content":"..."}]}`
- 일부 행은 assistant 답변의 첫 부분에 공개 판단 근거 형식의 `<think>...</think>` 블록을 포함한다. 현재 포함 행 수는 111개이며, 닫는 태그 뒤에는 장문 최종 답변이 이어진다.

## 데이터 의미

`user` 메시지는 정책, 기술, 보안, 거시경제, 기후, 우주개발 같은 2026년 기준 고급 주제에 대한 질문이다. `assistant` 메시지는 한국어 장문 답변이며, 최신 사실과 일반 원리를 구분하고 실무적 함의와 한계를 함께 설명한다.

## 주요 주제

- 2026 AI Index와 기업 AI 도입
- EU AI Act와 GPAI 의무
- NIST post-quantum cryptography migration
- OWASP GenAI/LLM 보안 리스크
- AI 데이터센터와 전력망 이슈
- WMO 기후 지표
- IMF 2026 거시경제 전망
- NASA Artemis II와 달 탐사 프로그램

## 품질 기준

- 메타데이터, id, source, category 같은 보조 컬럼 없음
- 역할 순서 고정: `user` 다음 `assistant`
- raw URL, 생성 과정 설명, 자동화 흔적 제거
- 짧은 답변, 과장된 단정, 가짜 수치, 출처 없는 고유 사실 제거
- 완전 중복과 assistant 중복 제거
- `<think>` 블록은 한 행에 최대 1개만 허용하며, assistant content의 시작 위치에만 둔다
