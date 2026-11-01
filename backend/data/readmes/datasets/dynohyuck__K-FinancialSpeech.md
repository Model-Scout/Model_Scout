---
language:
- ko
license: cc-by-nc-4.0
task_categories:
- audio-classification
task_ids:
- audio-emotion-recognition
tags:
- speech-emotion-recognition
- korean
- financial
- multimodal
pretty_name: K-FinancialSpeech
size_categories:
- 1K<n<10K
dataset_info:
  features:
  - name: audio
    dtype: audio
  - name: file_name
    dtype: string
  - name: label
    dtype:
      class_label:
        names:
          '0': anger
          '1': anxiety
          '2': happiness
          '3': neutral
          '4': sadness
  - name: speaker_id
    dtype: string
  - name: gender
    dtype: string
  - name: scenario
    dtype: string
  - name: scenario_title
    dtype: string
  - name: script_text
    dtype: string
  - name: duration
    dtype: float64
configs:
- config_name: default
  data_dir: data
---

# K-FinancialSpeech

**한국어 금융 도메인 감정 음성 데이터셋**

금융 서비스(보이스피싱, 이체 오류, 대출 상담 등) 상황에서의 감정 발화를 수집한 한국어 음성 데이터셋입니다. FDS(이상거래탐지) 시스템의 감정 분류 모델 학습을 위해 제작되었습니다.

## Dataset Description

- **Language**: Korean (한국어)
- **Audio Format**: 16kHz, mono, WAV (PCM 16-bit)
- **Total Samples**: 1,250
- **Total Duration**: ~69 minutes
- **Speakers**: 10 (male 5, female 5)
- **Emotions**: 5 classes (균등 분포, 각 250개)
- **Recording Environment**: Browser microphone (실서비스와 동일한 환경)

## Emotion Classes

| Label | Korean | Description | Count |
|-------|--------|-------------|-------|
| `anger` | 분노/짜증 | 이체 오류, 수수료 부당 청구, 카드 도용 등 | 250 |
| `anxiety` | 불안/두려움 | 보이스피싱, 알 수 없는 출금, 투자 급락 등 | 250 |
| `sadness` | 슬픔/낙담 | 사기 피해, 대출 거절, 경제적 어려움 등 | 250 |
| `happiness` | 기쁨/만족 | 대출 승인, 적금 만기, 투자 수익 등 | 250 |
| `neutral` | 중립/평온 | 잔액 조회, 상품 문의, 일상 이체 등 | 250 |

## Scenarios

각 감정에 5개 시나리오, 시나리오당 5개 스크립트 = 총 25개 시나리오, 125개 스크립트.

<details>
<summary>전체 시나리오 목록</summary>

| ID | Emotion | Scenario |
|----|---------|----------|
| A1 | anger | 이체 오류 반복 |
| A2 | anger | 수수료 부당 청구 |
| A3 | anger | 카드 도용 의심 |
| A4 | anger | 대출 약속 번복 |
| A5 | anger | 앱/서비스 장애 |
| B1 | anxiety | 보이스피싱 의심 전화 |
| B2 | anxiety | 알 수 없는 출금 |
| B3 | anxiety | 투자 급락 |
| B4 | anxiety | 피싱 링크 클릭 |
| B5 | anxiety | 보증 요청 |
| C1 | sadness | 전 재산 사기 피해 |
| C2 | sadness | 대출 거절 연속 |
| C3 | sadness | 은퇴 후 자산 감소 |
| C4 | sadness | 가족 경제적 어려움 |
| C5 | sadness | 사기 후 자책 |
| D1 | happiness | 대출 승인 |
| D2 | happiness | 적금 만기 수령 |
| D3 | happiness | 투자 수익 실현 |
| D4 | happiness | 환불/보상 성공 |
| D5 | happiness | 처음 목돈 마련 |
| E1 | neutral | 잔액 조회 |
| E2 | neutral | 상품 문의 |
| E3 | neutral | 일상 이체 |
| E4 | neutral | 카드 재발급 |
| E5 | neutral | 인증서/OTP |

</details>

## Speaker Distribution

| Speaker | Gender | Samples |
|---------|--------|---------|
| spk01 | male | 125 |
| spk02 | male | 125 |
| spk03 | male | 125 |
| spk05 | male | 125 |
| spk06 | male | 125 |
| spk04 | female | 125 |
| spk07 | female | 125 |
| spk08 | female | 125 |
| spk09 | female | 125 |
| spk10 | female | 125 |

## Usage

```python
from datasets import load_dataset

dataset = load_dataset("dynohyuck/K-FinancialSpeech")

# Access a sample
sample = dataset["train"][0]
print(sample["label"])        # "anger"
print(sample["speaker_id"])   # "spk01"
print(sample["script_text"])  # "아니 이게 세 번째인데 왜 계속 오류가 나는 거예요?"
print(sample["audio"])        # {"path": ..., "array": [...], "sampling_rate": 16000}
```

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| `audio` | Audio | 16kHz mono WAV audio |
| `file_name` | string | WAV filename (`spk01_A1_01.wav`) |
| `label` | string | Emotion label (anger/anxiety/sadness/happiness/neutral) |
| `speaker_id` | string | Speaker identifier (spk01~spk10) |
| `gender` | string | Speaker gender (male/female) |
| `scenario` | string | Scenario ID (A1~E5) |
| `scenario_title` | string | Scenario description in Korean |
| `script_text` | string | Reference script text (speakers spoke freely, not read verbatim) |
| `duration` | float | Audio duration in seconds (after silence trimming) |

## Preprocessing Applied

- **Silence trimming**: Energy-based (-40dB threshold) leading/trailing silence removal
- **Volume normalization**: RMS normalization to 0.05 (~-26 dBFS) across all speakers

## Recording Protocol

- Speakers were given a scenario description and emotional context, then spoke **freely** (not reading scripts verbatim)
- Each speaker recorded all 5 emotions across all 25 scenarios to prevent speaker-emotion confounding
- Recorded via browser microphone to match real-service audio characteristics
- Sessions limited to 30-40 recordings with breaks to prevent emotional fatigue

## Intended Use

- Speech Emotion Recognition (SER) model training/fine-tuning
- Financial domain emotion detection research
- Fraud Detection System (FDS) emotion-aware components
- Korean speech emotion benchmark

## Limitations

- 1,250 samples is relatively small for standalone training; best used for domain adaptation/fine-tuning
- 10 speakers provides moderate speaker diversity
- Recorded in quiet indoor environments; may not cover all real-world noise conditions
- Self-labeled with cross-check (not multi-annotator soft labels)

## Citation

```bibtex
@dataset{k_financial_speech_2026,
  title={K-FinancialSpeech: Korean Financial Domain Speech Emotion Dataset},
  author={dynohyuck},
  year={2026},
  url={https://huggingface.co/datasets/dynohyuck/K-FinancialSpeech},
  license={CC BY-NC 4.0}
}
```
