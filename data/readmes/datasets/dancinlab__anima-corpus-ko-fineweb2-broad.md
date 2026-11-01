---
license: odc-by
language:
- ko
task_categories:
- text-generation
pretty_name: anima Korean broad corpus (FineWeb-2 kor_Hang)
size_categories:
- 10B<n<100B
tags:
- anima
- korean
- pretraining
- byte-level
- fineweb-2
---

# anima-corpus-ko-fineweb2-broad

🇰🇷 한국어 **broad (일반) 코퍼스** for anima `conv` 303M byte-level pretraining.

anima chat register 표준(`a_chat_registers`)의 4칸 `{ko·en} × {일반·SNS}` 중 **ko-일반** 칸을 메우기 위한 데이터셋이다. 기존 ko-일반 source 가 ~1.7MB 로 빈약(en ~202MB 대비)했던 갭을 FineWeb-2 한국어로 보강한다.

## Source

- **Upstream**: [`HuggingFaceFW/fineweb-2`](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2), config **`kor_Hang`** (한국어 한글 스크립트).
- **Extracted from**: train parquet `data/kor_Hang/train/000_00000.parquet` (1 of 25 shards).
- **Field**: `text` 컬럼만 추출 (raw UTF-8, byte-vocab256 학습용으로 정규화 없이 원문 그대로).

## Processing

- `text` 컬럼 → 문서당 1 블록, 문서 사이 빈 줄 separator.
- strip + 빈 문서 제거 + MD5 기반 정확-중복 제거 (dups 2개만 발견 = upstream 이 이미 dedup 됨).
- byte-level UTF-8 그대로 유지 (NFC/NFD 정규화·소문자화·토크나이즈 없음).

## Statistics

| metric | value |
|---|---|
| documents | 2,782,998 |
| lines | 65,486,209 |
| bytes (UTF-8) | 10,553,840,492 (~9.83 GiB) |
| UTF-8 decode errors | 0 (full-file incremental check) |
| hangul ratio (sample) | ~0.59 |
| source shards | 1 / 25 (FineWeb-2 kor_Hang train) |

`manifest.json` 에 sha256 / bytes / lines / docs 박제.

## License

**ODC-BY** — FineWeb-2 의 라이선스([Open Data Commons Attribution License](https://opendatacommons.org/licenses/by/1-0/))를 승계한다. 본 데이터셋은 FineWeb-2 `kor_Hang` 의 파생물이며 동일 라이선스를 따른다. 출처 표기: HuggingFaceFW/fineweb-2.

## Usage (anima)

anima `conv` (CLMConvMoE byte V256) 303M broad pretrain 의 ko-일반 칸. 다른 register/언어 칸:
- ko-SNS / en-SNS → `anima-persona-sns-corpus`
- en-일반 → `anima-corpus-5lang-7b-webscale`, `anima-chat-corpus-mix-70wiki-30dialogue`
- grounding 닻 → `anima-kosmos-303m-kr-en-sns`
