---
license: cc-by-nc-sa-4.0
language:
  - ko
task_categories:
  - text-classification
task_ids:
  - multi-class-classification
pretty_name: Korean Smishing Message Dataset
tags:
  - korean
  - smishing
  - sms
  - phishing
  - financial-security
  - cybersecurity
  - text-classification
---

# Korean Smishing Message Dataset

## Dataset Description

`kor-smishing-message`는 한국어 문자 메시지를 대상으로 정상 메시지와 스미싱 메시지를 분류하기 위해 구축한 데이터셋입니다.

본 데이터셋은 스미싱 탐지 모델 학습 및 평가를 목적으로 하며, 단순한 이진 분류 라벨뿐만 아니라 메시지의 판단 근거와 유형 정보를 함께 포함합니다. 이를 통해 모델이 단순히 정상/스미싱 여부를 예측하는 것을 넘어, 어떤 표현이나 맥락이 위험 신호로 작용하는지 분석하는 데 활용할 수 있습니다.

## Dataset Details

- **Language:** Korean
- **Task:** Text Classification
- **Domain:** Smishing Detection, Financial Security, Cybersecurity
- **License:** CC BY-NC-SA 4.0
- **Data Format:** CSV / Parquet
- **Labels:** Normal / Smishing

## Dataset Structure

각 데이터는 다음과 같은 필드로 구성되어 있습니다.

| Column | Type | Description |
|---|---|---|
| `content` | string | 문자 메시지 본문 |
| `label` | string or int | 정상 메시지 또는 스미싱 메시지 라벨 |
| `explanation` | string | 해당 메시지가 정상 또는 스미싱으로 판단되는 이유 |
| `type` | string | 메시지 유형 또는 스미싱 유형 |

## Label Description

| Label | Description |
|---|---|
| `normal` | 정상 문자 메시지 |
| `smishing` | 악성 링크, 개인정보 요구, 금융 사기, 기관 사칭 등 스미싱 의심 문자 |

라벨 값이 정수형으로 제공되는 경우 다음과 같이 해석할 수 있습니다.

| Label | Description |
|---|---|
| `0` | 정상 문자 메시지 |
| `1` | 스미싱 문자 메시지 |

## Example

```json
{
  "content": "[국민건강보험] 미납 보험료가 있습니다. 아래 링크에서 확인 바랍니다.",
  "label": "smishing",
  "explanation": "공공기관을 사칭하며 외부 링크 접속을 유도하고 있어 스미싱으로 판단됩니다.",
  "type": "기관 사칭"
}