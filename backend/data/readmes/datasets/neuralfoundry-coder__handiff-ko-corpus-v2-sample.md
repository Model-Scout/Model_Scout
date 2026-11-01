---
license: other
license_name: mixed-cc-by-sa-4.0-and-nia-research
language:
  - ko
tags:
  - korean
  - sample
  - handiff
size_categories:
  - n<1K
pretty_name: "HanDiff Korean Corpus v2 — Sample"
---

<!-- aegis-dataset-card -->

# handiff-ko-corpus-v2-sample

> **용도 기록 없음** · HanDiff Korean Corpus v2 — Sample  
> 파일 10개 · 6.0 MB · 행 140 · revision `3a0d2d32c9` · 카드 갱신 2026-10-20  
> 전체 모델 ↔ 데이터 매핑 · 서버 복원 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020)

## 개요
각 소스에서 무작위 10건을 추출한 inspection sample 입니다.
전체 데이터는 `neuralfoundry-coder/handiff-ko-corpus-v2` 에서 확인하세요.

## 이 데이터로 학습한 모델
이 데이터로 학습했다는 기록(학습 설정 · 모델 카드)을 찾지 못했다. 카탈로그의 '확인 필요' 목록에 있다.

## 파일 구성
| 파일 | 크기 | 행 | 내용 |
|---|---|---|---|
| `README.md` | 2.6 KB | - |  |
| `aihub_110_beoblyeong_sample.jsonl` | 45.5 KB | 10 |  |
| `aihub_110_nonmun_sample.jsonl` | 24.9 KB | 10 |  |
| `aihub_110_pannrei_sample.jsonl` | 156.1 KB | 10 |  |
| `aihub_116_dialog_sample.jsonl` | 8.2 KB | 10 |  |
| `aihub_71557_news_sample.jsonl` | 104.9 KB | 10 |  |
| `aihub_86_emotion_sample.jsonl` | 6.3 KB | 10 |  |
| `ko_v2_extended.json` | 5.2 MB | - |  |
| `kowiki_v1_sample.jsonl` | 48.7 KB | 10 |  |
| `samples_all.jsonl` | 394.5 KB | 70 |  |

## 필드 · 범주 분포
**`samples_all.jsonl`** (기준 `samples_all.jsonl`)

| 필드 | 타입 | 채움 |
|---|---|---|
| `source_id` | str | 100% |
| `text` | str | 100% |
| `license` | str | 100% |
| `title` | str | 71% |
| `doc_no` | int | 43% |
| `session_id` | str | 29% |
| `wiki_id` | str | 14% |
| `url` | str | 14% |
| `script_id` | str | 14% |
| `press` | str | 14% |
| `field` | str | 14% |
| `date` | str | 14% |

**`aihub_110_beoblyeong_sample.jsonl`, `aihub_110_nonmun_sample.jsonl`, `aihub_110_pannrei_sample.jsonl`** (기준 `aihub_110_beoblyeong_sample.jsonl`)

| 필드 | 타입 | 채움 |
|---|---|---|
| `source_id` | str | 100% |
| `doc_no` | int | 100% |
| `title` | str | 100% |
| `text` | str | 100% |
| `license` | str | 100% |

**`aihub_116_dialog_sample.jsonl`, `aihub_86_emotion_sample.jsonl`** (기준 `aihub_116_dialog_sample.jsonl`)

| 필드 | 타입 | 채움 |
|---|---|---|
| `source_id` | str | 100% |
| `session_id` | str | 100% |
| `text` | str | 100% |
| `license` | str | 100% |

**`aihub_71557_news_sample.jsonl`** (기준 `aihub_71557_news_sample.jsonl`)

| 필드 | 타입 | 채움 |
|---|---|---|
| `source_id` | str | 100% |
| `script_id` | str | 100% |
| `press` | str | 100% |
| `field` | str | 100% |
| `date` | str | 100% |
| `title` | str | 100% |
| `text` | str | 100% |
| `license` | str | 100% |

**`kowiki_v1_sample.jsonl`** (기준 `kowiki_v1_sample.jsonl`)

| 필드 | 타입 | 채움 |
|---|---|---|
| `source_id` | str | 100% |
| `title` | str | 100% |
| `wiki_id` | str | 100% |
| `url` | str | 100% |
| `text` | str | 100% |
| `license` | str | 100% |

필드는 행 최상위 키, 채움은 그 키가 있는 행 비율이다. 범주 분포는 글 필드가 아니고 값이 짧고(≤48자) 종류가 적은(≤40) 필드만 셌다.

## 내려받기 · 복원
```bash
hf download neuralfoundry-coder/handiff-ko-corpus-v2-sample --repo-type dataset --local-dir <폴더>
```
- 서버 파일 전체의 위치 · 재생성 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020) 의 `restore_map.json`

## 기존 설명 (2026-10-20 이전 카드)

### HanDiff Korean Corpus v2 — Sample

> ⚠️ **사용자 책임 고지**: 본 샘플은 7개 소스(라이선스 상이)에서 각 10건씩 추출했습니다.
> AI Hub(NIA-Research) 출처 데이터는 **상업적 사용·재배포가 금지**됩니다.
> 라이선스 준수 책임은 사용자에게 있습니다. 자세한 사항은 §라이선스 + §사용자 책임 참조.

각 소스에서 무작위 10건을 추출한 inspection sample 입니다.
전체 데이터는 `neuralfoundry-coder/handiff-ko-corpus-v2` 에서 확인하세요.

#### 포함 파일

각 소스별 `<source>_sample.jsonl` (10건) + 통합 `samples_all.jsonl` + tokenizer.
각 record에는 `source_id` + `license` 필드가 있어 라이선스 추적이 가능합니다.

| Source | License | 도메인 |
|---|---|---|
| kowiki_v1.jsonl | CC-BY-SA-4.0 | 백과 (위키) |
| aihub_110_nonmun.jsonl | LicenseRef-NIA-Research | 학술 논문 |
| aihub_110_pannrei.jsonl | LicenseRef-NIA-Research | 법률 판례 |
| aihub_110_beoblyeong.jsonl | LicenseRef-NIA-Research | 법령 제·개정문 |
| aihub_71557_news.jsonl | LicenseRef-NIA-Research | 뉴스 본문 |
| aihub_86_emotion.jsonl | LicenseRef-NIA-Research | 감성 대화 |
| aihub_116_dialog.jsonl | LicenseRef-NIA-Research | 도메인 대화 |

#### 사용 (예: 토크나이저 호환성 점검)

```bash
huggingface-cli download neuralfoundry-coder/handiff-ko-corpus-v2-sample \
    --repo-type dataset --local-dir samples/
head samples/samples_all.jsonl
```

#### 라이선스 (요약)

- **kowiki**: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) — 출처 표기 + 동일 라이선스
- **aihub_110, 71557, 86, 116**: AI Hub NIA Research Use License — **상업 사용 금지**, 연구·학술만.
  - 약관: <https://aihub.or.kr/intrcn/agreement/agreement.do>

#### 사용자 책임 (Disclaimer)

1. **라이선스 준수 책임은 사용자(다운로더)에게 있습니다**.
2. 본 샘플의 공개 배포는 원 라이선스 의무를 사용자가 면제받음을 의미하지 **않습니다**.
3. AI Hub 출처 record를 상업적으로 사용한 경우의 모든 법적 책임은 사용자에게 있으며,
   업로더(neuralfoundry-coder)는 어떠한 책임도 지지 않습니다.
4. 본 데이터셋은 ‘있는 그대로(AS IS)’ 제공되며, 보증은 없습니다.

전체 데이터셋: <https://huggingface.co/datasets/neuralfoundry-coder/handiff-ko-corpus-v2>
