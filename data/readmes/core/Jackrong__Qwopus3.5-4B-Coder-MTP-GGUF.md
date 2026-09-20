---
library_name: transformers
base_model:
- Qwen/Qwen3.5-4B
tags:
- gguf
- llama.cpp
- image-text-to-text
- vision
- multimodal
- text-generation-inference
- transformers
- unsloth
- qwen3_5
- reasoning
- chain-of-thought
- mtp
- multi-token-prediction
- speculative-decoding
- lora
- sft
- agent
- tool-use
- function-calling
- coder
- conversational
- RL
license: apache-2.0
language:
- en
- zh
- es
- ru
- ja
pipeline_tag: image-text-to-text
datasets:
- Jackrong/Claude-opus-4.6-TraceInversion-9000x
- Jackrong/Claude-opus-4.7-TraceInversion-5000x
- lambda/hermes-agent-reasoning-traces
---
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid #cbd5e1; border-radius: 16px; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.05); overflow: hidden; background: #ffffff; margin-bottom: 30px;">
  <div style="background: linear-gradient(135deg, #7c3aed 0%, #4c1d95 100%); padding: 24px; color: white;">
  <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
  <h1 style="margin: 0; font-size: 26px; font-weight: 800; display: flex; align-items: center; gap: 12px; color: white; border: none;">🪐 Qwopus3.5-4B-Coder</h1>
  <span style="background: #10b981; color: white; font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 20px; text-transform: uppercase; letter-spacing: 0.5px;">Coder SFT Release</span>
  </div>
  <p style="margin: 8px 0 0 0; font-size: 14px; color: #ddd6fe; font-weight: 500;">Compact Agentic Coding Model Fine-Tuned for Debugging, Tool Use, and Structured Reasoning</p>
  </div>
  <div style="display: flex; gap: 8px; flex-wrap: wrap; padding: 12px 24px; background: #f8fafc; border-bottom: 1px solid #e2e8f0;">
  <span style="background: #f3e8ff; color: #6b21a8; font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 20px; border: 1px solid #e9d5ff;">🧬 Trace Inversion</span>
  <span style="background: #dbeafe; color: #1e40af; font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 20px; border: 1px solid #bfdbfe;">🧠 4B Dense Model</span>
  <span style="background: #e0f2fe; color: #0369a1; font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 20px; border: 1px solid #bae6fd;">⚡ MTP n=2 Tested</span>
  <span style="background: #d1fae5; color: #065f46; font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 20px; border: 1px solid #a7f3d0;">🛠️ Agentic Coding</span>
  <span style="background: #fef3c7; color: #92400e; font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 20px; border: 1px solid #fde68a;">🏆 benchlocal Evaluated</span>
  </div>
  <div style="padding: 24px; display: flex; flex-direction: column; gap: 20px;">
  <div style="background: #f5f3ff; border-left: 5px solid #7c3aed; padding: 16px; border-radius: 0 8px 8px 0;">
  <h3 style="margin: 0 0 8px 0; font-size: 15px; color: #6d28d9; font-weight: 700; display: flex; align-items: center; gap: 6px;"><span>💡</span> What is Qwopus3.5-4B-Coder?</h3>
  <p style="margin: 0; font-size: 13px; color: #334155; line-height: 1.6;">🪐 <b>Qwopus3.5-4B-Coder</b> is a compact coding and agent model built on the Qwen3.5 4B family. It is optimized for local execution, code debugging, structured tool-use behavior, and reasoning-heavy developer workflows. The training recipe follows the Qwopus Coder line: Trace Inversion for learnable reasoning traces, high-quality agent trajectories for tool behavior, and curriculum SFT to preserve formatting stability under longer contexts.</p>
  </div>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-top: 10px;">
  <div style="border: 1px solid #e2e8f0; padding: 14px; border-radius: 8px; background: #fafafa; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);">
  <span style="font-weight: 700; color: #6b21a8; font-size: 12px; display: block; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.5px;">🧩 Structured Debugging</span>
  <span style="font-size: 13px; color: #4b5563; line-height: 1.5;">Targets bug localization, minimal patch reasoning, and environment-verified code repair behavior.</span>
  </div>
  <div style="border: 1px solid #e2e8f0; padding: 14px; border-radius: 8px; background: #fafafa; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);">
  <span style="font-weight: 700; color: #6b21a8; font-size: 12px; display: block; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.5px;">🪶 Agent Trace Alignment</span>
  <span style="font-size: 13px; color: #4b5563; line-height: 1.5;">Learns from tool-call trajectories that include real feedback loops, not only isolated prompt-response pairs.</span>
  </div>
  <div style="border: 1px solid #e2e8f0; padding: 14px; border-radius: 8px; background: #fafafa; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);">
  <span style="font-weight: 700; color: #6b21a8; font-size: 12px; display: block; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.5px;">🔁 MTP-Ready Evaluation</span>
  <span style="font-size: 13px; color: #4b5563; line-height: 1.5;">Benchmarked with Multi-Token Prediction enabled at <code>n=2</code> against the Qwen3.5-4B-MTP reference.</span>
  </div>
  <div style="border: 1px solid #e2e8f0; padding: 14px; border-radius: 8px; background: #fafafa; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);">
  <span style="font-weight: 700; color: #6b21a8; font-size: 12px; display: block; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.5px;">⚡ Local-First Design</span>
  <span style="font-size: 13px; color: #4b5563; line-height: 1.5;">To empower resource-constrained users, the 4B size serves as the sweet spot for running agentic tasks on 16GB laptops, making it an excellent choice for handling simple repetitive tasks and service monitoring operations.</span>
  </div>
  </div>
  </div>
</div>

## 💡 1. Base Model, MTP Setup, and Training Stack

<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; display: flex; flex-direction: column; gap: 20px; margin-bottom: 30px;">
  <!-- Card 1.1: Base Model Overview -->
  <div style="border: 1px solid #cbd5e1; border-radius: 12px; overflow: hidden; background: #ffffff; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
  <div style="background: linear-gradient(135deg, #7c3aed 0%, #5b21b6 100%); padding: 12px 16px; color: white; font-weight: 700; font-size: 14px; display: flex; align-items: center; gap: 8px;">
  <span>🧠</span> 1.1 Base Model Specifications (Qwopus3.5-4B-Coder)
  </div>
  <div style="padding: 16px;">
  <p style="margin: 0 0 16px 0; font-size: 13px; color: #334155; line-height: 1.6;">
  <b>Qwopus3.5-4B-Coder</b> inherits the compact Qwen3.5 4B dense architecture and adapts it toward agentic coding, debugging, tool routing, and long-form reasoning. The 4B size is intended to keep the model deployable on local machines while retaining enough reasoning capacity for developer workflows.
  </p>
  <table style="width: 100%; border-collapse: collapse; font-family: inherit; font-size: 13px;">
  <thead>
  <tr style="background: rgba(124, 58, 237, 0.05);">
  <th style="padding: 8px 10px; border-bottom: 2px solid #7c3aed; text-align: left; color: #7c3aed; font-weight: bold; width: 30%;">Attribute</th>
  <th style="padding: 8px 10px; border-bottom: 2px solid #7c3aed; text-align: left;">Specifications &amp; Details</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: bold;">🧠 Architecture</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">Dense Transformer / 4B-class Qwen3.5 family</td>
  </tr>
  <tr>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: bold;">🎯 Primary Focus</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">Agentic coding, code debugging, tool-use stability, instruction following</td>
  </tr>
  <tr>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: bold;">🧬 Training Recipe</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">Trace Inversion + high-quality agent trajectories + curriculum SFT</td>
  </tr>
  <tr>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: bold;">⚡ Tested MTP Variant</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);"><b>Qwopus3.5-4B-Coder-MTP</b>, configured with MTP <code>n=2</code></td>
  </tr>
  <tr>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: bold;">💾 Reference Model</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);"><b>Qwen3.5-4B-MTP</b>, configured with MTP <code>n=2</code></td>
  </tr>
  <tr>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: bold;">🔬 Additional 4B Comparison</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);"><b>Similar Public 4B Claude-Distilled Variant</b></td>
  </tr>
  </tbody>
  </table>
  </div>
  </div>

  <!-- Card 1.2: Hardware Cooperation -->
  <div style="border: 1px solid #cbd5e1; border-radius: 12px; overflow: hidden; background: #ffffff; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
  <div style="background: linear-gradient(135deg, #10b981 0%, #047857 100%); padding: 12px 16px; color: white; font-weight: 700; font-size: 14px; display: flex; align-items: center; gap: 8px;">
  <span>🧪</span> 1.2 Hardware Cooperation &amp; Joint Collaboration
  </div>
  <div style="padding: 16px; font-size: 13px; color: #334155; line-height: 1.6;">
  This project continues the Qwopus collaboration path with engineer <b>Kyle Hessling</b>, whose hardware support and evaluation feedback helped make the local model testing workflow practical and reproducible.
  <div style="margin-top: 10px; display: flex; align-items: center; gap: 6px;">
  <span>👉</span>
  <span>Follow hardware and model training updates on X / Twitter: <a href="https://x.com/KyleHessling1" target="_blank" style="color: #047857; text-decoration: none; font-weight: 700;">@KyleHessling1</a></span>
  </div>
  </div>
  </div>

  <!-- Card 1.3: Fine-Tuning Framework (Unsloth) -->
  <div style="border: 1px solid #cbd5e1; border-radius: 12px; overflow: hidden; background: #ffffff; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
  <div style="background: linear-gradient(135deg, #7c3aed 0%, #6d28d9 100%); padding: 12px 16px; color: white; font-weight: 700; font-size: 14px; display: flex; align-items: center; gap: 8px;">
  <span>🦥</span> 1.3 Fine-Tuning Framework (Unsloth)
  </div>
  <div style="padding: 16px; font-size: 13px; color: #334155; line-height: 1.6;">
  Training and adaptation use the Qwopus SFT workflow with <b>Unsloth</b> acceleration where applicable, focusing on efficient supervised fine-tuning, stable LoRA-style adaptation, and clean model-card reproducibility.
  <div style="margin-top: 10px; display: flex; align-items: center; gap: 6px;">
  <span>👉</span>
  <span>Unsloth documentation: <a href="https://unsloth.ai/docs" target="_blank" style="color: #7c3aed; text-decoration: none; font-weight: 700;">unsloth.ai/docs</a></span>
  </div>
  </div>
  </div>
</div>

> [!WARNING]
> **Community Release Notice**: Qwopus3.5-4B-Coder is an experimental community release intended for research, local coding experiments, and agent workflow exploration. It has not undergone full safety evaluation or broad general-domain benchmarking.

---

## 📖 2. Background and Motivation

<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; display: flex; flex-direction: column; gap: 20px; margin-bottom: 30px;">
  <!-- Card 2.1: Why a 4B Coder Model? -->
  <div style="border: 1px solid #cbd5e1; border-radius: 12px; overflow: hidden; background: #ffffff; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
  <div style="background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%); padding: 12px 16px; color: white; font-weight: 700; font-size: 14px; display: flex; align-items: center; gap: 8px;">
  <span>⚠️</span> 2.1 Why a 4B Coder Model?
  </div>
  <div style="padding: 16px; font-size: 13px; color: #334155; line-height: 1.6;">
  A 4B-class model is small enough to run locally with practical latency, but large enough to benefit from structured reasoning and agent trace training. The goal of this release is not to maximize raw benchmark size, but to create a compact coding assistant that remains stable under debugging, instruction-following, and tool-use pressure.
  </div>
  </div>

  <!-- Card 2.2: Trace Inversion and Agent Behavior -->
  <div style="border: 1px solid #cbd5e1; border-radius: 12px; overflow: hidden; background: #ffffff; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
  <div style="background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); padding: 12px 16px; color: white; font-weight: 700; font-size: 14px; display: flex; align-items: center; gap: 8px;">
  <span>🧬</span> 2.2 Trace Inversion and Agent Behavior
  </div>
  <div style="padding: 16px; font-size: 13px; color: #334155; line-height: 1.6;">
  Commercial and frontier models often expose only compressed reasoning summaries. Qwopus-style training uses <b>Trace Inversion</b> to reconstruct these compressed "reasoning bubbles" into fuller learnable reasoning traces. For coding, this is paired with agent trajectories that include tool definitions, tool calls, and real feedback, teaching the model to reason through interactive work rather than only produce static answers.
  </div>
  </div>
</div>

---

## 📊 3. benchlocal Evaluation and Baseline Comparison

<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid #cbd5e1; border-radius: 16px; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.05); overflow: hidden; background: #ffffff; margin-bottom: 30px;">
  <div style="background: linear-gradient(135deg, #7c3aed 0%, #4f46e5 100%); padding: 20px; color: white;">
  <h3 style="margin: 0; font-size: 20px; font-weight: 700; display: flex; align-items: center; gap: 8px; color: white; border: none;">📊 benchlocal Agent &amp; Coding Benchmark</h3>
  <p style="margin: 4px 0 0 0; font-size: 13px; color: #ddd6fe;">Local MTP comparison across official Qwen, Claude-Opus reasoning distill, and 9B reference rows for debugging, agent workflow, tool routing, and instruction following.</p>
  </div>

  <div style="padding: 24px; display: flex; flex-direction: column; gap: 24px;">
  <!-- Key Stats Grid -->
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px;">
  <div style="border: 1px solid #e2e8f0; padding: 16px; border-radius: 10px; background: #f8fafc; text-align: center; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);">
  <span style="font-size: 11px; font-weight: 700; color: #7c3aed; text-transform: uppercase; display: block; margin-bottom: 6px; letter-spacing: 0.5px;">🏆 Suite Average</span>
  <span style="font-size: 24px; font-weight: 800; color: #1e293b; display: block;">82.0%</span>
  <span style="font-size: 11px; color: #64748b; font-weight: 500;">vs. 74.0% baseline (+8.0 pp)</span>
  </div>
  <div style="border: 1px solid #e2e8f0; padding: 16px; border-radius: 10px; background: #f8fafc; text-align: center; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);">
  <span style="font-size: 11px; font-weight: 700; color: #7c3aed; text-transform: uppercase; display: block; margin-bottom: 6px; letter-spacing: 0.5px;">🐛 BugFind-15</span>
  <span style="font-size: 24px; font-weight: 800; color: #1e293b; display: block;">71 / 100</span>
  <span style="font-size: 11px; color: #64748b; font-weight: 500;">+19 Delta over baseline</span>
  </div>
  <div style="border: 1px solid #e2e8f0; padding: 16px; border-radius: 10px; background: #f8fafc; text-align: center; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);">
  <span style="font-size: 11px; font-weight: 700; color: #7c3aed; text-transform: uppercase; display: block; margin-bottom: 6px; letter-spacing: 0.5px;">🧠 HermesAgent-20</span>
  <span style="font-size: 24px; font-weight: 800; color: #1e293b; display: block;">64 / 100</span>
  <span style="font-size: 11px; color: #64748b; font-weight: 500;">+3 Delta over baseline</span>
  </div>
  <div style="border: 1px solid #e2e8f0; padding: 16px; border-radius: 10px; background: #f8fafc; text-align: center; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);">
  <span style="font-size: 11px; font-weight: 700; color: #7c3aed; text-transform: uppercase; display: block; margin-bottom: 6px; letter-spacing: 0.5px;">🛠️ ToolCall-15</span>
  <span style="font-size: 24px; font-weight: 800; color: #1e293b; display: block;">100 / 100</span>
  <span style="font-size: 11px; color: #64748b; font-weight: 500;">Perfect tool routing</span>
  </div>
  </div>

  <!-- Test Configuration Note -->
  <div style="background: #f0f9ff; border-left: 4px solid #0284c7; border-radius: 0 8px 8px 0; padding: 12px 16px; font-size: 13px; color: #0f172a; line-height: 1.6;">
  <b>Test configuration:</b> Models were evaluated through <a href="https://github.com/stevibe/benchlocal" target="_blank" style="color: #0369a1; text-decoration: none; font-weight: 700;">benchlocal</a> using LM Studio on the same local Apple Silicon / MLX / GGUF-style setup as the 9B Coder evaluation. Tested 4B models: <b>Qwopus3.5-4B-Coder-MTP</b>, <b>Qwen3.5-4B-MTP</b>, and <b>Similar Public 4B Claude-Distilled Variant</b>. MTP was set to <code>n=2</code> for the MTP rows, sampling used <code>temperature=1.0</code> and <code>top_p=0.95</code>. Each scenario allowed up to <b>three answer attempts per model</b>; a scenario was counted as correct if any attempt passed. Deep-blue rows mark <a href="https://huggingface.co/Jackrong/Qwopus3.5-9B-Coder-GGUF" target="_blank" style="color: #0369a1; text-decoration: none; font-weight: 700;">Qwopus3.5-9B-Coder-GGUF</a> reference scores. Other 9B comparison models use neutral rows, and the official <b>Qwen/Qwen3.5-9B</b> baseline is kept on a white background.
  </div>

  <!-- Table 3.1 BugFind-15 -->
  <div style="border: 1px solid #cbd5e1; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
  <div style="background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); padding: 12px 16px; border-bottom: 1px solid #cbd5e1; font-weight: 700; font-size: 14px; color: #1e293b; display: flex; align-items: center; gap: 8px;">
  <span>🐛</span> 3.1 BugFind-15: Code Debugging and Bug Localization
  </div>
  <div style="padding: 16px;">
  <div style="overflow-x: auto;">
  <table style="width: 100%; border-collapse: collapse; font-size: 13px; min-width: 900px;">
  <thead>
  <tr style="background: rgba(124, 58, 237, 0.05);">
  <th style="padding: 8px 10px; border-bottom: 2px solid #7c3aed; text-align: left; color: #7c3aed; font-weight: bold; width: 25%;">Model</th>
  <th style="padding: 8px 10px; border-bottom: 2px solid #7c3aed; text-align: center; color: #7c3aed; font-weight: bold; width: 10%;">Score</th>
  <th style="padding: 8px 10px; border-bottom: 2px solid #7c3aed; text-align: center; color: #7c3aed; font-weight: bold; width: 10%;">Delta</th>
  <th style="padding: 8px 10px; border-bottom: 2px solid #7c3aed; text-align: left; color: #7c3aed; font-weight: bold; width: 35%;">Dimension Scores</th>
  <th style="padding: 8px 10px; border-bottom: 2px solid #7c3aed; text-align: left; color: #7c3aed; font-weight: bold; width: 20%;">Readout</th>
  </tr>
  </thead>
  <tbody>
  <tr style="background: rgba(16, 185, 129, 0.06);">
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: 700; color: #047857;">Qwopus3.5-4B-Coder-MTP</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center; font-weight: 700; color: #047857;">71</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center; font-weight: 700; color: #10b981;">+19</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">A: 53 / B: 67 / C: 73 / D: 77 / E: 83</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">Clear debugging lead.</td>
  </tr>
  <tr>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: 500;">Qwen3.5-4B-MTP</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center;">52</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center; color: #64748b;">baseline</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">A: 43 / B: 53 / C: 67 / D: 32 / E: 60</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">Lower consistency on bug-fix scenarios.</td>
  </tr>
  <tr>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: 500;">Similar Public 4B Claude-Distilled Variant</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center;">45</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center; color: #b91c1c;">-26</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">A: 36 / B: 40 / C: 53 / D: 32 / E: 67</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">Lower debugging consistency in this run.</td>
  </tr>
  <tr style="background: #dbeafe; color: #1e40af;">
  <td style="padding: 8px 10px; border-bottom: 1px solid #93c5fd; font-weight: 700;">Qwopus3.5-9B-Coder-GGUF</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid #93c5fd; text-align: center; font-weight: 700;">79</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid #93c5fd; text-align: center; font-weight: 700;">9B reference</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid #93c5fd;">A: 67 / B: 87 / C: 100 / D: 77 / E: 43</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid #93c5fd;">Leading 9B-class row in this pack.</td>
  </tr>
  <tr>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: 500;">Qwen3.5-9B-DeepSeek-V4-Flash</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center;">75</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center; color: #64748b;">9B comparison</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">A: 67 / B: 100 / C: 67 / D: 57 / E: 80</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">Public comparison row from 9B card.</td>
  </tr>
  <tr>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: 500;">Other Public 9B Agent Model</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center;">58</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center; color: #64748b;">9B comparison</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">A: 29 / B: 87 / C: 73 / D: 20 / E: 67</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">Public comparison row from 9B card.</td>
  </tr>
  </tbody>
  </table>
  </div>
  </div>
  </div>

  <!-- Table 3.2 HermesAgent-20 -->
  <div style="border: 1px solid #cbd5e1; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
  <div style="background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); padding: 12px 16px; border-bottom: 1px solid #cbd5e1; font-weight: 700; font-size: 14px; color: #1e293b; display: flex; align-items: center; gap: 8px;">
  <span>🧠</span> 3.2 HermesAgent-20: Memory, Workspace Orchestration, and Agent Workflow
  </div>
  <div style="padding: 16px;">
  <div style="overflow-x: auto;">
  <table style="width: 100%; border-collapse: collapse; font-size: 13px; min-width: 900px;">
  <thead>
  <tr style="background: rgba(124, 58, 237, 0.05);">
  <th style="padding: 8px 10px; border-bottom: 2px solid #7c3aed; text-align: left; color: #7c3aed; font-weight: bold; width: 20%;">Model</th>
  <th style="padding: 8px 10px; border-bottom: 2px solid #7c3aed; text-align: center; color: #7c3aed; font-weight: bold; width: 8%;">Score</th>
  <th style="padding: 8px 10px; border-bottom: 2px solid #7c3aed; text-align: center; color: #7c3aed; font-weight: bold; width: 12%;">Delta</th>
  <th style="padding: 8px 10px; border-bottom: 2px solid #7c3aed; text-align: left; color: #7c3aed; font-weight: bold; width: 45%;">Visible Dimension Scores</th>
  <th style="padding: 8px 10px; border-bottom: 2px solid #7c3aed; text-align: left; color: #7c3aed; font-weight: bold; width: 15%;">Readout</th>
  </tr>
  </thead>
  <tbody>
  <tr style="background: rgba(16, 185, 129, 0.06);">
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: 700; color: #047857;">Qwopus3.5-4B-Coder-MTP</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center; font-weight: 700; color: #047857;">64</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center; font-weight: 700; color: #10b981;">+3</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">memory_recall 71 / workspace_orchestration 70 / skills_procedural_memory 50 / scheduling_delivery 75</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">Better memory and workspace behavior.</td>
  </tr>
  <tr>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: 500;">Qwen3.5-4B-MTP</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center;">61</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center; color: #64748b;">baseline</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">memory_recall 41 / workspace_orchestration 45 / skills_procedural_memory 100 / scheduling_delivery 68</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">Stronger visible procedural-memory slice.</td>
  </tr>
  <tr>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: 500;">Similar Public 4B Claude-Distilled Variant</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center;">57</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center; color: #b91c1c;">-7</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">memory_recall 69 / workspace_orchestration 41 / skills_procedural_memory 55 / scheduling_delivery 70 / delegation_recovery_boundaries 51</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">Competitive memory recall, lower workspace orchestration.</td>
  </tr>
  <tr style="background: #dbeafe; color: #1e40af;">
  <td style="padding: 8px 10px; border-bottom: 1px solid #93c5fd; font-weight: 700;">Qwopus3.5-9B-Coder-GGUF</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid #93c5fd; text-align: center; font-weight: 700;">85</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid #93c5fd; text-align: center; font-weight: 700;">9B reference</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid #93c5fd;">84 / 93 / 88 / 75 / 84</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid #93c5fd;">Leading 9B-class row in this pack.</td>
  </tr>
  <tr>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: 500;">Qwen/Qwen3.5-9B</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center;">71</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center; color: #64748b;">official 9B baseline</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">75 / 58 / 100 / 53 / 69</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">Official Qwen reference row.</td>
  </tr>
  <tr>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: 500;">Other Public 9B Agent Model</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center;">68</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center; color: #64748b;">9B comparison</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">71 / 83 / 43 / 61 / 80</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">Public comparison row from 9B card.</td>
  </tr>
  <tr>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: 500;">DJLougen/Harmonic-Hermes-9B</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center;">47</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center; color: #64748b;">9B comparison</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">60 / 45 / 23 / 69 / 38</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">Public comparison row from 9B card.</td>
  </tr>
  </tbody>
  </table>
  </div>
  </div>
  </div>

  <!-- Table 3.3 ToolCall-15 -->
  <div style="border: 1px solid #cbd5e1; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
  <div style="background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); padding: 12px 16px; border-bottom: 1px solid #cbd5e1; font-weight: 700; font-size: 14px; color: #1e293b; display: flex; align-items: center; gap: 8px;">
  <span>🛠️</span> 3.3 ToolCall-15: Tool Routing Stability
  </div>
  <div style="padding: 16px;">
  <div style="overflow-x: auto;">
  <table style="width: 100%; border-collapse: collapse; font-size: 13px; min-width: 900px;">
  <thead>
  <tr style="background: rgba(124, 58, 237, 0.05);">
  <th style="padding: 8px 10px; border-bottom: 2px solid #7c3aed; text-align: left; color: #7c3aed; font-weight: bold; width: 25%;">Model</th>
  <th style="padding: 8px 10px; border-bottom: 2px solid #7c3aed; text-align: center; color: #7c3aed; font-weight: bold; width: 10%;">Score</th>
  <th style="padding: 8px 10px; border-bottom: 2px solid #7c3aed; text-align: center; color: #7c3aed; font-weight: bold; width: 10%;">Delta</th>
  <th style="padding: 8px 10px; border-bottom: 2px solid #7c3aed; text-align: left; color: #7c3aed; font-weight: bold; width: 35%;">Dimension Scores</th>
  <th style="padding: 8px 10px; border-bottom: 2px solid #7c3aed; text-align: left; color: #7c3aed; font-weight: bold; width: 20%;">Readout</th>
  </tr>
  </thead>
  <tbody>
  <tr style="background: rgba(16, 185, 129, 0.06);">
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: 700; color: #047857;">Qwopus3.5-4B-Coder-MTP</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center; font-weight: 700; color: #047857;">100</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center; font-weight: 700; color: #10b981;">+10</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">A: 100 / B: 100 / C: 100 / D: 100 / E: 100</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">Perfect tool-routing run.</td>
  </tr>
  <tr>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: 500;">Qwen3.5-4B-MTP</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center;">90</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center; color: #64748b;">baseline</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">A: 100 / B: 100 / C: 100 / D: 83 / E: 67</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">Minor failures in later categories.</td>
  </tr>
  <tr>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: 500;">Similar Public 4B Claude-Distilled Variant</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center;">77</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center; color: #b91c1c;">-23</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">A: 100 / B: 33 / C: 67 / D: 83 / E: 100</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">Strong A/E categories, weaker B/C tool-routing slices.</td>
  </tr>
  <tr style="background: #dbeafe; color: #1e40af;">
  <td style="padding: 8px 10px; border-bottom: 1px solid #93c5fd; font-weight: 700;">Qwopus3.5-9B-Coder-GGUF</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid #93c5fd; text-align: center; font-weight: 700;">100</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid #93c5fd; text-align: center; font-weight: 700;">9B reference</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid #93c5fd;">A: 100 / B: 100 / C: 100 / D: 100 / E: 100</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid #93c5fd;">Matches the leading tool-call score.</td>
  </tr>
  <tr>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: 500;">Qwen/Qwen3.5-9B</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center;">100</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center; color: #64748b;">official 9B baseline</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">A: 100 / B: 100 / C: 100 / D: 100 / E: 100</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">Official Qwen reference row.</td>
  </tr>
  <tr>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: 500;">Other Public 9B Agent Model</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center;">93</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center; color: #64748b;">9B comparison</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">A: 100 / B: 100 / C: 100 / D: 67 / E: 100</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">Public comparison row from 9B card.</td>
  </tr>
  </tbody>
  </table>
  </div>
  </div>
  </div>

  <!-- Table 3.4 InstructFollow-15 -->
  <div style="border: 1px solid #cbd5e1; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
  <div style="background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); padding: 12px 16px; border-bottom: 1px solid #cbd5e1; font-weight: 700; font-size: 14px; color: #1e293b; display: flex; align-items: center; gap: 8px;">
  <span>📄</span> 3.4 InstructFollow-15: Formatting and Constraint Following
  </div>
  <div style="padding: 16px;">
  <div style="overflow-x: auto;">
  <table style="width: 100%; border-collapse: collapse; font-size: 13px; min-width: 900px;">
  <thead>
  <tr style="background: rgba(124, 58, 237, 0.05);">
  <th style="padding: 8px 10px; border-bottom: 2px solid #7c3aed; text-align: left; color: #7c3aed; font-weight: bold; width: 25%;">Model</th>
  <th style="padding: 8px 10px; border-bottom: 2px solid #7c3aed; text-align: center; color: #7c3aed; font-weight: bold; width: 10%;">Score</th>
  <th style="padding: 8px 10px; border-bottom: 2px solid #7c3aed; text-align: center; color: #7c3aed; font-weight: bold; width: 10%;">Delta</th>
  <th style="padding: 8px 10px; border-bottom: 2px solid #7c3aed; text-align: left; color: #7c3aed; font-weight: bold; width: 35%;">Dimension Scores</th>
  <th style="padding: 8px 10px; border-bottom: 2px solid #7c3aed; text-align: left; color: #7c3aed; font-weight: bold; width: 20%;">Readout</th>
  </tr>
  </thead>
  <tbody>
  <tr style="background: rgba(16, 185, 129, 0.06);">
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: 700; color: #047857;">Qwopus3.5-4B-Coder-MTP</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center; font-weight: 700; color: #047857;">93</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center; font-weight: 700; color: #10b981;">0</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">A: 100 / B: 100 / C: 100 / D: 65 / E: 100</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); color: #047857; font-weight: 700;">Tie</td>
  </tr>
  <tr>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: 500;">Qwen3.5-4B-MTP</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center;">93</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center; color: #64748b;">0</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">A: 100 / B: 100 / C: 100 / D: 65 / E: 100</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); color: #64748b;">Tie</td>
  </tr>
  <tr>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: 500;">Similar Public 4B Claude-Distilled Variant</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center;">60</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); text-align: center; color: #b91c1c;">-33</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15);">A: 65 / B: 35 / C: 100 / D: 60 / E: 39</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid rgba(128,128,128,0.15); color: #b91c1c; font-weight: 700;">Lower constraint-following reliability in this run.</td>
  </tr>
  <tr style="background: #dbeafe; color: #1e40af;">
  <td style="padding: 8px 10px; border-bottom: 1px solid #93c5fd; font-weight: 700;">Qwopus3.5-9B-Coder-GGUF</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid #93c5fd; text-align: center; font-weight: 700;">93</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid #93c5fd; text-align: center; font-weight: 700;">9B reference</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid #93c5fd;">A: 100 / B: 100 / C: 100 / D: 67 / E: 100</td>
  <td style="padding: 8px 10px; border-bottom: 1px solid #93c5fd;">Reported 9B Coder reference score.</td>
  </tr>
  </tbody>
  </table>
  </div>
  </div>
  </div>

  <!-- Test Screenshots & Hardware Support Notice -->
  <div style="background: #f5f3ff; border-left: 5px solid #7c3aed; padding: 16px; border-radius: 0 8px 8px 0;">
  <p style="margin: 0; font-size: 13px; color: #334155; line-height: 1.6;">
  🍎 All screenshots of the test interfaces have been uploaded to the image folder in the repository. Click the link below to view and verify:<br>
  🔗 <a href="https://huggingface.co/Jackrong/Qwopus3.5-4B-Coder/tree/main/test_results" target="_blank" style="color: #7c3aed; font-weight: 700; text-decoration: none;">View Test Screenshots</a>
  </p>
  <p style="margin: 8px 0 0 0; font-size: 13px; color: #334155; line-height: 1.6;">
  ❤️ Kyle Hessling for his generous hardware and equipment support. You can follow him for more updates on X / Twitter: <a href="https://x.com/KyleHessling1" target="_blank" style="color: #7c3aed; font-weight: 700; text-decoration: none;">@KyleHessling1</a>.
  </p>
  </div>

  </div>
</div>

---

## 🗺️ 4. Training & Data Pipeline Overview

The training process fuses **Trace Inversion** data augmentation with a **Three-Stage Curriculum Learning** pipeline. The core engineering focuses on expanding context length gradually while training on reconstructed reasoning traces and real agent trajectories to keep the output format stable.

```text
       [ 🗺️ Trace Inversion: Reconstructing Distillation Workflow ]

  A. Surrogate Model Training (Trace Inverter)
     Open-source Model (GLM-5.1 / DS-V4) ──► Complete Reasoning Chain ──► [ Qwen3-235B Compression ] ──► Reasoning Bubbles
                                              │                                   │
                                              └──────────► [ Training ] ◄─────────┘
                                                   (Base: Qwen3-4B-Instruct)
                                                   (Result: Trace-Inverter-4B)

  B. Inversion Phase: Reconstructing Claude-4.7-Max
     _______________________________________________________
    |                                                       |
    |  Claude-4.7-Max API ──► Compressed Bubbles + Answer   |
    |_______________________________________________________|
                      │
                      ▼
    [ 🧠 Trace-Inverter-4B (Logic Reconstructor) ] ──► Synthetic Deep Reasoning Trace (Learnable CoT)
                      │
                      ▼
    [ 🧩 Data Splicing ] ◄────────── (Original Prompt + Response)
    (Embed reconstructed CoT in <think> tags, splicing with original prompt/response)
                      │
                      ▼
             (Result: claude-opus-4.6/4.7 inverted sets)

  C. Final Coder SFT Curriculum Pipeline
     ___________________________________________
    |                                           |
    |       Base Model (Qwen3.5-4B family)      |
    |___________________________________________|
                      │
                      ▼
    [ 📦 Phase 1: Format Inception ] ──► [ 🛠️ Phase 2: Agent/Coding Expansion ] ──► [ 🚀 Phase 3: Long-Context SFT ]
      ( < 4096 tokens )                     ( 4096 - 8192 tokens )                     ( 8192 - 32K tokens )
      (Stable <think> format)               (Tool traces + coding tasks)               (Long / multi-turn / replay)
                      │                                                                            │
                      └─────────────────────────────┬──────────────────────────────────────────────┘
                                                    ▼
                                   ________________________________________
                                  |                                        |
                                  |   🌟 Final Model: Qwopus3.5-4B-Coder   |
                                  |________________________________________|
```

---

## 🎯 5. Three-Stage Curriculum Learning

To steadily scale reasoning quality under local and long-context inference, **Qwopus3.5-4B-Coder** uses a curriculum-style data mixture. The model is first stabilized on short, clean reasoning samples, then exposed to complex coding and agent traces, and finally reinforced with longer contexts plus replay data. This section also describes the fine-tuning context-length distribution; runtime long-context extension guidance is covered in Section 6.

<table style="width: 100%; border-collapse: collapse; margin-top: 15px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <thead>
    <tr style="background: rgba(124, 58, 237, 0.05);">
      <th style="padding: 10px; border-bottom: 2px solid #7c3aed; text-align: left; color: #7c3aed; font-size: 14px; width: 25%;">Curriculum Stage</th>
      <th style="padding: 10px; border-bottom: 2px solid #7c3aed; text-align: left; font-size: 14px; width: 35%;">Focus &amp; Sample Characteristics</th>
      <th style="padding: 10px; border-bottom: 2px solid #7c3aed; text-align: left; font-size: 14px;">Strategy Details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: bold; font-size: 13px; color: #7c3aed;">📦 Stage 1: Format Inception</td>
      <td style="padding: 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-size: 13px;">• Limit context within 4,096 tokens<br>• Emphasize stable reasoning templates</td>
      <td style="padding: 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-size: 13px;">Focuses on short-to-medium length, cleanly formatted reasoning samples. The primary goal is to establish reliable structured reasoning output, including stable <code>&lt;think&gt;</code> boundaries, before exposing the model to longer chains.</td>
    </tr>
    <tr>
      <td style="padding: 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: bold; font-size: 13px; color: #7c3aed;">🛠️ Stage 2: Complexity Expansion</td>
      <td style="padding: 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-size: 13px;">• Extend length to 4,096 - 8,192 tokens<br>• Introduce higher-difficulty coding and agent samples</td>
      <td style="padding: 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-size: 13px;">Gradually increases the ratio of complex reasoning chains, code debugging tasks, and multi-turn tool traces. The model learns to connect reasoning, action selection, and environment feedback.</td>
    </tr>
    <tr>
      <td style="padding: 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-weight: bold; font-size: 13px; color: #7c3aed;">🚀 Stage 3: Long-Context SFT</td>
      <td style="padding: 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-size: 13px;">• Progressively scale samples up to 32K tokens<br>• Use short-sample replay</td>
      <td style="padding: 10px; border-bottom: 1px solid rgba(128,128,128,0.15); font-size: 13px;">Pushes the model toward long-context and multi-turn reasoning while replaying high-quality short samples to reduce instruction-following drift. The 32K figure describes the fine-tuning sequence/data mixture target, not a hard architectural limit.</td>
    </tr>
  </tbody>
</table>

---

## 📄 6. Context Length and Long-Context Usage

<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid #cbd5e1; border-radius: 12px; overflow: hidden; background: #ffffff; box-shadow: 0 2px 4px rgba(0,0,0,0.02); margin-bottom: 18px;">
  <div style="background: linear-gradient(135deg, #0f766e 0%, #0e7490 100%); padding: 12px 16px; color: white; font-weight: 700; font-size: 14px; display: flex; align-items: center; gap: 8px;">
    <span>📄</span> 6.1 Runtime Context Guidance
  </div>
  <div style="padding: 16px; font-size: 13px; color: #334155; line-height: 1.6;">
    <p style="margin-top: 0;">During fine-tuning, this model was trained with a maximum sequence length of <b>32K tokens</b>. The training data mixture was also constructed around samples up to 32K tokens, so the context-length distribution in this model card reflects the fine-tuning data distribution rather than a hard architectural limit.</p>
    <p>The model still inherits the native long-context capability of the Qwen3.5-family base model. Longer context windows such as <b>128K</b> or <b>256K</b> may be available in compatible inference runtimes, depending on backend support and configuration.</p>
    <p>For practical long-context inference beyond 32K, especially when using <code>llama.cpp</code> / GGUF, it is recommended to enable <b>RoPE/YaRN scaling</b> instead of only increasing <code>n_ctx</code> or <code>--ctx-size</code>. Directly setting a larger context window without RoPE scaling may work in some setups, but it can be less stable and may not deliver the expected long-context behavior.</p>
    <p>This follows Qwen community guidance for GGUF long-context usage. In a Qwen GGUF discussion, a Qwen maintainer noted that <b>"128K context length needs YaRN"</b> and later clarified that supported scaling should be explicitly enabled rather than assumed to be on by default. Reference: <a href="https://huggingface.co/Qwen/Qwen2.5-72B-Instruct-GGUF/discussions/2" target="_blank" style="color: #0f766e; text-decoration: none; font-weight: 700;">Qwen/Qwen2.5-72B-Instruct-GGUF discussion #2</a>.</p>
  </div>
</div>

Community feedback also suggests that RoPE/YaRN scaling can improve long-context stability for this model family. One user reported that, on HermesAgent-20, **Qwopus3.6-35B-A3B-v1** performed better when extending from 32K to 128K via RoPE scaling than when directly setting a 128K context window without scaling, with scores of **83 vs. 72** in their setup. This result may vary depending on backend, quantization type, KV cache settings, hardware, and benchmark configuration, but it is consistent with the recommendation to use RoPE/YaRN scaling for contexts beyond 32K.

Example `llama.cpp` configuration for extending from 32K to 128K:

```bash
./llama-server \
  -m model.gguf \
  --ctx-size 131072 \
  --rope-scaling yarn \
  --rope-scale 4 \
  --yarn-orig-ctx 32768
```

For 256K context, users may need to adjust the scaling factor and validate the result in their own workload:

```bash
./llama-server \
  -m model.gguf \
  --ctx-size 262144 \
  --rope-scaling yarn \
  --rope-scale 8 \
  --yarn-orig-ctx 32768
```

Please note that long-context behavior may vary depending on inference backend, quantization type, KV cache settings, available memory, and task type. For best results, benchmark the target workload when using contexts beyond 32K.

---

## 🎯 7. Recommended Use Cases and Limitations

<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; margin-bottom: 30px;">
  <!-- Card 7.1: Good Fits -->
  <div style="border: 1px solid #cbd5e1; border-radius: 12px; overflow: hidden; background: #ffffff; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
  <div style="background: linear-gradient(135deg, #10b981 0%, #047857 100%); padding: 12px 16px; color: white; font-weight: 700; font-size: 14px; display: flex; align-items: center; gap: 8px;">
  <span>✅</span> Good Fits
  </div>
  <div style="padding: 16px; font-size: 13px; color: #334155; line-height: 1.6;">
  Code debugging, small repository tasks, tool-call routing, local coding agents, structured instruction following, development workflow assistants, and reasoning traces where concise local latency matters.
  </div>
  </div>
  <!-- Card 7.2: Known Limits -->
  <div style="border: 1px solid #cbd5e1; border-radius: 12px; overflow: hidden; background: #ffffff; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
  <div style="background: linear-gradient(135deg, #dc2626 0%, #991b1b 100%); padding: 12px 16px; color: white; font-weight: 700; font-size: 14px; display: flex; align-items: center; gap: 8px;">
  <span>❌</span> Known Limits
  </div>
  <div style="padding: 16px; font-size: 13px; color: #334155; line-height: 1.6;">
  As a compact model, it can still miss broad world knowledge, complex repository-wide dependencies, or highly specialized domain requirements. Tool-call behavior depends strongly on prompt format and tool schema consistency.
  </div>
  </div>
</div>

> [!CAUTION]
> **Deployment note**: The model may emit reasoning inside <code>&lt;think&gt;</code> and <code>&lt;/think&gt;</code> tags. Front-end applications and agent frameworks should parse or hide these sections where appropriate.

---

## 📚 8. Resources & Guides

👉 **[GitHub Repository: Jackrong-llm-finetuning-guide](https://github.com/R6410418/Jackrong-llm-finetuning-guide.git)**
Access the repository to dive into the codebase and reproduce our results locally or on Google Colab.

👉 **[Qwen MTP GGUF Processing Workflow](https://github.com/R6410418/Jackrong-llm-finetuning-guide/tree/main/qwen-mtp-gguf)**
A custom splitting and merging methodology designed specifically for Qwen series Multi-Token Prediction (MTP) heads.

👉 **[benchlocal Evaluation Framework](https://github.com/stevibe/benchlocal)**
The evaluation framework used to run the local agentic and coding benchmarks.

---

## 🙏 9. Acknowledgements

Special thanks to:
- The Qwen team for providing the powerful Qwen3.5 base model.
- Unsloth for providing the highly efficient fine-tuning framework.
- Open-source datasets and community contributors.
- **Kyle Hessling** for the close collaboration on hardware and evaluation support.

---

## 📖 10. Citation

```bibtex
@misc{jackrong_qwopus35_4b_coder,
  title        = {Qwopus3.5-4B-Coder},
  author       = {Jackrong},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/Jackrong/Qwopus3.5-4B-Coder}}
}
```
