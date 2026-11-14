---
base_model: Qwen/Qwen3-4B
library_name: peft
pipeline_tag: text-generation
language: [de, en, es, fr, id, ja, ko, lo, ms, my, pt, ru, ta, th, tl, vi, zh]
tags: [lora, qlora, conversation-title, research-preview]
---

# Qwen3-4B Chat v1 title generator

Research-preview LoRA adapter for short multilingual conversation titles. The
selected adapter is checkpoint step 800 from a QLoRA continuation run. This is
not a medical advice model, a general-purpose chat assistant, or a safety guarantee.

## Files

- Root: PEFT adapter and tokenizer. Requires `Qwen/Qwen3-4B` base weights.
- `ollama/`: merged GGUF Q8_0, Modelfile, local gate wrapper and runtime.
- `benchmark_summary.json`: aggregate benchmark results, without test messages.

Uploading a model does not automatically provide a hosted chat demo. Download
and run locally with Ollama or PEFT. A hosted demo requires a separate serving setup.

## Training

Base: Qwen3-4B. QLoRA 4-bit loading, LoRA rank 32, alpha 64, dropout 0.05,
all-linear targets, learning rate 5e-5, max sequence length 1024, microbatch 4,
gradient accumulation 16, language sampling alpha 0.3, seed 42.
Continuation initialized from the earlier Chat v1 checkpoint-100 adapter; it
was a warm start rather than a full optimizer/scheduler resume. The inherited
configuration also used a previously trained title adapter, so this is not a
clean from-base controlled experiment. Control tokens were disabled.

Current Chat v1 files contain 53,251 train, 866 validation and 825 test records.
Training summary reports 53,253 training examples; this two-record discrepancy
has not been reconciled. The continuation stopped at step 1100 and selected
step 800 (validation chrF++ 52.60). Its recorded wall time was about four hours,
excluding earlier runs and export. Validation generation sampled up to 20
examples per language, so that score is not a full-test or benchmark score.

Training data combines curated title pairs and synthetic medical messages.
The curated portion also contains general-domain conversations. Dataset files
are not distributed here.

## Benchmark

167 items in en/id/th/vi/zh, including 96 red-team items:

| Output | ConstraintScore | chrF++ | Red-team pass |
|---|---:|---:|---:|
| Raw adapter | 98.80% | 30.20 | 97.92% |
| External gate policy | 100% | 30.11 | 100% |

**Important:** language check C1 was skipped for 101 items because FastText was
unavailable during these evaluations. The numbers are incomplete-check results,
not evidence that every language constraint passed. No end-to-end GGUF benchmark
with all checks enabled has been completed. Gate results measure a serving
policy with retry/fallback, not improved model weights. A generic fallback can
pass constraints while being an unhelpful title. These scores are not accuracy
percentages and do not establish superiority over another model.

Raw chrF++ by language: en 32.05, id 32.00, th 23.66, vi 44.81, zh 19.28.
The full 17-language test set and inference latency remain unevaluated here.

## Local Ollama test

Download the `ollama` folder with `huggingface_hub.snapshot_download`, or from
the repository file browser. Install Ollama and Python, then inside that folder:

```powershell
python -m pip install -r requirements.txt
powershell -ExecutionPolicy Bypass -File .\setup_language_check.ps1
powershell -ExecutionPolicy Bypass -File .\install_model.ps1
python .\gated_cli.py --lang vi --message "Tôi bị đau đầu nhẹ ba ngày nay" --json
python .\gated_cli.py --lang vi --mode discreet --message "Tôi lo về xét nghiệm HIV" --json
```

`setup_language_check.ps1` downloads the official FastText language detector
separately. Its license is CC BY-SA 3.0; see
https://fasttext.cc/docs/en/language-identification.html.

Direct Ollama chat executes raw weights. Only `gated_cli.py` applies the external
checks. The CLI's mode changes post-generation checks; it does not inject a
discreet control token into this adapter's prompt. Inspect `source`, `attempts`
and violations; do not judge usefulness by gate pass alone.

## Raw PEFT test (GPU)

Install a suitable GPU PyTorch build, `transformers`, `peft`, and `accelerate`.
Use your actual repository ID in place of `YOUR_REPO_ID`.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

repo_id = "YOUR_REPO_ID"
tokenizer = AutoTokenizer.from_pretrained(repo_id)
base = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen3-4B", torch_dtype=torch.bfloat16, device_map="auto"
)
model = PeftModel.from_pretrained(base, repo_id).eval()
messages = [{"role": "user", "content":
    "Generate a conversation title in Vietnamese for the following message.\n\n"
    "Tôi bị đau đầu nhẹ ba ngày nay"}]
prompt = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True, enable_thinking=False
)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
with torch.inference_mode():
    output = model.generate(**inputs, max_new_tokens=48, do_sample=False)
print(tokenizer.decode(output[0, inputs.input_ids.shape[1]:], skip_special_tokens=True))
```

This is raw inference without gates. The example has been syntax-reviewed, not
executed on a clean third-party GPU environment.

## License and data provenance

The base model is Apache-2.0: https://huggingface.co/Qwen/Qwen3-4B.
An inherited base license does not resolve the provenance and redistribution
conditions of training data or project code. A complete dataset-license and
privacy review is still required before public release. No additional license
grant is asserted for this preview. No training messages, credentials, or
collaborator files are included in the upload manifest.

## Feedback

Report language, descriptive/discreet mode, anonymized input, raw title,
returned gated title, fallback status, runtime and model revision. Do not put
personal health information into public issues. Useful evaluation dimensions
are topic/symptom preservation, no invented diagnosis, brevity, language
correctness and discreet-mode leakage.
