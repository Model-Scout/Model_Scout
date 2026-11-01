---
thumbnail: https://huggingface.co/PocketDoc/Dans-PersonalityEngine-V1.3.0-24b/resolve/main/resources/pe.png
license: apache-2.0
tags:
- general-purpose
- roleplay
- storywriting
- chemistry
- biology
- code
- climate
- axolotl
- text-generation-inference
- finetune
- legal
- medical
- finance
- llama-cpp
- gguf-my-repo
datasets:
- PocketDoc/Dans-Prosemaxx-RP
- PocketDoc/Dans-Personamaxx-Logs-2
- PocketDoc/Dans-Personamaxx-VN
- PocketDoc/Dans-Kinomaxx-VanillaBackrooms
- PocketDoc/Dans-Prosemaxx-Gutenberg
- PocketDoc/Dans-Prosemaxx-Cowriter-3-XL
- PocketDoc/Dans-Prosemaxx-Adventure
- PocketDoc/Dans-Failuremaxx-Adventure-3
- PocketDoc/Dans-Prosemaxx-InstructWriter-ZeroShot-2
- PocketDoc/Dans-Prosemaxx-InstructWriter-ZeroShot-3
- PocketDoc/Dans-Prosemaxx-InstructWriter-Continue-2
- PocketDoc/Dans-Prosemaxx-Instructwriter-Long
- PocketDoc/Dans-Prosemaxx-RepRemover-1
- PocketDoc/Dans-MemoryCore-CoreCurriculum-Small
- AquaV/US-Army-Survival-Sharegpt
- AquaV/Multi-Environment-Operations-Sharegpt
- AquaV/Resistance-Sharegpt
- AquaV/Interrogation-Sharegpt
- AquaV/Chemical-Biological-Safety-Applications-Sharegpt
- AquaV/Energetic-Materials-Sharegpt
- PocketDoc/Dans-Mathmaxx
- PJMixers/Math-Multiturn-1K-ShareGPT
- PocketDoc/Dans-Taskmaxx
- PocketDoc/Dans-Taskmaxx-DataPrepper
- PocketDoc/Dans-Taskmaxx-ConcurrentQA-Reworked
- PocketDoc/Dans-Taskmaxx-TableGPT
- PocketDoc/Dans-Taskmaxx-SciRIFF
- PocketDoc/Dans-Taskmaxx-Edit
- PocketDoc/Dans-Toolmaxx-Agent
- PocketDoc/Dans-Toolmaxx-ShellCommands
- PocketDoc/Dans-Toolmaxx-Functions-Toolbench
- PocketDoc/Dans-Toolmaxx-Functions-ToolACE
- PocketDoc/Dans-Toolmaxx-Functions-apigen-subset
- PocketDoc/Dans-Assistantmaxx-OpenAssistant2
- PocketDoc/Dans-Assistantmaxx-Opus-Merge-2
- PocketDoc/Dans-Assistantmaxx-sonnetorca-subset
- PocketDoc/Dans-Assistantmaxx-sonnetorca-subset-2
- PocketDoc/Dans-Assistantmaxx-Synthia
- PocketDoc/Dans-Assistantmaxx-ASL
- PocketDoc/Dans-Assistantmaxx-PersonaLLM-Opus
- PocketDoc/Dans-Assistantmaxx-LongAlign
- PocketDoc/Dans-Assistantmaxx-OpenLeecher-Instruct
- PocketDoc/Dans-Assistantmaxx-Tulu3-IF
- PocketDoc/Dans-Systemmaxx
- PocketDoc/Dans-Logicmaxx-SAT-AP
- PJMixers/grimulkan_theory-of-mind-ShareGPT
- PJMixers/grimulkan_physical-reasoning-ShareGPT
- PocketDoc/Dans-Reasoningmaxx-NaturalReasoning
- PocketDoc/Dans-Reasoningmaxx-WebInstruct
- PocketDoc/Dans-Reasoningmaxx-GeneralReasoning
- PocketDoc/Dans-Assistantmaxx-ClosedInstruct
language:
- en
- ar
- de
- fr
- es
- hi
- pt
- ja
- ko
base_model: PocketDoc/Dans-PersonalityEngine-V1.3.0-24b
pipeline_tag: text-generation
library_name: transformers
---

# King-Cane/Dans-PersonalityEngine-V1.3.0-24b-Q4_K_M-GGUF
This model was converted to GGUF format from [`PocketDoc/Dans-PersonalityEngine-V1.3.0-24b`](https://huggingface.co/PocketDoc/Dans-PersonalityEngine-V1.3.0-24b) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/PocketDoc/Dans-PersonalityEngine-V1.3.0-24b) for more details on the model.
---
<!doctype html>
<html lang="en">
    <head>
        <title>Dans-PersonalityEngine-V1.3.0-24b</title>
    </head>
                        <div style="text-align: center">
                        <h3>Multilingual Support</h3>
                        <pre class="code-block">
Arabic  Chinese   English  French      German
Hindi   Japanese  Korean   Portuguese  Spanish</pre>
                        <h3>Key Details</h3>
                        <pre class="code-block">
BASE MODEL: mistralai/Mistral-Small-3.1-24B-Base-2503
LICENSE: apache-2.0
LANGUAGE: Multilingual with 10 supported languages
CONTEXT LENGTH: 32768 tokens, 131072 with degraded recall</pre>
                        <h3>Recommended Settings</h3>
                        <pre class="code-block">
TEMPERATURE: 1.0
TOP_P: 0.9</pre>
                        <h3>Prompting Format</h3>
                        <pre class="code-block">
The model uses the following format refered to as
"DanChat-2"</pre>
                    </div>
                </div>
            </div>
        </div>
    </div>
</html>


## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo King-Cane/Dans-PersonalityEngine-V1.3.0-24b-Q4_K_M-GGUF --hf-file dans-personalityengine-v1.3.0-24b-q4_k_m.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo King-Cane/Dans-PersonalityEngine-V1.3.0-24b-Q4_K_M-GGUF --hf-file dans-personalityengine-v1.3.0-24b-q4_k_m.gguf -c 2048
```

Note: You can also use this checkpoint directly through the [usage steps](https://github.com/ggerganov/llama.cpp?tab=readme-ov-file#usage) listed in the Llama.cpp repo as well.

Step 1: Clone llama.cpp from GitHub.
```
git clone https://github.com/ggerganov/llama.cpp
```

Step 2: Move into the llama.cpp folder and build it with `LLAMA_CURL=1` flag along with other hardware-specific flags (for ex: LLAMA_CUDA=1 for Nvidia GPUs on Linux).
```
cd llama.cpp && LLAMA_CURL=1 make
```

Step 3: Run inference through the main binary.
```
./llama-cli --hf-repo King-Cane/Dans-PersonalityEngine-V1.3.0-24b-Q4_K_M-GGUF --hf-file dans-personalityengine-v1.3.0-24b-q4_k_m.gguf -p "The meaning to life and the universe is"
```
or 
```
./llama-server --hf-repo King-Cane/Dans-PersonalityEngine-V1.3.0-24b-Q4_K_M-GGUF --hf-file dans-personalityengine-v1.3.0-24b-q4_k_m.gguf -c 2048
```
