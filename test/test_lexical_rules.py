"""lexical_rules 판정 규칙 self-check. 실제 코퍼스 값 모양을 그대로 쓴다."""

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

spec = importlib.util.spec_from_file_location(
    "lexical_rules", ROOT / "retrieval_lab" / "lexical_rules.py"
)
rules = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rules)


def model(model_id, **meta):
    return {"model_id": model_id, "filter_metadata": meta}


def test_direction_pair_models():
    forward = model("Helsinki-NLP/opus-mt-tc-big-en-ko", translation_pairs=["en-ko"])
    reverse = model("shun89/opus-mt-ko-zh", translation_pairs=["ko-zh"])

    assert rules.direction_match(forward, "en", ["ko"])
    assert not rules.direction_match(forward, "ko", ["en"])

    # zh->ko 질의에 ko->zh 모델은 위반이다.
    assert rules.direction_violation(reverse, "zh", ["ko"])
    assert not rules.direction_violation(forward, "en", ["ko"])


def test_direction_from_name_only():
    """translation_pairs는 코퍼스의 0.6%만 채워져 있어 이름 경로가 필요하다."""
    named = model("sappho192/aihub-ja-ko-translator")
    assert rules.explicit_pairs(named) == {"ja-ko"}
    assert rules.direction_match(named, "ja", ["ko"])


def test_direction_multilingual():
    """NLLB처럼 쌍 표기가 없고 languages로만 방향을 알 수 있는 모델."""
    nllb = model("facebook/nllb-200-distilled-600M",
                 translation_pairs=[], languages=["zh", "ko", "en"],
                 primary_task="translation")
    assert rules.direction_match(nllb, "zh", ["ko"])
    # 양방향을 다 하므로 위반으로 보지 않는다.
    assert not rules.direction_violation(nllb, "ko", ["zh"])

    # 같은 언어 목록이라도 번역 task가 아니면 방향을 주장하지 않는다.
    embedder = model("intfloat/multilingual-e5-small",
                     languages=["zh", "ko"], primary_task="sentence-similarity")
    assert not rules.direction_match(embedder, "zh", ["ko"])


def test_format_signals():
    # 플래그로 잡히는 경우
    assert rules.format_match(model("x/y", artifacts={"gguf": True}), "gguf")
    # artifacts에 칸이 없는 형식은 이름으로만 찾는다.
    assert rules.format_match(model("Systran/faster-whisper-small"), "ct2")
    assert rules.format_match(model("OpenVINO/whisper-base-int8-ov"), "openvino")
    assert not rules.format_match(model("openai/whisper-small"), "ct2")
    # variant_types 경로
    assert rules.format_match(model("a/b", variant_types=["awq"]), "awq")


def test_family_name_and_canonical():
    assert rules.family_match(model("monologg/koelectra-base-v3"), r"koelectra")
    # 이름엔 없고 canonical에만 있는 경우
    derived = model("someone/my-finetune", canonical_model_id="klue/roberta-base")
    assert rules.family_match(derived, r"klue[-_./]?roberta")
    assert not rules.family_match(model("skt/kogpt2-base-v2"), r"koelectra")


def test_satisfies_requires_task():
    """형식이 맞아도 용도가 다르면 정답이 아니다."""
    req = rules.REQUIREMENTS["sg_h049"]  # GGUF 임베딩
    embedding = model("x/emb-GGUF", artifacts={"gguf": True},
                      primary_task="sentence-similarity")
    chat = model("x/chat-GGUF", artifacts={"gguf": True}, primary_task="text-generation")
    assert rules.satisfies(embedding, req)
    assert not rules.satisfies(chat, req)


def test_score_shape():
    corpus = {
        "a": model("Helsinki-NLP/opus-mt-tc-big-en-ko", translation_pairs=["en-ko"],
                   primary_task="translation"),
        "b": model("shun89/opus-mt-ko-en", translation_pairs=["ko-en"],
                   primary_task="translation"),
    }
    req = {"kind": "direction", "source": "en", "target": "ko"}
    out = rules.score(["a", "b"], corpus, req, ks=(2,))
    assert out["lex_match@2"] == 0.5
    assert out["lex_violation@2"] == 0.5


def test_every_query_has_a_requirement():
    """질의 22개가 모두 규칙으로 판정 가능해야 한다."""
    assert len(rules.REQUIREMENTS) == 22
    kinds = [req["kind"] for req in rules.REQUIREMENTS.values()]
    assert kinds.count("direction") == 10
    assert kinds.count("format") == 7
    assert kinds.count("family") == 5


if __name__ == "__main__":
    for name, func in sorted(globals().items()):
        if name.startswith("test_"):
            func()
            print(f"ok  {name}")
