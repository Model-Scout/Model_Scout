# 119 Call Transcript Synthetic Labels

Synthetic Korean 119 emergency call transcripts labeled by Claude Sonnet 5

# 119 Call Transcript Synthetic Labels

한국 119 응급 신고 통화를 바탕으로 만든 합성(synthetic) 텍스트에, Claude Sonnet 5로 구조화 라벨링(연령/성별/의식/활력징후/증상/KTAS 등급 등)을 붙인 데이터셋입니다.

This dataset contains synthetic Korean 119 (emergency call) transcripts, labeled with structured fields (age, sex, consciousness, vital signs, symptoms, KTAS triage level, etc.) using **Claude Sonnet 5**.

## 데이터 구성 / Structure

- `train.jsonl`: 1,438 rows
- `val.jsonl`: 360 rows

각 라인은 하나의 JSON 레코드이며 다음 필드를 포함합니다:

- `id`: 레코드 고유 ID
- `split`: `train` 또는 `val`
- `text`: 합성된 119 통화 텍스트
- `meta`: 시나리오 메타데이터(원본 소스 ID, 검증 이슈 등)
- `v2`: Claude Sonnet 5로 라벨링한 구조화 필드 (call_type, ktas_level, ktas_evidence, chief_complaint, suspected_diagnosis, vitals, consciousness, symptoms, onset, incidents, disease_category, injuries, treatments, age, sex, medications, notes)

Each line is a single JSON record with the following fields:

- `id`: unique record identifier
- `split`: `train` or `val`
- `text`: the synthetic 119 call transcript
- `meta`: scenario metadata (original source id, verifier notes, etc.)
- `v2`: structured fields labeled by Claude Sonnet 5 (`call_type`, `ktas_level`, `ktas_evidence`, `chief_complaint`, `suspected_diagnosis`, `vitals`, `consciousness`, `symptoms`, `onset`, `incidents`, `disease_category`, `injuries`, `treatments`, `age`, `sex`, `medications`, `notes`)

## 라벨링 방법 / Labeling

- 라벨은 전부 **Claude Sonnet 5**를 사용해 생성했습니다.
- 텍스트 자체도 합성 데이터(synthetic)이며, 실제 개인의 신고 내용이 아닙니다.

- All labels were generated using **Claude Sonnet 5**.
- The call transcripts themselves are synthetic — they are not real emergency call recordings or transcriptions, and do not correspond to any real individual's report.
- Each record covers a single simulated 119 emergency call scenario, labeled for downstream tasks such as KTAS (Korean Triage and Acuity Scale) level prediction, chief-complaint extraction, and vital-sign / symptom structuring.

## 라이선스 / License

MIT

출처: Kaggle (podongchip/119-call-transcript-synthetic-labels)
태그: 
라이선스: MIT
수정일: 2026-09-29T07:46:54.040Z
