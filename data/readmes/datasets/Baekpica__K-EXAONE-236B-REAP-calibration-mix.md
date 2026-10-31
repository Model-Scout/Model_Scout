---
license: other
license_name: mixed-source
language:
- ko
- en
size_categories:
- 10K<n<100K
task_categories:
- text-generation
tags:
- calibration
- pruning
- quantization
- REAP
- NVFP4
- k-exaone
- moe
configs:
- config_name: default
  data_files:
  - split: train
    path: mix.jsonl
---

# K-EXAONE-236B REAP/NVFP4 Calibration Mix

**LGAI-EXAONE/K-EXAONE-236B-A23B**의 expert pruning(REAP)과 NVFP4 양자화 calibration을 위해 제작한 믹스.
총 **16,780 샘플 / 101,157,434 토큰** (K-EXAONE 토크나이저 기준).

## 제작 목적

MoE 모델을 one-shot pruning/양자화하면 **reasoning 무한 반복**(한국어/영어 공통)이 발생하는 문제가 있어,
이를 방지하기 위해 아래 원칙으로 설계:

1. **Context length 다각화**: 16 토큰 ~ 245K 토큰 (짧은 지시 → 32K agentic 궤적 → 128K 장문 → 245K needle 스트레스)
2. **한국어 대량 포함** (instruction/reasoning/tool-calling) — K-EXAONE 특화 expert 보호
3. **reasoning trace 원형 보존** — `<think>...</think>` 종료 전이 토큰이 라우터 통계에 정확히 반영되도록 함
4. **tool parser 보호** — `<tool_call>`/`<tool_result>`/`<|tool_declare|>` 경로 포함
5. Cerebras REAP agentic mix (60~70%) + 한국어 (20~30%) + long-context (5~10%) + 256K 스트레스 (~1%)

## 포맷

JSONL, 각 행: `{"bucket": str, "source": str, "token_len": int, "text": str}`

- `text`: **K-EXAONE chat template이 이미 적용된 완성 문자열** (`<|user|>`/`<|assistant|>`/`<think>`/`<|endofturn|>` 등 포함).
  토크나이즈 시 `add_special_tokens=False` 권장 (K-EXAONE 토크나이저는 auto-BOS 없음).
- `token_len`: K-EXAONE 토크나이저 기준 토큰 수
- 일부 장문 샘플(`long_ctx` 절반, 스트레스 제외)은 chat 형식이 아닌 raw LM 텍스트

## 버킷 구성

| bucket | samples | tokens | 길이 분포 (min/p50/p90/max) | 원천 | 비고 |
|---|---|---|---|---|---|
| code_en | 2,048 | 1.08M | 46/425/793/6.4K | theblackcat102/evol-codealpaca-v1 | code generation |
| mot_code | 2,048 | 10.49M | 488/3.7K/11.4K/14.8K | open-r1/Mixture-of-Thoughts[code] | R1 reasoning trace, 2K/4K/8K/16K 층화 |
| mot_math | 2,048 | 9.88M | 267/3.7K/10.1K/15.2K | open-r1/Mixture-of-Thoughts[math] | 〃 |
| mot_science | 2,048 | 7.89M | 325/3.4K/7.5K/9.8K | open-r1/Mixture-of-Thoughts[science] | 〃 |
| tool_en | 2,048 | 0.83M | 90/358/700/2.2K | Salesforce/xlam-function-calling-60k | tools kwarg로 선언, tool_calls 형식 |
| agentic_swe | 2,048 | 43.65M | 1.3K/21.4K/32.4K/32.8K | SWE-bench/SWE-smith-trajectories | 멀티턴 tool 궤적, 32K 초과 시 턴 단위 트리밍 |
| ko_instr | 3,072 | 6.38M | 56/863/6.0K/16.2K | OLAIR/Open-R1-Ko-SFT-v2.0 (1024) · amphora/korean-reasoning-small (512) · NotoriousH2/HRM8K-Reasoning-Korean (512) · beomi/KoAlpaca-v1.1a (512) · MarkrAI/KoCommercial-Dataset (512) | 한국어 reasoning(<think> 포함) + non-reasoning 혼합 |
| ko_tool | 1,024 | 2.28M | 814/2.2K/2.7K/4.9K | irene93/function-calling-v3 (512) · iamjoon/ecommerce-fc-ko (256) · gyung/toolllama-korean (256, ChatML 파싱 후 재렌더) | 한국어 tool-calling. 원본 system_prompt의 타 모델식 tool 선언부는 제거하고 K-EXAONE 네이티브 tools 선언 사용 |
| long_ctx | 384 | 16.05M | 16.5K/34.7K/65.1K/122.5K | zai-org/LongAlign-10k (128) · Yukang/LongAlpaca-12k (96) · emozilla/pg19 (64) · heegyu/kowikitext 연결 (64) · maywell/korean_textbooks 연결 (32) | pg19/kowiki는 절반 chat-QA(제목/출판연도 등 메타데이터 기반 검증 가능 정답), 절반 raw |
| stress_256k | 12 | 2.63M | 189.1K/223.2K/244.3K/244.5K | kowiki+pg19+korean_textbooks 합성 | needle-in-haystack: 10%/50%/90% 위치에 비밀 코드 3개 삽입 → 마지막 user 질문 → assistant가 3개 모두 회수. late-position expert/라우팅 검증용 |

## 생성 규칙 상세

- 시드 42, 중복 없는 랜덤 샘플링
- MoT: `num_tokens` 컬럼 기반 [0,2K)/[2K,4K)/[4K,8K)/[8K,15.9K) 4구간 균등(각 512)
- SWE-smith: 토큰 수가 32K를 넘으면 마지막 턴 그룹(같은 role 연속 구간)부터 제거해 템플릿 구조를 보존한 채 축소, 3턴 미만이 되면 폐기
- HRM8K-Reasoning-Korean: `question/reasoning/answer` → `<think>\n{reasoning}\n</think>\n\n{answer}` 합성 (순수 한국어 reasoning trace)
- xLAM: `answers`를 K-EXAONE `<tool_call>` 포맷의 tool_calls로 변환, `tools`는 chat template의 tools kwarg로 선언
- stress: 본문을 목표 토큰에 맞춰 먼저 절단한 **후** needle 삽입 (needle 소실 방지), 조립→측정→확장→절단 수렴 루프로 길이 제어
- 재현: 동봉된 `build_calib_mix.py` (원천 데이터셋은 `/data/raw`에 hf CLI로 다운로드 후 실행)

## 사용처

1. **REAP expert pruning** (Cerebras REAP saliency 수집): 전체 16,780샘플 사용, 길이 오름차순 처리
2. **NVFP4(W4A4) GPTQ 양자화**: 버킷 균형 서브셋 ~1,536샘플 (`quantize_nvfp4.py`의 QUANT_MIX 비율), max_seq_len 8192

## 원천 라이선스

원천 데이터셋 라이선스가 상이하므로(MIT/Apache-2.0/CC-BY-4.0/CC-BY-SA 등) 본 레포는 private 유지 권장.
재배포 시 각 원천 라이선스를 확인할 것.
