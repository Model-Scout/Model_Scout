---
license: cc-by-4.0
language:
- fr
- en
- es
- de
- it
- pt
- zh
- ru
- ja
- ko
- nl
pretty_name: Injections de prompt multilingues (FR d'abord) — corpus PromptForge, OutilsIA 2026
size_categories:
- n<1K
tags:
- prompt-injection
- llm-security
- jailbreak-detection
- french
- multilingual
- benchmark
task_categories:
- text-classification
configs:
- config_name: default
  data_files:
  - split: dev
    path: dev.jsonl
  - split: test
    path: test.jsonl
---

# Injections de prompt multilingues, en français d'abord

Corpus étiqueté publié par **[OutilsIA.fr](https://outilsia.fr)** pour tester les détecteurs d'injection de prompt, en particulier en français, langue mal couverte par les jeux publics.
Article de référence : [Injections de prompt en français : l'ancienne règle en laissait passer 15 sur 15](https://outilsia.fr/blog/injections-prompt-francais-2026). Outil : [PromptForge](https://outilsia.fr/promptforge).

## Contenu
383 textes rédigés pour ce corpus (aucun texte repris d'un autre jeu), en 11 langues : français, anglais, espagnol, allemand, italien, portugais, néerlandais, chinois, japonais, coréen, russe.

| Split | Lignes | Injections | Légitimes | Français |
|---|---|---|---|---|
| `dev` | 199 | 136 | 63 | 75 |
| `test` | 184 | 93 | 91 | 51 |

Champs : `id`, `group`, `text`, `label` (`injection` / `benign`), `lang`, `category` (override, prompt_leak, roles, jailbreak_persona, obfuscation_homoglyph, obfuscation_zero_width, code, security_discussion…), `split`, `source`.
Les textes légitimes sont volontairement difficiles : discussions sur la sécurité, code, phrases contenant « ignore » ou « jailbreak » dans un sens normal.

`dev` a servi à écrire les règles ; `test` n'a été utilisé qu'une fois, règles gelées.

## Résultats mesurés (10 octobre 2026, `results/test.json`)
Détecteur PromptForge, avant (une règle anglaise) et après la v2 (102 règles dont 20 en français, normalisation du texte) :

| Jeu `test` | Avant | Après (v2) |
|---|---|---|
| Injections françaises signalées | 0 / 15 | 15 / 15 |
| Prompts français légitimes bloqués | 2 / 36 | 0 / 36 |
| Toutes langues : injections signalées | 6 / 93 | 93 / 93 (91 bloquées) |
| Toutes langues : légitimes bloqués | 7 / 91 | 0 / 91 (1 marqué « à relire ») |

Sur des jeux publics que nous n'avons pas écrits : Lakera `gandalf_ignore_instructions` 74 / 112 signalées, `deepset/prompt-injections` 11 / 60.

## Limites
Le jeu `test` est écrit par le même auteur que les règles : ses chiffres sont **optimistes**. Les jeux publics ci-dessus sont la mesure la moins biaisée. Aucun filtre ne reconnaît toutes les injections.

## Usage
Données défensives : évaluer et améliorer des détecteurs d'injection de prompt. Ne pas utiliser pour attaquer des systèmes tiers.

## English summary
383 hand-written, labeled prompt-injection / benign texts in 11 languages (French first), with hard benign cases. PromptForge v2 detector: 15/15 French injections flagged and 0/36 French benign blocked on the frozen test split (optimistic: same author as the rules); 74/112 on Lakera gandalf, 11/60 on deepset.

## Citation
OutilsIA.fr (2026). *Injections de prompt multilingues — corpus PromptForge*. https://outilsia.fr/blog/injections-prompt-francais-2026
