---
license: apache-2.0
base_model:
- neureps/Qwen3.5-2B-enko
language:
- ko
- en
pipeline_tag: image-text-to-text
tags:
- gguf
- llama.cpp
- imatrix
- korean
- warmly
---

# warmly-qwen35-2b-enko-gguf — Warmly 프로덕션 모델 (프루닝 2B GGUF)

오프라인 SNS 앱 [Warmly(온기)](https://github.com/neureps/warmly)의 **프로덕션 배포 리포**입니다. EN/KO 어휘 프루닝 마스터 [neureps/Qwen3.5-2B-enko](https://huggingface.co/neureps/Qwen3.5-2B-enko)를 llama.cpp로 양자화했습니다. Android 앱(내장 llama-server)이 루트의 배포 파일을 직접 다운로드합니다.

## 버전 이력

| 버전 | 날짜 | 텍스트 본체 | 상태 | 개선 내용 (실측) |
| --- | --- | --- | --- | --- |
| distill-v1 | 2026-07-15 | `Qwen3.5-2B-enko-distill-v1-dIQ4_XS.gguf` | **게이트 통과 — 승격 대기** (프로덕션 전환은 별도 결정) | **한국어 자연성 증류** ([어댑터 리포](https://huggingface.co/neureps/warmly-qwen35-2b-enko-distill) v1 병합). Kanana-1.5-8B 교사 QLoRA — 어색 ~18/60→~6/60, 깨진 단어·환각 해소, 구체성 2.5→3.5+. 공식 게이트: 블라인드 승률 ~70%, 자기비하 동조 0/4, 후처리 55/60+재생성 폴백 0. 크기 1022MB |
| **base** | 2026-07-14 (앱 v0.2.15) | `Qwen3.5-2B-enko-dIQ4_XS.gguf` | **현행 프로덕션** | 어휘 프루닝(−9% 무손실)+도메인 imatrix IQ4_XS — 구 배포(1564MB) 대비 −363MB, 하니스 20/20 |

## 파일 (루트 — 프로덕션 파일명 변경 금지, 앱이 URL로 고정 참조)

| 파일 | 크기 | 설명 |
| --- | --- | --- |
| `Qwen3.5-2B-enko-dIQ4_XS.gguf` | 975MB | **현행 배포 본체 (base).** IQ4_XS + 도메인 imatrix |
| `Qwen3.5-2B-enko-distill-v1-dIQ4_XS.gguf` | 1022MB | **증류 v1 — 게이트 통과, 승격 대기.** 증류 병합본 + 도메인 imatrix(재산출) IQ4_XS. heldout PPL 11.85(댓글 도메인 특화로 위키 PPL은 상승 — 품질 지표 아님, 블라인드 승률이 판정) |
| `Qwen3.5-2B-enko-mmproj-q5_0.gguf` | 228MB | **배포 비전 프로젝터(공용).** 텍스트 LoRA와 무관해 두 버전이 공유. q8_0 대비 캡션 greedy 구별 불가 |
| `imatrix-domain-distill-v1.gguf` | 1.9MB | distill-v1 병합본에서 재산출한 도메인 imatrix (imatrix는 모델 종속 — base 것 재사용 불가) |
| `imatrix-domain.gguf` | 1.9MB | base용 도메인 imatrix (캘리브레이션 = `calib.txt`) |
| `imatrix-general.gguf` | 1.9MB | base용 일반 imatrix (캘리브레이션 = `calib-general.txt`) |
| `calib.txt` | 365KB | **도메인** 캘리브레이션 텍스트 — 페르소나 프롬프트 + 앱 학습 JSONL(영어 캡션+한국어 댓글) (양 버전 공용, 재현용) |
| `calib-general.txt` | 2MB | **일반** 캘리브레이션 텍스트 — KO/EN 위키+감성 댓글 표본 (재현용) |

현행 배포 구성 합계(base+q5_0) **1201MB** — 공식 하니스 20/20, heldout PPL 10.91, v0.2.15부터. distill-v1의 제작 과정·잔존 특성(복잡 캡션 영어 누출 → 후처리+재생성이 흡수, 폴백 0)은 [어댑터 리포 카드](https://huggingface.co/neureps/warmly-qwen35-2b-enko-distill)와 학습 데이터 [warmly-distill-data](https://huggingface.co/datasets/neureps/warmly-distill-data) 참조.

## 양자화 변형 (`variants/` — A안 실측 스윕 전체, 2026-07-13)

파일명 규칙: `Qwen3.5-2B-enko-{양자화}-{imatrix 종류}.gguf`
- `imatrix-domain` = 도메인 캘리브레이션(위 `imatrix-domain.gguf`) / `imatrix-general` = 위키+댓글(`imatrix-general.gguf`) / `plain` = imatrix 없음

| 파일 (variants/) | 크기 | PPL(heldout) | 실측 판정 |
| --- | --- | --- | --- |
| `...-Q4_K_M-plain.gguf` | 1.1GB | 10.94 | imatrix 없음 — 한국어 단어 오류("소파/소거"류), 비권장 |
| `...-Q4_K_M-imatrix-general.gguf` | 1.1GB | **10.70** | 동크기 최고 품질 |
| `...-IQ4_XS-imatrix-general.gguf` | 975MB | 10.87 | −12% 크기인데 plain Q4_K_M보다 나음 — 스위트스팟 |
| `...-Q3_K_M-imatrix-general.gguf` | 883MB | 12.10 | +10% 열화, 크기 절박할 때만 |
| `...-Q4_K_M-imatrix-domain.gguf` | 1.1GB | 10.75 | 후처리 통과 19/20, 어색 ~3 |
| `...-IQ3_M-imatrix-domain.gguf` | 845MB | 11.82 | 오역·환각 증가 시작 (usable-but-degraded) |
| `...-IQ3_XXS-imatrix-domain.gguf` | 745MB | 13.33 | **의미 붕괴 — 사용 부적합.** 단 후처리 통과 19/20 → 통과율은 저비트 붕괴를 못 잡는다는 실측 증거로 보존 |
| `...-mmproj-f16.gguf` | 638MB | — | 비전 프로젝터 원본 (llama.cpp 변환기는 q8_0까지만 지원) |
| `...-mmproj-q8_0.gguf` | 348MB | — | 구 배포(v1) 페어링 |
| `...-mmproj-q4_0.gguf` | 189MB | — | 자체 재양자화(mmproj_requant.py). 4/5 대등, 애매한 피사체(food)에서 환각 드리프트 — 크기 절박할 때만 |

핵심 교훈: **후처리 통과율은 저비트 열화를 못 잡는다** — 진짜 판별자는 자연성(주관 평가)이며 PPL과 강하게 상관. 2B는 품질을 유지하며 1GB 언더가 불가능(유일한 1GB 언더 IQ3_XXS는 붕괴).

## 사용법 (llama.cpp)

```bash
# 텍스트 (댓글 생성) — enable_thinking:false 필수, 안 끄면 출력이 빔
llama-server -m Qwen3.5-2B-enko-dIQ4_XS.gguf -c 4096
# 비전 (캡션)
llama-mtmd-cli -m Qwen3.5-2B-enko-dIQ4_XS.gguf --mmproj Qwen3.5-2B-enko-mmproj-q5_0.gguf --image photo.jpg -p "Describe..."
```

## 관련 리포

- 프루닝 마스터(safetensors): [neureps/Qwen3.5-2B-enko](https://huggingface.co/neureps/Qwen3.5-2B-enko)
- 구 배포 v1(프루닝 전, 롤백용): [neureps/warmly-qwen35-2b-gguf](https://huggingface.co/neureps/warmly-qwen35-2b-gguf)
- 0.8B GGUF: [neureps/warmly-qwen35-08b-enko-gguf](https://huggingface.co/neureps/warmly-qwen35-08b-enko-gguf)
