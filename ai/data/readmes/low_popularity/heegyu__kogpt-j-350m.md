---
license: mit
widget:
- text: 오늘 아침 정부는 발표를 통해
- text: |
    아 배고프다
datasets:
- heegyu/korean-petitions
- heegyu/namuwiki-extracted
- heegyu/kowikitext
language:
- ko
pipeline_tag: text-generation
---

## 모델 구성
- GPT-J(Flax, Pytorch)
- 20 Layers, 1024 hidden dim, 4096 intermediate, 16 heads, 51200 vocab size
- 1024 max_seq_len
- 파라미터 수: 350M

### 성능 벤치마크
<img src="https://github.com/HeegyuKim/language-model/blob/63d8bd7cd39f25e87e0e376cdd18df3f8b460dee/image/benchmark0304.png?raw=true" />

## 학습 환경 및 하이퍼파라미터
- TPU V2-8
- Learning Rate: 3e-4, Batch Size: 512(=64 accum x 8 devices), Scheduler: Linear, WarmUp: 1000 step
- adam_beta1=0.9 adam_beta2=0.98, weight_decay=0.01
- Training Steps: 43247 (3 epoch)
- 학습 토큰 수: 21.11B (43247 * 512 * 1024seq / 1024^3)
- 학습 기간: 2023/1/25 ~ 2023/1/29

## 학습에 사용한 데이터
- AIHub SNS 대화(730MB)
- AIHub 구어체(422MB)
- AIHub 도서(1.6MB)
- AIHub 대규모 웹데이터 기반 한국어 말뭉치(12GB)
- 한국어 위키(867MB)
- 나무위키(6.4GB)
- 국립국어원 메신저 대화(21MB)
- 국립국어원 일상대화 말뭉치(23MB)
- 국립국어원 문어 말뭉치(3.2GB)
- 국립국어원 구어 말뭉치(1.1GB)
- 국립국어원 신문 말뭉치(~2022, 17GB)
- 청와대 국민청원(525MB)

데이터셋 크기는 전처리한 jsonl파일을 기준으로 함.
총 토큰 수는 약 7B임

## 사용 예시
```python
from transformers import pipeline

model_name = "heegyu/kogpt-j-350m"
pipe = pipeline('text-generation', model=model_name)

print(pipe("안녕하세요", repetition_penalty=1.2, do_sample=True, eos_token_id=1, early_stopping=True, max_new_tokens=128))
print(pipe("오늘 정부 발표에 따르면, ", repetition_penalty=1.2, do_sample=True, eos_token_id=1, early_stopping=True, max_new_tokens=128))
print(pipe("싸늘하다. 가슴에 비수가 날아와 꽂힌다. ", repetition_penalty=1.2, do_sample=True, eos_token_id=1, early_stopping=True, max_new_tokens=128, min_length=64))
```
결과
```bash
[{'generated_text': '안녕하세요?\n네.\n자~ 오늘 그~ 뭐~ 남북정상회담에서 인제 남북 관계와 관련된 발언이죠?\n예. 그렇습니다.\n어~ 그~ 이산가족 문제 관련해서 이산가족 상봉을\n예.\n하는 방안이 좀 가능성이 있지 않아요?\n상당히 가능성이 있죠.\n예. 이~ 구체적으로 어떤 거였나요?\n어~ 먼저 이산가족 상봉을 이제 말씀드리겠습니다.\n예.\n아까 설명드린 것처럼 그~ 이산가족 상\n네.\n그~ 상봉에 대한 그~ 구체적인 방안이 어떻게 결정되는 게 가장 좋을까요?\n우선 상봉 방법부터 얘기를 드리죠.\n'}]
[{'generated_text': '오늘 정부 발표에 따르면, gtx-d d 노선을 창릉과 수서에서 출발하는 등 당초 예정된 노선들을 모두 정차하기로 했다. 지난 2월 국토교통부가 이 노선을 일산·금정·파주 운정역과 직접 연결키로 하면서 일산~동탄, 일산~분당, 일산~양재 구간에 추가 정차할 것이라는 예상이 나왔지만 실제 일산~수서 구간이 정차하기로 확정됐다. gtx-d 노선이 일산~수서역까지 개통되는 것은 이번이 처음이다.. gtx-d 노선과 gtx-a 노선이 모두 개통되면 지하철 5호선의 서울 도심 통과 구간이 추가된다. 현재 gtx-b'}]
[{'generated_text': '싸늘하다. 가슴에 비수가 날아와 꽂힌다. \U000f0854삼국사절요\U000f0855 ‘화살촉이 울버린’의 경우에서 보면, 총소리의 원음은 鐘(종자용 : 송악), 鐘을 비(鐘)라 하고 종자의 발음은 ‘이( )’이다. 이때에서 ‘이(은)로 시작하는 발음’은 ‘이/이’의 음운적 표현이다. ‘이/은→종자용[鐘] → 송악/종자[鐘]→이→종자(鐘) …’이다. 이는 한자어로서 그 발음'}]
```

## 주의사항
이 모델의 학습 데이터는 각종 차별/혐오 데이터가 포함됐을 수 있으며, 별도의 제거작업을 진행하지 않았습니다. 따라서 모델이 생성하는 문장에 특정 인물이나 인종, 성별, 장애에 따른 차별/혐오발언을 생성할 수 있습니다.