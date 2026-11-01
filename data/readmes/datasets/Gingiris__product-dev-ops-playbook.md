---
license: mit
language:
- zh
- en
- ja
- ko
tags:
- product-management
- engineering-operations
- sprint-planning
- agile
- cross-functional
- startup-operations
pretty_name: Product Dev Ops Playbook — Cross-Functional Sprint Alignment SOP
task_categories:
- text-generation
---

# Product Dev Ops Playbook — Cross-Functional Sprint Alignment SOP

Complete Product × Engineering × Operations alignment SOP — from unified backlog to 10-day sprint cadence to veto power rules.

## 📦 Install on ClawHub

```bash
clawhub install product-dev-ops-playbook
```

Then ask your AI agent:

> "Design a 10-day sprint cadence for our 8-person product+eng team"

Installs the **complete Product × Engineering × Operations alignment SOP** — dual-layer Kanban, 10-day sprint cadence, issue templates with reproducibility rules, ops-veto-on-release framework, user feedback → product iteration closed loop.

🔗 [View on ClawHub](https://clawhub.ai/gingiris/product-dev-ops-playbook) · [All Gingiris skills](https://clawhub.ai/user/gingiris) · [Author blog](https://gingiris.tools)

## 🚀 30-Second Preview

```
You: 8-person team (3 PM/design, 4 eng, 1 ops). Design our sprint cadence.
Agent (with product-dev-ops-playbook):

  Cadence: 10-day sprint (5-day half doesn't fit AI prototype work)

  Day 1 (Mon) — Sprint planning + kickoff:
    Backlog grooming (45min) → 10-day commitments
    Engineering: pick 3-5 stories with clear acceptance criteria
    Ops: surface customer-blocking issues (auto-escalates if reported ≥3x)
    Veto rules: P0 bugs from ops block any new story acceptance

  Day 2-5 — Build phase:
    Daily standup (15min, async-first via Discord/Slack thread)
    PM unblocks design questions, eng pairs on hard problems

  Day 6 — Testable build deadline:
    Eng ships to staging; ops + PM smoke-test
    Bug triage: P0/P1 fix-in-sprint, P2 defer

  Day 7-9 — Polish + edge cases:
    User feedback batched daily, sprint scope locked

  Day 10 (Fri) — Ship + retro:
    Ops has FINAL release veto if P0 bug present
    Retro: 3 things working, 3 things to fix next sprint
```

Real cadence with embedded governance — not abstract Agile theater.

---

## What's Inside

- **Dual-layer Kanban system** (master backlog + sprint board with unified tagging)
- **10-day sprint standard process** (Day 1 dev → Day 6 testable build → Day 10 ship)
- **Issue template** with reproducibility requirements (3x reported = auto-severe)
- **Tri-party alignment meetings** (daily standup / sprint planning / sprint review)
- **Operations veto power** on releases (P0 bug = block shipping)
- **User feedback → product iteration closed loop** (beta testing + interview SOP)
- **Core metrics framework** (acquisition → activation → retention → monetization → referral)
- **Technical debt management** (20-30% sprint capacity reserved)
- **Ready-to-use templates:** Bug Report, Sprint Planning, Responsibility Matrix

## Languages

| Language | File |
|----------|------|
| 中文 (Chinese) | [SKILL.md](SKILL.md) |
| English | [references/en/README.md](references/en/README.md) |
| 日本語 (Japanese) | [references/ja/README.md](references/ja/README.md) |
| 한국어 (Korean) | [references/ko/README.md](references/ko/README.md) |

## Install (Cola / ClawHub)

```bash
clawhub install product-dev-ops-playbook
```

## Author

By [@WeiYipei](https://github.com/Gingiris-1031)

<!-- gingiris-community-cta:start -->
## 加入出海社群与购买资料包 · Community & Resources

- **加入出海社群：** 微信添加 **staywildgrow**，留言「**加入社群**」即可。
- **购买资料包：** 微信添加 **staywildgrow**，咨询购买 Gingiris 出海资料包，价格 **599 元人民币**。

- **Join the global growth community:** Add **staywildgrow** on WeChat and send **“加入社群”** (join the community).
- **Get the resource pack:** Add **staywildgrow** on WeChat to purchase the Gingiris global growth resource pack for **CNY 599**.

社群与资料包为可选入口，不影响本开源 Skill 的安装和使用。

The community and paid resource pack are optional; neither is required to install or use this open-source skill.
<!-- gingiris-community-cta:end -->
