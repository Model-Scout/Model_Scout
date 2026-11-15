---
language:
- ko
license: apache-2.0
base_model: TeamUNIVA/qwen3_asr_1.7b_ko
pipeline_tag: automatic-speech-recognition
library_name: mlx-audio
tags:
- mlx
- mlx-audio
- qwen3-asr
- automatic-speech-recognition
- korean
- 8-bit
---

# Qwen3-ASR-1.7B-ko (MLX 8-bit)

[`TeamUNIVA/qwen3_asr_1.7b_ko`](https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko)(Qwen/Qwen3-ASR-1.7B를 한국어로 더 학습한 모델, Apache-2.0, revision `3e66f586033753589c3effeb2c8cbce46a1ddabb`)를 [mlx-audio](https://github.com/Blaizzy/mlx-audio)로 8bit 양자화한 변환본입니다. 모델을 만든 곳은 TeamUNIVA이고, 이 저장소는 변환만 했습니다.

This is an 8-bit MLX conversion of TeamUNIVA's Korean fine-tune of Qwen3-ASR-1.7B. All credit for the model goes to TeamUNIVA and the Qwen team; only the quantization was done here.

## 변환 / Conversion

```bash
python -m mlx_audio.convert --hf-path TeamUNIVA/qwen3_asr_1.7b_ko --mlx-path out \
  -q --q-bits 8 --q-group-size 64 --q-mode affine --model-domain stt
```

양자화 설정은 `mlx-community/Qwen3-ASR-1.7B-8bit`와 같습니다(affine, 8bit, group size 64). 가중치 파일 크기도 같습니다(2,463,307,541 bytes).

## 품질 / Quality

원본 bf16과 같은 구간(한국어 회의 5분)을 비교한 간이 점검만 했습니다. 두 출력의 글자 오류율 차이는 2.5%p였고 반복 루프는 없었습니다. 속도는 bf16보다 약 30% 빨랐고 가중치는 4.7GB에서 2.5GB로 줄었습니다. FLEURS·HiKE·AI Hub 같은 공개 벤치마크로는 재지 않았습니다.
This was only a quick check on a 5-minute Korean meeting (2.5 %p CER difference vs. the bf16 original, no repetition loops, about 30% faster, 4.7GB → 2.5GB). Public benchmarks were not run.

## 쓰는 법 / Usage

```python
from mlx_audio.stt.utils import load
model = load("voyagar/Qwen3-ASR-1.7B-ko-mlx-8bit")
print(model.generate("audio.wav", language="Korean").text)
```

언어 자동 감지(`language=None`)는 영어로 잘못 보고 빈 글을 내는 경우가 있어, 한국어 음성이면 `language="Korean"`으로 고정하거나 빈 글일 때 한국어로 다시 시도하세요.
With automatic language detection the model sometimes guesses English and returns nothing; for Korean speech set `language="Korean"` or retry in Korean on empty output.

## 라이선스 / License

Apache-2.0 (원본과 같음 / same as the original).
