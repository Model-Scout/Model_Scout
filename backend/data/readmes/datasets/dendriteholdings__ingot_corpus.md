---
pretty_name: Quantedo Corpus
license: other
license_details: Mixed. Each row keeps the license of its source dataset; see the Sources table.
task_categories:
- text-generation
language:
- en
- zh
- ar
- ru
- ko
- es
- de
- hi
- fr
- ja
- pt
- vi
- it
- tr
- nl
- te
- fi
- id
- pl
- ms
- bn
- sv
- lt
- mg
- cs
- el
- he
- si
- fa
- ro
- sw
- hu
- ha
- uk
- sr
- ne
- am
- ta
- da
- th
- so
- yo
- bg
- ky
- sl
- sk
- lv
- tl
- et
- ig
- mr
- sn
- km
- ny
- pa
- ur
- ml
- gu
- is
- hr
- no
- sq
- eu
- ti
- zu
- af
- xh
- my
- ca
- rw
- bs
- be
- mk
- ka
- az
- kn
- mt
- lb
- ga
- ps
- gl
- uz
- as
- tg
size_categories:
- 10M<n<100M
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: chungus
    path: data/chungus-*
dataset_info:
  features:
  - name: dataset
    dtype: string
  - name: split
    dtype: string
  - name: entry_name
    dtype: string
  - name: domain
    dtype: string
  - name: language
    dtype: string
  - name: user_prompt
    dtype: string
  - name: conversation
    dtype: string
  splits:
  - name: train
    num_examples: 1812669
  - name: chungus
    num_examples: 10614351
---

# quantedo_corpus

A broad prompt corpus. The `chungus` split contains 10,614,351 task prompts over 18 domains and 84
languages, taken from 366 public datasets; the `train` split is the legacy 1,812,669-row release. It
holds prompts only, no answers; swe and terminal rows are agent conversations (see Agent turns). It is meant for comparing a
model's output distribution with a reference model's (e.g. KL divergence between a quantized model and
its teacher) across as many capabilities and languages as possible.

## Columns

| column | meaning |
|---|---|
| `dataset` | short id of the source dataset (see Sources) |
| `split` | the split of the source dataset the row comes from |
| `entry_name` | the task's id in the source dataset (its id column, else `<file>:<row>`) |
| `domain` | the capability the task exercises |
| `language` | natural language of the prompt (ISO 639-1, else ISO 639-3) |
| `user_prompt` | the task as the first user message |
| `conversation` | swe and terminal rows only: the whole agent trajectory, as JSON `{"messages": [...], "tools": [...]}` in the chat-template format; null elsewhere |

## How it was built

1. Trajectories and conversations: only the first user message is kept. System prompts, assistant turns
   and everything after are dropped. For `systemchat`, `toolace`, `apigen_mt`, `toucan_p1`, `toucan_p2`, `toucan_p3`, `toucan_p4`, `xlam_apigen`, `toolbench_queries`, `dolci_tool_use`, `hammerbench_zh`, `turkish_fc`, `glaive_fc_v2`, `glaive_fc_ko`, `japanese_fc`, `arabic_fc`, `toolmind_graphsyn`, `dfm13_tool_be`, `dfm13_tool_bg`, `dfm13_tool_bs`, `dfm13_tool_fa`, `dfm13_tool_hr`, `dfm13_tool_hu`, `dfm13_tool_lb`, `dfm13_tool_lt`, `dfm13_tool_lv`, `dfm13_tool_sk`, `dfm13_tool_sl`, `dfm13_tool_sq`, `dfm13_tool_sr`, `simia_tau`, `areal_tau2`, `nemotron_agentic_v1_interactive`, `nemotron_agentic_v2_interactive`, `spreadsheet_rl`, `simia_officebench`, `crmarena_pro`, `crmarena`, `workbench`, `nemotron_calendar`, `nemotron_calendar_sched`, `nemotron_business_agent_ipi`, `if_nemotron_sysbench`, `if_nemotron_cfbench` the system prompt carries the task (tool
   schemas, policies, behaviour specs), so there it is prepended to the user message, separated by a
   blank line.
2. Prompt + response datasets: only the prompt is kept.
3. Pretraining-style datasets (task and solution in one document) are left out.
4. Repeated records of one task (several rollouts, several responses to one prompt) are collapsed to
   one row per (dataset, task id, language). The same question in different languages stays.
   A prompt whose exact text already appears earlier in the corpus (any source, in the order of the
   Sources table) is dropped as well: 407,340 rows.
5. Domains and languages with fewer than 10,000 rows are dropped. This repeats until nothing
   changes.

Dropped domains: none.
324 languages were dropped, with 521,798 rows between them.

To rebuild it, run `python src/combine.py` from the quantedo_datasets workspace. All source revisions,
and the affine corpus manifest, are pinned in its `datasets.toml`.

## Agent turns (swe and terminal)

In the `chungus` split the swe and terminal domains hold agent trajectories, not task statements:
each row is a whole trajectory in the `conversation` column, to be cut before one of its assistant
turns; the model reads the conversation up to the cut and writes the agent's next turn (its reasoning
and its next tool call or command). The task statements these two domains held before
(414,401 swe and 216,192 terminal rows) were taken out.

- swe: 67,074 OpenHands runs on 6.3k SWE-rebench tasks
  (`nebius/SWE-rebench-openhands-trajectories`), with their tool schemas. None comes from a repository
  in SWE-bench Multilingual.
- terminal: 139,403 Terminus-2 runs on Nemotron-Terminal's synthetic tasks
  (`nvidia/Nemotron-Terminal-Corpus`, its skill-based tasks only); runs whose task holds a
  Terminal-Bench instruction were left out.

The Ingot eval cuts each drawn trajectory before a seeded random assistant turn after the first,
among the turns whose prompt, rendered with Qwen3.8-27B's chat template, leaves 4,096 tokens of a
36,864-token context. Assistant turns keep their tool calls and drop their reasoning, as an agent
sends them back. Built by `scripts/build_agent_corpus.py` in the Ingot repository.

## Domains

| domain | rows |
|---|---|
| code | 2,511,875 |
| tool_calling | 1,268,561 |
| reasoning | 1,121,514 |
| translation | 1,085,335 |
| search | 983,671 |
| knowledge | 729,525 |
| reading | 476,446 |
| instruction_following | 440,309 |
| agent_dialogue | 380,953 |
| math | 347,821 |
| long_context | 322,268 |
| general_chat | 274,487 |
| formal_math | 140,323 |
| terminal | 139,403 |
| enterprise_ops | 119,908 |
| science | 102,796 |
| safety | 102,082 |
| swe | 67,074 |

## Languages

| language | rows |
|---|---|
| en | 7,162,278 |
| zh | 322,572 |
| ar | 211,198 |
| ru | 186,027 |
| ko | 126,619 |
| es | 117,016 |
| de | 107,278 |
| hi | 88,736 |
| fr | 88,272 |
| ja | 87,215 |
| pt | 83,789 |
| vi | 77,636 |
| it | 69,052 |
| tr | 64,089 |
| nl | 58,352 |
| te | 54,169 |
| fi | 52,523 |
| id | 52,104 |
| pl | 49,256 |
| ms | 46,364 |
| bn | 46,032 |
| sv | 45,338 |
| lt | 42,120 |
| mg | 41,340 |
| cs | 41,290 |
| el | 40,638 |
| he | 40,340 |
| si | 40,105 |
| fa | 39,185 |
| ro | 38,512 |
| sw | 38,328 |
| hu | 35,242 |
| ha | 34,266 |
| uk | 33,516 |
| sr | 33,485 |
| ne | 32,816 |
| am | 32,414 |
| ta | 30,520 |
| da | 30,264 |
| th | 30,090 |
| so | 29,440 |
| yo | 28,274 |
| bg | 27,779 |
| ky | 27,034 |
| sl | 26,839 |
| sk | 26,729 |
| lv | 26,588 |
| tl | 26,582 |
| et | 25,329 |
| ig | 22,474 |
| mr | 21,581 |
| sn | 21,055 |
| km | 21,021 |
| ny | 20,492 |
| pa | 19,949 |
| ur | 19,224 |
| ml | 18,652 |
| gu | 18,204 |
| is | 17,137 |
| hr | 17,009 |
| no | 16,358 |
| sq | 14,916 |
| eu | 14,857 |
| ti | 14,843 |
| zu | 14,497 |
| af | 14,040 |
| xh | 13,913 |
| my | 13,724 |
| ca | 13,678 |
| rw | 13,410 |
| bs | 13,340 |
| be | 12,438 |
| mk | 11,987 |
| ka | 11,848 |
| az | 11,701 |
| kn | 11,614 |
| mt | 11,198 |
| lb | 11,048 |
| ga | 10,953 |
| ps | 10,815 |
| gl | 10,588 |
| uz | 10,408 |
| as | 10,357 |
| tg | 10,042 |

## Source splits

| split | rows |
|---|---|
| train | 5,793,406 |
| test | 3,249,426 |
| validation | 669,686 |
| math | 162,692 |
| 80k | 80,359 |
| 8k | 37,217 |
| 4k | 37,145 |
| 16k | 37,031 |
| code | 31,960 |
| 32k | 30,717 |
| direct_generation | 28,145 |
| diversified_tasks | 19,332 |
| silver | 13,574 |
| original | 12,472 |
| mlqa.en.en.test | 11,587 |
| 128k | 7,577 |
| 64k | 7,577 |
| mlqa.en.vi.test | 5,495 |
| mlqa.vi.en.test | 5,489 |
| mlqa.vi.vi.test | 5,489 |
| mlqa.ar.en.test | 5,335 |
| mlqa.ar.ar.test | 5,334 |
| mlqa.en.ar.test | 5,332 |
| mlqa.en.es.test | 5,251 |
| mlqa.es.en.test | 5,250 |
| mlqa.es.es.test | 5,250 |
| mlqa.en.zh.test | 5,136 |
| mlqa.zh.en.test | 5,132 |
| mlqa.zh.zh.test | 5,132 |
| mlqa.en.hi.test | 4,918 |
| mlqa.hi.en.test | 4,918 |
| mlqa.hi.hi.test | 4,918 |
| mlqa.de.de.test | 4,516 |
| mlqa.de.en.test | 4,516 |
| mlqa.en.de.test | 4,515 |
| b2b | 2,140 |
| b2c | 2,139 |
| 256k | 2,081 |
| mlqa.ar.vi.test | 2,047 |
| mlqa.vi.ar.test | 2,046 |
| indicqa.gu | 2,017 |
| mlqa.es.vi.test | 2,017 |
| mlqa.vi.es.test | 2,012 |
| aze_Latn | 1,997 |
| ben_Beng | 1,997 |
| guj_Gujr | 1,997 |
| hun_Latn | 1,997 |
| ron_Latn | 1,997 |
| zho_Hans | 1,997 |
| afr_Latn | 1,996 |
| bel_Cyrl | 1,996 |
| ces_Latn | 1,996 |
| ell_Grek | 1,996 |
| eus_Latn | 1,996 |
| gle_Latn | 1,996 |
| heb_Hebr | 1,996 |
| ind_Latn | 1,996 |
| kan_Knda | 1,996 |
| khm_Khmr | 1,996 |
| kin_Latn | 1,996 |
| mal_Mlym | 1,996 |
| mya_Mymr | 1,996 |
| pan_Guru | 1,996 |
| pol_Latn | 1,996 |
| sin_Sinh | 1,996 |
| som_Latn | 1,996 |
| swa_Latn | 1,996 |
| tam_Taml | 1,996 |
| vie_Latn | 1,996 |
| yor_Latn | 1,996 |
| yue_Hant | 1,996 |
| arb_Arab | 1,995 |
| bos_Latn | 1,995 |
| bul_Cyrl | 1,995 |
| cat_Latn | 1,995 |
| est_Latn | 1,995 |
| fas_Arab | 1,995 |
| fil_Latn | 1,995 |
| fra-CA_Latn | 1,995 |
| hau_Latn | 1,995 |
| hin_Deva | 1,995 |
| ibo_Latn | 1,995 |
| isl_Latn | 1,995 |
| kat_Geor | 1,995 |
| kir_Cyrl | 1,995 |
| mar_Deva | 1,995 |
| mkd_Cyrl | 1,995 |
| nep_Deva | 1,995 |
| pus_Arab | 1,995 |
| rus_Cyrl | 1,995 |
| tel_Telu | 1,995 |
| tgk_Cyrl | 1,995 |
| tha_Thai | 1,995 |
| tir_Ethi | 1,995 |
| tur_Latn | 1,995 |
| ukr_Cyrl | 1,995 |
| urd_Arab | 1,995 |
| uzb_Latn | 1,995 |
| dan_Latn | 1,994 |
| deu_Latn | 1,994 |
| fin_Latn | 1,994 |
| ita_Latn | 1,994 |
| jpn_Jpan | 1,994 |
| kor_Hang | 1,994 |
| lav_Latn | 1,994 |
| lit_Latn | 1,994 |
| mlt_Latn | 1,994 |
| por-BR_Latn | 1,994 |
| sna_Latn | 1,994 |
| sqi_Latn | 1,994 |
| swe_Latn | 1,994 |
| xho_Latn | 1,994 |
| zho_Hant | 1,994 |
| amh_Ethi | 1,993 |
| glg_Latn | 1,993 |
| ltz_Latn | 1,993 |
| mlg_Latn | 1,993 |
| nld_Latn | 1,993 |
| slv_Latn | 1,993 |
| spa-MX_Latn | 1,993 |
| msa_Latn | 1,992 |
| nya_Latn | 1,992 |
| srp_Cyrl | 1,992 |
| zul_Latn | 1,992 |
| slk_Latn | 1,991 |
| por_Latn | 1,984 |
| spa_Latn | 1,981 |
| mlqa.ar.es.test | 1,978 |
| mlqa.es.ar.test | 1,978 |
| fra_Latn | 1,975 |
| srp_Latn | 1,957 |
| hrv_Latn | 1,952 |
| mlqa.hi.vi.test | 1,947 |
| mlqa.vi.hi.test | 1,947 |
| mlqa.es.zh.test | 1,946 |
| mlqa.zh.es.test | 1,945 |
| mlqa.vi.zh.test | 1,942 |
| mlqa.zh.vi.test | 1,940 |
| mlqa.ar.zh.test | 1,912 |
| mlqa.zh.ar.test | 1,912 |
| ar | 1,871 |
| en | 1,871 |
| es | 1,871 |
| eu | 1,871 |
| hi | 1,871 |
| id | 1,871 |
| my | 1,871 |
| ru | 1,871 |
| sw | 1,871 |
| te | 1,871 |
| zh | 1,871 |
| mlqa.ar.hi.test | 1,831 |
| mlqa.hi.ar.test | 1,831 |
| indicqa.ta | 1,804 |
| indicqa.as | 1,788 |
| mlqa.de.es.test | 1,775 |
| mlqa.es.de.test | 1,774 |
| mlqa.hi.zh.test | 1,767 |
| mlqa.zh.hi.test | 1,766 |
| indicqa.bn | 1,763 |
| indicqa.te | 1,734 |
| mlqa.es.hi.test | 1,723 |
| mlqa.hi.es.test | 1,723 |
| mlqa.de.vi.test | 1,675 |
| mlqa.vi.de.test | 1,672 |
| mlqa.ar.de.test | 1,649 |
| mlqa.de.ar.test | 1,648 |
| mlqa.de.zh.test | 1,621 |
| mlqa.zh.de.test | 1,619 |
| b2b_interactive | 1,600 |
| indicqa.mr | 1,600 |
| b2c_interactive | 1,599 |
| indicqa.ml | 1,587 |
| indicqa.hi | 1,547 |
| indicqa.pa | 1,539 |
| indicqa.kn | 1,517 |
| mlqa.de.hi.test | 1,430 |
| mlqa.hi.de.test | 1,430 |
| mlqa.en.en.validation | 1,145 |
| main | 680 |
| toxic | 655 |
| mlqa.ar.ar.validation | 517 |
| mlqa.ar.en.validation | 517 |
| mlqa.en.ar.validation | 514 |
| mlqa.de.de.validation | 512 |
| mlqa.de.en.validation | 512 |
| mlqa.en.de.validation | 510 |
| mlqa.en.vi.validation | 510 |
| mlqa.vi.en.validation | 510 |
| mlqa.vi.vi.validation | 510 |
| mlqa.en.hi.validation | 507 |
| mlqa.hi.en.validation | 507 |
| mlqa.hi.hi.validation | 507 |
| mlqa.en.zh.validation | 503 |
| mlqa.zh.en.validation | 503 |
| mlqa.zh.zh.validation | 503 |
| mlqa.es.en.validation | 499 |
| mlqa.es.es.validation | 499 |
| mlqa.en.es.validation | 498 |
| contrast | 379 |
| mlqa.ar.de.validation | 207 |
| mlqa.de.ar.validation | 207 |
| mlqa.de.es.validation | 196 |
| mlqa.es.de.validation | 195 |
| mlqa.de.zh.validation | 190 |
| mlqa.zh.de.validation | 190 |
| mlqa.es.vi.validation | 189 |
| mlqa.hi.zh.validation | 189 |
| mlqa.vi.es.validation | 189 |
| mlqa.zh.hi.validation | 189 |
| mlqa.ar.zh.validation | 188 |
| mlqa.es.hi.validation | 187 |
| mlqa.hi.es.validation | 187 |
| mlqa.zh.ar.validation | 187 |
| mlqa.ar.hi.validation | 186 |
| mlqa.hi.ar.validation | 186 |
| mlqa.vi.zh.validation | 183 |
| mlqa.zh.vi.validation | 183 |
| mlqa.de.vi.validation | 182 |
| mlqa.vi.de.validation | 182 |
| mlqa.hi.vi.validation | 177 |
| mlqa.vi.hi.validation | 177 |
| mlqa.ar.vi.validation | 163 |
| mlqa.de.hi.validation | 163 |
| mlqa.hi.de.validation | 163 |
| mlqa.vi.ar.validation | 162 |
| mlqa.ar.es.validation | 161 |
| mlqa.es.zh.validation | 161 |
| mlqa.zh.es.validation | 161 |
| mlqa.es.ar.validation | 160 |
| valid | 117 |
| hard | 1 |

## Sources

Every row comes from one of these datasets, pinned to the revision shown. Please cite and follow the
license of each one you use. Rows is how many rows the source contributes after the filters above.

| id | title | source | revision | license | rows |
|---|---|---|---|---|---|
| `affine` | Affine corpus | [data.affine.io](https://data.affine.io) (manifest `a24b55a25586c5ae`) | - | - | 56,557 |
| `no_robots` | No Robots | [HuggingFaceH4/no_robots](https://huggingface.co/datasets/HuggingFaceH4/no_robots) | `e6f9a4ac5c37` | cc-by-nc-4.0 | 9,947 |
| `wildchat` | WildChat-1M (shard 0) | [allenai/WildChat-1M](https://huggingface.co/datasets/allenai/WildChat-1M) | `7d6490e46228` | odc-by | 51,171 |
| `oasst2` | OpenAssistant oasst2 | [OpenAssistant/oasst2](https://huggingface.co/datasets/OpenAssistant/oasst2) | `179dd21fc551` | apache-2.0 | 13,651 |
| `arena_140k` | LMArena human preference 140k (shard 0) | [lmarena-ai/arena-human-preference-140k](https://huggingface.co/datasets/lmarena-ai/arena-human-preference-140k) | `6322995ab34d` | cc-by-4.0 | 17,380 |
| `arena_hard` | Arena-Hard-Auto v0.1 + v2.0 | [lmarena-ai/arena-hard-auto](https://huggingface.co/datasets/lmarena-ai/arena-hard-auto) | `15f3746e2143` | apache-2.0 | 1,248 |
| `writingprompts` | WritingPrompts (valid + test) | [euclaise/writingprompts](https://huggingface.co/datasets/euclaise/writingprompts) | `35f0aa359452` | mit | 10,894 |
| `systemchat` | SystemChat 1.1 | [abacusai/SystemChat-1.1](https://huggingface.co/datasets/abacusai/SystemChat-1.1) | `98dfec4b292c` | apache-2.0 | 19,590 |
| `webdev_arena` | WebDev Arena 10k | [lmarena-ai/webdev-arena-preference-10k](https://huggingface.co/datasets/lmarena-ai/webdev-arena-preference-10k) | `7c397e652ffb` | other | 6,708 |
| `aya` | Aya Dataset | [CohereLabs/aya_dataset](https://huggingface.co/datasets/CohereLabs/aya_dataset) | `f9ea04583f02` | apache-2.0 | 166,378 |
| `m_arenahard` | m-ArenaHard | [CohereLabs/m-ArenaHard](https://huggingface.co/datasets/CohereLabs/m-ArenaHard) | `ab393a96cd0b` | apache-2.0 | 11,000 |
| `global_mmlu` | Global-MMLU | [CohereLabs/Global-MMLU](https://huggingface.co/datasets/CohereLabs/Global-MMLU) | `0e619dbeb342` | apache-2.0 | 586,461 |
| `include44` | INCLUDE (base-44) | [CohereLabs/include-base-44](https://huggingface.co/datasets/CohereLabs/include-base-44) | `d2e1f6015f67` | apache-2.0 | 22,173 |
| `mgsm` | MGSM | [juletxara/mgsm](https://huggingface.co/datasets/juletxara/mgsm) | `b2f13d426afe` | cc-by-sa-4.0 | 2,750 |
| `belebele` | Belebele | [facebook/belebele](https://huggingface.co/datasets/facebook/belebele) | `7899cdfa4e1e` | cc-by-sa-4.0 | 81,000 |
| `wmt24pp` | WMT24++ | [google/wmt24pp](https://huggingface.co/datasets/google/wmt24pp) | `fd7405c06494` | apache-2.0 | 52,745 |
| `multi_if` | Multi-IF (turn 1) | [facebook/Multi-IF](https://huggingface.co/datasets/facebook/Multi-IF) | `0ab97ce0b45c` | cc-by-nc-2.0 | 3,673 |
| `coconot` | CoCoNot | [allenai/coconot](https://huggingface.co/datasets/allenai/coconot) | `2cbe16aabf90` | see dataset card | 12,851 |
| `or_bench` | OR-Bench | [bench-llm/or-bench](https://huggingface.co/datasets/bench-llm/or-bench) | `e36d8b80e818` | cc-by-4.0 | 81,015 |
| `beavertails` | BeaverTails 30k | [PKU-Alignment/BeaverTails](https://huggingface.co/datasets/PKU-Alignment/BeaverTails) | `8401fe609d28` | cc-by-nc-4.0 | 7,768 |
| `xstest` | XSTest | [Paul/XSTest](https://huggingface.co/datasets/Paul/XSTest) | `f600c994b256` | cc-by-4.0 | 448 |
| `supergpqa` | SuperGPQA | [m-a-p/SuperGPQA](https://huggingface.co/datasets/m-a-p/SuperGPQA) | `4430d4458112` | odc-by | 26,529 |
| `mmlu_pro` | MMLU-Pro | [TIGER-Lab/MMLU-Pro](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro) | `b189ec765aa7` | mit | 11,613 |
| `simpleqa` | SimpleQA | [basicv8vc/SimpleQA](https://huggingface.co/datasets/basicv8vc/SimpleQA) | `e319282ab125` | mit | 4,326 |
| `medqa` | MedQA (USMLE) | [GBaker/MedQA-USMLE-4-options](https://huggingface.co/datasets/GBaker/MedQA-USMLE-4-options) | `0fb93dd23a73` | cc-by-4.0 | 11,451 |
| `medmcqa` | MedMCQA (validation + test) | [openlifescienceai/medmcqa](https://huggingface.co/datasets/openlifescienceai/medmcqa) | `91c6572c4540` | apache-2.0 | 10,333 |
| `webinstruct` | WebInstruct-verified | [TIGER-Lab/WebInstruct-verified](https://huggingface.co/datasets/TIGER-Lab/WebInstruct-verified) | `3e8a350b3a93` | apache-2.0 | 223,911 |
| `multipl_e` | MultiPL-E | [nuprl/MultiPL-E](https://huggingface.co/datasets/nuprl/MultiPL-E) | `28441b6024e7` | mit | 12,667 |
| `mceval` | McEval (generation) | [Multilingual-Multimodal-NLP/McEval](https://huggingface.co/datasets/Multilingual-Multimodal-NLP/McEval) | `c4767fec950d` | cc-by-sa-4.0 | 2,007 |
| `bigcodebench` | BigCodeBench (v0.1.4, instruct) | [bigcode/bigcodebench](https://huggingface.co/datasets/bigcode/bigcodebench) | `b74c0d0bf70d` | apache-2.0 | 1,139 |
| `cruxeval` | CRUXEval (output prediction) | [cruxeval-org/cruxeval](https://huggingface.co/datasets/cruxeval-org/cruxeval) | `b96af0450242` | mit | 800 |
| `code_contests` | CodeContests (valid + test + train shard 0) | [deepmind/code_contests](https://huggingface.co/datasets/deepmind/code_contests) | `802411c3010c` | cc-by-4.0 | 624 |
| `omni_math` | Omni-MATH | [KbsdJames/Omni-MATH](https://huggingface.co/datasets/KbsdJames/Omni-MATH) | `40ba231d8f16` | apache-2.0 | 4,393 |
| `numina_proofs` | NuminaMath-1.5 proofs (shard 0) | [AI-MO/NuminaMath-1.5](https://huggingface.co/datasets/AI-MO/NuminaMath-1.5) | `1b05109f9e5c` | apache-2.0 | 90,216 |
| `gsm8k` | GSM8K (test) | [openai/gsm8k](https://huggingface.co/datasets/openai/gsm8k) | `740312add88f` | mit | 1,069 |
| `lean_workbook` | Lean Workbook | [internlm/Lean-Workbook](https://huggingface.co/datasets/internlm/Lean-Workbook) | `2e066e310b2c` | apache-2.0 | 140,214 |
| `drop` | DROP (validation) | [ucinlp/drop](https://huggingface.co/datasets/ucinlp/drop) | `95cda593fae7` | cc-by-sa-4.0 | 8,686 |
| `tablebench` | TableBench | [Multilingual-Multimodal-NLP/TableBench](https://huggingface.co/datasets/Multilingual-Multimodal-NLP/TableBench) | `a23c244f9cca` | apache-2.0 | 885 |
| `bbeh` | BIG-Bench Extra Hard | [BBEH/bbeh](https://huggingface.co/datasets/BBEH/bbeh) | `08e07a803851` | apache-2.0 | 4,513 |
| `bbh` | BIG-Bench Hard | [lukaemon/bbh](https://huggingface.co/datasets/lukaemon/bbh) | `982bb89fd795` | see dataset card | 6,507 |
| `musr` | MuSR | [TAUR-Lab/MuSR](https://huggingface.co/datasets/TAUR-Lab/MuSR) | `7c365b439a22` | cc-by-4.0 | 756 |
| `zebralogic` | ZebraLogic (multiple choice) | [WildEval/ZebraLogic](https://huggingface.co/datasets/WildEval/ZebraLogic) | `0a473f5a0054` | see dataset card | 3,259 |
| `longbench_v2` | LongBench v2 | [THUDM/LongBench-v2](https://huggingface.co/datasets/THUDM/LongBench-v2) | `2b48e494f2c7` | apache-2.0 | 503 |
| `babilong` | BABILong qa1-qa5 (8k, 64k) | [RMT-team/babilong](https://huggingface.co/datasets/RMT-team/babilong) | `ee0d588794c7` | see dataset card | 1,000 |
| `frames` | FRAMES | [google/frames-benchmark](https://huggingface.co/datasets/google/frames-benchmark) | `58d9fb6330f3` | apache-2.0 | 824 |
| `webwalker` | WebWalkerQA | [callanwu/WebWalkerQA](https://huggingface.co/datasets/callanwu/WebWalkerQA) | `c7ab3329a2a4` | apache-2.0 | 14,254 |
| `toolace` | ToolACE | [Team-ACE/ToolACE](https://huggingface.co/datasets/Team-ACE/ToolACE) | `6bda777c88d2` | apache-2.0 | 11,297 |
| `apigen_mt` | APIGen-MT 5k | [Salesforce/APIGen-MT-5k](https://huggingface.co/datasets/Salesforce/APIGen-MT-5k) | `abc4a517d67c` | cc-by-nc-4.0 | 4,924 |
| `search_xor_tydi` | XOR-TyDi QA (full) | [akariasai/xor_tydi_qa](https://huggingface.co/datasets/akariasai/xor_tydi_qa) | `bc9220f3643b` | see dataset card | 72,623 |
| `search_mkqa` | MKQA | [omai-research/mkqa](https://huggingface.co/datasets/omai-research/mkqa) | `9e5e724fc16b` | see dataset card | 170,596 |
| `search_mintaka` | Mintaka | [AmazonScience/mintaka](https://huggingface.co/datasets/AmazonScience/mintaka) | `fe3f1235e31b` | see dataset card | 178,080 |
| `search_hotpotqa` | HotpotQA (fullwiki) | [hotpotqa/hotpot_qa](https://huggingface.co/datasets/hotpotqa/hotpot_qa) | `1908d6afbbea` | cc-by-sa-4.0 | 105,248 |
| `search_2wikimultihop` | 2WikiMultihopQA | [framolfese/2WikiMultihopQA](https://huggingface.co/datasets/framolfese/2WikiMultihopQA) | `fe713bfbd1af` | see dataset card | 192,604 |
| `search_musique` | MuSiQue (answerable) | [dgslibisey/MuSiQue](https://huggingface.co/datasets/dgslibisey/MuSiQue) | `c8f4f8c9465f` | see dataset card | 22,314 |
| `search_mr_tydi` | Mr. TyDi | [castorini/mr-tydi](https://huggingface.co/datasets/castorini/mr-tydi) | `1d43c80218d0` | apache-2.0 | 21,864 |
| `search_triviaqa` | TriviaQA (questions) | [mandarjoshi/trivia_qa](https://huggingface.co/datasets/mandarjoshi/trivia_qa) | `0f7faf33a390` | unknown | 101,512 |
| `search_nq_open` | Natural Questions (open) | [google-research-datasets/nq_open](https://huggingface.co/datasets/google-research-datasets/nq_open) | `5dd9790a8300` | cc-by-sa-3.0 | 88,683 |
| `search_web_questions` | WebQuestions | [stanfordnlp/web_questions](https://huggingface.co/datasets/stanfordnlp/web_questions) | `0e473cbe21d1` | unknown | 5,810 |
| `search_strategyqa` | StrategyQA | [ChilleD/StrategyQA](https://huggingface.co/datasets/ChilleD/StrategyQA) | `705562638fe1` | mit | 2,289 |
| `search_deepsearchqa` | DeepSearchQA | [google/deepsearchqa](https://huggingface.co/datasets/google/deepsearchqa) | `b2623f865306` | apache-2.0 | 900 |
| `search_sealqa` | SealQA (Seal-0, Seal-Hard) | [vtllms/sealqa](https://huggingface.co/datasets/vtllms/sealqa) | `0c298f519c87` | apache-2.0 | 254 |
| `search_bamboogle` | Bamboogle | [chiayewken/bamboogle](https://huggingface.co/datasets/chiayewken/bamboogle) | `5787baaae24a` | see dataset card | 125 |
| `search_assistantbench` | AssistantBench | [AssistantBench/AssistantBench](https://huggingface.co/datasets/AssistantBench/AssistantBench) | `482cbbc0400f` | apache-2.0 | 214 |
| `search_freshqa_en` | FreshQA multilingual (English) | [SeaLLMs/FreshQA-multilingual](https://huggingface.co/datasets/SeaLLMs/FreshQA-multilingual) | `694ab7715bda` | see dataset card | 588 |
| `search_freshqa_zh` | FreshQA multilingual (Chinese) | [SeaLLMs/FreshQA-multilingual](https://huggingface.co/datasets/SeaLLMs/FreshQA-multilingual) | `694ab7715bda` | see dataset card | 599 |
| `search_freshqa_vi` | FreshQA multilingual (Vietnamese) | [SeaLLMs/FreshQA-multilingual](https://huggingface.co/datasets/SeaLLMs/FreshQA-multilingual) | `694ab7715bda` | see dataset card | 599 |
| `search_freshqa_th` | FreshQA multilingual (Thai) | [SeaLLMs/FreshQA-multilingual](https://huggingface.co/datasets/SeaLLMs/FreshQA-multilingual) | `694ab7715bda` | see dataset card | 599 |
| `search_freshqa_id` | FreshQA multilingual (Indonesian) | [SeaLLMs/FreshQA-multilingual](https://huggingface.co/datasets/SeaLLMs/FreshQA-multilingual) | `694ab7715bda` | see dataset card | 599 |
| `search_freshqa_ms` | FreshQA multilingual (Malay) | [SeaLLMs/FreshQA-multilingual](https://huggingface.co/datasets/SeaLLMs/FreshQA-multilingual) | `694ab7715bda` | see dataset card | 590 |
| `search_freshqa_km` | FreshQA multilingual (Khmer) | [SeaLLMs/FreshQA-multilingual](https://huggingface.co/datasets/SeaLLMs/FreshQA-multilingual) | `694ab7715bda` | see dataset card | 599 |
| `search_freshqa_lo` | FreshQA multilingual (Lao) | [SeaLLMs/FreshQA-multilingual](https://huggingface.co/datasets/SeaLLMs/FreshQA-multilingual) | `694ab7715bda` | see dataset card | 0 |
| `lc_longalign` | LongAlign-10k | [zai-org/LongAlign-10k](https://huggingface.co/datasets/zai-org/LongAlign-10k) | `12f17c4baff1` | see dataset card | 9,888 |
| `lc_longreward` | LongReward-10k (SFT queries) | [zai-org/LongReward-10k](https://huggingface.co/datasets/zai-org/LongReward-10k) | `9d5f9b1f8e2b` | apache-2.0 | 9,999 |
| `lc_longcite` | LongCite-45k | [zai-org/LongCite-45k](https://huggingface.co/datasets/zai-org/LongCite-45k) | `b776b01faf6e` | apache-2.0 | 44,597 |
| `lc_longbench_v1` | LongBench v1 + LongBench-E | [Xnhyacinth/LongBench](https://huggingface.co/datasets/Xnhyacinth/LongBench) | `944462f8d747` | mit | 8,021 |
| `lc_loogle_qa` | LooGLE QA | [bigai-nlco/LooGLE](https://huggingface.co/datasets/bigai-nlco/LooGLE) | `4b50b4cb9333` | cc-by-sa-4.0 | 3,041 |
| `lc_loogle_cloze` | LooGLE cloze | [bigai-nlco/LooGLE](https://huggingface.co/datasets/bigai-nlco/LooGLE) | `4b50b4cb9333` | cc-by-sa-4.0 | 2,880 |
| `lc_loogle_summ` | LooGLE summarization | [bigai-nlco/LooGLE](https://huggingface.co/datasets/bigai-nlco/LooGLE) | `4b50b4cb9333` | cc-by-sa-4.0 | 516 |
| `lc_longbench_pro` | LongBench-Pro | [caskcsg/LongBench-Pro](https://huggingface.co/datasets/caskcsg/LongBench-Pro) | `4b64bea870ba` | see dataset card | 1,500 |
| `lc_libra` | LIBRA (Russian long context) | [ai-forever/LIBRA](https://huggingface.co/datasets/ai-forever/LIBRA) | `10d668ab4416` | mit | 14,725 |
| `lc_babilong_qa6_10` | BABILong qa6-qa10 (4k-128k) | [RMT-team/babilong](https://huggingface.co/datasets/RMT-team/babilong) | `ee0d588794c7` | see dataset card | 3,000 |
| `lc_babilong_1k` | BABILong 1k samples qa1-qa5 (4k-128k) | [RMT-team/babilong-1k-samples](https://huggingface.co/datasets/RMT-team/babilong-1k-samples) | `fc4d1a584dfc` | see dataset card | 28,976 |
| `lc_ruler` | RULER (4k, 8k, 16k) | [simonjegou/ruler](https://huggingface.co/datasets/simonjegou/ruler) | `24adceac8a0e` | see dataset card | 19,500 |
| `lc_ruler_long` | RULER-style tasks (4k-256k) | [zechen-nlp/ruler-long](https://huggingface.co/datasets/zechen-nlp/ruler-long) | `b37032cd3c76` | other | 39,855 |
| `lc_multilingual_niah` | Multilingual Needle-in-a-Haystack | [ameyhengle/Multilingual-Needle-in-a-Haystack](https://huggingface.co/datasets/ameyhengle/Multilingual-Needle-in-a-Haystack) | `ec4c18d60b7e` | see dataset card | 67,014 |
| `lc_narrativeqa_train` | NarrativeQA full stories (train) | [deepmind/narrativeqa](https://huggingface.co/datasets/deepmind/narrativeqa) | `2e643e736394` | apache-2.0 | 32,507 |
| `lc_narrativeqa_eval` | NarrativeQA full stories (validation + test) | [deepmind/narrativeqa](https://huggingface.co/datasets/deepmind/narrativeqa) | `2e643e736394` | apache-2.0 | 13,904 |
| `lc_clongeval_qa` | CLongEval QA (story QA, table querying) | [zexuanqiu22/CLongEval](https://huggingface.co/datasets/zexuanqiu22/CLongEval) | `178d74d88f52` | see dataset card | 2,091 |
| `lc_clongeval_memory` | CLongEval long conversation memory | [zexuanqiu22/CLongEval](https://huggingface.co/datasets/zexuanqiu22/CLongEval) | `178d74d88f52` | see dataset card | 1,067 |
| `lc_clongeval_summ` | CLongEval story summarization | [zexuanqiu22/CLongEval](https://huggingface.co/datasets/zexuanqiu22/CLongEval) | `178d74d88f52` | see dataset card | 1,000 |
| `lc_clongeval_labeling` | CLongEval stacked news labeling | [zexuanqiu22/CLongEval](https://huggingface.co/datasets/zexuanqiu22/CLongEval) | `178d74d88f52` | see dataset card | 1,005 |
| `lc_clongeval_typo` | CLongEval stacked typo detection | [zexuanqiu22/CLongEval](https://huggingface.co/datasets/zexuanqiu22/CLongEval) | `178d74d88f52` | see dataset card | 1,000 |
| `lc_clongeval_kpr` | CLongEval key-passage retrieval | [zexuanqiu22/CLongEval](https://huggingface.co/datasets/zexuanqiu22/CLongEval) | `178d74d88f52` | see dataset card | 1,100 |
| `lc_infinitebench` | InfiniteBench | [xinrongzhang2022/InfiniteBench](https://huggingface.co/datasets/xinrongzhang2022/InfiniteBench) | `90f039433361` | see dataset card | 3,945 |
| `lc_longalpaca` | LongAlpaca-12k (long rows) | [Yukang/LongAlpaca-12k](https://huggingface.co/datasets/Yukang/LongAlpaca-12k) | `46dce924ed87` | see dataset card | 8,766 |
| `lc_longseal` | LongSeal | [vtllms/sealqa](https://huggingface.co/datasets/vtllms/sealqa) | `0c298f519c87` | apache-2.0 | 254 |
| `toucan_p1` | Toucan MCP tool use (1/4) | [Agent-Ark/Toucan-1.5M](https://huggingface.co/datasets/Agent-Ark/Toucan-1.5M) | `0df3cf37f2ab` | apache-2.0 | 110,574 |
| `toucan_p2` | Toucan MCP tool use (2/4) | [Agent-Ark/Toucan-1.5M](https://huggingface.co/datasets/Agent-Ark/Toucan-1.5M) | `0df3cf37f2ab` | apache-2.0 | 187,442 |
| `toucan_p3` | Toucan MCP tool use (3/4) | [Agent-Ark/Toucan-1.5M](https://huggingface.co/datasets/Agent-Ark/Toucan-1.5M) | `0df3cf37f2ab` | apache-2.0 | 131,368 |
| `toucan_p4` | Toucan MCP tool use (4/4) | [Agent-Ark/Toucan-1.5M](https://huggingface.co/datasets/Agent-Ark/Toucan-1.5M) | `0df3cf37f2ab` | apache-2.0 | 188,264 |
| `xlam_apigen` | xLAM + Synth-APIGen function calling | [argilla/apigen-function-calling](https://huggingface.co/datasets/argilla/apigen-function-calling) | `170a8a7e0832` | cc-by-4.0 | 101,290 |
| `toolbench_queries` | ToolBench queries | [Maurus/ToolBench](https://huggingface.co/datasets/Maurus/ToolBench) | `075bdaa04006` | see dataset card | 87,319 |
| `dolci_tool_use` | Dolci tool use (Olmo 3) | [allenai/Dolci-Instruct-SFT-Tool-Use](https://huggingface.co/datasets/allenai/Dolci-Instruct-SFT-Tool-Use) | `dc042846f0f2` | see dataset card | 226,158 |
| `hammerbench_zh` | HammerBench (Chinese) | [MadeAgents/HammerBench](https://huggingface.co/datasets/MadeAgents/HammerBench) | `18b4f4ea47e8` | apache-2.0 | 13,054 |
| `turkish_fc` | Turkish function calling | [atasoglu/turkish-function-calling-20k](https://huggingface.co/datasets/atasoglu/turkish-function-calling-20k) | `aff155df2ed8` | mit | 21,992 |
| `glaive_fc_v2` | Glaive function calling v2 | [hiyouga/glaive-function-calling-v2-sharegpt](https://huggingface.co/datasets/hiyouga/glaive-function-calling-v2-sharegpt) | `5d941e9da462` | apache-2.0 | 42,844 |
| `glaive_fc_ko` | Glaive function calling (Korean) | [heegyu/glaive-function-calling-v2-ko](https://huggingface.co/datasets/heegyu/glaive-function-calling-v2-ko) | `5d65af5898ec` | see dataset card | 14,584 |
| `japanese_fc` | Function calling (Japanese) | [DataPilot/Function-Calling-Japanese-Dataset](https://huggingface.co/datasets/DataPilot/Function-Calling-Japanese-Dataset) | `34e5d18e5c18` | odc-by | 6,917 |
| `arabic_fc` | Arabic function calling | [HeshamHaroon/Arabic_Function_Calling](https://huggingface.co/datasets/HeshamHaroon/Arabic_Function_Calling) | `ec4d3302f6b2` | apache-2.0 | 42,461 |
| `toolmind_graphsyn` | ToolMind graph-synthesized | [Nanbeige/ToolMind](https://huggingface.co/datasets/Nanbeige/ToolMind) | `8020ed1c03c3` | apache-2.0 | 29,162 |
| `dfm13_tool_be` | DFM13 tool dialogue (be) | [schneiderkamplab/dfm13-multilingual-tool-dialogue-be](https://huggingface.co/datasets/schneiderkamplab/dfm13-multilingual-tool-dialogue-be) | `08136544d7a3` | see dataset card | 2,691 |
| `dfm13_tool_bg` | DFM13 tool dialogue (bg) | [schneiderkamplab/dfm13-multilingual-tool-dialogue-bg](https://huggingface.co/datasets/schneiderkamplab/dfm13-multilingual-tool-dialogue-bg) | `1ba23b0216c7` | see dataset card | 2,850 |
| `dfm13_tool_bs` | DFM13 tool dialogue (bs) | [schneiderkamplab/dfm13-multilingual-tool-dialogue-bs](https://huggingface.co/datasets/schneiderkamplab/dfm13-multilingual-tool-dialogue-bs) | `39a3eb33bbc3` | see dataset card | 2,804 |
| `dfm13_tool_fa` | DFM13 tool dialogue (fa) | [schneiderkamplab/dfm13-multilingual-tool-dialogue-fa](https://huggingface.co/datasets/schneiderkamplab/dfm13-multilingual-tool-dialogue-fa) | `f3a7d914b9ab` | see dataset card | 3,188 |
| `dfm13_tool_hr` | DFM13 tool dialogue (hr) | [schneiderkamplab/dfm13-multilingual-tool-dialogue-hr](https://huggingface.co/datasets/schneiderkamplab/dfm13-multilingual-tool-dialogue-hr) | `cc3274bf6781` | see dataset card | 3,031 |
| `dfm13_tool_hu` | DFM13 tool dialogue (hu) | [schneiderkamplab/dfm13-multilingual-tool-dialogue-hu](https://huggingface.co/datasets/schneiderkamplab/dfm13-multilingual-tool-dialogue-hu) | `31c0f4b5180f` | see dataset card | 3,067 |
| `dfm13_tool_lb` | DFM13 tool dialogue (lb) | [schneiderkamplab/dfm13-multilingual-tool-dialogue-lb](https://huggingface.co/datasets/schneiderkamplab/dfm13-multilingual-tool-dialogue-lb) | `de00fd102024` | see dataset card | 8,530 |
| `dfm13_tool_lt` | DFM13 tool dialogue (lt) | [schneiderkamplab/dfm13-multilingual-tool-dialogue-lt](https://huggingface.co/datasets/schneiderkamplab/dfm13-multilingual-tool-dialogue-lt) | `e02e4ee920ed` | see dataset card | 3,410 |
| `dfm13_tool_lv` | DFM13 tool dialogue (lv) | [schneiderkamplab/dfm13-multilingual-tool-dialogue-lv](https://huggingface.co/datasets/schneiderkamplab/dfm13-multilingual-tool-dialogue-lv) | `bec8f281de5a` | see dataset card | 3,359 |
| `dfm13_tool_sk` | DFM13 tool dialogue (sk) | [schneiderkamplab/dfm13-multilingual-tool-dialogue-sk](https://huggingface.co/datasets/schneiderkamplab/dfm13-multilingual-tool-dialogue-sk) | `b6b7a0273a4b` | see dataset card | 3,106 |
| `dfm13_tool_sl` | DFM13 tool dialogue (sl) | [schneiderkamplab/dfm13-multilingual-tool-dialogue-sl](https://huggingface.co/datasets/schneiderkamplab/dfm13-multilingual-tool-dialogue-sl) | `cae873f21493` | see dataset card | 2,954 |
| `dfm13_tool_sq` | DFM13 tool dialogue (sq) | [schneiderkamplab/dfm13-multilingual-tool-dialogue-sq](https://huggingface.co/datasets/schneiderkamplab/dfm13-multilingual-tool-dialogue-sq) | `204ee3fcb2b7` | see dataset card | 2,812 |
| `dfm13_tool_sr` | DFM13 tool dialogue (sr) | [schneiderkamplab/dfm13-multilingual-tool-dialogue-sr](https://huggingface.co/datasets/schneiderkamplab/dfm13-multilingual-tool-dialogue-sr) | `34faa5a2f4f9` | see dataset card | 2,758 |
| `simia_tau` | Simia tau airline/retail | [Simia-Agent/Simia-Tau-SFT-90k-Hermes](https://huggingface.co/datasets/Simia-Agent/Simia-Tau-SFT-90k-Hermes) | `aacd83f00181` | see dataset card | 72,709 |
| `areal_tau2` | AReaL tau2 SFT dialogues | [inclusionAI/AReaL-tau2-data](https://huggingface.co/datasets/inclusionAI/AReaL-tau2-data) | `86971dc03da6` | apache-2.0 | 2,331 |
| `nemotron_agentic_v1_interactive` | Nemotron Agentic v1 interactive agent | [nvidia/Nemotron-Agentic-v1](https://huggingface.co/datasets/nvidia/Nemotron-Agentic-v1) | `650d590978ca` | cc-by-4.0 | 15,443 |
| `nemotron_agentic_v2_interactive` | Nemotron SFT Agentic v2 interactive agent | [nvidia/Nemotron-SFT-Agentic-v2](https://huggingface.co/datasets/nvidia/Nemotron-SFT-Agentic-v2) | `7c804833427f` | cc-by-4.0, apache-2.0, mit | 278,866 |
| `spreadsheet_rl` | Spreadsheet-RL | [Spreadsheet-RL/Spreadsheet-RL](https://huggingface.co/datasets/Spreadsheet-RL/Spreadsheet-RL) | `6f274cd4cbc2` | cc-by-sa-4.0 | 9,138 |
| `simia_officebench` | Simia OfficeBench | [Simia-Agent/Simia-OfficeBench-SFT-30k](https://huggingface.co/datasets/Simia-Agent/Simia-OfficeBench-SFT-30k) | `c9226cc16d46` | see dataset card | 29,585 |
| `crmarena_pro` | CRMArena-Pro | [Salesforce/CRMArenaPro](https://huggingface.co/datasets/Salesforce/CRMArenaPro) | `8c055f5b45f1` | cc-by-nc-4.0 | 7,478 |
| `crmarena` | CRMArena | [Salesforce/CRMArena](https://huggingface.co/datasets/Salesforce/CRMArena) | `15b168599570` | cc-by-nc-4.0 | 1,170 |
| `workbench` | WorkBench workplace assistant | [nvidia/Nemotron-RL-agent-workplace_assistant](https://huggingface.co/datasets/nvidia/Nemotron-RL-agent-workplace_assistant) | `f674d9bba178` | cc-by-4.0 | 1,800 |
| `enron_email_qa` | Enron inbox questions (ART-E) | [corbt/enron_emails_sample_questions](https://huggingface.co/datasets/corbt/enron_emails_sample_questions) | `abc84674cefc` | see dataset card | 52,776 |
| `nemotron_calendar` | Nemotron calendar assistant | [nvidia/Nemotron-RL-Instruction-Following-Calendar-v2](https://huggingface.co/datasets/nvidia/Nemotron-RL-Instruction-Following-Calendar-v2) | `7c88e10b7539` | cc-by-4.0 | 9,915 |
| `nemotron_calendar_sched` | Nemotron calendar scheduling agent | [nvidia/Nemotron-RL-agent-calendar_scheduling](https://huggingface.co/datasets/nvidia/Nemotron-RL-agent-calendar_scheduling) | `8b62cf67e53d` | cc-by-4.0 | 4,000 |
| `nemotron_business_agent_ipi` | Nemotron business-tool agent tasks | [nvidia/Nemotron-RL-Agentic-Indirect-Prompt-Injection-v1](https://huggingface.co/datasets/nvidia/Nemotron-RL-Agentic-Indirect-Prompt-Injection-v1) | `d738d4f361cc` | cc-by-4.0 | 1,272 |
| `ba_calendar` | BA-Calendar meeting scheduling | [microsoft/ba-calendar](https://huggingface.co/datasets/microsoft/ba-calendar) | `ec3ceadc516c` | mit | 2,000 |
| `swe_rebench_v2` | SWE-rebench V2 | [nebius/SWE-rebench-V2](https://huggingface.co/datasets/nebius/SWE-rebench-V2) | `10483de0f50f` | cc-by-4.0 | 0 |
| `swe_rebench_v2_prs` | SWE-rebench V2 PRs | [nebius/SWE-rebench-V2-PRs](https://huggingface.co/datasets/nebius/SWE-rebench-V2-PRs) | `fbf0ecf50f26` | cc-by-4.0 | 0 |
| `swe_rebench_v1` | SWE-rebench | [nebius/SWE-rebench](https://huggingface.co/datasets/nebius/SWE-rebench) | `89cdfbab4ab1` | cc-by-4.0 | 0 |
| `swe_smith_java` | SWE-smith Java | [SWE-bench/SWE-smith-java](https://huggingface.co/datasets/SWE-bench/SWE-smith-java) | `1172df9919a8` | see dataset card | 0 |
| `swe_smith_js` | SWE-smith JavaScript | [SWE-bench/SWE-smith-js](https://huggingface.co/datasets/SWE-bench/SWE-smith-js) | `d6aeb41ba9fb` | see dataset card | 0 |
| `swe_smith_ts` | SWE-smith TypeScript | [SWE-bench/SWE-smith-ts](https://huggingface.co/datasets/SWE-bench/SWE-smith-ts) | `c243d86f112d` | see dataset card | 0 |
| `swe_smith_cpp` | SWE-smith C++ | [SWE-bench/SWE-smith-cpp](https://huggingface.co/datasets/SWE-bench/SWE-smith-cpp) | `b1554a5f1260` | see dataset card | 0 |
| `swe_smith_rs` | SWE-smith Rust | [SWE-bench/SWE-smith-rs](https://huggingface.co/datasets/SWE-bench/SWE-smith-rs) | `1ae20d63edd6` | see dataset card | 0 |
| `swe_smith_go` | SWE-smith Go | [SWE-bench/SWE-smith-go](https://huggingface.co/datasets/SWE-bench/SWE-smith-go) | `d2f6ecc2cf8a` | mit | 0 |
| `swe_smith_py` | SWE-smith Python | [SWE-bench/SWE-smith](https://huggingface.co/datasets/SWE-bench/SWE-smith) | `ea6d7173829c` | mit | 0 |
| `swe_multi_swe_rl` | Multi-SWE-RL (2024 batch) | [PrimeIntellect/Multi-SWE-RL-Reupload](https://huggingface.co/datasets/PrimeIntellect/Multi-SWE-RL-Reupload) | `dbf7ae8a407d` | other | 0 |
| `swe_multi_swe_rl_2025` | Multi-SWE-RL (2025 batch) | [ByteDance-Seed/Multi-SWE-RL](https://huggingface.co/datasets/ByteDance-Seed/Multi-SWE-RL) | `9777648932da` | other | 0 |
| `swe_live_multilang` | SWE-bench-Live MultiLang | [SWE-bench-Live/MultiLang](https://huggingface.co/datasets/SWE-bench-Live/MultiLang) | `3638632e8153` | mit | 0 |
| `swe_live` | SWE-bench-Live | [SWE-bench-Live/SWE-bench-Live](https://huggingface.co/datasets/SWE-bench-Live/SWE-bench-Live) | `b51a86422e10` | mit | 0 |
| `swe_bench_pro` | SWE-bench Pro (public) | [ScaleAI/SWE-bench_Pro](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro) | `2d52cb3df914` | see dataset card | 0 |
| `swe_polybench` | SWE-PolyBench | [AmazonScience/SWE-PolyBench](https://huggingface.co/datasets/AmazonScience/SWE-PolyBench) | `d56445f9940e` | mit | 0 |
| `swe_sharp` | SWE-Sharp-Bench | [microsoft/SWE-Sharp-Bench](https://huggingface.co/datasets/microsoft/SWE-Sharp-Bench) | `41e599424ff9` | cdla-permissive-2.0 | 0 |
| `swe_fixer` | SWE-Fixer 110K | [internlm/SWE-Fixer-Train-110K](https://huggingface.co/datasets/internlm/SWE-Fixer-Train-110K) | `44504294da75` | see dataset card | 0 |
| `swe_gym` | SWE-Gym | [SWE-Gym/SWE-Gym](https://huggingface.co/datasets/SWE-Gym/SWE-Gym) | `bb94ed9e39bb` | mit | 0 |
| `swe_r2e_gym` | R2E-Gym V1 | [R2E-Gym/R2E-Gym-V1](https://huggingface.co/datasets/R2E-Gym/R2E-Gym-V1) | `903d405799ac` | apache-2.0 | 0 |
| `swe_multilingual` | SWE-bench Multilingual | [SWE-bench/SWE-bench_Multilingual](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multilingual) | `846e647b9f33` | mit | 0 |
| `swe_omnigirl` | OmniGIRL | [Deep-Software-Analytics/OmniGIRL](https://huggingface.co/datasets/Deep-Software-Analytics/OmniGIRL) | `2c15ae7c64d5` | cc-by-nc-sa-4.0 | 0 |
| `swe_bench_c` | SWE-bench-c | [SWE-bench-c/SWE-bench-c](https://huggingface.co/datasets/SWE-bench-c/SWE-bench-c) | `417f0208132e` | mit | 0 |
| `swe_factory_gym` | SWE-Factory Gym | [SWE-Factory/SWE-Factory-Gym](https://huggingface.co/datasets/SWE-Factory/SWE-Factory-Gym) | `c31daaecf6cd` | mit | 0 |
| `term_nemotron_synth` | Nemotron-Terminal synthetic tasks | [nvidia/Nemotron-Terminal-Corpus](https://huggingface.co/datasets/nvidia/Nemotron-Terminal-Corpus) | `a1667c4ffdad` | cc-by-4.0 | 0 |
| `term_nemotron_adapters` | Nemotron-Terminal dataset adapters | [nvidia/Nemotron-Terminal-Corpus](https://huggingface.co/datasets/nvidia/Nemotron-Terminal-Corpus) | `a1667c4ffdad` | cc-by-4.0 | 194,652 |
| `term_facet` | FACET-Terminal Tasks | [FACET-Terminal/FACET-Terminal-Tasks-6k](https://huggingface.co/datasets/FACET-Terminal/FACET-Terminal-Tasks-6k) | `b2d02645932e` | apache-2.0 | 0 |
| `term_nl2sh` | NL2SH-ALFA | [westenfelder/NL2SH-ALFA](https://huggingface.co/datasets/westenfelder/NL2SH-ALFA) | `a99cb5784cf5` | mit | 0 |
| `term_terminalworld` | TerminalWorld | [EuniAI/TerminalWorld](https://huggingface.co/datasets/EuniAI/TerminalWorld) | `dda7c099cc07` | cc-by-4.0 | 0 |
| `term_shell_tasks` | Shell tasks | [deathbyknowledge/shell-tasks](https://huggingface.co/datasets/deathbyknowledge/shell-tasks) | `194bcfc08c79` | see dataset card | 0 |
| `term_bashbench2` | BashBench2 | [Eccentricity/bashbench2](https://huggingface.co/datasets/Eccentricity/bashbench2) | `13e19f9c2c91` | cc-by-sa-4.0 | 0 |
| `term_tb_pro` | Terminal-Bench Pro (public) | [alibabagroup/terminal-bench-pro](https://huggingface.co/datasets/alibabagroup/terminal-bench-pro) | `b79dec3e67ac` | apache-2.0 | 0 |
| `term_cybergym` | CyberGym | [sunblaze-ucb/cybergym](https://huggingface.co/datasets/sunblaze-ucb/cybergym) | `bde190ded494` | see dataset card | 0 |
| `term_lhtb` | Long-Horizon Terminal-Bench | [IntelligenceLab/Long-Horizon-Terminal-Bench](https://huggingface.co/datasets/IntelligenceLab/Long-Horizon-Terminal-Bench) | `21458ac18bd0` | apache-2.0 | 0 |
| `rs_hellaswagx` | HellaSwag-X (20 EU languages) | [Eurolingua/hellaswagx](https://huggingface.co/datasets/Eurolingua/hellaswagx) | `c38911a20475` | mit | 200,801 |
| `rs_hellaswag` | HellaSwag | [Rowan/hellaswag](https://huggingface.co/datasets/Rowan/hellaswag) | `218ec52e09a7` | see dataset card | 59,940 |
| `rs_puzzleclone` | PuzzleClone | [hithink-ai/PuzzleClone](https://huggingface.co/datasets/hithink-ai/PuzzleClone) | `a1755b078608` | apache-2.0 | 83,630 |
| `rs_logiqa2_en` | LogiQA 2.0 (English) | [datatune/LogiQA2.0](https://huggingface.co/datasets/datatune/LogiQA2.0) | `7dd2d321373e` | see dataset card | 14,349 |
| `rs_logiqa2_zh` | LogiQA 2.0 (Chinese) | [datatune/LogiQA2.0](https://huggingface.co/datasets/datatune/LogiQA2.0) | `7dd2d321373e` | see dataset card | 15,230 |
| `rs_xstorycloze` | XStoryCloze | [juletxara/xstory_cloze](https://huggingface.co/datasets/juletxara/xstory_cloze) | `c4c2d88a1ec8` | cc-by-sa-4.0 | 20,581 |
| `rs_planbench` | PlanBench | [tasksource/planbench](https://huggingface.co/datasets/tasksource/planbench) | `653dcebd2120` | see dataset card | 11,012 |
| `rs_winogrande` | WinoGrande (XL) | [allenai/winogrande](https://huggingface.co/datasets/allenai/winogrande) | `01e74176c635` | see dataset card | 43,428 |
| `rs_commonsenseqa` | CommonsenseQA | [tau/commonsense_qa](https://huggingface.co/datasets/tau/commonsense_qa) | `94630fe30dad` | mit | 12,102 |
| `rs_social_iqa` | Social IQa | [allenai/social_i_qa](https://huggingface.co/datasets/allenai/social_i_qa) | `537a2ec8ec56` | see dataset card | 35,311 |
| `rs_piqa` | PIQA | [ybisk/piqa](https://huggingface.co/datasets/ybisk/piqa) | `142c51238b3c` | see dataset card | 21,027 |
| `rs_global_piqa` | Global PIQA (non-parallel) | [mrlbenchmarks/global-piqa-nonparallel](https://huggingface.co/datasets/mrlbenchmarks/global-piqa-nonparallel) | `6777742fa363` | cc-by-sa-4.0 | 9,796 |
| `rs_global_piqa_parallel` | Global PIQA (parallel) | [mrlbenchmarks/global-piqa-parallel](https://huggingface.co/datasets/mrlbenchmarks/global-piqa-parallel) | `b0b18516a8bc` | cc-by-sa-4.0 | 9,989 |
| `rs_xcopa` | XCOPA | [cambridgeltl/xcopa](https://huggingface.co/datasets/cambridgeltl/xcopa) | `042f78955ba4` | cc-by-4.0 | 5,400 |
| `rs_xwinograd` | XWinograd | [Muennighoff/xwinograd](https://huggingface.co/datasets/Muennighoff/xwinograd) | `90b619ef5278` | cc-by-4.0 | 4,449 |
| `rs_proofwriter` | ProofWriter | [tasksource/proofwriter](https://huggingface.co/datasets/tasksource/proofwriter) | `ee4d22d49b84` | see dataset card | 545,382 |
| `rs_travelplanner` | TravelPlanner (sole-planning) | [osunlp/TravelPlanner](https://huggingface.co/datasets/osunlp/TravelPlanner) | `8736504ecfc3` | cc-by-4.0 | 1,225 |
| `rs_reclor` | ReClor | [tasksource/reclor](https://huggingface.co/datasets/tasksource/reclor) | `0414b39bfc39` | other | 350 |
| `rs_folio` | FOLIO | [tasksource/folio](https://huggingface.co/datasets/tasksource/folio) | `295b95fb4fe9` | cc | 1,204 |
| `rs_autologi` | AutoLogi | [qzhu/AutoLogi](https://huggingface.co/datasets/qzhu/AutoLogi) | `7ea358389896` | apache-2.0 | 2,458 |
| `if_multi_constraints` | IF multi-constraints (up to 5) | [allenai/IF_multi_constraints_upto5](https://huggingface.co/datasets/allenai/IF_multi_constraints_upto5) | `2e3a77407b7f` | odc-by | 95,367 |
| `if_marco_mif` | Marco-Bench-MIF | [ATH-MaaS/Marco-Bench-MIF](https://huggingface.co/datasets/ATH-MaaS/Marco-Bench-MIF) | `7488394adb46` | apache-2.0 | 17,231 |
| `if_multi_ifeval_300` | MultiIFEval (300+ languages) | [danish-foundation-models/multi-ifeval](https://huggingface.co/datasets/danish-foundation-models/multi-ifeval) | `1c1bc2ba1b2f` | cc-by-nc-sa-4.0 | 45,732 |
| `if_nemotron_so_v2` | Nemotron Structured Outputs v2 (single message) | [nvidia/Nemotron-RL-Instruction-Following-Structured-Outputs-v2](https://huggingface.co/datasets/nvidia/Nemotron-RL-Instruction-Following-Structured-Outputs-v2) | `b0187e180294` | cc-by-4.0 | 18,552 |
| `if_nemotron_so_v2_pair` | Nemotron Structured Outputs v2 (schema + document) | [nvidia/Nemotron-RL-Instruction-Following-Structured-Outputs-v2](https://huggingface.co/datasets/nvidia/Nemotron-RL-Instruction-Following-Structured-Outputs-v2) | `b0187e180294` | cc-by-4.0 | 24,299 |
| `if_nemotron_so_v2_multistep` | Nemotron Structured Outputs v2 (multi-step, turn 1) | [nvidia/Nemotron-RL-Instruction-Following-Structured-Outputs-v2](https://huggingface.co/datasets/nvidia/Nemotron-RL-Instruction-Following-Structured-Outputs-v2) | `b0187e180294` | cc-by-4.0 | 4,626 |
| `if_nemotron_so_v2_tools` | Nemotron Structured Outputs v2 (tool extraction) | [nvidia/Nemotron-RL-Instruction-Following-Structured-Outputs-v2](https://huggingface.co/datasets/nvidia/Nemotron-RL-Instruction-Following-Structured-Outputs-v2) | `b0187e180294` | cc-by-4.0 | 5,261 |
| `if_nemotron_so_v2_tools_sys` | Nemotron Structured Outputs v2 (tool extraction, with instruction) | [nvidia/Nemotron-RL-Instruction-Following-Structured-Outputs-v2](https://huggingface.co/datasets/nvidia/Nemotron-RL-Instruction-Following-Structured-Outputs-v2) | `b0187e180294` | cc-by-4.0 | 3,522 |
| `if_nemotron_wildchat_if` | Nemotron RL instruction following | [nvidia/Nemotron-RL-instruction_following](https://huggingface.co/datasets/nvidia/Nemotron-RL-instruction_following) | `bcdec57a62a1` | odc-by | 46,391 |
| `if_nemotron_sysbench` | Nemotron SysBench | [nvidia/Nemotron-RL-SysBench-v1](https://huggingface.co/datasets/nvidia/Nemotron-RL-SysBench-v1) | `7083ab2bdd59` | cc-by-4.0 | 1,010 |
| `if_nemotron_cfbench` | Nemotron CFBench | [nvidia/Nemotron-RL-CFBench-v1](https://huggingface.co/datasets/nvidia/Nemotron-RL-CFBench-v1) | `7de374a40dd1` | cc-by-4.0 | 1,121 |
| `if_tulu_personas` | Tulu 3 persona instruction following | [allenai/tulu-3-sft-personas-instruction-following](https://huggingface.co/datasets/allenai/tulu-3-sft-personas-instruction-following) | `fe0c7d350c9b` | odc-by | 29,962 |
| `if_argilla_ifeval_like` | IFEval-like data (filtered) | [argilla/ifeval-like-data](https://huggingface.co/datasets/argilla/ifeval-like-data) | `56505d1771e3` | other | 52,124 |
| `if_conifer` | Conifer | [ConiferLM/Conifer](https://huggingface.co/datasets/ConiferLM/Conifer) | `8f085348895f` | apache-2.0 | 13,576 |
| `if_autoif` | AutoIF instruct 61k | [Post-training-Data-Flywheel/AutoIF-instruct-61k](https://huggingface.co/datasets/Post-training-Data-Flywheel/AutoIF-instruct-61k) | `0705aa867cce` | apache-2.0 | 38,528 |
| `if_followbench` | FollowBench | [YuxinJiang/FollowBench](https://huggingface.co/datasets/YuxinJiang/FollowBench) | `03a0578946af` | apache-2.0 | 1,796 |
| `if_jsonschemabench` | JSONSchemaBench | [epfl-dlab/JSONSchemaBench](https://huggingface.co/datasets/epfl-dlab/JSONSchemaBench) | `5bd0f4640bad` | mit | 8,977 |
| `if_ru_ifeval_like` | Russian IFEval-like data | [mizinovmv/ru_ifeval-like-data](https://huggingface.co/datasets/mizinovmv/ru_ifeval-like-data) | `fe7d385414fe` | cc-by-4.0 | 3,323 |
| `commitpackft_edit` | CommitPackFT (edit file) | [bigcode/commitpackft](https://huggingface.co/datasets/bigcode/commitpackft) | `fc56fe33c030` | mit | 461,982 |
| `commitpackft_new` | CommitPackFT (new file) | [bigcode/commitpackft](https://huggingface.co/datasets/bigcode/commitpackft) | `fc56fe33c030` | mit | 66,380 |
| `xcodeeval_problems` | xCodeEval problem statements | [NTU-NLP-sg/xCodeEval](https://huggingface.co/datasets/NTU-NLP-sg/xCodeEval) | `aa0938660407` | cc-by-4.0 | 7,635 |
| `xcodeeval_apr` | xCodeEval program repair | [NTU-NLP-sg/xCodeEval](https://huggingface.co/datasets/NTU-NLP-sg/xCodeEval) | `aa0938660407` | cc-by-4.0 | 22,757 |
| `xcodeeval_translate_to_python` | xCodeEval code translation (to Python) | [NTU-NLP-sg/xCodeEval](https://huggingface.co/datasets/NTU-NLP-sg/xCodeEval) | `aa0938660407` | cc-by-4.0 | 24,329 |
| `xcodeeval_translate_to_cpp` | xCodeEval code translation (Python to C++) | [NTU-NLP-sg/xCodeEval](https://huggingface.co/datasets/NTU-NLP-sg/xCodeEval) | `aa0938660407` | cc-by-4.0 | 2,781 |
| `debugbench` | DebugBench | [Rtian/DebugBench](https://huggingface.co/datasets/Rtian/DebugBench) | `f474dcd2ad92` | apache-2.0 | 4,170 |
| `fullstackbench` | FullStackBench | [ByteDance/FullStackBench](https://huggingface.co/datasets/ByteDance/FullStackBench) | `11e2e64dbcd6` | apache-2.0 | 3,228 |
| `codefeedback` | CodeFeedback-Filtered-Instruction | [m-a-p/CodeFeedback-Filtered-Instruction](https://huggingface.co/datasets/m-a-p/CodeFeedback-Filtered-Instruction) | `a08c213a9748` | apache-2.0 | 143,762 |
| `humaneval_xl` | HumanEval-XL | [iNeil77/HumanEval-XL](https://huggingface.co/datasets/iNeil77/HumanEval-XL) | `2f2044483da1` | see dataset card | 20,234 |
| `humanevalpack_fix` | HumanEvalFix | [bigcode/humanevalpack](https://huggingface.co/datasets/bigcode/humanevalpack) | `9a41762f73a8` | mit | 984 |
| `humanevalpack_explain` | HumanEvalExplain | [bigcode/humanevalpack](https://huggingface.co/datasets/bigcode/humanevalpack) | `9a41762f73a8` | mit | 984 |
| `synthetic_text_to_sql` | Gretel synthetic text-to-SQL | [gretelai/synthetic_text_to_sql](https://huggingface.co/datasets/gretelai/synthetic_text_to_sql) | `740ab236e645` | apache-2.0 | 105,851 |
| `stackoverflow_questions` | Stack Overflow questions (test) | [pacovaldez/stackoverflow-questions](https://huggingface.co/datasets/pacovaldez/stackoverflow-questions) | `869802e52b4d` | apache-2.0 | 1,570,866 |
| `ds1000` | DS-1000 | [xlangai/DS-1000](https://huggingface.co/datasets/xlangai/DS-1000) | `4416080ac5cb` | cc-by-sa-4.0 | 996 |
| `apps` | APPS | [codeparrot/apps](https://huggingface.co/datasets/codeparrot/apps) | `21e74ddf8de1` | mit | 10,000 |
| `kernelbench` | KernelBench | [ScalingIntelligence/KernelBench](https://huggingface.co/datasets/ScalingIntelligence/KernelBench) | `ca1464e5d472` | see dataset card | 270 |
| `verilogeval_v2` | VerilogEval v2 (spec-to-RTL) | [dakies/nvlabs-verilogeval-v2-spec-to-rtl](https://huggingface.co/datasets/dakies/nvlabs-verilogeval-v2-spec-to-rtl) | `47e52e887f29` | mit | 156 |
| `canitedit_descriptive` | CanItEdit (descriptive) | [nuprl/CanItEdit](https://huggingface.co/datasets/nuprl/CanItEdit) | `3c07f38b1f93` | mit | 105 |
| `canitedit_lazy` | CanItEdit (lazy) | [nuprl/CanItEdit](https://huggingface.co/datasets/nuprl/CanItEdit) | `3c07f38b1f93` | mit | 105 |
| `classeval` | ClassEval | [FudanSELab/ClassEval](https://huggingface.co/datasets/FudanSELab/ClassEval) | `fef204b34e22` | mit | 100 |
| `wmt24pp_reverse` | WMT24++ (reverse, X -> English) | [google/wmt24pp](https://huggingface.co/datasets/google/wmt24pp) | `fd7405c06494` | apache-2.0 | 52,726 |
| `smoldoc_to_en` | SMOL doc (X -> English) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 12,445 |
| `smoldoc_from_en` | SMOL doc (English -> X, named languages) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 12,091 |
| `smoldoc_from_en_lowres` | SMOL doc (English -> X, low-resource) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 354 |
| `smoldoc_abq_ru` | SMOL doc (Abaza -> Russian) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 0 |
| `smoldoc_am_ar` | SMOL doc (Amharic -> Arabic) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 329 |
| `smoldoc_am_zh` | SMOL doc (Amharic -> Chinese (Simplified)) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 329 |
| `smoldoc_ar_am` | SMOL doc (Arabic -> Amharic) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 329 |
| `smoldoc_ar_sw` | SMOL doc (Arabic -> Swahili) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 330 |
| `smoldoc_ce_ru` | SMOL doc (Chechen -> Russian) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 0 |
| `smoldoc_jdt_ru` | SMOL doc (Judeo-Tat (Juhuri) -> Russian) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 0 |
| `smoldoc_kjh_ru` | SMOL doc (Khakas -> Russian) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 0 |
| `smoldoc_ru_abq` | SMOL doc (Russian -> Abaza) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 66 |
| `smoldoc_ru_ce` | SMOL doc (Russian -> Chechen) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 66 |
| `smoldoc_ru_jdt` | SMOL doc (Russian -> Judeo-Tat (Juhuri)) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 584 |
| `smoldoc_ru_kjh` | SMOL doc (Russian -> Khakas) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 66 |
| `smoldoc_sw_ar` | SMOL doc (Swahili -> Arabic) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 330 |
| `smoldoc_sw_zh` | SMOL doc (Swahili -> Chinese (Simplified)) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 330 |
| `smoldoc_zh_am` | SMOL doc (Chinese (Simplified) -> Amharic) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 329 |
| `smoldoc_zh_sw` | SMOL doc (Chinese (Simplified) -> Swahili) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 330 |
| `smolsent_to_en` | SMOL sent (X -> English) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 31,716 |
| `smolsent_from_en` | SMOL sent (English -> X, named languages) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 30,874 |
| `smolsent_from_en_lowres` | SMOL sent (English -> X, low-resource) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 863 |
| `smolsent_abq_ru` | SMOL sent (Abaza -> Russian) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 0 |
| `smolsent_ce_ru` | SMOL sent (Chechen -> Russian) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 0 |
| `smolsent_jdt_ru` | SMOL sent (Judeo-Tat (Juhuri) -> Russian) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 0 |
| `smolsent_kjh_ru` | SMOL sent (Khakas -> Russian) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 0 |
| `smolsent_ru_abq` | SMOL sent (Russian -> Abaza) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 863 |
| `smolsent_ru_ce` | SMOL sent (Russian -> Chechen) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 863 |
| `smolsent_ru_jdt` | SMOL sent (Russian -> Judeo-Tat (Juhuri)) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 863 |
| `smolsent_ru_kjh` | SMOL sent (Russian -> Khakas) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 863 |
| `smolsent_yue_zh_hant` | SMOL sent (Cantonese -> Chinese (Traditional)) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 3,655 |
| `smolsent_yue_zh` | SMOL sent (Cantonese -> Chinese (Simplified)) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 3,512 |
| `smolsent_zh_hant_yue` | SMOL sent (Chinese (Traditional) -> Cantonese) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 3,489 |
| `smolsent_zh_yue` | SMOL sent (Chinese (Simplified) -> Cantonese) | [google/smol](https://huggingface.co/datasets/google/smol) | `fdaff3a1a019` | cc-by-4.0 | 3,483 |
| `ntrex_to_en` | NTREX-128 (X -> English) | [davidstap/NTREX](https://huggingface.co/datasets/davidstap/NTREX) | `b5c285fdc991` | see dataset card | 173,428 |
| `wmt23_de_en` | WMT23 general test (de-en) | [haoranxu/WMT23-Test](https://huggingface.co/datasets/haoranxu/WMT23-Test) | `19c6f6f18f37` | see dataset card | 549 |
| `wmt23_en_cs` | WMT23 general test (en-cs) | [haoranxu/WMT23-Test](https://huggingface.co/datasets/haoranxu/WMT23-Test) | `19c6f6f18f37` | see dataset card | 2,071 |
| `wmt23_en_de` | WMT23 general test (en-de) | [haoranxu/WMT23-Test](https://huggingface.co/datasets/haoranxu/WMT23-Test) | `19c6f6f18f37` | see dataset card | 556 |
| `wmt23_en_he` | WMT23 general test (en-he) | [haoranxu/WMT23-Test](https://huggingface.co/datasets/haoranxu/WMT23-Test) | `19c6f6f18f37` | see dataset card | 2,071 |
| `wmt23_en_is` | WMT23 general test (en-is) | [haoranxu/WMT23-Test](https://huggingface.co/datasets/haoranxu/WMT23-Test) | `19c6f6f18f37` | see dataset card | 1,000 |
| `wmt23_en_ja` | WMT23 general test (en-ja) | [haoranxu/WMT23-Test](https://huggingface.co/datasets/haoranxu/WMT23-Test) | `19c6f6f18f37` | see dataset card | 2,071 |
| `wmt23_en_ru` | WMT23 general test (en-ru) | [haoranxu/WMT23-Test](https://huggingface.co/datasets/haoranxu/WMT23-Test) | `19c6f6f18f37` | see dataset card | 2,071 |
| `wmt23_en_uk` | WMT23 general test (en-uk) | [haoranxu/WMT23-Test](https://huggingface.co/datasets/haoranxu/WMT23-Test) | `19c6f6f18f37` | see dataset card | 2,071 |
| `wmt23_en_zh` | WMT23 general test (en-zh) | [haoranxu/WMT23-Test](https://huggingface.co/datasets/haoranxu/WMT23-Test) | `19c6f6f18f37` | see dataset card | 2,071 |
| `wmt23_he_en` | WMT23 general test (he-en) | [haoranxu/WMT23-Test](https://huggingface.co/datasets/haoranxu/WMT23-Test) | `19c6f6f18f37` | see dataset card | 1,890 |
| `wmt23_is_en` | WMT23 general test (is-en) | [haoranxu/WMT23-Test](https://huggingface.co/datasets/haoranxu/WMT23-Test) | `19c6f6f18f37` | see dataset card | 1,000 |
| `wmt23_ja_en` | WMT23 general test (ja-en) | [haoranxu/WMT23-Test](https://huggingface.co/datasets/haoranxu/WMT23-Test) | `19c6f6f18f37` | see dataset card | 1,982 |
| `wmt23_ru_en` | WMT23 general test (ru-en) | [haoranxu/WMT23-Test](https://huggingface.co/datasets/haoranxu/WMT23-Test) | `19c6f6f18f37` | see dataset card | 1,723 |
| `wmt23_uk_en` | WMT23 general test (uk-en) | [haoranxu/WMT23-Test](https://huggingface.co/datasets/haoranxu/WMT23-Test) | `19c6f6f18f37` | see dataset card | 1,822 |
| `wmt23_zh_en` | WMT23 general test (zh-en) | [haoranxu/WMT23-Test](https://huggingface.co/datasets/haoranxu/WMT23-Test) | `19c6f6f18f37` | see dataset card | 1,959 |
| `wmt25_cs_de` | WMT25 general test (cs-de, documents) | [hgissbkh/wmt25](https://huggingface.co/datasets/hgissbkh/wmt25) | `f9d8b9d5f826` | see dataset card | 254 |
| `wmt25_cs_uk` | WMT25 general test (cs-uk, documents) | [hgissbkh/wmt25](https://huggingface.co/datasets/hgissbkh/wmt25) | `f9d8b9d5f826` | see dataset card | 228 |
| `wmt25_en_ar` | WMT25 general test (en-ar, documents) | [hgissbkh/wmt25](https://huggingface.co/datasets/hgissbkh/wmt25) | `f9d8b9d5f826` | see dataset card | 87 |
| `wmt25_en_bho` | WMT25 general test (en-bho, documents) | [hgissbkh/wmt25](https://huggingface.co/datasets/hgissbkh/wmt25) | `f9d8b9d5f826` | see dataset card | 0 |
| `wmt25_en_cs` | WMT25 general test (en-cs, documents) | [hgissbkh/wmt25](https://huggingface.co/datasets/hgissbkh/wmt25) | `f9d8b9d5f826` | see dataset card | 113 |
| `wmt25_en_et` | WMT25 general test (en-et, documents) | [hgissbkh/wmt25](https://huggingface.co/datasets/hgissbkh/wmt25) | `f9d8b9d5f826` | see dataset card | 87 |
| `wmt25_en_is` | WMT25 general test (en-is, documents) | [hgissbkh/wmt25](https://huggingface.co/datasets/hgissbkh/wmt25) | `f9d8b9d5f826` | see dataset card | 87 |
| `wmt25_en_ja` | WMT25 general test (en-ja, documents) | [hgissbkh/wmt25](https://huggingface.co/datasets/hgissbkh/wmt25) | `f9d8b9d5f826` | see dataset card | 87 |
| `wmt25_en_ko` | WMT25 general test (en-ko, documents) | [hgissbkh/wmt25](https://huggingface.co/datasets/hgissbkh/wmt25) | `f9d8b9d5f826` | see dataset card | 87 |
| `wmt25_en_mas` | WMT25 general test (en-mas, documents) | [hgissbkh/wmt25](https://huggingface.co/datasets/hgissbkh/wmt25) | `f9d8b9d5f826` | see dataset card | 0 |
| `wmt25_en_ru` | WMT25 general test (en-ru, documents) | [hgissbkh/wmt25](https://huggingface.co/datasets/hgissbkh/wmt25) | `f9d8b9d5f826` | see dataset card | 87 |
| `wmt25_en_sr` | WMT25 general test (en-sr, documents) | [hgissbkh/wmt25](https://huggingface.co/datasets/hgissbkh/wmt25) | `f9d8b9d5f826` | see dataset card | 87 |
| `wmt25_en_uk` | WMT25 general test (en-uk, documents) | [hgissbkh/wmt25](https://huggingface.co/datasets/hgissbkh/wmt25) | `f9d8b9d5f826` | see dataset card | 87 |
| `wmt25_en_zh` | WMT25 general test (en-zh, documents) | [hgissbkh/wmt25](https://huggingface.co/datasets/hgissbkh/wmt25) | `f9d8b9d5f826` | see dataset card | 87 |
| `wmt25_ja_zh` | WMT25 general test (ja-zh, documents) | [hgissbkh/wmt25](https://huggingface.co/datasets/hgissbkh/wmt25) | `f9d8b9d5f826` | see dataset card | 106 |
| `tico19_to_en` | TICO-19 (X -> English) | [gmnlp/tico19](https://huggingface.co/datasets/gmnlp/tico19) | `55d70dc0b1d1` | see dataset card | 85,514 |
| `opus100_from_en` | OPUS-100 (English -> X) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 263,367 |
| `opus100_af_en` | OPUS-100 (af -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,718 |
| `opus100_am_en` | OPUS-100 (am -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,046 |
| `opus100_ar_de` | OPUS-100 (ar -> de) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,981 |
| `opus100_de_ar` | OPUS-100 (de -> ar) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,965 |
| `opus100_ar_en` | OPUS-100 (ar -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,973 |
| `opus100_ar_fr` | OPUS-100 (ar -> fr) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,990 |
| `opus100_fr_ar` | OPUS-100 (fr -> ar) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,992 |
| `opus100_ar_nl` | OPUS-100 (ar -> nl) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,987 |
| `opus100_nl_ar` | OPUS-100 (nl -> ar) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,987 |
| `opus100_ar_ru` | OPUS-100 (ar -> ru) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,989 |
| `opus100_ru_ar` | OPUS-100 (ru -> ar) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,989 |
| `opus100_ar_zh` | OPUS-100 (ar -> zh) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,999 |
| `opus100_zh_ar` | OPUS-100 (zh -> ar) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,998 |
| `opus100_as_en` | OPUS-100 (as -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,571 |
| `opus100_az_en` | OPUS-100 (az -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,598 |
| `opus100_be_en` | OPUS-100 (be -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 2,881 |
| `opus100_bg_en` | OPUS-100 (bg -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,960 |
| `opus100_bn_en` | OPUS-100 (bn -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,944 |
| `opus100_br_en` | OPUS-100 (br -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 0 |
| `opus100_bs_en` | OPUS-100 (bs -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,971 |
| `opus100_ca_en` | OPUS-100 (ca -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,956 |
| `opus100_cs_en` | OPUS-100 (cs -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,969 |
| `opus100_cy_en` | OPUS-100 (cy -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 0 |
| `opus100_da_en` | OPUS-100 (da -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,966 |
| `opus100_de_en` | OPUS-100 (de -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,985 |
| `opus100_de_fr` | OPUS-100 (de -> fr) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,995 |
| `opus100_fr_de` | OPUS-100 (fr -> de) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,997 |
| `opus100_de_nl` | OPUS-100 (de -> nl) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,995 |
| `opus100_nl_de` | OPUS-100 (nl -> de) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,995 |
| `opus100_de_ru` | OPUS-100 (de -> ru) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,981 |
| `opus100_ru_de` | OPUS-100 (ru -> de) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,978 |
| `opus100_de_zh` | OPUS-100 (de -> zh) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,979 |
| `opus100_zh_de` | OPUS-100 (zh -> de) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,991 |
| `opus100_el_en` | OPUS-100 (el -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,951 |
| `opus100_eo_en` | OPUS-100 (eo -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 0 |
| `opus100_es_en` | OPUS-100 (es -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,989 |
| `opus100_et_en` | OPUS-100 (et -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,974 |
| `opus100_eu_en` | OPUS-100 (eu -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,952 |
| `opus100_fa_en` | OPUS-100 (fa -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,968 |
| `opus100_fi_en` | OPUS-100 (fi -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,970 |
| `opus100_fr_en` | OPUS-100 (fr -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,992 |
| `opus100_fy_en` | OPUS-100 (fy -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 0 |
| `opus100_ga_en` | OPUS-100 (ga -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,658 |
| `opus100_gd_en` | OPUS-100 (gd -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 0 |
| `opus100_gl_en` | OPUS-100 (gl -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,934 |
| `opus100_gu_en` | OPUS-100 (gu -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 2,788 |
| `opus100_ha_en` | OPUS-100 (ha -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,364 |
| `opus100_he_en` | OPUS-100 (he -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,915 |
| `opus100_hi_en` | OPUS-100 (hi -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,682 |
| `opus100_hr_en` | OPUS-100 (hr -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,956 |
| `opus100_hu_en` | OPUS-100 (hu -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,960 |
| `opus100_id_en` | OPUS-100 (id -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,943 |
| `opus100_ig_en` | OPUS-100 (ig -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 457 |
| `opus100_is_en` | OPUS-100 (is -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,917 |
| `opus100_it_en` | OPUS-100 (it -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,972 |
| `opus100_ja_en` | OPUS-100 (ja -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,961 |
| `opus100_ka_en` | OPUS-100 (ka -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,867 |
| `opus100_kk_en` | OPUS-100 (kk -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 0 |
| `opus100_km_en` | OPUS-100 (km -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 2,756 |
| `opus100_kn_en` | OPUS-100 (kn -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,351 |
| `opus100_ko_en` | OPUS-100 (ko -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,952 |
| `opus100_ku_en` | OPUS-100 (ku -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 0 |
| `opus100_ky_en` | OPUS-100 (ky -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,403 |
| `opus100_li_en` | OPUS-100 (li -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 0 |
| `opus100_lt_en` | OPUS-100 (lt -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,954 |
| `opus100_lv_en` | OPUS-100 (lv -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,950 |
| `opus100_mg_en` | OPUS-100 (mg -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,944 |
| `opus100_mk_en` | OPUS-100 (mk -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,903 |
| `opus100_ml_en` | OPUS-100 (ml -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,915 |
| `opus100_mr_en` | OPUS-100 (mr -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,700 |
| `opus100_ms_en` | OPUS-100 (ms -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,902 |
| `opus100_mt_en` | OPUS-100 (mt -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,896 |
| `opus100_my_en` | OPUS-100 (my -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,510 |
| `opus100_nb_en` | OPUS-100 (nb -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 0 |
| `opus100_ne_en` | OPUS-100 (ne -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 2,502 |
| `opus100_nl_en` | OPUS-100 (nl -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,964 |
| `opus100_nn_en` | OPUS-100 (nn -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 0 |
| `opus100_no_en` | OPUS-100 (no -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,932 |
| `opus100_oc_en` | OPUS-100 (oc -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 0 |
| `opus100_or_en` | OPUS-100 (or -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 0 |
| `opus100_pa_en` | OPUS-100 (pa -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,906 |
| `opus100_pl_en` | OPUS-100 (pl -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,967 |
| `opus100_ps_en` | OPUS-100 (ps -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,262 |
| `opus100_pt_en` | OPUS-100 (pt -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,978 |
| `opus100_ro_en` | OPUS-100 (ro -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,959 |
| `opus100_ru_en` | OPUS-100 (ru -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,970 |
| `opus100_rw_en` | OPUS-100 (rw -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,920 |
| `opus100_se_en` | OPUS-100 (se -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 0 |
| `opus100_sh_en` | OPUS-100 (sh -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 0 |
| `opus100_si_en` | OPUS-100 (si -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,848 |
| `opus100_sk_en` | OPUS-100 (sk -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,942 |
| `opus100_sl_en` | OPUS-100 (sl -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,947 |
| `opus100_sq_en` | OPUS-100 (sq -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,934 |
| `opus100_sr_en` | OPUS-100 (sr -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,946 |
| `opus100_sv_en` | OPUS-100 (sv -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,944 |
| `opus100_ta_en` | OPUS-100 (ta -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 2,776 |
| `opus100_te_en` | OPUS-100 (te -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 2,506 |
| `opus100_tg_en` | OPUS-100 (tg -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,123 |
| `opus100_th_en` | OPUS-100 (th -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,939 |
| `opus100_tk_en` | OPUS-100 (tk -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 0 |
| `opus100_tr_en` | OPUS-100 (tr -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,916 |
| `opus100_tt_en` | OPUS-100 (tt -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 0 |
| `opus100_ug_en` | OPUS-100 (ug -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 0 |
| `opus100_uk_en` | OPUS-100 (uk -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,907 |
| `opus100_ur_en` | OPUS-100 (ur -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,572 |
| `opus100_uz_en` | OPUS-100 (uz -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 2,961 |
| `opus100_vi_en` | OPUS-100 (vi -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,888 |
| `opus100_wa_en` | OPUS-100 (wa -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 0 |
| `opus100_xh_en` | OPUS-100 (xh -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,815 |
| `opus100_yi_en` | OPUS-100 (yi -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 0 |
| `opus100_zh_en` | OPUS-100 (zh -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 3,997 |
| `opus100_zu_en` | OPUS-100 (zu -> en) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 944 |
| `opus100_fr_nl` | OPUS-100 (fr -> nl) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,981 |
| `opus100_nl_fr` | OPUS-100 (nl -> fr) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,981 |
| `opus100_fr_ru` | OPUS-100 (fr -> ru) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,996 |
| `opus100_ru_fr` | OPUS-100 (ru -> fr) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,996 |
| `opus100_fr_zh` | OPUS-100 (fr -> zh) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 2,000 |
| `opus100_zh_fr` | OPUS-100 (zh -> fr) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 2,000 |
| `opus100_nl_ru` | OPUS-100 (nl -> ru) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,984 |
| `opus100_ru_nl` | OPUS-100 (ru -> nl) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,982 |
| `opus100_nl_zh` | OPUS-100 (nl -> zh) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,997 |
| `opus100_zh_nl` | OPUS-100 (zh -> nl) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 1,998 |
| `opus100_ru_zh` | OPUS-100 (ru -> zh) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 2,000 |
| `opus100_zh_ru` | OPUS-100 (zh -> ru) | [Helsinki-NLP/opus-100](https://huggingface.co/datasets/Helsinki-NLP/opus-100) | `805090dc28bf` | unknown | 2,000 |
| `tydiqa_goldp` | TyDi QA GoldP | [google-research-datasets/tydiqa](https://huggingface.co/datasets/google-research-datasets/tydiqa) | `da78f23f9119` | apache-2.0 | 54,939 |
| `mlqa` | MLQA | [facebook/mlqa](https://huggingface.co/datasets/facebook/mlqa) | `0d43d0f635e3` | see dataset card | 173,739 |
| `indicqa` | IndicQA | [ai4bharat/IndicQA](https://huggingface.co/datasets/ai4bharat/IndicQA) | `2ae91669875c` | see dataset card | 16,896 |
| `korquad_v1` | KorQuAD 1.0 | [KorQuAD/squad_kor_v1](https://huggingface.co/datasets/KorQuAD/squad_kor_v1) | `01aad2385335` | cc-by-nd-4.0 | 66,017 |
| `sberquad` | SberQuAD | [kuznetsoffandrey/sberquad](https://huggingface.co/datasets/kuznetsoffandrey/sberquad) | `deb870ee29b2` | unknown | 74,284 |
| `swe_rebench_openhands` | SWE-rebench OpenHands trajectories | [nebius/SWE-rebench-openhands-trajectories](https://huggingface.co/datasets/nebius/SWE-rebench-openhands-trajectories) | `35455389ab51` | cc-by-4.0 | 67,074 |
| `term_nemotron_trajectories` | Nemotron-Terminal synthetic-task trajectories | [nvidia/Nemotron-Terminal-Corpus](https://huggingface.co/datasets/nvidia/Nemotron-Terminal-Corpus) | `a1667c4ffdad` | cc-by-4.0 | 139,403 |

Data files: 292 chungus parquet shard(s) under `data/`.
