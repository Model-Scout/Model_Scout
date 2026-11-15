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
- GPT2(Flax, Pytorch)
- 12 Layers, 768 hidden dim, 3072 intermediate, 12 heads, 51200 vocab size
- 1024 max_seq_len
- 파라미터 수: 210M

### 성능 벤치마크
<img src="https://github.com/HeegyuKim/language-model/blob/63d8bd7cd39f25e87e0e376cdd18df3f8b460dee/image/benchmark0304.png?raw=true" />

## 학습 환경 및 하이퍼파라미터
- TPU V2-8
- Learning Rate: 5e-4, Batch Size: 512(=64 accum x 8 devices), Scheduler: Linear, WarmUp: 1000 step
- Optimizer: AdamW(adam_beta1=0.9 adam_beta2=0.98, weight_decay=0.01)
- Training Steps: 43247 (3 epoch)
- 학습 토큰 수: 21.11B (43247 * 512 * 1024seq / 1024^3)
- 학습 기간: 2023/1/25 ~ 2023/1/29
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

model_name = "heegyu/ajoublue-gpt2-base-24L"
pipe = pipeline('text-generation', model=model_name)

print(pipe("안녕하세요", repetition_penalty=1.2, do_sample=True, eos_token_id=1, early_stopping=True, max_new_tokens=128))
print(pipe("오늘 정부 발표에 따르면, ", repetition_penalty=1.2, do_sample=True, eos_token_id=1, early_stopping=True, max_new_tokens=128))
print(pipe("싸늘하다. 가슴에 비수가 날아와 꽂힌다. ", repetition_penalty=1.2, do_sample=True, eos_token_id=1, early_stopping=True, max_new_tokens=128, min_length=64))
```
결과
```bash
[{'generated_text': '안녕하세요.\n네.\n어~ 오늘\n제가 많이 알려줘야 되는 시간이긴 한데요.\n\n아 그래요? 네.\n네. 오늘\n예. 어~ 제가 그래서 이 노래 가사를 한번 소개해 드려 보겠습니다. 이게 저 노래처럼 들릴지 모르겠는데요.\n이 노래가\n그래요. 어~ 정말 잘하시네 예.\n저는 이제 아까 저 저기 어유 그~ 우리 홍현희 씨랑 지금 얘기했던 것처럼\n음\n사실 뭐 이런 거 다 이제 제 입으로 막 말씀 드리는 게\n아하\n쉽고 그래서 그냥\n그냥 가볍게 들리실 수도 있겠지만 뭐 그렇게\n이렇게 해서 이렇게 살짝만 짧게 들려 주시면 좋을'}]
[{'generated_text': "오늘 정부 발표에 따르면, 女 5명중 1명은 10대 자녀였다.\n경제협력개발기구(OECD)는 '한국 청소년 흡연율은 20% 안팎으로 OECD 평균보다 낮을 것'이라고 예측했던 바 있다."}]
[{'generated_text': "싸늘하다. 가슴에 비수가 날아와 꽂힌다. 氣가 꺾인다'고 했다.. 한편 한솔그룹은 2014년 말 한화건설과 ㈜효성을 각각 3개 법인으로 분할한 뒤 기업지배구조 개선 작업을 벌여왔다.. 하지만 현재 '한화그룹이 추진하는 태양광사업에 투자할 의향이 없음을 통보해 와 최근 한화그룹 주가는 7% 이상 급락했다'는 이유를 들며 불만을 나타내고 있다.."}]
```

## 주의사항
이 모델의 학습 데이터는 각종 차별/혐오 데이터가 포함됐을 수 있으며, 별도의 제거작업을 진행하지 않았습니다. 따라서 모델이 생성하는 문장에 특정 인물이나 인종, 성별, 장애에 따른 차별/혐오발언을 생성할 수 있습니다.
