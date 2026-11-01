---
license: mit
widget:
- text: "오늘 아침 정부는 발표를 통해"
- text: "0 : 아 배고프다\n"
---
PoC를 위해 학습한 작은 GPT 모델

## 모델 구성
- GPT-Neo-X, Pytorch
- 2 Layers, 512 hidden dim, 2048 intermediate, 8 heads, 8000 vocab size
- 512 max_seq_len
- 모델 크기: 13M

## 학습 데이터셋
- AIHub SNS 대화(747MB)
- AIHub 구어체(435MB)
- 한국어 위키(773MB)
- 나무위키(5.8GB)
- 국립국어원 메신저 대화(21MB)

## 학습 환경 및 하이퍼파라미터
- NVIDIA Tesla T4(16GB VRAM)
- fp 16, deepspeed stage2
- 350000 steps, 2일 17시간 소요
- batch size 32
- learning rate 5e-5, linear scheduler
- 최종 train loss: 3.684
- 학습 코드: https://github.com/HeegyuKim/language-model

### 
<details>
<summary>deepspeed parameter</summary>
<div markdown="1">

```json
{
    "zero_optimization": {
       "stage": 2,
       "offload_optimizer": {
           "device": "cpu",
           "pin_memory": true
       },
       "allgather_partitions": true,
       "allgather_bucket_size": 5e8,
       "reduce_scatter": true,
       "reduce_bucket_size": 5e8,
       "overlap_comm": true,
       "contiguous_gradients": true
    },
    "train_micro_batch_size_per_gpu": "auto",
    "train_batch_size": "auto",
    "steps_per_print": 1000
  }
```

</div>
</details>

### example
```python
from transformers import pipeline

generator = pipeline('text-generation', model='heegyu/kogpt-neox-tiny')

def generate(prefix: str):
    print(generator(prefix, do_sample=True, top_p=0.6, repetition_penalty=1.4, max_length=128, penalty_alpha=0.6)[0]["generated_text"])

generate("0 : 만약 오늘이 ")
generate("오늘 정부가 발표한 내용에 따르면")
generate("수학이란 학자들의 정의에 따라")
generate("영상 보는데 너무 웃겨 ")
```
실행 결과
```
0 : 만약 오늘이 #@이름#가 먼저 자는거면 또 자는건데ㅋ
1 : ㅇㄷㆍ_==
2 : 아까 아침에 일어났어?!!
3 : 아니아니 근데 이따 시간표가 끝날때까지 잤지않게 일주일동안 계속 잠들었엉.. 나도 지금 일어났는데, 너무 늦을듯해. 그러다 다시 일어나서 다행이다
4 : 어차피 2:30분에 출발할것같아요~
5 : 이제 곧 일어낫어요
오늘 정부가 발표한 내용에 따르면, 한참 여부는 "한숨이 살릴 수 있는 게 무엇인가"라는 질문에 대해 말할 것도 없다. 하지만 그건 바로 이러한 문제 때문일 것이다."
실제로 해당 기사에서 나온 바 있다. 실제로 당시 한국에서 이게 사실이 아니라고 밝혔다는 건데도 불구하고 말이다. 기사화되기는 했는데 '한국어'의 경우에도 논란이 있었다. 사실 이 부분만 언급되어있고, 대한민국은 무조건 비난을 하는 것이 아니라 본인의 실수를 저지른다는 것인데 반해 유튜브 채널의 영상에서는 그냥 저런 댓글이 올라오
수학이란 학자들의 정의에 따라 이 교과서에서 교육하는 경우가 많은데, 그 이유는 교수들(실제로 학생들은 공부도 하교할 수 있는 등)을 학교로 삼아 강의실에서 듣기 때문이다.
이 학교의 교사들이 '학교'를 선택한 것은 아니지만 교사가 "학생들의"라는 뜻이다."라고 한다. 하지만 이쪽은 교사와 함께 한 명씩 입학식 전부터 교사의 인생들을 시험해보고 싶다는 의미다. 또한 수학여행에서는 가르칠 수도 있고 수학여행을 갔거나 전공 과목으로 졸업하고 교사는 다른
영상 보는데 너무 웃겨 #@기타#웃기네
0 : ㅋㅌㄱㆍ이별명인듯
1 : ㅠㅜ그렇지뭐? 아빠는 아니고? 왜케 많음... 나도 그럴수가 없어.. 내가 말한건데 ㅎ,, #@이름#씨에스나게놀아주까봐 어제부터 내맘대로해달라햇어 그래서 우리집에서 안쓰럽거든 근데 진짜 많이해서 걱정하지말라고 해줬으면좋
```