# Free-registry harvest — XRPL issuers × MiCA × LEI

Mirror of Hugging Face csoai/registry-harvest-xrpl-mica-lei

## Download and use this snapshot

This page describes the published files in `nicktempleman/csoai-registry-harvest-xrpl-mica-lei`. Treat them as a dated snapshot: use the observation dates and limitations in the files and source notes below. A page edit does not refresh the measurements.

With the Kaggle CLI installed and authenticated:

```bash
kaggle datasets download -d nicktempleman/csoai-registry-harvest-xrpl-mica-lei -p ./dataset --unzip
```

Start by inspecting `lei-crosswalk.jsonl`. Keep its original bytes and record the Kaggle version before transforming or comparing results.

Published files include:

- `README.md`
- `manifest.jsonl`
- `lei-crosswalk.jsonl`
- `xrpl-mica-join.jsonl`
- `mica-art-issuers.json`
- `mica-emt-issuers.json`
- `xrpl-16-factrun.jsonl`
- `eurcv-multichain.jsonl`
- See the Data tab for all 12 files.

[Current GSPC board](https://councilof.ai/api/gspc) · [Methodology](https://councilof.ai/methodology/) · [Verify supported signed records](https://councilof.ai/gspc-verify/) · [Corrections](https://councilof.ai/claim-maintenance)

Apply the licence shown on this dataset. Published by Council of AI — Council for the Safety of Artificial Intelligence, operated by CSOAI Ltd. Measurement is not certification; a mirror or package is not evidence of current board admission or benchmark leadership.

---

> **Mirror.** This is a copy of https://huggingface.co/datasets/csoai/registry-harvest-xrpl-mica-lei at revision `94d60c2a93cd303b1f3bbcb02c7cffcc0e0561ff`, made 2026-09-29. The Hugging Face copy is the original; if the two differ, it wins.

# Free-registry harvest — XRPL issuers × MiCA × LEI

Public registers and public ledgers joined, read 2026-09-04T07:12:30Z. **Every source is free, keyless and re-runnable by
anyone.** No part of this needed a relationship, an API key, or anyone's permission.

## The finding

Of the 16 XRPL issued assets in the CSOAI reader, 5 join to a MiCA e-money-token authorisation.

| group | n | declares an on-chain domain | enforces allowlisting | retains freeze capability |
|---|---:|---:|---:|---:|
| MiCA-authorised EMTs | 5 | **1 / 5** | 1 / 5 | 5 / 5 |
| Not MiCA-authorised | 11 | **6 / 11** | 6 / 11 | 10 / 11 |

**Four of the five MiCA-authorised EMTs on XRPL declare no issuer `Domain` on their account root.**
EU authorisation and on-chain issuer disclosure are uncorrelated here, and the relationship runs
opposite to the intuitive direction.

**What this is not.** Declaring a `Domain` is not a MiCA requirement, so a blank field is not
non-compliance and nothing here is a compliance finding, a rating, or advice. It is one
deterministic fact — is the field set — read off a public ledger. The risk verdict is UNMEASURED.

## Method

- **XRPL** — `account_info` on the validated ledger via public rippled nodes. AccountRoot flags
  decoded: `lsfRequireAuth` (allowlisting), `lsfNoFreeze` (freeze capability renounced),
  `lsfGlobalFreeze`. `Domain` hex-decoded. No model, no judgement, no score.
- **MiCA** — ESMA register via the `casptracker.eu` mirror (CC-licensed), snapshot 2026-08-20:
  331 CASPs, 23 EMT issuers, **0 authorised ARTs**, 167 non-compliant warnings. This is a
  **mirror**, not ESMA directly; the ESMA CSV path in circulation returns HTML.
- **LEI** — GLEIF public API. Group-head resolution by exact legal name + country + registration
  status. A naive first-hit name match returns wrong entities (`HSBC` → a US entity marked
  INACTIVE; `Citi` → India; `JPMorgan` → Luxembourg), so that shortcut is not used here.
- **Issuer join** — name-normalised with a hand-checked alias map. The 11 non-matches are
  non-EU issuers that correctly hold no EMT authorisation, not lookup failures.

## Also in here

`lei-crosswalk.jsonl` resolves all 26 banks of the CSOAI SWIFT census to group LEIs — 26/26,
24 `ISSUED`, one **LAPSED** (MUFG Bank) and one **DUPLICATE** (Wells Fargo). Two banks needed
fulltext search; Shinhan Bank's legal name is registered in Hangul, which is why exact matching
missed it.

## Second pass — the register validates itself, offline

Every LEI in the ESMA CASP register can be checked with arithmetic alone: ISO 17442 is 20
alphanumeric characters whose base-36 digit expansion is `mod 97 == 1`. No API, no key, no
permission, no network.

**10 of the 335 rows in the CSV snapshot fail that check.** Four are the wrong length — one ends
in a full stop (`89450036UW3ID72T1M84.`) and two are 19 characters — and six fail the check
digits outright.

| home state | entity | LEI as published | fault |
|---|---|---|---|
| AT | OSL EU | `8945001TKX2A5OJMNR45` | check digits |
| CY | Noemon Finance Ltd | `25490004TC93R20KW073` | check digits |
| DE | Raiffeisenbank Falkenstein-Wörth | `391200236O6D9SGBE882` | check digits |
| ES | PROSEGUR CRYPTO | `59800G0P3PV13KLX615` | 19 characters |
| ES | FINTECH PAYMENTS PSC S.L. | `549300746K71T6YJCV41` | check digits |
| IE | Ramp Network | `89450036UW3ID72T1M84.` | 21 characters, trailing full stop |
| LU | B2C2 | `969500OA6NVZB5BXAB29` | check digits |
| MT | Strike | `984500457TABOA3BZ224` | check digits |
| NL | EU Internet Ventures \|EUIV\|BNXA | `69940000HAL9ODW3IMO22` | 21 characters |
| NL | Ari10 \| Ari10 NL \| WEB3 Technologies | `724500YJVIN0Q94ZZG5` | 19 characters |

Corroborated independently: all ten also fail to resolve against the GLEIF API, and **every**
GLEIF lookup failure across the 331 mirrored rows is explained by this. There were no genuine
"valid LEI, absent from GLEIF" cases.

Separately, four CASPs carry a well-formed LEI whose GLEIF registration is not current:
**Bitpanda** (`RETIRED`), **Cryptonow**, **Legend Trading** and **PAYTOP** (all `LAPSED`).

### Boundaries on this finding

- The fault is present in the **CSV snapshot as mirrored**, not introduced by the mirror's JSON
  conversion — checked against `source/CASPS.csv` directly. It is dated **2026-08-20** and is not
  a live ESMA pull; the ESMA CSV path in circulation returns HTML, so a live confirmation needs
  someone to open the register by hand.
- A malformed identifier in a register is a **data-quality fact, not a compliance finding**. It
  says nothing about the authorisation itself, the firm, or its conduct.
- The raw CSV holds 335 rows; the mirror's JSON keeps 331. That gap is unexplained here and the
  two counts are reported separately rather than reconciled.

## Correction recorded against my own first read

The warning list is **not** evidence of asymmetric enforcement across the EU. 165 of its 167
entries come from Italy's CONSOB — but the mirror's own note says it covers
*"CONSOB/IT, AFM/NL, NBS/SK only"*. That ratio is the dataset's stated scope, not a finding about
Europe. It is recorded here because the denominator error was nearly published as a result.

No XRPL issuer measured in this dataset appears on that warning list — a clean negative, stated
as one.

## Third pass — one instrument, two ledgers, no way to authenticate it

EURCV is the single most ledger-verifiable bank-adjacent instrument in existence: a MiCA-authorised
e-money token from a G-SIB subsidiary (Société Générale-FORGE, LEI `969500FX8K40ZDW4F377`), live on
four public chains. So it is the fair test of whether "on a public chain" means "verifiable".

It does not. On neither ledger can an outsider establish which issuer account is the real one.

**XRPL.** One issuer in our registry, `rUNaS5sqRuxZz6V7rBGhoSaZiVYA3ut4UL`, holding 120 trustlines.
It declares **no `Domain`**, so the standard two-way `xrp-ledger.toml` check has nothing to check
against. Our own identification rests on the XRPScan well-known directory — a third party, not the
issuer.

**Stellar.** **Eight distinct issuers publish an asset with the code `EURCV`.** On Stellar an asset
is the pair (code, issuer), so the code alone identifies nothing. And the pattern inverts what you
would expect:

| issuer | home_domain | auth_required | revocable | clawback | SEP-1 two-way check |
|---|---|---|---|---|---|
| `GCEYGIVOLA…` | **(none)** | **true** | true | true | UNCHECKABLE — nothing declared |
| `GD4NLHSEOF…` | stellar.dtcc.network | false | false | false | toml 200, names issuer back |
| `GDV2VT25MZ…` | eurcv.xlmmint.com | false | false | false | toml 200, names issuer back |
| `GAUZUBEC6A…` | eurcvtoken.space | false | false | false | **domain does not resolve** |
| `GCOITVQ7BQ…` | xmintstellar.org | false | false | false | **domain does not resolve** |
| `GDGYNXSM63…` | xmintstellar.org | false | false | false | **domain does not resolve** |
| `GDPJ5PBS2A…` | eurcv.io | false | false | false | **domain does not resolve** |
| `GAUQKYP3GL…` | (none) | false | false | false | UNCHECKABLE — nothing declared |

The **only** issuer configured like a regulated one — allowlisting, revocable authorisation and
clawback all enabled — publishes no domain at all. Four of the six that do publish a domain point
at DNS names that **do not resolve**.

**The issuer's own domain resolves nothing either.** `sgforge.com` serves neither
`/.well-known/stellar.toml` nor `/.well-known/xrp-ledger.toml` — both 404. Those are the two
standard machine-readable mechanisms by which an issuer states which addresses are its own.

### What this does and does not say

- It does **not** say any of these accounts is fraudulent, an impersonation, or unauthorised.
  Several may be test issuances, mirrors, or unrelated projects reusing a four-letter code, and
  that is exactly the point: **from public data you cannot tell.**
- It does **not** say Société Générale-FORGE has done anything wrong. Publishing a toml is not a
  MiCA requirement and its absence is not non-compliance.
- It does **not** identify SG-FORGE's official Stellar address. Nobody can, from these sources.
- Checked mechanisms are named exactly, so the claim is falsifiable: if SG-FORGE publishes its
  addresses somewhere else, one link overturns this and the finding should be withdrawn.

What it does say is narrow and deterministic: **the standard on-chain mechanism for binding an
issuer to an identity is unused here, on both ledgers, by the instrument with the strongest reason
to use it.** "On a public chain" and "independently verifiable" are not the same property, and this
is the measurement that separates them.

## Fourth pass — the pattern is systemic, and it is a stale pointer, not a missing one

**Ticker collision on Stellar is the norm, not the EURCV exception.** Distinct issuers publishing
the same asset code:

| code | distinct issuers | | code | distinct issuers |
|---|---:|---|---|---:|
| USDC | **428** | | EURCV | 8 |
| EURC | **67** | | EURI | 7 |
| EURT | 34 | | EURD | 5 |
| USDG | 21 | | EUROP | 3 |
| EURS | 20 | | USDQ | 2 |

Ten of the thirteen euro/dollar EMT codes checked are claimed by more than one issuer. A ticker on
Stellar carries no identity at all; only the (code, issuer) pair does.

**So the two-way domain binding is the only thing that can disambiguate — and it mostly is not
completed.** On XRPL, of 16 instruments:

- **10 declare no `Domain`**, so the check cannot start.
- 6 declare one. **Four complete the binding** — RLUSD (`ripple.com`), OUSG (`ondo.finance`), and
  Braza's USDB and BBRL (`tokens.brazacripto.com.br`) all serve an `xrp-ledger.toml` naming the
  issuer back.
- Two do not: Bitstamp and Circle both declare a domain that returns **404** for the toml.

**Only 4 of 16 XRPL instruments are fully bound to an identity by the standard mechanism.**

### The Circle case is the instructive one

Circle declares `circle.com` on **both** ledgers. `circle.com` serves neither
`/.well-known/xrp-ledger.toml` nor `/.well-known/stellar.toml` — both 404. But a valid Stellar
binding **does exist**: `centre.io/.well-known/stellar.toml` returns 200 and names Circle's
canonical Stellar issuer back.

That is not a missing proof. It is a **stale pointer** — the on-chain declaration points at
`circle.com` while the proof lives at `centre.io`, the legacy CENTRE consortium domain. The
binding is completable only by someone who already knows to look there, which is precisely the
out-of-band knowledge the mechanism exists to remove.

Note also `circle.io/.well-known/stellar.toml` returns 200 and does **not** name this issuer — a
third domain in the same family with a different answer.

### What this changes about the EURCV finding

It makes it less about one issuer and more about the mechanism. Publishing the binding works and
is cheap: Ripple, Ondo and Braza all do it correctly today. The gap is not technical capability.
It is that the largest regulated issuers either point somewhere stale (Circle) or declare nothing
at all (Société Générale-FORGE, on both ledgers).

**Boundary, unchanged:** none of this is a compliance finding. Serving a toml is not required by
MiCA or by any regulator. It is the ecosystem's own standard for saying "this address is mine",
and this measures who uses it.

**Lid:** 22 axes measured · 14 model fleets · 3 public leader scores · 8 fact runs · TIE is TIE · not a certificate.

출처: Kaggle (nicktempleman/csoai-registry-harvest-xrpl-mica-lei)
태그: 
라이선스: Attribution 4.0 International (CC BY 4.0)
수정일: 2026-09-29T07:06:01.577Z
