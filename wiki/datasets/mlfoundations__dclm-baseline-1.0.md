---
type: "dataset"
id: "mlfoundations/dclm-baseline-1.0"
source: "huggingface"
url: "https://huggingface.co/datasets/mlfoundations/dclm-baseline-1.0"
downloads: 323254
summary: "DCLM-baseline은 4조 토큰, 30억 문서 기반 언어 모델 사전학습용 연구 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[언어 모델링]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# mlfoundations/dclm-baseline-1.0

> dataset · [Hugging Face](https://huggingface.co/datasets/mlfoundations/dclm-baseline-1.0)

DCLM-baseline은 4조 토큰, 30억 문서 기반 언어 모델 사전학습용 연구 데이터셋입니다.

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `DCLM-baseline is a 4T token / 3B document pretraining dataset that achieves strong performance on language model benchmarks.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:language_modeling = `The dataset is in plain text format.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `DCLM-baseline is a 4T token / 3B document pretraining dataset that achieves strong performance on language model benchmarks.` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The source data is from Common Crawl, which is a repository of web crawl data.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `DCLM-Baseline is intended to be used as a research baseline for the DCLM benchmark.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `9999999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[BlinkDL__rwkv-7-world|BlinkDL/rwkv-7-world]]
- [[BlinkDL__rwkv7-g1|BlinkDL/rwkv7-g1]]
- [[RWKV__RWKV7-1.5B-20260805|RWKV/RWKV7-1.5B-20260805]]
- [[RWKV__RWKV7-13.3B-20260805|RWKV/RWKV7-13.3B-20260805]]
- [[RWKV__RWKV7-2.9B-20260805|RWKV/RWKV7-2.9B-20260805]]
- [[RWKV__RWKV7-7.2B-20260805|RWKV/RWKV7-7.2B-20260805]]
- [[RWKV__RWKV7-G1j-1.5B-20260831|RWKV/RWKV7-G1j-1.5B-20260831]]
- [[RWKV__RWKV7-G1j-13.3B-20260831|RWKV/RWKV7-G1j-13.3B-20260831]]
- [[RWKV__RWKV7-G1j-2.9B-20260831|RWKV/RWKV7-G1j-2.9B-20260831]]
- [[RWKV__RWKV7-G1j-7.2B-20260831|RWKV/RWKV7-G1j-7.2B-20260831]]
- [[RWKV__RWKV7-Goose-World-PTH|RWKV/RWKV7-Goose-World-PTH]]
- [[aabbdev__RWKV7-1.5B-20260805|aabbdev/RWKV7-1.5B-20260805]]
- [[fla-hub__RWKV7-G1j-1.5B-20260831|fla-hub/RWKV7-G1j-1.5B-20260831]]
- [[fla-hub__RWKV7-G1j-13.3B-20260831|fla-hub/RWKV7-G1j-13.3B-20260831]]
- [[fla-hub__RWKV7-G1j-2.9B-20260831|fla-hub/RWKV7-G1j-2.9B-20260831]]
- [[fla-hub__RWKV7-G1j-7.2B-20260831|fla-hub/RWKV7-G1j-7.2B-20260831]]
