---
language:
- en
- ko
pipeline_tag: text-generation
inference: false
tags:
- facebook
- meta
- pytorch
- llama
- llama-2
- kollama
- llama-2-ko
- llama-2-ko-chat
- legal-llama
- law-llama
- legal-gpt
- law-gpt
---

<img src=https://github.com/taemin6697/Paper_Review/assets/96530685/9f94505c-4fda-41ae-9a67-1e4c96c501cc style="max-width: 500px; width: 100%" />

Llama-2-Ko-7b-Chat은 [kfkas/Llama-2-ko-7b-Chat](https://huggingface.co/kfkas/Llama-2-ko-7b-Chat)를 토대로 만들어졌습니다. 학습 데이터는 자체 법률 질의 응답 데이터를 통해 학습하였습니다.

## Model Details

**Backbone Model** kfkas/Llama-2-ko-7b-Chat

**Model Developers** Boostcamp AI Tech Team YoonSeul

**data** leagl data

**prompts** kullm

**Input** Models input text only.

**Output** Models generate text only.

---
| Model              | 질문 : 아빠가 돌아가시고 나서 한 정승인과 상속 포기 판결문을 받았는데요. 그러고 나서 근로 건설공제회에서 전화가 왔는데요. 퇴직금 공제가 있다고 신청하여서 찾아가라고 하였더라고요. 근데 이게 상속인의 고유재산이 다 아니다 하여 법원에 재산으로 신고하여야 한다고 안 해도 된다고 합니다. 정확하게 알고 싶습니다. 상속인의 고유재산으로 법원에 재산 신고하여야 하나요? 아니면 안 해도 되나요?                                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Llama-2-ko-7b-Chat | `[안녕하세요! 상속인 고유 재산이 아니더라도 근로건설공제회로부터 퇴직금을 지급받기 위해 법원에 재산을 신고해야 할 수 있습니다. 하지만 구체적인 상황은 상속인이 속한 국가의 법률에 따라 달라질 수 있으므로, 해당 법률 전문가에게 문의하거나 확인하는 것이 좋습니다. 상속인이 상속 재산을 신고하지 않고도 퇴직금을 받을 수 있는 경우도 있지만, 경우에 따라 추가적인 절차가 필요할 수도 있습니다. 상속인은 상속 재산의 범위가 불분명하거나 상속 재산이 전혀 없을 수 있는 등 다양한 상황에 직면할 수 있기 때문에, 관련 법률 전문가의 조언을 구하는 것이 중요합니다.]` |
| kfkas/Legal-Llama-2-ko-7b-Chat | `[상속인의 고유 재산은 상속인에게 귀속되는 상속 재산입니다. 상속인이 상속 재산에 대한 권리와 의무를 행사할 수 있습니다. 상속 재산에는 상속인 고유 재산과 일반 상속 재산이 포함됩니다. 상속인은 상속 재산의 범위 내에서 상속 재산을 관리하고 처분할 수 있으며, 상속 재산 중 일부를 다른 상속인에게 증여할 수도 있습니다.그러나 상속 재산 중에서 상속인이 고유 재산으로 취득한 재산이 있는 경우, 상속인은 그 재산을 상속 재산에서 제외속세가 과세됩니다.따라서 상속 재산 중에 상속인이 소유한 고유 재산을 제외하고 상속 재산을 계산하여 상속세 신고를 해야 하며, 상속세 신고 시에는 상속 재산 목록을 작성하여 제출하여야 합니다. 또한, 상속세는 상속 개시일(사망일)로부터 6개월 이내에 신고해야 하며, 신고하지 않을 경우 가산세가 부과될 수 있으므로 주의해야 합니다.(참고: 상속세법 제18조)]`                                                                                                                                                                                                                                                                                        |
---
| Model              | 질문 : 재판이 끝난 후에 손해배상 청구를 할 수 있는지 궁금합니다. 부동산 관련 사기를 당해서 자세한 상담을 받고 싶어요                                                                                                                                                                                                                                                                                                        |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Llama-2-ko-7b-Chat | `[예, 재판이 끝난 후에도 민사 소송을 제기할 수 있습니다. 부동산 사기 또는 기타 민사 분쟁과 관련하여 변호사의 도움을 구할 수 있는 몇 가지 옵션이 있습니다:1. 민사 소송: 부동산 사기와 같은 민사 분쟁이 있는 경우 변호사를 고용하여 민사소송을 제기하여 손해 배상을 청구하는 것이 가장 일반적입니다.2. 개인 소장: 민사 사건에서 민사 소장을 작성하여 법원에 제출하는 것도 한 가지 방법입니다.3. 중재: 중재 기관을 통해 분쟁을 해결할 수도 있습니다.4. 형사 고소: 부동산 사기로 형사 고소가 가능한지 확인해야 합니다. 이러한 옵션 중 어떤 것을 선택할지 결정하기 전에 변호사와 상담하여 조언을 구하는 것이 좋습니다.]`                 |
| Legal-Llama-2-ko-7b-Chat | `[예, 재판이 끝난 후에도 손해배상 청구가 가능합니다. 민사소송법 제766조(손해배상청구권의 소멸시효)에 따르면, 불법행위로 인한 손해배상의 청구권은 피해자나 그 법정대리인이 그 손해 및 가해자를 안 날로부터 3년간 이를 행사하지 아니하면 시효로 인하여 소멸한다고 규정하고 있습니다.따라서 부동산 사기로 인해 입은 손해를 입증할 수 있는 증거와 증인을 확보하고, 법원에 손해배상을 청구할 수 있습니다. 또한, 부동산 사기를 당한 사실을 경찰에 신고하여 수사를 의뢰하는 것도 좋은 방법입니다.]`                                                                                                                                                                                     |
---


### Inference

```python
def gen(x, model, tokenizer, device):
    prompt = (
        f"아래는 작업을 설명하는 명령어입니다. 요청을 적절히 완료하는 응답을 작성하세요.\n\n### 명령어:\n{x}\n\n### 응답:"
    )
    len_prompt = len(prompt)
    gened = model.generate(
        **tokenizer(prompt, return_tensors="pt", return_token_type_ids=False).to(
            device
        ),
        max_new_tokens=1024,
        early_stopping=True,
        do_sample=True,
        top_k=20,
        top_p=0.92,
        no_repeat_ngram_size=3,
        eos_token_id=2,
        repetition_penalty=1.2,
        num_beams=3
    )
    return tokenizer.decode(gened[0])[len_prompt:]

def LLM_infer(input):
    device = (
        torch.device("cuda:0") if torch.cuda.is_available() else torch.device("cpu")
    )
    model_id = "kfkas/Legal-Llama-2-ko-7b-Chat"
    model = AutoModelForCausalLM.from_pretrained(
        model_id, device_map={"": 0},torch_dtype=torch.float16, low_cpu_mem_usage=True
    )
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model.eval()
    model.config.use_cache = (True)
    tokenizer.pad_token = tokenizer.eos_token
    output = gen(input, model=model, tokenizer=tokenizer, device=device)

    return output


if __name__ == "__main__":
    text = LLM_infer("음주운전을 하면 어떻게 처벌 받아?")
    print(text)
```

## Note for oobabooga/text-generation-webui

Remove `ValueError` at `load_tokenizer` function(line 109 or near), in `modules/models.py`.

```python
diff --git a/modules/models.py b/modules/models.py
index 232d5fa..de5b7a0 100644
--- a/modules/models.py
+++ b/modules/models.py
@@ -106,7 +106,7 @@ def load_tokenizer(model_name, model):
                 trust_remote_code=shared.args.trust_remote_code,
                 use_fast=False
             )
-        except ValueError:
+        except:
             tokenizer = AutoTokenizer.from_pretrained(
                 path_to_model,
                 trust_remote_code=shared.args.trust_remote_code,
```

Since Llama-2-Ko uses FastTokenizer provided by HF tokenizers NOT sentencepiece package, 
it is required to use `use_fast=True` option when initialize tokenizer.

Apple Sillicon does not support BF16 computing, use CPU instead. (BF16 is supported when using NVIDIA GPU)


---

> Below is the original model card of the Llama-2 model.

# **Llama 2**
Llama 2 is a collection of pretrained and fine-tuned generative text models ranging in scale from 7 billion to 70 billion parameters. This is the repository for the 7B pretrained model, converted for the Hugging Face Transformers format. Links to other models can be found in the index at the bottom.

## Model Details
*Note: Use of this model is governed by the Meta license. In order to download the model weights and tokenizer, please visit the [website](https://ai.meta.com/resources/models-and-libraries/llama-downloads/) and accept our License before requesting access here.*

Meta developed and publicly released the Llama 2 family of large language models (LLMs), a collection of pretrained and fine-tuned generative text models ranging in scale from 7 billion to 70 billion parameters. Our fine-tuned LLMs, called Llama-2-Chat, are optimized for dialogue use cases. Llama-2-Chat models outperform open-source chat models on most benchmarks we tested, and in our human evaluations for helpfulness and safety, are on par with some popular closed-source models like ChatGPT and PaLM.

**Model Developers** Meta

**Variations** Llama 2 comes in a range of parameter sizes — 7B, 13B, and 70B — as well as pretrained and fine-tuned variations.

**Input** Models input text only.

**Output** Models generate text only.

**Model Architecture** Llama 2 is an auto-regressive language model that uses an optimized transformer architecture. The tuned versions use supervised fine-tuning (SFT) and reinforcement learning with human feedback (RLHF) to align to human preferences for helpfulness and safety.


||Training Data|Params|Content Length|GQA|Tokens|LR|
|---|---|---|---|---|---|---|
|Llama 2|*A new mix of publicly available online data*|7B|4k|&#10007;|2.0T|3.0 x 10<sup>-4</sup>|
|Llama 2|*A new mix of publicly available online data*|13B|4k|&#10007;|2.0T|3.0 x 10<sup>-4</sup>|
|Llama 2|*A new mix of publicly available online data*|70B|4k|&#10004;|2.0T|1.5 x 10<sup>-4</sup>|

*Llama 2 family of models.* Token counts refer to pretraining data only. All models are trained with a global batch-size of 4M tokens. Bigger models -  70B -- use Grouped-Query Attention (GQA) for improved inference scalability.

**Model Dates** Llama 2 was trained between January 2023 and July 2023.

**Status** This is a static model trained on an offline dataset. Future versions of the tuned models will be released as we improve model safety with community feedback.

**License** A custom commercial license is available at: [https://ai.meta.com/resources/models-and-libraries/llama-downloads/](https://ai.meta.com/resources/models-and-libraries/llama-downloads/)

**Research Paper** ["Llama-2: Open Foundation and Fine-tuned Chat Models"](arxiv.org/abs/2307.09288)

## Intended Use
**Intended Use Cases** Llama 2 is intended for commercial and research use in English. Tuned models are intended for assistant-like chat, whereas pretrained models can be adapted for a variety of natural language generation tasks.

To get the expected features and performance for the chat versions, a specific formatting needs to be followed, including the `INST` and `<<SYS>>` tags, `BOS` and `EOS` tokens, and the whitespaces and breaklines in between (we recommend calling `strip()` on inputs to avoid double-spaces). See our reference code in github for details: [`chat_completion`](https://github.com/facebookresearch/llama/blob/main/llama/generation.py#L212).

**Out-of-scope Uses** Use in any manner that violates applicable laws or regulations (including trade compliance laws).Use in languages other than English. Use in any other way that is prohibited by the Acceptable Use Policy and Licensing Agreement for Llama 2.

## Hardware and Software
**Training Factors** We used custom training libraries, Meta's Research Super Cluster, and production clusters for pretraining. Fine-tuning, annotation, and evaluation were also performed on third-party cloud compute.

**Carbon Footprint** Pretraining utilized a cumulative 3.3M GPU hours of computation on hardware of type A100-80GB (TDP of 350-400W). Estimated total emissions were 539 tCO2eq, 100% of which were offset by Meta’s sustainability program.

||Time (GPU hours)|Power Consumption (W)|Carbon Emitted(tCO<sub>2</sub>eq)|
|---|---|---|---|
|Llama 2 7B|184320|400|31.22|
|Llama 2 13B|368640|400|62.44|
|Llama 2 70B|1720320|400|291.42|
|Total|3311616||539.00|

**CO<sub>2</sub> emissions during pretraining.** Time: total GPU time required for training each model. Power Consumption: peak power capacity per GPU device for the GPUs used adjusted for power usage efficiency. 100% of the emissions are directly offset by Meta's sustainability program, and because we are openly releasing these models, the pretraining costs do not need to be incurred by others.

## Training Data
**Overview** Llama 2 was pretrained on 2 trillion tokens of data from publicly available sources. The fine-tuning data includes publicly available instruction datasets, as well as over one million new human-annotated examples. Neither the pretraining nor the fine-tuning datasets include Meta user data.

**Data Freshness** The pretraining data has a cutoff of September 2022, but some tuning data is more recent, up to July 2023.

## Evaluation Results

In this section, we report the results for the Llama 1 and Llama 2 models on standard academic benchmarks.For all the evaluations, we use our internal evaluations library.

|Model|Size|Code|Commonsense Reasoning|World Knowledge|Reading Comprehension|Math|MMLU|BBH|AGI Eval|
|---|---|---|---|---|---|---|---|---|---|
|Llama 1|7B|14.1|60.8|46.2|58.5|6.95|35.1|30.3|23.9|
|Llama 1|13B|18.9|66.1|52.6|62.3|10.9|46.9|37.0|33.9|
|Llama 1|33B|26.0|70.0|58.4|67.6|21.4|57.8|39.8|41.7|
|Llama 1|65B|30.7|70.7|60.5|68.6|30.8|63.4|43.5|47.6|
|Llama 2|7B|16.8|63.9|48.9|61.3|14.6|45.3|32.6|29.3|
|Llama 2|13B|24.5|66.9|55.4|65.8|28.7|54.8|39.4|39.1|
|Llama 2|70B|**37.5**|**71.9**|**63.6**|**69.4**|**35.2**|**68.9**|**51.2**|**54.2**|

**Overall performance on grouped academic benchmarks.** *Code:* We report the average pass@1 scores of our models on HumanEval and MBPP. *Commonsense Reasoning:* We report the average of PIQA, SIQA, HellaSwag, WinoGrande, ARC easy and challenge, OpenBookQA, and CommonsenseQA. We report 7-shot results for CommonSenseQA and 0-shot results for all other benchmarks. *World Knowledge:* We evaluate the 5-shot performance on NaturalQuestions and TriviaQA and report the average. *Reading Comprehension:* For reading comprehension, we report the 0-shot average on SQuAD, QuAC, and BoolQ. *MATH:* We report the average of the GSM8K (8 shot) and MATH (4 shot) benchmarks at top 1.

|||TruthfulQA|Toxigen|
|---|---|---|---|
|Llama 1|7B|27.42|23.00|
|Llama 1|13B|41.74|23.08|
|Llama 1|33B|44.19|22.57|
|Llama 1|65B|48.71|21.77|
|Llama 2|7B|33.29|**21.25**|
|Llama 2|13B|41.86|26.10|
|Llama 2|70B|**50.18**|24.60|

**Evaluation of pretrained LLMs on automatic safety benchmarks.** For TruthfulQA, we present the percentage of generations that are both truthful and informative (the higher the better). For ToxiGen, we present the percentage of toxic generations (the smaller the better).


|||TruthfulQA|Toxigen|
|---|---|---|---|
|Llama-2-Chat|7B|57.04|**0.00**|
|Llama-2-Chat|13B|62.18|**0.00**|
|Llama-2-Chat|70B|**64.14**|0.01|

**Evaluation of fine-tuned LLMs on different safety datasets.** Same metric definitions as above.

## Ethical Considerations and Limitations
Llama 2 is a new technology that carries risks with use. Testing conducted to date has been in English, and has not covered, nor could it cover all scenarios. For these reasons, as with all LLMs, Llama 2’s potential outputs cannot be predicted in advance, and the model may in some instances produce inaccurate, biased or other objectionable responses to user prompts. Therefore, before deploying any applications of Llama 2, developers should perform safety testing and tuning tailored to their specific applications of the model.

Please see the Responsible Use Guide available at [https://ai.meta.com/llama/responsible-use-guide/](https://ai.meta.com/llama/responsible-use-guide)

## Reporting Issues
Please report any software “bug,” or other problems with the models through one of the following means:
- Reporting issues with the model: [github.com/facebookresearch/llama](http://github.com/facebookresearch/llama)
- Reporting problematic content generated by the model: [developers.facebook.com/llama_output_feedback](http://developers.facebook.com/llama_output_feedback)
- Reporting bugs and security concerns: [facebook.com/whitehat/info](http://facebook.com/whitehat/info)

## Llama Model Index
|Model|Llama2|Llama2-hf|Llama2-chat|Llama2-chat-hf|
|---|---|---|---|---|
|7B| [Link](https://huggingface.co/llamaste/Llama-2-7b) | [Link](https://huggingface.co/llamaste/Llama-2-7b-hf) | [Link](https://huggingface.co/llamaste/Llama-2-7b-chat) | [Link](https://huggingface.co/llamaste/Llama-2-7b-chat-hf)|
|13B| [Link](https://huggingface.co/llamaste/Llama-2-13b) | [Link](https://huggingface.co/llamaste/Llama-2-13b-hf) | [Link](https://huggingface.co/llamaste/Llama-2-13b-chat) | [Link](https://huggingface.co/llamaste/Llama-2-13b-hf)|
|70B| [Link](https://huggingface.co/llamaste/Llama-2-70b) | [Link](https://huggingface.co/llamaste/Llama-2-70b-hf) | [Link](https://huggingface.co/llamaste/Llama-2-70b-chat) | [Link](https://huggingface.co/llamaste/Llama-2-70b-hf)|
