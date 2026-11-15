---
language:
- ko
license: mit
library_name: mlx-audio
pipeline_tag: automatic-speech-recognition
base_model: BuzzASR/korean
base_model_relation: quantized
tags:
- mlx
- mlx-audio
- whisper
- korean
- automatic-speech-recognition
- 8-bit
- apple-silicon
---

# BuzzASR Korean — MLX 8-bit

An 8-bit [MLX](https://github.com/ml-explore/mlx) build of [BuzzASR/korean](https://huggingface.co/BuzzASR/korean),
a Korean speech recognition model fine-tuned from Whisper large-v3, for fast local transcription on Apple Silicon Macs
with [mlx-audio](https://github.com/Blaizzy/mlx-audio).

- **Half the size of the original:** 1.64 GB instead of 3.09 GB (FP16), about 2.3 GB of peak GPU memory while transcribing.
- **Strong on Korean–English code-switching:** the best HiKE score among the models we measured, and it writes English
  technical terms in Latin script without a vocabulary prompt.
- **Same weights, nothing retrained:** a straight conversion with `mlx_audio.convert`. All credit for the model goes to the
  BuzzASR authors.

This build was made for [Tractus](https://github.com/sjoon21/Tractus), a local-first note and meeting recorder for macOS,
where it is offered as an optional transcription engine.

## Model details

| | |
| --- | --- |
| Original model | [BuzzASR/korean](https://huggingface.co/BuzzASR/korean) @ `411b68546497bd0efb87599ad7ad4d98fa3dbc62` |
| Architecture | Whisper large-v3 (32 encoder + 32 decoder layers, d_model 1280, 128 mel bins, ≈1.55B parameters) |
| Language | Korean (monolingual fine-tune; the language/task prompt is baked into the generation config) |
| Quantization | MLX affine, 8 bits, group size 64 |
| Weights | `model.safetensors`, 1,644,890,110 bytes, sha256 `51e3f3401548cc97e22b21b12fd3fbbc846f119d38a100d9d8af777a59bf5d78` |
| Converted with | mlx-audio 0.5.7, mlx 0.32.3 (2026-10-22) |
| License | MIT, inherited from the original model |

Reproduce the conversion:

```bash
hf download BuzzASR/korean --revision 411b68546497bd0efb87599ad7ad4d98fa3dbc62 --local-dir buzzasr-korean
python -m mlx_audio.convert --hf-path buzzasr-korean --mlx-path BuzzASR-korean-mlx-8bit --quantize --q-bits 8
```

## Usage

Requires an Apple Silicon Mac and `pip install mlx-audio` (tested with 0.5.7). Input is 16 kHz mono audio.

```python
from mlx_audio.stt.utils import load

model = load("voyagar/BuzzASR-korean-mlx-8bit")
result = model.generate("meeting.wav", language="ko", temperature=0.0, condition_on_previous_text=False)
print(result.text)
```

Command line:

```bash
python -m mlx_audio.stt.generate --model voyagar/BuzzASR-korean-mlx-8bit \
  --audio meeting.wav --language ko --format srt --output-path meeting
```

Recommended settings:

- `temperature=0.0` gives the same output on every run. Without it, Whisper's temperature fallback samples again on
  low-confidence segments, so a few hard segments can come out differently from run to run.
- `condition_on_previous_text=False` keeps an error in one 30-second window from spreading into the next.
- For long recordings, cut the audio at silences into chunks of 30 seconds or less (for example with a VAD) and
  transcribe each chunk on its own. This is how the meeting numbers below were measured.

## Evaluation

Measured on an Apple M3 Mac with 16 GB of memory using the Tractus benchmark
([`bench/`](https://github.com/sjoon21/Tractus/tree/main/bench)): language fixed to Korean, no vocabulary or
initial prompt, and no post-processing. Lower is better for error rates.

| Model (all MLX) | FLEURS-ko CER | HiKE MER | HiKE PIER | AI Hub meetings CER | English term recall (meetings) | Real-time factor (meetings) | Peak GPU memory |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **BuzzASR Korean 8-bit (this model)** | 4.02 | **22.79** | **32.40** | 10.29 | 86.3% | 0.169 | **2.33 GB** |
| Qwen3-ASR 1.7B 8-bit | **2.62** | 28.30 | 35.43 | **9.49** | 71.6% | **0.136** | 3.63 GB |
| Whisper large-v3-turbo | 3.08 | 27.73 | 35.37 | 14.92 | **87.4%** | 0.100 | 2.15 GB |

- **FLEURS-ko:** the Korean test split of [FLEURS](https://huggingface.co/datasets/google/fleurs), 382 read sentences.
- **HiKE:** [HiKE](https://github.com/ThetaOne-AI/HiKE), 1,121 Korean–English code-switching utterances. MER is the
  mixed error rate. PIER (point-of-interest error rate) counts errors only on the code-switched words.
- **AI Hub meetings:** 4 Korean meeting sessions (5.2 hours of multi-speaker discussion) from the AI Hub meeting speech corpus, split
  at silences into chunks of 30 seconds or less. *English term recall* is the share of English terms in the reference
  that also appear in the output. The corpus cannot be redistributed, so only metrics are published.
- **CER normalization:** punctuation and whitespace removed and Latin letters lowercased. Numbers are *not* normalized,
  so writing "30분" where the reference has "삼십 분" counts as an error. These numbers therefore are not directly
  comparable with the normalized CER on the original model card (5.16 on FLEURS).
- **Real-time factor:** processing time divided by audio duration. 0.169 means about 10 minutes for one hour of audio.

How to read the results: Qwen3-ASR is a little more accurate on read speech and plain Korean meetings. BuzzASR is clearly
better when people mix English into Korean, and it gets English terms right without being given a vocabulary list. It
also uses less memory.

## Limitations

- **Korean only.** It is a monolingual fine-tune. Mostly-English speech is not its target.
- **No vocabulary prompts.** Whisper-style `initial_prompt` vocabulary lists made errors much worse on our Korean
  meeting set (Whisper large-v3-turbo: CER 14.92 → 26.89, with output pulled toward English), so Tractus does not send
  one to this model. We have not re-measured this with BuzzASR.
- **Occasional run-on output.** Like other Whisper models, it can keep generating past the end of speech on some short or
  unclear clips. We saw this on 1 of 50 FLEURS sentences checked during conversion. The original card recommends
  `no_repeat_ngram_size=3` and `repetition_penalty=1.2` with transformers. mlx-audio does not expose these, so use
  chunking and a repetition check downstream.
- **Domain:** trained on FLEURS and Common Voice (read speech). Accuracy on noisy, far-field, or dialect speech may be
  lower.
- 8-bit quantization is lossy. We did not benchmark the FP16 original on the same sets, so the size of that loss is
  not measured here.

## License and attribution

MIT, the same as [BuzzASR/korean](https://huggingface.co/BuzzASR/korean), which is fine-tuned from
[openai/whisper-large-v3](https://huggingface.co/openai/whisper-large-v3) (MIT). This repository only changes the
weight format and precision. Please cite the original work:

```bibtex
@misc{buzzasr2026,
  title         = {BuzzASR: A Swarm of 100+ Monolingual Speech Recognition Models},
  author        = {Shivam Singh and Aditya Yadavalli and Catherine Arnett and Alex Warstadt},
  year          = {2026},
  eprint        = {2609.09554},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  note          = {Findings of the Association for Computational Linguistics: EMNLP 2026},
  url           = {https://arxiv.org/abs/2609.09554}
}
```

---

## 한국어 요약

[BuzzASR/korean](https://huggingface.co/BuzzASR/korean)(Whisper large-v3 한국어 파인튜닝, MIT)을
[mlx-audio](https://github.com/Blaizzy/mlx-audio)로 8bit 변환한 판이다. Apple Silicon Mac에서 로컬로 돌리는 것이
목적이며, 다시 학습하지 않았다.

- **크기:** 1.64GB(원본 FP16은 3.09GB), 받아 적는 동안 최대 GPU 메모리 약 2.3GB
- **강점:** 한국어와 영어가 섞인 말(HiKE MER 22.79)에서 우리가 잰 모델 가운데 가장 좋다. 영어 용어를 단어 목록 없이도
  영문으로 적는다(회의 용어 재현율 86.3%).
- **약점:** 낭독과 한국어만 쓰는 회의는 Qwen3-ASR 1.7B보다 조금 나쁘다(회의 CER 10.29 vs 9.49). 짧거나 불분명한 구간에서
  말이 끝난 뒤에도 글을 이어 쓰는 경우가 드물게 있다.
- **권장 설정:** `temperature=0.0`(매번 같은 결과), `condition_on_previous_text=False`, 긴 녹음은 무음에서 30초 이하로
  잘라 넣기
- [Tractus](https://github.com/sjoon21/Tractus)(macOS 로컬 노트·녹음 앱)의 선택 변환 엔진으로 쓰려고 만들었다.
