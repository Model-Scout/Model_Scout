---
license: cc-by-sa-4.0
language:
- ko
tags:
- agent
- LLM
---

# TelAgentBench 
TelAgentBench는 LLM의 통신 산업 특화 에이전트 능력(Reasoning, Planning, Action, RAG, Instruction Following)을 평가하는 한국어 벤치마크입니다[[논문 참고](https://aclanthology.org/2025.emnlp-industry.83/)]. 기존 영어 중심 벤치마크가 다루지 못한 현실적이고 도메인 특화된 과제를 측정하기 위해 제작되었습니다. 실제 통신사 환경에서 LLM의 문제 해결력과 도구 활용 능력을 검증하며, 한국 NLP 커뮤니티의 연구/발전에 기여하고자 5개 Agent Task 중 공개 가능한 3개 Task를 공개합니다.

## TelAgent Action
TelAgent Action은 통신 고객 서비스 시나리오에서 LLM의 함수 호출(Function-calling) 능력을 평가합니다. 10개의 하위 과제(sub-task)와 757개의 벤치마크 인스턴스를 구축했으며, 함수 사용 복잡도(예: Simple, Parallel, Multiple, Multi-turn-base)와 맥락적 난이도(예: Relevance identification, Missing parameter handling) 기준으로 분류되었습니다. 이 구성은 BFC(Yan et al., 2024)에서 제안된 방식을 따릅니다.

### Data Schema
**Single-Turn (Simple, Parallel, Multiple, Parallel-Multiple, Item-Recommendation) Schema**:
```
{
  "id": "telco_{task}_N",
  "question": [
    [
      {
        "role": "system",
        "content": "Containing User State"
      },
      {
        "role": "user",
        "content": "Query"
      }
    ]
  ],
  "function": [
    {
      "name": "FUNCTION_1",
      …
    },
    {
      "name": "FUNCTION_2",
      …
    },
    {
      "name": "FUNCTION_3",
      …
    },
    {
      "name": "FUNCTION_4",
      …
    }
  ]
}

Ground_Truth: // See possible_answer/*.json
{
  "id": "telco_{task}_N",
  "ground_truth": [
    {
      "FUNCTION_NAME": {
        "VALUE": [
          "PARAMETER"
        ]
      }
    }
  ]
  …
}
```

**Multi-step (Whole, Partial) and Multi-turn Schema**:
```
{
  "id": "telco_multi_turn_stateless_base_N",
  "question": [
    [
      {
        "role": "system",
        "content": "System instructions with user persona" // for live_multi_step, and multi_turn
      },
      {
        "role": "user",
        "content": "First user query"
      }
    ],
    [
      {
        "role": "user",
        "content": "Second user query (context from turn 1)"
      }
    ],
    [
      {
        "role": "user",
        "content": "Third user query (context from turns 1-2)"
      }
    ]
  ],
  "possible_answer": [
    [
      "Function call for turn 1",
      ...
    ],
    [
      "Function call for turn 2"
    ],
    ...
  ],
  "possible_answer_result": [
    [
      {
        "resultCode": "0000",
        ...
      }
    ],
    [
      {
        "resultCode": "0000",
        ...
      }
    ],
    ...
  ],
  "possible_postcall_answer": [
    // only for multi_turn
    {
      "role": "assistant",
      "content": "Response for turn 1"
    },
    {
      "role": "assistant",
      "content": "Response for turn 2"
    },
    ...
  ]
}
```

### 수량
| Evaluation Category | Count | File Name | Functions Provided | Functions Called | Description |
|---------------------|-------|-----------|-------------------|------------------|-------------|
| **1. Simple** | **110** | | **1** | **1** | **Single function call** |
| ├─ Non-Live | 55 | telco_simple.json | 1 | 1 | Without system message |
| └─ Live | 55 | telco_live_simple.json | 1 | 1 | With persona/system message |
| **2. Parallel** | **38** | | **1** | **>1** | **Same function × N (parallel)** |
| ├─ Non-Live | 19 | telco_parallel.json | 1 | >1 | Without system message |
| └─ Live | 19 | telco_live_parallel.json | 1 | >1 | With persona/system message |
| **3. Multiple** | **110** | | **7** | **1** | **Function selection from multiple** |
| ├─ Non-Live | 55 | telco_multiple.json | 7 | 1 | Without system message |
| └─ Live | 55 | telco_live_multiple.json | 7 | 1 | With persona/system message |
| **4. Parallel Multiple** | **36** | | **7** | **>1** | **Mixed parallel + sequential** |
| ├─ Non-Live | 18 | telco_parallel_multiple.json | 7 | >1 | Without system message |
| └─ Live | 18 | telco_live_parallel_multiple.json | 7 | >1 | With persona/system message |
| **5. Multi-step** | **92** | | **7/23** | **>1** | **Consecutive/conditional calls** |
| ├─ Partial (Non-Live) | 23 | telco_multi_step_stateless_partial.json | 7 | >1 | Subset of functions provided |
| ├─ Partial (Live) | 23 | telco_live_multi_step_stateless_partial.json | 7 | >1 | With persona, subset functions |
| ├─ Whole (Non-Live) | 23 | telco_multi_step_stateless_whole.json | 23 | >1 | All functions provided |
| └─ Whole (Live) | 23 | telco_live_multi_step_stateless_whole.json | 23 | >1 | With persona, all functions |
| **6. Item Recommendation** | **52** | | **7** | **1-3** | **Recommendation logic** |
| ├─ Non-Live | 26 | telco_item_recommendation_parallel_multiple.json | 1-3 | >=1 | Without system message |
| └─ Live | 26 | telco_live_item_recommendation_parallel_multiple.json | 1-3 | >=1 | With persona/system message |
| **7. Irrelevance** | **118** | | **6-8** | **0** | **Negative testing (no calls)** |
| └─ Live Only | 118 | telco_live_irrelevance.json | 6-8 | 0 | Should NOT trigger functions |
| **8. Relevance** | **117** | | **23** | **>=1** | **Positive relevance testing** |
| └─ Live Only | 117 | telco_live_relevance.json | 23 | 1+ | Should trigger appropriate functions |
| **9. Multi-turn Base** | **46** | | **23** | **1-4/turn** | **Multi-turn conversation** |
| └─ Live Only | 46 | telco_multi_turn_stateless_base.json | 23 | >=1 per turn | Context continuity across turns |
| **10. Multi-turn Miss Param** | **38** | | **23** | **>=1/turn** | **Parameter clarification** |
| └─ Live Only | 38 | telco_multi_turn_stateless_miss_param.json | 23 | >=1 per turn | Missing parameters across turns |


**Function Description Schema**: *_tools.json을 참고하세요.
```
{"name": "FUNCTION_NAME", "description": "...", "parameters": {FUNCTION_SCHEMA}}
```


## TelAgent Plan
TelAgentPlan은 복잡한 여행 계획 수립 및 로밍 요금제 추천 분야에서의 언어 에이전트 능력을 평가하기 위해 설계되었으며, 기존 TravelPlanner 벤치마크를 확장하고 한국어로 현지화한 데이터셋입니다. 미국 여행지 중심의 데이터를 넘어 한국 사람들이 자주 방문하는 관광지(베트남 호치민, 일본 도쿄, 대만 타이베이 등)를 포함한 다양한 해외 목적지들로 범위를 확장했습니다. 또한 여행 예산, 숙소 유형, 로밍 데이터 사용량 등 사용자의 선호도를 반영하여 맞춤형 여행 및 로밍 계획을 생성할 수 있도록 지원합니다.

### Data Schema
```
{
  "org": "서울",
  "dest": "도쿄/오사카/교토/요코하마",
  "days": 7,
  "visiting_city_number": 4,
  "people_number": 4,
  "data_usage_per_day": "3GB",
  "transportation": "교통(기차)",
  "minimum_nights": "최소 숙박(3일/도시)",
  "budget": 10000000,
  "query": "가족 4명이 함께 도쿄, 오사카, 교토, 요코하마로 7일간 여행가려고요...",
  "level": "easy",
  "reference_information": [
    {
      "Description": "Attractions in 도쿄",
      "Content": [
        {
          "Name": "도쿄 스카이트리",
          "Latitude": 35.710068,
          생략
        }
      ]
    },
    {
      "Description": "Restaurants in 도쿄",
      "Content": [
        {
          "Name": "스시 다이",
          "AverageCost": 50000,
          생략
        }
      ]
    },
    {
      "Description": "Accommodations in 도쿄",
      "Content": [
        {
          "Name": "신주쿠 코지 스튜디오",
          "Price": 108000,
          생략
        }
      ]
    },
    {
      "Description": "Flights from 서울 to 도쿄",
      "Content": [
        {
          "FlightNumber": "KE0710",
          "Price": 750000,
          생략
        }
      ]
    },
    {
      "Description": "All Roaming Plans",
      "Content": [
        {
          "Category": "baro 요금제",
          "Name": "baro 3GB",
          생략
        }
      ]
    }
  ]
}
```

### 평가용 샌드박스 데이터

TelPlan을 평가하려면, 기준(reference) 정보를 생성할 때 사용된 샌드박스 데이터가 필요합니다. Google Drive [링크](https://drive.google.com/drive/folders/1yihZhPc7Hj5YwJ6k4woaUkdjw-pTCWF6?usp=sharing)를 통해 접근하고 다운로드할 수 있습니다.

### 수량
TelAgent Plan에는 총 200개의 쿼리가 있으며, 난이도별로는 easy 67개, medium 67개, hard 66개로 구성되어 있습니다.


## TelAgent IF

이 데이터셋은 한국어 지침 준수 능력을 멀티턴 대화 상황에서 평가하기 위해 설계되었습니다. 이번에 공개하는 일반 도메인(통신 도메인 데이터셋은 제외)에서는 3단계 대화를 통해 복합적인 한국어 지침을 지속적으로 따르는지를 측정합니다. 

### Data Schema
```
{
  "turn_1": {
    "prompt": "서울 종로구에서 5명의 가족들과 함께 먹을만한 한식당 7개만 추천해주세요. 응답은 번호를 매긴 항목 7개로 구성되어야 하고, 각 항목은 1,2,3,4,5,6,7로 표기해야 합니다.",
    "instruction_id_list": [
      "ko:detectable_format:number_digit_lists"
    ],
    "kwargs": [
      {
        "num_digit_list": 7
      }
    ]
  },
  "turn_2": {
    "prompt": "해당 추천 리스트에 제목을 지어주시고, 제목을 <<>>  이중 꺾쇠 괄호로 감싸세요. 추천한 내용에 단어 '가족', '단체석', '넓은'을 포함하세요",
    "instruction_id_list": [
      "ko:detectable_format:number_digit_lists",
      "ko:detectable_format:title",
      "ko:keywords:existence"
    ],
    "kwargs": [
      {
        "num_digit_list": 7
      },
      {},
      {
        "keywords": [
          "가족",
          "단체석",
          "넓은"
        ]
      }
    ]
  },
  "turn_3": {
    "prompt": "전체 내용이 500자에서 700자 사이가 되도록 작성해주세요.",
    "instruction_id_list": [
      "ko:detectable_format:number_digit_lists",
      "ko:detectable_format:title",
      "ko:keywords:existence",
      "ko:length_constraints:number_syllables",
      "ko:length_constraints:number_syllables"
    ],
    "kwargs": [
      {
        "num_digit_list": 7
      },
      {},
      {
        "keywords": [
          "가족",
          "단체석",
          "넓은"
        ]
      },
      {
        "relation": "at least",
        "num_syllables": 500
      },
      {
        "relation": "less than",
        "num_syllables": 701
      }
    ]
  }
}
```

### 수량

TelAgent IF는 3-turn으로 구성되어 있으며, 200개의 평가셋으로 구성되어 있습니다.

# License
이 데이터셋은 Creative Commons Attribution ShareAlike 4.0 International License (CC BY-SA 4.0) 하에 배포됩니다.

# Citation

```
@inproceedings{lee-etal-2025-telagentbench,
    title = "{T}el{A}gent{B}ench: A Multi-faceted Benchmark for Evaluating {LLM}-based Agents in Telecommunications",
    author = "Lee, Sunwoo  and
      Jang, Daseong  and
      Arya, Dhammiko  and
      Han, Gyoung-eun  and
      Song, Injee  and
      Kim, SaeRom  and
      Kim, Sangjin  and
      Lee, Seojin  and
      Hong, Seokyoung  and
      Sek, Sereimony  and
      Cho, Seung-Mo  and
      Park, Sohee  and
      Yoon, Sungbin  and
      Jang, Wonbeom  and
      Davis, Eric",
    editor = "Potdar, Saloni  and
      Rojas-Barahona, Lina  and
      Montella, Sebastien",
    booktitle = "Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track",
    month = nov,
    year = "2025",
    address = "Suzhou (China)",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.emnlp-industry.83/",
    doi = "10.18653/v1/2025.emnlp-industry.83",
    pages = "1173--1211",
    ISBN = "979-8-89176-333-3",
    abstract = "As Large Language Models (LLMs) evolve into powerful agentic systems, the telecommunications industry{'}s expansion into AI services necessitates industry-grounded benchmarks to evaluate their underexplored domain-specific capabilities. To address the gap left by generic benchmarks that fail to assess realistic, non-English performance, we present TelAgentBench, a Korean benchmark for the telecommunications domain evaluating five core agentic capabilities: Reasoning, Planning, Action (tool-use), Retrieval-Augmented Generation, and Instruction Following. Evaluations reveal significant performance disparities between models that employ explicit reasoning and those that do not, providing actionable insights for deploying agentic LLMs in real-world telecommunications tasks."
}
```