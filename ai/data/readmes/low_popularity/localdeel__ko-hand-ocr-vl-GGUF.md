---
license: apache-2.0
language:
- ko
- en
base_model: localdeel/ko-hand-ocr-vl
base_model_relation: quantized
pipeline_tag: image-text-to-text
tags:
- ocr
- korean
- handwriting
- hangul
- vision-language
- qwen3.5
- gguf
---

# ko-hand-ocr-vl — 한글 손글씨 OCR 전용 VL 모델 (0.8B) — GGUF

사진을 그대로 넣으면 손글씨를 글자로 돌려주는 **오픈 웨이트** 모델입니다. [Qwen3.5-0.8B](https://huggingface.co/Qwen/Qwen3.5-0.8B) 를 한글 손글씨로 미세조정했고 **구조는 한 칸도 안 바꿨습니다.** 그래서 Qwen3.5 를 올리는 곳 — Ollama, LM Studio, llama.cpp, vLLM, transformers — 에 새 코드 없이 그대로 올라갑니다.

이 저장소는 GGUF 판입니다. safetensors 는 [localdeel/ko-hand-ocr-vl](https://huggingface.co/localdeel/ko-hand-ocr-vl) 에 있습니다.

| 파일 | 크기 | 쓰임 |
|---|---:|---|
| `ko-hand-ocr-vl-Q4_K_M.gguf` | 345MB | 가장 작음 |
| `ko-hand-ocr-vl-Q8_0.gguf` | 570MB | **권장** — 원본과 거의 같음 |
| `mmproj-ko-hand-ocr-vl-F16.gguf` | 195MB | 그림 읽는 몫 — 반드시 같이 |

같은 저장소 계열의 [ko-hand-ocr](https://huggingface.co/localdeel/ko-hand-ocr)(41M)는 **잘라 둔 한 줄**만 읽는 작고 빠른 모델이고, 이것은 **사진 통째**를 읽습니다. 잘라 둔 줄 하나만 읽을 때는 둘이 비슷합니다 — 시험 글씨체는 이것이, 사진 줄 칸은 41M 이 조금 높습니다. 41M 은 받는 크기가 17분의 1이고 GPU 에서 줄을 3.9배 빨리 읽습니다(아래 표, 같은 판에서 잰 값).

> **2026-10-12 — 어휘를 잘라 가벼워졌습니다.** 원본 Qwen3.5 의 어휘 248,077개 가운데 한글·자모·숫자·기호·짧은
> 영문 조각과 학습·시험에 쓰인 토큰만 남겨 59,453개로 줄였습니다(파라미터 853M -> 660M). 다시 학습하지 않은 같은 판이고,
> 시험 글씨체·처음 보는 글씨체·사진 줄 칸·사진 통째에서 **답이 글자 하나까지 같았습니다** — transformers 로도, llama-server
> (Q8_0, 한 줄씩) 로도. 받는 크기는 safetensors 1.63GB -> 1.27GB, Q8_0 774MB -> 570MB, Q4_K_M 505MB -> 345MB 이고, llama.cpp
> 에서 글자를 내는 빠르기가 26~36% 올랐습니다(이 PC, llama-bench). 어휘에서 뺀 긴 영어 낱말로만 지은 줄 200개에서는 173개가
> 같았고 자모 닮음이 98.34 -> 98.01 로 조금 내려갔습니다. **줄 견줌표와 빠르기는 자른 판으로 다시 잰 값이고, 사진 통째와
> 「어디서 돌려도 같은가」 표는 자르기 전에 잰 값입니다**(답이 같아 그대로 둡니다). 자르기 전 판은 이 저장소의 태그
> [`full-vocab`](https://huggingface.co/localdeel/ko-hand-ocr-vl-GGUF/tree/full-vocab) 에 있습니다.

## 얼마나 읽나

모두 **같은 시험지, 같은 PC**(RTX 5060 Laptop 8GB)에서 잰 값입니다. 시험 글씨체는 학습에서 뺀 글꼴이고, 사진 11장은 사람이 실제로 쓴 손글씨이며 **학습에 한 장도 쓰지 않았습니다**(공개하지 않습니다). 자모 닮음은 높을수록, CER(글자 오류율)은 낮을수록 좋습니다.

### 줄 하나씩 — 다른 OCR 과 같은 자로

![같은 시험지로 열 모델을 견준 자모 닮음](charts/bench-vs-accuracy.svg)

| 모델 | 크기 | 시험 글씨체 6벌 (자모 닮음 / CER) | 처음 보는 글씨체 24벌 | 사진 11장 줄 칸 (자모 닮음 / CER) | GPU 줄/초 |
|---|---:|---:|---:|---:|---:|
| **ko-hand-ocr-vl (이것, 660M)** | 1.27GB | 97.0 / 5.8 | 97.4 | 93.4 / 15.8 | 10.8 |
| Qwen3.5-0.8B (미세조정 전 원본) | 1.63GB | 53.0 / 161.8 | 51.4 | 54.2 / 115.3 | 9.6 |
| ko-hand-ocr 단일 모델 (41M, 줄 전용) | 78MB | 96.8 / 7.2 | 97.3 | 94.2 / 13.4 | 42.0 |
| ko-hand-ocr 앙상블 (모델 3개) | 225MB | 97.1 / 6.7 | 97.7 | 96.5 / 8.6 | 8.3 |
| Qwen/Qwen3-VL-2B-Instruct | 3.96GB | 66.6 / 79.1 | 68.0 | 69.9 / 38.3 | 7.3 |
| PaddlePaddle/PaddleOCR-VL-1.6 | 1.79GB | 63.6 / 62.9 | 66.5 | 61.7 / 44.0 | 1.2 |
| ddobokki/ko-trocr | 408MB | 78.2 / 42.3 | 80.4 | 78.5 / 39.2 | 6.1 |
| PaddleOCR PP-OCRv5 (korean) | 13MB | 72.7 / 40.5 | 75.3 | 71.8 / 39.7 | 397.4 |
| EasyOCR (korean) | 15MB | 56.6 / 64.3 | 64.6 | 66.9 / 55.0 | 81.3 |
| Tesseract 5 (kor+eng) | 6MB | 17.7 / 97.3 | 19.7 | 13.2 / 98.6 | — |


2026-10-13 에 열 모델을 같은 PC 에서 한 번에 쟀습니다. 시험 글씨체는 6벌 합쳐 640줄, 줄 칸은 [ko-hand-ocr](https://github.com/jysvai/ko-hand-ocr) 의 줄 자르기로 잘라 모두에게 같은 칸을 줍니다. 상대에게는 모델 카드의 사용법 그대로, 욕심 뽑기(greedy)로 묻습니다. 물음은 Qwen 계열이 「이 이미지에 쓰인 글자를 그대로 읽어 적으세요. 글자만 출력하세요.」, PaddleOCR-VL 이 「OCR:」 입니다.

### 사진 통째

사진 한 장을 원본 그대로 줍니다. 그림은 4,096토큰까지로 줄여 들어갑니다(llama.cpp·Ollama 와 같은 상한). **쪽** 은 쪽의 글자를 다 이어 붙여 견준 값(통째 OCR 을 재는 흔한 자)이고, **줄 짝** 은 읽은 줄을 정답 줄과 짝지어 잰 값입니다. 정답표가 한 줄에 나란히 쓴 「부서: …  성명: …」 을 두 줄로 나눠 적어 두어서, 한 줄로 바르게 읽어도 줄 짝으로는 깎입니다. 상대 VL 둘은 우리 상한을 씌우지 않고 그쪽 기본 그림 크기 그대로 줍니다.

![사진 통째 — 쪽 단위 닮음과 오류율](charts/bench-vl-whole.svg)

| 모델 | 쪽 자모 닮음 | 쪽 CER | 가장 낮은 사진(쪽) | 줄 짝 자모 닮음 |
|---|---:|---:|---:|---:|
| **ko-hand-ocr-vl (이것)** | 94.3 | 15.3 | 78.3 | 95.6 |
| Qwen3.5-0.8B (원본) | 72.7 | 42.1 | 55.3 | 62.1 |
| Qwen3-VL-2B-Instruct | 76.9 | 41.1 | 47.6 | 72.5 |
| PaddleOCR-VL-1.6 | 79.9 | 37.3 | 54.5 | 57.3 |


### 어디서 돌려도 같은가

같은 모델을 받는 길마다 다시 쟀습니다. 양자화나 그림 크기 맞추기가 길마다 달라서 그대로 믿지 않고 쟀습니다(이 표는 글씨체 벌마다 100줄). llama.cpp 쪽(LM Studio·Ollama 포함)이 사진에서 낮은 것은 양자화 탓이 아닙니다 — 양자화 안 한 F16 GGUF 도 같은 값이 나옵니다. 그림 크기를 맞추는 법이 transformers 와 달라서입니다. llama.cpp 는 가로세로 비를 지키며 줄이고 남는 가장자리를 **검정**으로 채우며, 작은 그림을 8토큰까지 줄입니다(이 모델은 64토큰부터 배웠습니다).

그래서 그림 최소·최대 크기(64~4,096토큰)를 `mmproj` 파일 안에 적어 두었습니다(2026-10-09). llama.cpp 와 LM Studio 는 받기만 하면 이 값을 씁니다 — 같은 LM Studio 에서 사진 줄 칸이 90.8 -> 92.5, llama-server 에서 90.9 -> 92.0 으로 올랐습니다. Ollama 0.34.4 는 아직 이 값을 읽지 않아 그대로입니다. 검정 여백은 파일로 바꿀 수 없습니다.

| 돌리는 길 | 시험 글씨체 6벌 | 사진 줄 칸 | 사진 통째 |
|---|---:|---:|---:|
| transformers (bf16, safetensors) | 96.9 | 93.3 | 94.3 |
| llama.cpp `llama-server` — Q8_0 | 96.7 | 92.0 | 91.8 |
| LM Studio — Q8_0, 받은 그대로 (설정 안 건드림) | 96.4 | 92.5 | 91.8 |
| Ollama — `hf.co/…:Q8_0`, 받은 그대로 | 96.2 | 90.9 | 91.8 |


### 어떤 줄을 틀리나

줄 안에 무엇이 들었는지에 따라 나눈 글자 오류율(CER)입니다. 낮을수록 좋습니다.

![갈래별 글자 오류율](charts/bench-vs-kind.svg)

### 빠르기와 덩치

![빠르기와 덩치](charts/bench-vs-speed.svg)

## 벤치마크는 이렇게 쟀습니다

위 숫자가 어디서 나왔는지 다 적습니다. **같은 시험지를 같은 PC 에서, 열 모델을 한 번에** 돌렸고(2026-10-13 14:59) 사진은 학습에 한 장도 쓰지 않았습니다.

### 시험지

| 시험지 | 무엇인가 | 크기 | 학습에 썼나 |
|---|---|---|---|
| 시험 글씨체 6벌 | 무료 손글씨 글꼴 여섯 벌(OFL)로 줄을 그린 그림. 학습 그림과 같은 그리개로 종이 결·기울기·지운 자국 같은 흔들기를 입혔고, 씨앗은 학습에 안 쓰는 고정값입니다 | 640줄 4,448자 | 안 씀. 학습 글꼴 450벌 가운데 이 여섯과 생김새가 닮은 것(닮음 0.7 이상)도 뺐습니다 |
| 처음 보는 글씨체 24벌 | 나눔손글씨 6 · 그 밖 17 · 구글 1 (아래 목록). 같은 방식으로 그림 | 634줄 3,614자 | 안 씀. **모델을 고르는 데도 안 씀** — 그래서 「두루 읽나」를 묻는 자입니다 |
| 사진 11장 — 줄 칸 | 사람이 실제 서식 종이에 손으로 써서 찍은 사진. [ko-hand-ocr](https://github.com/jysvai/ko-hand-ocr) 의 줄 자르기로 잘라 **모두에게 같은 칸**을 줍니다 | 34줄 209자 | 안 씀. 사람 자료라 공개하지 않습니다 |
| 사진 11장 — 통째 | 같은 사진을 자르지 않고 한 장 그대로 | 11장 | 〃 |

![시험 글씨체 시험지](charts/test-sheet.png)

시험 글씨체 줄은 서식에서 실제로 보는 꼴을 섞어 만듭니다. 대략 셋에 하나가 **뜻 없는 음절을 이어 붙인 줄**(이름·상호처럼 언어 지식이 안 통하는 줄 — 획만 보고 읽는 힘을 잽니다), 셋에 하나가 서식 칸(「성명 : …」, 「일자 : 2026.03.17」), 다섯에 하나가 제목·라벨, 나머지가 문장입니다. 숫자·날짜·영문 약어·기호가 섞입니다. 홑자모 줄과 **그 글꼴이 못 그리는 글자가 든 줄**은 뺍니다 — 아무도 맞힐 수 없는 줄이라서입니다(2026-10-08 에 고친 자. 그 전 숫자와 섞어 견주지 않습니다).

사진 쪽 12번째 장(저해상도 인쇄 서식 + 서명)은 손글씨 판독의 목표가 아니라서 **재기만 하고 점수에서는 뺍니다.** 이 모델은 그 장에서 61.3% 입니다.

<details><summary>처음 보는 글씨체 24벌 목록</summary>

나눔브러시스크립트, KCC 도담도담체, 가비아 봄바람체, 그리운 규원체, 그리운 프롬솔, 날쌘돌이체, 세구세구체, 어비 김빠른체, 어비 마츠코체, 어비 스윗체, 어비 은디체, 어비 퀸제이체, 온글잎 공부잘하자나, 온글잎 언즈체, 윤초록우산어린이 민국, 카페24 동동, 학교안심 꾸러기, 학교안심 칠판지우개, 나눔손글씨 기쁨밝음, 나눔손글씨 따뜻한 작별, 나눔손글씨 부장님 눈치체, 나눔손글씨 아빠글씨, 나눔손글씨 외할머니글씨, 나눔손글씨 하람체

</details>

### 점수

| 점수 | 어떻게 셈하나 |
|---|---|
| **자모 닮음** | 읽은 것과 정답을 자모(ㄱ ㅏ ㅁ …)로 풀고 띄어쓰기를 지운 뒤 얼마나 닮았나(파이썬 `difflib` 비율). 「팀」을 「탐」으로 읽으면 자모 셋 가운데 하나만 틀려 0.67 입니다. 줄마다 내서 평균합니다 |
| **CER**(글자 오류율) | 정답이 되도록 고쳐야 하는 글자 수(편집 거리) ÷ 정답 글자 수, 띄어쓰기는 지우고. 줄마다 평균 내지 않고 **글자를 다 모아** 나눕니다. 정답보다 길게 지어내면 100% 를 넘습니다(원본 Qwen3.5 의 161.8% 가 그 경우) |
| 가장 낮은 벌 / 사진 | 평균이 가리는 바닥. 여섯 벌 사이가 몇 점씩 벌어지기 때문에 따로 적습니다 |
| 사진 통째 — 쪽 | 읽은 글자를 쪽 전체로 이어 붙여 정답 전체와 견줍니다(통째 OCR 을 재는 흔한 자) |
| 사진 통째 — 줄 짝 | 읽은 줄과 정답 줄을 가장 닮은 것끼리 짝지어 잽니다. 정답표가 한 줄에 나란히 쓴 두 칸을 두 줄로 적어 두어서, 한 줄로 바르게 읽어도 깎입니다 |

### 장비와 판

| | |
|---|---|
| GPU | NVIDIA GeForce RTX 5060 Laptop GPU (8GB) |
| CPU | AMD Ryzen 7 260 (노트북, 8코어 16스레드) |
| 운영체제 | Windows 11 Pro |
| PyTorch | 2.14.0+cu130 |
| 이 모델 (transformers) | transformers 5.16.1, bfloat16, 욕심 뽑기(greedy), 줄 하나에 최대 64토큰. 사진 통째는 그림을 4,096토큰까지로 줄여 넣음 |
| 물음 | 「이 이미지에 쓰인 글자를 그대로 읽어 적으세요. 글자만 출력하세요.」 |
| llama.cpp | llama.cpp `llama-server` build 11474 (b9acf138a), CUDA |
| LM Studio | LM Studio — 엔진 llama.cpp CUDA 12 2.55.0, 받은 설정 그대로 |
| Ollama | Ollama 0.34.4, 받은 설정 그대로 |

### 모델마다 어떻게 돌렸나

상대는 모두 **모델 카드의 사용법 그대로** 돌렸습니다. 엔진마다 따로 깐 환경에서 돌리고, 시간은 엔진 안에서 잰 값만 셉니다(그림을 넘기는 값은 뺍니다).

| 모델 | 어떻게 |
|---|---|
| ko-hand-ocr 앙상블 | 모델 3개 x 흔들기 셋을 읽고 서로 가장 닮은 답(가운데 답) |
| ko-hand-ocr 단일 모델 | ko-hand-ocr 0.4.1 `Reader`, float32, 빔 5, 흔들기 셋 |
| ddobokki/ko-trocr | transformers, float32, 빔 5, 길이 상한 16 -> 64 로 풀어 줌 |
| PaddleOCR PP-OCRv5 (korean) | paddleocr TextRecognition(korean_PP-OCRv5_mobile_rec) (paddleocr 3.7.0 / paddle 3.4.0) |
| EasyOCR (korean) | easyocr korean_g2 (ko+en), recognize() 에 줄 그림 전체를 한 칸으로 (1.7.2) |
| Tesseract 5 (kor+eng) | tesseract 5.5.3, --oem 1 --psm 7 -l kor+eng |
| PaddlePaddle/PaddleOCR-VL-1.6 | transformers 5.16.1, bfloat16, 물음 'OCR:', 욕심 뽑기, 최대 64토큰 |
| Qwen/Qwen3-VL-2B-Instruct | transformers 5.16.1, bfloat16, 물음 '이 이미지에 쓰인 글자를 그대로 읽어 적으세요. 글자만 출력하세요.', 욕심 뽑기, 최대 64토큰 |
| ko-hand-ocr-vl (Qwen3.5-0.8B 미세조정) | transformers 5.16.1, bfloat16, 물음 '이 이미지에 쓰인 글자를 그대로 읽어 적으세요. 글자만 출력하세요.', 욕심 뽑기, 최대 64토큰 |
| Qwen/Qwen3.5-0.8B | transformers 5.16.1, bfloat16, 물음 '이 이미지에 쓰인 글자를 그대로 읽어 적으세요. 글자만 출력하세요.', 욕심 뽑기, 최대 64토큰 |

### 글씨체마다

합계 하나만 보면 무너지는 글씨체가 가려집니다. 벌마다 줄 수가 다른 것은 못 그리는 줄을 뺐기 때문입니다.

| 글씨체 | 줄 | **이 모델** | 41M 단일 모델 | 41M 앙상블 | ko-trocr (상대 가운데 1등) |
|---|---:|---:|---:|---:|---:|
| 나눔펜스크립트 (NanumPenScript) | 112 | **95.4** | 95.4 | 96.2 | 69.1 |
| 감자꽃 (GamjaFlower) | 112 | **97.2** | 97.9 | 97.9 | 82.1 |
| 하이멜로디 (HiMelody) | 112 | **97.3** | 97.2 | 97.3 | 75.3 |
| 싱글데이 (SingleDay) | 112 | **98.2** | 99.0 | 98.9 | 88.9 |
| 동해독도 (EastSeaDokdo) | 97 | **95.0** | 93.1 | 94.1 | 65.9 |
| 기랑해랑 (KirangHaerang) | 95 | **99.0** | 97.9 | 97.8 | 87.9 |

### 사진마다 (줄 칸, 자모 닮음)

| | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **이 모델** | 94 | 100 | 98 | 82 | 100 | 94 | 89 | 100 | 88 | 91 | 93 |
| 41M 단일 모델 | 94 | 100 | 100 | 96 | 93 | 83 | 94 | 100 | 89 | 87 | 100 |
| 41M 앙상블 | 100 | 100 | 100 | 98 | 100 | 90 | 95 | 97 | 91 | 93 | 98 |

사진은 장마다 서너 줄뿐이라 **한 줄이 한 장 점수를 10점 넘게 움직입니다.** 그래서 사진 쪽 차이는 글씨체 쪽보다 훨씬 덜 믿을 만합니다.

### 빠르기는 이렇게 쟀습니다

- 서른 줄짜리 서류 한 쪽을 기준으로 잽니다. 줄 자르기(CPU, 모두 같은 0.40초) + 읽기입니다.
- GPU 는 묶음을 1·4·8·16·32줄로 바꿔 가며 세 번씩 재고, 카드(8GB) 밖으로 넘치지 않은 것 가운데 줄당 가장 싼 묶음을 씁니다. 이 모델은 16줄 묶음이 가장 싸고, 그때 VRAM 꼭대기는 2.2GB 입니다.
- CPU 는 1·8줄 묶음, 큰 VL 모델은 줄당 1초 안팎이라 1줄만 잽니다.
- **CPU 값은 이 노트북의 그때 상태를 크게 탑니다.** 줄/초 자체보다 같은 판 안의 순서를 봐 주세요.

### 같지 않은 것 — 누구에게 유리한지까지

| 무엇이 | 어떻게 | 누구에게 유리 |
|---|---|---|
| 시험 글꼴 | **우리** 학습에서만 뺐습니다. 상대가 무엇을 보고 배웠는지는 모릅니다 | 상대 |
| 줄 자르기 | 줄 인식기들에게 우리 줄 자르기를 빌려주었습니다 | 상대 |
| 물음 | Qwen3-VL-2B 는 정해 둔 OCR 물음이 없어 셋을 대 보고 가장 잘 읽는 것을 주었습니다 | 상대 |
| 사진 통째 그림 크기 | 우리와 원본은 4,096토큰까지로 줄이고, 상대 VL 둘은 그쪽 기본 크기 그대로 | 상대 |
| 길이 상한 | ko-trocr 의 기본 16글자를 64로 풀어 주었습니다 | 상대 |
| 그리개 | 우리는 시험지와 **같은 그리개**로 만든 합성 그림으로 배웠습니다(글꼴은 다름). 시험 글씨체 쪽은 우리에게 낯익은 꼴입니다 — 그래서 사진 쪽이 가장 깨끗한 견줌입니다 | 우리 |
| 만든 목적 | 상대 VL 은 문서 전체·여러 언어용입니다. 이것은 한글 손글씨 하나만 노렸습니다 | 우리 |

**상대들이 나쁜 모델이라는 뜻이 아닙니다.** 인쇄 문서·표·장면 글자를 읽으라고 만든 모델에 손글씨를 준 것이고, 그 반대(인쇄 문서 전체, 표)는 재지 않았습니다. 재면 이 모델이 질 가능성이 큽니다.

LM Studio·Ollama·llama.cpp 줄은 같은 Q8_0 파일을 받은 설정 그대로 띄우고, 같은 시험지(글씨체 벌마다 100줄)와 같은 사진으로 OpenAI 꼴 API 에 물어 잰 값입니다. LM Studio·Ollama 가 이 저장소에서 받은 Q8_0 과 그림 파일(mmproj)은 올린 파일과 sha256 이 같습니다.


## 쓰는 법

물음은 무엇이든 됩니다(「OCR」, 「글자 읽어 줘」, 영어, 빈 물음). 대답은 **글자만** 줄마다 한 줄로
나옵니다. 생각 칸은 대화 틀에서 늘 닫혀 있어서 생각하는 데 시간을 쓰지 않습니다.
temperature 는 0 으로 두십시오(OCR 은 고르게 뽑으면 틀립니다).

### Ollama

```bash
ollama run hf.co/localdeel/ko-hand-ocr-vl-GGUF:Q8_0
```

그림 읽는 몫과 설정(temperature 0, top_k 1, 맥락 8192)이 같이 받아집니다(저장소의 `params`).

API 로는 그림을 base64 로 넣습니다.

```bash
curl http://localhost:11434/api/chat -d '{"model": "hf.co/localdeel/ko-hand-ocr-vl-GGUF:Q8_0", "stream": false,
  "messages": [{"role": "user", "content": "OCR", "images": ["<base64>"]}]}'
```

### LM Studio

검색에서 `ko-hand-ocr-vl` 을 찾아 `Q8_0` 을 받거나, 명령줄로 받습니다.

```bash
lms get https://huggingface.co/localdeel/ko-hand-ocr-vl-GGUF@q8_0
```

그림 읽는 몫(`mmproj`)이 같이 받아지고(합쳐 765MB), **설정을 하나도 안 바꿔도** 맞게 돕니다 —
생각 칸은 대화 틀에서 닫혀 있고, 가장 그럴듯한 글자 하나만 고르는 설정(`top_k 1`)이 파일에 들어
있습니다. 위 표의 LM Studio 줄이 그렇게 받은 그대로 잰 값입니다. 대화창에 사진을 끌어 놓거나,
서버를 켜고 OpenAI 꼴로 부릅니다.

### llama.cpp

```bash
llama-server -hf localdeel/ko-hand-ocr-vl-GGUF:Q8_0 --temp 0
```

### vLLM

```bash
vllm serve localdeel/ko-hand-ocr-vl --max-model-len 8192 --limit-mm-per-prompt '{"image": 1}'
```

구조가 Qwen3.5-0.8B 그대로라 vLLM 의 Qwen3.5 지원으로 올라갑니다. 이 모델을 만든 PC 에서는
vLLM 이 돌지 않아(Windows) 직접 띄워 보지는 못했습니다.

### transformers

```python
from transformers import AutoModelForImageTextToText, AutoProcessor
from PIL import Image

proc = AutoProcessor.from_pretrained("localdeel/ko-hand-ocr-vl")
model = AutoModelForImageTextToText.from_pretrained("localdeel/ko-hand-ocr-vl", dtype="auto", device_map="auto")
talk = [{"role": "user", "content": [{"type": "image"}, {"type": "text", "text": "OCR"}]}]
text = proc.apply_chat_template(talk, add_generation_prompt=True)
ask = proc(text=[text], images=[Image.open("photo.jpg")], return_tensors="pt").to(model.device)
out = model.generate(**ask, max_new_tokens=512)
print(proc.batch_decode(out[:, ask["input_ids"].shape[1]:], skip_special_tokens=True)[0])
```

OpenAI 꼴 서버(LM Studio·llama-server·Ollama·vLLM)에는 모두 같은 꼴로 묻습니다.

```python
import base64
from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="none")   # 서버 주소만 바꾼다
data = base64.b64encode(open("photo.jpg", "rb").read()).decode()
got = client.chat.completions.create(model="ko-hand-ocr-vl", temperature=0, messages=[{
    "role": "user", "content": [
        {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64," + data}},
        {"type": "text", "text": "OCR"}]}])
print(got.choices[0].message.content)
```

## 어떻게 만들었나

- 원본: Qwen3.5-0.8B (Gated DeltaNet 18층 + 주의 6층, 그림 인코더 1억 개)
- LoRA(r=64, 모든 선형 층 — 그림 인코더 포함), 대답 자리에서만 손실, 학습률 5e-5. 누적 46,000걸음(한 걸음 = 줄 6개 또는 사진 1장)을 여러 차례 이어 돌렸고, 긴 두 차례(20,000걸음씩) 끝마다 마지막 저장 넷을 평균했습니다. 녹여서 내보냄
- 학습 그림은 전부 합성: 손글씨 글꼴 450벌로 그린 한 줄(55%), 한 사람이 종이에 쓴 1~10줄을 책상 위에서 찍은 것처럼 만든 사진(35%, 긴 변 640~2,400px), 인쇄체 줄(10%)
- 지운 자국·획 휘기·기울임·그늘·흐림·JPEG 를 섞었습니다. 시험 글씨체 30벌과 사진은 학습에서 뺐습니다
- 사진처럼 만든 쪽은 한 가로줄에 두세 덩이를 나란히 쓰기도 합니다(「팀: …」 왼쪽, 「이름: …」 오른쪽). 실제 서식이 그렇게 쓰여서, 안 그러면 오른쪽 덩이를 빠뜨렸습니다
- 글꼴이 못 그리는 글자(□·빈칸)가 든 줄은 그 글꼴로 그리지 않습니다. 네모를 그려 놓고 정답에 제 글자를 적으면 못 읽는 자리를 지어내라고 가르치는 꼴이라서입니다
- 둘째 차례(20,000걸음)에는 뜻 없는 글자 줄을 15% 섞었습니다. 흐린 글자를 흔한 낱말로 고쳐 읽는 버릇(인재팀→인사팀)을 줄이려는 것입니다
- 바꾼 설정: 대화 틀의 생각 칸을 늘 닫음, 그림 상한 4,096토큰, `top_k: 1`

## 한계

- **사람 손글씨로는 학습하지 않았습니다.** 글꼴로 그린 손글씨만 봤습니다. 흘려 쓴 글씨, 겹쳐 쓴 글씨는 약합니다.
- 시험 사진이 11장뿐이라 사진 점수의 폭이 큽니다(한 장이 9%p).
- 표·도장·서명 같은 서식 구조는 읽지 않습니다. 글자만 줄마다 냅니다.
- safetensors 의 `mtp.*`(여러 토큰 미리 짐작) 머리는 원본 그대로라 미세조정되지 않았습니다. 답은 안 바뀌지만 짐작이 덜 맞을 수 있습니다. GGUF 에는 없습니다.
- safetensors 를 손수 GGUF 로 바꿀 때 llama.cpp `convert_hf_to_gguf.py` 가 토크나이저를 못 알아봅니다 — 어휘를 잘라 지문이 달라졌기 때문입니다. 원본과 같은 `qwen35` 로 정해 주고 바꾸거나 [GGUF 판](https://huggingface.co/localdeel/ko-hand-ocr-vl-GGUF)을 받습니다.

## 라이선스

Apache-2.0. 원본 Qwen3.5-0.8B 도 Apache-2.0 입니다. 자세한 것은 `NOTICE`.

## English

An **open-weight** Korean handwriting OCR model: give it a photo, get the text back. It is [Qwen3.5-0.8B](https://huggingface.co/Qwen/Qwen3.5-0.8B) fine-tuned on Korean handwriting with **the architecture unchanged**, so anything that runs Qwen3.5 — Ollama, LM Studio, llama.cpp, vLLM, transformers — runs it with no new code.

> **2026-10-12 — vocabulary cut, same answers.** Of the base Qwen3.5 vocabulary (248,077 tokens) we kept Hangul, jamo,
> digits, symbols, short Latin pieces and every token our training and test text uses: 59,453 tokens (853M -> 660M
> parameters). The weights were not retrained, and on the test fonts, the held-out fonts, the photo line crops and the whole
> photos **every answer came out identical, character for character** — through transformers and through llama-server
> (Q8_0, one request at a time). Downloads shrink: safetensors 1.63GB -> 1.27GB, Q8_0 774MB -> 570MB, Q4_K_M 505MB -> 345MB, and llama.cpp
> generates 26–36% faster (this PC, llama-bench). On 200 lines built only from long English words that left the vocabulary,
> 173 came out the same and jamo similarity went 98.34 -> 98.01. **The line table and the speeds were re-measured on the cut
> model; the whole-photo and runtime tables were measured before the cut** (the answers are the same, so they stand). The
> uncut model is at this repo's tag [`full-vocab`](https://huggingface.co/localdeel/ko-hand-ocr-vl-GGUF/tree/full-vocab).

All numbers below are measured on the same test sheets on the same PC. Test fonts were held out of training; the 11 photos are real handwriting, **never used for training**, and not published.

![Character similarity, ten models on the same test sheets](charts/bench-vs-accuracy.svg)

| Model | Size | Test fonts 6 (char. sim. / CER) | Unseen fonts 24 | Photos 11, line crops (sim. / CER) | GPU lines/s |
|---|---:|---:|---:|---:|---:|
| **ko-hand-ocr-vl (this, 660M)** | 1.27GB | 97.0 / 5.8 | 97.4 | 93.4 / 15.8 | 10.8 |
| Qwen3.5-0.8B (base, before fine-tuning) | 1.63GB | 53.0 / 161.8 | 51.4 | 54.2 / 115.3 | 9.6 |
| ko-hand-ocr single model (41M, lines only) | 78MB | 96.8 / 7.2 | 97.3 | 94.2 / 13.4 | 42.0 |
| ko-hand-ocr ensemble (3 models) | 225MB | 97.1 / 6.7 | 97.7 | 96.5 / 8.6 | 8.3 |
| Qwen/Qwen3-VL-2B-Instruct | 3.96GB | 66.6 / 79.1 | 68.0 | 69.9 / 38.3 | 7.3 |
| PaddlePaddle/PaddleOCR-VL-1.6 | 1.79GB | 63.6 / 62.9 | 66.5 | 61.7 / 44.0 | 1.2 |
| ddobokki/ko-trocr | 408MB | 78.2 / 42.3 | 80.4 | 78.5 / 39.2 | 6.1 |
| PaddleOCR PP-OCRv5 (korean) | 13MB | 72.7 / 40.5 | 75.3 | 71.8 / 39.7 | 397.4 |
| EasyOCR (korean) | 15MB | 56.6 / 64.3 | 64.6 | 66.9 / 55.0 | 81.3 |
| Tesseract 5 (kor+eng) | 6MB | 17.7 / 97.3 | 19.7 | 13.2 / 98.6 | — |


Whole photos (original size, capped at 4,096 image tokens). *Page* compares the whole page's text joined together (the usual page-level CER); *line-paired* matches each line read to a label line. The two rival VLMs get their own default image size, not our cap:


![Whole photos](charts/bench-vl-whole.svg)

| Model | Page char. similarity | Page CER | Worst photo (page) | Line-paired similarity |
|---|---:|---:|---:|---:|
| **ko-hand-ocr-vl (this)** | 94.3 | 15.3 | 78.3 | 95.6 |
| Qwen3.5-0.8B (base) | 72.7 | 42.1 | 55.3 | 62.1 |
| Qwen3-VL-2B-Instruct | 76.9 | 41.1 | 47.6 | 72.5 |
| PaddleOCR-VL-1.6 | 79.9 | 37.3 | 54.5 | 57.3 |


Same model, different runtimes (100 lines per font). The llama.cpp family is lower on photos because of image preprocessing, not quantization (the unquantized F16 GGUF scores the same): llama.cpp keeps the aspect ratio and pads the edge with black, and shrinks small images down to 8 tokens, while this model was trained from 64. The `mmproj` now carries the 64-4,096 token limits (2026-10-09), which llama.cpp and LM Studio read on load: photo line crops went 90.8 -> 92.5 in the same LM Studio and 90.9 -> 92.0 in llama-server. Ollama 0.34.4 does not read them yet. The black padding cannot be changed from the file.


| How it runs | Test fonts 6 | Photos, line crops | Photos, whole |
|---|---:|---:|---:|
| transformers (bf16, safetensors) | 96.9 | 93.3 | 94.3 |
| llama.cpp `llama-server` — Q8_0 | 96.7 | 92.0 | 91.8 |
| LM Studio — Q8_0, 받은 그대로 (설정 안 건드림) | 96.4 | 92.5 | 91.8 |
| Ollama — `hf.co/…:Q8_0`, 받은 그대로 | 96.2 | 90.9 | 91.8 |


### How the benchmark was run

- **Same test sheets, same PC, all ten models in one run** (2026-10-13 14:59). GPU: NVIDIA GeForce RTX 5060 Laptop GPU (8GB); CPU: AMD Ryzen 7 260 (laptop, 8 cores); Windows 11; PyTorch 2.14.0+cu130.
- **Test fonts (6):** 640 lines / 4,448 characters drawn with six free handwriting fonts (OFL) held out of training, with paper texture, tilt and strike-through marks; fixed seed never used in training. About a third of the lines are meaningless syllable strings (no language prior to lean on), a third are form fields, the rest titles and sentences, with digits, dates, Latin abbreviations and symbols mixed in. Lines a font cannot draw are dropped.
- **Unseen fonts (24):** 634 lines, never used for training **or for picking models**.
- **Photos (11):** real handwriting on real forms, 34 lines / 209 characters, never used for training and not published. Line crops come from the ko-hand-ocr line cutter, so every model gets the same crops. A 12th photo (low-res printed form + signatures) is measured but not scored.
- **Scores:** character similarity = `difflib` ratio over jamo with spaces removed, averaged per line; CER = edit distance / reference characters, pooled over all characters (can exceed 100% when a model rambles).
- **Rivals** run exactly as their model cards say, in their own environments; timing counts only time inside the engine. Qwen3-VL-2B got the best of three prompts; ko-trocr's 16-char length cap was raised to 64; the rival VLMs read whole photos at their own default size. Our training images come from the same renderer as the font sheets (different fonts), so the photo set is the cleanest comparison.
- **Runtimes:** llama.cpp build 11474, LM Studio (llama.cpp CUDA 12 engine 2.55.0) and Ollama 0.34.4, each with the downloaded Q8_0 file and default settings, 100 lines per font. The Q8_0 and mmproj files LM Studio and Ollama downloaded from this repo match the upload by sha256.

![Test sheet](charts/test-sheet.png)


## Usage

Any prompt works ("OCR", "Read the text", Korean, or empty). The answer is **only the text**, one
line per line. The thinking block is always closed by the chat template, so no time is spent
thinking. Use temperature 0 (sampling makes OCR worse).

- **Ollama**: `ollama run hf.co/localdeel/ko-hand-ocr-vl-GGUF:Q8_0`
- **LM Studio**: search `ko-hand-ocr-vl` or `lms get https://huggingface.co/localdeel/ko-hand-ocr-vl-GGUF@q8_0`. The `mmproj`
  vision file comes with it and it works with **no settings changed** (thinking is closed in the
  template; `top_k 1` is in the file).
- **llama.cpp**: `llama-server -hf localdeel/ko-hand-ocr-vl-GGUF:Q8_0 --temp 0`
- **vLLM**: `vllm serve localdeel/ko-hand-ocr-vl --max-model-len 8192` — same architecture as Qwen3.5-0.8B, so
  vLLM's Qwen3.5 support loads it. Not run by us (the build machine is Windows).
- **transformers**: `AutoModelForImageTextToText` + `AutoProcessor`, as in the Korean section.

**Limits.** Trained on synthetic handwriting only (450 fonts), no real handwriting samples. Only 11 test photos, so the photo scores are noisy. Reads text line by line; does not parse tables or forms. To convert the safetensors to GGUF yourself, set the pre-tokenizer to `qwen35` (the cut vocabulary changes the fingerprint `convert_hf_to_gguf.py` checks); the GGUF repo already has it. License: Apache-2.0 (same as the base model).
