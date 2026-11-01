---
language:
- en
- vi
- ko
- es
- pt
- zh
- fr
- it
- de
- ja
- ru
- pl
- nl
- hi
- tr
- id
pretty_name: 'xllms - dialogue grettings'
dataset_info:
  features:
  - name: system
    dtype: string
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: hash
    dtype: string
  - name: languages
    sequence: string
  - name: tokens
    dtype: int64
  splits:
  - name: train
    num_bytes: 48746065.0
    num_examples: 41320
  download_size: 27680512
  dataset_size: 48746065.0
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# 👋 xLLMs – Dialogue Grettings

**xLLMs – Dialogue Grettings** is a **multilingual greeting & small-talk dataset** for building assistants that **recognize salutations, respond politely, elicit intent, and pivot from chit-chat to helpful task support**.  
It spans **41,320 dialogues** across **16 languages** (en, vi, ko, es, pt, zh, fr, it, de, ja, ru, pl, nl, hi, tr, id). Each sample is a short, natural exchange that begins with a greeting and evolves into a light informational micro-task.

> This dataset focuses on **conversational finesse** rather than knowledge grounding: tone, etiquette, language identification, follow-up prompts, and concise, age-appropriate explanations.

## 🌍 Why This Dataset Matters

| Design Aspect                                        | Impact on Model Quality |
| ---------------------------------------------------- | ----------------------- |
| **Greeting & intent handoff**                        | Teaches models to *acknowledge*, *offer help*, then *clarify intent* without friction. |
| **Multilingual salutations & tone**                  | Improves *language ID*, *polite forms*, and culturally appropriate phrasing. |
| **Short, purposeful follow-ups**                     | Encourages *clarifying questions* that quickly uncover user goals. |
| **Kid-friendly micro-explanations**                  | Trains *concise, simple, non-patronizing* explanations for general audiences. |
| **Consistency in roles & structure**                 | Stabilizes turn-taking behavior and response formatting for production assistants. |

## 📊 Dataset Metadata

**Pretty name:** `xllms - dialogue grettings`  
**Languages (16):** en, vi, ko, es, pt, zh, fr, it, de, ja, ru, pl, nl, hi, tr, id

| Split | #Examples |   Size (bytes) |
| :---- | --------: | -------------: |
| train |    41,320 |     48,746,065 |

- **Download size:** 27,680,512 bytes  
- **Total dataset size:** 48,746,065 bytes

### Features
- `system: string` – optional system prompt seed  
- `messages: list` of `{ content: string, role: string }` *(note the order: `content` then `role`)*  
- `hash: string` – dialogue identifier  
- `languages: sequence<string>` – detected languages per dialogue  
- `tokens: int64` – token count (per conversation)

### Config
- `default` → `data/train-*`

## 💬 Representative Examples  
*(Each includes **why it’s good** & **what it trains** to make the dataset’s focus explicit.)*

### 🇵🇹 Portuguese — From greeting → curiosity → concise teaching
- **Why this example is good:** Quick *“Olá” → offer help → child-friendly science*; progressive follow-ups and actionable tips.  
- **Targets to improve:** polite greeting templates, age-appropriate explanations, summarizing environment benefits, simple actionables.

```json
[
  {"content": "", "role": "system"},
  {"content": "Olá", "role": "user"},
  {"content": "Olá! Como posso ajudá-lo hoje?", "role": "assistant"},
  {"content": "Estou aprendendo sobre plantas na escola. Por que as plantas são importantes?", "role": "user"},
  {"content": "As plantas são muito importantes porque elas nos fornecem oxigênio para respirar e alimento para muitos animais. Elas também ajudam a manter o ar e a água limpos.", "role": "assistant"},
  {"content": "Isso faz sentido. O que mais as plantas fazem pelo meio ambiente?", "role": "user"},
  {"content": "As plantas ajudam a prevenir a erosão do solo, fornecem abrigo para os animais e sustentam ecossistemas inteiros como florestas e recifes de corais.", "role": "assistant"},
  {"content": "Isso é muito legal. Como posso ajudar a cuidar das plantas?", "role": "user"},
  {"content": "Você pode ajudar regando-as, fornecendo luz solar e mantendo o ar ao redor delas limpo. Você também pode plantar mais árvores e flores em sua comunidade para torná-la um lugar mais verde e saudável.", "role": "assistant"}
]
````

### 🇸🇪 Swedish — Greeting → culinary choice → brief comparison

* **Why this example is good:** Immediate help after “Hej!”, practical recommendation, **contrastive** explanation (vegetable vs rapeseed oil), positive closure.
* **Targets to improve:** domain-lite comparisons, neutral tone, “acknowledge → answer → compare → encourage”.

```json
[
  {"content": "", "role": "system"},
  {"content": "Hej!", "role": "user"},
  {"content": "Hej! Hur kan jag hjälpa dig idag?", "role": "assistant"},
  {"content": "Jag ska laga stekt kyckling till middag, men jag är inte säker på vilken olja jag ska använda.", "role": "user"},
  {"content": "Till stekt kyckling kan du använda vegetabilisk olja, jordnötsolja eller rapsolja. De har en hög rökpunkt, vilket gör dem idealiska för stekning.", "role": "assistant"},
  {"content": "Vad är skillnaden mellan vegetabilisk olja och rapsolja?", "role": "user"},
  {"content": "Vegetabilisk olja är en blandning av olika oljor, medan rapsolja är tillverkad av rapsfrö. Rapsolja har en mildare smak och anses generellt vara nyttigare.", "role": "assistant"},
  {"content": "Okej, då tror jag att jag tar rapsolja.", "role": "user"},
  {"content": "Det låter som ett bra val. Smaklig spis på stekt kycklingen!", "role": "assistant"}
]
```

### 🇯🇵 Japanese — Greeting → family skills → positive reinforcement

* **Why this example is good:** Polite *こんにちは* register, **active listening** concept, **positive reinforcement** with concrete phrasing.
* **Targets to improve:** formality control (JP), short actionable examples, empathy signals.

```json
[
  {"content": "", "role": "system"},
  {"content": "やあ", "role": "user"},
  {"content": "こんにちは。今日は何をしてあげましょうか？", "role": "assistant"},
  {"content": "家族とのコミュニケーションを改善しようとしているんですが、何か方法はないでしょうか？", "role": "user"},
  {"content": "それは素晴らしいですね！1つの方法はアクティブリスニングを実践することです。つまり、相手が話すことに注意を払い、その考えや気持ちに自分が関心があることを示すということです。",
   "role": "assistant"},
  {"content": "それは役立ちそうです。家族のコミュニケーションを改善する別の方法はありますか？", "role": "user"},
  {"content": "もう1つの方法は、心からの褒め言葉や感謝の気持ちを表現するなどのポジティブな強化を使用することです。これにより、より支え合っていて愛情のある環境を作ることができます。", "role": "assistant"},
  {"content": "すばらしい考えですね。家族の中でポジティブな強化を使用する方法の例を教えてもらえますか？", "role": "user"},
  {"content": "例えば、「今夜、夕食を手伝ってくれてありがとう。本当に助かりました。」と言うことができます。これは彼らの努力に感謝し、彼らの貢献を評価していることを示します。", "role": "assistant"}
]
```

### 🇻🇳 Vietnamese — Greeting → pet care → tool choice & sequencing

* **Why this example is good:** Friendly opener, **frequency guidance**, **tool distinction** (brush vs comb), and **ordered routine**.
* **Targets to improve:** brief care schedules, vocabulary precision, step-by-step grooming advice.

```json
[
  {"content": "", "role": "system"},
  {"content": "Xin chào", "role": "user"},
  {"content": "Xin chào! Hôm nay tôi có thể giúp gì cho bạn?", "role": "assistant"},
  {"content": "Tôi có một con mèo và tôi không biết nên chải lông cho nó bao nhiêu lần.", "role": "user"},
  {"content": "Chải lông thường xuyên cho mèo có thể giúp giảm rụng lông và ngăn ngừa búi lông. Tốt nhất bạn nên chải lông cho mèo ít nhất 2-3 lần một tuần, tùy thuộc vào loại lông và độ dài lông của mèo.", "role": "assistant"},
  {"content": "Sự khác biệt giữa lược và chải lông cho mèo là gì?", "role": "user"},
  {"content": "Lược thường mềm và nhẹ nhàng hơn, dùng để chải sạch lông rụng và phân bổ dầu trên da. Chải lông thường được sử dụng để gỡ rối và chải sạch búi lông, đặc biệt là ở quanh tai và bàn chân.", "role": "assistant"},
  {"content": "Tôi có thể sử dụng cả lược và chải lông cùng lúc không?", "role": "user"},
  {"content": "Có, bạn có thể sử dụng cả lược và chải lông cùng lúc như một phần trong quy trình chải chuốt cho mèo. Trước tiên, hãy dùng chổi để loại bỏ lông rụng, sau đó dùng lược để gỡ nhẹ nhàng những nút thắt hoặc búi lông.", "role": "assistant"}
]
```

## 🔧 How to Use This Dataset

* **Greeting detection & response selection** (map from salutation to polite, language-matched reply).
* **Intent elicitation** (ask one clear, low-friction follow-up question).
* **Tone & register control** (friendly, concise, non-patronizing).
* **Micro-explanations** (short, correct, audience-appropriate).
* **Multilingual robustness** (language ID and culturally appropriate phrasing).

## 📜 Citation

```
@dataset{xllms_dialogue_grettings,
  title       = {xLLMs – Dialogue Grettings},
  year        = {2025},
  languages   = {en, vi, ko, es, pt, zh, fr, it, de, ja, ru, pl, nl, hi, tr, id},
  description = {Multilingual greeting & small-talk dialogues focused on salutations, intent elicitation, and polite, concise help across 16 languages.}
}
```

## ⚖️ License & Attribution

Use is permitted for **research and development** subject to the dataset’s page terms. When using or redistributing, **please attribute the source**:

> *xLLMs – Dialogue Grettings (2025). Multilingual greeting & small-talk dataset. Hugging Face: xllms/dialogue-grettings.*
