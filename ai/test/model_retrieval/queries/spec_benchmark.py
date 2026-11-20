"""benchmark_lookup 질문 40개. 전부 현재 코퍼스에 실제로 점수가 있는 벤치마크다.

구 골든셋이 묻던 KorQuAD·NSMC·AutoRAG·CLIcK·COMET·ROUGE 는 코퍼스에 0건이라 뺐다.
한국어 벤치마크(KMMLU 4모델, KoBEST 3, HAE-RAE 3)만으로는 40개가 안 되므로
영어·다국어 벤치마크도 넣었다. 실제 사용자도 MMLU·GSM8K 는 이름으로 묻는다.

1점(같은 벤치마크 다른 표기)에서 뺀 것과 그 근거 — 점수 분포로 확인했다.

  GPQA (0-shot) 6.49~21.92     vs GPQA Diamond 82.50~94.44
      Open LLM Leaderboard v2 의 정규화 점수다. 같은 수치가 아니다.
  GPQA (main) 31.97            Diamond 은 198문항 하위셋이라 다른 평가셋이다.
  Winogrande XL (xl) 50.51~63.38 vs Winogrande (5-shot) 72.93~82.95
      역시 정규화 점수다.
  MMLU-ProX-Lite               MMLU-Pro 의 다국어 확장판이라 다른 벤치마크다.
  ARC (맨 이름) 98.39           Challenge 로 보기 어려운 값이다. Easy 일 수 있다.
  FLORES-200 (AVG, 71 pairs) 86.89  BLEU 로 볼 수 없는 값이다.

남긴 것은 같은 벤치마크의 설정·표기 차이다(GSM8K _(EM)_, kmmlu (chat CoT),
HellaSwag (10-Shot) 등). 점수대가 조금 벗어나도 표본이 1~4개라 분포로는
가를 수 없고, 프롬프트·shot 설정 차이로 설명된다.

채점 규칙은 dataset·metric 정규식이다. 저장된 표기를 그대로 맞춘다
(표기가 11가지로 갈린 GSM8K 처럼, 다른 평가 설정은 다른 dataset 으로 본다).
"""

GEN = ["text-generation"]
ASR = ["automatic-speech-recognition"]
VLM = ["image-text-to-text"]
TR = ["translation"]
EMB = ["sentence-similarity", "feature-extraction"]


def q(qid, text, tasks, dataset_regex, metric_regex, note=None, also=None,
      persona="ml_engineer", style="technical"):
    """also: 같은 벤치마크의 다른 표기(1점). 다른 벤치마크는 절대 넣지 않는다.

    저장된 표기가 갈려 있다(GSM8K / GSM8K _(EM)_ / GSM8k (5-shot) …). 설정이
    다르면 점수를 나란히 못 놓으므로 2점은 질의가 말한 표기만 받고, 같은
    벤치마크의 다른 표기는 1점으로 둔다. GreekMMLU 를 KMMLU 로, MMLU-PRO 를
    MMLU 로 세지 않도록 질문마다 손으로 적었다.
    """
    bench = {"dataset_regex": dataset_regex, "metric_regex": metric_regex}
    if note:
        bench["note"] = note
    if also:
        bench["also_dataset_regex"] = also
    return {
        "qid": qid, "text": text, "query_type": "benchmark_lookup", "origin": "corpus_grounded",
        "persona": persona, "expression_style": style,
        "conditions": {"tasks": tasks, "korean_required": True} if tasks else {"korean_required": True},
        "conditions_fidelity": {"tasks": "질의가 지목한 모델 종류"} if tasks else {},
        "relevance_rule": {
            "grade_2": "질의가 말한 표기 그대로 점수가 저장된 모델",
            "grade_1": "같은 벤치마크지만 다른 설정·표기로 적힌 모델, 또는 변환·재업로드본",
            "benchmark": bench,
        },
    }


QUERIES = [
    # ── 음성 인식 ──────────────────────────────────────────────
    q("bm01", "음성 인식 모델을 Common Voice 11.0 WER 로 비교하려고 합니다. 그 점수가 있는 모델을 찾아 주세요.",
      ASR, r"^common voice 11\.0$", r"^wer$"),
    q("bm02", "LibriSpeech clean WER 가 README 에 적힌 음성 인식 모델만 보고 싶어요.",
      ASR, r"^librispeech \(clean\)$", r"^wer$"),
    q("bm03", "LibriSpeech other WER 로 잡음 환경 성능을 비교하고 싶습니다.",
      ASR, r"^librispeech \(other\)$", r"^wer$"),
    q("bm04", "Common Voice 13.0 기준 WER 이 공개된 음성 인식 모델이 있나요?",
      ASR, r"^common voice 13\.0$", r"^wer$"),
    q("bm05", "Zeroth Korean 에서 CER 이 측정된 한국어 음성 인식 모델을 찾습니다.",
      ASR, r"^zeroth korean$", r"^cer$"),
    q("bm06", "Zeroth Korean WER 이 기록된 음성 인식 모델을 알려 주세요.",
      ASR, r"^zeroth korean$", r"^wer$"),
    q("bm07", "VoxPopuli 점수가 있는 음성 인식 모델이 필요합니다.",
      ASR, r"^voxpopuli$", r"^score$"),

    # ── 한국어 벤치마크 ────────────────────────────────────────
    q("bm08", "KMMLU 점수가 공개된 한국어 모델을 같은 기준으로 비교하고 싶습니다.",
      None, r"^kmmlu$", r"^score$", "kmmlu (chat CoT)·kmmlu-direct·KMMLU-Pro 는 다른 평가 설정이라 제외",
      also=r"^(kmmlu|kmmlu[ -]direct.*|kmmlu \(chat cot\)|\*\*kmmlu\*\* \(ko, knowledge\))$"),
    q("bm09", "KMMLU 를 chat CoT 설정으로 측정한 결과가 있는 모델을 찾습니다.",
      GEN, r"^kmmlu \(chat cot\)$", r"^exact-match$"),
    q("bm10", "KoBEST 결과가 README 에 있는 한국어 LLM 을 찾고 있어요.",
      GEN, r"kobest", r"^score$",
      also=r"^(kobest|\*\*kobest\*\* \(ko, conversational\))$"),
    q("bm11", "HAE-RAE 로 한국 문화·상식 이해를 검증한 한국어 LLM 이 필요합니다.",
      GEN, r"hae-rae", r"^score$",
      also=r"^(hae-rae \(ko, knowledge\)|hae-rae bench v1\.1|haerae \(5-shots\))$"),
    q("bm12", "KLUE NLI 점수가 공개된 한국어 모델이 있나요?",
      None, r"^klue-nli$", r"^score$"),
    q("bm13", "KorSTS 점수가 적힌 한국어 문장 임베딩 모델을 찾습니다.",
      EMB, r"^korsts$", r"^score$"),
    # LogicKor·KoMT-Bench 점수를 가진 모델은 코퍼스에서 전부 비전 언어 모델이다.
    # task 를 text-generation 으로 좁히면 0건이 되므로 질문을 사실에 맞춘다.
    q("bm14", "LogicKor 점수가 공개된 한국어 모델을 찾습니다. 추론·글쓰기 점수를 보고 싶어요.",
      None, r"^logickor$", r"^score$"),
    q("bm15", "KoMT-Bench 점수가 기록된 한국어 모델이 있나요? 멀티턴 대화 품질을 숫자로 보고 싶습니다.",
      None, r"^komt-bench$", r"^score$"),
    q("bm16", "K-DTCBench 로 한국어 문서·표·차트 이해를 검증한 비전 언어 모델을 찾습니다.",
      VLM, r"^k-dtcbench$", r"^score$"),

    # ── 일반 추론·지식 ─────────────────────────────────────────
    q("bm17", "GPQA Diamond 정확도가 README 에 적힌 모델을 찾아 주세요.",
      None, r"^gpqa diamond$", r"^accuracy$", "metric 이 score 로만 적힌 GPQA Diamond 는 다른 metric 으로 본다",
      also=r"^(gpqa[ -]diamond|gpqa[ -]diamond _\(acc\)_|\*\*gpqa diamond\*\*|gpqa diamond ★)$"),
    q("bm18", "MMLU 점수가 공개된 모델만 모아서 비교하고 싶습니다.",
      None, r"^mmlu$", r"^score$", "MMLU (5-Shot)·MMLU _(Acc)_·MMLU-Pro 는 다른 표기라 제외",
      also=r"^(mmlu|mmlu _\(acc\)_|mmlu \(5-shot\)|mmlu \(5-shot, acc\)|mmlu \(acc, 5-shot\)|mmlu \(letter\)|mmlu \(chat cot\)|mmlu \(5-shots\)|\*\*mmlu\*\* \(en, knowledge\)|mmlu-redux|mmlu-redux _\(acc\)_)$"),
    q("bm19", "MMLU-PRO 5-shot accuracy 가 기록된 모델을 비교하려고 합니다.",
      GEN, r"^mmlu-pro \(5-shot\)$", r"^accuracy$",
      also=r"^(mmlu-pro|mmlu pro|mmlu-pro _\(acc\)_|mmlu-pro \(acc, 5-shot\)|mmlu-pro \(5-shot, cot em\)|mmlu-pro \(cot\) ⚠|mmlu-pro ★)$"),
    q("bm20", "GSM8K 점수로 수학 추론 성능을 비교할 수 있는 모델을 찾습니다.",
      GEN, r"^gsm8k$", r"^score$", "GSM8K (EM)·5-shot accuracy 등 설정이 적힌 결과는 다른 표기로 본다",
      also=r"^(gsm8k|gsm8k _\(em\)_|gsm8k \(5-shot\)|gsm8k \(5-shots\)|gsm8k \(8-shot, acc\)|gsm8k \(cot\)|gsm8k \(math, strict\)|gsm8k \(strict-match, 5-shot\)|\*\*gsm8k / basic math reasoning\*\*)$"),
    q("bm21", "GSM8K 를 5-shot accuracy 로 측정한 결과가 있는 모델이 있나요?",
      GEN, r"^gsm8k \(5-shot\)$", r"^accuracy$",
      also=r"^(gsm8k|gsm8k _\(em\)_|gsm8k \(5-shots\)|gsm8k \(8-shot, acc\)|gsm8k \(cot\)|gsm8k \(math, strict\)|gsm8k \(strict-match, 5-shot\))$"),
    q("bm22", "BBH 3-shot 점수가 공개된 모델을 찾고 있습니다.",
      GEN, r"^bbh \(3-shot\)$", r"^acc-norm$",
      also=r"^(bbh|bbh \(3-shot\))$"),
    q("bm23", "MATH Lvl 5 점수가 적힌 모델로 고난도 수학 성능을 보고 싶어요.",
      GEN, r"^math lvl 5 \(4-shot\)$", r"^exact-match$"),
    q("bm24", "HellaSwag 점수가 공개된 모델을 비교하려고 합니다.",
      None, r"^hellaswag$", r"^score$", "HellaSwag (10-Shot) 은 다른 설정이라 제외",
      also=r"^(hellaswag|hellaswag _\(acc\)_|hellaswag \(10-shot\)|hellaswag \(10-shot, acc_norm\)|hellaswag \(acc-norm, 10-shot\))$"),
    q("bm25", "TruthfulQA 점수가 README 에 있는 모델을 찾습니다.",
      GEN, r"^truthfulqa$", r"^score$",
      also=r"^(truthfulqa|truthfulqa \(0-shot\)|truthfulqa mc2|truthfulqa \(mc2, 0-shot\))$"),
    q("bm26", "AI2 Reasoning Challenge 25-shot 점수가 있는 모델이 필요해요.",
      GEN, r"^ai2 reasoning challenge \(25-shot\)$", r"^acc-norm$",
      also=r"^(ai2 reasoning challenge \(25-shot\)|ai2 reasoning challenge|arc-challenge|arc-c)$"),
    q("bm27", "MuSR 0-shot 점수가 기록된 모델을 보고 싶습니다.",
      GEN, r"^musr \(0-shot\)$", r"^acc-norm$"),
    q("bm28", "Winogrande 5-shot accuracy 가 공개된 모델을 찾습니다.",
      GEN, r"^winogrande \(5-shot\)$", r"^accuracy$",
      also=r"^(winogrande|winogrande \(5-shot\)|winogrande _\(acc\)_|winogrande \(acc, 5-shot\)|winogrande \(5-shot, acc\))$"),
    q("bm29", "MMMLU 점수로 다국어 지식 성능을 비교하고 싶어요.",
      None, r"^mmmlu$", r"^score$",
      also=r"^(mmmlu|mmmlu _\(acc\)_)$"),

    # ── 지시 따르기 ────────────────────────────────────────────
    q("bm30", "IFEval 0-shot strict accuracy 가 기록된 모델을 같은 기준으로 비교해 주세요.",
      GEN, r"^ifeval \(0-shot\)$", r"strict-acc",
      also=r"^(ifeval|if_eval|ifeval \(0-shot\)|ifeval \(en\)|ifeval \(inst-and-prompt level strict acc, 0-shot\))$"),
    q("bm31", "Multi-IF 점수가 공개된 모델이 있나요? 다중 지시 수행 능력을 보고 싶습니다.",
      GEN, r"^multi-if$", r"^score$"),

    # ── 다국어 이해 ────────────────────────────────────────────
    q("bm32", "XNLI 영어 정확도가 기록된 모델을 찾고 있습니다.",
      GEN, r"^xnli \(en\)$", r"^accuracy$"),
    q("bm33", "XCOPA 인도네시아어 정확도가 있는 모델이 필요해요.",
      GEN, r"^xcopa \(id\)$", r"^accuracy$"),
    q("bm34", "XStoryCloze 중국어 점수가 공개된 모델을 찾습니다.",
      GEN, r"^xstorycloze \(zh\)$", r"^accuracy$"),

    # ── 번역 ───────────────────────────────────────────────────
    q("bm35", "FLORES-200 En→Xx BLEU 점수가 있는 번역 모델을 비교하고 싶습니다.",
      None, r"^flores-200 en→xx _\(bleu\)_$", r"^score$",
      also=r"^(flores-200 en→xx _\(bleu\)_)$"),
    q("bm36", "flores101-devtest BLEU 가 README 에 적힌 번역 모델을 찾습니다.",
      TR, r"^flores101-devtest$", r"^bleu$", "FLORES-200 은 다른 dataset 으로 본다"),
    q("bm37", "WMT24++ Xx→En BLEU 점수가 공개된 번역 모델이 있나요?",
      None, r"^wmt24\+\+ xx→en _\(bleu\)_$", r"^score$",
      also=r"^(wmt24\+\+ xx→en _\(bleu\)_|wmt24\+\+ en→xx _\(bleu\)_)$"),

    # ── 비전·문서 ──────────────────────────────────────────────
    q("bm38", "AI2D 점수가 있는 비전 언어 모델로 도표 이해 성능을 보고 싶어요.",
      VLM, r"^ai2d$", r"^score$"),
    q("bm39", "ICDAR2015 점수가 기록된 문서 인식 모델을 찾습니다.",
      VLM, r"^icdar2015$", r"^score$"),
    q("bm40", "CORD 영수증 인식 점수가 공개된 비전 언어 모델이 필요합니다.",
      VLM, r"^cord$", r"^score$"),
]
