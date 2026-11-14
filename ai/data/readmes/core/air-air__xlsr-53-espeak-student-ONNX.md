---
license: apache-2.0
library_name: transformers.js
pipeline_tag: automatic-speech-recognition
base_model: facebook/wav2vec2-xlsr-53-espeak-cv-ft
base_model_relation: finetune
datasets:
- google/fleurs
language:
- de
- es
- fr
- it
- ja
- ko
- pl
- pt
- ru
- sv
tags:
- onnx
- phoneme-recognition
- ctc
- wav2vec2
- distillation
---

# xlsr-53-espeak-student (ONNX, 4-bit)

A small multilingual phoneme recogniser for the browser. It's
[facebook/wav2vec2-xlsr-53-espeak-cv-ft](https://huggingface.co/facebook/wav2vec2-xlsr-53-espeak-cv-ft)
cut from 24 transformer layers to 8, then trained to hear what the full model hears. It's a
**77 MB** download, against 241 MB for the full model at the same precision, and about three
times faster.

## How it was made

- **Student.** It started as the full model's layers 0, 3, 7, 10, 13, 16, 20 and 23, with its
  feature encoder, positional convolution and CTC head. Everything but the feature encoder was
  then trained.
- **Distillation.** For every 20 ms frame, the student was trained on the full model's
  distribution over its 16 likeliest phones (cross-entropy against the renormalised top 16). No
  transcripts were needed.
- **Audio.** [FLEURS](https://huggingface.co/datasets/google/fleurs) train splits in German,
  Spanish, French, Italian, Japanese, Korean, Polish, Portuguese, Russian and Swedish (88
  hours). It also used short crops of the same audio with 150 ms of silence either side. The
  student heard everything with random gain and noise (10–40 dB below the speech) that the full
  model didn't.
- **Training.** AdamW at a 3e-5 peak learning rate, with the feature encoder frozen. It kept the
  checkpoint with the best held-out loss on FLEURS dev.
- **Export.** ONNX with the matrix weights quantised to 4 bits (block 32), and the convolution
  weights stored as 8-bit with a DequantizeLinear in front of each Conv.

On held-out FLEURS dev audio, the student's likeliest phone matches the full model's on 67% of
the frames where the full model hears a phone (the blank aside).

## Limitations

It knows what the full model knows. That model wasn't fine-tuned on Japanese or Korean, so both
come out in the phones of other languages, and the student copies that. It was trained and
checked on read speech.

## Use

The vocabulary is the full model's: 392 espeak phones, with `<pad>` (id 0) as the CTC blank.

```js
import { AutoFeatureExtractor, AutoModelForCTC } from '@huggingface/transformers';

const id = 'air-air/xlsr-53-espeak-student-ONNX';
const extractor = await AutoFeatureExtractor.from_pretrained(id);
const model = await AutoModelForCTC.from_pretrained(id, { dtype: 'q4' });
const { logits } = await model(await extractor(audio)); // audio: Float32Array, 16 kHz mono
```

## Licence

Apache License 2.0, as the source model is released (see `LICENSE`). FLEURS is CC BY 4.0
(Conneau et al., 2022).
