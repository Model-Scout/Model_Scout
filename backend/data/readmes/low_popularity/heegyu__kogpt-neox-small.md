---
license: mit
widget:
- text: "오늘 아침 정부는 발표를 통해"
- text: "0 : 아 배고프다\n"
---
PoC를 위해 학습한 작은 GPT 모델

## 모델 구성
- GPT-Neo-X, Pytorch
- 6 Layers, 768 hidden dim, 3072 intermediate, 12 heads, 8000 vocab size
- 512 max_seq_len
- 모델 크기: 54M

## 학습 데이터셋
- AIHub SNS 대화(747MB)
- AIHub 구어체(435MB)
- 한국어 위키(773MB)
- 나무위키(5.8GB)
- 국립국어원 메신저 대화(21MB)
- 국립국어원 일상대화 말뭉치(29.5MB)
- 국립국어원 문어 말뭉치(2.91GB)
- 국립국어원 구어 말뭉치(1.1GB)
- 청와대 국민청원(651.8MB)

## 학습 환경 및 하이퍼파라미터
- NVIDIA Tesla T4(16GB VRAM)
- fp 16, deepspeed stage2
- 1000000 steps
- 2022/11/24 시작, 2022/12/7 종료, 중간에 2-3일 쉰 듯?
- batch size 8
- learning rate 5e-5, linear scheduler
- 마지막 step train loss: 2.969
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

generator = pipeline('text-generation', model='heegyu/kogpt-neox-small')

def generate(prefix: str):
    print(generator(prefix, do_sample=True, top_p=1.0, repetition_penalty=1.2, max_length=128)[0]["generated_text"])

generate("0 : 만약 오늘이 ")
generate("오늘 정부가 발표한 내용에 따르면")
generate("수학이란 학자들의 정의에 따라")
generate("영상 보는데 너무 웃겨 ")
```
실행 결과
```
0: 만약 오늘이 00시즌 말인데 저기서 계속 보자며 대마스크 들고 가면 되거든요.가족이나 저도 가족이나 친척하고 싶어서 (반사회적용어)을 간첩으로 보내는 장면이 (이름)다.그걸로 인해 동생분은 당연히 아들만 죽인다는 말까지 나오겠지만,엄마는 이 아빠말대로 저 아홉수인데 저 아이가 내 인생에 어떤 아들인지 잘 몰라주고있고 그아이는 누명을 씌우고 엄마는 어차피 살아야해 그리고 엄마 딸
오늘 정부가 발표한 내용에 따르면 ‘정지'의 경우 (이름)이 아닌 가수 출신 가수, 제작자, 연예인, 방송인, 대중에게 큰 사랑을 받고 있다. 지난 2013년 10월 '친정어머니'에서 '고양이가 죽었다'로 데뷔하는 등 반향률 1위를 거머썼던 (이름)((이름) 분), 5월에는 제왕그룹 아이콘 멤버들의 외도 의혹과 고생진 (이름)(노다메 유리코 분)가 등장해 충격을 줬다.. 이밖에 kbs 2tv 새 수목드
수학이란 학자들의 정의에 따라 주위 사람들과 학부생들의 논리를 들어 보게 되는 것이다. 이런 관점에서 보면 인간은 이분법적인 체험을 통해서 본능을 찾거나 동물을 통해 이기심, 자기 감정에 빠져서 자기 생각을 그저 관찰 할 뿐이다. 하지만 이러한 진리는 이미 앞에서 살펴본 대로 그 어느 정도 극복이 가능하고 그 정도의 능력을 갖추는 것이 불가능하다. 즉, 인간은 본능이나 충동에 대한 진리로 이해되지 않는 한 스스로 스스로 자립심과 이기를 포기할 수 없다. 그래서 인간을 보는 안목에서 자신의 생각
영상 보는데 너무 웃겨 #@기타#이웃곀ㄴ데 저기여보가 저희엄마한잔하루에저러며저어서왻음
아 #@이름#아 아 근데도 한통해서
그러게ㅠ 나 저거는 그냥 나아랑사고 #@시스템#검색#
그렇게해
와서 한통함 저도사려구요 저건 어쩌지..? 아님 지금자랑만하는중이에유 그래서 저게머야?
얜 우리집에
```