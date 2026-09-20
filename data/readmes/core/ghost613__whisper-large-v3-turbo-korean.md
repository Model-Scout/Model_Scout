---
datasets:
- Bingsu/zeroth-korean
language:
- ko
metrics:
- cer
- wer
base_model:
- openai/whisper-large-v3-turbo
pipeline_tag: automatic-speech-recognition
---

## Description
Fine-tuning Whisper Large V3 Turbo on zeroth Korean dataset. 

## Dataset split: 
- The test dataset from Korean zeroth is divided to test and validation -> 50% validation, 50% test
- Train set duration: 206 hours 43 minutes
- Validation set duration: 2 hours 22 minutes
- Test set duration: 2 hours 22 minutes

## Results: 
- initial validation WER: 26.26%
- final validation WER: 4.90%
- initial validation CER: 6.67%
- final validation CER: 1.78%
- initial test WER: 26.75%
- final test WER: 4.89%
- initial test CER: 7.58%
- final test CER: 2.06%

## Notes
- Models did not converge, better results are possible.