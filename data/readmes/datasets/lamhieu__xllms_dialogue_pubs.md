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
pretty_name: 'xllms - dialogue pubs'
dataset_info:
  features:
  - name: system
    dtype: string
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: tokens
    dtype: float64
  - name: hash
    dtype: string
  - name: languages
    sequence: string
  splits:
  - name: train
    num_bytes: 3488347874
    num_examples: 988866
  - name: test
    num_bytes: 35098603
    num_examples: 9887
  download_size: 1775333788
  dataset_size: 3523446477
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
---

# 🗣️ xLLMs – Dialogue Pubs

**xLLMs – Dialogue Pubs** is a **large-scale multilingual dialogue dataset** for training and evaluating **conversational LLMs** on long-context reasoning, factual grounding, multilingual agility, and tool use.  
It contains **nearly one million synthetic conversations** in **9 languages** — **en, vi, ko, es, pt, zh, fr, it, de** — with many dialogues reaching **tens of thousands of tokens** (tokenized with "Ghost 8B Beta").

The data were generated via **document-guided prompting** that instructs models to consult **Wikipedia, WikiHow, and scientific/technical materials** when composing Q&A and explanations. This reduces unsupported claims and improves coherence in multi-turn settings.

## 🌍 Why This Dataset Matters

| Design Aspect                                                        | Impact on Model Quality                                                                        |
| -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Document-based generation** (Wikipedia, WikiHow, scientific texts) | Encourages evidence-based answers and clearer, step-wise exposition → **lower hallucination**. |
| **Multi-turn, long-context dialogues**                               | Trains **discourse coherence**, **context carryover**, and **summary skills**.                 |
| **Multilingual & mixed-language**                                    | Improves **language ID**, **code-switch control**, and cross-lingual generalization.           |
| **Worked examples & critique**                                       | Strengthens **methodical reasoning**, arithmetic exactness, and **error awareness**.           |
| **Tool-augmented traces**                                            | Teaches **function calling**: list tools → choose → form args → interpret results.             |

## 📊 Dataset Metadata

**Pretty name:** `xllms - dialogue pubs`  
**Languages:** en, vi, ko, es, pt, zh, fr, it, de

| Split | #Examples |  Size (bytes) |
| :---- | --------: | ------------: |
| train |   988,866 | 3,488,347,874 |
| test  |     9,887 |    35,098,603 |

- **Download size:** 1,775,333,788 bytes
- **Total dataset size:** 3,523,446,477 bytes

**Features:** `system: string`, `messages: list[{role, content}]`, `tokens: float64`, `hash: string`, `languages: sequence<string>`  
**Config:** `default` → `data/train-*`, `data/test-*`

## 💬 Representative Examples (each includes: **why it’s good** & **what it trains**)

> These examples **replace earlier samples**. Each block shows the **exact JSON** and a brief rationale for why this pattern benefits training/eval.

### 🇪🇸 Grounded Military History (Spanish)

- **Why this example is good:** concise, factual narrative; multi-turn clarification; closes with summary & commentary.  
- **Targets to improve:** source-aware historical Q&A, turn-to-turn consistency, summary fidelity.

```json
[
  {
    "role": "system",
    "content": ""
  },
  {
    "role": "user",
    "content": "¿Qué papel desempeñó Kurt Meyer en la Segunda Guerra Mundial?"
  },
  {
    "role": "assistant",
    "content": "Kurt Meyer fue un militar alemán que alcanzó el rango de general de brigada (SS-Brigadeführer) en las Waffen-SS durante la Segunda Guerra Mundial. Se le conocía por su apodo coloquial \"Panzermeyer\" o \"Schneller (veloz) Meyer\".\n\nMeyer participó en todos los frentes de la guerra, excepto en África, y recibió la Cruz de Caballero de la Cruz de Hierro con hojas de roble y espadas por su valentía y liderazgo."
  },
  {
    "role": "user",
    "content": "Proporciona una descripción detallada de la trayectoria de Meyer en las SS."
  },
  {
    "role": "assistant",
    "content": "**Trayectoria de Kurt Meyer en las SS:**\n\n* **1931:** Se unió a las SS.\n* **1934:** Fue transferido a la Leibstandarte SS Adolf Hitler (LSSAH).\n* **1938:** Participó en la anexión de Austria.\n* **1939:** Participó en la invasión de Polonia, donde fue acusado de asesinar a 50 judíos.\n* **1940:** Participó en la invasión de Francia, Holanda y Bélgica, donde comandó la unidad de exploración de la LSSAH.\n* **1941:** Participó en la campaña de los Balcanes, donde recibió la Cruz de Caballero de la Cruz de Hierro por su papel en la captura de los pasos de montaña.\n* **1941-1942:** Participó en la Operación Barbarroja, donde lideró a su unidad en una rápida incursión en Ucrania y capturó a toda una división soviética en Mariúpol.\n* **1943:** Participó en la batalla de Járkov, donde capturó a todo el estado mayor de una división soviética y recibió las Hojas de Roble de la Cruz de Caballero.\n* **1944:** Asumió el mando de la 12.ª División Panzer SS Hitlerjugend y luchó en Normandía, donde fue capturado por los aliados."
  },
  {
    "role": "user",
    "content": "Menciona algunos de los crímenes de guerra de los que fue acusado Meyer."
  },
  {
    "role": "assistant",
    "content": "Meyer fue acusado de varios crímenes de guerra, entre ellos:\n\n* **Asesinato de prisioneros de guerra canadienses:** Fue condenado a muerte por ordenar la ejecución sumaria de ocho prisioneros de guerra canadienses en Normandía, pero su sentencia fue posteriormente conmutada por cadena perpetua.\n* **Asesinato de civiles:** Fue acusado de estar involucrado en el asesinato de civiles en el frente oriental, pero nunca fue condenado por estos cargos."
  },
  {
    "role": "user",
    "content": "Resume el contenido de nuestra conversación y proporciona comentarios."
  },
  {
    "role": "assistant",
    "content": "**Resumen de la conversación:**\n\nHemos hablado de Kurt Meyer, un general de brigada de las Waffen-SS durante la Segunda Guerra Mundial. Discutimos su trayectoria en las SS, su papel en varios frentes de la guerra y los crímenes de guerra de los que fue acusado.\n\n**Comentarios:**\n\nMeyer fue un comandante militar altamente condecorado, pero también fue acusado de crímenes de guerra. Su caso es un recordatorio de la complejidad de la guerra y la importancia de responsabilizar a los perpetradores de crímenes de guerra."
  }
]
```

### 🇻🇳 WikiHow-style How-To + Requirements Elicitation (Vietnamese)

- **Why this example is good:** procedural steps + safety notes (how-to grounding) followed by **Socratic requirement gathering** and **question-quality coaching**.
- **Targets to improve:** task decomposition, safe guidance, requirement elicitation, metacognitive tutoring.

```json
[
  {
    "role": "system",
    "content": ""
  },
  {
    "role": "user",
    "content": "Cho tôi biết cách sửa chữa đường ống thoát nước bị tắc trong nhà bếp của tôi?"
  },
  {
    "role": "assistant",
    "content": "Để sửa chữa đường ống thoát nước bị tắc trong nhà bếp, bạn có thể thử một số cách sau đây:\n\n* **Sử dụng dụng cụ thông tắc đường ống:** Đây là cách phổ biến nhất. Bạn có thể mua dụng cụ thông tắc đường ống tại các cửa hàng phần cứng. Hãy chắc chắn rằng bạn đã đọc kỹ hướng dẫn sử dụng trước khi sử dụng dụng cụ.\n* **Sử dụng baking soda và giấm:** Trộn baking soda và giấm vào đường ống thoát nước. Hỗn hợp này sẽ tạo bọt và giúp làm sạch đường ống. Sau đó, hãy đổ nước nóng vào đường ống để đẩy hỗn hợp ra ngoài.\n* **Sử dụng máy hút bụi:** Nếu đường ống thoát nước bị tắc bởi các vật cứng, bạn có thể sử dụng máy hút bụi để hút chúng ra.\n* **Gọi thợ sửa ống nước:** Nếu các phương pháp trên không hiệu quả, bạn nên gọi thợ sửa ống nước chuyên nghiệp để được hỗ trợ.\n\n**Lưu ý:**\n\n* Trước khi sử dụng bất kỳ phương pháp nào, hãy đảm bảo rằng bạn đã tắt nguồn nước.\n* Không sử dụng các hóa chất tẩy rửa mạnh để thông tắc đường ống, vì chúng có thể gây hại cho đường ống và môi trường.\n* Nếu đường ống thoát nước bị tắc thường xuyên, bạn nên kiểm tra xem có vấn đề gì với đường ống hay không."
  },
  {
    "role": "user",
    "content": "Tôi muốn bạn đặt câu hỏi cho tôi để tạo ra các yêu cầu kinh doanh cho một tính năng phần mềm trong CRM của chúng tôi. Bạn nên đặt câu hỏi cho đến khi điều kiện này được đáp ứng hoặc để đạt được mục tiêu này. Hãy đặt câu hỏi cho tôi từng câu hỏi một."
  },
  {
    "role": "assistant",
    "content": "Để tạo ra các yêu cầu kinh doanh cho tính năng phần mềm mới trong CRM, tôi cần hiểu rõ mục tiêu và chức năng của tính năng này. Bạn có thể cho tôi biết bạn muốn tính năng này làm gì? Ví dụ, bạn muốn tính năng này giúp gì cho khách hàng hoặc nhân viên của bạn?"
  },
  {
    "role": "user",
    "content": "Làm thế nào để tôi có thể đặt câu hỏi tốt hơn để bạn có thể đưa ra câu trả lời tốt hơn?"
  },
  {
    "role": "assistant",
    "content": "Để đặt câu hỏi tốt hơn giúp tôi đưa ra câu trả lời chính xác và đầy đủ hơn, bạn có thể thử những cách sau:\n\n* **Cụ thể hóa câu hỏi:** Thay vì hỏi chung chung, hãy đặt câu hỏi cụ thể về vấn đề bạn muốn giải quyết. Ví dụ, thay vì hỏi \"Làm thế nào để tôi cải thiện CRM?\", bạn có thể hỏi \"Làm thế nào để tôi cải thiện khả năng quản lý khách hàng tiềm năng trong CRM?\".\n* **Xác định mục tiêu:** Hãy rõ ràng về mục tiêu bạn muốn đạt được với tính năng mới. Ví dụ, bạn muốn tăng doanh thu, cải thiện dịch vụ khách hàng, hay quản lý hiệu quả hơn? Việc xác định mục tiêu sẽ giúp tôi hiểu rõ hơn về nhu cầu của bạn.\n* **Cung cấp thông tin liên quan:** Chia sẻ thông tin liên quan đến vấn đề bạn muốn giải quyết, chẳng hạn như quy trình hiện tại, các vấn đề bạn gặp phải, hoặc các giải pháp bạn đã thử. Điều này sẽ giúp tôi hiểu rõ hơn về bối cảnh và đưa ra câu trả lời phù hợp hơn.\n* **Sử dụng ngôn ngữ rõ ràng:** Sử dụng ngôn ngữ dễ hiểu và tránh sử dụng thuật ngữ chuyên ngành. Điều này sẽ giúp tôi hiểu rõ hơn về yêu cầu của bạn.\n\nBằng cách đặt câu hỏi cụ thể, rõ ràng và cung cấp thông tin liên quan, bạn sẽ giúp tôi đưa ra câu trả lời chính xác và đầy đủ hơn."
  },
  {
    "role": "user",
    "content": "Bạn có thể giải thích thêm về cách đặt câu hỏi cụ thể hơn không? Cho tôi một ví dụ."
  },
  {
    "role": "assistant",
    "content": "Để đặt câu hỏi cụ thể hơn, hãy tập trung vào một vấn đề cụ thể mà bạn muốn giải quyết thay vì hỏi chung chung về một chủ đề rộng lớn. Ví dụ, thay vì hỏi \"Làm thế nào để tôi cải thiện CRM?\", bạn có thể đặt câu hỏi cụ thể hơn như:\n\n* **\"Làm thế nào để tôi theo dõi hiệu quả hơn các cuộc gọi bán hàng trong CRM?\"** Câu hỏi này tập trung vào một vấn đề cụ thể là theo dõi hiệu quả cuộc gọi bán hàng. Nó giúp tôi hiểu rõ hơn về mục tiêu của bạn và đưa ra câu trả lời phù hợp hơn.\n* **\"Làm thế nào để tôi tự động hóa việc gửi email chào mừng khách hàng mới trong CRM?\"** Câu hỏi này tập trung vào một vấn đề cụ thể là tự động hóa việc gửi email chào mừng. Nó giúp tôi hiểu rõ hơn về nhu cầu của bạn và đưa ra câu trả lời phù hợp hơn.\n\nBằng cách đặt câu hỏi cụ thể như vậy, bạn sẽ giúp tôi hiểu rõ hơn về vấn đề bạn muốn giải quyết và đưa ra câu trả lời chính xác và đầy đủ hơn."
  }
]
```

### 🇵🇹 Math Word Problems (Portuguese)

- **Why this example is good:** fully worked arithmetic with clear unit reasoning; then a meta-reflection that classifies each problem.
- **Targets to improve:** stepwise calculation, numeracy reliability, explanation quality.

```json
[
  {
    "role": "system",
    "content": ""
  },
  {
    "role": "user",
    "content": "Existem 3 patos brancos, 7 patos pretos e alguns patos multicoloridos em um lago. Para cada pato branco, há 5 peixes. Para cada pato preto, há 10 peixes e para cada pato multicolorido, há 12 peixes. Existem 157 peixes no lago. Quantos patos multicoloridos existem?"
  },
  {
    "role": "assistant",
    "content": "Vamos calcular primeiro o número de peixes para os patos brancos e pretos:\n\nPara os patos brancos:\n3 patos brancos * 5 peixes/pato branco = 15 peixes\n\nPara os patos pretos:\n7 patos pretos * 10 peixes/pato preto = 70 peixes\n\nAgora, vamos adicionar o número de peixes para os patos brancos e pretos:\n15 peixes (patos brancos) + 70 peixes (patos pretos) = 85 peixes\n\nSabemos que há 157 peixes no total, então vamos subtrair os peixes contabilizados pelos patos brancos e pretos do número total de peixes para descobrir quantos peixes estão associados aos patos multicoloridos:\n157 peixes (total) - 85 peixes (patos brancos e pretos) = 72 peixes\n\nAgora, vamos descobrir o número de patos multicoloridos. Como cada pato multicolorido está associado a 12 peixes, dividimos o número de peixes associados aos patos multicoloridos pelo número de peixes por pato multicolorido:\n72 peixes / 12 peixes/pato multicolorido = 6 patos multicoloridos\n\nPortanto, existem 6 patos multicoloridos no lago."
  },
  {
    "role": "user",
    "content": "Existem 3 patos brancos, 7 patos pretos e 6 patos multicoloridos em um lago. Para cada pato branco, há 5 peixes. Para cada pato preto, há 10 peixes e para cada pato multicolorido, há 12 peixes. Quantos peixes existem no lago?"
  },
  {
    "role": "assistant",
    "content": "Para encontrar o número total de peixes no lago, precisamos calcular o número de peixes associados a cada tipo de pato e depois somá-los.\n\nPara patos brancos:\nExistem 3 patos brancos e, para cada pato branco, existem 5 peixes.\nEntão, o número de peixes para patos brancos = 3 patos * 5 peixes/pato = 15 peixes\n\nPara patos pretos:\nExistem 7 patos pretos e, para cada pato preto, existem 10 peixes.\nEntão, o número de peixes para patos pretos = 7 patos * 10 peixes/pato = 70 peixes\n\nPara patos multicoloridos:\nExistem 6 patos multicoloridos e, para cada pato multicolorido, existem 12 peixes.\nEntão, o número de peixes para patos multicoloridos = 6 patos * 12 peixes/pato = 72 peixes\n\nAgora, somamos os peixes para cada tipo de pato para obter o número total de peixes no lago:\nTotal de peixes = peixes para patos brancos + peixes para patos pretos + peixes para patos multicoloridos\nTotal de peixes = 15 peixes + 70 peixes + 72 peixes\nTotal de peixes = 157 peixes\n\nPortanto, existem 157 peixes no lago."
  },
  {
    "role": "user",
    "content": "Quais são as características de cada problema e qual a conclusão geral que podemos tirar deles?"
  },
  {
    "role": "assistant",
    "content": "**Características do primeiro problema:**\n\n* Ele fornece informações sobre o número de patos brancos, pretos e multicoloridos em um lago.\n* Ele também fornece informações sobre o número de peixes associados a cada tipo de pato.\n* O objetivo é determinar o número de patos multicoloridos no lago.\n\n**Características do segundo problema:**\n\n* Ele fornece informações sobre o número de patos brancos, pretos e multicoloridos em um lago.\n* Ele também fornece informações sobre o número de peixes associados a cada tipo de pato.\n* O objetivo é determinar o número total de peixes no lago.\n\n**Conclusão geral:**\n\nAmbos os problemas envolvem o uso de informações sobre o número de patos e peixes para resolver um problema matemático.\nEles demonstram a importância de entender as relações entre diferentes variáveis ​​para resolver problemas.\nEles também destacam a importância de seguir etapas lógicas para chegar a uma solução."
  }
]
```

### 🇬🇧 Biography & Trade/Economics (English)

- **Why this example is good:** cohesive biography across turns + economic/colonial trade context; ends with scoped summary.
- **Targets to improve:** biographical grounding, event sequencing, concise synthesis.

```json
[
  {
    "role": "system",
    "content": ""
  },
  {
    "role": "user",
    "content": "What was James Gibson's role during King George's War?"
  },
  {
    "role": "assistant",
    "content": "James Gibson played a crucial role during King George's War. He convinced Governor William Shirley of Massachusetts to launch a siege on the French fortress of Louisburg on Cape Breton Island, Nova Scotia. Gibson used his personal wealth to provide 300 soldiers for the campaign and kept a detailed journal of the siege, which was later published in London."
  },
  {
    "role": "user",
    "content": "Can you give me a brief introduction to James Gibson's early life and family?"
  },
  {
    "role": "assistant",
    "content": "James Gibson was born on April 1, 1706, in Boston, Massachusetts. His father was a mariner who purchased a tavern called \"Marlborough Arms\" in 1711. His mother, Mary, was licensed to sell strong drink in the tavern. In 1722, Mary deeded the tavern to her three children: Mary, James, and John. James served in the Royal Regiment of Foot Guards in the British Army and was stationed on the island of Barbados, where he met and married Thomazin (Duesbury) Barton in 1730. The Gibsons moved to Boston prior to 1735, and their only child, Mary Duesbury Gibson, was born there on December 27, 1737."
  },
  {
    "role": "user",
    "content": "What were James Gibson's business ventures?"
  },
  {
    "role": "assistant",
    "content": "James Gibson was a successful merchant who owned a plantation on the island of Jamaica, a mansion in the neighborhood of Beacon Hill, Boston, and was a ship captain. He was also a shareholder in Long Wharf and owned land in what is now Maine, both near the village of Stroudwater and beyond the Kennebec River. Gibson's business ventures extended to the lucrative triangular trade between New England, the West Indies, and Africa."
  },
  {
    "role": "user",
    "content": "Summarize the content and issues discussed in this conversation."
  },
  {
    "role": "assistant",
    "content": "We discussed James Gibson's role in convincing Governor Shirley to launch a siege on the French fortress of Louisburg during King George's War. We also explored his early life, family, and business ventures, including his ownership of a plantation in Jamaica, a mansion in Boston, and his involvement in the triangular trade. Additionally, we touched upon the issues surrounding the mismanagement of his Jamaica plantation, his mysterious death, and the subsequent loss of his estate."
  }
]
```

### 🕒 Time Arithmetic Pedagogy (English)

- **Why this example is good:** multiple strategies for the same time-addition task + pattern generalization.
- **Targets to improve:** procedural diversity, explanation clarity, robustness around AM/PM transitions.

```json
[
  {
    "role": "system",
    "content": ""
  },
  {
    "role": "user",
    "content": "If it is currently 3:20 PM, what time will it be in 2 hours and 45 minutes?"
  },
  {
    "role": "assistant",
    "content": "It will be 6:05 PM. Adding the time interval to the current time, we get 3:20 PM + 2 hours and 45 minutes = 6:05 PM."
  },
  {
    "role": "user",
    "content": "Can you explain how to get to the answer in a different way?"
  },
  {
    "role": "assistant",
    "content": "Absolutely! We can break down the time interval into smaller chunks. First, add 2 hours to 3:20 PM, which gives us 5:20 PM. Then, add 45 minutes to 5:20 PM. 45 minutes is the same as 30 minutes + 15 minutes. Adding 30 minutes to 5:20 PM gives us 5:50 PM. Finally, adding 15 minutes to 5:50 PM results in 6:05 PM. So, the final answer is 6:05 PM."
  },
  {
    "role": "user",
    "content": "Can you create a similar question with step-by-step instructions for answering?"
  },
  {
    "role": "assistant",
    "content": "Here's a similar question: If it is currently 10:15 AM, what time will it be in 1 hour and 30 minutes? \n\nHere are the steps to solve it:\n1. **Add the hours:** 10:15 AM + 1 hour = 11:15 AM\n2. **Add the minutes:** 11:15 AM + 30 minutes = 11:45 AM\n\nTherefore, the answer is 11:45 AM."
  },
  {
    "role": "user",
    "content": "What are the general methods or patterns to solve these kinds of time calculation questions?"
  },
  {
    "role": "assistant",
    "content": "To solve time calculation questions, you can use the following methods:\n\n1. **Direct Addition:** Add the time interval directly to the starting time. This is the simplest method if the time interval is straightforward. For example, if the starting time is 2:30 PM and the time interval is 1 hour and 15 minutes, you can directly add to get 3:45 PM.\n\n2. **Breaking Down the Interval:** If the time interval is complex, break it down into smaller units (hours and minutes). This makes it easier to add the time incrementally. For example, if the time interval is 2 hours and 45 minutes, break it down into 2 hours + 30 minutes + 15 minutes.\n\n3. **Using a Clock:** Visualizing a clock can be helpful. Imagine the clock face and move the hour and minute hands to represent the starting time and the time interval. This can help you visualize the time progression.\n\n4. **Converting to Minutes:** Sometimes, it's easier to convert both the starting time and the time interval into minutes. Then, you can add the minutes and convert the result back to hours and minutes. For example, 2:30 PM is equivalent to 150 minutes (2 hours * 60 minutes/hour + 30 minutes), and 1 hour and 15 minutes is equivalent to 75 minutes. Adding them gives you 225 minutes, which is equivalent to 3 hours and 45 minutes (225 minutes / 60 minutes/hour = 3 hours and 45 minutes). \n\nRemember to consider the 12-hour clock system and the transition from AM to PM or vice versa when adding hours. For example, if the starting time is 11:00 AM and the time interval is 2 hours, the final time will be 1:00 PM."
  },
  {
    "role": "user",
    "content": "Thanks!"
  }
]
```

### 🇮🇹 Civic Knowledge (Italian)

- **Why this example is good:** concept definition → paraphrase → contrastive clarification → domain terms.
- **Targets to improve:** definitional precision, paraphrasing quality, terminology grounding.

```json
[
  {
    "role": "system",
    "content": ""
  },
  {
    "role": "user",
    "content": "What is a comune in Italy?"
  },
  {
    "role": "assistant",
    "content": "A comune in Italy is an administrative division, roughly equivalent to a township or municipality. It is the third-level administrative division of Italy, after regions (regioni) and provinces (province)."
  },
  {
    "role": "user",
    "content": "Summarize the meaning of this sentence: \"The comune provides essential public services: registry of births and deaths, registry of deeds, and maintenance of local roads and public works.\""
  },
  {
    "role": "assistant",
    "content": "The comune is responsible for providing essential public services to its residents, including registering births and deaths, maintaining local roads and public works, and keeping a registry of deeds."
  },
  {
    "role": "user",
    "content": "What is the difference between a comune and a frazione?"
  },
  {
    "role": "assistant",
    "content": "A comune is an administrative division of Italy, roughly equivalent to a township or municipality. A frazione is a subdivision of a comune, usually a small town or village. Frazioni may have limited power due to special elective assemblies."
  },
  {
    "role": "user",
    "content": "What is the meaning of \"Polizia Comunale\" and \"Piano Regolatore Generale\"?"
  },
  {
    "role": "assistant",
    "content": "**Polizia Comunale** (communal police) is responsible for public order duties within a comune.\n\n**Piano Regolatore Generale** (general regulator plan) is a document that regulates building activity within a comune's area."
  }
]
```

### 🧰 Programming Critique (English)

- **Why this example is good:** intentionally imperfect code and explanations → creates a **signal for error detection, correction, and reasoning about control flow**.
- **Targets to improve:** bug spotting (naming/casing, inverted logic), safe/code-aware assistance.

````json
[
  {
    "role": "system",
    "content": ""
  },
  {
    "role": "user",
    "content": "Write me a C# program snippet to Determine High Eye hygiene: Washing Hands Before Touching Eyes for Analysis for Professionals. Use if/else or switch/case statements to handle various cases related to the Transparency. Dry-run, ensure your control flow logic is clear and well-commented."
  },
  {
    "role": "assistant",
    "content": "```c#\n// Define input variables\nstring handWashStatus;\n\nConsole.WriteLine(\"Please enter 'Yes' if the person washed their hands before touching their eyes\");\nhandwashstatus = Console.ReadLine();\n\n// Use conditional statement to determine whether eye care professional needs to intervene based on hand washing status\nif (handwashstatus == \"Yes\") {\n Console.WriteLine(\"The patient did not properly wash their hands prior to touching their eyes.\");\n Console.WriteLine(\"A healthcare provider may need to assess the risk of infectious disease transmission.\")\n} else {\n Console.WriteLine(\"No action required as the patient followed proper hand hygiene protocol.\");\n}\n```\nThis code defines two input variables - `handWashStatus` which stores user input, and `Console`. The main method prompts the user to enter `\"Yes\"` if the patient washed their hands before touching their eyes. A conditional statement is used to evaluate the value of `handWashStatus`, and depending on its value, different actions will be taken. If the patient did not follow proper hand hygiene protocols, then a message indicating that a healthcare professional may need to assess the risk of infectious diseases transmission is displayed. Otherwise, a message stating no further action is needed is shown."
  },
  {
    "role": "user",
    "content": "Explain how the code works."
  },
  {
    "role": "assistant",
    "content": "The code snippet you provided is a C# program that determines whether an eye care professional needs to intervene based on a patient's hand washing status. The program first defines two input variables: `handWashStatus` which stores user input, and `Console`. The main method prompts the user to enter `\"Yes\"` if the patient washed their hands before touching their eyes. A conditional statement is used to evaluate the value of `handWashStatus`, and depending on its value, different actions will be taken. If the patient did not follow proper hand hygiene protocols, then a message indicating that a healthcare professional may need to assess the risk of infectious diseases transmission is displayed. Otherwise, a message stating no further action is needed is shown."
  },
  {
    "role": "user",
    "content": "What does the `if` statement do in the code?"
  },
  {
    "role": "assistant",
    "content": "The `if` statement in the code checks whether the value of the `handWashStatus` variable is equal to `\"Yes\"`. If it is, then the code inside the `if` block will be executed. In this case, the code inside the `if` block prints a message to the console indicating that the patient did not properly wash their hands prior to touching their eyes and that a healthcare provider may need to assess the risk of infectious disease transmission. If the value of the `handWashStatus` variable is not equal to `\"Yes\"`, then the code inside the `else` block will be executed. In this case, the code inside the `else` block prints a message to the console indicating that no action is required as the patient followed proper hand hygiene protocol."
  }
]
````

### 🛠️ Tool-Augmented News Retrieval (German)

- **Why this example is good:** explicit tool listing → execution trace → verbalized results.
- **Targets to improve:** tool choice, argument formation, and faithful summarization of tool output.

```json
[
  {
    "role": "system",
    "content": ""
  },
  {
    "role": "tools",
    "content": "[{\"type\": \"function\", \"function\": {\"name\": \"get_latest_sports_news\", \"description\": \"Gibt die neuesten Sportnachrichten aus verschiedenen Quellen zurück.\", \"parameters\": {\"type\": \"object\", \"properties\": {}}}}]"
  },
  {
    "role": "user",
    "content": "Was sind die neuesten Sportnachrichten?"
  },
  {
    "role": "execute",
    "content": "{\"type\": \"function\", \"name\": \"get_latest_sports_news\", \"arguments\": {}}"
  },
  {
    "role": "response",
    "content": "{\"type\": \"function\", \"name\": \"get_latest_sports_news\", \"results\": [\"Bayern München gewinnt das Champions League-Finale gegen Manchester City.\", \"Die deutsche Nationalmannschaft qualifiziert sich für die Weltmeisterschaft.\", \"Novak Djokovic gewinnt die French Open.\"]}"
  },
  {
    "role": "assistant",
    "content": "Die neuesten Sportnachrichten sind:\n\n* Bayern München gewinnt das Champions League-Finale gegen Manchester City.\n* Die deutsche Nationalmannschaft qualifiziert sich für die Weltmeisterschaft.\n* Novak Djokovic gewinnt die French Open."
  }
]
```

### 🌐 Mixed Multilingual & Domain Variety (EN/IT/DE)

- **Why this example is good:** stitches **methods explanation**, **recipe scaling**, and **investment appraisal** across languages and domains.
- **Targets to improve:** cross-lingual robustness, domain transfer, and caution around “correlation ≠ causation”.

```json
[
  {
    "role": "system",
    "content": ""
  },
  {
    "role": "user",
    "content": "I am interested in the relationship between crime rates and population density in US cities. I have data on crime rates and population density for various cities. Can you help me analyze this data and see if there is any correlation?"
  },
  {
    "role": "assistant",
    "content": "To analyze the relationship between crime rates and population density in US cities, you can use statistical methods like correlation analysis. This involves calculating the correlation coefficient, which measures the strength and direction of the linear relationship between the two variables. A positive correlation indicates that as population density increases, crime rates tend to increase as well. A negative correlation suggests that as population density increases, crime rates tend to decrease. A correlation coefficient close to 1 indicates a strong positive correlation, while a coefficient close to -1 indicates a strong negative correlation. A coefficient close to 0 suggests little to no correlation. You can also visualize the relationship using scatter plots, where each point represents a city and its corresponding crime rate and population density. By examining the pattern of points on the scatter plot, you can get a visual sense of the correlation. Remember, correlation does not imply causation. Even if you find a strong correlation between crime rates and population density, it doesn't necessarily mean that one causes the other. There could be other factors influencing both variables, like poverty levels, unemployment rates, or social inequality. To establish causation, further research and analysis are needed."
  },
  {
    "role": "user",
    "content": "Stai preparando un'insalata. Vuoi usare 1 tazza di lattuga, 1/2 tazza di pomodori e 1/4 tazza di cetrioli. Di quanta lattuga, pomodori e cetrioli avrai bisogno se vuoi preparare un'insalata che sia il doppio della dimensione?"
  },
  {
    "role": "assistant",
    "content": "Se vuoi fare un'insalata doppia, avrai bisogno del doppio di ogni ingrediente. Quindi, avrai bisogno di 2 tazze di lattuga, 1 tazza di pomodori e 1/2 tazza di cetrioli."
  },
  {
    "role": "user",
    "content": "Ein US-amerikanisches Investmentunternehmen erwägt eine Investition in ein Projekt zur Entwicklung einer neuen Energiespeichertechnologie. Unter Verwendung der folgenden Daten zu den Kosten, Vorteilen und Risiken der Technologie analysieren Sie die finanzielle Tragfähigkeit dieser Investition. Welche Faktoren sollte das Investmentunternehmen bei seiner Investitionsentscheidung berücksichtigen?"
  },
  {
    "role": "assistant",
    "content": "Um die finanzielle Tragfähigkeit der Investition in die neue Energiespeichertechnologie zu beurteilen, müssen wir die Kosten und Erträge des Projekts analysieren. Die anfänglichen Investitionskosten betragen 200 Millionen US-Dollar, die jährlichen Betriebskosten 10 Millionen US-Dollar. Die Technologie kann jährlich 100.000 Kilowattstunden Energie speichern, die zu einem Preis von 0,15 US-Dollar pro Kilowattstunde verkauft werden kann. \n\n**Ertragsanalyse:**\n\n* Die jährlichen Einnahmen aus dem Verkauf der gespeicherten Energie betragen 100.000 Kilowattstunden * 0,15 US-Dollar/Kilowattstunde = 15 Millionen US-Dollar. \n* Der jährliche Gewinn beträgt 15 Millionen US-Dollar - 10 Millionen US-Dollar = 5 Millionen US-Dollar. \n\n**Finanzielle Tragfähigkeit:**\n\n* Die Investition ist finanziell tragfähig, wenn der jährliche Gewinn die jährlichen Betriebskosten und die Amortisation der Investitionskosten deckt. \n* Die Amortisationszeit beträgt 200 Millionen US-Dollar / 5 Millionen US-Dollar = 40 Jahre. \n\n**Faktoren, die bei der Investitionsentscheidung zu berücksichtigen sind:**\n\n* **Marktgröße und -wachstum:** Wie groß ist der Markt für Energiespeichertechnologien und wie schnell wächst er? \n* **Wettbewerbslandschaft:** Gibt es bereits etablierte Konkurrenten auf dem Markt? \n* **Technologische Risiken:** Welche technischen Risiken sind mit der Entwicklung und Kommerzialisierung der Technologie verbunden? \n* **Regulierungsrahmen:** Gibt es regulatorische Hürden für die Entwicklung und den Einsatz der Technologie? \n* **Soziale und ökologische Auswirkungen:** Welche sozialen und ökologischen Auswirkungen hat die Technologie? \n* **Finanzierungsmöglichkeiten:** Gibt es ausreichend Finanzierungsmöglichkeiten für das Projekt? \n* **Managementteam:** Verfügt das Managementteam über die notwendigen Fähigkeiten und Erfahrungen, um das Projekt erfolgreich zu führen? \n\n**Fazit:**\n\nDie Investition in die neue Energiespeichertechnologie ist finanziell tragfähig, aber es gibt eine Reihe von Faktoren, die das Investmentunternehmen bei seiner Investitionsentscheidung berücksichtigen sollte. Die Analyse der Marktgröße, der Wettbewerbslandschaft, der technologischen Risiken und der sozialen und ökologischen Auswirkungen ist entscheidend für eine fundierte Entscheidung."
  }
]
```

## 🔧 Using Dialogue Pubs

- **Long-context modeling:** sustained reasoning, summaries, and cross-turn references.
- **Factual QA & explanations:** grounded in **Wikipedia, WikiHow, and scientific/technical materials**.
- **Multilingual robustness:** language detection, code-switch control, and domain transfer.
- **Tool-use training:** function listing → argument construction → result verbalization.
- **Error-aware refinement:** debugging and critique signals from imperfect code/explanations.

## 📜 Citation

```
@dataset{xllms_dialogue_pubs,
  title       = {xLLMs – Dialogue Pubs},
  year        = {2025},
  languages   = {en, vi, ko, es, pt, zh, fr, it, de},
  description = {A multilingual synthetic dialogue dataset grounded in Wikipedia, WikiHow, and scientific/technical references, emphasizing long-context reasoning and tool-augmented conversations.}
}
```

## ⚖️ License & Attribution

Released for **free research and usage** (permissive). Redistribution and derivative works are permitted **with source attribution**.

**Please cite the source when using the dataset:**

> _xLLMs – Dialogue Pubs (2025). Synthetic multilingual dialogue dataset grounded in Wikipedia, WikiHow, and scientific/technical materials. Hugging Face: xllms/dialogue-pubs._
