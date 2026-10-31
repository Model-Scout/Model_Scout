---
type: "dataset"
id: "codeparrot/github-code-clean"
source: "huggingface"
url: "https://huggingface.co/datasets/codeparrot/github-code-clean"
downloads: 40750
summary: "GitHub에서 수집한 32개 프로그래밍 언어의 1TB 코드 파일 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# codeparrot/github-code-clean

> dataset · [Hugging Face](https://huggingface.co/datasets/codeparrot/github-code-clean)

GitHub에서 수집한 32개 프로그래밍 언어의 1TB 코드 파일 데이터셋입니다.

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `The GitHub Code clean dataset in a more filtered version of codeparrot/github-code dataset` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:language_modeling = `it consists of 115M code files from GitHub in 32 programming languages with 60 extensions totaling in almost 1TB of text data` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `it consists of 115M code files from GitHub in 32 programming languages with 60 extensions totaling in almost 1TB of text data` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The GitHub Code clean dataset in a more filtered version of codeparrot/github-code dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The GitHub Code clean dataset in a more filtered version of codeparrot/github-code dataset` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[AneekC__quipu-moe-1B-A149M|AneekC/quipu-moe-1B-A149M]]
- [[AneekC__quipu-moe-1B-A149M-chat|AneekC/quipu-moe-1B-A149M-chat]]
- [[AneekC__quipu-moe-1B-A149M-chat-distill|AneekC/quipu-moe-1B-A149M-chat-distill]]
