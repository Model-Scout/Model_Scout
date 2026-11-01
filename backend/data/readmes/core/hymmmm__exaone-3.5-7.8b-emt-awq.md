---
language:
- ko
license: other
license_name: exaone
license_link: https://huggingface.co/LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct/blob/main/LICENSE
base_model: LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct
pipeline_tag: text-generation
tags:
- "exaone"
- "korean"
- "medical"
- "emergency-medicine"
- "pediatrics"
- "119"
- "hapes"
- "full-finetune"
- "awq"
- "4-bit"
---

# EXAONE 3.5 7.8B · EMT Full Fine-tuning (AWQ 4-bit)

> **상태: ✅ 학습방식 비교군 (Full FT vs QLoRA)**

한국어 소아 응급(119 구급대원) 대화용으로 파인튜닝한 EXAONE 3.5 7.8B 모델입니다.

## 이 모델은

- **베이스**: `LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct`
- **데이터**: v2 (2,001건) — QLoRA v2 모델과 같은 데이터
- **목적**: 같은 데이터에서 **Full fine-tuning vs QLoRA** 비교. 처음엔 Full FT도 메인 후보였지만 epoch 2에서 과적합이 확인돼, 이후 프로젝트 메인 방식은 QLoRA로 정했습니다.
- BF16 학습 결과를 Hub에 따로 올리지 않고 바로 AWQ로 양자화했습니다. 보정 데이터는 AutoAWQ 기본값(pileval, 영어)입니다. 한국어 도메인 데이터로 보정한 버전은 [`exaone-3.5-7.8b-emt-awq-calib`](https://huggingface.co/hymmmm/exaone-3.5-7.8b-emt-awq-calib)입니다.

| 항목 | 값 |
|---|---|
| 방법 | Full fine-tuning (BF16), assistant 턴만 학습 (`[|endofturn|]`까지 라벨 포함) |
| 학습 | 2 epoch, lr 1e-5, batch 1 × grad_accum 4 × 8 GPU (=32), max_length 1,024 |
| 환경 | SageMaker ml.p4d.24xlarge (8×A100), DeepSpeed ZeRO-3, transformers 5.5.0 |
| eval_loss | epoch1 0.9126 → **epoch2 0.8479** |

## 알려진 이슈

- 가끔 가짜 대화 턴(`[|user|]` 등)을 생성하는 드문 사례가 있습니다. 학습 라벨에는 EOS가 정상 포함되어 있어, AWQ 4-bit 양자화 부작용으로 추정합니다. 서빙 시 `stop` 토큰 지정을 권장합니다.

## 사용법 (vLLM)

```python
from vllm import LLM, SamplingParams

llm = LLM(
    model="hymmmm/exaone-3.5-7.8b-emt-awq",
    quantization="awq",
    dtype="float16",
    max_model_len=8192,
    trust_remote_code=True,
)
out = llm.chat(
    [{"role": "user", "content": "3세 남아, 열성경련 후 의식 저하. 현장에서 뭘 확인해야 하나요?"}],
    SamplingParams(temperature=0.3, max_tokens=1024),
)
print(out[0].outputs[0].text)
```

## 모델 패밀리 한눈에 보기

HAPES(소아 응급 119 구급대원 보조 챗봇) 연구에서 만든 모델들입니다. 모두 같은 과제(구급대원–챗봇 대화)로 학습했고, **백본 · 학습 방식 · 데이터 버전**만 다릅니다.

| 레포 | 백본 | 학습 방식 | 학습 데이터 | 형식 | 상태 |
|---|---|---|---|---|---|
| [exaone-3.5-7.8b-emt-qlora-awq-v2](https://huggingface.co/hymmmm/exaone-3.5-7.8b-emt-qlora-awq-v2) | EXAONE 3.5 7.8B | QLoRA (EOS 수정) | v2 · 2,001건 | AWQ 4bit | ✅ **권장 · HAPES 앱 기본 모델** |
| [qwen3-8b-emt-qlora-awq-v2](https://huggingface.co/hymmmm/qwen3-8b-emt-qlora-awq-v2) | Qwen3 8B | QLoRA (EOS 수정) | v2 · 2,001건 | AWQ 4bit | ✅ 백본 비교군 |
| [exaone-3.5-7.8b-emt-awq](https://huggingface.co/hymmmm/exaone-3.5-7.8b-emt-awq) | EXAONE 3.5 7.8B | Full FT (BF16) | v2 · 2,001건 | AWQ 4bit | ✅ 학습방식 비교군 (Full vs QLoRA) |
| [exaone-3.5-7.8b-emt-awq-calib](https://huggingface.co/hymmmm/exaone-3.5-7.8b-emt-awq-calib) | EXAONE 3.5 7.8B | Full FT (BF16) | v2 · 2,001건 | AWQ 4bit (도메인 보정) | 🧪 양자화 보정 실험 |
| [exaone-3.5-7.8b-emt-qlora-awq](https://huggingface.co/hymmmm/exaone-3.5-7.8b-emt-qlora-awq) | EXAONE 3.5 7.8B | QLoRA (**EOS 버그**) | v2 · 2,001건 | AWQ 4bit | ⛔ 사용 금지 → v2 사용 |
| [qwen3-8b-emt-qlora-awq](https://huggingface.co/hymmmm/qwen3-8b-emt-qlora-awq) | Qwen3 8B | QLoRA (**EOS 버그**) | v2 · 2,001건 | AWQ 4bit | ⛔ 사용 금지 → v2 사용 |
| [exaone-3.5-7.8b-emt-chatbot](https://huggingface.co/hymmmm/exaone-3.5-7.8b-emt-chatbot) | EXAONE 3.5 7.8B | Full FT (BF16) | v1 · 2,021건 | BF16 원본 | 🗄️ 구버전 (2026-01) |
| [exaone-3.5-7.8b-awq](https://huggingface.co/hymmmm/exaone-3.5-7.8b-awq) | EXAONE 3.5 7.8B | 위 `emt-chatbot`을 양자화 | v1 · 2,021건 | AWQ 4bit | 🗄️ 구버전 (2026-01) |

- **데이터 v1** (2026-01): 초기 대화 데이터셋 2,021건, train/val/test = 70/15/15, 최대 512 토큰.
- **데이터 v2** (2026-06): `final_dataset.jsonl` 2,001건(단일턴 712 · 멀티턴 1,289), train/val = 1,800/201 (주호소 × 대화유형 층화, seed 42), 최대 1,024 토큰(잘림 0%).
- **EOS 버그**: v1 QLoRA 학습용 chat_template에서 `{% generation %}` 블록이 종료 토큰(`[|endofturn|]` / `<|im_end|>`)을 빼먹어, assistant-only loss가 **멈추는 법을 학습하지 못함** → 같은 문장 무한 반복·가짜 대화 턴 생성. v2는 종료 토큰까지 학습 대상에 넣어 재학습했습니다.
- **Full FT vs QLoRA**: Full FT는 epoch 2에서 과적합이 확인됐습니다(학습 데이터 약 1M 토큰으로 7.8B 전체 파라미터를 학습하기엔 데이터가 작음). 그래서 **QLoRA를 메인 방식**으로 채택했고, Full FT는 비교군으로 남겼습니다.
- 모든 AWQ 모델: AutoAWQ, 4-bit, group size 128, zero point, GEMM 커널. 보정(calibration) 데이터는 `-calib`만 한국어 도메인 대화(`final_dataset.jsonl`, 최대 2,048 토큰)이고, 나머지는 AutoAWQ 기본값(pileval, 영어)입니다.

## 주의

연구용 모델입니다. 실제 환자 처치에 단독으로 사용하지 마세요. 약물 용량 등 수치 정보는 반드시 공식 지침으로 확인해야 합니다. HAPES 앱에서는 RAG(현장응급처치 지침·중독·소아 기저질환 문서)와 함께 사용합니다.
