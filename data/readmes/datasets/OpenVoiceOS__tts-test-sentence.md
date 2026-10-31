---
license: cc0-1.0
language:
  - af
  - am
  - ar
  - az
  - be
  - bg
  - bn
  - ca
  - ceb
  - cs
  - cy
  - da
  - de
  - el
  - en
  - eo
  - es
  - et
  - eu
  - fa
  - fi
  - fr
  - ga
  - gd
  - gl
  - gu
  - ha
  - he
  - hi
  - hr
  - ht
  - hu
  - hy
  - id
  - ig
  - is
  - it
  - ja
  - jv
  - ka
  - kk
  - kn
  - ko
  - ku
  - ky
  - la
  - lb
  - lo
  - lt
  - lv
  - mk
  - ml
  - mn
  - mr
  - ms
  - mt
  - my
  - nb
  - ne
  - nl
  - ny
  - oc
  - pa
  - pl
  - pt
  - ro
  - ru
  - rw
  - si
  - sk
  - sl
  - sn
  - so
  - sq
  - sr
  - sv
  - sw
  - ta
  - te
  - tg
  - th
  - tk
  - tl
  - tr
  - uk
  - ur
  - uz
  - vi
  - xh
  - yo
  - zh
  - zu
tags: [tts, text-to-speech, evaluation, multilingual]
pretty_name: TTS Test Sentence
size_categories: [n<1K]
---

# tts-test-sentence

One canonical **TTS test sentence** — the *rainbow sentence* — translated across
languages and scripts, for quickly sanity-checking multilingual text-to-speech
voices (does the voice produce intelligible speech in its language?).

**English source:** *After the rain, a colorful rainbow appeared in the sky, and the children went outside to look at it.*

Each row: `lang` (BCP-47), `language` (name), `script` (ISO-15924), `text`
(native translation), `source_en`. Some languages appear in multiple scripts
(e.g. Serbian: `sr-Cyrl` / `sr-Latn`).

```python
from datasets import load_dataset
ds = load_dataset("OpenVoiceOS/tts-test-sentence", split="train")
```

Many translations are best-effort (some AI-authored); corrections and additional languages/scripts are very welcome. The ~1000 long-tail MMS languages (one voice each) are not yet covered.
