---
license: other
language:
- ko
task_categories:
- text-generation
tags:
- korean
- cultural-heritage
- museum
- sft
- persona
pretty_name: heri Korean Cultural Heritage SFT Datasets
---

# heri — 한국 문화유산 스토리텔링 SFT 데이터셋

문화유산 해설 AI(고려대, RS-2023-00220195) 파이프라인에서 **코드로 생성한 학습용 중간 산출물**을 모은 데이터셋입니다.
GPT-4o / GPT-4.1 / Claude로 생성했으며, 근거는 한국민족문화대백과(EncyKorea)·국립중앙박물관·aimuse 자료입니다.

## 구성

| 폴더 | 설명 | 생성 방법 |
|------|------|-----------|
| `2024_sft/` | 2024 큐레이터 QA·해설 대화 SFT 데이터(`merged_file`, train/dev) | GPT-4o |
| `2025_gen_persona_qa/` | 관람객 5유형 페르소나 QA·해설 생성 결과(gen_inst) | GPT-4.1 / Claude 배치 |
| `2025_visitor_datasets/` | Gemma-3-27B SFT 학습셋(유형별 train/dev/test) | 위 생성물 가공 |
| `2026_visitor_datasets/` | Gemma-4-12B SFT 학습셋(통합 `all` + 유형별) | 위 생성물 가공 |
| `2026_visitor_datasets_neg/` | 위와 동일 구성 + 거절(negative) 학습 데이터 포함 — 운영 모델 학습셋 | 위 생성물 + 거절 데이터 |
| `2026_gen_qa/` | 2026 GPT 배치 생성 원본(QA/재작성) — 학습셋 조립(`make_train_data`) 입력 | GPT-5.4 배치 |
| `evidence/` | 근거문서(`aimuse_items_enriched_final_v5.json`) | aimuse + Solr 병합 |

## 용도

`google/gemma-*` 계열을 관람객 유형별 문화유산 해설 생성으로 SFT하는 학습 데이터입니다.
운영 모델(gemma-4-12B)은 `2026_visitor_datasets/all`(1차) 및 거절 강화판은 `2026_visitor_datasets_neg/all`로 학습되었습니다.

## 라이선스 / 이용 주의

- 원 근거 콘텐츠는 한국민족문화대백과(한국학중앙연구원)·국립중앙박물관(공공누리)·aimuse의 자료이며, 각 출처의 이용 조건을 따릅니다.
- 합성 데이터는 OpenAI/Anthropic API로 생성되어 해당 공급자 약관의 영향을 받습니다(경쟁 모델 학습 제한 등).
- 상업적 재배포 전 위 출처·약관을 반드시 확인하세요. 연구·과제 목적 사용 기준으로 정리되었습니다.

## 재현

이 데이터셋은 코드로 재생성할 수 있습니다(크롤 → GPT/Claude 배치 생성 → 정제/분할). 파이프라인 코드는 heri 코드 저장소를 참고하세요.
