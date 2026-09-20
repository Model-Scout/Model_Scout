
---
library_name: gguf
license: apache-2.0
base_model:
- Ellbendls/Qwen-3-4b-Text_to_SQL
- Qwen/Qwen3-4B-Instruct-2507
tags:
- gguf
- llama.cpp
- qwen
- text-to-sql
- sql
- instruct
language:
- eng
- zho
- fra
- spa
- por
- deu
- ita
- rus
- jpn
- kor
- vie
- tha
- ara
pipeline_tag: text-generation
---

# Ellbendls/Qwen-3-4b-Text_to_SQL-GGUF

Quantized GGUF builds of `Ellbendls/Qwen-3-4b-Text_to_SQL` for fast CPU/GPU inference with llama.cpp-compatible runtimes.

- **Base model**. Fine-tuned from **Qwen/Qwen3-4B-Instruct-2507** for Text-to-SQL.
- **License**. Apache-2.0 (inherits from base). Keep attribution.
- **Purpose**. Turn natural language into SQL. When schema is missing, the model can infer a simple schema then produce SQL.

## Files

Base and quantized variants:

- `Qwen-3-4b-Text_to_SQL-F16.gguf`  — reference float16 export
- `Qwen-3-4b-Text_to_SQL-q2_k.gguf`
- `Qwen-3-4b-Text_to_SQL-q3_k_m.gguf`
- `Qwen-3-4b-Text_to_SQL-q4_k_s.gguf`
- `Qwen-3-4b-Text_to_SQL-q4_k_m.gguf`  ← good default
- `Qwen-3-4b-Text_to_SQL-q5_k_m.gguf`
- `Qwen-3-4b-Text_to_SQL-q6_k.gguf`
- `Qwen-3-4b-Text_to_SQL-q8_0.gguf`    ← near-lossless, larger

Conversion and quantization done with `llama.cpp`.

## Recommended pick

- **Q4_K_M**. Best balance of speed and quality for laptops and small servers.
- **Q5_K_M**. Higher quality, a bit more RAM/VRAM.
- **Q8_0**. Highest quality among quants. Use if you have headroom.

## Approximate memory needs

These are ballpark for a 4B model. Real usage varies by runtime and context length.

- Q4_K_M: 3–4 GB RAM/VRAM
- Q5_K_M: 4–5 GB
- Q8_0: 6–8 GB
- F16: 10–12 GB

## Quick start

### llama.cpp (CLI)

CPU only:
```bash
./llama-cli -m Qwen-3-4b-Text_to_SQL-q4_k_m.gguf \
  -p "Generate SQL to get average salary by department in 2024." \
  -n 256 -t 6
````

NVIDIA GPU offload (build with `-DLLAMA_CUBLAS=ON`):

```bash
./llama-cli -m Qwen-3-4b-Text_to_SQL-q4_k_m.gguf \
  -p "Generate SQL to get average salary by department in 2024." \
  -n 256 -ngl 999 -t 6
```

### Python (llama-cpp-python)

```python
from llama_cpp import Llama

llm = Llama(model_path="Qwen-3-4b-Text_to_SQL-q4_k_m.gguf", n_ctx=4096, n_gpu_layers=35)  # set 0 for CPU-only
prompt = "Generate SQL to list total orders and revenue by month for 2024."
out = llm(prompt, max_tokens=256, temperature=0.2, top_p=0.9)
print(out["choices"][0]["text"].strip())
```

### LM Studio / Kobold / text-generation-webui

* Select the `.gguf` file and load.
* Set temperature 0.1–0.3 for deterministic SQL.
* Use a system prompt to anchor behavior.

## Model details

* **Base**. `Qwen/Qwen3-4B-Instruct-2507` (32k context, multilingual).
* **Fine-tune**. Trained on `gretelai/synthetic_text_to_sql`.
* **Task**. NL → SQL. Capable of simple schema inference when needed.
* **Languages**. Works best in English. Can follow prompts in several languages from the base model.

## Conversion reproducibility

Export used:

```bash
python convert_hf_to_gguf.py /path/to/hf_model --outtype f16 --outfile Qwen-3-4b-Text_to_SQL-F16.gguf
```

Quantization used:

```bash
./llama-quantize Qwen-3-4b-Text_to_SQL-F16.gguf Qwen-3-4b-Text_to_SQL-q4_k_m.gguf Q4_K_M
# likewise for q2_k, q3_k_m, q5_k_m, q8_0
```

## Intended use and limits

* **Use**. Analytics, reporting, dashboards, data exploration, SQL prototyping.
* **Limits**. No database connectivity. It only generates SQL text. Validate and test queries before use in production. Provide real schema for best accuracy.

## Attribution

* Base model: [`Qwen/Qwen3-4B-Instruct-2507`](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507)
* Fine-tuned model: [`Ellbendls/Qwen-3-4b-Text_to_SQL`](https://huggingface.co/Ellbendls/Qwen-3-4b-Text_to_SQL)

## License

Apache-2.0. Include license and NOTICE from upstream when redistributing the weights. Do not imply endorsement from Qwen or original authors.

## Changelog

* 2025-09-17. Initial GGUF release. Added q2\_k, q3\_k\_m, q4\_k\_m, q5\_k\_m, q8\_0, and F16.

```
::contentReference[oaicite:0]{index=0}
```
