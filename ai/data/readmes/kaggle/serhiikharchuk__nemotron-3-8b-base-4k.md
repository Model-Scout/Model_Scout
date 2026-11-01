# nemotron-3-8b-base-4k

Nemotron 3 8B Base 4k

Nemotron-3-8B-Base-4k
Model Overview
License

The use of this model is governed by the NVIDIA AI Foundation Models Community License Agreement.
Description

Nemotron-3-8B-Base-4k is a large language foundation model for enterprises to build custom LLMs. This foundation model has 8 billion parameters, and supports a context length of 4,096 tokens. Nemotron-3-8B-Base-4k is part of Nemotron-3, which is a family of enterprise ready generative text models compatible with NVIDIA NeMo Framework. For other models in this collection, see the collections page.

NVIDIA NeMo is an end-to-end, cloud-native platform to build, customize, and deploy generative AI models anywhere. It includes training and inferencing frameworks, guardrailing toolkits, data curation tools, and pretrained models, offering enterprises an easy, cost-effective, and fast way to adopt generative AI. To get access to NeMo Framework, please sign up at this link.
References

Announcement Blog
Model Architecture

Architecture Type: Transformer

Network Architecture: Generative Pre-Trained Transformer (GPT-3)
Software Integration

Runtime Engine(s): NVIDIA AI Enterprise

Toolkit: NeMo Framework

To get access to NeMo Framework, please sign up at this link. See NeMo inference container documentation for details on how to setup and deploy an inference server with NeMo.

Sample Inference Code:

from nemo.deploy import NemoQuery

# In this case, we run inference on the same machine
nq = NemoQuery(url="localhost:8000", model_name="Nemotron-3-8B-4K")

output = nq.query_llm(prompts=["The meaning of life is"], max_output_token=200, top_k=1, top_p=0.0, temperature=0.1)
print(output)

Supported Hardware:

    H100
    A100 80GB, A100 40GB

Model Version(s)

Nemotron-3-8B-base-4k-BF16-1
Dataset & Training

The model uses a learning rate of 3e-4 with a warm-up period of 500M tokens and a cosine learning rate annealing schedule for 95% of the total training tokens. The decay stops at a minimum learning rate of 3e-5. The model is trained with a sequence length of 4096 and uses FlashAttention’s Multi-Head Attention implementation. 1,024 A100s were used for 19 days to train the model.

NVIDIA models are trained on a diverse set of public and proprietary datasets. This model was trained on a dataset containing 3.8 Trillion tokens of text. The dataset contains 53 different human languages (including English, German, Russian, Spanish, French, Japanese, Chinese, Italian, and Dutch) and 37 programming languages. The model also uses the training subsets of downstream academic benchmarks from sources like FLANv2, P3, and NaturalInstructions v2. NVIDIA is committed to the responsible development of large language models and conducts reviews of all datasets included in training.
Evaluation
Task 	Num-shot 	Score
MMLU* 	5 	54.4
WinoGrande 	0 	70.9
Hellaswag 	0 	76.4
ARC Easy 	0 	72.9
TyDiQA-GoldP** 	1 	49.2
Lambada 	0 	70.6
WebQS 	0 	22.9
PiQA 	0 	80.4
GSM8K 	8-shot w/ maj@8 	39.4

* The calculation of MMLU follows the original implementation. See Hugging Face’s explanation of different implementations of MMLU.

** The languages used are Arabic, Bangla, Finnish, Indonesian, Korean, Russian and Swahili.
Intended use

This is a completion model. For best performance, users are encouraged to customize the completion model using NeMo Framework suite of customization tools including Parameter-Efficient Fine-Tuning (P-tuning, Adapters, LoRA), and SFT/RLHF. For chat use cases, please consider using Nemotron-3-8B chat variants.
Ethical use

Technology can have a profound impact on people and the world, and NVIDIA is committed to enabling trust and transparency in AI development. NVIDIA encourages users to adopt principles of AI ethics and trustworthiness to guide your business decisions by following the guidelines in the NVIDIA AI Foundation Models Community License Agreement.
Limitations

    The model was trained on data that contains toxic language and societal biases originally crawled from the internet. Therefore, the model may amplify those biases and return toxic responses especially when prompted with toxic prompts.
    The model may generate answers that may be inaccurate, omit key information, or include irrelevant or redundant text producing socially unacceptable or undesirable text, even if the prompt itself does not include anything explicitly offensive.

출처: Kaggle (serhiikharchuk/nemotron-3-8b-base-4k)
태그: earth and nature
라이선스: Other (specified in description)
수정일: 2024-08-31T16:49:22.660Z
