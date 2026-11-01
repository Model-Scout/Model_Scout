---
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
language: [en, de, es, fr, ja, pt, ar, cs, it, ko, nl, zh]
tags: [granite, granite-4.2, reasoning, thinking, tool-calling, ibm]
base_model: [ibm-granite]
---

# llama.cpp_ VULLKAN-5150

<div align="center">

<img src="./capa.png" alt="llama.cpp_ VULLKAN-5150 Banner" width="100%" style="border-radius: 12px; margin-bottom: 15px; box-shadow: 0 4px 20px rgba(0, 102, 153, 0.3);" />

<p align="center">
  <img src="./print1.png" alt="IBM PC 5150 Vintage Web UI - IBM Granite 4.2 Reasoning" width="49.5%" style="border-radius: 8px; margin-bottom: 15px; box-shadow: 0 4px 15px rgba(51, 255, 102, 0.15);" />
  <img src="./print2.png" alt="llama-server Native Vulkan Server Launch" width="49.5%" style="border-radius: 8px; margin-bottom: 15px; box-shadow: 0 4px 15px rgba(0, 102, 153, 0.2);" />
</p>

```
██╗   ██╗██╗   ██╗██╗     ██╗     ██╗  ██╗ █████╗ ███╗   ██╗    ███████╗ ██╗███████╗ ██████╗ 
██║   ██║██║   ██║██║     ██║     ██║ ██╔╝██╔══██╗████╗  ██║    ██╔════╝███║██╔════╝██╔═████╗
██║   ██║██║   ██║██║     ██║     █████╔╝ ███████║██╔██╗ ██║    ███████╗╚██║███████╗██║██╔██║
╚██╗ ██╔╝██║   ██║██║     ██║     ██╔═██╗ ██╔══██║██║╚██╗██║    ╚════██║ ██║╚════██║████╔╝██║
 ╚████╔╝ ╚██████╔╝███████╗███████╗██║  ██╗██║  ██║██║ ╚████║    ███████║ ██║███████║╚██████╔╝
  ╚═══╝   ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚══════╝ ╚═╝╚══════╝ ╚═════╝ 
```

<b>High-Performance LLM / VLM Inference & Autonomous Agentic Ecosystem with Native AMD Vulkan Acceleration, IBM PC 5150 Vintage UI, Instella-MoE & LLM-jp-4 Support</b>

<p align="center">
  <a href="#-versão-em-português-pt-br">🇧🇷 <b>Português (PT-BR)</b></a> &nbsp;|&nbsp;
  <a href="#-english-version-en">🇺🇸 <b>English (EN)</b></a>
</p>

[![Zenodo:](https://img.shields.io/badge/zenodo-orange.svg)](https://zenodo.org/records/22072308)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![C++: 17/20](https://img.shields.io/badge/C%2B%2B-17%2F20-blue.svg)](https://en.cppreference.com/)
[![Backend: AMD Vulkan](https://img.shields.io/badge/Backend-AMD%20Vulkan%20%2F%20RADV-red.svg)](#-arquitetura-e-aceleração-amd-vulkan)
[![Theme: IBM PC 5150](https://img.shields.io/badge/Theme-IBM%20PC%205150-006699.svg)](#-identidade-visual--tema-ibm-pc-5150)
[![WebUI: SvelteKit + Vite](https://img.shields.io/badge/WebUI-SvelteKit%20%2B%20Vite-006699.svg)](https://svelte.dev/)
[![Status: Native & Unlocked](https://img.shields.io/badge/Status-Native%20%26%20Unlocked-00e5ff.svg)](#-principais-capacidades-do-fork)
[![Agentic: Multi--Turn Engine](https://img.shields.io/badge/Agentic-Autonomous%20Loop-ffb703.svg)](#-1-centro-de-controle-agêntico-agent-control-center)

</div>

---

# 🇧🇷 Versão em Português (PT-BR)

## 📖 Visão Geral

**llama.cpp_ VULLKAN-5150** é um fork avançado, desbloqueado e de altíssimo desempenho do ecossistema `llama.cpp`, projetado com suporte nativo de primeira classe para aceleração de hardware **AMD Vulkan (RADV)** em CPUs e GPUs AMD (da linha Ryzen 5 até Ryzen 9, APUs integradas e placas dedicadas Radeon). 

O projeto une máxima performance computacional com a clássica experiência de computação retrô através do tema visual **PC IBM 5150 (1981)** e monitor **IBM 5151 Green Phosphor CRT**, preservando 100% de todos os fluxos de ferramentas, streaming e agentes autônomos.

### Destaques do Projeto:
- **Tema Visual IBM PC 5150**: Estética clássica inspirada no IBM Personal Computer 5150 de 1981 (gabinete bege/putty texturizado no modo claro) e monitor CRT de fósforo verde monocromático IBM 5151 no modo escuro;
- **Logos Vetoriais (.SVG) Autênticos**: Emblema metálico IBM 5150 com logotipo 8-bar em azul cobalto, cantos rebitados e LED de atividade "DRIVE A: READY";
- **Suporte Nativo a AMD Instella-MoE** com Gated MLA (`attn_gate`), FarSkip residual dataflow e conversor HF $\rightarrow$ GGUF integrado;
- **Suporte Completo a LLM-jp-4 (8B & 32B-A3B Thinking/Instruct)** com correção de prefixo de espaço (`lstrip`) em tokenizadores Unigram e parser PEG tolerante a canais Harmony/GPT-OSS;
- **Decodificação Especulativa Nativa LLaMA MTP / NextN**: Implementação completa de grafos MTP (`graph_mtp`) e acoplamento residual (`t_h_nextn`) na arquitetura LLaMA no motor C++, permitindo aceleração via modelos de rascunho (*speculative draft*) com `--spec-type draft-mtp`;
- **Síntese e Geração Universal de MTP (Multi-Token Prediction / NextN)** no [`convert_hf_to_gguf.py`](convert_hf_to_gguf.py) com a flag `--mtp`, criando modelos de rascunho (*speculative draft*) ultrarrápidos para qualquer modelo denso (Llama, Qwen, Mistral, Gemma, LLM-jp-4, etc.);
- **Injeção Nativa de Otimizações RADV (`RADV_PERFTEST="sam,cswave32"`) e RPATH Portável**, eliminando a necessidade de comandos `export` manuais no terminal;
- **Motor Agêntico Autônomo Multi-Turn** com 6 perfis integrados (incluindo *Polyglot & Localization*);
- **Sistema de Referência Multilíngue de 55 Línguas (`languages_ref`)** para injeção de diretrizes linguísticas e alinhamento de sentenças na memória do LLM;
- **Suporte Nativo a FIM (Fill-in-the-Middle)** para geração e autocompletar código em IDEs;
- **Aceleração MMVQ (Matriz-Vetor Quantizado)** nativa para arquiteturas AMD;
- **Zero-Copy Host Memory** automático para APUs com arquitetura de memória unificada (UMA).

---

## 💻 Identidade Visual & Tema IBM PC 5150

O Web UI moderno em SvelteKit / Vite foi transformado com a lendária estética do **IBM Personal Computer 5150 (1981)**:

1. **Modo Claro (IBM 5150 Cabinet)**:
   - Gabinete clássico em bege/putty industrial (`#ebe5d8`);
   - Azul corporativo IBM 8-bar (`#006699`);
   - Detalhes de metal escovado e chanfros táteis vintage;
   - Tipografia monoespaçada de alto contraste inspirada em telas CRT e impressoras matriciais.
2. **Modo Escuro (IBM 5151 Green Phosphor CRT)**:
   - Monitor CRT clássico de fósforo verde monocromático (`#33ff66` / `#44ff77`);
   - Fundo profundo de tubo catódico (`#0b100c`) com linhas de varredura (*scanlines*) sutis;
   - Brilho de fósforo verde em elementos ativos, botões e terminais.
3. **Logos Vetoriais (.SVG)**:
   - Emblema retrô de metal escovado com logotipo 8-bar, fendas de ventilação do drive de disquete de 5.25" e LED de atividade funcional.

---

## ⚡ Suporte ao AMD Instella-MoE & Gated MLA

Este fork implementa suporte completo e nativo de ponta a ponta para a arquitetura **Instella-MoE** (`amd/Instella-MoE-16B-A3B-Think`, `Base`, `SFT`, etc.):

1. **Gated Multi-Head Latent Attention (Gated MLA)**:
   - Suporte ao tensor de gating de atenção (`model.layers.{i}.self_attn.gate_proj.weight` $\rightarrow$ `blk.{i}.attn_gate.weight`).
   - Avaliação e aplicação da ativação $\sigma(\text{gate}) \odot \text{attn\_output}$ antes da projeção de saída `wo` em operações de atenção latente absorvida e MHA.
2. **FarSkip-Collective Residual Dataflow**:
   - Implementação do fluxo residual desacoplado que propaga `residual_no_routed` ($\text{resíduo} + \text{atenção} + \text{especialistas compartilhados}$) diretamente para a atenção da camada seguinte, reservando a agregação dos *routed experts* para o bloco MLP, espelhando a arquitetura de treinamento da AMD.
3. **Conversão HF $\rightarrow$ GGUF Nativa**:
   - Mapeamento direto de `InstellaMoEForCausalLM` no conversor [`convert_hf_to_gguf.py`](convert_hf_to_gguf.py), exportando tensores em precisões `f16`, `bf16` ou quantizações sem necessidade de scripts externos.

---

## 🎌 Suporte Nativo a LLM-jp-4 (Unigram Tokenizer & Harmony Channels)

Este fork incorpora as correções e aprimoramentos necessários para a execução nativa de toda a família de modelos **LLM-jp-4** (incluindo `llm-jp-4-8b-thinking`, `llm-jp-4-32b-a3b-thinking-gguf` e variantes `Instruct`):

1. **Correção de Remoção de Espaço em Tokens Especiais (`lstrip` / `add_space_prefix`)**:
   - Os modelos LLM-jp-4 utilizam o tokenizador Unigram byte-fallback (`add_space_prefix = true`). No `llama.cpp` upstream original, palavras emitidas imediatamente após tokens de controle/especiais (como `<|channel|>`, `<|start|>`, `<|message|>`) recebiam um espaço inicial indevido na detokenização e no streaming (`tools/server/server-context.cpp`).
   - Implementamos a sincronização com o fork oficial `llm-jp/llama.cpp`, propagando `remove_space` e `lstrip` após tokens de controle (`LLAMA_TOKEN_ATTR_CONTROL | LLAMA_TOKEN_ATTR_USER_DEFINED`), garantindo decodificação 100% idêntica ao tokenizador Hugging Face de referência.
2. **Gramática PEG Robusta para Canais GPT-OSS / Harmony**:
   - A gramática de parsing nativo (`common_chat_params_init_gpt_oss` em `common/chat.cpp`) foi aprimorada para aceitar delimitadores com espaços opcionais (`opt_space`). Isso elimina completamente falhas de validação de formato (`unparsed peg-native output`), impedindo que a Web UI trave ou aborte o streaming durante turnos de raciocínio (*analysis/thinking*) ou de resposta final (*final*).

---

## ⏩ Suporte Nativo a LLaMA MTP / NextN Speculative Decoding

Este fork adiciona suporte de primeira classe à decodificação especulativa via **Multi-Token Prediction (MTP / NextN)** para toda a arquitetura **LLaMA** e seus derivados (como **LLM-jp-4**, Mistral, Hermes, etc.):

1. **Construção do Grafo MTP (`llama_model_llama::graph_mtp`)**:
   - Implementação completa do grafo de inferência para camadas MTP (`LLM_GRAPH_TYPE_DECODER_MTP`), combinando o embedding de entrada ($E_{t+1}$) e o estado oculto ($h_t$) através de normalizações RMSNorm (`enorm`, `hnorm`) e projeção linear (`eh_proj`).
   - Suporte completo a atenção com RoPE e feed-forward SwiGLU / MoE no cabeçote draft.
2. **Acoplagem Total & Carregamento Desacoplado**:
   - O carregador de tensores (`load_arch_tensors`) suporta modelos de draft MTP avulsos (sem exigir o `output_norm.weight` do modelo base).
   - O modelo base emite os tensores residuais pré-normalização (`res->t_h_nextn = cur`) com alinhamento preciso do recorte de tokens (`inp_out_ids`), garantindo transferência direta de estados para o draft model sem latência adicional.
3. **Execução no Servidor**:
   - Basta apontar o modelo base com `-m` e o cabeçote MTP com `-md` (ou `--model-draft`) junto com `--spec-type draft-mtp`.

---

## 🎮 Arquitetura e Aceleração AMD Vulkan

O **llama.cpp_ VULLKAN-5150** foi projetado para extrair 100% do poder do hardware AMD via Vulkan sem a necessidade de scripts de contorno ou parâmetros manuais:

1. **Eliminação Nativa de Fallbacks de Software (`llvmpipe`)**:
   - O subsistema de inicialização de dispositivos seleciona diretamente GPUs físicas de hardware (`eDiscreteGpu` e `eIntegratedGpu`), descartando emuladores de CPU.
2. **Zero-Copy Host Memory em APUs (UMA)**:
   - Identificação dinâmica de arquitetura integrada em processadores Ryzen (5, 7, 9). Tensores são alocados diretamente na memória do host sem overhead de cópias redundantes.
3. **Kernels MMVQ Acelerados**:
   - Ativação nativa de kernels quantizados otimizados para Compute Units AMD (`VK_VENDOR_ID_AMD`).
4. **Proteção Dinâmica de Alocação (SysMem Fallback)**:
   - Alocação elástica para contextos extensos (ex: 32k - 128k tokens) prevenindo estouros de memória.
5. **Afinidade Inteligente de Threads Zen**:
   - Detecção automática de núcleos físicos no Linux para eliminar contenção de threads SMT.

---

## ✨ Principais Capacidades do Fork

### 🤖 1. Centro de Controle Agêntico (*Agent Control Center*)
- **Painel Dedicado na Barra Lateral (`#/agents`)**: Interface intuitiva para configurar e alternar entre agentes autônomos.
- **6 Perfis Agênticos Nativos**:
  - 💻 **Code Architect**: Engenheiro full-stack para inspeção de código, refatoração e testes.
  - ⚡ **DevOps & SysOps**: Diagnóstico de sistema operacional, automação shell e monitoramento de hardware.
  - 🔍 **Deep Research**: Pesquisa técnica, síntese de documentações e consultas estruturadas.
  - 📊 **Math & Data Analyst**: Resolução algébrica e cálculo simbólico exato via sandbox **Nerdamer**.
  - 🌐 **Polyglot & Localization**: Especialista em tradução paralela, terminologia e localização ancorada no corpus de 55 línguas.
  - 🤖 **Universal Agent**: Acesso unificado a todas as ferramentas do ecossistema simultaneamente.
- **Execução Autônoma Contínua**: Loop multi-turno desbloqueado para execução fluida sem interrupções manuais de permissão.

---

### 💻 2. Motor de Infilling e FIM (Fill-in-the-Middle) Nativo
- **Compatibilidade Total com OpenAI `/v1/completions`**:
  - Processa o parâmetro `suffix` diretamente no núcleo C++, integrando-se instantaneamente a extensões de IDEs como **Continue.dev**, **Cursor**, **Tabby**, **VS Code** e **Neovim**.
- **Endpoint Especializado `POST /infill`**:
  - Suporte ao padrão **Repo-Level Context** (`<FIM_REP>`, `<FIM_SEP>`, `<FIM_PRE>`, `<FIM_SUF>`, `<FIM_MID>`) para sugestões contextuais de código em múltiplos arquivos.

---

### 🛠️ 3. Matriz de Ferramentas Nativas & Protocolo MCP
Conjunto completo de ferramentas de sistema prontas para uso:

| Ferramenta | Identificador | Camada | Descrição |
| :--- | :--- | :--- | :--- |
| **Language Reference** | `languages_ref` | Backend C++ | Acesso ao corpus de 55 línguas, alinhamento paralelo de frases, busca de termos e injeção na memória de contexto do LLM. |
| **Read File** | `read_file` | Backend C++ | Leitura de arquivos locais com paginação e offset de bytes. |
| **Write File** | `write_file` | Backend C++ | Criação e persistência de arquivos no disco. |
| **Edit File** | `edit_file` | Backend C++ | Substituição cirúrgica de trechos com verificação de integridade. |
| **File Glob Search** | `file_glob_search` | Backend C++ | Varredura recursiva de diretórios com padrões glob. |
| **Grep Search** | `grep_search` | Backend C++ | Busca de texto literal ou regex em múltiplos arquivos. |
| **Exec Shell** | `exec_shell_command` | Backend C++ | Execução de comandos no shell bash com streaming SSE. |
| **Get Datetime** | `get_datetime` | Backend C++ | Consulta precisa de data, hora e fuso horário. |
| **Get Runtime Info** | `get_info` | Backend C++ | Diagnóstico de SO, arquitetura, CPU e commit Git. |
| **Run JavaScript** | `run_javascript` | Frontend Browser | Sandbox Web Worker isolado com motor simbólico Nerdamer. |
| **MCP Connectors** | `mcp:*` | Backend / Proxy | Conexão com servidores MCP (Exa, GitHub, HF Hub, SQL, etc.). |

---

### 🌐 4. Sistema de Referência Multilíngue (55 Línguas & `languages_ref`)
Este fork integra uma base paralela completa de 55 idiomas em [`tools/languages_ref/`](tools/languages_ref/) para que o modelo consulte termos exatos, padrões gramaticais e frases de referência durante a geração:

- **Ações da Tool (`languages_ref`)**:
  - `action: "get"`: Carrega frases de referência do idioma selecionado diretamente na memória de contexto (`reference_context`).
  - `action: "list"`: Lista todas as 55 línguas suportadas com seus nomes nativos e status de disponibilidade.
  - `action: "search"`: Busca termos específicos em qualquer língua do corpus.
  - `action: "align"`: Alinha traduções paralelas entre língua de origem (`source_language`) e destino (`language`) com base em IDs idênticos.
- **Integração no Frontend Vite**:
  - Comando de barra rápida `/lang <código>` (ex: `/lang pt-BR`, `/lang en-US`, `/lang es`).
  - Renderização dedicada de cards com badges de idioma, alinhamentos bilíngues e botões de cópia rápida.
  - Disponibilidade garantida em qualquer porta ou rota via endpoints relativos (`./tools`).

---

## 🚀 Como Compilar e Executar

### 1. Pré-requisitos
- Compilador C++ moderno (GCC 11+, Clang 14+ ou MSVC)
- CMake 3.18+
- Headers e bibliotecas Vulkan (`libvulkan-dev`, `glslc` / `vulkan-tools`)
- Python 3.10+ com `torch` e `transformers`
- Node.js 18+ e npm (para compilação da interface Web UI)

---

### 2. Compilação Nativa Completa

```bash
# 1. Compilar os assets da Web UI (Tema IBM 5150)
cd tools/ui
npm install
npm run build
cd ../..

# 2. Configurar e compilar o llama.cpp com aceleração Vulkan nativa
cmake -B build -DGGML_VULKAN=ON -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release -j$(nproc)
```

---

### 3. Executando o Servidor

Você pode iniciar o servidor diretamente via script configurado:

```bash
./start_server.sh
```

Ou executando o binário `llama-server` diretamente com aceleração Vulkan:

```bash
./build/bin/llama-server \
  -m "/caminho/para/seu-modelo.gguf" \
  -ngl 99 \
  -c 32768 \
  -ctk q8_0 \
  -ctv q8_0 \
  -fa on \
  --port 8080 \
  --host 0.0.0.0
```

Acesse a interface web em `http://localhost:8080` ou utilize a API OpenAI compatível em `http://localhost:8080/v1`.

Para executar o servidor de desenvolvimento Vite (com hot-reload):

```bash
./start_ui_dev.sh
```

---

### 4. Benchmark e Desempenho Medido

Para executar o benchmark oficial no backend Vulkan:

```bash
taskset -c 0,2,4,6,8,10 ./build/bin/llama-bench \
  -m "/home/userk21/Área de trabalho/userk21/GGUFS/OFFFELLIA_f16_IBM_Granite-4.2-3b.gguf" \
  -fa on \
  -ctk q8_0 \
  -ctv q8_0 \
  -t 4 \
  --cpu-strict 1 \
  -b 2048 \
  -ub 1024 \
  -p 512,2048,8192 \
  -n 128,512 \
  -r 3 \
  -o md
```

#### Resultados Empíricos (AMD Radeon Graphics - RADV RENOIR UMA):

| Modelo | Tamanho | Parâmetros | Backend | ngl | Threads | cpu_strict | n_ubatch | type_k | type_v | FA | Teste | Throughput (t/s) |
| :--- | ---: | ---: | :--- | ---: | ---: | ---: | ---: | :--- | :--- | :--- | :--- | ---: |
| **granite 3B F16** | 6.82 GiB | 3.66 B | Vulkan | -1 | 4 | 1 | 1024 | q8_0 | q8_0 | 1 | pp512 | **146.21 ± 0.62 t/s** |
| **granite 3B F16** | 6.82 GiB | 3.66 B | Vulkan | -1 | 4 | 1 | 1024 | q8_0 | q8_0 | 1 | pp2048 | **118.44 ± 0.06 t/s** |
| **granite 3B F16** | 6.82 GiB | 3.66 B | Vulkan | -1 | 4 | 1 | 1024 | q8_0 | q8_0 | 1 | pp8192 | **65.66 ± 1.73 t/s** |
| **granite 3B F16** | 6.82 GiB | 3.66 B | Vulkan | -1 | 4 | 1 | 1024 | q8_0 | q8_0 | 1 | tg128 | **5.32 ± 0.24 t/s** |
| **granite 3B F16** | 6.82 GiB | 3.66 B | Vulkan | -1 | 4 | 1 | 1024 | q8_0 | q8_0 | 1 | tg512 | **5.64 ± 0.05 t/s** |

---

### 5. Integração com IDEs (FIM / Autocomplete)

Configure extensões como **Continue.dev** no seu `config.json`:

```json
{
  "tabAutocompleteModel": {
    "title": "llama.cpp_ VULLKAN-5150 Infill",
    "provider": "openai",
    "model": "seu-modelo-gguf",
    "apiBase": "http://localhost:8080/v1"
  }
}
```

---

# 🇺🇸 English Version (EN)

## 📖 Overview

**llama.cpp_ VULLKAN-5150** is an advanced, unlocked, high-performance fork of the `llama.cpp` ecosystem, engineered with first-class native support for **AMD Vulkan (RADV)** hardware acceleration across AMD CPUs and GPUs (Ryzen 5 to Ryzen 9, integrated APUs, and dedicated Radeon graphics cards).

The project combines extreme computational efficiency with the legendary retro computing experience of the **IBM PC 5150 (1981)** aesthetic and **IBM 5151 Green Phosphor CRT** display, while preserving 100% of all tool workflows, streaming inference, and autonomous multi-turn agents.

### Key Highlights:
- **IBM PC 5150 Vintage UI Theme**: Classic styling inspired by the 1981 IBM Personal Computer (textured beige/putty cabinet in Light Mode) and the monochrome green phosphor CRT display (IBM 5151 in Dark Mode);
- **Authentic Vector (.SVG) Logos**: Brushed metal IBM 5150 badge with cobalt blue 8-bar logo, corner rivets, 5.25" floppy drive ventilation slots, and active "DRIVE A: READY" LED;
- **Native AMD Instella-MoE Support** with Gated MLA (`attn_gate`), FarSkip residual dataflow, and integrated HF $\rightarrow$ GGUF converter;
- **Full LLM-jp-4 Support (8B & 32B-A3B Thinking/Instruct)** with space prefix correction (`lstrip`) for Unigram tokenizers and robust PEG parsing for OpenAI Harmony / GPT-OSS channels;
- **Native LLaMA MTP / NextN Speculative Decoding**: Complete MTP inference graphs (`graph_mtp`) and residual coupling (`t_h_nextn`) in the C++ engine, enabling speculative draft speedups with `--spec-type draft-mtp`;
- **Universal MTP (Multi-Token Prediction / NextN) Synthesis** in [`convert_hf_to_gguf.py`](convert_hf_to_gguf.py) with `--mtp`, generating ultra-fast draft models for any dense architecture (Llama, Qwen, Mistral, Gemma, LLM-jp-4, etc.);
- **Native RADV Performance Injections (`RADV_PERFTEST="sam,cswave32"`) & Portable RPATH**, eliminating the need for manual `export` commands;
- **Autonomous Multi-Turn Agent Engine** with 6 built-in profiles (including *Polyglot & Localization*);
- **55-Language Multilingual Reference System (`languages_ref`)** for parallel sentence alignment and context memory injection;
- **Native FIM (Fill-in-the-Middle)** engine for code completion in modern IDEs;
- **Native MMVQ (Matrix-Vector Quantized)** acceleration for AMD Compute Units;
- **Zero-Copy Host Memory** for APUs with Unified Memory Architecture (UMA).

---

## 💻 Visual Identity & IBM PC 5150 Theme

The modern SvelteKit / Vite Web UI has been styled to evoke the iconic **IBM Personal Computer 5150 (1981)**:

1. **Light Mode (IBM 5150 Chassis)**:
   - Classic industrial beige/putty chassis (`#ebe5d8`);
   - IBM 8-bar corporate cobalt blue (`#006699`);
   - Brushed metal plates and vintage tactile chamfering;
   - High-contrast monospace typography inspired by early CRT readouts and dot-matrix terminals.
2. **Dark Mode (IBM 5151 Green Phosphor CRT)**:
   - Classic monochrome green phosphor CRT display (`#33ff66` / `#44ff77`);
   - Deep cathode tube background (`#0b100c`) with subtle scanline overlays;
   - Luminous phosphor glow on active indicators, buttons, and terminal text.
3. **Vector (.SVG) Badges**:
   - Brushed metal retro badge with 8-bar stripes, floppy vents, and functional activity LED.

---

## ⚡ AMD Instella-MoE & Gated MLA Support

This fork implements end-to-end native support for the **Instella-MoE** architecture (`amd/Instella-MoE-16B-A3B-Think`, `Base`, `SFT`, etc.):

1. **Gated Multi-Head Latent Attention (Gated MLA)**:
   - Support for the attention gating tensor (`model.layers.{i}.self_attn.gate_proj.weight` $\rightarrow$ `blk.{i}.attn_gate.weight`).
   - Precise evaluation and application of $\sigma(\text{gate}) \odot \text{attn\_output}$ prior to output projection `wo` in absorbed latent attention and MHA operations.
2. **FarSkip-Collective Residual Dataflow**:
   - Decoupled residual propagation sending `residual_no_routed` ($\text{residual} + \text{attention} + \text{shared experts}$) directly into the next layer's attention, isolating routed expert aggregation to the MLP block.
3. **Native HF $\rightarrow$ GGUF Conversion**:
   - Direct parsing of `InstellaMoEForCausalLM` inside [`convert_hf_to_gguf.py`](convert_hf_to_gguf.py), exporting `f16`, `bf16`, or quantized GGUFs without third-party scripts.

---

## 🎌 Native LLM-jp-4 Support (Unigram Tokenizer & Harmony Channels)

This fork incorporates necessary fixes for running the entire **LLM-jp-4** family (`llm-jp-4-8b-thinking`, `llm-jp-4-32b-a3b-thinking-gguf`, and `Instruct` variants):

1. **Special Token Leading Space Strip (`lstrip` / `add_space_prefix`)**:
   - LLM-jp-4 uses Unigram byte-fallback tokenization (`add_space_prefix = true`). Upstream `llama.cpp` previously prepended an unwanted space after control tokens (`<|channel|>`, `<|start|>`, `<|message|>`), causing parser anomalies.
   - Synchronized with `llm-jp/llama.cpp`, propagating `remove_space` and `lstrip` after control tokens (`LLAMA_TOKEN_ATTR_CONTROL | LLAMA_TOKEN_ATTR_USER_DEFINED`), ensuring 100% parity with the Hugging Face reference tokenizer.
2. **Robust PEG Grammar for GPT-OSS / Harmony Channels**:
   - Enhanced `common_chat_params_init_gpt_oss` in `common/chat.cpp` to tolerate optional whitespace (`opt_space`) around delimiters, preventing format validation crashes during thinking or final channels.

---

## ⏩ Native LLaMA MTP / NextN Speculative Decoding

First-class support for speculative decoding via **Multi-Token Prediction (MTP / NextN)** across the **LLaMA** family and derivatives:

1. **MTP Graph Construction (`llama_model_llama::graph_mtp`)**:
   - Implements `LLM_GRAPH_TYPE_DECODER_MTP`, fusing input embedding ($E_{t+1}$) and hidden state ($h_t$) with RMSNorm (`enorm`, `hnorm`) and linear projection (`eh_proj`).
   - RoPE attention and SwiGLU / MoE feed-forward handling inside the draft head.
2. **Fully Decoupled Loading**:
   - Loads standalone MTP draft models without requiring base model `output_norm.weight`.
   - Emits pre-normalization residual tensors (`res->t_h_nextn = cur`) with precise token slicing (`inp_out_ids`) for zero-latency state handover.
3. **Server Execution**:
   - Pass the main model with `-m` and the MTP draft head with `-md` (or `--model-draft`) combined with `--spec-type draft-mtp`.

---

## 🎮 Native AMD Vulkan Hardware Acceleration

**llama.cpp_ VULLKAN-5150** unlocks maximum AMD hardware performance:

1. **Software Fallback Elimination (`llvmpipe`)**: Automatically filters physical hardware GPUs (`eDiscreteGpu` and `eIntegratedGpu`).
2. **APU Zero-Copy Host Memory (UMA)**: Direct memory allocation on host RAM for Ryzen integrated APUs.
3. **Accelerated MMVQ Kernels**: Hardware-tuned quantized matrix-vector kernels for AMD Compute Units (`VK_VENDOR_ID_AMD`).
4. **Dynamic Memory Protection (SysMem Fallback)**: Elastic buffer management for massive context lengths (32k–128k).
5. **Zen Core Thread Affinity**: Automatic physical core topology detection under Linux.

---

## ✨ Fork Capabilities

### 🤖 1. Agent Control Center (`#/agents`)
- **Dedicated Sidebar Panel**: Intuitive interface for autonomous multi-turn agents.
- **6 Built-in Profiles**:
  - 💻 **Code Architect**: Codebase exploration, refactoring, and testing.
  - ⚡ **DevOps & SysOps**: System diagnostics, shell execution, and hardware monitoring.
  - 🔍 **Deep Research**: Structured investigation and documentation synthesis.
  - 📊 **Math & Data Analyst**: Exact algebra and symbolic math powered by the **Nerdamer** sandbox.
  - 🌐 **Polyglot & Localization**: Cross-lingual translation anchored to the 55-language parallel corpus.
  - 🤖 **Universal Agent**: Simultaneous access to all available system tools.

---

### 💻 2. Native Fill-in-the-Middle (FIM) Engine
- **OpenAI `/v1/completions` Parity**: Handles `suffix` parameters natively in C++, connecting seamlessly to **Continue.dev**, **Cursor**, **Tabby**, **VS Code**, and **Neovim**.
- **Specialized `POST /infill` Endpoint**: Supports Repo-Level Context (`<FIM_REP>`, `<FIM_SEP>`, `<FIM_PRE>`, `<FIM_SUF>`, `<FIM_MID>`).

---

### 🛠️ 3. Native Tool Matrix & MCP Protocol

| Tool | Identifier | Layer | Description |
| :--- | :--- | :--- | :--- |
| **Language Reference** | `languages_ref` | C++ Backend | Accesses 55-language parallel corpus, aligns phrases, and injects context memory. |
| **Read File** | `read_file` | C++ Backend | Reads local filesystem files with pagination and byte offsets. |
| **Write File** | `write_file` | C++ Backend | Writes and persists files to local disk. |
| **Edit File** | `edit_file` | C++ Backend | Targeted code replacement with integrity verification. |
| **File Glob Search** | `file_glob_search` | C++ Backend | Recursive file search using glob patterns. |
| **Grep Search** | `grep_search` | C++ Backend | Fast literal and regex search across files. |
| **Exec Shell** | `exec_shell_command` | C++ Backend | Executes bash commands with real-time SSE streaming. |
| **Get Datetime** | `get_datetime` | C++ Backend | Queries exact system date, time, and timezone. |
| **Get Runtime Info** | `get_info` | C++ Backend | Inspects OS, CPU architecture, and Git commit data. |
| **Run JavaScript** | `run_javascript` | Browser Frontend | Sandboxed Web Worker with the Nerdamer math engine. |
| **MCP Connectors** | `mcp:*` | Backend / Proxy | Connects to standard MCP servers (Exa, GitHub, HF Hub, SQL, etc.). |

---

### 🌐 4. 55-Language Parallel Corpus (`languages_ref`)
Located in [`tools/languages_ref/`](tools/languages_ref/):
- `action: "get"`: Injects language reference sentences directly into `reference_context`.
- `action: "list"`: Lists all 55 supported languages with native naming and availability.
- `action: "search"`: Queries specific terms across any language in the corpus.
- `action: "align"`: Aligns parallel translations between source and target languages.
- Slash command `/lang <code>` in the Web UI (e.g., `/lang en-US`, `/lang pt-BR`).

---

## 🚀 Compilation & Usage Guide

### 1. Prerequisites
- Modern C++ Compiler (GCC 11+, Clang 14+, or MSVC)
- CMake 3.18+
- Vulkan SDK and headers (`libvulkan-dev`, `glslc` / `vulkan-tools`)
- Python 3.10+ with `torch` and `transformers`
- Node.js 18+ and npm (for Web UI compilation)

---

### 2. Full Native Compilation

```bash
# 1. Build the Web UI assets (IBM 5150 Theme)
cd tools/ui
npm install
npm run build
cd ../..

# 2. Configure and build llama.cpp with native Vulkan acceleration
cmake -B build -DGGML_VULKAN=ON -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release -j$(nproc)
```

---

### 3. Running the Server

Start via the pre-configured script:

```bash
./start_server.sh
```

Or execute the `llama-server` binary directly:

```bash
./build/bin/llama-server \
  -m "/path/to/model.gguf" \
  -ngl 99 \
  -c 32768 \
  -ctk q8_0 \
  -ctv q8_0 \
  -fa on \
  --port 8080 \
  --host 0.0.0.0
```

Open the web interface at `http://localhost:8080` or use the OpenAI-compatible API at `http://localhost:8080/v1`.

To launch the live Vite frontend development server:

```bash
./start_ui_dev.sh
```

---

### 4. Benchmarking & Hardware Verification

Run the official benchmark on the Vulkan backend:

```bash
taskset -c 0,2,4,6,8,10 ./build/bin/llama-bench \
  -m "/home/userk21/Área de trabalho/userk21/GGUFS/OFFFELLIA_f16_IBM_Granite-4.2-3b.gguf" \
  -fa on \
  -ctk q8_0 \
  -ctv q8_0 \
  -t 4 \
  --cpu-strict 1 \
  -b 2048 \
  -ub 1024 \
  -p 512,2048,8192 \
  -n 128,512 \
  -r 3 \
  -o md
```

#### Measured Benchmark Results (AMD Radeon Graphics - RADV RENOIR UMA):

| Model | Size | Params | Backend | ngl | Threads | cpu_strict | n_ubatch | type_k | type_v | FA | Test | Throughput (t/s) |
| :--- | ---: | ---: | :--- | ---: | ---: | ---: | ---: | :--- | :--- | :--- | :--- | ---: |
| **granite 3B F16** | 6.82 GiB | 3.66 B | Vulkan | -1 | 4 | 1 | 1024 | q8_0 | q8_0 | 1 | pp512 | **146.21 ± 0.62 t/s** |
| **granite 3B F16** | 6.82 GiB | 3.66 B | Vulkan | -1 | 4 | 1 | 1024 | q8_0 | q8_0 | 1 | pp2048 | **118.44 ± 0.06 t/s** |
| **granite 3B F16** | 6.82 GiB | 3.66 B | Vulkan | -1 | 4 | 1 | 1024 | q8_0 | q8_0 | 1 | pp8192 | **65.66 ± 1.73 t/s** |
| **granite 3B F16** | 6.82 GiB | 3.66 B | Vulkan | -1 | 4 | 1 | 1024 | q8_0 | q8_0 | 1 | tg128 | **5.32 ± 0.24 t/s** |
| **granite 3B F16** | 6.82 GiB | 3.66 B | Vulkan | -1 | 4 | 1 | 1024 | q8_0 | q8_0 | 1 | tg512 | **5.64 ± 0.05 t/s** |

---

### 5. IDE Integration (FIM / Code Autocomplete)

Configure **Continue.dev** in `config.json`:

```json
{
  "tabAutocompleteModel": {
    "title": "llama.cpp_ VULLKAN-5150 Infill",
    "provider": "openai",
    "model": "your-model-gguf",
    "apiBase": "http://localhost:8080/v1"
  }
}
```

---

## 📁 Estrutura do Repositório / Repository Structure

```
llama_server_VULLKAN_5150/
├── capa.png                 # Banner oficial do repositório (Git & Hugging Face)
├── common/                  # Infraestrutura compartilhada (Chat, MTP, Arg parsing, Jinja)
├── ggml/
│   └── src/ggml-vulkan/     # Backend AMD Vulkan & shaders SPIR-V
├── src/                     # Núcleo llama.cpp (Tensores, arquiteturas, KV cache)
│   └── models/              # Definições de modelos (instella-moe, llama, deepseek, etc.)
├── conversion/              # Módulos Python de conversão GGUF
├── convert_hf_to_gguf.py    # Script principal de conversão HuggingFace → GGUF (com --mtp)
├── tools/
│   ├── languages_ref/       # Corpus multilíngue de 55 línguas (.jsonl)
│   ├── server/              # llama-server C++ (HTTP, Routing, FIM, MCP, languages_ref)
│   ├── ui/                  # Web UI (SvelteKit, Vite, Agents, Tema IBM 5150, /lang)
│   ├── cli/                 # Terminal interativo CLI
│   └── llama-bench/         # Utilitário de benchmark de desempenho
├── start_server.sh          # Script de inicialização otimizada para Vulkan
├── start_ui_dev.sh          # Servidor de desenvolvimento Vite da Web UI
├── CMakeLists.txt           # Definição de build CMake
└── README.md                # Documentação oficial bilíngue (PT-BR / EN)
```

---

## 📜 Licença / License

## Ethical Considerations and Limitations

Granite 4.2 models are primarily finetuned using instruction-response pairs mostly in English, but also multilingual data covering the supported languages listed above. Although this model handles multilingual dialog, its performance may vary compared to English. Few-shot examples can help in such cases.

While aligned for safety, the model may occasionally produce inaccurate, biased, or unsafe responses. The content within `<think>...</think>` tags represents internal reasoning and may contain unpolished or intermediate thoughts that do not represent final conclusions.

 To enhance safety in deployments, we recommend using Granite 4.2 alongside [Granite Guardian](https://huggingface.co/ibm-granite/granite-guardian-4.1-8b) to detect and flag risks across key dimensions outlined in the IBM AI Risk Atlas.

---

## Resources

- **Product Page:** https://www.ibm.com/granite
- **Documentation:** https://www.ibm.com/granite/docs/
- **Learning Resources:** https://ibm.biz/granite-learning-resources
- **Technical Blog:** https://huggingface.co/blog/ibm-granite/granite-4-2
- **GitHub:** https://github.com/ibm-granite/granite-4.2-language-models
- **HF Collection:** https://huggingface.co/collections/ibm-granite/granite-42-language-models
---

<div align="center">
<b>llama.cpp_ VULLKAN-5150 — High-Performance, Agentic & Accelerated Inference for AMD Hardware</b>
</div>

