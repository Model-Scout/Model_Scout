---
license: "apache-2.0"
language: ["af","ar","az","be","bg","bn","ca","ceb","cs","cy","da","de","el","en","es","et","eu","fa","fi","fr","gl","gu","he","hi","hr","ht","hu","hy","id","is","it","ja","jv","ka","kk","km","kn","ko","ky","lo","lt","lv","mk","ml","mn","mr","ms","my","ne","nl","pa","pl","pt","qu","ro","ru","si","sk","sl","so","sq","sr","sv","sw","ta","te","th","tl","tr","uk","ur","vi","yo","zh"]
base_model: Snowflake/snowflake-arctic-embed-l-v2.0
base_model_relation: quantized
library_name: gguf
pipeline_tag: "sentence-similarity"
tags:
- gguf
- llama.cpp
- embeddings
---

# snowflake-arctic-embed-l-v2.0 GGUF

[Snowflake/snowflake-arctic-embed-l-v2.0](https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0) converted to GGUF with llama.cpp b10630. Embeddings have 1024 dimensions.

| File | Type |
| --- | --- |
| snowflake-arctic-embed-l-v2.0-Q8_0.gguf | Q8_0 |

## Usage

With llama.cpp:

```sh
llama-server -hf infosecinnovations/snowflake-arctic-embed-l-v2.0-GGUF:Q8_0 --embeddings
```

With Shabti, in `custom_models.ini`:

```ini
[snowflake-arctic-embed-l-v2.0]
hf = infosecinnovations/snowflake-arctic-embed-l-v2.0-GGUF:Q8_0
tags = embeddings
```
