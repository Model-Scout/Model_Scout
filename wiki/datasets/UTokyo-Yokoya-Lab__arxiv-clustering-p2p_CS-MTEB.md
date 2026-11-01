---
type: "dataset"
id: "UTokyo-Yokoya-Lab/arxiv-clustering-p2p_CS-MTEB"
source: "huggingface"
url: "https://huggingface.co/datasets/UTokyo-Yokoya-Lab/arxiv-clustering-p2p_CS-MTEB"
downloads: 153
summary: "ArXiv 논문 클러스터링 데이터셋의 다국어 코드스위칭 버전으로 임베딩 평가용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
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
  - "[[학술·논문]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# UTokyo-Yokoya-Lab/arxiv-clustering-p2p_CS-MTEB

> dataset · [Hugging Face](https://huggingface.co/datasets/UTokyo-Yokoya-Lab/arxiv-clustering-p2p_CS-MTEB)

ArXiv 논문 클러스터링 데이터셋의 다국어 코드스위칭 버전으로 임베딩 평가용입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `ArXiv Clustering P2P CS-MTEB` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Massive Text Embedding Benchmark` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding = `sentences rewritten in Chinese-English, Japanese-English, German-English, Spanish-English, Korean-English, French-English, Italian-English, Portuguese-English, ` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `sentences rewritten in Chinese-English, Japanese-English, German-English, Spanish-English, Korean-English, French-English, Italian-English, Portuguese-English, ` · 신뢰도 low
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
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `407` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `ArXiv Clustering P2P CS-MTEB` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `An MTEB dataset` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `sentences` 열 p90 1629자 ≈ 407 토큰 (viewer statistics, test_ko_en/test)
