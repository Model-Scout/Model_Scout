---
license: apache-2.0
base_model: Qwen/Qwen3-ASR-0.6B
base_model_relation: quantized
pipeline_tag: automatic-speech-recognition
library_name: mlx
language:
- zh
- en
- yue
- ar
- de
- fr
- es
- pt
- id
- it
- ko
- ru
- th
- vi
- ja
- tr
- hi
- ms
- nl
- sv
- da
- fi
- pl
- cs
- fil
- fa
- el
- hu
- mk
- ro
tags:
- mlx
- mlx-audio
- qwen3_asr
- asr
- speech
- speech-recognition
- quantized
- mixed-precision
- apple-silicon
model-index:
- name: Qwen3-ASR-0.6B-MLX-mixed-6-8bit
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: LibriSpeech test-clean
      type: openslr/librispeech_asr
      config: clean
      split: test
      revision: '71cacbf'
    metrics:
    - type: wer
      value: 2.12
      name: Test WER
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: LibriSpeech test-other
      type: openslr/librispeech_asr
      config: other
      split: test
      revision: '71cacbf'
    metrics:
    - type: wer
      value: 4.61
      name: Test WER
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: FLEURS en_us
      type: google/fleurs
      config: en_us
      split: test
      revision: '70bb2e8'
    metrics:
    - type: wer
      value: 4.34
      name: Test WER
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: FLEURS cmn_hans_cn
      type: google/fleurs
      config: cmn_hans_cn
      split: test
      revision: '70bb2e8'
    metrics:
    - type: cer
      value: 2.99
      name: Test CER
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: AISHELL-1
      type: shenyunhang/AISHELL-1
      split: test
      revision: '2724409'
    metrics:
    - type: cer
      value: 2.23
      name: Test CER
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: Common Voice 19.0 zh-TW
      type: JacobLinCool/common_voice_19_0_zh-TW
      split: test
      revision: '0a1a9ed'
    metrics:
    - type: cer
      value: 5.80
      name: Test CER
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: FormosaSpeech (133 clean clips <= 40 s)
      type: MediaTek-Research/formosaspeech
      split: test
      revision: 'debc9e2'
    metrics:
    - type: cer
      value: 8.00
      name: Test CER
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: ASCEND (16 clips < 0.3 s removed)
      type: CAiRE/ASCEND
      split: test
      revision: '737e980'
    metrics:
    - type: mer
      value: 11.36
      name: Test MER
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: NTU ML2021 lectures
      type: ky552/ML2021_ASR_ST
      split: test
      revision: '1e121cc'
    metrics:
    - type: mer
      value: 10.41
      name: Test MER
---

# Qwen3-ASR-0.6B-MLX-mixed-6-8bit (706 MB)

- A mixed 6/8-bit MLX quantization of [Qwen/Qwen3-ASR-0.6B](https://huggingface.co/Qwen/Qwen3-ASR-0.6B) for Apple silicon
- It is the same size as the common 4-bit builds (706 MB vs 708 MB), with error rates no more than 0.10 points worse than bf16 on all 9 test sets (on mlx-audio 0.4.2 and 0.6.4)
- Had a Claude Opus 5.5 agent make this build for [Lamitype](https://lamitype.com), my macOS dictation app, and tested it in the app's transcription engine
- Sharing it back with the community in case it helps. Please do your own verification (or ask your agent to do so)
- Other Qwen3-ASR languages should work but are untested; we only tested English and Mandarin

This is an independent quantization. Not affiliated with or endorsed by the Qwen team.

## Results

Error rate in %, lower is better. English: WER; Chinese: CER; code-switch: mixed error rate. mlx-audio 0.6.4, mlx 0.32.4, full test splits (exceptions and hardware in REPRODUCE.md). All builds are our own runs (same harness, same clips); none are copied from other sources.

| test set | metric | bf16 (original) | **this model** | 4-bit (mlx-community) |
|---|---|---:|---:|---:|
| size (MB) | | 1565 | 706 | 708 |
| LibriSpeech clean | WER | 2.12 | 2.12 | 2.41 |
| LibriSpeech other | WER | 4.52 | 4.61 | 5.14 |
| FLEURS en | WER | 4.33 | 4.34 | 4.92 |
| FLEURS zh | CER | 2.92 | 2.99 | 3.68 |
| AISHELL-1 | CER | 2.22 | 2.23 | 2.83 |
| CV19 zh-TW | CER | 5.85 | 5.80 | 11.22 |
| FormosaSpeech (133 clips) | CER | 8.06 | 8.00 | 8.96 |
| ASCEND | MER | 11.48 | 11.36 | 25.84 |
| NTU ML2021 | MER | 10.41 | 10.41 | 11.38 |

Table footnotes, confidence intervals and evaluation details are in [REPRODUCE.md](REPRODUCE.md); scores and run metadata are in [results/](results/). REPRODUCE.md also compares the common 8-, 6- and 5-bit builds (run on mlx-audio 0.4.2; between the two versions, this model and bf16 moved by at most 0.17 points on any set). The recipe was tuned on a development sample partly drawn from these test splits; removing the overlapping clips gives the same conclusions ([REPRODUCE.md](REPRODUCE.md#how-the-recipe-was-chosen)).

The 4-bit numbers above include two mlx-audio failure modes:
- **No text.** With automatic language detection (the default), the 4-bit build labels 4.2% of CV19 clips as English and returns no text. Re-running those 209 clips with `language="Chinese"` gives text for all of them, and the 4-bit build then scores 7.16% on CV19, still 1.36 points worse than this model.
- **Runaway repetition.** Some 4-bit outputs repeat text, most on ASCEND (for example 1,330 characters for an 11-character reference), so its ASCEND score is unstable (95% CI 13.8-44.9). With the two worst clips removed, it is still 4.90 points worse than this model.

In speech-swift (the runtime Lamitype uses), with the same ASR prompt for both builds, the 4-bit build is 1.08 points worse than this model on CV19 zh-TW and 0.56 points worse on ASCEND. Both differences are significant.

## Usage

Neither of the following runtimes runs this model out of the box: both assume the audio encoder is never quantized, and this model quantizes it to 8-bit. We made two small changes, described in [REPRODUCE.md](REPRODUCE.md#runtime-changes):

- **mlx-audio:** a load-time override (the snippet below) that applies the per-module settings from `config.json`. No fork; transcription code is unchanged.
- **speech-swift:** our fork ([felixfu824/speech-swift](https://github.com/felixfu824/speech-swift)) adds per-module quantization support, including the encoder, and makes the forced ASR prompt the default.

**Python (mlx-audio).** Tested with `pip install mlx-audio==0.6.4` (mlx 0.32.4). Stock mlx-audio (tested 0.4.2 and 0.6.4) ignores this checkpoint's per-module settings for the audio encoder. The model then loads without error but fails on the first transcription with a `[matmul]` shape error. The fix is to apply the per-module config from `config.json` before loading; the snippet below does this, and it is the loader used for this card's Python results:

```python
import json
from pathlib import Path
from huggingface_hub import snapshot_download
import mlx_audio.stt.models.qwen3_asr.qwen3_asr as q
from mlx_audio.stt.utils import load_model

path = snapshot_download("felixfu824/Qwen3-ASR-0.6B-MLX-mixed-6-8bit")
cfg = json.loads((Path(path) / "config.json").read_text())["quantization"]
orig = q.Qwen3ASRModel.model_quant_predicate
q.Qwen3ASRModel.model_quant_predicate = lambda self, p, m: cfg[p] if p in cfg else orig(self, p, m)
model = load_model(path)
print(model.generate("audio.wav").text)
```

**Swift (speech-swift).** Use release [`mixed-precision-v1`](https://github.com/felixfu824/speech-swift/releases/tag/mixed-precision-v1) of our fork [felixfu824/speech-swift](https://github.com/felixfu824/speech-swift) (commit `9ff1963`; the fork's `main` adds later fixes, such as safer handling of interrupted downloads). It reads the per-module `quantization` block from `config.json`, loads the quantized audio encoder, and uses the forced ASR prompt by default. With the model's automatic-language prompt, a few short code-switch clips came out in the wrong script (6 of 1,299 on ASCEND, against 0 with the forced prompt).

## Limitations

- Layer choice was tuned for Mandarin and code-switch speech. Two sets are slightly but significantly worse than bf16: LibriSpeech test-other (+0.09 points) and FLEURS zh (+0.07).
- Traditional characters appear in 82% of this model's CV19 zh-TW outputs and none of AISHELL-1 outputs. Scoring converts both reference and output to Simplified.
- NTU ML2021 test audio is a single lecturer.

## How this was made

- The quantization, the evaluation and the conclusions were produced by Claude Code agents (Claude Opus 5.5). No human re-ran or hand-checked the evaluation.
- Separate agents reviewed the work:
  - Two independent Claude Opus 5.5 reviews re-derived the mlx-audio 0.4.2 numbers from the raw score files.
  - A third Claude Opus 5.5 review checked the mlx-audio 0.6.4 table and text.
  - A second Claude Code session reproduced the Swift results through Lamitype's engine.
  - All reviewers were Claude models, so the reviews are not fully independent of the agents that did the work.
- Details are in [REPRODUCE.md](REPRODUCE.md#verification).

## Licence and citation

Apache-2.0, inherited from Qwen3-ASR-0.6B (see `LICENSE`). The weights are modified (quantized) from the original.

```bibtex
@article{Qwen3-ASR,
  title={Qwen3-ASR Technical Report},
  author={Xian Shi and Xiong Wang and Zhifang Guo and Yongqi Wang and Pei Zhang and Xinyu Zhang and Zishan Guo and Hongkun Hao and Yu Xi and Baosong Yang and Jin Xu and Jingren Zhou and Junyang Lin},
  journal={arXiv preprint arXiv:2601.21337},
  year={2026}
}
```
