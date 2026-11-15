---
language:
  - en
  - zh
  - de
  - es
  - ru
  - ko
  - fr
  - ja
  - pt
  - tr
  - pl
  - ca
  - nl
  - ar
  - sv
  - it
  - id
  - hi
  - fi
  - vi
  - he
  - uk
  - el
  - ms
  - cs
  - ro
  - da
  - hu
  - ta
  - 'no'
  - th
  - ur
  - hr
  - bg
  - lt
  - la
  - mi
  - ml
  - cy
  - sk
  - te
  - fa
  - lv
  - bn
  - sr
  - az
  - sl
  - kn
  - et
  - mk
  - br
  - eu
  - is
  - hy
  - ne
  - mn
  - bs
  - kk
  - sq
  - sw
  - gl
  - mr
  - pa
  - si
  - km
  - sn
  - yo
  - so
  - af
  - oc
  - ka
  - be
  - tg
  - sd
  - gu
  - am
  - yi
  - lo
  - uz
  - fo
  - ht
  - ps
  - tk
  - nn
  - mt
  - sa
  - lb
  - my
  - bo
  - tl
  - mg
  - as
  - tt
  - haw
  - ln
  - ha
  - ba
  - jw
  - su
tags:
- ctranslate2
- int8
- whisper
- whisper-large-v3-turbo
- automatic-speech-recognition
- audio
license: mit
library_name: ctranslate2
datasets:
- librispeech_asr
metrics:
- wer
inference: false
---

# Whisper large-v3-turbo INT8 CTranslate2

## Fast-Inference with CTranslate2

Speedup inference while reducing memory using INT8 quantization with CTranslate2.

This is a quantized version of [openai/whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo) converted to [CTranslate2](https://github.com/OpenNMT/CTranslate2) format.

Compatible with [faster-whisper](https://github.com/SYSTRAN/faster-whisper) and CTranslate2 directly.

```bash
pip install faster-whisper
```

**Checkpoint compatible with CTranslate2 >= 3.22.0**

- `compute_type=int8` for both CPU and GPU

### Usage example

```python
from faster_whisper import WhisperModel

model = WhisperModel("/path/to/whisper-turbo", device="cuda", compute_type="int8")

segments, info = model.transcribe("audio.mp3", beam_size=5, language="es")
for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
```

### Conversion details

This model was converted using `ct2-transformers-converter` with INT8 quantization. After conversion, the original model files (normalizer.json, preprocessor_config.json, vocab.json, vocabulary.json, etc.) were copied and merged to preserve full compatibility.

```bash
ct2-transformers-converter --model openai/whisper-large-v3-turbo --output_dir /path/to/whisper-turbo \
    --copy_files tokenizer.json --quantization int8
```

## License

This model is a quantized version of [openai/whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo), which is released under the **MIT** license. The same license applies to this conversion.

## Model description

**Whisper large-v3-turbo** is a optimized variant of Whisper large-v3 from OpenAI. It uses the same 32-layer encoder as large-v3 but with a reduced 4-layer decoder, significantly improving inference speed while maintaining competitive quality.

- **Paper:** [Robust Speech Recognition via Large-Scale Weak Supervision](https://arxiv.org/abs/2212.04356) (Radford et al., 2022)
- **Original model:** [openai/whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo)
- **Repository:** [github.com/openai/whisper](https://github.com/openai/whisper)

### Supported languages

99 languages: Afrikaans, Arabic, Armenian, Azerbaijani, Belarusian, Bosnian, Bulgarian, Catalan, Chinese, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, Galician, German, Greek, Hebrew, Hindi, Hungarian, Icelandic, Indonesian, Italian, Japanese, Kannada, Kazakh, Korean, Latvian, Lithuanian, Macedonian, Malay, Marathi, Maori, Nepali, Norwegian, Persian, Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, Swahili, Swedish, Tagalog, Tamil, Thai, Turkish, Ukrainian, Urdu, Vietnamese, Welsh, and more.

### Metrics

Evaluated using Word Error Rate (WER) on LibriSpeech and other benchmarks. See the [original model card](https://huggingface.co/openai/whisper-large-v3-turbo) for detailed metrics.

### Evaluation Data

Whisper was evaluated on LibriSpeech, Common Voice, Fleurs, and other multilingual speech datasets.

### Training Data

Trained on 680,000 hours of multilingual and multitask supervised data collected from the web.

### Ethical Considerations

Whisper may transcribe speech inaccurately, particularly for accented speech, low-resource languages, or noisy environments. The model should not be used as a sole decision-making tool in sensitive domains. Whisper's training data was sourced from the web and may contain biases.

### Caveats and Recommendations

Performance varies by language and domain. For best results, use audio with clear speech and minimal background noise. The model is not intended for speaker identification or verification.

## Repository

**Hugging Face:** [mijuanlo/whisper-large-v3-turbo-ct2-int8](https://huggingface.co/mijuanlo/whisper-large-v3-turbo-ct2-int8)
