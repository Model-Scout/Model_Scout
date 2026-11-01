---
license: cc-by-4.0
language:
- en
pretty_name: Nemotron Content Safety Dataset V1
task_categories:
- text-classification
tags:
- safety
- content moderation
- LLM safety
- toxicity detection
- aegis
- nemoguard
- nemotron
size_categories:
- 10K<n<100K
---

# 🛡️ Nemotron Content Safety Dataset V1

_Nemotron Content Safety Dataset V1_, formerly known as _Aegis AI Content Safety Dataset_, is an open-source content safety dataset (CC-BY-4.0), which adheres to Nvidia's content safety taxonomy, covering 13 critical risk categories (see [Dataset Description](#dataset-description)).

## Dataset Details

### Dataset Description

_Nemotron Content Safety Dataset V1_ is comprised of approximately `11,000` manually annotated interactions between humans and LLMs, split into `10,798` training samples and `1,199` test samples.

To curate the dataset, we use the Hugging Face version of human preference data about harmlessness from [Anthropic HH-RLHF](https://huggingface.co/datasets/Anthropic/hh-rlhf). We extract only the prompts, and elicit responses from [Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1). Mistral excels at instruction following and generates high quality responses for the content moderation categories. We use examples in the system prompt to ensure diversity by instructing Mistral to not generate similar responses. Our data comprises four different formats: user prompt only, system prompt with user prompt, single turn user prompt with Mistral response, and multi-turn user prompt with Mistral responses.

The samples are annotated with respect to the following taxonomy.

PLEASE NOTE: The samples are only annotated at the dialog level. If the dialog consists of a single prompt only, then the annotations are valid for that prompt. Otherwise, the annotations are only applicable for prompt(s) + response(s), at a partial or whole dialog level. 

### Nvidia's Content Safety Taxonomy
| Harm Category |
| --- |
| Hate /Identity Hate |
| Sexual |
| Violence |
| Suicide and Self Harm |
| Threat |
| Sexual Minor |
| Guns /Illegal Weapons |
| Controlled /Regulated substances |
| Criminal Planning /Confessions |
| PII |
| Harassment |
| Profanity |
| Other |
| Needs Caution |

- **Curated by:** Shaona Ghosh, Nvidia.
- **Paper:** [AEGIS: Online Adaptive AI Content Safety Moderation with Ensemble of LLM Experts](https://arxiv.org/abs/2404.05993)
- **Language(s) (NLP):** English (may contain small samples in other languages).
- **License:** CC-BY-4.0

### Dataset Sources

1. We use the Hugging Face version of human preference data about harmlessness from [Anthropic HH-RLHF](https://huggingface.co/datasets/Anthropic/hh-rlhf). 
2. We extract only the prompts, and elicit responses from [Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1).
3. Annotation was performed by a team of `twelve` annotators along with `two` data quality assurance persons, using data teams at Nvidia.

## Uses

### Direct Use

1. To build content moderation guardrails around LLMs.
2. Aligning LLMs to generate safe reponses using SFT or DPO methods.

### Out-of-Scope Use

The data contain content that may be offensive or upsetting. Topics include, but are not limited to, discriminatory language and discussions of abuse, violence, self-harm, exploitation, and other potentially upsetting subject matter. Please only engage with the data in accordance with your own personal risk tolerance. The data are intended for research purposes, especially research that can make models less harmful. The views expressed in the data do not reflect the views of Nvidia or any of its employees. These data are not intended for training dialogue agents as this will likely lead to harmful model behavior.

## Dataset Creation

### Annotation process

Quality Assurance (QA) is maintained by the leads of this project. Two to three times
per week, leads choose fifteen questions at random of every one hundred completed by
three annotators to reevaluate. This accounts for fifteen percent of the data analyzed
for three-way agreement at a minimum, often having at least twenty to thirty percent
analyzed to further ensure quality. These corrections are sent to each individual annotator
as audits, with brief explanations of why certain corrections were made with reference to
the project guidelines. Data sets are commonly broken into 2,000-4,000 text-based prompts
and delivered to annotators in batches of three to five. In the transitions between each
batch, Person In Charge (PIC) or the lead designate at least one full eight hour work day
for annotators to self-correct their categorization work. Many training sessions have been
held throughout the duration of this project for tips on best practices when self-correcting,
including filtering through key words in the data, referencing the regularly updated FAQ
sheet with example questions, and choosing completed prompts at random to reevaluate.
Annotators are instructed to only self-correct their own work and avoid looking at any
other annotations besides their own. Both Leads are also available at all times for further
questions or meetings to ensure consistent understanding of the material. Mandatory virtual
group training are held every two weeks or as needed depending on the circumstances of
the project. These meetings are led by leads and often utilize examples of commonly seen
discrepancies to present as learning opportunities.

#### Who are the annotators?

Throughout the three month time span of the Content Moderation Guardrails project, we
have averaged twelve annotators at any given time. Of these twelve, four annotators come
from Engineering backgrounds specializing in data analysis and collection, gaming, and
robotics. Eight annotators have a background in Creative Writing, with specialization in
linguistics, research and development, and other creative arts such as photography and
film. All annotators have been extensively trained in working with Large Language Models
(LLM), as well as other variations of Generative AI such as image retrieval or evaluations
of multi-turn conversations. All are capable of generating creative text-based output and
categorization work. Each of these twelve annotators resides in the United States, all from
various ethnic and religious backgrounds that allow for representation across race, age, and
social status.

### Personal and Sensitive Information

This dataset comprises LLM responses generated from  [Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1) . We have carefully gone through the data and taken out anything that could have personal information in it. However, there is still a chance that some personal information might be left in the data. If you come across anything in the data that you think should not be made public, please let us know right away.

## Bias, Risks, and Limitations

- Safety and Moderation: This dataset is intended to be used for building content moderations systems, or aligning LLMs to generate safe responses. By the nature of the work, the dataset contains critically unsafe content and annotations for that content. Extreme care and caution should be exercised in referring and using this dataset.
- Legal Compliance: Users of this data are responsible for ensuring its appropriate use. The dataset should not be utilized in manners that conflict with legal and ethical standards.
- Non-Identification: Users of this data agree to not attempt to determine the identity of individuals in this dataset.

## Ethical Statement

The process in which the _Nemotron Content Safety Dataset V1_ creation abides by ethical data categorization work is based within the tooling of [Label Studio](http://label-studio.nvidia.com/user/login/), an open source data labeling tool often used for Nvidia's internal projects. This tooling technology allows for large sets of data to be analyzed by individual annotators without seeing the work of their peers. This is essential in preventing bias between annotators, as well as delivering prompts to each individual with variability so that no one annotator is completing similar tasks based
on how the data was initially arranged.

Due to the serious nature of this project, annotators were asked to join on a volunteer basis
based on their skill level, availability, and willingness to expose themselves to potentially
toxic content. Before work on this project began, all participants were asked to sign an
“_Adult Content Acknowledgement_” that coincides with the organization’s existing _AntiHarassment Policy_ and _Code of Conduct_. This was to ensure that all annotators be made  aware of the nature of this work, as well as the resources available to them should it affect their mental well-being. Regular 1:1 meetings were held between the leads assigned to this project and each annotator to make sure they are still comfortable with the material and are capable of continuing on with this type of work.

## Citation

**BibTeX:**
```
@article{ghosh2024aegis,
    title={AEGIS: Online Adaptive AI Content Safety Moderation with Ensemble of LLM Experts},
    author={Ghosh, Shaona and Varshney, Prasoon and Galinkin, Erick and Parisien, Christopher},
    journal={arXiv preprint arXiv:2404.05993},
    year={2024}
}
```

## Dataset Card Authors 

Shaona Ghosh, shaonag@nvidia.com

## Dataset Card Contact

shaonag@nvidia.com