---
library_name: transformers
license: apache-2.0
language:
- ko
- en
base_model: answerdotai/ModernBERT-base
pipeline_tag: feature-extraction
tags:
- masked-lm
- long-context
- modernbert
- coco-lm
---

# Kiwi COCO-LM

## Table of Contents
1. [Model Summary](#model-summary)
2. [Usage](#usage)
3. [Evaluation](#evaluation)
4. [Limitations](#limitations)
5. [Training](#training)
6. [License](#license)
7. [Citation](#citation)

## Model Summary

Kiwi COCO-LM은 [ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base)를 기반으로 한 한국어·영어 인코더 모델로, 최대 8192 토큰 길이의 입력을 처리할 수 있습니다. ModernBERT-base의 어휘에서 사용 빈도가 낮은 다국어 토큰을 덜어내고 그 자리에 한국어 토큰을 추가한 뒤, 기존 가중치를 이어받아 한국어·영어 말뭉치로 추가 사전학습을 진행했습니다.

추가 사전학습에는 [COCO-LM](https://arxiv.org/abs/2102.08473)의 방법론을 적용했습니다. ELECTRA의 Replaced Token Detection(RTD)은 각 토큰이 치환되었는지 여부만 판별하기 때문에 말뭉치로부터 얻는 학습 신호가 제한적입니다. COCO-LM은 이를 보완하기 위해 치환 여부 판별과 함께 원래 토큰을 복원하는 Corrective Language Modeling(CLM)으로 토큰 수준의 학습을 강화하고, Sequence Contrastive Learning(SCL)으로 시퀀스 수준의 표현도 함께 학습합니다. ModernBERT에 이 학습 방법론을 적용한 결과 Kiwi COCO-LM은 한국어(KLUE)와 영어(GLUE) 벤치마크 모두에서 비슷한 규모의 모델과 견줄 만한 성능을 보입니다([Evaluation](#evaluation) 참고).

이 저장소는 Kiwi COCO-LM의 Discriminator를 제공합니다. 일반적으로는 Discriminator를 다운스트림 태스크에 미세조정하여 사용하지만, Generator가 필요한 경우라면 [Kiwi COCO-LM Generator](https://huggingface.co/kiwi-farm/kiwi-coco-lm-base-generator) 저장소를 참고하시기 바랍니다.

| 종류 | 레이어 개수 | 파라미터 | 설명 |
|---|---|---|---|
| [Generator](https://huggingface.co/kiwi-farm/kiwi-coco-lm-base-generator) | 6 | 80M | Discriminator가 잘 학습할 수 있도록 그럴싸한 노이즈를 생성 |
| [Discriminator](https://huggingface.co/kiwi-farm/kiwi-coco-lm-base) | 22 | 161M | Generator가 생성한 노이즈들을 파악하고 그 안에서 원래 의미를 복원하도록 학습. |

※ 파라미터 개수는 임베딩(64k × 768, 약 49M)을 포함한 값입니다. Discriminator의 파라미터 개수에는 사전학습에만 사용되는 RTD/SCL 헤드(약 1.3M)도 포함되어 있습니다.

## Usage

이 모델은 `transformers` v5 이상에서 사용할 수 있습니다. (토크나이저 설정이 v5 형식으로 저장되어 있어 v4.x에서는 `AutoTokenizer` 로딩이 실패할 수 있습니다.)

```sh
pip install -U "transformers>=5.0.0"
```

### 임베딩 추출

```python
import torch
from transformers import AutoTokenizer, AutoModel

model_id = "kiwi-farm/kiwi-coco-lm-base"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModel.from_pretrained(model_id)

inputs = tokenizer(["키위는 한국어 형태소 분석기입니다.", "Kiwi is a Korean morphological analyzer."], padding=True, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)
cls_embeddings = outputs.last_hidden_state[:, 0]  # [CLS] 토큰 임베딩
```

### 다운스트림 태스크 미세조정

분류, 개체명 인식, 질의응답, 검색 등의 다운스트림 태스크에는 일반적인 BERT 계열 모델과 동일한 방식으로 미세조정하여 사용하면 됩니다.

```python
from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained("kiwi-farm/kiwi-coco-lm-base", num_labels=7)
```

모델을 불러올 때 `rtd_head`, `scl_head` 등 사전학습용 헤드의 가중치가 사용되지 않는다(UNEXPECTED)는 메시지가 출력될 수 있는데, 이는 COCO-LM 사전학습에만 쓰이는 보조 헤드이므로 무시해도 됩니다.

**⚠️ `fill-mask` 사용 관련 주의:** 이 모델은 COCO-LM 방식으로 학습되었기 때문에, 메인 모델은 `[MASK]` 토큰이 아니라 Generator가 치환한 토큰이 섞인 입력을 받아 원래 토큰을 복원(Corrective LM)하도록 학습되었습니다. 따라서 `fill-mask` 파이프라인에 `[MASK]` 토큰을 넣어 빈칸을 채우는 용도로는 적합하지 않으며, 미세조정 후 사용하는 것을 권장합니다.

**⚠️ ModernBERT의 아키텍처는 Flash Attention 2에서 효과적으로 동작하도록 설계되어 있습니다. 따라서  아래와 같이 Flash Attention을 설치한 뒤 사용하는걸 권장합니다:**

```bash
pip install flash-attn
```

## Evaluation

KLUE 태스크 중 일부(모델 크기 Base 기준)
| Model | Avg | YNAT | KLUE-STS | KLUE-NLI | KLUE-NER | KLUE-RE | KLUE-MRC |
|---|---|---|---|---|---|---|---|
|  |  | MacroF1 | PearsonR / F1 | Accuracy | Ent. MacroF1 / Chr. MacroF1 | MicroF1 / AUC | EM / RougeW |
| **Kiwi COCO-LM** | 82.34 | 86.15 | 92.23 / 86.90 | **87.87** | 84.44 / 93.02 | 65.36 / 69.67 | 71.38 / 77.00 |
| **KLUE RoBERTa** | 80.44 | 85.99 | 92.68 / 85.89 | 85.63 | 83.47 / 90.77 | 63.11 / 63.54 | 68.98 / 73.60 |
| **KoELECTRA** | 77.79 | 86.05 | **93.13** / 86.23 | 87.23 | 85.59 / 92.61 | 59.09 / 53.44 | 55.18 / 61.68 |
| **A.X-Encoder** | **82.91** | 85.77 | 92.58 / 86.33 | 87.37 | **87.63** / **93.29** | 65.74 / 68.40 | **74.97** / **79.70** |
| **KF-DeBERTa** | 82.89 | **86.53** | 92.63 / **87.45** | 87.73 | 85.26 / 92.62 | **67.16** / **70.38** | 72.92 / 77.73 |
| **ModernBERT** | 62.36 | 77.05 | 76.63 / 69.62 | 67.40 | 74.96 / 86.15 | 39.40 / 29.13 | 39.51 / 44.02 |
| **mmBERT** | 79.33 | 84.24 | 90.51 / 81.58 | 83.30 | 85.49 / 92.42 | 61.95 / 69.06 | 65.26 / 70.65 |

GLUE 태스크 중 일부
| Model | Avg | SST2 | CoLA | MRPC | STS-B | QQP | MNLI | QNLI | RTE | WNLI |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  | Accuracy | MCC | Accuracy / F1 | PearsonR / SpearmanRho | Accuracy / F1 | Accuracy | Accuracy | Accuracy | Accuracy |
| **Kiwi COCO-LM** | **83.02** | 93.01 | 61.16 | **90.93** / **93.47** | **91.00** / **90.79** | 91.12 / 88.10 | 87.64 | 93.26 | **83.03** | **56.34** |
| **KLUE RoBERTa** | 70.75 | 87.27 | 4.45 | 83.82 / 88.26 | 85.24 / 84.92 | 89.44 / 85.50 | 79.78 | 86.78 | 63.54 | **56.34** |
| **KoELECTRA** | 69.49 | 81.65 | 11.84 | 86.03 / 89.69 | 84.48 / 84.24 | 86.35 / 80.87 | 72.73 | 84.94 | 62.09 | **56.34** |
| **A.X-Encoder** | 74.99 | 90.48 | 24.23 | 85.05 / 89.32 | 87.55 / 87.41 | 90.28 / 86.90 | 83.53 | 91.05 | 66.07 | **56.34** |
| **KF-DeBERTa** | 71.34 | 86.47 | 9.25 | 85.05 / 89.57 | 86.81 / 86.54 | 88.34 / 84.10 | 78.46 | 88.19 | 63.18 | **56.34** |
| **ModernBERT** | 80.30 | **95.30** | **61.92** | 86.52 / 90.30 | 90.00 / 89.95 | 90.83 / 87.74 | **88.73** | **93.34** | 66.43 | 49.30 |
| **mmBERT** | 81.01 | 93.69 | 60.79 | 87.75 / 91.38 | 90.81 / **90.79** | **91.35** / **88.42** | 87.46 | 93.06 | 80.14 | 43.66 |

### Tokenizer

위 표에 나온 모델들의 tokenizer가 한국어와 영어를 얼마나 효율적으로 처리하는지 비교했습니다. 한국어 샘플 문서(6,162 바이트, 534 어절)와 영어 샘플 문서(4,503 바이트, 693 단어)를 토큰화한 결과이며, 자세한 분석 방법과 전체 결과는 [korean-tokenizer-analysis](https://github.com/bab2min/korean-tokenizer-analysis)에서 확인할 수 있습니다.

| Model | 방식 | 전체 vocab 수 | 한글 포함 vocab 수 | 한국어 어절당 토큰 수 | 한국어 토큰당 바이트 수 | 영어 단어당 토큰 수 | 드문 음절 16개 중 UNK 수 |
|---|---|---:|---:|---:|---:|---:|---:|
| **Kiwi COCO-LM** | Byte-level BPE | 64,000 | 26,858 (41.97%) | 2.37 | 4.87 | 1.31 | **0** |
| **KLUE RoBERTa** | WordPiece | 32,000 | 28,445 (88.89%) | 2.41 | 4.79 | 2.54 | 14 |
| **KoELECTRA** | WordPiece | 35,000 | 29,021 (82.92%) | 2.44 | 4.73 | 2.48 | 10 |
| **A.X-Encoder** | WordPiece | 50,000 | 24,084 (48.17%) | 2.54 | 4.54 | 1.89 | **0** |
| **KF-DeBERTa** | WordPiece | 130,000 | 104,522 (80.40%) | **2.19** | **5.26** | 1.62 | 10 |
| **ModernBERT** | Byte-level BPE | 50,368 | 25 (0.05%) | 7.12 | 1.62 | 1.30 | **0** |
| **mmBERT** | BPE (byte fallback) | 256,000 | 2,295 (0.90%) | 3.30 | 3.50 | **1.24** | **0** |

- 토큰 수에는 [CLS], [SEP] 등 특수 토큰을 포함하지 않았습니다. 어절(단어)은 공백 문자로 나눈 단위입니다.
- **드문 음절 16개 중 UNK 수**: `걁`, `겼`, `긂`, `깄`, `뇄`, `렜`, `뢔`, `뢨`, `붴`, `뻤`, `쌘`, `얬`, `칢`, `텼`, `퉜`, `홥`처럼 잘 쓰이지 않는 한글 음절 16개를 각각 토큰화했을 때 `[UNK]`로 처리되어 원래 글자를 잃어버린 음절 수입니다.

Kiwi COCO-LM의 tokenizer는 한국어 어절당 2.37토큰으로, 한국어 전용 WordPiece tokenizer인 KLUE RoBERTa(2.41), KoELECTRA(2.44)와 비슷하거나 조금 더 효율적입니다. 동시에 영어는 단어당 1.31토큰으로, 원본인 ModernBERT(1.30)와 거의 같은 효율을 유지합니다. 한국어 효율이 가장 좋은 KF-DeBERTa(2.19)는 vocab 크기가 Kiwi COCO-LM의 2배가 넘고 영어 효율은 떨어집니다(1.62). 또한 Kiwi COCO-LM의 tokenizer는 Byte-level BPE를 사용하기 때문에 WordPiece 기반 tokenizer와 달리 어떤 글자도 `[UNK]`로 처리되지 않습니다.

한편 ModernBERT는 한글 vocab이 25개뿐이라 한국어를 대부분 UTF-8 바이트 단위로 쪼개며, 어절당 7.12토큰으로 Kiwi COCO-LM보다 약 3배 많은 토큰을 사용합니다. 같은 8192 토큰 길이 안에 담을 수 있는 한국어 텍스트 분량이 그만큼 적다는 뜻입니다.

## Limitations

- 한국어와 영어 위주로 학습되었으며, ModernBERT-base의 어휘 중 사용빈도가 낮은 외국어 토큰을 제거하였기 때문에 그 외 언어에 대한 성능은 보장되지 않습니다.
- 학습 데이터에 웹 커뮤니티 댓글 등 정제되지 않은 텍스트가 포함되어 있어, 모델이 학습 데이터에 존재하는 편향이나 부적절한 표현을 반영할 수 있습니다.
- COCO-LM 방식으로 학습된 인코더 모델이므로 텍스트 생성에는 사용할 수 없으며, `[MASK]` 토큰 기반의 빈칸 채우기 용도로도 적합하지 않습니다. 다운스트림 태스크에 미세조정하여 사용하는 것을 권장합니다.
- 최대 8192 토큰까지 입력 가능하지만, 벤치마크 평가는 주로 짧은 문장/문단 단위 태스크에서 이루어졌습니다.

## Training

- 아키텍처: ModernBERT를 그대로 채용
- 토크나이저: ModernBERT-base의 토크나이저에서 사용빈도가 적은 외국어 토큰들을 덜어내고 한국어 토큰을 추가하여 64k 크기의 Vocab을 구성. 한국어 토큰의 경우 kiwipiepy에서 제공하는 [형태소 경계를 고려한 Byte-level BPE tokenizer](https://bab2min.github.io/kiwipiepy/v0.24.0/kr/bpe_trainer.html)를 이용해 학습
- 가중치 재사용: ModernBERT-base의 가중치를 재사용하고 한국어 & 영어 말뭉치를 추가로 학습하는 방식 사용
- 하드웨어: NVIDIA RTX 4070 Ti SUPER 1대에서 약 1239시간(51일) 학습
- 학습 최적화: [Muon Optimizer에 Stochastic Rounding을 적용](https://github.com/bab2min/muon_sr)하여 Weight, Activation, Gradient, Optimizer State를 모두 BF16 타입으로 학습 진행. Liger Kernel과 Flash Attention 2를 적용하여 학습 속도 최적화.
- SCL 학습 방식 변경: COCO-LM의 Sequence Contrastive Learning(SCL)은 원본 시퀀스의 일부 구간을 잘라낸(crop) 시퀀스와 생성기가 토큰을 치환한 시퀀스를 positive 쌍으로, 배치 내 다른 시퀀스를 negative로 삼아 두 시퀀스의 [CLS] 표현이 가까워지도록 학습하는데 Kiwi COCO-LM에서는 이를 다음과 같이 변경했음:
  - **whole-word crop**: 서브워드 토큰 단위가 아니라 단어(어절) 경계 단위로 crop하여 단어가 중간에 잘리지 않도록 했음.
  - **긴 시퀀스의 구간 crop**: 1,024 토큰보다 긴 시퀀스는 최대 1,024 토큰 길이의 구간을 무작위로 고른 뒤 그 안에서 crop합니다. 긴 시퀀스를 통째로 crop하면 모델이 내용 대신 시퀀스 길이 정보만으로 positive 쌍을 찾아내는 지름길(shortcut)을 학습할 수 있기 때문.
  - **crop 시퀀스에 stop-gradient 적용**: crop 시퀀스는 비교 대상으로만 사용하여 forward만 계산하고 gradient는 흘리지 않음. 따라서 배치 전체(1,024개)의 crop 표현을 activation을 저장하지 않고 미리 계산해 둘 수 있고, 각 micro step의 치환 시퀀스를 1,024개 crop 표현 전체와 대조할 수 있음. 덕분에 GradCache 같은 기법 없이도 16GB VRAM GPU 1대에서 배치 크기 1,024 이상의 대조 학습이 가능했음.
- 길이 혼합 배치 구성: Gradient Accumulation을 16스텝 동안 적용하되 각 스텝별로 Seq Length를 다르게 설정하여 모델이 다양한 길이의 데이터를 효율적으로 보도록 설계하였음. Optimizer 1회 업데이트당 총 1024개의 Sequence를 보게 되며 실제 forward/backward 연산이 진행되는 각각의 Micro 스텝 구성은 아래쪽에 같이 설정하였음.

| Seq Length | Batch Size | Tokens per Batch |
|------------|------------|------------------|
| 8192 | 4 | 32K |
| 8192 | 4 | 32K |
| 8192 | 4 | 32K |
| 8192 | 4 | 32K |
| 4096 | 8 | 32K |
| 4096 | 8 | 32K |
| 2048 | 16 | 32K |
| 2048 | 16 | 32K |
| 1024 | 32 | 32K |
| 1024 | 32 | 32K |
| 512 | 64 | 32K |
| 512 | 64 | 32K |
| 256 | 128 | 32K |
| 256 | 128 | 32K |
| 128 | 256 | 32K |
| 128 | 256 | 32K |
| 총 16 스텝 | 총 1024 배치 | 총 512K 토큰 |

### Training Data
| Language | Dataset | Tokens (1M) |
|----------|---------|------|
| Korean | 한국어 위키백과 | 601.4 |
| Korean | KcBERT 댓글 데이터 | 2747.8 |
| Korean | 한국어 웹 커뮤니티 댓글 | 133.7 |
| Korean | Koreascience.kr 초록 말뭉치 | 214.9 |
| Korean | 나무위키 | 1149.8 |
| Korean | AIHub 대규모 구매도서 말뭉치 | 1118.4 |
| Korean | AIHub 전문분야 말뭉치 | 1608.4 |
| Korean | AIHub 뉴스 말뭉치 | 439.8 |
| Korean | AIHub 대화 말뭉치 | 71.4 |
| Korean | NIK 구어 말뭉치 | 244.7 |
| Korean | NIK 문어 말뭉치 | 1452.2 |
| Korean | NIK 신문 말뭉치 | 2280.2 |
| Korean | NIK 온라인 게시자료 말뭉치 | 80.4 |
| - | Total | 12143.3 |

| Language | Dataset | Tokens (1M) |
|----------|---------|------|
| English | English Wikipedia | 8191.2 |
| Multilingual | FLAN Zero-shot (Train Set, Random Sampled) | 6833.1 |
| - | Total | 15024.3 |

학습 데이터는 약 27.2B 토큰으로 구성되어 있으며, 그 중 한국어 데이터는 12143.3M 토큰을, 영어(및 다국어) 데이터는 15024.3M 토큰을 차지합니다. 학습 데이터가 충분하지 않았기 때문에 동일한 데이터를 총 5 epoch 반복하여 약 136B 토큰을 학습했습니다. 단 동일한 말뭉치를 다시 학습하더라도 입력 자체는 달라지도록 매 epoch마다 random seed를 다르게 주어 마스킹이 적용되는 토큰을 다르게 만들었습니다.

## License

Apache 2.0 license

## Citation

If you use Kiwi COCO-LM in your work, please cite:

```bibtex
@misc{kiwi-coco-lm-2026,
  author       = {Minchul Lee},
  title        = {Kiwi COCO-LM: A Korean-English Long-Context Encoder based on ModernBERT},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/kiwi-farm/kiwi-coco-lm-base}}
}
```

