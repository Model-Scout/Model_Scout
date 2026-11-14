---
base_model: ibm-granite/granite-4.2-30b
base_model_relation: quantized
quantized_by: Vultr
license: apache-2.0
pipeline_tag: text-generation
language:
  - en
  - de
  - es
  - fr
  - ja
  - pt
  - ar
  - cs
  - it
  - ko
  - nl
  - zh
tags:
  - gguf
  - llama.cpp
  - granite
---

# Granite 4.2 30B, GGUF

Granite 4.2 30B is the flagship reasoning model in the Granite 4.2 family, designed for advanced coding, mathematics, tool calling, agentic workflows, and multilingual dialogue. The architecture employs Grouped Query Attention, RoPE, and a SwiGLU feed-forward network, with native reasoning and flexible thinking modes for balancing quality and latency. It is optimized for complex long-context reasoning and enterprise applications.

This repository holds Vultr's GGUF quantizations of it. They are hybrid quantizations: rather than applying one precision to the whole network, each layer's precision is chosen from a measured importance score, so the bits go where they change the output most.

## Model Overview

<div class="dark:hidden" style="overflow-x:auto;">
<table style="display:table;width:auto;max-width:100%;border-collapse:collapse;border:none;border-radius:0;">
<thead>
<tr>
<th scope="col" style="padding:12px;text-align:left;background:#031059;color:#FFFFFF;border:none;border-right:1px solid #FFFFFF;">Attribute</th>
<th scope="col" style="padding:12px;text-align:left;background:#031059;color:#FFFFFF;border:none;">Value</th>
</tr>
</thead>
<tbody>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#EEFBFF;color:#031059;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;border-left:1px solid #C9F4FF;">Base model</th>
<td style="padding:10px 12px;text-align:left;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;"><a href="https://huggingface.co/ibm-granite/granite-4.2-30b">ibm-granite/granite-4.2-30b</a></td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#EEFBFF;color:#031059;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;border-left:1px solid #C9F4FF;">Architecture</th>
<td style="padding:10px 12px;text-align:left;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;">granite, dense</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#EEFBFF;color:#031059;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;border-left:1px solid #C9F4FF;">Parameters</th>
<td style="padding:10px 12px;text-align:left;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;">30B</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#EEFBFF;color:#031059;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;border-left:1px solid #C9F4FF;">Layers</th>
<td style="padding:10px 12px;text-align:left;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;">64</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#EEFBFF;color:#031059;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;border-left:1px solid #C9F4FF;">Hidden size</th>
<td style="padding:10px 12px;text-align:left;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;">4,096</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#EEFBFF;color:#031059;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;border-left:1px solid #C9F4FF;">Attention heads</th>
<td style="padding:10px 12px;text-align:left;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;">32</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#EEFBFF;color:#031059;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;border-left:1px solid #C9F4FF;">Key-value heads</th>
<td style="padding:10px 12px;text-align:left;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;">8</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#EEFBFF;color:#031059;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;border-left:1px solid #C9F4FF;">Context length</th>
<td style="padding:10px 12px;text-align:left;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;">128K native, with extension to 512K</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#EEFBFF;color:#031059;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;border-left:1px solid #C9F4FF;">Vocabulary</th>
<td style="padding:10px 12px;text-align:left;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;">100,352</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#EEFBFF;color:#031059;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;border-left:1px solid #C9F4FF;">RoPE theta</th>
<td style="padding:10px 12px;text-align:left;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;">50M</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#EEFBFF;color:#031059;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;border-left:1px solid #C9F4FF;">Feed-forward size</th>
<td style="padding:10px 12px;text-align:left;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;">32,768-dimensional</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#EEFBFF;color:#031059;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;border-left:1px solid #C9F4FF;">License</th>
<td style="padding:10px 12px;text-align:left;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;"><a href="https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/apache-2.0.md">Apache 2.0</a></td>
</tr>
</tbody>
</table>
</div>
<div class="hidden dark:block" style="overflow-x:auto;">
<table style="display:table;width:auto;max-width:100%;border-collapse:collapse;border:none;border-radius:0;">
<thead>
<tr>
<th scope="col" style="padding:12px;text-align:left;background:#031059;color:#FFFFFF;border:none;border-right:1px solid #1A3169;">Attribute</th>
<th scope="col" style="padding:12px;text-align:left;background:#031059;color:#FFFFFF;border:none;">Value</th>
</tr>
</thead>
<tbody>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#172147;color:#C9F4FF;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;border-left:1px solid #1A3169;">Base model</th>
<td style="padding:10px 12px;text-align:left;color:#B9C5DE;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;"><a href="https://huggingface.co/ibm-granite/granite-4.2-30b">ibm-granite/granite-4.2-30b</a></td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#172147;color:#C9F4FF;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;border-left:1px solid #1A3169;">Architecture</th>
<td style="padding:10px 12px;text-align:left;color:#B9C5DE;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;">granite, dense</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#172147;color:#C9F4FF;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;border-left:1px solid #1A3169;">Parameters</th>
<td style="padding:10px 12px;text-align:left;color:#B9C5DE;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;">30B</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#172147;color:#C9F4FF;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;border-left:1px solid #1A3169;">Layers</th>
<td style="padding:10px 12px;text-align:left;color:#B9C5DE;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;">64</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#172147;color:#C9F4FF;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;border-left:1px solid #1A3169;">Hidden size</th>
<td style="padding:10px 12px;text-align:left;color:#B9C5DE;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;">4,096</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#172147;color:#C9F4FF;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;border-left:1px solid #1A3169;">Attention heads</th>
<td style="padding:10px 12px;text-align:left;color:#B9C5DE;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;">32</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#172147;color:#C9F4FF;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;border-left:1px solid #1A3169;">Key-value heads</th>
<td style="padding:10px 12px;text-align:left;color:#B9C5DE;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;">8</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#172147;color:#C9F4FF;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;border-left:1px solid #1A3169;">Context length</th>
<td style="padding:10px 12px;text-align:left;color:#B9C5DE;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;">128K native, with extension to 512K</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#172147;color:#C9F4FF;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;border-left:1px solid #1A3169;">Vocabulary</th>
<td style="padding:10px 12px;text-align:left;color:#B9C5DE;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;">100,352</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#172147;color:#C9F4FF;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;border-left:1px solid #1A3169;">RoPE theta</th>
<td style="padding:10px 12px;text-align:left;color:#B9C5DE;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;">50M</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#172147;color:#C9F4FF;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;border-left:1px solid #1A3169;">Feed-forward size</th>
<td style="padding:10px 12px;text-align:left;color:#B9C5DE;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;">32,768-dimensional</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#172147;color:#C9F4FF;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;border-left:1px solid #1A3169;">License</th>
<td style="padding:10px 12px;text-align:left;color:#B9C5DE;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;"><a href="https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/apache-2.0.md">Apache 2.0</a></td>
</tr>
</tbody>
</table>
</div>

## Quantizations

<div class="dark:hidden" style="overflow-x:auto;">
<table style="display:table;width:auto;max-width:100%;border-collapse:collapse;border:none;border-radius:0;">
<thead>
<tr>
<th scope="col" style="padding:12px;text-align:left;background:#031059;color:#FFFFFF;border:none;border-right:1px solid #FFFFFF;">File</th>
<th scope="col" style="padding:12px;text-align:left;background:#031059;color:#FFFFFF;border:none;border-right:1px solid #FFFFFF;">Type</th>
<th scope="col" style="padding:12px;text-align:left;background:#031059;color:#FFFFFF;border:none;border-right:1px solid #FFFFFF;">Size</th>
<th scope="col" style="padding:12px;text-align:left;background:#031059;color:#FFFFFF;border:none;">KLD vs bf16</th>
</tr>
</thead>
<tbody>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#EEFBFF;color:#031059;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;border-left:1px solid #C9F4FF;">granite-4.2-30b-Q5_K_M.gguf</th>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#EEFBFF;color:#031059;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;">Q5_K_M</th>
<td style="padding:10px 12px;text-align:left;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;">22.73 GB</td>
<td style="padding:10px 12px;text-align:left;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;">0.0172</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#EEFBFF;color:#031059;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;border-left:1px solid #C9F4FF;">granite-4.2-30b-Q4_K_M.gguf</th>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#EEFBFF;color:#031059;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;">Q4_K_M</th>
<td style="padding:10px 12px;text-align:left;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;">19.22 GB</td>
<td style="padding:10px 12px;text-align:left;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;">0.0471</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#EEFBFF;color:#031059;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;border-left:1px solid #C9F4FF;">granite-4.2-30b-IQ3_M.gguf</th>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#EEFBFF;color:#031059;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;">IQ3_M</th>
<td style="padding:10px 12px;text-align:left;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;">14.37 GB</td>
<td style="padding:10px 12px;text-align:left;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;">0.1642</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#EEFBFF;color:#031059;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;border-left:1px solid #C9F4FF;">granite-4.2-30b-IQ3_S.gguf</th>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#EEFBFF;color:#031059;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;">IQ3_S</th>
<td style="padding:10px 12px;text-align:left;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;">14.06 GB</td>
<td style="padding:10px 12px;text-align:left;border-bottom:1px solid #C9F4FF;border-right:1px solid #C9F4FF;border-radius:0;">0.1674</td>
</tr>
</tbody>
</table>
</div>
<div class="hidden dark:block" style="overflow-x:auto;">
<table style="display:table;width:auto;max-width:100%;border-collapse:collapse;border:none;border-radius:0;">
<thead>
<tr>
<th scope="col" style="padding:12px;text-align:left;background:#031059;color:#FFFFFF;border:none;border-right:1px solid #1A3169;">File</th>
<th scope="col" style="padding:12px;text-align:left;background:#031059;color:#FFFFFF;border:none;border-right:1px solid #1A3169;">Type</th>
<th scope="col" style="padding:12px;text-align:left;background:#031059;color:#FFFFFF;border:none;border-right:1px solid #1A3169;">Size</th>
<th scope="col" style="padding:12px;text-align:left;background:#031059;color:#FFFFFF;border:none;">KLD vs bf16</th>
</tr>
</thead>
<tbody>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#172147;color:#C9F4FF;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;border-left:1px solid #1A3169;">granite-4.2-30b-Q5_K_M.gguf</th>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#172147;color:#C9F4FF;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;">Q5_K_M</th>
<td style="padding:10px 12px;text-align:left;color:#B9C5DE;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;">22.73 GB</td>
<td style="padding:10px 12px;text-align:left;color:#B9C5DE;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;">0.0172</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#172147;color:#C9F4FF;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;border-left:1px solid #1A3169;">granite-4.2-30b-Q4_K_M.gguf</th>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#172147;color:#C9F4FF;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;">Q4_K_M</th>
<td style="padding:10px 12px;text-align:left;color:#B9C5DE;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;">19.22 GB</td>
<td style="padding:10px 12px;text-align:left;color:#B9C5DE;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;">0.0471</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#172147;color:#C9F4FF;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;border-left:1px solid #1A3169;">granite-4.2-30b-IQ3_M.gguf</th>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#172147;color:#C9F4FF;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;">IQ3_M</th>
<td style="padding:10px 12px;text-align:left;color:#B9C5DE;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;">14.37 GB</td>
<td style="padding:10px 12px;text-align:left;color:#B9C5DE;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;">0.1642</td>
</tr>
<tr>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#172147;color:#C9F4FF;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;border-left:1px solid #1A3169;">granite-4.2-30b-IQ3_S.gguf</th>
<th scope="row" style="padding:10px 12px;text-align:left;font-weight:400;background:#172147;color:#C9F4FF;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;">IQ3_S</th>
<td style="padding:10px 12px;text-align:left;color:#B9C5DE;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;">14.06 GB</td>
<td style="padding:10px 12px;text-align:left;color:#B9C5DE;border-bottom:1px solid #1A3169;border-right:1px solid #1A3169;border-radius:0;">0.1674</td>
</tr>
</tbody>
</table>
</div>

KL divergence measures how far a quantized model's next-token probabilities drift from those of the original bf16 model, averaged over every token of the evaluation text. The lower the value, the closer the quantized model is to the original; zero would mean identical output.

## Evaluation

Every variant in this repository was evaluated against the original bf16 model for perplexity, KL divergence, top-token agreement, HellaSwag and WinoGrande, under identical conditions. The full results are maintained on the model's page in the Vultr Model Library:

**https://docs.vultr.com/models/ibm-granite-42/granite-4.2-30b?tab=quantized**

That page is the reference for these files. The summary above is an excerpt from it.

## Run

    llama-server -hf vultr/granite-4.2-30b-GGUF:Q4_K_M

The model's chat template is embedded in every file, so no extra prompt formatting is needed.

## License

These files are derived from [ibm-granite/granite-4.2-30b](https://huggingface.co/ibm-granite/granite-4.2-30b) and are distributed under the same license, [Apache 2.0](https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/apache-2.0.md). The model is the work of IBM Granite; Vultr produced the quantizations.
