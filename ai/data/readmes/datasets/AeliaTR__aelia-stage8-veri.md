---
license: apache-2.0
task_categories:
- text-generation
language:
- tr
- en
- it
- es
- pt
- ru
- de
- zh
- ja
- ar
- fr
- ko
pretty_name: AELIA Stage 8 - AeLLM 1.08 Agent
---

# AELIA Stage 8 - AeLLM 1.08 Ajan verisi

`AeliaTR` ajan modeli (AeLLM 1.08) icin **iki dosya**:

| dosya | satir | rol |
|---|---|---|
| `STAGE_8_AGENT_MASTER.jsonl` | 15000 | SFT QLoRA |
| `STAGE_8_GRPO_VERI.jsonl` | 2000 | GRPO (odul fonksiyonlu) |

## 1) STAGE_8_AGENT_MASTER.jsonl

- kategori: `tool` 9000, `rag` 2250, `kimlik` 1500, `sohbet` 1500, `replay` 750
- dil: `ar` 125, `de` 125, `en` 3675, `es` 125, `fr` 125, `it` 125, `ja` 125, `ko` 125, `pt` 125, `ru` 125, `tr` 10075, `zh` 125
- sha256: `893b2400f08b8cb304737815652e53681045cadd1f43e40726b92fabbf8ad9b5`

Satir semasi (`messages` OpenAI sohbet formatinda):

```json
{"id": "s8-tr-tr10k-0001", "dil": "tr", "kategori": "tool",
 "kaynak": "tr10k", "kaynak_tur": "tool_call",
 "system": "...", "tools": [{"type": "function", "function": {...}}],
 "messages": [{"role": "user", "content": "..."},
              {"role": "assistant", "content": null,
               "tool_calls": [{"type": "function",
                               "function": {"name": "...", "arguments": "{...}"}}]}],
 "arac": "get_weather", "cok_adimli": false}
```

RAG satirlarinda kullanici turu `<context>[1]..[3]</context>` tasir; asistan turu
`<think>...</think>` gerekcesi + `Cevap: ... [1]` bicimindedir (yalniz guvenilir
kaynaga atif; `[2]` cop, `[3]` reklam).

## 2) STAGE_8_GRPO_VERI.jsonl

- tur: matematik 1000 (tam sayi cevap) + tool 1000
- dil: `tr` 1786, `en` 214
- sha256: `28a47d63d955d569176e21619f5913e0266f72f91a90175039dcb4ac31eb9b9b`
- tool satirlari SFT master'i ile **cakismaz** (ayni tohumla disarida birakildi).

```json
{"id": "s8-grpo-tool-0001", "tur": "tool", "dil": "tr", "tools": [...],
 "prompt": [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}],
 "beklenen": {"arac": "get_weather", "arguments": {"sehir": "Ankara"}},
 "cozuldu": true, "denetim": "json_esitligi"}
```

`prompt` alani GRPO egitiminde `apply_chat_template(prompt, tools=tools)` ile
render edilir; `beklenen`/`cevap` alanlari odul fonksiyonuna kwargs olarak gecer.

## Kullanim

```python
from huggingface_hub import hf_hub_download
m = hf_hub_download("AeliaTR/aelia-stage8-veri", "STAGE_8_AGENT_MASTER.jsonl",
                    repo_type="dataset")
```

Colab defteri: `colab_llm_agent_stage8.ipynb` (SFT QLoRA -> GRPO).

## Uyari

- Kimlik satirlari (`kategori=kimlik`) kurgusal bir marka/persona tanimi icerir;
  ticari kullanimda kendi marka metninizle degistirin.
- Tool semalari kamuya acik korpuslardan (Glaive v2, arcee, TR BFCL, enstitu)
  turetilmistir; parametre degerleri sentetiktir (gercek musteri verisi yoktur).
