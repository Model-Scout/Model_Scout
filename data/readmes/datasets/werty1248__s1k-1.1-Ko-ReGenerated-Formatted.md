---
dataset_info:
  features:
  - name: index
    dtype: int64
  - name: question
    dtype: string
  - name: question_ko
    dtype: string
  - name: reasoning_ko
    dtype: string
  - name: answer_ko
    dtype: string
  - name: boxed_ko
    dtype: string
  - name: deepseek_answer
    dtype: string
  - name: deepseek_boxed
    dtype: string
  - name: gemini_naswer
    dtype: string
  - name: gemini_boxed
    dtype: string
  - name: solution
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 43812381
    num_examples: 984
  download_size: 18860751
  dataset_size: 43812381
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: mit
task_categories:
- text-generation
language:
- ko
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6629154d55d7c289634b8c5d/qG17_r3-Yl0yQlBaBkInE.png)

1. **[simplescaling/s1K-1.1](https://huggingface.co/datasets/simplescaling/s1K-1.1)** 에서 **question 데이터만** GPT-4o를 이용하여 번역
  - 단, crossword 퍼즐은 제외 (번역 불가)
2. Deepseek-R1 (fp8, Provider: fireworks.ai)을 사용하여 **한국어로 추론 및 답하게 함** (3차 정제 시점에는 bf16? Provider: FriendliAI 사용)
3. 1차 정제
  - 원본 데이터에서, **gemini의 출력, r1의 출력, solution 중 두 개**의 답이 일치하면 **신뢰할 수 있는 답**이라고 정의
  - 한국어 R1 답변 결과가 신뢰할 수 있는 답과 다르거나, 답변이 씹힌 경우, 서식이 틀린 경우 총 123개에 대해 추론 및 답변 재생성
4. 2차 정제
  - 1차와 동일한 프로세스, 63개 데이터 재생성
5. 3차 정제
  - **추론 과정에서 한자가 출력된** 7개 데이터 재생성 (대부분 추론 중 붕괴로 인한 한자 출력)
  - 1개 데이터는 7번의 재시도 후에도 계속 한자가 포함되었으므로, 불가피하게 학습 데이터에서 제거

여전히 52개 데이터는 신뢰할 수 있는 답과 차이가 있으나, 원본 데이터 역시 r1의 답이 항상 옳았던 것은 아니며, solution 역시 정답이라고 확신할 수 없음

---

### Formatted

- **EXAONE 포맷**에 맞게 text 컬럼을 추가, 공식 코드(https://github.com/simplescaling/s1) 사용 가능하도록 변경