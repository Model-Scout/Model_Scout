---
license: cc-by-4.0
language: [ko]
task_categories: [token-classification]
tags: [coreference, anaphora, korean, corefud]
size_categories: [1K<n<10K]
---

# elda-coref-ko-v2 — 한국어 조응 재료 (CorefUD **Korean-ECMT** 파생)

`CorefUD 1.4` 의 **Korean-ECMT** 를 우리 학습 형식(턴 · 멘션 · 선행사)으로 옮긴 것입니다.
`train.jsonl` 1,204문서 · `dev.jsonl` 133문서.

## 출처와 라이선스
| | |
|---|---|
| 원본 | [`lattice-nlp/corefud-1-4`](https://huggingface.co/datasets/lattice-nlp/corefud-1-4) → **CorefUD_Korean-ECMT** |
| 원본 라이선스 | **CC BY 4.0** |
| 이 파생물 | **CC BY 4.0** (원본과 같음 · 출처 표기 필요) |

> ⛔ **CorefUD 전체를 이 조건으로 읽지 마십시오.** CorefUD 1.4 는 **트리뱅크마다 라이선스가 다르고
> NC(상업적 이용 금지)가 섞여 있습니다** — English-GUM `CC BY-NC-SA 4.0` · English-ParCorFull
> `CC BY-NC 4.0` · Lithuanian-LCC 는 CC 가 아닌 `CLARIN-LT End User License`.
> 여기 담긴 것은 **한국어(Korean-ECMT) 하나뿐**이고 그것이 **CC BY 4.0** 이라서 냅니다.
> 그래서 이 저장소는 **언어를 섞지 않습니다.**

## ★ 원본 변환에서 **고친 것** — 같은 문장 안 선행사

우리 변환기가 사슬 지도를 **문장 단위로 뒤늦게** 갱신하고 있었습니다. 그래서 같은 문장 안 선행사가
보이지 않았고, 그 줄에 **NULL** 이거나 **앞 문장의 다른 고리**가 정답으로 적혔습니다.
```
원본이 「같은 문장 선행사」라 한 1,397줄을 옛 변환본은 이렇게 적었다
   NULL 로 적음             652  46.67%
   앞 턴의 다른 고리로 적음    592  42.38%
```
이 판(`v2`)은 **멘션마다** 사슬을 갱신합니다 ⇒ 같은 턴 선행사 **7.76%** 가 제자리에 섭니다
(NULL 76.34%→72.04% · 앞 턴 23.66%→20.20%).

## 형식
한 줄 = 한 문서. `turns[]` 안에 `words` · `items`(멘션) · `gold`(`ref_to: {turn,item} | null`) · `cands`.
★ **`ref_to.turn` 이 자기 턴과 같으면 같은 문장 안 선행사**입니다.

⚠ **소비자 주의 둘**
1. 같은 턴 선행사를 쓰려면 후보 목록에 **그 턴의 앞 멘션**을 넣어야 합니다. 안 넣으면 그 라벨은
   후보에 없어서 **조용히 마스크**됩니다(= 안 배웁니다).
2. 멘션이 **자기보다 뒤**를 가리키지 못하게 **인과 마스크**를 거십시오. 안 걸면 자기 자신을
   가리키는 것이 정답이 될 수 있습니다.

## 인용
원본 **CorefUD 1.4** 를 함께 인용해 주십시오. 이 파생물이 더한 것은 **형식 변환 + 위 라벨 수정**뿐입니다.
