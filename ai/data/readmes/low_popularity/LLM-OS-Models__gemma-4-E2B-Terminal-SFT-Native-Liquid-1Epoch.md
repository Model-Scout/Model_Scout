---
language:
- en
- ko
library_name: transformers
pipeline_tag: text-generation
tags:
- terminal
- sft
- vllm
- tb2-lite
base_model: google/gemma-4-E2B
---

# LLM-OS-Models/gemma-4-E2B-Terminal-SFT-Native-Liquid-1Epoch

터미널 작업 자동화를 위한 Terminal SFT 모델입니다. 입력된 작업/이전 터미널 상태를 보고 다음에 실행할 명령을 JSON 형태로 생성하는 용도로 학습했습니다.

## 모델 요약

- Base model: `google/gemma-4-E2B`
- Training setup: `1 epoch, Gemma native Liquid preprocessing`
- Evaluation snapshot: `2026-05-14 07:17:04 UTC`
- Evaluation result id: `gemma4_e2b_base_native_e1`

## Quickstart

설치와 로그인:

```bash
pip install -U vllm transformers huggingface_hub
huggingface-cli login
```

관련 코드:

- GitHub: https://github.com/LLM-OS-Models/Terminal
- vLLM 평가 실행: `tb2_lite/scripts/replay_eval.py`
- chat template/fallback 생성: `tb2_lite/scripts/prompt_builder.py`
- JSON/command 채점: `tb2_lite/scripts/replay_metrics.py`

vLLM 직접 실행 예시. 평가 코드와 동일하게 chat template을 우선 사용하고, template이 없으면 ChatML/Gemma fallback을 사용합니다.

```python
from transformers import AutoTokenizer
from vllm import LLM, SamplingParams

model_id = "LLM-OS-Models/gemma-4-E2B-Terminal-SFT-Native-Liquid-1Epoch"
tp = 1

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
llm = LLM(
    model=model_id,
    tokenizer=model_id,
    trust_remote_code=True,
    dtype="bfloat16",
    tensor_parallel_size=tp,
    max_model_len=49152,
    gpu_memory_utilization=0.92,
)

messages = [
    {"role": "system", "content": "You are a terminal automation assistant. Return JSON only."},
    {"role": "user", "content": "Inspect the current directory and list Python files."},
]

def render_chatml(messages):
    parts = []
    for message in messages:
        role = "assistant" if message["role"] == "assistant" else message["role"]
        if role == "tool":
            role = "user"
        parts.append(f"<|im_start|>{role}\n{message['content']}<|im_end|>\n")
    parts.append("<|im_start|>assistant\n")
    return "".join(parts)

def render_gemma4_turn(messages, empty_thought_channel=False):
    parts = ["<bos>"]
    for message in messages:
        role = "model" if message["role"] == "assistant" else message["role"]
        if role == "tool":
            role = "user"
        parts.append(f"<|turn>{role}\n{message['content'].strip()}<turn|>\n")
    parts.append("<|turn>model\n")
    if empty_thought_channel:
        parts.append("<|channel>thought\n<channel|>")
    return "".join(parts)

def render_prompt(model_id, tokenizer, messages):
    model_key = model_id.lower()
    if "gemma-4" in model_key:
        try:
            return tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True,
                enable_thinking=False,
            )
        except Exception:
            return render_gemma4_turn(
                messages,
                empty_thought_channel=("26b" in model_key or "31b" in model_key),
            )
    try:
        return tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    except Exception:
        return render_chatml(messages)

prompt = render_prompt(model_id, tokenizer, messages)
sampling = SamplingParams(
    temperature=0.0,
    top_p=1.0,
    max_tokens=1024,
    repetition_penalty=1.0,
)
outputs = llm.generate([prompt], sampling_params=sampling)
print(outputs[0].outputs[0].text)
```

권장 출력 형식:

```json
{
  "analysis": "brief reasoning about the next terminal action",
  "plan": "short execution plan",
  "commands": [
    {"keystrokes": "ls -la\n", "duration": 0.1}
  ],
  "task_complete": false
}
```

평가와 동일한 replay 명령:

```bash
python tb2_lite/scripts/replay_eval.py \
  --model LLM-OS-Models/gemma-4-E2B-Terminal-SFT-Native-Liquid-1Epoch \
  --model-short gemma4_e2b_base_native_e1 \
  --eval-path tb2_lite/data/replay_full.jsonl \
  --output-dir /home/work/.data/tb2_lite_eval/corrected_readme_models_vllm \
  --dtype bfloat16 \
  --tp 1 \
  --max-model-len 49152 \
  --max-tokens 1024 \
  --temperature 0.0 \
  --top-p 1.0 \
  --gpu-memory-utilization 0.92 \
  --thinking-mode off \
  --strip-thinking-history auto \
  --gemma4-empty-thought-channel auto \
  --language-model-only
```

- 기본 권장 tensor parallel: `1`. OOM이면 `--tp`와 `tensor_parallel_size`를 2/4/8로 올리세요.
- corrected TB2-lite 평가는 `temperature=0.0`, `top_p=1.0`, `max_tokens=1024`로 고정했습니다.
- Gemma 4는 JSON 출력을 위해 `enable_thinking=False`를 사용하고, 26B/31B 계열은 평가 코드에서 empty thought channel 처리를 자동 적용합니다.

## 평가 결과

평가는 corrected TB2-lite replay set에서 vLLM으로 수행했습니다. 순위 점수는 `100 * avg_command_f1`만 사용하고, `first_cmd_exact_pct`는 보조 지표로만 봅니다.

- Rank: `8 / 8`
- Score: `11.35`
- Command F1: `0.1135`
- Command precision: `0.1767`
- Command recall: `0.1191`
- First command exact: `6.6%`
- Valid JSON: `7.3%`
- Steps / tasks: `303 / 50`
- Sec/step: `0.219`
- Load time: `45.3s`
- Template status: `model_specific_or_mixed`
- Rank eligible: `True`
- Eval timestamp: `2026-05-09T00:22:14.401669`
- 현재 집계된 평가 결과 수: `8`

Prompt/template audit:

```json
{
  "template_status": "model_specific_or_mixed",
  "rank_eligible": true,
  "steps": 303,
  "tasks": 50
}
```

## 장점

- 특정 크기/가속 경로에서 비용 대비 빠른 추론을 기대할 수 있습니다.
- 잘못된 명령을 많이 내기보다 보수적으로 맞는 명령을 내는 경향이 있습니다.

## 모델군 해석

- 이 repo는 Gemma 4 전용 chat template, thinking history 제거, assistant JSON-only target, base 모델 template 주입 정책으로 다시 학습한 native Liquid 결과입니다.
- 기존 Gemma SFT의 낮은 점수는 template/target 포맷 충돌과 일부 checkpoint/export 문제를 포함했으므로, 이 native 결과를 새 기준으로 봐야 합니다.
- 속도는 `0.219` sec/step 수준으로 빠른 편입니다.
- RL 후보성: 현재 점수만으로는 주력 후보보다 보조/비교군에 가깝습니다.

## 한계와 주의사항

- recall이 상대적으로 낮아 필요한 명령 일부를 빠뜨릴 수 있습니다.
- JSON 형식 실패가 있어 실행 전에 파싱 검증/재시도가 필요합니다.
- Gemma 계열은 학습/평가 chat template 불일치에 민감하므로 vLLM chat_template 경로로만 비교해야 합니다.
- 이 모델은 자동 터미널 조작 보조용 SFT 모델이며, 일반 대화/범용 추론 성능을 보장하지 않습니다.
- 생성 명령은 실제 실행 전에 sandbox, allowlist, human review 같은 안전장치를 거쳐야 합니다.

## 해석 메모

TB2-lite 점수는 일반 지능 벤치마크가 아니라 터미널 next-action JSON 재현 능력을 측정합니다. 따라서 모델 크기, chat template 일치, assistant-only masking, tokenizer, 학습 데이터 holdout 여부가 모두 점수에 영향을 줍니다.

README.md와 MODEL_EVALUATION_REPORT.md의 값이 더 최신이면 해당 값을 우선 확인하세요. 이 모델카드는 완료된 평가 JSON을 기준으로 개별 저장소에 빠르게 반영한 스냅샷입니다.
