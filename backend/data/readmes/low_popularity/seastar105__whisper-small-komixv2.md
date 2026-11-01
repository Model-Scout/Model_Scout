---
library_name: transformers
language:
- ko
base_model:
- openai/whisper-small
---

### Model Description

OpenAI의 whisper-small 모델을 아래 데이터셋으로 학습한 모델입니다. 사용중인 테스트셋 기준으로 평균 성능이 whisper-large-v3보다 좋습니다.

- 한국어 음성 (https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=123)
- 주소 음성 데이터 (https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=71556)
- 주요 영역별 회의 음성인식 데이터 (https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=464)
- 저음질 전화망 음성인식 데이터 (https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=571)
- 방송 콘텐츠 대화체 음성인식 데이터 (https://www.aihub.or.kr/aihubdata/data/view.do?dataSetSn=463)

Training setup

```
train_steps: 50000
warmup_steps: 500
lr scheduler: linear warmup cosine decay
max learning rate: 1e-4
batch size: 1024
max_grad_norm: 1.0
adamw_beta1: 0.9
adamw_beta2: 0.98
adamw_eps: 1e-6
```

### Evaluation

https://github.com/rtzr/Awesome-Korean-Speech-Recognition

위 레포지토리에서 주요 영역별 회의 음성을 제외한 테스트셋 결과입니다. 아래 테이블에서 whisper_small_komixv2가 본 모델 성능입니다.


|         Model          | Average | cv_15_ko | fleurs_ko | kcall_testset | kconf_test | kcounsel_test | klec_testset | kspon_clean | kspon_other |
|------------------------|---------|----------|-----------|---------------|------------|---------------|--------------|-------------|-------------|
|      whisper_tiny      |  36.63  |  31.03   |   18.48   |     58.57     |   36.02    |     33.52     |    35.74     |    42.22    |    37.42    |
|  whisper_tiny_komixv2  |   11.6  |  14.56   |    6.54   |      9.12     |   13.19    |     11.62     |    13.16     |    12.13    |    12.52    |
|      whisper_base      |  40.61  |  22.45   |    15.7   |     85.94     |   41.95    |     32.38     |    39.24     |    46.92    |    40.29    |
|  whisper_base_komixv2  |   8.73  |  10.27   |    5.14   |      6.23     |   10.86    |      7.01     |    10.38     |     9.98    |     9.99    |
|     whisper_small      |  17.52  |  11.56   |    6.33   |     30.79     |   18.96    |     13.57     |    18.71     |    22.02    |    18.23    |
| whisper_small_komixv2  |   7.36  |   7.07   |    4.19   |      5.6      |    9.67    |      5.5      |     8.55     |     9.26    |     9.07    |
|     whisper_medium     |  13.92  |   8.2    |    4.38   |     25.73     |   15.66    |      10.1     |     14.9     |    17.16    |    15.22    |
| whisper_medium_komixv2 |   7.3   |   6.62   |    4.52   |      5.85     |    9.42    |      5.47     |     8.38     |     9.19    |     8.97    |
|    whisper_large_v3    |   7.99  |   5.11   |    3.72   |      5.45     |    9.35    |      3.83     |     8.46     |    15.08    |    12.89    |
| whisper_large_v3_turbo |  10.75  |   5.38   |    3.99   |     10.93     |   10.27    |      4.21     |     9.42     |    26.66    |    15.16    |


### Acknowledgement
- 본 모델은 구글의 TRC 프로그램의 지원으로 학습했습니다.
- Research supported with Cloud TPUs from Google's TPU Research Cloud (TRC)