---
license: apache-2.0
language:
  - ko
  - en
tags:
  - medical
  - clinical
  - korean
  - healthcare
  - mixture-of-experts
  - conversational
  - tool-use
  - sft
base_model:
  - trillionlabs/Gravity-30B-A5B-Base
base_model_relation: finetune
library_name: transformers
pipeline_tag: text-generation
---

<p align="center">
  <img src="banner.png" alt="L1-30B-A5B" style="width: 80%;">
</p>

# LearningUnit 2.0 (L1-30B-A5B)

**L1-30B-A5B** is the Korean-locale medical foundation model from [Lunit](https://www.lunit.io)
and Lunit Consortium. It is the 30B member of the L1 family, post-trained directly from
[Gravity-30B-A5B-Base](https://huggingface.co/trillionlabs/Gravity-30B-A5B-Base), a sparse
Mixture-of-Experts model developed by Trillion Labs and the Lunit Consortium.

L1-30B-A5B preserves the base model's `GravityMoEForCausalLM` architecture. GravityMoE is
weight- and attention-compatible with DeepSeek-V3 while retaining its own Hugging Face
architecture name and remote-code registration. Load the model with `trust_remote_code=True`.

* 🇰🇷 Korean clinical locale, trained natively — not machine-translated from English
* ⚡ 5.34B active of 29.56B total (sparse MoE)
* 💭 Reasons in `<think>...</think>` before answering — budget 2048+ output tokens
* 🔧 Multi-turn retrieval and tool-call trajectories with citation-grounded answers
* 📏 131,072-token context

| | | | |
|:---|:---|:---|:---|
| Architecture | GravityMoE (sparse MoE + MLA) | Layers | 52 (2 dense, 50 MoE) |
| Total / active params | 29.56B / 5.34B | Hidden size | 2048 |
| Routed experts | 64, top-8 | MoE intermediate | 1408 |
| Shared experts | 1 | Attention / KV heads | 16 / 16 |
| Context | 131,072 | Vocab | 151,552 |
| Tokenizer | GLM-4.5 | Precision | bf16 |

## 📊 Benchmark

All numbers were produced with [CoEval](https://github.com/lunit-io/CoEval), Lunit's
open-source medical LLM evaluation framework.

<p align="center">
  <img src="efficiency.png" alt="Chat quality vs MCQA, bubble area = active parameters" style="width: 100%;">
</p>

### Knowledge & reasoning

| Model | W.Avg | [PubMedQA](https://huggingface.co/datasets/qiaojin/PubMedQA) | [AttrBench](https://huggingface.co/datasets/osunlp/AttributionBench) | [MedQA](https://huggingface.co/datasets/GBaker/MedQA-USMLE-4-options) | [CareQA](https://huggingface.co/datasets/HPAI-BSC/CareQA) | [HeadQA](https://huggingface.co/datasets/alesi12/head_qa_v2) | [MedMCQA](https://huggingface.co/datasets/lighteval/med_mcqa) | [MMLU-Pro (Health)](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro) | [M-ARC](https://huggingface.co/datasets/mkieffer/M-ARC) | [MedExQA](https://huggingface.co/datasets/bluesky333/MedExQA) | [MetaMedQA](https://huggingface.co/datasets/maximegmd/MetaMedQA) | [MedHallu](https://huggingface.co/datasets/UTAustin-AIHealth/MedHallu) | [MedCalc](https://huggingface.co/datasets/ncbi/MedCalc-Bench) | [KorMedMCQA](https://huggingface.co/datasets/sean0042/KorMedMCQA) | [MedBullets 4-opt](https://huggingface.co/datasets/mkieffer/Medbullets) | [MedBullets 5-opt](https://huggingface.co/datasets/mkieffer/Medbullets) | [MedXpertQA-R](https://huggingface.co/datasets/TsinghuaC3I/MedXpertQA) | [MedXpertQA-U](https://huggingface.co/datasets/TsinghuaC3I/MedXpertQA) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [**L1-30B-A5B**](https://huggingface.co/learning-unit/L1-30B-A5B) | 83.76 | **82.20** | 76.31 | 92.30 | 92.55 | 89.66 | 76.45 | 79.34 | 42.00 | 86.17 | **86.23** | 82.71 | 81.55 | 89.53 | 84.74 | 79.87 | 43.10 | 37.86 |
| [GPT-OSS-120B](https://huggingface.co/openai/gpt-oss-120b) | 79.99 | 78.00 | 76.10 | 91.10 | 91.00 | 88.40 | 74.80 | 74.60 | 40.00 | 84.10 | 76.50 | 83.50 | 30.30 | 84.80 | 84.70 | 82.10 | 35.60 | 32.90 |
| GPT-5.6-SOL | 87.85 | 78.60 | 74.95 | 96.00 | 95.60 | 92.70 | 84.10 | 83.10 | 74.00 | 87.10 | 81.40 | 94.80 | 80.09 | 97.71 | 91.60 | 87.70 | 58.10 | 56.70 |
| GPT-5.6-TERRA | 86.97 | 78.20 | 75.44 | 93.80 | **95.60** | 92.50 | 83.00 | 80.70 | 72.00 | 87.00 | 81.90 | 92.90 | **82.55** | 94.18 | 89.90 | 85.10 | 52.20 | 50.90 |
| GPT-5.6-LUNA | 85.36 | 76.00 | 75.21 | 94.20 | 94.90 | 91.20 | 81.80 | 80.10 | 68.00 | 85.40 | 79.80 | 89.00 | 79.27 | 93.79 | 89.00 | 84.10 | 45.10 | 45.80 |
| [KIMI-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6) | 84.51 | 80.20 | 71.84 | 94.11 | 92.07 | 90.64 | 82.00 | 81.91 | 74.00 | 85.64 | 82.45 | 76.37 | 61.55 | 93.52 | 86.69 | 82.14 | 48.52 | 48.22 |
| [QWEN3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) | 81.06 | 78.80 | 75.90 | 89.32 | 90.55 | 87.87 | 76.14 | 77.87 | 55.00 | 82.98 | 76.47 | 77.50 | 70.82 | 86.34 | 81.17 | 78.90 | 39.49 | 36.50 |
| [QWEN3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) | 82.82 | 77.00 | 71.24 | 93.72 | 92.19 | 89.66 | 76.45 | 80.81 | 67.00 | 85.11 | 79.97 | 86.19 | 63.00 | 87.80 | 87.34 | 83.12 | 43.58 | 39.90 |
| [QWEN3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B) | 76.07 | 76.40 | 55.68 | 87.80 | 86.40 | 84.00 | 74.40 | 73.00 | 59.00 | 80.20 | 73.90 | 37.50 | 75.82 | 85.60 | 79.20 | 79.50 | 35.90 | 35.30 |
| [DEEPSEEK-V4-PRO-0813](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813) | 86.39 | 76.60 | 75.92 | 94.97 | 95.48 | 92.61 | 83.43 | 82.52 | **80.00** | **87.55** | 79.68 | 72.14 | 55.09 | 95.68 | 88.31 | 86.04 | 49.87 | 48.05 |
| [MEDGEMMA-27B](https://huggingface.co/google/medgemma-27b-text-it) | 72.74 | 73.40 | 74.80 | 84.40 | 85.00 | 83.80 | 71.90 | 73.00 | 48.00 | 80.30 | 69.60 | 81.40 | 24.10 | 56.40 | 73.70 | 68.80 | 19.10 | 20.50 |
| [GEMMA4-31B](https://huggingface.co/google/gemma-4-31B-it) | 80.25 | 77.60 | **76.98** | 87.40 | 87.90 | 85.90 | 73.00 | 77.90 | 79.00 | 82.00 | 76.80 | 79.60 | 53.10 | 86.10 | 76.00 | 74.44 | 54.60 | 48.90 |
| [GEMMA4-26B-A4B](https://huggingface.co/google/gemma-4-26B-A4B-it) | 75.86 | 76.40 | 72.00 | 81.80 | 84.50 | 82.30 | 67.30 | 73.50 | 67.00 | 78.30 | 71.50 | 86.50 | 45.60 | 80.70 | 73.70 | 67.50 | 45.10 | 39.20 |

### Chat quality

<p align="center">
  <img src="healthbench.png" alt="HealthBench Main / Professional / Consensus" style="width: 100%;">
</p>

| Model | [HealthBench Main](https://github.com/openai/simple-evals) | [HealthBench Professional](https://github.com/openai/simple-evals) | [HealthBench Consensus](https://github.com/openai/simple-evals) |
|:---|:---:|:---:|:---:|
| [**L1-30B-A5B**](https://huggingface.co/learning-unit/L1-30B-A5B) | 52.81 | 40.01 | 90.15 |
| [GPT-OSS-120B](https://huggingface.co/openai/gpt-oss-120b) | 50.49 | 23.77 | 78.72 |
| GPT-5.6-SOL | 56.59 | 63.18 | 84.98 |
| GPT-5.6-TERRA | 52.78 | 59.36 | 84.55 |
| GPT-5.6-LUNA | 50.73 | 55.07 | 83.60 |
| [KIMI-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6) | **56.71** | 43.68 | **90.68** |
| [QWEN3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) | 55.39 | 41.91 | 88.29 |
| [QWEN3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) | 52.71 | 31.42 | 84.78 |
| [QWEN3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B) | 51.28 | 43.55 | 86.88 |
| [DEEPSEEK-V4-PRO-0813](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813) | 51.23 | 33.99 | 87.43 |
| [MEDGEMMA-27B](https://huggingface.co/google/medgemma-27b-text-it) | 43.36 | 11.93 | 82.18 |
| [GEMMA4-31B](https://huggingface.co/google/gemma-4-31B-it) | 46.72 | 31.92 | 87.60 |
| [GEMMA4-26B-A4B](https://huggingface.co/google/gemma-4-26B-A4B-it) | 46.66 | 31.19 | 86.85 |

> [!NOTE]
> HealthBench rubric items are graded by an LLM judge: **`zai-org/GLM-5.2-FP8`**, thinking
> disabled (`chat_template_kwargs.enable_thinking: false`). GLM was chosen because it grades
> more strictly than the GPT-family judges and keeps a GPT model from judging its own family.

## 🚀 Quickstart

### ⚠️ Required settings

**`repetition_penalty = 1.05`** — at the default `1.0` the model degenerates into repeated
phrases on long clinical answers. It ships in `generation_config.json`, but any client that
sets its own sampling parameters overrides that. It is **not** an OpenAI API parameter —
through the OpenAI SDK it must go in `extra_body` or it is dropped silently.

**System prompt** — the identity line the model was aligned on, and the one every benchmark
number below used. Task-specific prompts go after it, not instead of it.

```python
client.chat.completions.create(
    model="learning-unit/L1-30B-A5B",
    messages=[{"role": "system", "content": "You are Chain-of-Evidence, a medical AI assistant developed by Lunit."}, *messages],
    temperature=0.0,          # 0.0 for benchmarks and deterministic clinical tasks
    top_p=1.0,
    max_tokens=32768,
    extra_body={"repetition_penalty": 1.05},
)
```

### SGLang

Native GravityMoE support is being upstreamed to SGLang. Until that work is merged, use
Trillion Labs' [`sglang-gravity`](https://github.com/trillion-labs/sglang-gravity) fork,
which registers `GravityMoEForCausalLM` on SGLang's DeepSeek-V3-compatible implementation.

```bash
pip install "sglang[all] @ git+https://github.com/trillion-labs/sglang-gravity.git#subdirectory=python"
```

Launch the server with the same GravityMoE deployment path as the base model, substituting
the L1 checkpoint:

```bash
python3 -m sglang.launch_server \
  --model-path learning-unit/L1-30B-A5B \
  --host 0.0.0.0 --port 30000 \
  --tp 4 --context-length 131072 \
  --trust-remote-code --dtype bfloat16
```

### Transformers

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

name = "learning-unit/L1-30B-A5B"
model = AutoModelForCausalLM.from_pretrained(name, torch_dtype=torch.bfloat16,
                                             device_map="auto", trust_remote_code=True)
tok = AutoTokenizer.from_pretrained(name, trust_remote_code=True)

messages = [
    {"role": "system", "content": "You are Chain-of-Evidence, a medical AI assistant developed by Lunit."},
    {"role": "user", "content": "성인 환자에서 Obstructive sleep apnea가 의심될 때, 진단을 위해 어떤 검사를 시행하고 어느 전문과로 의뢰하는 것이 적합한가요?"},
]
inputs = tok([tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)],
             return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=2048, do_sample=True, temperature=0.7,
                     repetition_penalty=1.05)
print(tok.decode(out[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
```

### 🔧 Tool use

Tool calling was trained end-to-end against **Lunit's own RAG harness** — the
Chain-of-Evidence MCP servers, with tool schemas frozen at a snapshot. Two consequences:

- Handed a tool that looks nothing like a retrieval tool, the model often answers from
  parametric knowledge instead of calling it. Force it with `tool_choice: "required"`, or
  keep your schema close to what it knows: a query string plus optional filters, returning
  ranked passages with stable ids.
- Citation markers index into what the retrieval tool returned that turn. With no retrieval
  tool attached they have nothing to point at.

## 💬 Examples

Representative prompts per capability. 🔧 expects a retrieval tool call first.

**🇰🇷 Korean clinical practice**

- *국시원 국가고시* — 65세 남성, 3개월간 기침과 체중 감소, 30갑년 흡연력, 흉부 X선상 우상엽 3 cm 결절. 가장 먼저 시행할 검사는? ① 흉부 CT ② 객담 세포검사 ③ 기관지내시경 ④ PET-CT ⑤ 경피적 세침흡인생검
- *KTAS 응급 분류* — 이 환자의 KTAS 중증도(1–5)를 분류하세요. **[환자]** 78세 여성, 22시경 갑자기 좌측 안면마비와 구음장애, 두통 호소, 고혈압 병력, BP 172/88, HR 92, SpO₂ 98%, 의식 명료.
- *응급실 감별진단* — 54세 남성, 2시간 전 시작된 상복부 통증과 식은땀, 30갑년 흡연·당뇨, BP 148/92 HR 104, 심전도 미확인. 놓치면 안 되는 진단부터 우선순위로.
- *청구 관련 업무* 🔧 — 만성 특발성 두드러기에 오말리주맙 급여 인정기준과 인정 투여 기간을 근거 고시와 함께. / 프레가발린 75 mg 처방에 상병이 M54.5 하나인 청구 건, 누락된 인정상병이 있는지.
- *의료 법령* 🔧 — 진료기록부 보존기간과, 전자의무기록을 외부 클라우드에 보관할 때의 요건을 근거 조문과 함께.

**🧠 Clinical reasoning**

- *Differential diagnosis* — 45F with lupus nephritis on mycophenolate and prednisone, fever, dry cough, bilateral ground-glass opacities, CD4 180. Differential and workup?
- *ADR causality* — 80세 여성, moxifloxacin 400 mg IV 투여 중 전신 소양감 발생, 중단 후 호전, 재투여 없음. WHO-UMC 기준으로 인과관계 평가.
- *Clinical calculation* — 72세 남성, 68 kg, Cr 1.4 mg/dL. Cockcroft-Gault 로 CrCl 계산 후 아픽사반 용량 조정 필요 여부.

**📚 Evidence & communication**

- *Literature Q&A* 🔧 — Does perioperative continuation of SGLT2 inhibitors increase euglycemic DKA risk? Cite every claim.
- *Guideline Q&A* 🔧 — 2형 당뇨에서 SGLT2 억제제를 1차 약제로 고려할 수 있는 조건을 지침 근거와 함께.
- *Patient education* — I use insulin daily. How should I store it at home?
- *Clinical documentation* — Overnight progress note from labs, vitals, and a stable nursing report.

## ⚠️ Limitations

- **Not a substitute for professional medical judgment.** Outputs may be wrong, incomplete,
  or outdated, and need review by a qualified clinician.
- **Knowledge is frozen at the training cutoff** — guidelines, 고시, and drug approvals move.
  Korean reimbursement answers in particular must be re-verified against current notices.
- **Thinking costs tokens.** `<think>` reasoning raises latency and token use.
- **Tool calling is harness-shaped.** Quality degrades the further your tool schemas drift
  from the ones it was trained on. See **Tool use** above.

## 📝 Citation

```bibtex
@misc{lunit2026l1_30b,
  title={L1-30B-A5B: A Korean-Locale Clinical Language Model by Lunit},
  author={Lunit},
  year={2026},
  url={https://huggingface.co/learning-unit/L1-30B-A5B}
}
```

## 🤝 Acknowledgements

This work was supported by the Domain-Specific Foundation Model Project (인공지능 특화 파운데이션 모델 프로젝트), funded by the Ministry of Science and ICT (과학기술정보통신부) and managed by the National IT Industry Promotion Agency (NIPA).

L1-30B-A5B is a collaborative effort by the following consortium members:

**Industry**
- Lunit
- Trillion Labs
- SK Biopharmaceuticals
- Kakao Healthcare
- AIGEN Sciences
- D-Circle
- Rebellions
- Standigm

**Academia**
- Prof. Choi Yun-jae's Lab from KAIST
- Prof. Hong Seung-hoon's Lab from KAIST
- Prof. Jung Yu-seong's Lab from SNU
- Prof. Kim Hyun-woo's Lab from KAIST
- Prof. Kim Tae-gyun's Lab from KAIST
- Prof. Ye Jong-cheol's Lab from KAIST

**Hospitals**
- NHIS Ilsan Hospital
- Ewha Womans University Seoul Hospital
- Keimyung University Dongsan Medical Center
- Konyang University Hospital
- Korea University Research & Business Foundation
- Kyung Hee University Hospital at Gangdong
- Kyung Hee University Medical Center
- Pusan National University Yangsan Hospital
- Yongin Severance Hospital

<p align="center">
  <img src="consortium.png" alt="Consortium Members" style="width: 80%;">
</p>

## 📄 License

This model is licensed under the [Apache 2.0 License](LICENSE).

## 📬 Contact

- Taesoo Kim (김태수) — [taesoo.kim@lunit.io](mailto:taesoo.kim@lunit.io)
- Donggeun Yoo (유동근) — [dgyoo@lunit.io](mailto:dgyoo@lunit.io)
