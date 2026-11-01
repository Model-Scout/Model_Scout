---
license: apache-2.0
language:
- ko
task_categories:
- text-generation
pretty_name: KAWK500M Korean SFT v1
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train/*.parquet
  - split: validation
    path: data/validation/*.parquet
---

# KAWK500M Korean SFT v1

한국어 전용 500M급 causal LM을 위한 assistant-only SFT 데이터입니다. 기존
Keural 대화/RAG 데이터는 사용하지 않았습니다.

## 고정된 원본

- `distilqwen`: [lcw99/DistilQwen_100k_korean](https://huggingface.co/datasets/lcw99/DistilQwen_100k_korean/tree/7324954c71af8f0974654e5c7e211f5b3fad5a96) @ `7324954c71af8f0974654e5c7e211f5b3fad5a96` (apache-2.0)
- `writing`: [coastral/korean-writing-style-instruct](https://huggingface.co/datasets/coastral/korean-writing-style-instruct/tree/9f31462314f07847534fd13f7406c330ab15d156) @ `9f31462314f07847534fd13f7406c330ab15d156` (apache-2.0)
- `carrot`: [CarrotAI/ko-instruction-dataset](https://huggingface.co/datasets/CarrotAI/ko-instruction-dataset/tree/5c0e2c0180b50400e401dd0b296043f18fc6cb3f) @ `5c0e2c0180b50400e401dd0b296043f18fc6cb3f` (apache-2.0)
- `aya-human-ko`: [CohereLabs/aya_dataset](https://huggingface.co/datasets/CohereLabs/aya_dataset/tree/f9ea04583f02a8f86404ff6c58bf75fe637df8a2) @ `f9ea04583f02a8f86404ff6c58bf75fe637df8a2` (apache-2.0)

## 처리

- 한국어 열만 사용하고 NFC 정규화
- HTML 정리 및 이메일·전화번호·주민등록번호 형태 마스킹
- 명시적인 코드, LaTeX/수식 중심 샘플, 공개된 사고과정 태그 제거
- 한국어 비율 및 반복·기호·목록 품질 필터
- 모든 원본 사이 BLAKE2b 정확 중복 제거
- KAWK500M 32K 토크나이저로 2,048토큰 고정 패킹
- 사용자·시스템 토큰은 `loss_mask=0`, 답변 및 EOS만 `loss_mask=1`
- 문서 해시 기반 고정 validation 분리

## 규모

- train: 22,155 records
- validation: 300 records
- sequence length: 2,048
- supervised assistant tokens: 34,174,461

각 행에는 `input_ids`, `loss_mask`, `source`가 있습니다. RunPod에서는
`load_dataset(..., streaming=True)`로 읽을 수 있습니다. 원본별 세부 조건과
제한도 함께 확인해야 합니다.
