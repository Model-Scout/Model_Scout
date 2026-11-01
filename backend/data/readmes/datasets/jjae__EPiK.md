---
license: apache-2.0
task_categories:
- text-classification
language:
- ko
pretty_name: EPiK
size_categories:
- n<1K
---

# EPiK: Everyday Physics in Korean Contexts

✨ Check out our paper for more details: [arXiv:2509.17807](https://arxiv.org/abs/2509.17807)! 📚💡


## Dataset Summary
EPiK is a Korean dataset that combines Korean cultural context and physical principles to evaluate AI models' physical commonsense reasoning capabilities. It consists of problems based on everyday situations that can be understood by any Korean person. Each problem is designed to require both physical reasoning and an understanding of Korean culture. 
- Total Samples: **181**
- Task Types: Built upon **9 distinct physical reasoning tasks**
- Cultural Relevance: 157 samples with a cultural_element_score of 1 and 24 samples with a score of 2


## Data Fields
| Field                  | Type    | Description                                                                                                  |
|-------------------------|---------|--------------------------------------------------------------------------------------------------------------|
| `problem_type_category`   | string  | Coarse-grained reasoning category |
| `problem_type_subcategory`| string  | Fine-grained reasoning sub-category |
| `prompt`                  | string  | Question |
| `solution0`               | string  | Candidate solution0                                                     |
| `solution1`               | string  | Candidate solution1                                                 |
| `label`                   | int | Index of the correct solution (0 or 1)                                                                 |
| `explanation`             | string  | Detailed explanation of why the correct answer is valid and why the alternative is incorrect              |
| `korea_relevance`         | string  | Korean cultural elements |
| `physical_relevance`      | string  | Physical reasoning principles or elements |
| `cultural_element_score`  | int | Degree to which the question leverages Korean-specific cultural elements (1: mentioned but not essential, 2: central and essential) |


## Taxonomy of problem types
<table border="1" cellpadding="6" cellspacing="0"> 
  <thead> 
    <tr> 
      <th>대분류</th> 
      <th>문제 유형</th> 
      <th>정의</th> 
    </tr> 
  </thead> 
  <tbody> 
    <tr> 
      <td rowspan="3">기초 지식 및 속성 이해</td> 
      <td>물리 개념 및 원리</td> 
      <td>기본적인 물리 법칙과 원리에 대한 이해를 평가합니다.</td> 
    </tr> 
    <tr> 
      <td>객체 속성 및 기능</td> 
      <td>사물의 재질, 무게, 형태, 질감 등 고유 속성과 가능한 상호작용을 이해하고 평가합니다.</td> 
    </tr> 
    <tr> 
      <td>물질의 상태와 변화</td> 
      <td>고체, 액체, 기체 상태의 특징과 녹는 것, 어는 것, 끓는 것, 녹이는 것 등 물질의 상태 변화의 원리를 이해하고 평가합니다.</td> 
    </tr> 
    <tr> 
      <td rowspan="2">인과관계 및 동적 추론</td> 
      <td>물리적 결과 예측</td> 
      <td>특정 행동이나 사건이 가져올 물리적 결과를 예측하는 능력을 평가합니다.</td> 
    </tr> 
    <tr> 
      <td>물리적 원인 분석</td> 
      <td>이미 발생한 현상의 원인을 가장 타당한 물리적 관점에서 설명하는 능력을 평가합니다.</td> 
    </tr> 
    <tr> 
      <td rowspan="3">목표 지향 및 응용 추론</td> 
      <td>도구 및 절차 활용</td> 
      <td>목표 달성을 위해 적절한 도구를 선택하고 올바른 절차에 따라 사용하는 능력을 평가합니다.</td> 
    </tr> 
    <tr> 
      <td>문제 해결 및 계획</td> 
      <td>주어진 문제를 해결하기 위해 여러 단계의 물리적 행동을 계획하고 실행하는 능력을 평가합니다.</td> 
    </tr> 
    <tr> 
      <td>물리적 타당성 판단</td> 
      <td>제시된 해결책이 물리적으로 가능한지, 현실 세계의 상식적인 도구와 개념에 기반하는지를 평가합니다.</td> 
    </tr> 
    <tr> 
      <td>상황 및 제약 조건 추론</td> 
      <td>위험성 및 안전성 평가</td> 
      <td>잠재적 위험을 예측하고 안전을 확보하기 위한 방법을 추론하는 능력을 평가하는 능력을 평가합니다.</td> 
    </tr> 
  </tbody> 
</table>


## Taxonomy of problem types (English ver.)
<table border="1" cellpadding="6" cellspacing="0">
  <thead>
    <tr>
      <th>Category</th>
      <th>Problem Type</th>
      <th>Definition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Basic Knowledge and Attribute Comprehension</td>
      <td>Physical Concepts and Principles</td>
      <td>Assesses understanding of fundamental physical laws and principles.</td>
    </tr>
    <tr>
      <td>Object Attributes and Functions</td>
      <td>Assesses understanding and evaluation of inherent properties like material, weight, shape, and texture, and potential interactions.</td>
    </tr>
    <tr>
      <td>States of Matter and Changes</td>
      <td>Assesses understanding and evaluation of the characteristics of solid, liquid, and gas states, and the principles of state changes like melting, freezing, boiling, and dissolving.</td>
    </tr>
    <tr>
      <td rowspan="2">Causality and Dynamic Reasoning</td>
      <td>Predicting Physical Outcomes</td>
      <td>Assesses the ability to predict the physical outcomes of specific actions or events.</td>
    </tr>
    <tr>
      <td>Analyzing Physical Causes</td>
      <td>Assesses the ability to explain the cause of an already-occurred phenomenon from the most plausible physical perspective.</td>
    </tr>
    <tr>
      <td rowspan="3">Goal-Oriented and Applied Reasoning</td>
      <td>Utilizing Tools and Procedures</td>
      <td>Assesses the ability to select appropriate tools and follow correct procedures to achieve a goal.</td>
    </tr>
    <tr>
      <td>Problem Solving and Planning</td>
      <td>Assesses the ability to plan and execute multi-step physical actions to solve a given problem.</td>
    </tr>
    <tr>
      <td>Judging Physical Plausibility</td>
      <td>Assesses whether a proposed solution is physically possible and based on common-sense tools and concepts in the real world.</td>
    </tr>
    <tr>
      <td>Situational and Constraint Reasoning</td>
      <td>Risk and Safety Assessment</td>
      <td>Assesses the ability to predict potential risks and infer methods to ensure safety.</td>
    </tr>
  </tbody>
</table>


## Dataset Construction Stages
1. **Foundational Framework**: Establish a task taxonomy and sourcing realistic scenarios.

2. **Two-Stage Generation and Verification Pipeline**: Problems generation and verification process

3. **Deduplication**: Filter out by Min-hash algorithm to ensure dataset diversity.

4. **Answer Bias Filtering**: Remove questions where the correct answer can be guessed from superficial cues, rather than genuine reasoning.

5. **Human Evaluation**: Final quality assurance by a human expert


## Example
```json
{
  "problem_type_category": "기초 지식 및 속성 이해",
  "problem_type_subcategory": "객체 속성 및 기능",
  "prompt": "한옥의 온돌방에서 바닥이 따뜻하게 유지되는 물리적 원리는 무엇인가요?",
  "solution0": "열이 바닥에 설치된 금속과 흙을 통해 저장 및 전달되기 때문입니다.",
  "solution1": "열이 바닥에 설치된 돌과 흙을 통해 저장 및 전달되기 때문입니다.",
  "label": 1,
  "explanation": "정답에서는 바닥에 설치된 '돌과 흙'을 통해 열이 저장 및 전달된다고 합니다. 이는 바닥재가 열을 저장하고 점차적으로 방출하여 방이 따뜻하게 유지되도록 하는 원리를 설명합니다. 반면, 오답은 '금속과 흙'을 통해 열이 저장 및 전달된다고 주장하는데, 금속은 열을 빠르게 전달하고 방출하므로 지속적인 열 유지에 적합하지 않습니다. 따라서 한옥 온돌의 특성과 맞지 않으며, 열이 오랫동안 유지되는 천천히 방출되는 특징을 설명하기에는 부족합니다.",
  "korea_relevance": ["한옥", "온돌"],
  "physical_relevance": ["열 전달", "바닥 난방", "돌과 흙"],
  "cultural_element_score": 2
}
```


## Citation
```
@misc{jeong2025everydayphysicskoreancontexts,
      title={Everyday Physics in Korean Contexts: A Culturally Grounded Physical Reasoning Benchmark}, 
      author={Jihae Jeong and DaeYeop Lee and DongGeon Lee and Hwanjo Yu},
      year={2025},
      eprint={2509.17807},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2509.17807}, 
}
``` 
