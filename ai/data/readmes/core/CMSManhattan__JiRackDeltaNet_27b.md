---
language:
- en
- zh
- ja
- ko
- fr
- es
- pt
- de
- it
- ru
- ar
- vi
- th
tags:
- text-generation
- deltanet
- qwen3.8
- gguf
- cpu
- efficient
- low-memory
- ternary
- bitnet
- jirack
- web-ui
- routing
- tool-call
- robotics
- ollama
- ternary-weights
- ternary-transformer
- quantization
- 1.58-bit
license: mit
---

# JiRack Ternary Architedure 
- Benefits high quality CPU inference TQ_2 on Llama.cpp and Ollama via QAT
- Robotcs, Routing, Coding,  Multimedia, Advanced tool calling via JiRackDeltaNetTokenizer
- JiRack DeltaNet understand video and images that best for Robotics also

## PARTNERSHIP
- NVIDIA
- FISERV

# JiRack DeltaNet 27B (CPU)
A fast and efficient 27B model optimized for CPU inference. Built on a Qwen3.8-style DeltaNet architecture (hybrid attention + SSM), with an updated tokenizer that includes **Routing**, **Media**, **Vision**, **Sound**, **Tool call**, and **Robotics** tags. Ready-to-run GGUF quantizations, and native Ollama support with reasoning disabled by default for fast, direct responses.
- JiRack is a cloud-ready model that helps save money on cloud infrastructure. It can be used as an expert model in RAG deployments, with the ONNX JiRack Java server as an alternative.

# JiRack service options
- Current quantizations were done from the FP16 model.
- If you need custom compression or fine-tuning, please write to me and I'll perform QAT from your dataset, tailored specifically to your task.
- Plus double QAT via ONNX QAT.
- Adapt train process to avoid catastrophic forgetting with NDA
- Adapt train process to avoid fast plateau in training with NDA
- Adapts to agentic or instruct models for tool calling, using the JiRack tokenizer to enable high-quality tool calling on small models — built as a domain-specific tool expert.
- Deployment and scale

# Live chat on HF Space
- https://huggingface.co/spaces/CMSManhattan/JiRackDeltaNet_27b
- https://huggingface.co/spaces/CMSManhattan/JiRack-16B-Chat
- https://huggingface.co/spaces/CMSManhattan/JiRack-8B-Chat
- https://huggingface.co/spaces/CMSManhattan/JiRack-2B-Chat
---

## JiRack Codding Agent IDE
- It is Agent Coding IDE for JiRack Models to run via Ollama on home PC 
- It good choose for Agent Coding IDE such as Cursor , Windsurf IDE or Devin IDE etc but more safe that ask you to apply changes and review.
- Web site https://www.jirack.com
- Eclise Plugin site https://marketplace.eclipse.org/content/jirack-coding-agent
- Jetbrain Plugin site https://plugins.jetbrains.com/plugin/35073-jirack-agent
- VS Code Plugin site https://marketplace.visualstudio.com/items?itemName=JiRackautomationCodingAgentIDE.jirack-agent
  
## JiRack Codding Agent IDE files
- Eclise Final release version https://huggingface.co/CMSManhattan/JiRackDeltaNet_27b/resolve/main/jirack_ide_final.zip
- Microsoft VS Code plugin https://huggingface.co/spaces/CMSManhattan/README/blob/main/jirack-agent-0.9.0.vsix
- Jetbrain plugin  https://huggingface.co/spaces/CMSManhattan/README/resolve/main/jirack-jetbrains-0.11.0.zip  
- JiRack DeskTop UI  https://huggingface.co/spaces/CMSManhattan/README/resolve/main/windows_v11.zip
  
---


# Ollama production support
- JiRack DeltaNet 27B runs natively on Ollama with reasoning disabled by default (no forced `<think>` blocks).
- Available now: **`cmsmanhattan/JiRackDeltaNet_27b-q4-reasoning`** — https://ollama.com/cmsmanhattan
- Runtime override also supported: `ollama run cmsmanhattan/JiRackDeltaNet_27b-q4-reasoning --think=false`
- Follow fresh Ollama platform updates


# Spring Boot AI tool calls examples for JiRack DeltaNet series
- Tool call library on java for Enterprise  https://github.com/alibaba/spring-ai-alibaba

# GoEx AI tool calls examples for JiRack DeltaNet series
- Tool call library on python  https://github.com/ShishirPatil/gorilla

# JiRack DeltaNet tool calls to boost tool call quality
- Use JiRack Precision tokenizer tags for tool calls with ToolBench https://github.com/OpenBMB/ToolBench
- https://huggingface.co/xalss/Qwen2-7B-Instruct-glaive-function-calling
- https://huggingface.co/datasets/NousResearch/hermes-function-calling-v1
- Add JiRack tool call tags in the dataset and modify tool call processor if needed


# JiRack RoboTech
- Advanced Tokenizer with Robotics & Routing & Tool calls Tokenizer and other
- [CMSManhattan/JiRackDeltaNetTokenizer](https://huggingface.co/CMSManhattan/JiRackDeltaNetTokenizer)


## Available Variants on Docker with UI
| Tag | Quant | Size | Approx. RAM | Description |
|-----|-------|------|-------------|-------------|
| `cmsmanhattan/jirack-deltanet-27b-cpu:latest` | Full | ~55 GB | ~56–64 GB | Full precision reference |
| `cmsmanhattan/jirack_deltanet_27b-cpu-q4:latest` | Q4_K_M | ~16.8 GB | ~18–24 GB | Recommended balance |
| `cmsmanhattan/jirack-deltanet-27b-cpu-q3:latest` | Q3_K_M | ~13.9 GB | ~15–20 GB | Good quality / size trade-off |
| `cmsmanhattan/jirack-deltanet-27b-cpu-q2:latest` | Q2_K | ~11.2 GB | ~12–17 GB | Maximum compression |
| `cmsmanhattan/jirack-deltanet-27b-cpu-tq2:latest`| TQ_2 | ~7.2 GB | ~8–13 GB |  Ultra compression |



## Quick Start

### Run with Ollama (recommended — reasoning off by default)
- https://ollama.com/cmsmanhattan
```bash
ollama pull cmsmanhattan/JiRackDeltaNet_27b-q4-reasoning
ollama run cmsmanhattan/JiRackDeltaNet_27b-q4-reasoning "What is the capital of France?"
```

### Run with Docker
- 27B docker images can be provided by request.
- Build docker on local from source or request from me.
- Docker images use hidden reasoning logic to make chat clear


**Q8/int8**
```bash
docker run -d \
  --name jirack_deltanet_27b \
  -p 7869:7869 \
  --cpus=16 \
  -e THREADS=16 \
  -e THREADS_BATCH=16 \
  --restart unless-stopped \
  cmsmanhattan/jirack_deltanet_27b-cpu-q8:latest
```

**Q6**
```bash
docker run -d \
  --name jirack_deltanet_27b \
  -p 7869:7869 \
  --cpus=16 \
  -e THREADS=16 \
  -e THREADS_BATCH=16 \
  --restart unless-stopped \
  cmsmanhattan/jirack_deltanet_27b-cpu-q6:latest
```

**Default CPU (Q4/int4 recommended)**
```bash
docker run -d \
  --name jirack_deltanet_27b \
  -p 7869:7869 \
  --restart unless-stopped \
  cmsmanhattan/jirack_deltanet_27b-cpu-q4:latest
```
**Q3**
```bash
docker run -d \
  --name jirack_deltanet_27b \
  -p 7869:7869 \
  --cpus=16 \
  -e THREADS=16 \
  -e THREADS_BATCH=16 \
  --restart unless-stopped \
  cmsmanhattan/jirack_deltanet_27b-cpu-q3:latest
```
**Q2 (lowest memory)**
```bash
docker run -d \
  --name jirack_deltanet_27b \
  -p 7869:7869 \
  --cpus=16 \
  -e THREADS=16 \
  -e THREADS_BATCH=16 \
  --restart unless-stopped \
  cmsmanhattan/jirack_deltanet_27b-cpu-q2:latest
```

**TQ_2 (Ultra lowe memory)**
```bash
docker run -d \
  --name jirack_deltanet_27b \
  -p 7869:7869 \
  --cpus=16 \
  -e THREADS=16 \
  -e THREADS_BATCH=16 \
  --restart unless-stopped \
  cmsmanhattan/jirack-deltanet-27b-cpu-tq2:latest
```



**Full precision**
```bash
docker run -d \
  --name jirack_deltanet_27b \
  -p 7869:7869 \
  --cpus=16 \
  -e THREADS=16 \
  -e THREADS_BATCH=16 \
  --restart unless-stopped \
  cmsmanhattan/jirack-deltanet-27b-cpu:latest
```
**Multi CPU**
```bash
docker run -d \
  --name jirack_deltanet_27b \
  -p 7869:7869 \
  --cpus=16 \
  -e THREADS=16 \
  -e THREADS_BATCH=16 \
  --restart unless-stopped \
  --memory=32g \
  --cpus=8 \
  cmsmanhattan/jirack-deltanet-27b-q4:latest
```

### Docker Compose Example
```yaml
services:
  jirack:
    image: cmsmanhattan/jirack-deltanet-27b-cpu-tq2:latest
    container_name: jirack_deltanet_27b
    ports:
      - "7869:7869"
    volumes:
      - .:/app
      - ./web:/app/web
    environment:
      - MAX_TOKENS=2048
      - TEMPERATURE=0.7
      - TOP_P=0.8
      - TOP_K=20
      - DEFAULT_STREAM=False
      - INTRA_THREADS=4
      - USE_ENV_ALLOCATOR=1
      - THREADS=16
      - THREADS_BATCH=16
    deploy:
      resources:
        limits:
          memory: 32g
```

## Ollama platform
- CPU without JiRack UI
- GPU without JiRack UI
- Ollama images displays reasoning logic by default but it can be off .
- Use JiRack UI from https://www.jirack.com
- cmsmanhattan/JiRackDeltaNet_27b-reasoning:latest         54 GB   
- cmsmanhattan/JiRackDeltaNet_27b-q2-reasoning:latest      10 GB   
- cmsmanhattan/JiRackDeltaNet_27b-q3-reasoning:latest      13 GB    
- cmsmanhattan/JiRackDeltaNet_27b-q4-reasoning:latest      16 GB    
- cmsmanhattan/JiRackDeltaNet_27b-q6-reasoning:latest      22 GB    
- cmsmanhattan/JiRackDeltaNet_27b-q8-reasoning:latest      29 GB     


## Access the UI
Once the container is running, open your browser and navigate to:
`http://localhost:7869`
This opens the JiRack UI — a clean web interface.

## Changing the Port
The listening port can be easily modified directly from the **Settings** panel within the JiRack UI.

## Licensing

- Model weights are released under the MIT License — free to use, modify, and distribute for any purpose, including commercial. No royalties, no per-user fees, no subscription.
- The Docker image with UI and the pre-built Ollama quantizations are separate paid products. If you prefer to build your own secure deployment — take the weights, assemble your own stack, and you're done.

- The JiRack DeltaNet 27B model for Docker and Ollama is provided under a commercial license ($12 per user per year).
- All JiRack UI clients are provided under a commercial license.
- However, the UI clients can be used for free when running together with the official JiRack Docker containers, as long as they are not redistributed separately.

For commercial licensing, cluster deployment, or enterprise use of JiRack models, please contact us.
- **JiRack MS Windows 11 Desktop Client (with Ollama API):**
  https://huggingface.co/kgrabko/JiRackTernary_1b/resolve/main/jirack-chat.zip
- **Live email chat with the model:** support@cmsmanhattan.com

## Hardware Recommendations

### Recommended Hardware for JiRack DeltaNet 27B (single Docker container)
| Use Case          | CPU                        | RAM       | Recommended Quant | Expected Speed      | Recommendation |
|-------------------|----------------------------|-----------|--------------------|---------------------|----------------|
| Recommended       | Ryzen 9 / Intel i9 / Xeon  | 24–32 GB  | Q4_K_M             | Good interactive    | Best choice    |
| High Performance  | High-core server CPU       | 48 GB+    | Full / Q4          | Excellent           | Excellent      |
| Low Memory        | Modern 12+ core CPU        | 16–24 GB  | Q3_K_M or Q2_K     | Usable              | Acceptable     |
| Edge / Minimal    | Strong workstation CPU     | 16 GB     | Q2_K               | Acceptable          | Budget option  |

## Important Memory Notes
Even though the quantized 27B models are relatively compact for their size, we recommend the following for best experience:
- Q4_K_M: 18–24 GB system RAM minimum
- Q3_K_M / Q2_K: 15–20 GB system RAM
- Full precision: 48 GB+ system RAM recommended

Reasons for extra headroom:
- KV-cache consumption during generation
- Runtime overhead and temporary buffers
- System stability and avoiding out-of-memory errors
- Room for larger context windows

**Minimum recommended (Q4):** 18 GB system RAM
**Ideal:** 24–32 GB system RAM

I added the default model in full precision. This serves as the base for quantization, allowing us to find the optimal balance between model size and performance.

## Architecture Notes
- **Qwen3.8-style DeltaNet architecture**: hybrid attention + SSM design (`qwen35` in GGUF metadata)
- **Updated tokenizer**: Extended with new special tags for **Routing**, **Tool call**, and **Robotics**
- **No-forced-reasoning support**: chat template patched so `<think>` blocks default to closed; native support on Ollama
- Hidden 5120, 65 layers, attention heads 24 / KV heads 4, feed-forward 17408
- SSM: conv kernel 4, state size 128, group count 16, time-step rank 48, inner size 6144
- RoPE θ = 10,000,000, RMSNorm ε = 1e-6
- Context length: up to 262,144 tokens
- Ready-to-run GGUF quantizations (Q2_K, Q3_K_M, Q4_K_M)

## Benchmarks
JiRack DeltaNet 27B is built on the Qwen3.5/Qwen3.8-style DeltaNet architecture. The table below reproduces the published base-model benchmark results from [Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) for reference — these reflect the upstream base model's capabilities, not JiRack-specific fine-tuning or quantization results.

### Text Performance

|                                                         | Qwen3.8-27B | Qwen3.6-27B | Qwen3.7-Plus | Muse Glimmer-30B | Opus4.6 Max |
|---------------------------------------------------------|-------------|-------------|--------------|-------------------|-------------|
| **Coding** | | | | | |
| Agentic terminal coding — Terminal Bench 2.1 (Terminus)  | 73.0        | 63.4        | 64.0         | 51.7              | **78.2**    |
| Agentic coding — SWE-bench Pro                           | **61.7**    | 53.5        | 57.6         | 51.2              | 53.4        |
| Repo-level code generation — NL2Repo-Bench               | 42.3        | 36.2        | 41.1         | --                | **47.6**    |
| Agentic coding — DeepSWE 1.1                             | **42.2**    | 13.3        | 14.2         | --                | --          |
| Software engineering — QwenSWEBench                      | **79.0**    | 49.3        | 59.2         | --                | 63.8        |
| **Agent** | | | | | |
| Long-horizon office work — CoWorkBench                   | **70.7**    | 61.0        | 65.1         | --                | 68.2        |
| Professional job tasks — JobBench                        | **33.4**    | 21.8        | 27.6         | --                | --          |
| Frontier agentic tasks — Agents' Last Exam (Pass@1/Score)| **20.4 / 42.9** | 10.6 / 27.3 | 13.2 / 33.6 | --          | --          |
| **General** | | | | | |
| Instruction following — IFBench                          | **79.5**    | 69.1        | 79.1         | 77.0              | 62.5        |
| Scientific reasoning — GPQA Diamond                       | 89.2        | 87.8        | 90.3         | 83.5              | **91.3**    |
| Multidisciplinary reasoning — HLE                         | 30.8        | 24.0        | 34.7         | 22.0              | **40.0**    |
| Competitive coding — LiveCodeBench v6                     | **90.3**    | 83.9        | 89.6         | --                | 88.8        |

### VL Performance

|                                          | Qwen3.8-27B | Qwen3.6-27B | Qwen3.7-Plus | Muse Glimmer-30B | Opus4.6 Max |
|------------------------------------------|-------------|-------------|--------------|-------------------|-------------|
| **Agentic Multimodal Intelligence** | | | | | |
| Computer use — OSWorld-Verified          | **84.3**    | 63.9        | 73.3         | 65.9              | 72.7        |
| Browser use — WebArena-Verified          | **64.8**    | 48.8        | 55.3         | --                | --          |
| Mobile use — AndroidWorld                | **81.9**    | 70.3        | 81.0         | --                | 62.0        |
| Application recreation — RecreationBench | **47.1**    | 29.8        | 30.2         | --                | --          |
| Multimodal tool use — ClawEval-MM (Pass@3/Avg) | 57.4 / 56.9 | 42.6 / 50.4 | **57.4 / 60.1** | --          | 52.5 / 54.7 |
| Multimodal SWE — SWE-MM                  | **38.6**    | 25.7        | 30.0         | --                | 27.1        |
| Visual web development — Vision2Web      | **62.9**    | 45.0        | 42.1         | --                | --          |
| **General Multimodal Intelligence** | | | | | |
| Visual math — MathVision (w/o CI / w/ CI)| 90.0 / **94.6** | 85.1 / -- | **90.3** / -- | --            | 65.5 / --   |
| General visual reasoning — BabyVision (w/o CI / w/ CI) | **65.7 / 85.6** | 28.9 / -- | 64.7 / 70.4 | --      | 12.6 / --   |
| Scientific chart analysis — CharXiv (RQ) (w/o CI / w/ CI) | 83.7 / **90.2** | 78.4 / -- | **85.8** / 85.9 | 78.8      | 66.0 / --   |
| Document intelligence — OmniDocBench 1.5 | 91.1        | 89.4        | **91.4**     | 75.8              | 86.6        |
| Real-world perception — RealWorldQA      | 85.9        | 84.1        | **86.9**     | --                | 73.9        |
| Embodied intelligence — ERQA             | 65.5        | 62.5        | **69.8**     | --                | 40.8        |

*Source: [Qwen/Qwen3.8-27B model card](https://huggingface.co/Qwen/Qwen3.8-27B). Best result in each row is bolded. Empty cells (--) indicate results not yet available. See the source card for full evaluation methodology and footnotes.*

## 📧 Contact & Licensing
For joint venture opportunities, hardware integration, or licensing inquiries:
- **Email:** grabko@cmsmanhattan.com
- **Phone:** +1 (516) 777-0945
- **Location:** New York, USA


## License
MIT License

![NVIDIA Inception Program Member](https://huggingface.co/spaces/CMSManhattan/README/resolve/main/badge.jpg)
