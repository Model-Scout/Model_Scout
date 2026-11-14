---
language:
- ko
- jje
license: apache-2.0
base_model: Qwen/Qwen3-4B
library_name: transformers
pipeline_tag: text-generation
tags:
- jeju
- korean
- dialect
- translation
- sft
- transformers
---

# Alan LLM Jeju Dialect v1 4B

제주어-표준어 양방향 변환 및 제주어 대화/QA를 위한 언어 모델입니다.

## Model Description

이 모델은 **Qwen3-4B**를 기반으로 제주 방언 데이터에 대해 **LoRA fine-tuning**을 수행한 모델입니다. 제주어↔표준어 번역, 제주어 대화 생성, 제주어 QA 등의 태스크에 특화되어 있습니다. 본 모델은 4B 규모의 경량 LLM이 타겟 언어에 특화될 경우, 수십~수백억 파라미터 모델을 능가할 수 있음을 보여줍니다.


- **Developed by:** ESTsoft
- **Model type:** Causal Language Model
- **Language(s):** Korean (ko), Jeju Dialect (ko-jeju)
- **License:** Apache-2.0
- **Finetuned from:** [Qwen/Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B)

## Uses

### Direct Use

- **제주어 → 표준어 번역**: 제주 방언 문장을 표준 한국어로 번역
- **표준어 → 제주어 번역**: 표준 한국어 문장을 제주 방언으로 번역
- **제주어 대화 생성**: 제주어 화자 페르소나로 자연스러운 대화 생성
- **제주어 QA**: 제주어로 질문에 답변

## Bias, Risks, and Limitations

- **성능 비대칭성**: 본 모델은 제주어 생성 및 이해에 최적화되어 있으며, 다른 용도로 활용될 때는 성능이 상대적으로 저하될 수 있습니다.
- **데이터 편향**: 학습 데이터가 특정 연령대, 지역, 주제에 편향되어 있을 수 있습니다.
- **방언 다양성**: 제주도 내에서도 지역별로 방언이 다를 수 있으며, 모든 변형을 완벽히 커버하지 못합니다.
- **Hallucination**: 생성 모델 특성상 사실과 다른 내용을 생성할 수 있습니다.

## How to Get Started

### Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "est-ai/alan-llm-jeju-dialect-v1-4b",
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("est-ai/alan-llm-jeju-dialect-v1-4b")

prompt = "서울 배경으로 헌 매력적인 얘기랑 같이, 서울 특징이랑 매력 좀 소개해 줍서."
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(
    **inputs,
    temperature=0.4,
    repetition_penalty=1.1,
    max_new_tokens=64
)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

### vLLM

```python
from vllm import LLM, SamplingParams

llm = LLM(model="est-ai/alan-llm-jeju-dialect-v1-4b")
sampling_params = SamplingParams(
    temperature=0.4,
    repetition_penalty=1.1,
    max_tokens=128
)

prompts = ["제주어로 변환해주세요. 대한민국은 사계절이 뚜렷해서 계절마다 매력이 달라요."]
outputs = llm.generate(prompts, sampling_params)
```

### Recommended Generation Settings

본 모델은 아래의 추론 세팅에서 가장 안정적인 성능을 보입니다.
특히 반복 표현을 줄이기 위해 repetition penalty 적용을 권장합니다.

**Recommended decoding parameters:**
- `temperature`: **0.4**
- `repetition_penalty`: **1.1**
- `top_p`: 0.9 (optional)
- `max_new_tokens`: 512~1024 (task에 따라 상이)


## Training Details

### LoRA Configuration

| Parameter | Value |
|-----------|-------|
| Base Model | Qwen/Qwen3-4B |
| Training Method | LoRA |
| LoRA Rank (r) | 64 |
| LoRA Alpha | 128 |
| LoRA Target Modules | q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj |
| Max Sequence Length | 4096 |

## Evaluation

### LLM Judge Evaluation (Jeju Dialect)

다양한 베이스라인 모델 및 SOTA 모델과 비교하여 LLM Judge(Gemini-3-Pro-Preview)로 제주어 성능 평가를 진행했습니다. 평가는 pair comparison 방식으로 수행되었습니다.

| Model | Ours Win Rate |
|-------|---------------|
| Qwen3-4B (Base) | **96.2%** |
| gpt-oss-20b | **91.4%** |
| gpt-oss-120b | **89.2%** |
| qwen3-32b | **80.1%** |
| qwen3-235b-a22b | **79.5%** |
| qwen3-30b-a3b | **78.7%** |
| gpt-5-mini | **74.9%** |

본 모델은 제주어 생성에 특화된 Specialist LLM로서, 4B 파라미터 규모임에도 불구하고 20B~120B 규모의 범용 모델보다 우수한 성능을 보입니다.

### Korean Benchmark

제주어 특화 학습 후에도 한국어 일반 성능이 유지되는지 확인하기 위해 한국어 벤치마크를 측정했습니다.

| Model | CLICK | HAERAE | KMMLU | KoBEST |
|-------|-------|--------|-------|--------|
| Qwen3-4B (Base) | 0.5564 | 0.5289 | 0.4582 | 0.5352 |
| **Ours** | **0.5729** | **0.5481** | **0.4683** | **0.5159** |

## Citation

```bibtex
@misc{alan-llm-jeju-dialect-v1-4b,
  author = {ESTsoft},
  title = {Alan LLM Jeju Dialect v1 4B},
  year = {2026},
  publisher = {HuggingFace},
  url = {https://huggingface.co/est-ai/alan-llm-jeju-dialect-v1-4b}
}
```

## Model Card Authors

ESTsoft