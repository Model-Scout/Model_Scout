---
language:
  - ko
  - en
license: other
license_name: batiai-community-v2
license_link: https://github.com/batiai/batiai-models/blob/main/LICENSE-BATIAI-COMMUNITY.md
tags:
  - automatic-speech-recognition
  - whisper
  - whisper-turbo
  - korean
  - speech-recognition
  - audio
  - asr
  - batiai
  - batisay
  - gguf
  - whisper.cpp
  - realtime
  - telephone
library_name: ggml
base_model: openai/whisper-large-v3-turbo
pipeline_tag: automatic-speech-recognition
---

# batisay-ko-turbo — 온디바이스 한국어 STT (통화·회의·대화)

> **로컬에서 도는 한국어 통화·회의 STT.** 오디오는 기기 밖으로 나가지 않고, 분당 과금도 없습니다.
> **212초 통화를 Mac Studio에서 ~5초에 전사** (41× 실시간, whisper.cpp Metal 실측 · 2026-07-31 팀 스모크).
> ✅ **추천 기본 모델: 이 모델의 `q5_0`** — 통화·회의·대화·강의 전 도메인.

**Quickstart (whisper.cpp — 주 경로):**
```bash
hf download batiai/batisay-ko-turbo ggml-batisay-ko-turbo-q5_0.bin --local-dir .
whisper-cli -m ggml-batisay-ko-turbo-q5_0.bin -l ko -f audio.wav \
  --suppress-nst --max-context 0 --output-txt
```
Mac 경로는 **whisper.cpp 또는 MLX**([batisay-ko-turbo-mlx](https://huggingface.co/batiai/batisay-ko-turbo-mlx)) 권장. Transformers `AutoProcessor` 는 2026-08-01 호환 핫픽스 반영됨(4.57+).

**내 Mac/PC에서 바로 돌리는 한국어 음성-텍스트 변환 모델.** 실제 전화 통화·회의·일상 대화에 강하고, 서버 없이 오프라인으로 동작합니다. 51분 통화를 약 1분에 전사(실시간 대비 최대 ~58배).

- 🎙️ **멀티도메인**: 통화(8kHz)·회의(다화자)·강의·일상 대화·일반 음성
- 🍎 **온디바이스**: Apple Silicon(MLX)·whisper.cpp(Mac/Linux/Windows/iOS/Android), 음성 외부 전송 없음
- 🔓 **공개 배포**: 게이트/로그인 없이 자유 다운로드 (상업 조건은 아래 라이선스)
- 베이스: [OpenAI Whisper large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo) (809M) 한국어 파인튜닝

> 🍎 **Mac 사용자**: 더 빠른 **MLX 버전** 있음 → [`batiai/batisay-ko-turbo-mlx`](https://huggingface.co/batiai/batisay-ko-turbo-mlx)
> 🔓 **완전 무료(Apache 2.0)** 가 필요하면 → [`batiai/batisay-ko-base`](https://huggingface.co/batiai/batisay-ko-base) (일반 음성 중심)

<!-- BENCH-START -->
## 정확도 (CER, 낮을수록 정확)

### 도메인별 — N=500/도메인, 엄격 정규화
| 도메인 | **turbo** | base | large | 측정셋 |
|---|---|---|---|---|
| 일상 대화 | **3.00%** | — | — | 자연 대화 |
| 상담 통화 (8kHz, in-domain) | **5.67%** | — | 10.00% | 콜센터 벤치셋 |
| 일반 음성 (깨끗) | **6.99%** | 7.77% | 7.41% | KsponSpeech eval_clean |
| 일반 음성 (소음) | **8.33%** | 12.28% | 8.49% | KsponSpeech eval_other |
| 회의 (다화자, 16kHz) | **8.90%** | — | 9.87% | 다화자 회의 |

> 측정: GPU(transformers), 도메인당 500발화. 상담 5.67%는 **콜센터 in-domain 벤치**로, 아래 실사용 장문 통화와는 별개입니다.

### 실사용 장문 통화 (2~51분)
| 모델 | 실통화 CER |
|---|---|
| **batisay-ko-turbo (MLX)** | **14.85%** |
| **batisay-ko-turbo (ggml q5_0, 배포본)** | **17.1%** |
| batisay-ko-base | 19.11% |

> 실제 사용자 통화 5건(2·4·8·12·51분, 약 27,000자 — 그중 51분 1건이 약 72%)의 **소표본** 측정.
> 참조 전사가 사람 정답이 아닌 자동 전사 기준이라 **절대치보다 버전/포맷 간 상대비교 지표**입니다(정식 정답셋 확대 예정).
> 51분 초장문: base 31.1% / 이전 버전 30.3% → **현재 19.4%**.
<!-- BENCH-END -->

## 속도 (Mac M4 Max, 동일 7.8분 통화 실측)

| 포맷 | 크기 | rtf | 7.8분 통화 | 51분 통화 |
|---|---|---|---|---|
| **MLX fp16** | 1.6 GB | **0.017** (~58×) | 8.2초 | 0.9분 |
| **ggml q5_0** ⭐ | 548 MB | **0.026** (~38×) | 12.2초 | 1.3분 |
| ggml q4_0 | 453 MB | 0.028 | 13.3초 | 1.4분 |
| ggml q8_0 | 834 MB | 0.036 | 16.7초 | 1.8분 |

> `rtf = 처리시간 / 오디오길이` (작을수록 빠름). **q5_0** 이 속도·품질·크기 밸런스로 배포 기본값, **MLX fp16** 이 최고 속도·정확도.

## 사용 방법

### whisper.cpp (Mac / Linux / Windows / iOS / Android)
```bash
hf download batiai/batisay-ko-turbo ggml-batisay-ko-turbo-q5_0.bin --local-dir .

# 권장 (전 도메인 기본값)
./whisper-cli -m ggml-batisay-ko-turbo-q5_0.bin -l ko -f audio.wav \
    --suppress-nst --max-context 0 --output-txt
```
> `--suppress-nst --max-context 0` 은 **장문 전사 시 침묵/전환 구간의 반복 환각·디코더 붕괴를 방지**합니다
> (60분+ 어닝콜에서 재무 수치 recall ~83% 확보). 표준 단문에서 무회귀 검증 → **전 도메인 기본 권장**.
> 실시간 streaming 은 `whisper.cpp/examples/stream` 사용.

### MLX (Apple Silicon 최적)
```python
import mlx_whisper
r = mlx_whisper.transcribe("audio.wav", path_or_hf_repo="batiai/batisay-ko-turbo-mlx",
                           language="ko", condition_on_previous_text=False)
```
> 자세한 옵션·fp16 변형은 [MLX 카드](https://huggingface.co/batiai/batisay-ko-turbo-mlx) 참조.

### BatiFlow App
녹음 → 자동 전사 → AI 요약 → 회의록. batisay-ko-turbo 가 표준 STT 엔진으로 임베드(무료).

## 모델 정보

- **베이스**: OpenAI Whisper large-v3-turbo (809M, encoder = Large v3)
- **학습**: 3-cycle 점진 학습, 엄선한 약 4,300시간 (가용 25,000시간+ 중 품질 우선 선별).
  일반(KsponSpeech)·회의·강의·일상 대화·콜센터 통화(8kHz)·소음 통화 — 한국어 멀티도메인, AI Hub 기반.
- **정제 라벨**: 전사 주석 제거 → 깨끗한 출력. 각 사이클 KsponSpeech 재학습으로 기존 도메인 성능 유지.
- **버전**: v1.1 (2026-06-20) — `batisay-ko-base` 위에 통화 데이터 다양화 + 상담 과적합 제거로 실사용 장문 통화 정확도를 회복. 멀티도메인은 v1.0 동급 유지.

## base vs turbo — 어느 걸 쓸까

| | **batisay-ko-base** | **batisay-ko-turbo** (본 모델) |
|---|---|---|
| 라이선스 | Apache 2.0 (완전 무료, 외부 SaaS OK) | Community v2 (공개·무게이트, 상업 협의) |
| 학습 도메인 | 일반 (KsponSpeech) | 일반 + 회의 + 통화 + 대화 |
| 실사용 통화 | 19.11% | **14.85%** |
| 추천 | 무료·외부 SaaS 임베드 | 통화·회의·대화 정확도 우선 (BatiFlow 표준) |

## 양자화

| 포맷 | 크기 | 권장 RAM |
|---|---|---|
| q5_0 ⭐ | 548 MB | 2 GB+ |
| q4_0 (lite) | 453 MB | 1 GB+ |
| q8_0 | 834 MB | 2 GB+ |
| f32 | 1.6 GB | 4 GB+ |

## 라이선스 — BatiAI Community v2

공개 다운로드(게이트 없음). **개인·사내 도구·연구·비영리·공공 = 자유 사용.**
외부 SaaS·재판매·연매출 10억원 이상 상업 사용 = **support@bati.ai 협의.** 출시 4년 후 Apache 2.0 자동 전환.
전문: [LICENSE-BATIAI-COMMUNITY.md](https://github.com/batiai/batiai-models/blob/main/LICENSE-BATIAI-COMMUNITY.md)

## 변경 이력

- **v1.1 (2026-06-20)** — 실사용 장문 통화 정확도 회복 (실통화 14.85% MLX / 17.1% ggml, base 19.11% 대비 개선; 51분 통화 base 31.1% → 19.4%). 멀티도메인 v1.0 동급 유지.
- **v1.0 (2026-06-15)** — 첫 출시 (통화·회의·대화 멀티도메인 3-cycle 학습).

## 문의
- 라이선스 / 임베드 협의: **support@bati.ai** · [HF Discussions](https://huggingface.co/batiai/batisay-ko-turbo/discussions) · [flow.bati.ai](https://flow.bati.ai)
