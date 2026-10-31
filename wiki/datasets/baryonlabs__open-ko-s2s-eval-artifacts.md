---
type: "dataset"
id: "baryonlabs/open-ko-s2s-eval-artifacts"
source: "huggingface"
url: "https://huggingface.co/datasets/baryonlabs/open-ko-s2s-eval-artifacts"
downloads: 71
summary: "Open Ko-S2S 평가 산출물로 음성 인식 모델의 문자 오류율(CER) 검증용 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# baryonlabs/open-ko-s2s-eval-artifacts

> dataset · [Hugging Face](https://huggingface.co/datasets/baryonlabs/open-ko-s2s-eval-artifacts)

Open Ko-S2S 평가 산출물로 음성 인식 모델의 문자 오류율(CER) 검증용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Open Ko-S2S 평가 산출물 (감사용)` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · tags, task_categories = `automatic-speech-recognition` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — task_rule · task:speech_recognition = `audio` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `전사 텍스트와 채점 결과만 담습니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `모델 출력(hyp)과 채점 결과(cer_err/cer_len/cer)는 우리 산출물이라 그대로 공개합니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `68` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Open Ko-S2S 평가 산출물 (감사용)` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `Open Ko-S2S 평가 산출물 (감사용)` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `transcripts_csv` 열 p90 102자 ≈ 68 토큰 (viewer statistics, index/train)
