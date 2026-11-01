---
license: mit
language:
- ko
tags:
- text
- web-corpus
- educational
dataset_info:
  features:
  - name: text
    dtype: string
  - name: score
    dtype: float
  splits:
  - name: train
    num_bytes: ...
    num_examples: ...
  download_size: ...
  dataset_size: ...
configs:
- config_name: default
  data_files:
  - split: train
    path: data-*.arrow
task_categories:
- text-classification
---

# Korean Webtext Edu

## 데이터셋 설명

**Korean-webtext-edu**는 **[HAERAE-HUB/KOREAN-WEBTEXT](https://huggingface.co/datasets/HAERAE-HUB/KOREAN-WEBTEXT)** 데이터셋에서 선별된 하위 집합입니다. 이 데이터셋은 원본 데이터의 128만 개 문서 중 교육적 가치가 높은 콘텐츠만을 필터링하여 구축되었습니다.

본 데이터셋의 필터링 과정은 **[HuggingFaceFW/fineweb-edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu)** 데이터셋의 방법론에서 영감을 받았습니다. 교육적이고 사실적이며 구조화된 한국어 웹 텍스트를 대규모로 제공하여, 모델 학습의 질을 높이는 것을 목표로 합니다.

## 데이터셋 구축

### 소스 데이터

* **HAERAE-HUB/KOREAN-WEBTEXT**

### 필터링 및 점수 산정

"교육적 가치" 점수 산정 방식은 [FineWeb-edu 방법론](https://huggingface.co/papers/2406.17557)을 기반으로 합니다. 텍스트의 일관성, 사실 관계의 정확성, 핵심 개념 소개, 교육적 적합성 등을 기준으로 5점 척도(Additive Scale)를 사용하여 평가했습니다.

FineWeb-Edu는 Llama-3로 학습된 별도의 분류기를 사용한 것과 달리, 본 데이터셋은 **[Qwen/Qwen3-Next-80B-A3B](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Thinking)** 모델을 사용하여 직접 점수를 산정했습니다.

`HAERAE-HUB/KOREAN-WEBTEXT`의 각 문서는 모델을 통해 점수가 매겨졌으며, 임계값(예: 3.0점 이상)을 통과한 고품질 데이터만 최종 데이터셋에 포함되었습니다.

### 점수 산정 프롬프트

문서 평가에 사용된 영어 프롬프트는 다음과 같습니다:

```text
Below is an extract from a web page. Evaluate whether the page has a high educational value and could be useful in an educational setting for teaching from primary school to grade school levels using the additive 5-point scoring system described below. Points are accumulated based on the satisfaction of each criterion:
- Add 1 point if the extract provides some basic information relevant to educational topics, even if it includes some irrelevant or non-academic content like advertisements and promotional material.
- Add another point if the extract addresses certain elements pertinent to education but does not align closely with educational standards. It might mix educational content with non-educational material, offering a superficial overview of potentially useful topics, or presenting information in a disorganized manner and incoherent writing style.
- Award a third point if the extract is appropriate for educational use and introduces key concepts relevant to school curricula. It is coherent though it may not be comprehensive or could include some extraneous information. It may resemble an introductory section of a textbook or a basic tutorial that is suitable for learning but has notable limitations like treating concepts that are too complex for grade school students.
- Grant a fourth point if the extract highly relevant and beneficial for educational purposes for a level not higher than grade school, exhibiting a clear and consistent writing style. It could be similar to a chapter from a textbook or a tutorial, offering substantial educational content, including exercises and solutions, with minimal irrelevant information, and the concepts aren’t too advanced for grade school students. The content is coherent, focused, and valuable for structured learning.
- Bestow a fifth point if the extract is outstanding in its educational value, perfectly suited for teaching either at primary school or grade school. It follows detailed reasoning, the writing style is easy to follow and offers profound and thorough insights into the subject matter, devoid of any non-educational or complex content.

The extract: <extract>

After examining the extract:
  - Briefly justify your total score, up to 100 words.
  - Conclude with the score using the format: "Educational score: "
```

## 데이터 필드 (Data Fields)

* **`text`** (string): 문서의 텍스트 본문.
* **`score`** (int): `Qwen3-next-80b-a3b` 모델이 할당한 교육적 점수 (0-5점).

## 사용 방법 (Usage)

Hugging Face `datasets` 라이브러리를 통해 간편하게 로드할 수 있습니다:

```python
from datasets import load_dataset

dataset = load_dataset("eliceai/korean-webtext-edu")
```

## 라이선스

본 데이터셋은 MIT License 하에 제공됩니다.

## 인용

본 데이터셋을 연구 또는 서비스에 사용할 경우, 이 데이터셋과 원본 HAERAE-HUB/KOREAN-WEBTEXT 데이터셋을 함께 인용해 주시기 바랍니다.

```bibtex
@misc{korean-webtext-edu,
  author = {Elice Group},
  title = {Korean Webtext Edu},
  year = {2025},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/eliceai/korean-webtext-edu}}
}

@misc{korean-webtext,
  author = {HAERAE HUB},
  title = {KOREAN-WEBTEXT},
  year = {2024},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/HAERAE-HUB/KOREAN-WEBTEXT}}
}
```

---

# Korean Webtext Edu

## Dataset Description

**Korean-webtext-edu** is a curated subset of the **[HAERAE-HUB/KOREAN-WEBTEXT](https://huggingface.co/datasets/HAERAE-HUB/KOREAN-WEBTEXT)** dataset. The dataset was created by filtering the original 1.28 million documents based on their educational value.

This filtering process is inspired by the methodology used to create the **[HuggingFaceFW/fineweb-edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu)** dataset. The goal is to provide a large-scale, high-quality corpus of Korean web text suitable for training models on educational, factual, and well-structured content.

## Dataset Creation

### Source Data

* **HAERAE-HUB/KOREAN-WEBTEXT**: A large-scale Korean web text corpus.

### Filtering and Scoring

The "educational" scoring function was adapted from the [FineWeb-edu methodology](https://huggingface.co/papers/2406.17557). This methodology evaluates text on an additive 5-point scale, assessing criteria such as:

* Coherence and clarity
* Factual accuracy
* Introduction of key concepts
* Suitability for educational use

While the original FineWeb-Edu used a classifier trained on Llama-3 annotations, this dataset was scored directly using the **[Qwen/Qwen3-Next-80B-A3B](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Thinking)** model. Documents that met a high-quality threshold (e.g., a score of 3.0 or higher) were retained.

### Scoring Prompt

```text
Below is an extract from a web page... [See full prompt in the Korean section or original source]

```

## Data Fields

* **`text`** (string): The text content of the document.
* **`score`** (int): The educational score (0-5) assigned by the `Qwen3-next-80b-a3b` model.

## Usage

You can load the dataset using the Hugging Face `datasets` library:

```python
from datasets import load_dataset

dataset = load_dataset("eliceai/korean-webtext-edu")

```

---

## License

This dataset is licensed under the MIT License.

## Citation

If you use this dataset, please cite both this dataset and the original HAERAE-HUB/KOREAN-WEBTEXT dataset.

```bibtex
@misc{korean-webtext-edu,
  author = {Elice Group},
  title = {Korean Webtext Edu},
  year = {2025},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/eliceai/korean-webtext-edu}}
}

@misc{korean-webtext,
  author = {HAERAE HUB},
  title = {KOREAN-WEBTEXT},
  year = {2024},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/HAERAE-HUB/KOREAN-WEBTEXT}}
}
```