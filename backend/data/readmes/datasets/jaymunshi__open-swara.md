---
license: cc-by-sa-4.0
task_categories:
  - text-to-speech
language:
  - ar
  - bg
  - ca
  - zh
  - cs
  - da
  - nl
  - en
  - fi
  - fr
  - ka
  - de
  - el
  - he
  - hi
  - hu
  - is
  - id
  - it
  - ja
  - kk
  - ko
  - lo
  - lv
  - lb
  - ml
  - ne
  - no
  - fa
  - pl
  - pt
  - ro
  - ru
  - sr
  - sk
  - sl
  - es
  - sw
  - sv
  - te
  - tr
  - tw
  - uk
  - vi
  - cy
tags:
  - voice-cloning
  - speech-synthesis
  - multilingual
  - tts
  - audio
  - voice
size_categories:
  - 1K<n<10K
---

# Open Swara

**The largest open-source humanized voice library** -- 4,065 voice samples across 44 languages, free forever under CC-BY-SA 4.0.

## What Is Open Swara?

We collected raw AI/synthetic voice samples from 10 open-source datasets, then **humanized every single one** through our proprietary voice processing pipeline. The original synthetic artifacts -- robotic tone, unnatural cadence, flat prosody -- are replaced with natural-sounding speech while preserving each voice's unique timbre, pitch, and character.

## Stats

| Metric | Count |
|--------|-------|
| Total voices | 4,065 |
| Languages | 44 |
| Native language voices | 3,454 |
| English accent voices | 611 |
| Male voices | 2,105 |
| Female voices | 1,818 |
| Unknown gender | 142 |

## Structure

```
voices/
  {language}/{gender}/{language}_{gender}_open_swara_{NNN}.wav          -- native language
  {language}/{gender}/{language}_{gender}_english_open_swara_{NNN}.wav  -- English accent
```

## Usage

These voices are ideal as **reference samples** for:
- Text-to-Speech (TTS) voice cloning
- Voice conversion systems
- Multilingual dubbing and localization
- Audiobook narration prototyping
- Creative and research projects

## License

**CC-BY-SA 4.0** -- free for commercial and non-commercial use with attribution.

## Attribution

> Voices from [Open Swara](https://github.com/jaymunshi/open-swara).
