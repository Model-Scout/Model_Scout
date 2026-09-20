---
license: other
license_name: qwen-research
license_link: https://huggingface.co/Qwen/Qwen2.5-3B/blob/main/LICENSE
library_name: gguf
language:
- ko
- en
tags:
- text-generation
- korean
- bilingual
- qwen2
- built-with-qwen
- inheritune
- gguf
- llama-cpp
- quantized
- imatrix
base_model: GuminiResearch/Gumini-1.5B-Base
quantized_by: Gumin Kwon
pipeline_tag: text-generation
---

# 🐻 Gumini-1.5B-Base-i1-GGUF (구미니)

<p align="center">
  <img src="https://img.shields.io/badge/Parameters-1.54B-blue" style="display:inline-block; margin-right:6px;" />
  <img src="https://img.shields.io/badge/Layers-16-green" style="display:inline-block; margin-right:6px;" />
  <img src="https://img.shields.io/badge/Format-GGUF-orange" style="display:inline-block; margin-right:6px;" />
  <img src="https://img.shields.io/badge/Quantization-imatrix-purple" style="display:inline-block; margin-right:6px;" />
  <img src="https://img.shields.io/badge/Built%20with-Qwen-purple" style="display:inline-block; margin-right:6px;" />
</p>

<p align="center">
  <a href="https://linkedin.com/in/devgumin" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Gumin%20Kwon-0A66C2?logo=linkedin&logoColor=white" style="display:inline-block; margin-right:6px;" />
  </a>

  <a href="https://x.com/Gumini_Research" target="_blank">
    <img src="https://img.shields.io/badge/X-@Gumini__Research-black?logo=x&logoColor=white" style="display:inline-block; margin-right:6px;" />
  </a>

  <a href="https://www.instagram.com/gumini_research/" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-gumini__research-E4405F?logo=instagram&logoColor=white" style="display:inline-block;" />
  </a>
</p>


<p align="center"><b>Built with Qwen</b></p>

## Model Description

GGUF quantized versions of [GuminiResearch/Gumini-1.5B-Base](https://huggingface.co/GuminiResearch/Gumini-1.5B-Base) for use with [llama.cpp](https://github.com/ggerganov/llama.cpp) and compatible tools (Ollama, LM Studio, etc.).

All quantizations were created using **importance matrix (imatrix)** calibration for optimal quality preservation.

> This is a **BASE model**, not instruction-tuned.  
> It produces text continuations rather than conversational responses.

## Model Details

| Attribute | Value |
|-----------|-------|
| **Original Model** | [Gumini-1.5B-Base](https://huggingface.co/GuminiResearch/Gumini-1.5B-Base) |
| **Quantized by** | [Gumin Kwon (권구민)](https://linkedin.com/in/devgumin) |
| **Parameters** | 1.54B |
| **Layers** | 16 |
| **Hidden Size** | 2048 |
| **Base PPL (F16)** | 8.48 |

## Quantization Results

### Perplexity Comparison

![PPL Comparison](ppl_comparison.png)

### PPL vs Size Trade-off

![PPL vs Size](ppl_vs_size.png)

### Recommended Quantizations

| Quant | PPL | Size | PPL Δ | Quality | Use Case |
|-------|-----|------|-------|---------|----------|
| **Q8_0** | 8.50 | 1.5G | +0.02 | Excellent | Maximum quality |
| **Q6_K** | 8.52 | 1.2G | +0.04 | Excellent | High quality |
| **Q5_K_M** | 8.61 | 1.1G | +0.13 | Excellent | Balanced (recommended) |
| **Q4_K_M** | 8.72 | 956M | +0.24 | Very Good | Size optimized |
| **IQ4_XS** | 8.79 | 876M | +0.31 | Very Good | imatrix 4-bit |
| **IQ3_M** | 9.09 | 770M | +0.61 | Good | Mobile/Edge |

### All Quantization Results

![Quantization Results](quantization_results.png)

## Comparison: 1B vs 1.5B

| Model | Layers | Params | PPL (F16) | Improvement |
|-------|--------|--------|-----------|-------------|
| Gumini 1B | 10 | 1.08B | 15.36 | - |
| **Gumini 1.5B** | 16 | 1.54B | **8.48** | **45% better** |

The 1.5B model shows significant quality improvement with only 6 additional layers!

## Usage

### With llama.cpp

```bash
# Download
huggingface-cli download GuminiResearch/Gumini-1.5B-Base-i1-GGUF Gumini-1.5B-Base.i1-Q4_K_M.gguf

# Run
./llama-cli -m Gumini-1.5B-Base.i1-Q4_K_M.gguf -p "저는 구미니입니다." -n 100
```

### With Ollama

```bash
echo 'FROM ./Gumini-1.5B-Base.i1-Q4_K_M.gguf' > Modelfile
ollama create gumini-1.5b -f Modelfile
ollama run gumini-1.5b
```

### With LM Studio

1. Download any `.gguf` file from this repo
2. Import into LM Studio
3. Start generating!

## Quantization Guide

![Quantization Types Guide](quant_types_guide.png)

### Tips
- **Best quality**: Use Q8_0 or Q6_K
- **Balanced**: Use Q5_K_M or Q4_K_M
- **Mobile/Edge**: Use IQ4_XS or IQ3_M
- **"i1" prefix**: Indicates imatrix was used during quantization

## Original Model

**Gumini-1.5B** (구미니) is a bilingual Korean-English base language model trained using the *Inheritune* methodology. Starting from **Qwen 2.5 3B**, the model progressively grew from 10 to 16 layers through 7 training stages.

### Inheritune Progressive Layer Growing
```
Stage 0: 10 layers (1.08B) → 393M tokens
Stage 1: 11 layers (1.15B) → 393M tokens
Stage 2: 12 layers (1.23B) → 393M tokens
Stage 3: 13 layers (1.31B) → 393M tokens
Stage 4: 14 layers (1.39B) → 393M tokens
Stage 5: 15 layers (1.47B) → 393M tokens
Stage 6: 16 layers (1.54B) → 786M tokens ⭐
────────────────────────────────────────────
Total: 16 layers, 1.54B params, ~3.14B tokens
```

- **Training Data**: 80% Korean, 20% English

See [GuminiResearch/Gumini-1.5B-Base](https://huggingface.co/GuminiResearch/Gumini-1.5B-Base) for full details.

## License

### Qwen Research License (Non-Commercial)

This model is **Built with Qwen** and derived from Qwen 2.5 3B.

```
Qwen is licensed under the Qwen RESEARCH LICENSE AGREEMENT.
Copyright (c) Alibaba Cloud. All Rights Reserved.
```

**This model is for NON-COMMERCIAL / RESEARCH use only.**  
For commercial use, contact Alibaba Cloud.

## References

### Inheritune Paper
```bibtex
@inproceedings{Sanyal2024inheritune,
  title={Inheritune: Training Smaller Yet More Attentive Language Models},
  author={Sunny Sanyal and Ravid Shwartz-Ziv and Alexandros G. Dimakis and Sujay Sanghavi},
  year={2024},
  url={https://arxiv.org/abs/2404.08634}
}
```

### Qwen 2.5
```bibtex
@misc{qwen2.5,
  title={Qwen2.5: A Party of Foundation Models},
  author={Qwen Team},
  year={2024},
  url={https://qwenlm.github.io/blog/qwen2.5/}
}
```

## Citation

```bibtex
@misc{gumini2025,
  title={Gumini-1.5B: Bilingual Korean-English Language Model via Inheritune},
  author={Gumin Kwon},
  year={2025},
  note={Built with Qwen. Trained with Inheritune progressive layer growing.},
  url={https://huggingface.co/GuminiResearch/Gumini-1.5B-Base-i1-GGUF}
}
```

## Author

**Gumin Kwon (권구민)**  
- 🔗 LinkedIn: https://linkedin.com/in/devgumin  
- 🤗 Hugging Face: https://huggingface.co/GuminiResearch  
- 𝕏 X (Twitter): https://x.com/Gumini_Research  
- 📸 Instagram: https://www.instagram.com/gumini_research/

---

<p align="center">
  <b>Built with Qwen</b><br>
  <i>Gumini - 작지만 똑똑한 AI</i>
</p>