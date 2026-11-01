---
license: mit
task_categories:
  - question-answering
  - text-generation
language:
  - ko
  - en
tags:
  - buddhism
  - religion
  - philosophy
  - meditation
  - korean
  - english
  - agama-sutra
  - qa
  - dialogue
  - multilingual
size_categories:
  - 100<n<1K
pretty_name: "장아함경 Buddha QA Dataset / Agama Sutra Buddha QA Dataset"
---

# 장아함경 Buddha QA Dataset (Complete) / Agama Sutra Buddha QA Dataset

*[한국어 설명](#한국어) | [English Description](#english)*

---

## 한국어

### 🙏 개요

이 데이터셋은 **장아함경(長阿含經) 제1-3권** 전체를 기반으로 생성된 한국어 불교 질문-답변 데이터셋입니다. GPT-4.1-2025-04-14 모델과 고급 추론 시스템(fill_thinking.py)을 사용하여 생성되었으며, 현대인이 이해하기 쉽도록 해석된 붓다의 가르침을 포함합니다.

### 📊 데이터셋 통계

- **총 QA 쌍**: 335개
- **훈련 데이터**: 268개 (80%)
- **검증 데이터**: 67개 (20%)
- **출처**: 장아함경 제1-3권 (총 70개 경전)
- **생성 모델**: GPT-4.1-2025-04-14
- **추론 시스템**: fill_thinking.py 기반

### 🔧 데이터 형식

각 레코드는 다음과 같은 3-message 구조를 가집니다:

```json
{
  "messages": [
    {
      "role": "system",
      "content": "reasoning language: English\n\n불교 교사로서의 시스템 프롬프트",
      "thinking": null
    },
    {
      "role": "user", 
      "content": "사용자의 질문",
      "thinking": null
    },
    {
      "role": "assistant",
      "content": "AI의 답변 (출처 포함)",
      "thinking": "영어로 된 추론 과정과 한자 용어집"
    }
  ]
}
```

### 🚀 사용 예시

```python
from datasets import load_dataset

# 데이터셋 로드
dataset = load_dataset("LeBrony/buddha_oss_dataset")

# 예시 확인
for example in dataset["train"]:
    print("질문:", example["messages"][1]["content"])
    print("답변:", example["messages"][2]["content"])
    print("추론:", example["messages"][2]["thinking"])
    print("=" * 50)
    break
```

### ✨ 주요 특징

#### 🎯 품질 보장
- **출처 기반**: 실제 경전 내용을 바탕으로 생성
- **고급 추론**: fill_thinking.py 시스템으로 품질 관리
- **영어 추론**: reasoning language를 English로 설정하여 일관성 보장

#### 📖 현대적 해석
- **이해하기 쉬운 설명**: 고전 불교 개념을 현대인에게 친화적으로 설명
- **실생활 적용**: 구체적인 실천 방법과 성찰 질문 포함
- **한자 용어집**: thinking 필드에 한자 용어의 정확한 한국어 해석

#### 🔬 기술적 특징
- **3-message 형식**: ChatML 호환 대화 구조
- **thinking 필드**: 추론 과정과 용어집 자동 생성
- **배치 처리**: 17개 배치로 나누어 안정적 생성
- **품질 검증**: 각 QA 쌍의 정확성과 유용성 검증

### 📚 포함된 경전

#### 제1권 (23개 경)
- 무상경(無常經) - 무상함의 가르침
- 정사유경(正思惟經) - 바른 사유의 방법  
- 무지경(無知經) - 무지와 해탈의 관계
- 염리경(厭離經) - 집착을 떠나는 방법
- 과거무상경(過去無常經) - 과거와 현재의 무상함
- 기타 18개 경전

#### 제2권 (22개 경)
- 다양한 불교 교리와 실천법
- 수행법과 명상 지침
- 일상생활 속 불교 적용

#### 제3권 (25개 경)
- 고급 불교 철학
- 해탈과 깨달음의 길
- 현대적 해석과 적용

### 📋 활용 분야

#### 🤖 AI 모델 훈련
- 한국어 불교 AI 어시스턴트 개발
- 종교/철학 도메인 특화 모델
- 대화형 명상 가이드 시스템

#### 📚 교육 및 연구
- 불교학 연구 자료
- 현대 불교 교육 콘텐츠
- 디지털 법문 시스템

#### 💡 실생활 적용
- 개인 수행 가이드
- 스트레스 관리 도구
- 마음챙김 앱 개발

---

## English

### 🙏 Overview

This dataset is a Korean Buddhist question-answering dataset generated from the complete **Agama Sutras (長阿含經) Volumes 1-3**. It was created using the GPT-4.1-2025-04-14 model and an advanced reasoning system (fill_thinking.py), containing Buddha's teachings interpreted for modern practitioners.

### 📊 Dataset Statistics

- **Total QA pairs**: 335
- **Training data**: 268 (80%)
- **Validation data**: 67 (20%)
- **Source**: Agama Sutras Volumes 1-3 (70 sutras total)
- **Generation model**: GPT-4.1-2025-04-14
- **Reasoning system**: fill_thinking.py based

### 🔧 Data Format

Each record follows a 3-message conversation structure:

```json
{
  "messages": [
    {
      "role": "system",
      "content": "reasoning language: English\n\nBuddhist teacher system prompt",
      "thinking": null
    },
    {
      "role": "user", 
      "content": "User's question in Korean",
      "thinking": null
    },
    {
      "role": "assistant",
      "content": "AI response with sources (in Korean)",
      "thinking": "English reasoning process and Chinese term glossary"
    }
  ]
}
```

### 🚀 Usage Example

```python
from datasets import load_dataset

# Load dataset
dataset = load_dataset("LeBrony/buddha_oss_dataset")

# Examine examples
for example in dataset["train"]:
    print("Question:", example["messages"][1]["content"])
    print("Answer:", example["messages"][2]["content"])
    print("Reasoning:", example["messages"][2]["thinking"])
    print("=" * 50)
    break
```

### ✨ Key Features

#### 🎯 Quality Assurance
- **Source-based**: Generated from authentic sutra texts
- **Advanced reasoning**: Quality control through fill_thinking.py system
- **English reasoning**: Consistent quality through English reasoning language setting

#### 📖 Modern Interpretation
- **Accessible explanations**: Classical Buddhist concepts explained for modern practitioners
- **Practical application**: Specific practice methods and reflection questions
- **Chinese term glossary**: Accurate Korean interpretations of Chinese terms in thinking field

#### 🔬 Technical Features
- **3-message format**: ChatML-compatible conversation structure
- **Thinking field**: Automatic generation of reasoning processes and glossaries
- **Batch processing**: Stable generation through 17 batches
- **Quality verification**: Accuracy and usefulness verification for each QA pair

### 📚 Included Sutras

#### Volume 1 (23 sutras)
- Anicca Sutra (無常經) - Teachings on impermanence
- Right Contemplation Sutra (正思惟經) - Methods of right thinking
- Ignorance Sutra (無知經) - Relationship between ignorance and liberation
- Renunciation Sutra (厭離經) - Methods of letting go of attachments
- Past Impermanence Sutra (過去無常經) - Impermanence of past and present
- 18 additional sutras

#### Volume 2 (22 sutras)
- Various Buddhist doctrines and practices
- Meditation methods and guidance
- Application of Buddhism in daily life

#### Volume 3 (25 sutras)
- Advanced Buddhist philosophy
- Paths to liberation and enlightenment
- Modern interpretations and applications

### 📋 Use Cases

#### 🤖 AI Model Training
- Korean Buddhist AI assistant development
- Religion/philosophy domain-specific models
- Interactive meditation guide systems

#### 📚 Education and Research
- Buddhist studies research materials
- Modern Buddhist educational content
- Digital dharma talk systems

#### 💡 Practical Applications
- Personal practice guides
- Stress management tools
- Mindfulness app development

---

## 🔍 품질 관리 / Quality Control

### 데이터 생성 과정 / Data Generation Process
1. **경전 파싱 / Sutra Parsing**: 장아함경 1-3권을 경별로 분할 / Dividing Agama Sutras 1-3 by individual sutras
2. **질문 생성 / Question Generation**: 각 경전에서 핵심 개념 추출 후 질문 생성 / Extracting key concepts from each sutra and generating questions
3. **답변 생성 / Answer Generation**: 경전 내용 기반으로 정확한 답변 작성 / Writing accurate answers based on sutra content
4. **추론 추가 / Reasoning Addition**: fill_thinking.py로 사고 과정과 용어집 생성 / Generating thought processes and glossaries with fill_thinking.py
5. **품질 검증 / Quality Verification**: 각 QA 쌍의 정확성과 유용성 확인 / Verifying accuracy and usefulness of each QA pair

### 데이터 품질 기준 / Data Quality Standards
- ✅ 경전 원문에 기반한 정확한 내용 / Accurate content based on original sutras
- ✅ 현대인이 이해하기 쉬운 설명 / Explanations accessible to modern practitioners
- ✅ 실생활 적용 가능한 실천 방법 / Practical methods applicable to daily life
- ✅ 깊이 있는 성찰 질문 포함 / Inclusion of deep reflection questions
- ✅ 한자 용어의 정확한 해석 / Accurate interpretation of Chinese terms

## 📜 라이선스 / License

MIT License - 자유롭게 사용, 수정, 배포 가능 / Free to use, modify, and distribute

## 🤝 기여 / Contributing

이 데이터셋은 불교 AI 연구와 교육 목적으로 제작되었습니다. / This dataset was created for Buddhist AI research and educational purposes.

### 문의 및 개선 제안 / Inquiries and Improvement Suggestions
- GitHub Issues를 통한 피드백 / Feedback through GitHub Issues
- 데이터 품질 개선 제안 / Data quality improvement suggestions
- 새로운 경전 추가 요청 / Requests for additional sutras

## 🛠 기술 세부사항 / Technical Details

- **생성 모델 / Generation Model**: GPT-4.1-2025-04-14
- **추론 언어 / Reasoning Language**: English (품질 일관성을 위한 설정 / Set for quality consistency)
- **출처 경전 / Source Sutras**: 장아함경 제1-3권 (총 70개 경전) / Agama Sutras Volumes 1-3 (70 sutras total)
- **데이터 형식 / Data Format**: 3-message conversation format (ChatML 호환 / ChatML compatible)
- **추론 시스템 / Reasoning System**: fill_thinking.py 기반 고급 추론 / Advanced reasoning based on fill_thinking.py
- **배치 크기 / Batch Size**: 20개 QA 쌍/배치 (총 17배치) / 20 QA pairs/batch (17 batches total)
- **생성 시간 / Generation Time**: 약 2시간 9분 / Approximately 2 hours 9 minutes

## 📈 업데이트 기록 / Update History

- **v2.0** (현재 / Current): 장아함경 1-3권 전체 (335개 QA) / Complete Agama Sutras 1-3 (335 QAs)
  - 17개 배치로 분할 생성 / Generated in 17 batches
  - fill_thinking.py 고급 추론 시스템 적용 / Applied fill_thinking.py advanced reasoning system
  - 한자 용어집 자동 생성 / Automatic generation of Chinese term glossaries
  - 품질 관리 강화 / Enhanced quality control

- **v1.0**: 초기 테스트 버전 (20개 QA) / Initial test version (20 QAs)

## 🙏 감사의 말 / Acknowledgments

이 데이터셋은 부처님의 가르침을 현대에 전하고자 하는 마음으로 제작되었습니다. 모든 중생이 괴로움에서 벗어나 행복을 얻기를 발원합니다. / This dataset was created with the intention of transmitting Buddha's teachings to the modern world. May all beings be free from suffering and attain happiness.

_"모든 형성된 것들은 무상하다. 정진하라." / "All conditioned things are impermanent. Strive diligently."_ - 부처님의 마지막 말씀 / Buddha's last words

## 📊 Citation

```bibtex
@dataset{jangaham_buddha_qa_2025,
  title={장아함경 Buddha QA Dataset},
  author={LeBrony},
  year={2025},
  url={https://huggingface.co/datasets/LeBrony/buddha_oss_dataset},
  note={Korean Buddhist Q&A dataset based on Agama Sutras volumes 1-3}
}
```

---

**Repository**: [https://huggingface.co/datasets/LeBrony/buddha_oss_dataset](https://huggingface.co/datasets/LeBrony/buddha_oss_dataset)
