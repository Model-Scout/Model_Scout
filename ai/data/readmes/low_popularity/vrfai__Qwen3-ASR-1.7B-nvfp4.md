---
language:
- en
- zh
- fr
- de
- ja
- ko
- vi
- ar
- es
- it
- pt
- ru
- th
- nl
- pl
- tr
- hi
- ms
- sv
- da
- fi
- cs
- fil
- fa
- el
- ro
- hu
- mk
- yue
- id
license: apache-2.0
tags:
- asr
- speech
- quantization
- nvfp4
- nvidia-modelopt
- vllm
base_model: Qwen/Qwen3-ASR-1.7B
pipeline_tag: automatic-speech-recognition
---

# Qwen3-ASR-1.7B NVFP4 Quantized

NVFP4 quantized version of [Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) using [NVIDIA ModelOpt](https://github.com/NVIDIA/Model-Optimizer) (Max calibration algorithm), ready for deployment with [vLLM](https://github.com/vllm-project/vllm).

## Quantization Details

Only the LLM component (`model`, ~1.4B params, 82% of total) is quantized to NVFP4. `audio_tower` and `lm_head` remain in BF16.

| Component | Parameters | Quantized |
|-----------|-----------|-----------|
| `audio_tower` | ~0.3B | No |
| `model` (LLM) | ~1.4B | **NVFP4** |
| `lm_head` | shared | No |

**Calibration algorithm:** Max (per-tensor symmetric, MaxCalibrator)

## Results

### Memory Usage (RTX 5090, `gpu_memory_utilization=0.7`)

| Model | Weights | KV Cache |
|-------|---------|----------|
| BF16  | 3.87 GB | 16.58 GB |
| NVFP4 | 1.99 GB | 18.43 GB |

### WER (760 VIVOS test samples, concurrency=1)

| Model | WER    |
|-------|--------|
| BF16  | 7.34%  |
| NVFP4 | 10.73% |

### Throughput across Concurrency Levels (7168 VIVOS samples)

| Concurrency | BF16 (req/s) | NVFP4 (req/s) |
|-------------|-------------|--------------|
| 1           | 15.42       | 15.77        |
| 256         | 227.88      | 260.87       |
| 512         | 227.50      | 262.87       |
| 1024        | 219.63      | 268.25       |

> NVFP4 achieves highest throughput at high concurrency due to smaller model size freeing more KV cache capacity.

### LLM Output Cosine Similarity vs BF16 (50 samples)

| Model | Cosine Similarity |
|-------|------------------|
| NVFP4 | 0.945            |

## Usage

### Serving with vLLM
```bash
git clone https://github.com/QwenLM/Qwen3-ASR
pip install nvidia-modelopt vllm

qwen-asr-serve vrfai/qwen3asr-nvfp4 \
    --quantization modelopt_fp4 \
    --gpu-memory-utilization 0.7
```

### Inference
```python
import requests, soundfile as sf, io

def transcribe(audio_path, url="http://localhost:8000/v1/audio/transcriptions"):
    audio, sr = sf.read(audio_path)
    buf = io.BytesIO()
    sf.write(buf, audio, sr, format="WAV")
    buf.seek(0)
    r = requests.post(
        url,
        files={"file": ("audio.wav", buf, "audio/wav")},
        data={"model": "vrfai/qwen3asr-nvfp4"},
    )
    return r.json().get("text", "")
```

## References

- [Qwen3-ASR Technical Report](https://arxiv.org/abs/2601.21337)
- [NVIDIA ModelOpt](https://github.com/NVIDIA/Model-Optimizer)
- [Quantization code](https://github.com/VLAOpt/qwen-asr-optimization)

## Quantization Script

The recipes and scripts used to quantize this model can be found in the following repository:
- [VinRobotics/model-quantization-recipes](https://github.com/VinRobotics/model-quantization-recipes/tree/main/recipes/qwen3-asr)