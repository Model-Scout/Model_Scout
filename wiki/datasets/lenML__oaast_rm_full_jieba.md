---
type: "dataset"
id: "lenML/oaast_rm_full_jieba"
source: "huggingface"
url: "https://huggingface.co/datasets/lenML/oaast_rm_full_jieba"
downloads: 40
summary: "llm 반복 문제 해결을 위해 oaast 말뭉치를 결바화하여 중복 내용 거부 효과를 강화한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
input_modality:
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
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# lenML/oaast_rm_full_jieba

> dataset · [Hugging Face](https://huggingface.co/datasets/lenML/oaast_rm_full_jieba)

llm 반복 문제 해결을 위해 oaast 말뭉치를 결바화하여 중복 내용 거부 효과를 강화한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `尝试解决"llm repetition problem"，使用分词模型对oaast语料进行“结巴化”数据增强，提供更强的重复内容拒绝效果。` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `尝试解决"llm repetition problem"，使用分词模型对oaast语料进行“结巴化”数据增强` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `尝试解决"llm repetition problem"，使用分词模型对oaast语料进行“结巴化”数据增强` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `35 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `222` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `尝试解决"llm repetition problem"，使用分词模型对oaast语料进行“结巴化”数据增强，提供更强的重复内容拒绝效果。` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `instruction` 열 p90 889자 ≈ 222 토큰 (viewer statistics, default/train)
