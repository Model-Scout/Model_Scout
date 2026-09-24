# Stage 4 retrieval validation (vector)

질의: 48 · 통과: 48 · 실패: 0 · 빈 결과: 2

task conflict는 후보를 삭제하지 않고 점수에 penalty를 적용했다.
benchmark 질의: 5개 · benchmark 점수는 동일 dataset·metric 조건에서만 비교했다.

## q01_ko_classification_cpu 한국어 텍스트 분류를 위한 가벼운 CPU 모델
후보 68개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `solbi12/ecommers_fasion_fine_tuned_3class_model` · text-classification · score=0.4769 (raw=0.4769)
- `circulus/koelectra-polite-v1` · text-classification · score=0.4746 (raw=0.4746)
- `monologg/koelectra-base-finetuned-nsmc` · text-classification · score=0.4659 (raw=0.4659)
- `monologg/koelectra-small-finetuned-nsmc` · text-classification · score=0.4636 (raw=0.4636)
- `Jinuuuu/KoELECTRA_fine_tunning_emotion` · text-classification · score=0.4635 (raw=0.4635)

## q02_ko_sentence_embedding 한국어 문장 임베딩과 문장 유사도 검색 모델
후보 380개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `ysmeta/EVE-Embed-1.1-Legal` · sentence-similarity · score=0.4709 (raw=0.4709)
- `0xnu/pmmlv2-fine-tuned-yoruba` · sentence-similarity · score=0.4461 (raw=0.4461)
- `mykor/paraphrase-multilingual-MiniLM-L12-v2` · sentence-similarity · score=0.4375 (raw=0.4375)
- `Moriec/Vinogradov_semantic_search` · sentence-similarity · score=0.4309 (raw=0.4309)
- `ddobokki/klue-roberta-base-nli-sts-ko-en` · sentence-similarity · score=0.4277 (raw=0.4277)

## q03_ko_document_embedding 한국어 긴 문서 임베딩용 모델, context 2048 이상
후보 135개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `nmixx-fin/nmixx-bge-m3` · sentence-similarity · score=0.4665 (raw=0.4665)
- `ysmeta/EVE-Embed-1.1-Legal` · sentence-similarity · score=0.4641 (raw=0.4641)
- `mp-juuuns/qwen3.5-4l-vocab40k-en-ko-headless` · feature-extraction · score=0.4633 (raw=0.4633)
- `LiquidAI/LFM2.5-Embedding-350M` · sentence-similarity · score=0.4619 (raw=0.4619)
- `BCCard/MoAI-Embedding-4B` · sentence-similarity · score=0.4612 (raw=0.4612)

## q04_ko_asr 한국어 음성 인식 ASR 모델
후보 234개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `Edge0/ARK-ASR-3B` · automatic-speech-recognition · score=0.5956 (raw=0.5956)
- `audio-cpp/VibeVoice-ASR-Streaming-7B-GGUF` · automatic-speech-recognition · score=0.5886 (raw=0.5886)
- `Edge0/Audio8-ASR-0.1B` · automatic-speech-recognition · score=0.5824 (raw=0.5824)
- `Edge0/ARK-ASR-0.6B` · automatic-speech-recognition · score=0.5821 (raw=0.5821)
- `harshav/ARK-ASR-3B-GGUF` · automatic-speech-recognition · score=0.5817 (raw=0.5817)

## q05_ko_translation 영어에서 한국어로 번역하는 모델
후보 239개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `Helsinki-NLP/opus-mt-tc-big-ko-en` · translation · score=0.5317 (raw=0.5317)
- `Helsinki-NLP/opus-mt-tc-big-en-ko` · translation · score=0.5272 (raw=0.5272)
- `sappho192/aihub-ja-ko-translator` · translation · score=0.5247 (raw=0.5247)
- `hell0ks/ja-ko-vn-12b-v2-gguf` · translation · score=0.5240 (raw=0.5240)
- `mradermacher/EraX-Translator-V1.0-GGUF` · translation · score=0.5187 (raw=0.5187)

## q06_ko_summarization 한국어 문서 요약 모델, 8B 이하
후보 6개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `eenzeenee/t5-small-korean-summarization` · summarization · score=0.4638 (raw=0.4638)
- `psyche/KoT5-summarization` · summarization · score=0.4434 (raw=0.4434)
- `EbanLee/kobart-summary-v3` · summarization · score=0.4379 (raw=0.4379)
- `eenzeenee/t5-base-korean-summarization` · summarization · score=0.4205 (raw=0.4205)
- `mskayacioglu/mbart50-xlsum` · summarization · score=0.4081 (raw=0.4081)

## q07_ko_qa 한국어 질문 답변 모델, 3B 이하
후보 6개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `monologg/koelectra-base-v3-finetuned-korquad` · question-answering · score=0.3907 (raw=0.3907)
- `bespin-global/klue-bert-base-aihub-mrc` · question-answering · score=0.3815 (raw=0.3815)
- `timpal0l/mdeberta-v3-base-squad2` · question-answering · score=0.3775 (raw=0.3775)
- `monologg/koelectra-small-v2-distilled-korquad-384` · question-answering · score=0.3719 (raw=0.3719)
- `FreedomIntelligence/Apollo-MoE-0.5B` · question-answering · score=0.3657 (raw=0.3657)

## q08_ko_generation_long_context 한국어 텍스트 생성 모델, context 8192 이상
후보 1172개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `blueapple8259/TinyKo` · text-generation · score=0.5623 (raw=0.5623)
- `mkd-hossain/Keural-Cortex-8B-64K` · text-generation · score=0.5608 (raw=0.5608)
- `MyeongHo0621/Qwen2.5-3B-Korean` · text-generation · score=0.5575 (raw=0.5575)
- `teddylee777/Qwen2.5-7B-Instruct-kowiki-qa-context-gguf` · text-generation · score=0.5535 (raw=0.5535)
- `blueapple8259/test_model1` · text-generation · score=0.5481 (raw=0.5481)

## q09_ko_multimodal 한국어 이미지와 텍스트를 함께 처리하는 멀티모달 모델
후보 385개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `kanarena/supergemma4-e4b-abliterated-multimodal-gguf-4bit` · image-text-to-text · score=0.5302 (raw=0.5302)
- `McG-221/SuperQwen3.8-27b-abliterated-Q8_0-GGUF` · image-text-to-text · score=0.5267 (raw=0.5267)
- `nopesadly/GLM-OCR-Q4_K_M.gguf` · image-text-to-text · score=0.5267 (raw=0.5267)
- `mncai/Hunmin-397B-A17B-CUA-FP8` · image-text-to-text · score=0.5261 (raw=0.5261)
- `mobilint/aya-vision-8b` · image-text-to-text · score=0.5249 (raw=0.5249)

## q10_ko_small_low_popularity 다운로드 80~499의 한국어 텍스트 생성 모델
후보 1313개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `north-wind/TinyStories-Korean-800K` · text-generation · score=0.6114 (raw=0.6114)
- `MyeongHo0621/Qwen2.5-3B-Korean` · text-generation · score=0.5901 (raw=0.5901)
- `blueapple8259/TinyKo` · text-generation · score=0.5854 (raw=0.5854)
- `lcw99/ko-dialoGPT-korean-chit-chat` · text-generation · score=0.5842 (raw=0.5842)
- `zhiyuan8/RWKV-v7-0.4B-G1-GGUF` · text-generation · score=0.5750 (raw=0.5750)

## q11_ko_known_hardware 파라미터와 context 정보가 확인된 한국어 임베딩 모델
후보 374개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `madatnlp/km-bert` · feature-extraction · score=0.5062 (raw=0.5062)
- `mp-juuuns/qwen3.5-4l-vocab40k-en-ko-headless` · feature-extraction · score=0.4969 (raw=0.4969)
- `artificial-nerds/pmnet` · sentence-similarity · score=0.4933 (raw=0.4933)
- `nounagnonsavoedo/multilingual-e5-base` · sentence-similarity · score=0.4910 (raw=0.4910)
- `nvidia/Nemotron-3-Embed-1B-NVFP4` · sentence-similarity · score=0.4905 (raw=0.4905)

## q12_ko_generation_unknown_safe 한국어 생성 모델, 3B 이하이며 수치가 확인된 후보만
후보 374개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `quantumaikr/KoreanLM-3B` · text-generation · score=0.4810 (raw=0.4810)
- `Bingsu/kanana-2-1.3b-instruct` · text-generation · score=0.4626 (raw=0.4626)
- `young-kim123/qwen3-1.7b-mymodel` · text-generation · score=0.4375 (raw=0.4375)
- `postcn/Jeju-Standard_Korean_Translator` · text-generation · score=0.4373 (raw=0.4373)
- `Infinity08/KAWK-500M-Korean-Instruct-v1` · text-generation · score=0.4331 (raw=0.4331)

## q13_small_cpu_classifier CPU에서 빠르게 돌릴 수 있는 5억 파라미터 이하 텍스트 분류 모델을 찾아줘
후보 60개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `solbi12/ecommers_fasion_fine_tuned_3class_model` · text-classification · score=0.4140 (raw=0.4140)
- `monologg/koelectra-base-finetuned-nsmc` · text-classification · score=0.3858 (raw=0.3858)
- `monologg/koelectra-small-finetuned-nsmc` · text-classification · score=0.3837 (raw=0.3837)
- `Huffon/klue-roberta-base-nli` · text-classification · score=0.3744 (raw=0.3744)
- `tartuNLP/mmBERT-small-m-edu-classifier` · text-classification · score=0.3708 (raw=0.3708)

## q14_semantic_search_embedding 의미 검색과 문장 검색에 적합한 문장 임베딩 모델을 추천해줘
후보 435개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `Moriec/Vinogradov_semantic_search` · sentence-similarity · score=0.4057 (raw=0.4057)
- `opensearch-project/opensearch-neural-sparse-encoding-multilingual-v1` · feature-extraction · score=0.3947 (raw=0.3947)
- `artificial-nerds/pmnet` · sentence-similarity · score=0.3940 (raw=0.3940)
- `ysmeta/EVE-Embed-1.1-Legal` · sentence-similarity · score=0.3884 (raw=0.3884)
- `nlpai-lab/KURE-v2` · sentence-similarity · score=0.3882 (raw=0.3882)

## q15_long_context_embedding 8192토큰 이상 긴 문서를 처리할 수 있는 임베딩 모델이 필요해
후보 132개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `nvidia/Nemotron-3-Embed-1B-NVFP4` · sentence-similarity · score=0.3848 (raw=0.3848)
- `codefuse-ai/F2LLM-v2-80M` · feature-extraction · score=0.3624 (raw=0.3624)
- `cnmoro/snowflake-arctic-embed-m-v2.0-cpu` · sentence-similarity · score=0.3612 (raw=0.3612)
- `mlx-community/LFM2.5-Embedding-350M-4bit` · sentence-similarity · score=0.3598 (raw=0.3598)
- `codefuse-ai/F2LLM-v2-8B` · feature-extraction · score=0.3588 (raw=0.3588)

## q16_realtime_asr_small 실시간 음성 인식에 쓸 수 있고 10억 파라미터 이하인 작은 모델을 찾아줘
후보 60개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `Edge0/Audio8-ASR-0.1B` · automatic-speech-recognition · score=0.3580 (raw=0.3580)
- `appautomaton/nemotron-3.5-asr-streaming-0.6b-int8-mlx` · automatic-speech-recognition · score=0.3554 (raw=0.3554)
- `aufklarer/Qwen3-ASR-1.7B-MLX-4bit` · automatic-speech-recognition · score=0.3506 (raw=0.3506)
- `mobilint/whisper-small` · automatic-speech-recognition · score=0.3478 (raw=0.3478)
- `mobilint/whisper-large-v3-turbo` · automatic-speech-recognition · score=0.3380 (raw=0.3380)

## q17_english_german_translation 영어와 독일어 사이를 번역하는 기계 번역 모델을 추천해줘
후보 239개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `mradermacher/EraX-Translator-V1.0-i1-GGUF` · translation · score=0.4455 (raw=0.4455)
- `sappho192/aihub-ja-ko-translator` · translation · score=0.4368 (raw=0.4368)
- `facebook/mbart-large-cc25` · translation · score=0.4265 (raw=0.4265)
- `sappho192/ffxiv-ja-ko-translator` · translation · score=0.4257 (raw=0.4257)
- `jhk/opus-mt-tc-big-wiki-en-ko` · translation · score=0.4228 (raw=0.4228)

## q18_long_document_summarization 긴 문서를 요약할 수 있고 30억 파라미터 이하인 모델을 찾아줘
후보 2개, 결과 2개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `EbanLee/kobart-summary-v3` · summarization · score=0.3349 (raw=0.3349)
- `mskayacioglu/mbart50-xlsum` · summarization · score=0.3219 (raw=0.3219)

## q19_small_question_answering 질문에 답하는 용도의 10억 파라미터 이하 소형 모델을 추천해줘
후보 5개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `FreedomIntelligence/Apollo-MoE-0.5B` · question-answering · score=0.2937 (raw=0.2937)
- `monologg/koelectra-base-v3-finetuned-korquad` · question-answering · score=0.2680 (raw=0.2680)
- `bespin-global/klue-bert-base-aihub-mrc` · question-answering · score=0.2632 (raw=0.2632)
- `monologg/koelectra-small-v2-distilled-korquad-384` · question-answering · score=0.2629 (raw=0.2629)
- `timpal0l/mdeberta-v3-base-squad2` · question-answering · score=0.2421 (raw=0.2421)

## q20_long_context_generation 16K 이상 긴 컨텍스트를 지원하는 80억 파라미터 이하 지시문 생성 모델이 필요해
후보 522개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `qingy2024/Qwark-4B` · text-generation · score=0.3869 (raw=0.3869)
- `CMSManhattan/JiRackUltra_1b` · text-generation · score=0.3866 (raw=0.3866)
- `jwg0830/AX-3.1-Light-sft_v0_1` · text-generation · score=0.3860 (raw=0.3860)
- `Calandracas/minnow-pico-50M-base` · text-generation · score=0.3777 (raw=0.3777)
- `lcw99/zephykor-ko-beta-7b-chang` · text-generation · score=0.3754 (raw=0.3754)

## q21_vision_language_ocr 이미지를 이해하고 OCR도 수행할 수 있는 비전 언어 모델을 찾아줘
후보 385개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `EZCon/GLM-OCR-4bit-mlx` · image-text-to-text · score=0.5037 (raw=0.5037)
- `ONTHEIT/BizOnAI-OCR` · image-text-to-text · score=0.4856 (raw=0.4856)
- `Lamapi/next-ocr-Q4_K_M-GGUF` · image-text-to-text · score=0.4835 (raw=0.4835)
- `batiai/batisee` · image-text-to-text · score=0.4703 (raw=0.4703)
- `NCSOFT/VARCO-VISION-2.0-1.7B-OCR` · image-text-to-text · score=0.4650 (raw=0.4650)

## q22_low_popularity_generation 실험용으로 사용할 다운로드 수가 낮은 텍스트 생성 모델을 추천해줘
후보 1313개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `north-wind/TinyStories-Korean-800K` · text-generation · score=0.4285 (raw=0.4285)
- `Yaongi/HybriKo-117M-ToolLLaMA-SFT` · text-generation · score=0.4173 (raw=0.4173)
- `zhiyuan8/RWKV-v7-0.4B-G1-GGUF` · text-generation · score=0.4123 (raw=0.4123)
- `blueapple8259/TinyKo` · text-generation · score=0.4114 (raw=0.4114)
- `Sangto/T3Q-qwen2.5-14b-v1.0-e3-Q4_K_M-GGUF` · text-generation · score=0.4091 (raw=0.4091)

## q23_known_embedding_metadata 파라미터 수와 컨텍스트 길이가 모두 확인된 임베딩 모델을 찾아줘
후보 374개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `artificial-nerds/pmnet` · sentence-similarity · score=0.3070 (raw=0.3070)
- `severinsimmler/xlm-roberta-longformer-base-16384` · feature-extraction · score=0.3022 (raw=0.3022)
- `severinsimmler/xlm-roberta-longformer-large-16384` · feature-extraction · score=0.3021 (raw=0.3021)
- `sangmini/msmarco-cotmae-MiniLM-L12_en-ko-ja` · sentence-similarity · score=0.2991 (raw=0.2991)
- `hasankursun/matryoshka-embedding-v1` · sentence-similarity · score=0.2986 (raw=0.2986)

## q24_small_sentence_similarity 10억 파라미터 이하로 문장 유사도를 계산하는 모델을 추천해줘
후보 248개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `hasankursun/matryoshka-embedding-v1` · sentence-similarity · score=0.3176 (raw=0.3176)
- `ysmeta/EVE-Embed-1.0-Legal` · sentence-similarity · score=0.3107 (raw=0.3107)
- `gomyk/me5s-me5s_compressed_v3_distilled` · sentence-similarity · score=0.3087 (raw=0.3087)
- `dragonkue/colbert-ko-0.1b` · sentence-similarity · score=0.3081 (raw=0.3081)
- `BCCard/MoAI-Embedding-0.6B` · sentence-similarity · score=0.3069 (raw=0.3069)

## q25_compact_translation 10억 파라미터 이하의 가벼운 기계 번역 모델이 필요해
후보 20개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `alirezamsh/small100` · translation · score=0.4418 (raw=0.4418)
- `Sube126/Hy-MT2-1.8B-1.25Bit-MLX` · translation · score=0.4269 (raw=0.4269)
- `Neurora/opus-hplt-en-ko-v2.0` · translation · score=0.4156 (raw=0.4156)
- `dhtocks/nllb-200-distilled-350M_en-ko` · translation · score=0.4117 (raw=0.4117)
- `Helsinki-NLP/opus-mt_tiny_kor-eng` · translation · score=0.4015 (raw=0.4015)

## q26_on_device_asr 엣지 디바이스에서 사용할 5억 파라미터 이하 음성 인식 모델을 찾아줘
후보 32개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `seastar105/whisper-small-komixv2` · automatic-speech-recognition · score=0.3991 (raw=0.3991)
- `Edge0/Audio8-ASR-0.1B` · automatic-speech-recognition · score=0.3919 (raw=0.3919)
- `42MARU/ko-spelling-wav2vec2-conformer-del-1s` · automatic-speech-recognition · score=0.3666 (raw=0.3666)
- `moonshine-ai/moonshine-base-ko` · automatic-speech-recognition · score=0.3641 (raw=0.3641)
- `mobilint/whisper-large-v3-turbo` · automatic-speech-recognition · score=0.3628 (raw=0.3628)

## q27_very_long_context_generation 32K 이상의 컨텍스트 길이를 지원하는 텍스트 생성 모델을 추천해줘
후보 1092개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `teddylee777/Qwen2.5-7B-Instruct-kowiki-qa-gguf` · text-generation · score=0.4373 (raw=0.4373)
- `qingy2024/Qwark-4B` · text-generation · score=0.4354 (raw=0.4354)
- `teddylee777/Qwen2.5-7B-Instruct-kowiki-qa-context-gguf` · text-generation · score=0.4340 (raw=0.4340)
- `kimjg/recallResolver-1B` · text-generation · score=0.4334 (raw=0.4334)
- `SamsungSAILMontreal/ByteCraft` · text-generation · score=0.4333 (raw=0.4333)

## q28_medium_text_classifier 성능과 크기의 균형이 좋은 30억 파라미터 이하 텍스트 분류 모델을 찾아줘
후보 69개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `solbi12/ecommers_fasion_fine_tuned_3class_model` · text-classification · score=0.4418 (raw=0.4418)
- `llm-semantic-router/mmbert-rerank-32k-2d-matryoshka` · text-classification · score=0.3856 (raw=0.3856)
- `circulus/koelectra-polite-v1` · text-classification · score=0.3774 (raw=0.3774)
- `amphora/KorFinASC-XLM-RoBERTa` · text-classification · score=0.3753 (raw=0.3753)
- `circulus/koelectra-wellness-v1` · text-classification · score=0.3737 (raw=0.3737)

## q29_very_long_embedding 16K 이상 긴 문서를 임베딩할 수 있는 모델을 추천해줘
후보 84개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `mlx-community/LFM2.5-Embedding-350M-4bit` · sentence-similarity · score=0.3705 (raw=0.3705)
- `shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4` · sentence-similarity · score=0.3683 (raw=0.3683)
- `codefuse-ai/F2LLM-v2-160M` · feature-extraction · score=0.3662 (raw=0.3662)
- `codefuse-ai/F2LLM-v2-14B` · feature-extraction · score=0.3660 (raw=0.3660)
- `codefuse-ai/F2LLM-v2-80M` · feature-extraction · score=0.3656 (raw=0.3656)

## q30_general_question_answering 범용 질문 답변에 사용할 30억 파라미터 이하 모델을 추천해줘
후보 6개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `monologg/koelectra-base-v3-finetuned-korquad` · question-answering · score=0.3405 (raw=0.3405)
- `monologg/koelectra-small-v2-distilled-korquad-384` · question-answering · score=0.3288 (raw=0.3288)
- `FreedomIntelligence/Apollo-MoE-0.5B` · question-answering · score=0.3251 (raw=0.3251)
- `timpal0l/mdeberta-v3-base-squad2` · question-answering · score=0.3220 (raw=0.3220)
- `bespin-global/klue-bert-base-aihub-mrc` · question-answering · score=0.3139 (raw=0.3139)

## q31_mteb_arguana_ndcg MTEB ArguAna에서 nDCG@10 성능이 보고된 문장 검색 임베딩 모델을 추천해줘
후보 435개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `Teradata/multilingual-e5-base` · sentence-similarity · score=0.4796 (raw=0.4344) [benchmark MTEB ndcg-at-10 score=44.230000000000004 boost=0.04519653339336116]
- `NaganoJRC/multilingual-e5-base` · sentence-similarity · score=0.4615 (raw=0.4163) [benchmark MTEB ndcg-at-10 score=44.230000000000004 boost=0.04519653339336116]
- `Alibaba-NLP/gte-multilingual-base` · sentence-similarity · score=0.4607 (raw=0.4058) [benchmark MTEB ndcg-at-10 score=58.231 boost=0.05489402780904227]
- `AbdullahMoQH/multilingual-e5-base` · sentence-similarity · score=0.4587 (raw=0.4135) [benchmark MTEB ndcg-at-10 score=44.230000000000004 boost=0.04519653339336116]
- `nmixx-fin/nmixx-bge-m3` · sentence-similarity · score=0.4438 (raw=0.4438)

## q32_mteb_embedding_evidence MTEB 평가 결과가 README에 근거와 함께 기록된 임베딩 모델을 찾아줘
후보 435개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `Teradata/multilingual-e5-base` · sentence-similarity · score=0.4701 (raw=0.4551) [benchmark MTEB accuracy score=78.97014925373135 boost=0.015]
- `amazon/Titan-text-embeddings-v2` · feature-extraction · score=0.4397 (raw=0.4247) [benchmark MTEB accuracy score=79.31343283582089 boost=0.015]
- `cnmoro/snowflake-arctic-embed-m-v2.0-cpu` · sentence-similarity · score=0.4397 (raw=0.4247) [benchmark MTEB accuracy score=66.6867 boost=0.015]
- `shadowrock-io/Nemotron-3-Embed-8B-Community-MLX-4bit` · sentence-similarity · score=0.4380 (raw=0.4230) [benchmark MTEB ndcg-at-10 score=1.0 boost=0.015]
- `gimhae-geunamja/bge-m3-ko-public-admin` · sentence-similarity · score=0.4332 (raw=0.4332)

## q33_asr_wer_evidence WER 평가 수치가 확인되는 음성 인식 모델을 추천해줘
후보 234개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `junnei/Phi-4-multimodal-instruct-ko-asr` · automatic-speech-recognition · score=0.4379 (raw=0.4229) [benchmark zeroth-korean-test wer score=2.951 boost=0.015]
- `handy-computer/SenseVoiceSmall-gguf` · automatic-speech-recognition · score=0.4202 (raw=0.4202)
- `seastar105/whisper-medium-komixv2` · automatic-speech-recognition · score=0.4171 (raw=0.4171)
- `EvoAwaken-Workshop/VibeVoice-ASR-Streaming-7B-GGUF` · automatic-speech-recognition · score=0.4170 (raw=0.4170)
- `Lexius/Phi-4-multimodal-instruct` · automatic-speech-recognition · score=0.4129 (raw=0.4129)

## q34_ko_summarization_small_long 한국어 긴 문서를 요약하는 3B 이하 모델 중 context 4096 이상이고 파라미터와 context가 모두 확인된 후보
후보 0개, 결과 0개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0

## q35_ko_asr_edge_low 다운로드가 낮고 5억 파라미터 이하인 한국어 실시간 음성 인식 모델
후보 15개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `seastar105/whisper-small-komixv2` · automatic-speech-recognition · score=0.4366 (raw=0.4366)
- `kimthegarden/whisper-small-ko-new` · automatic-speech-recognition · score=0.4243 (raw=0.4243)
- `Bingsu/distilhubert-ko-zeroth` · automatic-speech-recognition · score=0.4091 (raw=0.4091)
- `mobilint/whisper-large-v3-turbo` · automatic-speech-recognition · score=0.4071 (raw=0.4071)
- `team-lucid/hubert-large-korean` · automatic-speech-recognition · score=0.4013 (raw=0.4013)

## q36_en_to_ko_translation_small 영어에서 한국어로 번역하는 10억 파라미터 이하의 가벼운 모델
후보 20개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `Helsinki-NLP/opus-mt_tiny_kor-eng` · translation · score=0.4941 (raw=0.4941)
- `sappho192/aihub-ja-ko-translator` · translation · score=0.4875 (raw=0.4875)
- `Neurora/opus-hplt-en-ko-v2.0` · translation · score=0.4837 (raw=0.4837)
- `Helsinki-NLP/opus-mt-tc-big-ko-en` · translation · score=0.4828 (raw=0.4828)
- `sappho192/ffxiv-ja-ko-translator` · translation · score=0.4824 (raw=0.4824)

## q37_ko_embedding_long_small 한국어 긴 문서 검색용 임베딩 모델 중 1.5B 이하이고 context 16384 이상인 후보
후보 62개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `mp-juuuns/qwen3.5-4l-vocab40k-en-ko-headless` · feature-extraction · score=0.4674 (raw=0.4674)
- `LiquidAI/LFM2-ColBERT-350M` · sentence-similarity · score=0.4652 (raw=0.4652)
- `LiquidAI/LFM2.5-Embedding-350M` · sentence-similarity · score=0.4645 (raw=0.4645)
- `BCCard/MoAI-Embedding-0.6B` · sentence-similarity · score=0.4601 (raw=0.4601)
- `nvidia/Nemotron-3-Embed-1B-BF16` · sentence-similarity · score=0.4506 (raw=0.4506)

## q38_ko_vision_ocr_small 한국어 문서 이미지와 OCR을 처리할 수 있는 5B 이하 비전 언어 모델
후보 63개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `EZCon/GLM-OCR-4bit-mlx` · image-text-to-text · score=0.5644 (raw=0.5644)
- `NCSOFT/VARCO-VISION-2.0-1.7B-OCR` · image-text-to-text · score=0.5472 (raw=0.5472)
- `mobilint/aya-vision-8b` · image-text-to-text · score=0.5330 (raw=0.5330)
- `mlx-community/LFM2.5-VL-450M-6bit` · image-text-to-text · score=0.5165 (raw=0.5165)
- `CohereLabs/North-Micro-Vision-Instruct` · image-text-to-text · score=0.5122 (raw=0.5122)

## q39_ko_qa_context 한국어 질문 답변에 사용할 3B 이하 모델 중 context 2048 이상이고 파라미터가 확인된 후보
후보 2개, 결과 2개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=1
- `FreedomIntelligence/Apollo-MoE-0.5B` · question-answering · score=0.4019 (raw=0.4019)
- `haiFrHust/VNJPTranslate_base` · question-answering · score=0.3579 (raw=0.4079) [task_conflict penalty=0.05]
  - conflict evidence: question_answering_identity_marker:translate

## q40_low_long_generation 실험용 Low Popularity 중 context 32768 이상인 8B 이하 텍스트 생성 모델
후보 338개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `lcw99/zephykor-ko-beta-7b-chang` · text-generation · score=0.4269 (raw=0.4269)
- `jwg0830/AX-3.1-Light-sft_v0_1` · text-generation · score=0.4267 (raw=0.4267)
- `hoySky92/HyperCLOVA-X-U-CURATE-v2.0` · text-generation · score=0.4242 (raw=0.4242)
- `trillionlabs/Tri-7B-Search-preview` · text-generation · score=0.4194 (raw=0.4194)
- `ChanLumerico/EXAONE-3.5-7.8B-Instruct-Yaho` · text-generation · score=0.4169 (raw=0.4169)

## q41_low_small_similarity 다운로드 80~499이고 5억 파라미터 이하인 소형 문장 유사도 모델
후보 172개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `soulfree89/e5-small-ko-v2-fix` · sentence-similarity · score=0.3606 (raw=0.3606)
- `gomyk/me5s-me5s_compressed_v3_distilled` · sentence-similarity · score=0.3559 (raw=0.3559)
- `gomyk/me5s-student-me5s_compressed_v4_distilled` · sentence-similarity · score=0.3507 (raw=0.3507)
- `gomyk/me5s-student-me5s_compressed_v3_distilled` · sentence-similarity · score=0.3467 (raw=0.3467)
- `DLCorso/multilingual-e5-small` · sentence-similarity · score=0.3450 (raw=0.3450)

## q42_low_asr_wer Low Popularity 한국어 음성 인식 모델 중 README에 WER 수치가 기록된 후보
후보 103개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `TeamUNIVA/qwen3_asr_1.7b_ko_beta` · automatic-speech-recognition · score=0.4578 (raw=0.4578)
- `rearleg/SeloWhisper-ko-disfluency` · automatic-speech-recognition · score=0.4575 (raw=0.4425) [benchmark Held-out wer score=0.33 boost=0.015]
- `BuzzASR/korean` · automatic-speech-recognition · score=0.4558 (raw=0.4558)
- `mlx-community/VibeVoice-ASR-Streaming-7B-4bit` · automatic-speech-recognition · score=0.4553 (raw=0.4553)
- `OpenVoiceOS/qwen3-asr-0.6b-q5-k-m` · automatic-speech-recognition · score=0.4499 (raw=0.4499)

## q43_ko_mteb_long 한국어 긴 문서 임베딩에서 MTEB 평가 근거가 있고 context 8192 이상인 모델
후보 132개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `nmixx-fin/nmixx-bge-m3` · sentence-similarity · score=0.5097 (raw=0.5097)
- `hyunseop/bge-m3-ko` · sentence-similarity · score=0.4890 (raw=0.4890)
- `cnmoro/snowflake-arctic-embed-m-v2.0-cpu` · sentence-similarity · score=0.4884 (raw=0.4734) [benchmark MTEB accuracy score=66.6867 boost=0.015]
- `leeloolee/intention` · sentence-similarity · score=0.4705 (raw=0.4705)
- `shadowrock-io/Nemotron-3-Embed-8B-Community-MLX-4bit` · sentence-similarity · score=0.4680 (raw=0.4530) [benchmark MTEB ndcg-at-10 score=1.0 boost=0.015]

## q44_cpu_tiny_classifier CPU에서 사용할 1억 파라미터 이하 초소형 텍스트 분류 모델이며 파라미터 수가 확인된 후보
후보 9개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `monologg/koelectra-small-finetuned-nsmc` · text-classification · score=0.4119 (raw=0.4119)
- `snunlp/KR-FinBert-SC` · text-classification · score=0.4089 (raw=0.4089)
- `kfkas/legal-question-filter-koelectra` · text-classification · score=0.3824 (raw=0.3824)
- `bongsoo/albert-small-kor-cross-encoder-v1` · text-classification · score=0.3768 (raw=0.3768)
- `ethicalabs/Echo-DSRN-v0.1.3-Intent-CLF` · text-classification · score=0.3731 (raw=0.3731)

## q45_ko_multitask_retrieval_qa 한국어 검색과 질문 답변을 모두 고려할 수 있는 1B 이하 모델
후보 253개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `monologg/koelectra-base-v3-finetuned-korquad` · question-answering · score=0.4036 (raw=0.4036)
- `soulfree89/e5-small-ko-v2-fix` · sentence-similarity · score=0.4036 (raw=0.4036)
- `nmixx-fin/nmixx-bge-m3` · sentence-similarity · score=0.4028 (raw=0.4028)
- `exp-models/dragonkue-KoEn-E5-Tiny` · sentence-similarity · score=0.3933 (raw=0.3933)
- `FreedomIntelligence/Apollo-MoE-0.5B` · question-answering · score=0.3928 (raw=0.3928)

## q46_ko_generation_known_all 파라미터와 context가 모두 확인된 2B 이하 한국어 텍스트 생성 모델, context 4096 이상
후보 228개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `blueapple8259/TinyKo` · text-generation · score=0.4815 (raw=0.4815)
- `Mozilla/Qwen2.5-0.5B-Instruct` · text-generation · score=0.4808 (raw=0.4808)
- `ceyda/Qwen3-1.7B-Base-trim-koen-32768` · text-generation · score=0.4759 (raw=0.4759)
- `Bingsu/kanana-2-1.3b-instruct` · text-generation · score=0.4752 (raw=0.4752)
- `blueapple8259/test_model1` · text-generation · score=0.4735 (raw=0.4735)

## q47_low_compact_translation Low Popularity에서 5억 파라미터 이하인 한국어 번역 모델
후보 9개, 결과 5개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
- `Helsinki-NLP/opus-mt_tiny_kor-eng` · translation · score=0.4660 (raw=0.4660)
- `Neurora/opus-hplt-en-ko-v2.0` · translation · score=0.4644 (raw=0.4644)
- `seongs/ke-t5-base-aihub-koen-translation-integrated-10m-en-to-ko` · translation · score=0.4592 (raw=0.4592)
- `Darong/BlueT` · translation · score=0.4586 (raw=0.4586)
- `sappho192/gemma3-multilingual-translator-270m` · translation · score=0.4479 (raw=0.4479)

## q48_intentionally_empty 한국어 text-generation 중 10M 이하이고 context 131072 이상인 모델
후보 0개, 결과 0개, 통과=True
task 위반=0, 한국어 위반=0, unknown 위반=0, canonical 중복=0, task conflict=0
