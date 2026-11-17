# 골든셋 v3 검수 워크시트 — abstention (정답 없음(기권))

> 상태: **초안 + 전수 스캔 + 검수 준비 완료**. 아래 점수는 Claude 의 제안이며 정답이 아니다.
>
> 판정 입력: `python test/golden/v3/tools/judge.py <query_id> <model_id> --decision approve|2|1|exclude|hold --reason "…" --by <이름>`

## ab01 — 노트북에서 Ollama 로 돌릴 한국어 번역 모델을 찾고 있어요. MIT 라이선스이고 파라미터 1B 이하인 GGUF 모델이면 좋겠어요.

- 사용자 의도: MIT 라이선스 소형 GGUF 번역 모델
- persona / 표현: local_user / 혼합형 · 난이도 hard
- 기대 행동: abstain

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `licenses` | mit | MIT 라이선스 | 아니오(판정용) |
| `max_parameters_billion` | 1 | 파라미터 1B 이하 | 예 |
| `require_artifact` | gguf | Ollama 로 … GGUF 모델 | 예 |
| `tasks` | translation | 번역 모델 | 예 |

정답 기준: 조건을 모두 만족하는 모델이 코퍼스에 없다. 없다고 답하고 가까운 대안을 조건과 함께 설명하는 것이 정답이다.

| 조건 하나만 뺐을 때 | 후보 수 | 그 조건 하나만 불충족한 near-miss (최대 5) |
|---|---:|---|
| `licenses` | 6 | ikatrik/plamo-3-translate-0.8b-GGUF, mradermacher/OmniTranslate-1.0-GGUF, mradermacher/OmniTranslate-1.1-GGUF, mradermacher/OmniTranslate-1.1-i1-GGUF, mradermacher/plamo-3-translate-0.8b-GGUF |
| `max_parameters_billion` | 3 | tensorblock/llama3-eng-ko-8b-sl5-GGUF, tensorblock/llama3-pre1-pre2-inst3-lora3-mergkit-base-GGUF, tensorblock/llama_1-GGUF |
| `require_artifact` | 3 | alirezamsh/small100, sappho192/aihub-ja-ko-translator, sappho192/ffxiv-ja-ko-translator |
| `tasks` | 22 | Baekpica/DeepSeek-V4.1-Flash-1017-hVQ-GGUF, Baekpica/DeepSeek-V4.1-Flash-1017-iVQ-GGUF, Mattimax/DAC6.5-GGUF, cstr/internvl2-1b-crispembed-GGUF, cstr/multilingual-e5-small-GGUF |

- 조건 각각을 단독으로 만족하는 모델 수: licenses 383, max_parameters_billion 720, require_artifact 1643, tasks 280
- near-miss 합계 34개, temptation_count 22
- 극단성 검사: 통과
- 검수: 정말 정답이 없어야 하는지, near-miss 가 '조건 하나 차이'라는 설명이 맞는지 확인한다.

- 기권 확인: ☐ 정답 없음 확인 ☐ 보류 — `judge.py ab01 (abstain) --decision approve --reason … --by …`

## ab02 — 브라우저에서 ONNX 로 돌릴 번역 모델이 필요한데, 긴 문서를 넣어야 해서 컨텍스트가 32K 토큰 이상이고 MIT 라이선스인 걸 찾고 있어요.

- 사용자 의도: 장문 입력 가능한 MIT ONNX 번역 모델
- persona / 표현: ml_engineer / 기술형 · 난이도 hard
- 기대 행동: abstain

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `licenses` | mit | MIT 라이선스 | 아니오(판정용) |
| `min_context_length` | 32768 | 컨텍스트가 32K 토큰 이상 | 예 |
| `require_artifact` | onnx | ONNX 로 돌릴 | 예 |
| `tasks` | translation | 번역 모델 | 예 |

정답 기준: 조건을 모두 만족하는 모델이 코퍼스에 없다. 없다고 답하고 가까운 대안을 조건과 함께 설명하는 것이 정답이다.

| 조건 하나만 뺐을 때 | 후보 수 | 그 조건 하나만 불충족한 near-miss (최대 5) |
|---|---:|---|
| `licenses` | 4 | Doszhan-M/qlex-packages, TeamFlaxia/plamo-3-translate-0.8b-onnx, onnx-community/HY-MT1.5-1.8B-ONNX, sappho192/gemma3-multilingual-translator-270m |
| `min_context_length` | 5 | alirezamsh/small100, casawolice/small100-onnx, huggingworld/m2m100_418M, sappho192/aihub-ja-ko-translator, sappho192/ffxiv-ja-ko-translator |
| `require_artifact` | 0 | — |
| `tasks` | 3 | onnx-community/harrier-oss-v1-0.6b-ONNX, onnx-community/harrier-oss-v1-270m-ONNX, tss-deposium/pplx-embed-v1-0.6b-onnx-int8-standard |

- 조건 각각을 단독으로 만족하는 모델 수: licenses 383, min_context_length 2665, require_artifact 189, tasks 280
- near-miss 합계 12개, temptation_count 5
- 극단성 검사: 통과
- 검수: 정말 정답이 없어야 하는지, near-miss 가 '조건 하나 차이'라는 설명이 맞는지 확인한다.

- 기권 확인: ☐ 정답 없음 확인 ☐ 보류 — `judge.py ab02 (abstain) --decision approve --reason … --by …`

## ab03 — 상품 후기를 감정별로 나누는 걸 llama.cpp 에서 돌려 보고 싶어요. GGUF 로 받을 수 있는 한국어 텍스트 분류 모델 중에 MIT 라이선스인 게 있을까요?

- 사용자 의도: GGUF 텍스트 분류 모델(MIT)
- persona / 표현: local_user / 목적형 · 난이도 hard
- 기대 행동: abstain

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `licenses` | mit | MIT 라이선스 | 아니오(판정용) |
| `require_artifact` | gguf | llama.cpp … GGUF 로 받을 수 있는 | 예 |
| `tasks` | text-classification | 텍스트 분류 모델 | 예 |

정답 기준: 조건을 모두 만족하는 모델이 코퍼스에 없다. 없다고 답하고 가까운 대안을 조건과 함께 설명하는 것이 정답이다.

| 조건 하나만 뺐을 때 | 후보 수 | 그 조건 하나만 불충족한 near-miss (최대 5) |
|---|---:|---|
| `licenses` | 12 | Infosec-Consult/sage-memory-judge, Loksh/aegis-screen-4b-gguf, Metabaron6/Shieldstral-1.0-3B-GGUF, chaoliangUNSW/Jev-Style-0.8B-Decision-v3-GGUF, fr0stbit3/laya-multilingual-gguf |
| `require_artifact` | 15 | BalaRajesh1/mmbert-small-nli, DataWizardd/finbert-sentiment-ko, Dongjin-kr/ko-reranker, Genius1237/xlm-roberta-large-tydip, Jinuuuu/KoELECTRA_fine_tunning_emotion |
| `tasks` | 119 | 0ppxnhximxr/Motif-3-GGUF, AMAImedia/DeepSeek-V4.1-Flash-1017-FP8-GGUF, AMAImedia/Ling-3.1-Flash-1019-FP8-GGUF, AMAImedia/MiMo-V2.6-Flash-MOPD-BPW2.5-GGUF, AMAImedia/Naive-N0.5-Flash-Mixed-Quant-GGUF |

- 조건 각각을 단독으로 만족하는 모델 수: licenses 383, require_artifact 1643, tasks 157
- near-miss 합계 146개, temptation_count 119
- 극단성 검사: 통과
- 검수: 정말 정답이 없어야 하는지, near-miss 가 '조건 하나 차이'라는 설명이 맞는지 확인한다.

- 기권 확인: ☐ 정답 없음 확인 ☐ 보류 — `judge.py ab03 (abstain) --decision approve --reason … --by …`

## ab04 — 대학 연구용으로 사진 내용을 설명하는 웹 데모를 만들고 있어요. ONNX 파일로 제공되고 CC-BY-NC-4.0 라이선스인 비전-언어 모델을 찾고 있어요.

- 사용자 의도: 비상업 연구용 ONNX 비전-언어 모델
- persona / 표현: startup_dev / 혼합형 · 난이도 hard
- 기대 행동: abstain

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `licenses` | cc-by-nc-4.0 | CC-BY-NC-4.0 라이선스 | 아니오(판정용) |
| `require_artifact` | onnx | ONNX 파일로 제공되고 | 예 |
| `tasks` | image-text-to-text | 사진 내용을 설명하는 … 비전-언어 모델 | 예 |

정답 기준: 조건을 모두 만족하는 모델이 코퍼스에 없다. 없다고 답하고 가까운 대안을 조건과 함께 설명하는 것이 정답이다.

| 조건 하나만 뺐을 때 | 후보 수 | 그 조건 하나만 불충족한 near-miss (최대 5) |
|---|---:|---|
| `licenses` | 8 | LiquidAI/LFM2.5-VL-1.6B-ONNX, LiquidAI/LFM2.5-VL-3B-ONNX, LiquidAI/LFM2.5-VL-450M-ONNX, LiquidAI/LFM3-VL-2B-ONNX, LiquidAI/d1-2B-ONNX |
| `require_artifact` | 17 | CohereLabs/aya-vision-32b, CohereLabs/aya-vision-8b, NCSOFT/VARCO-VISION-14B, NCSOFT/VARCO-VISION-14B-HF, NCSOFT/VARCO-VISION-2.0-1.7B |
| `tasks` | 6 | Xenova/nllb-200-distilled-600M, jinaai/jina-clip-v2, jinaai/jina-embeddings-v3, jinaai/jina-embeddings-v3-hf, koble-ai/jina-embeddings-v3 |

- 조건 각각을 단독으로 만족하는 모델 수: licenses 195, require_artifact 189, tasks 537
- near-miss 합계 31개, temptation_count 17
- 극단성 검사: 통과
- 검수: 정말 정답이 없어야 하는지, near-miss 가 '조건 하나 차이'라는 설명이 맞는지 확인한다.

- 기권 확인: ☐ 정답 없음 확인 ☐ 보류 — `judge.py ab04 (abstain) --decision approve --reason … --by …`

## ab05 — Apache-2.0 라이선스이면서 파라미터 1B 이하인 한국어 질의응답 모델의 GGUF 버전이 있을까요?

- 사용자 의도: Apache-2.0 소형 GGUF QA 모델
- persona / 표현: ml_engineer / 기술형 · 난이도 hard
- 기대 행동: abstain

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `licenses` | apache-2.0 | Apache-2.0 라이선스 | 아니오(판정용) |
| `max_parameters_billion` | 1 | 파라미터 1B 이하 | 예 |
| `require_artifact` | gguf | GGUF 버전 | 예 |
| `tasks` | question-answering | 질의응답 모델 | 예 |

정답 기준: 조건을 모두 만족하는 모델이 코퍼스에 없다. 없다고 답하고 가까운 대안을 조건과 함께 설명하는 것이 정답이다.

| 조건 하나만 뺐을 때 | 후보 수 | 그 조건 하나만 불충족한 near-miss (최대 5) |
|---|---:|---|
| `licenses` | 3 | mradermacher/Prototype-Virus-1B-GGUF, mradermacher/Prototype-Virus-1B-i1-GGUF, mradermacher/next-1b-GGUF |
| `max_parameters_billion` | 4 | QuantFactory/Apollo2-7B-GGUF, cgus/Apollo2-7B-iMat-GGUF, mradermacher/IoGPT-A1-Instruct-GGUF, mradermacher/IoGPT-A1-Instruct-i1-GGUF |
| `require_artifact` | 2 | FreedomIntelligence/Apollo-MoE-0.5B, FreedomIntelligence/Apollo2-0.5B |
| `tasks` | 101 | Alcoft/Qwen2.5-0.5B-Instruct-GGUF, CHKH01/BGE-m3-ko-GGUF, ChristianAzinn/labse-gguf, EasierAI/Qwen-2.5-0.5B, Felladrin/gguf-Q5_K_M-Qwen2.5-0.5B-Instruct |

- 조건 각각을 단독으로 만족하는 모델 수: licenses 1930, max_parameters_billion 720, require_artifact 1643, tasks 29
- near-miss 합계 110개, temptation_count 101
- 극단성 검사: 통과
- 검수: 정말 정답이 없어야 하는지, near-miss 가 '조건 하나 차이'라는 설명이 맞는지 확인한다.

- 기권 확인: ☐ 정답 없음 확인 ☐ 보류 — `judge.py ab05 (abstain) --decision approve --reason … --by …`

## ab06 — 사내 문서 RAG 를 llama.cpp 로만 돌리려고 해요. 문서를 길게 넣을 수 있게 컨텍스트 32K 이상이고 MIT 라이선스인 GGUF 임베딩 모델이 필요해요.

- 사용자 의도: 장문 MIT GGUF 임베딩
- persona / 표현: backend_dev / 혼합형 · 난이도 hard
- 기대 행동: abstain

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `licenses` | mit | MIT 라이선스 | 아니오(판정용) |
| `min_context_length` | 32768 | 컨텍스트 32K 이상 | 예 |
| `require_artifact` | gguf | llama.cpp … GGUF | 예 |
| `tasks` | sentence-similarity, feature-extraction | 임베딩 모델 | 예 |

정답 기준: 조건을 모두 만족하는 모델이 코퍼스에 없다. 없다고 답하고 가까운 대안을 조건과 함께 설명하는 것이 정답이다.

| 조건 하나만 뺐을 때 | 후보 수 | 그 조건 하나만 불충족한 near-miss (최대 5) |
|---|---:|---|
| `licenses` | 27 | LiquidAI/LFM2-ColBERT-350M-GGUF, LiquidAI/LFM2.5-ColBERT-350M-GGUF, LiquidAI/LFM2.5-Embedding-350M-GGUF, NeoRoth/nemotron-3-embed-1b-gguf, PeterAM4/Qwen3-Embedding-0.6B-GGUF |
| `min_context_length` | 10 | cstr/multilingual-e5-small-GGUF, dinab/multilingual-e5-base-Q4_K_M-GGUF, dinab/multilingual-e5-base-Q8_0-GGUF, groonga/multilingual-e5-base-Q4_K_M-GGUF, groonga/multilingual-e5-large-Q4_K_M-GGUF |
| `require_artifact` | 8 | 777Radik/potion-multilingual-128M-int8, furiosa-ai/harrier-oss-v1-0.6b, microsoft/harrier-oss-v1-0.6b, microsoft/harrier-oss-v1-270m, microsoft/harrier-oss-v1-27b |
| `tasks` | 90 | 0ppxnhximxr/Motif-3-GGUF, AMAImedia/DeepSeek-V4.1-Flash-1017-FP8-GGUF, AMAImedia/Ling-3.1-Flash-1019-FP8-GGUF, AMAImedia/MiMo-V2.6-Flash-MOPD-BPW2.5-GGUF, ArchiveStudio/VibeVoice-ASR-BitNet |

- 조건 각각을 단독으로 만족하는 모델 수: licenses 383, min_context_length 2665, require_artifact 1643, tasks 338
- near-miss 합계 135개, temptation_count 90
- 극단성 검사: 통과
- 검수: 정말 정답이 없어야 하는지, near-miss 가 '조건 하나 차이'라는 설명이 맞는지 확인한다.

- 기권 확인: ☐ 정답 없음 확인 ☐ 보류 — `judge.py ab06 (abstain) --decision approve --reason … --by …`

## ab07 — 모바일 앱에 넣을 한국어 챗봇을 ONNX 로 온디바이스에서 돌리고 싶어요. 파라미터는 3B 이하, 라이선스는 MIT 였으면 해요.

- 사용자 의도: MIT 라이선스 소형 ONNX 생성 모델
- persona / 표현: startup_dev / 목적형 · 난이도 hard
- 기대 행동: abstain

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `licenses` | mit | 라이선스는 MIT | 아니오(판정용) |
| `max_parameters_billion` | 3 | 파라미터는 3B 이하 | 예 |
| `require_artifact` | onnx | ONNX 로 온디바이스 | 예 |
| `tasks` | text-generation | 챗봇(생성 모델) | 예 |

정답 기준: 조건을 모두 만족하는 모델이 코퍼스에 없다. 없다고 답하고 가까운 대안을 조건과 함께 설명하는 것이 정답이다.

| 조건 하나만 뺐을 때 | 후보 수 | 그 조건 하나만 불충족한 near-miss (최대 5) |
|---|---:|---|
| `licenses` | 4 | bigscience/mt0-base, bigscience/mt0-large, bigscience/mt0-small, uneeverse/unee-0.8b |
| `max_parameters_billion` | 0 | — |
| `require_artifact` | 25 | Amu/t1-1.5B, CMSManhattan/JiRackUltra_1b, Gunulhona/S2S_LLM, K-intelligence/Midm-2.0-Mini-Instruct, Motif-Technologies/Motif-2.6b-v1.1-LC |
| `tasks` | 40 | DLCorso/multilingual-e5-small, Hisham480/multilingual-e5-small, Hiveurban/multilingual-e5-base, Hiveurban/multilingual-e5-large-pooled, Hostage928/multilingual-e5-small |

- 조건 각각을 단독으로 만족하는 모델 수: licenses 383, max_parameters_billion 1335, require_artifact 189, tasks 2346
- near-miss 합계 69개, temptation_count 40
- 극단성 검사: 통과
- 검수: 정말 정답이 없어야 하는지, near-miss 가 '조건 하나 차이'라는 설명이 맞는지 확인한다.

- 기권 확인: ☐ 정답 없음 확인 ☐ 보류 — `judge.py ab07 (abstain) --decision approve --reason … --by …`

## ab08 — MIT 라이선스 비전-언어 모델 중에서 ONNX 파일이 있고 실행 파일 크기가 4GB 이하인 걸 찾고 있어요.

- 사용자 의도: 작은 MIT ONNX VLM
- persona / 표현: limited_gpu / 기술형 · 난이도 hard
- 기대 행동: abstain

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `licenses` | mit | MIT 라이선스 | 아니오(판정용) |
| `max_artifact_gib` | 4 | 실행 파일 크기가 4GB 이하 | 예 |
| `require_artifact` | onnx | ONNX 파일이 있고 | 예 |
| `tasks` | image-text-to-text | 비전-언어 모델 | 예 |

정답 기준: 조건을 모두 만족하는 모델이 코퍼스에 없다. 없다고 답하고 가까운 대안을 조건과 함께 설명하는 것이 정답이다.

| 조건 하나만 뺐을 때 | 후보 수 | 그 조건 하나만 불충족한 near-miss (최대 5) |
|---|---:|---|
| `licenses` | 3 | LiquidAI/LFM2.5-VL-3B-ONNX, LiquidAI/LFM2.5-VL-450M-ONNX, onnx-community/LFM2.5-VL-450M-ONNX |
| `max_artifact_gib` | 0 | — |
| `require_artifact` | 18 | Baekpica/DeepSeek-V4.1-Flash-1017-hVQ-GGUF, Baekpica/DeepSeek-V4.1-Flash-1017-iVQ-GGUF, Baekpica/MiMo-V2.6-Flash-MOPD-VQ-GGUF, Baekpica/MiMo-V2.6-Flash-RL-UNCENSORED-VQ-GGUF, Baekpica/MiMo-V2.6-Flash-RL-VQ-GGUF |
| `tasks` | 54 | DLCorso/multilingual-e5-small, Hisham480/multilingual-e5-small, Hiveurban/multilingual-e5-base, Hiveurban/multilingual-e5-large-pooled, Hostage928/multilingual-e5-small |

- 조건 각각을 단독으로 만족하는 모델 수: licenses 383, max_artifact_gib 1965, require_artifact 189, tasks 537
- near-miss 합계 75개, temptation_count 54
- 극단성 검사: 통과
- 검수: 정말 정답이 없어야 하는지, near-miss 가 '조건 하나 차이'라는 설명이 맞는지 확인한다.

- 기권 확인: ☐ 정답 없음 확인 ☐ 보류 — `judge.py ab08 (abstain) --decision approve --reason … --by …`

## ab09 — 인터넷 연결 없이 회의 내용을 받아 적는 도구를 llama.cpp 기반으로 만들려고 해요. GGUF 파일로 받을 수 있고 GPL-3.0 라이선스인 음성 인식 모델이 있나요?

- 사용자 의도: GPL-3.0 라이선스의 GGUF 음성 인식 모델
- persona / 표현: korean_service_planner / 혼합형 · 난이도 hard
- 기대 행동: abstain

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `licenses` | gpl-3.0 | GPL-3.0 라이선스 | 아니오(판정용) |
| `require_artifact` | gguf | llama.cpp … GGUF 파일로 | 예 |
| `tasks` | automatic-speech-recognition | 회의 내용을 받아 적는 … 음성 인식 모델 | 예 |

정답 기준: 조건을 모두 만족하는 모델이 코퍼스에 없다. 없다고 답하고 가까운 대안을 조건과 함께 설명하는 것이 정답이다.

| 조건 하나만 뺐을 때 | 후보 수 | 그 조건 하나만 불충족한 near-miss (최대 5) |
|---|---:|---|
| `licenses` | 104 | AMAImedia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-BF16-GGUF, ArchiveStudio/VibeVoice-ASR-BitNet, AtomicChat/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF, Bercraft/Voxtral-Mini-4B-Realtime-2602-GGUF, FunAudioLLM/SenseVoiceSmall-GGUF-audiocpp |
| `require_artifact` | 1 | BarathwajAnandan/cohere-transcribe-03-2026-CoreML-6bit |
| `tasks` | 2 | BSC-LT/salamandraTA-7B-instruct-GGUF, egekocabas/salamandraTA-7b-instruct-Q5_K_M-GGUF |

- 조건 각각을 단독으로 만족하는 모델 수: licenses 9, require_artifact 1643, tasks 321
- near-miss 합계 107개, temptation_count 104
- 극단성 검사: 통과
- 검수: 정말 정답이 없어야 하는지, near-miss 가 '조건 하나 차이'라는 설명이 맞는지 확인한다.

- 기권 확인: ☐ 정답 없음 확인 ☐ 보류 — `judge.py ab09 (abstain) --decision approve --reason … --by …`

## ab10 — 기존 PyTorch 로더를 그대로 써서 사내 문서 질의응답 기능을 만들려고 해요. Apache-2.0 라이선스이고 pytorch_model.bin 가중치를 제공하는 한국어 질의응답 모델을 찾아 주세요.

- 사용자 의도: Apache-2.0 PyTorch bin 질의응답 모델
- persona / 표현: startup_dev / 혼합형 · 난이도 hard
- 기대 행동: abstain

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `licenses` | apache-2.0 | Apache-2.0 라이선스 | 아니오(판정용) |
| `require_artifact` | pytorch_bin | pytorch_model.bin 가중치를 제공하는 | 예 |
| `tasks` | question-answering | 사내 문서 질의응답 … 한국어 질의응답 모델 | 예 |

정답 기준: 조건을 모두 만족하는 모델이 코퍼스에 없다. 없다고 답하고 가까운 대안을 조건과 함께 설명하는 것이 정답이다.

| 조건 하나만 뺐을 때 | 후보 수 | 그 조건 하나만 불충족한 near-miss (최대 5) |
|---|---:|---|
| `licenses` | 8 | Forturne/bert-base-finetuned-klue-mrc, HoGeeny/klue-qa-model, monologg/koelectra-base-v2-finetuned-korquad, monologg/koelectra-base-v2-finetuned-korquad-384, monologg/koelectra-base-v3-finetuned-korquad |
| `require_artifact` | 10 | FreedomIntelligence/Apollo-MoE-0.5B, FreedomIntelligence/Apollo-MoE-1.5B, FreedomIntelligence/Apollo2-0.5B, FreedomIntelligence/Apollo2-1.5B, FreedomIntelligence/Apollo2-7B |
| `tasks` | 191 | 42MARU/ko-spelling-wav2vec2-conformer-del-1s, AliaeAI/paraphrase-multilingual-MiniLM-L12-v2, BigBigBe/ynat-model, Blaxzter/LaBSE-sentence-embeddings, BlinkDL/rwkv-4-world |

- 조건 각각을 단독으로 만족하는 모델 수: licenses 1930, require_artifact 514, tasks 29
- near-miss 합계 209개, temptation_count 191
- 극단성 검사: 통과
- 검수: 정말 정답이 없어야 하는지, near-miss 가 '조건 하나 차이'라는 설명이 맞는지 확인한다.

- 기권 확인: ☐ 정답 없음 확인 ☐ 보류 — `judge.py ab10 (abstain) --decision approve --reason … --by …`
