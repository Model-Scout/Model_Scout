---
dataset_info:
  features:
  - name: en_prompt
    dtype: string
  - name: dataset_name
    dtype: string
  - name: language
    dtype: string
  - name: translated_prompt_raw
    dtype: string
  - name: num_tokens
    dtype: int64
  - name: translated_prompt
    dtype: string
  - name: is_valid_prompt
    dtype: bool
  - name: row_id
    dtype: int64
  - name: res_finish_reason
    dtype: string
  - name: response
    dtype: string
  - name: is_valid_think
    dtype: bool
  - name: is_valid_res
    dtype: bool
  - name: think_lang
    dtype: string
  - name: res_lang
    dtype: string
  - name: think_fluency
    dtype: float64
  - name: prompt_think_lang_correct
    dtype: bool
  - name: answer_correctness
    dtype: float64
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  splits:
  - name: train
    num_bytes: 23131354
    num_examples: 2477
  download_size: 9404172
  dataset_size: 23131354
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
language:
- am
- ar
- bn
- zh
- cs
- nl
- en
- fr
- de
- el
- ha
- he
- hi
- id
- it
- ja
- jv
- km
- ko
- lo
- ms
- mr
- fa
- pl
- pt
- ro
- ru
- es
- sw
- sv
- tl
- ta
- te
- th
- tr
- uk
- ur
- vi
---

# lightblue/reasoning-multilingual-R1-Llama-70B-train

This is a multilingual reasoning dataset covering more than 30 languages.

This dataset was made by:

1. Sampling prompts from English datasets and translating them to various languages
2. Generating responses to these prompts 8 times using deepseek-ai/DeepSeek-R1-Distill-Llama-70B
3. Filtering out \<think\> sections with incorrect language, non-fluent language, and incorrect answers

This dataset was then used to train a multilingual reasoning finetune of the [R1 distills](https://huggingface.co/collections/deepseek-ai/deepseek-r1-678e1e131c0169c0bc89728d).

The reason we made this dataset was that we found it incredibly difficult to consistently generate \<think\> sections (Chain-of-Though processes) in the language that the R1 model was prompted. 
Therefore, we generated many responses using one of these models and removed the ones which were not in the original language of the prompt. 
This serves to make these models more understandable, more interpretable, more accountable, and more transparent to users of these LLMs outside of English and Chinese.

# Code for making this dataset

### 1. Sample prompts from English datasets and translate them

```python
from FlagEmbedding import BGEM3FlagModel
from datasets import load_dataset, concatenate_datasets
import numpy as np
import torch
import math
import random
from openai import OpenAI
from google.colab import userdata

def sample_datasets():
    argilla_ds = load_dataset("argilla/distilabel-reasoning-prompts", split="train").map(
        lambda x: {"en_prompt": x["instructions"], "dataset_name": "distilabel-reasoning-prompts"},
        num_proc=12
    )
    
    oasst_ds = load_dataset("OpenAssistant/oasst2", split="train").filter(
        lambda x: x["parent_id"] is None, num_proc=12
    ).filter(
        lambda x: x["lang"] == "en", num_proc=12
    ).map(
        lambda x: {"en_prompt": x["text"], "dataset_name": "oasst2"},
        num_proc=12
    ).shuffle().select(
        range(1000)
    )
    
    hfcode_ds = load_dataset("HuggingFaceH4/code_alpaca_20_k", split="train").map(
        lambda x: {"en_prompt": x["prompt"], "dataset_name": "CodeAlpaca_20K"},
        num_proc=12
    ).shuffle().select(
        range(1000)
    )
    
    ds = concatenate_datasets([
        hfcode_ds,
        oasst_ds,
        argilla_ds,
    ]).select_columns(["en_prompt", "dataset_name"])
    
    ds = ds.map(lambda x: {
        "en_prompt": x["en_prompt"].strip()
    })

    return ds

def deduplicate_dataset(ds):
    model = BGEM3FlagModel('BAAI/bge-m3', use_fp16=True)
    
    embeddings = torch.Tensor(
        model.encode(ds["en_prompt"])['dense_vecs']
    ).to(torch.device("cuda"))

    # Remove the second instance of any row pairs which at least 0.9 cosine similarity
    sims = (embeddings @ embeddings.T).cpu().numpy()
    np.fill_diagonal(sims, 0)
    rm_idx = set([max(x) for x in zip(*np.where(sims >= 0.9))])
    ds = ds.select([i for i in range(len(ds)) if i not in rm_idx])

    return ds

def add_languages_to_ds(ds):

    unique_languages = [
        "English", "Chinese",
        "Swahili", "Hausa", "Yoruba", "Telugu", "Tamil", "Marathi", "Javanese", "Punjabi", # Not in original Qwen training
        "Amharic", "Ukrainian", "Swedish", "Greek", "Romanian", # Not in original Qwen training
        "German", "French", "Spanish", "Portuguese", "Italian", "Dutch",
        "Russian", "Czech", "Polish",
        "Arabic", "Persian", "Hebrew", "Turkish",
        "Japanese", "Korean",
        "Vietnamese", "Thai", "Indonesian", "Malay", "Lao", "Burmese", "Cebuano", "Khmer", "Tagalog",
        "Hindi", "Bengali", "Urdu"
    ]

    rows_per_language = math.floor(len(ds) / len(unique_languages))
    
    language_list = []
    for unique_language in unique_languages:
        language_list.extend([unique_language] * int(rows_per_language))
    
    language_list = language_list + random.sample(unique_languages, len(ds) - len(language_list))
    
    ds = ds.shuffle().add_column("language", language_list)

    return ds

client = OpenAI(api_key=userdata.get("OPENAI_API_KEY"))

def translate_prompt(row, max_completion_tokens=500):
    
    language = row["language"]

    if language == "English":
        return {
            "translated_prompt_raw": row["en_prompt"],
            "num_tokens": -1
        }

    translation_system_message = """You are a prompt translation AI. Given a target language and a prompt in English, translate it into an prompt in the target language. Surround the translation in <translation></translation> tags."""

    translation_examples = [
        {"role": "user", "content": "<Japanese>\nWhat is the eccentricity of the ellipse $\frac{x^{2}}{3}+\frac{y^{2}}{4}=1$?"},
        {"role": "assistant", "content": "<translation>\n楕円$\frac{x^{2}}{3}+\frac{y^{2}}{4}=1$の離心率はいくつですか？\n</translation>"},
        {"role": "user", "content": "<French>\nContrast the implications of two eigenvectors being orthogonal versus being linearly independent."},
        {"role": "assistant", "content": "<translation>\nComparez les implications lorsque deux vecteurs propres sont orthogonaux par rapport à lorsqu’ils ne sont que linéairement indépendants.\n</translation>"},
        {"role": "user", "content": "<German>\nHow many cells are there in the human body?"},
        {"role": "assistant", "content": "<translation>\nWie viele Zellen gibt es im menschlichen Körper?\n</translation>"},
    ]


    response = client.chat.completions.create(
      model="gpt-4o-2024-11-20",
      messages=[
        {
          "role": "system",
          "content": [
            {
              "type": "text",
              "text": translation_system_message
            }
          ]
        }]+translation_examples+[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "<" + language + ">\n"+ row["en_prompt"]
            }
          ]
        }
      ],
      response_format={
        "type": "text"
      },
      temperature=0.2,
      max_completion_tokens=max_completion_tokens,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    if response.choices[0].finish_reason == "stop":
        return {
          "translated_prompt_raw": response.choices[0].message.content,
          "num_tokens": response.usage.completion_tokens
        }
    else:
        return {
          "translated_prompt_raw": None,
          "num_tokens": -1
        }

def process_prompt(prompt_raw):
    if prompt_raw is None:
        return None

    prompt_raw = prompt_raw.strip()
    
    if not prompt_raw.startswith("<translation>") or not prompt_raw.endswith("</translation>"):
        return None
    
    return prompt_raw[len("<translation>"):-len("</translation>")].strip()


ds = sample_datasets()

ds = add_languages_to_ds(ds)

ds = ds.map(
    lambda x: translate_prompt(x),
    num_proc=64
)

ds = ds.map(lambda x: {
    "translated_prompt": x["translated_prompt_raw"] if x["language"] == "English" else process_prompt(x["translated_prompt_raw"])
})

ds = ds.map(lambda x: {
    "is_valid_prompt": isinstance(
            x["translated_prompt"], str
        ) and bool(
            x["num_tokens"] < 250
        )
})

ds.push_to_hub(
    "lightblue/reasoning-multilingual",
    split="train",
    private=True
)

```

### 2. Generate responses from deepseek-ai/DeepSeek-R1-Distill-Llama-70B

```python
from datasets import load_dataset, concatenate_datasets
from vllm import LLM, SamplingParams

examples = [
    {"role": "user", "content": "Wie viele Zellen gibt es im menschlichen Körper?\n<Deutsch>"},
    {"role": "assistant", "content": """<think>
Die Frage ist, wie viele Zellen im menschlichen Körper existieren. Um dies zu beantworten, muss ich verschiedene Faktoren berücksichtigen.

Zunächst denke ich an die Größe eines durchschnittlichen Menschen. Ein Erwachsener wiegt etwa 70 Kilogramm. Davon entfallen ungefähr 30 Kilogramm auf Wasser, was bedeutet, dass der Rest aus Zellen und anderen Materialien besteht.

Als nächstes frage ich mich, wie viel eine einzelne Zelle wiegt. Die meisten Zellen sind mikroskopisch klein, und ich vermute, dass eine typische Zelle etwa 1 Nanogramm wiegt. Das ist 10^-9 Gramm.

Mit diesen Zahlen kann ich nun eine grobe Schätzung vornehmen. Wenn ich die Gesamtmasse der Zellen durch das Gewicht einer einzelnen Zelle teile, erhalte ich die Anzahl der Zellen. Das ergibt ungefähr 30.000 bis 40.000 Milliarden Zellen.

Ich bin mir bewusst, dass dies eine grobe Schätzung ist, da Zellen unterschiedliche Größen und Gewichte haben können. Dennoch gibt mir das eine Vorstellung davon, wie viele Zellen der menschliche Körper enthält.
</think>

**Antwort:**

Der menschliche Körper besteht aus ungefähr 30 bis 40 Billionen Zellen."""},
    {"role": "user", "content": "Le soi est-il une illusion ?\n<Français>"},
    {"role": "assistant", "content": """<think>
Tout d'abord, je dois comprendre ce qu'est le "soi". Le soi fait référence à notre sens de l'identité personnelle, à notre conscience de nous-mêmes en tant qu'individus distincts. Cela inclut nos pensées, nos émotions, nos expériences et nos souvenirs, qui nous définissent en tant que personnes uniques.

Ensuite, je me demande pourquoi certaines personnes ou théories considèrent le soi comme une illusion. Peut-être parce que tout ce que nous percevons, y compris nous-mêmes, est construit par notre cerveau à partir de sensations et d'informations externes. Si notre perception de la réalité est subjective et sujette à des distorsions, notre sens du soi pourrait être une construction mentale plutôt qu'une réalité objective.

Je dois aussi penser aux différentes perspectives philosophiques et scientifiques sur cette question. Par exemple, le bouddhisme parle du "non-soi" (anatta), suggérant que le concept de soi est une illusion créée par l'ego. D'un point de vue scientifique, les neurosciences montrent que le cerveau construit notre identité à partir de multiples processus cognitifs, ce qui pourrait soutenir l'idée que le soi n'est pas une entité fixe ou essentielle.

Cependant, même si le soi est une construction, il reste une expérience subjective très réelle pour chacun de nous. Même si notre perception de nous-mêmes est influencée par divers facteurs, le sentiment d'exister en tant qu'individu avec des pensées et des émotions propres est inhérent à notre conscience humaine.

En conclusion, le débat sur le soi étant une illusion ou non dépend de la perspective adoptée. D'un côté, il peut être vu comme une construction mentale et sociale, et de l'autre, il représente une expérience intime et essentielle de notre existence.
</think>

Le soi est une question complexe qui a été explorée par divers domaines tels que la philosophie, la psychologie et les neurosciences. Voici une analyse organisée de cette question :

1. **Compréhension du concept de soi**:
   - Le soi se réfère à notre sentiment d'identité personnelle, englobant nos pensées, émotions, expériences et souvenirs. Il s'agit de ce qui nous distingue en tant qu'individus uniques.

2. **Arguments pour considérer le soi comme une illusion**:
   - **Perception subjective**: Notre perception de la réalité est construite par notre cerveau à partir de sensations et d'informations externes, qui peuvent être sujettes à des distorsions. Par conséquent, notre sens du soi pourrait être une construction mentale plutôt qu'une réalité objective.
   - **Influence des facteurs externes**: Les expériences, l'environnement et les interactions sociales influencent notre identité, suggérant que le soi est une construction dynamique plutôt qu'une entité fixe.
   - **Perspectives philosophiques**: Le bouddhisme, par exemple, soutient le concept du "non-soi" (anatta), où le soi est perçu comme une illusion créée par l'ego.

3. **Arguments contre l'idée que le soi est une illusion**:
   - **Expérience subjective**: Même si le soi est une construction, il reste une expérience intime et réelle pour chaque individu. Le sentiment d'exister en tant qu'entité distincte avec des pensées et des émotions propres est central à la conscience humaine.
   - **Nécessité fonctionnelle**: Le soi joue un rôle crucial dans la cohérence de notre comportement, la prise de décision et la création de buts personnels.

4. **Perspectives scientifiques**:
   - Les neurosciences montrent que le cerveau construit notre identité à travers de multiples processus cognitifs, ce qui soutient l'idée que le soi est une construction. Cependant, cela ne nie pas l'expérience subjective de l'individu.

5. **Conclusion**:
   Le débat sur le soi étant une illusion ou non dépend de la perspective adoptée. D'un côté, il peut être vu comme une construction mentale et sociale, et de l'autre, il représente une expérience intime et essentielle de notre existence. Ainsi, le soi est à la fois une construction dynamique et une réalité subjective profondément ancrée dans notre conscience.
"""},
    {"role": "user", "content": "顧客の名前、メールアドレス、住所を収集するHTMLフォームを作成してください。\n<日本語>"},
    {"role": "assistant", "content": """<think>
まず、必要な情報を収集するために、フォームに名前、メールアドレス、住所のフィールドを含める必要があります。名前はテキスト入力欄、メールアドレスはメール入力欄、住所はテキスト入力欄として設定します。各フィールドにラベルを付けて、ユーザーが入力する内容を明確にします。送信ボタンを追加し、フォームの送信時にデータが正しく送られるようにします。最後に、フォームの整体的なレイアウトを整理し、ユーザーが簡単に使用できるようにします。
</think>

以下に、顧客の名前、メールアドレス、住所を収集するためのHTMLフォームの例を示します。

\`\`\`html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>顧客情報登録フォーム</title>
</head>
<body>
    <h1>顧客情報登録フォーム</h1>
    
    <form action="/submit" method="POST">
        <div>
            <label for="name">名前：</label>
            <input type="text" id="name" name="name" required>
        </div>
        
        <div>
            <label for="email">メールアドレス：</label>
            <input type="email" id="email" name="email" required>
        </div>
        
        <div>
            <label for="address">住所：</label>
            <input type="text" id="address" name="address" required>
        </div>
        
        <button type="submit">送信</button>
    </form>
</body>
</html>
\`\`\`

### 解説：
1. **フォームの作成**：`<form>`タグでフォームを定義します。`action`属性にフォームデータを送信先のURLを指定し、`method`属性に送信方法（例：POST）を指定します。
2. **名前の入力**：`<input type="text">`を使用して名前を入力できるフィールドを作成します。`required`属性を追加して入力必須にします。
3. **メールアドレスの入力**：`<input type="email">`を使用してメールアドレスを入力できるフィールドを作成します。`required`属性を追加して入力必須にします。
4. **住所の入力**：`<input type="text">`を使用して住所を入力できるフィールドを作成します。`required`属性を追加して入力必須にします。
5. **送信ボタン**：`<button type="submit">`を使用して送信ボタンを作成します。

このフォームでは、ユーザーが必要な情報を入力し、送信ボタンを押すと指定されたURLにデータが送信されます。"""}
]

lang_map = {
    'Amharic': 'አማርኛ',
    'Arabic': 'العربية',
    'Bengali': 'বাংলা',
    'Burmese': 'မြန်မာစာ',
    'Cebuano': 'Binisaya',
    'Chinese': '中文',
    'Czech': 'Čeština',
    'Dutch': 'Nederlands',
    'English': 'English',
    'French': 'Français',
    'German': 'Deutsch',
    'Greek': 'Ελληνικά',
    'Hausa': 'Hausa',
    'Hebrew': 'עברית',
    'Hindi': 'हिन्दी',
    'Indonesian': 'Bahasa Indonesia',
    'Italian': 'Italiano',
    'Japanese': '日本語',
    'Javanese': 'Basa Jawa',
    'Khmer': 'ភាសាខ្មែរ',
    'Korean': '한국어',
    'Lao': 'ພາສາລາວ',
    'Malay': 'Bahasa Melayu',
    'Marathi': 'मराठी',
    'Persian': 'فارسی',
    'Polish': 'Polski',
    'Portuguese': 'Português',
    'Punjabi': 'ਪੰਜਾਬੀ',
    'Romanian': 'Română',
    'Russian': 'Русский',
    'Spanish': 'Español',
    'Swahili': 'Kiswahili',
    'Swedish': 'Svenska',
    'Tagalog': 'Tagalog',
    'Tamil': 'தமிழ்',
    'Telugu': 'తెలుగు',
    'Thai': 'ภาษาไทย',
    'Turkish': 'Türkçe',
    'Ukrainian': 'Українська',
    'Urdu': 'اُردُو',
    'Vietnamese': 'Tiếng Việt',
    'Yoruba': 'Yorùbá'
}


llm = LLM(
    model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B", 
    tensor_parallel_size=8,
    enable_prefix_caching=True
)

ds = load_dataset("lightblue/reasoning-multilingual", split="train")
ds = ds.add_column("row_id", list(range(len(ds))))
ds = ds.filter(lambda x: x["is_valid_prompt"])
repeat_num = 8
cat_ds = concatenate_datasets([ds] * repeat_num)

conversations = [
    [{
        "role": "system",
        "content": f"You receive a prompt and a language tag as inputs. Answer the prompt in the given language, making sure to also think in that language.",
    }] + examples + [{
        "role": "user",
        "content": text + "\n<" + lang_map[lang] + ">",
    }] for lang, text in zip(cat_ds["language"], cat_ds["translated_prompt"])
]

sampling_params = SamplingParams(temperature=0.5, max_tokens=2048)

outputs = llm.chat(conversations,
                   sampling_params=sampling_params,
                   continue_final_message=False,
                   add_generation_prompt=True)

finish_reasons = [x.outputs[0].finish_reason for x in outputs]
responses = [x.outputs[0].text for x in outputs]

cat_ds = cat_ds.add_column("res_finish_reason", finish_reasons)
cat_ds = cat_ds.add_column("response", responses)

cat_ds.push_to_hub("lightblue/reasoning-multilingual-R1-Llama-70B-multirow", private=True)
```

### 3. Filter out \<think\> sections with incorrect language and format training data

```python
from datasets import load_dataset
import pycld2 as cld2
import re
from datasets import Dataset
from openai import OpenAI
from google.colab import userdata
import httpx

def remove_markdown_code_blocks(text):
    # Remove code blocks from text to avoid incorrect language detection
    code_block_pattern = r"```.*?```"
    cleaned_text = re.sub(code_block_pattern, '', text, flags=re.DOTALL)
    return cleaned_text

def detect_language(text):
    if text is None:
        return None

    isReliable, textBytesFound, details = cld2.detect(
        remove_markdown_code_blocks(text)
    )

    if not isReliable:
        return None

    return details[0][0].replace("LAOTHIAN", "LAO")

def extract_think_block(text):
    pattern = r'^\s*<think>(.*?)</think>'
    match = re.search(pattern, text, re.DOTALL)  # re.DOTALL allows '.' to match newlines

    if match:
        return match.group(1).strip()
    else:
        return False

def extract_answer(text):
    if text.count("</think>") == 1:
        return text.split("</think>")[1].strip()
    else:
        return False

client = OpenAI(timeout=httpx.Timeout(15.0, read=5.0, write=5.0, connect=3.0), api_key=userdata.get("OPENAI_API_KEY"))

def parse_float(sys_msg, user_input, max_completion_tokens=4):
    response = client.chat.completions.create(
      model="gpt-4o-mini-2024-07-18",
      messages=[
        {
          "role": "system",
          "content": [
            {
              "type": "text",
              "text": sys_msg
            }
          ]
        }]+[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": user_input
            }
          ]
        }
      ],
      response_format={
        "type": "text"
      },
      temperature=0.0,
      max_completion_tokens=max_completion_tokens,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    if response.choices[0].finish_reason == "stop":
        try:
            return float(response.choices[0].message.content)
        except:
            return None
    else:
        return None

def evaluate_think_fluency(row):
    language = row["language"]

    think_block = extract_think_block(row["response"])

    if not isinstance(think_block, str):
        return None

    fluency_system_message = f"""You are a {language} fluency evaluation AI. Given a piece of text, give the fluency and naturalness of the {language} in the text a score from 1-5. Only include your final number in your output."""

    return parse_float(fluency_system_message, think_block)

def evaluate_correctness(row):
    language = row["language"]

    prompt = row["translated_prompt"]
    model_response = row["response"]

    if not isinstance(extract_think_block(model_response), str):
        return None

    correctness_system_message = f"""You are a {language} answer evaluation AI. Given a prompt and a chain-of-thought reasoning answer, rate the correctness of the answer with a score from 1-5. Only include your final number in your output."""

    return parse_float(correctness_system_message, 
                       "# Prompt\n" + prompt + "\n\n# Response\n" + model_response)

ds = load_dataset("lightblue/reasoning-multilingual-R1-Llama-70B-multirow", split="train")

# Validate answers
ds = ds.map(lambda x: {"is_valid_think": isinstance(extract_think_block(x["response"]), str)})
ds = ds.map(lambda x: {"is_valid_res": isinstance(extract_answer(x["response"]), str)})
ds = ds.map(lambda x: {"think_lang": detect_language(extract_think_block(x["response"])) if x["is_valid_think"] else None})
ds = ds.map(lambda x: {"res_lang": detect_language(extract_answer(x["response"])) if x["is_valid_res"] else None})
ds = ds.map(lambda x: {"think_fluency": evaluate_think_fluency(x)}, num_proc=32)
ds = ds.map(lambda x: {"answer_correctness": evaluate_correctness(x)}, num_proc=32)

ds = ds.map(lambda x: {
    "prompt_think_lang_correct": bool(
            x["is_valid_prompt"]
        ) and bool(
            x["is_valid_think"]
        ) and bool(
            x["res_finish_reason"] == "stop"
        ) and bool(
            x["think_lang"] is not None
        ) and bool(
            x["language"].lower() == x["think_lang"].lower()
        ) and bool(
            x["res_lang"] is not None
        ) and bool(
            x["language"].lower() == x["res_lang"].lower()
        ) and bool(
            x["think_fluency"] == 5
        ) and bool(
            x["answer_correctness"] == 5
        )
})

df = ds.to_pandas()
selected_df = df.groupby("row_id").apply(
    lambda x: x[x.prompt_think_lang_correct].sample(min(1, x.prompt_think_lang_correct.sum()))
)

selected_ds = Dataset.from_pandas(selected_df.reset_index(drop=True))

selected_ds = selected_ds.map(lambda x: {
    "conversations": {
        {"from": "human", "value": x["translated_prompt"]},
        {"from": "gpt", "value": x["response"]},
    }
})

selected_ds.push_to_hub("lightblue/reasoning-multilingual-R1-Llama-70B-train")
ds.push_to_hub("lightblue/reasoning-multilingual-R1-Llama-70B-train-nonunique")
```

# License

We have endeavoured to base our dataset only on source datasets which allow for fully free use. Therefore, we share this dataset with the Apache 2.0 license.

# Developed by

<a href="https://www.lightblue-tech.com">
<img src="https://www.lightblue-tech.com/wp-content/uploads/2023/08/color_%E6%A8%AA%E5%9E%8B-1536x469.png" alt="Lightblue technology logo" width="400"/>
</a>

This dataset was created by Peter Devine ([ptrdvn](https://huggingface.co/ptrdvn)) for Lightblue