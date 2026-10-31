---
pretty_name: Combined Titlegen Conversations
language:
  - vi
  - en
  - zh
  - ja
  - ko
  - th
  - fr
  - de
  - es
task_categories:
  - text-generation
tags:
  - conversation-title-generation
  - multilingual
  - synthetic
size_categories:
  - 10K<n<100K
configs:
  - config_name: default
    data_files:
      - split: train
        path: train.jsonl
      - split: validation
        path: validation.jsonl
      - split: test
        path: test.jsonl
      - split: test_vi
        path: test_vi.jsonl
      - split: synthetic_holdout
        path: synthetic_holdout.jsonl
---

# Combined Titlegen Conversations

This public release directly appends 10,284 accepted legacy title-generation
rows and 13,500 nine-language LLM-generated rows. The 23,784 examples are split
as train 20,584, validation 1,550, legacy test 200, legacy Vietnamese test 100,
and label-free synthetic holdout 1,350. Legacy rows contain only `messages`;
nine-language rows retain their richer IDs, language, coverage, cluster,
quality, and model-provenance fields. Train and validation intentionally use
this mixed schema without adding inferred fields to legacy rows.

The legacy tests keep their previously published assistant labels. The
synthetic holdout contains only system and user messages; its reference titles
remain private. Rejected rows, audit data, credentials, checkpoints, critic
explanations, and provider failures are excluded.

The legacy subset was teacher-distilled with automatic quality control. The
nine-language subset was produced with generator-v5 and critic-v6 using
`cx/gpt-5.6-sol` and seed 42; it is `quality_level=llm_generated` and
`human_validated=false`. Both sources can share model-family biases, and the
synthetic languages have no native-speaker review. Native-speaker and
task-specific safety review are required before production use. No dataset
license is asserted by this release.

## Languages

The current language metadata lists exactly Vietnamese, English, Chinese,
Japanese, Korean, Thai, French, German, and Spanish with codes vi, en, zh, ja,
ko, th, fr, de, and es. The nine-language source remains balanced at 1,500
examples per language: 1,200 train, 150 validation, and 150 synthetic holdout
rows. The legacy source contributes its original rows without inferred language
fields.

## Record Structure

Legacy rows retain only `messages`. Nine-language rows retain `id`, `language`,
`messages`, `split`, `coverage`, `cluster_id`, `quality_level`,
`human_validated`, `generator_model`, and `critic_model`.

## Generation and Review

The multilingual rows use generator prompt v5, critic prompt v6,
`cx/gpt-5.6-sol`, and seed 42. No native-speaking reviewer validated them.

## Quality and Leakage Checks

The combined release has zero normalized cross-source prompt overlap and zero
normalized cross-split prompt overlap. Aggregate reports and the SHA-256
manifest provide the reproducible counts and integrity metadata.

## Dataset QA Methodology

This release uses automated and LLM-assisted QA before publication. The
deterministic gates validate schema, message-role, language, and count checks;
the current release profile is 23,784 rows overall, including the nine-language
profile of 1,500 examples per language split as 1,200 train, 150 validation, and
150 synthetic holdout rows. Future profiles may use different counts, but the
declared counts must match the generated files exactly.

The row-level provenance fields record `generator_model` and `critic_model`.
The quality report records `generator_prompt_version=nine-language-llm-generator-v5`,
`critic_prompt_version=nine-language-llm-critic-v6`, model family
`cx/gpt-5.6-sol`, and seed 42. LLM critic review is used as an additional
quality gate, but it is not native-speaker human validation; the current rows
explicitly remain `human_validated=false`.

Duplicate and leakage controls require zero normalized prompt overlap across
sources and splits, and zero semantic cluster overlap across splits for any new
language release. The synthetic holdout contains only system/user messages, and
private holdout labels remain isolated outside the public bundle. Dataset,
duplicate, and quality reports plus the SHA-256 manifest provide reproducible
counts, overlap results, provenance, byte sizes, and checksums. Release
publication also requires remote byte checks plus Hugging Face card parsing,
mixed-schema loading, and Hugging Face Viewer gates.

## Adding a New Language

Use this checklist as the contract for promoting any roadmap language into
current coverage:

1. Define the language code, display name, and target split counts.
2. Generate rows with the recorded generator model, prompt version, and seed.
3. Run deterministic QC for required fields, message roles, supported language,
   split membership, and exact row counts.
4. Run the LLM critic and record critic model/prompt provenance.
5. Verify exact per-language split counts against the declared release profile.
6. Confirm zero normalized prompt overlap and zero semantic cluster overlap across splits.
7. Keep holdout rows to system/user messages only and store private labels separately.
8. Update dataset, duplicate, and quality reports plus the SHA-256 manifest.
9. Run Hugging Face mixed-schema, card, and Viewer validation.
10. Add the language to the YAML current coverage only after all gates pass.

## Intended Uses

Use this dataset to train or evaluate concise same-language conversation-title
generation. The synthetic holdout is not a human-authored benchmark.

## Limitations

Generator and critic share a model family, creating shared-model bias. Rows may
contain unnatural phrasing, cultural errors, subtle language mixing, or uneven
regional representation.

## Privacy

Private holdout labels, rejected candidates, critic explanations, provider
failures, credentials, audit payloads, and checkpoints are excluded.

## Future Language Roadmap

Portuguese, Russian, Indonesian, Filipino, Malay, Burmese, Lao, and Tamil have
no rows yet in this release. They are future roadmap languages and must pass the
same release gates later. Future roadmap languages are not included in the YAML metadata until their rows pass the checklist above. This is not completed 17-language coverage.

## License

No dataset license is asserted by this release.
