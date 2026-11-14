---
base_model: kakaocorp/kanana-2-1.3b-instruct
base_model_relation: quantized
license: other
license_name: kanana-open-license
license_link: LICENSE
language:
  - ko
  - en
pipeline_tag: text-generation
tags:
  - gguf
  - llama.cpp
  - kanana
  - on-device
  - imatrix
---

# Kanana-2-1.3B-Instruct GGUF (kanana2tiny)

**Powered by Kanana**

[kakaocorp/kanana-2-1.3b-instruct](https://huggingface.co/kakaocorp/kanana-2-1.3b-instruct)를 원본 구조(3:1 sliding-window/full attention 하이브리드 + 레이어별 RoPE)를 **그대로 보존**해 llama.cpp GGUF로 변환하고 imatrix 양자화한 모델입니다. 온디바이스(Android/iOS) 추론용입니다.

> ⚠️ **패치된 llama.cpp가 필요합니다.** 이 GGUF의 아키텍처는 `kanana2tiny`입니다. upstream llama.cpp와 이를 내장한 앱(LM Studio, Ollama, PocketPal 등)에는 아직 이 아키텍처가 없어 `unknown model architecture: 'kanana2tiny'` 오류가 납니다. 패치와 빌드 방법은 아래 [사용 방법](#사용-방법)을 참고하세요.

## 파일

모든 GGUF는 패치된 llama.cpp로 변환한 f16에서 같은 imatrix로 양자화했습니다. 아래 수치는 **이 저장소에 올린 파일 그대로** 측정한 값입니다.

| 파일 | 크기 | 한국어 512 dPPL / top-1 | 한국어 4096 dPPL / top-1 | 영어 4096 dPPL / top-1 | 비고 |
|---|---|---|---|---|---|
| `kanana2tiny-f16.gguf` | 2.41 GiB | ≈0 / 99.93% | ≈0 / 99.96% | ≈0 / 99.96% | 기준 (재양자화용) |
| `kanana2tiny-Q8_0.gguf` | 1,314 MB | +0.3% / 97.1% | +0.3% / 97.6% | +0.3% / 97.7% | |
| `kanana2tiny-Q6_K-im.gguf` | 1,070 MB | +1.7% / 93.6% | +1.2% / 94.2% | +1.0% / 94.3% | 품질 우선 |
| `kanana2tiny-Q6_K.gguf` | 1,070 MB | +2.0% / 93.5% | +1.4% / 94.1% | +1.2% / 94.1% | |
| **`kanana2tiny-Q5_K_M-im.gguf`** | **925 MB** | **+2.6% / 90.2%** | **+2.1% / 91.0%** | **+2.1% / 92.0%** | **추천** |
| `kanana2tiny-Q5_K_M.gguf` | 925 MB | +3.2% / 89.5% | +2.7% / 89.9% | +2.5% / 90.8% | |
| `kanana2tiny-Q4_K_M-im-emb8.gguf` | 852 MB | +6.6% / 83.5% | +6.9% / 85.0% | +7.7% / 86.4% | 임베딩 Q8_0 |
| `kanana2tiny-Q4_K_M-im.gguf` | 814 MB | +6.9% / 83.1% | +7.2% / 84.8% | +8.1% / 86.1% | 용량 우선 |
| `kanana2tiny-Q4_K_M.gguf` | 814 MB | +8.9% / 82.5% | +9.6% / 83.6% | +8.5% / 85.0% | |
| `kanana2tiny-IQ4_NL-im.gguf` | 744 MB | +11.2% / 80.8% | +10.3% / 82.9% | +9.2% / 84.1% | |
| `kanana2tiny-Q4_0-im.gguf` | 740 MB | +10.9% / 78.0% | +14.0% / 79.3% | +15.0% / 81.5% | ARM 프롬프트 처리 최속 |
| `kanana2tiny-Q4_0.gguf` | 739 MB | +14.9% / 76.5% | +18.8% / 77.2% | +18.4% / 79.6% | |
| `kanana2tiny-IQ4_XS-im.gguf` | 718 MB | +11.4% / 80.8% | +11.0% / 82.8% | +9.6% / 83.9% | |
| `kanana2tiny-Q3_K_M-im.gguf` | 682 MB | +24.8% / 70.7% | +31.3% / 72.4% | +32.0% / 74.5% | 비권장 |
| `kanana2tiny.imatrix.gguf` | 2 MB | – | – | – | importance matrix |

- `-im` = imatrix 적용. **dPPL** = HF 원본(fp32) 대비 perplexity 증가율, **top-1** = 다음 토큰 1순위가 원본과 같은 비율. KLD 등 전체 수치: [`results/quant/summary.txt`](results/quant/summary.txt)
- 측정: HF 원본 fp32 logits를 `llama-perplexity --kl-divergence-base` 포맷으로 저장해 토큰 단위 비교. 한국어·영어 위키백과(20231101) 각 약 3만 토큰.
- imatrix 보정 데이터: 평가 구간과 겹치지 않는 한국어/영어 위키백과 + 채팅 템플릿 QA 샘플 (161K 토큰).
- tied embedding(=출력층)은 기본적으로 Q6_K로 유지된다. 이 모델은 **4bit에 민감**해 5bit→4bit에서 손실이 급증하므로 Q5_K_M-im을 권장한다.

### 기존 공개 GGUF(Qwen3 매핑)와의 차이

기존에 공개된 일부 GGUF는 config를 `Qwen3ForCausalLM`으로 바꿔 변환한 것입니다. 이 방식에서는 **sliding window attention과 full-attention 층의 YaRN(factor 40)이 사라져** 원본과 다르게 동작합니다.

| 한국어 PPL | 원본 | Qwen3 매핑 Q4_K_M | 이 저장소 Q4_K_M-im | 이 저장소 Q5_K_M-im |
|---|---|---|---|---|
| ctx 512 | 16.57 | 19.64 (+19%) | +6.9% | +2.6% |
| ctx 4096 | 14.09 | 31.68 (+125%) | +7.2% | +2.1% |
| ctx 16384 | 13.25 | 붕괴 | – | – |

YaRN은 짧은 문맥에서도 attention 스케일(×1.369)과 저주파 RoPE 차원을 바꿉니다. 그래서 매핑 방식은 1024토큰 이내에서도 원본과 다릅니다(top-1 일치율 약 82%). 패치된 f16 GGUF는 HF 원본과 KLD ≈ 1e-6, top-1 일치율 99.9% 이상입니다(ctx 512~16K).

## 사용 방법

### 1. 패치된 llama.cpp 빌드

기준 커밋 `4da6337767f973e2b4d0797e5b323d77d8565e4a`에 `kanana2tiny` 아키텍처 패치를 적용합니다.

```bash
git clone https://github.com/ggml-org/llama.cpp && cd llama.cpp
git checkout 4da6337767f973e2b4d0797e5b323d77d8565e4a
git am 0001-model-add-Kanana-2-Tiny-kanana2tiny-architecture.patch
cmake -B build -DCMAKE_BUILD_TYPE=Release && cmake --build build -j
```

### 2. 실행

```bash
./build/bin/llama-cli -m kanana2tiny-Q5_K_M-im.gguf --jinja -c 4096 -t 4 -fa off -lm none
```

- `--jinja`: Kanana 채팅 템플릿을 적용합니다. 기본값은 `thinking_mode = no_think`입니다.
- **모바일 CPU 권장 옵션**(Galaxy S20 실측 기준):
  - `-t <성능 코어 수>`
  - `-fa off`: 끄면 긴 문맥 생성 속도가 +58%입니다.
  - `-lm none`: mmap을 끕니다. 기본 mmap에 CPU repack이 겹치면 가중치가 메모리에 이중으로 올라가서, 끄면 메모리가 -31%입니다.
- 앱에 임베드할 때 llama.cpp C API의 기본값 `swa_full=true`는 `false`로 바꾸기를 권장합니다. KV 캐시가 약 240MB 줄어듭니다.
- 멀티턴을 직접 구현한다면 템플릿 인자 `preserve_thinking=true`로 포맷하세요. 이 템플릿은 이전 assistant 턴에서 `<think></think>`를 빼고 렌더링하기 때문에, 과거 포맷과의 차이만 잘라 붙이는 방식이 어긋납니다.

### 실기기 참고치 (CPU, Q5_K_M-im, ctx 4096)

| 기기 | 짧은 대화 생성 | 1.5K토큰 입력 후 생성 | 메모리 |
|---|---|---|---|
| Galaxy S20 (Snapdragon 865, 4스레드) | 18.6 tok/s | 11.9 tok/s | 약 1.55 GB |
| Galaxy S23 Ultra (Snapdragon 8 Gen 2, 4스레드, 샘플 앱) | 약 18~19 tok/s | – (미측정) | 약 1.52 GB |

## 수정 내역 (Modifications)

- 원본 BF16 가중치를 패치된 llama.cpp 변환기(`Kanana2TinyForCausalLM` → `kanana2tiny`)로 f16 GGUF로 변환했습니다. 가중치 값 자체는 수정하지 않았습니다.
- imatrix를 생성해 Q4_K_M / Q5_K_M / Q6_K로 양자화했습니다. tied embedding(=출력층)은 Q6_K를 유지했습니다.
- GGUF 메타데이터 `general.name`을 "Kanana 2 1.3b Instruct"로 설정했습니다.
- 변환·양자화 환경: x86_64 Linux (llama.cpp CPU 빌드). ARM(Mac)에서 같은 절차로 양자화하면 비트 단위로는 달라지지만 품질은 오차 범위 내 동일함을 확인(Q5_K_M-im: KLD 0.0275 vs 0.0269)
- 수정자: winwinplatform, 2026-09

## 라이선스 및 사용 제한

이 모델은 **Kanana Open License Agreement**의 파생물(Derivative Works)입니다. 전문은 동봉된 [LICENSE](LICENSE)와 [NOTICE](NOTICE)를 참고하세요.

- Kanana is licensed in accordance with the Kanana Open License Agreement. Copyright © KAKAO Corp. All Rights Reserved.
- 사용 시 관련 법령과 KAKAO의 **Guidelines For Responsible AI**(금지 사용 정책, License §2.2)를 따라야 합니다. 재배포할 때는 후속 사용자에게도 같은 제한이 적용됨을 알려야 합니다.
- 다음 경우에는 KAKAO의 **별도 상업 라이선스**가 필요합니다(License §4.1).
  - API·클라우드로 제3자에게 제공하는 경우
  - SI·온프레미스로 납품하는 경우
  - **온디바이스 제품에 임베드해 제3자에게 제공·판매하는 경우**

## 결과 파일 (`results/`)

| 경로 | 내용 |
|---|---|
| `results/quant/summary.txt` | 양자화 13종 요약표 (dPPL, KLD, top-1, 99% KLD) |
| `results/quant/*.log` | 변형별 `llama-perplexity` KLD 원시 로그 (ko 512 / ko 4096 / en 4096) |
| `results/eval/hf_variants.json` | HF에서 YaRN/SWA 제거 변형의 PPL·KLD (Qwen3 매핑 손실 분석) |
| `results/eval/kld_k2f16_*.log` | 패치 f16 GGUF vs HF 원본 검증 (ctx 4096, 16384) |
| `results/eval/ppl_*.log`, `kld_qwen3map-*.log` | Qwen3 매핑 GGUF(기존 공개 방식)와 공개 Q4_K_M 측정 |
| `results/device/` | Galaxy S20 실측 (스레드, 4종 속도, 긴 문맥, FA/KV, mmap·repack별 메모리) |

## 체크섬

[`SHA256SUMS`](SHA256SUMS) 참고.
