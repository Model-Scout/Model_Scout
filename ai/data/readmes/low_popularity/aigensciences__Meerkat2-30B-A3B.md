---
license: cc-by-nc-4.0
base_model: Qwen/Qwen3-30B-A3B
base_model_relation: finetune
language:
  - en
  - ko
library_name: transformers
pipeline_tag: text-generation
tags:
  - medical
  - clinical-reasoning
  - korean
  - bilingual
  - reasoning
  - chain-of-thought
  - kmle
  - usmle
  - conversational
---

# Meerkat2

**Meerkat2** is a family of open medical reasoning models for **Korean and English clinical contexts**, released at 14B, 32B, and 30B-A3B (MoE) scales. The models are trained on an 837K-example mixture including carefully curated question-answer pairs from Korean medical statutes.

Two design choices drive the results:

* **Statute-grounded synthesis.** Legal knowledge depends on accurate memorization and requires high fidelity, which teacher distillation does not guarantee. Generating QA pairs directly from 12 Korean medical statutes substantially outperforms distillation on the legal subsets of KorMedMCQA.
* **Verbosity-Decoupled Distillation (VDD).** Long teacher rationales transfer reasoning ability well, but the student also inherits the teacher's verbose response style. VDD attaches an explicit verbosity instruction to the verbose training examples, so length is attributed to the prompt constraint rather than to the reasoning trajectory.

📄 **Paper**: Meerkat2: Bridging Global Reasoning and Local Knowledge for Efficient Medical AI \
🤗 **Collection**: [aigensciences/meerkat2](https://huggingface.co/collections/aigensciences/meerkat2)

---

## Model Family

| Model | Total Params | Active Params | Repository |
| --- | --- | --- | --- |
| Meerkat2-14B | 14B | 14B | `aigensciences/Meerkat2-14B` |
| Meerkat2-30B-A3B | 30B (MoE) | 3B | `aigensciences/Meerkat2-30B-A3B` |
| Meerkat2-32B | 32B | 32B | `aigensciences/Meerkat2-32B` |

All three share the same training mixture and recipe. Pick 30B-A3B if inference cost matters most, since it reaches Korean licensing accuracy comparable to Qwen3-235B-A22B while activating only 3B parameters. Pick 32B for the highest overall accuracy in the family, and 14B for the smallest memory footprint.

---

## Quick Start

### Transformers

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "aigensciences/Meerkat2-30B-A3B"  # or Meerkat2-14B, Meerkat2-32B

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(
    checkpoint,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

messages = [
    {
        "role": "system",
        "content": "Answer the following multiple choice question. Conclude with: 'ANSWER: (A/B/C/D)'",
    },
    {
        "role": "user",
        "content": "48세 남자가 3시간 전부터 시작된 명치 통증으로 왔다. ...",
    },
]

inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    enable_thinking=True,   # set False for Instant mode
    return_tensors="pt",
    return_dict=True,
).to(model.device)

outputs = model.generate(**inputs, max_new_tokens=2048)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

### vLLM

```bash
pip install vllm
vllm serve "aigensciences/Meerkat2-30B-A3B" --reasoning-parser qwen3
```

```bash
curl -X POST "http://localhost:8000/v1/chat/completions" \
  -H "Content-Type: application/json" \
  --data '{
    "model": "aigensciences/Meerkat2-30B-A3B",
    "messages": [{"role": "user", "content": "국내 의료법상 진료기록부 보존기간은?"}]
  }'
```

### SGLang

```bash
pip install sglang
python3 -m sglang.launch_server \
    --model-path "aigensciences/Meerkat2-30B-A3B" \
    --reasoning-parser qwen3 \
    --host 0.0.0.0 --port 30000
```

---

## Usage Notes

### Thinking and Instant modes

Meerkat2 inherits the Qwen3 hybrid thinking interface. Training applied loss masking to user prompts and to empty thought blocks, so the model initiates reasoning by default unless reasoning is explicitly disabled.

* **Thinking mode**: the model writes its reasoning inside `<think>` tags before answering. Use this for exam-style questions, differential diagnosis, and any case where the chain of reasoning should be inspectable.
* **Instant mode**: pass `enable_thinking=False` for a direct answer. Instant mode is still substantially stronger than the corresponding Qwen3 base model, so it is a reasonable default for latency-sensitive workflows.

### Response language

The model was trained with both English and Korean rationales for the same questions. State the desired output language in the system prompt, for example `Respond only in English.` or `한국어로만 응답하세요.` Unlike the base models, Meerkat2 does not lose accuracy when answering in Korean.

### Reproducing the reported numbers

Evaluations were run with [EvalScope](https://github.com/modelscope/evalscope) using the system prompt shown in the Transformers snippet above. Prompt formulation is not critical: the accuracy and token-efficiency ranking holds across minimal, EvalScope-style, and Meerkat1-style system prompts, and across three decoding seeds.

### Statutes covered

Medical Service Act, Pharmaceutical Affairs Act, Regional Public Health Act, National Health Insurance Act, Narcotics Control Act, Framework Act on Health and Medical Services, National Health Promotion Act, Infectious Disease Control and Prevention Act, Quarantine Act, Prevention of Acquired Immunodeficiency Syndrome Act, Emergency Medical Service Act, Blood Management Act.

### Decontamination

Training data was checked against the MedQA and KorMedMCQA test sets for shared 10-grams, following the criterion used in prior work. No 10-gram overlap was found between any training and test example.

---

## Intended Use and Limitations

Meerkat2 is intended for **research and educational use**. Its outputs are not a substitute for professional medical diagnosis or treatment, and clinical decisions should not be made on the basis of model responses without expert verification.

Known limitations:

* Legal knowledge reflects the Korean statutes as of the data collection date. Statutes are amended, so answers about legal detail should be verified against the current text.
* Localization is specific to Korean clinical and legal contexts. Applying the same recipe to another jurisdiction would require building an analogous legal corpus and clinical benchmark.
* Human evaluation by licensed clinicians was conducted at limited scale. Broader physician studies would be needed to fully characterize clinical behavior.
* General-domain capability is preserved but not improved. Some general benchmark scores sit slightly below the corresponding Qwen3 base model.

Training data comes from publicly available benchmarks, instruction-tuning datasets, and Korean statutes accessible through public legal information services. No identifiable patient records were used. A refusal subset is included in the training mixture to reject harmful prompts, with the resulting behavior reported on MedSafetyBench.

---

## License

Meerkat2 model weights are released under the [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) license. Meerkat2 is fine-tuned from the Qwen3 family (Qwen3-14B, Qwen3-30B-A3B, and Qwen3-32B), which is licensed under Apache 2.0.

### Commercial Use and Meerkat2-Pro

Commercial use of Meerkat2 requires a separate license from AIGEN Sciences.

For hospitals and enterprises, AIGEN Sciences also offers **Meerkat2-Pro**, an enterprise edition with enhanced performance.

For commercial licensing or Meerkat2-Pro inquiries, please contact [sanghoon.lee@aigensciences.com](mailto:sanghoon.lee@aigensciences.com).

---

## Citation

```bibtex
@article{park2026meerkat2,
  title={Meerkat2: Bridging Global Reasoning and Local Knowledge for Efficient Medical AI},
  author={Park, Jungwoo and Hwang, Hyeongsoon and Lee, Sanghoon and Kang, Jaewoo},
  year={2026}
}
```
