---
language:
- ko
license: cc-by-4.0
task_categories:
- text-to-speech
tags:
- tts
- korean
- speech
- gemini
size_categories:
- n<1K
dataset_info:
  features:
  - name: audio
    dtype:
      audio:
        sampling_rate: 24000
  - name: id
    dtype: int64
  - name: category
    dtype: string
  - name: sub
    dtype: string
  - name: text
    dtype: string
  - name: difficulty
    dtype: string
  - name: instruct
    dtype: string
  splits:
  - name: train
    num_bytes: 30261995
    num_examples: 120
  download_size: 30256510
  dataset_size: 30261995
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# Korean TTS Training Dataset

한국어 TTS 학습용 음성 데이터셋 (120문장)

## Dataset Description

Google Gemini `gemini-2.5-pro-preview-tts` 모델 (Voice: Zephyr)로 생성한 한국어 음성 데이터셋입니다.
발음, 운율, 감정, 억양 등 다양한 카테고리를 포함합니다.

### Audio Format
- Format: WAV (PCM)
- Sample Rate: 24,000 Hz
- Bit Depth: 16-bit
- Channels: Mono

## Categories

### 발음/운율 (70문장)
| Category | Count | Description |
|----------|-------|-------------|
| 1-숫자 | 10 | 숫자, 전화번호, 날짜, 금액 |
| 2-겹받침 | 10 | 겹받침, ㅎ받침 발음 |
| 3-음운변동 | 10 | 연음, 경음화, 비음화, 유음화 |
| 4-모음ㄹ | 10 | 이중모음, ㄹ발음, 두음법칙 |
| 5-외래어 | 10 | 외래어, 영어 혼용 |
| 6-긴문장 | 10 | 긴 문장, 호흡 |
| 8-특수 | 10 | 구개음화, 의성어, 의태어 |

### 감정/억양 (50문장)
| Category | Count | Description |
|----------|-------|-------------|
| 7A-억양 | 13 | 의문문, 명령, 나열, 강조 등 |
| 7B-긍정감정 | 12 | 기쁨, 감동, 감사, 안도, 설렘 |
| 7C-부정감정 | 13 | 슬픔, 분노, 짜증, 불안, 실망 |
| 7D-복합전환 | 12 | 감정 변화, 반어, 망설임 |

## Usage

```python
from datasets import load_dataset

ds = load_dataset("daje/korean-tts-training")
```

## Fields

| Field | Description |
|-------|-------------|
| `file_name` | 오디오 파일명 |
| `id` | 문장 고유 ID |
| `category` | 카테고리 |
| `sub` | 세부 카테고리 |
| `text` | 한국어 문장 |
| `difficulty` | 발음/억양 난이도 설명 |
| `instruct` | TTS 생성 시 사용한 영어 프롬프트 |
