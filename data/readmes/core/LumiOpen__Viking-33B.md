---
license: apache-2.0
datasets:
- cerebras/SlimPajama-627B
- bigcode/starcoderdata
- mc4
language:
- fi
- en
- da
- sv
- 'no'
- nn
- is
---


# Viking 33B

Viking 33B is a 33B parameter decoder-only transformer pretrained on Finnish,
English, Swedish, Danish, Norwegian, Icelandic and code.  It is being trained
on 2 trillion tokens (1300B billion as of this release). Viking 33B is a fully open source model and is made available under the Apache 2.0 License.

Viking was created in a collaboration between the [TurkuNLP group](https://turkunlp.org/) of the University of Turku, [SiloGen](https://www.silo.ai/silogen) from [Silo AI](https://www.silo.ai/),and [High Performance Language Technologies](https://hplt-project.org/) (HPLT). Training was conducted on the [LUMI supercomputer](https://www.lumi-supercomputer.eu/), using compute resources generously provided by [CSC](https://csc.fi/) - IT Center for Science, Finland.

This project is part of an ongoing effort to create open source large language models for non-English and especially low resource languages like Finnish. The mode is fluent in Finnish, English, the Scandinavian languages and capable of basic translation between them. It is also able to understand and generate code.

## Model Family

Viking is the second set of models released by LumiOpen and is available at
3 parameter counts:

[Viking 7B](https://huggingface.co/LumiOpen/Viking-7B)

[Viking 13B](https://huggingface.co/LumiOpen/Viking-13B)

[Viking 33B](https://huggingface.co/LumiOpen/Viking-33B)

## Model Overview
_**NOTE:** Viking is a base model which needs further fine tuning for most use cases._

Viking is a generative pretrained transformer using a LLaMA-like GPT architecture, and makes use of rotary positional embeddings and flash attention.

| Hyperparameter | Value  |
| :------------- | :----: |
| n_parameters | 33B |
| n_layers | 56 |
| n_heads | 56 |
| d_model | 7168 |
| vocab_size | 131072 |
| sequence_length | 4096 |

## Training

Viking 33B was trained on the LUMI supercomputer, using 1024 AMD MI250X GPUs.  Each MI250X GPU has two Graphics Complex Dies (GCDs) for a world size of 2048 during training, using activation checkpointing, a micro batch size of 1, gradient accumulation of 16, and a 3D parallelism strategy of TP=4, PP=4, DP=128.

Training began in September 2023 using a [custom fork](https://github.com/LumiOpen/Megatron-DeepSpeed) of the Megatron-Deepspeed framework.


## Training Hyperparameters

| Hyperparameter | Value | Comment |
| :------------: | :---: | :------:|
| Precision | bfloat16 | |
| Optimizer | AdamW | |
| Learning rate | 3e-4 | 10B tokens warm-up, cosine decay to 3e-5 |
| Weight decay | 1e-1 | |
| Batch size | 1024 | 1024 samples x 4096 tokens = 4194304 tokens |

## Tokenizer

Viking uses a custom 128K Bloom tokenizer trained on the same English, Finnish, Swedish, Danish, Norwegian, Icelandic and code dataset used to train the model.

## Dataset

Viking is being trained on a 2 trillion token mixed dataset of English, Finnish, Swedish, Danish, Norwegian, Icelandic and code.

Full details will be published soon.

## Evaluation Results

Full evaluation results will be published with the final model. 

## Training Checkpoints

Training checkpoints are available as branches in the repository.  Checkpoints will be released roughly every 100B tokens.  The main branch will always point to the latest checkpoint.  The following checkpoints are available:

* [100B](https://huggingface.co/LumiOpen/Viking-33B/tree/100B)
* [200B](https://huggingface.co/LumiOpen/Viking-33B/tree/200B)
* [300B](https://huggingface.co/LumiOpen/Viking-33B/tree/300B)
* [400B](https://huggingface.co/LumiOpen/Viking-33B/tree/400B)
* [500B](https://huggingface.co/LumiOpen/Viking-33B/tree/500B)
* [600B](https://huggingface.co/LumiOpen/Viking-33B/tree/600B)
* [700B](https://huggingface.co/LumiOpen/Viking-33B/tree/700B)
* [800B](https://huggingface.co/LumiOpen/Viking-33B/tree/800B)
* [900B](https://huggingface.co/LumiOpen/Viking-33B/tree/900B)
* [1000B](https://huggingface.co/LumiOpen/Viking-33B/tree/1000B)
* [1100B](https://huggingface.co/LumiOpen/Viking-33B/tree/1100B)
* [1200B](https://huggingface.co/LumiOpen/Viking-33B/tree/1200B)
* [1300B](https://huggingface.co/LumiOpen/Viking-33B/tree/1300B)
* [1400B](https://huggingface.co/LumiOpen/Viking-33B/tree/1400B)
* [1500B](https://huggingface.co/LumiOpen/Viking-33B/tree/1500B)
* [1600B](https://huggingface.co/LumiOpen/Viking-33B/tree/1600B)
* [1700B](https://huggingface.co/LumiOpen/Viking-33B/tree/1700B)
* [1800B](https://huggingface.co/LumiOpen/Viking-33B/tree/1800B)
* [1900B](https://huggingface.co/LumiOpen/Viking-33B/tree/1900B)
* [2000B](https://huggingface.co/LumiOpen/Viking-33B/tree/2000B)

The transformers library allows you to load a checkpoint from a branch as follows:

```python
branch = "200B"
model = transformers.AutoModelForCausalLM.from_pretrained(
    "LumiOpen/Viking-33B",
    torch_dtype=torch.bfloat16,
    revision=branch,
)
```


## Ethical Considerations and Limitations

_Viking 33B is a release of a partially trained model, and special care should be taken when using any output._

Viking is an advanced language model, primarily optimized for English, Finnish, Swedish, Norwegian, Danish, Icelandic and code, with no meaningful proficiency in any other languages. As with most AI-driven systems, Viking is a product of the vast data it has been trained on, which may reflect the imperfections, biases, and idiosyncrasies of the wider web. Viking may, at times, produce outputs that can be considered inaccurate, prejudiced, or controversial. Users and developers engaging with Viking should exercise discretion and consider additional evaluation and customization to ensure the model's responses align with their specific needs and ethical standards.

## License

Viking is released under the Apache 2.0 license.

## Citation Information

```
@misc {lumiopen_2025,
	author       = { Luukkonen, Risto and Burdge, Jonathan and Zosa, Elaine and Komulainen, Ville and Sarlin, Peter and Pyysalo, Sampo },
	title        = { Viking: A Family of Nordic LLMs },
	year         = 2025,
	url          = { https://huggingface.co/LumiOpen/Viking-33B },
	doi          = { 10.57967/hf/4885 },
	publisher    = { Hugging Face }
}
```

