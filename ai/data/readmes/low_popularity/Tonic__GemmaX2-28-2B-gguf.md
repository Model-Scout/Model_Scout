---
license: apache-2.0
language:
- ar
- bn
- cs
- de
- en
- es
- fa
- fr
- he
- hi
- id
- it
- ja
- km
- ko
- lo
- ms
- my
- nl
- pl
- pt
- ru
- th
- tl
- tk
- ur
- vi
- zh
base_model:
- ModelSpace/GemmaX2-28-2B-v0.1
pipeline_tag: translation
library_name: transformers
tags:
- gemma
- translation
- multilingual
- quantized
metrics:
- bleu
- rouge
model-index:
  - name: GemmaX2-28-2B-gguf
    results:
      - task:
          type: translation
        dataset:
          name: google/smol
          type: translation
        metrics:
          - name: ROUGE
            type: translate
            value: 0.6230
        source:
          name: self-eval
          url: https://huggingface.co/Tonic/GemmaX2-28-2B-gguf/blob/main/results_en_es_1740935448.json
  - name: GemmaX2-28-2B-gguf
    results:
      - task:
          type: translation
        dataset:
          name: google/smol
          type: translation
        metrics:
          - name: BLEU
            type: translate
            value: 0.6358
        source:
          name: self-eval
          url: https://huggingface.co/Tonic/GemmaX2-28-2B-gguf/blob/main/results_en_es_1740935448.json
---
# Model Card for GemmaX2-28-2B GGUF Quantizations

## Model Overview

**GemmaX2-28-2B GGUF Quantizations** are a set of quantized variants of `GemmaX2-28-2B-v0.1`, an LLM-based translation model developed by Xiaomi. The original model was finetuned from `GemmaX2-28-2B-Pretrain`, which itself is a continually pretrained version of `Gemma2-2B` using a diverse dataset of 56 billion tokens across 28 languages. These GGUF versions (`f16`, `bf16`, `q8_0`, `tq1_0`, `tq2_0`) were created to optimize the model for efficient inference on resource-constrained environments while preserving translation capabilities.

- **Developed by**: Xiaomi (original model); quantized by Tonic
- **Model Type**: Transformer-based language model, finetuned for translation, quantized to GGUF format
- **Quantization Formats**: `f16` (16-bit float), `bf16` (bfloat16), `q8_0` (8-bit quantization), `tq1_0` (ternary quantization 1), `tq2_0` (ternary quantization 2)
- **Languages**: Arabic, Bengali, Czech, German, English, Spanish, Persian, French, Hebrew, Hindi, Indonesian, Italian, Japanese, Khmer, Korean, Lao, Malay, Burmese, Dutch, Polish, Portuguese, Russian, Thai, Tagalog, Turkish, Urdu, Vietnamese, Chinese
- **License**: [Apache 2.0]
- **Repository**: [Tonic/GemmaX2-28-2B-gguf](https://huggingface.co/Tonic/GemmaX2-28-2B-gguf)

## Model Description

`GemmaX2-28-2B-v0.1` is designed for multilingual machine translation, built on `GemmaX2-28-2B-Pretrain`, which was pretrained on a mix of monolingual and parallel data (56 billion tokens) across 28 languages. The finetuning process used a small, high-quality set of translation instruction data to enhance its performance. These GGUF quantizations were generated using `convert_hf_to_gguf.py`, converting the original Hugging Face model into formats compatible with tools like `llama.cpp` for efficient deployment.

### Quantization Details
- **Source Model**: `ModelSpace/GemmaX2-28-2B-v0.1`
- **Conversion Tool**: `convert_hf_to_gguf.py`
- **Quantization Types**:
  - `f16`: 16-bit floating-point, minimal precision loss, larger file size (~5-7GB).
  - `bf16`: Brain floating-point 16-bit, optimized for certain hardware (e.g., TPUs), similar size to `f16`.
  - `q8_0`: 8-bit quantization, reduced size (~3-4GB), slight precision trade-off.
  - `tq1_0`: Ternary quantization (1-bit), smallest size (~1-2GB), higher precision loss.
  - `tq2_0`: Ternary quantization (2-bit variant), slightly larger than `tq1_0`, balanced size vs. quality.

## Intended Use

These quantized models are intended for:
- **Multilingual Translation**: Translating text across the 28 supported languages.
- **Efficient Inference**: Deployment on edge devices, low-memory systems, or environments with limited compute resources using GGUF-compatible frameworks (e.g., `llama.cpp`).
- **Research**: Studying the trade-offs between quantization levels and translation performance.

### Use Cases
- Real-time translation applications.
- Offline translation on mobile or embedded devices.
- Benchmarking quantized LLM performance in multilingual settings.

## Model Performance

The original `GemmaX2-28-2B-v0.1` model’s performance is detailed in the paper [Multilingual Machine Translation with Open Large Language Models at Practical Scale: An Empirical Study](https://arxiv.org/abs/2502.02481). Quantization introduces varying degrees of performance trade-offs:
- **`f16` and `bf16`**: Near-identical to the original model’s accuracy, with minimal degradation.
- **`q8_0`**: Slight reduction in translation quality, still suitable for most practical applications.
- **`tq1_0` and `tq2_0`**: Noticeable quality loss, best for scenarios prioritizing speed and size over precision.

Exact metrics depend on the downstream task and dataset; users are encouraged to evaluate performance for their specific use case.

## How to Use

### With Transformers (Original Model)
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "ModelSpace/GemmaX2-28-2B-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

text = "Translate this from Chinese to English:\nChinese: 我爱机器翻译\nEnglish:"
inputs = tokenizer(text, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=50)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

### With GGUF (Quantized Models)
Download a GGUF file from `Tonic/GemmaX2-28-2B-gguf` and use it with a GGUF-compatible inference tool like `llama.cpp`:

```bash
# Example with llama.cpp
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
make

# Run inference with q8_0 model
./main -m gemmax2-28-2b-q8_0.gguf -p "Translate from Chinese to English: 我爱机器翻译\nEnglish:""
```

Available files:
- `gemmax2-28-2b-f16.gguf`
- `gemmax2-28-2b-bf16.gguf`
- `gemmax2-28-2b-q8_0.gguf`
- `gemmax2-28-2b-tq1_0.gguf`
- `gemmax2-28-2b-tq2_0.gguf`

## Limitations

- **Language Support**: Only supports the 28 languages listed above; performance on unsupported languages is not guaranteed.
- **Quantization Trade-offs**: Lower-bit quantizations (`tq1_0`, `tq2_0`) may degrade translation quality, especially for complex sentences or rare language pairs.
- **Hardware Compatibility**: `bf16` benefits from specific hardware support (e.g., NVIDIA Ampere GPUs, TPUs); performance may vary otherwise.
- **Future Improvements**: The original authors plan to enhance `GemmaX2-28-2B`’s translation capabilities, which may not be reflected in these quantized versions until updated.

## Citation

For the original model:
```bibtex
@misc{cui2025multilingualmachinetranslationopen,
  title={Multilingual Machine Translation with Open Large Language Models at Practical Scale: An Empirical Study},
  author={Menglong Cui and Pengzhi Gao and Wei Liu and Jian Luan and Bin Wang},
  year={2025},
  eprint={2502.02481},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url={https://arxiv.org/abs/2502.02481},
}
```

For these quantized versions, please also credit:
- **Quantization by**: [Tonic](https://huggingface.co/Tonic)
- **Repository**: [Tonic/GemmaX2-28-2B-gguf](https://huggingface.co/Tonic/GemmaX2-28-2B-gguf)

## Contact

For questions about the original model, refer to Xiaomi’s publication. For issues with the GGUF quantizations, contact Tonic via Hugging Face discussions at `Tonic/GemmaX2-28-2B-gguf`.