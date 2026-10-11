---
base_model: PaddlePaddle/PaddleOCR-VL-1.6
library_name: peft
license: apache-2.0
language:
- ja
- ko
- zh
tags:
- lora
- ocr
- manga
- onomatopoeia
- doujin
- paddleocr-vl
pipeline_tag: image-text-to-text
---

# PaddleOCR-VL-1.6 · manga crop reader (LoRA + fine-tuned vision tower)

A crop-level reader for **manga text** built on
[PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6): a peft
LoRA (r 16, α 32) on the language model **plus a full fine-tune of the vision
tower and projector**, trained on the crop-level `OCR:` task. It reads
**onomatopoeia / SFX** — short, hand-lettered, often vertical or diagonal kana
bursts, with hearts and small kana — and keeps (slightly improves) the base
model's speech-bubble reading. It reads crops; for whole pages pair it with the
`deepghs/AnimeText_yolo` text-block detector (see **Detection** below).

> **v4 is out, in the [`v4/`](./v4) folder.** It reads **Japanese, Korean and
> Chinese**. v3 (the repo root, described below) is Japanese-only and reads
> most Korean as kana. v4 flips the parametrization to a LoRA on the vision
> tower and a full fine-tune of the LM decoder layers, and it improves or
> holds every Japanese number:
>
> | | stock | v3 (root) | **v4** |
> |---|---|---|---|
> | KO hand-lettered, exact / 48 | 21 | 1 | **26** |
> | ZH hand-lettered, exact / 48 | 31 | 16 | **29** |
> | doujin SFX strict / ♡-blind, / 597 | — | 289 / 336 | **316 / 379** |
> | COO test SFX / speech exact | 31.6 / 82.8 % | 83.9 / 88.1 % | **85.0 / 88.5 %** |
>
> Files, loading code and training details are in [`v4/README.md`](./v4/README.md).
> The rest of this card describes v3.

Two files carry the weights:

| file | what | size |
|---|---|---|
| `adapter_model.safetensors` | peft LoRA on the 18 ERNIE layers (q/k/v/o + gate/up/down, 126 modules, 6.0 M params) | 24 MB |
| `tower.safetensors` | the fine-tuned NaViT vision tower + projector, bf16, under the base model's key names (443 tensors, 439 M params) | 878 MB |

Both are needed.

## Results

Greedy decoding, `max_new_tokens=48`

**In-domain — COO test books ∩ Manga109-s**

| model | SFX exact | SFX sim | speech exact | speech sim | spaced / 192 | runaways |
|---|---|---|---|---|---|---|
| PaddleOCR-VL-1.6 stock | 31.6 % | 0.545 | 82.8 % | 0.976 | 30 | 331 |
| + LoRA + tower FT, v2 | 83.6 % | 0.930 | 88.1 % | 0.986 | 19 | 191 |
| **+ LoRA + tower FT, v3 (this revision)** | **83.9 %** | **0.928** | **88.1 %** | **0.987** | **16** | **31** |
| manga-ocr-base stock | 28.9 % | 0.478 | 81.0 % | 0.975 | 0 | 0 |
| manga-ocr-base, same data, full FT | 76.0 % | 0.884 | 80.1 % | 0.975 | 0 | 0 |

The published COO baseline (TRBA + 2D attention, full 10-book test) is 81.2 %;
this checkpoint is at that level on the 6-book subset in one epoch.

**Out-of-domain — hand-labelled lines on colour digital doujin pages** 

| model | exact / 617 | ♡-blind | sim | sim ≥ 0.8 | checked 87 (strict / ♡-blind) |
|---|---|---|---|---|---|
| PaddleOCR-VL-1.6 stock | 19 | 52 | 0.366 | 15.2 % | 4 / 11 |
| + LoRA + tower FT, v2 | 294 | 346 | 0.830 | 71.2 % | 42 / 51 |
| **+ LoRA + tower FT, v3 (this revision)** | **305** | **354** | **0.836** | **72.3 %** | **44 / 54** |
| manga-ocr-base stock | 6 | 15 | 0.312 | 17.2 % | 0 / 1 |
| manga-ocr-base, same data, full FT | 127 | 153 | 0.682 | 60.1 % | 20 / 29 |

12 of the 617 labels were corrected on 2026-09-12; the v2 and v3 rows are
scored on the corrected set (v2 was 297 / 350 on the old one), the stock and
manga-ocr rows on the old one — a difference of a few lines either way.

`♡-blind` ignores hearts; the strict column does not. v3 writes the heart as
`♥` (one token in this tokenizer) where the labels write `♡` — fold one into
the other before comparing, as the strict column here does.

Known behaviour inherited from the base: **autoregressive runaways** on a few
percent of short crops (`ぐくーーーー…`). In production, wrap generation with a
repetition guard or a length cap tied to the crop's aspect; none is baked in
here so the numbers above stay honest.

## Training

| | |
|---|---|
| data | COO onomatopoeia polygons + Manga109-s `<text>` speech boxes, **official COO book split ∩ Manga109-s** (74 / 7 / 6 books); 38,582 SFX + 38,582 speech crops (1 : 1 by count), truncation-link pairs joined as one string on the union box |
| crops | `minAreaRect` deskew (orientation preserved), 12 % pad, min side 16 px |
| targets | NFKC-folded transcription, whitespace runs collapsed to one space (a balloon line break or U+3000 becomes a space) + `</s>`. v3 adds one glyph fold: every dot run (`・・・` / `...` / `……`) → `…`, `〜` → `~`, long dashes → `―`, spacing dakuten → the combining mark, and every heart (`♡` / `❤`) → `♥` — the single-token spelling; teaching `♡` (three bytes) instead cost the model every heart it read. v2 had no glyph fold; v1 deleted all whitespace. |
| prompt | the chat template's `User: <image>OCR:\nAssistant:\n`, batched with left padding |
| LoRA | r 16, α 32, dropout 0.05 on q/k/v/o + gate/up/down of the 18 ERNIE layers; lr 1e-4 |
| tower | NaViT vision tower + projector fully trained, fp32 master copy, lr 1e-5, same schedule |
| optim | AdamW, linear warmup 3 % / linear decay, bs 8 × grad-accum 2, **1 epoch** (4,822 steps), bf16, loss on the target suffix only (`logits_to_keep`), seed 0 |
| aug | pad jitter, ±8° rotation, scale, JPEG, contrast, invert, colour tint |
| hardware | one RTX 5070 Ti (16 GB), ~90 min, 12.1 GB peak |

The training curve was still rising at the end of the single epoch. Three
epochs lift COO but lower the doujin set, so one epoch is kept.

Revisions: **v1** `3b5fe022` (no whitespace in targets, doujin 365 ♡-blind but
glued Latin), **v2** `4caffe65` (spaced targets), **v3** this one (v2 + the glyph
fold; the dot fold also drops in-domain runaways 191 → 31).

## Usage

```python
import torch
from PIL import Image
from huggingface_hub import hf_hub_download
from peft import PeftModel
from safetensors.torch import load_file
from transformers import AutoModelForImageTextToText, AutoProcessor

base, repo = "PaddlePaddle/PaddleOCR-VL-1.6", "sorryhyun/paddleocr-vl-1.6-manga-lora"

model = AutoModelForImageTextToText.from_pretrained(base, dtype=torch.bfloat16, attn_implementation="sdpa")
model = PeftModel.from_pretrained(model, repo).merge_and_unload()          # 1. LoRA on the LM
tower = load_file(hf_hub_download(repo, "tower.safetensors"))
missing = model.load_state_dict(tower, strict=False)                        # 2. fine-tuned vision tower + projector
assert not missing.unexpected_keys, missing.unexpected_keys[:5]
model = model.cuda().eval()
proc = AutoProcessor.from_pretrained(base)

crop = Image.open("sfx_crop.png").convert("RGB")   # a tight crop around one line, ~12 % margin, upright (see "Detection" below)
msgs = [{"role": "user", "content": [{"type": "image"}, {"type": "text", "text": "OCR:"}]}]
text = proc.apply_chat_template(msgs, add_generation_prompt=True, tokenize=False)
inputs = proc(text=[text], images=[crop], return_tensors="pt").to("cuda")
out = model.generate(**inputs, max_new_tokens=48, do_sample=False, use_cache=True)
print(proc.tokenizer.decode(out[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True).strip())
```

Note the base's shipped `generation_config.json` has `use_cache: false`; pass
`use_cache=True` (identical text, ~10× faster). For batches, left-pad and group
crops by area.

## Detection — pairing it with a page detector

This is a **crop reader, not a page reader**: something else has to box the
text first. The detector it is paired with is
**[`deepghs/AnimeText_yolo`](https://huggingface.co/deepghs/AnimeText_yolo)**
(`yolo12l_animetext/model.onnx`, one class, `text_block`), a YOLO12-l trained on
the AnimeText dataset. The
recipe that was measured:

| knob | value | why |
|---|---|---|
| input | top-left letterbox to 640 × 640, grey 114 pad, RGB 0–1, no mean/std | the export's own convention; 1024 / native are a wash on every column |
| score floor | **0.25** (the card's F1 threshold is 0.426) | ~15 % more boxes, nearly all real text; hand SFX 98 % → 100 % boxed |
| NMS | greedy, IoU 0.5 | |
| nesting | **drop a box that contains ≥ 2 others** (≥ 85 % of their area) | a vertical balloon comes back as the block *and* its columns; keeping the columns is right, keeping the block reads the balloon as one line |
| crop | axis-aligned box grown by 12 % of its longer side, upright | what this reader was trained on |

Do **not** run a line recognizer such as PP-OCRv6's on these boxes — they are
blocks, and a line recognizer garbles them (measured once on the same boxes,
on the older 99-line label set: 4 exact for PP-OCRv6's recognizer vs 63 for
this reader). Note the detector's weights are **GPL-3.0** and
its training data **CC-BY-NC-SA-4.0**; they are not included in this repo and
are fetched separately — check both against your own use.

Minimal onnxruntime detection, then the reader above on each crop:

```python
import cv2, numpy as np, onnxruntime as ort
from PIL import Image
from huggingface_hub import hf_hub_download

onnx = hf_hub_download("deepghs/AnimeText_yolo", "yolo12l_animetext/model.onnx")
sess = ort.InferenceSession(onnx, providers=["CUDAExecutionProvider", "CPUExecutionProvider"])

def detect(bgr, imgsz=640, conf=0.25, nms=0.5, nest=0.85):
    h0, w0 = bgr.shape[:2]
    r = min(imgsz / h0, imgsz / w0)
    nw, nh = max(1, round(w0 * r)), max(1, round(h0 * r))
    canvas = np.full((imgsz, imgsz, 3), 114, np.uint8)
    canvas[:nh, :nw] = cv2.resize(bgr, (nw, nh), interpolation=cv2.INTER_AREA)
    x = np.ascontiguousarray(canvas[:, :, ::-1].transpose(2, 0, 1)[None].astype(np.float32) / 255)
    pred = sess.run(None, {sess.get_inputs()[0].name: x})[0][0].T      # (N, 5): cx cy w h score, canvas px
    p = pred[pred[:, 4] >= conf]
    if not len(p):
        return []
    xywh = np.stack([p[:, 0] - p[:, 2] / 2, p[:, 1] - p[:, 3] / 2, p[:, 2], p[:, 3]], 1)
    keep = np.asarray(cv2.dnn.NMSBoxes(xywh.tolist(), p[:, 4].tolist(), conf, nms)).flatten()
    boxes = []
    for i in keep:
        x, y, w, h = xywh[i] / r
        x0, y0, x1, y1 = max(int(x), 0), max(int(y), 0), min(int(x + w), w0), min(int(y + h), h0)
        if x1 > x0 and y1 > y0:
            boxes.append((x0, y0, x1, y1))
    # nesting: drop a block that holds >= 2 smaller boxes (keep the balloon's columns)
    def inside(a, b):  # share of a's area inside b
        ix = max(0, min(a[2], b[2]) - max(a[0], b[0])); iy = max(0, min(a[3], b[3]) - max(a[1], b[1]))
        return ix * iy / max(1, (a[2] - a[0]) * (a[3] - a[1]))
    area = lambda b: (b[2] - b[0]) * (b[3] - b[1])
    return [b for b in boxes
            if sum(area(o) < area(b) and inside(o, b) >= nest for o in boxes if o is not b) < 2]

def crop(bgr, box, pad=0.12):
    x0, y0, x1, y1 = box
    g = round(pad * max(x1 - x0, y1 - y0))
    h, w = bgr.shape[:2]
    return Image.fromarray(bgr[max(y0 - g, 0):min(y1 + g, h), max(x0 - g, 0):min(x1 + g, w), ::-1])

page = cv2.imread("page.png")
crops = [crop(page, b) for b in detect(page)]   # -> the reader's `crop` above, one per box
```

The packaged version of the whole thing is
[`anime_tools`](https://github.com/sorryhyun/anime_tools): `python -m
anime_tools.stages.cli.ocr_captions` runs exactly this detector + reader pair by
default (weights fetched on first use), with the repetition guard, an
area-batched reader and reading order; `anime_tools.ocr.animetext.AnimeTextDetector`
and `anime_tools.ocr.sfx.SfxReader.read_boxes` are the two pieces on their own.

## Data attribution

This model was trained on the **Manga109-s** dataset and the **COO (Comic
Onomatopoeia)** annotations distributed with it. No images or crops are
redistributed here; only weights. v4 also trains on Korean / Chinese SFX crops
from fan-translated pages on gelbooru, pseudo-labelled by the stock
PaddleOCR-VL-1.6. None of those images are redistributed either. Manga109 comics are courtesy of their
respective authors (see the Manga109 site for the list). If you use this model in
academic work, please cite:

```bibtex
@inproceedings{baek2026mangav26,
  title     = {{Manga109-v2026: Revisiting Manga109 Annotations for Modern Manga Understanding}},
  author    = {Baek, Jeonghun and Miyai, Atsuyuki and Onohara, Shota and Ikuta, Hikaru and Aizawa, Kiyoharu},
  booktitle = {ICML Workshop},
  year      = {2026},
}
@article{multimedia_aizawa_2020,
  author={Kiyoharu Aizawa and Azuma Fujimoto and Atsushi Otsubo and Toru Ogawa and Yusuke Matsui and Koki Tsubota and Hikaru Ikuta},
  title={Building a Manga Dataset ``Manga109'' with Annotations for Multimedia Applications},
  journal={IEEE MultiMedia}, volume={27}, number={2}, pages={8--18}, doi={10.1109/mmul.2020.2987895}, year={2020}
}
@article{mtap_matsui_2017,
  author={Yusuke Matsui and Kota Ito and Yuji Aramaki and Azuma Fujimoto and Toru Ogawa and Toshihiko Yamasaki and Kiyoharu Aizawa},
  title={Sketch-based Manga Retrieval using Manga109 Dataset},
  journal={Multimedia Tools and Applications}, volume={76}, number={20}, pages={21811--21838}, doi={10.1007/s11042-016-4020-z}, year={2017}
}
@inproceedings{baek2022coo,
  title     = {COO: Comic Onomatopoeia Dataset for Recognizing Arbitrary or Truncated Texts},
  author    = {Baek, Jeonghun and Matsui, Yusuke and Aizawa, Kiyoharu},
  booktitle = {ECCV},
  year      = {2022},
}
```

## License

Weights: Apache-2.0 (same as the base model). Use of the training data is
governed by the Manga109-s terms (no redistribution of images; results and
pretrained models may be published with attribution).
