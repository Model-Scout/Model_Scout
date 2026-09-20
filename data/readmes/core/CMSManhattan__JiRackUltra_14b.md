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
- ternary
- bitnet
- 1.58bit
- cpu
- gguf
- qwen2.5
- deepseek
- efficient
- low-memory
- jirack
- web-ui
- routing
- tool-call
- robotics
license: mit
---
# JiRack Ultra 14B (CPU)
A fast and efficient 14B model optimized for CPU inference. The model was refactored with BitNet features and an updated tokenizer that includes new **Routing**, **Media**, **Vision**, **Sound**, **Tool call**, and **Robotics** tags. Built on a DeepSeek R1-14B architecture with native ternary (BitNet-style) support and ready-to-run GGUF quantizations.
- JiRack is a cloud-ready model that helps save money on cloud infrastructure. It can be used as an expert model in RAG deployments, with the ONNX JiRack Java server as an alternative.



# JiRack Ternary Architedure & JiRack Tokenizer
- Benefits high quality CPU inference TQ_2 on Llama.cpp and Ollama via QAT
- Robotcs, Routing, Coding,  Multimedia, Advanced tool calling via CMSManhattan/JiRackPrecisionTokenizer
- 

# JiRack sevice options
- Current quantizations were done from the FP16 model, but the model allows for more compression thanks to its ternary architecture. 
- If you need to do ternary compression, please write to me and I'll perform QAT from your dataset, tailored specifically to your task.
- Plus double QAT via ONNX QAT.
- Adapt train process to avoid catastrophic forgetting with NDA
- Adapt train process to avoid fast plato in training with NDA
- Convert model to TQ2_0 with support AVX2 and AVX-512 CPU instructions for high performance on CPU
- QAT for TQ_2 Llama.cpp Ternarization docs https://huggingface.co/CMSManhattan/JiRackUltra_14b/blob/main/QAT_to_Llama.cpp_GGUF_TQ2_0_JirackUltra_14b.md
- Adapts to agentic or instruct models for tool calling, using the JiRak tokenizer to enable high-quality tool calling on small models — built as a domain-specific tool expert.
- Deployment and scale

# JiRack Codding Agent IDE
- It is Agent Coding IDE for JiRack Models to run via Ollama on home PC 
- It good choose for Agent Coding IDE such as Cursor , Windsurf IDE or Devin IDE etc but more safe that ask you to apply changes and review.
- Web site https://www.jirack.com
- Final release version https://huggingface.co/CMSManhattan/JiRackDeltaNet_27b/resolve/main/jirack_ide_final.zip

# Ollama production support 
- We are working to support JiRack on Ollama for production systems also 
- added Jirack chat without reasoning feature  https://ollama.com/cmsmanhattan 
- Follow fresh Ollama platform updates


# Spring Boot AI tool calls examples for JiRack Ultra series
- Tool call library on java for Enterprise  https://github.com/alibaba/spring-ai-alibaba

# GoEx AI tool calls examples for JiRack Ultra series  
- Tool call library on python  https://github.com/ShishirPatil/gorilla

# JiRack Ultra 1 tool calls to boost tool call quality
- Use JiRack Precision tokenzer tags for tool calls with ToolBench https://github.com/OpenBMB/ToolBench
- https://huggingface.co/xalss/Qwen2-7B-Instruct-glaive-function-calling
- https://huggingface.co/datasets/NousResearch/hermes-function-calling-v1
- Add JiRack tool call tags in the dataset and modify tool call processor if needed

  

# JiRack RoboTech
- Advanced Tokenizer with  Robotics & Routing & Tool calls Tokenizer and other
- [CMSManhattan/JiRackPrecisionTokenizer](https://huggingface.co/CMSManhattan/JiRackPrecisionTokenizer)
  
## Available Variants
| Tag | Quant | Size | Approx. RAM | Description |
|-----|-------|------|-------------|-------------|
| `cmsmanhattan/jirack-ultra-14b-cpu:latest` | Full | 28.1 GB | ~28–32 GB | Full precision reference |
| `cmsmanhattan/jirack-ultra-14b-cpu-q4:latest` | Q4_K_M | 10.1 GB | ~8–12 GB | Recommended balance |
| `cmsmanhattan/jirack-ultra-14b-cpu-q3:latest` | Q3_K_M | 8.42 GB | ~7–10 GB | Good quality / size trade-off |
| `cmsmanhattan/jirack-ultra-14b-cpu-q2:latest` | Q2_K | 6.81 GB | ~6–9 GB | Maximum compression |
## Quick Start
### Run with Docker
- 14 B docker can be provided by request .
- Build docker on local from source or request fro me

**Default CPU (Q4 recommended)**
```bash
docker run -d \
  --name jirack_ultra_14b \
  -p 7869:7869 \
  --restart unless-stopped \
  cmsmanhattan/jirack-ultra-14b-cpu-q4:latest
```
**Q3**
```bash
docker run -d \
  --name jirack_ultra_14b \
  -p 7869:7869 \
  --cpus=16 \
  -e THREADS=16 \
  -e THREADS_BATCH=16 \
  --restart unless-stopped \
  cmsmanhattan/jirack-ultra-14b-cpu-q3:latest
```
**Q2 (lowest memory)**
```bash
docker run -d \
  --name jirack_ultra_14b \
  -p 7869:7869 \
  --cpus=16 \
  -e THREADS=16 \
  -e THREADS_BATCH=16 \
  --restart unless-stopped \
  cmsmanhattan/jirack-ultra-14b-cpu-q2:latest
```
**Full precision**
```bash
docker run -d \
  --name jirack_ultra_14b \
  -p 7869:7869 \
  --cpus=16 \
  -e THREADS=16 \
  -e THREADS_BATCH=16 \
  --restart unless-stopped \
  cmsmanhattan/jirack-ultra-14b-cpu:latest
```
**Multi CPU**
```bash
docker run -d \
  --name jirack_ultra_14b \
  -p 7869:7869 \
  --cpus=16 \
  -e THREADS=16 \
  -e THREADS_BATCH=16 \
  --restart unless-stopped \
  --memory=16g \
  --cpus=8 \
  cmsmanhattan/jirack-ultra-14b-cpu-q4:latest
```
### Docker Compose Example
```yaml
services:
  jirack:
    image: cmsmanhattan/jirack-ultra-14b-cpu-q4:latest
    container_name: jirack_ultra_14b
    ports:
      - "7869:7869"
    volumes:
      - .:/app
      - ./web:/app/web
    environment:
      - MAX_TOKENS=2048
      - TEMPERATURE=0.7
      - TOP_P=0.9
      - DEFAULT_STREAM=False
      - INTRA_THREADS=4
      - USE_ENV_ALLOCATOR=1
      - THREADS=16
      - THREADS_BATCH=16
    deploy:
      resources:
        limits:
          memory: 16g
```
## Access the UI
Once the container is running, open your browser and navigate to:
`http://localhost:7869`
This opens the JiRack UI — a clean web interface.
## Changing the Port
The listening port can be easily modified directly from the **Settings** panel within the JiRack UI.
## Licensing
- Model weights are released under the MIT License — free to use, modify, and distribute for any purpose, including commercial. No royalties, no per-user fees, no subscription.
- The Docker image with UI and the pre-built Ollama quantizations are separate paid products. If you prefer to build your own secure deployment — take the weights, assemble your own stack, and you're done.
- The JiRack Ultra 14B model for Docker and Ollama is provided under a commercial license ($12 per user per year).
- All JiRack UI clients are provided under a commercial license.
- However, the UI clients can be used for free when running together with the official JiRack Docker containers, as long as they are not redistributed separately.
For commercial licensing, cluster deployment, or enterprise use of JiRack models, please contact us.
- **JiRack MS Windows 11 Desktop Client (with Ollama API):**
  https://huggingface.co/kgrabko/JiRackTernary_1b/resolve/main/jirack-chat.zip
- **Live email chat with the model:** support@cmsmanhattan.com
## Hardware Recommendations
### Recommended Hardware for JiRack Ultra 14B (single Docker container)
| Use Case | CPU | RAM | Recommended Quant | Expected Speed | Recommendation |
|-------------------|------------------------------|----------|-------------------|---------------------|----------------|
| Recommended | Ryzen 7 / Intel i7 | 24–32 GB | Q4_K_M | Good interactive | Best choice |
| High Performance | Ryzen 9 / Intel i9 | 32–48 GB | Full / Q4 | Excellent | Excellent |
| Low Memory | Modern 8+ core CPU | 16–24 GB | Q3_K_M or Q2_K | Usable | Acceptable |
| Edge / Minimal | Strong laptop CPU | 16 GB | Q2_K | Acceptable | Budget option |
## Important Memory Notes
Even though the quantized 14B models are relatively compact, we recommend the following for best experience:
- Q4_K_M: 16–24 GB system RAM minimum
- Q3_K_M / Q2_K: 12–20 GB system RAM
- Full precision: 32 GB+ system RAM recommended
Reasons for extra headroom:
- KV-cache consumption during generation
- Runtime overhead and temporary buffers
- System stability and avoiding out-of-memory errors
- Room for larger context windows
**Minimum recommended (Q4):** 16 GB system RAM  
**Ideal:** 24–32 GB system RAM
I added the default model in full precision. This serves as the base for quantization, allowing us to find the optimal balance between model size and performance.
## Architecture Notes
- **Refactored with BitNet features**: Native BitLinear ternary path (b1.58-style) with λ-warmup STE
- **Updated tokenizer**: Extended with new special tags for **Routing**, **Tool call**, and **Robotics**
- Base: Qwen2.5-14B style (Hidden 5120, 48 layers, GQA 40/8, vocab 152064)
- RoPE θ = 1 000 000, RMSNorm ε = 1e-6
- Intermediate size: 13824
- Ready-to-run GGUF quantizations (Q2_K, Q3_K_M, Q4_K_M)
## 📧 Contact & Licensing
For joint venture opportunities, hardware integration, or licensing inquiries:
- **Email:** grabko@cmsmanhattan.com
- **Phone:** +1 (516) 777-0945
- **Location:** New York, USA



## License
MIT License