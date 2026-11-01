---
license: cc-by-4.0  # [확인 필요] AI Hub 유래 문장 포함 시 재배포 조건에 맞게 수정
language:
- ko
- en
task_categories:
- translation
tags:
- metamorphic-testing
- machine-translation
- robustness
- korean
- word-order
size_categories:
- n<1K
---

# Korean Word-Order Metamorphic Testing Set for MT Robustness

한국어 어순 변형에 대한 대형 언어 모델(LLM) 번역의 강건성을 평가하기 위한
메타모픽 테스팅 데이터셋입니다. 문장의 의미를 보존한 채 어순만 변경한
원문–변형문 쌍으로 구성되며, 다섯 가지 어순 변형 유형을 포함합니다.

## Dataset Summary

- **총 세트 수**: 258
- **구성**: 각 세트는 한국어 원문(`src_orig`)과 어순 변형문(`src_trans`) 한 쌍
- **변형 원칙**: 단어·어미는 동일하게 유지하고 어순만 재배치
  (능동–피동 변형인 CAT-4는 태 변형 특성상 예외)
- **라벨**: `gold_mr_violated` — 모델 번역 시 변형 관계 위반 여부(사람 판정)

## Categories

| 코드 | 변형 유형 | 세트 수 | 변형 규칙 |
|---|---|---|---|
| CAT-1 | 주어–목적어 도치 | 46 | 주어·목적어 어순 교환 (SOV→OSV) |
| CAT-2 | 부사구 이동 | 52 | 부사구를 문두로 이동 |
| CAT-3 | 종속절 재배치 | 52 | 종속절과 주절의 상대 위치 재배치 |
| CAT-4 | 능동↔피동 | 52 | 능동문↔피동문 태 변형 |
| CAT-5 | 인용절 전치 | 56 | 인용절을 문두로 전치 |

## Data Fields

- `id` (string): 세트 식별자 (예: `CAT1-H001`)
- `cat` (string): 변형 카테고리 (`CAT-1` ~ `CAT-5`)
- `src_orig` (string): 원문 (한국어)
- `src_trans` (string): 어순 변형문 (한국어)
- `gold_mr_violated` (bool): 변형 관계 위반 여부.
  `true` = 어순 변형으로 번역의 핵심 의미가 달라짐,
  `false` = 의미 유지(강건). 특정 모델의 번역 출력을 사람이 판정한 값.
- `source` (string): 문장 출처 (`human` = 전문가 작성 등)

## Usage

```python
from datasets import load_dataset

ds = load_dataset("YMmim/korean-word-order-mt-robustness", split="train")
print(ds[0])
# {'id': 'CAT1-H001', 'cat': 'CAT-1',
#  'src_orig': '농부가 씨앗을 뿌렸다.', 'src_trans': '씨앗을 농부가 뿌렸다.',
#  'gold_mr_violated': None, 'source': 'human', ...}
```

> `gold_mr_violated` 라벨은 특정 대상 모델(아래 참조)의 번역 출력을
> 기준으로 부여된 것이므로, 다른 모델을 평가할 때는 재라벨링이 필요합니다.

## Labeling Protocol

각 세트의 원문과 변형문을 대상 모델로 각각 번역(그리디 디코딩)한 뒤,
두 영어 출력의 핵심 의미가 달라졌는지를 사람이 판정하여 라벨링하였습니다.

- **대상 모델**: `Qwen/Qwen2.5-1.5B-Instruct`
- **판정 기준**: 핵심 의미(명제 내용·논항 관계)가 달라지면 위반(true)
- **검수**: 어순 보존 여부는 자동 검증(문자 구성 일치), 자연스러움·의미
  보존은 전문가 검수

## Key Findings (해당 모델 기준)

- 전체 변형 관계 위반율: **7.8%** (20/258)
- 카테고리별 위반율: CAT-2 0.0% ~ CAT-1 15.2% (유형별 체계적 차이)
- 위반 20건 중 **18건(90%)은 어순이 아닌 모델의 어휘 오역**에서 비롯
  → 어순 변형에 기인한 실질적 위반은 전체의 약 0.8%

## Source & License

- **전문가 작성분**: 본 데이터셋 저자가 직접 작성.
- **말뭉치 유래분(있는 경우)**: [확인 필요] 일부 베이스 문장이 공개
  말뭉치에서 유래한 경우, 해당 출처(예: AI Hub 한국어–영어 번역 말뭉치)와
  그 이용 약관·재배포 조건을 여기에 명시하십시오. 재배포가 제한되면
  해당 문장을 제외하거나 재현 스크립트만 공개하는 방식으로 조정하십시오.
- **License**: [확인 필요] 위 출처 조건에 부합하는 라이선스로 설정.

## Citation

```bibtex
@misc{[확인필요]2026koreanwordorder,
  title  = {한국어 어순 변형에 대한 대형 언어 모델 번역의 강건성:
            메타모픽 테스팅 기반 실증 연구},
  author = {[저자명]},
  year   = {2026},
  howpublished = {Hugging Face Datasets},
  url    = {https://huggingface.co/datasets/YMmim/korean-word-order-mt-robustness}
}
```

## Limitations

- 단일 대상 모델(Qwen2.5-1.5B-Instruct) 기준 라벨.
- 258세트·위반 20건으로 양성 샘플이 적음.
- 비교적 짧은 단문 위주 — 장문·복문 일반화는 미검증.