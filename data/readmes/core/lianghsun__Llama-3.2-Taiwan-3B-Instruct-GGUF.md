---
license: llama3.2
language:
- zh
- en
- ja
- ko
- fr
- it
- de
base_model:
- lianghsun/Llama-3.2-Taiwan-3B-Instruct
new_version: lianghsun/Llama-3.2-Taiwan-3B-Instruct
pipeline_tag: text-generation
library_name: llama.cpp
tags:
- ROC
- Taiwan
- zh-tw
- llama3.2
- GGUF
- quantization
---

# Model Card for Llama-3.2-Taiwan-3B-Instruct-GGUF

<!-- Provide a quick summary of what the model is/does. -->
**Llama-3.2-Taiwan-3B-Instruct-GGUF** 是 [Llama-3.2-Taiwan-3B-Instruct](https://huggingface.co/lianghsun/Llama-3.2-Taiwan-3B-Instruct) 透過 [llama.cpp](https://github.com/ggerganov/llama.cpp) 轉換之 `.gguf` 量化版本，提供多種量化等級權重，可在 llama.cpp、Ollama、LM Studio 等推論工具中部署，適合本機端使用。

> ⚠️ 規格重點：
> 本模型為 GGUF 量化版本，非原始 fp16／bf16 權重。**已知問題：量化後模型有機率輸出全部簡體中文**。

## Model Details

繁中模型在端側部署時常受限於 GPU 記憶體；本模型對 [Llama-3.2-Taiwan-3B-Instruct](https://huggingface.co/lianghsun/Llama-3.2-Taiwan-3B-Instruct) 進行 GGUF 量化，提供多種精度等級的權重檔，方便使用者依硬體限制與品質需求選擇對應版本。

請依不同 tag 選擇對映之原始非量化版本，最新 main 分支對映 `v2025.01.01`；原始（非量化）模型介紹請參考 [lianghsun/Llama-3.2-Taiwan-3B-Instruct](https://huggingface.co/lianghsun/Llama-3.2-Taiwan-3B-Instruct)。

<details>
  <summary><b>Model Change Log</b></summary>

  | Update Date  | Model Version  | Key Changes |
  |--------------|----------------|-------------|
  | 2025-01-01   | v2025.01.01    | This version corresponds to the `v2025.01.01` release of [Llama-3.2-Taiwan-3B-Instruct](https://huggingface.co/lianghsun/Llama-3.2-Taiwan-3B-Instruct). |
  | 2024-12-11   | v2024.12.11    | This version corresponds to the `v2024.11.27` release of [Llama-3.2-Taiwan-3B-Instruct](https://huggingface.co/lianghsun/Llama-3.2-Taiwan-3B-Instruct). |
</details>

**核心特點 (Key Features)**
1. **多量化等級**：提供 Q4、Q5、Q6、Q8 等不同精度權重，方便依硬體選擇。
2. **本機可部署**：適用於 llama.cpp、Ollama、LM Studio 等推論工具，可在筆電 CPU／Apple Silicon 流暢執行。
3. **與母模型同步更新**：每次 [Llama-3.2-Taiwan-3B-Instruct](https://huggingface.co/lianghsun/Llama-3.2-Taiwan-3B-Instruct) 釋出新版本時同步重新量化。

### Model Description

- **Developed by:** [Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)
- **Base model:** [lianghsun/Llama-3.2-Taiwan-3B-Instruct](https://huggingface.co/lianghsun/Llama-3.2-Taiwan-3B-Instruct)
- **Model type:** LlamaForCausalLM (GGUF)
- **Language(s) (NLP):** Traditional Chinese, English（含其他多語）
- **License:** [llama3.2](https://huggingface.co/meta-llama/Llama-3.2-1B/blob/main/LICENSE.txt)

### Model Sources

- **Repository:** [lianghsun/Llama-3.2-Taiwan-3B-Instruct-GGUF](https://huggingface.co/lianghsun/Llama-3.2-Taiwan-3B-Instruct-GGUF)
- **Original Model:** [lianghsun/Llama-3.2-Taiwan-3B-Instruct](https://huggingface.co/lianghsun/Llama-3.2-Taiwan-3B-Instruct)

## Known Issues

#### How to use in Ollama

直接以 `ollama run` 載入 GGUF 時可能出現「文不對題」現象，根因為預設 chat template 不正確。本 repo 內含 `template` 檔可解決此問題。如需自訂對話模板，請參考 [Ollama Modelfile 文件](https://github.com/ollama/ollama/blob/main/docs/modelfile.md)。

## Citation

```bibtex
@misc{llama_3_2_taiwan_3b_instruct_gguf,
  title        = {Llama-3.2-Taiwan-3B-Instruct-GGUF: Quantized GGUF Version of Llama-3.2-Taiwan-3B-Instruct},
  author       = {Huang, Liang Hsun},
  year         = {2024},
  howpublished = {\url{https://huggingface.co/lianghsun/Llama-3.2-Taiwan-3B-Instruct-GGUF}}
}
```

## Model Card Authors

[Huang Liang Hsun](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)

## Model Card Contact

[Huang Liang Hsun](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)
