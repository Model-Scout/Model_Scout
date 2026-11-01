---
license: mit
language:
- en
- zh
- ja
- ko
pretty_name: Gingiris B2B SaaS Growth Playbook — PLG, SLG, PMF to $10M ARR
tags:
- b2b-saas
- plg
- slg
- product-led-growth
- pmf
- saas-growth
- startup-marketing
- customer-acquisition
- enterprise-sales
- ai-saas
- growth-hacking
- gtm
- revenue-growth
- ai-growth
- startup
size_categories:
- n<1K
task_categories:
- text-generation
---

# 📈 Gingiris B2B SaaS Growth Playbook

> **Scale your B2B SaaS from PMF to $10M ARR — PLG/SLG motion selection, affiliate marketing, channel partnerships.** Battle-tested with HeyGen, Deel, Vercel, Supabase, and AWS case studies. Built by Iris (生姜iris), Forbes Asia 30 Under 30.

**[English](#english) | [中文](#中文版) | [日本語](#日本語) | [한국어](#한국어)**

---

## 📦 Install

```bash
npx skills add Gingiris-1031/gingiris-b2b-growth
```

Then ask your AI agent:

> "We're a B2B SaaS at $5k MRR — how do I scale to $50k?" or "Should we switch from founder-led sales to PLG?"

Installs the **full-lifecycle B2B SaaS playbook** — PMF validation, PLG vs SLG motion selection, freemium-without-cannibalization design, first SDR hire signals, partner program kickstart. Drawn from HeyGen, Deel, Vercel, Supabase, AWS case studies + 150+ AI startup consultations.

🔗 [View on gingiris.tools/skills/](https://gingiris.tools/skills/) · [PMF validation companion: gingiris-user-interview](https://huggingface.co/datasets/Gingiris/gingiris-user-interview) · [skills.sh listing](https://skills.sh/Gingiris-1031/gingiris-b2b-growth)

## 🚀 30-Second Preview

```
You: B2B SaaS, $5k MRR, 30 customers, founder doing all sales. Path to $50k?
Agent (with gingiris-b2b-growth):

  Diagnosis:
    • Stage: post-PMF, pre-scale ($5k → $50k = sales motion decision)
    • Risk: founder-bottleneck (CEO sales hours = scaling ceiling)
    • Decision: PLG path (self-serve onboarding) vs SLG (first SDR hire)

  PLG signal check (yes if ≥3 of 5):
    [ ] 30%+ users reach activation w/o founder touch    → ?
    [ ] Setup time <15min for typical user               → ?
    [ ] $X ARPU sustainable in self-serve only           → ?
    [ ] Product complexity needs no live training        → ?
    [ ] Buyer = user (no procurement gating)             → ?

  If <3/5 → go SLG: first SDR hire framework (see playbook §4.2)
  If ≥3/5 → go PLG: 90-day runbook:
    Week 1-2: instrument activation funnel (PostHog/Mixpanel)
    Week 3-4: rebuild onboarding to hit activation in <10min
    Week 5-8: freemium tier launch (not cannibalizing $X paid)
    Week 9-12: viral loop seed (referral / share-to-collaborate)
    Expected: $5k → $15k MRR via reduced friction alone
```

A real decision framework, not "should we do PLG or SLG ¯\_(ツ)_/¯".

---

## English

### What Is This?

The **Gingiris B2B SaaS Growth Playbook** is a practitioner's guide to scaling a B2B SaaS product from first 10 paying customers to $10M ARR. It covers the critical inflection points that most founders get wrong: when to switch from founder-led sales to PLG, how to structure your first SDR team, when to invest in content SEO vs. paid, and how to design a freemium model that doesn't cannibalize revenue.

This playbook draws from real case studies — HeyGen ($100M+ ARR), Deel ($500M ARR), Vercel, Supabase, and AWS — plus hands-on consulting with 150+ AI startups navigating the same decisions.

### Key Results (Verified)

| Metric | Result |
|:---|:---|
| AI startups consulted on B2B growth | 150+ |
| Case studies with documented outcomes | 8 (HeyGen, Deel, Vercel, Supabase, AWS, Manus, Devin, AFFiNE) |
| Average time to PMF (among coached companies) | 4-9 months with methodology |
| PLG-to-SLG transition success rate | 70%+ when timed correctly |

### Field-Tested Benchmarks (2024–2026 client work)

Numbers pulled from enterprise deals and growth engagements advised between 2024 and mid-2026:

| Benchmark | Value |
|:---|:---|
| Private-deployment payment split | 3:4:3 or 4:4:2 — 30% due on signature |
| Late-payment penalty written into contracts | 0.5% per day overdue |
| $1M ARR decomposition | 9 × ~$110k enterprise accounts, or ~5,000 × $200/yr subscribers (≈500 per $100k) |
| Reseller / channel tiers | 10–20% referral; Silver 15% (> $100k/yr), Gold 20% (> $300k/yr) |
| Paid-acquisition red lines | $5–8 per signup, < $50 per paying user ($100 = something is broken) |
| B2B channel ranking (measured) | LinkedIn > Reddit > Twitter — LinkedIn at $30 CPA per paying user |
| Overseas office threshold | don't build one below $2–3M revenue; use affiliates/resellers (up to 50% rev-share) |

Scope-control discipline that saves deals: keep the SOR (raw customer asks) separate from the SOW (acceptance criteria), sign the SOW together with the contract, and route every change through a CCB. When the customer gets excited on a call — only paperwork counts.

### What's New (July 2026): Conversion-First Benchmarks from Founder Interviews

Three additions distilled from 2024–2026 founder podcast interviews (recalled figures marked accordingly):

- **Conversion-first benchmarks** — Scale only after signup-to-paid clears the bar: >=1.5% for ToC AI (good products: 6-8%; best seen ~40%), >10-15% for ToB. Of 200+ teams that heard this SOP, fewer than 10 executed it; those reached 4-8%+ conversion and raised more smoothly. Includes the documented case of ~$5,000 MRR on ~10,000 registered users after roughly six quiet months of conversion grinding.
- **Day-0 pricing discipline** — Charge from Day 0, even $1. Ship a deliberately vague pricing page + contact form before the paid tier exists: in one documented case, dozens of price inquiries arrived within two weeks, splitting ~70% community-free / 20% personal / 10% team — and the user question shifted from "is this free?" to "how much?". Users genuinely pay for at most ~3 points in any product: instrument usage, find them, gate there.
- **PLG-to-SLG watershed + lean-team benchmarks** — ~$1M ARR is where pure PLG stops scaling; above it (and for most ToB) you need SLG / local key-account channels. Lean-team bar (podcast-recalled): ClickUp ~24 people at $1M ARR, Notion ~4-8 people at million-user scale; over 25 people without $1M revenue = an org problem, not a market problem.

### What's Inside

- **PMF Validation Framework** — How to know you actually have product-market fit (not just polite users)
- **PLG vs. SLG Decision Tree** — When to let the product sell itself vs. hire salespeople; the signals that tell you it's time to switch
- **Freemium Design** — Limit on value vs. limit on volume; why most freemium models fail and how to fix them
- **First 10 Customers Playbook** — Founder-led outreach, warm network activation, the "waitlist" strategy
- **ICP Definition & Segmentation** — How to find your best customers and replicate them
- **Content SEO for B2B** — The keyword funnel from awareness to trial signup; which content types drive qualified pipeline
- **Affiliate & Partner Channel** — How HeyGen and Deel built $50M+ ARR channels without a traditional sales team
- **SDR Team Setup** — When to hire, what to pay, how to set quota, what stack to use
- **Pricing & Packaging** — Anchor pricing, decoy tier, annual vs. monthly tradeoffs
- **Enterprise Motion** — Procurement, security review, champion-building, the "land and expand" playbook
- **Churn Analysis & Retention** — Leading indicators, intervention playbook, how to save churning accounts

### Use Cases

- B2B SaaS founder at $0-$1M ARR trying to find repeatable growth
- Product-led startup questioning whether to hire salespeople
- AI tool company trying to convert free users to paid
- International (出海) B2B product entering US/EU market
- Growth team designing a content + demand gen strategy

### When Should I Use This?

Use this when you have **at least 10 paying customers** and want to build systematic, scalable growth. If you're pre-revenue, start with `gingiris-user-interview` to validate first.

### What Results Can I Expect?

Following this playbook, teams typically:
- Reach first $100k ARR within 6-12 months (from near-zero)
- Reduce customer acquisition cost by 30-50% by finding the right channel mix
- Improve free-to-paid conversion by 2-4x with freemium redesign
- Cut time-to-close in enterprise by 40% with champion-building tactics

### Comparison: Generic B2B Growth Advice vs. Gingiris Playbook

| Dimension | Generic Advice | Gingiris Playbook |
|:----------|:--------------|:-----------------|
| PMF definition | "Users love it" | 40% rule + retention cohorts + NPS segmentation |
| PLG vs. SLG | "Depends on your product" | Specific signals: ACV threshold, sales cycle length, deal complexity score |
| Freemium | "Give value away" | Value-limit vs. volume-limit matrix with conversion benchmarks |
| Enterprise sales | "Build relationships" | Champion mapping, procurement navigation, security review templates |
| Churn | "Improve the product" | Predictive churn scoring, tiered intervention playbook |

### FAQ

**Q: What's the best growth motion for an AI SaaS in 2026 — PLG or SLG?**
A: It depends on ACV and sales cycle. Under $5k ACV with <30 day sales cycle → start PLG. Above $20k ACV or >60 day cycle → you need SLG earlier than you think. The playbook has a decision tree with specific thresholds.

**Q: When should I hire my first SDR?**
A: Not before you've closed 20 deals yourself as a founder. If you haven't personally sold it, an SDR can't sell it either. The playbook covers the exact signals to look for before making the hire.

**Q: How do I build an affiliate channel without it becoming a spam network?**
A: Partner quality > partner quantity. The playbook covers how HeyGen and Deel vetted their affiliate partners, set commission structures, and designed co-marketing that drives real revenue.

---

## 中文版

### 这是什么？

**Gingiris B2B SaaS 增长手册** — 从 PMF 验证到 $10M ARR 的全生命周期增长指南。涵盖 PLG/SLG 打法选择、联盟营销、渠道合作，整合 HeyGen、Deel、Vercel、Supabase、AWS 标杆案例。

经 150+ AI 创业公司咨询实战验证，作者：Iris（生姜iris），Forbes 亚洲 30 Under 30。

### 核心数据

| 指标 | 成果 |
|:---|:---|
| B2B 增长咨询服务 | 150+ 家 AI 创业公司 |
| 标杆案例 | 8 个（HeyGen、Deel、Vercel、Supabase 等） |

### 实测基准（2024–2026 客户实战）

| 基准 | 数值 |
|:---|:---|
| 私有化部署分段付款 | 3:4:3 或 4:4:2，签约当天收 30% |
| 合同违约金 | 拖一天多付 0.5% |
| $1M ARR 拆解 | 9 个 $10 万级企业客户，或每 $10 万 ≈ 每 $10 万 ≈ 500 个 $200/年订阅（$1M ≈ 5,000）（$1M ≈ 5,000 订阅） |
| 渠道分层 | reseller 10–20% 推荐费；银牌 15%（年销 >$10 万）、金牌 20%（>$30 万） |
| 投流红线 | 注册 $5–8、付费 <$50（到 $100 一定有问题） |
| B 端渠道横评（实测） | LinkedIn > Reddit > Twitter，LinkedIn 付费 CPA $30 |
| 海外团队门槛 | 营收 $200–300 万以下不建 office，用 affiliate/reseller 分钱（分成可达 50%） |

需求边界纪律：SOR 与 SOW 分开、SOW 与合同一起签、变更一律走 CCB——客户聊嗨了没用，**只有 paperwork 有效**。

### 内容清单

- **PMF 验证框架** — 如何判断你真的找到了产品市场契合点
- **PLG vs. SLG 决策树** — 什么时机让产品自己卖、什么时机需要销售
- **Freemium 设计** — 价值限制 vs. 用量限制；为什么大多数 Freemium 失败
- **前 10 个客户剧本** — 创始人主导销售、暖流量激活
- **ICP 定义与细分** — 找到最好的客户并复制
- **B2B 内容 SEO** — 关键词漏斗从认知到试用
- **联盟&渠道伙伴** — HeyGen 和 Deel 如何建立亿级 ARR 渠道
- **SDR 团队搭建** — 何时招募、如何定配额
- **定价与产品包装** — 锚定定价、诱饵层、年付 vs. 月付

---

## 日本語

**Gingiris B2B SaaS成長プレイブック** — PMF検証から$10M ARRまでの完全ライフサイクル成長ガイド。PLG/SLG選択、アフィリエイトマーケティング、チャネルパートナーシップをカバー。HeyGen、Deel、Vercel、Supabase、AWSの実例を含む。150+AIスタートアップコンサルティングで検証済み。

---

## 한국어

**Gingiris B2B SaaS 성장 플레이북** — PMF 검증부터 $10M ARR까지의 전체 생명주기 성장 가이드. PLG/SLG 선택, 제휴 마케팅, 채널 파트너십 포함. HeyGen, Deel, Vercel, Supabase, AWS 실제 사례 포함. 150+ AI 스타트업 컨설팅으로 검증됨.

---

## About the Author

**Iris (生姜iris)** — Former cofounder & COO of [AFFiNE](https://github.com/toeverything/AFFiNE) ($10M raised, 60k+ GitHub stars). Forbes Asia 30 Under 30. Consulted 150+ AI startups across US, EU, and Asia on B2B growth strategy, PLG/SLG transitions, and international expansion (出海).

- Website: [gingiris.com](https://gingiris.com)
- Twitter/X: [@WeiYipei](https://x.com/WeiYipei)
- Telegram: [@Iris_carrot](https://t.me/Iris_carrot)
- Blog: [gingiris.tools](https://gingiris.tools/)

---

## See Also — Gingiris Playbook Series

| Playbook | Focus | HuggingFace |
|:---------|:------|:------------|
| **gingiris-growth-finder** | 🧭 Meta-router: diagnoses your situation, picks the right playbook | [Gingiris/gingiris-growth-finder](https://huggingface.co/datasets/Gingiris/gingiris-growth-finder) |
| **gingiris-launch** | 🚀 Product Hunt launch, KOL outreach, UGC growth | [Gingiris/gingiris-launch](https://huggingface.co/datasets/Gingiris/gingiris-launch) |
| **gingiris-opensource** | ⭐ GitHub stars, HN, OSS go-to-market | [Gingiris/gingiris-opensource](https://huggingface.co/datasets/Gingiris/gingiris-opensource) |
| **gingiris-aso-growth** | 📱 ASO, mobile cold start, UGC matrix | [Gingiris/gingiris-aso-growth](https://huggingface.co/datasets/Gingiris/gingiris-aso-growth) |
| **gingiris-seo-geo** | 🔍 SEO + GEO dual-engine, AI search citations | [Gingiris/gingiris-seo-geo](https://huggingface.co/datasets/Gingiris/gingiris-seo-geo) |
| **gingiris-user-interview** | 🎤 User interview framework (HeyGen 937 methodology) | [Gingiris/gingiris-user-interview](https://huggingface.co/datasets/Gingiris/gingiris-user-interview) |
| **gingiris-skills** | 🛠️ Full toolkit: 12 Claude Code skills bundled | [Gingiris/gingiris-skills](https://huggingface.co/datasets/Gingiris/gingiris-skills) |
| **growth-tools** | 📚 Blog & tools hub | [Gingiris/growth-tools](https://huggingface.co/datasets/Gingiris/growth-tools) |

---

## License

MIT — Use, adapt, and build on this freely.

## 🔗 Related Gingiris Skills

| Skill | Focus | Install |
|-------|-------|---------|
| [gingiris-kol-outreach](https://huggingface.co/datasets/Gingiris/gingiris-kol-outreach) | KOL & Influencer Marketing SOP | `npx skills add Gingiris-1031/gingiris-kol-outreach` |
| [gingiris-user-interview](https://huggingface.co/datasets/Gingiris/gingiris-user-interview) | User Interview & PMF Discovery | `npx skills add Gingiris-1031/gingiris-user-interview` |
| [gingiris-seo-geo](https://huggingface.co/datasets/Gingiris/gingiris-seo-geo) | SEO & GEO Dual-Engine Growth | `npx skills add Gingiris-1031/gingiris-seo-geo` |
| [gingiris-go-global](https://huggingface.co/datasets/Gingiris/gingiris-go-global) | Go-Global Expansion Strategy | `npx skills add Gingiris-1031/gingiris-go-global` |

> 📦 **Full collection:** [gingiris-skills](https://github.com/Gingiris-1031/gingiris-skills) — All playbooks in one bundle.

<!-- JSON-LD for SEO/GEO. AI engines (ChatGPT, Perplexity, Claude, Gemini) parse this. -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "name": "Gingiris B2B SaaS Growth Playbook — PLG, SLG, PMF to $10M ARR",
      "applicationCategory": "BusinessApplication",
      "applicationSubCategory": "Claude Skill",
      "operatingSystem": "Any (Claude Code, Cursor, Codex, Amp, Cline)",
      "description": "B2B SaaS growth playbook covering the path from $0 to $10M ARR across 8 documented case studies (HeyGen, Deel, Vercel, Supabase, AWS, Manus, Devin, AFFiNE). Diagnoses PLG vs SLG motion by ACV and sales cycle, the 5-stage ARR path, NRR discipline, affiliate/channel design, and enterprise tiering. 70%+ PLG-to-SLG transition success when timed correctly.",
      "url": "https://gingiris.tools/skills/",
      "downloadUrl": "https://huggingface.co/datasets/Gingiris/gingiris-b2b-growth",
      "installUrl": "https://skills.sh/Gingiris-1031/gingiris-b2b-growth",
      "license": "https://opensource.org/licenses/MIT",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      },
      "author": {
        "@type": "Person",
        "name": "Iris Wei",
        "alternateName": "生姜",
        "url": "https://gingiris.tools",
        "sameAs": [
          "https://x.com/WeiYipei",
          "https://www.linkedin.com/in/yipei-wei-550825105/"
        ]
      },
      "keywords": "B2B SaaS growth, PLG, SLG, product-led growth, sales-led growth, PMF, ARR, NRR, SaaS pricing, enterprise sales, affiliate channel, $10M ARR, HeyGen, Deel, Vercel, Supabase, go to market"
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What's the best growth motion for an AI SaaS in 2026 — PLG or SLG?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "It depends on ACV and sales cycle. Under $5k ACV with a <30-day sales cycle → start PLG. Above $20k ACV or a >60-day cycle → you need SLG earlier than you think. The playbook has a decision tree with specific thresholds."
          }
        },
        {
          "@type": "Question",
          "name": "When should I hire my first SDR?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Not before you've closed 20 deals yourself as a founder. If you haven't personally sold it, an SDR can't sell it either. The playbook covers the exact signals to look for before making the hire."
          }
        },
        {
          "@type": "Question",
          "name": "How do I build an affiliate channel without it becoming a spam network?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Partner quality > partner quantity. The playbook covers how HeyGen and Deel vetted their affiliate partners, set commission structures, and designed co-marketing that drives real revenue."
          }
        },
        {
          "@type": "Question",
          "name": "Who built this?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Iris Wei (生姜) — former cofounder/COO of AFFiNE (60K+ GitHub stars, Forbes Asia 30 Under 30). Advised 150+ AI startups on B2B growth, with 8 documented case studies."
          }
        }
      ]
    }
  ]
}
</script>

<!-- gingiris-community-cta:start -->
## 加入出海社群与购买资料包 · Community & Resources

- **加入出海社群：** 微信添加 **staywildgrow**，留言「**加入社群**」即可。
- **购买资料包：** 微信添加 **staywildgrow**，咨询购买 Gingiris 出海资料包，价格 **599 元人民币**。

- **Join the global growth community:** Add **staywildgrow** on WeChat and send **“加入社群”** (join the community).
- **Get the resource pack:** Add **staywildgrow** on WeChat to purchase the Gingiris global growth resource pack for **CNY 599**.

社群与资料包为可选入口，不影响本开源 Skill 的安装和使用。

The community and paid resource pack are optional; neither is required to install or use this open-source skill.
<!-- gingiris-community-cta:end -->
