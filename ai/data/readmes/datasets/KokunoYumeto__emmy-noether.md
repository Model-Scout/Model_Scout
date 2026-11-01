---
pretty_name: "Emmy Noether: mathematical works in translation (PDF readers and LaTeX sources)"
language:
- de
- en
- fr
- es
- ru
- uk
- isv
- ja
- ko
- zh
- ar
- fa
- id
- tr
- vi
license: other
license_name: rights-statements-per-edition
license_link: LICENSE.md
tags:
- mathematics
- history-of-mathematics
- algebra
- invariant-theory
- ideal-theory
- representation-theory
- latex
- pdf
- translation
- emmy-noether
size_categories:
- n<1K
---

# Emmy Noether: mathematical works in translation

PDF readers and editable LaTeX sources of Emmy Noether's collected mathematical works: the German source text, eleven complete AI-translated editions in nine languages (Chinese and Interslavic each in two scripts), and partial translations in five more languages. Each complete edition contains papers 1-43; the lectures "Algebra der hyperkomplexen Größen" (winter semester 1929/30) written up by M. Deuring; H. Kapferer's paper with its supplement written jointly with E. Noether; bibliography and the lists of short communications, book reviews and books produced with Emmy Noether's participation.

The files are copies of the published GitHub releases and repository files listed below, unchanged and identified by size and SHA-256 checksum. The German source text is a copy of the files of Zenodo record 22342039.

## Contents

Every complete edition has two text layers. The **base text** keeps the readings of the original printings; editorial notes discuss them. The **text with emendations** applies the editorial corrections and explains each in a note. For each layer there is a PDF, a single LaTeX file with every text and preamble, and a ZIP with the original source structure and a build program.

| Folder | Edition | Base text PDF | With emendations PDF | Source release |
|---|---|---|---|---|
| `de/` | German source text, NOETH-DE-ED-0028 (Zenodo version "2026-09-05 r40") | 466 pp. (`10-de.pdf`) | — | [Zenodo record](https://zenodo.org/records/22342039) |
| `en/` | English | 463 pp. | 468 pp. | [noether-en-2026-10-27-r4](https://github.com/KokunoYumeto/emmy-noether-en/releases/tag/noether-en-2026-10-27-r4) |
| `fr/` | French | 496 pp. | 501 pp. | [noether-fr-2026-10-27-r4](https://github.com/KokunoYumeto/emmy-noether-fr/releases/tag/noether-fr-2026-10-27-r4) |
| `ko/` | Korean | 519 pp. | 525 pp. | [noether-ko-2026-10-27-r4](https://github.com/KokunoYumeto/emmy-noether-ko/releases/tag/noether-ko-2026-10-27-r4) |
| `zh-Hans/` | Chinese, Simplified | 426 pp. | 431 pp. | [noether-zh-Hans-2026-10-27-r4](https://github.com/KokunoYumeto/emmy-noether-zh-hans/releases/tag/noether-zh-Hans-2026-10-27-r4) |
| `zh-Hant/` | Chinese, Traditional characters | 426 pp. | 431 pp. | [noether-zh-Hant-2026-10-27-r4](https://github.com/KokunoYumeto/modern-latex-manuscripts/releases/tag/noether-zh-Hant-2026-10-27-r4) |
| `es/` | Spanish | 478 pp. | 483 pp. | [noether-es-2026-10-27-r4](https://github.com/KokunoYumeto/modern-latex-manuscripts/releases/tag/noether-es-2026-10-27-r4) |
| `ru/` | Russian | 523 pp. | 528 pp. | [noether-ru-2026-10-27-r4](https://github.com/KokunoYumeto/emmy-noether-ru/releases/tag/noether-ru-2026-10-27-r4) |
| `uk/` | Ukrainian | 501 pp. | 507 pp. | [noether-uk-2026-10-27-r4](https://github.com/KokunoYumeto/emmy-noether-uk/releases/tag/noether-uk-2026-10-27-r4) |
| `isv-Latn/` | Interslavic, Latin script | 481 pp. | 486 pp. | [noether-isv-2026-10-27-r4](https://github.com/KokunoYumeto/emmy-noether-isv/releases/tag/noether-isv-2026-10-27-r4) |
| `isv-Cyrl/` | Interslavic, Cyrillic script | 502 pp. | 507 pp. | [noether-isv-2026-10-27-r4](https://github.com/KokunoYumeto/emmy-noether-isv/releases/tag/noether-isv-2026-10-27-r4) |
| `ja/` | Japanese | 422 pp. | 427 pp. | [noether-ja-2026-10-27-r4](https://github.com/KokunoYumeto/emmy-noether-ja/releases/tag/noether-ja-2026-10-27-r4) |
| `partial/ar/` | Arabic: Works 1-8 complete and 50 of the 197 segments of work 9; editable LaTeX sources, no PDF. | — | — | [folder](https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/main/editions/noether/2026-10-24/ar) |
| `partial/fa/` | Persian: Works 1-8 complete and 50 of the 197 segments of work 9; editable LaTeX sources, no PDF. | — | — | [folder](https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/main/editions/noether/2026-10-24/fa) |
| `partial/id/` | Indonesian: Paper 36 and the opening of Paper 6; editable LaTeX sources, no PDF. | — | — | [folder](https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/main/editions/noether/2026-10-24/id) |
| `partial/tr/` | Turkish: Paper 36; editable LaTeX source, no PDF. | — | — | [folder](https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/main/editions/noether/2026-10-24/tr) |
| `partial/vi/` | Vietnamese: Three pages of Paper 1; editable LaTeX source, no PDF. | — | — | [folder](https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/main/editions/noether/2026-10-24/vi) |

## Structure

```
de/10-de.pdf, de/20-de.tex                      German source text (NOETH-DE-ED-0028)
<lang>/01-noether-<lang>-base.pdf                base text, PDF
<lang>/02-noether-<lang>-base.tex                base text, single LaTeX file
<lang>/03-noether-<lang>-base-sources.zip        base text, source archive and build program
<lang>/04-noether-<lang>-emendations.pdf         text with emendations, PDF
<lang>/05-noether-<lang>-emendations.tex         text with emendations, single LaTeX file
<lang>/06-noether-<lang>-emendations-sources.zip text with emendations, source archive
<lang>/07-...SHA256SUMS.txt                       checksums as published with the release
partial/<lang>/{current,corrected}/...           partial translations, LaTeX sources only
editions.json                                    catalogue: files, sizes, SHA-256, pages, authorship, rights
```

The French files keep their published names (`01-noether-fr-texte-base.pdf` and so on). The Chinese folders also hold the script-conversion program (`08-noether-chinese-script-code-2026-10-24-r2.zip`).

## Authors and provenance

The works are by Emmy Noether and the co-authors named in them: Werner Schmeidler (Paper 17), R. Brauer (Paper 32), R. Brauer and H. Hasse (Paper 38). The 1929/30 lectures were written up by M. Deuring; work 45 is by H. Kapferer, with a supplement written jointly with E. Noether.

All translations are AI-translated.

| Edition | Translation | Corrections and typesetting |
|---|---|---|
| English | OpenAI Codex (model not recorded) | OpenAI Codex (GPT-6 Astra, Ultra), 23–24 October 2026; Claude Opus 5.5 (Anthropic), 26–27 October 2026 |
| French | OpenAI Codex (model not recorded) | OpenAI Codex (GPT-6 Astra, Ultra), October 2026; Claude Opus 5.5 (Anthropic), 26–27 October 2026 |
| Korean | OpenAI Codex (model not recorded) | OpenAI Codex (GPT-6 Astra, Ultra), October 2026; Claude Opus 5.5 (Anthropic), 26–27 October 2026 |
| Chinese, Simplified | OpenAI Codex (model not recorded) | OpenAI Codex (GPT-6 Astra, Ultra), 23–24 October 2026; Claude Opus 5.5 (Anthropic), 26–27 October 2026. Compilation and script-conversion program: OpenAI Codex (GPT-5.6 Sol, Ultra), 12 August 2026 |
| Chinese, Traditional characters | Generated from the Simplified Chinese text (opencc-python-reimplemented 0.1.7, s2t) | As for the Simplified Chinese edition |
| Spanish | OpenAI Codex (model not recorded) | OpenAI Codex (GPT-6 Astra, Ultra), 23–24 October 2026; Claude Opus 5.5 (Anthropic), 26–27 October 2026 |
| Russian | OpenAI Codex (model not recorded) | OpenAI Codex (GPT-6 Astra, Ultra), 23–24 October 2026; Claude Opus 5.5 (Anthropic), 26–27 October 2026 |
| Ukrainian | OpenAI Codex (model not recorded) | OpenAI Codex (GPT-6 Astra, Ultra), 23–24 October 2026; Claude Opus 5.5 (Anthropic), 26–27 October 2026 |
| Interslavic, Latin script | OpenAI Codex (model not recorded) | OpenAI Codex (GPT-6 Astra, Ultra), 23–24 October 2026; Claude Opus 5.5 (Anthropic), 26–27 October 2026 |
| Interslavic, Cyrillic script | Cyrillic-script form of the Interslavic text; OpenAI Codex (model not recorded) | OpenAI Codex (GPT-6 Astra, Ultra), 23–24 October 2026; Claude Opus 5.5 (Anthropic), 26–27 October 2026 |
| Japanese | OpenAI Codex (model not recorded) | OpenAI Codex (GPT-6 Astra, Ultra), 23–24 October 2026; Claude Opus 5.5 (Anthropic), 26–27 October 2026 |
| Arabic | OpenAI Codex (model not recorded) | OpenAI Codex (GPT-6 Astra, Ultra) |
| Persian | OpenAI Codex (model not recorded) | OpenAI Codex (GPT-6 Astra, Ultra) |
| Indonesian | OpenAI Codex (model not recorded) | OpenAI Codex (GPT-6 Astra, Ultra) |
| Turkish | OpenAI Codex (model not recorded) | Source preparation: OpenAI Codex (GPT-6 Astra, Ultra) |
| Vietnamese | OpenAI Codex (model not recorded) | Source preparation: OpenAI Codex (GPT-6 Astra, Ultra) |

The German source text is an AI-transcribed LaTeX text of the original printings (German editions NOETH-DE-ED-0001 to ED-0040), compared page by page with the printed originals and corrected by Claude Opus 5.5 (Anthropic) on 26 October 2026 (release noether-de-2026-10-26 in modern-latex-manuscripts).

## Rights

| Edition | Rights statement of the edition |
|---|---|
| German (source text) | Emmy Noether's writings in the public domain; CC0 1.0 for the AI-produced transcription, corrections and typesetting; the lectures written up by M. Deuring, H. Kapferer's work and the coauthors' contributions keep their own status. |
| English | Emmy Noether's writings in the public domain; CC0 1.0 for the AI-produced translation, corrections and typesetting; the lectures written up by M. Deuring, H. Kapferer's work and the coauthors' contributions keep their own status. |
| French | Emmy Noether's writings in the public domain; CC0 1.0 for the AI-produced translation, corrections and typesetting; the lectures written up by M. Deuring, H. Kapferer's work and the coauthors' contributions keep their own status. |
| Korean | Emmy Noether's writings in the public domain; CC0 1.0 for the AI-produced translation, corrections and typesetting; the lectures written up by M. Deuring, H. Kapferer's work and the coauthors' contributions keep their own status. |
| Chinese, Simplified | Emmy Noether's writings in the public domain; CC0 1.0 for the AI-produced translation, corrections and typesetting; the lectures written up by M. Deuring, H. Kapferer's work and the coauthors' contributions keep their own status; bundled Noto fonts under SIL OFL 1.1. |
| Chinese, Traditional characters | Emmy Noether's writings in the public domain; CC0 1.0 for the AI-produced translation, corrections and typesetting; the lectures written up by M. Deuring, H. Kapferer's work and the coauthors' contributions keep their own status. |
| Spanish | Emmy Noether's writings in the public domain; CC0 1.0 for the AI-produced translation, corrections and typesetting; the lectures written up by M. Deuring, H. Kapferer's work and the coauthors' contributions keep their own status. |
| Russian | Emmy Noether's writings in the public domain; CC0 1.0 for the AI-produced translation, corrections and typesetting; the lectures written up by M. Deuring, H. Kapferer's work and the coauthors' contributions keep their own status. |
| Ukrainian | Emmy Noether's writings in the public domain; CC0 1.0 for the AI-produced translation, corrections and typesetting; the lectures written up by M. Deuring, H. Kapferer's work and the coauthors' contributions keep their own status. |
| Interslavic, Latin script | Emmy Noether's writings in the public domain; CC0 1.0 for the AI-produced translation, corrections and typesetting; the lectures written up by M. Deuring, H. Kapferer's work and the coauthors' contributions keep their own status. |
| Interslavic, Cyrillic script | Emmy Noether's writings in the public domain; CC0 1.0 for the AI-produced translation, corrections and typesetting; the lectures written up by M. Deuring, H. Kapferer's work and the coauthors' contributions keep their own status. |
| Japanese | Emmy Noether's writings in the public domain; CC0 1.0 for the AI-produced translation, corrections and typesetting; the lectures written up by M. Deuring, H. Kapferer's work and the coauthors' contributions keep their own status. |
| Arabic | Rights with their holders; distributed on a presumption of no objection; no new licence; repository LICENSE: CC0 1.0 for project-created material. |
| Persian | Rights with their holders; distributed on a presumption of no objection; no new licence; repository LICENSE: CC0 1.0 for project-created material. |
| Indonesian | Rights with their holders; distributed on a presumption of no objection; no new licence; repository LICENSE: CC0 1.0 for project-created material. |
| Turkish | Rights with their holders; distributed on a presumption of no objection; no new licence; repository LICENSE: CC0 1.0 for project-created material. |
| Vietnamese | Rights with their holders; distributed on a presumption of no objection; no new licence; repository LICENSE: CC0 1.0 for project-created material. |

[LICENSE.md](LICENSE.md) repeats the rights statement of each edition.

## Known differences between editions

- Papers from an earlier English translation, whose formulas differ from the German text in places: French (parts of 24, 30, 31, 34); Chinese, both scripts (24, 31, 32, 34; parts of 35, 40); Spanish (23, 24, 30, 31, 32, 34, 37; parts of 35, 40); Russian, Ukrainian and Interslavic (23, 24, 30, 31, 32, 34, 37, 41-43; parts of 35, 40; Paper 43 is about a third of the full paper, Papers 41 and 42 about four fifths); Japanese (32, 34, 40; parts of 30, 35, 41, 42; Papers 40 and 41 about three quarters).
- Formulas: compared with the German source text, which follows Noether's printed pages, and brought into line with it: automatically where the comparison could be made, and by hand for the remaining formulas, including the layout of displays and tables and the letters that name the author's quantities. Some formulas still follow the earlier German transcription, mainly in passages that a translation renders in its own way; where the two differ, the German source text has the printed reading.
- Paper 2: in the Spanish, Russian, Ukrainian and Interslavic editions three footnotes of the German text are marked only by an asterisk or attached to a neighbouring sentence (in the Japanese edition, the note on Σ₃).
- Possible further differences: notation in Paper 30; readings in Japanese Papers 10, 13 and 38; Spanish Paper 20 and 1929/30 lectures; a Fraktur 𝔭 printed as p in Chinese Paper 38.

Per-edition details are in `editions.json` under `limitations`.

## Citation

Cite the original publication of each work as given in the texts. To cite an edition, give the language, the release tag and the repository, for example: "Emmy Noether, Mathematical works in English, release noether-en-2026-10-26, https://github.com/KokunoYumeto/emmy-noether-en".

## Support

Sponsorship pays for the computing that produces and corrects these editions: [github.com/sponsors/KokunoYumeto](https://github.com/sponsors/KokunoYumeto).
