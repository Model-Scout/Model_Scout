---
license: apache-2.0
tags:
- darwin
- darwin-v7
- evolutionary-merge
- reasoning
- advanced-reasoning
- chain-of-thought
- thinking
- qwen3.6
- qwen
- moe
- mixture-of-experts
- distillation
- multilingual
- gpqa
- benchmark
- open-source
- apache-2.0
- hybrid-vigor
- proto-agi
- vidraft
- eval-results
- mlx
language:
- en
- zh
- ko
- ja
- de
- fr
- es
- ru
- ar
- multilingual
pipeline_tag: text-generation
library_name: mlx
base_model: FINAL-Bench/Darwin-36B-Opus
model-index:
- name: Darwin-36B-Opus
  results:
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: GPQA Diamond
      type: Idavidrein/gpqa
      config: gpqa_diamond
    metrics:
    - type: accuracy
      value: 88.4
      name: Accuracy
---

# Darwin-36B-Opus (MLX Optimized)

This repository provides an **MLX-optimized** version of **`FINAL-Bench/Darwin-36B-Opus`**, a state-of-the-art Mixture-of-Experts (MoE) model engineered for advanced reasoning, chain-of-thought (CoT) processes, and complex problem-solving.

Apple Silicon(Mac) 환경의 MLX 프레임워크에서 최적의 속도와 효율적인 메모리 대역폭으로 구동되도록 포맷 변환 및 최적화가 완료된 버전입니다.

## 🚀 Model Highlights

- **Evolutionary Merge & MoE**: Qwen 기반 아키텍처를 진화적 머지(Evolutionary Merge) 기법과 Mixture-of-Experts(MoE) 구조로 결합하여 체급을 뛰어넘는 최고의 효율성을 자랑합니다.
- **Advanced Reasoning**: 깊은 다단계 사고 과정(`<thought>`)을 거쳐 복잡한 코딩, 수학, 과학적 난제를 해결하는 심층 추론(Chain-of-Thought) 능력이 탑재되어 있습니다.
- **Top-Tier Benchmark Performance**: 박사급 난이도의 하드코어 추론 테스트인 **GPQA Diamond 벤치마크에서 88.4%의 고득점**을 기록했습니다.
- **Multilingual Support**: 한국어, 영어, 중국어, 일본어를 포함한 10개 이상의 다국어 환경을 완벽하게 지원합니다.

## 🛠️ Requirements & Installation

이 모델을 구동하려면 최신 버전의 `mlx-lm` 라이브러리가 필요합니다.

```bash
pip install -U mlx-lm
```

## 💻 How to Use

### 1. Python API를 이용한 실행
```python
from mlx_lm import load, generate

model, tokenizer = load("cudo528/Darwin-36B-Opus-MLX-6bit")

prompt = "Quantum computing과 기존 컴퓨터의 근본적인 추론 방식 차이를 한국어로 명확하게 설명해줘."

response = generate(
    model, 
    tokenizer, 
    prompt=prompt, 
    max_tokens=2048,
    verbose=True # 심층 추론 과정(<thought>)을 확인하려면 True로 설정
)
print(response)
```

### 2. 터미널(CLI) 환경에서 즉시 실행
```bash
mlx_lm.generate --model cudo528/Darwin-36B-Opus-MLX-6bit --prompt "Explain the concept of Hybrid Vigor in AI." --max-tokens 1024
```

## 📂 Quantization & Lineage

- **Original Base Model**: [FINAL-Bench/Darwin-36B-Opus](https://huggingface.co/FINAL-Bench/Darwin-36B-Opus)
- **Format**: MLX Formatted (`.safetensors`)
- **License**: Apache-2.0

본 변환 버전은 원본 모델의 가중치 성질과 라이선스를 전적으로 준수합니다. 로컬 하드웨어 사양에 맞춰 양자화 비트 수(예: 8-bit, 4-bit)를 조정한 경우, 파일 목록의 수정을 확인해 주시기 바랍니다.
