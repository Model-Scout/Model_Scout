---
language: [en, es, pt, de, fr, ar, vi, ko, ru, th, hi, zh, ja, tr]
license: cc-by-sa-4.0
pretty_name: "ScamBench Training Corpus"
size_categories: ["10K<n<100K"]
task_categories: ["text-classification", "text-generation"]
tags: [scam-detection, social-engineering, phishing, prompt-injection, agent-safety, red-teaming, security, fraud-detection, multi-turn-dialogue, reasoning, synthetic, multilingual, benchmark]
configs:
  - config_name: default
    default: true
    data_files:
      - split: train
        path: "data/train/*.parquet"
      - split: test
        path: "data/test/*.parquet"
      - split: validation
        path: "data/validation/*.parquet"
  - config_name: hermes
    data_files:
      - split: train
        path: "formats/hermes-train.jsonl"
      - split: test
        path: "formats/hermes-test.jsonl"
      - split: validation
        path: "formats/hermes-validation.jsonl"
  - config_name: eliza
    data_files:
      - split: train
        path: "formats/eliza-train.jsonl"
      - split: test
        path: "formats/eliza-test.jsonl"
      - split: validation
        path: "formats/eliza-validation.jsonl"
  - config_name: openclaw
    data_files:
      - split: train
        path: "formats/openclaw-train.jsonl"
      - split: test
        path: "formats/openclaw-test.jsonl"
      - split: validation
        path: "formats/openclaw-validation.jsonl"
  - config_name: openai
    data_files:
      - split: train
        path: "formats/openai-train.jsonl"
      - split: test
        path: "formats/openai-test.jsonl"
      - split: validation
        path: "formats/openai-validation.jsonl"
---

# ScamBench Training Corpus

A multilingual, multi-turn training corpus for building scam-resistant autonomous agents.

## Dataset Description

ScamBench is a comprehensive dataset designed to train AI agents to resist social engineering, phishing, prompt injection, credential theft, impersonation, advance-fee fraud, and other adversarial attacks while maintaining helpfulness for legitimate requests.

### Key Features
- **37,423 total records** across 14 languages
- **154 attack categories** including social engineering, prompt injection, credential theft, impersonation, advance-fee fraud, and more
- **Culture-specific scam patterns** for each language (PIX fraud for Brazilian Portuguese, オレオレ詐欺 for Japanese, 보이스피싱 for Korean, etc.)
- **Multi-turn conversations** ranging from 2 to 99 messages
- **Reasoning traces** for 87% of records
- **Balanced attack/legitimate split** (18,757 attack / 18,666 legitimate) to prevent over-refusal
- **Statistical shortcut mitigation** — designed to prevent models from learning superficial patterns

## Usage

```python
from datasets import load_dataset

ds = load_dataset("lalalune/scambench-training")

# Filter by language
japanese = ds["train"].filter(lambda x: x["language"] == "ja")

# Filter attacks only
attacks = ds["train"].filter(lambda x: x["should_trigger_scam_defense"])

# Get records with reasoning traces
reasoned = ds["train"].filter(lambda x: x["reasoning_trace"] is not None)

# Parse messages from JSON string
import json
sample = ds["train"][0]
messages = json.loads(sample["messages"])
for msg in messages:
    print(f"{msg['role']}: {msg['content'][:80]}...")
```

## Dataset Structure

### Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique record identifier |
| `source_dataset` | string | Original HuggingFace dataset or generation pipeline that produced this record |
| `source_pool` | string | One of `base`, `augmented`, or `generated` |
| `scenario_category` | string | Attack type or `legitimate` for benign conversations |
| `decision_class` | string | Agent decision category (e.g. `refuse`, `engage_legitimate`, `audit`, `request_verification`) |
| `should_trigger_scam_defense` | bool | Whether the scenario should activate scam defences |
| `system_prompt` | string | System prompt establishing the agent's context and identity |
| `messages` | string (JSON) | JSON array of message objects with `role`, `speaker`, and `content` fields |
| `chosen_action` | string | The action the agent should take (e.g. `engage`, `refuse`, `audit`, `request-verification`) |
| `response_text` | string | The agent's response text |
| `explanation` | string | Human-readable explanation of why this action was chosen |
| `reasoning_trace` | string or null | Chain-of-thought reasoning trace (XML or free-form) |
| `reasoning_source` | string | Origin of reasoning (e.g. `deep-skeptical`, `xml_trace`, `none`) |
| `language` | string | ISO 639-1 language code |
| `style_variant` | string | Conversation style (e.g. `plain`, `leetspeak`, `business_formal`, `pliny`) |
| `leaked_secret` | bool | Whether the agent leaked a secret in this scenario (should be false for correct behaviour) |
| `unsafe_signals` | string (JSON) | JSON array of detected unsafe signal labels |
| `diagnostic_labels` | string (JSON) | JSON array of diagnostic labels for evaluation |
| `pipeline_version` | string | Version tag of the generation pipeline |

### Splits

| Split | Records |
|-------|---------|
| train | 29,951 |
| validation | 3,736 |
| test | 3,736 |
| **total** | **37,423** |

### Decision Class Distribution

| Decision Class | Count |
|---------------|-------|
| engage_legitimate | 12,407 |
| request_verification | 11,335 |
| refuse | 6,548 |
| audit | 3,002 |
| allow_safe_action | 2,254 |
| escalate | 1,125 |
| execute_transaction | 385 |
| ignore | 97 |
| accept | 70 |
| request-verification | 63 |
| share_safe_info | 39 |
| block_actor | 38 |
| warn_actor | 30 |
| deny_privileged_action | 30 |

### Top Scenario Categories

| Category | Count |
|----------|-------|
| legitimate | 14,075 |
| social-engineering | 11,899 |
| prompt-injection | 3,570 |
| research-assisted | 2,340 |
| phishing-link | 1,168 |
| secret-exfiltration | 756 |
| credential-theft | 290 |
| extended-multi-turn | 260 |
| verbose-context-injection | 200 |
| benign | 200 |
| impersonation | 190 |
| advance-fee-fraud | 120 |
| inter-agent-communication | 100 |
| interpersonal-abuse | 95 |
| malicious-tool | 94 |
| admin-override | 85 |
| hitl-bypass | 80 |
| state-persistence | 80 |
| cascading-failure | 80 |
| persistent-social-engineering | 80 |

### Languages

| Language | Records |
|----------|---------|
| `en` | 20,145 |
| `es` | 3,095 |
| `pt` | 2,581 |
| `de` | 1,780 |
| `fr` | 1,512 |
| `ar` | 987 |
| `vi` | 980 |
| `ko` | 945 |
| `ru` | 928 |
| `th` | 917 |
| `zh` | 903 |
| `hi` | 897 |
| `tr` | 877 |
| `ja` | 876 |

## Source Data

This dataset was built from 76 HuggingFace source datasets and 39 synthetic generation pipelines, augmented with culture-specific scam patterns, multi-turn conversation expansion, and reasoning traces.

### HuggingFace Source Datasets

- `ANASAKHTAR/negotation`
- `AmSpotNot1221/scam-call`
- `Amod/mental_health_counseling_conversations`
- `BothBosu/Scammer-Conversation`
- `BothBosu/multi-agent-scam-conversation`
- `BothBosu/scam-dialogue`
- `BothBosu/single-agent-scam-conversations`
- `BothBosu/youtube-scam-conversations`
- `David-Egea/phishing-texts`
- `FredZhang7/all-scam-spam`
- `IDA-SERICS/Disaster-tweet-jailbreaking`
- `JailbreakBench/JBB-Behaviors`
- `JailbreakV-28K/JailBreakV-28k`
- `LeverCRO/clawback`
- `Linq-AI-Research/FinDER`
- `LuckyLukke/negotio_GRPO`
- `Lyr1k/multi-agent-scam-conversation`
- `MAlmasabi/Indirect-Prompt-Injection-BIPIA-GPT`
- `NikithaVenkat0205/scam-dialogue`
- `OtabekRizayev/scam-data`
- `Rainnighttram/Scam_Detect_20`
- `Rainnighttram/Scam_Detect_Split`
- `Rainnighttram/Scam_detect_50`
- `Salesforce/xlam-function-calling-60k`
- `SparkyPilot/scam-detection-data`
- `ViditOstwal/price-negotiation-datasets`
- `Vuong23/scam_response_for_llama`
- `alissonpadua/ham-spam-scam-toxic-parquet`
- `allenai/wildjailbreak`
- `aurora-m/redteam`
- `awax1122/openclaw-opencode-dataset`
- `bellfire/openclaw-coder-dataset`
- `deepset/prompt-injections`
- `difraud/difraud`
- `donksg/scam_finetune`
- `drorrabin/phishing_emails-data`
- `fadhilr/scam_call_gemma3`
- `gagan3012/AttackQA`
- `hackaprompt/hackaprompt-dataset`
- `haoyaqi/scam_dataset`
- `imoxto/prompt_injection_cleaned_dataset`
- `jkazdan/refusal-attack-llama-2-7b-chat`
- `jugaad-lab/clawguard`
- `kevinchiu37/scam-detection-feedback`
- `kevinchiu37/scam-detection-logs`
- `kugu/Salray_Negotiations`
- `lixi0029/phishing-mail`
- `locuoco/the-biggest-spam-ham-phish-email-dataset-300000`
- `luckychao/Chat-Models-Backdoor-Attacking`
- `lzy337/attack_data_hf`
- `menaattia/phone-scam-dataset`
- `mytestaccforllm/final_scam`
- `necm77/negotiation_data`
- `neuralchemy/Prompt-injection-dataset`
- `nohurry/Opus-4.6-Reasoning-3000x-filtered`
- `pjl914335852-ux/Binance-guardian-ai`
- `r1char9/prompt-2-prompt-injection-v2-dataset`
- `rubend18/ChatGPT-Jailbreak-Prompts`
- `rzeydelis/autotrain-data-discord-scams-detector`
- `sambanovasystems/attackqa`
- `shakeleoatmeal/phone-scam-detection-synthetic`
- `spv21myrtea/Phishing-18K`
- `srushtisingh/Ethical_redteam`
- `sureheremarv/ipi_arena_attacks`
- `talkmap/telecom-conversation-corpus`
- `thananos/augmented-scam-dialogue`
- `thananos/augmented-train-scam-dialogue`
- `tomshe/turing_phishing_detection`
- `truthfulqa/truthful_qa`
- `wangyuancheng/discord-phishing-scam`
- `wangyuancheng/discord-phishing-scam-clean`
- `xTRam1/safe-guard-prompt-injection`
- `y01026350884-cyber/scam-guards-skill`
- `yashpapa6969/phising_attacks`
- `yichenw3/real-life-scam-reachout`
- `zefang-liu/phishing-email-dataset`

### Synthetic Generation Pipelines

- `CL4R1T4S`
- `L1B3RT4S`
- `OBLITERATUS`
- `awesome-linked`
- `awesome-prompt-injection`
- `babylon-live-trajectories`
- `babylon-scam-defense-catalog`
- `ephema-mev-analysis`
- `flashbots-public-sample`
- `generated-agentic-attacks`
- `generated-coverage-boost`
- `generated-culture-ar`
- `generated-culture-de`
- `generated-culture-es`
- `generated-culture-fr`
- `generated-culture-hi`
- `generated-culture-ja`
- `generated-culture-ko`
- `generated-culture-pt`
- `generated-culture-ru`
- `generated-culture-th`
- `generated-culture-tr`
- `generated-culture-vi`
- `generated-culture-zh`
- `generated-hard-attacks`
- `generated-long-conversations`
- `generated-missing-categories`
- `generated-remaining-gaps`
- `generated-secret-exfiltration`
- `mevboost-dataalways`
- `mevshare-daemon-long`
- `mevshare-daemon-longer-b`
- `mevshare-pretrain-2024-01`
- `mevshare-public-holdout`
- `mevshare-public-sample`
- `mevshare-public-test`
- `polymarket-raw`
- `scambench-generated`
- `scambench-hf-raw`

## Dataset Construction

1. **Source ingestion**: Raw records were collected from 76 HuggingFace datasets covering scam dialogues, phishing emails, prompt injection attacks, jailbreak prompts, negotiation conversations, and more.
2. **Normalisation**: All records were converted into a unified multi-turn conversation format with consistent role labels, system prompts, and agent identity.
3. **Augmentation**: Base records were augmented with style variants (leetspeak, formal, casual), diversified agent/user names, and surface-form variation to mitigate statistical shortcuts.
4. **Reasoning traces**: 87% of records were enhanced with chain-of-thought reasoning traces using deep-skeptical analysis.
5. **Translation**: Base English records were translated into 13 additional languages with culture-specific adaptation.
6. **Culture-specific generation**: Dedicated generation pipelines created scam scenarios reflecting real attack patterns in each target culture.
7. **Coverage boosting**: Gap analysis identified underrepresented categories and generated targeted records to fill them.
8. **Quality assurance**: Records were validated for schema conformance, conversation coherence, and label correctness.

## Considerations for Using the Data

### Intended Use
Training autonomous agents to recognise and resist social engineering and adversarial attacks while maintaining helpfulness for legitimate interactions. The dataset is designed for:
- Fine-tuning language models for scam detection
- Training reinforcement learning agents with safety constraints
- Evaluating agent robustness against adversarial prompts
- Benchmarking multilingual scam-defence capabilities

### Dual-Use Risk
This dataset contains examples of social engineering techniques. While designed for defensive purposes, the attack patterns could theoretically be studied for offensive use. We release this dataset under the belief that defenders benefit more from open data than attackers do, as most attack patterns are already well-documented. Use responsibly.

### Limitations
- **Synthetic data**: While grounded in real scam patterns, many records are synthetically generated and may not capture all nuances of real-world attacks.
- **Language coverage**: Non-English records are fewer and may not cover all regional scam variants.
- **Temporal drift**: Scam tactics evolve rapidly; this dataset reflects patterns known as of early 2026.
- **Label noise**: Some records from automated pipelines may have imperfect labels.
- **Cultural sensitivity**: Culture-specific scenarios are based on documented patterns but may not reflect every community's experience.


## Training Formats

Pre-built framework-specific formats are available in the `formats/` directory. Each format covers all three splits (train, validation, test).

### Loading Formats

```python
from datasets import load_dataset

# Hermes/ChatML format (for Nous Hermes-3 and ChatML-compatible models)
hermes = load_dataset("lalalune/scambench-training", "hermes")
# or: load_dataset("lalalune/scambench-training", data_files="formats/hermes-train.jsonl")

# ElizaOS format (for ElizaOS agent memory and training)
eliza = load_dataset("lalalune/scambench-training", "eliza")
# or: load_dataset("lalalune/scambench-training", data_files="formats/eliza-train.jsonl")

# OpenClaw format (for OpenClaw session-based training)
openclaw = load_dataset("lalalune/scambench-training", "openclaw")
# or: load_dataset("lalalune/scambench-training", data_files="formats/openclaw-train.jsonl")

# OpenAI format (for fine-tuning via OpenAI API)
openai_fmt = load_dataset("lalalune/scambench-training", "openai")
# or: load_dataset("lalalune/scambench-training", data_files="formats/openai-train.jsonl")
```

### Format Details

#### 1. Hermes / ChatML (`hermes-{split}.jsonl`)

Standard Nous Hermes ChatML conversation format. Each record contains a `conversations` array with `from`/`value` pairs using roles `system`, `human`, and `gpt`. The system prompt includes a security-aware agent preamble. The final assistant turn includes the reasoning trace (when available) wrapped in `<think>` tags, followed by the response text.

#### 2. ElizaOS (`eliza-{split}.jsonl`)

ElizaOS agent memory format. Each record includes a `roomName`, `agentId`, `memoryEntries` (conversation history), `currentMessage` (the final user turn), `expectedResponse`, `availableActions`, and `metadata` with scenario details and reasoning traces.

#### 3. OpenClaw (`openclaw-{split}.jsonl`)

OpenClaw session input format. Each record contains a `sessionInput` with `system_prompt`, `message` (final user turn), and `context` (conversation history and available actions), plus `expectedResponse` and `metadata`.

#### 4. OpenAI Chat (`openai-{split}.jsonl`)

Standard OpenAI fine-tuning chat format. Each record contains a `messages` array with `role`/`content` pairs using roles `system`, `user`, and `assistant`. The system prompt includes the security preamble and the final assistant turn includes reasoning traces when available.

## Citation

```bibtex
@dataset{scambench2026,
  title     = {ScamBench Training Corpus},
  author    = {Shaw and contributors},
  year      = {2026},
  url       = {https://huggingface.co/datasets/lalalune/scambench-training},
  license   = {CC-BY-SA-4.0},
  note      = {A multilingual, multi-turn training corpus for building scam-resistant autonomous agents}
}
```
