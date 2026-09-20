---
library_name: transformers
license: other
license_name: exaone
license_link: LICENSE
language:
  - en
  - ko
tags:
  - lg-ai
  - exaone
---

# EXAONE-3.0-8B-it

[!WARNING]

https://github.com/ggerganov/llama.cpp/wiki/Templates-supported-by-llama_chat_apply_template

chat template이 적용 안될 수 있습니다.

llama-cpp-python은 jinja2를 사용하므로 템플릿이 적용되나, 이외의 런타임에서는 적용되지 않을 수 있음에 유의하세요.


```py
from llama_cpp import Llama

llm = Llama.from_pretrained(
    repo_id="Bingsu/exaone-3.0-7.8b-it",
    filename="exaone-3.0-7.8B-it-Q8_0.gguf"
)
```

```sh
llama_model_loader: loaded meta data with 34 key-value pairs and 291 tensors from /root/.cache/huggingface/hub/models--Bingsu--exaone-3.0-7.8b-it/snapshots/c7b9c43a7d1db6509b40e9b18f10ae0554b3d4cb/./exaone-3.0-7.8B-it-Q8_0.gguf (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.type str              = model
llama_model_loader: - kv   2:                               general.name str              = Exaone 3.0 7.8b It
llama_model_loader: - kv   3:                           general.finetune str              = it
llama_model_loader: - kv   4:                           general.basename str              = exaone-3.0
llama_model_loader: - kv   5:                         general.size_label str              = 7.8B
llama_model_loader: - kv   6:                            general.license str              = other
llama_model_loader: - kv   7:                       general.license.name str              = exaone
llama_model_loader: - kv   8:                       general.license.link str              = LICENSE
llama_model_loader: - kv   9:                               general.tags arr[str,2]       = ["lg-ai", "exaone"]
llama_model_loader: - kv  10:                          general.languages arr[str,2]       = ["en", "ko"]
llama_model_loader: - kv  11:                          llama.block_count u32              = 32
llama_model_loader: - kv  12:                       llama.context_length u32              = 4096
llama_model_loader: - kv  13:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv  14:                  llama.feed_forward_length u32              = 14336
llama_model_loader: - kv  15:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv  16:              llama.attention.head_count_kv u32              = 8
llama_model_loader: - kv  17:                       llama.rope.freq_base f32              = 500000.000000
llama_model_loader: - kv  18:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  19:                          general.file_type u32              = 7
llama_model_loader: - kv  20:                           llama.vocab_size u32              = 102400
llama_model_loader: - kv  21:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv  22:            tokenizer.ggml.add_space_prefix bool             = false
llama_model_loader: - kv  23:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  24:                         tokenizer.ggml.pre str              = default
llama_model_loader: - kv  25:                      tokenizer.ggml.tokens arr[str,102400]  = ["[PAD]", "[BOS]", "[EOS]", "[UNK]", ...
llama_model_loader: - kv  26:                  tokenizer.ggml.token_type arr[i32,102400]  = [3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, ...
llama_model_loader: - kv  27:                      tokenizer.ggml.merges arr[str,101782]  = ["t h", "Ġ a", "Ġ í", "i n", "Ġ t...
llama_model_loader: - kv  28:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  29:                tokenizer.ggml.eos_token_id u32              = 361
llama_model_loader: - kv  30:            tokenizer.ggml.unknown_token_id u32              = 3
llama_model_loader: - kv  31:            tokenizer.ggml.padding_token_id u32              = 0
llama_model_loader: - kv  32:                    tokenizer.chat_template str              = {% for message in messages %}{% if lo...
llama_model_loader: - kv  33:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q8_0:  226 tensors
llm_load_vocab: special tokens cache size = 362
llm_load_vocab: token to piece cache size = 0.6622 MB
llm_load_print_meta: format           = GGUF V3 (latest)
llm_load_print_meta: arch             = llama
llm_load_print_meta: vocab type       = BPE
llm_load_print_meta: n_vocab          = 102400
llm_load_print_meta: n_merges         = 101782
llm_load_print_meta: vocab_only       = 0
llm_load_print_meta: n_ctx_train      = 4096
llm_load_print_meta: n_embd           = 4096
llm_load_print_meta: n_layer          = 32
llm_load_print_meta: n_head           = 32
llm_load_print_meta: n_head_kv        = 8
llm_load_print_meta: n_rot            = 128
llm_load_print_meta: n_swa            = 0
llm_load_print_meta: n_embd_head_k    = 128
llm_load_print_meta: n_embd_head_v    = 128
llm_load_print_meta: n_gqa            = 4
llm_load_print_meta: n_embd_k_gqa     = 1024
llm_load_print_meta: n_embd_v_gqa     = 1024
llm_load_print_meta: f_norm_eps       = 0.0e+00
llm_load_print_meta: f_norm_rms_eps   = 1.0e-05
llm_load_print_meta: f_clamp_kqv      = 0.0e+00
llm_load_print_meta: f_max_alibi_bias = 0.0e+00
llm_load_print_meta: f_logit_scale    = 0.0e+00
llm_load_print_meta: n_ff             = 14336
llm_load_print_meta: n_expert         = 0
llm_load_print_meta: n_expert_used    = 0
llm_load_print_meta: causal attn      = 1
llm_load_print_meta: pooling type     = 0
llm_load_print_meta: rope type        = 0
llm_load_print_meta: rope scaling     = linear
llm_load_print_meta: freq_base_train  = 500000.0
llm_load_print_meta: freq_scale_train = 1
llm_load_print_meta: n_ctx_orig_yarn  = 4096
llm_load_print_meta: rope_finetuned   = unknown
llm_load_print_meta: ssm_d_conv       = 0
llm_load_print_meta: ssm_d_inner      = 0
llm_load_print_meta: ssm_d_state      = 0
llm_load_print_meta: ssm_dt_rank      = 0
llm_load_print_meta: model type       = 8B
llm_load_print_meta: model ftype      = Q8_0
llm_load_print_meta: model params     = 7.82 B
llm_load_print_meta: model size       = 7.74 GiB (8.50 BPW) 
llm_load_print_meta: general.name     = Exaone 3.0 7.8b It
llm_load_print_meta: BOS token        = 1 '[BOS]'
llm_load_print_meta: EOS token        = 361 '[|endofturn|]'
llm_load_print_meta: UNK token        = 3 '[UNK]'
llm_load_print_meta: PAD token        = 0 '[PAD]'
llm_load_print_meta: LF token         = 490 'Ä'
llm_load_print_meta: EOT token        = 42 '<|endoftext|>'
llm_load_print_meta: max token length = 48
ggml_cuda_init: GGML_CUDA_FORCE_MMQ:    yes
ggml_cuda_init: GGML_CUDA_FORCE_CUBLAS: no
ggml_cuda_init: found 1 CUDA devices:
  Device 0: NVIDIA L4, compute capability 8.9, VMM: yes
llm_load_tensors: ggml ctx size =    0.14 MiB
llm_load_tensors: offloading 0 repeating layers to GPU
llm_load_tensors: offloaded 0/33 layers to GPU
llm_load_tensors:        CPU buffer size =  7923.02 MiB
............................................................................................
llama_new_context_with_model: n_ctx      = 512
llama_new_context_with_model: n_batch    = 512
llama_new_context_with_model: n_ubatch   = 512
llama_new_context_with_model: flash_attn = 0
llama_new_context_with_model: freq_base  = 500000.0
llama_new_context_with_model: freq_scale = 1
llama_kv_cache_init:  CUDA_Host KV buffer size =    64.00 MiB
llama_new_context_with_model: KV self size  =   64.00 MiB, K (f16):   32.00 MiB, V (f16):   32.00 MiB
llama_new_context_with_model:  CUDA_Host  output buffer size =     0.39 MiB
llama_new_context_with_model:      CUDA0 compute buffer size =   633.00 MiB
llama_new_context_with_model:  CUDA_Host compute buffer size =     9.01 MiB
llama_new_context_with_model: graph nodes  = 1030
llama_new_context_with_model: graph splits = 356
AVX = 1 | AVX_VNNI = 0 | AVX2 = 1 | AVX512 = 0 | AVX512_VBMI = 0 | AVX512_VNNI = 0 | AVX512_BF16 = 0 | FMA = 1 | NEON = 0 | SVE = 0 | ARM_FMA = 0 | F16C = 1 | FP16_VA = 0 | WASM_SIMD = 0 | BLAS = 1 | SSE3 = 1 | SSSE3 = 1 | VSX = 0 | MATMUL_INT8 = 0 | LLAMAFILE = 1 | 
Model metadata: {'tokenizer.ggml.unknown_token_id': '3', 'tokenizer.ggml.eos_token_id': '361', 'general.quantization_version': '2', 'tokenizer.ggml.model': 'gpt2', 'tokenizer.ggml.add_space_prefix': 'false', 'llama.rope.dimension_count': '128', 'llama.vocab_size': '102400', 'general.file_type': '7', 'llama.attention.layer_norm_rms_epsilon': '0.000010', 'llama.rope.freq_base': '500000.000000', 'tokenizer.ggml.bos_token_id': '1', 'llama.attention.head_count': '32', 'general.architecture': 'llama', 'llama.attention.head_count_kv': '8', 'llama.block_count': '32', 'tokenizer.ggml.padding_token_id': '0', 'general.basename': 'exaone-3.0', 'tokenizer.ggml.pre': 'default', 'llama.context_length': '4096', 'general.name': 'Exaone 3.0 7.8b It', 'general.type': 'model', 'general.size_label': '7.8B', 'general.finetune': 'it', 'general.license.name': 'exaone', 'tokenizer.chat_template': "{% for message in messages %}{% if loop.first and message['role'] != 'system' %}{{ '[|system|][|endofturn|]\n' }}{% endif %}{{ '[|' + message['role'] + '|]' + message['content'] }}{% if message['role'] == 'user' %}{{ '\n' }}{% else %}{{ '[|endofturn|]\n' }}{% endif %}{% endfor %}{% if add_generation_prompt %}{{ '[|assistant|]' }}{% endif %}", 'general.license.link': 'LICENSE', 'general.license': 'other', 'llama.feed_forward_length': '14336', 'llama.embedding_length': '4096'}
Available chat formats from metadata: chat_template.default
Using gguf chat template: {% for message in messages %}{% if loop.first and message['role'] != 'system' %}{{ '[|system|][|endofturn|]
' }}{% endif %}{{ '[|' + message['role'] + '|]' + message['content'] }}{% if message['role'] == 'user' %}{{ '
' }}{% else %}{{ '[|endofturn|]
' }}{% endif %}{% endfor %}{% if add_generation_prompt %}{{ '[|assistant|]' }}{% endif %}
Using chat eos_token: [|endofturn|]
Using chat bos_token: [BOS]
```

```py
llm.create_chat_completion(
      messages = [
          {
              "role": "system",
              "content": "You are EXAONE model from LG AI Research, a helpful assistant."
        },
          {
              "role": "user",
              "content": "다 해줬잖아"
          }
      ]
)
```

```sh
llama_print_timings:        load time =    1812.86 ms
llama_print_timings:      sample time =      20.39 ms /   220 runs   (    0.09 ms per token, 10788.54 tokens per second)
llama_print_timings: prompt eval time =    1812.72 ms /    38 tokens (   47.70 ms per token,    20.96 tokens per second)
llama_print_timings:        eval time =   33280.46 ms /   219 runs   (  151.97 ms per token,     6.58 tokens per second)
llama_print_timings:       total time =   35397.95 ms /   257 tokens
{'id': 'chatcmpl-451b0538-c70d-45f4-924b-106f5ac3c02f',
 'object': 'chat.completion',
 'created': 1723204952,
 'model': '/root/.cache/huggingface/hub/models--Bingsu--exaone-3.0-7.8b-it/snapshots/c7b9c43a7d1db6509b40e9b18f10ae0554b3d4cb/./exaone-3.0-7.8B-it-Q8_0.gguf',
 'choices': [{'index': 0,
   'message': {'role': 'assistant',
    'content': '네, 알겠습니다. 이전에 말씀하신 내용을 요약해 드리겠습니다:\n\n1. EXAONE 2.0 모델의 특징:\n   - 7.8B instruction 튜닝 파라미터\n   - 한국어와 영어에서 우수한 성능\n   - 다양한 작업에서 높은 정확도\n\n2. 연구 논문:\n   - "EXAONE 2.0: An Open-Retrieval Large Language Model for Dense Retrieval and Question Answering"\n\n3. 주요 성과:\n   - 한국어와 영어에서 우수한 성능\n   - 다양한 작업에서 높은 정확도\n\n4. 활용 사례:\n   - 고객 지원 챗봇\n   - 법률 문서 요약\n   - 의료 정보 제공\n\n5. 기술적 세부 사항:\n   - 7.8B instruction 튜닝 파라미터\n   - 한국어와 영어에서 우수한 성능\n   - 다양한 작업에서 높은 정확도\n\n이 외에 추가로 궁금한 사항이 있으시면 언제든지 말씀해 주세요!'},
   'logprobs': None,
   'finish_reason': 'stop'}],
 'usage': {'prompt_tokens': 38, 'completion_tokens': 219, 'total_tokens': 257}}
```
