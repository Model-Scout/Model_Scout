---
type: "dataset"
id: "bigcode/starcoderdata"
source: "huggingface"
url: "https://huggingface.co/datasets/bigcode/starcoderdata"
downloads: 15863
summary: "StarCoder 모델 학습용으로 86개 프로그래밍 언어 코드와 GitHub 데이터 포함한 대규모 코드 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[code]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# bigcode/starcoderdata

> dataset · [Hugging Face](https://huggingface.co/datasets/bigcode/starcoderdata)

StarCoder 모델 학습용으로 86개 프로그래밍 언어 코드와 GitHub 데이터 포함한 대규모 코드 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `This is the dataset used for training StarCoder and StarCoderBase.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `It contains 783GB of code in 86 programming languages, and includes 54GB GitHub Issues + 13GB Jupyter notebooks in scripts and text-code pairs, and 32GB of GitH` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `It contains 783GB of code in 86 programming languages, and includes 54GB GitHub Issues + 13GB Jupyter notebooks in scripts and text-code pairs, and 32GB of GitH` · 신뢰도 medium
- **언어**: [[code]] — metadata · languages = `code` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `It contains 783GB of code in 86 programming languages, and includes 54GB GitHub Issues + 13GB Jupyter notebooks in scripts and text-code pairs, and 32GB of GitH` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This is the dataset used for training StarCoder and StarCoderBase.` · 신뢰도 medium

## 이 데이터로 학습한 모델

- [[BlinkDL__rwkv-5-world|BlinkDL/rwkv-5-world]]
- [[BlinkDL__rwkv-6-world|BlinkDL/rwkv-6-world]]
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
- [[RWKV__rwkv-5-world-all-pth|RWKV/rwkv-5-world-all-pth]]
- [[SmerkyG__rwkv-5-world-all-pth|SmerkyG/rwkv-5-world-all-pth]]
- [[SmerkyG__rwkv-6-world-all-pth|SmerkyG/rwkv-6-world-all-pth]]
- [[aabbdev__RWKV7-1.5B-20260805|aabbdev/RWKV7-1.5B-20260805]]
- [[fla-hub__RWKV7-G1j-1.5B-20260831|fla-hub/RWKV7-G1j-1.5B-20260831]]
- [[fla-hub__RWKV7-G1j-13.3B-20260831|fla-hub/RWKV7-G1j-13.3B-20260831]]
- [[fla-hub__RWKV7-G1j-2.9B-20260831|fla-hub/RWKV7-G1j-2.9B-20260831]]
- [[fla-hub__RWKV7-G1j-7.2B-20260831|fla-hub/RWKV7-G1j-7.2B-20260831]]
