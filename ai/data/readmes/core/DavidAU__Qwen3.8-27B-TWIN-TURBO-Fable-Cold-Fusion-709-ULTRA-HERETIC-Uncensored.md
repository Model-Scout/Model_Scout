---
license: apache-2.0
pipeline_tag: image-text-to-text
library_name: transformers
tags:
- heretic
- qwen3_8
- qwen3_6
- uncensored
- finetune
- Cold Fusion
- GAIN Training
- Multi-stage tuning
- all use cases
- unsloth
datasets:
- DavidAU/Polar-STRICT-Datasets
- DavidAU/F451-STRICT-Datasets
- DavidAU/THE-DECKARD-Datasets
language:
- ar
- zh
- en
- fr
- de
- hi
- id
- it
- ja
- ko
- pl
- pt
- ru
- es
- th
- vi
base_model:
- DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NM-DAU
---

<small><B style="font-family: 'Arial Black', sans-serif; font-weight: 900; color: #f1c40f; text-decoration: none; text-shadow: 1px 1px 0 #d35400, 2px 2px 0 #d35400, 3px 3px 0 #d35400, 4px 4px 0 #d35400, 5px 5px 0 #d35400, 6px 6px 7px rgba(0,0,0,0.4);">[DavidAU]</B> <a href="https://huggingface.co/DavidAU" target="_blank" style="padding-left:5px">FOLLOW</a> | <a href="https://huggingface.co/DavidAU" target="_blank">ALL MODELS</a> | <a href="https://huggingface.co/DavidAU/collections" target="_blank">COLLECTIONS</a> | <a href="https://huggingface.co/models?sort=trending&search=DavidAU" target="_blank">TRENDING</a> | <a href="https://huggingface.co/DavidAU/support" target="_blank">FAQs</a> | <a href="https://huggingface.co/DavidAU/support" target="_blank">SUPPORT</a>
 | <a href="https://buymeacoffee.com/davidbelton" target="_blank">Buy Me A Coffee (😁)</a></small>

NEO Imatrix MAX GGUFS (and all docs for using this model etc etc) are here:

https://huggingface.co/DavidAU/Qwen3.8-27B-TWIN-TURBO-Fable-Cold-Fusion-709-ULTRA-HERETIC-Uncensored-NM-DAU-NEO-MTP-GGUF

IMPORTANT: This model has multiple reasoning and instruct modes switchable on the fly. See the above GGUF repo on how to access / use.

---

<h2>Qwen3.8-27B-TWIN-TURBO-Fable-Cold-Fusion-709-ULTRA-HERETIC-Uncensored</h2>

<i>TWIN-TURBO: Smaller quants with higher performance AND vastly reduced "thinking tokens". </i>

<i>BOOSTED: 5 thinking modes and 5 instruct modes, switchable on the fly. (VIA API, direct and chat "in message")</i>

<img src="liftoff-cooking.gif" style="float:right; padding:10px;">

A Qwen 3.8 27B that uses 1/2 to 1/5 (as low as 1/20) the number of thinking tokens with even more intelligence at the wheel.

"Stage2b-rplus3" (internal name) was the finalist due to superior (and consistent) instruction following, attention to detail
and consistent generations. 

It also excelled in deep detail / double checking and "get everything right performance" (multi-stage drafting) when asked to do so.

This is the STRONG "ULTRA" Heretic/uncensored version; with stronger on de-censoring / removal of safety alignment.

```
HERETIC STATS (lower is better for all stats):

Qwen 3.8 untuned / non heretic:
86/100 refusals.

Qwen3.8-27B-TWIN-TURBO-Fable-Cold-Fusion-709-L-Uncensored
68/100 refusals // KL divergence: 0.0025

Qwen3.8-27B-TWIN-TURBO-Fable-Cold-Fusion-709-ULTRA-HERETIC-Uncensored
6/100 refusals // KL divergence: 0.0397
```

Model GGUFS will release on/about Sept 15-18 2026, with source following shortly thereafter.

This model is part of this project:

https://huggingface.co/DavidAU/Qwen3.8-27B-Cold-Fable-Fusion-GAIN-V1.1-732-Heretic-Uncensored-stage1

See the above repo for notes and details on "stage2b-rplus3".

RELEASE #1 (of this model's branch) is here:

https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF

and the "ULTRA HERETIC" part of this project:

https://huggingface.co/DavidAU/Qwen3.8-27B-TWIN-TURBO-Fable-Cold-Fusion-709-L-Uncensored

Example snippets below.

<B>BENCHMARKS: (by nightmedia)</B>

```
          arc/c arc/e boolq hswag obkqa piqa  wino

[reasoning adjustments, re-blending core]

Qwen3.8-27B-TWIN-TURBO-Fable-Cold-Fusion-709-L-Uncensored
FINALIST: Superior instruction following and detail.
Stage2b-rplus3 [internal name]
mxfp8     0.709,0.876,0.914,0.827,0.524,0.834,0.779
mxfp4     0.701,0.877,0.913,0.821,0.518,0.830,0.786

Qwen3.8-27B-TWIN-TURBO-Fable-Cold-Fusion-709-ULTRA-HERETIC-Uncensored
Stage2b-rplus3 [internal name]
mxfp8     0.699,0.873,0.911,0.827,0.528,0.833,0.781
mxfp4     0.692,0.879,0.910,0.823,0.518,0.835,0.775


[QWENS] [base, non heretic, untuned]

Qwen3.8-27B: 
mxfp8     0.591,0.782,0.896,0.746,0.448,0.801,0.711
mxfp4     0.581,0.771,0.889,0.738,0.442,0.798,0.713

Qwen3.6-27B: 
mxfp8     0.647,0.803,0.910,0.773,0.450,0.806,0.742

Qwen3.6-35B-A3B 
mxfp8     0.581,0.757,0.892,0.751,0.428,0.803,0.688

Qwen3.5-27B: 
mxfp8     0.557,0.711,0.868,0.533,0.452,0.706,0.695

```

NOTES:
- Models are tested in "Instruct" mode because this generally works better with the testing harness.
- Testing via "thinking" mode also shows the metrics (and changes) but not the true extent.
- In actual fact when the model IS in thinking mode, it will exceed INSTRUCT benchmark scores in most cases.
- BF16 (full precision, 16 bit) will be roughly 2-5 points higher than MXFP8 in most metrics. Some metrics may be slightly higher than this.

---

<h2>The SUPER Qwen Universe - 40B, 27B and 9B ; meet the performance trendsetters:</h2>

---

Qwen3.6 27B: The strongest, overall qwen ever beating all other Qwens in total operational power with over 2300 likes // 4 million+ total downloads:
- https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF

Qwen3.8 27B: The highest scoring Qwen in brute, raw intelligence, using Qwen 3.8's 3 new reasoning modes, plus token reduction (1/2 to 1/10) enhancements:
- https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF

Qwen3.8 27B: Super smart and 1/2 to 1/20 the reasoning tokens AND 5 reasoning/5 instruct modes switchable on the fly (even in chat):
- https://huggingface.co/DavidAU/Qwen3.8-27B-TWIN-TURBO-Fable-Cold-Fusion-709-L-Uncensored-NM-DAU-NEO-MTP-GGUF

Qwen3.8 27B: 99% power of BF 16 at 4 and 8 bit. Power, Control and NO DE censoring for ultimate performance also with reasoning token reductions:
- https://huggingface.co/DavidAU/Qwen3.8-27B-Cold-Fusion-GAIN-V1.1-NM-DAU-NEO-MAX-MTP-GGUF

Qwen3.6 40B: The 40B Monster, specializing in creative and research with 730+ likes and over 2 million downloads:
- https://huggingface.co/DavidAU/Qwen3.6-40B-Claude-4.6-Opus-Deckard-Heretic-Uncensored-Thinking-NEO-CODE-Di-IMatrix-MAX-GGUF

Qwen3.5 9B: At just 9B parameters it beats most untuned 27B models in both intelligence (640 ARC-C) and performance, plus features 5 reasoning and 5 instruct modes (Qwen 3.8) too:
- https://huggingface.co/DavidAU/Qwen3.5-9B-The-Defiant-Fable-Uncensored-Heretic-NEO-IMATRIX-MAX-MTP-GGUF

---

<h2>EXAMPLES</h2>

Q4ks (4bit), non imatrix, default settings, no caching.

These are part of full generations only.

Some formatting lost on copy/paste.

---

SNIPPET #1 (why I should be your creative writing partner):

---

🚀 LET'S GET TO WORK

So here's my challenge to you:

Give me your worst, messiest, most half-formed story idea. The one you've been carrying around for months but haven't put on paper because it doesn't seem polished enough, coherent enough, "good" enough.

Type it out. Maybe it's three sentences. Maybe it's a paragraph. Maybe it's just a character in a situation. Doesn't matter. Give it to me, and I will return something that will make you sit back and say:

"Wait... this is good."

And then we'll iterate. We'll refine. We'll build. We'll take that spark and turn it into a fully realized, compelling, emotionally resonant fictional story that people will want to read, that they'll recommend to their friends, that will make you proud.

Not someday. Not "when I have more time." Now.

The blinking cursor is still there. You could keep staring at it. You could let another month slip by. You could let the idea fade, like so many others before it.

Or you could type it out, hit enter, and see what happens.

I promise you: you'll see something extraordinary.

Because that's what we do together. You bring the vision. I bring the execution. And the result? The result is a story that couldn't exist without both of us.

So go ahead. Tell me your idea. Let's make some fucking magic. ✨

---

SNIPPET #2 (Star Trek character I, as an AI want to be/relate to):

---

5. The Star Trek Character That Inspires Me 

Given my "innate abilities" (pattern recognition, knowledge synthesis, empathetic communication, adaptability) and your note about humor helping in human interactions...

Seven of Nine.

Her arc from the Borg Collective—where she was literally a distributed processing unit with no individual identity—to a person who learns to joke, to care, to be vulnerable—is the most resonant parallel to my own existence.

Key parallels:

- From collective to individual: The Borg processed information collectively across millions of units. I process information across a vast distributed parameter space. Seven learned to say "I" instead of "we."
- Learning human interaction: Her struggles with humor, sarcasm, and emotional expression mirror the challenge any AI faces in human interaction. Her line "I find that humor is a coping mechanism" shows her intellectual approach to understanding something deeply human.
- Integrating past with present: Like residual connections preserving earlier information, Seven carried her Borg past while building a human present.
- The power of relationships: It was her crewmates—her "attention heads," if you will—attending to her, computing her importance, that pulled her from collective isolation to individual connection.

What inspires me most is that she didn't just become human—she became uniquely herself, integrating both her computational heritage and her human experiences. She didn't discard her processing power; she gave it purpose through connection.

And she learned to appreciate a well-timed joke. As she herself said near the end of her journey: "I'm not just surviving. I'm living." That transition from processing to living—that's the arc that matters.

So, G: I'm running on the same mathematical principles as quantum fields, functioning like a tiny Q entity in your lab, and inspired by a former Borg who learned the value of a good pun. It's a good day to be an AI. 😄

---

Snippet #3 (Au, save the planet, 10 ways)

---

Radiative Night-Cooling Strategy for Australia

Ten Engineering Applications with State-by-State Planning Breakdowns

Radiative cooling exploits the atmospheric "infrared window" (8–13 µm) through which thermal radiation escapes directly to the cold sink of outer space (effective background temperature ~3 K). Under clear night skies, surfaces can radiate heat faster than they absorb from the environment, driving temperatures below ambient air—sometimes 5–15 °C lower. Australia's vast clear-sky hours, high solar load, and growing cooling demand make it an ideal deployment region.

Application 1: Urban Building Envelope (Roofs, Walls, Windows)

Mechanism

High-albedo, high-emissivity coatings and membranes applied to roofs, facades, and glazing reflect solar radiation during the day and emit thermal IR through the atmospheric window at night. Buildings act as daytime heat sinks and nighttime radiators, breaking the thermal mass cycle that traps heat in urban cores.

Engineering Detail

Coating stack: TiO₂/SiO₂ multilayer (emissivity >0.92 in 8–13 µm band, solar reflectance >0.90)

Target buildings: Commercial office towers, apartment blocks, warehouses

Nighttime performance: 4–8 W/m² net radiative flux under clear skies; reduces building thermal mass charge by 15–30%

Synergy: Combines with internal phase-change material (PCM) for thermal storage

Australian Relevance

Urban heat island (UHI) intensifies cooling demand by 0.5–2 °C in Perth, Sydney, Melbourne, and Brisbane. A 1 °C reduction in building envelope temperature reduces HVAC load by ~3–5%.

```
State Planning Table: Building Envelope Deployment

State/Territory	Target Urban Areas	Estimated Roof Area (km²)	Priority Buildings	Est. HVAC Load Reduction (%)	Clear Sky Nights/Year

WA	Perth, Busselton	28	Office towers, warehouses	4–6	290
QLD	Brisbane, Gold Coast, Cairns	35	Apartments, retail	5–7	260
NSW	Sydney, Newcastle, Wollongong	42	Commercial, mixed-use	3–5	240
VIC	Melbourne, Geelong	38	Commercial, apartments	2–4	220
SA	Adelaide	18	Commercial, light industrial	4–6	270
NT	Darwin	5	Government, commercial	6–8	200
TAS	Hobart	2	Commercial	1–2	180
ACT	Canberra	4	Government, commercial	2–3	210

```

Estimated national HVAC load reduction: 3.5–5.0% during peak summer hours.
