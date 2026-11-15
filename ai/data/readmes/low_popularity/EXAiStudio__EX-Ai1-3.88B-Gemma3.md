---
license: gemma
base_model: google/gemma-3-4b-it
pipeline_tag: text-generation
tags:
  - gemma3
  - llama.cpp
  - ollama
  - conversational
  - multilingual
  - persian
  - farsi
  - chinese
  - iranian-culture
  - instruction-following
  - lora
  - gguf
language:
  - fa
  - en
  - zh
  - ru
  - ar
  - de
  - fr
  - es
  - pt
  - it
  - nl
  - pl
  - tr
  - uk
  - ur
  - hi
  - bn
  - pa
  - ta
  - te
  - mr
  - gu
  - ja
  - ko
  - vi
  - th
  - id
  - ms
  - fil
  - sw
  - ha
  - yo
  - ig
  - am
  - he
  - el
  - hy
  - ka
  - az
  - kk
  - uz
  - ky
  - tg
  - ps
  - ku
  - sd
  - si
  - ne
  - my
  - km
  - lo
  - mn
  - bo
  - ug
  - tt
  - ba
  - be
  - bg
  - cs
  - sk
  - sl
  - hr
  - sr
  - bs
  - mk
  - sq
  - ro
  - hu
  - fi
  - sv
  - no
  - da
  - is
  - et
  - lv
  - lt
  - ga
  - cy
  - gd
  - eu
  - ca
  - gl
  - af
  - zu
  - xh
  - sn
  - so
  - rw
  - ny
  - mg
  - mt
  - lb
  - eo
  - la
  - jv
  - su
  - ceb
  - haw
  - mi
  - sm
  - co
  - fy
  - gd
  - ht
  - hmn
  - iu
  - kl
  - fo
  - br
  - oc
  - sc
  - fur
  - ast
  - an
  - lmo
  - vec
  - nap
  - pms
  - scn
  - wa
  - rm
  - nds
  - bar
  - ksh
  - pdc
  - yi
  - lad
  - mdf
  - mrj
  - sah
  - crh
  - cv
  - mhr
  - myv
  - udm
  - alt
  - xal
  - kaa
  - krc
  - lez
  - av
  - ce
  - os
  - ab
  - ady
  - kab
  - ber
  - bm
  - wo
  - ff
  - ln
  - kg
  - ti
  - om
  - so
  - sg
  - sn
  - st
  - tn
  - ts
  - ve
  - nr
  - ss
  - kr
  - lu
  - rn
  - ny
  - toi
  - tum
  - mos
  - dag
  - ee
  - ak
  - tw
  - gaa
  - fon
  - din
  - dyo
  - kmb
  - umb
  - bem
  - loz
  - lua
  - tsn
  - war
  - hil
  - ilo
  - pam
  - bcl
  - min
  - bug
  - mad
  - ace
  - ban
  - tet
  - pap
  - srd
  - hrv
  - mfe
  - prs
  - ckb
  - bal
  - brh
  - bra
  - doi
  - kok
  - mai
  - mni
  - as
  - or
  - sa
  - ks
  - sd
  - bho
  - awa
  - mag
  - lus
  - kha
  - sat
  - dz
  - dv
  - ug
  - sah
  - ch
  - gv
---

# EX-Ai1-3.88B-Gemma3

> EN — A LoRA fine-tuned Gemma 3 4B by EXAiStudio, optimized for Persian fluency, instruction-following, multilingual communication, intermediate Iranian cultural awareness, and reducing model hallucinations.
>
> FA — نسخه فاین‌تیون‌شده Gemma 3 4B توسط EXAiStudio که برای بهبود روانی زبان فارسی، دستورپذیری، ارتباط چندزبانه، آشنایی متوسط با فرهنگ ایرانی و کاهش توهم‌های مدل بهینه‌سازی شده است.
>
> ZH — 由 EXAiStudio 基于 Gemma 3 4B 进行 LoRA 微调的模型，重点提升波斯语流畅度、指令遵循、多语言交流能力、对伊朗文化的中级认知，并减少模型幻觉。

> ⚠️ Note on naming — The `3.88B` in the model name refers to the effective parameter count of the Gemma 3 4B base model. Google markets it as "4B", but the actual parameter count is approximately 3.88B.

---

## 🇬🇧 English

### 📌 Model Details

| Property | Value |
|---|---|
| Developed by | EXAiStudio |
| Model type | Causal Language Model (Decoder-only Transformer) |
| Base model | [google/gemma-3-4b-it](https://huggingface.co/google/gemma-3-4b-it) |
| Parameters | 3.88B |
| Architecture | Gemma 3 (decoder-only Transformer, GQA, RoPE) |
| Context length | 128,000 tokens (same as base model) |
| Fine-tuning method | LoRA |
| Language coverage | Multilingual, inherited from Gemma 3 pretraining |
| Fine-tuning focus | Persian fluency, instruction-following, Iranian culture, hallucination reduction |
| License | [Gemma Terms of Use](https://ai.google.dev/gemma/terms) |
| Version | V1.0 |
| Release date | October 22, 2026 |
| Format | GGUF (Q4_K_M only) |

### 🌐 Multilingual Coverage

EX-Ai1-3.88B-Gemma3 is derived from Gemma 3, a multilingual model family pretrained on data covering more than 140 languages.

The base model's multilingual capabilities may support communication, text generation, comprehension, and translation across a wide range of languages. The EXAiStudio fine-tuning specifically focuses on Persian fluency, instruction-following, Iranian cultural awareness, and reducing hallucinations.

Examples of languages within the broader multilingual landscape include:

- **Major international languages:** English, Spanish, French, German, Portuguese, Italian, Dutch, Russian, Chinese (Simplified and Traditional), Japanese, Korean, Arabic, Persian, Turkish, Hindi, Urdu, Bengali, Indonesian, Vietnamese, Thai, Swahili, and Filipino.
- **European languages:** Polish, Ukrainian, Romanian, Czech, Slovak, Hungarian, Bulgarian, Serbian, Croatian, Bosnian, Slovenian, Albanian, Greek, Swedish, Norwegian, Danish, Finnish, Icelandic, Estonian, Latvian, Lithuanian, Irish, Welsh, Scottish Gaelic, Catalan, Galician, Basque, Luxembourgish, Maltese, and Esperanto.
- **South and Central Asian languages:** Pashto, Kurdish, Tajik, Uzbek, Kazakh, Kyrgyz, Turkmen, Azerbaijani, Armenian, Georgian, Nepali, Sinhala, Punjabi, Gujarati, Marathi, Assamese, Odia, Tamil, Telugu, Kannada, Malayalam, and Mongolian.
- **Southeast and East Asian languages:** Burmese, Khmer, Lao, Javanese, Sundanese, Malay, Cebuano, Hmong, Tibetan, and Uyghur.
- **African languages:** Afrikaans, Amharic, Hausa, Yoruba, Igbo, Somali, Oromo, Kinyarwanda, Malagasy, Zulu, Xhosa, Shona, Sesotho, Setswana, Wolof, Bambara, and Lingala.
- **Additional regional and historical languages:** Latin, Yiddish, Māori, Hawaiian, Samoan, Tatar, Bashkir, Chechen, Ossetian, Breton, Occitan, Friulian, Sardinian, Romansh, and other regional languages.

This list is illustrative rather than exhaustive. It does not imply that every language listed has been individually tested or fine-tuned by EXAiStudio.

**Important:** Language coverage and language quality are not the same. Performance can vary considerably by language, dialect, writing system, task, and available training data. Persian is a primary focus of this fine-tuning, while equal performance across all languages is not guaranteed.

### Description

EX-Ai1-3.88B-Gemma3 is a lightweight language model derived from Gemma 3 4B. It was fine-tuned with a LoRA adapter using a curated proprietary dataset of approximately 2,700 samples developed by NT Ai on commission for EXAiStudio.

The fine-tuning focused on:

- Strengthening Persian (Farsi) language quality and fluency.
- Improving instruction-following across structured tasks.
- Introducing intermediate Iranian cultural awareness, including customs, expressions, and cultural references.
- Reducing model hallucinations and improving the reliability of generated responses.
- Preserving and utilizing the multilingual capabilities inherited from the Gemma 3 base model.

The model is designed to provide a practical balance between response quality and computational requirements. With Q4_K_M quantization, it can be deployed on compatible consumer hardware, including mid-range GPUs and supported Apple Silicon systems.

Hallucination reduction is a training objective and an observed target of the fine-tuning process; it does not mean that the model is completely free of hallucinations or that every response is guaranteed to be correct.

### 🎯 Intended Use

#### ✅ Direct Use

- Persian, English, and multilingual conversational assistants.
- Persian-language content generation and rewriting.
- Culturally aware Persian content generation.
- Structured instruction-following, including question answering and summarization.
- Translation and multilingual text assistance, subject to language-specific performance.
- General-purpose text generation and comprehension.
- Local and offline deployment through Ollama, llama.cpp, or LM Studio.
- Applications that benefit from reduced hallucination tendencies, with independent verification where accuracy is important.

#### ❌ Out-of-Scope Use

- Highly advanced mathematics and symbolic computation without additional verification.
- Unverified medical, legal, financial, or psychological advice.
- High-stakes automated decision-making.
- Safety-critical systems.
- Treating generated responses as guaranteed facts.
- Assuming equal quality across all supported or inherited languages.

### 🏋️ Training Details

- **Source:** Proprietary dataset from NT Ai, commissioned by EXAiStudio.
- **Dataset size:** Approximately 2,700 curated samples.
- **Fine-tuning method:** LoRA.
- **Focus areas:** Persian fluency, instruction-following, Iranian cultural awareness, and hallucination reduction.
- **Multilingual capability:** Inherited from Gemma 3 pretraining.
- **Maximum sequence length:** Same as the base model.
- **Hardware:** 1 × NVIDIA Tesla T4 (16 GB VRAM).
- **Training time:** Approximately 1 hour and 45 minutes.
- **Base model:** Gemma 3 4B Instruct (full precision).

#### Fine-Tuning Objectives and Improvements

The fine-tuning process was designed to improve the base model in several areas:

1. **Persian language quality:** Improve fluency, phrasing, and natural language generation in Persian.
2. **Instruction-following:** Improve the model's ability to understand and follow user instructions, particularly structured tasks.
3. **Iranian cultural awareness:** Improve familiarity with Iranian customs, expressions, and cultural references.
4. **Hallucination reduction:** Reduce the tendency to generate fabricated or unsupported information and improve response reliability.
5. **Multilingual usability:** Retain the multilingual foundation of Gemma 3 while prioritizing the specific objectives of the EXAiStudio fine-tuning.

These improvements do not eliminate all model errors or guarantee factual accuracy. Independent evaluations are required to quantify the extent of improvement across languages and tasks.

> Detailed hyperparameters, including LoRA rank, alpha, learning rate, epochs, and optimizer, are not disclosed at this time.

### 💻 How to Use

#### Ollama

```bash
ollama run hf.co/EXAiStudio/EX-Ai1-3.88B-Gemma3:Q4_K_M
```

#### llama.cpp

```bash
llama serve -hf EXAiStudio/EX-Ai1-3.88B-Gemma3:Q4_K_M
```

For additional deployment options, refer to the documentation for [llama.cpp](https://github.com/ggml-org/llama.cpp), [Ollama](https://ollama.com/), and [Hugging Face](https://huggingface.co/).

---

## Model Information and Limitations

- **Model family:** Gemma 3.
- **Parameter count:** Approximately 3.88 billion.
- **Context window:** Up to 128,000 tokens, inherited from the base model.
- **Quantization:** Q4_K_M.
- **License:** Subject to the applicable Gemma Terms of Use.
- **Language performance:** Varies by language and task.
- **Hallucinations:** Reduced hallucination tendencies are a fine-tuning objective, not a guarantee of factual correctness.

Developers should independently evaluate the model for their intended use cases before deployment, particularly where factual accuracy, multilingual reliability, or safety is important.

## Acknowledgements

- **Google DeepMind:** For the Gemma 3 base model.
- **NT Ai:** For developing the proprietary dataset commissioned by EXAiStudio.
- **EXAiStudio:** For the fine-tuning, development, and release of EX-Ai1-3.88B-Gemma3.