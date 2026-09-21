---
license: other
base_model: youngseok12/HyperCLOVA-X-SEED-Think-14B-minimal-sft-71875
language:
- ko
library_name: transformers
pipeline_tag: text-generation
tags:
- korean
- sft
- aihub
- lora-merge
- grammar
---

# HyperCLOVA X SEED Think-14B KL-Grammar (v_proj,o_proj, lr=5e-6)

이 저장소는 K-AI 리더보드 최고 제출 모델
`youngseok12/HyperCLOVA-X-SEED-Think-14B-minimal-sft-71875`(K-AI 실제 평균
0.4788) 위에, 검수한 국어 문법 데이터로 학습한 2차 LoRA를 병합한 standalone
BF16 모델입니다. pristine Base가 아니라 이미 한 번 SFT된 최고 제출 모델을
base로 삼아 추가 학습한 결과물입니다.

## 배경

`v_proj,o_proj` / `q_proj,v_proj` 두 module 조합과 `1e-6/5e-6/1e-5/3e-5` 네
학습률을 같은 데이터·같은 32 step·같은 r=4/alpha=8 조건에서 대조한 sweep 중
하나입니다. 같은 조건에서 `q_proj,v_proj`와 `v_proj,o_proj`(lr=1e-6)는 출력이
Minimal SFT와 96~99% 동일했고 목표 축(CLIcK)이 오히려 소폭 하락했지만, 이
`v_proj,o_proj`/`lr=5e-6` 조합만 로컬 5축에서 근소하게 개선됐습니다.

## 학습 데이터

- AI Hub 71857(국어 교과 지문형 문제) 중 2015/2022 교육과정 성취기준 코드로
  국어04(문법) 영역만 추린 뒤, 선택지 중복·정의 그대로 베끼면 맞는 문항·주제
  이탈 문항을 제거하고 품사·형태소(126) / 음운·맞춤법(128) / 문장·높임·문맥
  어휘(128) 세 갈래로 나눠 뽑은 **382개**
- 최고 제출 모델 학습에 실제 쓰인 AI Hub 71875(필수의료) self-distill
  512개 파일에서 무작위로 뽑은 **유지용 128개**(정답 유지 목적)
- 합계 510행, label-only(정답 선택지 문자 한 글자)
- 공개 benchmark 문제·정답·평가 파일은 사용하지 않음
- 검증 홀드아웃 200개는 학습 데이터와 문항 ID·지문 fingerprint 양쪽 모두 겹치지 않게 별도 확보(이번 로컬 평가에는 canonical suite만 사용)
- 데이터셋 안내: <https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71857>, <https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71875>

## 학습 설정

- Base: `youngseok12/HyperCLOVA-X-SEED-Think-14B-minimal-sft-71875`
- LoRA: `r=4`, `alpha=8`, `dropout=0`, bias=`none`
- Target modules: `v_proj`, `o_proj`
- Learning rate: `5e-6`; scheduler: constant; warmup: `0`; weight decay: `0`
- Epochs: `1`; optimizer steps: `32`
- Per-device batch size: `1`; gradient accumulation: `16`(effective batch `16`)
- BF16; max sequence length `1024`; packing disabled
- Assistant-only loss; gradient checkpointing enabled
- Seed/data seed: `42/42`
- 최종 train loss: `2.6378`

## 병합 및 사용

LoRA adapter를 base 모델에 병합한 standalone BF16 `safetensors` 모델입니다.
병합 후 전체 텐서 NaN/Inf 검사를 통과했고, 병합본에서 직접 생성한 문법·의료
smoke 문항 모두 정답을 출력했습니다.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "youngseok12/HyperCLOVA-X-SEED-Think-14B-kl-grammar-vo-lr5e-6"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="bfloat16",
    device_map="auto",
)
```

## 라이선스 및 제한

Base 모델과 병합 모델은 NAVER의 HyperCLOVA X SEED 14B Think Model License
Agreement를 따릅니다. `LICENSE`의 전체 조건과 AI Hub 원천 데이터 이용약관을
확인해야 합니다. 연구·평가용 모델이며, 출력의 정확성을 보장하지 않습니다.
전문적인 판단의 유일한 근거로 사용하지 마십시오.
