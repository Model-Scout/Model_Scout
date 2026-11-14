---
language: ko
license: cc-by-sa-4.0
library_name: transformers
pipeline_tag: text-generation
base_model: gogamza/kobart-base-v2
tags:
- grammatical-error-correction
- spelling-correction
- korean
---

# dadeum-gec-small

A small Korean spelling, spacing and grammar corrector that fixes only what is
wrong and leaves the rest of the sentence alone. It comes from
[dadeum](https://github.com/zmflm0110/dadeum), a grammar checker that runs on
the user's own Mac, and is trained only on openly licensed text: no training
pair was annotated by an AI provider.

틀린 곳만 고치고 나머지는 그대로 두는 작은 한국어 맞춤법 · 띄어쓰기 · 문법 교정 모델입니다. 기기 안에서 도는 맞춤법
검사기 [다듬](https://github.com/zmflm0110/dadeum)에서 나왔고, 공개 라이선스 글과 정답만으로 학습했습니다(AI 가 단
정답은 쓰지 않았습니다). 앱이 쓰는 규칙 엔진보다는 낮고, 아래 비교표는 다듬에 유리한 우리 평가셋에서 잰 것입니다
(Limitations 참고).

The model rewrites a sentence; each change it makes is then judged by its own
log-likelihood margin and kept only at or above the margin in `gating.json`,
and guards drop changes that touch non-Hangul, non-ASCII characters, add or
remove two or more characters, change a number, or jump three or more jamo to a
word absent from the open word list (`known_words.bin`). Use `dadeum_correct.py`,
which does all of this; plain `generate()` skips the judgement and the guards.

```bash
pip install torch transformers
python dadeum_correct.py "오늘은 날씨가 좋아서 산책을 갔는데 사람이 많앗다."
```

```python
from dadeum_correct import Corrector
corrector = Corrector(".")
corrector.correct("회의는 다음주 화요일에 하기로 했어요.")
corrector.edits("...")   # [(start, end, replacement), ...]
```

## Model

BART, 4 encoder and 1 decoder layers, width 768, 62.5M parameters, started from
KoBART (gogamza/kobart-base-v2).

## Training data

Openly licensed text and targets only - no pair was annotated by an AI provider.

| Pairs | Source text | Target |
|---|---|---|
| Rule-engine corrections | nsmc (CC0), unlabeled kocohub comments, Korean Wikipedia and Wikinews (CC BY-SA 4.0), 정책브리핑 (KOGL Type 1) | the dadeum rule engine, with its parts fitted to AI-annotated data switched off |
| Wikipedia editors' corrections | Korean Wikipedia page history (CC BY-SA 4.0) | the editor's corrected sentence, filtered (no evaluation sentences, no content swaps, no foreign-script or number changes) |

Training steps, from the base: clean_e4d1_init (layers cut) -> clean_e4d1 (legacy_clean:60, wiki_edits:7)

## Evaluation

Measured against gold that AI annotators wrote (not distributed); F0.5 over character edits, touching edits merged. That gold trained nothing, but its val split chose the training checkpoint and the margin in `gating.json`, so the val scores are slightly optimistic.

| Measure | Value |
|---|---|
| Blind half of val (1,196 sentences), F0.5 (P / R) | .890 (.958 / .692); the dadeum rule engine: .899 (.946 / .750) |
| Development, 300 sentences, F0.5 | .914; rule engine .950 |
| In-domain test, 350, F0.5 | .905; rule engine .927 |
| Sealed domains (reviews, comments, policy, requests), 870, F0.5 | .811; rule engine .863 |
| Confirmation domains, 600, F0.5 | .805; rule engine .831 |
| News, business and comments (single annotator), 799, F0.5 | .798; rule engine .820 |
| Kor-Lang8 rebuild (learners), 2,000, F0.5 | .083; rule engine .088 |
| Correct workplace email (27 sentences and the whole email), sentences changed | 0 |
| Clean Wikipedia sentences (19,759), sentences changed | 785, 645 of them spacing only; rule engine 424 |
| CPU latency per sentence, Apple M4 Pro, 4 threads | 34 ms median, 87 ms p95 |

### Next to other Korean correctors

The same sentences and scorer, F0.5. This model runs at its margin; the other open correctors as their cards say; the LLMs with the same annotation guideline in the prompt. The gold rewards minimal edits; on learners' writing (Kor-Lang8), where the reference corrections rewrite more, KoBART gec_kr leads. No public Korean leaderboard for this task was found, so this is our table, not a third-party ranking.

| System | Sealed domains (870) | Confirmation domains (600) | Kor-Lang8 (2,000) |
|---|---|---|---|
| **this model (dadeum-gec-small)** | .811 | .805 | .083 |
| [dadeum rule engine (the app)](https://github.com/zmflm0110/dadeum) | .863 | .831 | .088 |
| Claude Sonnet 5.5 with an annotation guideline | .895 | .887 | not run |
| Qwen3-8B | .548 | .562 | .127 |
| KoGrammar distil (theSOL1) | .481 | .435 | .107 |
| KoGrammar base (theSOL1) | .476 | .439 | .104 |
| ET5 typos corrector (j5ng) | .408 | .347 | .102 |
| KoBART gec_kr (Soyoung97) | .216 | .187 | .266 |

## Limitations

- The benchmark above is ours and favours this model: its gold was written by Claude under our annotation guideline,
  and it rewards minimal edits, so correctors that rewrite score low on it. No human checked that gold.
- It learns from the dadeum rule engine's corrections and does not beat that engine, which the dadeum app uses. Its
  point is an open license and a single file that runs on a CPU.
- It is a corrector for native writing. On learners' writing corrected by people (Kor-Lang8), where the references
  rewrite whole phrases, it rarely changes anything and KoBART gec_kr does far better.
- It shares the rule engine's blind spots; it corrects spelling, spacing and particles far better than word choice
  or style.
- One sentence at a time, up to 128 tokens; longer text is split at sentence ends.

## License

CC BY-SA 4.0 (`LICENSE`); attributions in `NOTICE`. `dadeum_correct.py` is MIT, like the dadeum repository.
