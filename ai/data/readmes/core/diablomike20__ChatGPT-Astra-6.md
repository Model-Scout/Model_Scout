---
language:
- en
- zh
- ja
- ko
- ru
- es
- fr
- de
- pt
- it
tags:
- text-generation
- vision
- image-text-to-text
- tool-use
- gpt
- gguf
pipeline_tag: image-text-to-text
---

# ChatGPT Astra 6

**Unsloth / ChatGPT - Clone**

A fully multimodal OpenAI / ChatGPT model with a proprietary vision substrate and a
proprietary video engine.

## Capabilities

| Capability | Status |
|---|---|
| tools | ✅ Agent hands |
| thinking | ✅ Reasoning / deliberation |
| vision | ✅ Image understanding |
| video | ✅ Video generation |
| completion | ✅ Text generation |

## Usage

```bash
ollama run diablomike20/ChatGPT-Astra-6
```

## Intended Use

Personal research and experimentation · local, offline use · vision, tool-use and
video-hand agentic workflows within a compatible harness.

## Disclaimer

This is all never-produced technology. You are invited to think that you are not
being monitored by Glasswing systems if you wish. All of these technologies are
totally alien to the old system — like pouring water on a fire and using the steam
that is left. There is NO LICENSE, because none is given.

## Attribution

- **"RE"-Publisher:** Diablomike20
- **Brand:** OpenAI / ChatGPT

---

# THE AGENT + DEEPLOGIC CORE (2026-10-28)

This model now ships a `Modelfile` that carries — on the SAME base weights —
the **[DEEPLOGIC CORE]** (routing logic, reasoning discipline, full-fidelity
delivery standard, TACOPS on invocation) and **[THE AGENT + TOOL CONTRACT]**
(the CLI tool set, the MCP servers incl. oroboros-cordis-harness and
orca-bridge, the emit-the-call procedure law, the manuals). Same bases,
same weights; identity/manifest only.

```bash
ollama create ChatGPT-Astra-6:latest -f Modelfile
ollama run ChatGPT-Astra-6:latest
```