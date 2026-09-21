---
license: other
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
base_model:
- LiquidAI/LFM2-350M
pipeline_tag: text-generation
tags:
- loom
- text-generation
library_name: loom-py-rt
---
# LFM2-350M (modular export)

Liquid AI's LFM2-350M hybrid conv/attention LM, exported as per-layer topologies.

This is a [loom.cpp](https://github.com/loom-ai-org/loom.cpp) export: a single self-describing GGUF
that carries its own graph topologies, tokenizer (if any) and driver script, produced by
[loom-exporter](https://github.com/loom-ai-org/loom-exporter).

## Original model

Exported from [`LiquidAI/LFM2-350M`](https://huggingface.co/LiquidAI/LFM2-350M). Weights are unmodified; this repo packages the same parameters into
loom.cpp's GGUF format.

## License

[LFM Open License v1.0](https://huggingface.co/LiquidAI/LFM2-350M/blob/main/LICENSE) -- inherited from the base model above.

## Language(s)

`en`, `ar`, `zh`, `fr`, `de`, `ja`, `ko`, `es`

## Usage

Run it with [loom-py](https://github.com/loom-ai-org/loom-py) -- `loom-py-rt` on PyPI:

```sh
pip install -U "loom-py-rt[hub]"
```

```python
import loom

model = loom.Model.from_pretrained("loom-ai-org/lfm2-350m-modular-loom")
print(model.text2text.chat("Who discovered Brazil?", max_new_tokens=256))

# The same model, one turn at a time, and with the decode rule named rather than inherited:
print(model.chat([("user", "Name one river in Brazil.")], temperature=0.0))
```

### The layer underneath

The call above is the high-level door: one per task, named for the modality pair it maps between, with
the windowing, sampling and assembly this model needs already applied. Under it, `model.infer(...)`
passes your arguments straight to the driver this GGUF embeds -- which is where you go for a knob the
door does not name.

`model.driver_source` prints that driver, including a header comment documenting every argument it
accepts for this model, and is the authority on it. See [loom-py](https://github.com/loom-ai-org/loom-py) for the API and
[loom.cpp](https://github.com/loom-ai-org/loom.cpp) for what the engine does between the two.

## Files

- `lfm2-350m-modular.gguf` -- the model, exported with loom-exporter.
