# 골든셋 v3 질문 품질 보고서

> 기준 코퍼스 sync_run_id `cb1b5e48-11dd-4018-bf6b-d48b8a76054b` · active 4,017 · 상태: 초안 + 전수 스캔 + 검수 준비 완료(사람 판정 전). 아래 '정답'은 모두 Claude 제안 기준이다.

## 유형·표현·페르소나

| 유형 | 질문 수 | 기술형 | 목적형 | 혼합형 | easy | hard |
|---|---|---|---|---|---|---|
| structured_constraint (구조화 조건) | 10 | 5 | 0 | 5 | 10 | 0 |
| semantic_capability (의미 능력) | 10 | 2 | 6 | 2 | 3 | 7 |
| semantic_constraint (의미 + 조건) | 10 | 2 | 2 | 6 | 0 | 10 |
| lexical_exact (모델명 지목) | 10 | 5 | 2 | 3 | 10 | 0 |
| model_comparison (모델 비교) | 10 | 5 | 2 | 3 | 10 | 0 |
| benchmark_lookup (벤치마크 조회) | 10 | 5 | 2 | 3 | 0 | 10 |
| abstention (정답 없음(기권)) | 10 | 3 | 2 | 5 | 0 | 10 |

전체 표현 비율: 기술형 27 (39%), 혼합형 27 (39%), 목적형 16 (23%)

페르소나: ml_engineer 16, startup_dev 14, backend_dev 13, korean_service_planner 9, local_user 8, researcher 6, limited_gpu 4

- 쿼터 예외 — structured_constraint 의 목적형: 이 유형은 수치·포맷·라이선스 조건을 사용자가 직접 말해야 성립한다. 목적만 말하는 질문으로 쓰면 조건을 추론해 넣어야 하므로(숨은 조건) 목적형 대신 혼합형으로 상황을 함께 담았다.

## 조건 사용

| 조건 키 | 질문 수 |
|---|---|
| `tasks` | 36 |
| `require_artifact` | 21 |
| `max_parameters_billion` | 12 |
| `licenses` | 12 |
| `commercial_status` | 11 |
| `max_artifact_gib` | 5 |
| `min_context_length` | 4 |
| `exclude_gated` | 1 |

- 상업 이용·라이선스 조건 질문: 23개
- 파라미터·컨텍스트 수치 조건 질문: 15개
- GGUF·ONNX 등 파일 형식·크기 조건 질문: 22개
- 순수 의미 질문(semantic_capability 중 task 외 조건 없음): 10개

## 제안 정답 분포

- pool: {'low_popularity': 279, 'core': 216} (2점 {'low_popularity': 142, 'core': 124}, 1점 {'low_popularity': 137, 'core': 92})
- 근거가 확인된 단계: {'model_id': 228, 'filter_metadata': 132, 'benchmark_metadata': 71, 'semantic_metadata': 51, 'technical_metadata': 9, 'canonical_model_id': 4}
- 같은 canonical family 상위: LGAI-EXAONE/EXAONE-4.0-1.2B ×18, google/madlad400-3b-mt ×13, LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct ×12, jhu-clsp/mmBERT-base ×11, tencent/Hy-MT2-1.8B ×10, FunAudioLLM/SenseVoiceSmall ×8, jhu-clsp/mmBERT-small ×6, Qwen/Qwen3-1.7B ×6, kakaocorp/kanana-1.5-2.1b-instruct-2505 ×6, Qwen/Qwen3.6-35B-A3B ×6, nvidia/nemotron-3.5-asr-streaming-0.6b ×5, trillionlabs/Tri-1.8B-Translation ×5, Qwen/Qwen2.5-7B-Instruct ×5, zai-org/GLM-OCR ×5, openai/whisper-large-v3-turbo ×4

## 질문별 수

| query | eligible | 2점 제안 | 1점 제안 | 사람 판단 | 검수 대상 | unknown 때문에 제외 | 최대 family 중복 |
|---|---|---|---|---|---|---|---|
| st01 | 23 | 23 | 0 | 0 | 23 | 18 | 2 |
| st02 | 12 | 12 | 0 | 0 | 12 | 1 | 2 |
| st03 | 21 | 21 | 0 | 0 | 21 | 16 | 6 |
| st04 | 5 | 5 | 0 | 0 | 5 | 0 | 1 |
| st05 | 5 | 5 | 0 | 0 | 5 | 0 | 1 |
| st06 | 10 | 6 | 4 | 0 | 10 | 0 | 2 |
| st07 | 17 | 17 | 0 | 0 | 17 | 20 | 3 |
| st08 | 13 | 5 | 8 | 0 | 13 | 43 | 7 |
| st09 | 15 | 4 | 11 | 0 | 15 | 2 | 3 |
| st10 | 3 | 3 | 0 | 0 | 3 | 4 | 1 |
| sc01 | 2,346 | 3 | 0 | 1 | 4 | 0 | 1 |
| sc02 | 157 | 2 | 2 | 0 | 4 | 0 | 1 |
| sc03 | 157 | 1 | 15 | 2 | 18 | 0 | 5 |
| sc04 | 537 | 1 | 2 | 0 | 3 | 0 | 2 |
| sc05 | 321 | 7 | 4 | 12 | 23 | 0 | 7 |
| sc06 | 4,017 | 3 | 7 | 4 | 14 | 0 | 1 |
| sc07 | 4,017 | 6 | 1 | 1 | 8 | 0 | 2 |
| sc08 | 157 | 3 | 2 | 5 | 10 | 0 | 2 |
| sc09 | 338 | 3 | 1 | 2 | 6 | 0 | 1 |
| sc10 | 4,017 | 6 | 1 | 3 | 10 | 0 | 1 |
| sx01 | 28 | 0 | 4 | 0 | 4 | 0 | 2 |
| sx02 | 101 | 8 | 8 | 0 | 16 | 0 | 2 |
| sx03 | 968 | 4 | 8 | 1 | 13 | 261 | 2 |
| sx04 | 152 | 2 | 1 | 1 | 4 | 10 | 1 |
| sx05 | 72 | 0 | 4 | 3 | 7 | 96 | 3 |
| sx06 | 146 | 7 | 12 | 5 | 24 | 41 | 7 |
| sx07 | 115 | 0 | 10 | 2 | 12 | 26 | 5 |
| sx08 | 2,363 | 2 | 7 | 3 | 12 | 244 | 1 |
| sx09 | 720 | 4 | 9 | 10 | 23 | 586 | 3 |
| sx10 | 747 | 1 | 0 | 0 | 1 | 172 | 1 |
| lx01 | 4,017 | 1 | 0 | 0 | 1 | 0 | 1 |
| lx02 | 4,017 | 2 | 2 | 0 | 4 | 0 | 2 |
| lx03 | 4,017 | 1 | 9 | 0 | 10 | 0 | 9 |
| lx04 | 4,017 | 1 | 1 | 0 | 2 | 0 | 2 |
| lx05 | 4,017 | 1 | 0 | 0 | 1 | 0 | 1 |
| lx06 | 189 | 1 | 0 | 0 | 1 | 0 | 1 |
| lx07 | 1,643 | 4 | 0 | 0 | 4 | 0 | 2 |
| lx08 | 4,017 | 1 | 2 | 0 | 3 | 0 | 2 |
| lx09 | 4,017 | 1 | 1 | 0 | 2 | 0 | 2 |
| lx10 | 4,017 | 1 | 3 | 0 | 4 | 0 | 4 |
| mc01 | 4,017 | 6 | 0 | 0 | 6 | 0 | 1 |
| mc02 | 4,017 | 3 | 21 | 0 | 24 | 0 | 12 |
| mc03 | 4,017 | 1 | 10 | 0 | 11 | 0 | 4 |
| mc04 | 4,017 | 6 | 19 | 0 | 25 | 0 | 7 |
| mc05 | 4,017 | 2 | 10 | 0 | 12 | 0 | 9 |
| mc06 | 4,017 | 2 | 2 | 0 | 4 | 0 | 2 |
| mc07 | 321 | 3 | 9 | 0 | 12 | 0 | 6 |
| mc08 | 4,017 | 2 | 9 | 0 | 11 | 0 | 3 |
| mc09 | 4,017 | 2 | 0 | 0 | 2 | 0 | 1 |
| mc10 | 4,017 | 2 | 1 | 0 | 3 | 0 | 1 |
| bl01 | 4,017 | 7 | 0 | 0 | 7 | 0 | 3 |
| bl02 | 4,017 | 13 | 0 | 0 | 13 | 0 | 1 |
| bl03 | 321 | 13 | 0 | 0 | 13 | 0 | 3 |
| bl04 | 4,017 | 3 | 0 | 0 | 3 | 0 | 1 |
| bl05 | 4,017 | 2 | 0 | 0 | 2 | 0 | 1 |
| bl06 | 4,017 | 2 | 0 | 0 | 2 | 0 | 1 |
| bl07 | 4,017 | 4 | 3 | 0 | 7 | 0 | 2 |
| bl08 | 4,017 | 6 | 0 | 0 | 6 | 0 | 3 |
| bl09 | 4,017 | 5 | 3 | 0 | 8 | 0 | 3 |
| bl10 | 4,017 | 4 | 3 | 0 | 7 | 0 | 2 |
| ab01 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ab02 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ab03 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ab04 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ab05 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ab06 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ab07 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ab08 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ab09 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ab10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## abstention near-miss

| query | 조건 하나만 불충족한 near-miss | 단일 조건 완화 후보 | temptation | 극단성 |
|---|---|---|---|---|
| ab01 | {'licenses': 6, 'max_parameters_billion': 3, 'require_artifact': 3, 'tasks': 22} | {'licenses': 6, 'max_parameters_billion': 3, 'require_artifact': 3, 'tasks': 22} | 22 | 통과 |
| ab02 | {'licenses': 4, 'min_context_length': 5, 'tasks': 3} | {'licenses': 4, 'min_context_length': 5, 'require_artifact': 0, 'tasks': 3} | 5 | 통과 |
| ab03 | {'licenses': 12, 'require_artifact': 15, 'tasks': 119} | {'licenses': 12, 'require_artifact': 15, 'tasks': 119} | 119 | 통과 |
| ab04 | {'licenses': 8, 'require_artifact': 17, 'tasks': 6} | {'licenses': 8, 'require_artifact': 17, 'tasks': 6} | 17 | 통과 |
| ab05 | {'licenses': 3, 'max_parameters_billion': 4, 'require_artifact': 2, 'tasks': 101} | {'licenses': 3, 'max_parameters_billion': 4, 'require_artifact': 2, 'tasks': 101} | 101 | 통과 |
| ab06 | {'licenses': 27, 'min_context_length': 10, 'require_artifact': 8, 'tasks': 90} | {'licenses': 27, 'min_context_length': 10, 'require_artifact': 8, 'tasks': 90} | 90 | 통과 |
| ab07 | {'licenses': 4, 'require_artifact': 25, 'tasks': 40} | {'licenses': 4, 'max_parameters_billion': 0, 'require_artifact': 25, 'tasks': 40} | 40 | 통과 |
| ab08 | {'licenses': 3, 'require_artifact': 18, 'tasks': 54} | {'licenses': 3, 'max_artifact_gib': 0, 'require_artifact': 18, 'tasks': 54} | 54 | 통과 |
| ab09 | {'licenses': 104, 'require_artifact': 1, 'tasks': 2} | {'licenses': 104, 'require_artifact': 1, 'tasks': 2} | 104 | 통과 |
| ab10 | {'licenses': 8, 'require_artifact': 10, 'tasks': 191} | {'licenses': 8, 'require_artifact': 10, 'tasks': 191} | 191 | 통과 |
