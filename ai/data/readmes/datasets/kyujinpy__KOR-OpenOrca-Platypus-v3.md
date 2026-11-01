---
language:
- ko
license: cc-by-nc-4.0
size_categories:
- 10K<n<50K
task_categories:
- conversational
- text-classification
- token-classification
- table-question-answering
- question-answering
- zero-shot-classification
- summarization
- feature-extraction
- text-generation
- text2text-generation
pretty_name: OpenOrca
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: id
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  - name: instruction
    dtype: string
  splits:
    - name: train
      num_examples: 34214
---

# KOR-OpenOrca-Platypus-v3
- KOR-OpenOrca-Platypus 데이터셋에서 수작업으로 번역 오류 200건 이상을 고친 데이터셋.  
- 데이터셋 이용하셔서 모델이나 데이터셋을 만드실 때, 간단한 출처 표기를 해주신다면 연구에 큰 도움이 됩니다😭😭

## KOpen-platpyus
Repo: [KOpen-platypus](https://huggingface.co/datasets/kyujinpy/KOpen-platypus)

- 고품질 한국어 데이터셋  
1. 코드와 주석은 그대로 유지하고, 설명 부분만 한국어로 수정
2. 1번과 더불어서, Python, Java, Cpp, xml 등등 결과들은 전부 기존의 데이터 형태로 최대한 보존
3. 단일 숫자와 영어는 본래의 결과 그대로 가져옴
4. DeepL Pro 번역 결과 중 미완성 변역 결과 직접 수정(예를 들면, '[...]'가 포함되어 있음)
5. DeepL Pro 번역 결과가 본래의 데이터에 비해 글자수가 50% 이하로 낮으면, 번역 결과 수정
6. 번역하고자 하는 글자수가 1500자 이상일 경우, API로 변경해서 번역
7. 고유명사는 최대한 유지함
> Post-processing 작업 내용 

- Add post-processing (v2)  
+) 단답형 Task 삭제.  

## OpenOrca-Ko-v2  
1. NIV // 약 1500개
2. FLAN // 약 9000개
3. T0 // 약 6000개
4. CoT // 약 2000개
> Dataset 구성  
  
- 수작업으로 고친 내용(v2)  
1. 영어로 된 답변 수정. (Ex. Nick -> 닉, Lucky -> 운이 좋음, ...)  
2. KoCoT 데이터셋 제거.  
3. Yes, True, False 등등 일부 답변 수정  
> Post-processing 작업 내용 


## Translation
Using DeepL Pro API. Thanks.

---
>Below is original dataset card

## Table of Contents
- [Dataset Summary](#dataset-summary)
- [Dataset Attribution](#dataset-attribution)
- [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
- [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
- [Dataset Use](#dataset-use)
  - [Use Cases](#use-cases)
  - [Usage Caveats](#usage-caveats)
  - [Getting Started](#getting-started)


<p><h1>🐋 The OpenOrca Dataset! 🐋</h1></p>

![OpenOrca Logo](https://huggingface.co/datasets/Open-Orca/OpenOrca/resolve/main/OpenOrcaLogo.png "OpenOrca Logo")

<a name="dataset-announcement"></a>

We are thrilled to announce the release of the OpenOrca dataset!
This rich collection of augmented FLAN data aligns, as best as possible, with the distributions outlined in the [Orca paper](https://arxiv.org/abs/2306.02707).
It has been instrumental in generating high-performing model checkpoints and serves as a valuable resource for all NLP researchers and developers!

# Official Models

## OpenOrca-Platypus2-13B

Our [latest release](https://huggingface.co/Open-Orca/OpenOrca-Platypus2-13B), the first 13B model to score higher than LLaMA1-65B on the HuggingFace Leaderboard!
Released in partnership with Platypus.

## LlongOrca 7B & 13B

* Our [first 7B release](https://huggingface.co/Open-Orca/LlongOrca-7B-16k), trained on top of LLongMA2 to achieve 16,000 tokens context. #1 long context 7B model at release time, with >99% of the overall #1 model's performance.
* [LlongOrca-13B-16k](https://huggingface.co/Open-Orca/LlongOrca-13B-16k), trained on top of LLongMA2. #1 long context 13B model at release time, with >97% of the overall #1 model's performance.

## OpenOrcaxOpenChat-Preview2-13B

Our [second model](https://huggingface.co/Open-Orca/OpenOrcaxOpenChat-Preview2-13B), highlighting that we've surpassed the performance reported in the Orca paper.
Was #1 at release time, now surpassed by our own OpenOrca-Platypus2-13B.
Released in partnership with OpenChat.

## OpenOrca-Preview1-13B

[OpenOrca-Preview1-13B](https://huggingface.co/Open-Orca/OpenOrca-Preview1-13B)
This model was trained in less than a day, for <$200, with <10% of our data.
At release, it beat the current state of the art models on BigBench-Hard and AGIEval. Achieves ~60% of the improvements reported in the Orca paper.

<a name="dataset-summary"></a>

# Dataset Summary

The OpenOrca dataset is a collection of augmented [FLAN Collection data](https://arxiv.org/abs/2301.13688).
Currently ~1M GPT-4 completions, and ~3.2M GPT-3.5 completions.
It is tabularized in alignment with the distributions presented in the ORCA paper and currently represents a partial completion of the full intended dataset, with ongoing generation to expand its scope.
The data is primarily used for training and evaluation in the field of natural language processing.

<a name="dataset-attribution"></a>

# Dataset Attribution

We would like to give special recognition to the following contributors for their significant efforts and dedication:
        

    Teknium                     
    WingLian/Caseus
    Eric Hartford
    NanoBit
    Pankaj
    Winddude
    Rohan

    http://AlignmentLab.ai:
    Autometa
    Entropi
    AtlasUnified
    NeverendingToast
    NanoBit
    WingLian/Caseus

Also of course, as always, TheBloke, for being the backbone of the whole community.

Many thanks to NanoBit and Caseus, makers of [Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl), for lending us their expertise on the platform that developed and trained manticore, minotaur, and many others! 

We are welcoming sponsors or collaborators to help us build these models to the scale they deserve. Please reach out via our socials:
http://Alignmentlab.ai https://discord.gg/n9hXaBPWxx

Want to visualize our full dataset? Check out our [Nomic Atlas Map](https://atlas.nomic.ai/map/c1b88b47-2d9b-47e0-9002-b80766792582/2560fd25-52fe-42f1-a58f-ff5eccc890d2).
  [<img src="https://huggingface.co/Open-Orca/OpenOrca-Preview1-13B/resolve/main/OpenOrca%20Nomic%20Atlas.png" alt="Atlas Nomic Dataset Map" width="400" height="400" />](https://atlas.nomic.ai/map/c1b88b47-2d9b-47e0-9002-b80766792582/2560fd25-52fe-42f1-a58f-ff5eccc890d2)


<a name="supported-tasks-and-leaderboards"></a>

# Supported Tasks and Leaderboards

This dataset supports a range of tasks including language modeling, text generation, and text augmentation.
It has been instrumental in the generation of multiple high-performing model checkpoints which have exhibited exceptional performance in our unit testing.
Further information on leaderboards will be updated as they become available.

<a name="languages"></a>

# Languages

The language of the data is primarily English.

<a name="dataset-structure"></a>

# Dataset Structure

<a name="data-instances"></a>

## Data Instances

A data instance in this dataset represents entries from the FLAN collection which have been augmented by submitting the listed question to either GPT-4 or GPT-3.5.
The response is then entered into the response field.

<a name="data-fields"></a>

## Data Fields

The fields are:
1) 'id', a unique numbered identifier which includes one of 'niv', 't0', 'cot', or 'flan' to represent which source FLAN Collection submix the 'question' is sourced from.
2) 'system_prompt', representing the System Prompt presented to the GPT-3.5 or GPT-4 API for the datapoint
3) 'question', representing a question entry as provided by the FLAN Collection
4) 'response', a response to that question received from a query to either GPT-3.5 or GPT-4.

<a name="data-splits"></a>

## Data Splits

The data is unsplit.

<a name="dataset-creation"></a>

# Dataset Creation

<a name="curation-rationale"></a>

## Curation Rationale

The dataset was created to provide a source of augmented text data for researchers and developers.
The datapoints are intended primarily to provide an enhancement of the core FLAN Collection data which relies upon the detailed step by step reasoning capabilities of GPT-3.5 and GPT-4.
This "reasoning trace" augmentation has demonstrated exceptional results, allowing a LLaMA-13B model trained with this data to rival or beat GPT-3.5 on broad sets of hard reasoning tasks which all models below 100B parameters had previously performed dramatically worse on.

<a name="source-data"></a>

## Source Data

The data is generated using techniques in alignment with the distributions outlined in the Orca paper, except as noted below:

1) There is not enough CoT data in the FLAN Collection to generate 150K zero-shot entries, as the paper purports to use.
 We suspect this portion was either undocumented or misrepresented. We have used the ~75K points available.
2) We used the pre-generated FLAN Collection datasets hosted on HuggingFace under conceptofmind, e.g. [conceptofmind/flan2021](https://huggingface.co/datasets/conceptofmind/flan2021_submix_original).
 These are referenced by the [official FLAN Collection repo](https://github.com/google-research/FLAN/tree/main/flan/v2) as the preferred data source.
 However, these are a subset of the full FLAN Collection data, and have less than the required entries for the flan2021 and t0 submixes, by ~1.25M and 200k respectively.

Combined, this gave us ~1.5M fewer datapoints than in the original Orca paper. Completing the set is an ongoing work.

<a name="dataset-use"></a>

# Dataset Use

<a name="use-cases"></a>

## Use Cases

The dataset can be used for tasks related to language understanding, natural language processing, machine learning model training, and model performance evaluation.

<a name="usage-caveats"></a>

## Usage Caveats

Given that this is a work-in-progress dataset, it is recommended to regularly check for updates and improvements.
Further, the data should be used in accordance with the guidelines and recommendations outlined in the Orca paper.

<a name="getting-started"></a>

## Getting Started

This dataset is organized such that it can be naively loaded via Hugging Face datasets library.
We recommend using streaming due to the large size of the files.
Regular updates and data generation progress can be monitored through the OpenOrca repository on Hugging Face.


# Citation

```bibtex
@misc{OpenOrca,
  title = {OpenOrca: An Open Dataset of GPT Augmented FLAN Reasoning Traces},
  author = {Wing Lian and Bleys Goodson and Eugene Pentland and Austin Cook and Chanvichet Vong and "Teknium"},
  year = {2023},
  publisher = {HuggingFace},
  journal = {HuggingFace repository},
  howpublished = {\url{https://https://huggingface.co/Open-Orca/OpenOrca},
}
```
```bibtex
@misc{mukherjee2023orca,
      title={Orca: Progressive Learning from Complex Explanation Traces of GPT-4}, 
      author={Subhabrata Mukherjee and Arindam Mitra and Ganesh Jawahar and Sahaj Agarwal and Hamid Palangi and Ahmed Awadallah},
      year={2023},
      eprint={2306.02707},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
```bibtex
@misc{longpre2023flan,
      title={The Flan Collection: Designing Data and Methods for Effective Instruction Tuning}, 
      author={Shayne Longpre and Le Hou and Tu Vu and Albert Webson and Hyung Won Chung and Yi Tay and Denny Zhou and Quoc V. Le and Barret Zoph and Jason Wei and Adam Roberts},
      year={2023},
      eprint={2301.13688},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}
```
```bibtex
@misc{touvron2023llama,
    title={Llama 2: Open Foundation and Fine-Tuned Chat Models}, 
    author={Hugo Touvron and Louis Martin and Kevin Stone and Peter Albert and Amjad Almahairi and Yasmine Babaei and Nikolay Bashlykov and Soumya Batra and Prajjwal Bhargava and Shruti Bhosale and Dan Bikel and Lukas Blecher and Cristian Canton Ferrer and Moya Chen and Guillem Cucurull and David Esiobu and Jude Fernandes and Jeremy Fu and Wenyin Fu and Brian Fuller and Cynthia Gao and Vedanuj Goswami and Naman Goyal and Anthony Hartshorn and Saghar Hosseini and Rui Hou and Hakan Inan and Marcin Kardas and Viktor Kerkez and Madian Khabsa and Isabel Kloumann and Artem Korenev and Punit Singh Koura and Marie-Anne Lachaux and Thibaut Lavril and Jenya Lee and Diana Liskovich and Yinghai Lu and Yuning Mao and Xavier Martinet and Todor Mihaylov and Pushkar Mishra and Igor Molybog and Yixin Nie and Andrew Poulton and Jeremy Reizenstein and Rashi Rungta and Kalyan Saladi and Alan Schelten and Ruan Silva and Eric Michael Smith and Ranjan Subramanian and Xiaoqing Ellen Tan and Binh Tang and Ross Taylor and Adina Williams and Jian Xiang Kuan and Puxin Xu and Zheng Yan and Iliyan Zarov and Yuchen Zhang and Angela Fan and Melanie Kambadur and Sharan Narang and Aurelien Rodriguez and Robert Stojnic and Sergey Edunov and Thomas Scialom},
    year={2023},
    eprint= arXiv 2307.09288
}
@software{touvron2023llama,
  title={LLaMA: Open and Efficient Foundation Language Models},
  author={Touvron, Hugo and Lavril, Thibaut and Izacard, Gautier and Martinet, Xavier and Lachaux, Marie-Anne and Lacroix, Timoth{\'e}e and Rozi{\`e}re, Baptiste and Goyal, Naman and Hambro, Eric and Azhar, Faisal and Rodriguez, Aurelien and Joulin, Armand and Grave, Edouard and Lample, Guillaume},
  journal={arXiv preprint arXiv:2302.13971},
  year={2023}
}
```