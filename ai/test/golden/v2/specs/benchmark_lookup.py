"""benchmark_lookup 질의 10개.

이 유형이 묻는 것은 "이 벤치마크 점수를 README에 공개했는가"다.

★ 벤치마크 이름은 HARD_FILTER_KEYS에 없다
  그래서 후보를 좁히지 못한다. task와 수치 조건으로 후보를 잡고, 벤치마크
  이름은 ④단계(benchmark_metadata.results) 규칙으로 처리한다. 결과적으로
  eligible은 크고(34~247) ✅ 오답 더미가 대부분을 흡수하며 🚩는 작다.
  이게 이 유형의 정상적인 모양이다.

★ reliable_stages=(4,)
  다른 유형에서는 ④⑤가 믿을 수 없는 단계다(README 원문엔 어떤 단어든 있다).
  그런데 이 유형은 ④의 안전하게 귀속된 구조화 결과가 바로 답이므로 ④만
  신뢰한다. 출처/variant가 불명확한 결과는 ⑥으로 보내 ⚠️로 올린다.

★ weak_any는 인접 벤치마크 이름만 쓴다
  metric 이름(wer, nli)이나 짧은 토큰을 넣으면 ⚠️가 폭발한다. 'arc'는
  "search", "architecture"에 걸려서 ⚠️가 169개가 됐다.

코퍼스의 벤치마크 보유율은 439/3872 = 11.3%다. 이름이 확인되는 것은
mmlu 81, mteb 58, gpqa 47, librispeech 36, kmmlu 25, fleurs 18,
common voice 18, miracl 9, klue 3이다.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from scan import Rule  # noqa: E402

GEN_CORE_8B = {
    "tasks": ["text-generation"],
    "korean_required": True,
    "pools": ["core"],
    "max_parameters_billion": 8.0,
}
GEN_CORE_8B_FIDELITY = {
    "tasks": "생성 모델 / LLM",
    "korean_required": "한국어",
    "pools": "많이 쓰이는 → core (다운로드 500 이상)",
    "max_parameters_billion": "8B 이하",
}
ASR_CORE_1B = {
    "tasks": ["automatic-speech-recognition"],
    "korean_required": True,
    "pools": ["core"],
    "max_parameters_billion": 1.0,
}
ASR_CORE_1B_FIDELITY = {
    "tasks": "음성 인식",
    "korean_required": "한국어",
    "pools": "많이 쓰이는 → core",
    "max_parameters_billion": "1B 이하",
}


def benchmark_rule(names, adjacent, label, grade_2, grade_1, *, exclude=()):
    """벤치마크 이름 규칙. ④단계만 권위 있는 근거로 본다."""
    return Rule(
        must_any=names,
        grade_2_any=names,
        weak_any=adjacent,
        reliable_stages=(4,),
        must_label=label,
        grade_2_label=grade_2,
        grade_1_label=grade_1,
        benchmark_terms=names,
        benchmark_exclude=exclude,
    )


SPECS = [
    {
        "query_id": "bl01",
        "query": "KMMLU 점수를 공개한 한국어 LLM을 찾고 있어. 많이 쓰이는 것 중에 파라미터 8B 이하인 모델로.",
        "conditions": GEN_CORE_8B,
        "fidelity": GEN_CORE_8B_FIDELITY,
        "rule": benchmark_rule(
            ["kmmlu", "k-mmlu", "k mmlu", "korean mmlu"], [],
            "benchmark_metadata.results에 KMMLU 결과가 있다",
            "KMMLU 점수가 수치로 기록돼 있다",
            "KMMLU를 언급하나 점수가 수치로 확인되지 않는다",
        ),
    },
    {
        "query_id": "bl02",
        "query": "MTEB 결과가 공개된 한국어 임베딩 모델을 추천해줘. 많이 쓰이는 것으로.",
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
        "rule": benchmark_rule(
            ["mteb"], ["beir"],
            "benchmark_metadata.results에 MTEB 결과가 있다",
            "MTEB 점수가 수치로 기록돼 있다",
            "MTEB를 언급하나 점수가 확인되지 않거나, BEIR 등 인접 벤치마크만 있다",
        ),
    },
    {
        "query_id": "bl03",
        "query": "파라미터 500M 이하인 한국어 문장 임베딩 모델 중에 MTEB 점수가 있는 걸 찾아줘. 많이 쓰이는 것으로.",
        "conditions": {
            "tasks": ["sentence-similarity"],
            "korean_required": True,
            "pools": ["core"],
            "max_parameters_billion": 0.5,
        },
        "fidelity": {
            "tasks": "문장 임베딩",
            "korean_required": "한국어",
            "pools": "많이 쓰이는 → core",
            "max_parameters_billion": "500M 이하",
        },
        "rule": benchmark_rule(
            ["mteb"], ["beir"],
            "benchmark_metadata.results에 MTEB 결과가 있다",
            "MTEB 점수가 수치로 기록돼 있다",
            "MTEB를 언급하나 점수가 확인되지 않거나 인접 벤치마크만 있다",
        ),
    },
    {
        "query_id": "bl04",
        "query": "LibriSpeech 결과가 README에 있는 한국어 음성 인식 모델을 찾고 있어. 1B 이하인 것 중 많이 쓰이는 것으로.",
        "conditions": ASR_CORE_1B,
        "fidelity": ASR_CORE_1B_FIDELITY,
        "rule": benchmark_rule(
            ["librispeech"], ["libri-light", "tedlium"],
            "benchmark_metadata.results에 LibriSpeech 결과가 있다",
            "LibriSpeech WER 등이 수치로 기록돼 있다",
            "LibriSpeech를 언급하나 수치가 없거나, 인접 음성 데이터셋만 있다",
        ),
    },
    {
        "query_id": "bl05",
        "query": "FLEURS 점수가 공개된 한국어 음성 인식 모델 있어? 1B 이하인 것 중 많이 쓰이는 것으로.",
        "conditions": ASR_CORE_1B,
        "fidelity": ASR_CORE_1B_FIDELITY,
        "rule": benchmark_rule(
            ["fleurs"], ["voxpopuli", "mls"],
            "benchmark_metadata.results에 FLEURS 결과가 있다",
            "FLEURS 점수가 수치로 기록돼 있다",
            "FLEURS를 언급하나 수치가 없거나, 인접 다국어 음성 벤치마크만 있다",
        ),
    },
    {
        "query_id": "bl06",
        "query": "Common Voice 평가 결과가 있는 한국어 음성 인식 모델을 추천해줘. 1B 이하인 것 중 많이 쓰이는 것으로.",
        "conditions": ASR_CORE_1B,
        "fidelity": ASR_CORE_1B_FIDELITY,
        "rule": benchmark_rule(
            ["common voice", "common_voice", "commonvoice"], ["voxpopuli"],
            "benchmark_metadata.results에 Common Voice 결과가 있다",
            "Common Voice 점수가 수치로 기록돼 있다",
            "Common Voice를 언급하나 수치가 없거나 인접 벤치마크만 있다",
        ),
    },
    {
        "query_id": "bl07",
        "query": "MMLU 점수가 공개된 한국어 LLM 중에 4B 이하인 걸 찾아줘. 많이 쓰이는 것으로.",
        "conditions": {
            "tasks": ["text-generation"],
            "korean_required": True,
            "pools": ["core"],
            "max_parameters_billion": 4.0,
        },
        "fidelity": {
            "tasks": "LLM → text-generation",
            "korean_required": "한국어",
            "pools": "많이 쓰이는 → core",
            "max_parameters_billion": "4B 이하",
        },
        "rule": benchmark_rule(
            ["mmlu"], ["mmlu-pro", "mmlu pro", "multilingual mmlu", "mmmlu", "kmmlu", "k-mmlu", "hellaswag"],
            "benchmark_metadata.results에 원본 MMLU 결과가 있다",
            "현재 모델에 귀속되는 원본 MMLU 점수가 수치로 기록돼 있다",
            "MMLU-Pro·KMMLU·MMMLU 등 변형만 있는 모델은 정답으로 넣지 않고, 원본 MMLU라도 변환본·재업로드 여부는 사람 검수 후 1점으로 낮춘다",
            exclude=("mmlu-pro", "mmlu pro", "multilingual mmlu", "mmmlu", "kmmlu", "k-mmlu"),
        ),
    },
    {
        "query_id": "bl08",
        "query": "도구 호출 성능을 비교하려고 해. BFCL v3 점수를 공개한 한국어 LLM이 있을까? 4B 이하인 것 중 많이 쓰이는 것으로.",
        "conditions": {
            "tasks": ["text-generation"],
            "korean_required": True,
            "pools": ["core"],
            "max_parameters_billion": 4.0,
        },
        "fidelity": {
            "tasks": "LLM → text-generation",
            "korean_required": "한국어",
            "pools": "많이 쓰이는 → core",
            "max_parameters_billion": "4B 이하",
        },
        "rule": benchmark_rule(
            ["bfclv3", "bfcl v3", "bfcl-v3"], ["tool calling", "function calling"],
            "benchmark_metadata.results에 BFCL v3 결과가 있다",
            "현재 모델에 귀속되는 BFCL v3 점수가 수치로 기록돼 있다",
            "도구 호출을 언급하나 BFCL v3 점수가 없거나 출처가 불명확하다",
        ),
    },
    {
        "query_id": "bl09",
        "query": "KLUE 평가 결과가 README에 있는 한국어 텍스트 분류 모델을 찾고 있어.",
        "conditions": {
            "tasks": ["text-classification"],
            "korean_required": True,
        },
        "fidelity": {
            "tasks": "텍스트 분류",
            "korean_required": "한국어",
        },
        "rule": benchmark_rule(
            ["klue"], ["korsts", "kornli"],
            "benchmark_metadata.results에 KLUE 결과가 있다",
            "KLUE 점수가 수치로 기록돼 있다",
            "KLUE를 언급하나 수치가 없거나, KorSTS·KorNLI 등 인접 한국어 벤치마크만 있다",
        ),
    },
    {
        "query_id": "bl10",
        "query": "한국어 STS 벤치마크 점수가 공개된 문장 유사도 모델을 추천해줘. 많이 쓰이는 것으로.",
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
        "rule": benchmark_rule(
            ["korsts", "klue-sts", "klue sts", "klue_sts"], ["stsb", "sts-b", "stsbenchmark", "sts"],
            "benchmark_metadata.results에 한국어 STS 계열 결과가 있다",
            "KorSTS 또는 KLUE-STS 점수가 수치로 기록돼 있다",
            "일반 STSBenchmark/STSB만 있는 모델은 한국어 STS 정답으로 넣지 않고, 한국어 STS 언급이지만 수치·출처가 불명확한 경우만 사람 검수 후 1점으로 둔다",
        ),
    },
]
