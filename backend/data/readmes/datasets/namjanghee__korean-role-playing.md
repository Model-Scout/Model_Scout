---
license: apache-2.0
configs:
- config_name: exa-data
  data_files:
  - split: train
    path: exa-data/train-*
- config_name: general-roleplay-data
  data_files:
  - split: train
    path: general-roleplay-data/train-*
- config_name: gf-persona-data
  data_files:
  - split: train
    path: gf-persona-data/train-*
- config_name: youtube-couple-data
  data_files:
  - split: train
    path: youtube-couple-data/train-*
dataset_info:
- config_name: exa-data
  features:
  - name: text
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: topic
    dtype: string
  splits:
  - name: train
    num_bytes: 912254
    num_examples: 890
  download_size: 428351
  dataset_size: 912254
- config_name: general-roleplay-data
  features:
  - name: text
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 169138957
    num_examples: 32367
  download_size: 96374557
  dataset_size: 169138957
- config_name: gf-persona-data
  features:
  - name: text
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 3030200
    num_examples: 1920
  download_size: 1643660
  dataset_size: 3030200
- config_name: youtube-couple-data
  features:
  - name: text
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 161269
    num_examples: 125
  download_size: 85804
  dataset_size: 161269
language:
- ko
tags:
- korean
- persona
- role-playing
size_categories:
- 10K<n<100K
---
# Dataset Card for korean-role-playing: 한국어 롤플레잉 대화 데이터셋

### 데이터셋 요약  
**korean-role-playing**은 다양한 상황과 관계를 반영한 한국어 기반 롤플레잉 대화 데이터셋입니다. 본 데이터셋은 총 4개의 세부 데이터셋으로 구성되어 있으며, 연인 간의 역할극, 유튜브 커플 대화, 일반 상황 기반 롤플레잉, EXA 스타일 페르소나 역할극 등 다양한 맥락을 포함합니다. 한국어 기반의 캐릭터 AI, 역할 기반 LLM, 인격 일관성 평가 등에 활용할 수 있습니다.

### 지원 태스크 및 리더보드
- `role-playing`: 다양한 캐릭터와 상황에 맞춘 대화를 생성하거나 이해하는 태스크에 사용됩니다.
- `multi-turn dialogue`: 다중 발화 문맥에서의 자연스러운 응답 생성

### 언어  
모든 데이터는 한국어(`ko`)로 구성되어 있습니다.

## 데이터셋 구조

### Subset 구성
- `gf-persona-data`: 연인 관계를 기반으로 구성된 페르소나 대화  
  👉 [관련 토론 링크](https://github.com/Pseudo-Lab/Hugging-Face-Hub-Garden/discussions/31)

- `youtube-couple-data`: 한국 커플 유튜브 영상에서 자막을 기반으로 구축한 실제 커플 대화 데이터

- `general-roleplay-data`: Hugging Face의 데이터 Smoltalk의 subset인 Role-Playing 데이터를 한국어로 재구성한 일반 롤플레잉 데이터  
  👉 원본: [Smoltalk](https://huggingface.co/datasets/HuggingFaceTB/smoltalk/viewer/smol-magpie-ultra)

- `exa-data`: LG EXAONE을 재해석한 자체 캐릭터 엑사(EXA) 시나리오와 페르소나에 맞춘 역할극 대화  
  👉 [관련 토론 링크](https://github.com/Pseudo-Lab/Hugging-Face-Hub-Garden/discussions/30)

### 데이터 필드
각 서브셋은 다음과 같은 필드를 포함합니다:

- `text`: multi-turn format으로 되어있는 conversation 필드
  - `user`: 유저(남자로 가정)
  - `assistant`: 어시스턴트(여자로 가정), 현재 역할극에 맞는 자연스러운 응답  

### 데이터 분할
- 모든 서브셋은 현재 `train` split만 제공됩니다.
- 각 서브셋의 샘플 수는 Hugging Face Viewer에서 확인 가능합니다.

## 데이터셋 생성

### 큐레이션 근거  
한국어로 자연스럽고 페르소나 기반의 역할극 대화를 가능하게 하는 모델 개발을 위해 구축되었습니다. 기존 영어 중심의 역할극 데이터의 한계를 보완하고, 한국어로 된 상호작용을 반영한 데이터 구성을 목표로 하였습니다.

### 구축 방식 요약
- `gf-persona-data`: 설정된 페르소나 기반 시나리오와 발화 구조 설계
- `youtube-couple-data`: 유튜브 영상 자막 수집 → 대화 단위 분할 및 정제 → 페어링
- `general-roleplay-data`: gpt-4o-mini를 이용해 영어 Smoltalk 데이터를 한국어로 재가공
- `exa-data`: EXAONE 스타일 페르소나 설계 및 대화 유도 → gpt-4o를 이용한 응답 생성

## 데이터 사용 시 고려사항

### 알려진 한계
- **응답 다양성**: 일부 서브셋은 응답이 특정 스타일로 편향될 수 있습니다.  
- **관계 중심 대화**: 연인 관계에 기반한 대화가 포함되어 있으며, 특정 성별/관계를 가정할 수 있습니다.  
- **LLM 생성 기반 일부 포함**: 일부 응답은 LLM 기반 생성 결과이며, 수동 정제 과정을 거쳤지만 완전한 사람 대화와의 차이가 존재할 수 있습니다.  

## 추가 정보

### 데이터셋 큐레이터
[@lastdefiance20](https://huggingface.co/lastdefiance20), [@jjlee6496](https://huggingface.co/jjlee6496)

### 라이선스 정보
본 데이터셋은 **Apache 2.0** 라이선스를 따릅니다.

### 인용 정보
이 데이터셋을 연구 등에 활용하실 경우, 다음 형식으로 인용해주시기 바랍니다.

```
@misc{korean_role_playing_2025,
title={korean-role-playing},
author={Jaeyoon Jung, Jeongjin Lee},
year={2025},
publisher={Hugging Face KREW},
howpublished={\url{https://huggingface.co/datasets/huggingface-KREW/korean-role-playing}}
}
```
### 기여
데이터셋 구축에 참여한 모든 팀원들과 가짜연구소, Hugging Face KREW에게 감사드립니다.