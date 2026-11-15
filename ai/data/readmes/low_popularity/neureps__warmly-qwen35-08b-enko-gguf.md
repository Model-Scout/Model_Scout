---
license: apache-2.0
base_model:
- neureps/Qwen3.5-0.8B-enko
language:
- ko
- en
pipeline_tag: image-text-to-text
tags:
- gguf
- llama.cpp
- korean
- warmly
- lora
---

# warmly-qwen35-08b-enko-gguf — 0.8B 온디바이스 소형 티어 (프루닝·증류 GGUF)

EN/KO 어휘 프루닝 마스터 [neureps/Qwen3.5-0.8B-enko](https://huggingface.co/neureps/Qwen3.5-0.8B-enko) 기반. [Warmly(온기)](https://github.com/neureps/warmly) 앱의 **소형 티어(저·중램 기기)** 배포 모델이자 이미지 캡셔너를 담는다. 한 모델이 캡션(비전)과 댓글(텍스트)을 모두 낸다.

## ★ 현재 배포 — `v3.1/` (2026-07-23)

**소형 티어 배포 = 증류 v3c 가중치(Q4_K_M) + 페르소나 어댑터.** "v3.1"은 판정 프로토콜을 새로 세운 뒤 재검증한 릴리스 라벨이다(**재학습 아님 — 베이스 가중치는 v3c**). base와 어댑터는 **한 몸으로** 배포한다.

| 파일 (`v3.1/`) | 크기 | 설명 |
| --- | --- | --- |
| `v3.1/Qwen3.5-0.8B-enko-distill-v3c-Q4_K_M-imatrix-domain.gguf` | 419MB | 텍스트 본체 (v3c 가중치·Q4_K_M·도메인 imatrix) |
| `v3.1/louie-v3.1-f16.gguf` | 12.2MB | 페르소나 어댑터(LoRA) — 5번째 캐릭터 "루이" |
| `Qwen3.5-0.8B-enko-mmproj-q8_0.gguf` (루트 공용) | 111MB | 비전 프로젝터 |

**스택 합계 ≈ 542MB.**

**페르소나 어댑터 방식:** 본체에는 4개 캐릭터가 학습돼 있고, 5번째 캐릭터만 12.2MB 어댑터로 얹는다. llama.cpp `--lora … --lora-init-without-apply`로 로드한 뒤 **요청별로 스케일을 토글**한다 — 기존 4인은 `scale 0`(본체와 출력이 글자까지 동일=항등), 루이는 `scale 1`. 캐릭터 추가에 본체 재배포가 필요 없다.

```bash
# llama-server 기동
llama-server -m v3.1/Qwen3.5-0.8B-enko-distill-v3c-Q4_K_M-imatrix-domain.gguf \
  --mmproj Qwen3.5-0.8B-enko-mmproj-q8_0.gguf \
  --lora v3.1/louie-v3.1-f16.gguf --lora-init-without-apply

# 요청 본문에서 페르소나별 스케일 (루이=1, 그 외=0)
curl .../completion -d '{"prompt":"...", "lora":[{"id":0,"scale":1}]}'
```

**품질(Gemma 4 12B 심사, gold144 N=144, 프로덕션 샘플링):** 루이 결함율 **13.2%**(회상 속 지명은 캐릭터 정의라 제외). 재양자화 전(Q5_K_M 베이스) 12.5%와 동급.

## 파일 구조

- **루트** — 캡셔너/폴백용 base GGUF + 공용 비전 프로젝터
  - `Qwen3.5-0.8B-enko-Q4_K_M.gguf` (419MB, 증류 전 base 텍스트 본체)
  - `Qwen3.5-0.8B-enko-mmproj-q8_0.gguf` (111MB, 비전 프로젝터 — 전 버전 공용)
- **`v3.1/`** — 현재 배포(위 참조)
- **`variants/`** — 증류 개선 이력(아래)
- **`adapters/`** — 페르소나 어댑터 원본 위치(`louie-v1-f16.gguf`, `v3.1/louie-v3.1`과 동일 가중치)

## `variants/` — 증류 개선 이력

증류 어댑터([`warmly-qwen35-08b-enko-distill`](https://huggingface.co/neureps/warmly-qwen35-08b-enko-distill))를 병합·재양자화한 GGUF. imatrix는 모델 종속이라 각 병합본에서 재산출한다(캘리브레이션 = 도메인 `calib.txt`).

| 버전 | 파일 | 판정 |
| --- | --- | --- |
| **v3c** ★현행 배포 계보 | `variants/…-distill-v3c-{IQ4_XS 395MB, Q4_K_M 419MB, Q5_K_M 466MB}-imatrix-domain.gguf` + `imatrix-domain-distill-v3c.gguf` | 혼합 피벗(하드워드 접지를 페르소나 목소리로 재생성해 혼합). 심사 결함율 v2 51%→**45%**·사물오접지 20→6·자기비하동조 0. **배포는 Q4_K_M**(양자화 재검 gold144 N=288에서 IQ4_XS≤Q4_K_M≤Q5_K_M, Q5 우위는 표본 노이즈였음) |
| v2 | `variants/…-distill-v2-{IQ4_XS 414MB, Q4_K_M 440MB}-…` + imatrix | 입력 커버리지 보강 — 자기비하 동조 0·영어누출 2→0·지명환각 11→0. v3c로 교체 |
| v1 | `variants/…-distill-v1-{IQ4_XS 395MB, Q4_K_M 419MB}-…` + imatrix | 레시피 이식 실증(블라인드 승률 ~79% vs base). 배포 부적합, 폴백 후보 |

## 사용 시 주의

- 추론 시 `enable_thinking: false` 필수(안 끄면 출력이 빔).
- 캡션: `llama-mtmd-cli -m <본체>.gguf --mmproj ...mmproj-q8_0.gguf --image 사진 -p "Describe..."`
- 어댑터는 **댓글(텍스트)에만** 영향 — 캡션 경로는 본체+mmproj 그대로.

## 관련 리포

- 프루닝 마스터(safetensors): [neureps/Qwen3.5-0.8B-enko](https://huggingface.co/neureps/Qwen3.5-0.8B-enko)
- 증류 어댑터: [neureps/warmly-qwen35-08b-enko-distill](https://huggingface.co/neureps/warmly-qwen35-08b-enko-distill)
- 2B 프로덕션 GGUF: [neureps/warmly-qwen35-2b-enko-gguf](https://huggingface.co/neureps/warmly-qwen35-2b-enko-gguf)
