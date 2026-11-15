---
license: other
license_name: openmdw-1.1
license_link: https://openmdw.ai/license/1-1/
base_model: nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B
base_model_relation: quantized
pipeline_tag: automatic-speech-recognition
library_name: gguf
language: [en, de, fr, es, it, pt, nl, pl, cs, sk, hi, ja, ko, zh, multilingual]
tags: [gguf, rocmfpx, nemotron-3.5, nemo-speech-cpp, speech-to-text, asr, transcription, strix-halo]
---

# NVIDIA Nemotron 3.5 Transcribe 30B-A4B ROCmFPX

ROCmFPX GGUF files of [nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B), a speech-to-text model (a speech encoder plus a Nemotron 3.5 MoE language decoder, 30B parameters, about 4B active).

These files are for the [ROCmFPX](https://github.com/HarshaVardhan3002/ROCmFPX) fork of llama.cpp, made with our AMD-oriented weight types. If you just want stock llama.cpp types, use [AtomicChat/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF](https://huggingface.co/AtomicChat/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF): on our tests the stock Q8_0 is as good as or slightly better than ours.

## Files

| File | Size | What it is |
|---|---|---|
| `NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-Q8_0_ROCMFPX.gguf` | 34.0 GB | decoder, ROCmFPX 8-bit |
| `NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-Q6_K_ROCMFPX.gguf` | 27.6 GB | decoder, ROCmFPX 6-bit experts, 8-bit rest |
| `NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-Q4_0_ROCMFP4_STRIX.gguf` | 18.7 GB | decoder, ROCmFPX 4-bit experts, 8-bit rest (for Strix Halo) |
| `NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-Encoder-F16.gguf` | 1.67 GB | speech encoder (needed by every decoder file) |

You need one decoder file and the encoder file, in the same folder. The decoder files carry small per-tensor scales (`.scale` tensors) and need ROCmFPX at commit `367cdf8bf` or newer. The multi-token-prediction layer is kept in the files.

## Quality

Word error rate (WER) on the 73 clean English clips of LibriSpeech (`hf-internal-testing/librispeech_asr_dummy`), CPU, greedy, lower is better. KLD and "same top" compare the decoder's next-token predictions with BF16 on text.

| Decoder | WER | KLD vs BF16 | same top token |
|---|---|---|---|
| BF16 (reference) | 2.09 % | 0 | 100 % |
| stock Q8_0 | 1.91 % | 0.0124 | 95.6 % |
| NVIDIA's IQ4_NL experts | 2.17 % | 0.0338 | 92.1 % |
| **Q8_0_ROCMFPX** | 2.43 % | 0.0175 | 94.4 % |
| **Q6_K_ROCMFPX** | 2.35 % | 0.0228 | 93.6 % |
| **Q4_0_ROCMFP4_STRIX** | 2.35 % | 0.0411 | 91.2 % |

On 73 short clips one wrong word moves the WER by about 0.07 %, so all files transcribe about as well as BF16. The JFK sample ("ask not what your country can do for you") comes out word for word with Q8_0_ROCMFPX.

Speed was measured only on the ARM CPU of an NVIDIA DGX Spark, where the ROCmFPX 6-bit type is slow (no ARM kernel for it). AMD GPU numbers from the community are welcome.

## Run

The model runs in NVIDIA's [NeMo-Speech.cpp](https://github.com/NVIDIA/NeMo-Speech.cpp) (tested at `d8a1abf`), built against the ROCmFPX tree instead of its own llama.cpp:

```sh
git clone https://github.com/HarshaVardhan3002/ROCmFPX
git clone https://github.com/NVIDIA/NeMo-Speech.cpp && cd NeMo-Speech.cpp
git apply ../nemo-speech-cpp-rocmfpx.patch   # from this repo, see below
bash scripts/build_sentencepiece_static.sh
cmake -B build -DCMAKE_BUILD_TYPE=Release -DNEMO_SPEECH_LLAMA_CPP_SOURCE_DIR=$PWD/../ROCmFPX \
  -DNEMO_SPEECH_GGML_PATCHED=OFF -DNEMO_SPEECH_BUILD_SPEECHLM=ON -DGGML_VULKAN=ON
cmake --build build -j
build/bin/nemo-speech transcribe meeting.wav -m NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-Q8_0_ROCMFPX.gguf -l en
```

`nemo-speech-cpp-rocmfpx.patch` turns off speculative decoding (a drafter), whose call into llama.cpp's common code differs in ROCmFPX. Plain decoding is not affected. We only tested the CPU build so far.

## How these were made

- Decoder converted to BF16 with NVIDIA's own converter (NeMo-Speech.cpp `conversion/`), then quantized with ROCmFPX using `LLAMA_ROCMFPX_TENSOR_SCALE=1` and an importance matrix.
- Token embeddings stay Q8_0.
- The encoder is NVIDIA's F16 encoder, unchanged.

## License

The model is NVIDIA's, under the [OpenMDW License 1.1](https://openmdw.ai/license/1-1/). `LICENSE`, `THIRD_PARTY_NOTICES.md` and `licenses/` are copied unchanged from the original repository. These files are quantized (modified) versions of the original weights.

Runtime: [ROCmFPX](https://github.com/HarshaVardhan3002/ROCmFPX), built on [llama.cpp](https://github.com/ggml-org/llama.cpp) (MIT).
