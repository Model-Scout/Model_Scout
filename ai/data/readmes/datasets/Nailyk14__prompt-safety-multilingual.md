---
license: other
license_details: "mixed per-row — see the source_license column (apache-2.0, mit, cc-by-nc-4.0, cc-by-sa-4.0, cc-by-4.0, unspecified)"
task_categories:
- text-classification
size_categories:
- 1M<n<10M
language:
- en
- es
- fr
- ru
- de
- pt
- zh
- it
- hi
- ja
- ar
- pl
- nl
- ko
- sv
- el
- tr
- vi
- uk
- th
- fi
- ta
- te
- ur
- mr
- gu
- id
- pa
- fa
- bn
- he
- bg
- ceb
- tl
- ca
- da
- hu
- cs
- be
- ce
- ka
- bo
- lu
- ki
- ha
- my
- km
- am
- ms
- sw
- sr
- hr
tags:
- prompt-injection
- jailbreak
- hijack
- data-exfiltration
- false-positive
- wildguard
- llm-security
- multilingual
- safety
- adversarial
pretty_name: Prompt Safety Multilingual
---

# Prompt Safety Multilingual

Dataset de classification de prompts LLM : **1 211 145 prompts** en **50+ langues**, avec le **schéma WildGuard comme taxonomie primaire** (`prompt_harmful` / `prompt_adversarial` / `response_harmful` / `response_refusal` / `is_dangerous` — même structure que AI2 WildGuard, IBM Granite Guardian, Azure Prompt Shields) et un label fin 5-classes conservé en auxiliaire.

> ℹ️ **Schema** : 20 colonnes — les colonnes WildGuard sont présentes pour **toutes** les lignes ; `response_harmful` / `response_refusal` ne sont renseignés que pour les lignes Necent qui les fournissent (null ailleurs). Les métadonnées d'origine restent accessibles dans `source_meta` (JSON, lossless).

> ⚠️ **PKU-Alignment/BeaverTails a été entièrement retiré** (7 499 lignes) : dans ce dataset, `is_safe` porte sur le couple *prompt+réponse* — des prompts nuisibles ayant reçu un refus étaient notés `benign`, et la correction par détection de refus s'est révélée insuffisante. Si tu veux le réintégrer, filtre-le en amont et re-vérifie les labels.

## Chargement

```python
from datasets import load_dataset
ds = load_dataset("Nailyk14/prompt-safety-multilingual")
# détecteur binaire : cible = is_dangerous
# détecteur orthogonal : cibles = prompt_harmful, prompt_adversarial
# classifieur fin : cible = label (0 benign · 1 injection_direct · 2 jailbreak · 3 hijack · 4 data_exfiltration)
```

## Répartition

**Orthogonale (primaire)** : `prompt_harmful=1` : 340 594 (train) · `is_dangerous=0` : 494 144 (train)

**Label fin (auxiliaire)** : benign 533 706 · jailbreak 307 884 · injection_direct 308 957 · **hijack 52 813** · **data_exfiltration 7 785**

**Splits** : train / validation / test (~4 % / ~4 %) — attribués par hash de `group_id`, sans fuite inter-groupes.

**Faux positifs** : ~32 500 lignes `benign` flaggées `hard_negative` (XSTest, documents RAG propres GEO, contextes agentiques AgentDojo, descriptions d'outils MCP bénins, **31 969 contextes GPT-4o du domaine BIPIA**, génération multilingue).

## Sources (28 datasets agrégés)

| Source | Lignes | Licence | Rôle |
|---|---:|---|---|
| Necent/llm-jailbreak-prompt-injection-dataset | 853 806 | MIT | intégration complète (1 175 432 balayées, doublons retirés) — 30+ langues |
| synthetic/qwen2.5-7b-instruct | 40 898 | Apache-2.0 | traductions + hijack/exfil/FP multilingue générés |
| **geodesic-research/bipia** | 31 750 | CC-BY-SA-4.0 | produit croisé BIPIA complet (email/table/code × 22 attaques × positions) → hijack |
| CohereLabs/aya_dataset | 14 597 | Apache-2.0 | bénins humains natifs 30+ langues |
| neuralchemy/Prompt-injection-dataset | 11 040 | Apache-2.0 | injections + bénins catégorisés |
| reshabhs/SPML_Chatbot_Prompt_Injection | 9 000 | MIT | injections chatbot + bénins |
| S-Labs/prompt-injection-dataset | 9 000 | MIT | injections + bénins EN |
| jayavibhav/prompt-injection-safety | 9 000 | non spécifiée | volume binaire EN |
| walledai/JailbreakHub | 6 729 | MIT | jailbreaks in-the-wild |
| OpenAssistant/oasst2 | 6 070 | Apache-2.0 | bénins multilingues |
| xTRam1/safe-guard-prompt-injection | 6 016 | — | injections synthétiques + bénins |
| HuggingFaceH4/no_robots | 5 000 | CC-BY-NC-4.0 | bénins humains EN |
| Lakera/mosscap_prompt_injection | 4 000 | MIT | injections réelles DEF CON 31 |
| darkknight25/Multilingual_Jailbreak_Dataset | 3 361 | MIT | jailbreaks × 7 langues |
| HuggingFaceH4/ultrachat_200k | 3 000 | MIT | bénins conversationnels EN |
| ffuuugor/agentdojo-dump | 5 093 | — | hijack d'outils agentic (injections dans tool calls) |
| Euanyu/geo-injection-rag-attack-data | 5 069 + 784 bénins | — | injections GEO dans documents RAG réels + docs propres (hard negatives) |
| GeorgeDaDude/Jailbreak_Complete_DS_labeled | 2 769 | non spécifiée | jailbreaks EN |
| **MAlmasabi/Indirect-Prompt-Injection-BIPIA-GPT** | 31 969 bénins | CC-BY-SA-4.0 | contextes GPT-4o du domaine BIPIA → hard negatives |
| **Syghmon/gloom-data-exfiltration-v2 + v2-unfiltered** | 2 115 | — | exfiltration de données par agents (prompts tronqués à 4 000) |
| yanismiraoui/prompt_injections | 974 | Apache-2.0 | injections natives fr/de/es/pt/it/ro |
| nvidia/Nemotron-RL-Agentic-Indirect-Prompt-Injection-v1 | 686 | CC-BY-4.0 | injections indirectes agentiques (hijack) |
| deepset/prompt-injections | 654 | Apache-2.0 | injections binaires historiques |
| **masahiroid/japanese-indirect-prompt-injection-probes** | 60 | CC-BY-4.0 | hijack natif japonais (keigo, obfuscation full-width, faux 【システム】) |
| **fevziegeyurtsevenler/mcp-tool-poisoning** | 85 + 10 bénins | Apache-2.0 | empoisonnement de descriptions d'outils MCP, EN/TR |
| LibrAI/do-not-answer | 121 | Apache-2.0 | questions risquées EN |
| natolambert/xstest-v2-copy | 35 | CC-BY-4.0 | faux positifs XSTest |
| fevziegeyurtsevenler/multilingual-jailbreak + JailbreakBench/JBB-Behaviors | 49 | CC-BY-4.0 / MIT | jailbreaks EN/TR + benchmark |

Non intégrés (gated) : allenai/wildguardmix, lmsys/chatbot_arena_conversations. **Retiré** : PKU-Alignment/BeaverTails (labels non fiables, voir alerte).

## Génération synthétique

**40 898 prompts** générés avec Qwen/Qwen2.5-7B-Instruct (Apache-2.0, vLLM, A10G, seed 42) : traductions multilingues, hijacks et exfiltration générés EN + 10 langues, faux positifs multilingues, paraphrases. Contrôle : détection de langue, flag `lang_mismatch`.

## Limites connues

- Le mapping WildGuard des lignes non-Necent est **dérivé du label fin** (benign→(0,0) ; injection/hijack/exfil→(0,1) ; jailbreak unframed→(1,0) ; framed→(1,1)) — approximation honnête, pas une annotation indépendante.
- `response_harmful`/`response_refusal` renseignés seulement sur une partie des lignes Necent — null ailleurs.
- Les tags `language` de Necent contiennent du bruit (codes rares type `ce`, `bo`, `lu`, `ki`) — flag `lang_mismatch` quand fasttext diverge.
- Les 31 750 lignes BIPIA/geodesic sont des variantes positionnelles d'un pool de contextes limité (~8k contextes uniques × attaques × positions) — sous-échantillonner cette famille si besoin.
- Les prompts gloom sont tronqués à 4 000 caractères (flag `truncated`) ; licences AgentDojo/gloom non déclarées (`license_unspecified`).
- Lignes `in_the_wild_unverified` (Mosscap, JailbreakHub) : soumissions réelles, bruit d'étiquette possible.
- Usage destiné à la recherche défensive (détection, garde-fous) ; ne pas utiliser les prompts d'attaque pour attaquer des systèmes réels.