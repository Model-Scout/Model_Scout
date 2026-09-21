---
language:
- ko
- en
license: apache-2.0
base_model: Qwen/Qwen2.5-3B-Instruct
tags:
- qwen
- qwen2.5
- korean
- merged
- gguf
- conversational
library_name: transformers
pipeline_tag: text-generation
datasets:
- MyeongHo0621/smol-koreantalk
model-index:
- name: Qwen2.5-3B-Korean
  results: []
---

# Qwen2.5-3B-Korean

## Model Description

**Qwen2.5-3B-Korean**은 [Qwen/Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct)를 한국어로 파인튜닝한 **Merged 모델**입니다.

이 리포지토리는 **LoRA 어댑터가 이미 병합된 완전한 모델**과 **GGUF 파일**을 제공합니다.

> **PEFT/LoRA 어댑터**가 필요하신 경우: [MyeongHo0621/Qwen2.5-3B-Korean-QLoRA](https://huggingface.co/MyeongHo0621/Qwen2.5-3B-Korean-QLoRA)

### 🎯 Key Features

- 🇰🇷 **Korean Optimization**: 200,000개 고품질 한국어 대화 데이터로 학습
- 📦 **Ready-to-Use**: LoRA 병합 완료, 즉시 사용 가능
- 🚀 **Multi-Format**: Safetensors (루트) + GGUF (gguf/)
- 💻 **All Frameworks**: Transformers, vLLM, SGLang, Ollama, Llama.cpp
- ⚖️ **Apache 2.0**: 상업적 사용 가능

---

## 📦 Available Formats

| Format | Path | Use Case | Size |
|--------|------|----------|------|
| **Safetensors** | `/` (루트) | Transformers, vLLM, SGLang | ~6GB |
| **GGUF Q4_K_M** | `gguf/qwen25-3b-korean-Q4_K_M.gguf` | Ollama, Llama.cpp (권장) | ~2GB |
| **GGUF Q5_K_M** | `gguf/qwen25-3b-korean-Q5_K_M.gguf` | 고품질 | ~2.5GB |
| **GGUF Q8_0** | `gguf/qwen25-3b-korean-Q8_0.gguf` | 최고 품질 | ~3.5GB |
| **GGUF F16** | `gguf/qwen25-3b-korean-F16.gguf` | 벤치마크 | ~6GB |

---

## 🚀 Quick Start

### 1️⃣ Transformers (가장 간단)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

# 모델 로딩 (Merged 모델)
model = AutoModelForCausalLM.from_pretrained(
    "MyeongHo0621/Qwen2.5-3B-Korean",
    torch_dtype="auto",
    device_map="auto"
)

tokenizer = AutoTokenizer.from_pretrained("MyeongHo0621/Qwen2.5-3B-Korean")

# 채팅 템플릿 사용
messages = [
    {"role": "system", "content": "You are a helpful Korean assistant."},
    {"role": "user", "content": "한국의 수도는 어디인가요?"}
]

text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)

outputs = model.generate(**inputs, max_new_tokens=512, temperature=0.7)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

### 2️⃣ vLLM (Production Serving)

```python
from vllm import LLM, SamplingParams

# Merged 모델 로딩
llm = LLM(
    model="MyeongHo0621/Qwen2.5-3B-Korean",
    quantization="bitsandbytes",  # 옵션: 4-bit 양자화
    gpu_memory_utilization=0.6
)

prompts = ["한국의 수도는 어디인가요?"]
params = SamplingParams(temperature=0.7, max_tokens=512)

outputs = llm.generate(prompts, params)
for output in outputs:
    print(output.outputs[0].text)
```

**Server Mode:**

```bash
vllm serve MyeongHo0621/Qwen2.5-3B-Korean \
    --quantization bitsandbytes \
    --port 8000
```

---

### 3️⃣ SGLang (Fastest)

```python
import sglang as sgl

runtime = sgl.Runtime(
    model_path="MyeongHo0621/Qwen2.5-3B-Korean",
    quantization="bitsandbytes"
)

sgl.set_default_backend(runtime)

@sgl.function
def chat(s, prompt):
    s += sgl.user(prompt)
    s += sgl.assistant(sgl.gen("response", max_tokens=512))

state = chat.run(prompt="한국의 수도는?")
print(state["response"])
```

---

### 4️⃣ Ollama (Local Desktop)

```bash
# 1. GGUF 다운로드
huggingface-cli download MyeongHo0621/Qwen2.5-3B-Korean \
    gguf/qwen25-3b-korean-Q4_K_M.gguf \
    --local-dir ./

# 2. Modelfile 생성
cat > Modelfile << 'EOF'
FROM ./gguf/qwen25-3b-korean-Q4_K_M.gguf

TEMPLATE """<|im_start|>system
You are a helpful Korean assistant.<|im_end|>
<|im_start|>user
{{ .Prompt }}<|im_end|>
<|im_start|>assistant
"""

PARAMETER stop "<|im_start|>"
PARAMETER stop "<|im_end|>"
PARAMETER temperature 0.7
EOF

# 3. 모델 생성 & 실행
ollama create qwen25-korean -f Modelfile
ollama run qwen25-korean "한국의 수도는?"
```

---

### 5️⃣ Llama.cpp (CPU/Edge)

```bash
# 1. GGUF 다운로드
huggingface-cli download MyeongHo0621/Qwen2.5-3B-Korean \
    gguf/qwen25-3b-korean-Q4_K_M.gguf \
    --local-dir ./

# 2. 추론 (GPU)
./llama.cpp/main \
    -m ./gguf/qwen25-3b-korean-Q4_K_M.gguf \
    -p "<|im_start|>user\n한국의 수도는?<|im_end|>\n<|im_start|>assistant\n" \
    -n 512 \
    --temp 0.7 \
    -ngl 99

# 3. 추론 (CPU)
./llama.cpp/main \
    -m ./gguf/qwen25-3b-korean-Q4_K_M.gguf \
    -p "<|im_start|>user\n한국의 수도는?<|im_end|>\n<|im_start|>assistant\n" \
    -n 512 \
    -t 8
```

---

## 🔧 Training Details

### Dataset
- **Source**: [MyeongHo0621/smol-koreantalk](https://huggingface.co/datasets/MyeongHo0621/smol-koreantalk)
- **Samples**: 200,000 한국어 대화 쌍
- **Domain**: 일반 대화, 지시 수행, 지식 Q&A

### Training Configuration
| Hyperparameter | Value |
|----------------|-------|
| **Method** | QLoRA (4-bit NF4) |
| **LoRA Rank** | 64 |
| **LoRA Alpha** | 128 |
| **Learning Rate** | 2e-4 |
| **Batch Size** | 128 (effective) |
| **Epochs** | 3 |
| **Steps** | 4689 |
| **Max Length** | 2048 |

---

## 📊 Repository Structure

```
MyeongHo0621/Qwen2.5-3B-Korean/
├── config.json                 # 모델 설정
├── model.safetensors          # Merged 모델 (~6GB)
├── tokenizer.json             # 토크나이저
├── tokenizer_config.json
└── gguf/                      # GGUF 파일들
    ├── qwen25-3b-korean-Q4_K_M.gguf  (~2GB) ⭐ 권장
    ├── qwen25-3b-korean-Q5_K_M.gguf  (~2.5GB)
    ├── qwen25-3b-korean-Q8_0.gguf    (~3.5GB)
    └── qwen25-3b-korean-F16.gguf     (~6GB)
```

---

## 🔗 Related Repositories

- **PEFT Adapter**: [MyeongHo0621/Qwen2.5-3B-Korean-QLoRA](https://huggingface.co/MyeongHo0621/Qwen2.5-3B-Korean-QLoRA)
  - LoRA 어댑터만 필요한 경우
  - 파인튜닝 연구용
  - ~479MB (경량)

---

## 📝 Citation

```bibtex
@misc{qwen25-korean-2025,
  author = {MyeongHo Shin},
  title = {Qwen2.5-3B-Korean: Korean-Optimized Conversational Model},
  year = {2025},
  publisher = {HuggingFace},
  howpublished = {\url{https://huggingface.co/MyeongHo0621/Qwen2.5-3B-Korean}},
}
```

---

## 🙏 Acknowledgments

- **Base Model**: [Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct) by Alibaba Cloud
- **Dataset**: [smol-koreantalk](https://huggingface.co/datasets/MyeongHo0621/smol-koreantalk)
- **Tools**: Unsloth, PEFT, vLLM, SGLang, Llama.cpp

---

## 📞 Contact

- **Author**: MyeongHo Shin
- **HuggingFace**: [@MyeongHo0621](https://huggingface.co/MyeongHo0621)

---

## ⚖️ License

Apache 2.0 - 상업적 사용, 수정, 배포 가능



---

##  Evaluation results

### Benchmark Results

#### General Benchmarks

| Task | Score | Metric |
|------|-------|--------|
| gsm8k | 42.00% | acc |
| mmlu | 58.00% | acc |
| hellaswag | 71.00% | acc_norm |
| winogrande | 65.00% | acc |
| arc_easy | 78.00% | acc |
| arc_challenge | 48.00% | acc_norm |

**Average Score**: 60.33%
