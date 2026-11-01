# Stage 4 retrieval validation (vector)

질의: 48 · 통과: 48 · 실패: 0 · 빈 결과: 2

task conflict는 후보를 삭제하지 않고 점수에 penalty를 적용했다.
benchmark 질의: 5개 · benchmark 점수는 동일 dataset·metric 조건에서만 비교했다.

## q01_ko_classification_cpu 한국어 텍스트 분류를 위한 가벼운 CPU 모델
후보 71개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `DataWizardd/finbert-sentiment-ko` · text-classification · score=0.6217 (raw=0.6217, route=hybrid, dense=0.3997, sparse=0.8436)
- `Jinuuuu/KoELECTRA_fine_tunning_emotion` · text-classification · score=0.5615 (raw=0.5533, route=hybrid, dense=0.4636, sparse=0.6430)
- `solbi12/ecommers_fasion_fine_tuned_3class_model` · text-classification · score=0.5513 (raw=0.5348, route=hybrid, dense=0.4769, sparse=0.5927)
- `mp-juuuns/qwen35-c8q-distilled-8l-edge-classifier-gguf` · text-classification · score=0.3515 (raw=0.3433, route=hybrid, dense=0.4329, sparse=0.2536)
- `Zeolit/lettuce-thymos-26m-v1` · text-classification · score=0.3221 (raw=0.3221, route=hybrid, dense=0.3944, sparse=0.2497)

## q02_ko_sentence_embedding 한국어 문장 임베딩과 문장 유사도 검색 모델
후보 380개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `dragonkue/BGE-m3-ko` · sentence-similarity · score=0.5079 (raw=0.5079, route=hybrid, dense=0.3979, sparse=0.8380)
- `hyunseop/bge-m3-ko` · sentence-similarity · score=0.5053 (raw=0.5053, route=hybrid, dense=0.3942, sparse=0.8385)
- `upskyy/gte-base-korean` · sentence-similarity · score=0.4921 (raw=0.4921, route=hybrid, dense=0.3766, sparse=0.8385)
- `upskyy/e5-base-korean` · sentence-similarity · score=0.4913 (raw=0.4913, route=hybrid, dense=0.3723, sparse=0.8480)
- `0xnu/pmmlv2-fine-tuned-yoruba` · sentence-similarity · score=0.3396 (raw=0.3396, route=hybrid, dense=0.4459, sparse=0.0205)

## q03_ko_document_embedding 한국어 긴 문서 임베딩용 모델, context 2048 이상
후보 135개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `dragonkue/BGE-m3-ko` · sentence-similarity · score=0.6465 (raw=0.6393, route=hybrid, dense=0.4406, sparse=0.8380)
- `hyunseop/bge-m3-ko` · sentence-similarity · score=0.6396 (raw=0.6396, route=hybrid, dense=0.4406, sparse=0.8385)
- `upskyy/gte-base-korean` · sentence-similarity · score=0.6295 (raw=0.6295, route=hybrid, dense=0.4204, sparse=0.8385)
- `BidirLM/BidirLM-0.6B-Embedding` · sentence-similarity · score=0.5544 (raw=0.5472, route=hybrid, dense=0.3938, sparse=0.7007)
- `BidirLM/BidirLM-1.7B-Embedding` · sentence-similarity · score=0.5530 (raw=0.5458, route=hybrid, dense=0.3909, sparse=0.7007)

## q04_ko_asr 한국어 음성 인식 ASR 모델
후보 237개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `Edge0/Audio8-ASR-0.1B` · automatic-speech-recognition · score=0.6450 (raw=0.6334, route=hybrid, dense=0.5824, sparse=0.7867)
- `BuzzASR/korean` · automatic-speech-recognition · score=0.6157 (raw=0.6157, route=hybrid, dense=0.5613, sparse=0.7790)
- `Kkonjeong/wav2vec2-base-korean` · automatic-speech-recognition · score=0.6046 (raw=0.6046, route=hybrid, dense=0.5264, sparse=0.8393)
- `w11wo/wav2vec2-xls-r-300m-korean` · automatic-speech-recognition · score=0.6029 (raw=0.6029, route=hybrid, dense=0.5231, sparse=0.8421)
- `moonshine-ai/moonshine-base-ko` · automatic-speech-recognition · score=0.6012 (raw=0.5897, route=hybrid, dense=0.5245, sparse=0.7855)

## q05_ko_translation 영어에서 한국어로 번역하는 모델
후보 239개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `Helsinki-NLP/opus-mt-tc-big-en-ko` · translation · score=0.8366 (raw=0.8366, route=hybrid, dense=0.5272, sparse=0.9397)
- `R4kSo1997/opus-mt-en-ko-onnx-int8` · translation · score=0.8256 (raw=0.8256, route=hybrid, dense=0.5048, sparse=0.9325)
- `jhk/opus-mt-tc-big-wiki-en-ko` · translation · score=0.8218 (raw=0.8218, route=hybrid, dense=0.5029, sparse=0.9282)
- `ooeoeo/opus-mt-tc-big-en-ko-ct2-float16` · translation · score=0.8103 (raw=0.8103, route=hybrid, dense=0.4449, sparse=0.9321)
- `dhtocks/nllb-200-distilled-350M_en-ko` · translation · score=0.8063 (raw=0.8063, route=hybrid, dense=0.4485, sparse=0.9255)

## q06_ko_summarization 한국어 문서 요약 모델, 8B 이하
후보 6개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `eenzeenee/t5-small-korean-summarization` · summarization · score=0.2460 (raw=0.2460, route=hybrid, dense=0.4638, sparse=0.0282)
- `psyche/KoT5-summarization` · summarization · score=0.2358 (raw=0.2358, route=hybrid, dense=0.4434, sparse=0.0283)
- `EbanLee/kobart-summary-v3` · summarization · score=0.2331 (raw=0.2331, route=hybrid, dense=0.4379, sparse=0.0282)
- `eenzeenee/t5-base-korean-summarization` · summarization · score=0.2240 (raw=0.2240, route=hybrid, dense=0.4205, sparse=0.0276)
- `mskayacioglu/mbart50-xlsum` · summarization · score=0.2165 (raw=0.2165, route=hybrid, dense=0.4081, sparse=0.0248)

## q07_ko_qa 한국어 질문 답변 모델, 3B 이하
후보 6개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `bespin-global/klue-bert-base-aihub-mrc` · question-answering · score=0.2047 (raw=0.2047, route=hybrid, dense=0.3815, sparse=0.0279)
- `timpal0l/mdeberta-v3-base-squad2` · question-answering · score=0.1972 (raw=0.1972, route=hybrid, dense=0.3775, sparse=0.0170)
- `monologg/koelectra-base-v3-finetuned-korquad` · question-answering · score=0.1954 (raw=0.1954, route=hybrid, dense=0.3907, sparse=0.0000)
- `FreedomIntelligence/Apollo-MoE-0.5B` · question-answering · score=0.1934 (raw=0.1934, route=hybrid, dense=0.3657, sparse=0.0211)
- `monologg/koelectra-small-v2-distilled-korquad-384` · question-answering · score=0.1860 (raw=0.1860, route=hybrid, dense=0.3719, sparse=0.0000)

## q08_ko_generation_long_context 한국어 텍스트 생성 모델, context 8192 이상
후보 1184개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `MyeongHo0621/Qwen2.5-3B-Korean` · text-generation · score=0.7031 (raw=0.6949, route=hybrid, dense=0.5575, sparse=0.8322)
- `kez-lab/gemma-2-2b-quiz-korean` · text-generation · score=0.6508 (raw=0.6425, route=hybrid, dense=0.4919, sparse=0.7932)
- `soka0000/vclm-korean-7b` · text-generation · score=0.6200 (raw=0.5953, route=hybrid, dense=0.4789, sparse=0.7118)
- `jwg0830/AX-3.1-Light-sft_v0_21` · text-generation · score=0.6176 (raw=0.6094, route=hybrid, dense=0.4461, sparse=0.7726)
- `intrect/VELA` · text-generation · score=0.6149 (raw=0.6066, route=hybrid, dense=0.4743, sparse=0.7389)

## q09_ko_multimodal 한국어 이미지와 텍스트를 함께 처리하는 멀티모달 모델
후보 395개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `kakaocorp/kanana-1.5-v-3b-instruct` · image-text-to-text · score=0.5017 (raw=0.5017, route=hybrid, dense=0.4827, sparse=0.5586)
- `NCSOFT/VARCO-VISION-2.0-14B` · image-text-to-text · score=0.4474 (raw=0.4474, route=hybrid, dense=0.5117, sparse=0.2543)
- `NCSOFT/VARCO-VISION-2.0-1.7B` · image-text-to-text · score=0.4442 (raw=0.4442, route=hybrid, dense=0.5090, sparse=0.2496)
- `kanarena/supergemma4-e4b-abliterated-multimodal-gguf-4bit` · image-text-to-text · score=0.4046 (raw=0.4046, route=hybrid, dense=0.5302, sparse=0.0277)
- `McG-221/SuperQwen3.8-27b-abliterated-Q8_0-GGUF` · image-text-to-text · score=0.4019 (raw=0.4019, route=hybrid, dense=0.5267, sparse=0.0277)

## q10_ko_small_low_popularity 다운로드 80~499의 한국어 텍스트 생성 모델
후보 1317개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `MyeongHo0621/Qwen2.5-3B-Korean` · text-generation · score=0.7194 (raw=0.7111, route=hybrid, dense=0.5901, sparse=0.8322)
- `tensorblock/llama2-13b.kor.v1-GGUF` · text-generation · score=0.7128 (raw=0.7128, route=hybrid, dense=0.5224, sparse=0.9031)
- `kez-lab/gemma-2-2b-quiz-korean` · text-generation · score=0.6254 (raw=0.6254, route=hybrid, dense=0.5138, sparse=0.7370)
- `intrect/VELA` · text-generation · score=0.6199 (raw=0.6117, route=hybrid, dense=0.4844, sparse=0.7389)
- `jwg0830/AX-3.1-Light-sft_v0_21` · text-generation · score=0.6198 (raw=0.6116, route=hybrid, dense=0.4505, sparse=0.7726)

## q11_ko_known_hardware 파라미터와 context 정보가 확인된 한국어 임베딩 모델
후보 374개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `upskyy/bge-m3-korean` · sentence-similarity · score=0.7506 (raw=0.7506, route=hybrid, dense=0.4583, sparse=0.8481)
- `hyunseop/bge-m3-ko` · sentence-similarity · score=0.7462 (raw=0.7462, route=hybrid, dense=0.4690, sparse=0.8385)
- `upskyy/e5-base-korean` · sentence-similarity · score=0.7454 (raw=0.7454, route=hybrid, dense=0.4374, sparse=0.8480)
- `BidirLM/BidirLM-1.7B-Embedding` · sentence-similarity · score=0.6376 (raw=0.6293, route=hybrid, dense=0.4154, sparse=0.7007)
- `BidirLM/BidirLM-0.6B-Embedding` · sentence-similarity · score=0.6365 (raw=0.6283, route=hybrid, dense=0.4111, sparse=0.7007)

## q12_ko_generation_unknown_safe 한국어 생성 모델, 3B 이하이며 수치가 확인된 후보만
후보 376개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `EleutherAI/polyglot-ko-1.3b` · text-generation · score=0.6274 (raw=0.6274, route=hybrid, dense=0.3840, sparse=0.8707)
- `42dot/42dot_LLM-PLM-1.3B` · text-generation · score=0.6215 (raw=0.6215, route=hybrid, dense=0.3802, sparse=0.8628)
- `42dot/42dot_LLM-SFT-1.3B` · text-generation · score=0.6124 (raw=0.6124, route=hybrid, dense=0.3632, sparse=0.8616)
- `kez-lab/gemma-2-2b-quiz-korean` · text-generation · score=0.5573 (raw=0.5573, route=hybrid, dense=0.3777, sparse=0.7370)
- `Motif-Technologies/Motif-2.6B` · text-generation · score=0.4808 (raw=0.4808, route=hybrid, dense=0.4013, sparse=0.5604)

## q13_small_cpu_classifier CPU에서 빠르게 돌릴 수 있는 5억 파라미터 이하 텍스트 분류 모델을 찾아줘
후보 62개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `solbi12/ecommers_fasion_fine_tuned_3class_model` · text-classification · score=0.4580 (raw=0.4436, route=hybrid, dense=0.4140, sparse=0.4535)
- `Jinuuuu/KoELECTRA_fine_tunning_emotion` · text-classification · score=0.4374 (raw=0.4278, route=hybrid, dense=0.3598, sparse=0.4505)
- `mp-juuuns/qwen35-c8q-distilled-8l-edge-classifier-gguf` · text-classification · score=0.2677 (raw=0.2677, route=hybrid, dense=0.3585, sparse=0.2375)
- `Zeolit/lettuce-thymos-26m-v1` · text-classification · score=0.2542 (raw=0.2542, route=hybrid, dense=0.3096, sparse=0.2358)
- `guardion/ModernGuard-1` · text-classification · score=0.2123 (raw=0.2123, route=hybrid, dense=0.2905, sparse=0.1862)

## q14_semantic_search_embedding 의미 검색과 문장 검색에 적합한 문장 임베딩 모델을 추천해줘
후보 435개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `Moriec/Vinogradov_semantic_search` · sentence-similarity · score=0.3042 (raw=0.3042, route=hybrid, dense=0.4057, sparse=0.0000)
- `opensearch-project/opensearch-neural-sparse-encoding-multilingual-v1` · feature-extraction · score=0.2960 (raw=0.2960, route=hybrid, dense=0.3947, sparse=0.0000)
- `artificial-nerds/pmnet` · sentence-similarity · score=0.2955 (raw=0.2955, route=hybrid, dense=0.3940, sparse=0.0000)
- `ysmeta/EVE-Embed-1.1-Legal` · sentence-similarity · score=0.2913 (raw=0.2913, route=hybrid, dense=0.3884, sparse=0.0000)
- `nlpai-lab/KURE-v2` · sentence-similarity · score=0.2912 (raw=0.2912, route=hybrid, dense=0.3882, sparse=0.0000)

## q15_long_context_embedding 8192토큰 이상 긴 문서를 처리할 수 있는 임베딩 모델이 필요해
후보 132개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `sigridjineth/ModernBERT-korean-large-preview` · sentence-similarity · score=0.4749 (raw=0.4749, route=hybrid, dense=0.2948, sparse=0.5349)
- `upskyy/gte-base-korean` · sentence-similarity · score=0.4451 (raw=0.4451, route=hybrid, dense=0.3068, sparse=0.4912)
- `gomyk/modernbert-student-modernbert_L4_uniform_distilled` · sentence-similarity · score=0.4438 (raw=0.4438, route=hybrid, dense=0.2946, sparse=0.4935)
- `omai-research/milco-650m` · feature-extraction · score=0.4151 (raw=0.4151, route=hybrid, dense=0.2737, sparse=0.4622)
- `amazon/Titan-text-embeddings-v2` · feature-extraction · score=0.3964 (raw=0.3964, route=hybrid, dense=0.2682, sparse=0.4391)

## q16_realtime_asr_small 실시간 음성 인식에 쓸 수 있고 10억 파라미터 이하인 작은 모델을 찾아줘
후보 60개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `seastar105/whisper-medium-komixv2` · automatic-speech-recognition · score=0.3955 (raw=0.3955, route=hybrid, dense=0.3333, sparse=0.5820)
- `seastar105/whisper-small-komixv2` · automatic-speech-recognition · score=0.3937 (raw=0.3937, route=hybrid, dense=0.3309, sparse=0.5820)
- `AMAImedia/NOESIS-Qwen3-Forced-Aligner-0.6B-112LANG-BF16` · automatic-speech-recognition · score=0.3468 (raw=0.3468, route=hybrid, dense=0.2995, sparse=0.4887)
- `aufklarer/Nemotron-3.5-ASR-Streaming-0.6B-MLX-8bit` · automatic-speech-recognition · score=0.3315 (raw=0.3315, route=hybrid, dense=0.3326, sparse=0.3285)
- `Edge0/Audio8-ASR-0.1B` · automatic-speech-recognition · score=0.3110 (raw=0.3110, route=hybrid, dense=0.3580, sparse=0.1702)

## q17_english_german_translation 영어와 독일어 사이를 번역하는 기계 번역 모델을 추천해줘
후보 239개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `Helsinki-NLP/opus-mt_tiny_kor-eng` · translation · score=0.7360 (raw=0.7360, route=hybrid, dense=0.4087, sparse=0.8451)
- `Helsinki-NLP/opus-mt-ko-de` · translation · score=0.6125 (raw=0.6125, route=hybrid, dense=0.4071, sparse=0.6810)
- `BSC-LT/salamandraTA-7b-instruct` · translation · score=0.5953 (raw=0.5953, route=hybrid, dense=0.3161, sparse=0.6884)
- `mradermacher/OmniTranslate-1.0-GGUF` · translation · score=0.4281 (raw=0.4281, route=hybrid, dense=0.3699, sparse=0.4476)
- `mradermacher/OmniTranslate-1.1-i1-GGUF` · translation · score=0.4212 (raw=0.4212, route=hybrid, dense=0.3528, sparse=0.4440)

## q18_long_document_summarization 긴 문서를 요약할 수 있고 30억 파라미터 이하인 모델을 찾아줘
후보 2개, 결과 2개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `EbanLee/kobart-summary-v3` · summarization · score=0.0837 (raw=0.0837, route=hybrid, dense=0.3349, sparse=0.0000)
- `mskayacioglu/mbart50-xlsum` · summarization · score=0.0805 (raw=0.0805, route=hybrid, dense=0.3219, sparse=0.0000)

## q19_small_question_answering 질문에 답하는 용도의 10억 파라미터 이하 소형 모델을 추천해줘
후보 5개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `monologg/koelectra-small-v2-distilled-korquad-384` · question-answering · score=0.3695 (raw=0.3695, route=hybrid, dense=0.2629, sparse=0.4050)
- `FreedomIntelligence/Apollo-MoE-0.5B` · question-answering · score=0.0734 (raw=0.0734, route=hybrid, dense=0.2938, sparse=0.0000)
- `monologg/koelectra-base-v3-finetuned-korquad` · question-answering · score=0.0670 (raw=0.0670, route=hybrid, dense=0.2681, sparse=0.0000)
- `bespin-global/klue-bert-base-aihub-mrc` · question-answering · score=0.0658 (raw=0.0658, route=hybrid, dense=0.2633, sparse=0.0000)
- `timpal0l/mdeberta-v3-base-squad2` · question-answering · score=0.0605 (raw=0.0605, route=hybrid, dense=0.2421, sparse=0.0000)

## q20_long_context_generation 16K 이상 긴 컨텍스트를 지원하는 80억 파라미터 이하 지시문 생성 모델이 필요해
후보 526개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `Mozilla/Qwen2.5-0.5B-Instruct` · text-generation · score=0.5337 (raw=0.5337, route=hybrid, dense=0.3691, sparse=0.5885)
- `soka0000/vclm-korean-7b` · text-generation · score=0.5058 (raw=0.5010, route=hybrid, dense=0.3339, sparse=0.5566)
- `mlx-community/kanana-2-3b-instruct-mixed_4_6` · text-generation · score=0.5036 (raw=0.5036, route=hybrid, dense=0.2948, sparse=0.5732)
- `LiquidAI/LFM2.5-1.2B-Thinking` · text-generation · score=0.3823 (raw=0.3775, route=hybrid, dense=0.3262, sparse=0.3946)
- `MuXodious/LFM2.5-1.2B-Thinking-absolute-heresy` · text-generation · score=0.3809 (raw=0.3761, route=hybrid, dense=0.3229, sparse=0.3938)

## q21_vision_language_ocr 이미지를 이해하고 OCR도 수행할 수 있는 비전 언어 모델을 찾아줘
후보 395개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `thelamapi/next-ocr` · image-text-to-text · score=0.5517 (raw=0.5517, route=hybrid, dense=0.4779, sparse=0.7731)
- `NCSOFT/VARCO-VISION-2.0-1.7B-OCR` · image-text-to-text · score=0.4542 (raw=0.4542, route=hybrid, dense=0.4650, sparse=0.4218)
- `ONTHEIT/BizOnAI-OCR` · image-text-to-text · score=0.4530 (raw=0.4530, route=hybrid, dense=0.4856, sparse=0.3551)
- `jc-builds/Qwen3.5-9B-VLM-Q4_K_M-GGUF` · image-text-to-text · score=0.4355 (raw=0.4355, route=hybrid, dense=0.4018, sparse=0.5365)
- `cstr/internvl2.5-2b-crispembed-GGUF` · image-text-to-text · score=0.4212 (raw=0.4212, route=hybrid, dense=0.4327, sparse=0.3866)

## q22_low_popularity_generation 실험용으로 사용할 다운로드 수가 낮은 텍스트 생성 모델을 추천해줘
후보 1317개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `aixk/BAAR2-9M` · text-generation · score=0.4073 (raw=0.4009, route=hybrid, dense=0.4036, sparse=0.4000)
- `idah4/etm-korean-tiny` · text-generation · score=0.1136 (raw=0.1008, route=hybrid, dense=0.4034, sparse=0.0000)
- `north-wind/TinyStories-Korean-800K` · text-generation · score=0.1071 (raw=0.1071, route=hybrid, dense=0.4285, sparse=0.0000)
- `Yaongi/HybriKo-117M-ToolLLaMA-SFT` · text-generation · score=0.1043 (raw=0.1043, route=hybrid, dense=0.4173, sparse=0.0000)
- `ThakiCloud/Qwen3.8-27B-Human-KO-Enterprise-v0.1` · text-generation · score=0.1031 (raw=0.1031, route=hybrid, dense=0.4123, sparse=0.0000)

## q23_known_embedding_metadata 파라미터 수와 컨텍스트 길이가 모두 확인된 임베딩 모델을 찾아줘
후보 374개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `artificial-nerds/pmnet` · sentence-similarity · score=0.0767 (raw=0.0767, route=hybrid, dense=0.3070, sparse=0.0000)
- `sttempler/KORPatent-BGE` · sentence-similarity · score=0.0764 (raw=0.0700, route=hybrid, dense=0.2800, sparse=0.0000)
- `severinsimmler/xlm-roberta-longformer-base-16384` · feature-extraction · score=0.0756 (raw=0.0756, route=hybrid, dense=0.3022, sparse=0.0000)
- `severinsimmler/xlm-roberta-longformer-large-16384` · feature-extraction · score=0.0755 (raw=0.0755, route=hybrid, dense=0.3021, sparse=0.0000)
- `sangmini/msmarco-cotmae-MiniLM-L12_en-ko-ja` · sentence-similarity · score=0.0748 (raw=0.0748, route=hybrid, dense=0.2992, sparse=0.0000)

## q24_small_sentence_similarity 10억 파라미터 이하로 문장 유사도를 계산하는 모델을 추천해줘
후보 248개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `ysmeta/EVE-Embed-1.1-Legal` · sentence-similarity · score=0.5478 (raw=0.5478, route=hybrid, dense=0.3090, sparse=0.6274)
- `FronyAI/frony-embed-arctic-ko-0.6B-v2.5` · sentence-similarity · score=0.5138 (raw=0.5138, route=hybrid, dense=0.2791, sparse=0.5920)
- `exp-models/dragonkue-KoEn-E5-Tiny` · sentence-similarity · score=0.5017 (raw=0.5017, route=hybrid, dense=0.2885, sparse=0.5727)
- `dragonkue/multilingual-e5-small-ko` · sentence-similarity · score=0.4966 (raw=0.4966, route=hybrid, dense=0.2664, sparse=0.5733)
- `AbdullahMoQH/multilingual-e5-base` · sentence-similarity · score=0.4898 (raw=0.4898, route=hybrid, dense=0.2793, sparse=0.5599)

## q25_compact_translation 10억 파라미터 이하의 가벼운 기계 번역 모델이 필요해
후보 20개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `Neurora/opus-hplt-en-ko-v2.0` · translation · score=0.4030 (raw=0.4030, route=hybrid, dense=0.4153, sparse=0.3989)
- `Babelscape/mrebel-large-32` · translation · score=0.3763 (raw=0.3763, route=hybrid, dense=0.3865, sparse=0.3729)
- `Babelscape/mrebel-large` · translation · score=0.3715 (raw=0.3715, route=hybrid, dense=0.3712, sparse=0.3717)
- `alirezamsh/small100` · translation · score=0.1104 (raw=0.1104, route=hybrid, dense=0.4417, sparse=0.0000)
- `Sube126/Hy-MT2-1.8B-1.25Bit-MLX` · translation · score=0.1067 (raw=0.1067, route=hybrid, dense=0.4268, sparse=0.0000)

## q26_on_device_asr 엣지 디바이스에서 사용할 5억 파라미터 이하 음성 인식 모델을 찾아줘
후보 32개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `seastar105/whisper-small-komixv2` · automatic-speech-recognition · score=0.0998 (raw=0.0998, route=hybrid, dense=0.3991, sparse=0.0000)
- `Edge0/Audio8-ASR-0.1B` · automatic-speech-recognition · score=0.0979 (raw=0.0979, route=hybrid, dense=0.3917, sparse=0.0000)
- `42MARU/ko-spelling-wav2vec2-conformer-del-1s` · automatic-speech-recognition · score=0.0916 (raw=0.0916, route=hybrid, dense=0.3666, sparse=0.0000)
- `moonshine-ai/moonshine-base-ko` · automatic-speech-recognition · score=0.0910 (raw=0.0910, route=hybrid, dense=0.3640, sparse=0.0000)
- `mobilint/whisper-large-v3-turbo` · automatic-speech-recognition · score=0.0907 (raw=0.0907, route=hybrid, dense=0.3627, sparse=0.0000)

## q27_very_long_context_generation 32K 이상의 컨텍스트 길이를 지원하는 텍스트 생성 모델을 추천해줘
후보 1104개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `OpenBuddy/openbuddy-yi1.5-34b-v21.3-32k` · text-generation · score=0.5654 (raw=0.5654, route=hybrid, dense=0.3538, sparse=0.6359)
- `soka0000/vclm-korean-7b` · text-generation · score=0.4115 (raw=0.4051, route=hybrid, dense=0.3350, sparse=0.4285)
- `LiquidAI/LFM2.5-1.2B-Thinking` · text-generation · score=0.3589 (raw=0.3525, route=hybrid, dense=0.3710, sparse=0.3463)
- `MuXodious/LFM2.5-1.2B-Thinking-absolute-heresy` · text-generation · score=0.3521 (raw=0.3457, route=hybrid, dense=0.3459, sparse=0.3456)
- `OpenBuddy/openbuddy-zero-56b-v21.2-32k` · text-generation · score=0.3501 (raw=0.3501, route=hybrid, dense=0.3691, sparse=0.3438)

## q28_medium_text_classifier 성능과 크기의 균형이 좋은 30억 파라미터 이하 텍스트 분류 모델을 찾아줘
후보 72개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `Horizon-Labs/prompt-injection-guard-small` · text-classification · score=0.4797 (raw=0.4797, route=hybrid, dense=0.3030, sparse=0.5386)
- `Horizon-Labs/prompt-injection-guard-base` · text-classification · score=0.4797 (raw=0.4797, route=hybrid, dense=0.3029, sparse=0.5386)
- `solbi12/ecommers_fasion_fine_tuned_3class_model` · text-classification · score=0.4610 (raw=0.4506, route=hybrid, dense=0.4418, sparse=0.4535)
- `Jinuuuu/KoELECTRA_fine_tunning_emotion` · text-classification · score=0.4316 (raw=0.4263, route=hybrid, dense=0.3538, sparse=0.4505)
- `mp-juuuns/qwen35-c8q-distilled-8l-edge-classifier-gguf` · text-classification · score=0.2727 (raw=0.2727, route=hybrid, dense=0.3043, sparse=0.2622)

## q29_very_long_embedding 16K 이상 긴 문서를 임베딩할 수 있는 모델을 추천해줘
후보 84개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `mlx-community/LFM2.5-Embedding-350M-4bit` · sentence-similarity · score=0.0927 (raw=0.0927, route=hybrid, dense=0.3706, sparse=0.0000)
- `shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4` · sentence-similarity · score=0.0921 (raw=0.0921, route=hybrid, dense=0.3683, sparse=0.0000)
- `codefuse-ai/F2LLM-v2-160M` · feature-extraction · score=0.0916 (raw=0.0916, route=hybrid, dense=0.3664, sparse=0.0000)
- `codefuse-ai/F2LLM-v2-14B` · feature-extraction · score=0.0915 (raw=0.0915, route=hybrid, dense=0.3661, sparse=0.0000)
- `nvidia/Nemotron-3-Embed-1B-NVFP4` · sentence-similarity · score=0.0909 (raw=0.0909, route=hybrid, dense=0.3637, sparse=0.0000)

## q30_general_question_answering 범용 질문 답변에 사용할 30억 파라미터 이하 모델을 추천해줘
후보 6개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `monologg/koelectra-base-v3-finetuned-korquad` · question-answering · score=0.2554 (raw=0.2554, route=hybrid, dense=0.3405, sparse=0.0000)
- `monologg/koelectra-small-v2-distilled-korquad-384` · question-answering · score=0.2466 (raw=0.2466, route=hybrid, dense=0.3288, sparse=0.0000)
- `FreedomIntelligence/Apollo-MoE-0.5B` · question-answering · score=0.2438 (raw=0.2438, route=hybrid, dense=0.3251, sparse=0.0000)
- `timpal0l/mdeberta-v3-base-squad2` · question-answering · score=0.2415 (raw=0.2415, route=hybrid, dense=0.3220, sparse=0.0000)
- `bespin-global/klue-bert-base-aihub-mrc` · question-answering · score=0.2355 (raw=0.2355, route=hybrid, dense=0.3140, sparse=0.0000)

## q31_mteb_arguana_ndcg MTEB ArguAna에서 nDCG@10 성능이 보고된 문장 검색 임베딩 모델을 추천해줘
후보 435개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `AbdullahMoQH/multilingual-e5-base` · sentence-similarity · score=0.7702 (raw=0.7198, route=hybrid, dense=0.4135, sparse=0.8219) [benchmark MTEB ndcg-at-10 score=44.230000000000004 boost=0.04519653339336116]
- `Teradata/multilingual-e5-base` · sentence-similarity · score=0.7609 (raw=0.7105, route=hybrid, dense=0.4344, sparse=0.8025) [benchmark MTEB ndcg-at-10 score=44.230000000000004 boost=0.04519653339336116]
- `amazon/Titan-text-embeddings-v2` · feature-extraction · score=0.7607 (raw=0.7054, route=hybrid, dense=0.3907, sparse=0.8102) [benchmark MTEB ndcg-at-10 score=51.312000000000005 boost=0.05010172984017593]
- `NaganoJRC/multilingual-e5-base` · sentence-similarity · score=0.7583 (raw=0.7078, route=hybrid, dense=0.4163, sparse=0.8050) [benchmark MTEB ndcg-at-10 score=44.230000000000004 boost=0.04519653339336116]
- `Nextcloud-AI/multilingual-e5-large-instruct` · feature-extraction · score=0.7565 (raw=0.6963, route=hybrid, dense=0.3835, sparse=0.8005) [benchmark MTEB ndcg-at-10 score=58.384 boost=0.055]

## q32_mteb_embedding_evidence MTEB 평가 결과가 README에 근거와 함께 기록된 임베딩 모델을 찾아줘
후보 435개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `Teradata/multilingual-e5-base` · sentence-similarity · score=0.7076 (raw=0.6868, route=hybrid, dense=0.4550, sparse=0.7641) [benchmark MTEB accuracy score=78.97014925373135 boost=0.015]
- `amazon/Titan-text-embeddings-v2` · feature-extraction · score=0.7056 (raw=0.6849, route=hybrid, dense=0.4246, sparse=0.7716) [benchmark MTEB accuracy score=79.31343283582089 boost=0.015]
- `cnmoro/snowflake-arctic-embed-m-v2.0-cpu` · sentence-similarity · score=0.7042 (raw=0.6835, route=hybrid, dense=0.4246, sparse=0.7698) [benchmark MTEB accuracy score=66.6867 boost=0.015]
- `shadowrock-io/Nemotron-3-Embed-8B-Community-MLX-4bit` · sentence-similarity · score=0.7002 (raw=0.6780, route=hybrid, dense=0.4229, sparse=0.7630) [benchmark MTEB ndcg-at-10 score=1.0 boost=0.015]
- `AbdullahMoQH/multilingual-e5-base` · sentence-similarity · score=0.6987 (raw=0.6780, route=hybrid, dense=0.4176, sparse=0.7648) [benchmark MTEB accuracy score=78.97014925373135 boost=0.015]

## q33_asr_wer_evidence WER 평가 수치가 확인되는 음성 인식 모델을 추천해줘
후보 237개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `litert-community/VibeVoice-ASR-BitNet` · automatic-speech-recognition · score=0.6635 (raw=0.6563, route=hybrid, dense=0.3934, sparse=0.7440)
- `voconly-org/whisper-large-v3-turbo-gguf` · automatic-speech-recognition · score=0.6532 (raw=0.6460, route=hybrid, dense=0.3932, sparse=0.7302)
- `RedHatAI/whisper-tiny` · automatic-speech-recognition · score=0.6489 (raw=0.6267, route=hybrid, dense=0.3507, sparse=0.7188) [benchmark LIBRISPEECH wer score=7.54 boost=0.015]
- `unsloth/whisper-base` · automatic-speech-recognition · score=0.6487 (raw=0.6265, route=hybrid, dense=0.3497, sparse=0.7187) [benchmark LIBRISPEECH wer score=5.008769117619326 boost=0.015]
- `unsloth/whisper-small` · automatic-speech-recognition · score=0.6471 (raw=0.6249, route=hybrid, dense=0.3443, sparse=0.7185) [benchmark LIBRISPEECH wer score=3.432213777886737 boost=0.015]

## q34_ko_summarization_small_long 한국어 긴 문서를 요약하는 3B 이하 모델 중 context 4096 이상이고 파라미터와 context가 모두 확인된 후보
후보 0개, 결과 0개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- 현재 조건을 모두 만족하는 후보가 없습니다.
- 조건 완화 제안: 파라미터가 확인되지 않은 후보도 포함 (후보 3개)
- 조건 완화 제안: context 길이가 확인되지 않은 후보도 포함 (후보 1개)
- 조건 완화 제안: 최소 context 조건을 해제 (후보 5개)

## q35_ko_asr_edge_low 다운로드가 낮고 5억 파라미터 이하인 한국어 실시간 음성 인식 모델
후보 15개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `team-lucid/hubert-large-korean` · automatic-speech-recognition · score=0.6685 (raw=0.6685, route=hybrid, dense=0.4013, sparse=0.7575)
- `seastar105/whisper-small-komixv2` · automatic-speech-recognition · score=0.1302 (raw=0.1302, route=hybrid, dense=0.4366, sparse=0.0281)
- `kimthegarden/whisper-small-ko-new` · automatic-speech-recognition · score=0.1278 (raw=0.1278, route=hybrid, dense=0.4243, sparse=0.0289)
- `Bingsu/distilhubert-ko-zeroth` · automatic-speech-recognition · score=0.1233 (raw=0.1233, route=hybrid, dense=0.4091, sparse=0.0280)
- `mobilint/whisper-large-v3-turbo` · automatic-speech-recognition · score=0.1144 (raw=0.1144, route=hybrid, dense=0.4071, sparse=0.0169)

## q36_en_to_ko_translation_small 영어에서 한국어로 번역하는 10억 파라미터 이하의 가벼운 모델
후보 20개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `Helsinki-NLP/opus-mt-tc-big-en-ko` · translation · score=0.8248 (raw=0.8248, route=hybrid, dense=0.4800, sparse=0.9397)
- `dhtocks/nllb-200-distilled-350M_en-ko` · translation · score=0.8020 (raw=0.8020, route=hybrid, dense=0.4312, sparse=0.9255)
- `Neurora/opus-hplt-en-ko-v2.0` · translation · score=0.7733 (raw=0.7733, route=hybrid, dense=0.4837, sparse=0.8699)
- `Helsinki-NLP/opus-mt_tiny_kor-eng` · translation · score=0.7579 (raw=0.7579, route=hybrid, dense=0.4941, sparse=0.8458)
- `seongs/ke-t5-base-aihub-koen-translation-integrated-10m-en-to-ko` · translation · score=0.7222 (raw=0.7222, route=hybrid, dense=0.4777, sparse=0.8037)

## q37_ko_embedding_long_small 한국어 긴 문서 검색용 임베딩 모델 중 1.5B 이하이고 context 16384 이상인 후보
후보 62개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `severinsimmler/xlm-roberta-longformer-large-16384` · feature-extraction · score=0.6568 (raw=0.6568, route=hybrid, dense=0.4308, sparse=0.8828)
- `severinsimmler/xlm-roberta-longformer-base-16384` · feature-extraction · score=0.6562 (raw=0.6562, route=hybrid, dense=0.4296, sparse=0.8828)
- `BidirLM/BidirLM-0.6B-Embedding` · sentence-similarity · score=0.5640 (raw=0.5596, route=hybrid, dense=0.4185, sparse=0.7007)
- `BidirLM/BidirLM-1B-Embedding` · sentence-similarity · score=0.5611 (raw=0.5566, route=hybrid, dense=0.4126, sparse=0.7007)
- `dragonkue/colbert-ko-0.1b` · sentence-similarity · score=0.4939 (raw=0.4895, route=hybrid, dense=0.4296, sparse=0.5493)

## q38_ko_vision_ocr_small 한국어 문서 이미지와 OCR을 처리할 수 있는 5B 이하 비전 언어 모델
후보 64개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `useful-quants/LFM2.5-VL-3B-NVFP4-FP8-Mixed` · image-text-to-text · score=0.5819 (raw=0.5819, route=hybrid, dense=0.4183, sparse=0.6364)
- `kakaocorp/kanana-1.5-v-3b-instruct` · image-text-to-text · score=0.5443 (raw=0.5443, route=hybrid, dense=0.5012, sparse=0.5586)
- `NCSOFT/VARCO-VISION-2.0-1.7B-OCR` · image-text-to-text · score=0.4602 (raw=0.4602, route=hybrid, dense=0.5472, sparse=0.4311)
- `LiquidAI/LFM2.5-VL-3B` · image-text-to-text · score=0.3849 (raw=0.3849, route=hybrid, dense=0.4872, sparse=0.3508)
- `OpenMed/North-Micro-Vision-Instruct-bf16-mlx` · image-text-to-text · score=0.3578 (raw=0.3578, route=hybrid, dense=0.4637, sparse=0.3225)

## q39_ko_qa_context 한국어 질문 답변에 사용할 3B 이하 모델 중 context 2048 이상이고 파라미터가 확인된 후보
후보 2개, 결과 2개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=1
- `FreedomIntelligence/Apollo-MoE-0.5B` · question-answering · score=0.2115 (raw=0.2115, route=hybrid, dense=0.4019, sparse=0.0212)
- `haiFrHust/VNJPTranslate_base` · question-answering · score=0.1666 (raw=0.2166, route=hybrid, dense=0.4079, sparse=0.0252) [task_conflict penalty=0.05]
  - conflict evidence: question_answering_identity_marker:translate

## q40_low_long_generation 실험용 Low Popularity 중 context 32768 이상인 8B 이하 텍스트 생성 모델
후보 339개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `ceyda/Qwen3-1.7B-Base-trim-koen-32768` · text-generation · score=0.7506 (raw=0.7458, route=hybrid, dense=0.4120, sparse=0.8571)
- `OpenLLM-Korea/EXAONE-Deep-7.8B` · text-generation · score=0.7324 (raw=0.7276, route=hybrid, dense=0.3668, sparse=0.8479)
- `jwg0830/AX-3.1-Light-sft_v0_21` · text-generation · score=0.7054 (raw=0.7006, route=hybrid, dense=0.3530, sparse=0.8165)
- `gaianet/EXAONE-Deep-7.8B-GGUF` · text-generation · score=0.5785 (raw=0.5785, route=hybrid, dense=0.4013, sparse=0.6376)
- `trillionlabs/Tri-7B-Search-preview` · text-generation · score=0.5045 (raw=0.5045, route=hybrid, dense=0.4194, sparse=0.5329)

## q41_low_small_similarity 다운로드 80~499이고 5억 파라미터 이하인 소형 문장 유사도 모델
후보 172개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `alphaedge-ai/bge-m3-kor-32768` · sentence-similarity · score=0.5223 (raw=0.5223, route=hybrid, dense=0.3325, sparse=0.5856)
- `bongsoo/moco-sentencebertV2.0` · sentence-similarity · score=0.5195 (raw=0.5195, route=hybrid, dense=0.3149, sparse=0.5878)
- `caasman/klue-roberta-base-klue-sts` · sentence-similarity · score=0.5095 (raw=0.5095, route=hybrid, dense=0.2842, sparse=0.5847)
- `gomyk/minilm-student-L4_uniform_distilled` · sentence-similarity · score=0.5085 (raw=0.5085, route=hybrid, dense=0.3324, sparse=0.5671)
- `NetherQuartz/LaBSE-tokipona` · sentence-similarity · score=0.1874 (raw=0.1874, route=hybrid, dense=0.2777, sparse=0.1573)

## q42_low_asr_wer Low Popularity 한국어 음성 인식 모델 중 README에 WER 수치가 기록된 후보
후보 106개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `leuconoe/whisper-acft-ko` · automatic-speech-recognition · score=0.7313 (raw=0.7313, route=hybrid, dense=0.4161, sparse=0.8364)
- `BuzzASR/korean` · automatic-speech-recognition · score=0.7171 (raw=0.7111, route=hybrid, dense=0.4558, sparse=0.7962)
- `litert-community/VibeVoice-ASR-BitNet` · automatic-speech-recognition · score=0.7075 (raw=0.7027, route=hybrid, dense=0.4476, sparse=0.7877)
- `voconly-org/whisper-large-v3-turbo-gguf` · automatic-speech-recognition · score=0.6953 (raw=0.6905, route=hybrid, dense=0.4424, sparse=0.7732)
- `RedHatAI/whisper-tiny` · automatic-speech-recognition · score=0.6924 (raw=0.6726, route=hybrid, dense=0.3934, sparse=0.7657) [benchmark LIBRISPEECH wer score=7.54 boost=0.015]

## q43_ko_mteb_long 한국어 긴 문서 임베딩에서 MTEB 평가 근거가 있고 context 8192 이상인 모델
후보 132개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `upskyy/gte-base-korean` · sentence-similarity · score=0.7624 (raw=0.7576, route=hybrid, dense=0.4497, sparse=0.8603)
- `dragonkue/BGE-m3-ko` · sentence-similarity · score=0.7586 (raw=0.7538, route=hybrid, dense=0.4760, sparse=0.8464)
- `hyunseop/bge-m3-ko` · sentence-similarity · score=0.7512 (raw=0.7512, route=hybrid, dense=0.4890, sparse=0.8385)
- `amazon/Titan-text-embeddings-v2` · feature-extraction · score=0.7070 (raw=0.6872, route=hybrid, dense=0.4292, sparse=0.7732) [benchmark MTEB accuracy score=79.31343283582089 boost=0.015]
- `cnmoro/snowflake-arctic-embed-m-v2.0-cpu` · sentence-similarity · score=0.6799 (raw=0.6601, route=hybrid, dense=0.4734, sparse=0.7223) [benchmark MTEB accuracy score=66.6867 boost=0.015]

## q44_cpu_tiny_classifier CPU에서 사용할 1억 파라미터 이하 초소형 텍스트 분류 모델이며 파라미터 수가 확인된 후보
후보 9개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `Zeolit/lettuce-thymos-26m-v1` · text-classification · score=0.2621 (raw=0.2621, route=hybrid, dense=0.3409, sparse=0.2358)
- `monologg/koelectra-small-finetuned-nsmc` · text-classification · score=0.1030 (raw=0.1030, route=hybrid, dense=0.4119, sparse=0.0000)
- `snunlp/KR-FinBert-SC` · text-classification · score=0.1023 (raw=0.1023, route=hybrid, dense=0.4089, sparse=0.0000)
- `kfkas/legal-question-filter-koelectra` · text-classification · score=0.0956 (raw=0.0956, route=hybrid, dense=0.3824, sparse=0.0000)
- `prismdata/guardrail-ko-11class` · text-classification · score=0.0945 (raw=0.0897, route=hybrid, dense=0.3589, sparse=0.0000)

## q45_ko_multitask_retrieval_qa 한국어 검색과 질문 답변을 모두 고려할 수 있는 1B 이하 모델
후보 253개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `hyunseop/bge-m3-ko` · sentence-similarity · score=0.6140 (raw=0.6140, route=hybrid, dense=0.3894, sparse=0.8385)
- `dragonkue/BGE-m3-ko` · sentence-similarity · score=0.6078 (raw=0.6025, route=hybrid, dense=0.3670, sparse=0.8380)
- `dragonkue/colbert-ko-0.1b` · sentence-similarity · score=0.6065 (raw=0.6065, route=hybrid, dense=0.3448, sparse=0.8681)
- `upskyy/gte-base-korean` · sentence-similarity · score=0.5957 (raw=0.5957, route=hybrid, dense=0.3529, sparse=0.8385)
- `upskyy/e5-base-korean` · sentence-similarity · score=0.5952 (raw=0.5952, route=hybrid, dense=0.3424, sparse=0.8480)

## q46_ko_generation_known_all 파라미터와 context가 모두 확인된 2B 이하 한국어 텍스트 생성 모델, context 4096 이상
후보 229개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `mobilint/EXAONE-4.0-1.2B` · text-generation · score=0.7626 (raw=0.7626, route=hybrid, dense=0.4476, sparse=0.8677)
- `LiquidAI/LFM2-1.2B` · text-generation · score=0.7559 (raw=0.7559, route=hybrid, dense=0.3960, sparse=0.8758)
- `GMODEOS/EXAONE-4.0-1.2B` · text-generation · score=0.7534 (raw=0.7490, route=hybrid, dense=0.3992, sparse=0.8656)
- `cooler8/yejin-korean-1b-v8` · text-generation · score=0.5076 (raw=0.5076, route=hybrid, dense=0.4518, sparse=0.5262)
- `cooler8/yejin-korean-1b-v8-sft` · text-generation · score=0.5059 (raw=0.5059, route=hybrid, dense=0.4480, sparse=0.5252)

## q47_low_compact_translation Low Popularity에서 5억 파라미터 이하인 한국어 번역 모델
후보 9개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `dhtocks/nllb-200-distilled-350M_en-ko` · translation · score=0.7327 (raw=0.7327, route=hybrid, dense=0.4429, sparse=0.8293)
- `seongs/ke-t5-base-aihub-koen-translation-integrated-10m-en-to-ko` · translation · score=0.7037 (raw=0.7037, route=hybrid, dense=0.4592, sparse=0.7853)
- `Darong/BlueT` · translation · score=0.1502 (raw=0.1358, route=hybrid, dense=0.4586, sparse=0.0281)
- `Helsinki-NLP/opus-mt_tiny_kor-eng` · translation · score=0.1372 (raw=0.1372, route=hybrid, dense=0.4660, sparse=0.0276)
- `Neurora/opus-hplt-en-ko-v2.0` · translation · score=0.1371 (raw=0.1371, route=hybrid, dense=0.4644, sparse=0.0280)

## q48_intentionally_empty 한국어 text-generation 중 10M 이하이고 context 131072 이상인 모델
후보 0개, 결과 0개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- 현재 조건을 모두 만족하는 후보가 없습니다.
- 조건 완화 제안: 파라미터가 확인되지 않은 후보도 포함 (후보 29개)
- 조건 완화 제안: 최소 context 조건을 해제 (후보 6개)
- 조건 완화 제안: 파라미터 상한을 해제 (후보 648개)
