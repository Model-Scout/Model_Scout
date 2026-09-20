---
base_model: skt/A.X-4.0-Light
language:
- en
- ko
license: apache-2.0
tags:
- gguf
- llama.cpp
- qwen2
- A.X
pipeline_tag: text-generation
---

# A.X-4.0-Light-GGUF

[skt/A.X-4.0-Light](https://huggingface.co/skt/A.X-4.0-Light) 모델을 [llama.cpp](https://github.com/ggml-org/llama.cpp)로 GGUF 변환 및 양자화한 버전입니다.

## 제공 파일

| 파일 | 비트 | 비고 |
|---|---|---|
| A.X-4.0-Light-F16.gguf | F16 | 원본 정밀도 |
| A.X-4.0-Light-Q8_0.gguf | 8-bit | 거의 무손실 |
| A.X-4.0-Light-Q6_K.gguf | 6-bit | |
| A.X-4.0-Light-Q5_K_M.gguf | 5-bit | |
| A.X-4.0-Light-Q5_K_S.gguf | 5-bit | |
| A.X-4.0-Light-Q5_0.gguf | 5-bit | legacy |
| A.X-4.0-Light-Q4_K_M.gguf | 4-bit | 일반 권장 기본값 |
| A.X-4.0-Light-Q4_K_S.gguf | 4-bit | |
| A.X-4.0-Light-Q4_0.gguf | 4-bit | legacy |
| A.X-4.0-Light-IQ4_XS.gguf | ~4.3-bit | importance-aware |
| A.X-4.0-Light-Q3_K_L.gguf | 3-bit | |
| A.X-4.0-Light-Q3_K_M.gguf | 3-bit | |
| A.X-4.0-Light-Q3_K_S.gguf | 3-bit | |
| A.X-4.0-Light-IQ3_M.gguf | ~3.7-bit | importance-aware |
| A.X-4.0-Light-Q2_K.gguf | 2-bit | 최소 용량, 품질 저하 큼 |

IQ3_XXS / IQ2_M / IQ2_XS / IQ2_XXS는 importance matrix(imatrix)가 필요한 양자화 방식이라 이번 배치에는 포함하지 않았습니다.

## 사용법

```bash
llama-cli -m A.X-4.0-Light-Q4_K_M.gguf -p "안녕하세요"
```

## 변환 정보

- 변환 도구: llama.cpp `convert_hf_to_gguf.py` (mainline, A.X-4.0 tokenizer pre-tokenizer 지원 버전)
- 양자화 도구: llama.cpp `llama-quantize`
- 베이스 모델 아키텍처: Qwen2ForCausalLM (hidden 3584, 28 layers, GQA 4 KV heads, 7.3B params)
