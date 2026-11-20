"""model_comparison 질문 40개 — 사용자가 모델 둘을 대고 비교를 요청하는 경우.

채점은 두 계열의 모델명 정규식이다. 각 계열의 원본이 2점, 같은 가중치의
변환·양자화·재업로드가 1점이다.

이 유형의 불변식은 **양쪽 계열에 모두 정답이 있어야 한다**는 것이다. 한쪽만
찾으면 비교라는 답변이 성립하지 않는다. 쌍은 전부 코퍼스에 양쪽 모델이 실제로
있는 것만 골랐다(verify 가 매번 다시 확인한다).
"""

GEN = ["text-generation"]
EMB = ["sentence-similarity", "feature-extraction"]
ASR = ["automatic-speech-recognition"]
TR = ["translation"]
CLS = ["text-classification"]
VLM = ["image-text-to-text"]


def q(qid, text, a, b, originals=None, tasks=None, persona="ml_engineer", style="technical"):
    """a, b: (표시 이름, id 정규식)"""
    return {
        "qid": qid, "text": text, "query_type": "model_comparison", "origin": "corpus_grounded",
        "persona": persona, "expression_style": style,
        "conditions": {"korean_required": True, **({"tasks": tasks} if tasks else {})},
        "conditions_fidelity": {"tasks": "질의가 지목한 모델 종류"} if tasks else {},
        "comparison_groups": {a[0]: a[1], b[0]: b[1]},
        "relevance_rule": {
            "grade_2": "각 계열의 원본 모델",
            "grade_1": "각 계열의 변환·양자화·재업로드본",
            "families": [{"name": a[0], "id_regex": a[1]}, {"name": b[0], "id_regex": b[1]}],
            **({"originals": originals} if originals else {}),
        },
    }


QUERIES = [
    # ── 한국어 LLM 끼리 ────────────────────────────────────────
    q("mc01", "2B 남짓한 소형 한국어 챗봇으로 EXAONE 3.5 2.4B 와 kanana 1.5 2.1b 중 하나를 고르려고 해요. 둘 다 보여 주세요.",
      ("EXAONE-3.5-2.4B", r"exaone-3\.5-2\.4b-instruct"), ("kanana-1.5-2.1b", r"kanana-1\.5-2\.1b"),
      [r"LGAI-EXAONE/EXAONE-3\.5-2\.4B-Instruct", r"kakaocorp/kanana-1\.5-2\.1b-instruct-2505",
       r"kakaocorp/kanana-1\.5-2\.1b-base"], tasks=GEN),
    q("mc02", "저사양 PC 용으로 믿음 2.0 Mini 랑 EXAONE 4.0 1.2B 를 비교해 보고 싶어요.",
      ("Midm-2.0-Mini", r"midm-2\.0-mini"), ("EXAONE-4.0-1.2B", r"exaone-4\.0-1\.2b"),
      [r"K-intelligence/Midm-2\.0-Mini-Instruct", r"LGAI-EXAONE/EXAONE-4\.0-1\.2B"], tasks=GEN),
    q("mc03", "8B 급 한국어 LLM 으로 EXAONE 3.5 7.8B 와 kanana 1.5 8b 중 뭐가 나을지 비교하려고 합니다.",
      ("EXAONE-3.5-7.8B", r"exaone-3\.5-7\.8b"), ("kanana-1.5-8b", r"kanana-1\.5-8b"),
      [r"LGAI-EXAONE/EXAONE-3\.5-7\.8B-Instruct", r"kakaocorp/kanana-1\.5-8b-instruct-2505",
       r"kakaocorp/kanana-1\.5-8b-base"], tasks=GEN),
    q("mc04", "SKT A.X-4.0-Light 와 trillionlabs Tri-21B-Think 를 비교해 주세요.",
      ("A.X-4.0-Light", r"a\.x-4\.0-light"), ("Tri-21B-Think", r"tri-21b-think"),
      [r"skt/A\.X-4\.0-Light", r"trillionlabs/Tri-21B-Think$"], tasks=GEN),
    q("mc05", "대형 한국어 모델로 Solar-Open2-250B 와 K-EXAONE-236B 중 무엇을 볼지 비교하고 싶습니다.",
      ("Solar-Open2-250B", r"solar-open2-250b"), ("K-EXAONE-236B", r"k-exaone-236b"),
      [r"upstage/Solar-Open2-250B", r"LGAI-EXAONE/K-EXAONE-236B-A23B"], tasks=GEN),
    q("mc06", "EXAONE-Deep-7.8B 와 EXAONE-3.5-7.8B-Instruct 가 어떻게 다른지 둘 다 보고 싶어요.",
      ("EXAONE-Deep-7.8B", r"exaone-deep-7\.8b"), ("EXAONE-3.5-7.8B-Instruct", r"exaone-3\.5-7\.8b-instruct"),
      [r"LGAI-EXAONE/EXAONE-Deep-7\.8B", r"LGAI-EXAONE/EXAONE-3\.5-7\.8B-Instruct"], tasks=GEN),
    q("mc07", "Llama 3 기반 8B 한국어 모델인 Bllossom 8B 와 Llama-VARCO-8B-Instruct 를 비교하려고 합니다.",
      ("Bllossom-8B", r"llama-3-korean-bllossom-8b"), ("Llama-VARCO-8B", r"llama-varco-8b"),
      [r"MLP-KTLim/llama-3-Korean-Bllossom-8B", r"NCSOFT/Llama-VARCO-8B-Instruct"], tasks=GEN),
    q("mc08", "polyglot-ko-5.8b 와 kogpt2-base-v2 중 베이스로 뭘 쓸지 비교하고 싶어요.",
      ("polyglot-ko-5.8b", r"polyglot-ko-5\.8b"), ("kogpt2-base-v2", r"kogpt2-base-v2"),
      [r"EleutherAI/polyglot-ko-5\.8b", r"skt/kogpt2-base-v2"], tasks=GEN),
    q("mc09", "trillionlabs 의 Gravity-30B-A5B 와 Gravity-16B-A3B 를 비교해 주세요.",
      ("Gravity-30B-A5B", r"gravity-30b-a5b"), ("Gravity-16B-A3B", r"gravity-16b-a3b"),
      [r"trillionlabs/Gravity-30B-A5B-Base", r"trillionlabs/Gravity-16B-A3B-Base"], tasks=GEN),
    # EXAONE-4.5-33B 는 코퍼스에서 image-text-to-text 로 분류돼 있어 GEN 으로 좁히면 빠진다.
    q("mc10", "EXAONE-4.0-32B 와 EXAONE-4.5-33B 중 어느 쪽을 쓸지 비교하고 싶습니다.",
      ("EXAONE-4.0-32B", r"exaone-4\.0-32b"), ("EXAONE-4.5-33B", r"exaone-4\.5-33b"),
      [r"LGAI-EXAONE/EXAONE-4\.0-32B", r"LGAI-EXAONE/EXAONE-4\.5-33B"]),
    q("mc11", "EXAONE-Deep-2.4B 와 EXAONE-Deep-32B 를 같이 보고 싶어요. 크기별로 비교하려고요.",
      ("EXAONE-Deep-2.4B", r"exaone-deep-2\.4b"), ("EXAONE-Deep-32B", r"exaone-deep-32b"),
      [r"LGAI-EXAONE/EXAONE-Deep-2\.4B", r"LGAI-EXAONE/EXAONE-Deep-32B"], tasks=GEN),
    q("mc12", "skt A.X-K2 와 upstage Solar-Open-100B 를 비교해 주세요.",
      ("A.X-K2", r"a\.x-k2"), ("Solar-Open-100B", r"solar-open-100b"),
      [r"skt/A\.X-K2", r"upstage/Solar-Open-100B"], tasks=GEN),
    q("mc13", "EXAONE 3.0 7.8B 와 EXAONE 3.5 7.8B 가 얼마나 다른지 둘 다 보여 주세요.",
      ("EXAONE-3.0-7.8B", r"exaone-3\.0-7\.8b"), ("EXAONE-3.5-7.8B", r"exaone-3\.5-7\.8b"),
      [r"LGAI-EXAONE/EXAONE-3\.0-7\.8B-Instruct", r"LGAI-EXAONE/EXAONE-3\.5-7\.8B-Instruct"], tasks=GEN),
    q("mc14", "kanana-nano-2.1b-instruct 와 kanana-1.5-2.1b-instruct 중 어느 걸 쓸지 비교하고 싶어요.",
      ("kanana-nano-2.1b", r"kanana-nano-2\.1b"), ("kanana-1.5-2.1b", r"kanana-1\.5-2\.1b"),
      [r"kakaocorp/kanana-nano-2\.1b-instruct", r"kakaocorp/kanana-1\.5-2\.1b-instruct-2505"], tasks=GEN),
    q("mc15", "EXAONE-3.5-32B-Instruct 와 EXAONE-4.0-32B 를 비교해 주세요.",
      ("EXAONE-3.5-32B", r"exaone-3\.5-32b"), ("EXAONE-4.0-32B", r"exaone-4\.0-32b"),
      [r"LGAI-EXAONE/EXAONE-3\.5-32B-Instruct", r"LGAI-EXAONE/EXAONE-4\.0-32B"], tasks=GEN),

    # ── 임베딩 ─────────────────────────────────────────────────
    q("mc16", "한국어 문장 임베딩으로 KoSimCSE 와 ko-sroberta 중 뭘 쓸지 비교해 보고 싶어요.",
      ("KoSimCSE", r"kosimcse"), ("ko-sroberta", r"ko-sroberta"), tasks=EMB),
    q("mc17", "한국어 검색용 임베딩으로 KURE-v1 과 KURE-v3 를 비교하려고 합니다.",
      ("KURE-v1", r"kure-v1"), ("KURE-v3", r"kure-v3"),
      [r"nlpai-lab/KURE-v3"], tasks=EMB),
    q("mc18", "bge-m3-korean 과 snowflake-arctic-embed-l-v2.0-ko 중 어느 임베딩이 나을지 비교해 주세요.",
      ("bge-m3-korean", r"bge-m3-korean"), ("snowflake-arctic-embed-l-v2.0-ko", r"snowflake-arctic-embed-l-v2\.0-ko"),
      [r"upskyy/bge-m3-korean", r"dragonkue/snowflake-arctic-embed-l-v2\.0-ko"], tasks=EMB),
    q("mc19", "kanana-2 임베딩의 1.3b 와 3b 중 어느 크기를 쓸지 비교하고 싶어요.",
      ("kanana-2-1.3b-embedding", r"kanana-2-1\.3b-embedding"), ("kanana-2-3b-embedding", r"kanana-2-3b-embedding"),
      [r"kakaocorp/kanana-2-1\.3b-embedding", r"kakaocorp/kanana-2-3b-embedding"], tasks=EMB),
    # A.X-Encoder-base 는 코퍼스에서 text-classification 으로 분류돼 있어 EMB 로 좁히면 빠진다.
    q("mc20", "skt A.X-Encoder-base 와 KURE-v3 를 임베딩 용도로 비교해 주세요.",
      ("A.X-Encoder-base", r"a\.x-encoder-base"), ("KURE-v3", r"kure-v3"),
      [r"skt/A\.X-Encoder-base", r"nlpai-lab/KURE-v3"]),

    # ── 번역 ───────────────────────────────────────────────────
    q("mc21", "한영 번역에 Helsinki-NLP opus-mt-ko-en 과 NLLB-200 distilled 600M 중 뭐가 나을지 비교하려고 해요.",
      ("opus-mt-ko-en", r"opus-mt-ko-en"), ("nllb-200-distilled-600M", r"nllb-200-distilled-600m"),
      [r"Helsinki-NLP/opus-mt-ko-en", r"facebook/nllb-200-distilled-600M"], tasks=TR),
    q("mc22", "구글 MADLAD 번역 모델과 헬싱키대 opus-mt 한영 모델 중 무엇이 나을지 비교 자료가 필요해요.",
      ("MADLAD-400", r"madlad400-[\d.]+b-mt"), ("opus-mt ko-en", r"opus-mt(-tc-big)?-ko-en"),
      [r"google/madlad400-3b-mt", r"google/madlad400-7b-mt", r"google/madlad400-10b-mt",
       r"Helsinki-NLP/opus-mt-ko-en", r"Helsinki-NLP/opus-mt-tc-big-ko-en"], tasks=TR,
      persona="korean_service_planner", style="mixed"),
    q("mc23", "한영 번역용으로 Tri-1.8B-Translation 과 NLLB-200 distilled 1.3B 를 비교해 보고 싶어요.",
      ("Tri-1.8B-Translation", r"tri-1\.8b-translation"), ("nllb-200-distilled-1.3B", r"nllb-200-distilled-1\.3b"),
      [r"trillionlabs/Tri-1\.8B-Translation", r"facebook/nllb-200-distilled-1\.3B"], tasks=TR),
    q("mc24", "다국어 번역 서버를 띄우려는데 NLLB-200 distilled 600M 이랑 M2M100 418M 을 비교하고 싶어요.",
      ("nllb-200-distilled-600M", r"nllb-200-distilled-600m"), ("m2m100_418M", r"m2m100[-_]418m"),
      [r"facebook/nllb-200-distilled-600M"], tasks=TR),
    q("mc25", "opus-mt-tc-big-en-ko 와 opus-mt-tc-big-ko-en 을 양방향으로 비교하려고 합니다.",
      ("opus-mt-tc-big-en-ko", r"opus-mt-tc-big-en-ko"), ("opus-mt-tc-big-ko-en", r"opus-mt-tc-big-ko-en"),
      [r"Helsinki-NLP/opus-mt-tc-big-en-ko", r"Helsinki-NLP/opus-mt-tc-big-ko-en"], tasks=TR),

    # ── 음성 ───────────────────────────────────────────────────
    q("mc26", "회의 녹음 받아쓰기에 SenseVoice Small 을 쓸지 whisper-large-v3-turbo 를 쓸지 고민이에요. 두 쪽 후보를 다 보여 주세요.",
      ("SenseVoiceSmall", r"sense-?voice-?small"), ("whisper-large-v3-turbo", r"whisper-large-v3-turbo"),
      [r"FunAudioLLM/SenseVoiceSmall", r"openai/whisper-large-v3-turbo"], tasks=ASR,
      persona="backend_dev", style="mixed"),
    q("mc27", "moonshine-base-ko 와 whisper-base 중 가벼운 한국어 음성 인식으로 뭐가 나을지 비교해 주세요.",
      ("moonshine-base-ko", r"moonshine-base-ko"), ("whisper-base", r"whisper-base"),
      [r"moonshine-ai/moonshine-base-ko", r"openai/whisper-base"], tasks=ASR),
    q("mc28", "whisper-small 과 whisper-medium 중 어느 쪽을 쓸지 비교하고 싶습니다.",
      ("whisper-small", r"whisper-small"), ("whisper-medium", r"whisper-medium"),
      [r"openai/whisper-small", r"openai/whisper-medium"], tasks=ASR),
    q("mc29", "nemotron-3.5-asr-streaming-0.6b 와 Qwen3-ASR-0.6B 를 스트리밍 인식용으로 비교해 주세요.",
      ("nemotron-3.5-asr-streaming", r"nemotron-3\.5-asr-streaming"), ("Qwen3-ASR-0.6B", r"qwen3-asr-0\.6b"),
      [r"nvidia/nemotron-3\.5-asr-streaming-0\.6b", r"Qwen/Qwen3-ASR-0\.6B"], tasks=ASR),
    q("mc30", "whisper-large-v3-turbo 와 whisper-large 중 뭐가 나을지 비교하고 싶어요.",
      ("whisper-large-v3-turbo", r"whisper-large-v3-turbo"), ("whisper-large", r"whisper-large(?!-v3-turbo)"),
      [r"openai/whisper-large-v3-turbo", r"openai/whisper-large"], tasks=ASR),

    # ── 비전 언어 ──────────────────────────────────────────────
    q("mc31", "한국어 이미지 이해 기능에 VARCO-VISION 2.0 1.7B 와 kanana-1.5-v-3b 중 뭐가 나을지 비교하고 싶어요.",
      ("VARCO-VISION-2.0-1.7B", r"varco-vision-2\.0-1\.7b(?!-ocr)"), ("kanana-1.5-v-3b", r"kanana-1\.5-v-3b"),
      [r"NCSOFT/VARCO-VISION-2\.0-1\.7B", r"kakaocorp/kanana-1\.5-v-3b-instruct"], tasks=VLM),
    q("mc32", "VARCO-VISION-2.0-1.7B 와 VARCO-VISION-2.0-14B 를 크기별로 비교해 주세요.",
      ("VARCO-VISION-2.0-1.7B", r"varco-vision-2\.0-1\.7b(?!-ocr)"), ("VARCO-VISION-2.0-14B", r"varco-vision-2\.0-14b"),
      [r"NCSOFT/VARCO-VISION-2\.0-1\.7B", r"NCSOFT/VARCO-VISION-2\.0-14B"], tasks=VLM),
    q("mc33", "OCR 용으로 VARCO-VISION-2.0-1.7B-OCR 과 GLM-OCR 중 어느 쪽이 나을지 보고 싶습니다.",
      ("VARCO-VISION-2.0-1.7B-OCR", r"varco-vision-2\.0-1\.7b-ocr"), ("GLM-OCR", r"glm-ocr"),
      [r"NCSOFT/VARCO-VISION-2\.0-1\.7B-OCR"], tasks=VLM),
    q("mc34", "LFM2.5-VL-3B 와 kanana-1.5-v-3b 를 비전 언어 모델로 비교해 주세요.",
      ("LFM2.5-VL-3B", r"lfm2\.5-vl-3b"), ("kanana-1.5-v-3b", r"kanana-1\.5-v-3b"),
      [r"LiquidAI/LFM2\.5-VL-3B", r"kakaocorp/kanana-1\.5-v-3b-instruct"], tasks=VLM),

    # ── 분류 ───────────────────────────────────────────────────
    q("mc35", "커뮤니티 댓글 필터로 koelectra-base-v3-hate-speech 와 koelectra-base-bias 중 뭘 쓸지 비교하려고 해요.",
      ("koelectra-base-v3-hate-speech", r"koelectra-base-v3-hate-speech"),
      ("koelectra-base-bias", r"koelectra-base(-v3)?-(gender-)?bias"),
      [r"monologg/koelectra-base-v3-hate-speech", r"monologg/koelectra-base-bias",
       r"monologg/koelectra-base-v3-bias", r"monologg/koelectra-base-gender-bias",
       r"monologg/koelectra-base-v3-gender-bias"], tasks=CLS),
    q("mc36", "감성 분석에 KR-FinBert-SC 와 koelectra 기반 감성 모델 중 뭐가 나을지 비교해 주세요.",
      ("KR-FinBert-SC", r"kr-finbert-sc"), ("koelectra 감성", r"koelectra.*sentiment"),
      [r"snunlp/KR-FinBert-SC", r"Copycats/koelectra-base-v3-generalized-sentiment-analysis"], tasks=CLS),

    # ── 교차 영역 ──────────────────────────────────────────────
    q("mc37", "요약에 kobart-summary-v3 와 t5-base-korean-summarization 중 뭐가 나을지 비교하고 싶어요.",
      ("kobart-summary-v3", r"kobart-summary-v3"), ("t5-base-korean-summarization", r"t5-base-korean-summarization"),
      [r"EbanLee/kobart-summary-v3", r"eenzeenee/t5-base-korean-summarization"]),
    q("mc38", "Midm-2.0-Mini 와 kanana-nano-2.1b 중 소형 한국어 모델로 뭐가 나을지 비교해 주세요.",
      ("Midm-2.0-Mini", r"midm-2\.0-mini"), ("kanana-nano-2.1b", r"kanana-nano-2\.1b"),
      [r"K-intelligence/Midm-2\.0-Mini-Instruct", r"kakaocorp/kanana-nano-2\.1b-instruct"], tasks=GEN),
    q("mc39", "A.X-3.1 과 A.X-4.0-Light 를 비교해 보고 싶습니다.",
      ("A.X-3.1", r"a\.x-3\.1"), ("A.X-4.0-Light", r"a\.x-4\.0-light"),
      [r"skt/A\.X-3\.1", r"skt/A\.X-4\.0-Light"], tasks=GEN),
    q("mc40", "Tri-1.8B-Translation 과 Tri-21B-Think 중 어느 trillionlabs 모델을 쓸지 비교해 주세요.",
      ("Tri-1.8B-Translation", r"tri-1\.8b-translation"), ("Tri-21B-Think", r"tri-21b-think"),
      [r"trillionlabs/Tri-1\.8B-Translation", r"trillionlabs/Tri-21B-Think$"]),
]
