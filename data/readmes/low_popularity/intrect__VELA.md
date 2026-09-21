---
license: apache-2.0
language:
  - ko
  - en
library_name: transformers
tags:
  - finance
  - korean
  - stock-analysis
  - reasoning
  - dpo
  - gguf
  - llama-cpp
  - llama-cpp-python
  - mlx
  - apple-silicon
  - 4bit
  - quantized
  - vllm
  - ollama
base_model: Qwen/Qwen2.5-7B-Instruct
pipeline_tag: text-generation
---

# VELA (Vector-Encoded Learning Agent)

[![GitHub](https://img.shields.io/badge/Framework-GitHub-181717?logo=github)](https://github.com/Intrect-io/vela-framework)
[![Hugging Face Model](https://img.shields.io/badge/%F0%9F%A4%97%20Model-intrect%2FVELA-yellow)](https://huggingface.co/intrect/VELA)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Demo-Spaces-blue)](https://huggingface.co/spaces/intrect/vela-demo)

**한국 주식시장 전문 AI 애널리스트**

VELA는 한국 주식시장 뉴스 분석 및 투자 리서치를 위해 특화된 7B 파라미터 언어 모델입니다.
KOSPI/KOSDAQ 2,135개 종목에 대한 뉴스 영향 분석, 증권사 리포트 해석,
Reasoning Trace 기반 구조화된 투자 분석을 수행합니다.

> **58K+ SFT 샘플**과 **26K+ DPO 페어**로 학습하여,
> 한국어 금융 도메인에서 정확하고 구조화된 분석을 제공합니다.
>
> **Agent Framework**: [github.com/Intrect-io/vela-framework](https://github.com/Intrect-io/vela-framework) — `pip install vela-framework`

---

## Model Details

| 항목 | 내용 |
|------|------|
| **Base Model** | [Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) |
| **Training** | SFT (58,206 samples) + DPO (26,421 pairs) |
| **Parameters** | 7.6B |
| **Context Length** | 8,192 tokens |
| **RT Format** | Markdown Reasoning Trace |
| **Stock Coverage** | 2,135 종목 (KOSPI + KOSDAQ) |
| **License** | Apache 2.0 |

### Available Formats

| Format | File | Size | Use Case |
|--------|------|------|----------|
| **BF16** (safetensors) | [`model-*.safetensors`](https://huggingface.co/intrect/VELA/tree/main) | 14.5 GB | Full precision, GPU inference |
| **GGUF Q4_K_M** | [`vela-dpo-v6-q4_k_m.gguf`](https://huggingface.co/intrect/VELA/blob/main/vela-dpo-v6-q4_k_m.gguf) | 4.4 GB | llama.cpp / Ollama / LM Studio |
| **MLX 4-bit** | [`mlx-int4/`](https://huggingface.co/intrect/VELA/tree/main/mlx-int4) | 4.0 GB | Apple Silicon (M1/M2/M3/M4) |

---

## What Can VELA Do?

### 1. 뉴스 영향 분석
주식 관련 뉴스가 주가에 미치는 영향을 단계적으로 추론합니다.

### 2. Reasoning Trace (단계별 사고 과정)
분석 과정을 투명하게 보여주는 Markdown Reasoning Trace를 생성합니다:

```
**Step 1**:
**Thought**: 삼성전자 3나노 양산 성공 뉴스의 기술적 의미를 파악해야 합니다.
**Action**: search
**Query**: 삼성전자 3나노 파운드리 수율 경쟁력 TSMC
**Confidence**: 35%

**Step 2**:
**Thought**: TSMC 대비 수율 격차가 핵심 변수이며, 양산 성공은 기술력 입증이나 수율 안정화까지 시간 필요.
**Action**: analyze
**Confidence**: 65%

**Step 3**:
**Thought**: 3나노 양산 성공은 중장기 긍정 시그널이나, 단기적으로 수율 이슈 리스크가 존재합니다.
**Action**: conclude
**Confidence**: 80%
```

### 3. 증권사 리포트 해석
애널리스트 리포트를 기반으로 핵심 포인트와 투자 시사점을 도출합니다.

### 4. 투자 리서치 리포트
7개 섹션으로 구조화된 투자 분석 보고서를 생성합니다:
Executive Summary / Key Metrics / 시장 동향 / 수급 분석 / 뉴스 영향 / 리스크 / 투자 의견

### 5. 도구 호출 (Tool Calling)
Search, Price, Investor 등 외부 도구와 연동하는 분석을 수행합니다.

---

## Training Pipeline

```
Qwen/Qwen2.5-7B-Instruct
        |
        v
   SFT (58,206 samples)
   ├── 뉴스 분류 분석      10,830  (18.6%)
   ├── 극단 시그널 분석      9,603  (16.5%)
   ├── 증권사 리포트 (GPT-4o) 5,117   (8.8%)
   ├── 뉴스 영향 분석        4,839   (8.3%)
   ├── 멀티턴 대화           8,000  (13.8%)
   ├── Gap Fill (12 카테고리) 12,635  (21.7%)
   │   ├── 밸류에이션 분석    2,000
   │   ├── 수급/리스크/EOD    3,000
   │   ├── 거절/유보 응답     1,000
   │   ├── 간결 분석          1,000
   │   ├── 심층 추론 (5+ steps) 1,000
   │   └── 기타 (매크로, 섹터 등) 4,635
   └── 기타                  7,182  (12.3%)
        |
        v
   DPO (26,421 pairs)
   ├── 중복 제거 기본 페어   12,000  (45.4%)
   ├── 다국어 leak 보강      5,997  (22.7%)
   ├── VELA ChatML 정렬      5,000  (18.9%)
   ├── 불충분 분석 교정      1,642   (6.2%)
   ├── 중국어 leak 교정 v2   1,216   (4.6%)
   └── Reasoning Trace 정렬    566   (2.1%)
        |
        v
      VELA v1.3
```

---

## Training Data Details

### SFT v3 (58,206 samples)

| Source | Samples | Ratio | Description |
|--------|---------|-------|-------------|
| `classified_news` | 10,830 | 18.6% | GPT-4o 분류된 뉴스 Reasoning Trace |
| `extreme_signals` | 9,603 | 16.5% | 급등/급락 시그널 뉴스 분석 |
| `securities_report_gpt4o` | 5,117 | 8.8% | 증권사 리포트 GPT-4o 재구성 |
| `analysis_news` | 4,839 | 8.3% | 일반 뉴스 영향 분석 |
| `multi_turn_2t` | 4,000 | 6.9% | 단일 턴 다양 종목 분석 |
| `multi_turn_4t` | 4,000 | 6.9% | 2턴 follow-up 대화 |
| **`valuation`** | **2,000** | **3.4%** | 밸류에이션 분석 (v3 Gap Fill) |
| `tool_calling` | 1,965 | 3.4% | Search/Price/Investor 도구 호출 |
| **`supply_demand_ext`** | **1,000** | **1.7%** | 수급 확장 분석 (v3) |
| **`risk`** | **1,000** | **1.7%** | 리스크 분석 (v3) |
| **`eod_report`** | **1,000** | **1.7%** | EOD 시황 리포트 (v3) |
| **`refusal`** | **1,000** | **1.7%** | 거절/유보 응답 (v3) |
| **`short_analysis`** | **1,000** | **1.7%** | 간결 분석 <500자 (v3) |
| **`deep_reasoning`** | **1,000** | **1.7%** | 심층 추론 5+ steps (v3) |
| **`low_confidence`** | **1,000** | **1.7%** | 저확신도 분석 (v3) |
| **`macro_impact_ext`** | **1,000** | **1.7%** | 거시경제 확장 (v3) |
| **`sector_theme`** | **1,000** | **1.7%** | 섹터/테마 분석 (v3) |
| `multi_stock_comparison` | 981 | 1.7% | 복수 종목 비교 분석 |
| `earnings_impact` | 971 | 1.7% | 실적 발표 영향 분석 |
| `risk_alert` | 948 | 1.6% | 리스크 경고 분석 |
| **`null_impact`** | **900** | **1.5%** | 주가 무영향 응답 (v3) |
| Other | 2,050 | 3.5% | batch5 fallback, 기존 수급/섹터/매크로 |

> v3에서 12개 카테고리 12,635개 샘플을 추가하여 데이터 갭을 보강했습니다.
> 생성 비용: Perplexity Sonar 2K ($4.60) + OpenAI gpt-4o-mini Batch API 10.6K ($2.76) = **~$7.36**

### DPO v2 (26,421 pairs)

| Source | Pairs | Ratio | Rejection Type |
|--------|-------|-------|----------------|
| `dpo_dedup` | 12,000 | 45.4% | 짧은/저품질 응답 vs 상세 분석 |
| `multilingual_aug` | 5,997 | 22.7% | 중국어/영어 leak, 짧은 응답, 저확신 |
| `vela_chatml` | 5,000 | 18.9% | 형식 오류, 짧은 응답 |
| `batch5_insuf_dpo` | 1,642 | 6.2% | 불충분 분석 품질 교정 |
| `chinese_leak_v2` | 1,216 | 4.6% | 중국어 문자 leak 집중 교정 |
| `reasoning_trace_2k` | 566 | 2.1% | 영어 leak, RT 형식 오류 |

### Data Version History

| Version | SFT Samples | DPO Pairs | Changes |
|---------|-------------|-----------|---------|
| v1.0 | 36,713 | 24,779 | 초기 학습 데이터 (JSON RT) |
| v1.1 | 36,713 | 24,779 | RT JSON → Markdown 변환 |
| v2.0 | 45,571 | 26,421 | +멀티턴 8K, +batch5 불충분 DPO |
| **v3.0** | **58,206** | **26,421** | **+Gap Fill 12개 카테고리 12,635** |

---

## Benchmarks

### 한국어 LLM 벤치마크 (KMMLU + HAE-RAE)

모든 모델 **Q4_K_M 양자화**, **0-shot** 조건으로 평가. `lm-evaluation-harness` v0.4.9 + `llama.cpp`, Apple M1 Max 32GB 환경.

#### KMMLU (한국어 MMLU, 10과목)

| 과목 | VELA DPO v6 | Qwen2.5-7B-Instruct | EXAONE-3.5-7.8B |
|------|:-----------:|:--------------------:|:---------------:|
| 마케팅 | **75.7** | 72.5 | 75.6 |
| 컴퓨터과학 | **73.7** | 69.7 | 69.7 |
| 경영학 | 54.0 | 55.2 | **57.3** |
| 정치사회학 | 49.0 | 49.3 | **56.0** |
| 경제학 | 45.4 | 47.7 | **51.5** |
| 법학 | 43.4 | 46.1 | **49.9** |
| 심리학 | 39.2 | 39.3 | **45.7** |
| 회계 | 38.0 | 33.0 | **42.0** |
| 수학 | **33.0** | **33.7** | 27.7 |
| 한국사 | **31.0** | 29.0 | 22.0 |
| **평균** | **48.2** | **47.6** | **49.7** |

#### HAE-RAE Bench (한국어 특화)

| 영역 | VELA DPO v6 | Qwen2.5-7B-Instruct | EXAONE-3.5-7.8B |
|------|:-----------:|:--------------------:|:---------------:|
| 희귀어 | 69.9 | 68.4 | **78.8** |
| 표준명칭 | 64.7 | 66.0 | **71.9** |
| 외래어 | 48.5 | 57.4 | **81.1** |
| 한국사 | 45.7 | 42.6 | **77.7** |
| 일반상식 | **44.3** | 42.1 | 44.3 |
| **평균** | **54.5** | **55.3** | **70.7** |

#### 주요 발견

- **Catastrophic forgetting 없음**: 도메인 특화 fine-tuning 후에도 베이스 모델(Qwen2.5) 능력 유지 (KMMLU 평균 48.2% vs 47.6%)
- **도메인 전이 효과**: 금융 관련 과목에서 베이스 모델 대비 향상 — 마케팅(+3.2%), 컴퓨터과학(+4.0%), 회계(+5.0%)
- **한국어 네이티브 모델과 경쟁**: 대규모 한국어 코퍼스로 사전학습된 EXAONE-3.5-7.8B (LG AI Research) 대비 KMMLU 10과목 중 4개에서 우위

### 양자화 벤치마크 (GGUF)

RTX 3060 12GB, llama-cpp-python, `n_gpu_layers=-1`, `n_ctx=4096`

| 포맷 | 속도 | 중국어 Leak | 품질 |
|------|------|-------------|------|
| **Q4_K_M (v6)** | **36 tok/s** | 0/5 클린 | RT + 리포트 정상 |

> 스트레스 테스트 5회: Synthesis + 3K Reasoning Trace 교대 — 전 구간 **중국어 leak 제로**

### MLX 벤치마크 (Apple Silicon)

M1 Max 32GB, MLX 4-bit 양자화

| 구성 | 양자화 | 로딩 시간 | 추론 속도 | 메모리 |
|------|--------|----------|----------|--------|
| **MLX 4-bit** | 4-bit (4.5 bpw) | 0.59초 | **15.93 tok/s** | 4.4 GB |
| PyTorch (CPU) | BF16 | 0.10초 | 4.93 tok/s | 0.3 GB |
| PyTorch + LoRA (CPU) | BF16 | 1.64초 | 4.22 tok/s | 14.1 GB |

MLX 4-bit vs PyTorch CPU:
- 추론 속도 **3.2배** (15.93 vs 4.93 tok/s)
- 모델 크기 **73% 감소** (4 GB vs 15 GB)
- 메모리 **68% 절약** (4.4 vs 14.1 GB)

### DPO 학습 품질 개선

| 지표 | DPO 전 | DPO 후 |
|------|--------|--------|
| 중국어 leak | 빈번 | **0/10 클린** |
| 영어 leak | 간헐적 | 최소화 |
| RT 형식 준수율 | ~80% | **~98%** |
| 한국어 유창성 | 양호 | **우수** |
---

## Usage

### llama-cpp-python (Recommended for GGUF)

```python
from llama_cpp import Llama

model = Llama(
    model_path="vela-dpo-v6-q4_k_m.gguf",
    n_ctx=4096,
    n_gpu_layers=-1,
    chat_format="chatml",
)

response = model.create_chat_completion(
    messages=[
        {"role": "system", "content": "당신은 한국 주식 전문 애널리스트입니다."},
        {"role": "user", "content": "삼성전자 HBM 사업 전망을 분석해주세요."},
    ],
    max_tokens=1024,
    temperature=0.7,
)
print(response["choices"][0]["message"]["content"])
```

### Transformers (BF16)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained(
    "intrect/VELA",
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
tokenizer = AutoTokenizer.from_pretrained("intrect/VELA")

messages = [
    {"role": "system", "content": "당신은 한국 주식 전문 애널리스트입니다."},
    {"role": "user", "content": "삼성전자 HBM 사업 전망을 분석해주세요."},
]

text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)

outputs = model.generate(
    **inputs,
    max_new_tokens=1024,
    temperature=0.7,
    do_sample=True,
)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

### vLLM

```python
from vllm import LLM, SamplingParams

llm = LLM(model="intrect/VELA", dtype="bfloat16")
params = SamplingParams(temperature=0.7, max_tokens=1024)

outputs = llm.generate(
    ["삼성전자 HBM 시장 전망을 분석해주세요."],
    params,
)
print(outputs[0].outputs[0].text)
```

### MLX (Apple Silicon)

```python
from mlx_lm import load, generate

# HF에서 mlx-int4 폴더만 다운로드
from huggingface_hub import snapshot_download
mlx_path = snapshot_download("intrect/VELA", allow_patterns="mlx-int4/*")
model, tokenizer = load(f"{mlx_path}/mlx-int4")

response = generate(
    model,
    tokenizer,
    prompt="삼성전자 3나노 양산 뉴스 분석",
    max_tokens=1024,
)
print(response)
```

### Ollama

```bash
# Modelfile
FROM ./vela-q4_k_m.gguf
TEMPLATE """<|im_start|>system
{{ .System }}<|im_end|>
<|im_start|>user
{{ .Prompt }}<|im_end|>
<|im_start|>assistant
"""
PARAMETER temperature 0.7
PARAMETER num_ctx 4096
```

---

## Output Format

VELA는 두 가지 출력 모드를 지원합니다.

### 1. Reasoning Trace (분석 과정)

Markdown 형식으로 단계별 사고 과정을 투명하게 보여줍니다:

```markdown
**Step 1**:
**Thought**: 삼성전자 HBM3E 12단 양산 관련 뉴스를 확인합니다. 수주 현황과 시장 점유율 파악이 필요합니다.
**Action**: search
**Query**: 삼성전자 HBM3E 12단 수주 시장점유율
**Confidence**: 45%

**Step 2**:
**Thought**: SK하이닉스 대비 삼성전자의 HBM 시장 점유율 확대 추세를 분석합니다.
**Action**: analyze
**Confidence**: 70%

**Step 3**:
**Thought**: HBM3E 양산 성공은 긍정적이나, NVIDIA 인증 지연 리스크가 존재합니다.
**Action**: conclude
**Confidence**: 82%
```

### 2. Synthesis Report (최종 리포트)

7개 섹션으로 구조화된 투자 분석 보고서:

```markdown
# 분석 리포트: 삼성전자 (005930.KS)

## Executive Summary
[2-3문장 핵심 요약]

## Key Metrics
| 지표 | 수치 |
|------|------|
| 현재가 | 181,200원 |
| 12M FWD PER | 15.4배 |
| PBR | 3.13배 |

## 시장 동향 분석
## 수급 분석
## 뉴스 영향 분석
## 리스크 요인
## 투자 의견
```

---

## Example Output

> 아래는 VELA 모델이 실제로 생성하는 응답 예시입니다 (SFT 학습 데이터 기반).
>
> **Query**: "LGU+ 오픈랜 상용망 구축 뉴스가 CS(065770) 주가에 미치는 영향을 분석해주세요."

<details>
<summary><b>Reasoning Trace (추론 과정) 펼치기</b></summary>

```
**Step 1**:
**Thought**: CS는 통신장비 제조업체로, LGU+ 오픈랜 상용망 구축 뉴스는
직접적 수혜 가능성이 있다. 뉴스에서 언급된 '삼지전자·노키아'와의 협력 관계,
기술 실증 의미를 파악해야 한다. CS의 오픈랜 관련 포지셔닝 확인 필요.
**Action**: search
**Query**: CS 065770 오픈랜 5G 통신장비 사업
**Confidence**: 40%

**Step 2**:
**Thought**: 뉴스 본문에서 '삼지전자·노키아'가 장비 구축을 담당했다고 명시.
CS가 이 프로젝트에 직접 참여했는지, 아니면 간접 수혜인지 구분이 필수.
LGU+ 오픈랜 실증 프로젝트의 규모와 향후 상용화 일정도 중요.
**Action**: search
**Query**: LGU+ 오픈랜 실증단지 삼지전자 CS 참여
**Confidence**: 50%

**Step 3**:
**Thought**: 뉴스에서 CS의 직접 언급이 없으므로, CS가 오픈랜 밸류체인 내 어느
위치에 있는지 불명확. 다만 통신장비 제조사로서 오픈랜 시장 확대는 장기 성장 기회.
실제 1일/3일 수익률이 각각 +0.73%, +0.87%로 완만한 상승이므로,
뉴스 직접 영향보다는 섹터 긍정 심리 반영으로 해석.
**Action**: analyze
**Confidence**: 65%
```

</details>

<details>
<summary><b>Quick Assessment (빠른 판정) 펼치기</b></summary>

```json
{
  "category": "product_innovation",
  "sentiment": "bullish",
  "impact": "medium",
  "confidence": 0.68,
  "reasoning": "LGU+ 오픈랜 상용망 구축은 국내 통신장비 산업의 기술 고도화 신호이나,
    뉴스에서 CS의 직접 참여가 명시되지 않음. 간접 수혜 가능성과 섹터 긍정 심리로
    인한 완만한 상승으로 평가."
}
```

</details>

<details open>
<summary><b>Analysis Report (상세 리포트)</b></summary>

### 1. Executive Summary

LG유플러스의 오픈랜 상용망 구축은 국내 통신 인프라의 5G-6G 기술 고도화를 시사하는 긍정적 신호입니다.
뉴스에서는 삼지전자와 노키아의 장비 구축을 명시했으나, CS의 직접 참여 여부는 공개되지 않았습니다.
다만 CS는 통신장비 제조업체로서 국내 오픈랜 시장 확대의 장기 수혜자가 될 가능성이 있습니다.
실제 주가 반응(1일 +0.73%, 3일 +0.87%)은 제한적이며, 이는 뉴스가 개별 종목보다는
섹터 전체에 대한 긍정 심리를 반영한 것으로 해석됩니다. **종합 신뢰도: 0.68 (MEDIUM)**

### 2. Key Metrics

| 지표 | 수치 | 평가 |
|------|------|------|
| 1일 수익률 | +0.73% | 약한 상승 |
| 3일 수익률 | +0.87% | 지속적 약세 상승 |
| 뉴스 영향력 | Medium | 섹터 영향 > 개별 종목 영향 |
| 직접 언급 | 없음 | CS 미언급 |
| 기술 카테고리 | 오픈랜(Open RAN) | 5G-6G 핵심 기술 |

### 3. 시장 동향 분석

오픈랜은 기존 폐쇄형 통신장비 시스템을 개방형 표준으로 전환하는 구조적 변화입니다.
LGU+의 금오공과대학교 캠퍼스 구축은 한국지능정보사회진흥원(NIA)과 과학기술정보통신부 주도의
국가 실증 프로젝트로, 정부 차원의 오픈랜 생태계 조성 의지를 보여줍니다.

"기존 5G 네트워크와 동등한 수준의 서비스"를 제공한다고 명시한 것은 국내 오픈랜 기술이
글로벌 수준에 도달했음을 의미합니다. 이는 국내 통신장비 산업 전반에 긍정적 신호이며,
CS와 같은 관련 업체들의 기술 고도화 필요성을 강조합니다.

### 4. 리스크 요인

- CS의 오픈랜 프로젝트 직접 참여 여부 불확실
- 삼지전자·노키아 등 경쟁사 대비 기술 포지셔닝 미확인
- 오픈랜 상용화 일정 및 수주 가시성 부족

### 5. 투자 의견

오픈랜 시장 확대는 **중장기 긍정 요인**이나, CS의 직접적 수혜 경로가 확인되기 전까지
**관망** 포지션이 적절합니다. 향후 CS의 오픈랜 관련 수주 공시나 기술 제휴 발표 시
재평가가 필요합니다.

</details>

---

## Architecture

VELA는 단독 LLM으로도 동작하지만, 에이전트 시스템과 결합하면 실시간 데이터 기반 분석이 가능합니다:

```
[사용자 쿼리]
      |
      v
[멀티소스 검색] ─── DuckDuckGo (최신 뉴스)
      |          ├── 한국투자증권 KIS (현재가, PER, PBR, EPS, 수급)
      |          ├── FnGuide (사업개요, 재무정보)
      |          └── FAISS 317K (과거 유사 뉴스 + 주가 반응)
      v
[컨텍스트 주입] → System Prompt + 검색 결과
      |
      v
[VELA LLM] → Reasoning Trace (Step-by-Step)
      |
      v
[리서치 리포트]
```

---

## Limitations

- **실시간 시세**: 모델 자체는 실시간 데이터에 접근하지 못합니다 (에이전트 시스템 필요)
- **수치 할루시네이션**: 구체적 수치(주가, PER 등)는 외부 검증이 필요합니다
- **컨텍스트**: 8K 토큰 제한으로 긴 문서 처리에 한계가 있습니다
- **투자 조언 아님**: 정보 제공 목적이며, 투자 결정은 본인의 판단과 책임입니다

---

## Citation

```bibtex
@misc{vela2026,
  title={VELA: Vector-Encoded Learning Agent for Korean Stock Analysis},
  author={intrect},
  year={2026},
  publisher={Hugging Face},
  url={https://huggingface.co/intrect/VELA}
}
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| **v1.3** | **2026-03-31** | **DPO v6 모델 업데이트 (Unsloth 학습, SFT v6 + DPO v6 merged)** |
| v1.2 | 2026-02-16 | SFT v3 (58K) Gap Fill 12카테고리, Markdown RT, 벤치마크 추가 |
| v1.1 | 2026-02-12 | GGUF 양자화 모델 추가 (Q4_K_M, Q8_0) |
| v1.0 | 2026-01-28 | DPO 병합, 중국어/영어 leak 해결 |
| v0.9 | 2026-01-15 | SFT 베이스 모델 공개 |

---

**Disclaimer**: 이 모델의 출력은 투자 조언이 아닙니다. 모든 투자 결정은 본인의 판단과 책임 하에 이루어져야 합니다.
