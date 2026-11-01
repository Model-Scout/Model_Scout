---
dataset_info:
  features:
  - name: title
    dtype: string
  - name: content
    dtype: string
  - name: date
    dtype: string
  - name: category
    dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 406481.1590909091
    num_examples: 503
  download_size: 240548
  dataset_size: 406481.1590909091
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: cc-by-nc-sa-4.0
language:
- ko
---

# **Dataset Card for 한국어 밈 설명 데이터셋 (KoCulture-Descriptions)**

This dataset card provides a comprehensive overview of the KoCulture-Descriptions Dataset, created by Hugging Face KREW. This dataset is a companion to KoCulture-Dialogues, focusing on detailed explanations rather than conversational examples.

### **Dataset Details**

- **Dataset Description:** 본 데이터셋은 최신 한국어 신조어, 유행어, 밈 및 관련 문화 현상에 대한 **상세한 설명**을 제공하여 대형 언어 모델(LLM)의 한국어 이해 및 생성 능력을 심층적으로 향상시키기 위해 구축되었습니다. 각 용어의 정의, 유래, 사용 방식, 문화적 맥락 등을 포함합니다. 나무위키와 트렌드어워드 등에서 수집한 원시 자료를 바탕으로 여러 LLM(Claude Sonnet 3.7, Gpt-4o, Gemini 2.5 등)을 활용해 초기 설명을 생성한 후, Hugging Face KREW 참여자들이 직접 검수하고 정제했습니다.
- **Curated by:** Hugging Face KREW (참여자: 유용상 (Yongsang Yoo), 김하림 (Harheem Kim), 오성민 (Sungmin Oh))
- **Shared by:** Hugging Face KREW
- **Language(s) (NLP):** 한국어 (Korean)
- **License:** CC BY-NC-SA 4.0 International (이 라이선스는 원본 데이터 중 하나인 나무위키의 라이선스 조건(CC BY-NC-SA)을 반영하며, 비영리적 사용과 동일조건변경허락을 주요 조건으로 합니다. 트렌드어워드 데이터의 포함은 해당 출처의 이용 약관을 준수했음을 전제합니다.)
- **Dataset Sources:**
    - **Repository:** https://huggingface.co/datasets/huggingface-KREW/KoCulture-Descriptions

### **Uses**

- **Direct Use:**
    - 대형 언어 모델(LLM)의 한국어 신조어 및 문화적 맥락에 대한 **심층 이해** 능력 강화
    - 한국어 신조어, 유행어, 밈 관련 정보 검색 및 요약 시스템 개발
    - 문화 해설, 교육용 콘텐츠 생성 등 한국어 기반 AI 서비스의 정보 제공 능력 향상
    - 한국어 어휘 및 문화 변천 과정 연구를 위한 상세 자료 제공
- **Out-of-Scope Use:**
    - 본 데이터셋은 CC BY-NC-SA 4.0 라이선스에 따라 영리적 목적으로 사용될 수 없습니다.
    - 데이터셋에 포함된 유해성 판별 기준에 따라, 유해하거나 차별적인 콘텐츠(공격적 언어, 특정 대상 공격, 차별적 속성 기반 공격 등)를 생성하거나 확산하는 데 사용되어서는 안 됩니다.
    - 원본 데이터 출처의 저작권을 침해하는 방식으로 사용되어서는 안 됩니다.

### **Dataset Structure**

본 데이터셋은 각 한국어 신조어 및 문화 용어에 대한 상세 정보를 담고 있는 항목들로 구성됩니다. 각 항목은 다음 필드를 포함합니다:

- `title` (String):
    - **설명:** 핵심이 되는 유행어, 밈 또는 문화 용어의 명칭입니다.
    - **타입:** 문자열 (String).
    - **특징:** 텍스트 길이는 최소 1자에서 최대 57자 사이입니다. (예시 데이터 기준)
    - **예시:** "원영적 사고", "말아주다", "기습숭배", "할매니얼", "비질게"
- `content` (String):
    - **설명:** `title`에 해당하는 용어의 정의, 유래, 의미 변화, 사용 예시, 관련 문화적 배경 등 상세한 설명을 포함하는 주요 텍스트 필드입니다.
    - **타입:** 문자열 (String).
- `date` (String):
    - **설명:** 해당 용어가 중요하게 언급되거나, 관련 사건 발생일, 또는 자료 작성/수집 기준일입니다.
    - **타입:** 문자열 (String).
    - **특징:** "YYYY.MM.DD" 혹은 "YYYY" 형식을 따릅니다. (길이가 0인 경우 정보가 없는 경우입니다.)
    - **예시:** "2024.04.18", "2023.05.18", "2020"
- `category` (String):
    - **설명:** 용어의 분류를 나타냅니다.
    - **타입:** 문자열 (String).
    - **예시:** "meme", "trend"
        - meme: 일상 대화에서 자연스럽게 사용되는 유행 표현이나 개념
        - trend: 특정 시기에 유행하는 숏폼 콘텐츠, 짤방, 챌린지 등 대화형 텍스트에 녹여내기 어려운 현상
- `source` (String):
    - **설명:** 해당 설명의 원본 정보 출처 또는 주로 참고한 플랫폼을 나타냅니다.
    - **타입:** 문자열 (String).
    - **예시:** "trendaword", "namuwiki"

### **Dataset Creation**

- **Curation Rationale:**
대부분의 대형 언어 모델(LLM)은 주로 영어 중심으로 학습되어 한국어 데이터 및 문화적 맥락에 대한 **깊이 있는 이해**가 부족합니다. 본 프로젝트는 한국어의 독특한 특성, 특히 시시각각 변화하는 신조어와 유행어 및 그 배경에 대한 **상세하고 구조화된 설명**을 담은 고품질 데이터셋을 제작하여 한국어 LLM의 성능 개선 및 정보 제공 능력 강화에 기여하는 것을 목표로 합니다. 이러한 설명 데이터는 단순한 용어 사용 예시를 넘어, 용어의 생성 배경과 문화적 함의까지 전달하여 모델이 보다 풍부한 맥락을 학습할 수 있도록 돕습니다.
- **Source Data:**
    - **Data Collection and Processing:**
        - [TrendAward](https://maily.so/trendaword): 웹사이트의 텍스트 콘텐츠와 카드뉴스 형태의 이미지 내 텍스트를 OCR(광학 문자 인식) 기술을 활용하여 수집했습니다.
        - [Namuwiki](https://namu.wiki/): '국내밈/해외밈/유행어' 관련 문서들의 제목, 개요, 본문 내 주요 정보를 스크립트를 통해 수집했습니다.
        - 상기 수집된 원시 자료 및 주제를 기반으로, **Claude Sonnet 3.7, Gpt-4o, Gemini 2.5 등**의 LLM을 활용하여 각 용어에 대한 초기 **설명문 초안**을 생성했습니다.
        - 이후 프로젝트 참여자들이 직접 각 설명문을 검토하고, 사실 관계를 확인하며 내용을 수정, 보완하고 부적절한 부분을 제거하는 정제 작업을 수행했습니다.
        - 구체적인 프롬프트와 각 파생물들은 이 레포지토리에서 확인하실 수 있습니다. (코드 및 프롬프트 자료 업데이트 예정)

### **Personal and Sensitive Information**

본 데이터셋은 개인을 식별할 수 있는 정보(PII)나 민감 정보를 포함하지 않도록 노력했습니다. 데이터 수집 및 정제 과정에서 다음과 같은 유해성 판별 기준을 적용하여 관련 내용을 제거하거나 수정했습니다:

- **유해성 발화 정의:**
    - 공격적 언어 사용: 욕설, 모욕, 비하, 위협 등의 표현.
    - 특정 대상의 공격: 개인이나 특정 집단을 겨냥한 모욕 및 공격.
    - 차별적 속성 기반 공격: 인종, 성별, 성적 지향, 종교, 연령, 장애 등 사회적 차별 요소를 기반으로 한 공격 (혐오 발언으로 간주).
    - 맥락적 이해 중요: 언어의 문자적 의미뿐만 아니라 사용 맥락을 고려하여 유해성 여부를 판단.
    - 암시적 표현 포함: 명시적 욕설 외에도 암시적이고 우회적인 표현 역시 유해 발언으로 간주.
    - 편견과 혐오의 연관성: 사회적 편견과 혐오 발언 간의 밀접한 연관성을 고려.
- **PII 제거 노력:**
수집된 데이터에서 이름, 전화번호, 주소, 이메일 주소 등 명백한 개인 식별 정보는 검토 과정에서 제거되었습니다. 그러나 웹에서 수집된 데이터의 특성상, 공개적으로 사용되는 닉네임이나 간접적으로 유추될 수 있는 정보가 미량 포함될 가능성은 배제할 수 없습니다. 발견 시 보고해주시면 수정하겠습니다.

### **Bias, Risks, and Limitations**

- **Bias:**
    - 본 데이터셋은 주로 온라인 커뮤니티와 미디어에서 유래된 신조어 및 유행어를 중심으로 구성되어 있어, 특정 연령대(예: 젊은 세대)나 특정 온라인 문화에 편향된 언어 사용 및 관점을 반영할 수 있습니다.
    - 설명 내용은 객관성을 지향했으나, 원본 자료의 편향이나 큐레이터의 주관이 일부 반영될 수 있으며, 유해성 판별 기준을 적용했음에도 민감할 수 있는 내용이 미처 필터링되지 못했을 가능성이 있습니다.
- **Risks:**
    - 신조어와 유행어는 시의성이 매우 강하여 시간이 지남에 따라 의미가 변하거나 사용되지 않게 될 수 있습니다(데이터 노후화).
    - 필터링 노력에도 불구하고, 맥락에 따라 부적절하거나 공격적으로 해석될 수 있는 내용이 포함될 위험이 있습니다.
- **Limitations:**
    - 본 데이터셋은 한국어 신조어 및 문화 현상의 전체 범위를 포괄하지 못하며, 특정 시점까지 수집된 내용을 기반으로 합니다.
    - 제공되는 설명의 깊이나 관점이 모든 사용자를 만족시키지 못할 수 있습니다.
    - 데이터셋의 크기는 약 **500개**로, 모든 종류의 LLM 학습이나 연구에 충분하지 않을 수 있습니다.

### **Recommendations**

- 사용자는 본 데이터셋을 CC BY-NC-SA 4.0 라이선스 조건에 따라 비영리 목적으로만 사용하고, 출처(Hugging Face KREW 및 원본 데이터 제공처)를 명확히 밝혀야 합니다.
- 신조어 및 유행어의 시의성을 고려하여, 최신 트렌드를 반영하기 위해서는 주기적인 업데이트나 추가 데이터 수집이 필요할 수 있습니다.
- 데이터셋 사용 시 발생할 수 있는 편향이나 민감한 내용에 대해 인지하고 주의 깊게 사용해야 합니다.
- 데이터셋의 개선을 위한 피드백이나 오류 보고는 언제나 환영합니다. ([Dataset Card Contact 정보 참조])

### **Citation**

- **BibTeX:**

```
@misc{huggingface_krew_koculture_descriptions_2025,
  title={{한국어 밈 설명 데이터셋 (KoCulture-Descriptions Dataset)}},
  author={{Hugging Face KREW} and Yoo, Yongsang and Kim, Harheem and Oh, Sungmin},
  year={2025}, 
  publisher={Hugging Face KREW},
  howpublished={\url{https://huggingface.co/datasets/huggingface-KREW/KoCulture-Descriptions}} 
}
```

- APA:
    
    Hugging Face KREW, Yoo, Y., Kim, H., & Oh, S. (2025). 한국어 밈 설명 데이터셋 (KoCulture-Descriptions Dataset). Hugging Face KREW. Retrieved from https://huggingface.co/datasets/huggingface-KREW/KoCulture-Descriptions
    

### **More Information**

- **Hugging Face KREW 커뮤니티:** `https://discord.gg/bKh5M7xsXP`
- **프로젝트 관련 자료:** `https://github.com/Pseudo-Lab/Hugging-Face-Hub-Garden`

### **Dataset Card Authors**

- 유용상 (Yongsang Yoo)
- 김하림 (Harheem Kim)
- 오성민 (Sungmin Oh)

### **Dataset Card Contact**

- `https://github.com/Pseudo-Lab/Hugging-Face-Hub-Garden/issues`