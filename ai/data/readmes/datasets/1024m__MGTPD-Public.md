---
configs:
- config_name: Latest Version
  data_files:
  - split: Train
    path: MGTPD-Train.csv 
  - split: Dev
    path: MGTPD-Dev.csv 
  - split: Test
    path: MGTPD-Test.csv    
task_categories:
- token-classification
language:
- ar
- cs
- de
- nl
- en
- zh
- fa
- fr
- el
- he
- hi
- id
- it
- ja
- ko
- pl
- pt
- ro
- ru
- es
- tr
- uk
- vi
tags:
- linguistics
- MGT
- AI text detection
pretty_name: mMGTD
size_categories:
- 1M<n<10M
license: cc-by-nc-nd-4.0
---
# Dataset for Multilingual Machine-Generated Text Portion Detection

## Model Details

**To be made Available by Aug 1, 2025**      

### Model Description
- Developed by: 1-800-SHARED-TASKS
- Funded by: Traversaal L.A.R.G.E Research Grant (Nov 2024) , and Cohere's Research Compute Grant (July 2024)(dataset creation for cohere's LLMs) 
- Model type: Small Transformer-based for token-classification
- Languages (NLP): 23 languages (scalable to 102) 
- License: Non-commercial; all derivatives must remain non-commercial with proper attribution;

### Model Sources
- **Code Repository:** [Github Placeholder]
- **Paper:** [ACL Anthology Placeholder]
- **Inital Presentation:** [Multi-lingual Machine-Generated Text Portion(s) Detection](https://youtu.be/d5m0twUvuUE?si=iO0p8oKLAPDEUibP)

## Uses
The dataset is suitable for machine-generated text portion detection, token classification tasks, and other linguistic tasks. The methods applied here aim to improve the accuracy of detecting which portions of text are machine-generated, particularly in multilingual contexts. The dataset could be beneficial for research and development in areas like AI-generated text moderation, natural language processing, and understanding the integration of AI in content generation.

## **Training Details**

The model was trained on a dataset consisting of approximately 2.4M text samples from various LLMs. The dataset includes 10k samples per language for each LLM, with a distribution of 10% fully human-written texts, 10% entirely machine-generated texts, and 80% mixed cases.

| LLM Model | Samples |
|-----------|--------------|
| GPT-o1 | 230,000 |
| GPT-4o | 230,000 |
| Perplexity-Sonar-Large | 50,000 |
| Amazon-Nova-Pro-1.0 | 230,000 |
| Amazon-Nova-Lite-1.0 | 230,000 |
| Mistral-Large-instruct | 230,000 |
| Claude-3.5-Haiku | 230,000 |
| Claude-3.5-Sonnet | 230,000 |
| Gemini-1.5-Pro | 230,000 |
| Gemini-1.5-Flash | 230,000 |
| Command-R-Plus-104B | 100,000 |
| Aya-23-35B | 230,000 |
| **Total** | **2,450,000** |

**Parameters and architecture TBA**

## **Evaluation**
We have evaluated over our test set as well as other pre-existing benchmarks in 3 formats : word-level accuracy (char-level for JPN,ZHO) , sentence level accuracy , text wise accuracy (binary cases)

### **Results on unseen generators and domains (trained on just 10k samples of a single generator of the 2.4M)**
- M4GT-Bench (includes partial cases) - 98.38% sentence level accuracy [ unseen generators, partially seen domains ]
- ETS Essays (only binary cases) - 99.21% overall accuracy , 98.27% sentence level accuracy [ unseen generators, unseen domains, non-native human authored texts]
- RAID-Bench (binary cases with adversarial inputs) - 79.41% sentence level accuracy [ unseen generators, unseen domains , with adversarial methods (not trained on) ] 

## **Bibtex**
```
@inproceedings{kadiyala-2024-rkadiyala,
    title = "{RK}adiyala at {S}em{E}val-2024 Task 8: Black-Box Word-Level Text Boundary Detection in Partially Machine Generated Texts",
    author = "Kadiyala, Ram Mohan Rao",
    booktitle = "Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)",
    month = jun,
    year = "2024",
    address = "Mexico City, Mexico",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.semeval-1.78/",
    doi = "10.18653/v1/2024.semeval-1.78",
    pages = "511--519",
}
```
```
To Be Replaced by arxiv preprint, (april 15 2025)
@misc {ram_kadiyala_2024,
	authors       = { {Ram Mohan Rao Kadiyala, Siddartha Pullakhandam, Kanwal Mehreen, Ashay Srivastava, Subhasya TippaReddy, Arvind Reddy Bobbili, Drishti Sharma, Suraj Chandrashekhar, Modabbir Adeeb, Srinadh Vura } },
	title        = { mMGTD-Corpus (v1) },
	year         = 2024,
	url          = { https://huggingface.co/datasets/1024m/mMGTD-Corpus },
	doi          = { 10.57967/hf/3194 },
	publisher    = { Hugging Face }
}
```

## **Authors**

- Ram Kadiyala [[contact@rkadiyala.com](mailto:contact@rkadiyala.com)]
- Siddartha Pullakhandam [[pullakh2@uwm.edu](mailto:pullakh2@uwm.edu)]
- Kanwal Mehreen [[kanwal@traversaal.ai](mailto:kanwal@traversaal.ai)]
- Drishti Sharma [[drishtisharma96505@gmail.com](mailto:drishtisharma96505@gmail.com)]
- Subhasya TippaReddy [[subhasyat@usf.edu](mailto:subhasyat@usf.edu)]
- Arvind Reddy Bobbili [[abobbili@cougarnet.uh.edu](mailto:abobbili@cougarnet.uh.edu)]
- Ashay Srivastava [[ashays06@umd.edu](mailto:ashays06@umd.edu)]

**Other Contributors**
- Suraj Chandrashekhar [[stelugar@umd.edu](mailto:stelugar@umd.edu)]
- Modabbir Adeeb [[madeeb@umd.edu](mailto:madeeb@umd.edu)]
- Srinadh Vura [[320106410055@andhrauniversity.edu.in](mailto:320106410055@andhrauniversity.edu.in)]

## **Contact**

 [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:contact@rkadiyala.com)