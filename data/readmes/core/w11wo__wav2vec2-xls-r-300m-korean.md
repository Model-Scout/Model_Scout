---
language: ko
license: apache-2.0
tags:
- automatic-speech-recognition
- generated_from_trainer
- hf-asr-leaderboard
- robust-speech-event
datasets:
- kresnik/zeroth_korean
base_model: Wav2Vec2-XLS-R-300M
model-index:
- name: Wav2Vec2 XLS-R 300M Korean
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: Zeroth Korean
      type: kresnik/zeroth_korean
      args: clean
    metrics:
    - type: wer
      value: 29.54
      name: Test WER
    - type: cer
      value: 9.53
      name: Test CER
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: ko
    metrics:
    - type: wer
      value: 76.26
      name: Test WER
    - type: cer
      value: 38.67
      name: Test CER
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: ko
    metrics:
    - type: wer
      value: 73.18
      name: Test WER
---

# Wav2Vec2 XLS-R 300M Korean

Wav2Vec2 XLS-R 300M Korean is an automatic speech recognition model based on the [XLS-R](https://arxiv.org/abs/2111.09296) architecture. This model is a fine-tuned version of [Wav2Vec2-XLS-R-300M](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the [Zeroth Korean](https://huggingface.co/datasets/kresnik/zeroth_korean) dataset.

This model was trained using HuggingFace's PyTorch framework and is part of the [Robust Speech Challenge Event](https://discuss.huggingface.co/t/open-to-the-community-robust-speech-recognition-challenge/13614) organized by HuggingFace. All training was done on a Tesla V100, sponsored by OVH.

All necessary scripts used for training could be found in the [Files and versions](https://huggingface.co/w11wo/wav2vec2-xls-r-300m-korean/tree/main) tab, as well as the [Training metrics](https://huggingface.co/w11wo/wav2vec2-xls-r-300m-korean/tensorboard) logged via Tensorboard.

## Model

| Model                        | #params | Arch. | Training/Validation data (text) |
| ---------------------------- | ------- | ----- | ------------------------------- |
| `wav2vec2-xls-r-300m-korean` | 300M    | XLS-R | `Zeroth Korean` Dataset         |

## Evaluation Results

The model achieves the following results on evaluation:

| Dataset                          | Loss   | WER    | CER    |
| -------------------------------- | ------ | ------ | ------ |
| `Zeroth Korean`                  | 0.2089 | 29.54% | 9.53%  |
| `Robust Speech Event - Dev Data` | N/A    | 76.26% | 38.67% |

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:

- `learning_rate`: 7.5e-05
- `train_batch_size`: 8
- `eval_batch_size`: 8
- `seed`: 42
- `gradient_accumulation_steps`: 4
- `total_train_batch_size`: 32
- `optimizer`: Adam with `betas=(0.9, 0.999)` and `epsilon=1e-08`
- `lr_scheduler_type`: linear
- `lr_scheduler_warmup_steps`: 2000
- `num_epochs`: 50.0
- `mixed_precision_training`: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |  Wer   |  Cer   |
| :-----------: | :---: | :---: | :-------------: | :----: | :----: |
|    19.7138    | 0.72  |  500  |     19.6427     |  1.0   |  1.0   |
|    4.8039     | 1.44  | 1000  |     4.7842      |  1.0   |  1.0   |
|    4.5619     | 2.16  | 1500  |     4.5608      | 0.9992 | 0.9598 |
|     4.254     | 2.88  | 2000  |     4.2729      | 0.9955 | 0.9063 |
|    4.1905     |  3.6  | 2500  |     4.2257      | 0.9903 | 0.8758 |
|    4.0683     | 4.32  | 3000  |     3.9294      | 0.9937 | 0.7911 |
|     3.486     | 5.04  | 3500  |     2.7045      | 1.0012 | 0.5934 |
|     2.946     | 5.75  | 4000  |     1.9691      | 0.9425 | 0.4634 |
|     2.634     | 6.47  | 4500  |     1.5212      | 0.8807 | 0.3850 |
|    2.4066     | 7.19  | 5000  |     1.2551      | 0.8177 | 0.3601 |
|    2.2651     | 7.91  | 5500  |     1.0423      | 0.7650 | 0.3039 |
|    2.1828     | 8.63  | 6000  |     0.9599      | 0.7273 | 0.3106 |
|    2.1023     | 9.35  | 6500  |     0.9482      | 0.7161 | 0.3063 |
|    2.0536     | 10.07 | 7000  |     0.8242      | 0.6767 | 0.2860 |
|    1.9803     | 10.79 | 7500  |     0.7643      | 0.6563 | 0.2637 |
|    1.9468     | 11.51 | 8000  |     0.7319      | 0.6441 | 0.2505 |
|    1.9178     | 12.23 | 8500  |     0.6937      | 0.6320 | 0.2489 |
|    1.8515     | 12.95 | 9000  |     0.6443      | 0.6053 | 0.2196 |
|    1.8083     | 13.67 | 9500  |     0.6286      | 0.6122 | 0.2148 |
|     1.819     | 14.39 | 10000 |     0.6015      | 0.5986 | 0.2074 |
|    1.7684     | 15.11 | 10500 |     0.5682      | 0.5741 | 0.1982 |
|    1.7195     | 15.83 | 11000 |     0.5385      | 0.5592 | 0.2007 |
|    1.7044     | 16.55 | 11500 |     0.5362      | 0.5524 | 0.2097 |
|    1.6879     | 17.27 | 12000 |     0.5119      | 0.5489 | 0.2083 |
|     1.656     | 17.98 | 12500 |     0.4990      | 0.5362 | 0.1968 |
|    1.6122     | 18.7  | 13000 |     0.4561      | 0.5092 | 0.1900 |
|    1.5919     | 19.42 | 13500 |     0.4778      | 0.5225 | 0.1975 |
|    1.5896     | 20.14 | 14000 |     0.4563      | 0.5098 | 0.1859 |
|    1.5589     | 20.86 | 14500 |     0.4362      | 0.4940 | 0.1725 |
|    1.5353     | 21.58 | 15000 |     0.4140      | 0.4826 | 0.1580 |
|    1.5441     | 22.3  | 15500 |     0.4031      | 0.4742 | 0.1550 |
|    1.5116     | 23.02 | 16000 |     0.3916      | 0.4748 | 0.1545 |
|    1.4731     | 23.74 | 16500 |     0.3841      | 0.4810 | 0.1542 |
|    1.4647     | 24.46 | 17000 |     0.3752      | 0.4524 | 0.1475 |
|    1.4328     | 25.18 | 17500 |     0.3587      | 0.4476 | 0.1461 |
|    1.4129     | 25.9  | 18000 |     0.3429      | 0.4242 | 0.1366 |
|    1.4062     | 26.62 | 18500 |     0.3450      | 0.4251 | 0.1355 |
|    1.3928     | 27.34 | 19000 |     0.3297      | 0.4145 | 0.1322 |
|    1.3906     | 28.06 | 19500 |     0.3210      | 0.4185 | 0.1336 |
|     1.358     | 28.78 | 20000 |     0.3131      | 0.3970 | 0.1275 |
|    1.3445     | 29.5  | 20500 |     0.3069      | 0.3920 | 0.1276 |
|    1.3159     | 30.22 | 21000 |     0.3035      | 0.3961 | 0.1255 |
|    1.3044     | 30.93 | 21500 |     0.2952      | 0.3854 | 0.1242 |
|    1.3034     | 31.65 | 22000 |     0.2966      | 0.3772 | 0.1227 |
|    1.2963     | 32.37 | 22500 |     0.2844      | 0.3706 | 0.1208 |
|    1.2765     | 33.09 | 23000 |     0.2841      | 0.3567 | 0.1173 |
|    1.2438     | 33.81 | 23500 |     0.2734      | 0.3552 | 0.1137 |
|    1.2487     | 34.53 | 24000 |     0.2703      | 0.3502 | 0.1118 |
|    1.2249     | 35.25 | 24500 |     0.2650      | 0.3484 | 0.1142 |
|    1.2229     | 35.97 | 25000 |     0.2584      | 0.3374 | 0.1097 |
|    1.2374     | 36.69 | 25500 |     0.2568      | 0.3337 | 0.1095 |
|    1.2153     | 37.41 | 26000 |     0.2494      | 0.3327 | 0.1071 |
|    1.1925     | 38.13 | 26500 |     0.2518      | 0.3366 | 0.1077 |
|    1.1908     | 38.85 | 27000 |     0.2437      | 0.3272 | 0.1057 |
|    1.1858     | 39.57 | 27500 |     0.2396      | 0.3265 | 0.1044 |
|    1.1808     | 40.29 | 28000 |     0.2373      | 0.3156 | 0.1028 |
|    1.1842     | 41.01 | 28500 |     0.2356      | 0.3152 | 0.1026 |
|    1.1668     | 41.73 | 29000 |     0.2319      | 0.3188 | 0.1025 |
|    1.1448     | 42.45 | 29500 |     0.2293      | 0.3099 | 0.0995 |
|    1.1327     | 43.17 | 30000 |     0.2265      | 0.3047 | 0.0979 |
|    1.1307     | 43.88 | 30500 |     0.2222      | 0.3078 | 0.0989 |
|    1.1419     | 44.6  | 31000 |     0.2215      | 0.3038 | 0.0981 |
|    1.1231     | 45.32 | 31500 |     0.2193      | 0.3013 | 0.0972 |
|     1.139     | 46.04 | 32000 |     0.2162      | 0.3007 | 0.0968 |
|    1.1114     | 46.76 | 32500 |     0.2122      | 0.2982 | 0.0960 |
|     1.111     | 47.48 | 33000 |     0.2125      | 0.2946 | 0.0948 |
|    1.0982     | 48.2  | 33500 |     0.2099      | 0.2957 | 0.0953 |
|     1.109     | 48.92 | 34000 |     0.2092      | 0.2955 | 0.0955 |
|    1.0905     | 49.64 | 34500 |     0.2088      | 0.2954 | 0.0953 |

## Disclaimer

Do consider the biases which came from pre-training datasets that may be carried over into the results of this model.

## Authors

Wav2Vec2 XLS-R 300M Korean was trained and evaluated by [Wilson Wongso](https://w11wo.github.io/). All computation and development are done on OVH Cloud.

## Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.10.3
