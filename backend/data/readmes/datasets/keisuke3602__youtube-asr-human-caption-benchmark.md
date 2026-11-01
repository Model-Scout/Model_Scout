---
license: cc-by-4.0
language: [en, es, ko, ja, vi, pt, zh, th, hi]
pretty_name: Whisper large-v3 on YouTube audio, scored against uploaded captions
task_categories: [automatic-speech-recognition]
size_categories: [n<1K]
configs:
- config_name: per_video
  data_files: scores_per_video.csv
  default: true
- config_name: per_language
  data_files: summary_per_language.csv
---


# Whisper large-v3 on YouTube audio, scored against uploaded captions

Error rates of open speech-to-text models on 234 public YouTube videos in 9 languages. The reference for each video
is the caption track the channel uploaded in the video's own language, not an auto-generated track and not any
system's output, so no system under test is graded against itself.

This dataset holds **scores only**: per-video error rates keyed by YouTube video ID, per-language summaries, the
scoring script and the compute-cost method. It contains no audio, no caption text and no transcripts.

## Systems

| system | what it is |
|---|---|
| whisper-large-v3_two-pass | faster-whisper 1.1.1, large-v3, beam 5, Silero VAD; a second pass without VAD when the first returns under 30 characters per minute |
| whisper-large-v3_two-pass_batched | the same, first pass through faster-whisper's batched pipeline (batch 16) |
| whisper-large-v3_version-c | batched, language detected at three points in the audio, low-threshold VAD on the second pass |
| kotoba-whisper-v2.0_two-pass | Japanese only, first 180 videos only |
| reazonspeech-nemo-v2 | Japanese only, first 180 videos only |
| commercial-api | a commercial speech-to-text API, not named |

All open models ran on an NVIDIA T4 (Modal).

## Selection and filters

- Videos: public, 3 to 15 minutes, with an uploaded caption track in the language under test; 20 per language
  picked first, then 6 more per language that required the video's declared audio language to match.
- Filter 1, translated captions: a video is dropped when the speech is not in the caption's language (language as
  settled by Whisper large-v3 two-pass). Many non-English uploaded captions are translations.
- Filter 2, caption coverage: a video is dropped when its caption is under half the shortest system output or over
  twice the longest, i.e. every system disagrees with the caption in the same direction (partial or unrelated
  caption). One system failing alone never removes a video.
- `scores_per_video.csv` keeps every scored video, with `translated_caption` and `caption_coverage_fail` flags;
  `summary_per_language.csv` uses only videos that pass both filters.

## Metric

CER for ja, zh, th, ko; WER for the others. NFKC, lower case, punctuation and symbols removed, whitespace collapsed,
Chinese folded to Simplified on both sides. `score.py` reproduces the per-video rates given reference and
hypothesis text files. Summary: median per-video rate, and corpus rate (total edits / total reference units) with a
95% bootstrap interval over videos.

## Files

- `scores_per_video.csv`: video_id, language, metric, system, reference_units, hypothesis_units, edits, error_rate,
  translated_caption, caption_coverage_fail
- `summary_per_language.csv`: language, metric, system, videos, median_error_rate, corpus_error_rate, ci95_low,
  ci95_high
- `score.py`: the scorer (MIT)
- `COMPUTE_COST.md`: how the GPU cost per audio hour was measured

## Limits

- 13 to 26 videos per language after filtering; medians are indicative.
- Uploaded captions are not always verbatim (edited, abridged), which raises every system's error alike.
- Videos can be removed or made private after publication; the scores stay but cannot be re-derived.

## License and rights

Scores and documentation: CC BY 4.0. `score.py`: MIT. Rights holder: Glasp.
The underlying videos and captions belong to their uploaders and are not included.

To have a video removed from this dataset, open a discussion in the Community tab with the video ID.