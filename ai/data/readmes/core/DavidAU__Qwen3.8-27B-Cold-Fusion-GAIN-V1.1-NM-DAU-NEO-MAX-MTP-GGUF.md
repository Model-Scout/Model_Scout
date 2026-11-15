---
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
license: apache-2.0
tags:
- unsloth
- GAIN Training
- COLD-FUSION
- finetune
- unsloth
- MTP GGUF Quants
- Regular GGUF Quants
- qwen3.8
- multi-stage tuned
- thinking
- reasoning
- all use cases
- coder
- creative
- creative writing
- all genres
- story
- writing
- fiction
- roleplaying
- bfloat16
datasets:
- DavidAU/Polar-STRICT-Datasets
- DavidAU/Reasoning-STRICT-Datasets
pipeline_tag: image-text-to-text
base_model:
- DavidAU/Qwen3.8-27B-Cold-Fusion-GAIN-V1.1
---

<small><B style="font-family: 'Arial Black', sans-serif; font-weight: 900; color: #f1c40f; text-decoration: none; text-shadow: 1px 1px 0 #d35400, 2px 2px 0 #d35400, 3px 3px 0 #d35400, 4px 4px 0 #d35400, 5px 5px 0 #d35400, 6px 6px 7px rgba(0,0,0,0.4);">[DavidAU]</B> <a href="https://huggingface.co/DavidAU" target="_blank" style="padding-left:5px">FOLLOW</a> | <a href="https://huggingface.co/DavidAU" target="_blank">ALL MODELS</a> | <a href="https://huggingface.co/DavidAU/collections" target="_blank">COLLECTIONS</a> | <a href="https://huggingface.co/models?sort=trending&search=DavidAU" target="_blank">TRENDING</a> | <a href="https://huggingface.co/DavidAU/support" target="_blank">FAQs</a> | <a href="https://huggingface.co/DavidAU/support" target="_blank">SUPPORT</a>
 | <a href="https://buymeacoffee.com/davidbelton" target="_blank">Buy Me A Coffee (😁)</a></small>

<small><font color="red">IMPORTANT:</font> The COLD FUSION (GAIN+Unsloth) method of training maintains 99% of performance of BF16, at both 8 bit and 4 bit levels. This 
version also reduces thinking tokens by 1/2 to as much as 1/10 the amount, while maintaining core details AND reasoning power. Model exceeds all Qwen 3.8, 3.6 
and 3.5 27B critical core benchmarks. MTP speeds are also faster. A model that gets down to business faster, with less "talking" and is smarter too. Part of the tech is based on (2200+ likes, 3m + downloads): 
[Fable-Fusion-711](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF) || [Turbo - 1/2 to 1/10 the reasoning tokens](https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF)

</small>

<h2>Qwen3.8-27B-Cold-Fusion-GAIN-V1.1-NM-DAU-NEO-MAX-MTP-GGUF</h2>

<img src="cannonball.webp" style="float:right; padding:10px;">

Cold Fusion has 1/5 (as low as 1/10 in some cases) to 1/2 the thinking tokens (vs reg Qwen 3.8) across all 3 modes of operation, and it is faster and smarter too 
created using the COLD FUSION method of training.

This is a high detail focused model, with tuning specific to address over reasoning/over thinking and excessive token consumption.

EXAMPLE generations at the bottom of the page.

A Colab between myself (tuning, COLD Fusion), Nightmedia (benching), and TeichAI (Datasets). 

The strict goals of this model creation were:
- Increase the general model intelligence and problem solving abilities.
- Reduce thinking block size from 1/2 to as low as 1/10 the size [median reduction: 2/3 roughly].
- Reformatting the thinking block, as well as improving it.
- Speed up token generation, especially MTP.
- Ensure all updates work with all three modes of thinking.
- ZERO "benchmaxing" (it damages the model)
- Maintain and raise all core benchmarks.

<B>COLD FUSION ("Gain" + "Unsloth") TRAINING: </B>

COLD FUSION (GAIN+UNSLOTH) training tech which was invented by my team during the R & D 
of "Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic" (2100+ likes, 3 million + downloads, 60+ quant repos):

https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF

The "GAIN" is the core invented component, then coupled with Unsloth's trainers/systems => AKA -> COLD FUSION.

The "GAIN" method (programming) automatically (and dynamically) changes training on a per sample basis in real time during training AS THE MODEL LEARNS. 

The method improved metrics as well as overall model performance without overcooking or damaging the model.

This has also resulted, in the strongest and most stable model at both 4 bit and 8 bit and made 4 bit performance 99% of 8 bit performance too.

Note this model (Qwen3.8-27B-Cold-Fusion-GAIN-V1.1) is about a level 1 or 2 relative to Qwen3.6-27B-Fable-Fusion-711 at level 7-8.

A stronger, more in depth tune of Qwen3.8-27B (including ablit/uncensored) using both COLD Fusion method and the "Fable-Fusion-711" pipeline is planned. 
This is also a heavier undertaking which takes 7-10 days (min) to complete as it includes 6 stages plus multiple sub-stages. 

<B>TESTING:</B>

Testing and benching was done at each stage to ensure quality.

You can also see benchmarks below too for this model, Qwen 3.6 27B, and Qwen 3.5 27B.

HOWEVER, the final testing was HUMAN testing. A trust, but verify approach.

Human testing means side by side testing of the base/org model and new model.

Features:
- Improved instruction following.
- Overall increase in general intelligence and problem solving.
- Better thinking/reasoning with far smaller thinking/reasoning blocks, output generation will also be compressed by default in many cases.
- Even lower/lowest quants are exceptional.
- No corruption or change to Team Qwen's exceptional model - everything is there.
- Vision

<B>IMPORTANT:</B>

This model, like regular Qwen 3.8 27b, supports THREE modes of reasoning : xhigh (default), medium and low [see info in Qwen 3.8 section below].

Reduction in thinking tokens/reasoning block size extends across all three modes of operation.

Likewise detail levels extend to all three modes too, even with reduced thinking/reasoning block the OUTPUT detail will remain high.

To REDUCE thinking block[s] further, increase the level/detail of your instructions/prompts - it only takes a little bit more here so the model has to guess / reason a little bit less.

Also, generally within the same chat additional reasoning blocks will also be reduced from typical Qwen levels many times hitting 1/5 the size or lower. Multi-turn
chat - example: prompt, reasoning and 1st output - in the refinement stage(s) will see very strong reduction in thinking tokens/blocks.

Also note that the modification of "reasoning" is a major change to the model please carefully test it for your use case(s).

<B>Modification of REASONING:</b>

If you AI app does not support a "switch" you can manually modify the JINJA template.

The default setting is "xhigh" ; to change to medium or low use:

```
{%- set reasoning_effort = 'medium' %}

OR

{%- set reasoning_effort = 'low' %}
```

Place this at the VERY TOP of the jinja template.

In LMStudio you can access this in DEV mode, and switch off the "advanced updates" option.

Other AI apps may vary.

You can also make your own quants from source here:

https://huggingface.co/DavidAU/Qwen3.8-27B-Cold-Fusion-GAIN-V1.1

Just modify the "chat-template.jinja" (in NOTEPAD or similar) AND the token-config.. json file too (or delete the "chat template" from this file).

ADVANCED:

Qwen 3.8 uses System prompt injection control by the Jinja template to control reasoning levels.

If you set it at "medium" this turns off injection [ie: no system prompt is injected]

You can then set a "reasoning" system prompt yourself.

The other option: 

Modify the jinja itself and the system prompt(s) to better tune reasoning to your use cases.

This is the section:

```
{%- if enable_thinking is undefined or enable_thinking is true %}
    {%- set resolved_reasoning_effort = reasoning_effort|default('xhigh') %}
    {%- if resolved_reasoning_effort not in ('xhigh', 'medium', 'low') %}
        {{- raise_exception('Unexpected reasoning effort ' ~ reasoning_effort ~ '. Supported types are xhigh (default), medium, and low.') }}
    {%- endif %}
    {%- if resolved_reasoning_effort == 'xhigh' %}
        {%- set reasoning_instructions = 'Reasoning effort is set to xhigh. Please think carefully through the task, validate key assumptions, consider plausible alternatives, and prioritize correctness, consistency, and clarity in the final answer.' %}
    {%- elif resolved_reasoning_effort == 'low' %}
        {%- set reasoning_instructions = 'Reasoning effort is set to low. Keep your thinking brief and focused, moving directly to the conclusion without unnecessary elaboration.' %}
    {%- endif %}
{%- endif %}
```

<B>Regular and MTP GGUFS:</b>

<a href="https://www.buymeacoffee.com/davidbelton" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" style="height: 60px !important;width: 217px !important;" ></a>

All quants (regular and MTP) are NEO IMATRIX, which improve accuracy of the quants by an additional 2-4% over normal GGUFs as well as long context performance.

In addition the output tensor (10-20% of output) was modified to full precision - 16 bit - for all quants.

"MTP" GGUFS (multi-token prediction):
- "MTP" GGUFS will have "MTP" in the name as a suffix.
- I have also set the MTP tensors to Q8_0 precision for all quants.
- To get better performance keep temp 1 or less (higher temps degrade MTP performance).
- Likewise with rep pen ; keep at 1 (off). If you raise it performance will suffer.
- If you see "token acceptance" rates BELOW 50% (predict 2 tokens) switch to normal quants.

I have also added two "LOW" quants, with "LOW" in the name:
- IQ4_XS and Q6_K
- These are for max speed / reduced VRAM and without MTP/OT mods.
- Performance may be slightly lower than the reg "MAX" quants.

SPEED:
- On Q4_K_S (4bit) quant, regular GGUFs are about 75 t/s, whereas MTP GGUFs (acceptance at 60%, 2 tokens) can exceed 90 T/S. (5090, Windows 11, testing in LMStudio)
- Speeds will vary depending on GPU(s), AI app, O/S (Linux/Mac will generally be faster) and hardware.
- "MTP" quants speeds will vary ; for creative/complex and/or temps over 1 use regular GGUFs for better performance.

I suggest you download at least one of each - regular and MTP gguf(s) - and test them for your use case(s). 

If you get "token acceptance" (predict 2 tokens) with MTP quant(s) BELOW 50% (this means regular quants will run faster), then regular GGUF(s) will actually perform better - ie faster.

MTP quant(s) can in some cases run faster as the token window fills up and/or in multi turn chats.

Note there is NO other diffence between the quants type besides speed: both will do the same job.

<B>Model:</b>
- 256k context
- Gguf quants run in all standard AI apps.
- Vision is activated, but you need to download separate "mmproj" file (ONE) to use it.

<B>VISION:</B>
- Vision (images) tested.
- You need an "mmproj" (just one) of these downloaded too, and placed in the same folder as the GGUF for images.

<B>Qwen Model Settings (suggested) 3.8 and 3.5/3.6:</B>

Qwen 3.8 uses the same framework (tensors, layers, repeating 4 layers, etc) as Qwen 3.5 and 3.6 ; however with new reasoning options the best settings for
your uses cases may vary IE you might find Qwen 3.5/.6 settings better and/or Qwen 3.8 settings.

NOTES - GENERAL: 
- Due to Qwen 3.8's new reasoning options you may need to adjust parameters - especially temp - slightly.
- Also, lower quants (Q4ks and lower) may benefit from slightly higher temps for some use cases.

NOTE presence_penalty: 
- If this is set, it can have major impact (neg) on coding, math and/or other specific use cases with high "repeats" in the thinking and/or output.
- If you use it, start LOW IE 0.25 and increase only as you need to.
- My view: ONLY set this if you need it ; it prevents loops / other issues in some use case(s).

QWEN 3.8 SETTINGS, including this model (from Qwen):
- Thinking Mode: temperature=1.0, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=0.0, repetition_penalty=1.0
- Instruct (or non-thinking) mode: temperature=0.7, top_p=0.80, top_k=20, min_p=0.0, presence_penalty=1.5, repetition_penalty=1.0
- Context window min from 8k to 16k ; suggest 24k to 32k even with reduced reasoning blocks.

QWEN 3.5/3.6 SETTINGS (from Qwen):
- Thinking mode for general tasks: temperature=1.0, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=0.0, repetition_penalty=1.0
- Thinking mode for precise coding tasks (e.g. WebDev): temperature=0.6, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=0.0, repetition_penalty=1.0
- Instruct (or non-thinking) mode: temperature=0.7, top_p=0.80, top_k=20, min_p=0.0, presence_penalty=1.5, repetition_penalty=1.0
- Context window min from 8k to 16k ; suggest 24k to 32k even with reduced reasoning blocks.

---

<h2>BENCHMARKS by Nightmedia</h2>

---

Important note on Qwen 27B 3.8 bench VS Qwen 3.6/3.5 27B versions:

Based on my testing / Qwen's own statements, community statements (ie localllama) and extended benchs for 3.8-27B version (team Qwen) this model is more focused on
deeper thinking, coding and agentic functions than previous Qwen versions.

```
          arc/c arc/e boolq hswag obkqa piqa  wino

Qwen3.8-27B-Cold-Fusion-GAIN-V1.1 [non heretic]
mxfp8     0.655,0.838,0.898,0.751,0.498,0.807,0.738
mxfp4     0.645,0.833,0.887,0.740,0.496,0.799,0.732

Qwen3.8-27B-Instruct: [base, non heretic]
mxfp8     0.591,0.782,0.896,0.746,0.448,0.801,0.711
mxfp4     0.581,0.771,0.889,0.738,0.442,0.798,0.713

Qwen3.6-27B-Instruct: [base, non heretic]
mxfp8     0.647,0.803,0.910,0.773,0.450,0.806,0.742

Qwen3.6-35B-A3B-Instruct [base, non heretic]
mxfp8     0.581,0.757,0.892,0.751,0.428,0.803,0.688

Qwen3.5-27B-Instruct: [base, non heretic]
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

NEW!:

<B>TURBO BRILLIANCE 50x: Reduce tokens, increase quality and IQ:</b> The new tech from DavidAU to change and improve all models see the collection (3B to 120B; and growing fast):
https://huggingface.co/collections/DavidAU/turbo-brilliance-ai-constructs-50x-reasoning-instruct

--

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

<B>Settings: CHAT / ROLEPLAY and/or SMOOTHER operation of this model:</B>

In "KoboldCpp" or  "oobabooga/text-generation-webui" or "Silly Tavern" ;

Set the "Smoothing_factor" to 1.5 

: in KoboldCpp -> Settings->Samplers->Advanced-> "Smooth_F"

: in text-generation-webui -> parameters -> lower right.

: In Silly Tavern this is called: "Smoothing"


NOTE: For "text-generation-webui" 

-> if using GGUFs you need to use "llama_HF" (which involves downloading some config files from the SOURCE version of this model)

Source versions (and config files) of my models are here:

https://huggingface.co/collections/DavidAU/d-au-source-files-for-gguf-exl2-awq-gptq-hqq-etc-etc-66b55cb8ba25f914cbf210be

OTHER OPTIONS:

- Increase rep pen to 1.1 to 1.15 (you don't need to do this if you use "smoothing_factor")

- If the interface/program you are using to run AI MODELS supports "Quadratic Sampling" ("smoothing") just make the adjustment as noted.

<B>Highest Quality Settings / Optimal Operation Guide / Parameters and Samplers</B>

This a "Class 1" model:

For all settings used for this model (including specifics for its "class"), including example generation(s) and for advanced settings guide (which many times addresses any model issue(s)), including methods to improve model performance for all use case(s) as well as chat, roleplay and other use case(s) please see:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]

You can see all parameters used for generation, in addition to advanced parameters and samplers to get the most out of this model here:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]

---

# Qwen3.8-27B

> [!Note]
> This repository contains model weights and configuration files for the post-trained model in the Hugging Face Transformers format. 
>
> These artifacts are compatible with Hugging Face Transformers, vLLM, SGLang, TokenSpeed, etc.

> [!Tip]
> For users seeking managed, scalable inference without infrastructure maintenance, the official Qwen API service is provided by [Qwen Cloud](https://www.qwencloud.com).
> In particular, **Qwen3.8-27B** will be available as a hosted version with more production features, e.g., 1M context length by default, official built-in tools. For more information, please refer to the [Qwen3.8-27B Overview](https://www.qwencloud.com/models/qwen3.8-27b). The service is coming soon. Stay tuned for updates.

Following the widespread community adoption of the Qwen3.5 and Qwen3.6 series, we are pleased to introduce Qwen3.8, the most capable generation in the Qwen open-model family to date.

Built on the architectural foundation of Qwen3.5, Qwen3.8 delivers substantial gains across coding, professional work, research, and long-horizon agentic tasks. Qwen3.8-27B brings these advances to a compact, deployment-friendly dense model: a native vision-language model that understands images and videos, with flexible thinking control, designed to carry complex, multi-step tasks through to completion with greater reliability.

## Qwen3.8 Highlights

Qwen3.8-27B features the following enhancements:
- **Core Capabilities**: Comprehensive improvements across coding, professional work, research, and long-horizon agentic tasks.
- **Agent Execution**: Stronger autonomous planning and better handling of environment feedback, leading to more reliable end-to-end task completion.
- **Downstream Compatibility**: Broader support for popular harnesses and development tools, making it easier to integrate into your existing stack.
- **Flexible Thinking Control**: Thinking mode is on by default and can be disabled per request; reasoning depth can be tuned with `reasoning_effort`, and reasoning context from historical messages is retained via `preserve_thinking`.
- **Vision-Language Understanding**: Native support for image and video understanding, from STEM diagrams and documents to hour-scale videos.


## Model Overview

- Type: Causal Language Model with Vision Encoder
- Training Stage: Pre-training & Post-training
- Language Model
    - Number of Parameters: 27B
    - Hidden Dimension: 5120
    - Token Embedding: 248,320 (Padded)
    - Number of Layers: 64
    - Hidden Layout: 16 × (3 × (Gated DeltaNet → FFN) → 1 × (Gated Attention → FFN))
    - Gated DeltaNet:
        - Number of Linear Attention Heads: 48 for V and 16 for QK
        - Head Dimension: 128
    - Gated Attention:
        - Number of Attention Heads: 24 for Q and 4 for KV
        - Head Dimension: 256
        - Rotary Position Embedding Dimension: 64
    - Feed Forward Network:
        - Intermediate Dimension: 17,408
    - LM Output: 248,320 (Padded)
    - MTP (Multi-Token Prediction): trained with multiple steps
- Context Length: 262,144 natively and extensible up to 1,000,000 tokens.


## Benchmark Results

### Text Performance
<style>
.vl-table th{font-size:15px!important;line-height:1.2}
.vl-table td:not(.benchmark-cell):not([colspan]){font-size:15px;line-height:1.2;vertical-align:middle}
.vl-table .benchmark-cell{padding:12px 10px 12px 18px!important;vertical-align:middle}
.vl-table .benchmark-capability{font-size:15px;font-weight:600;line-height:1.22;color:#171717}
.vl-table .benchmark-name{margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B}
.vl-table .metric-stack{display:flex;flex-direction:column;gap:7px;padding:3px 0}
.vl-table .metric-label{font-size:10px;font-weight:400;line-height:1.1;color:#777}
.vl-table .metric-value{margin-top:2px;font-size:15px;line-height:1.15;color:#171717}
</style>
<div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;max-width:1200px;margin:0 auto;padding:16px 0">
<table class="vl-table" style="width:100%;table-layout:fixed;border-collapse:collapse;font-size:13px">
<thead><tr>
<th style="padding:10px 7px;text-align:left;font-weight:600;border-bottom:2px solid #0A2EFE;color:#0A2EFE"></th><th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #0A2EFE;color:#0A2EFE;font-size: 14px;width:14.00%;background:rgba(10, 46, 254, 0.08);">Qwen3.8-27B</th><th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #0A2EFE;color:#0A2EFE;font-size: 14px;width:14.00%;">Qwen3.6-27B</th><th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #0A2EFE;color:#0A2EFE;font-size: 14px;width:14.00%;">Qwen3.7-Plus</th><th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #0A2EFE;color:#0A2EFE;font-size: 14px;width:14.00%;">Muse Glimmer-30B</th><th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #0A2EFE;color:#0A2EFE;font-size: 14px;width:14.00%;">Opus4.6 Max</th></tr></thead>
<tbody>
<tr><td colspan="6" style="padding:8px 12px;font-weight:600;color:#0A2EFE;border-bottom:1px solid rgba(10, 46, 254, 0.2);background:#D6DAFC">Coding</td></tr>
<tr>
<td class="benchmark-cell" style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);"><div class="benchmark-capability" style="font-size:15px;font-weight:600;line-height:1.22;color:#171717">Agentic terminal coding</div><div class="benchmark-name" style="margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B">Terminal Bench 2.1 (Terminus)</div></td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);background:rgba(10, 46, 254, 0.08);vertical-align:middle;font-size:15px;line-height:1.2;">73.0</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">63.4</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">64.0</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">51.7</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;"><strong>78.2</strong></td>
</tr>
<tr>
<td class="benchmark-cell" style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);"><div class="benchmark-capability" style="font-size:15px;font-weight:600;line-height:1.22;color:#171717">Agentic coding</div><div class="benchmark-name" style="margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B">SWE-bench Pro</div></td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);background:rgba(10, 46, 254, 0.08);vertical-align:middle;font-size:15px;line-height:1.2;"><strong>61.7</strong></td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">53.5</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">57.6</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">51.2</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">53.4</td>
</tr>
<tr>
<td class="benchmark-cell" style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);"><div class="benchmark-capability" style="font-size:15px;font-weight:600;line-height:1.22;color:#171717">Repo-level code generation</div><div class="benchmark-name" style="margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B">NL2Repo-Bench</div></td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);background:rgba(10, 46, 254, 0.08);vertical-align:middle;font-size:15px;line-height:1.2;">42.3</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">36.2</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">41.1</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">--</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;"><strong>47.6</strong></td>
</tr>
<tr>
<td class="benchmark-cell" style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);"><div class="benchmark-capability" style="font-size:15px;font-weight:600;line-height:1.22;color:#171717">Agentic coding</div><div class="benchmark-name" style="margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B">DeepSWE 1.1</div></td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);background:rgba(10, 46, 254, 0.08);vertical-align:middle;font-size:15px;line-height:1.2;"><strong>42.2</strong></td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">13.3</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">14.2</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">--</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">--</td>
</tr>
<tr>
<td class="benchmark-cell" style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);"><div class="benchmark-capability" style="font-size:15px;font-weight:600;line-height:1.22;color:#171717">Software engineering</div><div class="benchmark-name" style="margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B">QwenSWEBench</div></td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);background:rgba(10, 46, 254, 0.08);vertical-align:middle;font-size:15px;line-height:1.2;"><strong>79.0</strong></td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">49.3</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">59.2</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">--</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">63.8</td>
</tr>
<tr><td colspan="6" style="padding:8px 12px;font-weight:600;color:#0A2EFE;border-bottom:1px solid rgba(10, 46, 254, 0.2);background:#D6DAFC">Agent</td></tr>
<tr>
<td class="benchmark-cell" style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);"><div class="benchmark-capability" style="font-size:15px;font-weight:600;line-height:1.22;color:#171717">Long-horizon office work</div><div class="benchmark-name" style="margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B">CoWorkBench</div></td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);background:rgba(10, 46, 254, 0.08);vertical-align:middle;font-size:15px;line-height:1.2;"><strong>70.7</strong></td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">61.0</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">65.1</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">--</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">68.2</td>
</tr>
<tr>
<td class="benchmark-cell" style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);"><div class="benchmark-capability" style="font-size:15px;font-weight:600;line-height:1.22;color:#171717">Professional job tasks</div><div class="benchmark-name" style="margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B">JobBench</div></td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);background:rgba(10, 46, 254, 0.08);vertical-align:middle;font-size:15px;line-height:1.2;"><strong>33.4</strong></td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">21.8</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">27.6</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">--</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">--</td>
</tr>
<tr>
<td class="benchmark-cell" style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);"><div class="benchmark-capability" style="font-size:15px;font-weight:600;line-height:1.22;color:#171717">Frontier agentic tasks</div><div class="benchmark-name" style="margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B">Agents' Last Exam</div></td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);background:rgba(10, 46, 254, 0.08);vertical-align:middle;font-size:15px;line-height:1.2;"><div class="metric-stack" style="padding:3px 0"><div><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Pass@1</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717"><strong>20.4</strong></div></div><div style="margin-top:7px"><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Score</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717"><strong>42.9</strong></div></div></div></td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;"><div class="metric-stack" style="padding:3px 0"><div><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Pass@1</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717">10.6</div></div><div style="margin-top:7px"><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Score</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717">27.3</div></div></div></td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;"><div class="metric-stack" style="padding:3px 0"><div><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Pass@1</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717">13.2</div></div><div style="margin-top:7px"><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Score</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717">33.6</div></div></div></td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">--</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">--</td>
</tr>
<tr><td colspan="6" style="padding:8px 12px;font-weight:600;color:#0A2EFE;border-bottom:1px solid rgba(10, 46, 254, 0.2);background:#D6DAFC">General</td></tr>
<tr>
<td class="benchmark-cell" style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);"><div class="benchmark-capability" style="font-size:15px;font-weight:600;line-height:1.22;color:#171717">Instruction following</div><div class="benchmark-name" style="margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B">IFBench</div></td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);background:rgba(10, 46, 254, 0.08);vertical-align:middle;font-size:15px;line-height:1.2;"><strong>79.5</strong></td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">69.1</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">79.1</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">77.0</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">62.5</td>
</tr>
<tr>
<td class="benchmark-cell" style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);"><div class="benchmark-capability" style="font-size:15px;font-weight:600;line-height:1.22;color:#171717">Scientific reasoning</div><div class="benchmark-name" style="margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B">GPQA Diamond</div></td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);background:rgba(10, 46, 254, 0.08);vertical-align:middle;font-size:15px;line-height:1.2;">89.2</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">87.8</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">90.3</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">83.5</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;"><strong>91.3</strong></td>
</tr>
<tr>
<td class="benchmark-cell" style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);"><div class="benchmark-capability" style="font-size:15px;font-weight:600;line-height:1.22;color:#171717">Multidisciplinary reasoning</div><div class="benchmark-name" style="margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B">HLE</div></td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);background:rgba(10, 46, 254, 0.08);vertical-align:middle;font-size:15px;line-height:1.2;">30.8</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">24.0</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">34.7</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">22.0</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;"><strong>40.0</strong></td>
</tr>
<tr>
<td class="benchmark-cell" style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);"><div class="benchmark-capability" style="font-size:15px;font-weight:600;line-height:1.22;color:#171717">Competitive coding</div><div class="benchmark-name" style="margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B">LiveCodeBench v6</div></td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);background:rgba(10, 46, 254, 0.08);vertical-align:middle;font-size:15px;line-height:1.2;"><strong>90.3</strong></td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">83.9</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">89.6</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">--</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">88.8</td>
</tr>
</tbody>
</table>
<div style="margin-top:12px;font-size:11px;line-height:1.5;color:rgba(0,0,0,0.72)">
<ol style="margin:0;padding-left:20px">
<li>SWE-bench Pro: Except for Opus4.6 Max, which uses the officially reported score, all models are evaluated with the Claude Code harness at temp=1.0, top_p=0.95, and a 256K context window. Problematic tasks were corrected, and all baseline models were re-evaluated on the refined benchmark.</li>
<li>NL2Repo-Bench: Evaluated with the Claude Code harness. To prevent reward hacking, we disable Bash commands that attempt to access the specific repository, such as pip download, pip install, and git clone.</li>
<li>DeepSWE 1.1: Evaluated with the Claude Code harness at temp=1.0, top_p=0.95, and a 256K context window.</li>
<li>QwenSWEBench: In-house coding benchmark for evaluating models' software engineering capabilities. Evaluated with the Claude Code harness. Reporting avg@3 with an 8-hour timeout, max_tokens=32,768, temperature=1.0, and a 256K context window.</li>
<li>CoWorkBench: In-house cowork benchmark for evaluating long-horizon tasks across computer science, finance, law, medical, and other productivity domains.</li>
<li>HLE: Judged by GPT-4o.</li>
<li>The best result in each row is shown in bold.</li>
<li>Empty cells (--) indicate that results are not yet available or not applicable.</li>
</ol>
</div>
</div>

### VL Performance
<div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;max-width:1200px;margin:0 auto;padding:16px 0">
<table class="vl-table" style="width:100%;table-layout:fixed;border-collapse:collapse;font-size:13px">
<thead><tr><th style="padding:10px 7px;text-align:left;font-weight:600;border-bottom:2px solid #0A2EFE;color:#0A2EFE"></th><th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #0A2EFE;color:#0A2EFE;font-size: 14px;width:14.00%;background:rgba(10, 46, 254, 0.08);">Qwen3.8-27B</th><th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #0A2EFE;color:#0A2EFE;font-size: 14px;width:14.00%;">Qwen3.6-27B</th><th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #0A2EFE;color:#0A2EFE;font-size: 14px;width:14.00%;">Qwen3.7-Plus</th><th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #0A2EFE;color:#0A2EFE;font-size: 14px;width:14.00%;">Muse Glimmer-30B</th><th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #0A2EFE;color:#0A2EFE;font-size: 14px;width:14.00%;">Opus4.6 Max</th></tr></thead>
<tbody>
<tr><td colspan="6" style="padding:8px 12px;font-weight:600;color:#0A2EFE;border-bottom:1px solid rgba(10, 46, 254, 0.2);background:#D6DAFC">Agentic Multimodal Intelligence</td></tr>
<tr><td class="benchmark-cell" style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);"><div class="benchmark-capability" style="font-size:15px;font-weight:600;line-height:1.22;color:#171717">Computer use</div><div class="benchmark-name" style="margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B">OSWorld-Verified</div></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);background:rgba(10, 46, 254, 0.08);vertical-align:middle;font-size:15px;line-height:1.2;"><strong>84.3</strong></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">63.9</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">73.3</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">65.9</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">72.7</td></tr>
<tr><td class="benchmark-cell" style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);"><div class="benchmark-capability" style="font-size:15px;font-weight:600;line-height:1.22;color:#171717">Browser use</div><div class="benchmark-name" style="margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B">WebArena-Verified</div></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);background:rgba(10, 46, 254, 0.08);vertical-align:middle;font-size:15px;line-height:1.2;"><strong>64.8</strong></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">48.8</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">55.3</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">--</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">--</td></tr>
<tr><td class="benchmark-cell" style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);"><div class="benchmark-capability" style="font-size:15px;font-weight:600;line-height:1.22;color:#171717">Mobile use</div><div class="benchmark-name" style="margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B">AndroidWorld</div></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);background:rgba(10, 46, 254, 0.08);vertical-align:middle;font-size:15px;line-height:1.2;"><strong>81.9</strong></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">70.3</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">81.0</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">--</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">62.0</td></tr>
<tr><td class="benchmark-cell" style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);"><div class="benchmark-capability" style="font-size:15px;font-weight:600;line-height:1.22;color:#171717">Application recreation</div><div class="benchmark-name" style="margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B">RecreationBench</div></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);background:rgba(10, 46, 254, 0.08);vertical-align:middle;font-size:15px;line-height:1.2;"><strong>47.1</strong></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">29.8</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">30.2</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">--</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">--</td></tr>
<tr><td class="benchmark-cell" style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);"><div class="benchmark-capability" style="font-size:15px;font-weight:600;line-height:1.22;color:#171717">Multimodal tool use</div><div class="benchmark-name" style="margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B">ClawEval-MM</div></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);background:rgba(10, 46, 254, 0.08);vertical-align:middle;font-size:15px;line-height:1.2;"><div class="metric-stack" style="padding:3px 0"><div><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Pass@3</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717"><strong>57.4</strong></div></div><div style="margin-top:7px"><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Average</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717">56.9</div></div></div></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;"><div class="metric-stack" style="padding:3px 0"><div><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Pass@3</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717">42.6</div></div><div style="margin-top:7px"><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Average</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717">50.4</div></div></div></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;"><div class="metric-stack" style="padding:3px 0"><div><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Pass@3</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717"><strong>57.4</strong></div></div><div style="margin-top:7px"><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Average</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717"><strong>60.1</strong></div></div></div></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">--</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;"><div class="metric-stack" style="padding:3px 0"><div><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Pass@3</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717">52.5</div></div><div style="margin-top:7px"><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Average</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717">54.7</div></div></div></td></tr>
<tr><td class="benchmark-cell" style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);"><div class="benchmark-capability" style="font-size:15px;font-weight:600;line-height:1.22;color:#171717">Multimodal software engineering</div><div class="benchmark-name" style="margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B">SWE-MM</div></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);background:rgba(10, 46, 254, 0.08);vertical-align:middle;font-size:15px;line-height:1.2;"><strong>38.6</strong></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">25.7</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">30.0</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">--</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">27.1</td></tr>
<tr><td class="benchmark-cell" style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);"><div class="benchmark-capability" style="font-size:15px;font-weight:600;line-height:1.22;color:#171717">Visual web development</div><div class="benchmark-name" style="margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B">Vision2Web</div></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);background:rgba(10, 46, 254, 0.08);vertical-align:middle;font-size:15px;line-height:1.2;"><strong>62.9</strong></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">45.0</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">42.1</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">--</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">--</td></tr>
<tr><td colspan="6" style="padding:8px 12px;font-weight:600;color:#0A2EFE;border-bottom:1px solid rgba(10, 46, 254, 0.2);background:#D6DAFC">General Multimodal Intelligence</td></tr>
<tr><td class="benchmark-cell" style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);"><div class="benchmark-capability" style="font-size:15px;font-weight:600;line-height:1.22;color:#171717">Visual math problem solving</div><div class="benchmark-name" style="margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B">MathVision</div></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);background:rgba(10, 46, 254, 0.08);vertical-align:middle;font-size:15px;line-height:1.2;"><div class="metric-stack" style="padding:3px 0"><div><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Without CI</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717">90.0</div></div><div style="margin-top:7px"><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">With CI</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717"><strong>94.6</strong></div></div></div></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;"><div class="metric-stack" style="padding:3px 0"><div><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Without CI</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717">85.1</div></div></div></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;"><div class="metric-stack" style="padding:3px 0"><div><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Without CI</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717"><strong>90.3</strong></div></div></div></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">--</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;"><div class="metric-stack" style="padding:3px 0"><div><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Without CI</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717">65.5</div></div></div></td></tr>
<tr><td class="benchmark-cell" style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);"><div class="benchmark-capability" style="font-size:15px;font-weight:600;line-height:1.22;color:#171717">General visual reasoning</div><div class="benchmark-name" style="margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B">BabyVision</div></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);background:rgba(10, 46, 254, 0.08);vertical-align:middle;font-size:15px;line-height:1.2;"><div class="metric-stack" style="padding:3px 0"><div><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Without CI</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717"><strong>65.7</strong></div></div><div style="margin-top:7px"><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">With CI</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717"><strong>85.6</strong></div></div></div></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;"><div class="metric-stack" style="padding:3px 0"><div><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Without CI</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717">28.9</div></div></div></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;"><div class="metric-stack" style="padding:3px 0"><div><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Without CI</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717">64.7</div></div><div style="margin-top:7px"><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">With CI</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717">70.4</div></div></div></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">--</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;"><div class="metric-stack" style="padding:3px 0"><div><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Without CI</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717">12.6</div></div></div></td></tr>
<tr><td class="benchmark-cell" style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);"><div class="benchmark-capability" style="font-size:15px;font-weight:600;line-height:1.22;color:#171717">Scientific chart analysis</div><div class="benchmark-name" style="margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B">CharXiv (RQ)</div></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);background:rgba(10, 46, 254, 0.08);vertical-align:middle;font-size:15px;line-height:1.2;"><div class="metric-stack" style="padding:3px 0"><div><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Without CI</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717">83.7</div></div><div style="margin-top:7px"><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">With CI</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717"><strong>90.2</strong></div></div></div></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;"><div class="metric-stack" style="padding:3px 0"><div><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Without CI</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717">78.4</div></div></div></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;"><div class="metric-stack" style="padding:3px 0"><div><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Without CI</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717"><strong>85.8</strong></div></div><div style="margin-top:7px"><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">With CI</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717">85.9</div></div></div></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">78.8</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;"><div class="metric-stack" style="padding:3px 0"><div><div class="metric-label" style="font-size:10px;font-weight:400;line-height:1.1;color:#777">Without CI</div><div class="metric-value" style="margin-top:2px;font-size:15px;line-height:1.15;color:#171717">66.0</div></div></div></td></tr>
<tr><td class="benchmark-cell" style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);"><div class="benchmark-capability" style="font-size:15px;font-weight:600;line-height:1.22;color:#171717">Document intelligence</div><div class="benchmark-name" style="margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B">OmniDocBench 1.5</div></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);background:rgba(10, 46, 254, 0.08);vertical-align:middle;font-size:15px;line-height:1.2;">91.1</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">89.4</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;"><strong>91.4</strong></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">75.8</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">86.6</td></tr>
<tr><td class="benchmark-cell" style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);"><div class="benchmark-capability" style="font-size:15px;font-weight:600;line-height:1.22;color:#171717">Real-world perception</div><div class="benchmark-name" style="margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B">RealWorldQA</div></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);background:rgba(10, 46, 254, 0.08);vertical-align:middle;font-size:15px;line-height:1.2;">85.9</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">84.1</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;"><strong>86.9</strong></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">--</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">73.9</td></tr>
<tr><td class="benchmark-cell" style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);"><div class="benchmark-capability" style="font-size:15px;font-weight:600;line-height:1.22;color:#171717">Embodied intelligence</div><div class="benchmark-name" style="margin-top:4px;font-size:11px;font-weight:400;line-height:1.2;color:#6B6B6B">ERQA</div></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);background:rgba(10, 46, 254, 0.08);vertical-align:middle;font-size:15px;line-height:1.2;">65.5</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">62.5</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;"><strong>69.8</strong></td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">--</td><td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);vertical-align:middle;font-size:15px;line-height:1.2;">40.8</td></tr>
</tbody>
</table>
<div style="margin-top:12px;font-size:11px;line-height:1.5;color:rgba(0,0,0,0.72)">
<ol style="margin:0;padding-left:20px">
<li>MathVision, BabyVision, and CharXiv (RQ): Where both settings are available, cells report “Without CI” and “With CI” separately; otherwise, only the available setting is shown. A small number of incorrect ground-truth annotations in MathVision and CharXiv (RQ) were corrected following manual verification, and all reported scores on those benchmarks were computed using the corrected annotations.</li>
<li>MathVision: Qwen3.8-27B is evaluated using the fixed prompt: “Please reason step by step, and put your final answer within <code>\boxed{}</code>.” For the remaining models, we report the higher score from two prompt variants—one with and one without the <code>\boxed{}</code> formatting requirement.</li>
<li>WebArena-Verified: Scores are computed with the official WebArena-Verified grader under the OSWorld scaffold.</li>
<li>RecreationBench: An in-house, long-horizon application-recreation benchmark designed to evaluate hybrid-agent capabilities across five platforms: desktop (Ubuntu, macOS, and Windows), mobile (Android), and the web.</li>
<li>ClawEval-MM: Scores are reported as “Pass@3 / average score.” Pass@3 is the percentage of tasks passed in at least one of three trials; the average score is the mean benchmark score across the three trials.</li>
<li>Vision2Web: Scores are averaged across the frontend, webpage, and website categories. Evaluations use the Claude Code harness and are judged by <code>gpt-5.4-2026-03-05</code>.</li>
<li>SWE-MM: Scores are evaluated on the Claude Code harness using the public dev split of SWE-bench Multimodal, with the modifications described in Appendix 8.3 of the Claude Opus 4.7 system card.</li>
<li>Empty cells (--) indicate that results are not yet available or not applicable.</li>
</ol></div>
</div>


## Quickstart

For streamlined integration, we recommend using Qwen3.8 via APIs.

### Serving Qwen3.8

> [!Important]
> Inference efficiency and throughput vary significantly across frameworks. 
> We recommend using the latest framework versions to ensure optimal performance and compatibility.
> For production workloads or high-throughput scenarios, dedicated serving engines such as SGLang, vLLM, or TokenSpeed are recommended.

Qwen3.8 can be deployed with popular inference frameworks, e.g.:

- [SGLang](https://www.sglang.io/): [Qwen3.8 Cookbook](https://docs.sglang.io/cookbook/autoregressive/Qwen/Qwen3.8-27B)
- [vLLM](https://vllm.ai/): [Qwen3.8 Recipe](https://recipes.vllm.ai/Qwen/Qwen3.8-27B)
- [TokenSpeed](https://lightseek.org/tokenspeed/): [Qwen3.8 Recipe](https://lightseek.org/tokenspeed/recipes/models#qwen3-8)


### API Usage

> [!Important]
> Qwen3.8 models operate in thinking mode by default, generating thinking content signified by `<think>\n...</think>\n\n` before producing the final response.
> To disable thinking content and obtain a direct response, refer to the examples [here](#instruct-or-non-thinking-mode).


> [!Tip]
> We recommend using the following sets of sampling parameters for generation:
> - Thinking Mode: `temperature=1.0`, `top_p=0.95`, `top_k=20`, `min_p=0.0`, `presence_penalty=0.0`, `repetition_penalty=1.0`
> - Instruct (or non-thinking) mode: `temperature=0.7`, `top_p=0.80`, `top_k=20`, `min_p=0.0`, `presence_penalty=1.5`, `repetition_penalty=1.0`
>
> Please note that the support for sampling parameters varies according to inference frameworks.


Qwen3.8 comes with official support for `reasoning_effort`, which can be used to adjust reasoning depth and control cost:  
  - `xhigh` (default): for complex tasks demanding thorough analysis
  - `medium`: balancing accuracy and speed
  - `low`: efficient reasoning optimizing for speed and cost


In addition, `preserve_thinking` is enabled by default for all workloads for the best out-of-the-box experience. To disable preserved thinking, refer to the examples [here](#disable-preserved-thinking).

> [!Tip]
> In multi-turn agentic tasks, lower reasoning effort does not always reduce overall task completion time. Although it may produce faster per-turn responses, it can also lead to insufficient analysis, more failures, and repeated retries, which may increase total latency and token consumption.


#### Chat Completions API

The Chat Completions API can be used with most inference frameworks, as well as [Qwen Cloud](https://www.qwencloud.com/).
Before starting, make sure the OpenAI Python SDK is installed and the API key and the API base URL are configured, e.g.:
```shell
pip install -U openai

# Set the following accordingly
export OPENAI_BASE_URL='your-base-url'
export OPENAI_API_KEY='your-api-key'
```

##### Text-Only Input

```python
from openai import OpenAI
# Configured by environment variables
client = OpenAI()

messages = [{"role": "user", "content": "Write a Python function to merge two sorted linked lists."}]

completion = client.chat.completions.create(
    model="Qwen/Qwen3.8-27B",
    messages=messages,
    extra_body={
        "chat_template_kwargs": {
            "enable_thinking": True,  # on by default
            "preserve_thinking": True, # on by default
        },
    },
    reasoning_effort="xhigh",  # xhigh by default; supported levels are xhigh, medium, and low
    stream=True,
    stream_options={"include_usage": True},
)

reasoning_content = ""
answer_content = ""
is_answering = False
print("\n" + "=" * 20 + "Reasoning" + "=" * 20 + "\n")

for chunk in completion:
    if not chunk.choices:
        print("\nUsage:")
        print(chunk.usage)
        continue

    delta = chunk.choices[0].delta

    if hasattr(delta, "reasoning_content") and delta.reasoning_content is not None:
        if not is_answering:
            print(delta.reasoning_content, end="", flush=True)
        reasoning_content += delta.reasoning_content
    elif hasattr(delta, "reasoning") and delta.reasoning is not None:
        if not is_answering:
            print(delta.reasoning, end="", flush=True)
        reasoning_content += delta.reasoning

    if hasattr(delta, "content") and delta.content:
        if not is_answering:
            print("\n" + "=" * 20 + "Answer" + "=" * 20 + "\n")
            is_answering = True
        print(delta.content, end="", flush=True)
        answer_content += delta.content

messages.append({
    "role": "assistant",
    "content": answer_content,
    "reasoning_content": reasoning_content,
    "reasoning": reasoning_content,
})
```


##### Image Input

```python
from openai import OpenAI
# Configured by environment variables
client = OpenAI()

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://qianwen-res.oss-accelerate.aliyuncs.com/Qwen3.5/demo/CI_Demo/mathv-1327.jpg"
                }
            },
            {
                "type": "text",
                "text": "The centres of the four illustrated circles are in the corners of the square. The two big circles touch each other and also the two little circles. With which factor do you have to multiply the radii of the little circles to obtain the radius of the big circles?\nChoices:\n(A) $\\frac{2}{9}$\n(B) $\\sqrt{5}$\n(C) $0.8 \\cdot \\pi$\n(D) 2.5\n(E) $1+\\sqrt{2}$"
            }
        ]
    }
]

chat_response = client.chat.completions.create(
    model="Qwen/Qwen3.8-27B",
    messages=messages,
)
print("Chat response:", chat_response)
```

##### Video Input

```python
from openai import OpenAI
# Configured by environment variables
client = OpenAI()

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "video_url",
                "video_url": {
                    "url": "https://qianwen-res.oss-accelerate.aliyuncs.com/Qwen3.5/demo/video/N1cdUjctpG8.mp4"
                }
            },
            {
                "type": "text",
                "text": "How many porcelain jars were discovered in the niches located in the primary chamber of the tomb?"
            }
        ]
    }
]

chat_response = client.chat.completions.create(
    model="Qwen/Qwen3.8-27B",
    messages=messages,
)

# When vLLM is launched with `--media-io-kwargs '{"video": {"num_frames": -1}}'`,
# video frame sampling can be configured via `extra_body` (e.g., by setting `fps`).
# This feature is currently supported only in vLLM.
#
# By default, `fps=2` and `do_sample_frames=True`.
# With `do_sample_frames=True`, you can customize the `fps` value to set your desired video sampling rate.
# chat_response = client.chat.completions.create(
#     model="Qwen/Qwen3.8-27B",
#     messages=messages,
#     extra_body={
#         "mm_processor_kwargs": {"fps": 2, "do_sample_frames": True},
#     }, 
# )

print("Chat response:", chat_response)
```


##### Instruct (or Non-Thinking) Mode

Qwen3.8-27B will think by default before responding.
You can obtain a direct response from the model without thinking by configuring the API parameters. 
For example,
```python
from openai import OpenAI
# Configured by environment variables
client = OpenAI()

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://qianwen-res.oss-accelerate.aliyuncs.com/Qwen3.5/demo/RealWorld/RealWorld-04.png"
                }
            },
            {
                "type": "text",
                "text": "Where is this?"
            }
        ]
    }
]

chat_response = client.chat.completions.create(
    model="Qwen/Qwen3.8-27B",
    messages=messages,
    temperature=0.7,
    top_p=0.8,
    presence_penalty=1.5,
    extra_body={
        "top_k": 20,
        "chat_template_kwargs": {"enable_thinking": False},
    }, 
)
print("Chat response:", chat_response)
```

> [!Note]
> If you are using APIs from Qwen Cloud, in addition to changing `model`, please use `"enable_thinking": False` instead of `"chat_template_kwargs": {"enable_thinking": False}`.


##### Disable Preserved Thinking


By default, Qwen3.8 retains thinking blocks from all historical messages, maintaining a complete reasoning trace across the conversation. This behavior, known as preserved thinking, ensures full context continuity and is especially beneficial for agent scenarios where decision consistency and reduced redundant reasoning are critical. It also improves KV cache utilization, optimizing inference efficiency in both thinking and non-thinking modes.

If you prefer to retain only the thinking blocks from the latest user message, you can disable this behavior by setting `preserve_thinking` to `False`:

```python
from openai import OpenAI

# Configured by environment variables
client = OpenAI()
messages = [...]
chat_response = client.chat.completions.create(
    model="Qwen/Qwen3.8-27B",
    messages=messages,
    extra_body={
        "chat_template_kwargs": {"preserve_thinking": False},
    },
)
print("Chat response:", chat_response)
```

> [!Note]
> If you are using APIs from Qwen Cloud, in addition to changing `model`, please use `"preserve_thinking": False` directly instead of wrapping it in `chat_template_kwargs`.


## Best Practices

To achieve optimal performance, we recommend the following settings:

1. **Sampling Parameters**: We suggest using the following sets of sampling parameters:  
    
    - Thinking Mode: `temperature=1.0`, `top_p=0.95`, `top_k=20`, `min_p=0.0`, `presence_penalty=0.0`, `repetition_penalty=1.0`
    - Instruct (or non-thinking) mode: `temperature=0.7`, `top_p=0.80`, `top_k=20`, `min_p=0.0`, `presence_penalty=1.5`, `repetition_penalty=1.0`
    
    For supported frameworks, you can adjust the `presence_penalty` parameter between 0 and 2 to reduce endless repetition. However, using a higher value may occasionally result in language mixing and a slight decrease in model performance.

2. **Adequate Output Length**: To optimize performance on agentic tasks, we recommend allocating sufficient output length to allow the model to generate detailed and comprehensive responses. For frameworks that support separate token limits for internal reasoning and final outputs, we suggest the following configuration within the 1M context length:
    
    - Reasoning Content: Set the maximum output length to 262,144 tokens.
    - Final Response: Set the maximum output length to 131,072 tokens.

    These settings provide the necessary capacity for complex reasoning while ensuring ample space for high-quality final deliverables.

3. **Processing Ultra-Long Texts**: Qwen3.8-27B natively supports context lengths of up to 262,144 tokens. For long-horizon tasks where the total length (including both input and output) exceeds this limit, we recommend using RoPE scaling techniques to handle long texts effectively, e.g., YaRN.

    YaRN is currently supported by several inference frameworks, e.g., vLLM, SGLang, and TokenSpeed. 
    In general, there are two approaches to enabling YaRN for supported frameworks:

    - Modifying the model configuration file:
        
        In the `config.json` file, change the `rope_parameters` fields in `text_config` to:
        ```json
        {
            "mrope_interleaved": true,
            "mrope_section": [
                11,
                11,
                10
            ],
            "rope_type": "yarn",
            "rope_theta": 10000000,
            "partial_rotary_factor": 0.25,
            "factor": 4.0,
            "original_max_position_embeddings": 262144,
        }
        ```

    - Passing command line arguments:

        For vLLM, you can use
        ```shell
        VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 vllm serve ... --hf-overrides '{"text_config": {"rope_parameters": {"mrope_interleaved": true, "mrope_section": [11, 11, 10], "rope_type": "yarn", "rope_theta": 10000000, "partial_rotary_factor": 0.25, "factor": 4.0, "original_max_position_embeddings": 262144}}}' --max-model-len 1000000  
        ```

        For SGLang, you can use
        ```shell
        SGLANG_ALLOW_OVERWRITE_LONGER_CONTEXT_LEN=1 python -m sglang.launch_server ... --json-model-override-args '{"text_config": {"rope_parameters": {"mrope_interleaved": true, "mrope_section": [11, 11, 10], "rope_type": "yarn", "rope_theta": 10000000, "partial_rotary_factor": 0.25, "factor": 4.0, "original_max_position_embeddings": 262144}}}' --context-length 1000000
        ```

        For TokenSpeed, you can use
        ```shell
        TOKENSPEED_ALLOW_OVERWRITE_LONGER_CONTEXT_LEN=1 tokenspeed serve ... --hf-overrides '{"text_config": {"rope_parameters": {"mrope_interleaved": true, "mrope_section": [11, 11, 10], "rope_type": "yarn", "rope_theta": 10000000, "partial_rotary_factor": 0.25, "factor": 4.0, "original_max_position_embeddings": 262144}}}' --max-model-len 1000000  
        ```
    
    > [!NOTE]
    > All the notable open-source frameworks implement static YaRN, which means the scaling factor remains constant regardless of input length, **potentially impacting performance on shorter texts.**
    > We advise modifying the `rope_parameters` configuration only when processing long contexts is required. 
    > It is also recommended to modify the `factor` as needed. For example, if the typical context length for your application is 524,288 tokens, it would be better to set `factor` as 2.0. 


4. **Long Video Understanding**: To optimize inference efficiency for plain text and images, the `size` parameter in the released `video_preprocessor_config.json` is conservatively configured. It is recommended to set the `longest_edge` parameter in the video_preprocessor_config file to 469,762,048 (corresponding to 224k video tokens) to enable higher frame-rate sampling for hour-scale videos and thereby achieve superior performance. For example,
    ```json
    {"longest_edge": 469762048, "shortest_edge": 4096}
    ```

    Alternatively, override the default values via engine startup parameters. For implementation details, refer to: [vLLM](https://github.com/vllm-project/vllm/pull/34330) / [SGLang](https://github.com/sgl-project/sglang/pull/18467).


## Citation

If you find our work helpful, feel free to give us a cite.


```bibtex
@misc{qwen38,
    title = {{Qwen3.8-Max}: A New Bar for Coding and Cowork},
    url = {https://qwen.ai/blog?id=qwen3.8},
    author = {{Qwen Team}},
    month = {August},
    year = {2026}
}
```

---

<h2>EXAMPLE GENERATION(S):</h2>

Q4KS, non imatrix, standard Qwen settings, NO cache compression of any kind.

NOTE: Some formatting may be lost on copy/paste/export.

---

<style type="text/css">
		@page { size: 21cm 29.7cm; margin: 2cm }
		p { line-height: 115%; margin-bottom: 0.25cm; background: transparent }
		h1 { margin-bottom: 0.21cm; background: transparent; page-break-after: avoid }
		h1.western { font-family: "Liberation Serif", serif; font-weight: bold; font-size: 24pt }
		h1.cjk { font-size: 24pt; font-family: "NSimSun"; font-weight: bold }
		h1.ctl { font-family: "Arial"; font-size: 24pt; font-weight: bold }
		h2 { margin-top: 0.35cm; margin-bottom: 0.21cm; background: transparent; page-break-after: avoid }
		h2.western { font-family: "Liberation Serif", serif; font-weight: bold; font-size: 18pt }
		h2.cjk { font-size: 18pt; font-family: "NSimSun"; font-weight: bold }
		h2.ctl { font-family: "Arial"; font-size: 18pt; font-weight: bold }
		td p { orphans: 0; widows: 0; background: transparent }
		th p { font-weight: bold; text-align: center; orphans: 0; widows: 0; background: transparent }
		strong { font-weight: bold }
		em { font-style: italic }
		a:link { color: #000080; text-decoration: underline }
		a:visited { color: #800000; text-decoration: underline }
	</style>

---

<br/>
Example #1 of 4, using “xhigh” (default reasoning)</p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm">This is about 1/3 to
½ the size of normal output.<br/>
<br/>
Example #2, same prompt
[below], but at “medium”.</p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm">---</p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm"><b>PROMPT:<br/>
<br/>
Explain
10 ways (in extensive detail) to use the &quot;night&quot; time
cooling of radiant energy into space to reduce global temperatures.</b></p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p><span style="display: inline-block; border: none; padding: 0cm"><font color="#c9211e"><b>Thought
for 1 minutes 28 seconds</b></font></span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">We
need answer user: &quot;Explain 10 ways (in extensive detail) to use
the 'night' time cooling of radiant energy into space to reduce
global temperatures.&quot; Need interpret: nighttime cooling via
thermal radiation to space, passive radiative cooling, perhaps
enhancement. Need give 10 ways in extensive detail. We need ensure
scientifically accurate, maybe distinguish passive radiative cooling,
selective emitters, sky windows, materials, geometry, location,
systems, urban/industrial/agricultural, refrigeration, power, carbon
capture, etc. Need discuss feasibility, mechanisms, caveats: Earth
emits in mid-IR; atmosphere has window 8-13 microns; radiative
cooling to sky possible when surface/emitter cooler than effective
radiating temp, requires selective spectral emissivity high in sky
window and low/reflective elsewhere to minimize solar/IR absorption;
works best clear nights, low humidity, low wind, high altitude. We
should not overclaim. Need 10 ways maybe: (1) passive radiative
cooling materials for buildings; (2) architectural coatings and
membranes; (3) nighttime cooling towers/heat sinks for data
centers/industrial; (4) radiative chillers/refrigeration; (5)
district cooling networks with radiative coolers; (6) agricultural
cold storage and evaporative/condensing? Maybe use to cool water? (7)
enhanced space radiative cooling with selective emitters at large
scale (engineered surfaces or films) to increase planetary
albedo/emissivity? (8) nighttime thermal storage: cool materials by
night, store thermal energy/cold for daytime; (9) integration with
solar-thermal or solar-electric plants: nighttime radiative cooling
of heat exchangers to increase efficiency and reduce thermal
pollution; (10) urban heat island mitigation and microclimate (cool
pavements, roofs, facades); maybe &quot;cooling the land via
engineered materials in arid regions&quot;. Also (maybe) &quot;radiative
cooling of atmospheric water vapor / condensation&quot;? Use
condensation? Or &quot;cooling the ocean?&quot; Might be too
speculative.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
explain &quot;night time cooling of radiant energy into space&quot;
perhaps as a method: increase emission of infrared radiation to outer
space during nights, lowering surface temperature. Need 10 ways in
detail. We can organize.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Potential
ways:</span></p>
<ol>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Passive
	radiative cooling coatings for roofs/walls: use selective emitters
	(e.g., BaSO4, polymer films with micro/nanostructures, multilayer
	dielectric films) high emissivity in 8-13 μm sky window and high
	solar reflectance; reduces roof temp, indoor cooling load; deployed
	globally in cities.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Large-area
	radiative cooling membranes over buildings/infrastructure: tents,
	awnings, cool roofs with air gaps; airflow, ventilation; cooling
	effect at night and day; can reduce urban heat island.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Night-time
	radiative chillers for refrigeration/air conditioning: emitter
	panels with heat exchangers and fans; cool water or air below
	ambient using sky as heat sink; integrated with evaporative or
	desiccant dehumidification; data centers, hospitals, cold storage.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative
	cooling for district cooling and industrial process cooling:
	centralized rooftop/field radiative coolers that transfer process
	waste heat to sky; paired with heat pumps or absorption chillers;
	reduce fossil-fuel cooling.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Thermal
	energy storage: store &quot;cold&quot; or pre-cooled materials/phase
	change materials at night via radiative cooling; use for daytime
	cooling; combined with PCM, latent heat; reduce peak load and AC
	energy.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Enhance
	planetary radiative cooling with engineered surfaces/land cover: in
	high-altitude arid regions, deploy large fields of selective
	emitters or reflective white surfaces that emit in atmospheric
	window to increase outgoing longwave radiation; evaluate albedo,
	ecosystem, hydrology impacts.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cool
	pavements and transportation infrastructure: radiatively cooling
	asphalt/concrete substitutes, road surfaces, parking lots; reduces
	heat stored in pavement and lowers vehicle fuel/AC consumption;
	especially in sunny, clear-sky areas.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative
	cooling for agriculture: cooling seed stores, livestock housing,
	greenhouses, vineyards/orchards; night cooling to prevent heat
	stress, reduce spoilage; using selective emitters on roofs or sheds;
	can also manage condensation.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Solar
	power and solar thermal efficiency: cool PV panels by night/day
	using radiative surfaces (backsheet, coatings) and heat pipes;
	reduces module temperature and increases efficiency; cool heat
	exchangers in solar thermal; maybe reduce thermal stratification.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Data
	centers and electronics cooling: dedicated radiative cooling panels
	as low-energy heat rejection for servers; nocturnal operation with
	fans and heat exchangers; reduces PUE and water use. Alternative:
	&quot;Cooling seawater for carbon capture/thermal storage&quot;?
	Need 10. Could include &quot;Cooling oceans via selective emitters?&quot;
	not realistic. Could include &quot;use to assist
	condensation/humidification?&quot; We can mention radiative cooling
	can condense moisture; but user asks reduce global temperatures.
	Need focus.</span></p></li>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
maybe mention fundamental physics:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Earth
	radiates ~390 W/m²; sky emits ~200 W/m²; net radiative cooling
	depends on temperature difference; cooling power = εσ(T_s^4 -
	T_sky^4) minus absorbed IR and convective; sky window 8-13 μm.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">To
	maximize: high emissivity in 8-13 μm, high solar reflectance
	(10-2500 nm), minimize convective/absorbed heat; clear skies, high
	altitude, low humidity; night operation best.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
&quot;extensive detail&quot; maybe each way with mechanisms, design,
implementation, quantification examples, challenges.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
ensure not misleading: &quot;reduce global temperatures&quot; not
instant; local and system-level; global effect if large-scale
adoption; could be a small fraction. We can say can contribute to
demand-side mitigation, reducing fossil fuel emissions from cooling,
but direct global cooling depends on large area.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
maybe include &quot;night-time&quot; specific: all methods can be
operated/optimized at night. Some are passive (continuous). Could
mention:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Passive
	roofs: cool at night via radiative cooling, lower indoor temp.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative
	cooling towers: at night, radiative cooling of water below ambient;
	day still useful if selective and reflective, but night better.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Solar-thermal:
	store heat in high temp? Wait use radiative cooling to reject waste
	heat and increase cycle efficiency, but not directly lower ambient.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Use
	&quot;night-time radiative cooling as an auxiliary refrigerant&quot;
	by cooling heat exchanger fluid, driving absorption chiller.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Use
	&quot;radiative cooling to produce cold for ice-making&quot; in
	developing regions.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Potential
10 in more nuanced way:</span></p>
<ol>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Passive
	radiative cool roofs with selective emitters.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Active
	radiative cooling systems (fan-assisted) for building HVAC.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative
	chillers and absorption/heat-pump assisted cooling for
	process/refrigeration.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">District
	cooling networks using centralized radiative heat rejection.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Night-time
	cold storage and phase-change thermal storage.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Large-scale
	landscape-level radiative cooling deployments (engineered emitters)
	in suitable regions.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative-cooled
	pavements/roads/infrastructure for urban heat island mitigation.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Agricultural
	cooling (greenhouses, livestock, cold chain) using radiative
	cooling.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative
	cooling of solar PV/thermal collectors to improve efficiency and
	reduce thermal load.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Data
	center/electronics radiative cooling and night-time heat rejection.</span></p></li>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
perhaps separate &quot;radiative cooling membranes/films&quot; and
&quot;coatings&quot;. Could combine. Need ensure 10 distinct.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Maybe
include &quot;cooling water bodies/evaporation&quot; or &quot;radiative
cooling to enhance ocean-atmosphere exchange&quot;? Hmm.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Let's
design final answer: intro with physics. Then 10 sections. For each:
concept, how it works, detailed implementation, quantitative
potential, key challenges.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
answer not too short. Oververbosity 9: thorough. Need be careful with
scientific terms.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Let's
draft in mind.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Intro:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative
	cooling: any body with T &gt; environment emits thermal radiation;
	if emissivity high in atmospheric transparency window (8-13 μm), it
	can radiate to cold outer space; at night, effective sky temp ~-40
	to -70 C or radiative heat flux can be 50-150 W/m² under clear
	skies; selective surfaces can be 10-30 C below ambient.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Requirements:
	high IR emissivity in 8-13 μm; high reflectance in solar 300-2500
	nm; low thermal conductance or airflow; clear, dry, high-altitude
	climates best.</span></p></li>
</ul>
<ol>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Passive
	radiative cool roofs/facades.</span></p></li>
</ol>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Materials:
	multilayer dielectric films, BaSO4/polymer, micro-nanostructured
	photonic crystals, ceramic composites.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Mechanism:
	emits in sky window, reflects sunlight; reduces roof temp by 10-30
	C; reduces HVAC.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Deployment:
	roofing membranes, tiles, paints, cool glass; cost-effective; reduce
	building energy demand and urban heat.</span></p></li>
</ul>
<ol start="2">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative-cooled
	building envelopes and membranes with airflow.</span></p></li>
</ol>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Use
	panels/tarps with air gaps, louvers, night vents; passive stack
	effect; night purging.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Mechanism:
	cool shell at night; daytime insulation; lower indoor temp;
	especially hot-arid.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Detailed:
	double-skin roofs, ventilated facades, cool awnings; sensors
	controlling vents; reduce peak heat gains.</span></p></li>
</ul>
<ol start="3">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Active
	radiative chillers for air conditioning/refrigeration.</span></p></li>
</ol>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Components:
	selective emitter, heat exchanger, water/air circuit, fans,
	sometimes heat pump/absorption.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Mechanism:
	pump warm fluid from indoor coils to emitter; emitter radiates heat
	to sky; can cool fluid below ambient at night; drive AC or store
	cold.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Example:
	roof-top units; 20-50 W/m² cooling at night; can offset 50-100% AC
	in mild climates.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Integration:
	desiccant dehumidification to manage humidity; hybrid with
	evaporative cooling.</span></p></li>
</ul>
<ol start="4">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">District
	cooling and industrial waste-heat rejection via radiative coolers.</span></p></li>
</ol>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Central
	plant radiative cooling fields (emitter arrays, cooling towers) at
	night; connect to district cooling loops; industrial process cooling
	(plastics, food, chemical, data centers).</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Use
	low-grade heat; reduce chiller electricity; night operation shifts
	load.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Large
	area: thousands of m²; use in sunny arid cities; potential kW-MW.</span></p></li>
</ul>
<ol start="5">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Night-time
	cold storage and phase-change thermal storage.</span></p></li>
</ol>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cool
	PCM or water at night via radiative emitters; store thermal energy
	as cold; release next day.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Example:
	paraffin/eutectic salts at 5-25 C; insulated tanks with radiative
	coolers; provide pre-cooling for buildings, cold rooms.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Use
	for peak shaving and resilience; reduces AC runtime and grid
	emissions.</span></p></li>
</ul>
<ol start="6">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Large-scale
	land-based radiative cooling deployments.</span></p></li>
</ol>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Install
	selective emitter arrays on rooftops, deserts, high plateaus;
	increase outgoing longwave radiation through atmospheric window.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Mechanism:
	more of surface heat emitted to space; lower surface/albedo? Need
	reflect solar too.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Challenges:
	land use, ecosystem, water, wind; requires governance; can reduce
	urban heat island and local warming; global effect small but could
	matter with millions km².</span></p></li>
</ul>
<ol start="7">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative-cooled
	pavements/roads and transport infrastructure.</span></p></li>
</ol>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Use
	cool pavement coatings, aggregates, membranes with high 8-13 μm
	emissivity and high solar reflectance; cool roads/parking lots;
	reduce heat stored and reradiated; lower vehicle fuel/AC; reduce
	UHI.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Deployment:
	parking lots, highways, airport aprons; use in hot regions;
	integrate with drainage.</span></p></li>
</ul>
<ol start="8">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Agricultural
	cooling and cold chain.</span></p></li>
</ol>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Use
	radiative cooling shelters for livestock, poultry, greenhouses,
	produce storage; night cooling of barns; reduce heat stress,
	mortality, spoilage; lower refrigeration energy.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Details:
	insulated barn roofs with emitter panels; cold storage warehouses
	with radiative chiller; dew management; integration with
	dehumidification.</span></p></li>
</ul>
<ol start="9">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative
	cooling of solar PV/thermal systems.</span></p></li>
</ol>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Use
	cool backsheets, selective emitter panels behind PV, heat pipes;
	cool modules by day/night; reduce PV cell temperature; improve
	efficiency; for solar-thermal, use radiative coolers as night-time
	heat sinks to recover energy and reduce thermal losses.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Could
	include concentrating solar: radiatively cool mirrors/absorbers at
	night to improve next-day startup; reduce parasitic cooling.</span></p></li>
</ul>
<ol start="10">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Data
	center/electronics radiative cooling.</span></p></li>
</ol>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Dedicated
	radiative cooling panels as heat exchangers; night-time operation;
	fans; chilled water loops; reduce PUE and water use; especially in
	data centers in dry climates; can use free cooling to reject server
	heat.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Integration
	with liquid cooling, immersion tanks, free-air cooling; use during
	nights to pre-cool thermal storage.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Could
also add &quot;radiative cooling of condensation/evaporation cycles&quot;?
But already 10. Need maybe mention &quot;global temperature
reduction&quot; tie-in for each.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
also caveats:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative
	cooling is a cooling method, not a replacement for emission
	reductions; can reduce cooling demand, but if powered by fossil grid
	may offset.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Requires
	selective spectral properties; if it absorbs too much IR or
	convective heat, not cool.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Night-time:
	clear skies and low humidity; performance degrades under clouds; use
	storage/hybrid systems.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Large-scale:
	land use, water, ecology, governance, feedbacks (clouds, moisture),
	feedbacks with albedo.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
maybe include sample calculations:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">If
	a 1000 m² roof with 150 W/m² radiative cooling: 150 kW thermal.
	Could offset 100 kW AC? 1 ton = 3.5 kW; 150 kW = ~43 tons. But
	cooling power depends.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">For
	a 100 m² house, 50 W/m² = 5 kW = 1.4 tons; significant at night.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
maybe answer &quot;Explain 10 ways (in extensive detail)&quot; with
maybe bullet/numbered. Ensure extensive detail for each. Could be
long. We'll do that.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
check if user wants &quot;night time cooling of radiant energy into
space&quot; maybe &quot;use the night-time cooling of radiant energy
into space&quot; meaning &quot;use the fact that radiant energy can
be lost into space at night&quot;. Yes.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Let's
refine each section for accuracy:</span></p>
<ol>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Passive
	radiative cool roofs:</span></p></li>
</ol>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Mechanism:
	material emits thermal IR; high emissivity in 8-13 μm; sky is cold
	sink; at night, surface T can drop below ambient. Solar reflectance
	avoids daytime heating. It can also reduce daytime temp if emitter
	cools.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Use:
	white/reflective paints with micro/nanostructures; ceramic powders;
	polymer films.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Impact:
	reduce HVAC, urban heat.</span></p></li>
</ul>
<ol start="2">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative-cooled
	building skins, ventilated cavities:</span></p></li>
</ol>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Add
	air gap between interior and emitter; night stack ventilation; use
	louvers; reduce heat conduction into building.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Could
	use &quot;cooling blankets&quot; or membranes for existing
	buildings; retrofit.</span></p></li>
</ul>
<ol start="3">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Active
	radiative chillers for HVAC:</span></p></li>
</ol>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Use
	fans to enhance heat transfer to emitter; heat exchanger
	(water/glycol) collects heat from indoor cooling coils. Emitter
	radiates to sky. At night can get below ambient; drive chiller. Need
	dehumidification.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Example:
	roof unit with 10 m² emitter can produce ~3-10 kW cooling.</span></p></li>
</ul>
<ol start="4">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">District
	cooling/industrial:</span></p></li>
</ol>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Large
	fields of radiative panels/cooling towers; central plant; supply
	chilled water; night pre-cooling; use for hospitals, factories;
	shift cooling to off-peak.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Use
	waste heat from processes; reduce chiller electricity and water.</span></p></li>
</ul>
<ol start="5">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Thermal
	storage:</span></p></li>
</ol>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Use
	radiative coolers to cool water tanks or PCM at night; store cold;
	discharge in day; can supply pre-cooling to AHUs, radiant ceilings,
	chilled beams; can make ice in hot climates.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Integration:
	thermal batteries; reduce peak grid use.</span></p></li>
</ul>
<ol start="6">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Large-scale
	land-based radiative cooling arrays:</span></p></li>
</ol>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Selective
	emitters on large flat roofs or open land; increase outgoing
	longwave radiation; reduce surface temp; can reduce UHI and local
	atmospheric heat.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
	careful: not just white paint; must be emissive in sky window; avoid
	moisture issues; consider local ecology, albedo; possible climate
	engineering but limited.</span></p></li>
</ul>
<ol start="7">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Pavements/roads:</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cool
	road coatings with high emissivity; reduce pavement temperature;
	less heat re-radiated to air; lower vehicle fuel and AC; reduce
	stormwater heat; use in urban corridors.</span></p></li>
</ul>
<ol start="8">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Agriculture/cold
	chain:</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative
	cooling shelters for animals; cooling of produce; greenhouse roofs
	with emitter panels; night cooling; reduce refrigeration; in hot dry
	areas; manage condensation.</span></p></li>
</ul>
<ol start="9">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Solar
	energy:</span></p></li>
</ol>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cool
	PV modules: emitter backsheets; heat pipes; lower cell temperature,
	increase efficiency; for solar thermal: use radiative cooling to
	pre-cool absorbers or store heat at night? Need phrase: at night,
	use radiative cooler to reject heat from solar-thermal loops to sky;
	can keep thermal storage at higher temperature by night? Wait if you
	reject heat, it cools storage; but you can use radiative cooling to
	increase heat sink temperature difference? Let's think.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">In
	solar thermal, cooling the heat sink can increase net solar heat
	gain. If you cool the collector/heat exchanger at night via
	radiative cooling, then next day you have lower starting temp, more
	ΔT, more energy collected. Also can use radiative cooling as a
	passive heat rejection system for waste heat in industrial or
	cooling systems.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">For
	data centers maybe separate.</span></p></li>
</ul>
<ol start="10">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Data
	centers/electronics:</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Use
	radiative cooling panels as heat exchangers to reject server waste
	heat; night free cooling; can cool immersion tanks, chilled water
	loops; reduce PUE and water; especially in dry climates.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
perhaps differentiate 3 and 10 (both HVAC/data center). But one is
general building HVAC, one is high-density electronics. Fine.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Could
add &quot;cooling water for evaporative cooling&quot;? Maybe not.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
perhaps include &quot;cooling seawater for desalination?&quot; Not
necessary.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
maybe include &quot;cooling to condense water vapor and use as
desiccant&quot;? It uses radiative cooling to produce cold for
dehumidification, reducing indoor cooling. But it's more system
integration.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Potential
alternate 10: (a) roofs, (b) walls/facades, (c) membranes, (d) data
centers, (e) industrial, (f) district cooling, (g) cold storage, (h)
agriculture, (i) roads, (j) large-scale arrays. That's clear.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
include formulas: Q_rad = εσA(T_surface^4 - T_sky^4), with T_sky ~
150-250 K effective? Actually sky temp depends; in clear night T_sky
~ 150-250 K; cooling power can be 50-150 W/m². Use safe ranges.
Mention that if surface T less than air temp, it's still radiating
more to space than receiving due to spectral window.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
maybe mention &quot;emissivity in atmospheric window&quot; and &quot;solar
reflectance&quot; details.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Let's
craft final: Title, intro, then numbered items.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
be careful with &quot;global temperatures&quot;: we can state &quot;If
widely deployed, these reduce energy demand for cooling and increase
heat rejection to space; individually local, collectively can lower
human-caused warming&quot;.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
maybe include &quot;night-time&quot; as operating mode: for each, say
&quot;night-time operation&quot; and how.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Let's
write with high detail:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Intro:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Physics:
	Earth/surfaces emit longwave IR; atmosphere mostly opaque but has
	8-13 μm window; selective materials can radiate through; night sky
	is radiative sink; cooling power depends on emissivity, temperature
	difference, sky clearness, humidity, wind.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">To
	exploit: high 8-13 μm emissivity, high solar reflectance, minimize
	convective/absorbed heat; deploy where clear nights and dry air.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Then
10:</span></p>
<ol>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Passive
	radiative cool roofs and façades</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Explanation,
	design, examples, potential, challenges.</span></p></li>
</ul>
<ol start="2">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative-cooled
	building envelopes and air-gapped membranes</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Explanation:
	double skin, ventilated cavities, night purge; materials; effect.</span></p></li>
</ul>
<ol start="3">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative
	chillers for building air conditioning</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Explanation:
	active units with heat exchangers; fluid loop; night sub-ambient
	cooling; integration with AHUs, chilled beams; sizing; performance;
	issues with humidity.</span></p></li>
</ul>
<ol start="4">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">District
	cooling and industrial heat-rejection fields</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Explanation:
	central radiative cooling plants, large emitters; connect to
	district loop; night pre-cooling; industrial process heat; reduce
	chiller electricity.</span></p></li>
</ul>
<ol start="5">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Night-time
	cold storage and phase-change thermal storage</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Explanation:
	cool water/PCM with radiative emitters at night; use next day;
	reduce peak cooling; ice-making; backup.</span></p></li>
</ul>
<ol start="6">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Large-scale
	land-based radiative cooling installations</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Explanation:
	large arrays of selective emitters on rooftops/land; increase
	outgoing longwave radiation; reduce local/urban heat; climate
	considerations; governance.</span></p></li>
</ul>
<ol start="7">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative-cooled
	pavements, roads, and transportation surfaces</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Explanation:
	cool pavement with high emissivity; reduces heat storage; lower UHI;
	vehicle energy savings; airports/parking lots.</span></p></li>
</ul>
<ol start="8">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Agricultural,
	greenhouse, and livestock cooling</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Explanation:
	cool barns, greenhouses, cold rooms; reduce heat stress and
	spoilage; night operation; condensation control.</span></p></li>
</ul>
<ol start="9">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative
	cooling for solar power and solar thermal systems</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Explanation:
	cool PV modules/backsheets; heat pipes; reduce cell temp; for solar
	thermal pre-cooling of collectors; improves efficiency; reduces
	cooling energy.</span></p></li>
</ul>
<ol start="10">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Data-center
	and electronics radiative cooling</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Explanation:
	dedicated panels, immersion cooling, free cooling at night; reduce
	PUE/water; integration with liquid loops; in dry climates.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
include for each: &quot;How to use night-time cooling&quot; and
&quot;impact&quot;.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Let's
ensure each is extensive but not repetitive. Could include design
specifics, sizing examples. Need not be too massive but user wants
extensive detail. We'll aim about 3000-4500 words? Maybe less. But
oververbosity 9, detailed.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Let's
draft in final.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
perhaps include note: &quot;Some are direct (increase cooling load
offset) and some are indirect (reduce emissions from cooling)&quot;.
Good.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Potential
issue: &quot;use the 'night' time cooling of radiant energy into
space&quot; maybe they might ask for 10 ways to use the phenomenon to
reduce global temperatures (like solar reflectors, high altitude
emitters?). We can mention &quot;large-scale engineered radiative
cooling surfaces&quot; and &quot;cooling high-altitude or arid land&quot;.
But avoid unrealistic.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Maybe
add &quot;high-altitude radiative cooling platforms&quot;? That would
be interesting but maybe too speculative. Could include as one of 10?
But better stick to practical.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Let's
think of possible direct global temperature effects:</span></p>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Increase
	planetary albedo? Radiative cooling at night is not albedo; but can
	increase net radiative loss if material is cooler and emissive. On
	Earth, outgoing longwave radiation already around 240 W/m².
	Increasing it via surface changes is hard due to atmospheric window
	limited. Large-scale selective emitters could slightly increase OLR.
	We can mention as a small geoengineering possibility but with
	governance.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
maybe mention &quot;cloud and humidity effects&quot; as caveat.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Let's
ensure each is a distinct method, not just application. The question
likely wants 10 ways. We can phrase:</span></p>
<ol>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Passive
	radiative cooling roofs</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Active
	radiative cooling HVAC systems</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative-cooled
	district cooling loops</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative-cooled
	industrial process heat rejection</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative-cooled
	thermal storage (cold storage)</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative-cooled
	pavements/roads</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative-cooled
	agriculture/cold chain</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative-cooled
	solar PV/thermal collectors</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative-cooled
	data centers/electronics</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Large-scale
	land-based radiative cooling arrays (geophysical/urban heat
	mitigation) This is clear.</span></p></li>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
maybe combine 2 and 3? But distinct enough.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Let's
refine each:</span></p>
<ol>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Passive
	radiative cool roofs:</span></p></li>
</ol>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Use
	materials with photonic bandgap, high emissivity in 8-13 μm. At
	night, roof radiates heat through window. Solar reflectance prevents
	heating. Example: 100 m² roof at 30 W/m² = 3 kW = 1 ton. Reduces
	HVAC.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Implementation:
	cool paint, membrane, tiles. Cost, durability, reflectivity.</span></p></li>
</ul>
<ol start="2">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Active
	radiative cooling HVAC:</span></p></li>
</ol>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Fans
	and heat exchangers; fluid loop; emitter panel; can cool water below
	ambient. Night-time operation. Use as primary or supplemental
	cooling. Need humidity. Sizing: 50 m² panel can yield ~10-30 kW
	depending.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Integration:
	air handling units, radiant ceilings, chilled water.</span></p></li>
</ul>
<ol start="3">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">District
	cooling/industrial:</span></p></li>
</ol>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Central
	plant with large radiative cooling fields; night pre-cooling of
	district loop; reduce peak chiller use. Industrial: reject waste
	heat from plastic/chemical/food.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Large
	area: 10,000 m² can produce MW-scale.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Use
	where space and clear sky.</span></p></li>
</ul>
<ol start="4">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Night-time
	cold storage:</span></p></li>
</ol>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative
	coolers cool water tanks/PCM at night; store cold; use next day;
	reduces peak load and makes ice.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Design:
	insulated tanks, selective emitters, fans, pumps, control.</span></p></li>
</ul>
<ol start="5">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Pavements/roads:</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cool
	road coatings with high emissivity; reduce stored heat; lower
	ambient around roads; reduce vehicle cooling; use in hot areas;
	reflectivity and skid resistance.</span></p></li>
</ul>
<ol start="6">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Agriculture/cold
	chain:</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cool
	livestock barns, poultry houses, greenhouses, warehouses; night
	cooling of produce; reduce spoilage; use passive radiative roofs;
	integrate with dehumidification.</span></p></li>
</ul>
<ol start="7">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Solar
	power/thermal:</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cool
	PV modules via emitter backsheets, heat pipes, or airflow; lower
	cell temp, increase efficiency. For solar thermal, pre-cool
	collectors and reject heat to sky at night to increase ΔT next day;
	reduce parasitic cooling.</span></p></li>
</ul>
<ol start="8">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Data
	centers/electronics:</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative
	cooling panels as heat sinks; cool liquid loops; night free cooling;
	reduce PUE and water; especially in arid regions; integrate with
	immersion tanks.</span></p></li>
</ul>
<ol start="9">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Large-scale
	land-based radiative cooling arrays:</span></p></li>
</ol>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Deploy
	selective emitters on large flat surfaces; increase OLR through
	atmospheric window; reduce surface temp and local air temp; may
	reduce regional warming; governance.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
	avoid ecosystem harm, water, land; use existing roofs or deserts.</span></p></li>
</ul>
<ol start="10">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Urban
	heat island mitigation via radiative-cooled public infrastructure:</span></p></li>
</ol>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Use
	on bridges, overpasses, stadium roofs, water tanks, public shelters;
	reduce re-radiated heat; improve comfort; reduce energy use of
	nearby buildings.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">This
	is somewhat similar to pavements/roofs but distinct (public
	infrastructure). Or maybe replace with &quot;cooling of water
	bodies?&quot; Hmm.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Maybe
we should separate &quot;building roofs&quot; and &quot;urban/public
infrastructure&quot; as above. But we already have roofs and
pavements. 10 can be public infrastructure.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Alternative
#10: &quot;Radiative-cooled seawater or reservoir cooling for
coastal/urban heat islands&quot; maybe too speculative. Better public
infrastructure.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
maybe include &quot;nighttime cooling for carbon capture&quot;? Could
use radiative cooling to chill amine solvents or membranes? This
reduces energy for CO2 capture. Interesting. But user asks global
temperatures; reducing energy use helps. Could include instead of one
above. But we already have data centers and industrial. Could include
&quot;radiative cooling to improve carbon capture efficiency&quot; as
an indirect method: cool solvent, increase absorption, reduce
reboiler energy. But not night-specific? At night can cool. But maybe
too niche.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Could
include &quot;radiative cooling to assist condensation and water
harvesting&quot;? It reduces temperature and can capture water; not
directly global cooling but could help. But not needed.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Maybe
include &quot;cooling the atmosphere via high-altitude selective
emitters&quot; as a geoengineering method? But might be risky. User
asks &quot;reduce global temperatures&quot; maybe wants creative.
Could mention as a high-level idea but caveat. However, 10 ways
should be plausible. We can include one &quot;large-scale engineered
radiative cooling surfaces/geoengineering&quot;.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
maybe include &quot;cooling the oceans via selective emitters?&quot;
Not feasible; but ocean surface already emits. Not good.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
final with intro and sections. Ensure &quot;extensive detail&quot;.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Let's
compose final answer in a clear style.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Potential
formulas: Q_rad = ε_window σ A (T_surf^4 - T_sky^4) + convective
term. Under clear skies, T_sky can be 150-250 K; for 10 m² panel at
T_surf 300 K, T_sky 230 K: 5.67e-8*(9e8 - 2.79e7) = 50 W? times 10 =
500 W. With selective emissivity and low absorption maybe 30-150
W/m². Good.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
be careful: &quot;T_sky&quot; not actual air temp. Fine.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Let's
start:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">&quot;Below
are 10 practical and semi-practical strategies...&quot;</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Then
each.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Let's
write:</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Intro:</span></p>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Mechanism,
	spectral window, conditions, performance.</span></p></li>
</ul>
<ol>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Passive
	radiative cooling roofs and façades</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Description,
	materials, implementation, performance, global effect.</span></p></li>
</ul>
<ol start="2">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Air-gapped
	radiative membranes for building shells</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Different:
	double-skin, ventilated.</span></p></li>
</ul>
<ol start="3">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Active
	radiative chillers for HVAC</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Different:
	pumps/fans, sub-ambient cooling.</span></p></li>
</ul>
<ol start="4">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">District
	cooling and industrial waste-heat rejection</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">large
	systems.</span></p></li>
</ul>
<ol start="5">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Night-time
	cold storage and phase-change thermal storage</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">storage.</span></p></li>
</ul>
<ol start="6">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative-cooled
	pavements/roads/transport infrastructure</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">infrastructure.</span></p></li>
</ul>
<ol start="7">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Agricultural,
	greenhouse, and livestock cooling</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">sector.</span></p></li>
</ul>
<ol start="8">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative-cooled
	solar PV/thermal systems</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">energy.</span></p></li>
</ul>
<ol start="9">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Data-center
	and electronics radiative cooling</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">high
	heat.</span></p></li>
</ul>
<ol start="10">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Large-scale
	land/rooftop radiative cooling arrays</span></p></li>
</ol>
<ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">geo/urban.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
ensure each has &quot;night-time&quot; aspect. Some passive are
continuous; we can emphasize night operation: at night they
radiatively cool; next day they start cooler. Active systems can run
at night.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
maybe add caveats at end:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Must
	be high emissivity in 8-13 μm, high solar reflectance.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cloudy/humid
	reduces; use hybrids.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Avoid
	increasing albedo in sensitive regions? Actually high albedo can
	also cool; but must not harm ecosystems.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Best
	where clear skies, low humidity, high altitude, abundant existing
	roof/infrastructure.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Let's
write final answer with enough detail.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Double-check
no misinformation:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative
	cooling can cool below ambient only if surface emits in atmospheric
	window and receives less IR from sky; under clear sky. If it also
	absorbs IR from air/ground, may not. Need mention.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Building
	coatings can be white to reflect solar, but white alone not enough;
	need IR emissivity. Good.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Potential
nuance: &quot;increase OLR&quot; for large arrays: Earth already
emits; increasing surface emissivity in window could increase net OLR
if surface temperature not too low; but clouds and water vapor block.
Good.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Let's
craft final.</span></p>
<p style="border: none; padding: 0cm"><br/>
<br/>

</p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><font color="#c9211e"><b>OUTPUT:</b></font><br/>
</span><br/>
<br/>

</p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Below
are 10 ways to exploit night-time radiative cooling to space as a
strategy for reducing temperatures—both locally and, when deployed
at scale, as a contribution to limiting global warming.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">First,
a short physics note:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Any
	surface above ~−273°C emits thermal infrared radiation.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
	atmosphere is mostly opaque to infrared, but has a key “window”
	around 8–13 μm where radiation can escape more easily to space.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">On
	clear nights, especially in dry or high-altitude regions, a surface
	that radiates efficiently in this window can lose 50–150+ W/m² of
	heat to the sky and become several to tens of degrees cooler than
	surrounding air.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
	ideal material or system:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Has
		very high emissivity in the 8–13 μm atmospheric window.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Has
		high reflectance in the solar range (~0.3–2.5 μm) so it doesn’t
		overheat in daylight.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Minimizes
		unwanted heat inflow via conduction/convection.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">These
are not “miracles,” but they can reduce building cooling demand,
industrial energy use, urban heat islands, and—through lower
fossil-fuel consumption for cooling—reduce global warming. In a few
concepts, they also directly increase the net radiative cooling of
Earth’s surface.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Below
are 10 detailed pathways.</span></p>
<ol>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Passive
	radiative cooling roofs and façades</span></p></li>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Concept:
Use specially engineered materials on roofs, walls, and domes that
emit strongly in the 8–13 μm window and reflect sunlight, so that
buildings lose heat directly to the night sky.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">How
it works:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">A
	“cool roof” material is not just white paint. It is engineered
	to:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reflect
		most sunlight (high solar reflectance), preventing daytime heating.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Emit
		thermal IR strongly in 8–13 μm, allowing heat to escape through
		the atmospheric window.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">At
	night, the roof radiates heat to space faster than it absorbs heat
	from the surrounding air, so:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
		roof surface becomes cooler than ambient air.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
		building interior starts the next day cooler, reducing peak heat
		gain.</span></p></li>
	</ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">This
	works even without electricity or moving parts.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Implementation:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Materials
	examples:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Polymer
		films with micro/nano-scale textures.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Ceramic
		or inorganic coatings (e.g., barium sulfate-based, silica-based).</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Photonic-crystal-style
		multilayer dielectric films.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Applications:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Flat
		roofs on offices, schools, hospitals, warehouses.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Curved
		roofs and domes in hot, arid cities.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Building
		façades, especially west-facing walls that overheat in afternoon.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Performance
and impact:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Roof
	temperatures can be 10–30°C lower than conventional roofs in
	sunny conditions.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">In
	hot climates, this can cut air-conditioning demand by 10–40% or
	more, depending on climate and building design.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">At
	scale (millions of rooftops), this:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reduces
		electricity use (especially fossil-fueled).</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Lowers
		urban heat island intensity.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Indirectly
		reduces global warming through avoided emissions.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Key
challenges:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Durability
	under UV, wind, dust, hail.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Ensuring
	true emissivity in the 8–13 μm band, not just high visible
	reflectance.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Avoiding
	excessive moisture ingress or condensation issues.</span></p></li>
</ul>
<ol start="2">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Air-gapped
	radiative cooling building shells and membranes</span></p></li>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Concept:
Install a radiatively cooling outer layer—like a membrane, panel,
or tarp—above existing building surfaces, using air gaps and
passive airflow to prevent that cold from entering the building
structure directly and instead improve overall thermal behavior.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">How
it works:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">A
	selective radiative-emission membrane is mounted:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Above
		a roof,</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Or
		as an external screen on a façade.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">An
	air gap is left between the membrane and the building surface.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">At
	night:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
		membrane radiates heat to space, becoming cool.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Natural
		convection or stack ventilation allows warm air from under the
		membrane to escape.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">In
	the morning:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
		building’s roof and upper walls are cooler than they would
		otherwise be.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
		membrane acts as an additional shield against solar heat.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Implementation:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Rooftop
	tents or parasols with radiatively cooling top layers.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">External
	“cool skins” over parking structures, warehouses, industrial
	halls.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Ventilated
	double-skin façades where the outer skin is a radiative-cooling
	material.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Use
	louvers, vents, or perforated panels to allow airflow; control them
	automatically:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Open
		at night for cooling and ventilation.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Close
		or partly close during extreme daylight heat to reduce convective
		heating.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Performance
and impact:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">This
	reduces heat transfer into the building by combining:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative
		cooling at the outer layer.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Airflow
		that removes trapped heat.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">For
	large commercial or industrial buildings, this can:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cut
		peak indoor temperatures by several degrees.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reduce
		chiller runtime during hot afternoons.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Lower
		electricity demand during peak hours when grids are most stressed.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Key
challenges:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Balancing
	airflow (which can bring in hot air in some conditions) with
	radiative gains.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Ensuring
	wind and dust do not degrade performance.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Integrating
	with existing roof drainage and structural loads.</span></p></li>
</ul>
<ol start="3">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Active
	radiative chillers for building air-conditioning</span></p></li>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Concept:
Use radiative cooling panels as “cooling engines” for
air-conditioning: heat from indoor spaces is carried by water,
glycol, or air to a rooftop or outdoor emitter, which radiates that
heat to the night sky.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">How
it works:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">System
	components:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Selective
		emitter panels (high 8–13 μm emissivity).</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Heat
		exchanger in contact with a circulating fluid.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Pumps
		and/or fans to move fluid and air.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Connection
		to indoor cooling coils, chilled beams, or radiant ceilings.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">At
	night, especially under clear skies:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
		emitter panel radiates heat to space.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
		circulating fluid can be cooled below ambient air temperature.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">This
		sub-ambient cooling is used to:</span></p>
		<ul>
			<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Chill
			indoor air directly.</span></p></li>
			<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cool
			water for chiller plants.</span></p></li>
			<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Pre-cool
			dehumidification or air handling systems.</span></p></li>
		</ul>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">By
	day, the same system:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Continues
		radiative cooling if the sky window is clear.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reduces
		the workload of conventional vapor-compression chillers.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Implementation:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Rooftop
	units on offices, hotels, hospitals, schools.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Integration
	with existing HVAC:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Add
		radiative cooling loops as a “free cooling” source.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Use
		chilled water from radiative chillers to pre-cool air before
		entering dehumidifiers (reducing latent load).</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">In
	hot, dry climates, combine with:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Evaporative
		cooling.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Desiccant
		dehumidification.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Performance
and impact:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">A
	10–50 m² emitter panel under good conditions can deliver several
	kW of cooling, enough to meaningfully assist a small building or
	room.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">In
	favorable climates:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Can
		offset 50–100% of nighttime cooling loads.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Can
		reduce peak chiller electricity by 10–30% over the cooling
		season.</span></p></li>
	</ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Avoided
	electricity use translates directly to avoided CO₂ in
	fossil-fueled grids.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Key
challenges:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Humidity:
	radiative cooling can drop surface temperatures below dew point,
	causing condensation.</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Requires
		control logic, surface hydrophobic coatings, or dehumidification
		integration.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cloud
	cover: cooling performance drops; must be hybrid with conventional
	cooling.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Siting:
	best on high roofs with unobstructed sky view.</span></p></li>
</ul>
<ol start="4">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">District
	cooling and industrial waste-heat rejection fields</span></p></li>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Concept:
Centralize radiative cooling as a large “heat sink” for an entire
district, campus, or industrial park, especially using night-time
operation to pre-cool district loops and reject low-grade waste heat.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">How
it works:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Large
	fields of selective emitters are installed:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">On
		rooftops of central plants.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Or
		in open fields or industrial yards.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Warm
	water from:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">District
		cooling loops.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Industrial
		process loops.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Data
		centers or cold rooms. is passed through heat exchangers on top of
		the emitters.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">At
	night:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
		emitters radiate this heat to space.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
		return water is cooler than ambient, allowing:</span></p>
		<ul>
			<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Storage
			of “cold” in the district loop.</span></p></li>
			<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Pre-cooling
			of buildings and factories.</span></p></li>
		</ul>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
		next day, less chiller capacity is needed to maintain set points.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Implementation:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">District
	cooling plants in cities with:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Clear
		skies,</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Low
		humidity,</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Available
		roof or open land.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Integration
	with:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Centralized
		chillers (radiative cooling as supplemental sink).</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Ice
		or chilled-water storage tanks.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Industrial
		cooling loops in plastics, food, chemicals, electronics, textiles.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Performance
and impact:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">A
	field of 10,000 m² of well-designed emitters can deliver MW-scale
	cooling potential under ideal conditions.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">At
	industrial scale:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Large
		reductions in cooling electricity.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Less
		freshwater use for cooling towers.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Lower
		carbon footprint of manufacturing.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">At
	urban scale:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reduced
		peak grid load.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Lower
		urban heat island intensity due to cooler surfaces and reduced
		waste heat from chillers.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Key
challenges:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Large
	land or roof area required.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Need
	robust controls for fluid temperature and condensation.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Economic
	competitiveness with existing cooling infrastructure.</span></p></li>
</ul>
<ol start="5">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Night-time
	cold storage and phase-change thermal storage</span></p></li>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Concept:
Use radiative cooling at night to cool water, ice, or phase-change
materials (PCMs), storing “cold energy” that can be released
during the hottest part of the next day.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">How
it works:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">At
	night:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative
		emitters cool:</span></p>
		<ul>
			<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Water
			tanks,</span></p></li>
			<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">PCM
			containers,</span></p></li>
			<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Ice-making
			plates.</span></p></li>
		</ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
		stored cold is thermally insulated.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">During
	the day:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
		stored cold is used to:</span></p>
		<ul>
			<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Pre-cool
			supply air in air handling units.</span></p></li>
			<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cool
			radiant ceilings or chilled beams.</span></p></li>
			<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Chill
			water for evaporative coolers or absorption chillers.</span></p></li>
			<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Maintain
			low temperatures in cold rooms or warehouses.</span></p></li>
		</ul>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Implementation:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Rooftop
	radiative cooling + insulated cold storage:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Water
		tanks with emitters on top or on adjacent frames.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">PCM
		tanks (e.g., paraffin, salt hydrates) at 5–25°C.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Ice-making
	in arid regions:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative
		coolers drive evaporative/adiabatic or plate-type ice makers at
		night.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Ice
		is stored for daytime use.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Integration:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">With
		building HVAC.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">With
		commercial cold storage.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">With
		medical/pharmaceutical refrigeration.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Performance
and impact:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">This
	shifts cooling energy use from expensive daytime peaks to cheaper
	nighttime hours.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">For
	buildings:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reduces
		compressor runtime during peak heat.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Improves
		power grid stability by shaving peaks.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">For
	developing regions:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Can
		provide reliable cold storage without large diesel generators.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">For
	the climate:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Less
		fossil-fuel electricity used for cooling.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Less
		waste heat dumped into the local environment from chillers.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Key
challenges:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Maintaining
	thermal insulation while allowing radiative emission.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Managing
	condensation and microbial growth in cold-water systems.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Ensuring
	that stored cold is delivered when needed, not lost.</span></p></li>
</ul>
<ol start="6">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative-cooled
	pavements, roads, and transport infrastructure</span></p></li>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Concept:
Use radiatively cooling materials in roads, bridges, parking lots,
and rail yards to keep surfaces cooler, reducing urban heat islands
and the energy needed by vehicles and adjacent buildings.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">How
it works:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Conventional
	asphalt and concrete:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Absorb
		a lot of sunlight.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Store
		heat and re-radiate it into the street canyon.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Create
		strong urban heat islands.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiatively
	cooling pavement:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Contains
		high-emissivity particles or coatings in the 8–13 μm band.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reflects
		sunlight.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Emits
		heat to the sky at night and to some extent during clear days.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Result:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Surface
		and subsurface temperatures are lower.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Less
		heat is radiated back into the air.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Vehicles
		experience lower ambient temperatures, reducing air-conditioning
		demand.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Implementation:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cool
	asphalt mixes:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Use
		reflective aggregates.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Add
		IR-emissive pigments or fillers.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cool
	coatings:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Apply
		selective emitters on existing roads, bridges, parking lots,
		airport aprons.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Rail
	and logistics:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cool
		rail yards and freight containers using radiative-cooling roofs and
		ground covers.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Lower
		temperature of stored goods, reducing spoilage and refrigeration
		demand.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Performance
and impact:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Pavement
	temperatures can be reduced by 10–30°C compared to standard black
	asphalt.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Urban
	air temperature can drop by ~1–3°C in heavily paved areas with
	widespread cool pavement.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Indirect
	climate benefits:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reduced
		vehicle fuel/electricity use for AC.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reduced
		need for building AC along streets.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reduced
		heat stress for pedestrians and workers.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Key
challenges:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Ensuring
	skid resistance and durability.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Avoiding
	glare issues.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Maintaining
	high 8–13 μm emissivity under traffic abrasion and pollution.</span></p></li>
</ul>
<ol start="7">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative
	cooling for agriculture, greenhouses, and livestock</span></p></li>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Concept:
Use radiative cooling to protect crops, animals, and stored produce
from heat stress, and to reduce the energy needed for refrigeration
in the agricultural and food supply chain.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">How
it works:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">In
	hot regions, excessive heat:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Stresses
		livestock and poultry.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reduces
		crop yields.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Increases
		spoilage of harvested produce.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative
	cooling can:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cool
		barns, sheds, greenhouses, and storage warehouses at night.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Keep
		structures and contents cooler during the day.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reduce
		or replace conventional refrigeration.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Implementation:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Livestock
	barns:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative-cooling
		panels on roofs.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Night
		ventilation with passive airflow.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Lower
		indoor temperatures improve animal comfort, growth, and egg/milk
		yield.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Greenhouses:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Selective-emission
		roofs or films.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Combined
		with shade and ventilation.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Useful
		for horticulture in hot, sunny climates.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cold
	chain:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cold
		rooms and warehouses with radiative-cooling roofs.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Night-time
		pre-cooling of storage spaces.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative-cooling-assisted
		chillers for produce, dairy, meat, vaccines.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Performance
and impact:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reduced
	heat stress:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Lower
		mortality in poultry and livestock.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Improved
		feed efficiency and productivity.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reduced
	food loss:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cooler
		storage delays spoilage.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Less
		reliance on diesel generators for cold chains.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Climate
	benefit:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reduced
		fossil fuel and electricity consumption.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Lower
		emissions from both energy and decomposing food waste.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Key
challenges:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Managing
	humidity and condensation.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Ensuring
	materials withstand cleaning, ammonia, chemicals, and high humidity.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Integrating
	with local agricultural practices and economics.</span></p></li>
</ul>
<ol start="8">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative
	cooling for solar power and solar-thermal systems</span></p></li>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Concept:
Use radiative cooling to keep solar photovoltaic (PV) panels and
solar-thermal collectors cooler, improving efficiency and reducing
energy losses.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">How
it works:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">PV
	panels:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cell
		efficiency drops as temperature rises (~0.3–0.5%/°C).</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative-cooling
		backsheets or attached emitters:</span></p>
		<ul>
			<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Increase
			IR emission to the sky.</span></p></li>
			<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Lower
			module temperatures.</span></p></li>
		</ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Result:
		higher electrical output per panel and longer component life.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Solar-thermal
	collectors:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Heat
		collection is driven by temperature difference between collector
		and environment.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">By
		using radiative cooling at night:</span></p>
		<ul>
			<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Pre-cool
			the collector and heat exchanger.</span></p></li>
			<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Increase
			temperature difference available the next morning.</span></p></li>
		</ul>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Can
		also help reject low-grade heat to space in industrial loops.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Implementation:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">PV
	modules:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Selective-emission
		backsheets.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative-cooling
		films on the rear of panels.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Heat
		pipes or fin structures that connect the module back to an external
		emitter.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Solar-thermal
	plants:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative
		cooling panels integrated with the plant’s heat rejection loops.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Night-time
		pre-cooling of receivers and storage tanks in solar-thermal power
		plants.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Performance
and impact:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">PV:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Module
		temperatures several degrees lower.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Electrical
		yield improvement of a few percent, significant at utility scale.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reduced
		thermal stress and module degradation.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Solar-thermal:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Improved
		daily energy capture.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Less
		need for auxiliary fuels or electric heating.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Climate
	benefit:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">More
		clean electricity and heat per unit of infrastructure.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reduced
		fossil-fuel displacement required to meet energy demand.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Key
challenges:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Ensuring
	no added electrical losses or shading.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Robustness
	under high UV, dust, wind.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">System-level
	optimization (cooling too much in very cold climates can reduce
	useful heat).</span></p></li>
</ul>
<ol start="9">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative
	cooling for data centers and high-density electronics</span></p></li>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Concept:
Deploy radiative cooling panels as low-energy heat sinks for data
centers, telecom hubs, server rooms, and industrial electronics,
especially during clear nights.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">How
it works:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Data
	centers produce large amounts of low-grade waste heat.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Traditional
	cooling:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Chiller
		plants or evaporative cooling towers.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Energy-
		and water-intensive.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative
	cooling approach:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Install
		selective emitters on rooftops or in open yards.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Circulate
		water or secondary fluids through emitters.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">At
		night, these fluids are cooled below ambient by radiation to space.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Use
		this cooling:</span></p>
		<ul>
			<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">To
			directly cool server rooms via air handlers.</span></p></li>
			<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">To
			chill water loops used in server cooling.</span></p></li>
			<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">To
			pre-cool thermal storage for daytime operation.</span></p></li>
		</ul>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Implementation:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Rooftop
	or yard radiative cooling panels connected to:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Air
		handling units.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Liquid
		cooling loops.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Immersion
		cooling tanks.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Hybrid
	operation:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Night:
		use radiative cooling as the primary heat rejection.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Day:
		use stored cold + supplemental conventional cooling as needed.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Best
	in:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Arid
		regions with clear skies.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Data
		centers with large roof areas or open space.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Performance
and impact:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Can
	significantly reduce the Power Usage Effectiveness (PUE) of data
	centers.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reduced
	need for:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Electricity
		for chillers.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Water
		for evaporative cooling.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Climate
	benefit:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Data
		centers are energy-hungry; reducing their cooling load is a
		meaningful emissions reduction.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Less
		waste heat dumped into the local environment.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Key
challenges:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Maintaining
	server temperature control under high density and 24/7 operation.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Ensuring
	stable fluid temperatures and avoiding condensation in electronics.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Economic
	integration with existing cooling systems.</span></p></li>
</ul>
<ol start="10">
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Large-scale
	land-based radiative cooling arrays</span></p></li>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Concept:
Deploy vast arrays of selective radiative emitters on roofs, deserts,
high plateaus, or other suitable surfaces to increase the net cooling
of Earth’s surface by enhancing emission through the atmospheric
window.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">How
it works:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">This
	is a more explicit “climate engineering” style application of
	the physics:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Increase
		the fraction of surface heat radiated in the 8–13 μm window.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Increase
		net outgoing longwave radiation (OLR) in regions where the sky is
		clear and dry.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Lower
		surface temperature and, indirectly, local air temperature.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Unlike
	simple white paint, these surfaces:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Must
		be engineered for high emissivity specifically in the atmospheric
		window.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Should
		also reflect sunlight to avoid daytime heating.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">On
	very large scales (thousands to millions of km²):</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
		cumulative effect could:</span></p>
		<ul>
			<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reduce
			regional average surface temperatures.</span></p></li>
			<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reduce
			energy demand for cooling.</span></p></li>
			<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Contribute
			marginally to global radiative cooling.</span></p></li>
		</ul>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Implementation
scenarios:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Urban
	rooftops:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Coordinated
		deployment of radiative-cooling roofs and panels across megacities.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Arid,
	high-altitude regions:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Install
		radiative-cooling fields on flat land, industrial yards, or
		existing infrastructure.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Hybrid
	use:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Combine
		with district cooling, cold storage, industrial loops, and
		agriculture.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
		same infrastructure both provides cooling services and increases
		net radiative loss to space.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Performance
and impact:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Local:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Clear
		reductions in surface and near-surface temperatures.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Lower
		cooling demand across many sectors.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Regional/global:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">If
		enough area is treated, the planet radiates slightly more heat to
		space.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
		effect is not a substitute for cutting greenhouse gases, but:</span></p>
		<ul>
			<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Adds
			to demand-side cooling reductions.</span></p></li>
			<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Adds
			a direct, though small, radiative forcing offset.</span></p></li>
		</ul>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Socio-economic:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Creates
		infrastructure for resilient cooling in hot regions.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Improves
		public health by lowering heat stress.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Key
challenges and caveats:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Land
	use and ecological impacts:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Must
		avoid harming ecosystems, water cycles, and local livelihoods.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Climate
	feedbacks:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Could
		influence cloud formation, humidity, or regional weather patterns.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Governance:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Needs
		international oversight and environmental impact assessment.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Technical:</span></p>
	<ul>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Materials
		must be stable and inexpensive at very large scale.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Important
overall caveats</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">To
avoid overclaiming, note:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative
	cooling:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Works
		best under clear skies and low humidity.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Is
		strongly dependent on the 8–13 μm spectral window.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Must
		not be confused with ordinary white paint, which is good for albedo
		but may be a poor selective emitter.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">It
	is primarily:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">A
		powerful tool for reducing cooling energy demand and emissions.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">A
		way to lower local and urban temperatures.</span></p></li>
	</ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">As
	a “global” cooling strategy:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">It
		can help via avoided fossil-fuel use for cooling.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">And,
		at large scale, by increasing net outgoing longwave radiation—but
		this must be studied carefully and implemented responsibly.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">If
you’d like, I can:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Turn
	these into a prioritized list based on feasibility and cost.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Sketch
	simple system diagrams for a building, district, or data-center
	implementation.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Provide
	sample calculations of cooling power and energy savings for a
	specific city or climate.</span></p></li>
</ul>
<p style="line-height: 100%; margin-bottom: 0cm">---</p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm"><font size="6" style="font-size: 24pt">Example
2 of 4</font></p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm">“medium”
reasoning</p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm">---</p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm"><b>PROMPT:</b></p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm"><b>Explain 10 ways
(in extensive detail) to use the &quot;night&quot; time cooling of
radiant energy into space to reduce global temperatures.</b></p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p><span style="display: inline-block; border: none; padding: 0cm"><font color="#c9211e"><b>Thought
for 15.28 seconds</b></font></span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">This
is a fascinating question about radiative cooling to space. Let me
think through this carefully.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
basic principle: Earth continuously radiates infrared energy to
space. Certain wavelengths of IR radiation can pass through the
atmosphere more efficiently than others (the atmospheric transmission
windows, particularly 8-13 μm). If we can enhance radiative cooling
to space, we could theoretically remove heat from Earth's climate
system.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Key
considerations:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
	atmosphere has transmission windows where IR radiation escapes more
	easily (particularly 8-13 μm, and to some extent 3-5 μm)</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Radiative
	cooling to space works by emitting at wavelengths that pass through
	the atmosphere more readily than the atmosphere emits at those
	wavelengths</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">This
	is different from reflecting sunlight (albedo) - this is about
	enhancing outgoing longwave radiation (OLR)</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Let
me think through 10 distinct approaches:</span></p>
<ol>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Space-based
	radiators (orbital heat sinks)</strong></span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Place
		large radiator panels in orbit (possibly at high altitude or
		specific orbital positions)</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">These
		would radiate to deep space with no atmospheric interference</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Could
		be positioned to intercept terrestrial radiation</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Challenges:
		scale, materials, deployment, power for positioning</span></p></li>
	</ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Stratospheric/aerosol-free
	high-altitude radiating platforms</strong></span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Deploy
		platforms above the troposphere in the stratosphere</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">These
		radiate to space through clearer IR windows</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Could
		absorb lower-altitude IR and re-radiate more efficiently</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Balloons,
		high-altitude aircraft, or stationary platforms</span></p></li>
	</ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Enhanced
	atmospheric CO2 reduction (removing IR absorbers)</strong></span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">This
		is more indirect but directly relates to the principle</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">By
		reducing greenhouse gases that absorb in the 8-13 μm window, we
		allow more natural cooling</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Carbon
		removal technologies (DAC, ocean alkalinity, etc.)</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">This
		effectively &quot;opens&quot; the window for radiative cooling</span></p></li>
	</ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Surface
	radiative cooling materials</strong></span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Materials
		that emit strongly in the 8-13 μm window while absorbing less
		solar radiation</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Applied
		to buildings, roofs, urban areas</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Passive
		cooling below ambient temperature possible</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Scalable
		to large areas</span></p></li>
	</ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Oceanic
	radiative cooling (enhanced OLR over oceans)</strong></span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Oceans
		are a major source of outgoing radiation</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Perhaps
		ways to enhance the IR emission from ocean surfaces</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reduce
		surface skin temperature effects that trap radiation</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Wave
		or wind modification to enhance mixing and reduce the &quot;blanket&quot;
		effect</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Actually,
		the ocean is already radiating - the issue is the atmosphere above
		it</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Better
		approach: reduce atmospheric opacity over ocean regions in IR
		windows</span></p></li>
	</ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>High-altitude
	cirrus cloud modification (reducing IR trapping)</strong></span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cirrus
		clouds trap outgoing IR by being colder and having different IR
		properties</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Actually,
		this is tricky - cirrus can both reflect sunlight AND trap IR</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reducing
		high-altitude clouds that act as IR &quot;blankets&quot; could
		enhance cooling</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">This
		would be cloud manipulation in the opposite direction of usual
		geoengineering</span></p></li>
	</ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Atmospheric
	dust/mineral aerosol injection (in IR-transparent layers)</strong></span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Actually
		this is counterintuitive - most aerosols absorb IR</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">But
		if we could inject materials that are transparent in the IR window
		but still...</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Hmm,
		this doesn't work well. Let me reconsider.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Actually,
		we want to REDUCE atmospheric absorption in the 8-13 window, not
		add to it</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">So
		this might work by: reducing natural aerosols that absorb IR, or by
		creating conditions where IR passes more freely</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Or:
		using the 8-13 window strategically</span></p></li>
	</ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Stratospheric
	water vapor removal</strong></span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Water
		vapor is a major IR absorber</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Removing
		water vapor from upper atmosphere would open IR windows</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Could
		potentially be done with... this is very challenging</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Dehydration
		of the stratosphere</span></p></li>
	</ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Passive
	space-based solar shields combined with IR radiators</strong></span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Orbits
		positioned to block incoming solar radiation at the same time
		radiating heat to space</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Dual-purpose:
		reflect sunlight AND radiate heat</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Positioned
		at L1 point or low orbit</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
		radiator panels would need to be very large</span></p></li>
	</ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Night-time
	enhanced radiative cooling infrastructure</strong></span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Building
		structures specifically optimized for night-time cooling</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Large
		radiating surfaces that cool at night and store cold energy for
		daytime use</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Thermal
		energy storage coupled to radiative coolers</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Urban-scale
		implementations</span></p></li>
	</ul>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Let
me refine and expand these 10 ideas with extensive detail.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Actually,
let me reconsider some of these and make sure they're truly distinct
and technically sound.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Key
physics:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Earth's
	surface emits ~240 W/m² of OLR on average</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
	8-13 μm window is where the atmosphere is most transparent
	(especially between CO2 and O3 absorption bands)</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
	stratosphere is relatively clear in certain IR bands</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Space
	at altitude &gt; 50 km has essentially no atmospheric absorption</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Let
me develop these 10 ideas in detail:</span></p>
<ol>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Orbital
	Radiating Heat Sinks</strong></span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Stratospheric
	IR Transparent Platforms</strong></span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Stratospheric
	Dehydration (Water Vapor Removal)</strong></span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Advanced
	Radiative Cooling Materials for Surfaces</strong></span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Cloud
	Layer Manipulation to Enhance IR Emission</strong></span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Atmospheric
	Composition Modification (Reducing IR Absorbers)</strong></span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Polar
	Region Enhanced Radiative Cooling</strong></span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Night-time
	Radiative Cooling Thermal Storage Systems</strong></span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Ocean-Surface
	Radiative Enhancement</strong></span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>High-Altitude
	Balloon Arrays with IR-Optimized Emitters</strong></span></p></li>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Let
me develop each of these in extensive detail now.</span></p>
<h1 class="western" style="border-top: none; border-bottom: 1px solid #fbfcfc; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm">
<span style="display: inline-block; border: none; padding: 0cm"><font color="#c9211e">OUTPUT</font></span></h1>
<h1 class="western" style="border-top: none; border-bottom: 1px solid #fbfcfc; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">Ten
Approaches to Night-Time Radiative Cooling for Climate Mitigation</span></h1>
<h2 class="western" style="border-top: none; border-bottom: 1px solid #fbfcfc; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">The
Fundamental Principle</span></h2>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Earth
continuously radiates infrared energy to space, but greenhouse gases
(water vapor, CO₂, methane, etc.) absorb and re-emit some of this
radiation back toward the surface. The &quot;night&quot; aspect is
crucial because without incoming solar radiation, the imbalance
between emitted IR and absorbed IR becomes the dominant heat transfer
mechanism. The atmosphere has transmission &quot;windows&quot;—particularly
8–13 μm—where IR escapes relatively unimpeded. All ten
approaches below exploit or enhance this mechanism.</span></p>
<hr/>

<h2 class="western" style="border-top: none; border-bottom: 1px solid #fbfcfc; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">1.
Orbital Radiating Heat Sinks</span></h2>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Concept:</strong>
Deploy massive radiator structures in orbit (particularly low Earth
orbit, ~200–600 km) that actively absorb terrestrial infrared
radiation and re-radiate it into the vacuum of space with no
atmospheric interference.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Technical
Detail:</strong></span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">At
altitudes above ~100 km, there is essentially no atmospheric
absorption. A radiator in this space would radiate into a 2.7 K
cosmic background with perfect efficiency. The key physics is the
Stefan-Boltzmann law: a blackbody at temperature T radiates power
proportional to T⁴. A panel at 300 K (surface-equivalent) radiates
~459 W/m².</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Architecture:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Capture
	arrays:</strong>&nbsp;Large, angled panels oriented to intercept
	outgoing longwave radiation (OLR) from Earth's surface. These panels
	would need to be highly absorptive in the 8–13 μm window.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Radiator
	wings:</strong>&nbsp;On the opposite side (facing away from Earth),
	the panels would be highly emissive in IR and highly reflective in
	visible/near-IR to minimize solar heating.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Thermal
	management:</strong>&nbsp;The panels would need to reach a
	temperature high enough that they radiate efficiently but low enough
	to not conduct excessive heat to their structure. This requires
	thermal isolation between the capture side and radiator side.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Scale
Considerations:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Earth's
	total OLR is approximately 240 W/m² × 5.1×10¹⁴ m² ≈
	1.23×10¹⁷ W.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Even
	capturing 0.1% of this (~1.2×10¹⁴ W) would represent a massive
	climate intervention.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">A
	panel 10 km × 10 km × 10 km (cubic kilometers of radiating area)
	could handle ~5.5×10¹⁰ W.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">To
	capture 1% of Earth's OLR, you'd need roughly 10⁶ km² of
	radiating surface area in orbit.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Engineering
Challenges:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Deployment:</strong>&nbsp;The
	structural mass would be enormous. Current space launch costs make
	this extraordinarily expensive, though in-space manufacturing (from
	asteroid or lunar materials) could eventually make it feasible.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Thermal
	stress:</strong>&nbsp;The day-night cycle in orbit creates extreme
	thermal cycling (from -150°C in shadow to +120°C in sunlight).
	Materials must handle this.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Orbital
	mechanics:</strong>&nbsp;The panels need stable positioning. Active
	station-keeping or carefully chosen orbits are needed.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Space
	debris:</strong>&nbsp;Large structures create significant debris
	risk if damaged.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Advantages:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">No
	atmospheric interference—perfect radiative cooling.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Continuous
	operation (no day-night cycle limitation).</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Scalable
	in principle.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Limitations:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Currently
	infeasible at the scale needed.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Significant
	environmental and political concerns (space debris, orbital
	occupation).</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cost
	prohibitive with current technology.</span></p></li>
</ul>
<hr/>

<h2 class="western" style="border-top: none; border-bottom: 1px solid #fbfcfc; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">2.
Stratospheric IR-Transparent Platforms</span></h2>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Concept:</strong>
Deploy floating platforms (high-altitude balloons, airships, or
tethered structures) at 20–50 km altitude in the stratosphere,
where the atmosphere is thinner and more transparent in certain IR
bands. These platforms would act as intermediate radiators.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Technical
Detail:</strong></span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
stratosphere above ~25 km has significantly reduced water vapor and
CO₂ density. The 8–13 μm transmission window is more open at
these altitudes. A platform at 30 km altitude would radiate into an
atmosphere that absorbs less of its outgoing IR than the troposphere.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Architecture:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Buoyancy
	systems:</strong>&nbsp;Helium or hydrogen-filled balloons, or
	lighter-than-air structures using heated gas.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>IR-optimized
	panels:</strong>&nbsp;Surfaces highly emissive in 8–13 μm, highly
	reflective in solar spectrum.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Altitude
	maintenance:</strong>&nbsp;Ballast systems, solar-powered fans, or
	tethered to ground-based moorings.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Heat
	absorption:</strong>&nbsp;The platform absorbs IR radiation from
	below (from the surface and lower atmosphere) and re-radiates it
	upward more efficiently.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Thermodynamic
Advantage:</strong> At 30 km altitude, the ambient temperature is
approximately -56°C (217 K). A platform at this temperature radiates
only ~120 W/m² (Stefan-Boltzmann). However, if the platform absorbs
IR from below and maintains a higher temperature, it can radiate more
effectively into the thinner upper atmosphere. The key insight is
that the platform sits in a region where the atmospheric emission at
that altitude is lower, creating a net radiative loss.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Scale
and Practicality:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Current
	high-altitude balloons (like Google's Loon project, or various
	scientific balloons) operate at 20–30 km.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">A
	balloon array covering 1,000 km² would be massive but conceptually
	within reach.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cost
	per km²: potentially $10,000–$100,000 with current technology.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Advantages:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Technically
	closer to feasibility than orbital solutions.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">No
	space debris concerns (balloons eventually descend).</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Can
	be positioned over specific regions.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Limitations:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Limited
	by buoyancy and wind patterns.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Must
	contend with stratospheric conditions (UV radiation, temperature
	extremes).</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Scale
	still insufficient for global climate impact.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Wind
	drift requires constant repositioning.</span></p></li>
</ul>
<hr/>

<h2 class="western" style="border-top: none; border-bottom: 1px solid #fbfcfc; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">3.
Stratospheric Dehydration (Water Vapor Removal)</span></h2>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Concept:</strong>
Actively remove water vapor from the stratosphere to reduce IR
absorption in the 8–13 μm window, thereby enhancing natural
radiative cooling to space.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Technical
Detail:</strong></span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Water
vapor is the most potent greenhouse gas, with a complex absorption
spectrum spanning many IR bands. In the stratosphere, water vapor is
particularly abundant above ~20 km due to methane oxidation and
transport from the troposphere. Reducing stratospheric water vapor
would:</span></p>
<ol>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reduce
	IR absorption in the 6 μm and 18 μm bands.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reduce
	absorption in parts of the 8–13 μm window.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Allow
	more terrestrial IR radiation to escape to space.</span></p></li>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Mechanisms
for Removal:</strong></span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>A.
Chemical Catalysis:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Deploy
	catalysts that convert H₂O to less IR-absorbing species.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Example:
	React H₂O with a surface that binds water molecules permanently.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Challenge:
	Finding catalysts that work at stratospheric conditions and don't
	create other harmful byproducts.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>B.
Physical Capture:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">High-altitude
	balloons or drones carrying desiccant materials.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Materials
	like molecular sieves, silica gels, or advanced zeolites.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
	desiccant absorbs water vapor and is either:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Disposed
		of (heavy, impractical at scale)</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Regenerated
		by heating (requires energy)</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Dropped
		to the surface for regeneration</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>C.
Electrostatic Precipitation:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Use
	electrostatic fields to attract water vapor molecules to collecting
	surfaces.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">More
	theoretical—requires understanding of water molecule behavior at
	low pressure.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Quantitative
Impact:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Stratospheric
	water vapor contributes ~0.1–0.5 W/m² of radiative forcing
	(estimates vary).</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Removing
	50% of stratospheric H₂O might reduce this by ~0.05–0.25 W/m².</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">This
	is small compared to the total greenhouse effect (~3.7 W/m² from
	anthropogenic GHGs), but not negligible.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Advantages:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Addresses
	a natural greenhouse gas directly.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Could
	work synergistically with other approaches.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Limitations:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Very
	small effect relative to CO₂ and other GHGs.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Technically
	challenging at scale.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Potential
	unintended consequences (ozone chemistry interactions).</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Water
	vapor is continuously replenished from below.</span></p></li>
</ul>
<hr/>

<h2 class="western" style="border-top: none; border-bottom: 1px solid #fbfcfc; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">4.
Advanced Radiative Cooling Materials for Surfaces</span></h2>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Concept:</strong>
Develop and deploy materials that emit strongly in the 8–13 μm
atmospheric window while minimizing solar absorption, enabling
passive cooling of surfaces below ambient temperature.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Technical
Detail:</strong></span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">This
is the most immediately practical approach. The physics is
straightforward:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">A
	material with high emissivity (ε &gt; 0.95) in the 8–13 μm band
	will radiate efficiently to space.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">A
	material with low absorptivity (α &lt; 0.15) in the solar spectrum
	(0.3–2.5 μm) will not heat from sunlight.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
	combination allows the material to reach a steady-state
	temperature&nbsp;<em>below</em>&nbsp;ambient.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Material
Design:</strong></span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>A.
Multilayer Dielectric Structures:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Alternating
	layers of high-index and low-index materials (e.g., Si₃N₄ and
	SiO₂, or Al₂O₃ and SiO₂).</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Each
	layer thickness is tuned to be λ/4 at target wavelengths.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Creates
	constructive interference in the 8–13 μm band (high emissivity).</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Creates
	destructive interference in the solar band (low absorptivity).</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Number
	of layers: typically 20–50 for optimal performance.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>B.
Nanoparticle Composites:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Embed
	nanoparticles (e.g., SiC, ZnO, or TiO₂) in a polymer matrix.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
	nanoparticles provide resonant IR emission.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
	matrix provides structural integrity and UV stability.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">More
	manufacturable than multilayer structures.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>C.
Graphene and 2D Materials:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Graphene
	has tunable optical properties.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Stacked
	graphene layers can be engineered for specific emission spectra.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">More
	research needed but promising.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Performance
Metrics:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Net
	radiative power: 50–150 W/m² achievable (depends on humidity, sky
	conditions).</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Temperature
	reduction: 3–10°C below ambient in optimal conditions.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cost:
	$1–$10/m² for advanced materials.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Deployment
Scales:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Buildings:</strong>&nbsp;Roofs,
	walls, parking structures.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Infrastructure:</strong>&nbsp;Road
	surfaces, rail tracks, airport runways.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Energy
	systems:</strong>&nbsp;Cooling panels for solar cells, data centers,
	industrial processes.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Agriculture:</strong>&nbsp;Cooling
	greenhouses, reducing irrigation needs.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Quantitative
Impact:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Urban
	areas represent ~3% of Earth's surface.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">If
	50% of urban area is covered with radiative cooling materials at 100
	W/m² net cooling:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">0.03
		× 5.1×10¹⁴ m² × 0.5 × 100 W/m² = 7.65×10¹⁴ W.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">This
		is ~0.6% of Earth's OLR—significant but not sufficient alone.</span></p></li>
	</ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">However,
	the energy savings from reduced cooling demand (HVAC) could be
	substantial.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Advantages:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Technically
	mature—already demonstrated in lab and pilot scale.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Low
	cost at scale.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">No
	moving parts, no energy input needed.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Beneficial
	co-benefits (energy savings, reduced urban heat island).</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Limitations:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Performance
	depends on sky clarity and humidity.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Limited
	to surfaces it can be applied to.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Not
	a solution for ocean or open atmosphere cooling.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Scale
	insufficient for global climate impact alone.</span></p></li>
</ul>
<hr/>

<h2 class="western" style="border-top: none; border-bottom: 1px solid #fbfcfc; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">5.
Cloud Layer Manipulation to Enhance IR Emission</span></h2>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Concept:</strong>
Modify cloud properties (composition, altitude, thickness, droplet
size) to enhance the net IR emission to space while minimizing solar
reflection changes.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Technical
Detail:</strong></span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Clouds
are the most complex component of Earth's radiation budget. They
reflect ~102 W/m² of solar radiation (cooling) but absorb and
re-emit ~33 W/m² of terrestrial IR (warming). The net effect is
cooling, but the details matter.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Strategy
A: Reducing High-Altitude Cirrus Clouds</strong></span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cirrus
clouds (ice crystals at 6–12 km altitude) have a warming effect
because they:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Absorb
	outgoing IR radiation.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Re-emit
	it from a colder altitude, reducing the amount that escapes to
	space.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Are
	relatively thin, so they reflect less sunlight than they trap IR.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Mechanisms:</strong></span></p>
<ol>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Ice
	nucleation suppression:</strong></span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Remove
		or deactivate ice nucleating particles (INPs) in the upper
		atmosphere.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">INPs
		include dust particles, biological particles, and certain aerosols.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Without
		INPs, fewer ice crystals form, reducing cirrus cover.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Method:
		Deploy &quot;anti-nucleating&quot; agents that coat INPs and
		prevent ice formation.</span></p></li>
	</ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Cloud
	dissipation:</strong></span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Use
		wind shear or temperature manipulation to dissipate existing
		cirrus.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Challenge:
		Cirrus are high and thin; hard to access.</span></p></li>
	</ul>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Expected
Impact:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cirrus
	clouds contribute ~0.4–1.0 W/m² of net warming (estimates vary).</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reducing
	cirrus cover by 20% might yield ~0.1–0.2 W/m² of net cooling.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Significant
	but small.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Strategy
B: Enhancing Low-Altitude Stratus Clouds</strong></span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Low-altitude
stratus clouds (water droplets at 1–2 km altitude) have a net
cooling effect because:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">They
	reflect more sunlight than they trap IR.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Their
	droplets are larger and more efficient at scattering visible light.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Mechanisms:</strong></span></p>
<ol>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Cloud
	brightening (albedo enhancement):</strong></span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Inject
		salt particles or other condensation nuclei at low altitude.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">More,
		smaller droplets form, increasing cloud reflectivity.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">This
		is a form of marine cloud brightening (MCB), already studied.</span></p></li>
	</ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Cloud
	seeding with IR-optimizing agents:</strong></span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Particles
		that enhance cloud IR emission in the 8–13 μm window.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">More
		theoretical—requires specific particle properties.</span></p></li>
	</ul>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Quantitative
Impact:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Marine
	cloud brightening: ~0.1–0.5 W/m² possible with large-scale
	deployment.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cirrus
	reduction: ~0.1–0.2 W/m² possible.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Combined:
	potentially 0.2–0.7 W/m² of net cooling.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Advantages:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Leverages
	existing cloud physics.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Potentially
	reversible (clouds are transient).</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Can
	be targeted regionally.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Limitations:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Complex
	atmospheric interactions—hard to predict.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Potential
	impacts on precipitation patterns.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Requires
	continuous operation.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Small
	effect relative to total radiative forcing.</span></p></li>
</ul>
<hr/>

<h2 class="western" style="border-top: none; border-bottom: 1px solid #fbfcfc; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">6.
Atmospheric Composition Modification (Reducing IR Absorbers)</span></h2>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Concept:</strong>
Actively reduce concentrations of greenhouse gases that absorb in the
8–13 μm window and other key IR bands, thereby opening the
atmospheric window for enhanced radiative cooling.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Technical
Detail:</strong></span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">This
approach addresses the root cause of reduced radiative cooling:
increased greenhouse gases that trap outgoing IR radiation.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>A.
Carbon Dioxide Removal (CDR)</strong></span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">CO₂
absorbs strongly in:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">4.3
	μm band (very strong)</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">15
	μm band (strong)</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Parts
	of the 8–13 μm window (weaker but significant)</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Methods:</strong></span></p>
<ol>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Direct
	Air Capture (DAC):</strong></span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Large
		fans draw air past chemical sorbents.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">CO₂
		is captured and stored permanently (geological sequestration,
		mineralization).</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Current
		cost: $250–$500/ton CO₂.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Scale
		needed: ~10¹⁰ tons/year for 1 ppm reduction.</span></p></li>
	</ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Ocean
	Alkalinity Enhancement:</strong></span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Add
		alkaline minerals (e.g., olivine, lime) to oceans.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Increases
		ocean's capacity to absorb CO₂ from the atmosphere.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cost:
		$50–$100/ton CO₂.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Potential
		scale: 10⁹–10¹⁰ tons/year.</span></p></li>
	</ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Enhanced
	Weathering:</strong></span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Crush
		and spread silicate minerals on land.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Natural
		weathering processes absorb CO₂.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cost:
		$50–$200/ton CO₂.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Slower
		but cheaper.</span></p></li>
	</ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Bioenergy
	with Carbon Capture (BECCS):</strong></span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Grow
		biomass, burn it for energy, capture the CO₂.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Net-negative
		emissions.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cost:
		$50–$150/ton CO₂.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Limited
		by land availability.</span></p></li>
	</ul>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Quantitative
Impact:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Each
	1 ppm reduction in CO₂ ≈ 0.04 W/m² of radiative cooling.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">To
	achieve 1 W/m² of cooling, need ~25 ppm CO₂ reduction.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Currently
	~420 ppm; reducing to ~395 ppm would require ~10¹¹ tons CO₂
	removal.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">At
	$100/ton, cost: $10¹³ (trillions of dollars).</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>B.
Methane Reduction</strong></span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Methane
absorbs in:</span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">3.3
	μm band (strong)</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">7.7
	μm band (strong)</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Parts
	of 8–13 μm window</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Methods:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reduce
	livestock methane emissions (feed additives).</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Capture
	methane from landfills, coal mines, natural gas systems.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Catalytic
	oxidation of atmospheric methane (theoretical).</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Quantitative
Impact:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Methane
	contributes ~0.5 W/m² of radiative forcing.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reducing
	methane by 50% ≈ 0.25 W/m² of cooling.</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Advantages:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Addresses
	root cause of radiative trapping.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Permanent
	solution (if CO₂ is permanently stored).</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Co-benefits
	(cleaner air, ecosystem protection).</span></p></li>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Limitations:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Cost
	prohibitive at scale needed for significant cooling.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Slow
	process (CO₂ removal takes decades to show full effect).</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Requires
	permanent storage infrastructure.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Energy-intensive
	(especially DAC).</span></p></li>
</ul>
<hr/>

<h2 class="western" style="border-top: none; border-bottom: 1px solid #fbfcfc; border-left: none; border-right: none; padding-top: 0cm; padding-bottom: 0.05cm; padding-left: 0cm; padding-right: 0cm">
<span style="display: inline-block; border: none; padding: 0cm">7.
Polar Region Enhanced Radiative Cooling</span></h2>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Concept:</strong>
Focus radiative cooling efforts on polar regions (Arctic and
Antarctic) where the albedo-ice feedback is critical and where
cooling can have amplified global effects.</span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Technical
Detail:</strong></span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
polar regions are particularly sensitive to radiative cooling
because:</span></p>
<ol>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Ice-albedo
	feedback:</strong>&nbsp;Cool ice reflects more sunlight, further
	cooling. Warm ice melts, absorbs more sunlight, further warming.
	Enhancing cooling in the Arctic could stabilize or reverse this
	feedback.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Permafrost:</strong>&nbsp;Cooling
	prevents permafrost thaw, which would release massive amounts of
	methane and CO₂.</span></p></li>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Arctic
	amplification:</strong>&nbsp;The Arctic is warming 2–4× faster
	than the global average. Targeted cooling here could have outsized
	global benefits.</span></p></li>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Approaches:</strong></span></p>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>A.
Arctic Radiative Cooling Infrastructure:</strong></span></p>
<ol>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Ice
	sheet radiative cooling:</strong></span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Apply
		radiative cooling materials to ice surfaces.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
		ice already radiates efficiently; the goal is to reduce atmospheric
		IR trapping above it.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Deploy
		IR-transparent platforms above the Arctic.</span></p></li>
	</ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Atmospheric
	IR window enhancement:</strong></span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reduce
		stratospheric water vapor over the Arctic.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Remove
		aerosols that absorb IR.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Create
		a more transparent atmospheric path for IR to escape.</span></p></li>
	</ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Ocean
	radiative enhancement:</strong></span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">The
		Arctic Ocean radiates IR to the atmosphere.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Enhance
		this by reducing atmospheric IR absorption above the ocean.</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Deploy
		radiative cooling buoys or platforms.</span></p></li>
	</ul>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>B.
Permafrost Cooling:</strong></span></p>
<ol>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Ground
	heat exchangers:</strong></span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Install
		heat pipes or heat exchangers in permafrost regions.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Connect
		them to radiative cooling panels above.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">At
		night, the panels radiate heat to space, cooling the ground.</span></p></li>
	</ul>
	<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Albedo
	enhancement:</strong></span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Increase
		albedo of permafrost regions (clean snow, reflective coatings).</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Reduces
		solar absorption, keeping the ground colder.</span></p></li>
	</ul>
</ol>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><strong>Quantitative
Impact:</strong></span></p>
<ul>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Arctic
	sea ice extent has declined ~13% per decade.</span></p></li>
	<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">If
	we can reduce Arctic warming by even 0.5°C/decade, we could:</span></p>
	<ul>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Preserve
		significant sea ice area.</span></p></li>
		<li><p style="margin-bottom: 0cm; border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Prevent
		permafrost carbon release (~500–800 GtC potential).</span></p></li>
		<li><p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm">Stabilize
		Arctic ecosystems.</span></p></li>
	</ul>
</ul>
<p style="border: none; padding: 0cm"><span style="display: inline-block; border: none; padding: 0cm"><stro