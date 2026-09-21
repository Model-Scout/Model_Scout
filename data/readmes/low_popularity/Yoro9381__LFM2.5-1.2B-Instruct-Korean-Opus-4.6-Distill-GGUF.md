---
base_model: Yoro9381/LFM2.5-1.2B-Instruct-Korean-Opus-4.6-Distill
library_name: transformers
pipeline_tag: text-generation
license: other
license_name: lfm-open-license-v1.0
license_link: https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct/blob/main/LICENSE
tags:
- unsloth
- lfm2
- lfm2.5
- korean
- text-generation
- conversational
- instruction-tuned
datasets:
- Jongsim/claude-opus-4.6-reasoning-12k-ko-filtered-v2
language:
- ko
---
# LFM2.5-1.2B-Instruct-Korean

## Model Overview

`LFM2.5-1.2B-Instruct-Korean` is a Korean instruction-following language model based on `LiquidAI/LFM2.5-1.2B-Instruct`.  
This model was fine-tuned on Korean-centered datasets with the goal of improving performance on Korean question answering, general conversation, and instruction-following tasks.

The model is designed to generate responses that are more natural, consistent, and contextually appropriate in Korean.

## Base Model

- **Base model**: `LiquidAI/LFM2.5-1.2B-Instruct`

## Training Data

This model was fine-tuned using the following Korean-centered datasets:

- `maywell/koVast`
- `CarrotAI/ko-instruction-dataset`
- `MarkrAI/KoCommercial-Dataset`
- `Jongsim/claude-opus-4.6-reasoning-12k-ko-filtered-v2`

The training data includes Korean instruction-response pairs, general conversational data, and commercially or practically oriented text.  
This setup was intended to help the model learn a broad range of Korean expressions, styles, and contexts.

## Training Details

The model was trained for **3 full epochs** over the entire dataset.  
Training proceeded for a total of **2,160 steps** and was completed successfully without interruption.

### Training Summary

- **Number of epochs**: 3
- **Total training steps**: 2,160
- **Training completion status**: Completed
- **Training status**: Stable

## Evaluation Results

The final evaluation metrics are as follows:

- **training_loss**: 0.9999
- **eval_loss**: 1.0480
- **eval_mean_token_accuracy**: 0.7445

These results show that the training loss and evaluation loss remained at nearly the same level, suggesting that the model demonstrated relatively stable generalization performance on the validation set without a clear sign of overfitting.

## Result Interpretation

One notable point in this experiment is the very small gap between **training loss** and **evaluation loss**.

- **training_loss = 0.9999**
- **eval_loss = 1.0480**

In general, a large gap between these two values may indicate overfitting.  
However, in this experiment, the difference was very small, which suggests that the model adapted to the training data in a stable manner while maintaining a similar level of performance on the validation set.

In addition, the result of **eval_mean_token_accuracy = 0.7445** indicates that the model predicts the next token in a relatively stable and consistent way.  
Taken together, these results suggest that the model successfully learned the major patterns in the training data and converged stably without severe instability.

## Overall Conclusion

This fine-tuning was completed successfully and showed overall solid results.  
The close alignment between training loss and evaluation loss suggests that the model did not significantly overfit during training and that the optimization process remained stable.

Moreover, no sharp divergence in loss values was observed throughout the training process.  
Therefore, this experiment can be regarded as a fine-tuning run that converged stably overall.

## Limitations and Future Work

While these metrics are useful for assessing training stability and convergence, they do not fully reflect response quality, factuality, instruction-following accuracy, or real-world usability.

To obtain a more comprehensive evaluation of the model, the following additional assessments are planned:

- evaluation on real user question-answer examples
- downstream task performance evaluation
- qualitative analysis of generated responses
- safety and hallucination checks

Through these follow-up evaluations, we aim to verify whether the model can go beyond stable training-time metrics and provide reliable and consistent performance in real-world usage scenarios.

## License

This model is a fine-tuned derivative of `LiquidAI/LFM2.5-1.2B-Instruct`.

Use and distribution of this model are subject to the terms of the **LFM Open License v1.0** applicable to the base model.

Please also review any additional obligations arising from the datasets used during fine-tuning.

## Feedback

This model will continue to be improved through further evaluation and refinement.  
If you have any feedback on your experience using the model or notice areas that need improvement, your input will be carefully considered and reflected in future quality improvements.  
Your feedback will be a great source of support in improving and further developing the model.