---
language:
- en
- es
- fr
- de
- pt
- ja
- it
- zh
- ko
- ru
- vi
- nl
- pl
- tr
- ar
- id
- fa
- he
- cs
- th
- hi
- lo
- bn
- km
- ur
- my
- ms
task_categories:
- text-to-audio
- text-retrieval
- audio-classification
- text-classification
extra_gated_prompt: '**Access Restricted: Research Use Only**  

  
  - This dataset is **strictly for academic research purposes** and **is not available for commercial use**.  

  
  **Access Requirements:**  
  
  - You **must** be affiliated with a **non-commercial research institution** (e.g., university, non-profit research center).  
  
  - Your **Hugging Face account must be linked to an institutional email address** (e.g., .edu, .ac, .org).  
  
  - Your application **will be manually reviewed**. If your linked email does not belong to a non-commercial institution, your request **will be rejected**.  
  

  **By requesting access, you confirm that:**  
  
  - You will **not** use this dataset for any **commercial purposes** (e.g., monetized applications, commercial AI training, advertising).  
  
  - You will **not** share, distribute, or publish this dataset in any form.  
  
  - You will **not** modify or create derivative datasets for redistribution.  
  
  - Violating these terms may result in **access revocation and legal consequences**.  
  

  **Applications are manually reviewed.**  

  - For urgent access, please email shangda@mail.ccom.edu.cn from the institutional email address linked to your Hugging Face account to expedite your request.

  - Please ensure your **Hugging Face account email is an institutional email** before submitting your request.'  
  
extra_gated_fields:
  I confirm that I am affiliated with a non-commercial research institution: checkbox
  I confirm that I am using my institutional email address for this request: checkbox
  I agree that I will not use this dataset for any commercial purposes: checkbox
  I agree that I will not redistribute or share this dataset: checkbox
  I agree that I will not modify or create derivative datasets for redistribution: checkbox
  I acknowledge that violating these terms may result in access revocation or legal action: checkbox
license: cc-by-nc-nd-4.0
tags:
- music
size_categories:
- 1M<n<10M
---

# 🎵 M4-RAG: Million-scale Multilingual Music Metadata  

M4-RAG is a **large-scale music-text dataset** with **2.31 million music-text pairs**, including **1.56 million audio-text pairs**. It supports **multimodal and multilingual music research**, enabling tasks like **text-to-music generation, music captioning, music information retrieval, and music classification**. 🚀  

## 🏆 Overview  

M4-RAG aggregates **music metadata** from diverse online sources and enhances it using **retrieval-augmented generation (RAG)**. It includes:  

✔ **Short-text metadata**, including **region, genres, and various tags** (e.g., **moods, keywords, playlists**) for structured classification and retrieval  
✔ **Detailed descriptions**, background information, musical analysis, and scene depictions  
✔ **Translations in 27 languages**, making it accessible for multilingual research  
✔ **Covering 194 countries**, enabling regional music studies  

- **Total size**: 2.31 million music-text pairs  
  - **1.56 million audio-text pairs** (available for research use only)  
  - **0.75 million symbolic-text pairs** (internal data, not publicly available)  
- **Languages**: 27  
- **Regions**: 194 countries  

Each metadata entry includes both **short-form annotations** (e.g., genre, region, language) and **long-form descriptions** (providing rich contextual and musical details).  

> **Note:** The **0.75 million symbolic-text pairs** are **internal data and not publicly available**. The **1.56 million audio-text pairs are available for research purposes only and not for commercial use**.  

---

## 🌍 Supported Languages  

M4-RAG provides metadata and translations in **27 languages**, covering:  

### **Western Europe**  
🇬🇧 **English**, 🇩🇪 **German**, 🇫🇷 **French**, 🇪🇸 **Spanish**, 🇵🇹 **Portuguese**, 🇮🇹 **Italian**, 🇳🇱 **Dutch**  

### **Eastern & Central Europe**  
🇷🇺 **Russian**, 🇨🇿 **Czech**, 🇵🇱 **Polish**  

### **Middle East**  
🇸🇦 **Arabic**, 🇮🇷 **Persian**, 🇮🇱 **Hebrew**, 🇹🇷 **Turkish**  

### **East Asia**  
🇨🇳 **Chinese**, 🇯🇵 **Japanese**, 🇰🇷 **Korean**  

### **Southeast Asia**  
🇻🇳 **Vietnamese**, 🇹🇭 **Thai**, 🇮🇩 **Indonesian**, 🇲🇾 **Malay**, 🇱🇦 **Lao**, 🇲🇲 **Burmese**, 🇰🇭 **Khmer**  

### **South Asia**  
🇮🇳 **Hindi**, 🇧🇩 **Bengali**, 🇵🇰 **Urdu**  

This multilingual support enhances **cross-lingual retrieval, music description generation, and classification across diverse languages**.  

---

## 📝 Metadata Structure  

M4-RAG metadata consists of **structured annotations** divided into three categories:  

| **Category**       | **Field**       | **Description**            | **Avg. Bytes**  |  
|--------------------|----------------|----------------------------|--------------|  
|   **Basic**       | Title           | Music title                | 20.04        |  
|                   | Artists         | Artist names               | 21.97        |  
|   **Annotations** | Region          | Country of origin          | 20.69        |  
|                   | Language        | Document language          | 7.02         |  
|                   | Genres          | Genre list                 | 21.83        |  
|                   | Tags            | Keywords/playlists         | 51.91        |  
|                   | Background      | Context about the song     | 531.79       |  
|                   | Analysis        | Musical structure & details | 770.29       |  
|                   | Description     | Generalized overview (without song titles, artist names, or lyrics) | 591.86       |  
|                   | Scene           | Scene or mood depiction    | 750.92       |  
|   **Translations**| Language        | Translation language       | 6.38         |  
|                   | Background      | Translated background      | 819.76       |  
|                   | Analysis        | Translated analysis        | 1130.47      |  
|                   | Description     | Translated description     | 888.86       |  
|                   | Scene           | Translated scene           | 1077.07      |  

---

## 🏗️ Curation Process  

M4-RAG metadata was carefully curated through the following steps:  

### **1️⃣ Title Filtering**  
🔹 Entries **without titles** were removed to ensure meaningful metadata retrieval.  

### **2️⃣ Web Search & Data Retrieval**  
🔍 **Google searches** were conducted using **music titles and artist names**, retrieving the **top 10 search results** to ensure **high-quality and diverse sources**.  

### **3️⃣ Retrieval-Augmented Generation (RAG)**  
🤖 [Qwen2.5-72B](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) was used to **generate rich annotations** from retrieved documents and refine existing metadata.  

### **4️⃣ Quality Filtering**  
✅ Entries were **removed** if they lacked sufficient content or did not meet formatting standards.  
🌍 **Region fields** were normalized to **standard country names**.  
📝 **Descriptions** were refined to eliminate **identifiable details such as titles**.  

### **5️⃣ Language Verification & Postprocessing**  
🗣️ [FastText](https://github.com/facebookresearch/fastText) was used to **validate language consistency** in long-form fields.  
🚫 Entries with **unsupported languages** or **detected inconsistencies** were removed.  

### **6️⃣ Multilingual Translations**  
🌎 **Qwen** was used to translate long-form fields of each entry in a random language, **enhancing cross-lingual diversity**.  

---

## 🔥 Usage  

M4-RAG is designed for a variety of **music-text multimodal tasks**, leveraging **diverse textual semantics** (short-form and long-form metadata) and **multilingual support**.  

### 🎶 **1. Text-to-Music Generation**  
- Train models to generate **music from text descriptions**, using **scene, background, and analysis** fields as conditioning inputs.  
- Supports **multilingual prompts** for text-to-music generation in different languages.  
- Allows **region-based filtering** for **culturally grounded** music generation.  

### 📝 **2. Music Captioning**  
- Train models to generate **rich textual descriptions** from **audio** using:  
  - **Background**: Historical and cultural context.  
  - **Analysis**: Structural and musical elements.  
  - **Description**: A **generalized overview**, **excluding identifiable details** (e.g., title, artist, lyrics).  
  - **Scene**: Imagery and mood depiction.  
- Supports **cross-lingual captioning** across 27 languages.  

### 🔍 **3. Music Information Retrieval**  
- **Text-to-music retrieval**: Retrieve relevant music based on **textual descriptions**.  
- **Music-to-text retrieval**: Extract **contextual metadata** given an audio query.  

### 🎼 **4. Music Classification**  
- Use **short-form metadata** (e.g., **genre, tags, language, region**) for tasks like:  
  - **Genre classification**  
  - **Region prediction**  

## 📜 Citation  
If you find M4-RAG useful in your work, please consider citing our paper:

```bibtex
@misc{wu2025clamp3universalmusic,
  title={CLaMP 3: Universal Music Information Retrieval Across Unaligned Modalities and Unseen Languages}, 
  author={Shangda Wu and Zhancheng Guo and Ruibin Yuan and Junyan Jiang and Seungheon Doh and Gus Xia and Juhan Nam and Xiaobing Li and Feng Yu and Maosong Sun},
  year={2025},
  eprint={2502.10362},
  archivePrefix={arXiv},
  primaryClass={cs.SD},
  url={https://arxiv.org/abs/2502.10362}
}
```