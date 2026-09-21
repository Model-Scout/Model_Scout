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
- 24 Layers, 768 hidden dim, 3072 intermediate, 12 heads, 51200 vocab size
- 1024 max_seq_len
- 파라미터 수: 237M

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
model_name = "heegyu/kogpt-j-base-24L"
pipe = pipeline('text-generation', model=model_name)
print(pipe("안녕하세요", repetition_penalty=1.2, do_sample=True, eos_token_id=1, early_stopping=True, max_new_tokens=128))
print(pipe("오늘 정부 발표에 따르면, ", repetition_penalty=1.2, do_sample=True, eos_token_id=1, early_stopping=True, max_new_tokens=128))
print(pipe("싸늘하다. 가슴에 비수가 날아와 꽂힌다. ", repetition_penalty=1.2, do_sample=True, eos_token_id=1, early_stopping=True, max_new_tokens=128, min_length=64))
```
결과
```bash
[{'generated_text': '안녕하세요?\n우선은\n네.\n뭐~ 이런 부분들이\n네.\n좀 어~ 영향을 많이 받는 거 같다는 생각이 좀 듭니다.\n네.\n네.\n어~ 우리 윤종천 교수님께서 먼저 정리를 해주셨잖아요.\n네.\n어~ 사실은 인제 아까 우 교수님 말씀하신 것처럼 좀 이런 게 그~\n사실은\n네.\n그~ 한 가지 문제가 더 있는데 그~ 어~ 인제\n음\n이제 아까 이혜정 선생님이 말씀하신 것처럼 이제 어떤 부분에 대한 어~ 그런 저~ 그런 어~ 인제 그~ 이런 부분들이 있는 것 같구요.\n네.\n그래서 어떤 부분에 이제'}]
[{'generated_text': '오늘 정부 발표에 따르면, ㎡당 평균 분양가는 1천215만4천원으로, 1천209만8천원에 해당하는 서울시 강동구 둔촌주공을 재건축하는 둔촌주공 아파트가 재건축 후 최고가를 기록했다.\n동부준공 임대의 경우 분양가가 1천262만5천원이며, 2천만~3천600만원에 달하는 강남구 개포동 개포 주공아파트(옛 개포 주공2단지)의 경우는 1천208만6천원으로 1천208만7천원인 대치동 은마아파트(개포시영아파트)의 절반에도 미치지 못했다.\n반면 개포동 개'}]
[{'generated_text': '싸늘하다. 가슴에 비수가 날아와 꽂힌다. 詩人은 시커멓고 불길하다.\n詩는 꽃 중의 꽃\n詩人은 꽃은 다 시커멓고 불길하다.\n詩人은 시커멀고 불길하다.\n詩無詩無詩無詩無\n詩無詩無詩無詩無\n(고은, 「서정에서 시로」)\n서정에 대한 시비, 시에 대한 시비, 시에 대한 시비가 있는데, 이 두 시비가 시인이 시인지 아닌지 시비인지 아닌지 판가름하는 잣대를 지녔다.\n나는 시인의 삶 속에서 이 시인들의 삶과 시를 바라보며 시인이 무엇을 추구'}]
```
## 주의사항
이 모델의 학습 데이터는 각종 차별/혐오 데이터가 포함됐을 수 있으며, 별도의 제거작업을 진행하지 않았습니다. 따라서 모델이 생성하는 문장에 특정 인물이나 인종, 성별, 장애에 따른 차별/혐오발언을 생성할 수 있습니다.