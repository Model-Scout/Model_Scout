---
license: other
license_name: openmdw-1.1
license_link: LICENSE
language: [en, es, de, fr, it, ar, ja, ko, pt, ru, hi, zh, vi, he, nl, cs, da, pl, 'no', sv, th, tr, bg, el, et, fi, hr, hu, lt, lv, ro, sk, uk, mt, sl]
pipeline_tag: automatic-speech-recognition
base_model: nvidia/nemotron-3.5-asr-streaming-0.6b
base_model_relation: quantized
library_name: litert
tags: [litert, tflite, android, npu, gpu, speech-recognition, streaming, rnnt, nemotron]
---

# nemotron-3.5-asr-streaming-0.6b for LiteRT

This repository is a conversion of [nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b) (streaming speech recognition in 40 language-locales) to LiteRT, made with litert-torch 0.10.0 and ai-edge-quantizer 0.10.0 for LiteRT 2.3.0: it transcribes audio in 320 ms chunks as they arrive, and on a Galaxy S26 a chunk takes a median 25.4 ms with its float16 subsampling and conformer graph on the NPU, 73.3 ms on the GPU and 40.2 ms with float16 arithmetic on the CPU; on a Pixel 11 Pro's CPU, 70.3 ms. These are short runs of 10 to 25 utterances (measured 2026-11-02 and 2026-11-03); over all 655 utterances of the subset below, the medians are, in the same order, 27.0, 63.4, 64.7 and 111.4 ms, the Pixel's at 5 threads (Sustained, under Performance). On a 655-utterance LibriSpeech test-clean subset, scored as the Open ASR Leaderboard scores it, the word error rate on the Galaxy S26's NPU is 2.630 %, against 2.638 % for our float32 PyTorch run of the original.

The original is a cache-aware streaming FastConformer encoder with an RNN-T decoder and a language prompt. This conversion keeps its streaming design at lookahead 3 (320 ms chunks): the chunking and the caches follow transformers' `Nemotron3_5AsrForRNNT` streaming generation, and every cache is a graph input and output, so the host carries the state from one chunk to the next. The graphs are plain PyTorch modules that read the checkpoint's weights (no NeMo), exported with litert-torch. The speeds on this card are for this repository's `.tflite` files run with LiteRT 2.3.0's C API (the Android runner below), not for LiteRT-LM or for any other conversion of this model.

## Files

| file | bytes | what | backend |
|---|---|---|---|
| `nemotron_asr_mel.tflite` | 964,732 | log-mel front end: `mel_first` (the first 4,040 samples → 25 frames) and `mel` (5,520 samples → 32 frames) | CPU |
| `nemotron_asr_pre.tflite` | 18,402,700 | the 8× subsampling with its three convolution caches: `pre_first` and `pre` (25 or 32 mel frames → 4 frames of 1,024) | CPU |
| `nemotron_asr_conformer_f16_cpu.tflite` | 1,217,291,232 | the 24-layer conformer for one chunk (`conformer`), its attention and convolution caches as inputs and outputs; float16 weights, its LayerNorm inputs rescaled so that float16 arithmetic does not overflow, and its relative-position matmuls written as fully connected layers so that XNNPACK runs its arithmetic in float16 (4,090 of the graph's 4,093 nodes; the three concatenations at its end stay on LiteRT's own CPU kernel) | CPU |
| `nemotron_asr_conformer_pre_f16.tflite` | 1,191,615,072 | `pre` and the conformer in one graph (`conformer_pre`), with the same float16 weights and LayerNorm rescale | NPU |
| `nemotron_asr_conformer_f16.tflite` | 1,182,197,680 | the conformer with the same float16 weights and LayerNorm rescale | GPU |
| `nemotron_asr_conformer_f32.tflite` | 2,350,467,936 | the conformer in float32 | CPU (the Python example) |
| `nemotron_asr_decoder_i8.tflite` | 24,267,072 | RNN-T prediction network (`predict`) and joint network (`joint`) with int8 weights, one scale per output channel, int8 activations computed at run time | CPU |
| `nemotron_asr_decoder_f32.tflite` | 94,969,956 | the same in float32 | CPU (beside the GPU conformer, and in the Python example) |
| `tokenizer.json` | 752,051 | the original's tokenizer, unchanged | host |
| `processor_config.json` | 2,519 | the original's processor settings, unchanged; `prompt_dictionary` gives each language-locale's prompt id | host |
| `nemotron_stream_runner.cc`, `build_android.sh` | 83,707 and 3,294 | a command-line runner for Android (LiteRT C API) and its build script; the runner reads the model files from its arguments | |
| `rnnt_text.py` | 796 | turns the runner's token ids into text | host |
| `LICENSE` | 2,619 | the OpenMDW License Agreement, version 1.1 | |

Take `mel`, `pre`, `conformer_f16_cpu` and `decoder_i8` for a phone's CPU (1.26 GB), `mel`, `conformer_pre_f16` and `decoder_i8` for the NPU (1.22 GB), `mel`, `pre`, `conformer_f16` and `decoder_f32` for the GPU (1.30 GB), or `mel`, `pre`, `conformer_f32` and `decoder_f32` for the Python example on a desktop (2.46 GB).

## How it works

audio (16 kHz mono) → 320 ms chunks → mel → pre → conformer (caches in, caches out) → greedy RNN-T → text

- **Chunks.** Append 5,520 zero samples to the audio. Chunk 0 is samples [0, 4,040) through `mel_first` and `pre_first`; chunk k ≥ 1 is the 5,520 samples from 3,744 + 5,120 (k − 1) through `mel` and `pre`, for every k whose chunk ends before the end of the padded audio. Each chunk adds 5,120 new samples (320 ms) and gives 4 encoder frames. The loop in the original card's transformers snippet stops before the audio's last partial chunk, so the end of the audio is not transcribed there; the appended zeros carry it through here.
- **Caches.** `conformer` takes `x` [1, 4, 1024] (the chunk's `embeds` from `pre`), `neg_mask` [1, 1, 4, 60], `k_cache` and `v_cache` [24, 8, 56, 128] (each layer's last 56 frames of keys and values, right-aligned), `conv_cache` [24, 1024, 8] (each layer's convolution context) and `one_hot` [1, 128]; it returns `enc_proj` [1, 4, 640] and `k_out`, `v_out`, `conv_out`, which are the next chunk's caches. At the start of an utterance the caches are zeros, and `neg_mask` is −30,000 on the first 56 − min(56, 4k) of its 60 key slots in chunk k and 0 elsewhere (the slots not filled yet). `pre` carries `cache0`, `cache1` and `cache2` the same way, from `pre_first`'s outputs on.
- **One graph on the NPU.** `conformer_pre` runs `pre` and `conformer` in one call: it takes the chunk's 32 mel frames (`mel`) and `pre`'s three caches in place of `x`, plus two row masks, `pre_m0` [1, 1, 16, 1] and `pre_m1` [1, 1, 8, 1], and returns `conformer`'s outputs with `pre`'s next caches. The masks are 1 except in chunk 0, which goes in as 7 zero rows followed by `mel_first`'s 25 rows, with zeros on the first 3 rows of `pre_m0` and on the first row of `pre_m1`; that gives `pre_first`'s result. The runner's `--conf-mode fused` does this.
- **Language.** `one_hot` is 1 at the prompt id of the audio's language-locale in `processor_config.json`'s `prompt_dictionary` (`en-US` 0, `fr-FR` 8, `de-DE` 9, `ja-JP` 10, `ru-RU` 11, …) and 0 elsewhere. The dictionary also has `auto` (101), which leaves the language to the model; we measured only the five locales above.
- **Decoding** (on the host). Start from `predict(token = 13087 (blank), h = c = 0)`. For each encoder frame, `joint(dec_out, frame)` gives 13,088 logits; take the arg-max: blank moves to the next frame, any other token is emitted and fed to `predict`, which gives the next `dec_out`, `h` and `c`; after 10 tokens on one frame, move to the next frame. The decoder state runs on across chunks.
- **Text.** `Tokenizer.decode(ids, skip_special_tokens=True)` with `tokenizer.json`.
- **Lookahead.** The original supports lookahead 0, 3, 6 and 13 (80 ms to 1.12 s chunks); these files are for lookahead 3 only.

## Use it

### 1. Download

<!-- usage:download -->
```bash
pip install -U huggingface_hub
hf download litert-community/nemotron-3.5-asr-streaming-0.6b --local-dir nemotron-asr
cd nemotron-asr
```

### 2. Your audio

Both runners below read 16 kHz mono 16-bit WAV files listed in `audio/index.tsv` with their language-locale. The block below writes them from any format ffmpeg reads; replace the two lines before `EOF` with your files (no spaces in the names) and their locales (the keys of `prompt_dictionary` in `processor_config.json`).

<!-- usage:audio -->
```bash
mkdir -p audio && : > audio/index.tsv && i=0
while read -r f locale; do
  id=$(printf %03d $i)
  ffmpeg -nostdin -loglevel error -y -i "$f" -ac 1 -ar 16000 -c:a pcm_s16le "audio/$id.wav"
  printf '%s\t%s\t%s.wav\t%s\n' "$id" "$(basename "$f")" "$id" "$locale" >> audio/index.tsv
  i=$((i + 1))
done <<'EOF'
sample1.wav en-US
sample2.wav ja-JP
EOF
```

The accuracy tables below score the FLEURS files as published (32-bit float), and this block writes 16-bit PCM, which can change a transcript. On FLEURS's Japanese test file 10401481013809636276.wav (the `sample2.wav` above), every phone backend gives 確率予測 from the 16-bit file, where the Pixel 11 Pro's CPU and the Galaxy S26's NPU give 確率で予測 from the 32-bit file; the desktop runner below gives 確立で予測, the text of our float32 PyTorch reference (Accuracy, below), from the 16-bit file.

### 3a. On a desktop (Python, CPU)

Save this as `transcribe.py` in the `nemotron-asr` folder. It streams each file chunk by chunk through the float32 files, as a live input would arrive, and prints the time each chunk took:

<!-- usage:python -->
```python
import json
import sys
import time
import wave

import numpy as np
from ai_edge_litert.interpreter import Interpreter
from tokenizers import Tokenizer


def signatures(path, threads):
    it = Interpreter(model_path=path, num_threads=threads)
    return {name: it.get_signature_runner(name) for name in it.get_signature_list()}


mel = signatures("nemotron_asr_mel.tflite", 1)
pre = signatures("nemotron_asr_pre.tflite", 1)
conformer = signatures("nemotron_asr_conformer_f32.tflite", 4)["conformer"]
decoder = signatures("nemotron_asr_decoder_f32.tflite", 1)
predict, joint = decoder["predict"], decoder["joint"]
tokenizer = Tokenizer.from_file("tokenizer.json")
PROMPT = json.load(open("processor_config.json"))["prompt_dictionary"]
BLANK, FIRST, NEXT = 13087, 4040, 5520  # blank id; samples of the first chunk and of every later chunk


def read_wav(path):  # 16 kHz mono 16-bit PCM
    with wave.open(path) as w:
        assert (w.getframerate(), w.getnchannels(), w.getsampwidth()) == (16000, 1, 2), path
        return np.frombuffer(w.readframes(w.getnframes()), "<i2").astype(np.float32) / 32768


def transcribe(audio, locale):
    x = np.concatenate([audio, np.zeros(NEXT, np.float32)])  # the zeros carry the last real samples through
    one_hot = np.zeros((1, 128), np.float32)
    one_hot[0, PROMPT[locale]] = 1
    k_cache = np.zeros((24, 8, 56, 128), np.float32)
    v_cache = np.zeros((24, 8, 56, 128), np.float32)
    conv_cache = np.zeros((24, 1024, 8), np.float32)
    state = predict(token=np.array([[BLANK]], np.int32), h=np.zeros((2, 1, 640), np.float32), c=np.zeros((2, 1, 640), np.float32))
    ids, chunk_ms, chunk, start = [], [], 0, 0
    while chunk == 0 or start + NEXT < len(x):
        t0 = time.perf_counter()
        if chunk == 0:
            p = pre["pre_first"](mel=mel["mel_first"](pcm=x[None, :FIRST])["mel"])
        else:
            m = mel["mel"](pcm=x[None, start:start + NEXT])["mel"]
            p = pre["pre"](mel=m, cache0=p["cache0_out"], cache1=p["cache1_out"], cache2=p["cache2_out"])
        mask = np.zeros((1, 1, 4, 60), np.float32)
        mask[..., :56 - min(56, 4 * chunk)] = -30000.0  # the cache slots not filled yet
        out = conformer(x=p["embeds"], neg_mask=mask, k_cache=k_cache, v_cache=v_cache, conv_cache=conv_cache, one_hot=one_hot)
        k_cache, v_cache, conv_cache = out["k_out"], out["v_out"], out["conv_out"]
        for frame in range(4):  # greedy RNN-T, at most 10 tokens per encoder frame
            for _ in range(10):
                token = int(np.argmax(joint(dec_out=state["dec_out"], enc_frame=out["enc_proj"][:, frame])["logits"]))
                if token == BLANK:
                    break
                ids.append(token)
                state = predict(token=np.array([[token]], np.int32), h=state["h_out"], c=state["c_out"])
        chunk_ms.append((time.perf_counter() - t0) * 1000)
        chunk += 1
        start = 3744 + 5120 * (chunk - 1)
    return tokenizer.decode(ids, skip_special_tokens=True), chunk_ms


for line in open(sys.argv[1] + "/index.tsv", encoding="utf-8"):
    _, name, wav, locale = line.rstrip("\n").split("\t")[:4]
    text, ms = transcribe(read_wav(sys.argv[1] + "/" + wav), locale)
    print(f"{name}\t{locale}\t{len(ms)} chunks, median {np.median(ms):.1f} ms per chunk\t{text}")
```

<!-- usage:python-run -->
```bash
pip install ai-edge-litert==2.3.0 tokenizers numpy
python transcribe.py audio
```

### 3b. On an Android phone (native runner)

Build the runner with the Android NDK r29 (we built it on macOS; the path below is Android Studio's default there). The script downloads the LiteRT 2.3.0 C headers (`litert_cc_sdk.zip` from LiteRT's GitHub release) and the runtime libraries (Google's Maven), and checks their sha256.

<!-- usage:build -->
```bash
NDK=$HOME/Library/Android/sdk/ndk/29.0.13113456 bash build_android.sh
```

Copy the runner, the CPU files and your audio to the phone, run it, and turn its output into text:

<!-- usage:push -->
```bash
adb shell mkdir -p /data/local/tmp/nemotron-asr
adb push nemotron_stream_runner libs/libLiteRt.so nemotron_asr_mel.tflite nemotron_asr_pre.tflite nemotron_asr_conformer_f16_cpu.tflite nemotron_asr_decoder_i8.tflite audio /data/local/tmp/nemotron-asr/
adb shell chmod 755 /data/local/tmp/nemotron-asr/nemotron_stream_runner
```

On the Pixel 11 Pro (the settings of its row in Performance):

<!-- usage:run-cpu-p11p -->
```bash
adb shell 'cd /data/local/tmp/nemotron-asr && LD_LIBRARY_PATH=. ./nemotron_stream_runner --accel cpu --libdir . \
  --model nemotron_asr_conformer_f16_cpu.tflite --conf-xnn-flags 7 --mel-first nemotron_asr_mel.tflite --mel nemotron_asr_mel.tflite \
  --pre-first nemotron_asr_pre.tflite --pre nemotron_asr_pre.tflite \
  --predict nemotron_asr_decoder_i8.tflite --joint nemotron_asr_decoder_i8.tflite --threads 4 --state swap \
  --fixtures audio --count $(grep -c . audio/index.tsv) --rounds 0 --dump none --out out' > out.jsonl
```

On the Galaxy S26 (the settings of its CPU row in Performance):

<!-- usage:run-cpu -->
```bash
adb shell 'cd /data/local/tmp/nemotron-asr && LD_LIBRARY_PATH=. ./nemotron_stream_runner --accel cpu --libdir . \
  --model nemotron_asr_conformer_f16_cpu.tflite --conf-xnn-flags 7 --mel-first nemotron_asr_mel.tflite --mel nemotron_asr_mel.tflite \
  --pre-first nemotron_asr_pre.tflite --pre nemotron_asr_pre.tflite \
  --predict nemotron_asr_decoder_i8.tflite --joint nemotron_asr_decoder_i8.tflite --threads 4 --state copy \
  --fixtures audio --count $(grep -c . audio/index.tsv) --rounds 0 --dump none --out out' > out.jsonl
```

<!-- usage:text -->
```bash
pip install tokenizers
python rnnt_text.py tokenizer.json out.jsonl
```

The runner streams the files one after another, each from fresh caches, after streaming the first file once as a warm-up. Each line of `out.jsonl` that starts with `{"kind":"utt"` holds one file's token ids (`tok`), each token's encoder frame (`frame`) and, per chunk, the time from handing its samples to `mel` to the end of its decoding (`chunk_ms`), with the times of the stages (`mel_ms`, `pre_ms`, `conf_ms`, `dec_ms`). The `stream_summary` line gives the median and 90th percentile of `chunk_ms` over the files and `rtf_stream`, the summed chunk time over the audio time. `--conf-xnn-flags 7` asks XNNPACK for float16 arithmetic in the conformer (7 = XNNPACK's default flags 3 with FORCE_FP16, 4); without it, XNNPACK runs the same file in float32 arithmetic. `--threads` sets the CPU threads of every graph, and `--state swap` alternates two sets of cache buffers instead of copying each cache output into its input after the chunk (`--state copy`, the runner's default). The CPU and NPU runs print `GPU accelerator could not be loaded and registered` on stderr: the GPU library is not on the phone until the GPU block below copies it, and nothing else changes.

**NPU (Galaxy S26, Qualcomm Hexagon).** The runner compiles `conformer_pre_f16` for the Hexagon NPU on the phone the first time (LiteRT's Qualcomm compiler plugin, on-device JIT) and keeps the result in `--cache-dir`; `mel` and the decoder run on the CPU. `--conf-mode fused` tells the runner that this graph holds `pre`: it feeds the chunk's mel frames to it and opens no `pre` graph. It needs LiteRT's Qualcomm plugin libraries (`libLiteRtDispatch_Qualcomm.so` and `libLiteRtCompilerPlugin_Qualcomm.so`, from the `litert-npu-runtime-qualcomm` package that `build_android.sh` fetches) and the QNN libraries of the Qualcomm AI Runtime SDK (QAIRT) 2.50.0.260828, which you download from Qualcomm; copy these eight files flat into a folder `qnn/`: from `lib/aarch64-android/`, `libQnnHtp.so`, `libQnnHtpPrepare.so`, `libQnnHtpV81Stub.so`, `libQnnHtpV81CalculatorStub.so`, `libQnnSystem.so`, `libQnnIr.so` and `libQnnSaver.so`; from `lib/hexagon-v81/unsigned/`, `libQnnHtpV81Skel.so`. The block uses the runner, `mel`, `decoder_i8` and the audio that the push block above copied. Run it before the GPU block, with other apps closed (the first compile takes the runner up to 5.9 GB, see Notes); run the same block again and the graph loads from the cache.

<!-- usage:npu -->
```bash
adb push libs/libLiteRtDispatch_Qualcomm.so libs/libLiteRtCompilerPlugin_Qualcomm.so qnn/. nemotron_asr_conformer_pre_f16.tflite /data/local/tmp/nemotron-asr/
adb shell 'cd /data/local/tmp/nemotron-asr && LD_LIBRARY_PATH=. ADSP_LIBRARY_PATH="/data/local/tmp/nemotron-asr;/vendor/dsp/cdsp;/vendor/lib/rfsa/adsp;/system/lib/rfsa/adsp;/dsp" \
  ./nemotron_stream_runner --accel npu+cpu --libdir . --cache-dir cache --conf-mode fused \
  --model nemotron_asr_conformer_pre_f16.tflite --mel-first nemotron_asr_mel.tflite --mel nemotron_asr_mel.tflite \
  --predict nemotron_asr_decoder_i8.tflite --joint nemotron_asr_decoder_i8.tflite \
  --fixtures audio --count $(grep -c . audio/index.tsv) --rounds 0 --dump none --out out' > out_npu.jsonl
```

**GPU.** Push `libs/libLiteRtClGlAccelerator.so`, the `f16` conformer and `decoder_f32`, and run with `--accel gpu --gpu-precision fp16`:

<!-- usage:push-gpu -->
```bash
adb push libs/libLiteRtClGlAccelerator.so nemotron_asr_conformer_f16.tflite nemotron_asr_decoder_f32.tflite /data/local/tmp/nemotron-asr/
adb shell 'cd /data/local/tmp/nemotron-asr && LD_LIBRARY_PATH=. ./nemotron_stream_runner --accel gpu --gpu-precision fp16 --libdir . \
  --model nemotron_asr_conformer_f16.tflite --mel-first nemotron_asr_mel.tflite --mel nemotron_asr_mel.tflite \
  --pre-first nemotron_asr_pre.tflite --pre nemotron_asr_pre.tflite \
  --predict nemotron_asr_decoder_f32.tflite --joint nemotron_asr_decoder_f32.tflite \
  --fixtures audio --count $(grep -c . audio/index.tsv) --rounds 0 --dump none --out out' > out_gpu.jsonl
```

To remove everything from the phone: `adb shell rm -rf /data/local/tmp/nemotron-asr`.

## Accuracy

Word error rate (%) and, for Japanese, character error rate (%), against our PyTorch reference: transformers 5.22.1 `Nemotron3_5AsrForRNNT` in float32, the same chunks with the same 5,520 zeros appended, greedy decoding, each set's language-locale as the prompt. LibriSpeech test-clean and FLEURS German / French / Russian are scored as the Open ASR Leaderboard scores them, against its `text` column (its English or multilingual normalizer, compound merging, kaldialign: the first number of each pair) and as plain corpus WER with jiwer on the same normalized text, without the compound merging (the second number); FLEURS Japanese is scored as corpus CER against FLEURS' `raw_transcription`, after the leaderboard's multilingual normalizer with every whitespace removed (kaldialign and jiwer give the same number).

Every utterance of each test split, on a Mac (Apple M4 Max) with ai-edge-litert 2.3.0. The float32 files give the reference's text on all 5,583 utterances. `f16_cpu` ran on the Mac's CPU with XNNPACK's float16 arithmetic (flags 7), as on the phones' CPUs; `conformer_pre_f16` and the `f16` conformer ran on the Mac's GPU with float16 arithmetic (Metal), the first in place of the phone's NPU, whose numbers are in the second table, the second as on the phone's GPU.

| set | utterances | PyTorch reference and the float32 files | `f16_cpu` + `decoder_i8` (CPU files) | `conformer_pre_f16` + `decoder_i8` (NPU files) | `f16` conformer + `decoder_f32` (GPU files) |
|---|---|---|---|---|---|
| LibriSpeech test-clean | 2,620 | 2.862 / 3.317 | 2.840 / 3.283 | 2.851 / 3.291 | 2.849 / 3.311 |
| FLEURS German | 862 | 8.207 / 10.442 | 8.200 / 10.319 | 8.184 / 10.330 | 8.207 / 10.426 |
| FLEURS French | 676 | 9.833 / 10.126 | 9.855 / 10.131 | 9.850 / 10.137 | 9.816 / 10.109 |
| FLEURS Russian | 775 | 9.836 / 10.781 | 9.790 / 10.710 | 9.842 / 10.736 | 9.836 / 10.775 |
| FLEURS Japanese (CER) | 650 | 12.294 | 12.355 | 12.374 | 12.263 |

On the phones, with the backends of the Performance table (the Pixel 11 Pro's settings are given below the table): S4 = every fourth utterance of LibriSpeech test-clean (655), J200 = 200 FLEURS Japanese utterances picked at random (seed 20261101).

| phone, backend | S4 WER | J200 CER |
|---|---|---|
| PyTorch reference | 2.638 / 3.133 | 11.614 |
| Galaxy S26, NPU (`conformer_pre_f16` + `decoder_i8`) | 2.630 / 3.141 | 11.915 |
| Galaxy S26, GPU (`f16` conformer, float16 arithmetic, + `decoder_f32`) | 2.645 / 3.141 | not run |
| Galaxy S26, CPU (`f16_cpu` + `decoder_i8`, 4 threads) | 2.630 / 3.126 | not run |
| Pixel 11 Pro, CPU (`f16_cpu` + `decoder_i8`) | 2.630 / 3.141 | 11.574 |

The Pixel 11 Pro's J200 ran with the Performance row's 4 threads and `--state swap`, its S4 with 5 threads and `--state copy`; at 4 threads and `--state swap` the runner gave the same token ids and the same frame for every token on all 82 utterances of the 82-utterance LibriSpeech test-clean subset that Performance times (all of them inside S4).

## Performance

Each row times the first 5 utterances of an 82-utterance LibriSpeech test-clean subset, streamed 2 to 5 times over in one process after a warm-up utterance (Workload, below the table).

| phone | backend | chunk ms, median | chunk ms, 90th percentile | RTF | conformer per chunk (ms) | decoding per chunk (ms) | peak memory |
|---|---|---|---|---|---|---|---|
| Galaxy S26 | NPU (Hexagon): `conformer_pre_f16`; `decoder_i8` and mel on the CPU, 4 threads | 25.442 | 28.095 | 0.0811 | 23.114 | 1.860 | 2.50 GB (2,446,136 kB) |
| Galaxy S26 | GPU (Adreno, float16 arithmetic): `f16` conformer; `decoder_f32`, mel and pre on the CPU, 4 threads | 73.309 | 87.709 | 0.2272 | 58.817 | 11.085 | 6.09 GB (5,948,436 kB) |
| Galaxy S26 | CPU: `f16_cpu` (float16 arithmetic) + `decoder_i8`, 4 threads | 40.203 | 48.037 | 0.1283 | 37.878 | 0.895 | 2.65 GB (2,586,300 kB) |
| Pixel 11 Pro | CPU: `f16_cpu` (float16 arithmetic) + `decoder_i8`, 4 threads, `--state swap` | 70.334 | 140.818 | 0.2778 | 63.165 | 3.190 | 2.64 GB (2,579,128 kB) |

- **chunk ms** = the time from handing a chunk's samples to `mel` until its 4 encoder frames are decoded, as the runner in "Use it" measures it (`chunk_ms`); a chunk holds 320 ms of new audio, so a chunk under 320 ms keeps up with live input. **RTF** = the summed chunk time over the audio time (`rtf_stream`). The conformer and decoding columns are the medians of the runner's `conf_ms` (the input writes, the run, the output reads and the cache move; on the NPU it includes `pre`, which runs inside that graph) and `dec_ms` per chunk.
- **Workload**: the first 5 utterances of an 82-utterance LibriSpeech test-clean subset, in one process after one warm-up utterance: 5 passes over them on the NPU (25 utterances), 4 on the GPU (20) and 2 on the CPUs (10). Each row is the mean of two such runs, made in the order A B B A against another setting of the same backend (on the NPU, against `pre` and the conformer as two graphs, which took 27.546 ms; on the Galaxy S26's GPU, against `--state swap`, 72.547 ms (next bullet); on the Galaxy S26's CPU, against 6 threads, 50.258 ms; on the Pixel 11 Pro's CPU, against 5 threads with `--state copy`, 74.087 ms); the peak memory is the larger of the two runs' VmHWM (GB = kB × 1024 / 10⁹).
- **Sustained.** Over all 655 utterances of S4 (4,876 s of audio; one process on the Galaxy S26's NPU, GPU and CPU, 2 processes on the Pixel 11 Pro's CPU), the median chunk took 26.970 ms on the Galaxy S26's NPU (RTF 0.0878), 63.389 ms on its GPU (RTF 0.2050), 64.677 ms on its CPU (RTF 0.2011, 4 threads) and 111.439 ms on the Pixel 11 Pro's CPU (RTF 0.4149, 5 threads).
- **Galaxy S26 GPU** ran the conformer with `--state copy` (the runner copies each cache output into its input buffer); `--state swap` (two buffer sets alternated per chunk) took 72.547 ms. On the Pixel 11 Pro the GPU (the `f16` conformer at float16 precision with `decoder_f32`, the 5 utterances streamed once after the warm-up) was slower than its CPU: 143.747 ms with `--state swap`, 204.835 ms with `--state copy`.
- Galaxy S26 (SM-S942Q, Android 16) and Pixel 11 Pro (Android 17); LiteRT 2.3.0 from Google's Maven; on the NPU the QNN libraries of QAIRT 2.50.0.260828 for Hexagon v81; 2026-11-02 and 2026-11-03.

## Notes

- **First NPU run.** On a Galaxy S26 the on-device compile of `conformer_pre_f16` took 11.8–16.4 s in four runs and 33.8 s in a fifth that started right after a 7-minute run (thermal status 3); the compiled graph takes 1.20 GB (1,175,471 kB) in the cache folder, and a later run loads it from the cache in 0.39–0.92 s (6 runs). While it compiles, the runner's peak memory is 5.0–5.9 GB (VmHWM 4,919,612–5,730,976 kB) and the phone's available memory went down to 2.26 GB (2,205,156 kB) in one of the runs. Start the first NPU run with other apps closed. The runner puts one graph on the NPU.
- **GPU and float16.** In the checkpoint's encoder the variance of a LayerNorm input row reaches 137,326 over the 3,661 chunks of our range check (98 utterances), beyond float16's largest value 65,504. The `f16` conformer scales each of its 144 LayerNorm inputs by 2^-k (k = 2–9 per norm) and its epsilon by 4^-k, which leaves the float32 result the same function and keeps every scaled input within 32 of its row mean on those chunks; its float16 weights are the float32 weights rounded to the nearest float16. `f16_cpu`, `conformer_pre_f16` and the `f16` conformer carry this rescale; the float32 file runs without it.
- **CPU and float16.** In LiteRT 2.3.0, XNNPACK's float16 mode refuses a matrix multiplication whose second input is a constant, and each conformer layer applies its relative-position embedding that way (24 such matmuls), so the original layout cannot run in float16 arithmetic on the CPU. `f16_cpu` folds each layer's query projection into that term and computes it as one fully connected layer on the attention input (952 × 1,024 weights per layer, 3.5 % more fully connected weights in all); the GPU and NPU files keep the original layout.
- **int8 decoder and float16 on the CPU.** `decoder_i8` computes int8 activations at run time on the CPU (XNNPACK). To see whether multi-threaded int8 or float16 arithmetic changes a result from one process to the next, we scored FLEURS Japanese in three fresh processes on the Mac: CER 12.374 each time with `conformer_pre_f16` on the Mac's GPU, 12.355 each time with `f16_cpu` on its CPU.
- **Pixel 11 Pro chunk times** spread wider than the Galaxy S26's (90th percentile 140.818 ms against a median of 70.334 ms in the table's runs).
- **Clocks in the Galaxy S26 rows.** In the GPU row's two runs (124 s and 123 s), the GPU's clock cap (kgsl) began to fall 22 s and 24 s after the start and reached 578 MHz, from 1,300 MHz, at 48 s and 70 s. In the CPU row's two runs (34 s and 37 s), the CPU clock caps began to fall 2–5 s after the start and reached their lowest at 16 s and 11 s, the prime cores' from 4.74 to 1.75 GHz and the other cores' from 3.63 to 1.79 GHz.
- Converted from the weights of [nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b) at revision `ea30d66`, rewritten as plain PyTorch graphs (the 24 conformer layers in one graph, the caches as inputs and outputs, the LSTM step as explicit gates; in `f16_cpu` the relative-position term as fully connected layers, in `conformer_pre_f16` `pre` and the conformer in one graph) and exported with litert-torch 0.10.0; checked against transformers 5.22.1's `Nemotron3_5AsrForRNNT` streaming generation. The steps and scripts are in [hf-to-litertlm](https://github.com/john-rocky/hf-to-litertlm) (REPRODUCE.md, nemotron-3.5-asr-streaming-0.6b).

## License

The model files are a conversion of [nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b) and are distributed under the OpenMDW License Agreement, version 1.1 ([`LICENSE`](LICENSE); [openmdw.ai/license/1-1](https://openmdw.ai/license/1-1/)), as the original is. The original's card: "Governing Terms: Use of the model is governed by the [OpenMDW-1.1](https://openmdw.ai/license/1-1/) license." `tokenizer.json` and `processor_config.json` are the original's files. The runner and the scripts (`nemotron_stream_runner.cc`, `build_android.sh`, `rnnt_text.py`) are under the Apache License 2.0.
