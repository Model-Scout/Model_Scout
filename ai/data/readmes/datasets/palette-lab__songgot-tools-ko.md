---
license: apache-2.0
language:
- ko
task_categories:
- text-generation
tags:
- tool-calling
- function-calling
- korean
- synthetic
size_categories:
- 100K<n<1M
---

# Songgot Tools KO

Synthetic Korean tool-calling data used to post-train Songgot (github.com/hanishkeloth/songgot): 336,602 verified
(request, call) pairs over 183,737 tool schemas across 60 Korean service domains. Released 2026-09-11 under
Apache 2.0.

## How it was made

Every row was produced by our own open teacher model, Palette-K-Midm, in three stages
(harness/teacher_synth.py in the Songgot repo):

1. Schemas: the teacher invents tool schemas for a domain in a given naming style (snake_case, camelCase,
   PascalCase, suffixed and abbreviated variants), with Korean descriptions and JSON Schema parameters. A share
   of tools get "confusable siblings": tools in the same service with similar names and different functions.
2. Requests and calls: for each tool the teacher writes three Korean requests in different registers (polite,
   casual, terse, typo-laden, long-winded, hurried) together with the exact call JSON.
3. Verification: with the target tool shown among three distractors (siblings first), the teacher re-derives the
   call from the request alone. A pair is kept only when tool name, argument keys and argument values agree
   (about 97 percent agree on the name, 57 percent on everything). Nothing else filters the data.

No closed model touched the data. The 645 real tool schemas from the glaive-function-calling-v2 (Apache 2.0)
catalogue and Songgot's own Korean catalogue seeded the first run; every other schema is invented.

## Fields

- `domain`: Korean domain name (`catalogue` for the seed tools)
- `tool`: the schema (`name`, `description`, `parameters`)
- `query`: the Korean request
- `call`: `{"name": ..., "arguments": {...}}`, the label

`tools.json` lists every schema (183,737), including those with no surviving rows, with `domain` and, for
siblings, `sibling_of`.

## Numbers

Top domains by rows: 세금과 연말정산 7,341, 수면과 건강 데이터 6,420, 파일과 클라우드 6,172, 보험 6,161, 주차와 주유 6,133, 학교와 학사 6,048, 매장 운영과 POS 6,028, 부동산과 임대 6,022.

Measured effect on a 50M-parameter from-scratch model (FunctionChat-Bench SingleCall, Kakao, exact match):
11.4 percent call accuracy without this data, 23.8 with the first 36k rows, 27.6 with the first 100k rows, on the
same base. Details, error bars and the negative results are in the Songgot paper.

## Caveats

The requests are teacher-written Korean, not user logs; register variety is prompted, not observed. Argument
values are whatever the teacher chose; dates and times were asked for in ISO-like forms. Verification is
self-consistency of one teacher, which catches inconsistent labels but not shared blind spots. Use the
benchmark guard in the repo (harness/assemble_sft.py) if you evaluate on FunctionChat-Bench: no tool name or
query here collides with it, and we keep it that way.
