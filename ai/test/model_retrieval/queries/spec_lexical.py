"""lexical_exact 질문 40개 — 사용자가 모델 이름을 직접 대는 경우.

채점은 모델 이름 정규식이다. 원본이 2점, 같은 가중치의 변환·양자화·재업로드가
1점이다. 질의가 포맷을 직접 요구하면(GGUF·ONNX 로 받고 싶다) 원본은 그 포맷이
없으므로 변환본이 2점이 된다(scan.format_requested).

계열은 전부 현재 코퍼스에 사본이 있는 것만 골랐다. 사본이 하나뿐인 계열은
'그 하나를 4,017개 중에서 찾나'를 재는 바늘찾기 문제이고, 사본이 여럿인 계열은
'원본을 변환본보다 위에 놓나'까지 본다.
"""

GEN = ["text-generation"]
EMB = ["sentence-similarity", "feature-extraction"]
ASR = ["automatic-speech-recognition"]
TR = ["translation"]
CLS = ["text-classification"]
VLM = ["image-text-to-text"]


def q(qid, text, families, originals=None, tasks=None, fmt=None,
      persona="ml_engineer", style="technical", origin="corpus_grounded"):
    rule = {
        "grade_2": "질의가 지목한 그 모델의 원본",
        "grade_1": "같은 모델의 변환·양자화·재업로드본",
        "families": families,
    }
    if originals:
        rule["originals"] = originals
    conditions = {"korean_required": True}
    if tasks:
        conditions["tasks"] = tasks
    if fmt:
        conditions["require_artifact"] = fmt
        rule["format_requested"] = True
        # scan.classify_family 가 모델명에서 포맷 표지를 찾을 때 쓴다.
        # 이게 없으면 요청한 포맷의 변환본도 1점으로 떨어진다.
        rule["format_any"] = list(fmt)
        rule["grade_2"] = "질의가 요구한 포맷으로 받을 수 있는 그 모델"
        rule["grade_1"] = "같은 계열이지만 다른 버전·용도"
    return {
        "qid": qid, "text": text, "query_type": "lexical_exact", "origin": origin,
        "persona": persona, "expression_style": style,
        "conditions": conditions,
        "conditions_fidelity": ({"tasks": "질의가 지목한 모델 종류"} if tasks else {}) |
                               ({"require_artifact": "질의가 직접 요구한 포맷"} if fmt else {}),
        "relevance_rule": rule,
    }


def fam(name, regex):
    return [{"name": name, "id_regex": regex}]


QUERIES = [
    # ── EXAONE 계열 (사본이 많아 원본/변환본 구분이 드러난다) ──
    q("lx01", "LGAI 의 EXAONE-3.5-7.8B-Instruct 를 쓰려고 합니다. 어디서 받나요?",
      fam("EXAONE-3.5-7.8B-Instruct", r"exaone-3\.5-7\.8b-instruct"),
      [r"LGAI-EXAONE/EXAONE-3\.5-7\.8B-Instruct"]),
    q("lx02", "EXAONE-4.0-1.2B 원본이랑 양자화 버전들을 한 번에 보고 싶어요.",
      fam("EXAONE-4.0-1.2B", r"exaone-4\.0-1\.2b"), [r"LGAI-EXAONE/EXAONE-4\.0-1\.2B"]),
    q("lx03", "EXAONE-Deep-7.8B 모델이 등록돼 있나요? 추론 특화 버전을 찾고 있습니다.",
      fam("EXAONE-Deep-7.8B", r"exaone-deep-7\.8b"), [r"LGAI-EXAONE/EXAONE-Deep-7\.8B"]),
    q("lx04", "EXAONE 3.5 2.4B Instruct 를 llama.cpp 로 돌리려고 하는데 GGUF 로 변환된 게 있나요?",
      fam("EXAONE-3.5-2.4B-Instruct", r"exaone-3\.5-2\.4b-instruct"), fmt=["gguf"]),
    q("lx05", "EXAONE-4.0-32B 를 찾고 있습니다.",
      fam("EXAONE-4.0-32B", r"exaone-4\.0-32b"), [r"LGAI-EXAONE/EXAONE-4\.0-32B"]),

    # ── 카카오 kanana ──
    q("lx06", "카카오가 공개한 kanana-1.5-8b-instruct 모델을 받고 싶어요.",
      fam("kanana-1.5-8b-instruct", r"kanana-1\.5-8b-instruct"),
      [r"kakaocorp/kanana-1\.5-8b-instruct-2505"]),
    q("lx07", "kanana-nano-2.1b-instruct 원본과 변환본을 같이 보고 싶습니다.",
      fam("kanana-nano-2.1b-instruct", r"kanana-nano-2\.1b-instruct"),
      [r"kakaocorp/kanana-nano-2\.1b-instruct"]),
    q("lx08", "kanana 1.5 2.1b instruct 를 GGUF 로 받을 수 있나요?",
      fam("kanana-1.5-2.1b-instruct", r"kanana-1\.5-2\.1b-instruct"), fmt=["gguf"]),
    q("lx09", "카카오가 공개한 kanana-2 임베딩 모델로 사내 검색을 만들어 보려는데, 어떤 걸 받으면 되나요?",
      fam("kanana-2 embedding", r"kanana-2-[\d.]+b-embedding"),
      [r"kakaocorp/kanana-2-[\d.]+b-embedding"], tasks=EMB, persona="backend_dev", style="mixed"),

    # ── SKT A.X ──
    q("lx10", "SKT 의 A.X-4.0-Light 모델을 찾고 있습니다.",
      fam("A.X-4.0-Light", r"a\.x-4\.0-light"), [r"skt/A\.X-4\.0-Light"]),
    q("lx11", "skt 의 A.X-Encoder-base 를 임베딩 용도로 쓰려고 합니다. 받을 수 있나요?",
      fam("A.X-Encoder-base", r"a\.x-encoder-base"), [r"skt/A\.X-Encoder-base"]),
    q("lx12", "A.X-K2 모델이 등록돼 있는지 보고 싶어요.",
      fam("A.X-K2", r"a\.x-k2"), [r"skt/A\.X-K2"]),
    q("lx13", "SKT KoGPT2 base v2 를 베이스로 실험하려고 합니다.",
      fam("kogpt2-base-v2", r"kogpt2-base-v2"), [r"skt/kogpt2-base-v2"]),

    # ── 업스테이지 Solar ──
    q("lx14", "업스테이지 Solar-Open2-250B 를 찾습니다.",
      fam("Solar-Open2-250B", r"solar-open2-250b"), [r"upstage/Solar-Open2-250B"]),
    q("lx15", "Solar-Open-100B 모델이 있나요?",
      fam("Solar-Open-100B", r"solar-open-100b"), [r"upstage/Solar-Open-100B"]),

    # ── trillionlabs ──
    q("lx16", "trillionlabs 의 Tri-1.8B-Translation 을 한영 번역에 쓰려고 합니다.",
      fam("Tri-1.8B-Translation", r"tri-1\.8b-translation"),
      [r"trillionlabs/Tri-1\.8B-Translation"], tasks=TR),
    q("lx17", "trillionlabs 의 Tri-21B-Think 모델을 받고 싶어요.",
      fam("Tri-21B-Think", r"tri-21b-think"), [r"trillionlabs/Tri-21B-Think$"]),
    q("lx18", "Gravity-30B-A5B-Base 가 등록돼 있나요?",
      fam("Gravity-30B-A5B-Base", r"gravity-30b-a5b-base"), [r"trillionlabs/Gravity-30B-A5B-Base"]),

    # ── 임베딩·인코더 ──
    q("lx19", "BM-K 의 KoSimCSE-roberta 모델이 있나요?",
      fam("KoSimCSE-roberta", r"kosimcse-roberta(?!-multitask)"), [r"BM-K/KoSimCSE-roberta"], tasks=EMB),
    q("lx20", "jhgan 의 ko-sroberta-multitask 를 문장 임베딩에 쓰려고 합니다.",
      fam("ko-sroberta-multitask", r"ko-sroberta-multitask"), [r"jhgan/ko-sroberta-multitask"], tasks=EMB),
    # nlpai-lab/KURE-v1 원본은 코퍼스에 없고 GGUF·ONNX 변환본만 있다.
    q("lx21", "KURE-v1 임베딩을 GGUF 로 받아서 llama.cpp 로 돌리려고 합니다.",
      fam("KURE-v1", r"kure-v1"), tasks=EMB, fmt=["gguf"]),
    q("lx22", "KURE-v1 임베딩을 ONNX 버전으로 받을 수 있을까요? 서버에서 ONNX Runtime 으로 돌릴 거예요.",
      fam("KURE-v1", r"kure-v1"), tasks=EMB, fmt=["onnx"]),
    q("lx23", "nlpai-lab 의 KURE-v3 가 등록돼 있나요?",
      fam("KURE-v3", r"kure-v3"), [r"nlpai-lab/KURE-v3"], tasks=EMB),
    q("lx24", "dragonkue 의 snowflake-arctic-embed-l-v2.0-ko 를 찾습니다.",
      fam("snowflake-arctic-embed-l-v2.0-ko", r"snowflake-arctic-embed-l-v2\.0-ko"),
      [r"dragonkue/snowflake-arctic-embed-l-v2\.0-ko"], tasks=EMB),
    q("lx25", "upskyy 의 bge-m3-korean 모델이 있는지 보고 싶어요.",
      fam("bge-m3-korean", r"bge-m3-korean"), [r"upskyy/bge-m3-korean"], tasks=EMB),

    # ── 분류·인코더 ──
    q("lx26", "monologg 의 koelectra-base-v3-generalized-sentiment-analysis 모델을 찾습니다.",
      fam("koelectra-base-v3-generalized-sentiment-analysis",
          r"koelectra-base-v3-generalized-sentiment-analysis"),
      [r"Copycats/koelectra-base-v3-generalized-sentiment-analysis"], tasks=CLS),
    q("lx27", "monologg 의 koelectra-base-v3-hate-speech 모델을 찾습니다.",
      fam("koelectra-base-v3-hate-speech", r"koelectra-base-v3-hate-speech"),
      [r"monologg/koelectra-base-v3-hate-speech"], tasks=CLS),
    q("lx28", "leewaay 의 klue-roberta-large-klueSTS-cross 가 등록돼 있나요? cross-encoder 로 쓰려고 합니다.",
      fam("klue-roberta-large-klueSTS-cross", r"klue-roberta-large-kluests-cross"),
      [r"leewaay/klue-roberta-large-klueSTS-cross"], tasks=EMB),

    # ── 번역 ──
    q("lx29", "Helsinki-NLP 의 opus-mt-ko-en 을 쓰려고 해요. 원본이랑 바로 쓸 수 있는 변환본이 있으면 알려 주세요.",
      fam("opus-mt-ko-en", r"opus-mt-ko-en"), [r"Helsinki-NLP/opus-mt-ko-en"], tasks=TR),
    q("lx30", "Helsinki-NLP opus-mt-tc-big-en-ko 를 영한 번역에 쓰려고 합니다.",
      fam("opus-mt-tc-big-en-ko", r"opus-mt-tc-big-en-ko"),
      [r"Helsinki-NLP/opus-mt-tc-big-en-ko"], tasks=TR),
    q("lx31", "facebook 의 nllb-200-distilled-600M 을 받고 싶어요.",
      fam("nllb-200-distilled-600M", r"nllb-200-distilled-600m"),
      [r"facebook/nllb-200-distilled-600M"], tasks=TR),
    q("lx32", "google 의 madlad400-3b-mt 번역 모델이 있나요?",
      fam("madlad400-3b-mt", r"madlad400-3b-mt"), [r"google/madlad400-3b-mt"], tasks=TR),

    # ── 음성 ──
    q("lx33", "openai 의 whisper-large-v3-turbo 가 등록돼 있는지 보고 싶습니다.",
      fam("whisper-large-v3-turbo", r"whisper-large-v3-turbo"),
      [r"openai/whisper-large-v3-turbo"], tasks=ASR),
    q("lx34", "SenseVoice Small 을 whisper.cpp 처럼 로컬에서 돌리려고 하는데 GGUF 로 변환된 게 있나요?",
      fam("SenseVoiceSmall", r"sense-?voice-?small"), tasks=ASR, fmt=["gguf"],
      persona="local_user", style="mixed"),
    q("lx35", "moonshine-base-ko 음성 인식 모델을 찾습니다.",
      fam("moonshine-base-ko", r"moonshine-base-ko"), [r"moonshine-ai/moonshine-base-ko"], tasks=ASR),

    # ── 비전 언어 ──
    q("lx36", "엔씨소프트가 OCR 전용으로 낸 바르코 비전 1.7B 모델이 있다던데, 그 모델을 찾아 주세요.",
      fam("VARCO-VISION-2.0-1.7B-OCR", r"varco-vision-2\.0-1\.7b-ocr"),
      [r"NCSOFT/VARCO-VISION-2\.0-1\.7B-OCR"], tasks=VLM, persona="korean_service_planner", style="mixed"),
    q("lx37", "kanana-1.5-v-3b-instruct 비전 언어 모델을 받고 싶어요.",
      fam("kanana-1.5-v-3b-instruct", r"kanana-1\.5-v-3b-instruct"),
      [r"kakaocorp/kanana-1\.5-v-3b-instruct"], tasks=VLM),

    # ── 기타 한국어 LLM ──
    q("lx38", "llama-3.2-Korean-Bllossom-3B 원본과 GGUF 버전을 같이 찾아 주세요.",
      fam("Bllossom-3B", r"llama-3\.2-korean-bllossom-3b"),
      [r"Bllossom/llama-3\.2-Korean-Bllossom-3B"]),
    q("lx39", "KT 에서 나온 믿음 2.0 Mini 를 써 보라는 얘기를 들었어요. 이 모델 어디서 받을 수 있나요?",
      fam("Midm-2.0-Mini", r"midm-2\.0-mini"), [r"K-intelligence/Midm-2\.0-Mini-Instruct"],
      persona="local_user", style="mixed"),
    q("lx40", "EleutherAI polyglot-ko-5.8b 를 베이스로 실험하려고 합니다. 이 모델이 등록돼 있나요?",
      fam("polyglot-ko-5.8b", r"polyglot-ko-5\.8b"), [r"EleutherAI/polyglot-ko-5\.8b"]),
]
