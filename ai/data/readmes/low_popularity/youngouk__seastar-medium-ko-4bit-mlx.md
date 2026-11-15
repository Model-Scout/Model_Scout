---
license: apache-2.0
language:
- ko
library_name: mlx
tags:
- whisper
- mlx
- quantized
- 4bit
- korean
- speech-recognition
- automatic-speech-recognition
base_model: seastar105/whisper-medium-ko-zeroth
---

# Whisper Medium Korean (Zeroth fine-tune) — MLX 4bit

한국어 음성 인식을 위한 [Whisper Medium](https://huggingface.co/openai/whisper-medium) fine-tune 모델을 Apple MLX 프레임워크용으로 **4bit 양자화**한 버전입니다.

원본: [`seastar105/whisper-medium-ko-zeroth`](https://huggingface.co/seastar105/whisper-medium-ko-zeroth) (Whisper Medium을 Zeroth Korean 데이터셋으로 fine-tune)

## 요약

- **베이스**: Whisper Medium (769M 파라미터)
- **Fine-tune**: Zeroth Korean ASR corpus
- **양자화**: 4bit (group size 64), `mlx-examples/whisper/convert.py` 사용
- **디스크 크기**: **831 MB** (원본 fp16 2.8GB 대비 약 70% 감소)
- **추론 RAM**: ~1.26 GB
- **프레임워크**: Apple MLX (Apple Silicon 전용)

## 한국어 성능 (Zeroth Korean test split)

| 지표 | 값 |
|------|------|
| **CER** | **1.25%** |
| **WER** | **3.21%** |
| **RTF** | 0.055 (M3 16GB 기준) |

원본 fp16 모델과 거의 동일한 정확도를 유지하면서 크기와 메모리를 크게 줄였습니다.

## 사용법

### 1) `mlx-whisper` 직접 호출

```bash
pip install mlx-whisper
```

```python
import mlx_whisper

result = mlx_whisper.transcribe(
    "audio.wav",
    path_or_hf_repo="youngouk/seastar-medium-ko-4bit-mlx",
    language="ko",
    word_timestamps=True,
)
print(result["text"])
```

### 2) `meeting-transcriber` 앱에서 사용

[meeting-transcriber](https://github.com/youngouk/meeting-transcriber)는 이 모델을 기본 선택지로 제공하는 macOS 로컬 회의 전사 앱입니다.

웹 UI에서 `설정 → 음성 인식 모델 (STT) → seastar medium-ko-zeroth (4bit)`를 선택하면 자동 다운로드 및 활성화됩니다.

## 파일 구성

```
config.json              # MLX Whisper 모델 설정 (양자화 파라미터 포함)
weights.safetensors      # 4bit 양자화된 가중치 (~415MB)
```

`mlx-whisper` 런타임이 위 두 파일을 `path_or_hf_repo=` 인자로 바로 로드합니다. 토크나이저는 `mlx-whisper`가 내장한 multilingual vocab을 사용하므로 별도 파일 불필요.

## 양자화 파라미터

```json
{
  "quantization": {
    "bits": 4,
    "group_size": 64
  }
}
```

재현 커맨드:

```bash
python mlx-examples/whisper/convert.py \
  --torch-name-or-path seastar105/whisper-medium-ko-zeroth \
  --mlx-path ./seastar-medium-ko-4bit \
  -q --q-bits 4 --q-group-size 64
```

## 라이선스

Apache License 2.0 — [원본](https://huggingface.co/seastar105/whisper-medium-ko-zeroth) 라이선스를 그대로 승계합니다.

## 제한 사항

- **Apple Silicon 전용**: MLX 프레임워크는 x86 CPU / CUDA에서 동작하지 않습니다. Intel Mac / Linux / Windows 사용자는 원본 [seastar105/whisper-medium-ko-zeroth](https://huggingface.co/seastar105/whisper-medium-ko-zeroth)를 사용하세요.
- **한국어 특화**: Zeroth Korean 데이터셋으로 fine-tune되어 한국어 외 언어 성능은 베이스 Whisper Medium보다 낮을 수 있습니다.
- **4bit 양자화 특성**: 매우 드물게 희귀 어휘에서 원본 fp16보다 약간 낮은 정확도를 보일 수 있습니다 (측정된 CER/WER 차이는 무시 가능한 수준).

## 출처 · 인용

- 원본 Whisper: [OpenAI](https://github.com/openai/whisper)
- 한국어 fine-tune: [seastar105/whisper-medium-ko-zeroth](https://huggingface.co/seastar105/whisper-medium-ko-zeroth)
- 양자화 도구: [mlx-examples/whisper](https://github.com/ml-explore/mlx-examples/tree/main/whisper)
- 재배포: [youngouk](https://huggingface.co/youngouk) for [meeting-transcriber](https://github.com/youngouk/meeting-transcriber)
