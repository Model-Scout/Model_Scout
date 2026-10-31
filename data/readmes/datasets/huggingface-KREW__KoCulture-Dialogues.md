---
dataset_info:
  features:
  - name: title
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 903842
    num_examples: 3456
  download_size: 540922
  dataset_size: 903842
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: cc-by-nc-sa-4.0
language:
- ko
tags:
- text-generation
---

## **Dataset Card for 한국어 신조어 대화 데이터셋 (Korean Neologism Dialogues Dataset)**

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6502be90a33ce3ae28727396/8v1tOSMzKI9EuQhvybuRw.png)

This dataset card provides a comprehensive overview of the Korean Neologism Dataset, created by Hugging Face KREW.

### **Dataset Details**

- **Dataset Description:** 본 데이터셋은 최신 한국어 신조어, 유행어, 밈을 포함하여 대형 언어 모델(LLM)의 한국어 이해 및 생성 능력을 향상시키기 위해 구축되었습니다. 나무위키와 트렌드어워드 등에서 수집한 원시 자료를 바탕으로 여러 LLM을 활용해 초기 데이터를 생성한 후, Hugging Face KREW 참여자들이 직접 검수하고 정제했습니다.
- **Curated by:** Hugging Face KREW (참여자: 유용상 (Yongsang Yoo), 김하림 (Harheem Kim), 오성민 (Sungmin Oh))
- **Shared by:** Hugging Face KREW
- **Language(s) (NLP):** 한국어 (Korean)
- **License:** **CC BY-NC-SA 4.0 International** (이 라이선스는 원본 데이터 중 하나인 나무위키의 라이선스 조건(CC BY-NC-SA)을 반영하며, 비영리적 사용과 동일조건변경허락을 주요 조건으로 합니다. 트렌드어워드 데이터의 포함은 해당 출처의 이용 약관을 준수했음을 전제합니다.)
- **Dataset Sources:**
    - **Repository:** [`https://huggingface.co/datasets/huggingface-KREW/KoCulture-Dialogues`](https://huggingface.co/datasets/huggingface-KREW/KoCulture-Dialogues)

### **Uses**

- **Direct Use:**
    - 대형 언어 모델(LLM)의 한국어 학습 데이터 보강 및 성능 개선
    - 한국어 신조어, 유행어, 밈 관련 자연어 이해(NLU) 및 생성(NLG) 연구
    - 챗봇, 가상 비서 등 한국어 기반 AI 서비스의 표현력 및 사용자 경험 향상
    - 한국어 언어 자원 구축 및 언어 변화 연구
- **Out-of-Scope Use:**
    - 본 데이터셋은 CC BY-NC-SA 4.0 라이선스에 따라 **영리적 목적으로 사용될 수 없습니다.**
    - 데이터셋에 포함된 유해성 판별 기준에 따라, 유해하거나 차별적인 콘텐츠(공격적 언어, 특정 대상 공격, 차별적 속성 기반 공격 등)를 생성하거나 확산하는 데 사용되어서는 안 됩니다.
    - 원본 데이터 출처의 저작권을 침해하는 방식으로 사용되어서는 안 됩니다.

### **Dataset Structure**

본 데이터셋은 **유행어/밈 데이터셋 (Slang/Meme Dataset)** 으로 구성됩니다. 각 데이터 항목은 특정 유행어/밈을 나타내는 `title`, 해당 유행어/밈이 사용될 법한 맥락을 제시하는 `question`, 그리고 그 맥락 안에서 유행어/밈을 포함하여 응답하는 `answer`로 이루어집니다.

- **`title` (String):**
    - **설명:** 핵심이 되는 유행어 또는 밈의 명칭입니다. 이 데이터셋에서 각 유행어나 밈을 대표하는 키워드 역할을 합니다.
    - **타입:** 문자열 (String).
    - **예시:** `"추구미"`, `"어쩔티비"`, `"폼 미쳤다"`
- **`question` (String):**
    - **설명:** `title`에 해당하는 유행어/밈이 자연스럽게 사용될 수 있는 상황이나 대화의 시작 부분을 제시하는 질문 또는 문맥입니다. 사용자가 `answer`에서 해당 유행어를 어떻게 활용하는지 보여주기 위한 배경 역할을 합니다.
    - **타입:** 문자열 (String).
    - **예시 (`title`이 `"추구미"`인 경우):**
        - `"ㅋㅋㅋ 지수야 인스타 스토리 봤는데 또 카페 투어했네?"`
        - `"야 넌 진짜 아무리 술 마셔도 필기 다 하고 수업 다 들어가더라 대단하다 ㄹㅇ"`
        - `"요즘 퇴근하고 뭐해? 갑자기 젤네일 하고 옷 스타일도 바뀌고 무슨일이야"`
- **`answer` (String):**
    - **설명:** `question`에서 제시된 상황이나 질문에 대한 응답으로, `title`에 해당하는 유행어/밈을 핵심적으로 사용하여 그 의미나 뉘앙스, 활용법을 보여주는 내용입니다.
    - **타입:** 문자열 (String).
    - **예시 (`title`이 `"추구미"`이고, 위 `question` 예시들에 각각 대응하는 경우):**
        - `"ㅇㅇ ㅋㅋㅋ 조용한 동네에 작은 로스터리 카페 사장님이 되는 게 내 추구미라... 요즘 열심히 리서치 중"`
        - `"뭔소리야 ㅋㅋㅋㅋ 그냥 내 추구미가 놀때는 놀더라도 학점관리 철저한 대학생인데, 현실은... 어제도 술먹고 수업 출튀했잖아 ㅠㅠ"`
        - `"그냥 이제 좀 꾸미면서 살려고...ㅎㅎ 프렌치 감성 오피스룩이 내 추구미인데 요즘 되게 망가져 있었거든. 너무 우울해서 확 바꿔봄"`

이렇게 세 가지 필드로 구성되며, 각 `title`별로 여러 `question`과 `answer` 쌍이 존재하여 다양한 사용 맥락을 학습할 수 있도록 설계될 수 있습니다.

### **Dataset Creation**

- **Curation Rationale:**
대부분의 대형 언어 모델(LLM)은 주로 영어 중심으로 학습되어 한국어 데이터 및 문화적 맥락에 대한 이해가 부족합니다. 본 프로젝트는 한국어의 독특한 특성, 특히 시시각각 변화하는 신조어와 유행어를 반영하는 고품질 데이터셋을 제작하여 한국어 LLM 성능 개선에 기여하는 것을 목표로 합니다. 신조어는 데이터 수집이 비교적 용이하고, 한국어의 언어적 창의성을 잘 보여주며, 모델 학습 시 사용자에게 흥미롭고 현실적인 경험을 제공할 수 있다는 점에서 주요 주제로 선정되었습니다.
- **Source Data:**
    - **Data Collection and Processing:**
        - `TrendAward`: 웹사이트의 텍스트 콘텐츠와 카드뉴스 형태의 이미지 내 텍스트를 OCR(광학 문자 인식) 기술을 활용하여 수집했습니다. 이미지 OCR 파이프라인을 구축하여 효율성을 높였습니다.
        - `Namuwiki`: '국내밈/해외밈/유행어' 관련 문서들의 제목, 개요, 본문 내 주요 정보를 스크립트를 통해 수집했습니다.
        - 상기 수집된 원시 데이터를 기반으로, Claude Sonnet 3.7, GPT-4o, Gemini 2.5 등을 활용하여 초기 데이터셋 초안을 생성했습니다.
        - 이후 프로젝트 참여자들이 직접 각 항목을 검토, 수정, 보완하고 부적절한 내용을 제거하는 정제 작업을 수행했습니다.
        - 구체적인 프롬프트와 각 파생물들은 이 레포지토리에서 확인하실 수 있습니다. (추후 업로드 예정)

### **Personal and Sensitive Information**

본 데이터셋은 개인을 식별할 수 있는 정보(PII)나 민감 정보를 포함하지 않도록 노력했습니다. 데이터 수집 및 정제 과정에서 다음과 같은 유해성 판별 기준을 적용하여 관련 내용을 제거하거나 수정했습니다:

- **유해성 발화 정의:**
    - `공격적 언어 사용`: 욕설, 모욕, 비하, 위협 등의 표현.
    - `특정 대상의 공격`: 개인이나 특정 집단을 겨냥한 모욕 및 공격.
    - `차별적 속성 기반 공격`: 인종, 성별, 성적 지향, 종교, 연령, 장애 등 사회적 차별 요소를 기반으로 한 공격 (혐오 발언으로 간주).
    - `맥락적 이해 중요`: 언어의 문자적 의미뿐만 아니라 사용 맥락을 고려하여 유해성 여부를 판단.
    - `암시적 표현 포함`: 명시적 욕설 외에도 암시적이고 우회적인 표현 역시 유해 발언으로 간주.
    - `편견과 혐오의 연관성`: 사회적 편견과 혐오 발언 간의 밀접한 연관성을 고려.
- **PII 제거 노력:** 수집된 데이터에서 이름, 전화번호, 주소, 이메일 주소 등 명백한 개인 식별 정보는 검토 과정에서 제거되었습니다. 그러나 웹에서 수집된 데이터의 특성상, 공개적으로 사용되는 닉네임이나 간접적으로 유추될 수 있는 정보가 미량 포함될 가능성은 배제할 수 없습니다. 발견 시 보고해주시면 수정하겠습니다.

### **Bias, Risks, and Limitations**

- **Bias:**
    - 본 데이터셋은 주로 온라인 커뮤니티와 미디어에서 유래된 신조어 및 유행어를 중심으로 구성되어 있어, 특정 연령대(예: 젊은 세대)나 특정 온라인 문화에 편향된 언어 사용을 반영할 수 있습니다.
    - 유해성 판별 기준을 적용했으나, 주관적 판단의 여지가 있어 일부 편향적이거나 민감할 수 있는 내용이 미처 필터링되지 못했을 가능성이 있습니다.
- **Risks:**
    - 신조어와 유행어는 시의성이 매우 강하여 시간이 지남에 따라 의미가 변하거나 사용되지 않게 될 수 있습니다(데이터 노후화).
    - 라이선스(CC BY-NC-SA 4.0)를 위반하여 영리적 목적으로 사용되거나, 출처 표시 없이 사용될 위험이 있습니다.
    - 필터링 노력에도 불구하고, 맥락에 따라 부적절하거나 공격적으로 해석될 수 있는 내용이 포함될 위험이 있습니다.
- **Limitations:**
    - 본 데이터셋은 한국어 신조어의 전체 범위를 포괄하지 못하며, 특정 시점까지 수집된 내용을 기반으로 합니다.
    - 아재개그의 경우 유머 코드가 주관적일 수 있으며, 모든 사용자에게 재미를 보장하지 않습니다.
    - 데이터셋의 크기가 약 3400으로, 모든 종류의 LLM 학습에 충분하지 않을 수 있습니다.

### **Recommendations**

- 사용자는 본 데이터셋을 CC BY-NC-SA 4.0 라이선스 조건에 따라 비영리 목적으로만 사용하고, 출처(Hugging Face KREW 및 원본 데이터 제공처)를 명확히 밝혀야 합니다.
- 신조어 및 유행어의 시의성을 고려하여, 최신 트렌드를 반영하기 위해서는 주기적인 업데이트나 추가 데이터 수집이 필요할 수 있습니다.
- 데이터셋 사용 시 발생할 수 있는 편향이나 민감한 내용에 대해 인지하고 주의 깊게 사용해야 합니다.
- 데이터셋의 개선을 위한 피드백이나 오류 보고는 언제나 환영합니다. (**[Dataset Card Contact 정보 참조]**)

### **Citation**

**BibTeX:**

```
@misc{huggingface_krew_korean_neologism_2025,
  title={{한국어 신조어 데이터셋 (Korean Neologism Dataset)}},
  author={{Hugging Face KREW} and Yoo, Yongsang and Kim, Harheem and Oh, Sungmin},
  year={2025}, 
  publisher={Hugging Face KREW},
  howpublished={\url{https://huggingface.co/datasets/huggingface-KREW/KoCulture-Dialogues}} 
}
```

**APA:**

Hugging Face KREW, Yoo, Y., Kim, H., & Oh, S. (2025). *한국어 신조어 데이터셋 (Korean Neologism Dataset)*. Hugging Face KREW. Retrieved from `https://huggingface.co/datasets/huggingface-KREW/korean-neologism-dataset`

### **More Information**

- **Hugging Face KREW 커뮤니티:** https://discord.gg/bKh5M7xsXP
- **프로젝트 관련 자료:** https://github.com/Pseudo-Lab/Hugging-Face-Hub-Garden

### **Dataset Card Authors**

- 유용상 (Yongsang Yoo)
- 김하림 (Harheem Kim)
- 오성민 (Sungmin Oh)

### **Dataset Card Contact**

- https://github.com/Pseudo-Lab/Hugging-Face-Hub-Garden/issues