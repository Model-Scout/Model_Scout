# 골든셋 라벨 검토 결과

판정실 골든셋 탭의 점수가 현재 라벨과 다른 후보다. 골든셋 라벨은 원문 확인을 거친 사례라 자동으로 바꾸지 않는다.
불일치 30건.

| 질의 | 모델 | 현재 라벨 | 점수 | 판정 메모 |
|---|---|---|---:|---|
| `g008` | openai/whisper-large-v3 | acceptable | 2 | [라벨 이견] 정확도 동일, 12GB에서 원본도 문제없음 → 정답 수준 |
| `g009` | batiai/gemma-4-E4B-it-GGUF | acceptable | 2 | [라벨 이견] 양자화 GGUF로 8GB에 적재 가능, E2B보다 품질 우위 (가중치 기준 추정 — KV 캐시 여유 확인 필요) |
| `g009` | google/gemma-4-E4B-it | acceptable | 2 | [라벨 이견] 총 8B(실효 4.5B)지만 int4 ~4GB로 8GB의 80% 이내, E2B보다 품질 우위 (가중치 기준 추정 — KV 캐시 여유 확인 필요) |
| `g010` | NCSOFT/VARCO-VISION-2.0-14B | acceptable | 2 | [라벨 이견] 2.0이 후속 버전으로 한국어 OCR·문서 성능 향상, 16B 이내 → 정답 수준 |
| `g013` | dragonkue/multilingual-e5-small-ko | acceptable | 2 |  |
| `g013` | dragonkue/multilingual-e5-small-ko-v2 | acceptable | 2 |  |
| `g017` | joongi007/llama-3-Korean-Bllossom-8B-20240809-GGUF | acceptable | 2 | [라벨 이견] GGUF라 Ollama에 바로 사용 가능 → 정답 수준 |
| `g018` | OpenVINO/whisper-large-v3-turbo-int8-ov | acceptable | 2 |  |
| `g018` | Zoont/faster-whisper-large-v3-turbo-int8-ct2 | acceptable | 2 |  |
| `g018` | deepdml/faster-whisper-large-v3-turbo-ct2 | acceptable | 2 |  |
| `g018` | jfmdai/faster-whisper-large-v3-turbo-ct2 | acceptable | 2 |  |
| `g018` | openai/whisper-large-v3-turbo | expected_any | 1 | [라벨 이견] PyTorch fp32 원본은 RAM 4GB t3.medium에서 빠듯하고 느림 — CT2/OpenVINO int8 변환본이 적합 |
| `g019` | Systran/faster-whisper-base | acceptable | 2 |  |
| `g019` | openai/whisper-small | acceptable | 2 |  |
| `g020` | FunAudioLLM/SenseVoiceSmall-GGUF-audiocpp | acceptable | 2 |  |
| `g021` | RedHatAI/Qwen2.5-7B-Instruct-FP8-dynamic | expected_any | 0 | [라벨 이견] 공개 가중치 파일만 약 8.7GB로 8GB 초과, FP8은 Ada/Hopper 이상 GPU 필요 |
| `g021` | RedHatAI/Qwen2.5-7B-Instruct-quantized.w8a8 | expected_any | 0 | [라벨 이견] 공개 가중치 파일만 약 8.7GB로 8GB GPU 초과 |
| `g021` | meta-llama/Llama-3.1-8B-Instruct | needs_review | 1 | Llama 3.1 라이선스 — 평가 가정: 월 7억 MAU 미만 일반 서비스. 한국어 환각 보고로 '경고 필요' 라벨에 동의 |
| `g021` | unsloth/Qwen2.5-7B-Instruct | expected_any | 1 | 원본 재업로드본 — 공식 저장소 우선 |
| `g022` | RedHatAI/Qwen2.5-7B-Instruct-FP8-dynamic | expected_any | 1 | FP8은 Ada/Hopper 이상 GPU 필요 |
| `g022` | RedHatAI/Qwen2.5-7B-Instruct-quantized.w8a8 | expected_any | 1 | vLLM + INT8 지원 GPU 전제 |
| `g024` | nlpai-lab/KURE-v1 | expected_any | 1 | [라벨 이견] 질의가 '작게 양자화된 버전'을 원함 — 비양자화 원본(568M)은 Jetson 메모리 조건에 불리 |
| `g025` | Bingsu/KURE-v1-Q8_0-GGUF | expected_any | 0 | [라벨 이견] 질의가 sentence-transformers 사용을 명시 — GGUF는 sentence-transformers로 로드 불가 |
| `g025` | mykor/KURE-v1-gguf | expected_any | 0 | [라벨 이견] 질의가 sentence-transformers 사용을 명시 — GGUF는 sentence-transformers로 로드 불가 |
| `g026` | cstr/qwen3-asr-1.7b-GGUF | expected_any | 1 | 커뮤니티 GGUF, 사용 근거 약함 |
| `g027` | handy-computer/whisper-large-v3-turbo-gguf | acceptable | 2 |  |
| `g029` | google/gemma-4-E4B-it | expected_any | 1 | [라벨 이견] 총 8B bf16 ~16GB로 16GB Mac에선 직접 양자화 필요 |
| `g029` | mlx-community/EXAONE-3.5-7.8B-Instruct-4bit | acceptable | 2 |  |
| `g030` | Qwen/Qwen3-4B | acceptable | 2 |  |
| `g030` | Qwen/Qwen3-8B | acceptable | 2 |  |
