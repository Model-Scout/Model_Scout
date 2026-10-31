---
language:
- ko
license: cc-by-4.0
task_categories:
- question-answering
dataset_info:
  features:
  - name: topic
    dtype: string
  - name: problem
    dtype: string
  - name: answer
    dtype: string
  - name: urls
    dtype: string
configs:
- config_name: default
  data_files:
  - split: test
    path: kosimpleqa.jsonl
---

# KoSimpleQA

KoSimpleQA (Korean SimpleQA) is a 1,000-prompt benchmark for evaluating factuality in large language models (LLMs) with a focus on **Korean cultural knowledge**. The benchmark is designed to be challenging yet easy to grade, consisting of short, fact-seeking questions with unambiguous answers. Unlike simply translating existing English benchmarks, KoSimpleQA addresses the need for culturally grounded evaluation—assessing not just linguistic competence in Korean, but also understanding of Korean cultural context.

## Motivation

Existing factuality benchmarks like SimpleQA primarily focus on English and Chinese, with questions rooted in Anglophone cultural contexts. Simply translating these benchmarks into Korean is insufficient, as they do not meaningfully assess models trained on Korean data. Evaluating LLMs in Korean requires both **linguistic competence** and **cultural knowledge** associated with the Korean language community.

## Key Results

- Even the strongest model evaluated achieves only **33.7%** correct answers, underscoring the challenging nature of KoSimpleQA.
- Performance rankings on KoSimpleQA **diverge substantially** from those on English SimpleQA, highlighting the distinct cultural dimension it captures.
- Analysis of reasoning LLMs shows that engaging reasoning capabilities can help models better elicit their latent knowledge and improve their ability to abstain when uncertain.

## Data Format

The dataset is provided in JSONL format with the following fields:

| Field | Description |
|-------|-------------|
| `topic` | Category of the question (e.g., art, science, history, sports, etc.) |
| `problem` | The Korean fact-seeking question |
| `answer` | The unambiguous correct answer |
| `urls` | Reference URLs for answer verification |

### Category Distribution

The benchmark covers diverse topics including: Art, Science, History, Sports, Geography, Politics, Economy, Society, and more.

## Example

```json
{
  "topic": "art",
  "problem": "봉준호 감독의 '기생충'은 대한민국 몇 번째 천만영화인가요?",
  "answer": "26번째",
  "urls": "https://www.newspim.com/news/view/20190722000045,https://www.khan.co.kr/article/201907221353001"
}
```

## Resources

- Paper: https://arxiv.org/abs/2510.18368
- Code: https://github.com/naver-ai/KoSimpleQA
- Original Dataset: https://anonymous.4open.science/r/KoSimpleQA-62EB