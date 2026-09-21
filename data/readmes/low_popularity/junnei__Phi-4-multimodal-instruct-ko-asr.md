---
library_name: transformers
datasets:
- Bingsu/zeroth-korean
- google/fleurs
language:
- ko
metrics:
- cer
- wer
- bleu
base_model:
- microsoft/Phi-4-multimodal-instruct
model-index:
- name: Phi-4-multimodal-instruct-ko-asr
  results:
  - task:
      type: automatic-speech-recognition
    dataset:
      type: Bingsu/zeroth_korean
      name: zeroth-korean-test
    metrics:
    - type: bleu
      name: zeroth-test-BLEU
      value: 94.837
    - type: cer
      name: zeroth-test-CER
      value: 1.316
    - type: wer
      name: zeroth-test-WER
      value: 2.951
  - task:
      type: automatic-speech-recognition
    dataset:
      type: google/flerus
      name: flerus-ko-test
    metrics:
    - type: bleu
      name: fleurs-test-BLEU
      value: 67.659
    - type: cer
      name: fleurs-test-CER
      value: 7.951
    - type: wer
      name: fleurs-test-WER
      value: 18.313
pipeline_tag: automatic-speech-recognition
---



This model is fine-tuned from [microsoft/Phi-4-multimodal-instruct](https://huggingface.co/microsoft/Phi-4-multimodal-instruct) on [Bingsu/zeroth-korean](https://huggingface.co/datasets/Bingsu/zeroth-korean), [google/flerus](https://huggingface.co/datasets/Bingsu/google/flerus) in 5 epochs.

This model is trained 960 steps on datasets for Korean Audio Speech Recognition on H100.

After that, we continue training with [CoVoST2 Dataset][Covost2] / [CoVoST2-Ko][Covost2-ko] for AST.

AST Finetuned model is Here : [Phi-4-multimodal-instruct-ko-speech][Speech]

[Covost2]: https://huggingface.co/datasets/junnei/covost2
[Covost2-ko]: https://huggingface.co/datasets/junnei/covost2-ko
[Speech]: https://huggingface.co/junnei/Phi-4-multimodal-instruct-ko-speech

## Evaluation

Evaluation was done on the following datasets:
- ASR (Automatic Speech Recognition): Evaluated with CER (Character Error Rate) on zeroth-test set (457 samples).
- AST (Automatic Speech Translation): Evaluated with BLEU score on fleurs ko <-> en speech translation result (270 samples).

Script is retrieved from [here](https://gist.github.com/seastar105/d1d8983b27611370528e3b194dcc5577#file-evaluate-py).

Compared to [Phi-4-mm-inst-zeroth-kor](https://huggingface.co/seastar105/Phi-4-mm-inst-zeroth-kor) and  [Phi-4-multimodal-finetune-ko-speech](https://huggingface.co/daekeun-ml/Phi-4-multimodal-finetune-ko-speech), ASR is significantly improved.

| Model                                          | zeroth-CER  | zeroth-WER | fleurs-ko_en-BLEU | fleurs-ko_en-cot-BLEU | fleurs-en_ko-BLEU | fleurs-en_ko-cot-BLEU |
|------------------------------------------------|-------------|------------|-------------------|-----------------------|-------------------|-----------------------|
| original                                       |  198.32     |     -      |       5.63        |         2.42          |       6.86        |         4.17          |
| daekeun-ml/Phi-4-multimodal-finetune-ko-speech |  1.61       |    3.54    |       7.67        |         8.38          |       12.31       |         9.69          |
| seastar105/Phi-4-mm-inst-zeroth-kor            |  7.02       |     -      |       7.07        |         9.19          |       13.08       |         9.35          |
| **ASR finetune(this model)**                   |  **1.31**   |    2.95    |       7.46        |         6.24          |       12.15       |         8.91          |
| + 1 epoch finetune with [Covost-Ko][Covost2-ko]|  3.88       |     -      |     **8.07**      |       **10.09**       |     **18.82**     |      **15.41**        |
| [**AST finetuned model**][Speech]              |  **1.77**   |  **2.99**  |     **8.01**      |       **9.09**        |     **17.09**     |      **11.82**        | 

