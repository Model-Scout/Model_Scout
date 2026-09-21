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
- 12 Layers, 768 hidden dim, 3072 intermediate, 12 heads, 51200 vocab size
- 1024 max_seq_len
- 파라미터 수: 163M

### 성능 벤치마크
<img src="https://github.com/HeegyuKim/language-model/blob/63d8bd7cd39f25e87e0e376cdd18df3f8b460dee/image/benchmark0304.png?raw=true" />

## 학습 환경 및 하이퍼파라미터
- TPU V2-8
- Learning Rate: 6e-4, Batch Size: 512(=64 accum x 8 devices), Scheduler: Linear, WarmUp: 1000 step
- Optimizer: AdamW(adam_beta1=0.9 adam_beta2=0.98, weight_decay=0.01)
- Training Steps: 43247 (3 epoch)
- 학습 토큰 수: 21.11B (43247 * 512 * 1024seq / 1024^3)
- 학습 기간: 2023/2/16 ~ 2023/2/18(2일 22시간 소요)
- 학습 코드: https://github.com/HeegyuKim/language-model

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

model_name = "heegyu/kogpt-j-base"
pipe = pipeline('text-generation', model=model_name)

print(pipe("안녕하세요", repetition_penalty=1.2, do_sample=True, eos_token_id=1, early_stopping=True, max_new_tokens=128))
print(pipe("오늘 정부 발표에 따르면, ", repetition_penalty=1.2, do_sample=True, eos_token_id=1, early_stopping=True, max_new_tokens=128))
print(pipe("싸늘하다. 가슴에 비수가 날아와 꽂힌다. ", repetition_penalty=1.2, do_sample=True, eos_token_id=1, early_stopping=True, max_new_tokens=128, min_length=64))
```
결과
```bash
[{'generated_text': "안녕하세요'라는 제목의 영상에서 (이름)는 '10년, 한 달 전쯤 kbs 9시 뉴스와 11시에 뉴스를 하면서 '아침에는 어떤 내용이고 아침이 왜 안 됐냐', '내가 뭘 잘못했느냐' 이런 이야기를 했다. 그런데 kbs '뉴스9'에 나와서 방송국에 사과해야 하는 게 아니냐고 하더라'고 말했다.. 이어'sns 활동을 하면서 이런 질문을 할 정도로 (진정성 없는 사람이라면 방송을 그만 뒀어야 했다)'며 '당시에는 '나도 방송인이 됐는데 왜 나에게 이런 질문과 비판을 하는가'라고 생각했고, 내가 무슨 잘못을 했다고 이렇게 이야기하냐 했다. 그러나 지금 생각해보면 그때 제가"}]
[{'generated_text': '오늘 정부 발표에 따르면, 美 제조업, 내수 모두 하락했다.미 상무부는 지난달 미국의 제조업 수주가 전월대비 0.5% 감소했다고 22일 밝혔다. 이는 직전월과 같은 수치다. 서비스업지수도 0.3% 후퇴하며 증가세를 견인하고 있다. 미국 제조업 수주도 전월에 비해 1포인트 저하한 수준이다.미중 무역전쟁에 따른 불안감이 지속되면서 뉴욕증시가 6주 연속 하락하면서 투자 심리를 악화시켰다.미국 연방준비제도(연준)의 9·12 양적완화(qe) 결정으로 6년반 만에 사상 최대로 늘어난 자금이 시장에 유입되고 있다는 분석이다'}]
[{'generated_text': "싸늘하다. 가슴에 비수가 날아와 꽂힌다. 救國者, 이것이 바로 한비자다, 그대의 용사다」\n『太平御覽』 「答薩於蕭金可書記事大會(太平朝覽)」.\n'아타시메시(Triasmehi…)'라고 하는 이 말은 일본어 '하츠네테키'(ハートとキルス)에 더 가까운 말이다. 일본의 역사학자 다카야마 세이시가 쓴 『토쿠이 테루오미(徳井奥義三)』에서 '도적'"}]
```

## 주의사항
이 모델의 학습 데이터는 각종 차별/혐오 데이터가 포함됐을 수 있으며, 별로의 제거작업을 진행하지 않았습니다. 따라서 모델이 생성하는 문장에 특정 인물이나 인종, 성별, 장애에 따른 차별/혐오발언을 생성할 수 있습니다.
