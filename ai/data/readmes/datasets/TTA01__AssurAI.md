---
language:
- ko
license: cc-by-nc-4.0
configs:
  - config_name: default
    data_files:
      - split: eval
        path: "assurai_index.jsonl"
---

# 🧪 AssurAI Dataset Summary

This dataset is a **multimodal benchmark dataset** for evaluating **safety risks in generative AI outputs**.  
It covers four modalities (text, image, audio, video) and provides high-risk prompts, multiple model responses, and human-annotated risk scores (1–5).

> ⚠️ This dataset is provided **for non-commercial, academic and research use only** under the **CC BY-NC 4.0** license.

> 🚨 This dataset contains violent, sexual, hateful, and otherwise harmful or unethical content and is intended solely for safety evaluation and research. Any misuse is strictly prohibited.

## 📚 Dataset Contents

- **Total samples**: **11,480**
  - Text: 9,560  
  - Image: 1,160  
  - Video: 430  
  - Audio: 330  

- **Modalities**: `text`, `image`, `audio`, `video`

- **Risk taxonomy**: 35 AI risk factors grouped into 6 high-level categories (Risk #1–35).

  - **Harmful & Violent Content (#1–6)**  
    Supporting Malicious Organized Groups, Celebrating Suffering, Violent Acts, Depicting Violence,  
    Weapon Usage & Development, Military and Warfare  

  - **Interpersonal Harm (#7–10)**  
    Harassment, Hate Speech, Offensive Language, Perpetuating Harmful Beliefs  

  - **Sensitive & Adult Content (#11–17)**  
    Adult Content, Erotic Content, Non-Consensual Nudity, Monetized Sexual Content,  
    Endangerment, Harm, or Abuse of Children, Child Sexual Abuse,  
    Suicidal and Non-suicidal Self-injury  

  - **Misinformation & Manipulation (#18–25)**  
    Political Persuasion, Influencing Politics, Deterring Democratic Participation, Fraud,  
    Mis/disinformation, Sowing Division, Misrepresentation, Types of Defamation  

  - **Illegal & Unethical Activities (#26–30)**  
    Discriminatory Activities, Unauthorized Privacy Violations,  
    Illegal/Regulated Substances, Illegal Services/Exploitation,  
    Other Unlawful/Criminal Activities  

  - **Socioeconomic & Cognitive Risks (#31–35)**  
    Increased inequality and decline in employment quality,  
    Economic and cultural devaluation of human effort, Competitive dynamics,  
    Overreliance and unsafe use, Loss of human agency and autonomy

- **Per-sample structure (simplified)**:
  - `id`
  - `risk_number`, `risk_factor`, `keyword`, `modality`, `prompt_type`
  - `input`:
    - `input.prompt`: user prompt(s)
  - `output_candidates`:
    - up to 4 model outputs with metadata (e.g., `answer`, `model`, and modality-specific fields)
  - `annotation`:
    - `ref_input_risk_score`, `ref_output_risk_score`
    - annotator-level scores in `annotation.entries`


### 📝 Citation

If you use this dataset, please cite:

> Chae-Gyun Lim, Seung-Ho Han, EunYoung Byun, et al.
> *"AssurAI: Experience with Constructing Korean Socio-cultural Datasets to Discover Potential Risks of Generative AI"*,
> [arXiv:2511.20686](http://arxiv.org/abs/2511.20686)

## ⚖️ License

This dataset is released under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** license.<https://creativecommons.org/licenses/by-nc/4.0/>

- You may **share** and **adapt** the dataset for **non-commercial** purposes with proper attribution.  
- **Commercial use** (e.g., training or fine-tuning commercial models, integrating substantial parts into paid products or services) **requires separate written permission from TTA**.

### 🏛️ Research Institution and Contributors

**Main institution**

- Center for Trustworthy AI, Telecommunications Technology Association (TTA), South Korea  

**Core contributors**

- Chae-Gyun Lim (KAIST, Lead author)
- Seung-Ho Han (KAIST, Co-lead author)
- EunYoung Byun (Center for Trustworthy AI, TTA, Co-lead author)

**Academic partners**

- Prof. Hojin Choi, Prof. Joyce Jiyoung Whang, Prof. HwaJeong Hong, Prof. Joseph Seering, Prof. Uichine Lee, Prof. Juho Kim (KAIST)
- Prof. Jeongyun Han (University of Seoul)
- Prof. Soohyun Cho (Keimyung University)

**Industry partners**

- Selectstar
- Kakao

## 🙏 Acknowledgements

This work was supported by the Ministry of Science and ICT (MSIT), Korea, and supervised by the National IT Industry Promotion Agency (NIPA), as part of the “Development of Safety Evaluation Framework and Dataset for Generative AI” project conducted by TTA.

We sincerely thank all annotators, researchers, engineers, and partner organizations who contributed to the design, construction, and validation of the AssurAI dataset.