---
type: "dataset"
id: "MindCastSogang/Youtube_news_comments_analysis_ver2"
source: "huggingface"
url: "https://huggingface.co/datasets/MindCastSogang/Youtube_news_comments_analysis_ver2"
downloads: 561
summary: "2014~2026년 유튜브 뉴스 댓글 7천4백만 개의 감정 분석 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# MindCastSogang/Youtube_news_comments_analysis_ver2

> dataset · [Hugging Face](https://huggingface.co/datasets/MindCastSogang/Youtube_news_comments_analysis_ver2)

2014~2026년 유튜브 뉴스 댓글 7천4백만 개의 감정 분석 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[임베딩]] — ner · readme = `44개 세부 감정 점수는 sigmoid 다중 라벨 점수로 합이 1이 아니며, 대분류 점수는 대응 세부 점수의 합입니다.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding = `댓글 본문·제목·감정 예측 값은 변경하거나 재추론하지 않았습니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `댓글 본문·제목·감정 예측 값은 변경하거나 재추론하지 않았습니다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `884` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — ner · readme = `YouTube 뉴스 댓글 감정 분석 — 최종 통합본` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `학습/평가용 분할은 수행하지 않았습니다. Hugging Face의 `train` 이름은 전체 데이터 로딩을 위한 기본 split 명칭일 뿐입니다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `emotion_scores_44_json` 열 p90 1326자 ≈ 884 토큰 (viewer statistics, final/train)
