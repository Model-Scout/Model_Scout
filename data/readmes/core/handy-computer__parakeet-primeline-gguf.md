---
license: cc-by-4.0
base_model: primeline/parakeet-primeline
base_model_relation: quantized
library_name: transcribe.cpp
pipeline_tag: automatic-speech-recognition
language:
  - bg
  - hr
  - cs
  - da
  - nl
  - en
  - et
  - fi
  - fr
  - de
  - el
  - hu
  - it
  - lv
  - lt
  - mt
  - pl
  - pt
  - ro
  - ru
  - sk
  - sl
  - es
  - sv
  - uk
tags:
  - gguf
  - transcribe.cpp
  - asr
  - speech-to-text
  - parakeet
  - conformer
  - rnnt
  - tdt
  - german
  - multilingual
transcribe_cpp:
  schema_version: 2
  wer_fleurs_bg:
    q8_0: 16.33
  wer_fleurs_cs:
    q8_0: 15.05
  wer_fleurs_da:
    q8_0: 20.52
  wer_fleurs_de:
    q8_0: 5.98
    f32: 6.0
    f16: 6.0
    q6_k: 5.96
    q5_k_m: 5.99
    q4_k_m: 5.98
  wer_fleurs_el:
    q8_0: 34.76
  wer_fleurs_en:
    q8_0: 4.82
  wer_fleurs_es:
    q8_0: 3.85
  wer_fleurs_et:
    q8_0: 17.17
  wer_fleurs_fi:
    q8_0: 13.39
  wer_fleurs_fr:
    q8_0: 6.35
  wer_fleurs_hr:
    q8_0: 13.68
  wer_fleurs_hu:
    q8_0: 17.52
  wer_fleurs_it:
    q8_0: 3.17
  wer_fleurs_lt:
    q8_0: 23.08
  wer_fleurs_lv:
    q8_0: 28.83
  wer_fleurs_mt:
    q8_0: 24.74
  wer_fleurs_nl:
    q8_0: 8.49
  wer_fleurs_pl:
    q8_0: 8.19
  wer_fleurs_pt:
    q8_0: 5.17
  wer_fleurs_ro:
    q8_0: 13.8
  wer_fleurs_ru:
    q8_0: 7.81
  wer_fleurs_sk:
    q8_0: 12.36
  wer_fleurs_sl:
    q8_0: 51.07
  wer_fleurs_sv:
    q8_0: 16.42
  wer_fleurs_uk:
    q8_0: 8.11
  wer_librispeech_test_clean:
    q8_0: 2.2
    f32: 2.2
    f16: 2.19
    q6_k: 2.19
    q5_k_m: 2.2
    q4_k_m: 2.26
  rtf_m4_max:
    cpu: 36.73
    metal: 199.38
  rtf_ryzen_4750u:
    cpu: 13.63
    vulkan: 24.97
  streaming: false
  translate: false
  lang_detect: true
  timestamps: token
---

# parakeet-primeline: transcribe.cpp GGUF

GGUF conversions of [primeline/parakeet-primeline](https://huggingface.co/primeline/parakeet-primeline) for use
with [transcribe.cpp](https://github.com/handy-computer/transcribe.cpp).

Ported from upstream commit
[3f1a9bc](https://huggingface.co/primeline/parakeet-primeline/commit/3f1a9bc),
pinned 2026-08-16.
Validated against the NeMo reference at transcribe.cpp commit
[856d7c1](https://github.com/handy-computer/transcribe.cpp/tree/856d7c1)
on 2026-08-16.

primeLine's German fine-tune of NVIDIA's parakeet-tdt-0.6b-v3. A
0.6B-parameter FastConformer encoder with a TDT/RNNT transducer decoder,
taking 16 kHz mono WAV and producing a punctuated, cased transcript with
optional token-level timestamps. Tuned for German, but the fine-tune did
not collapse the base model's multilingual ability: it still transcribes
the other 24 v3 languages with correct per-language casing and
punctuation. Not a streaming model and does not translate.


## Downloads

| Quantization | Download | Size | WER (FLEURS de test) |
| --- | --- | ---: | ---: |
| F32 | [parakeet-primeline-F32.gguf](https://huggingface.co/handy-computer/parakeet-primeline-gguf/resolve/main/parakeet-primeline-F32.gguf) | 2.51 GB | 6.00% |
| F16 | [parakeet-primeline-F16.gguf](https://huggingface.co/handy-computer/parakeet-primeline-gguf/resolve/main/parakeet-primeline-F16.gguf) | 1.26 GB | 6.00% |
| Q8_0 | [parakeet-primeline-Q8_0.gguf](https://huggingface.co/handy-computer/parakeet-primeline-gguf/resolve/main/parakeet-primeline-Q8_0.gguf) | 740 MB | 6.00% |
| Q6_K | [parakeet-primeline-Q6_K.gguf](https://huggingface.co/handy-computer/parakeet-primeline-gguf/resolve/main/parakeet-primeline-Q6_K.gguf) | 610 MB | 5.96% |
| Q5_K_M | [parakeet-primeline-Q5_K_M.gguf](https://huggingface.co/handy-computer/parakeet-primeline-gguf/resolve/main/parakeet-primeline-Q5_K_M.gguf) | 549 MB | 5.99% |
| Q4_K_M | [parakeet-primeline-Q4_K_M.gguf](https://huggingface.co/handy-computer/parakeet-primeline-gguf/resolve/main/parakeet-primeline-Q4_K_M.gguf) | 485 MB | 5.98% |

WER on the full FLEURS de split (862 utterances), batch size 1, timestamps none. Figures without a commit were published before provenance was recorded.

Greedy transducer decoding, no external LM.

primeLine's published figures (2.95% average over Tuda-De, Multilingual
LibriSpeech, and Common Voice 19.0) are on different corpora and are not
comparable to these numbers. As a like-for-like baseline we ran primeLine's
own NeMo checkpoint over the identical manifest: **5.98% WER**. The C++
numbers above match that reference within bootstrap-CI noise, and the quant
spread is 0.04pp end to end with no monotonic degradation.

Orthography note: this checkpoint writes Swiss `ss` forms (`grosse`,
`heisst`) almost everywhere instead of `ß`, which appears just 5 times
across the 862 hypotheses. The upstream SentencePiece vocabulary carries
only 4 pieces containing `ß` against 58 containing `ss`, so this is a
property of the v3-family tokenizer, not of the port — the NeMo reference
produces the same spellings on the same utterances. FLEURS references use
`ß` throughout, which costs roughly 1.05pp: folding `ß`→`ss` on both sides
gives 4.92% for the reference and 4.94% for F32.


## Usage

Build transcribe.cpp from source:

```bash
git clone git@github.com:handy-computer/transcribe.cpp.git
cd transcribe.cpp
cmake -B build && cmake --build build
```

Run on a 16 kHz mono WAV:

```bash
build/bin/transcribe-cli \
  -m parakeet-primeline-Q8_0.gguf \
  input.wav
```

If your audio isn't already 16 kHz mono WAV, convert it first:

```bash
ffmpeg -i input.mp3 -ar 16000 -ac 1 output.wav
```

See the [transcribe.cpp model page](https://github.com/handy-computer/transcribe.cpp/blob/main/docs/models/parakeet-primeline.md) for performance
numbers, numerical validation, and reproduction steps.

## License

Inherited from the base model: **CC-BY-4.0**. See the
[upstream model card](https://huggingface.co/primeline/parakeet-primeline) for full terms.

---

## Original Model Card

> The section below is reproduced from
> [primeline/parakeet-primeline](https://huggingface.co/primeline/parakeet-primeline) at commit
> `3f1a9bc` for offline reference. The upstream card is the
> authoritative source.

# Model Card: primeline-parakeet

## Description
**primeline-parakeet** is a state-of-the-art, 600-million-parameter multilingual Automatic Speech Recognition (ASR) model, specifically optimized for high-precision German transcription. It is based on the [NVIDIA parakeet-tdt-0.6b-v3](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3) architecture, utilizing the efficient FastConformer encoder and Token-and-Duration Transducer (TDT) decoder.

While the base model provides broad European language support, **primeline-parakeet** has been refined to deliver superior accuracy in German contexts, significantly reducing Word Error Rates (WER) across diverse benchmarks compared to both the original NVIDIA release and various Whisper-based architectures.

## Key Features
*   **Optimized for German:** Exceptional performance on German datasets like Tuda-De.
*   **High Efficiency:** Built on the TDT architecture, offering significantly higher throughput than standard Transducer models.
*   **Rich Outputs:** Includes automatic punctuation, capitalization, and precise word-level timestamps.
*   **Robustness:** Maintains high accuracy across different domains, from clean read speech to spontaneous conversations.
*   **Long-Audio Support:** Capable of transcribing audio files up to several hours in length using local attention mechanisms.

## Performance
The following table compares the Word Error Rate (WER %) of **primeline-parakeet** against the base model and other industry standards. **Lower is better.**

| Model | All (Avg) | Tuda-De | Multilingual LibriSpeech | Common Voice 19.0 |
| :--- | :---: | :---: | :---: | :---: |
| **primeline-parakeet** | **2.95** | **4.11** | **2.60** | **3.03** |
| nvidia-parakeet-tdt-0.6b-v3 | 3.64 | 7.05 | 2.95 | 3.70 |
| openai-whisper-large-v3 | 3.28 | 7.86 | 2.85 | 3.46 |
| openai-whisper-large-v3-turbo | 3.64 | 8.20 | 3.19 | 3.85 |

### Analysis
`primeline-parakeet` demonstrates a significant leap in performance for German speech-to-text:
*   **41% improvement** on the Tuda-De benchmark compared to the NVIDIA base model (`4.11` vs `7.05`).
*   Outperforms **OpenAI Whisper-large-v3** across all tested categories while maintaining a much smaller and more efficient parameter count (0.6B).

## Model Architecture
*   **Architecture Type:** FastConformer-TDT (Hybrid Transducer/CTC)
*   **Parameters:** 600 Million
*   **Input:** 16kHz Mono-channel audio (WAV, FLAC)
*   **Output:** Text (including Punctuation and Capitalization)

## Use Cases
This model is designed for developers and researchers requiring high-speed, high-accuracy German transcription for:
*   **Media & Entertainment:** Subtitle generation and automated captioning.
*   **Enterprise:** Meeting minutes, call center analytics, and documentation.
*   **Accessibility:** Real-time speech-to-text services.
*   **Research:** Large-scale linguistic data processing.

***

## Why This Model is a Game Changer: Instant Domain Adaptation

Beyond its compact **600M parameter size** and **blazing-fast TDT inference speed**, the true power of `primeline-parakeet` lies in its architecture's compatibility with external Language Models (LM). 

Unlike many modern ASR models that are "locked" after training, this model supports **Shallow Fusion with KenLM-based N-gram models**. This allows for massive accuracy gains without the need to retrain the neural network itself:

*   **Zero-Retrain Customization:** You can enhance the ASR accuracy by simply training a lightweight, "cheap" LM on pure text data (e.g., legal documents, medical records, or company-specific jargon).
*   **Drastic Error Reduction:** Internal tests show that adding a general-purpose LM can lower the Word Error Rate (WER) by **up to 20%**. 
*   **Niche Specialization:** When targeting specific industries with unique vocabulary, the enhancement is even more significant, allowing the model to recognize specialized terms that standard models would miss.
*   **Low Resource Requirements:** Since the LM only processes text and works alongside the pre-trained ASR model, you can adapt your pipeline to new domains in minutes on standard CPU hardware.

This makes `primeline-parakeet` not just a static model, but a highly adaptable ASR engine that grows with your specific data needs.

***

### Quellen für diese Integration:
1.  [NVIDIA NeMo: GPU Language Modeling and Customization](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/asr_customization/ngpulm_language_modeling_and_customization.html)
2.  [NVIDIA NeMo: Training N-gram LMs for ASR](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/asr_customization/ngram_utils.html#train-ngram-lm)

To train, fine-tune or play with the model you will need to install [NVIDIA NeMo](https://github.com/NVIDIA/NeMo). We recommend you install it after you've installed latest PyTorch version.
```bash
pip install -U nemo_toolkit['asr']
```

The model is available for use in the NeMo toolkit, and can be used as a pre-trained checkpoint for inference or for fine-tuning on another dataset.

#### Automatically instantiate the model

```python

from huggingface_hub import hf_hub_download
from nemo.collections.asr.models import ASRModel
model_path = hf_hub_download(
    repo_id="primeline/parakeet-primeline", filename="2_95_WER.nemo"
)

asr_model = ASRModel.restore_from(model_path, map_location="cpu")
asr_model.eval()

```

#### Transcribing using Python
First, let's get a sample
```bash
wget https://dldata-public.s3.us-east-2.amazonaws.com/2086-149220-0033.wav
```
Then simply do:
```python
output = asr_model.transcribe(['2086-149220-0033.wav'])
print(output[0].text)
```

#### Transcribing with timestamps

To transcribe with timestamps:
```python
output = asr_model.transcribe(['2086-149220-0033.wav'], timestamps=True)
# by default, timestamps are enabled for char, word and segment level
word_timestamps = output[0].timestamp['word'] # word level timestamps for first sample
segment_timestamps = output[0].timestamp['segment'] # segment level timestamps
char_timestamps = output[0].timestamp['char'] # char level timestamps
for stamp in segment_timestamps:
    print(f"{stamp['start']}s - {stamp['end']}s : {stamp['segment']}")
```

#### Transcribing long-form audio

```python

#updating self-attention model of fast-conformer encoder
#setting attention left and right context sizes to 256
asr_model.change_attention_model(self_attention_model="rel_pos_local_attn", att_context_size=[256, 256])
output = asr_model.transcribe(['2086-149220-0033.wav'])
print(output[0].text)

```

#### Openai compatible server


```python
import asyncio
import gc
import io
import json
import logging
import os
import time
from concurrent.futures import ThreadPoolExecutor
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import numpy as np
import soundfile as sf
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import JSONResponse
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown logic"""
    global batch_processor
    logger.info("Starting ASR Proxy Server...")
    try:
        load_model()
    except Exception as e:
        logger.error(f"Failed to initialize model on startup: {e}")
    batch_processor = BatchProcessor(BATCH_SIZE, BATCH_TIMEOUT_MS, MAX_QUEUE_SIZE)
    batch_processor.start()
    logger.info(
        f"Batch processor started (batch_size={BATCH_SIZE}, "
        f"timeout={BATCH_TIMEOUT_MS}ms, max_queue={MAX_QUEUE_SIZE})"
    )
    yield
    logger.info("Shutting down ASR Proxy Server...")
    if batch_processor:
        await batch_processor.stop()


app = FastAPI(title="Openai ASR Server", middleware=middleware, lifespan=lifespan)

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Silence httpx logs
logging.getLogger("httpx").setLevel(logging.WARNING)

# Environment variables
ASR_MODEL_NAME = os.getenv("ASR_MODEL_NAME", "primeline/parakeet-primeline")
ASR_MODEL_PATH = os.getenv("ASR_MODEL_PATH", None)
ASR_QUANTIZATION = os.getenv("ASR_QUANTIZATION", None) or None
ASR_PROVIDER = os.getenv("ASR_PROVIDER", "tensorrt")
TRT_FP16_ENABLE = os.getenv("TRT_FP16_ENABLE", "true").lower() == "true"
TRT_MAX_WORKSPACE_GB = int(os.getenv("TRT_MAX_WORKSPACE_GB", "6"))
USE_VAD = os.getenv("USE_VAD", "true").lower() == "true"

# NeMo export settings (only used when ONNX files not cached)
NEMO_REPO_ID = os.getenv("NEMO_REPO_ID", "primeline/parakeet-primeline")
NEMO_FILENAME = os.getenv("NEMO_FILENAME", "2_95_WER.nemo")
ONNX_CACHE_DIR = Path(os.getenv("ONNX_CACHE_DIR", "/root/.cache/huggingface/onnx_export"))

# Batching configuration
BATCH_SIZE = int(os.getenv("BATCH_SIZE", "8"))
BATCH_TIMEOUT_MS = float(os.getenv("BATCH_TIMEOUT_MS", "100"))
MAX_QUEUE_SIZE = int(os.getenv("MAX_QUEUE_SIZE", "64"))

# Global state
asr_model = None
model_loading = False
batch_processor: Optional["BatchProcessor"] = None


# ---------------------------------------------------------------------------
# Batch processor
# ---------------------------------------------------------------------------


@dataclass
class _BatchItem:
    """A single queued transcription request."""
    waveform: np.ndarray
    sample_rate: int
    future: asyncio.Future
    filename: str
    submit_time: float = field(default_factory=time.time)


class BatchProcessor:
    """Collects concurrent transcription requests and processes them with
    controlled GPU concurrency.  Incoming requests are queued; a background
    task drains up to *max_batch_size* items (or fewer after *batch_timeout_ms*)
    and runs inference sequentially on a single-thread executor so the event
    loop stays responsive while only one GPU call is in-flight at a time."""

    def __init__(self, max_batch_size: int, batch_timeout_ms: float, max_queue_size: int):
        self.max_batch_size = max_batch_size
        self.batch_timeout_ms = batch_timeout_ms
        self._queue: asyncio.Queue[_BatchItem] = asyncio.Queue(maxsize=max_queue_size)
        self._gpu_executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix="gpu")
        self._task: Optional[asyncio.Task] = None
        self._stats = {
            "batches_processed": 0,
            "items_processed": 0,
            "items_failed": 0,
        }

    # -- lifecycle ------------------------------------------------------------

    def start(self):
        self._task = asyncio.create_task(self._process_loop())

    async def stop(self):
        if self._task:
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass
        self._gpu_executor.shutdown(wait=False)

    # -- public API -----------------------------------------------------------

    @property
    def queue_size(self) -> int:
        return self._queue.qsize()

    @property
    def stats(self) -> dict:
        return {**self._stats, "queue_depth": self._queue.qsize()}

    async def submit(self, waveform: np.ndarray, sample_rate: int, filename: str) -> dict:
        """Submit audio for transcription.  Blocks until result is ready.
        Raises asyncio.QueueFull when the service is overloaded."""
        loop = asyncio.get_running_loop()
        future: asyncio.Future = loop.create_future()
        item = _BatchItem(waveform=waveform, sample_rate=sample_rate,
                          future=future, filename=filename)
        try:
            self._queue.put_nowait(item)
        except asyncio.QueueFull:
            raise HTTPException(
                status_code=429,
                detail=f"Transcription queue full ({self._queue.maxsize}). Try again later.",
            )
        return await future

    # -- internal -------------------------------------------------------------

    async def _collect_batch(self) -> list[_BatchItem]:
        """Wait for at least one item, then collect up to max_batch_size
        within the timeout window."""
        batch: list[_BatchItem] = []
        # Block until the first item arrives
        batch.append(await self._queue.get())

        deadline = asyncio.get_event_loop().time() + self.batch_timeout_ms / 1000.0
        while len(batch) < self.max_batch_size:
            remaining = deadline - asyncio.get_event_loop().time()
            if remaining <= 0:
                break
            try:
                item = await asyncio.wait_for(self._queue.get(), timeout=remaining)
                batch.append(item)
            except asyncio.TimeoutError:
                break
        return batch

    def _run_inference(self, waveform: np.ndarray, sample_rate: int):
        """Blocking inference — called inside the thread-pool executor."""
        return asr_model.recognize(waveform, sample_rate=sample_rate)

    async def _process_loop(self):
        """Background loop: collect batches and process items."""
        loop = asyncio.get_running_loop()
        while True:
            try:
                batch = await self._collect_batch()
                logger.info(f"Batch collected: {len(batch)} item(s)")
                self._stats["batches_processed"] += 1

                for item in batch:
                    try:
                        start_time = time.time()
                        result = await loop.run_in_executor(
                            self._gpu_executor,
                            self._run_inference,
                            item.waveform,
                            item.sample_rate,
                        )
                        elapsed = round(time.time() - start_time, 3)
                        queue_wait = round(start_time - item.submit_time, 3)

                        full_text = _extract_text(result)
                        segments = _result_to_segments(result)

                        total_duration = 0.0
                        if segments:
                            total_duration = max(seg["end"] for seg in segments)
                        if total_duration == 0.0:
                            total_duration = round(len(item.waveform) / item.sample_rate, 3)

                        response = {
                            "text": full_text,
                            "segments": segments,
                            "language": "en",
                            "duration": total_duration,
                            "transcription_time": elapsed,
                            "queue_wait_time": queue_wait,
                            "task": "transcribe",
                        }
                        item.future.set_result(response)
                        self._stats["items_processed"] += 1
                        logger.info(
                            f"Batch item '{item.filename}': {elapsed}s inference, "
                            f"{queue_wait}s queue wait, {len(full_text)} chars"
                        )
                    except Exception as e:
                        if not item.future.done():
                            item.future.set_exception(e)
                        self._stats["items_failed"] += 1
                        logger.error(f"Batch item '{item.filename}' failed: {e}")

            except asyncio.CancelledError:
                # Drain remaining items on shutdown
                while not self._queue.empty():
                    try:
                        item = self._queue.get_nowait()
                        if not item.future.done():
                            item.future.set_exception(
                                HTTPException(status_code=503, detail="Server shutting down")
                            )
                    except asyncio.QueueEmpty:
                        break
                raise
            except Exception as e:
                logger.error(f"Batch processing loop error: {e}", exc_info=True)
                await asyncio.sleep(0.1)  # avoid tight error loop


def _build_providers():
    """Build ONNX Runtime provider list based on configuration."""
    if ASR_PROVIDER == "tensorrt":
        try:
            import tensorrt_libs  # noqa: F401
        except ImportError:
            logger.warning("tensorrt_libs not available, will try TensorRT anyway")

        return [
            (
                "TensorrtExecutionProvider",
                {
                    "trt_max_workspace_size": TRT_MAX_WORKSPACE_GB * 1024**3,
                    "trt_fp16_enable": TRT_FP16_ENABLE,
                },
            ),
            "CUDAExecutionProvider",
            "CPUExecutionProvider",
        ]
    elif ASR_PROVIDER == "cuda":
        return ["CUDAExecutionProvider", "CPUExecutionProvider"]
    else:
        return ["CPUExecutionProvider"]


def _ensure_onnx_export():
    """Export .nemo model to ONNX if not already cached. Returns local ONNX path."""
    onnx_dir = ONNX_CACHE_DIR / NEMO_REPO_ID.replace("/", "_")
    marker = onnx_dir / "config.json"

    if marker.exists():
        logger.info(f"ONNX export found at {onnx_dir}, skipping export.")
        return str(onnx_dir)

    logger.info(f"No ONNX export cached. Exporting {NEMO_REPO_ID}/{NEMO_FILENAME}...")
    onnx_dir.mkdir(parents=True, exist_ok=True)

    from huggingface_hub import hf_hub_download
    from nemo.collections.asr.models import ASRModel

    # Download .nemo checkpoint
    nemo_path = hf_hub_download(repo_id=NEMO_REPO_ID, filename=NEMO_FILENAME)
    logger.info(f"Downloaded .nemo to {nemo_path}, loading model for export...")

    # Load on CPU to minimise GPU memory during export
    model = ASRModel.restore_from(nemo_path, map_location="cpu")
    model.eval()

    # Export to ONNX
    onnx_path = str(onnx_dir / "model.onnx")
    logger.info(f"Exporting to ONNX: {onnx_path}")
    model.export(onnx_path)

    # NeMo produces model_encoder.onnx + model_decoder_joint.onnx
    # onnx-asr expects encoder-model.onnx + decoder_joint-model.onnx
    renames = {
        "model_encoder.onnx": "encoder-model.onnx",
        "model_decoder_joint.onnx": "decoder_joint-model.onnx",
        "model_encoder.onnx.data": "encoder-model.onnx.data",
    }
    for src_name, dst_name in renames.items():
        src = onnx_dir / src_name
        if src.exists():
            src.rename(onnx_dir / dst_name)
            logger.info(f"Renamed {src_name} -> {dst_name}")

    # Write vocab.txt
    vocab_path = onnx_dir / "vocab.txt"
    with vocab_path.open("wt") as f:
        for i, token in enumerate([*model.tokenizer.vocab, "<blk>"]):
            f.write(f"{token} {i}\n")
    logger.info(f"Wrote vocab ({i+1} tokens) to {vocab_path}")

    # Write config.json (written last — acts as completion marker)
    config = {
        "model_type": "nemo-conformer-tdt",
        "features_size": 128,
        "subsampling_factor": 8,
        "max_tokens_per_step": 10,
    }
    with marker.open("w") as f:
        json.dump(config, f, indent=2)
    logger.info(f"Wrote config.json to {marker}")

    # Free NeMo/torch memory before loading with onnx-asr
    del model
    gc.collect()
    try:
        import torch
        torch.cuda.empty_cache()
    except Exception:
        pass

    logger.info(f"ONNX export complete at {onnx_dir}")
    return str(onnx_dir)


def load_model():
    """Load the ASR model lazily on first request"""
    global asr_model, model_loading

    if asr_model is not None:
        return

    if model_loading:
        max_wait = 120
        waited = 0
        while model_loading and waited < max_wait:
            time.sleep(0.5)
            waited += 0.5
        return

    model_loading = True
    try:
        import onnx_asr

        # If model path not set, ensure ONNX export exists
        model_path = ASR_MODEL_PATH
        if not model_path:
            model_path = _ensure_onnx_export()

        providers = _build_providers()
        logger.info(
            f"Loading ASR model: {ASR_MODEL_NAME} from {model_path} "
            f"(quantization={ASR_QUANTIZATION}, providers={[p if isinstance(p, str) else p[0] for p in providers]})"
        )

        model = onnx_asr.load_model(
            ASR_MODEL_NAME,
            path=model_path,
            quantization=ASR_QUANTIZATION,
            providers=providers,
        )

        # Use timestamps adapter for segment-level results
        asr_model = model.with_timestamps()

        if USE_VAD:
            vad = onnx_asr.load_vad("silero", providers=["CPUExecutionProvider"])
            asr_model = model.with_vad(vad).with_timestamps()
            logger.info("VAD (Silero) enabled for long audio support.")

        logger.info("ASR model loaded successfully.")

        # Warmup
        warmup_audio_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "flo.wav"
        )
        warmup_iterations = 3
        if os.path.exists(warmup_audio_path):
            logger.info(f"Performing {warmup_iterations} warmup transcriptions...")
            for i in range(warmup_iterations):
                try:
                    warmup_start = time.time()
                    warmup_result = asr_model.recognize(warmup_audio_path)
                    warmup_time = time.time() - warmup_start
                    if i == 0 or i == warmup_iterations - 1:
                        text = _extract_text(warmup_result)
                        logger.info(
                            f"Warmup {i+1}/{warmup_iterations}: {warmup_time:.2f}s - '{text[:80]}'"
                        )
                except Exception as e:
                    logger.warning(f"Warmup {i+1}/{warmup_iterations} failed (non-fatal): {e}")
        else:
            logger.warning(f"Warmup audio not found at {warmup_audio_path}, skipping.")

    except Exception as e:
        logger.critical(f"FATAL: Could not load ASR model. Error: {e}")
        raise
    finally:
        model_loading = False


def _extract_text(result):
    """Extract text from various onnx-asr result types."""
    if isinstance(result, str):
        return result
    if hasattr(result, "text"):
        return result.text
    # VAD iterator result
    parts = []
    try:
        for seg in result:
            if hasattr(seg, "text"):
                parts.append(seg.text)
            elif isinstance(seg, str):
                parts.append(seg)
    except TypeError:
        return str(result)
    return " ".join(parts)


def _result_to_segments(result):
    """Convert onnx-asr result to OpenAI-compatible segments list."""
    segments = []

    # Check if it's an iterator (VAD segments)
    items = []
    try:
        if hasattr(result, "__iter__") and not isinstance(result, str) and not hasattr(result, "text"):
            items = list(result)
        else:
            items = [result]
    except TypeError:
        items = [result]

    for idx, item in enumerate(items):
        if hasattr(item, "start") and hasattr(item, "end"):
            # SegmentResult / TimestampedSegmentResult from VAD
            segments.append({
                "id": idx,
                "start": round(item.start, 3),
                "end": round(item.end, 3),
                "text": item.text.strip() if hasattr(item, "text") else "",
                "seek": 0,
                "tokens": list(item.tokens) if hasattr(item, "tokens") and item.tokens else [],
                "temperature": 0.0,
                "avg_logprob": None,
                "compression_ratio": None,
                "no_speech_prob": None,
            })
        elif hasattr(item, "timestamps") and item.timestamps:
            # TimestampedResult without VAD — build segments from token timestamps
            segments.append({
                "id": idx,
                "start": round(item.timestamps[0], 3) if item.timestamps else 0.0,
                "end": round(item.timestamps[-1], 3) if item.timestamps else 0.0,
                "text": item.text.strip() if hasattr(item, "text") else "",
                "seek": 0,
                "tokens": list(item.tokens) if hasattr(item, "tokens") and item.tokens else [],
                "temperature": 0.0,
                "avg_logprob": None,
                "compression_ratio": None,
                "no_speech_prob": None,
            })
        elif hasattr(item, "text"):
            # Plain text result
            segments.append({
                "id": idx,
                "start": 0.0,
                "end": 0.0,
                "text": item.text.strip(),
                "seek": 0,
                "tokens": [],
                "temperature": 0.0,
                "avg_logprob": None,
                "compression_ratio": None,
                "no_speech_prob": None,
            })

    return segments


@app.get("/health")
async def health_check(deep: bool = False):
    """Health check endpoint."""
    base_status = {
        "model_loaded": asr_model is not None,
        "model_name": ASR_MODEL_NAME,
        "provider": ASR_PROVIDER,
        "quantization": ASR_QUANTIZATION,
        "vad_enabled": USE_VAD,
        "batch": batch_processor.stats if batch_processor else None,
    }

    if not deep:
        base_status["status"] = "healthy" if asr_model else "degraded"
        return base_status

    try:
        if not asr_model:
            load_model()
        if not asr_model:
            base_status["status"] = "unhealthy"
            base_status["error"] = "Model not loaded"
            return JSONResponse(content=base_status, status_code=503)

        warmup_audio_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "flo.wav"
        )
        if not os.path.exists(warmup_audio_path):
            base_status["status"] = "degraded"
            base_status["error"] = "Health check audio file not found"
            return base_status

        start_time = time.time()
        result = asr_model.recognize(warmup_audio_path)
        transcription_time = round(time.time() - start_time, 3)

        text = _extract_text(result)
        if len(text) < 3:
            base_status["status"] = "unhealthy"
            base_status["error"] = "Transcription returned empty or too short result"
            return JSONResponse(content=base_status, status_code=503)

        base_status["status"] = "healthy"
        base_status["transcription_test"] = {
            "success": True,
            "text_length": len(text),
            "transcription_time_seconds": transcription_time,
        }
        return base_status

    except Exception as e:
        logger.error(f"Deep health check failed: {e}")
        base_status["status"] = "unhealthy"
        base_status["error"] = str(e)
        return JSONResponse(content=base_status, status_code=503)


@app.post("/v1/audio/transcriptions")
async def transcribe_rest(file: UploadFile = File(...)):
    """Handles audio transcription via REST API (OpenAI compatible).
    Requests are queued and processed in batches for scalability."""
    if not asr_model:
        load_model()
    if not asr_model:
        raise HTTPException(status_code=503, detail="ASR model not available.")
    if not batch_processor:
        raise HTTPException(status_code=503, detail="Batch processor not ready.")

    logger.info(f"transcribe_rest: Received request for file: {file.filename}")

    try:
        # Read audio bytes and decode with soundfile (handles wav, flac, ogg, etc.)
        audio_bytes = await file.read()
        waveform, sample_rate = sf.read(io.BytesIO(audio_bytes), dtype="float32")

        # Convert stereo to mono if needed
        if waveform.ndim == 2:
            waveform = waveform.mean(axis=1)

        logger.info(
            f"transcribe_rest: Audio loaded, {len(waveform)} samples, {sample_rate}Hz, "
            f"{len(waveform) / sample_rate:.1f}s — submitting to batch queue "
            f"(depth={batch_processor.queue_size})"
        )

        response = await batch_processor.submit(
            waveform, sample_rate, file.filename or "unknown"
        )

        logger.info(
            f"transcribe_rest: Completed for '{file.filename}', "
            f"{response['transcription_time']}s inference, "
            f"{response.get('queue_wait_time', 0)}s queued"
        )

        return JSONResponse(content=response)

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"transcribe_rest: Unhandled exception: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


def main():
    """Main application entry point."""
    import uvicorn

    port = int(os.getenv("PORT", "8000"))
    log_level = os.getenv("LOG_LEVEL", "warning")

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        log_level=log_level,
        workers=None,
        forwarded_allow_ips="*",
        proxy_headers=True,
        timeout_keep_alive=900,
        reload=False,
    )


if __name__ == "__main__":
    main()

```



## Technical Limitations
*   **Accuracy:** While highly accurate, transcripts may still contain errors depending on audio quality, heavy accents, or extreme background noise.
*   **Out-of-Vocabulary (OOV):** Rare technical terms or highly specific jargon not present in the training data may not be recognized correctly.

## Ethical Considerations
Users should be aware of potential biases inherent in the training data. This model is intended for transcription purposes only and should be evaluated for specific use cases to ensure it meets safety and fairness requirements.

## License
Use of this model is governed by the [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode.en) license, consistent with the base model's licensing.



**Disclaimer**

```
This model is not a product of the primeLine Group. 
It represents research conducted by [Florian Zimmermeister](https://huggingface.co/flozi00), with computing power sponsored by primeLine. 
The model is published under this account by primeLine, but it is not a commercial product of primeLine Solutions GmbH.
Please be aware that while we have tested and developed this model to the best of our abilities, errors may still occur. 
Use of this model is at your own risk. We do not accept liability for any incorrect outputs generated by this model.
```


Model author: [Florian Zimmermeister](https://huggingface.co/flozi00)
