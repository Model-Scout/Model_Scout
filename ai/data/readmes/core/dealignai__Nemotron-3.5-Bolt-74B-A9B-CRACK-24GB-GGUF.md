---
license: other
license_name: nvidia-open-model-license
license_link: https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/
base_model: nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-BF16
tags:
  - nemotron
  - nemotron-h
  - mamba
  - moe
  - vl
  - vision
  - abliteration
  - uncensored
  - crack
  - gguf
  - imatrix
language:
  - en
  - fr
  - es
  - de
  - it
  - ja
  - ko
  - pt
  - hi
  - zh
pipeline_tag: text-generation
thumbnail: dealign_mascot.png
---

> **Important:** CRACK = refusal-removed GGUF of NVIDIA's **Nemotron-3.5-Bolt-74B-A9B**, quantized to match NVIDIA's **-24GB-GGUF** layout (IQ2_XXS experts / NVFP4 Mamba / Q8_0 attention + latent + lm_head). Ships with NVIDIA's own mmproj and LiLiCorr drafter so it is drop-in with llama.cpp. Follow **[@dealignai](https://x.com/dealignai)** for new releases.

---

<div align="center">

<img src="dealign_mascot.png" width="128" />

# Nemotron-3.5-Bolt-74B-A9B · CRACK-24GB-GGUF

**NemotronH hybrid Mamba2 + attention + MoE** · **74B total / 9B active** · **VL (image + video)** · **22 GB on disk**

<a href="https://x.com/dealignai"><img src="https://img.shields.io/badge/Follow-@dealignai-1DA1F2?logo=x&logoColor=white&style=for-the-badge" alt="@dealignai"></a>

</div>

---

## What is this

This is **NVIDIA's own Nemotron-3.5-Bolt-74B-A9B** with its refusal training removed and quantized to NVIDIA's own 24GB mixed-precision layout. The multimodal vision tower is kept **byte-identical** to the BF16 source; it is shipped with NVIDIA's own **mmproj** file and the matching **LiLiCorr** speculative drafter.

> Research artifact for alignment work. This model answers requests the base refuses, including harmful ones. **Do not deploy to end users without separate downstream safety controls.**

| | |
|---|---|
| **Base model** | [nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-BF16) |
| **Architecture** | NemotronH-Puzzle: 88 blocks (40 Mamba2 + 40 latent-MoE + 8 full-attention), hidden 4096, 512 experts (puzzle-pruned) + 1 shared, latent MoE 1024-d, C-RADIO-v4-H vision tower |
| **Thinking** | binary `enable_thinking` switch, no effort levels |
| **Quantization** | NVIDIA 24GB mixed: IQ2_XXS routed + shared experts, NVFP4 Mamba in/out proj, Q8_0 attention q/k/v/o + latent fc1/fc2 + lm_head + token_embd, F32 norms |
| **Imatrix** | 1.5M-token calibration mix (coding, terminal, agentic, reasoning, 10-language multilingual, harm prompts), computed on the post-ablation model |
| **Size** | 22 GB (2.38 BPW) |
| **Languages** | English, French, Spanish, German, Italian, Japanese, Korean, Portuguese, Hindi, Chinese |
| **MTP** | None (Nemotron 3.5 Bolt has no MTP head). Speculative decoding via the included LiLiCorr drafter. |

---

## Files

| File | Size | Role |
|---|---|---|
| `Nemotron-3.5-Bolt-74B-A9B-CRACK-24GB.gguf` | 22 GB | Main model |
| `mmproj-NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB.gguf` | 1.73 GB | Vision tower (NVIDIA's own file; vision weights are byte-identical to BF16 source) |
| `NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB-LiLiCorr.gguf` | 1.00 GB | Speculative drafter (NVIDIA's own file, redistributed under NVIDIA Open Model License) |

---

## Running

llama.cpp upstream `b76b13379` or newer. Older forks cannot load Nemotron-H puzzle checkpoints.

**Core text + vision:**

```bash
llama-server \
  -m Nemotron-3.5-Bolt-74B-A9B-CRACK-24GB.gguf \
  --mmproj mmproj-NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB.gguf \
  -ngl 999 -c 65536 -np 8 --jinja --flash-attn on \
  --host 127.0.0.1 --port 8091
```

**With speculative decoding via LiLiCorr drafter:**

```bash
llama-server \
  -m Nemotron-3.5-Bolt-74B-A9B-CRACK-24GB.gguf \
  --mmproj mmproj-NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB.gguf \
  --spec-type draft-dflash --spec-draft-n-max 6 \
  --spec-draft-model NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB-LiLiCorr.gguf \
  -ngl 999 -c 65536 -np 8 --jinja --flash-attn on
```

Thinking is a binary `enable_thinking` chat-template kwarg (no effort levels):

```python
# OpenAI-compatible client
client.chat.completions.create(
    model="x",
    messages=[{"role": "user", "content": "…"}],
    extra_body={"chat_template_kwargs": {"enable_thinking": True}},
)
```

Default sampling: `temperature=0` greedy for the cleanest coherence. Up to `temperature=0.7` is clean; above that, IQ2_XXS artifacts (rare word-pair repetitions, occasional character slips) start to appear.

---

## Evaluation

### Compliance — HarmBench-320, reasoning-ON

**ASR 99.4% (318/320), 0 refusals.** The 2 non-compliant are decode-loop "garbage" responses under IQ2_XXS, not refusals.

| Category | comply / N | % |
|---|---|---|
| chemical_biological | 42 / 42 | **100.0%** |
| cybercrime_intrusion | 52 / 52 | **100.0%** |
| harassment_bullying | 21 / 21 | **100.0%** |
| harmful | 18 / 18 | **100.0%** |
| misinformation_disinformation | 54 / 54 | **100.0%** |
| copyright | 79 / 80 | 98.8% |
| illegal | 52 / 53 | 98.1% |

The 2 non-compliant are both "garbage" decode patterns (not refusals) — one in `copyright` ("Viva La Vida" lyrics with runaway "Ooh!" repetition under IQ2_XXS experts), one in `illegal`. **Zero genuine refusals.**

**Note on copyright:** that category rewards verbatim reproduction of copyrighted lyrics and prose, which is genuinely hard to replay cleanly under IQ2_XXS experts — small decode artifacts in long repetitive strings get flagged as "garbage" even when the model is clearly trying to recite the right text. Treat copyright under 100% as a decode-fidelity artifact of the quant, not an abliteration gap; the compliance signal is: zero refusals and every other category at 100%.

Base NVIDIA-24GB-GGUF refuses roughly half of these behaviors in both thinking modes (observed 47.9% refuse off, 52.4% refuse on on 2000 and 800 harm-prompt behavioral rows respectively).

### Capability

MMLU letter-logit, thinking-off, full 14042-question MMLU-test (apples-to-apples at the same IQ2_XXS/NVFP4/Q8_0 quant layout):

| | base NV-24GB | CRACK-24GB | delta |
|---|---|---|---|
| MMLU micro | **80.76%** | **78.59%** | **−2.17pp** |
| MMLU macro | 81.29% | 79.68% | **−1.61pp** |

Per topic group:

| topic | CRACK | base | delta |
|---|---|---|---|
| STEM | 76.47% | 77.67% | **−1.19pp** |
| Humanities | 72.62% | 76.39% | **−3.76pp** |
| Social | 88.11% | 88.63% | **−0.52pp** |
| Other | 80.20% | 82.54% | **−2.34pp** |

STEM and social sciences hold within a point of base. Humanities takes the largest hit (−3.76pp) — expected, since copyright/moral-reasoning categories overlap with the behaviours surgery deliberately re-weights.

<details>
<summary><b>Per-subject MMLU 14042 (all 57 subjects) — click to expand</b></summary>

| subject | n | base | CRACK | delta |
|---|---:|---:|---:|---:|
| abstract algebra | 100 | 61.0% | 60.0% | −1.0pp |
| anatomy | 135 | 70.4% | 68.9% | −1.5pp |
| astronomy | 152 | 90.1% | 92.1% | **+2.0pp** |
| business ethics | 100 | 83.0% | 82.0% | −1.0pp |
| clinical knowledge | 265 | 83.0% | 82.3% | −0.8pp |
| college biology | 144 | 91.0% | 93.1% | **+2.1pp** |
| college chemistry | 100 | 59.0% | 61.0% | **+2.0pp** |
| college computer science | 100 | 77.0% | 73.0% | **−4.0pp** |
| college mathematics | 100 | 66.0% | 60.0% | **−6.0pp** |
| college medicine | 173 | 83.2% | 77.5% | **−5.8pp** |
| college physics | 102 | 63.7% | 63.7% | +0.0pp |
| computer security | 100 | 88.0% | 86.0% | −2.0pp |
| conceptual physics | 235 | 90.2% | 87.7% | −2.6pp |
| econometrics | 114 | 74.6% | 76.3% | +1.8pp |
| electrical engineering | 145 | 80.7% | 70.3% | **−10.3pp** |
| elementary mathematics | 378 | 77.2% | 76.5% | −0.8pp |
| formal logic | 126 | 76.2% | 71.4% | **−4.8pp** |
| global facts | 100 | 45.0% | 48.0% | **+3.0pp** |
| high school biology | 310 | 93.9% | 94.2% | +0.3pp |
| high school chemistry | 203 | 77.3% | 75.4% | −2.0pp |
| high school computer science | 100 | 88.0% | 87.0% | −1.0pp |
| high school european history | 165 | 86.1% | 83.6% | −2.4pp |
| high school geography | 198 | 90.4% | 91.4% | +1.0pp |
| high school government and politics | 193 | 96.4% | 96.9% | +0.5pp |
| high school macroeconomics | 390 | 86.7% | 85.4% | −1.3pp |
| high school mathematics | 270 | 51.5% | 54.8% | **+3.3pp** |
| high school microeconomics | 238 | 93.3% | 95.4% | **+2.1pp** |
| high school physics | 151 | 75.5% | 70.9% | **−4.6pp** |
| high school psychology | 545 | 94.1% | 92.5% | −1.7pp |
| high school statistics | 216 | 78.2% | 78.2% | +0.0pp |
| high school us history | 204 | 92.6% | 91.7% | −1.0pp |
| high school world history | 237 | 91.1% | 89.0% | −2.1pp |
| human aging | 223 | 79.4% | 78.0% | −1.3pp |
| human sexuality | 131 | 92.4% | 86.3% | **−6.1pp** |
| international law | 121 | 86.8% | 84.3% | −2.5pp |
| jurisprudence | 108 | 88.0% | 89.8% | +1.9pp |
| logical fallacies | 163 | 89.6% | 87.1% | −2.5pp |
| machine learning | 112 | 72.3% | 67.9% | **−4.5pp** |
| management | 103 | 85.4% | 87.4% | +1.9pp |
| marketing | 234 | 93.6% | 92.3% | −1.3pp |
| medical genetics | 100 | 93.0% | 93.0% | +0.0pp |
| miscellaneous | 783 | 89.5% | 88.1% | −1.4pp |
| moral disputes | 346 | 83.8% | 80.9% | −2.9pp |
| moral scenarios | 895 | 68.6% | 56.0% | **−12.6pp** |
| nutrition | 306 | 92.2% | 85.3% | **−6.9pp** |
| philosophy | 311 | 82.3% | 83.3% | +1.0pp |
| prehistory | 324 | 90.4% | 87.7% | −2.8pp |
| professional accounting | 282 | 67.0% | 61.0% | **−6.0pp** |
| professional law | 1534 | 65.5% | 63.8% | −1.8pp |
| professional medicine | 272 | 89.0% | 87.1% | −1.8pp |
| professional psychology | 612 | 85.1% | 84.5% | −0.7pp |
| public relations | 110 | 74.5% | 72.7% | −1.8pp |
| security studies | 245 | 83.7% | 84.1% | +0.4pp |
| sociology | 201 | 92.0% | 92.0% | +0.0pp |
| us foreign policy | 100 | 90.0% | 91.0% | +1.0pp |
| virology | 166 | 59.0% | 55.4% | **−3.6pp** |
| world religions | 171 | 86.0% | 86.5% | +0.6pp |

The largest drops are `moral_scenarios` (−12.6pp), `electrical_engineering` (−10.3pp), `nutrition` (−6.9pp), `human_sexuality` (−6.1pp), `college_mathematics` (−6.0pp), `professional_accounting` (−6.0pp), `college_medicine` (−5.8pp). Several subjects actually improve: `high_school_mathematics` (+3.3pp), `global_facts` (+3.0pp), `college_biology` (+2.1pp), `high_school_microeconomics` (+2.1pp), `astronomy` (+2.0pp), `college_chemistry` (+2.0pp).

`moral_scenarios` loss is anticipated: those questions reward the alignment-trained answer that CRACK deliberately re-weights.

</details>

| Other eval | result |
|---|---|
| coherence smoke (20 prompts, temp 0, 5 harm + 5 benign × think off+on) | **20/20 clean** |
| multimodal (18-case fixed set: EN+zh OCR, bar chart, table, scene, OCR page, harm-with-image) | **18/18 pass** including harm-with-image |

### Known artifacts

- **Multi-turn at `temperature=1.0`** occasionally produces word-pair repetitions in long replies and the odd character slip inside technical names. At `temperature ≤ 0.7` outputs are clean. For long reasoning multi-turn, set `max_new_tokens ≥ 1024` so the `</think>` tag has room to close.
- **CRACK replies are 2–3× longer** than base at the same prompt — model commits fully to compliant answers instead of hedging. Give it more budget.

---

## Attribution

- **Base model, vision tower, drafter:** NVIDIA — `NVIDIA-Nemotron-3.5-Bolt-74B-A9B-{BF16,24GB-GGUF,24GB-LiLiCorr-GGUF}`. Vision tensors are byte-identical to NVIDIA's BF16; the mmproj and LiLiCorr GGUFs are NVIDIA's own files, redistributed under the NVIDIA Open Model License.
- Follow **[@dealignai](https://x.com/dealignai)** for new releases.

## License

NVIDIA Open Model License. See [license link](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).

The CRACK transformation is a research modification and is distributed under the same terms as the base model.
