---
license: apache-2.0
language:
- ko
library_name: transformers
pipeline_tag: automatic-speech-recognition
tags:
- whisper
---

# whisper-small-ko
  해당 모델은 Whisper Small을 아래의 AI hub dataset에 대해 파인튜닝을 진행했습니다. <br>
  데이터셋의 크기가 큰 관계로 데이터셋을 랜덤하게 섞은 후 5개로 나누어 학습을 진행했습니다. <br>

### Training results

|    Dataset    | Training Loss | Epoch | Validation Loss | Wer     |
|:-------------:|:-------------:|:-----:|:---------------:|:-------:|
| Dataset part1 | 0.1943        |  0.2  | 0.0853          | 9.48    |

### dataset
해당 모델은 AI hub의 많은 데이터셋을 한번에 학습시킨 것이 특징입니다. <br>
ASR은 domain에 대한 의존도가 매우 큽니다. 이 때문에 하나의 데이터셋에 학습을 시키더라도 다른 데이터셋에 대해서 테스트를 진행하면 성능이 크게 떨어지게 됩니다. <br>
이런 부분을 막기 위해 최대한 많은 데이터셋을 한 번에 학습시켰습니다. <br>
추후 사투리나 어린아이, 노인의 음성은 adapter를 활용하면 좋은 성능을 얻을 수 있을 것입니다.

| 데이터셋 이름 | 데이터 샘플 수(train/test) |
| --- | --- |
| 고객응대음성 | 2067668/21092 |
| 한국어 음성 | 620000/3000 |
| 한국인 대화 음성 | 2483570/142399 |
| 자유대화음성(일반남녀) | 1886882/263371 |
| 복지 분야 콜센터 상담데이터 | 1096704/206470 |
| 차량내 대화 데이터 | 2624132/332787 |
| 명령어 음성(노인남여) | 137467/237469 |
| 전체 | 10916423(13946시간)/1206588(1474시간) |


## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 16
- gradient_accumulation_steps: 2
- warmup_ratio: 0.01,
- num_train_epoch: 1