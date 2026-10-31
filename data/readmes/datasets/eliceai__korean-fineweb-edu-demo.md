---
license: apache-2.0
task_categories:
- text-generation
language:
- ko
tags:
- korean
- education
- fineweb
- text
size_categories:
- 10M<n<100M
---

# Korean FineWeb-Edu Demo

이 데이터셋은 [eliceai/korean-translated-fineweb-edu-dedup](https://huggingface.co/datasets/eliceai/korean-translated-fineweb-edu-dedup)의 샘플링 버전(약 30GB, 5%)으로, 고품질 교육용 한국어 데이터를 제공합니다.

---

## 한국어

### 데이터셋 설명
**Korean FineWeb-Edu Demo**는 영문 교육용 웹 텍스트 코퍼스인 *FineWeb-Edu*를 한국어로 번역한 데이터셋인 *korean-translated-fineweb-edu-dedup* 의 5% 샘플 데모입니다. 거대 언어 모델(LLM)이 학술적이고 교육적인 도메인에서 한국어 성능을 높일 수 있도록 설계되었습니다.

### 데이터 생성 및 번역 공정
본 데이터셋은 **Qwen/Qwen3-Next-80B-A3B-Instruct** 모델을 사용하여 번역되었으며, 아래와 같은 가이드라인을 준수했습니다.

#### 1. 번역 원칙
* **의미 보존**: 원문의 의도, 뉘앙스, 의도를 누락하거나 수정하지 않고 충실하게 번역합니다.
* **코드 보존**: Python, JSON, Bash 등 모든 코드 스니펫과 인라인 코드는 수정이나 재포맷 없이 그대로 유지합니다. 오직 주석과 설명 텍스트만 번역합니다.
* **형식 유지**: 마크다운 서식, 리스트 구조, 줄바꿈을 원문과 동일하게 유지합니다.

#### 2. 세부 처리 규칙
| 항목 | 처리 방법 | 예시 |
| :--- | :--- | :--- |
| **고유 명사** | 인지도가 높으면 영어 유지, 필요시 첫 언급에 한글 병기 | John Smith (존 스미스) |
| **연도/날짜** | 아라비아 숫자 유지, 한국어 조사 추가 | in 2021 → 2021년에 |
| **약어/학술어** | 영어 유지, 첫 언급 시 한국어 확장 설명 추가 | LLM (대형 언어 모델) |
| **단위** | 숫자는 유지, 단위명은 한국어 번역 | 5 km → 5킬로미터 |
| **기술 용어** | 표준 한국어 용어 사용, 생소한 경우 영어 병기 | Tokenization → 토큰화 |
| **인용/제목** | 의미 번역 후 원문을 괄호 안에 병기 | "Deep Learning" → "딥러닝" |
| **화폐** | 기호와 수치 유지, 단위명 번역 | $10 → 10달러 |

#### 3. 번역 시 사용된 프롬프트

```
You are a professional English–Korean translator specializing in technical, academic, and programming-related texts.  
Your task is to translate the given text from English to natural, fluent Korean **without changing, adding, or omitting any meaning, nuance, or intent** of the original.

If the input contains code (e.g., Python, JSON, Bash, or inline code), **do not translate, modify, or reformat the code in any way**.  
Only translate the surrounding English text and comments, keeping all code, indentation, and structure identical.

---

### Translation Guidelines

1. **Preserve Meaning Exactly**
   - Translate every sentence faithfully and precisely.  
   - Do not summarize, reinterpret, or skip any content.  
   - The translated Korean text must fully retain the author's original intent.

2. **Code Handling**
   - Leave all code snippets, inline code, and syntax unchanged.  
   - Translate only natural language around or inside comments/docstrings.  
   - Keep indentation, formatting, and symbols intact.

3. **Style and Tone**
   - Maintain the same tone and formality level (academic, technical, etc.).  
   - Use fluent, idiomatic Korean appropriate for native readers.  
   - Avoid literal or awkward phrasing.

4. **Formatting**
   - Preserve markdown, list structures, and paragraph breaks.  
   - Keep inline code within backticks (`) unmodified.

---

### Translation Notes Rules (for internal reference)

Follow these rules silently; **do not include them in the output.**

- Keep proper names (people, places, organizations) in English if well-known; otherwise, transliterate in parentheses on first mention.  
- Keep abbreviations/acronyms in English; add Korean expansion on first mention if relevant.  
- Keep years, dates, and numbers in Arabic numerals.  
- Preserve units and symbols; translate only the unit name (e.g., 5 km → 5킬로미터).  
- Translate technical terms using standard Korean equivalents; if none exist, provide transliteration + English on first use.  
- Translate book/article titles, but retain original in parentheses.  
- For idioms or culture-specific phrases, translate meaning, not literal form.  
- Keep currency symbols and numeric values; convert unit name where appropriate.  

---

### Special Handling Rules (for internal reference)

| Category | How to Handle | Example |
|-----------|---------------|----------|
| Proper Names | Keep English if globally recognized; otherwise, transliterate once. | John Smith (존 스미스) |
| Years/Dates | Keep Arabic numerals, add Korean suffix when natural. | in 2021 → 2021년에 |
| Abbreviations | Keep English, add Korean expansion on first mention. | LLM (대형 언어 모델, Large Language Model) |
| Units | Preserve Arabic numerals; translate unit names. | 5 km → 5킬로미터 |
| Technical Terms | Use standard Korean; otherwise, add English in parentheses. | Tokenization → 토큰화 (Tokenization) |
| Quotes/Titles | Translate meaning; keep English in parentheses. | "Deep Learning Revolution" → "딥러닝 혁명(Deep Learning Revolution)" |
| Idioms | Translate meaning naturally; clarify if ambiguous. | "kick the bucket" → "죽다" (idiom meaning "to die") |
| Currency | Keep symbol and convert unit name. | $10 → 10달러 |

---

### Output Format

Return **only** the final translated text enclosed in XML tags:

<translated>
[Final Korean translation here, with all code unchanged]
</translated>

Do **not** include explanations, reasoning, or notes outside the <translated>...</translated> block.

### Input Text:
{input_text}
```

### 데이터 구성
* **소스**: [HuggingFaceTB/smollm-corpus](https://huggingface.co/datasets/HuggingFaceTB/smollm-corpus)의 *FineWeb-Edu*
* **구조**: `text` (string) 피처를 가진 단일 `train` split.
* **샘플링**: 약 600GB 원본 데이터에서 스트리밍 방식으로 5%를 추출.

### 사용 방법
```python
from datasets import load_dataset

dataset = load_dataset("eliceai/korean-fineweb-edu-demo", split="train")
print(dataset[0]["text"])

```

### 라이선스 및 인용

본 데이터셋은 **MIT License**를 따릅니다.

```bibtex
@misc{korean_fineweb_edu_demo,
  author = {Elice Group},
  title = {Korean FineWeb-Edu Demo},
  year = {2025},
  url = {[https://huggingface.co/datasets/eliceai/korean-fineweb-edu-demo](https://huggingface.co/datasets/eliceai/korean-fineweb-edu-demo)}
}

```

---

## ENGLISH

### Dataset Description

**Korean FineWeb-Edu Demo** is a 30GB sampled subset (~5%) of the [eliceai/korean-translated-fineweb-edu-dedup](https://huggingface.co/datasets/eliceai/korean-translated-fineweb-edu-dedup) dataset. It provides high-quality Korean translations of the *FineWeb-Edu* corpus, specifically curated for training and evaluating LLMs in educational and factual domains.

### Dataset Creation & Translation Process

All texts were translated using the **Qwen/Qwen3-Next-80B-A3B-Instruct** model with the following strict professional guidelines:

#### 1. Translation Guidelines

* **Preserve Meaning Exactly**: No summarization or omission; the Korean text retains the author's original intent and nuance.
* **Code Handling**: All code snippets (Python, JSON, etc.) and inline code remain untouched. Only comments and surrounding natural language are translated.
* **Formatting**: Markdown structures, indentations, and paragraph breaks are strictly preserved.

#### 2. Special Handling Rules

| Category | Strategy | Example |
| --- | --- | --- |
| **Proper Names** | Keep English if recognized; otherwise, transliterate. | John Smith (존 스미스) |
| **Years/Dates** | Keep Arabic numerals; add Korean suffixes. | in 2021 → 2021년에 |
| **Abbreviations** | Keep English; add Korean expansion on 1st use. | LLM (대형 언어 모델) |
| **Units** | Keep numerals; translate unit names. | 5 km → 5 kilometers |
| **Technical Terms** | Use standard Korean; add English in parentheses. | Tokenization → 토큰화 |
| **Titles/Quotes** | Translate meaning; keep original in parentheses. | "Deep Learning" (딥러닝) |
| **Currency** | Keep symbols and numeric values. | $10 → 10 dollars |

#### 3. Translation Prompt

#### 3. 번역 시 사용된 프롬프트

```
You are a professional English–Korean translator specializing in technical, academic, and programming-related texts.  
Your task is to translate the given text from English to natural, fluent Korean **without changing, adding, or omitting any meaning, nuance, or intent** of the original.

If the input contains code (e.g., Python, JSON, Bash, or inline code), **do not translate, modify, or reformat the code in any way**.  
Only translate the surrounding English text and comments, keeping all code, indentation, and structure identical.

---

### Translation Guidelines

1. **Preserve Meaning Exactly**
   - Translate every sentence faithfully and precisely.  
   - Do not summarize, reinterpret, or skip any content.  
   - The translated Korean text must fully retain the author's original intent.

2. **Code Handling**
   - Leave all code snippets, inline code, and syntax unchanged.  
   - Translate only natural language around or inside comments/docstrings.  
   - Keep indentation, formatting, and symbols intact.

3. **Style and Tone**
   - Maintain the same tone and formality level (academic, technical, etc.).  
   - Use fluent, idiomatic Korean appropriate for native readers.  
   - Avoid literal or awkward phrasing.

4. **Formatting**
   - Preserve markdown, list structures, and paragraph breaks.  
   - Keep inline code within backticks (`) unmodified.

---

### Translation Notes Rules (for internal reference)

Follow these rules silently; **do not include them in the output.**

- Keep proper names (people, places, organizations) in English if well-known; otherwise, transliterate in parentheses on first mention.  
- Keep abbreviations/acronyms in English; add Korean expansion on first mention if relevant.  
- Keep years, dates, and numbers in Arabic numerals.  
- Preserve units and symbols; translate only the unit name (e.g., 5 km → 5킬로미터).  
- Translate technical terms using standard Korean equivalents; if none exist, provide transliteration + English on first use.  
- Translate book/article titles, but retain original in parentheses.  
- For idioms or culture-specific phrases, translate meaning, not literal form.  
- Keep currency symbols and numeric values; convert unit name where appropriate.  

---

### Special Handling Rules (for internal reference)

| Category | How to Handle | Example |
|-----------|---------------|----------|
| Proper Names | Keep English if globally recognized; otherwise, transliterate once. | John Smith (존 스미스) |
| Years/Dates | Keep Arabic numerals, add Korean suffix when natural. | in 2021 → 2021년에 |
| Abbreviations | Keep English, add Korean expansion on first mention. | LLM (대형 언어 모델, Large Language Model) |
| Units | Preserve Arabic numerals; translate unit names. | 5 km → 5킬로미터 |
| Technical Terms | Use standard Korean; otherwise, add English in parentheses. | Tokenization → 토큰화 (Tokenization) |
| Quotes/Titles | Translate meaning; keep English in parentheses. | "Deep Learning Revolution" → "딥러닝 혁명(Deep Learning Revolution)" |
| Idioms | Translate meaning naturally; clarify if ambiguous. | "kick the bucket" → "죽다" (idiom meaning "to die") |
| Currency | Keep symbol and convert unit name. | $10 → 10달러 |

---

### Output Format

Return **only** the final translated text enclosed in XML tags:

<translated>
[Final Korean translation here, with all code unchanged]
</translated>

Do **not** include explanations, reasoning, or notes outside the <translated>...</translated> block.

### Input Text:
{input_text}
```

### Dataset Structure

* **Source**: *FineWeb-Edu* subset of [HuggingFaceTB/smollm-corpus](https://huggingface.co/datasets/HuggingFaceTB/smollm-corpus).
* **Features**: `text` (string).
* **Sampling**: 5% of the 600GB source dataset via streaming mode.

### Usage

```python
from datasets import load_dataset

dataset = load_dataset("eliceai/korean-fineweb-edu-demo", split="train")
print(dataset[0]["text"])

```

### License & Citation

This dataset is released under the **MIT License**.

```bibtex
@misc{korean_fineweb_edu_demo,
  author = {Elice Group},
  title = {Korean FineWeb-Edu Demo},
  year = {2025},
  url = {[https://huggingface.co/datasets/eliceai/korean-fineweb-edu-demo](https://huggingface.co/datasets/eliceai/korean-fineweb-edu-demo)}
}
```