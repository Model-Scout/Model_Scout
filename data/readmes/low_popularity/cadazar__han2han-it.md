---
license: apache-2.0
language:
- ko
library_name: transformers
pipeline_tag: text-generation
tags:
- han2han
- hanja
- hangul
- historical-korean
- encoder-decoder
- custom_code
---

# Han2Han IT

Instruction-tuned checkpoint of [Han2Han](https://github.com/cadazar/han2han)
(`han2han-ul2-base-1-it`, step 43153). Han2Han is a 169M-parameter
encoder-decoder model that learns script-invariant representations of Korean
text: a document written in Hanja and its Hangul transcription land at the same
point in embedding space. The recipe (jamo and character-level embedding fusion,
morpheme-aware denoising, bidirectional Hanja-Hangul transcription) is described
in the paper, accepted to Findings of EMNLP 2026.

This repo holds the PyTorch weights, the SentencePiece tokenizer, and the
modeling code needed to load them through the `transformers` Auto classes with
`trust_remote_code=True`. Training code, the Flax model, the Flax-to-PyTorch
converter, and the evaluation pipeline live in the GitHub repo.

## Usage

Runtime requirements: `torch`, `transformers`, `sentencepiece`, `regex`, and
`numpy` (tested with torch 2.12.0 and transformers 5.9.0 on CPU). `absl-py` is
optional.

```python
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

repo = "cadazar/han2han-it"
tokenizer = AutoTokenizer.from_pretrained(repo, trust_remote_code=True)
model = AutoModelForSeq2SeqLM.from_pretrained(repo, trust_remote_code=True).eval()

prompt = "<|user|>다음 한문을 한글로 옮기시오:\n韓國語는 世界에서 가장 科學的인 文字입니다.<|end_of_turn|>"
inputs = tokenizer(prompt, return_tensors="pt")
with torch.no_grad():
    output = model.generate(**inputs, max_new_tokens=64, use_fixed_length_generation=False)
print(tokenizer.decode(output[0].tolist()))
```

Prompt format, as used by the SFT collator in the GitHub repo:

- Encoder input: `<|system|>{system}<|user|>{user}<|end_of_turn|>`. The system
  part is optional.
- The decoder starts from `<|assistant|>` (`decoder_start_token_id` 9) and a turn
  ends with `<|end_of_turn|>` (`eos_token_id` 10).

`Han2HanTokenizer` is a plain SentencePiece wrapper rather than a
`PreTrainedTokenizer` subclass. It exposes `__call__`, `encode`, and `decode`;
`__call__` does not add BOS or EOS tokens, and special tokens written into the
text are mapped to their ids.

## Files

| File | Contents |
| --- | --- |
| `model.safetensors` | fp32 weights, 169.2M parameters, plus the `jbu` / `cbu` subword bucket tables |
| `config.json`, `generation_config.json` | model and generation config, with `auto_map` entries for the Auto classes |
| `spiece.model`, `tokenizer_config.json` | SentencePiece model (38400 pieces) and tokenizer config |
| `modeling_han2han.py`, `han2han_config.py`, `han2han_tokenizer.py` | modeling code, copied from the GitHub repo at commit `0b858ea5f1c7c5aeb325ba114eb87e335fe05dd9` (`modeling_han2han_pytorch.py` there) |

The code files differ from the repo copies only where remote-code loading
requires it: sibling imports are relative, optional `fla` / `flax` / `absl`
imports are guarded, the tokenizer and the model resolve Hub repo ids, the
tokenizer logs through a plain `logging` logger instead of the repo's JAX-aware
helper, and the module-level `register_han2han` import is replaced by the
`auto_map` entries.

## Instruction tuning

Fine-tuned from the Han2Han pre-trained checkpoint on instruction following,
chain-of-thought reasoning, Hanja-Hangul article transcription, and
summarization data (`configs/it-muon-stage_1.yaml` in the GitHub repo).

## Citation

```bibtex
@inproceedings{han2han2026,
  title     = {Han2Han: Efficient Language-Specific Character Representation
               through Script-Aware Pre-Training for Historical Text Analysis},
  author    = {Adams, Cellik and Jo, EunKyoung and Kim, Juae},
  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2026},
  year      = {2026}
}
```

## License

Apache License 2.0, the same as the [GitHub repo](https://github.com/cadazar/han2han).
