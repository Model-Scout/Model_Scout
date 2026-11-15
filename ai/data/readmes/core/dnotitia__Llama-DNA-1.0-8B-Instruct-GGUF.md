---
language:
- en
- ko
license: cc-by-nc-4.0
tags:
- dnotitia
- nlp
- llm
- slm
- conversation
- chat
- gguf
base_model:
- dnotitia/Llama-DNA-1.0-8B-Instruct
library_name: transformers
pipeline_tag: text-generation
---

# DNA 1.0 8B Instruct GGUF

<p align="center">
<img src="assets/dna-logo.png" width="400" style="margin: 40px auto;">
</p>

**DNA 1.0 8B Instruct** is a <u>state-of-the-art (**SOTA**)</u> bilingual language model based on Llama architecture, specifically optimized for Korean language understanding and generation, while also maintaining strong English capabilities. The model was developed through a sophisticated process involving model merging via spherical linear interpolation (**SLERP**) with Llama 3.1 8B Instruct, and underwent knowledge distillation (**KD**) using Llama 3.1 405B as the teacher model. It was extensively trained through continual pre-training (**CPT**) with a high-quality Korean dataset. The training pipeline was completed with supervised fine-tuning (**SFT**) and direct preference optimization (**DPO**) to align with human preferences and enhance instruction-following abilities.

<p align="center">
<img src="assets/training-procedure.png" width="600" style="margin: 40px auto;">
</p>

## Quickstart

We offer weights in `F32`, `F16` formats and quantized weights in `Q8_0`, `Q6_K`, `Q5_K`, `Q4_K`, `Q3_K` and `Q2_K` formats.

You can run GGUF weights with `llama.cpp` as follows:

1. Install `llama.cpp`. Please refer to the [llama.cpp repository](https://github.com/ggerganov/llama.cpp) for more details.

2. Download DNA 1.0 8B Instruct model in GGUF format.

```bash
# Install huggingface_hub if not already installed
$ pip install huggingface_hub[cli]

# Download the GGUF weights
$ huggingface-cli download dnotitia/Llama-DNA-1.0-8B-Instruct-GGUF \
    --include "Llama-DNA-1.0-8B-Instruct-Q8_0.gguf" \
    --local-dir .
```

3. Run the model with `llama.cpp` in conversational mode.

```bash
$ llama-cli -cnv -m ./Llama-DNA-1.0-8B-Instruct-Q8_0.gguf \
    -p "You are a helpful assistant, Dnotitia DNA."
```

## Ollama

DNA 1.0 8B Instruct model is compatible with Ollama. You can use it as follows:

1. Install Ollama. Please refer to the [Ollama repository](https://github.com/ollama/ollama) for more details.

2. Run the [model](https://ollama.com/dnotitia/dna) with Ollama.

```bash
$ ollama run dnotitia/dna
```

## Limitations

While DNA 1.0 8B Instruct demonstrates strong performance, users should be aware of the following limitations:

- The model may occasionally generate biased or inappropriate content.
- Responses are based on training data and may not reflect current information.
- The model may sometimes produce factually incorrect or inconsistent answers.
- Performance may vary depending on the complexity and domain of the task.
- Generated content should be reviewed for accuracy and appropriateness.

## License

The model is released under the CC BY-NC 4.0 license. For commercial usage inquiries, please [Contact us](https://www.dnotitia.com/contact/post-form).

## Citation

If you use or discuss this model in your academic research, please cite the project to help spread awareness:

```
@misc{lee2025dna10technicalreport,
      title={DNA 1.0 Technical Report}, 
      author={Jungyup Lee and Jemin Kim and Sang Park and SeungJae Lee},
      year={2025},
      eprint={2501.10648},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2501.10648}, 
}
```