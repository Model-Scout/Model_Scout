---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model:
- LiquidAI/LFM2-8B-A1B-smoltalk-LoRA
base_model_relation: quantized
tags:
- gguf
- llama.cpp
- lfm2
- lfm2-moe
- moe
- mixture-of-experts
- liquid-ai
- smoltalk
- lora-merged
datasets: HuggingFaceTB/smoltalk
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
pipeline_tag: text-generation
---
Ce dépôt contient les quantifications au format GGUF du modèle [LiquidAI/LFM2-8B-A1B-smoltalk-LoRA](https://huggingface.co/LiquidAI/LFM2-8B-A1B-smoltalk-LoRA).

⚙️ Paramètres de génération recommandés (LFM2)
Temperature = 0.3
Min_p = 0.15
Repetition_penalty = 1.05

🛠️ Méthode de quantization
`merge_and_unload()` de l'adaptateur LoRA dans le base model (PEFT >= 0.19.2.dev0, Transformers main)
Conversion HF → GGUF BF16 via `convert_hf_to_gguf.py`
Quantization via `llama-quantize` (llama.cpp)

📜 Licence
Hérite de la licence du base model : LFM Open License v1.0.

🙏 Remerciements
Liquid AI pour le base model et l'adaptateur LoRA
HuggingFaceTB pour le dataset SmolTalk
llama.cpp pour la quantization