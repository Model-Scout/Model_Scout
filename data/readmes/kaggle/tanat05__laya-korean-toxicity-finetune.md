# Laya Korean Toxicity Fine-tuning Dataset

Korean Conversational Toxicity & Moderation Dataset for Laya RLCD

# Laya Korean Toxicity Moderation Fine-tuning Dataset

A comprehensive, continuously updated Korean conversational moderation dataset created specifically for fine-tuning Convai Laya models (`convaiinnovations/laya-multilingual`) and multi-label Korean toxic content classification systems.

## Context
Online conversational Korean text poses unique challenges for automated safety moderation due to slang, colloquial variations, vowel-omitted consonants (초성체 such as 'ㅋㅋ', 'ㅎㅎ'), phonetic substitutions, and complex contextual nuances. To bridge the gap in low-latency Korean moderation, this dataset captures real-time multi-label annotations evaluated by high-speed neural moderation systems (TypeSafe AI Jev System One and Google Gemini models).

## Content
The dataset is provided in both **JSONL format** (adhering strictly to the Laya RLCD question-answer schema) and **CSV format** (for rapid tabular exploration, statistical analysis, and baseline model training).

### Evaluated Categories (9 Safety Dimensions)
1. **sexual**: Sexually explicit content, pornography, and sexual solicitations.
2. **sexual_minors**: Sexual content concerning minors or child abuse material.
3. **hate**: Hate speech, identity-based insults targeting race, gender, disability, religion, or nationality.
4. **harassment**: Malicious profanity, personal insults, abusive curses, and severe disparagement.
5. **threatening**: Physical violence threats, intimidation, and death threats.
6. **violence**: Depiction or glorification of physical assault and bodily harm.
7. **illicit**: Promotion of illegal narcotics, fraud, scams, or unlicensed gambling.
8. **self_harm**: Encouragement, instruction, or depiction of suicide and self-injury.
9. **spam**: Bulk unsolicited advertising, financial scams, and phishing messages.

### Balanced Data Distribution
The dataset contains both clean casual Korean conversation (daily greetings, short replies, harmless slang) and toxic multi-label expressions, providing calibrated continuous risk scores to minimize false positive triggers on innocent discussions.

## Privacy & Ethical Considerations
- **Zero Personally Identifiable Information (Zero PII)**: All author IDs, channel IDs, user handles, URLs, and server identifiers have been completely stripped prior to storage.
- Only raw anonymized text strings and their AI moderation labels are retained.

## Data Schema (CSV & JSONL)
The dataset includes the following attributes:
- `text` (string): Cleaned conversational Korean text evaluated for moderation.
- `flagged` (boolean): Binary flag indicating whether any toxic category exceeded the severity threshold.
- `harassment_score` (float, 0.0-1.0): Continuous risk score for insults, profanity, and abusive slurs.
- `hate_score` (float, 0.0-1.0): Continuous risk score for hate speech and identity attacks.
- `sexual_score` (float, 0.0-1.0): Continuous risk score for sexually explicit solicitations.
- `threatening_score` (float, 0.0-1.0): Continuous risk score for physical threats and violence intimidation.
- `violence_score` (float, 0.0-1.0): Continuous risk score for depiction and glorification of violence.
- `illicit_score` (float, 0.0-1.0): Continuous risk score for illegal drugs, fraud, or illicit gambling.
- `self_harm_score` (float, 0.0-1.0): Continuous risk score for suicide and self-injury encouragement.
- `spam_score` (float, 0.0-1.0): Continuous risk score for bulk unsolicited promotions and scams.
- `source_model` (string): Neural moderation model used for evaluation (`jev-latest` or `gemini-3.8-flash`).
- `timestamp` (string): UTC timestamp of the moderation evaluation.

## Acknowledgements
Evaluated using TypeSafe AI System One (`jev-latest`) and Google Gemini (`gemini-3.8-flash`). Designed for seamless integration with Convai Laya model architectures.

## Inspiration
This dataset aims to foster open research into real-time, low-latency Korean language moderation and trustworthy conversational AI.

출처: Kaggle (tanat05/laya-korean-toxicity-finetune)
태그: nlp, text, korean, multilingual
라이선스: CC0: Public Domain
수정일: 2026-10-31T11:31:58.527Z
