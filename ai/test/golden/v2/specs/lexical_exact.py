"""lexical_exact 질의 10개.

정확한 문자열이 중심이다. 모델명, 번역 방향(ko→en), 형식명(GGUF, ONNX, MLX),
양자화 방식(fp8, int8) 같은 리터럴.

★ artifacts는 불린 맵이다 — 키 이름이 아니라 값을 봐야 한다
  `{"gguf": false, "onnx": false, "safetensors": true}` 꼴이라, JSON을 그냥
  덤프하면 값이 false인 키 이름까지 본문에 들어간다. 처음에 그래서 "GGUF 형식"
  질의가 요약 후보 14개에 전부 걸렸다. `scan._flags()`가 참인 키만 남기도록
  고쳐서 3/14로 떨어졌다.

★ 번역 방향은 model_id와 claim을 함께 본다
  ko→en과 en→ko는 다른 모델이다. 양방향 모델은 둘 다 2점, 단방향은 반대 방향
  질의에 0점이다. `reject_any`로 반대 방향을 1점으로 내린다.

판정 기준
    2점 — 질의한 문자열이 model_id 또는 filter_metadata에서 확인된다
    1점 — 형식·방향이 claim에만 있거나 불명확하거나, 변환본이라 원본과 구별된다
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from scan import Rule  # noqa: E402

GEN_CORE_4B = {
    "tasks": ["text-generation"],
    "korean_required": True,
    "pools": ["core"],
    "max_parameters_billion": 4.0,
    "require_known_parameters": True,
}
GEN_CORE_4B_FIDELITY = {
    "tasks": "LLM → text-generation",
    "korean_required": "한국어",
    "pools": "많이 쓰이는 → core (다운로드 500 이상)",
    "max_parameters_billion": "4B 이하",
    "require_known_parameters": "로 공개된",
}
GEN_CORE_2B = {**GEN_CORE_4B, "max_parameters_billion": 2.0}
GEN_CORE_2B_FIDELITY = {**GEN_CORE_4B_FIDELITY, "max_parameters_billion": "2B 이하"}
TRANS_SMALL = {
    "tasks": ["translation"],
    "korean_required": True,
    "max_parameters_billion": 0.5,
    "require_known_parameters": True,
}
TRANS_SMALL_FIDELITY = {
    "tasks": "번역",
    "korean_required": "한국어",
    "max_parameters_billion": "500M 이하",
    "require_known_parameters": "로 공개된",
}

SPECS = [
    {
        "query_id": "le01",
        "query": "GGUF 형식으로 받을 수 있는 한국어 요약 모델을 찾고 있어.",
        "conditions": {"tasks": ["summarization"], "korean_required": True},
        "fidelity": {"tasks": "요약", "korean_required": "한국어"},
        "rule": Rule(
            must_any=["gguf"],
            grade_2_any=["gguf"],
            weak_any=["llama.cpp", "ollama", "q4_k_m", "q8_0"],
            must_label="GGUF 아티팩트를 실제로 가지고 있거나 model_id에 GGUF가 있다",
            grade_2_label="GGUF 파일이 artifacts에서 확인된다",
            grade_1_label="llama.cpp 호환만 언급하고 GGUF 파일 자체는 확인되지 않는다",
        ),
    },
    {
        "query_id": "le02",
        "query": "GGUF로 제공되는 한국어 이미지-텍스트 모델 있어? 파라미터 1B 이하로 공개된 것으로.",
        "conditions": {
            "tasks": ["image-text-to-text"],
            "korean_required": True,
            "max_parameters_billion": 1.0,
            "require_known_parameters": True,
        },
        "fidelity": {
            "tasks": "이미지-텍스트",
            "korean_required": "한국어",
            "max_parameters_billion": "파라미터 1B 이하",
            "require_known_parameters": "로 공개된",
        },
        "rule": Rule(
            must_any=["gguf"],
            grade_2_any=["gguf"],
            weak_any=["llama.cpp", "mmproj"],
            must_label="GGUF 아티팩트를 가지고 있거나 model_id에 GGUF가 있다",
            grade_2_label="GGUF 파일이 artifacts에서 확인된다",
            grade_1_label="llama.cpp 호환만 언급된다",
        ),
    },
    {
        "query_id": "le03",
        "query": "ONNX로 변환된 한국어 임베딩 모델을 추천해줘. 많이 쓰이는 것으로.",
        "conditions": {
            "tasks": ["feature-extraction"],
            "korean_required": True,
            "pools": ["core"],
        },
        "fidelity": {
            "tasks": "임베딩 → feature-extraction",
            "korean_required": "한국어",
            "pools": "많이 쓰이는 → core",
        },
        "rule": Rule(
            must_any=["onnx"],
            grade_2_any=["onnx"],
            weak_any=["optimum", "onnxruntime"],
            must_label="ONNX 아티팩트를 실제로 가지고 있다",
            grade_2_label="ONNX 파일이 artifacts에서 확인된다",
            grade_1_label="ONNX 변환 가능성만 언급된다",
        ),
    },
    {
        "query_id": "le04",
        "query": "ONNX 파일이 있는 한국어 문장 유사도 모델을 찾아줘. 많이 쓰이는 것으로.",
        "conditions": {
            "tasks": ["sentence-similarity"],
            "korean_required": True,
            "pools": ["core"],
        },
        "fidelity": {
            "tasks": "문장 유사도",
            "korean_required": "한국어",
            "pools": "많이 쓰이는 → core",
        },
        "rule": Rule(
            must_any=["onnx"],
            grade_2_any=["onnx"],
            weak_any=["optimum", "onnxruntime"],
            must_label="ONNX 아티팩트를 실제로 가지고 있다",
            grade_2_label="ONNX 파일이 artifacts에서 확인된다",
            grade_1_label="ONNX 변환 가능성만 언급된다",
        ),
    },
    {
        "query_id": "le05",
        "query": "한국어를 영어로 번역하는 모델을 찾고 있어. 파라미터 500M 이하로 공개된 것으로.",
        "conditions": TRANS_SMALL,
        "fidelity": TRANS_SMALL_FIDELITY,
        "rule": Rule(
            must_any=["ko-en", "ko2en", "koen", "ko_en", "kor2eng", "한영"],
            grade_2_any=["ko-en", "ko2en", "한영"],
            weak_any=["m2m", "nllb", "mbart", "opus-mt-mul"],
            reject_any=["en-ko", "en2ko", "영한"],
            must_label="ko→en 방향이 model_id 또는 claim에서 확인된다",
            grade_2_label="ko→en 방향이 명시돼 있다",
            grade_1_label="다국어 모델로 ko·en을 모두 지원하나 방향 명시가 없다",
        ),
    },
    {
        "query_id": "le06",
        "query": "영어를 한국어로 번역하는 모델이 필요해. 파라미터 500M 이하로 공개된 것으로.",
        "conditions": TRANS_SMALL,
        "fidelity": TRANS_SMALL_FIDELITY,
        "rule": Rule(
            must_any=["en-ko", "en2ko", "enko", "en_ko", "eng2kor", "영한"],
            grade_2_any=["en-ko", "en2ko", "영한"],
            weak_any=["m2m", "nllb", "mbart", "opus-mt-mul"],
            reject_any=["ko-en", "ko2en", "한영"],
            must_label="en→ko 방향이 model_id 또는 claim에서 확인된다",
            grade_2_label="en→ko 방향이 명시돼 있다",
            grade_1_label="다국어 모델로 ko·en을 모두 지원하나 방향 명시가 없다",
        ),
    },
    {
        "query_id": "le07",
        "query": "opus-mt 기반 한국어 번역 모델을 찾아줘. 많이 쓰이는 것으로.",
        "conditions": {
            "tasks": ["translation"],
            "korean_required": True,
            "pools": ["core"],
        },
        "fidelity": {
            "tasks": "번역",
            "korean_required": "한국어",
            "pools": "많이 쓰이는 → core",
        },
        "rule": Rule(
            must_any=["opus-mt", "opus_mt", "opusmt"],
            grade_2_any=["opus-mt"],
            weak_any=["marian", "helsinki"],
            must_label="model_id가 opus-mt 계열이다",
            grade_2_label="Helsinki-NLP/opus-mt 본체 또는 그 파인튜닝이다",
            grade_1_label="Marian 구조이나 opus-mt 계열임이 model_id에 없다",
        ),
    },
    {
        "query_id": "le08",
        "query": "MLX 형식으로 제공되는 한국어 LLM을 찾고 있어. 많이 쓰이는 것 중에 2B 이하로 공개된 모델로.",
        "conditions": GEN_CORE_2B,
        "fidelity": GEN_CORE_2B_FIDELITY,
        "rule": Rule(
            must_any=["mlx"],
            grade_2_any=["mlx"],
            weak_any=["apple silicon", "metal"],
            must_label="model_id 또는 filter_metadata에 MLX가 있다",
            grade_2_label="MLX 변환본임이 model_id에서 확인된다",
            grade_1_label="Apple Silicon 지원만 언급되고 MLX 변환본은 아니다",
        ),
    },
    {
        "query_id": "le09",
        "query": "fp8로 양자화된 한국어 LLM 있어? 많이 쓰이는 것 중에 4B 이하로 공개된 모델로.",
        "conditions": GEN_CORE_4B,
        "fidelity": GEN_CORE_4B_FIDELITY,
        "rule": Rule(
            must_any=["fp8"],
            grade_2_any=["fp8"],
            weak_any=["w8a8"],
            must_label="quantization.method가 fp8이거나 model_id에 fp8이 있다",
            grade_2_label="fp8 양자화가 quantization에서 확인된다",
            grade_1_label="8비트 가중치 양자화이나 fp8 방식은 아니다",
        ),
    },
    {
        "query_id": "le10",
        "query": "safetensors로 받을 수 있는 한국어 요약 모델을 추천해줘.",
        "conditions": {"tasks": ["summarization"], "korean_required": True},
        "fidelity": {"tasks": "요약", "korean_required": "한국어"},
        "rule": Rule(
            must_any=["safetensors"],
            grade_2_any=["safetensors"],
            weak_any=["pytorch_bin", "pytorch_model"],
            must_label="safetensors 아티팩트를 실제로 가지고 있다",
            grade_2_label="safetensors 파일이 artifacts에서 확인된다",
            grade_1_label="pytorch_bin만 있고 safetensors는 없다",
        ),
    },
]
