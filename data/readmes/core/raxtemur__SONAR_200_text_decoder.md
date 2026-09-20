---
language:
- multilingual
- en
- ru
- de
- fr
- es
- zh
- ja
- ko
- ar
license: cc-by-nc-4.0
library_name: transformers
tags:
- sonar
- sentence-embeddings
- multilingual
- translation
- text-generation
- text2text-generation
base_model: facebook/nllb-200-distilled-1.3B
pipeline_tag: translation
---

# SONAR 200 Text Decoder (HuggingFace Port)

This is a port of [Meta's SONAR](https://github.com/facebookresearch/SONAR) text decoder from fairseq2 to HuggingFace Transformers format.

## Model Description

SONAR decoder converts 1024-dimensional sentence embeddings back to text. It supports 202 languages (same as NLLB-200).

- **Original model:** [facebook/SONAR](https://huggingface.co/facebook/SONAR)
- **Encoder port:** [cointegrated/SONAR_200_text_encoder](https://huggingface.co/cointegrated/SONAR_200_text_encoder)
- **Code & Documentation:** [GitHub: SonarTransformers](https://github.com/raxtemur/SonarTransformers)

## Usage

### With sonar_transformers library (recommended, see [GitHub: SonarTransformers](https://github.com/raxtemur/SonarTransformers))

```bash
pip install torch transformers sentencepiece
```

```python
from sonar_transformers import SonarPipeline

pipeline = SonarPipeline()

# Translation
result = pipeline.translate(
    ["Hello, how are you?"],
    source_lang="eng_Latn",
    target_lang="rus_Cyrl"
)
print(result)  # ['Здравствуйте, как дела?']

# Encode text to embeddings
embeddings = pipeline.encode(["Hello world!"], source_lang="eng_Latn")
print(embeddings.shape)  # torch.Size([1, 1024])

# Decode embeddings back to text
texts = pipeline.decode(embeddings, target_lang="eng_Latn")
print(texts)  # ['Hello world!']
```

### Direct usage with transformers

```python
import torch
from transformers import M2M100ForConditionalGeneration, NllbTokenizer
from transformers.modeling_outputs import BaseModelOutput

# Load model and tokenizer
model = M2M100ForConditionalGeneration.from_pretrained("raxtemur/SONAR_200_text_decoder")
tokenizer = NllbTokenizer.from_pretrained("raxtemur/SONAR_200_text_decoder")

# Your embeddings from SONAR encoder (1024-dim vectors)
embeddings = torch.randn(1, 1024)  # Replace with actual embeddings

# Prepare encoder outputs
encoder_outputs = BaseModelOutput(last_hidden_state=embeddings.unsqueeze(1))

# Generate text
target_lang = "eng_Latn"
forced_bos_token_id = tokenizer.convert_tokens_to_ids(target_lang)

generated_ids = model.generate(
    encoder_outputs=encoder_outputs,
    forced_bos_token_id=forced_bos_token_id,
    max_length=128,
    num_beams=5
)

text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
print(text)
```

## Compatibility

Tested against original fairseq2 SONAR:

| Test | Result |
|------|--------|
| Encoder cosine similarity | **1.000000** |
| Decoder output match | **Identical** |
| Round-trip (encode→decode) | **Works** |
| Translation | **Works** |

Example outputs:
- "Hello world!" → "Hello world!" ✓
- "This is a test sentence." → "This is a test sentence." ✓
- eng→rus: "Hello, how are you?" → "Здравствуйте, как дела?" ✓
- eng→deu: "Machine learning is powerful." → "Maschinelles Lernen ist mächtig." ✓

## Conversion Details

This model was converted from the original fairseq2 checkpoint using the following key mappings:

| fairseq2 | HuggingFace |
|----------|-------------|
| `decoder.decoder.layers.N.encoder_decoder_attn.*` | `model.decoder.layers.N.encoder_attn.*` |
| `decoder.decoder.layers.N.ffn.inner_proj.*` | `model.decoder.layers.N.fc1.*` |
| `decoder.decoder.layers.N.ffn.output_proj.*` | `model.decoder.layers.N.fc2.*` |
| `decoder.decoder.layers.N.ffn_layer_norm.*` | `model.decoder.layers.N.final_layer_norm.*` |
| `decoder.decoder_frontend.embed.weight` | `model.decoder.embed_tokens.weight` |
| `decoder.final_proj.weight` | `lm_head.weight` |

Special tokens were reordered:
- fairseq2: `[pad=0, unk=1, bos=2, eos=3]`
- HuggingFace: `[bos=0, pad=1, eos=2, unk=3]`

## Language Codes (FLORES-200)

Common codes:
- `eng_Latn` - English
- `rus_Cyrl` - Russian
- `deu_Latn` - German
- `fra_Latn` - French
- `spa_Latn` - Spanish
- `zho_Hans` - Chinese (Simplified)
- `jpn_Jpan` - Japanese
- `kor_Hang` - Korean
- `arb_Arab` - Arabic

Full list: 202 languages from FLORES-200.

## Citation

```bibtex
@article{Duquenne:2023:sonar_arxiv,
  author = {Duquenne, Paul-Ambroise and Schwenk, Holger and Balikas, Georgios and others},
  title = {SONAR: Sentence-Level Multimodal and Language-Agnostic Representations},
  journal = {arXiv preprint arXiv:2308.11466},
  year = {2023},
}
```

## License

**CC-BY-NC-4.0** (inherited from original SONAR)

The model weights are derived from [Meta's SONAR](https://github.com/facebookresearch/SONAR) and are licensed under CC-BY-NC-4.0. Commercial use is not permitted.

## Acknowledgments

- [Meta AI](https://github.com/facebookresearch/SONAR) - Original SONAR
- [cointegrated](https://huggingface.co/cointegrated/SONAR_200_text_encoder) - Encoder conversion inspiration
