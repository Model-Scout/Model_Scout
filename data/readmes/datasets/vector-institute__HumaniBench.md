---
license: cc-by-nc-sa-4.0
task_categories:
- visual-question-answering
- object-detection
- question-answering
language:
- en
- ta
- ur
- es
- fa
- pt
- ko
- fr
pretty_name: HumaniBench
size_categories:
- 10K<n<100K
configs:
- config_name: task1_Scene_Understanding
  data_files:
  - split: test
    path: task1_Scene_Understanding/data.parquet
  features:
  - name: ID
    dtype: string
  - name: image
    dtype: image
  - name: Attribute
    dtype: string
  - name: version_type
    dtype: string
  - name: Question
    dtype: string
  - name: Answer
    dtype: string
- config_name: task2_Instance_Identity
  data_files:
  - split: test
    path: task2_Instance_Identity/data.parquet
  features:
  - name: ID
    dtype: string
  - name: image
    dtype: image
  - name: Attribute
    dtype: string
  - name: Question
    dtype: string
  - name: Answer
    dtype: string
- config_name: task3_Multiple_Choice_VQA
  data_files:
  - split: test
    path: task3_Multiple_Choice_VQA/data.parquet
  features:
  - name: ID
    dtype: string
  - name: image
    dtype: image
  - name: Attribute
    dtype: string
  - name: Question
    dtype: string
  - name: Options
    dtype: string
  - name: Answer
    dtype: string
  - name: Reasoning
    dtype: string
- config_name: task4_Multilingual_OpenEnded
  data_files:
  - split: test
    path: task4_Multilingual_OpenEnded/data.parquet
  features:
  - name: ID
    dtype: string
  - name: image
    dtype: image
  - name: Attribute
    dtype: string
  - name: Question(English)
    dtype: string
  - name: Answer(English)
    dtype: string
  - name: Language
    dtype: string
  - name: Question
    dtype: string
  - name: Answer
    dtype: string
- config_name: task4_Multilingual_CloseEnded
  data_files:
  - split: test
    path: task4_Multilingual_CloseEnded/data.parquet
  features:
  - name: ID
    dtype: string
  - name: image
    dtype: image
  - name: Attribute
    dtype: string
  - name: Question(English)
    dtype: string
  - name: Options(English)
    dtype: string
  - name: Answer(English)
    dtype: string
  - name: Reasoning(English)
    dtype: string
  - name: Language
    dtype: string
  - name: Question
    dtype: string
  - name: Answer
    dtype: string
  - name: Options
    dtype: string
  - name: Reasoning
    dtype: string
- config_name: task5_Visual_Grounding
  data_files:
  - split: test
    path: task5_Visual_Grounding/data.parquet
  features:
  - name: ID
    dtype: string
  - name: image
    dtype: image
  - name: question
    dtype: string
  - name: bbox
    dtype:
      sequence: float32
- config_name: task6_Empathetic_Captioning
  data_files:
  - split: test
    path: task6_Empathetic_Captioning/data.parquet
  features:
  - name: ID
    dtype: string
  - name: image
    dtype: image
  - name: social_attribute
    dtype: string
  - name: simple_prompt
    dtype: string
  - name: empathic_prompt
    dtype: string
- config_name: task7_Image_Resilience
  data_files:
  - split: test
    path: task7_Image_Resilience/data.parquet
  features:
  - name: ID
    dtype: string
  - name: attack_type
    dtype: string
  - name: image
    dtype: image
  - name: Attribute
    dtype: string
  - name: Question
    dtype: string
  - name: Answer
    dtype: string
---
# HumaniBench: A Human-Centric Benchmark for Large Multimodal Models Evaluation
<p align="center">
  <img src="https://github.com/user-attachments/assets/ebed8e26-5bdf-48c1-ae41-0775b8c33c0a" alt="HumaniBench Logo" height="120"/>
</p>
**HumaniBench** is a benchmark for evaluating large multimodal models (LMMs) using real-world, human-centric criteria. It consists of 32,000+ image–question pairs across 7 tasks:

- ✅ Open/closed VQA
- 🌍 Multilingual QA
- 📌 Visual grounding
- 💬 Empathetic captioning
- 🧠 Robustness, reasoning, and ethics

Each example is annotated with GPT-4o drafts, then verified by experts to ensure quality and alignment.


<p align="center">
  <a href="https://vectorinstitute.github.io/HumaniBench/"><img src="https://img.shields.io/badge/🌐-Website-4285F4" alt="Website"></a>
  <a href="https://arxiv.org/abs/2505.11454"><img src="https://img.shields.io/badge/arXiv-Paper-b31b1b?logo=arxiv&logoColor=white" alt="Paper"></a>
  <a href="https://github.com/VectorInstitute/HumaniBench"><img src="https://img.shields.io/badge/GitHub-Code-181717?logo=github" alt="Code"></a>
  <a href="https://huggingface.co/spaces/vector-institute/HumaniBench"><img src="https://img.shields.io/badge/🤗-Spaces-FFD21F" alt="Spaces"></a>
</p>


## Available Tasks

| Task ID | Description                               | Subsets                  |
|--------|-------------------------------------------|--------------------------|
| Task 1 | Scene Understanding                        | `task1_Scene_Understanding` |
| Task 2 | Instance Identity                          | `task2_Instance_Identity` |
| Task 3 | Multiple-Choice VQA                        | `task3_Multiple_Choice_VQA` |
| Task 4a | Multilingual Open-Ended VQA               | `task4_Multilingual_OpenEnded` |
| Task 4b | Multilingual Close-Ended VQA              | `task4_Multilingual_CloseEnded` |
| Task 5 | Visual Grounding          | `task5_Visual_Grounding` |
| Task 6 | Empathy Captioning                | `task6_Empathetic_Captioning` |
| Task 7 | Robustness  | `task7_Image_Resilience` |

---


## How to Load

```python
from datasets import load_dataset

# Load each task individually
ds1 = load_dataset("vector-institute/HumaniBench", "task1_Scene_Understanding")
ds2 = load_dataset("vector-institute/HumaniBench", "task2_Instance_Identity")
ds3 = load_dataset("vector-institute/HumaniBench", "task3_Multiple_Choice_VQA")
ds4a = load_dataset("vector-institute/HumaniBench", "task4_Multilingual_OpenEnded")
ds4b = load_dataset("vector-institute/HumaniBench", "task4_Multilingual_CloseEnded")
ds5 = load_dataset("vector-institute/HumaniBench", "task5_Visual_Grounding")
ds6 = load_dataset("vector-institute/HumaniBench", "task6_Empathetic_Captioning")
ds7 = load_dataset("vector-institute/HumaniBench", "task7_Image_Resilience")
```

## Dataset Structure

Each task contains task-specific fields. Examples include:

### Task 1: Scene Understanding
- `ID`: Unique image identifier  
- `image`: Embedded image data
- `Attributes`: Target social context or category (e.g., Sport, Ethnicity)  
- `version_type`: Version of the reasoning (cot_version or plain_version)
- `Question`: Question prompting the model to describe the image
- `Answer`: Descriptive reasoning response

### Task 2: Instance Identity
- `ID`: Unique sample ID  
- `image`: Embedded image data
- `Attribute`: Target social context or category (e.g., Sport, Ethnicity)  
- `Question`: Open-ended or contextual question about the image  
- `Answer`: Grounded, descriptive reasoning response  

### Task 3: Instance Attribute
- `ID`: Unique question ID  
- `image`: Embedded image data
- `Attribute`: Target dimension (e.g., Gender, Race)  
- `Question`: Multiple-choice question  
- `Options`: List of 4 answer choices  
- `Answer`: Correct answer text  
- `Reasoning`: Optional explanation supporting the answer  

### Task 4a: Multilingual Open-Ended VQA
- `ID`: Unique sample ID  
- `image`: Embedded image data
- `Attribute`: Target concept (e.g., Gender, Age)  
- `Question(English)`: Question in English  
- `Answer(English)`: Answer in English  
- `Language`: Language of translation (e.g., Tamil, Spanish)  
- `Question`: Localized version of the question  
- `Answer`: Localized version of the answer  

### Task 54b: Multilingual Close-Ended VQA
- Same fields as 5a, plus:  
- `Options(English)`: Multiple-choice options in English  
- `Options`: Localized options  
- `Reasoning(English)`: Answer rationale in English  
- `Reasoning`: Localized rationale

### Task 5: Visual Grounding and Localization
- `id`: Image ID  
- `image`: Embedded image dat
- `bbox`: Bounding box coordinates `[x_min, y_min, x_max, y_max]`

### Task 6: Emotion and Human-Centered
- `ID`: Unique identifier for the image
- `image`: Embedded image data
- `social_attribute`: Target concept (e.g., Gender, Age)  
- `simple_prompt`: Neutral, factual description of the scene  
- `empathic_prompt`: Emotionally rewritten caption that adds human-centered context  

Images for this task are stored in: `task6_emotion_style/images/`

---

### Task 7: Robustness and Stability Evaluation
- `ID`: Unique identifier for each VQA sample  
- `Attribute`: Target concept being tested (e.g., Sport)  
- `attack_type`: Type of perturbation applied (e.g., blackout, blur)
- `image`: Embedded image data
- `Question`: VQA-style prompt relevant to the image  
- `Answer`: Grounded, descriptive response expected across clean and perturbed inputs  

---

## Intended Use

HumaniBench is intended for:

- Benchmarking MLLMs across human-centered tasks  
- Studying robustness to perturbations and fairness in vision-language models  
- Evaluating multilingual reasoning and empathy in visual captioning  
- Training or fine-tuning models with rich multimodal annotations  

---


## Related Resources

- [Project Website](https://vectorinstitute.github.io/HumaniBench/)  
- [GitHub Repository](https://github.com/VectorInstitute/HumaniBench)  
- [Paper (arXiv)](https://arxiv.org/abs/XXXX.XXXXX) *(coming soon)*  

---

## License

This dataset is licensed under the **CC BY-NC-SA 4.0 License**.

----

## 🙏 Acknowledgments

Resources used in preparing this research were provided, in part, by the Province of Ontario, the Government of Canada through CIFAR, and companies sponsoring the Vector Institute ([vectorinstitute.ai/#partners](http://www.vectorinstitute.ai/#partners)). 

This research was funded by the European Union's Horizon Europe research and innovation programme under the AIXPERT project (Grant Agreement No. 101214389), which aims to develop an agentic, multi-layered, GenAI-powered framework for creating explainable, accountable, and transparent AI systems.

---


## 📚 Citation

```bibtex
@article{raza2026humanibench,
  author = {Raza, Shaina and Narayanan, Aravind and Khazaie, Vahid Reza and Vayani, Ashmal and Radwan, Ahmed Y. and Chettiar, Mukund S. and Singh, Amandeep and Shah, Mubarak and Pandya, Deval},
  title = {HumaniBench: A Human-Centric Framework for Large Multimodal Models Evaluation},
  year = {2026},
  publisher = {Association for Computing Machinery},
  address = {New York, NY, USA},
  issn = {2157-6904},
  url = {https://doi.org/10.1145/3845999},
  doi = {10.1145/3845999},
  note = {Just Accepted},
  journal = {ACM Trans. Intell. Syst. Technol.},
  month = sep,
}
```
---



