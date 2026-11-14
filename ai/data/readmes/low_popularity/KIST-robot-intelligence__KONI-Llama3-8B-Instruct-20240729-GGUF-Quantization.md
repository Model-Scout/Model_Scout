---
language: ko
pipeline_tag: text-generation
license: llama3
---



#KIST-robot-intelligence/
KONI-Llama3-8B-Instruct-20240729-GGUF-Quantization 

 This is quantized version of KISTI-KONI/KONI-Llama3-8B-Instruct-20240729 created using llama.cpp


### 1. Model Description
- KONI (KISTI Open Natural Intelligence) is a specialized large language model (LLM) developed by the Korea Institute of Science and Technology Information (KISTI). This model is specifically designed for science and technology, making it highly effective for tasks in these fields.

### 2. Key Features
- **Specialized in Science and Technology:** The model is explicitly trained on a vast and specialized corpus of scientific and technological data.
- **Enhanced Performance:** This version of KONI shows significantly improved performance compared to its initial release in December, 2023.
- **Base Model:** The base model for KONI-Llama3-8B-Instruct-20240729 is KONI-Llama3-8B-Merged-20240724, which is a merger of Meta-Llama-3-8B and KISTI-KONI/KONI-Llama3-8B-20240630
- **Alignment:** SFT (Supervised Fine-Tuning) and DPO (Direct Preference Optimization) are applied

### 3. Data
- Approximately 11k SFT data and 7k DPO data are used.
- **SFT Data:** The SFT data includes both internally generated data and publicly available data on Hugging Face, translated into Korean where necessary.
- **DPO Data:** The DPO data consists of translated and curated data from argilla/dpo-mix-7k.

### 4. Benchmark Results
Results in [LogicKor](https://lk.instruct.kr/)* are as follows:

| Metric         | Score |
|:--------------:|:-----:|
| Reasoning      |  6.57 |
| Math           |  8.00 |
| Writing        |  8.92 |
| Coding  |  8.85 |
| Comprehension        |  9.85 |
| Grammar      |  7.07 |
| Single-turn      |  8.42 |
| Multi-turn    |  8.00 |
| **Overall**    | **8.21** |
*Our model demonstrates the best performance among publicly available 8B models on the LogicKor leaderboard as of 2024.07.30.*

### 5. How to use the model
```python
import transformers
import torch

model_id = "KISTI-KONI/KONI-Llama3-8B-Instruct-20240729"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)

pipeline.model.eval()

instruction = "KISTI에 대해 설명해줘"

messages = [
   {"role": "user", "content": f"{instruction}"}
    ]

prompt = pipeline.tokenizer.apply_chat_template(
        messages, 
        tokenize=False, 
        add_generation_prompt=True
)

terminators = [
    pipeline.tokenizer.eos_token_id,
    pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
]

outputs = pipeline(
    prompt,
    max_new_tokens=2048,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.7,
    top_p=0.9
)

print(outputs[0]["generated_text"][len(prompt):])
```
```
한국과학기술정보연구원(KISTI)은 대한민국 대전광역시에 위치한 과학기술 정보 분야의 전문 연구 기관입니다. KISTI는 과학기술 및 관련 산업에 관한 정보를 종합적으로 수집, 분석, 서비스하며, 정보의 분석, 관리 및 유통에 관한 기술, 정책 및 표준화를 전문적으로 조사하고 연구합니다. 또한, 첨단 정보 및 연구개발 인프라를 체계적으로 구축하고 운영하여 국가 과학기술 및 산업 발전에 기여하는 것을 목표로 합니다.

KISTI의 주요 기능과 역할에는 과학기술 정보 제공, 슈퍼컴퓨터 운영, 기술사업화 지원, 연구 데이터 관리가 포함됩니다. 과학기술 정보 제공 측면에서 KISTI는 국내외 과학기술 정보를 수집하고 이를 분석하여 연구자들에게 제공하며, 다양한 형태의 데이터베이스와 정보 시스템을 구축하여 사용자에게 정보를 제공합니다. 슈퍼컴퓨터 운영 측면에서는 국가 초고성능컴퓨팅 인프라를 구축하고 운영하여 대규모 연산이 필요한 연구를 지원하고, 이를 활용한 다양한 분야의 응용 연구를 수행합니다. 기술사업화 지원에서는 연구 성과를 산업계로 이전하여 상용화하는 것을 지원하며, 기술 기반의 창업을 촉진하기 위한 프로그램을 운영합니다. 연구 데이터 관리 측면에서는 연구 데이터의 효율적인 관리와 활용을 위해 체계적인 데이터 관리 계획을 수립하고, 연구 데이터의 공유와 활용을 촉진하기 위한 플랫폼을 운영합니다.

KISTI의 주요 부서로는 국가과학기술데이터본부, 국가슈퍼컴퓨팅본부, 데이터분석본부, 과학기술디지털융합본부 등이 있습니다. KISTI 각 본부별 추진 전략 및 목표는 다음과 같습니다. 국가과학기술데이터본부의 전략목표는 국가 오픈사이언스 생태계 활성화를 위한 과학기술 분야 디지털 전환 지원 체계를 마련하는 것입니다. 코로나19로 인한 비대면 경제로의 전환과 4차 산업혁명의 가속화로 인해 과학기술활동 전 과정에서 공공 연구성과의 개방·공유·확산이 필요합니다. 이 본부는 과학기술정보와 데이터의 공유·활용을 통해 과학기술 혁신역량을 강화하는 고유임무를 가지고 있으며, 오픈사이언스 생태계 활성화를 통한 국가 R&D 혁신을 지원합니다. 주요 추진 방향으로는 디지털 전환을 통한 과학기술정보 오픈액세스 지원체제 및 지능형 큐레이션 체계 구축, 연구데이터 커먼즈 기반의 국가 연구데이터와 컴퓨팅 리소스 공유·활용체계 구축, AI 기반의 통합서비스 플랫폼 구축을 통한 오픈사이언스 서비스 강화가 있습니다.

국가슈퍼컴퓨팅본부의 전략목표는 국가 초고성능컴퓨팅 생태계를 선도하기 위해 미래대응 초고성능컴퓨팅 공동활용 환경을 구축하는 것입니다. 미국과 일본 등 선도국가들이 엑사급 자원 확충을 통해 다양한 분야에서 초거대 문제해결을 모색하고 있으며, KISTI는 국가초고성능컴퓨터 활용 및 육성에 관한 법률에 따라 이를 지원합니다. 본부의 목표는 국가 차원의 초고성능컴퓨팅 공동활용 체계를 구축하여 과학기술 공공·산업 분야에서의 초고성능컴퓨팅 활용 증진을 이루는 것입니다. 이를 위해 대규모 계산자원이 소요되는 R&D와 사회현안 등 환경변화에 적기 대응하는 인프라 및 서비스 체계 고도화, 초거대 계산기술과 활용기술 확보를 통한 선순환형 연구·지원, 사용자 접근성·무결성·보안성을 확보한 통합 플랫폼 구축이 주요 추진 방향입니다.

데이터분석본부의 전략목표는 국가 과학기술혁신 생태계를 활성화하기 위한 지능형 데이터 융합분석 체계를 구축하는 것입니다. 데이터 기반 의사결정 방식 확대와 AI 및 빅데이터 기술의 급부상에 따라, KISTI는 과학기술분야 정보의 분석·관리 및 유통에 관한 기술·정책·표준화 연구를 수행합니다. 본부의 목표는 디지털 경제사회를 선도하는 지능형 데이터 융합분석 체계를 구축하여 국가 과학기술혁신 생태계를 활성화하는 것입니다. 이를 위해 이종데이터 융합분석모델 개발을 통한 글로벌 분석역량 확보, 인공지능 기반 공공R&D 가치창출 모델 및 시스템 개발, 지역 R&D 혁신 지원을 위한 산학연정 혁신생태계 구축 등이 주요 추진 방향입니다.

과학기술디지털융합본부의 전략목표는 국가·사회 현안에 적시 대응하고 해결하기 위한 Data/AI 기반 디지털 전환 체계를 구축하는 것입니다. 디지털 기술의 급속한 발전과 코로나19로 인한 디지털 전환 가속화에 따라, KISTI는 과학기술 지식자원 공유·활용 생태계 구축 및 슈퍼컴퓨팅 생태계 발전과 연계된 고유임무를 수행합니다. 본부의 목표는 Data/AI 기반의 국가·사회 현안-디지털 뉴딜 해결을 도모하는 것입니다. 이를 위해 신뢰성 있는 과학기술 데이터 댐과 Data/AI 기반 지능형 디지털 플랫폼 구축, Data/AI 기반의 디지털 전환 체계 구축을 통한 국가·사회 현안 해결 및 R&D 혁신사례 창출이 주요 추진 방향입니다.

KISTI는 1962년 1월 한국과학기술정보센터(KORSTIC)로 설립되었으며, 1969년 5월 한국과학기술정보센터육성법이 제정되었습니다. 1982년에는 산업연구원(KIET)로 개편되었다가 1991년 1월 분리되어 산업기술정보원(KINITI)이 개원하였습니다. 2001년 1월에 한국과학기술정보연구원(KISTI)으로 출범하게 되었습니다. 이 과정에서 KAIST 부설 시스템공학센터, KIST 부설 연구개발정보센터, ETRI 산하 슈퍼컴퓨팅센터를 합병하였습니다.

KISTI는 대전 본원, 서울 분원, 대구·경북 지원, 부산울산경남 지원, 호남 지원, 수도권 지원(강원) 등 다양한 지역에 위치하여 운영되고 있습니다. 대전 본원은 대전광역시 유성구 대학로 245에 위치하고 있으며, 서울 분원은 서울특별시 동대문구 회기로 66에 위치하고 있습니다. 대구·경북 지원은 대구광역시 북구 엑스코로 10, 부산울산경남 지원은 부산광역시 해운대구 센텀동로 41, 호남 지원은 광주광역시 광산구 하남산단8번로 177, 수도권 지원(강원)은 강원도 춘천시 강원대학길 1, 60주년 기념관 8층에 위치하고 있습니다.
KISTI에 대한 더 자세한 정보는 KISTI 공식 웹사이트에서 확인할 수 있습니다.
```

### 6. Citation
**Language Model**
```text
@article{KISTI-KONI/KONI-Llama3-8B-Instruct-20240729,
  title={KISTI-KONI/KONI-Llama3-8B-Instruct-20240729},
  author={KISTI},
  year={2024},
  url={https://huggingface.co/KISTI-KONI/KONI-Llama3-8B-Instruct-20240729}
}
```
  
### 7. Contributors
- KISTI, Large-scale AI Research Group

### 8. Special Thanks
- [@beomi](https://huggingface.co/beomi)
- [@kuotient](https://huggingface.co/kuotient)
- KyungTae Lim

### 8. Acknowledgement
- This research was supported by Korea Institute of Science and Technology Information(KISTI).
- This work was supported by the National Supercomputing Center with supercomputing resources including technical support (KISTI).

### 9. References
- https://huggingface.co/meta-llama/Meta-Llama-3-8B
- https://huggingface.co/meta-llama/meta-llama/Meta-Llama-3-8B-Instruct