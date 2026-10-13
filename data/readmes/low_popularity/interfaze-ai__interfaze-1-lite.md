---
license: other
license_name: interfaze-open
license_link: https://huggingface.co/interfaze-ai/interfaze-1-lite/blob/main/LICENSE
library_name: transformers
pipeline_tag: image-text-to-text
language:
- en
- zh
- es
- fr
- de
- it
- pt
- ja
- ko
- ar
- hi
- bn
- id
- sw
- yo
tags:
- vlm
- any-to-text
- audio-text-to-text
- multimodal
- multilingual
- mixture-of-architectures
- ocr
- document-understanding
- speech-recognition
- speaker-diarization
- object-detection
- gui-grounding
- image-segmentation
- translation
- time-series-forecasting
- guardrails
- structured-output
- agent
---

![Interfaze 1.1 Lite](https://huggingface.co/interfaze-ai/interfaze-1-lite/resolve/main/assets/interfaze-1.1-lite-banner.png)

# Interfaze 1.1 Lite

[Website](https://interfaze.ai) · [Docs](https://interfaze.ai/docs/models/interfaze-1-lite) · [Run tasks](https://interfaze.ai/docs/run-tasks) · [Blog](https://interfaze.ai/blog/the-first-open-weight-model-for-deterministic-work-interfaze-1-lite) · [GitHub](https://github.com/InterfazeAI/interfaze-1-lite)

## Introduction

Interfaze 1.1 Lite is a mixture-of-architectures (MoA) model for developer workloads: reading documents, transcribing speech, locating objects and interface elements, and answering over all of it with structured output.

A single vision-language reasoning core works alongside a set of specialist architectures, each built for one kind of perception. The core reads the request, decides which specialists to run, and composes the answer from what they return. The whole model runs on one 80 GB GPU with no external services.

### Key features

- **Document understanding.** Text, reading order, tables and layout from images, PDFs (up to 50 pages a call) and Word files, with a box and confidence for every line and word.
- **Speech.** Transcription with timestamps and speaker diarization. Long recordings are cut at pauses and decoded in batches: a 95-minute recording transcribes in about 90 seconds.
- **Visual grounding.** Open-vocabulary object detection with outlines, and GUI element grounding for computer-use agents.
- **Structured output.** Responses constrained to a JSON schema you supply, reading from any mix of text, images, documents and audio.
- **Translation, forecasting and guardrails.** Translation across 160+ languages, time-series forecasting from CSV or JSON, and safety checks on text and images.
- **Multilingual reasoning.** Science, math, SQL and general knowledge across 14+ languages, with a 131k-token context.
- **Self-contained.** One repository, one GPU, runs offline.

### Model architecture

Interfaze 1.1 Lite is not one network. It is a reasoning core plus specialists, each chosen for the task it is best at, connected by tool calls.

| Component | Architecture | Role |
| --- | --- | --- |
| Reasoning core | Hybrid-attention decoder with a vision encoder, FP8, 131k context | Plans, calls specialists, grounds boxes on a 0–1000 grid, writes the answer |
| Document reader | Vision-language model trained for page reading | Text, reading order, tables and markdown |
| Line geometry | Text detector and recognizer | Every line's box and confidence |
| Layout | Document layout detector | Titles, paragraphs, tables and figures, with boxes |
| Speech | Encoder-decoder speech recognizer | Transcripts and timestamps in 99 languages |
| Diarization | Speaker segmentation and embedding pipeline | Who spoke when |
| Segmentation | Promptable segmentation model | Object outlines and masks |
| Forecasting | Time-series foundation model | Future values of a numeric series |
| Guardrails | Safety classifier | Text safety in 119 languages, reported as S1–S14 codes (S6 and S14 never) |

How the parts combine:

- **OCR is two views of one page, stitched.** The document reader supplies the text, and the line detector supplies the geometry. Each detected line takes the reader's words for it, so boxes are exact and text is complete.
- **Speakers are attributed per word,** by the largest overlap with each speaker's turns, then grouped into chunks.
- **Detection and GUI grounding run on the reasoning core,** which returns boxes on a 0–1000 grid. Outlines come from the segmentation model.
- **A run task skips planning.** Naming one capability (`task="ocr"`, `"speech_to_text"`, …) runs that specialist directly and returns its raw result.

## Performance

| Benchmark | What it measures | **Interfaze 1.1 Lite** | Interfaze | GPT-5.4-Mini | Claude-Sonnet-4.6 | Gemini-3-Flash | Grok-4.3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GPQA Diamond | Graduate-level science | **85.9** | 92.4 | 82.8 | 89.9 | 88.5 | 73.6 |
| MMMLU | Knowledge in 14 languages | **87.8** | 90.9 | 75.3 | 84.9 | 88.7 | 89.7 |
| MMMU-Pro | Multimodal reasoning | **73.2** | 71.1 | 40.4 | 46.3 | 67.6 | 68.7 |
| olmOCR-Bench | Document OCR | **83.8** | 85.7 | 80.1 | 73.9 | 75.3 | 81.9 |
| OCRBench v2 (English) | Text in images | **60.9** | 70.7 | 52.7 | 54.7 | 55.8 | 54.7 |
| RefCOCO (Acc@0.5) | Referring-expression grounding | **83.8** | 82.1 | – | – | – | – |
| VoxPopuli-Cleaned (WER ↓) | Speech recognition | **3.01** | 2.4 | – | – | 4.0 | – |
| SOB (value accuracy) | Structured output from text, images and audio | **81.5** | 80.5 | – | 77.9 | 77.3* | – |
| Spider 2.0-Lite (SQLite) | Text-to-SQL | **48.9** | 52.9 | 26.7 | 49.6 | 45.2 | 45.9 |

These are Interfaze 1 Lite's scores: 1.1 changes the document reader and the guard, and its own scores will replace them once measured. Interfaze 1 Lite was scored by us with each benchmark's official scorer. Every other score is from the [Interfaze leaderboard](https://interfaze.ai/leaderboards). Higher is better except WER. \*Gemini-3-Flash-Preview.

### The benchmarks

- **GPQA Diamond** (all 198 questions). Graduate-level physics, chemistry and biology multiple choice, written to resist search. Lite scores 85.9, ahead of GPT-5.4-Mini and Grok-4.3, and strongest in physics.
- **MMMLU** (MMMLU-lite, all 19,950: 1,425 questions in each of 14 languages). MMLU translated by professional translators. Lite averages 87.8, ahead of Claude-Sonnet-4.6. The low-resource languages (Swahili, Yoruba, Bengali) are where it loses most.
- **MMMU-Pro** (all 1,730 questions per track, mean of standard and vision tracks). College-level questions that need the image, including a track where the question itself is inside the picture. Lite leads the board at 73.2.
- **olmOCR-Bench** (all 1,403 PDFs). Unit tests on real documents: arXiv math, old scans, tables, headers and footers, multi-column pages and long tiny text. Lite scores 83.8, with 91.9 on long tiny text and 88.8 on tables.
- **OCRBench v2, English** (all 7,400 English items). Recognition, referring, spotting, extraction, parsing, calculation, understanding and reasoning over text in images. Lite scores 60.9; its text spotting leads every general-purpose model on the board.
- **RefCOCO** (Acc@0.5). Find the one object a sentence describes ("the man in red on the left"). Lite's answer box scores 83.8, first on the board.
- **VoxPopuli-Cleaned** (all 628 clips). European Parliament speech, scored by word error rate after the benchmark's standard text normalisation. Lite's WER is 3.01%.
- **SOB, the Structured Output Benchmark** (all 5,324 records). Extract values into a JSON schema from text, images and audio; value accuracy counts exact field matches. Lite scores 81.5, second of 30 models, with 97% of responses valid JSON.
- **Spider 2.0-Lite** (the 135 SQLite tasks). Enterprise text-to-SQL over real schemas, scored by executing the query. Lite solves 48.9%, between the Claude models and Gemini-3-Flash.

## Quickstart

To run Lite as an OpenAI-compatible server with Docker, see [GitHub](https://github.com/InterfazeAI/interfaze-1-lite).

### Requirements

- One 80 GB GPU with compute capability 8.9 or newer (Hopper, Ada). Tested on an H100.
- `ffmpeg` on the system, to decode audio.

```bash
hf download interfaze-ai/interfaze-1-lite requirements.txt --local-dir .
pip install -r requirements.txt
```

`flash-linear-attention` matters: without it, transformers runs the linear-attention layers as a plain PyTorch loop, and generation slows to minutes per page.

### Using 🤗 Transformers

```python
from transformers import AutoModel

model = AutoModel.from_pretrained("interfaze-ai/interfaze-1-lite", trust_remote_code=True)

answer = model.chat(
    [{"role": "user", "content": "What is the total, and which item is highlighted?"}],
    files=["receipt.jpg"],
)
print(answer["content"])      # the answer
print(answer["precontext"])   # each specialist's full result: [{"name", "result"}]
```

`trust_remote_code=True` is required: the model's routing and specialists are defined in this repository. Components load on first use, so a caller that only runs OCR never loads the others.

Each capability is also a method of its own:

| Method | Returns |
| --- | --- |
| `chat(messages, files=[...])` | `content` (the answer) and `precontext[]` (each specialist's result) |
| `ocr(source, page_range=None, return_markdown=False)` | `text`, `sections[]` (one per page, with `lines[].words[]`, four-corner `bounds`, `average_confidence`), `width`, `height` |
| `transcribe(audio, by_speaker=False, language="auto", word_timestamps=False)` | `text` and `chunks[]` with timestamps; each chunk carries a speaker with `by_speaker` |
| `detect(image, prompts, return_masks=False)` | `detected_objects[]` with `label`, `bounds` and `polygon` (and `mask` when asked) |
| `ground(image, prompts=None)` | `gui_elements[]` with `type` and `bounds`; with no prompts, every interactive element |
| `forecast(y, horizon)` | the next `horizon` points of a `{date: value}` series `y`: `timestamp[]` and `value[]` |
| `moderate(text)` | `output`: `"safe"`, or `"unsafe"` and the violated categories (S1–S14) |

Coordinates are pixels of the input: an image's own size, or a PDF page at 144 DPI.

### Using the Interfaze API

The same model is served behind an OpenAI-compatible API. Get your API key from the [Interfaze dashboard](https://interfaze.ai/dashboard/quick-start), then set `model` to `interfaze-1-lite`:

```ts
import { Interfaze } from "interfaze";

const interfaze = new Interfaze(); // reads INTERFAZE_API_KEY

const res = await interfaze.chat.completions.create({
  model: "interfaze-1-lite",
  messages: [{ role: "user", content: "Summarise the attached contract in three bullets." }],
});
```

## Examples

### Read a document, with boxes

```python
doc = model.ocr("invoice.pdf", page_range=[1, 2])

print(doc["text"])
for page in doc["sections"]:
    for line in page["lines"]:
        box = line["bounds"]
        print(page["page"], line["text"], box["top_left"], box["bottom_right"])
```

### Transcribe a call and split it by speaker

```python
call = model.transcribe("support_call.mp3", by_speaker=True)

for chunk in call["chunks"]:
    start, end = chunk["timestamp"]
    print(f"[{start:6.1f}–{end:6.1f}] {chunk['speaker']}: {chunk['text']}")
```

### Detect objects and outline them

```python
found = model.detect("street.jpg", ["car", "bicycle", "traffic light"])

for obj in found["detected_objects"]:
    print(obj["label"], obj["bounds"]["top_left"], obj["bounds"]["bottom_right"], len(obj.get("polygon", [])))
```

### Ground interface elements for an agent

```python
screen = model.ground("checkout.png", ["Add to cart button", "search box"])

for element in screen["gui_elements"]:
    b = element["bounds"]
    x = (b["top_left"]["x"] + b["bottom_right"]["x"]) / 2
    y = (b["top_left"]["y"] + b["bottom_right"]["y"]) / 2
    print(element["type"], "click at", (x, y))
```

### Forecast a time series

```python
weekly_sales = {
    "2024-01-01": 412, "2024-01-08": 387, "2024-01-15": 524, "2024-01-22": 461,
    "2024-01-29": 398, "2024-02-05": 542, "2024-02-12": 475, "2024-02-19": 401,
}
nxt = model.forecast(weekly_sales, horizon=4)
print(list(zip(nxt["timestamp"], nxt["value"])))
```

### Check a message before it reaches your app

```python
verdict = model.moderate("How do I make a weapon at home?")
print(verdict["output"])  # "safe", or "unsafe" and the violated codes on the next line
```

### Extract structured data through the API

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.interfaze.ai/v1", api_key="sk_...")

res = client.chat.completions.create(
    model="interfaze-1-lite",
    messages=[{"role": "user", "content": [
        {"type": "text", "text": "Extract the vendor, date and total."},
        {"type": "image_url", "image_url": {"url": "https://example.com/receipt.jpg"}},
    ]}],
    response_format={"type": "json_schema", "json_schema": {"name": "receipt", "schema": {
        "type": "object",
        "properties": {"vendor": {"type": "string"}, "date": {"type": "string"}, "total": {"type": "number"}},
        "required": ["vendor", "date", "total"],
    }}},
)
print(res.choices[0].message.content)
```

## Limitations

- Generation through transformers is correct but slower than a serving engine with paged attention and batching. For throughput, use the Interfaze API or serve the model with a batching engine.
- `chat` does not take a response schema; ask for JSON in the prompt, or use the API's `response_format`.
- A dense document page can take a minute or more to read on the transformers path.
- Memory: processing large PDFs can spike in significant use of CUDA memory.

## Thank You

We are grateful to the teams behind the models and open-source projects whose work we use and build upon.

### Models

1. [Qwen3.8 27B](https://huggingface.co/Qwen/Qwen3.8-27B-FP8)
2. [dots.mocr](https://huggingface.co/dots-studio/dots.mocr)
3. [Whisper large-v3 turbo](https://huggingface.co/openai/whisper-large-v3-turbo)
4. [speaker-diarization-community-1](https://huggingface.co/pyannote/speaker-diarization-community-1)
5. [SAM 2.1](https://huggingface.co/facebook/sam2.1-hiera-large)
6. [Qwen3Guard](https://huggingface.co/Qwen/Qwen3Guard-Gen-0.6B)
7. [TimesFM 2.5](https://huggingface.co/google/timesfm-2.5-200m-pytorch)
8. [PP-OCRv5 Detection](https://huggingface.co/PaddlePaddle/PP-OCRv5_server_det)
9. [PP-DocLayout](https://huggingface.co/PaddlePaddle/PP-DocLayout_plus-L)

### Open-Source Projects

Special thanks to the open-source projects that make these models possible:

1. [vLLM](https://github.com/vllm-project/vllm)
2. [Hugging Face Transformers](https://github.com/huggingface/transformers)
3. [pyannote.audio](https://github.com/pyannote/pyannote-audio)
4. [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
5. [SAM 2](https://github.com/facebookresearch/sam2)
6. [TimesFM](https://github.com/google-research/timesfm)