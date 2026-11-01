---
type: "dataset"
id: "UTokyo-Yokoya-Lab/tweet_sentiment_extraction_CS-MTEB"
source: "huggingface"
url: "https://huggingface.co/datasets/UTokyo-Yokoya-Lab/tweet_sentiment_extraction_CS-MTEB"
downloads: 62
summary: "다국어 코드스위칭 스타일로 재작성된 트윗 감정 추출 테스트셋 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[it]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[nl]]"
  - "[[pt]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# UTokyo-Yokoya-Lab/tweet_sentiment_extraction_CS-MTEB

> dataset · [Hugging Face](https://huggingface.co/datasets/UTokyo-Yokoya-Lab/tweet_sentiment_extraction_CS-MTEB)

다국어 코드스위칭 스타일로 재작성된 트윗 감정 추출 테스트셋 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · tags, task_categories = `text-classification` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `Tweet Sentiment Extraction CS-MTEB` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Tweet Sentiment Extraction CS-MTEB` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:information_extraction, task:question_answering = `test set sentences rewritten in Chinese-English, Japanese-English, German-English, Spanish-English, Korean-English, French-English, Italian-English, Portuguese-` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Tweet Sentiment Extraction CS-MTEB` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `10 languages` · 신뢰도 high
- **언어**: [[nl]] — metadata · languages = `nl` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `31` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Tweet Sentiment Extraction CS-MTEB` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Code-switching test sets` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Original train and test splits` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `label_text` 열 p90 123자 ≈ 31 토큰 (viewer statistics, test_ko_en/test)
