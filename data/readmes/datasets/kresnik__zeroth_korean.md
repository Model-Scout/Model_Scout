---
dataset_info:
  features:
  - name: id
    dtype: string
  - name: speaker_id
    dtype: int64
  - name: chapter_id
    dtype: int64
  - name: path
    dtype: string
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2818850887.0
    num_examples: 22263
  - name: test
    num_bytes: 59879514.0
    num_examples: 457
  download_size: 2877012819
  dataset_size: 2878730401.0
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
---


# Zeroth-Korean Dataset

## Introduction
The Zeroth-Korean dataset is a publicly available speech dataset created for Korean automatic speech recognition (ASR) research and development. This dataset is distributed under the CC BY 4.0 license, allowing anyone to use it freely. The goal of the Zeroth project is to make Korean speech recognition more widely accessible.

## Dataset Overview
- **Total Data**: Approximately 51.6 hours of training data and 1.2 hours of test data
- **Number of Utterances**: 22,263 utterances in the training set and 457 utterances in the test set
- **Number of Speakers**: 105 speakers in the training set, 10 speakers in the test set
- **Sampling Rate**: 16kHz

## Version Information
### Version 2.0.0
- **Changes**:
  - Instead of downloading the original files directly from openslr.org, the data is distributed using pyarrow for more efficient storage.
  - The `audio` field has been updated from `numpy.ndarray` to `datasets.Audio` type for improved accessibility of audio data.
  - The `file` field has been renamed to `path`.

## Dataset Composition
- **Training Data (Train)**: Consists of 51.6 hours of Korean utterances, with a total of 22,263 utterances. This data is used to train speech recognition models.
- **Test Data (Test)**: Consists of 1.2 hours of utterances, with a total of 457 utterances, used for evaluating model performance.

### Data Fields
- **id**: Unique identifier for each utterance (string)
- **speaker_id**: Speaker identifier (int64)
- **chapter_id**: Chapter identifier (int64)
- **path**: Path to the audio file (string)
- **audio**: Audio data (managed as `datasets.Audio` type, sampling rate 16kHz)
- **text**: Transcribed text of the utterance (string)

## Usage Example
The Zeroth-Korean dataset can be easily loaded using the Hugging Face library.

```python
from datasets import load_dataset

# Load Zeroth-Korean dataset
dataset = load_dataset("kresnik/zeroth_korean")

# Print an example from the training dataset
print(dataset['train'][0])
```

## License
This dataset follows the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license. This license allows the data to be used freely, provided the source is properly credited.

The uploader has transferred the publicly available data from openslr.org to the Hugging Face Hub and did not participate in the creation of the dataset. This dataset is provided to facilitate broader accessibility of the original dataset.

The Zeroth project was developed through the collaboration of Lucas Jo (@Atlas Guide Inc.) and Wonkyum Lee (@Gridspace Inc.).
- **Contact**: Lucas Jo (lucasjo@goodatlas.com), Wonkyum Lee (wonkyum@gridspace.com)







# Zeroth-Korean 데이터셋 (한글)

## 소개
Zeroth-Korean 데이터셋은 한국어 음성 인식 연구와 개발을 위해 제작된 공개 음성 데이터셋입니다. 이 데이터셋은 CC BY 4.0 라이선스 하에 배포되며, 누구나 자유롭게 사용할 수 있습니다. Zeroth 프로젝트의 목표는 한국어 음성 인식을 더 널리 사용할 수 있도록 하는 것입니다.

## 데이터셋 개요
- **총 데이터량**: 약 51.6시간의 훈련 데이터와 1.2시간의 테스트 데이터
- **발화 수**: 22,263개의 훈련 발화와 457개의 테스트 발화
- **화자 수**: 훈련 데이터에서 105명의 화자, 테스트 데이터에서 10명의 화자
- **샘플링 레이트**: 16kHz

## 버전 정보
### Version 2.0.0
- **변경 사항**:
  - openslr.org에서 원본 파일을 직접 다운로드하는 방식 대신 pyarrow를 사용하여 분산 저장
  - `audio` 필드를 `numpy.ndarray` 대신 `datasets.Audio` 타입으로 업데이트하여 오디오 데이터 접근성 향상
  - 기존 `file` 필드를 `path`로 이름 변경

## 데이터 구성
- **훈련 데이터 (Train)**: 51.6시간의 한국어 발화 데이터로 구성되며, 발화 수는 총 22,263개입니다. 이 데이터는 음성 인식 모델의 훈련에 사용됩니다.
- **테스트 데이터 (Test)**: 1.2시간의 발화 데이터로, 총 457개의 발화로 구성되어 있으며, 모델 성능 검증에 사용됩니다.

### 데이터 필드
- **id**: 발화 고유 식별자 (string)
- **speaker_id**: 화자 식별 번호 (int64)
- **chapter_id**: 챕터 식별 번호 (int64)
- **path**: 오디오 파일 경로 (string)
- **audio**: 오디오 데이터 (`datasets.Audio` 타입으로 관리, 샘플링 레이트 16kHz)
- **text**: 발화된 문장 (string)

## 사용 예시
Hugging Face 라이브러리를 통해 Zeroth-Korean 데이터셋을 쉽게 로드할 수 있습니다.

```python
from datasets import load_dataset

# Zeroth-Korean 데이터셋 로드
dataset = load_dataset("kresnik/zeroth_korean")

# 훈련 데이터셋 예시 출력
print(dataset['train'][0])
```

## 라이선스
이 데이터셋은 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 라이선스를 따릅니다. 이 라이선스는 데이터를 자유롭게 사용할 수 있도록 허용하되, 출처를 반드시 명시해야 합니다.

게시자는 openslr.org에 공개된 데이터를 Hugging Face Hub에 옮겨 배포하는 역할을 수행하였으며, 데이터셋 제작에는 참여하지 않았습니다. 이 데이터셋은 원본 데이터셋의 배포를 돕기 위한 목적으로 제공됩니다.

Zeroth 프로젝트는 Lucas Jo (@Atlas Guide Inc.)와 Wonkyum Lee (@Gridspace Inc.)의 협력으로 개발되었습니다.
- **연락처**: Lucas Jo (lucasjo@goodatlas.com), Wonkyum Lee (wonkyum@gridspace.com)

