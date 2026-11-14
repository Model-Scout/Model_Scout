---
license: apache-2.0
base_model: ibm-granite/granite-embedding-97m-multilingual-r2
base_model_relation: quantized
library_name: gguf
pipeline_tag: feature-extraction
language:
- ar
- az
- bg
- bn
- ca
- cs
- da
- de
- el
- en
- es
- et
- fa
- fi
- fr
- he
- hi
- hr
- hu
- id
- is
- it
- ja
- ka
- kk
- km
- ko
- lt
- lv
- mr
- ms
- nl
- 'no'
- pl
- pt
- ro
- ru
- sk
- sl
- sq
- sr
- sv
- sw
- te
- th
- tl
- tr
- uk
- ur
- uz
- vi
- zh
tags:
- granite
- embeddings
- gguf
- llama.cpp
- sentence-similarity
---

# Granite Embedding 97M Multilingual R2, GGUF Q8_0

A GGUF file of IBM's [granite-embedding-97m-multilingual-r2](https://huggingface.co/ibm-granite/granite-embedding-97m-multilingual-r2), for llama.cpp. It was made for the Mimini desktop assistant, which uses this model to find earlier chat messages by meaning.

This is not an IBM release. The model is IBM's work, under IBM's Apache-2.0 license; this repository converts it to GGUF and quantizes it to Q8_0. For what the model is, how it was trained, what it is for and its limitations, see [IBM's model card](https://huggingface.co/ibm-granite/granite-embedding-97m-multilingual-r2).

## File

| File | Size | SHA-256 |
|---|---|---|
| `granite-embedding-97M-multilingual-r2-Q8_0.gguf` | 115,061,216 bytes | `e52ab606180146f095056592b2ca16c1c1b48dbd8d80a41f27dca9480f121010` |

## Source and changes

- **Source:** `ibm-granite/granite-embedding-97m-multilingual-r2` at revision `835ad14087e140460703cf0fae09f97d469d65c2`. The conversion read `model.safetensors`, `config.json`, `tokenizer.json`, `tokenizer_config.json`, `special_tokens_map.json`, `modules.json`, `1_Pooling/config.json` and `README.md`.
- **Checked before converting:** IBM signs its release with Sigstore (`model.sig`, OpenSSF model signing). The signature was verified for the identity `Granite-sign@ibm.com`, issued by `https://sigstore.verify.ibm.com/oauth2`, and each file above matched the SHA-256 in IBM's signed list.
- **Changes:** converted from safetensors to GGUF and quantized to Q8_0 with llama.cpp b11669 (`convert_hf_to_gguf.py --outtype q8_0`). Nothing else was changed in the weights or the tokenizer.

## Reproduce it

The conversion is reproducible: run again, it gives a file with the same SHA-256. `scripts/convert-embedder.sh` in this repository does every step: it downloads IBM's files at the revision above, verifies the signature, converts with llama.cpp b11669 and the Python packages that version pins, and checks the hash.

```bash
bash scripts/convert-embedder.sh
```

It needs macOS on Apple Silicon or Linux (llama.cpp b11669 pins torch 2.11, which has no Intel Mac build), `curl`, and Python 3.10 or newer (`PYTHON=/path/to/python3` to choose one). It downloads about 220 MB of model files and 750 MB of Python packages (mostly torch) into `.llama-build/` and `.embedder-build/` in the repository folder, and writes the file to `.embedder-build/`.

## Use with llama.cpp

```bash
llama-server -m granite-embedding-97M-multilingual-r2-Q8_0.gguf --embeddings -c 2048 -b 2048 -ub 2048
```

- Each text must fit in one batch (`-ub`, here 2,048 tokens): the model reads its input at once, and with the default of 512 llama-server rejects longer texts.
- CLS pooling, the SiLU activation and IBM's tokenizer are set in the file. The model takes no query or document prefixes.
- Compare vectors with cosine similarity. The vectors have 384 dimensions.
- Mimini runs the model on the CPU: `--embeddings --device none --no-repack -c 2048 -b 2048 -ub 2048 --parallel 1`.

## Checks

- **Close to IBM's model:** 50 English and Vietnamese texts, from short questions to 3,600-character passages, were embedded by llama-server b11669 with this file and by IBM's model in transformers (float32, CLS pooling, L2 normalisation, as its sentence-transformers configuration says). The cosine between the two was at least 0.99968, 0.99988 on average, and the token ids were identical for all 50 texts.
- **Same weights as the earlier community file:** all 74 tensors are byte-identical to the Q8_0 file in `mykor/granite-embedding-97m-multilingual-r2-GGUF`. Two metadata keys differ: llama.cpp b11669 also writes `modern-bert.classifier.activation` and `modern-bert.classifier.pooling_type`, which only classification heads use.

## License

Apache-2.0, like IBM's model: see `LICENSE`. Granite Embedding 97M Multilingual R2 is developed by IBM.
