# 검색 결과 전후 비교

골든셋 v2 질의 70개를 기존 코퍼스(3853행)와 백필 코퍼스(3872행)에 각각 돌렸다.

하드 필터와 어휘 점수는 `05_validate_retrieval` 의 함수를 그대로 쓴다. 판정 라벨이 아직 없어 정답률은 재지 않고, 후보와 상위 노출의 변화만 본다.

## 1. 후보 수

- 질의 60개 (abstention 10개 제외)
- eligible 합계 **3,973 → 4,762** (+789)
- 바뀐 질의 **33개** / 60

## 2. 상위 10위에 새로 진입한 모델

- 연인원 **69건**, 서로 다른 모델 **25개**

백필 전에는 파라미터·컨텍스트가 null이라 하드 필터에서 탈락했던 모델들이다.

| 모델 | 진입한 질의 수 |
|---|---:|
| `cstr/internvl2-1b-crispembed-GGUF` | 5 |
| `FadedRedStar/LFM2.5-VL-450M-heretic-imatrix-GGUF` | 5 |
| `Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF` | 5 |
| `Jackrong/Qwopus3.6-27B-v2-MTP-GGUF` | 5 |
| `neureps/warmly-qwen35-08b-enko-gguf` | 5 |
| `thelamapi/next2-0.8b-GGUF` | 5 |
| `Mattimax/DAC6.5-GGUF` | 5 |
| `OpenVoiceOS/qwen3-forced-aligner-0.6b-q4-k-m` | 4 |
| `LiquidAI/LFM2.5-1.2B-Instruct-GGUF` | 4 |
| `localdeel/ko-hand-ocr-vl-GGUF` | 4 |
| `OpenVoiceOS/qwen3-asr-0.6b-f16` | 3 |
| `FunAudioLLM/SenseVoiceSmall-GGUF-audiocpp` | 2 |
| `bespin-global/klue-bert-base-aihub-mrc` | 2 |
| `monologg/koelectra-small-v2-distilled-korquad-384` | 2 |
| `monologg/koelectra-base-v3-finetuned-korquad` | 2 |
| `desert-ant-labs/emo` | 2 |
| `cswk/sayit-asr-gguf` | 1 |
| `handy-computer/SenseVoiceSmall-gguf` | 1 |
| `mlx-community/bge-m3-mlx-4bit` | 1 |
| `handy-computer/Qwen3-ASR-0.6B-gguf` | 1 |

## 3. 질의별 변화

| id | 유형 | 질의 | 후보 전→후 | 신규 진입 |
|---|---|---|---|---|
| `bl01` | benchmark_lookup | KMMLU 점수를 공개한 한국어 LLM을 찾고 있어. 많이 쓰이는 것 중… | 248 → 399 | — |
| `bl03` | benchmark_lookup | 파라미터 500M 이하로 공개된 한국어 문장 임베딩 모델 중에 MTEB … | 39 → 46 | — |
| `bl04` | benchmark_lookup | LibriSpeech 결과가 README에 있는 한국어 음성 인식 모델을… | 34 → 57 | `cswk/sayit-asr-gguf`, `OpenVoiceOS/qwen3-forced-aligner-0.6b-q4-k-m` |
| `bl05` | benchmark_lookup | FLEURS 점수가 공개된 한국어 음성 인식 모델 있어? 1B 이하로 공… | 34 → 57 | `OpenVoiceOS/qwen3-forced-aligner-0.6b-q4-k-m`, `OpenVoiceOS/qwen3-asr-0.6b-f16` |
| `bl06` | benchmark_lookup | Common Voice 평가 결과가 있는 한국어 음성 인식 모델을 추천해… | 34 → 57 | `OpenVoiceOS/qwen3-forced-aligner-0.6b-q4-k-m`, `OpenVoiceOS/qwen3-asr-0.6b-f16`, `handy-computer/SenseVoiceSmall-gguf` 외 1 |
| `bl07` | benchmark_lookup | MMLU 점수가 공개된 한국어 LLM 중에 4B 이하로 공개된 걸 찾아줘… | 179 → 278 | `LiquidAI/LFM2.5-1.2B-Instruct-GGUF` |
| `bl08` | benchmark_lookup | GPQA 결과를 공개한 한국어 LLM이 있을까? 4B 이하로 공개된 것 … | 179 → 278 | `LiquidAI/LFM2.5-1.2B-Instruct-GGUF` |
| `le02` | lexical_exact | GGUF로 제공되는 한국어 이미지-텍스트 모델 있어? 파라미터 1B 이하… | 12 → 26 | `cstr/internvl2-1b-crispembed-GGUF`, `FadedRedStar/LFM2.5-VL-450M-heretic-imatrix-GGUF`, `Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF` 외 5 |
| `le07` | lexical_exact | opus-mt 기반 한국어 번역 모델을 찾아줘. 많이 쓰이는 것으로.… | 116 → 117 | — |
| `le08` | lexical_exact | MLX 형식으로 제공되는 한국어 LLM을 찾고 있어. 많이 쓰이는 것 중… | 110 → 174 | — |
| `le09` | lexical_exact | fp8로 양자화된 한국어 LLM 있어? 많이 쓰이는 것 중에 4B 이하로… | 179 → 278 | `LiquidAI/LFM2.5-1.2B-Instruct-GGUF` |
| `mc04` | model_comparison | BGE랑 multilingual-E5 중에 한국어 임베딩에 뭐가 나아? … | 64 → 64 | `mlx-community/bge-m3-mlx-4bit` |
| `mc06` | model_comparison | KoGPT랑 Polyglot-Ko 비교해줘. 많이 쓰이는 한국어 생성 모… | 924 → 926 | — |
| `mc07` | model_comparison | NLLB와 mBART 중에 한국어 번역에 뭐가 나아? 많이 쓰이는 것으로… | 116 → 117 | — |
| `mc08` | model_comparison | Whisper small과 wav2vec 중에 한국어 음성 인식에 뭐가 … | 34 → 57 | `handy-computer/Qwen3-ASR-0.6B-gguf` |
| `mc09` | model_comparison | opus-mt와 m2m100 중에 한국어 번역에 뭐가 나아? 많이 쓰이는… | 116 → 117 | — |
| `ca08` | semantic_capability | 회의 녹음을 글로 받아 적어주는 한국어 모델을 찾고 있어. 1B 이하로 … | 34 → 57 | `OpenVoiceOS/qwen3-forced-aligner-0.6b-q4-k-m`, `OpenVoiceOS/qwen3-asr-0.6b-f16` |
| `ca09` | semantic_capability | 사진 속 글자를 읽어서 한국어로 알려주는 모델이 필요해. 파라미터 1B … | 12 → 26 | `cstr/internvl2-1b-crispembed-GGUF`, `FadedRedStar/LFM2.5-VL-450M-heretic-imatrix-GGUF`, `Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF` 외 4 |
| `ca10` | semantic_capability | 표나 그래프가 든 이미지를 읽고 설명해주는 한국어 모델 있어? 파라미터 … | 12 → 26 | `cstr/internvl2-1b-crispembed-GGUF`, `FadedRedStar/LFM2.5-VL-450M-heretic-imatrix-GGUF`, `Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF` 외 5 |
| `sm01` | semantic_constraint | 의료 분야에 쓸 한국어 LLM이 필요해. 많이 쓰이는 것 중에 파라미터 … | 179 → 278 | `LiquidAI/LFM2.5-1.2B-Instruct-GGUF` |
| `sm02` | semantic_constraint | 실시간으로 받아쓰기를 해야 해서 스트리밍이 되는 한국어 음성 인식 모델을… | 26 → 39 | `FunAudioLLM/SenseVoiceSmall-GGUF-audiocpp`, `cstr/sensevoice-small-GGUF` |
| `sm04` | semantic_constraint | 한국어 기계독해용 모델을 찾고 있어. 파라미터 1B 이하로.… | 17 → 8 | `bespin-global/klue-bert-base-aihub-mrc`, `monologg/koelectra-small-v2-distilled-korquad-384`, `monologg/koelectra-base-v3-finetuned-korquad` |
| `sm05` | semantic_constraint | 아주 긴 입력을 받아서 안전성이나 품질을 평가하는 한국어 모델이 필요해.… | 24 → 19 | `desert-ant-labs/emo` |
| `sm06` | semantic_constraint | 문서나 표를 읽어야 해서 OCR이 되는 한국어 이미지-텍스트 모델을 찾아… | 12 → 26 | `cstr/internvl2-1b-crispembed-GGUF`, `FadedRedStar/LFM2.5-VL-450M-heretic-imatrix-GGUF`, `Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF` 외 5 |
| `sm07` | semantic_constraint | RAG에 쓸 한국어 검색용 임베딩 모델이 필요해. 파라미터 100M 이하… | 13 → 15 | — |
| `sc01` | structured_constraint | 3B 이하 한국어 요약 모델을 찾고 있어.… | 14 → 12 | `QyrouNnet-AI/QNS-2-ReLearn-Preview`, `ainize/kobart-news` |
| `sc02` | structured_constraint | 파라미터 1B 이하인 한국어 질의응답 모델이 필요해.… | 17 → 8 | `bespin-global/klue-bert-base-aihub-mrc`, `monologg/koelectra-small-v2-distilled-korquad-384`, `monologg/koelectra-base-v3-finetuned-korquad` |
| `sc03` | structured_constraint | 긴 문서를 다뤄야 해서 컨텍스트 32768 토큰 이상인 한국어 텍스트 분… | 29 → 25 | `shreyasmeher/Qwen-GLOCON-Reasoning` |
| `sc04` | structured_constraint | 컨텍스트 131072 토큰 이상인 한국어 텍스트 분류 모델이 있을까?… | 24 → 19 | `desert-ant-labs/emo` |
| `sc05` | structured_constraint | 많이 쓰이는 모델 중에서 컨텍스트 32768 토큰 이상인 한국어 문장 유… | 28 → 22 | `PeterAM4/Qwen3-Embedding-0.6B-GGUF` |
| `sc06` | structured_constraint | 파라미터 수가 명시된 것 중에 100M 이하인 한국어 음성 인식 모델을 … | 15 → 19 | — |
| `sc07` | structured_constraint | 파라미터 1B 이하로 공개된 한국어 이미지-텍스트 모델을 추천해줘.… | 12 → 26 | `cstr/internvl2-1b-crispembed-GGUF`, `FadedRedStar/LFM2.5-VL-450M-heretic-imatrix-GGUF`, `Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF` 외 5 |
| `sc08` | structured_constraint | 파라미터 수가 공개된 100M 이하 한국어 임베딩 모델이 필요해.… | 13 → 15 | — |

## 4. abstention 영향 ⚠️

abstention 질의 10개는 `require_known_*` 로 후보 0개를 만들었다. 백필로 값이 채워지면 후보가 0이 아니게 될 수 있다. 그러면 그 질의는 다시 써야 한다.

| id | 질의 | 후보 전 | 후보 후 | 판정 |
|---|---|---:|---:|---|
| `ab01` | 온디바이스로 돌릴 수 있게 파라미터 100M 이하인 한국어 이… | 0 | 0 | ✅ 유지 |
| `ab02` | 파라미터 50M 이하인 초소형 한국어 요약 모델이 필요해. 파… | 0 | 0 | ✅ 유지 |
| `ab03` | 컨텍스트 길이가 262144 토큰 이상인 것으로 확인된 한국어… | 0 | 0 | ✅ 유지 |
| `ab04` | 파라미터 10M 이하로 명시된 한국어 질의응답 모델을 추천해줘… | 0 | 0 | ✅ 유지 |
| `ab05` | 책 한 권을 통째로 번역하려고 해. 컨텍스트 100만 토큰 이… | 0 | 0 | ✅ 유지 |
| `ab06` | 많이 쓰이는 한국어 번역 모델 중에서 파라미터 100M 이하로… | 0 | 0 | ✅ 유지 |
| `ab07` | 아주 긴 문서를 분류해야 해. 컨텍스트 524288 토큰 이상… | 0 | 0 | ✅ 유지 |
| `ab08` | 파라미터 50M 이하로 명시된 한국어 임베딩 모델을 찾고 있어… | 0 | 0 | ✅ 유지 |
| `ab09` | 파라미터 10M 이하로 공개된 한국어 문장 유사도 모델이 있나… | 0 | 0 | ✅ 유지 |
| `ab10` | 파라미터 10M 이하로 명시된 한국어 음성 인식 모델을 추천해… | 0 | 0 | ✅ 유지 |

**0개 질의가 재작성 대상이다.**

