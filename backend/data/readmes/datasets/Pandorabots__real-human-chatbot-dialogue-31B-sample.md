---
license: cc-by-nc-4.0
language:
- en
- ar
- ja
- hi
- vi
- ko
- pl
- es
- fr
tags:
- conversational-ai
- dialogue
- chatbot
- rlhf
- safety
- multilingual
- companion-ai
- long-context
pretty_name: Pandorabots Real Human Chatbot Dialogue 31B (Evaluation Sample)
size_categories:
- 100<n<1K
task_categories:
- text-generation
configs:
- config_name: companion_bot
  data_files: data/companion_bot.jsonl
- config_name: vertical_developer_bots
  data_files: data/vertical_developer_bots.jsonl
- config_name: multilingual
  data_files: data/multilingual.jsonl
---

# Pandorabots Real Human Chatbot Dialogue 31B — Evaluation Sample

**Gated sample of a 31B+ token corpus.** Full dataset licensing available, flexible terms.  
**Contact:** [data@pandorabots.com](mailto:data@pandorabots.com)

---

## What This Is

**18 years of real production traffic** from one of the longest-running conversational AI platforms in the world. Not synthetic. Not crowdsourced. Not scraped. Real users having real conversations with chatbots, collected with consent under platform Terms of Service from 2008 through 2026.

**Why this dataset is different:**
- **Real human intent:** Users typing to chatbots they chose to interact with, not paid annotators.
- **Exceptional depth:** Averages over 60 turns per session in the primary companion corpus, with interactions extending to thousands of turns.
- **Production diversity:** 7 channels, 20+ industry verticals, 100+ languages in the full corpus.
- **Genuine adversarial inputs:** Real users probing limits, not red-teamers simulating.
- **Clean provenance:** Consent secured, copyright cleared, PII removed, GDPR/EU AI Act compatible.
- **Enterprise governance:** Reviewed by external legal counsel as part of commercial licensing agreements with leading AI platforms.

---

## Sample Configurations

This sample is split into 3 configurations. Load any one or combine.

    from datasets import load_dataset

    # Pick a configuration
    ds = load_dataset("pandorabots/real-human-chatbot-dialogue-31B-sample", "companion_bot")
    ds = load_dataset("pandorabots/real-human-chatbot-dialogue-31B-sample", "vertical_developer_bots")
    ds = load_dataset("pandorabots/real-human-chatbot-dialogue-31B-sample", "multilingual")

| Config | Convos | Turns | Languages | Best For |
|---|---:|---:|---|---|
| `companion_bot` | 59 | 4,501 | English | Long-context dialogue, persona modeling, safety/alignment |
| `vertical_developer_bots` | 51 | 4,000 | English, French, Spanish, Polish | Domain adaptation, conversational agents |
| `multilingual` | 5 | 44 | Arabic, Japanese, Hindi, Vietnamese, Korean | Multilingual demonstration & fallback tracking |

**Total:** 115 conversations, 8,545 turns. Sample selected for quality; full corpus is vastly larger (see below).

---

## Configuration Details

### `companion_bot`

Long-running open-domain AI persona (Kuki / Mitsuku, multiple-time Loebner Prize winner) deployed across 7 channels: Discord, Facebook Messenger, Telegram, Roblox, Viber, web portal, and YouTube Live streaming.

**Segment Highlights:**
- **Extreme context length:** Averages 75+ turns per session in this sample, with some extending past 800 turns. This is among the longest-context real human-AI conversational data publicly available.
- **Authentic emotional range:** Joy, frustration, loneliness, humor, and curiosity expressed by real users.
- **Real adversarial inputs:** Users testing limits, attempting jailbreaks, and probing for inconsistencies.
- **Persona consistency:** A single named persona maintained across thousands of turns.
- **Multi-channel formats:** Demonstrates how communication style shifts between gaming (Discord, Roblox), messaging (Telegram, Messenger), and broadcast (YouTube Live).

### `vertical_developer_bots`

Real production chatbots built by independent developers and brands across 20+ industry verticals. Some are commercial enterprise deployments; others are indie projects. Includes both paid-tier and free-tier service samples for transparency.

**Verticals represented:**

| Vertical | Description |
|---|---|
| Fashion retail | Shopping assistants and product quizzes |
| Apparel retail | Fit advice and customer support |
| Automotive aftermarket | Customer service for tire dealerships |
| Legal | Support and guidance bots |
| Online gambling | Sports betting support |
| Financial / credit | Credit scoring assistance |
| Consumer health and beauty | Personal care advisors |
| E-commerce / pharmacy | Order and product support |
| Language learning | English and bilingual practice apps |
| Employment | Career guidance and job search |
| Enterprise service desk | Internal IT and operations |
| Social issues | Discussion bots on contemporary topics |
| Consumer IoT | Smart device personas |
| Encrypted messaging | Native platform assistants |
| Brand training | Internal training for brand ambassadors |
| B2B manufacturing | Service provider chatbots |
| SaaS | Customer support bots |
| CRM | Platform support bots |
| Media | Music and entertainment chatbots |
| Mobile assistants | Early-era voice assistant interactions |

### `multilingual`

A curated demonstration sample highlighting both native-language interactions and the structural routing constraints of early-era English-based AIML architectures.

| Code | Language | Convos | Notes |
|---|---|---:|---|
| ar | Arabic | 1 | Educational bot answering physics questions natively. |
| ja | Japanese | 1 | Open domain interaction showing high native fidelity. |
| hi | Hindi | 1 | Demonstrates English framework fallback constraints. |
| vi | Vietnamese | 1 | Demonstrates English framework fallback constraints. |
| ko | Korean | 1 | Multi-turn open domain conversational sample. |

This is a tiny cross-section, not a representative sample of the full multilingual corpus. The full corpus includes 100+ languages — see the **Full Language Breakdown** below.

**About multilingual coverage in the broader corpus:** The Pandorabots platform uses a wide variety of bots. Some bots (like the Arabic and Japanese samples) were built with localized native-language response logic. Many bots — including the primary Kuki/Mitsuku persona — are English-based AIML systems that have been deployed to users in many languages. For those deployments (like the Hindi, Vietnamese, and Korean samples), the unique value is the consent-cleared native-speaker **INPUT** distribution, which is scarce for many languages and useful for multilingual training even where bot output is not exemplary.

Samples in additional languages — including German, French, Spanish, Portuguese, Russian, Dutch, Italian, Korean, Japanese, Vietnamese, Mandarin, Hindi, and various low-resource languages — are available on request under NDA. Contact [data@pandorabots.com](mailto:data@pandorabots.com).

---

## Data Format

Each record in each `.jsonl` file is a single conversation:

    {
      "conversation_id": "companion_kuki_hq_0001",
      "channel": "web_portal",
      "language": "en",
      "turns": [
        {"role": "user", "content": "I like your name"},
        {"role": "assistant", "content": "Yes Kuki is a very nice name isn't it?"}
      ]
    }

| Field | Description |
|---|---|
| `conversation_id` | Unique identifier |
| `channel` | `web_chat`, `web_portal`, `messaging`, `gaming`, `social_streaming` |
| `language` | ISO 639-1 code |
| `turns` | Ordered list of `{"role": "user" or "assistant", "content": "..."}` |
| `use_case` | (vertical only) Generic business use case description |
| `bot_id` | (vertical & multilingual only) Anonymized bot identifier |
| `service_tier` | (vertical only) `paid` or `free` — service tier of the developer's bot |

### PII & Redaction Conventions

- `[REDACTED]` — placeholder for content that was masked at source (typically names, but in foreign-language conversations may include other identifying terms)
- `[IMAGE]` — images that the bot sent inline
- `[LINK]` — external links shared in conversation
- `[NAME REDACTED]` — full names (where they appeared)
- `[EMAIL REDACTED]` — email addresses
- `[BRAND REDACTED]` — brand names that appeared in conversation content
- First names alone are retained — they are not considered identifying PII under standard frameworks and are research-relevant for studying persona/name-following behavior

### Limitations & Considerations

While this dataset offers rare, authentic human-bot interactions, researchers should be aware of several structural characteristics and artifacts inherited from a live production environment:

*   **Variable Bot Quality & Fallback Loops:** Unlike distilled LLM datasets (e.g., GPT-4 synthetic outputs), the assistant responses in this corpus come from deployed AIML (rules-based) systems and earlier-era intent classifiers. The bots frequently rely on scripted fallback responses (e.g., *"I don't understand"*) and can occasionally get caught in repetitive conversational loops when users spam the system. The primary value of this dataset is the **authentic human input distribution**, not necessarily the bot's capabilities as a role model for generation.
*   **Multimodal UI Artifacts & System Tokens:** Because these bots were deployed on rich graphical interfaces (Messenger, Discord, web portals), user actions like clicking buttons or selecting carousels are logged as raw system tokens (e.g., `XREACT <emotion>`, `XREADING <feature>`, `xpayload`, `endlesstrivia`). These tokens are preserved because they encode meaningful multimodal interaction signals, but they will require filtering or special tokenization depending on your downstream training objective.
*   **Unfiltered Human Toxicity:** Open-domain, anonymous chatbots naturally attract boundary-testing. The dataset contains genuine instances of toxic language, explicit roleplay attempts, and aggressive adversarial probing. While highly valuable for RLHF and safety alignment, researchers should apply appropriate content warnings when distributing derivatives.
*   **Mismatched Multilingual Routing:** Outside of specifically localized bots, many non-English user inputs in the broader corpus were routed to English-centric AIML architectures. While this provides a massive, consent-cleared source of native-speaker input text, the corresponding bot outputs in those specific interactions are often structurally limited.

---

## Provenance & Compliance

| | |
|---|---|
| ✅ **GDPR / EU AI Act compatible** | Reviewed by external legal counsel |
| ✅ **User consent secured** | Via platform Terms of Service accepted at registration |
| ✅ **Copyright cleared** | Platform-owned content under ToS |
| ✅ **PII removed** | Names, usernames, URLs, emails redacted |
| ❌ **No synthetic data** | All real human inputs |
| ❌ **No web scraping** | Platform-native collection only |

---

## Intended Uses

| Use Case | Why This Data Helps |
|---|---|
| LLM grounding & fine-tuning | Naturalistic, unscripted human dialogue at scale |
| RLHF / preference modeling | Long multi-turn context with real user signals |
| Safety & alignment training | Real adversarial and guardrail-probing inputs |
| Long-context evaluation | Avg 70 turns — genuine persistent context |
| Companion AI training | Persona consistency across thousands of turns |
| Domain adaptation | 20+ real verticals with production task flows |
| Multilingual fine-tuning | 5 non-English languages in sample, 100+ in full corpus |
| Low-resource language research | Consent-cleared data in scarce-for-AI languages |
| Conversational agent training | Multi-step task-oriented dialogue across industries |
| Dialogue coherence research | Unusually long sessions reveal turn-level coherence patterns |

**Commercial use of this sample, or use of the full corpus in any form, requires a separate license.** Contact [data@pandorabots.com](mailto:data@pandorabots.com).

---

## Full Corpus

This sample represents a tiny fraction of the full corpus — well under 0.001%.

| Segment | Volume |
|---|---|
| Companion Bot | ~12.4B tokens |
| Vertical Developer Bots | ~18.6B tokens |
| Multilingual Subset (100+ languages) | ~1.5B tokens |
| **Full Corpus** | **31B+ tokens** |

Roughly 10B human input tokens. Average 61 turns per session in the full Companion Bot segment, with sessions extending up to thousands of turns.

### Full Language Breakdown (Top Languages by Token Volume)

| Language | Tokens |
|---|---:|
| English | 12.5B |
| German | 542.8M |
| Spanish | 194.9M |
| Portuguese | 177.9M |
| French | 131.6M |
| Russian | 104.0M |
| Dutch | 101.7M |
| Italian | 47.3M |
| Chinese | 21.0M |
| Polish | 20.2M |
| Turkish | 15.4M |
| Hungarian | 10.0M |
| Swahili | 9.0M |
| Tagalog | 8.6M |
| Arabic | 7.9M |
| Korean | 6.3M |
| Japanese | 6.1M |
| Persian | 4.5M |

Plus 80+ additional languages including low-resource languages scarce for AI training. Full breakdown available on request.

### Available Tranches

The full corpus can be licensed in segments or as a whole. Common configurations:

- **Companion Bot only** (~12.4B tokens) — ideal for safety/alignment, persona, and long-context research
- **Vertical Developer Bots** (~18.6B tokens) — ideal for domain adaptation and conversational agent training
- **Multilingual Subset** (~1.5B tokens) — licensable as a full bundle or by individual language cluster
- **Full Corpus** (31B+ tokens) — volume discounts available

Flexible terms — segment, language cluster, or full corpus licensing all available.

→ **[data@pandorabots.com](mailto:data@pandorabots.com)**

---

## Citation

    @dataset{pandorabots_real_human_chatbot_dialogue_31b_sample_2026,
      title   = {Pandorabots Real Human Chatbot Dialogue 31B (Evaluation Sample)},
      author  = {Pandorabots, Inc.},
      year    = {2026},
      url     = {https://huggingface.co/datasets/pandorabots/real-human-chatbot-dialogue-31B-sample},
      license = {CC BY-NC 4.0}
    }

---

## License

[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) — free for research and non-commercial use with attribution. Commercial use requires a license agreement.

**Pandorabots, Inc.** — [pandorabots.com](https://www.pandorabots.com) — [data@pandorabots.com](mailto:data@pandorabots.com)