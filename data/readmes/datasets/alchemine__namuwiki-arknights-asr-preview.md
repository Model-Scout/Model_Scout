---
language:
  - ko
task_categories:
  - automatic-speech-recognition
tags:
  - namuwiki
  - arknights
  - game
license: cc-by-nc-sa-2.0
---

# ⚠️ 이 데이터셋은 테스트 버전으로, 데이터 일관성이 보장되지 않습니다.

---

# Namuwiki Arknights ASR Dataset (Preview)

이 데이터셋은 [명일방주 - 나무위키](https://namu.wiki/w/명일방주) 관련 문서를 기반으로 음성 인식(Automatic Speech Recognition, ASR) 모델 훈련에 사용될 수 있는 한국어 음성 데이터셋입니다.

- version: [v1.0](https://huggingface.co/datasets/alchemine/namuwiki-arknights-asr-preview/tree/v1.0)

## 📅 텍스트 데이터 생성일

2025/09/12

## 🎙️ TTS 모델

[bosonai/higgs-audio-v2-generation-3B-base](https://huggingface.co/bosonai/higgs-audio-v2-generation-3B-base)

## 📊 데이터셋 통계

- **전체 문서 수**: 46
- **전체 데이터 수**: 11,930
- **훈련 데이터 수**: 7,635
- **검증 데이터 수**: 1,909
- **테스트 데이터 수**: 2,386
- **총 오디오 길이**: 32.14시간
- **평균 오디오 길이**: 9.70초
- **오디오 길이 최소값**: 1.96초
- **오디오 길이 최대값**: 22.68초
- **샘플링 레이트**: 16kHz
- **오디오 채널**: Mono

## 📝 데이터 구조

각 샘플은 다음과 같은 필드를 포함합니다:

- `id` (`str`): 고유 식별자
- `doc_title` (`str`): 문서 제목
- `path` (`str`): 오디오 파일 경로
- `text` (`str`): 한국어 텍스트 전사
- `audio` (`dict`): 16kHz 모노 오디오 파일
- `duration` (`float`): 오디오 길이(초)
- `created_at_text` (`str`): 텍스트 데이터 생성 시간 (ISO 8601 형식)
- `tts_model` (`str`): TTS 모델명

## 🏗️ 데이터 생성 과정

이 데이터셋은 다음 단계에 따라 구축되었습니다:

### 1. 텍스트 데이터 수집

나무위키의 "명일방주" 관련 문서들에서 텍스트 콘텐츠를 추출합니다.

### 2. 텍스트 전처리

수집된 텍스트는 ASR 모델 학습에 적합하도록 다음과 같은 전처리 과정을 거칩니다:

- 줄바꿈 대비 문장의 개수가 충분히 많은 문장을 선별합니다.
- 마침표, 물음표, 느낌표를 기준으로 문장을 분리하고, 너무 짧은 문장(5단어 이하)은 병합하며, 너무 긴 문장(20단어 초과)은 적절한 길이로 분할합니다.
- 불필요한 괄호, 줄바꿈 문자, 특정 특수 문자를 제거하고, `...`는 `.`으로 통일합니다.
- 한국어 내용이 없는 문장은 제외합니다.
- 동일한 텍스트를 가진 문장은 제거하여 데이터의 다양성을 확보합니다.

### 3. 음성 데이터 생성

전처리된 텍스트는 [bosonai/higgs-audio-v2-generation-3B-base](https://huggingface.co/bosonai/higgs-audio-v2-generation-3B-base) TTS(Text-to-Speech) 모델을 통해 음성으로 변환됩니다.

- 남성 및 여성 성우의 목소리를 무작위로 선택하여 데이터셋의 성별 분포를 다양화합니다.
- 모든 음성이 30초가 넘지 않도록 합니다.

## 💡 사용 예시

```python
from datasets import load_dataset

# 데이터셋 로드
dataset = load_dataset("alchemine/namuwiki-arknights-asr-preview")

# 훈련 데이터셋 접근
train_dataset = dataset["train"]
print("#train:", len(train_dataset))
print(train_dataset[0])

# 오디오 파일 재생 (예시: 첫 번째 훈련 데이터 샘플)
from IPython.display import Audio
Audio(train_dataset[0]["audio"]["array"], rate=train_dataset[0]["audio"]["sampling_rate"])
```

## 📄 라이선스

이 데이터셋은 [CC BY-NC-SA 2.0 KR](https://creativecommons.org/licenses/by-nc-sa/2.0/kr/legalcode) 라이선스 하에 배포됩니다.
