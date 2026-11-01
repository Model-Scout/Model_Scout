---
license: cc-by-4.0
language: [ko]
task_categories: [automatic-speech-recognition]
pretty_name: CampusVoice-RT evaluation set
---
# CampusVoice-RT evaluation set

Korean read speech (Zeroth-Korean test, FLEURS ko_kr test; both CC BY 4.0) mixed with
outdoor noise from FSD50K (CC0 / CC BY clips only) at SNR 20 / 10 / 5 / 0 dB, plus the
clean condition, each with 1 s of noise (or silence) before and after the utterance.
Built by https://github.com/ekgP525/asr-challenge (`data/scripts/`), seed 2026.

Files: `audio.tar.gz` (all audio in one archive; download this), `audio/<condition>/<id>.wav`
(same files, browsable), `manifest.jsonl`, `noise_list.csv`, `LICENSES/`.

```bash
huggingface-cli download ekgP115/campusvoice-rt-eval --repo-type dataset     --include manifest.jsonl audio.tar.gz --local-dir data/eval && tar -xzf data/eval/audio.tar.gz -C data/eval
```
