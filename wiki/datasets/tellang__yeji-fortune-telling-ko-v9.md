---
type: "dataset"
id: "tellang/yeji-fortune-telling-ko-v9"
source: "huggingface"
url: "https://huggingface.co/datasets/tellang/yeji-fortune-telling-ko-v9"
downloads: 63
summary: "한국어 점성술, 사주, 타로, 화투 분야의 운세 및 점술 지침 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[비상업 전용]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# tellang/yeji-fortune-telling-ko-v9

> dataset · [Hugging Face](https://huggingface.co/datasets/tellang/yeji-fortune-telling-ko-v9)

한국어 점성술, 사주, 타로, 화투 분야의 운세 및 점술 지침 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `instruction-output pairs` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Expert-level divination interpretation and advice` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1212` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Yeji-fortune-telling-ko-v9 is a comprehensive supervised fine-tuning (SFT) dataset` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 1818자 ≈ 1212 토큰 (viewer statistics, alpaca/train)
