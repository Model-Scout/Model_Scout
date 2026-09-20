---
pipeline_tag: automatic-speech-recognition
library_name: transformers
license: other
license_name: meralion-3-public-licence
license_link: https://huggingface.co/datasets/MERaLiON/MERaLiON_Public_Licence/blob/main/MERaLiON-3-Public-Licence.pdf
tags:
  - meralion3
  - meralion
  - audio
  - asr
  - southeast-asian
  - code-switching
language:
  - en
  - zh
  - ms
  - ta
  - id
  - th
  - vi
  - yue
  - nan
arxiv:
  - 2412.09818
  - 2501.01034
  - 2409.06635
---

# MERaLiON-3-ASR

**MERaLiON-3-ASR** is the speech-recognition line in the MERaLiON-3 generation of Speech-Text Large Language Models, developed by I2R, A\*STAR, Singapore. It is purpose-built for Singapore- and Southeast-Asia-centric ASR, with broad coverage across regional languages, dialects, and natural conversational code-switching.

**Coverage**

- **Languages:** English (Global and Singapore), Mandarin, Malay, Tamil, Indonesian, Thai, Vietnamese
- **Chinese dialects:** Cantonese, Hokkien
- **Code-switching:** natural conversational English ↔ {Mandarin, Malay, Tamil, Vietnamese, Cantonese, Hokkien} mixtures, including Singlish

## MERaLiON-3-ASR-API

**MERaLiON-3-ASR-API** is the hosted production endpoint, tuned for real-time and enterprise transcription workloads.

- **Fast streaming ASR**, ~600 ms first-token latency for interactive use cases.
- **Long-form decoding** for continuous audio up to multiple hours.
- **Word- and segment-level timestamps** with **speaker diarization** for offline transcription.
- **Reinforced regional-dialect recognition** for Cantonese and Hokkien.
- **State-of-the-art Southeast Asian code-switching** performance.

On the locked evaluation suite, MERaLiON-3-ASR-API achieves the lowest mean Word Error Rate among all systems tested on English (Singapore) (12.52, vs. 25.97 / 27.34 for Gemini 3.5 Flash / GPT-4o), Cantonese (10.42, best of all systems), Hokkien (36.43, vs. 46.50 next best), and Code-switching (20.87, vs. 22.65 / 31.14). On Healthcare it is statistically tied with Gemini 3.5 Flash (20.47 vs. 20.04, within 0.5 pp).

## MERaLiON-3-3B-ASR

**MERaLiON-3-3B-ASR** is the open-weights release published in this repository. At roughly one-third the size of its predecessor MERaLiON-2-10B-ASR, it matches or improves over the larger model on every evaluation section, with the largest gains concentrated where they matter most for the Southeast Asian setting:

| Section | MERaLiON-2-10B-ASR | MERaLiON-3-3B-ASR | Δ (pp) |
|---|---:|---:|---:|
| Thai | 35.07 | **7.55** | **−27.5** |
| Hokkien | 59.32 | **46.50** | **−12.8** |
| Cantonese | 18.55 | **11.27** | **−7.3** |
| Code-switching | 26.24 | **22.65** | **−3.6** |
| Tamil | 28.29 | **25.83** | **−2.5** |

The smaller footprint makes the open model practical for self-hosting on a single 80 GB GPU.

## Performance

![ASR WER comparison across 12 language and domain sections](assets/meralion_hf_comparison.png)

The figure reports mean Word Error Rate (lower is better) across twelve language and domain sections, covering 66 evaluation datasets in total. Datasets in the Healthcare and Code-switching sections also appear in their primary language section, so they contribute to both. The full per-dataset breakdown is at [SEA-SpeechBench](https://github.com/SEA-SpeechBench/SEA-SpeechBench).

The table below reports per-dataset Word/Character Error Rate (lower is better) for Cantonese and Hokkien — the two regional Chinese dialects where MERaLiON-3 shows its largest relative advantage. The best result on each row is highlighted.

<div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;max-width:1000px;margin:0 auto;padding:16px 0">
<table style="width:100%;border-collapse:collapse;font-size:13px">
<thead><tr>
<th style="padding:10px 7px;text-align:left;font-weight:600;border-bottom:2px solid #1e6f8b;color:#1e6f8b"></th><th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #1e6f8b;color:#1e6f8b;font-size:14px">MERaLiON-3-ASR-API</th><th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #1e6f8b;color:#1e6f8b;font-size:14px">MERaLiON-3-3B-ASR</th><th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #1e6f8b;color:#1e6f8b;font-size:14px">MERaLiON-2-10B-ASR</th><th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #1e6f8b;color:#1e6f8b;font-size:14px">Qwen3-ASR</th><th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #1e6f8b;color:#1e6f8b;font-size:14px">gpt-4o</th><th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #1e6f8b;color:#1e6f8b;font-size:14px">gpt-audio-1.5</th><th style="padding:10px 7px;text-align:center;font-weight:500;border-bottom:2px solid #1e6f8b;color:#1e6f8b;font-size:14px">gemini-3.5-flash</th></tr></thead>
<tbody>
<tr><td colspan="8" style="padding:8px 12px;font-weight:600;color:#1e6f8b;border-bottom:1px solid rgba(30, 111, 139, 0.2);background:rgba(30, 111, 139, 0.10)">Cantonese</td></tr>
<tr>
<td style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);font-family:monospace">cv21_cantonese_test</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">11.65</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">13.88</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">18.29</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">25.08</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);color:#1e6f8b;font-weight:700">8.74</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">21.96</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">20.34</td>
</tr>
<tr>
<td style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);font-family:monospace">fleurs_cantonese_test</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">8.75</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">8.93</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">10.53</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">11.30</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);color:#1e6f8b;font-weight:700">6.31</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">7.55</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">9.63</td>
</tr>
<tr>
<td style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);font-family:monospace">mdcc_cantonese_test</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);color:#1e6f8b;font-weight:700">4.95</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">5.11</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">6.95</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">8.67</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">7.56</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">18.51</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">11.27</td>
</tr>
<tr>
<td style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);font-family:monospace">wsyue_long_test</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);color:#1e6f8b;font-weight:700">9.37</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">9.76</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">18.17</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">11.66</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">25.16</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">29.59</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">14.66</td>
</tr>
<tr>
<td style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);font-family:monospace">wsyue_short_test</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);color:#1e6f8b;font-weight:700">11.19</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">12.56</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">24.55</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">17.77</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">18.23</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">33.99</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">31.01</td>
</tr>
<tr>
<td style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);font-family:monospace">ytb_asr_cantonese_short_v3</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);color:#1e6f8b;font-weight:700">16.63</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">17.38</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">32.83</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">16.92</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">35.48</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">38.66</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">19.87</td>
</tr>
<tr><td colspan="8" style="padding:8px 12px;font-weight:600;color:#1e6f8b;border-bottom:1px solid rgba(30, 111, 139, 0.2);background:rgba(30, 111, 139, 0.10)">Hokkien</td></tr>
<tr>
<td style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);font-family:monospace">sarahwei_minnan_test</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);color:#1e6f8b;font-weight:700">18.93</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">22.58</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">49.47</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">66.17</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">44.93</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">77.26</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">46.38</td>
</tr>
<tr>
<td style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);font-family:monospace">taiwan_tongues_hokkien_test</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);color:#1e6f8b;font-weight:700">51.64</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">58.64</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">63.90</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">99.05</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">66.41</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">109.41</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">73.40</td>
</tr>
<tr>
<td style="padding:7px 7px;padding-left:20px;border-bottom:1px solid rgba(128, 128, 128, 0.15);font-family:monospace">ytb_asr_hokkien_happycanalready_s4</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15);color:#1e6f8b;font-weight:700">38.72</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">58.30</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">64.58</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">128.21</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">78.89</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">68.55</td>
<td style="padding:7px 7px;text-align:center;border-bottom:1px solid rgba(128, 128, 128, 0.15)">63.37</td>
</tr>
</tbody>
</table>
</div>

### Qualitative examples

The four clips below illustrate cases where MERaLiON-3-ASR-API produces the most accurate transcript, MERaLiON-3-3B-ASR a near-equivalent transcript with one or two character-level differences, and a leading general-purpose model produces a substantially less faithful transcript.

<div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;max-width:1000px;margin:0 auto;padding:16px 0">
<h4 style="margin:18px 0 6px 0;color:#1e6f8b">Cantonese (with code-switching to English)</h4>
<audio controls preload="none" src="https://huggingface.co/MERaLiON/MERaLiON-3-3B-ASR/resolve/main/assets/samples/1_cantonese.wav" style="width:100%;max-width:520px"></audio>
<table style="width:100%;border-collapse:collapse;font-size:13px;margin:6px 0 4px 0">
<tbody>
<tr>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);color:#444;font-weight:600;width:170px;white-space:nowrap;vertical-align:top">Reference</td>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);font-family:monospace">嚟我公司，In-house PR Director，有冇兴趣？ 哇，你问得咁直接，我唔怕直接答啊。</td>
</tr>
<tr>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);color:#1e6f8b;;width:170px;white-space:nowrap;vertical-align:top">MERaLiON-3-ASR-API</td>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);font-family:monospace">嚟我公司，in-house PR director，有冇兴趣？你问得咁直接，我又唔怕直接答啊。</td>
</tr>
<tr>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);color:#444;;width:170px;white-space:nowrap;vertical-align:top">MERaLiON-3-3B-ASR</td>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);font-family:monospace">嚟我公司 in house p r director 有冇兴趣你问得咁直接我用唔怕直接答啊。</td>
</tr>
<tr>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);color:#888;;width:170px;white-space:nowrap;vertical-align:top">gemini-3.5-flash</td>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);font-family:monospace">你間公司 In-house PR director 係咪呀？你問得咁直接，我好難直接答呀。</td>
</tr>
</tbody></table>
<h4 style="margin:18px 0 6px 0;color:#1e6f8b">Hokkien (with code-switching to English)</h4>
<audio controls preload="none" src="https://huggingface.co/MERaLiON/MERaLiON-3-3B-ASR/resolve/main/assets/samples/2_hokkien.wav" style="width:100%;max-width:520px"></audio>
<table style="width:100%;border-collapse:collapse;font-size:13px;margin:6px 0 4px 0">
<tbody>
<tr>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);color:#444;font-weight:600;width:170px;white-space:nowrap;vertical-align:top">Reference</td>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);font-family:monospace">我……我……我新来的 recruit 啦！按怎无戴 helmet？ 我……我袂使戴！我一戴，人就认袂出是我了！哈哈哈！我是……我是 recruit 梁婆婆！哈哈哈！人夯 full pack，按怎汝无 full pack？ 有啊！我这个就是 full pack 啦！哈哈哈！</td>
</tr>
<tr>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);color:#1e6f8b;;width:170px;white-space:nowrap;vertical-align:top">MERaLiON-3-ASR-API</td>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);font-family:monospace">我啊，我是来 recruit 啊！安怎无带 helmet？我未使带，我一个带人欲啉袂出是我了！哈哈哈！我是、我是 recruit，梁某无！哈哈哈！人提 full pack，安怎汝无 full pack？我有啊！我即个就是 full pack 啊！哈哈哈！</td>
</tr>
<tr>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);color:#444;;width:170px;white-space:nowrap;vertical-align:top">MERaLiON-3-3B-ASR</td>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);font-family:monospace">我是哪的 recruit 啊按怎没有 helmet 我是 recruit 咩有 full pack 按怎你没有 full pack 我有啊我今天就是 full pack。</td>
</tr>
<tr>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);color:#888;;width:170px;white-space:nowrap;vertical-align:top">gemini-3.5-flash</td>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);font-family:monospace">Oh my god, 我是那一個 record。安仔，無 feedback 係點呀？Oh my god, 乜嘢 feedback 呀？我係，我係 record 嗰個。人哋有 feedback，你點解無 feedback 呀？Oh my god, 我呢個就係 feedback。</td>
</tr>
</tbody></table>
<h4 style="margin:18px 0 6px 0;color:#1e6f8b">Code-switching (Tamil + English)</h4>
<audio controls preload="none" src="https://huggingface.co/MERaLiON/MERaLiON-3-3B-ASR/resolve/main/assets/samples/3_codeswitch_tamil.wav" style="width:100%;max-width:520px"></audio>
<table style="width:100%;border-collapse:collapse;font-size:13px;margin:6px 0 4px 0">
<tbody>
<tr>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);color:#444;font-weight:600;width:170px;white-space:nowrap">Reference</td>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);font-family:monospace">நாம்ம என்ன snacks வீட்ல சைரோ எல்லா snacks கூட குடுக்கலாம்</td>
</tr>
<tr>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);color:#1e6f8b;;width:170px;white-space:nowrap">MERaLiON-3-ASR-API</td>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);font-family:monospace">நம்ம என்ன snacks வீட்ல சேரு எல்லா snacks கூட கொடுக்கலாம்.</td>
</tr>
<tr>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);color:#444;;width:170px;white-space:nowrap">MERaLiON-3-3B-ASR</td>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);font-family:monospace">நம்ம என்ன snacks வீட்ல சேர்ற எல்லா snacks கூட குடுக்கலாம்.</td>
</tr>
<tr>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);color:#888;;width:170px;white-space:nowrap">gemini-3.5-flash</td>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);font-family:monospace">நம்ம என்ன ஸ்நாக்ஸ் வீட்டுல செய்யற எல்லா ஸ்நாக்ஸ் கூட கொடுக்கலாம்</td>
</tr>
</tbody></table>
<h4 style="margin:18px 0 6px 0;color:#1e6f8b">Code-switching (English + Mandarin)</h4>
<audio controls preload="none" src="https://huggingface.co/MERaLiON/MERaLiON-3-3B-ASR/resolve/main/assets/samples/4_codeswitch_singlish.wav" style="width:100%;max-width:520px"></audio>
<table style="width:100%;border-collapse:collapse;font-size:13px;margin:6px 0 4px 0">
<tbody>
<tr>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);color:#444;font-weight:600;width:170px;white-space:nowrap">Reference</td>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);font-family:monospace">there's like two quarters 嘛 then 他 会 教</td>
</tr>
<tr>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);color:#1e6f8b;;width:170px;white-space:nowrap">MERaLiON-3-ASR-API</td>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);font-family:monospace">there's like two quarters (mah) then 他会教。</td>
</tr>
<tr>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);color:#444;;width:170px;white-space:nowrap">MERaLiON-3-3B-ASR</td>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);font-family:monospace">there's like two quarters (mah) then 他会叫。</td>
</tr>
<tr>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);color:#888;;width:170px;white-space:nowrap">gemini-3.5-flash</td>
<td style="padding:4px 10px;border-bottom:1px solid rgba(128, 128, 128, 0.15);font-family:monospace">that's like two quarters then how would you</td>
</tr>
</tbody></table>
</div>

## A note on the code-switching benchmark

The code-switching section aggregates 13 datasets of natural Southeast Asian conversational speech, totalling 5,430 samples / 35.4 hours, in which English is mixed organically with another SEA language. Coverage by direction:

| Code-switch direction | Samples | Hours |
|---|---:|---:|
| EN ↔ Mandarin (incl. SEAME) | 506 | 5.3 |
| IMDA Part 4 (Singlish, EN ↔ Mandarin) | 1,000 | 7.3 |
| EN ↔ Tamil | 2,184 | 9.0 |
| EN ↔ Cantonese | 904 | 6.2 |
| EN ↔ Hokkien | 536 | 3.7 |
| EN ↔ Malay | 200 | 2.6 |
| EN ↔ Vietnamese | 100 | 1.3 |

The benchmark is intended to capture real-world SEA usage patterns rather than synthetic alternation between scripts. Of the constituent corpora, only [IMDA Part 4 (NSC)](https://www.imda.gov.sg/how-we-can-help/national-speech-corpus) is publicly available; the remaining datasets are proprietary or curated in-house. Per-sample normalisation and scoring scripts for the whole evaluation are available at [SEA-SpeechBench](https://github.com/SEA-SpeechBench/SEA-SpeechBench).

## Model Description

| Property | Value |
|----------|-------|
| Audio format | Mono, 16,000 Hz |
| Parameters | 3 B |
| Precision | BF16 |
| Supported languages | English (Global + Singapore), Mandarin, Malay, Tamil, Indonesian, Thai, Vietnamese, Cantonese, Hokkien |
| Supported backend | vLLM |

The model is trained as an ASR-optimised fine-tune over a multilingual mixture of curated Southeast Asian speech data, with particular emphasis on Singapore English, regional dialects (Cantonese, Hokkien), and natural English-X code-switching.

## How to Use

The recommended way to run MERaLiON-3-3B-ASR is through the [`meralion-3-asr`](https://github.com/YingxuH/MERaLiON-3-ASR) Python package, which wraps a vLLM backend tuned for this model. Install from PyPI:

```bash
pip install meralion-3-asr
```

The package pre-wires the transcription prompt, decoding configuration, no-repeat-ngram guard, and 30 s audio chunking — on both the offline path and the served path. Callers only provide audio.

### 1. Offline batch (in-process vLLM)

```python
from meralion_3_asr import Meralion3ASR

model = Meralion3ASR.from_pretrained("MERaLiON/MERaLiON-3-3B-ASR", backend="vllm")

text = model.transcribe("audio.wav")                          # str
texts = model.transcribe_batch(["a.wav", "b.wav", "c.wav"])   # List[str]
```

Inputs may be local file paths, `https://` URLs, base64 data URLs, or `(numpy_array, sample_rate)` tuples. Audio is automatically resampled to mono 16 kHz; long files are chunked transparently.

### 2. Serving via the bundled sidecar

`meralion-3-asr serve` starts a FastAPI sidecar fronting an internal `vllm serve` process. The sidecar exposes a single OpenAI-compatible endpoint, `/v1/audio/transcriptions`, applies 30 s non-overlapping chunking server-side, and forwards each chunk to the internal vLLM. Clients send audio only — no prompt, no decoding flags.

```bash
meralion-3-asr serve --model MERaLiON/MERaLiON-3-3B-ASR --port 8000
```

OpenAI Python SDK:

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")

with open("audio.wav", "rb") as f:
    resp = client.audio.transcriptions.create(
        model="MERaLiON/MERaLiON-3-3B-ASR",
        file=f,
    )
print(resp.text)
```

curl:

```bash
curl -s -X POST http://localhost:8000/v1/audio/transcriptions \
    -F "model=MERaLiON/MERaLiON-3-3B-ASR" \
    -F "file=@audio.wav" \
  | jq -r .text
```

### 3. Transformers backend

vLLM (above) is the recommended backend. A pure `transformers` backend is also available — it loads the model in-process with `AutoModelForSpeechSeq2Seq`, which is convenient for debugging or environments without vLLM:

```python
from meralion_3_asr import Meralion3ASR

model = Meralion3ASR.from_pretrained("MERaLiON/MERaLiON-3-3B-ASR", backend="transformers")

text = model.transcribe("audio.wav")                          # str
texts = model.transcribe_batch(["a.wav", "b.wav", "c.wav"])   # List[str]
```

The same prompt, decoding configuration, and 30 s chunking are applied on both backends.

## Hardware & Infrastructure

MERaLiON-3 was trained on the **ASPIRE 2A+** supercomputer cluster at the National Supercomputing Centre (NSCC), Singapore, hosted by A\*STAR I2R:

- **GPUs**: 128 Nvidia H100 GPUs (16 nodes × 8 H100)
- **Memory**: 2 TB RAM per node
- **Storage**: 30 TB NVMe per node + 2.5 PB SSD-based Lustre filesystem
- **Interconnect**: 400 Gb/s NDR InfiniBand (full fat-tree topology)

## Related Resources

- [meralion-3-asr Python package (GitHub)](https://github.com/YingxuH/MERaLiON-3-ASR)
- [SEA-SpeechBench evaluation harness](https://github.com/SEA-SpeechBench/SEA-SpeechBench)
- Related models:
  - [MERaLiON-2-10B-ASR](https://huggingface.co/MERaLiON/MERaLiON-2-10B-ASR)
  - [MERaLiON-2-3B](https://huggingface.co/MERaLiON/MERaLiON-2-3B)
  - [MERaLiON-2-10B](https://huggingface.co/MERaLiON/MERaLiON-2-10B)

## License

[MERaLiON-3-Public-Licence](https://huggingface.co/datasets/MERaLiON/MERaLiON_Public_Licence/blob/main/MERaLiON-3-Public-Licence.pdf)

## Disclaimer

⚠️ MERaLiON-3-3B-ASR has not been specifically aligned for safety and may transcribe content that is inappropriate, offensive, or harmful. Developers and users are responsible for performing their own safety fine-tuning and implementing necessary security measures. The authors shall not be held liable for any claims, damages, or other liabilities arising from the use of the released models, weights, or code.

## Citation

If you use MERaLiON-3-3B-ASR in your work, please cite the foundational MERaLiON references:

```bibtex
@misc{he2024meralionaudiollmtechnicalreport,
      title={MERaLiON-AudioLLM: Bridging Audio and Language with Large Language Models},
      author={{MERaLiON Team}},
      year={2024},
      eprint={2412.09818},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2412.09818},
}

@article{wang2024audiobench,
    title={AudioBench: A Universal Benchmark for Audio Large Language Models},
    author={Wang, Bin and Zou, Xunlong and Lin, Geyu and Sun, Shuo and Liu, Zhuohan and Zhang, Wenyu and Liu, Zhengyuan and Aw, AiTi and Chen, Nancy F},
    journal={NAACL},
    year={2025}
}

@article{wang2025advancing,
    title={Advancing Singlish Understanding: Bridging the Gap with Datasets and Multimodal Models},
    author={Wang, Bin and Zou, Xunlong and Sun, Shuo and Zhang, Wenyu and He, Yingxu and Liu, Zhuohan and Wei, Chengwei and Chen, Nancy F and Aw, AiTi},
    journal={arXiv preprint arXiv:2501.01034},
    year={2025}
}

@article{zhang2024mowe,
    title={MoWE-Audio: Multitask AudioLLMs with Mixture of Weak Encoders},
    author={Zhang, Wenyu and Sun, Shuo and Wang, Bin and Zou, Xunlong and Liu, Zhuohan and He, Yingxu and Lin, Geyu and Chen, Nancy F and Aw, Ai Ti},
    journal={ICASSP},
    year={2025}
}
```
