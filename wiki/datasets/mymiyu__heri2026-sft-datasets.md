---
type: "dataset"
id: "mymiyu/heri2026-sft-datasets"
source: "huggingface"
url: "https://huggingface.co/datasets/mymiyu/heri2026-sft-datasets"
downloads: 115
summary: "한국 문화유산 해설 AI 학습용 중간 산출물로 문화유산 스토리텔링 SFT 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
---
# mymiyu/heri2026-sft-datasets

> dataset · [Hugging Face](https://huggingface.co/datasets/mymiyu/heri2026-sft-datasets)

한국 문화유산 해설 AI 학습용 중간 산출물로 문화유산 스토리텔링 SFT 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation = `GPT-4o / GPT-4.1 / Claude로 생성했으며, 근거는 한국민족문화대백과(EncyKorea)·국립중앙박물관·aimuse 자료입니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `2024 큐레이터 QA·해설 대화 SFT 데이터(merged_file, train/dev)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `한국 문화유산 스토리텔링 SFT 데이터셋` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `학습용 중간 산출물을 모은 데이터셋입니다.` · 신뢰도 medium
