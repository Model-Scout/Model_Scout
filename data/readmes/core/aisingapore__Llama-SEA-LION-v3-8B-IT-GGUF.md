---
library_name: transformers
pipeline_tag: text-generation
base_model:
- aisingapore/Llama-SEA-LION-v3-8B-IT
new_version: aisingapore/Qwen-SEA-LION-v4.5-27B-IT
language:
- en
- zh
- vi
- id
- th
- fil
- ta
- ms
- km
- lo
- my
- jv
- su
license: llama3.1
---

<div>
  <img src="llama_3.1_8b_sea-lion_v3_gguf_banner.png"/>
</div>

# Llama-SEA-LION-v3-8B-IT

[SEA-LION](https://arxiv.org/abs/2504.05747) is a collection of Large Language Models (LLMs) which have been pretrained and instruct-tuned for the Southeast Asia (SEA) region.

Llama-SEA-LION-v3-8B-IT is a multilingual model that has been fine-tuned in two stages on approximately **12.3M English instruction-completion pairs** alongside a pool of **4.5M Southeast Asian instruction-completion pairs** from SEA languages such as Indonesian, Javanese, Sundanese, Tamil, Thai and Vietnamese.

SEA-LION stands for _Southeast Asian Languages In One Network_.

- **Developed by:** Products Pillar, AI Singapore
- **Funded by:** Singapore NRF
- **Model type:** Decoder
- **Languages supported:** Burmese, Chinese, English, Filipino, Indonesia, Javanese, Khmer, Lao, Malay, Sundanese, Tamil, Thai, Vietnamese
- **License:** [Llama 3.1 Community License](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct/blob/main/LICENSE)

## Description

This repo contains `GGUF` format model files for [aisingapore/Llama-SEA-LION-v3-8B-IT](https://huggingface.co/aisingapore/Llama-SEA-LION-v3-8B-IT).

#### Model Weights Included in this repository:
- [Llama-SEA-LION-v3-8B-IT-F16](https://huggingface.co/aisingapore/Llama-SEA-LION-v3-8B-IT-GGUF/blob/main/Llama-SEA-LION-v3-8B-IT-F16.gguf)
- [Llama-SEA-LION-v3-8B-IT-Q2_K](https://huggingface.co/aisingapore/Llama-SEA-LION-v3-8B-IT-GGUF/blob/main/Llama-SEA-LION-v3-8B-IT-Q2_K.gguf)
- [Llama-SEA-LION-v3-8B-IT-Q3_K_M](https://huggingface.co/aisingapore/Llama-SEA-LION-v3-8B-IT-GGUF/blob/main/Llama-SEA-LION-v3-8B-IT-Q3_K_M.gguf)
- [Llama-SEA-LION-v3-8B-IT-Q4_0](https://huggingface.co/aisingapore/Llama-SEA-LION-v3-8B-IT-GGUF/blob/main/Llama-SEA-LION-v3-8B-IT-Q4_0.gguf)
- [Llama-SEA-LION-v3-8B-IT-Q4_K_M](https://huggingface.co/aisingapore/Llama-SEA-LION-v3-8B-IT-GGUF/blob/main/Llama-SEA-LION-v3-8B-IT-Q4_K_M.gguf)
- [Llama-SEA-LION-v3-8B-IT-Q5_0](https://huggingface.co/aisingapore/Llama-SEA-LION-v3-8B-IT-GGUF/blob/main/Llama-SEA-LION-v3-8B-IT-Q5_0.gguf)
- [Llama-SEA-LION-v3-8B-IT-Q5_K_M](https://huggingface.co/aisingapore/Llama-SEA-LION-v3-8B-IT-GGUF/blob/main/Llama-SEA-LION-v3-8B-IT-Q5_K_M.gguf)
- [Llama-SEA-LION-v3-8B-IT-Q6_K](https://huggingface.co/aisingapore/Llama-SEA-LION-v3-8B-IT-GGUF/blob/main/Llama-SEA-LION-v3-8B-IT-Q6_K.gguf)
- [lLlama-SEA-LION-v3-8B-IT-Q8_0](https://huggingface.co/aisingapore/Llama-SEA-LION-v3-8B-IT-GGUF/blob/main/Llama-SEA-LION-v3-8B-IT-Q8_0.gguf)

### Caveats
It is important for users to be aware that our model exhibits certain limitations that warrant consideration. Like many LLMs, the model can hallucinate and occasionally generates irrelevant content, introducing fictional elements that are not grounded in the provided context. Users should also exercise caution in interpreting and validating the model's responses due to the potential inconsistencies in its reasoning.

## Limitations
### Safety
Current SEA-LION models, including this commercially permissive release, have not been aligned for safety. Developers and users should perform their own safety fine-tuning and related security measures. In no event shall the authors be held liable for any claim, damages, or other liability arising from the use of the released weights and codes.

## Technical Specifications
### Fine-Tuning Details
Llama-SEA-LION-v3-8B-IT was tuned using a combination of a full parameter fine-tune, on-policy alignment, and model merges of the best performing checkpoints. The training process for fine-tuning was approximately 1024 GPU hours, on a single node of 8x H100-80GB GPUs.

## Data
Llama-SEA-LION-v3-8B-IT was trained on a wide range of synthetic instructions, alongside publicly available instructions hand-curated by the team with the assistance of native speakers. In addition, special care was taken to ensure that the datasets used had commercially permissive licenses through verification with the original data source. 

### Lineage & Versioning

This model card serves as an immutable record of the final released checkpoint. Consequently, the hardware specifications, compute hours, and precise dataset volumes (such as final filtered instruction counts) reported here reflect the exact production run used to generate this specific artifact. These figures may differ from the aggregate totals, pre-filtered data pools, or preliminary experimental runs (e.g., initial H100 benchmarks) documented in our accompanying research papers.

The training counts and dataset mixture details reported in this model card reflect the exact constructed training pool consumed during this specific model run. Figures may differ slightly from public dataset releases, which represent downloadable open-source subsets of the broader corpus.


## Call for Contributions
We encourage researchers, developers, and language enthusiasts to actively contribute to the enhancement and expansion of SEA-LION. Contributions can involve identifying and reporting bugs, sharing pre-training, instruction, and preference data, improving documentation usability, proposing and implementing new model evaluation tasks and metrics, or training versions of the model in additional Southeast Asian languages. Join us in shaping the future of SEA-LION by sharing your expertise and insights to make these models more accessible, accurate, and versatile. Please check out our GitHub for further information on the call for contributions.

## The Team
Chan Adwin, Cheng Nicholas, Choa Esther, Huang Yuli, Hulagadri Adithya Venkatadri, Lau Wayne, Lee Chwan Ren, Leong Wai Yi, Leong Wei Qi, Limkonchotiwat Peerat, Liu Bing Jie Darius, Montalan Jann Railey, Ng Boon Cheong Raymond, Ngui Jian Gang, Nguyen Thanh Ngan, Ong Brandon, Ong Tat-Wee David, Ong Zhi Hao, Rengarajan Hamsawardhini, Siow Bryan, Susanto Yosephine, Tai Ngee Chia, Tan Choon Meng, Teng Walter, Teo Eng Sipp Leslie, Teo Wei Yi, Tjhi William, Yeo Yeow Tong, Yong Xianbin

## Acknowledgements
[AI Singapore](​​https://aisingapore.org/) is a national programme supported by the National Research Foundation, Singapore and hosted by the National University of Singapore. Any opinions, findings and conclusions or recommendations expressed in this material are those of the author(s) and do not reflect the views of the National Research Foundation or the National University of Singapore. 

## Contact
For more info, please contact us using this [SEA-LION Inquiry Form](https://forms.gle/sLCUVb95wmGf43hi6)

[Link to SEA-LION's GitHub repository](https://github.com/aisingapore/sealion)

## Disclaimer
This is the repository for the commercial instruction-tuned model.
The model has _not_ been aligned for safety.
Developers and users should perform their own safety fine-tuning and related security measures.
In no event shall the authors be held liable for any claims, damages, or other liabilities arising from the use of the released weights and codes.