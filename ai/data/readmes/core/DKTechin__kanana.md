---
license: other
license_name: kanana
license_link: LICENSE
base_model: kakaocorp/kanana-2-3b-instruct
base_model_relation: quantized
pipeline_tag: text-generation
language:
  - ko
  - en
tags:
  - gguf
  - llama.cpp
  - quantized
  - kanana
---

# Kanana 2 3B Instruct — GGUF (Q4_K_M)

**Powered by Kanana**

[`kakaocorp/kanana-2-3b-instruct`](https://huggingface.co/kakaocorp/kanana-2-3b-instruct) 를 llama.cpp 에서 바로 쓸 수 있게 GGUF 로 변환하고 4bit(Q4_K_M) 양자화한 파일입니다. 원본 배포에는 GGUF 가 없어 사내 온디바이스(로컬 LLM) 용도로 직접 변환했습니다.

| | |
|---|---|
| 파일 | `kanana-2-3b-instruct-Q4_K_M.gguf` |
| 크기 | 2,161,793,408 bytes (2.01 GiB) |
| 양자화 | Q4_K_M — 4.92 BPW (원본 BF16 16.00 BPW) |
| 아키텍처 | `qwen3` (원본 `config.json` 이 `Qwen3ForCausalLM`) |
| 토크나이저 | `tokenizer.ggml.pre = kanana2`, vocab 128,256 |
| 컨텍스트 | 32,768 (rope: yarn, factor 40, original 4,096) |
| 대화 서식 | 원본 `chat_template.jinja` 를 GGUF 메타데이터에 포함 |

## 변경 사항 (Kanana Open License §3.1(iii))

가중치의 값을 바꾸는 학습·파인튜닝·병합은 하지 않았습니다. 원본 `safetensors` 를 아래 절차로 **형식 변환 + 4bit 양자화**만 했습니다.

```bash
# llama.cpp @ 7e1e28c (2026-07-28)
python convert_hf_to_gguf.py kanana-2-3b-instruct --outtype bf16 \
  --outfile kanana-2-3b-instruct-BF16.gguf
./build/bin/llama-quantize kanana-2-3b-instruct-BF16.gguf \
  kanana-2-3b-instruct-Q4_K_M.gguf Q4_K_M
```

4bit 양자화는 원본 대비 품질 손실을 수반합니다. 원본 품질이 필요하면 위 링크의 원본 저장소를 쓰세요.

## 사용법

```bash
# llama.cpp
llama-cli -hf DKTechin/kanana:Q4_K_M -c 2048 --jinja \
  -sys "당신은 사내 메신저 대화를 간결하게 요약하는 도우미입니다." \
  -p "아래 대화를 3줄로 요약해줘: ..."
```

LM Studio·Jan·Ollama 등 GGUF 를 읽는 런타임에서도 그대로 씁니다. 시스템 프롬프트 없이 쓰면 요약 대신 입력을 되풀이하는 경향이 있어, 역할을 지정하는 시스템 프롬프트를 함께 주는 편이 안전합니다.

## 확인한 것 · 확인하지 못한 것

- 확인: 메타데이터(arch·tokenizer pre·rope·chat template), 실제 한국어 요약 생성, macOS/Metal 기준 2048 토큰 조건에서 프롬프트 1,375 t/s · 생성 128 t/s.
- 미확인: 32k 장문 품질. 원본 `config.json` 은 rope 배수를 40 으로 적어 두었지만 길이 비율(32,768 / 4,096)로 계산하면 8 이라 서로 맞지 않습니다. 원본 파이썬 런타임과 동작을 맞추기 위해 **명시값 40 을 그대로 기록**했으니, 아주 긴 입력에서 이상하면 이 값을 먼저 의심하세요.

## 라이선스

이 파일은 [Kanana Open License Agreement](LICENSE) 를 따르는 파생물입니다. 사본은 이 저장소의 [`LICENSE`](LICENSE), 고지 문구는 [`NOTICE`](NOTICE) 에 있습니다.

- 사용자는 원본과 동일하게 **금지된 사용 정책(Agreement §2.2)** 과 KAKAO 의 Guidelines For Responsible AI 를 준수해야 하며, 이 파일을 재배포할 때에도 같은 의무를 후속 사용자에게 알려야 합니다.
- API·클라우드 등으로 제3자에게 접근을 제공하거나 재판매하려면 **KAKAO 의 별도 상업 라이선스**가 필요합니다(Agreement §4).
- 이 파일을 사용하는 웹사이트·UI·문서에는 **"Powered by Kanana"** 를 알아볼 수 있게 표시해야 합니다(Agreement §3.1(v)).

```
Kanana is licensed in accordance with the Kanana Open License Agreement.
Copyright © KAKAO Corp. All Rights Reserved.
```
