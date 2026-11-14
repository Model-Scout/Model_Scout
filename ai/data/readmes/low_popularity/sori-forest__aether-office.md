---
license: apache-2.0
base_model: Qwen/Qwen3.5-4B
language:
- ko
- en
- ja
pipeline_tag: text-generation
tags:
- gguf
- office
- offline
- lora
- lm-studio
---

# Aether Office v1.0

**An offline office-document assistant for Korean, English, and Japanese.**
No internet, no cloud — your documents never leave your computer.

[English](#english) · [한국어](#한국어) · [日本語](#日本語)

| File | Size | For |
|---|---|---|
| `aether-office-v1.0-Q4_K_M.gguf` | 2.78 GB | **Recommended.** Sized with 8 GB RAM devices in mind (not yet tested on such devices) |
| `aether-office-v1.0-Q3_K_M.gguf` | 2.32 GB | Smaller file. **Not evaluated** — all results below are for Q4_K_M |

---

## English

### What it does
- **Summarize** documents (keeps requested line counts and length)
- **Write and rewrite** business emails and memos in Korean, English, or Japanese business style
- **Extract** fields from invoices, contracts, and orders into **JSON only**
- **Answer only from the document** you give, and say plainly when the answer is **not in it**
- **Translate** business text between Korean, English, and Japanese
- Simple **office formulas** (Excel, regex, short scripts)

File size is 2.78 GB, chosen with 8 GB RAM devices in mind. It has not yet been tested on an actual 8 GB device.

### Quick start (LM Studio)
1. Download `aether-office-v1.0-Q4_K_M.gguf` and import it into LM Studio (**My Models → Import**).
2. Load the model and **turn Thinking off** in the model settings. Aether Office was trained to answer directly.
3. Paste the contents of the `system` file into the **System Prompt** box. Recommended: temperature 0.3, top_p 0.9.

Using the local API on Windows? Use `http://127.0.0.1:1234` instead of `localhost`. On Windows, `localhost` can add about 2 seconds to every request.

### Evaluation
Fixed 30-question set (ko/en/ja × summary, email, rewrite, JSON extraction, grounded answers, "not in the document" answers, translation). Automatic checks for format, required facts, language and refusals. Thinking off, same settings for both models, each model run twice.

| | Previous internal build | **Aether Office v1.0** |
|---|---|---|
| 30-question set, run 1 (all checks passed) | 29 / 30 | 29 / 30 |
| 30-question set, run 2 | 28 / 30 | 29 / 30 |
| Real-use test: Japanese 2-line summary of a holiday notice — keeps the "orders after Dec 25, 15:00 ship from Jan 5" date line | 3 / 8 answers | 5 / 5 answers |

- Aether Office v1.0 results were measured with the `system` prompt included in this repository.
- For reference, the base Qwen3.5-4B scored 17/30 on the same set (measured with the previous internal build, not re-measured here).
- Results move by 1–2 questions from run to run, so the difference on the 30-question set is within normal variation. The clearer change is the Japanese summary date line.
- The automatic checks do not fully measure writing quality.

### Known limitations
- **Run-to-run variation:** the same question can pass in one run and fail in the next (1–2 of 30 questions per run).
- **Human review was limited:** apart from the automatic checks, the answers a person read closely were the Japanese summary items only.
- **Summaries** can occasionally drop or alter a number or a comparison (e.g. a total amount, "vs. last month"). Check figures that matter.
- **AM/PM can flip:** a time can change between morning and afternoon (e.g. "3 p.m." became "3 a.m." when rewriting a memo as a notice). Always check dates and times.
- **Word swaps:** a word can be replaced by a similar but different word, changing the meaning (e.g. Korean 입고 "goods received" → 입금 "payment received"; "ship date" → "delivery date"). The base model (Qwen3.5-4B) showed the same behavior, and this training did not fully fix it. Review drafts before sending.
- **Emails** may add small details you did not ask for (placeholder company names).
- **Japanese honorifics:** high-stakes keigo can be off. Have a person check before sending.
- **Code:** only short office formulas and scripts. Not a general coding assistant.
- **Text only.** Images are not supported in this GGUF. Only Korean, English, and Japanese were trained.

### How it was made
- Base: Qwen3.5-4B (Apache-2.0). LoRA (r=16), 2 epochs, 1,400 examples (English 473, Japanese 472, Korean 455).
- The examples are the previous internal build's training set minus 40 summaries that dropped dates or amounts (summary data clean-up).
- Internal build name: v2.1.1.
- Training examples were drafted locally by Gemma 4 E4B (Apache-2.0), filtered by automatic checks (language, number formatting, invented numbers, JSON validity, unsafe code) and reviewed by people with AI assistance.
- Evaluation questions were kept out of the training data.

---

## 한국어

### 무엇을 하나요
- 문서 **요약** (줄 수·길이 지시를 지킵니다)
- 업무 **이메일·공문 작성과 다듬기** (한국어·영어·일본어 비즈니스 말투)
- 청구서·계약서·주문서에서 정보를 뽑아 **JSON만** 출력
- 입력한 **문서 안에서만 답하기**, 문서에 없으면 **없다고** 말하기
- 한·영·일 **업무 번역**
- 간단한 **사무 자동화** (엑셀 수식, 정규식, 짧은 스크립트)

인터넷 없이 내 컴퓨터에서만 돌아가므로, 회사 문서를 밖으로 내보내지 않아도 됩니다.
권장 파일(Q4_K_M)은 2.78GB로, 메모리 8GB 기기를 염두에 둔 크기입니다 (실제 8GB 기기에서는 아직 시험하지 않았습니다). 더 작은 Q3_K_M(2.32GB)은 평가하지 않았습니다.

### 시작하기 (LM Studio)
1. `aether-office-v1.0-Q4_K_M.gguf` 를 받아 LM Studio에 불러옵니다 (**My Models → Import**).
2. 모델을 불러온 뒤 설정에서 **Thinking(생각)을 끕니다.** 바로 답하도록 학습되었습니다.
3. `system` 파일 내용을 **System Prompt** 칸에 붙여 넣습니다. 권장: temperature 0.3, top_p 0.9.

윈도우에서 로컬 API를 쓴다면 `localhost` 대신 `http://127.0.0.1:1234` 를 쓰세요. 윈도우에서는 `localhost` 가 요청마다 약 2초를 더 쓸 수 있습니다.

### 평가
고정된 30문항(한·영·일 × 요약, 이메일, 재작성, JSON 추출, 근거 답변, "문서에 없음" 답변, 번역)을 형식·핵심 사실·언어·거절 여부로 자동 채점했습니다. Thinking 끔, 두 모델 같은 조건, 각각 2회.

| | 이전 내부 버전 | **Aether Office v1.0** |
|---|---|---|
| 30문항 1회차 (전 항목 통과) | 29 / 30 | 29 / 30 |
| 30문항 2회차 | 28 / 30 | 29 / 30 |
| 실사용 시험: 일본어 연말연시 휴업 안내 2줄 요약에서 "12월 25일 15시 이후 주문은 1월 5일 이후 발송" 날짜 줄 유지 | 8번 중 3번 | 5번 중 5번 |

- Aether Office v1.0 결과는 이 저장소에 함께 있는 `system` 프롬프트로 잰 것입니다.
- 참고로 학습 전 Qwen3.5-4B는 같은 문항에서 17/30이었습니다 (이전 내부 버전 때 측정, 이번에 다시 재지 않음).
- 회차마다 1~2문항씩 결과가 흔들리므로, 30문항 점수 차이는 흔들림 범위 안입니다. 더 분명한 변화는 일본어 요약의 날짜 줄입니다.
- 자동 채점은 문장의 품질까지 완전히 재지는 못합니다.

### 한계
- **회차마다 흔들림:** 같은 문항이 한 번은 통과하고 다음에는 실패할 수 있습니다 (회차마다 30문항 중 1~2개).
- **사람의 확인 범위:** 자동 채점 외에 사람이 답을 직접 읽어 확인한 것은 일본어 요약 문항뿐입니다.
- **요약**에서 숫자나 비교 기준(합계 금액, "전월 대비" 등)을 빠뜨리거나 바꿀 수 있습니다. 중요한 숫자는 확인하세요.
- **오전/오후 바뀜:** 시간의 오전/오후가 바뀔 수 있습니다 (예: 메모를 공지문으로 바꿀 때 "오후 3시" → "오전 3시"). 날짜·시간은 반드시 확인하세요.
- **단어 바뀜:** 단어를 비슷한 다른 단어로 바꿔 뜻이 달라질 수 있습니다 (예: 입고→입금, 발송일→도착일). 기본 모델(Qwen3.5-4B)에서도 같은 현상이 있었고, 이번 학습으로 완전히 고쳐지지 않았습니다. 보내기 전에 확인하세요.
- **이메일**에 요청하지 않은 세부 내용(가상의 회사 이름)을 넣을 때가 있습니다.
- **일본어 고급 경어**는 어색할 수 있으므로, 보내기 전에 사람이 확인하세요.
- **코드**는 짧은 사무용 수식·스크립트 수준이며, 일반 코딩용 모델이 아닙니다.
- **글자 전용**입니다. 이 GGUF는 이미지를 지원하지 않습니다. 한국어·영어·일본어만 학습했습니다.

### 만든 방법
- 바탕: Qwen3.5-4B (Apache-2.0). LoRA (r=16), 2회 학습, 예시 1,400개 (영어 473, 일본어 472, 한국어 455).
- 예시는 이전 내부 버전의 학습 데이터에서 날짜·금액을 빠뜨린 요약 40개를 뺀 것입니다 (요약 데이터 품질 정리).
- 내부 개발 이름 v2.1.1.
- 학습 예시는 Gemma 4 E4B(Apache-2.0)로 로컬에서 초안을 만들고, 자동 검사(언어, 숫자 표기, 지어낸 숫자, JSON 형식, 위험한 코드)와 AI 도움을 받은 사람 검토를 거쳤습니다.
- 평가 문항은 학습 데이터에 넣지 않았습니다.

---

## 日本語

### できること
- 文書の**要約**(行数・長さの指定を守ります)
- ビジネス**メール・社内文書の作成と書き直し**(日・英・韓のビジネス文体)
- 請求書・契約書・注文書から項目を抜き出し、**JSONのみ**で出力
- 入力した**文書の内容だけで回答**し、記載がなければ**「記載はありません」**と答える
- 日・英・韓の**ビジネス翻訳**
- 簡単な**事務自動化**(Excel関数、正規表現、短いスクリプト)

インターネット不要。社内文書を外部に送らずに使えます。
推奨ファイル(Q4_K_M)は 2.78GB で、メモリ 8GB の機器を想定した大きさです(実際の 8GB 機器ではまだ試していません)。より小さい Q3_K_M(2.32GB)は評価していません。

### 使い方(LM Studio)
1. `aether-office-v1.0-Q4_K_M.gguf` をダウンロードし、LM Studio に読み込みます(**My Models → Import**)。
2. モデル設定で **Thinking(思考)をオフ**にします。すぐに答えるよう学習されています。
3. `system` ファイルの内容を **System Prompt** 欄に貼り付けます。推奨:temperature 0.3、top_p 0.9。

Windows でローカル API を使う場合は、`localhost` ではなく `http://127.0.0.1:1234` を使ってください。`localhost` ではリクエストごとに約2秒余分にかかることがあります。

### 評価
固定の30問(日・英・韓 × 要約、メール、書き直し、JSON抽出、文書に基づく回答、「記載なし」回答、翻訳)を、形式・必要な事実・言語・回答拒否の有無で自動採点しました。Thinking オフ、同一条件、各モデル2回。

| | 以前の内部版 | **Aether Office v1.0** |
|---|---|---|
| 30問・1回目(全項目合格) | 29 / 30 | 29 / 30 |
| 30問・2回目 | 28 / 30 | 29 / 30 |
| 実用テスト:年末年始休業のお知らせを2行で要約し、「12月25日15時以降のご注文は1月5日以降の発送」の日付を残せたか | 8回中3回 | 5回中5回 |

- Aether Office v1.0 の結果は、このリポジトリに含まれる `system` プロンプトで測定したものです。
- 参考:学習前の Qwen3.5-4B は同じ30問で 17/30 でした(以前の内部版の時に測定、今回は再測定していません)。
- 回ごとに1〜2問の差が出るため、30問の点数差は通常のばらつきの範囲内です。よりはっきりした変化は、日本語要約の日付の行です。
- 自動採点では文章の質までは十分に測れません。

### 制限事項
- **回ごとのばらつき:** 同じ問題が、ある回では合格し別の回では不合格になることがあります(30問中1〜2問)。
- **人による確認の範囲:** 自動採点以外に人が回答を読んで確認したのは、日本語の要約問題だけです。
- **要約**で金額などの数字や比較の基準(「前月比」など)が抜けたり変わったりすることがあります。重要な数字は確認してください。
- **午前・午後の入れ替わり:** 時刻の午前・午後が入れ替わることがあります(例:メモをお知らせ文に書き換える際に「午後3時」→「午前3時」)。日付・時刻は必ず確認してください。
- **言葉の置き換わり:** 似た別の言葉に置き換わり、意味が変わることがあります(例:韓国語の「입고(入庫)」→「입금(入金)」、「発送日」→「到着日」)。ベースモデル(Qwen3.5-4B)でも同じ現象があり、今回の学習でも完全には直っていません。送信前に確認してください。
- **メール**に、依頼していない内容(仮の社名)が入ることがあります。
- **改まった敬語**は不自然になることがあります。送信前に人が確認してください。
- **コード**は簡単な事務用の関数・スクリプト程度で、一般的なコーディング用ではありません。
- **テキスト専用**です。この GGUF は画像に対応していません。学習した言語は日本語・英語・韓国語のみです。

### 作り方
- ベース:Qwen3.5-4B(Apache-2.0)。LoRA(r=16)、2エポック、学習例 1,400件(英語 473、日本語 472、韓国語 455)。
- 学習例は以前の内部版の学習データから、日付・金額が抜けた要約40件を除いたものです(要約データの品質整理)。
- 内部開発名 v2.1.1。
- 学習例は Gemma 4 E4B(Apache-2.0)でローカルに下書きし、自動チェック(言語、数字表記、作られた数字、JSON形式、危険なコード)と、AIの補助を受けた人の確認を経ています。
- 評価問題は学習データに含めていません。

---

Made by **Luciver (sori-forest)**. Base model: [Qwen/Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B) (Apache-2.0).
