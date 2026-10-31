---
type: "dataset"
id: "doanhlt/cabin-interpreter-interview-test"
source: "huggingface"
url: "https://huggingface.co/datasets/doanhlt/cabin-interpreter-interview-test"
downloads: 157
summary: "동시통역, 다국어 음성인식, 2방향 인터뷰 평가용 유튜브 영상 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[질의응답]]"
  - "[[음성 인식]]"
  - "[[번역]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# doanhlt/cabin-interpreter-interview-test

> dataset · [Hugging Face](https://huggingface.co/datasets/doanhlt/cabin-interpreter-interview-test)

동시통역, 다국어 음성인식, 2방향 인터뷰 평가용 유튜브 영상 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `xử lý ngữ cảnh đối đáp 2 chiều có phiên dịch viên` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · readme, tags, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `Chuẩn âm thanh trích xuất: 16kHz Mono WAV` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:translation = `Danh mục đầy đủ toàn bộ 218 video kèm siêu dữ liệu (URL, tiêu đề, cặp ngôn ngữ, loại hình hội thoại)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:speech_recognition, task:translation = `đánh giá năng lực dịch song song (simultaneous / consecutive interpretation), nhận dạng giọng nói đa ngôn ngữ (ASR) và xử lý ngữ cảnh đối đáp 2 chiều` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `24` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Cabin AI - YouTube Interpreter & Two-Way Interview Benchmark Dataset` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Tập dữ liệu kiểm thử thực tế phục vụ đánh giá năng lực dịch song song` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `title` 열 p90 96자 ≈ 24 토큰 (viewer statistics, default/test)
