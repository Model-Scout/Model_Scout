---
license: cc-by-4.0
language:
- en
- uk
- es
- ko
- ja
- zh
- fr
- hi
- de
task_categories:
- text-generation
- translation
- summarization
tags:
- code
- programming-tasks
- algorithmic-reasoning
- code-generation
- python
- synthetic
datasets:
- anon-researcher-ua/ua-codeforces-cots-open-r1
- anon-researcher-ua/ua-codeforces-cots-open-r1-for-training
- open-r1/codeforces-cots
base_model:
- anon-researcher-ua/codegpt-oss-20b
pipeline_tag: text-generation
---

# Model Summary

This model is a LoRA-tuned variant of [gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b) adapted for competitive programming with reasoning traces in Ukrainian and English.
It was trained on ~36M tokens from [ua-codeforces-cots-open-r1](https://huggingface.co/datasets/anon-researcher-ua/ua-codeforces-cots-open-r1) ([ua-codeforces-cots-open-r1-for-training](https://huggingface.co/datasets/anon-researcher-ua/ua-codeforces-cots-open-r1-for-training) in fact), which extends [open-r1/codeforces-cots](https://huggingface.co/datasets/open-r1/codeforces-cots) with translated Ukrainian problem statements and low/medium/high reasoning traces.

The model supports low, medium, and high reasoning effort as well as language control for reasoning via system prompts. 
This model is able to reason in other languages as well with proper sampling params ([check examples below](https://huggingface.co/anon-researcher-ua/codegpt-oss-20b#other-languages)).

# Training Details

- Base model: gpt-oss-20b

- Fine-tuning method: LoRA

- Trainable parameters: ~75M

- Target modules: all-linear

- Target parameters: ["7.mlp.experts.gate_up_proj", "7.mlp.experts.down_proj",
        "15.mlp.experts.gate_up_proj",
        "15.mlp.experts.down_proj",
        "21.mlp.experts.gate_up_proj",
        "21.mlp.experts.down_proj",
        "23.mlp.experts.gate_up_proj",
        "23.mlp.experts.down_proj",
      ]

- LoRA config: r=32, alpha=64, dropout=0.0

- Training tokens: 36M (4k train examples, avg length 7–8k tokens, ~300 >10k tokens)

- Max length: 26496

- Epochs: 3 (early stopping after epoch 2)

- Batching: per_device_batch=1, gradient_accumulation=8 (effective batch=8)

- Optimizer: paged_adamw_8bit

- Learning rate: 5e-5 (cosine schedule, min_lr_rate=0.01)

- Weight decay: 0.01

- Precision: bf16

# Capabilities

- Generates chain-of-thought reasoning traces in English or Ukrainian (works for other languages as well, check examples below)

- Supports low/medium/high reasoning effort (controllable verbosity & detail)

- Solves competitive programming tasks in Python with explanations

- Handles long contexts (up to 32k tokens)

# Limitations

- Dataset is relatively small (~36M tokens, 2 epoch) → model may overfit to training traces.

- Reasoning traces can be verbose or stylistically inconsistent (looped, truncated output for high reasoning effort).

- Only tuned for Python competitive programming tasks, not general coding.

# License
- Our contribution: CC BY 4.0.

- Original data from open-r1/codeforces-cots: ODC-By 4.0.

- Please attribute ua-codeforces-cots-open-r1 and the upstream dataset when you share or use it.

# Usage

## Transformers inference (Slow)
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from datasets import load_dataset

tokenizer = AutoTokenizer.from_pretrained("anon-researcher-ua/codegpt-oss-20b")

model_kwargs = dict(attn_implementation="flash_attention_2", torch_dtype="auto", use_cache=True, device_map="auto")
model = AutoModelForCausalLM.from_pretrained("anon-researcher-ua/codegpt-oss-20b", **model_kwargs).cuda()

train_dataset = load_dataset("anon-researcher-ua/ua-codeforces-cots-open-r1-for-training")

def format_row(row):
    return tokenizer.apply_chat_template(
        row["messages_gpt"][:-1],
        tokenize=True,
        return_tensors="pt",
        reasoning_effort=row['reasoning_effort']
    )

gen_kwargs = {"max_new_tokens": 32768, "do_sample": True, "temperature": 0.2, "top_p": 1.0, "repetition_penalty": 1}

for ridx, row in enumerate(train_dataset['validation']):
    input_ids = format_row(row).to(model.device)
    output_ids = model.generate(input_ids, **gen_kwargs)
    response = tokenizer.batch_decode(output_ids)[0]
    print(gen_kwargs, "\n")
    print(response, "\n\n=================================================\n\n")
```

## VLLM inference (Fast)
### Prerequisites
```bash
%pip install --upgrade -qqq uv
%uv pip install --pre vllm==0.10.1.1 --extra-index-url https://wheels.vllm.ai/gpt-oss --extra-index-url https://download.pytorch.org/whl/nightly/cu128 --index-strategy unsafe-best-match --no-cache
```

```python
from vllm import LLM, SamplingParams
from vllm.inputs import TokensPrompt
from transformers import AutoTokenizer

model = "anon-researcher-ua/codegpt-oss-20b"
tokenizer = AutoTokenizer.from_pretrained(model)

llm = LLM(model=model, dtype="bfloat16")

def run_predict(messages, sampling_params, reasoning_effort="low"):
    formatted_prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        reasoning_effort=reasoning_effort
    )
    input_ids = tokenizer(
        formatted_prompt,
        add_special_tokens=False
    ).input_ids
    prompt = TokensPrompt(prompt_token_ids=input_ids)
    output = llm.generate(prompt, sampling_params)
    return output[0].outputs[0].text

sampling_params = SamplingParams(
    max_tokens=32768,
    temperature=0.2, # recommended temp=1.0 leads to poor performance
    top_p=1,
    repetition_penalty=1,
    stop_token_ids=[200002, 199999, 200012],
    skip_special_tokens=False
)

messages = [
    {"role": "system", "content": "reasoning language: Ukrainian"},
    {"role": "user", "content": "Обчисліть площу бічної поверхні правильної трикутної піраміди, сторона основи якої дорівнює 8 см, а апофема на 2 см більша за сторону основи піраміди."},
]

print(run_predict(messages, sampling_params, reasoning_effort="medium"))
```

## Reasoning language: Ukrainian, reasoning effort: medium
```
<|start|>system<|message|>You are ChatGPT, a large language model trained by OpenAI.
Knowledge cutoff: 2024-06
Current date: 2025-08-29

Reasoning: medium

# Valid channels: analysis, commentary, final. Channel must be included for every message.<|end|><|start|>developer<|message|># Instructions

reasoning language: Ukrainian

<|end|><|start|>user<|message|>Обчисліть площу бічної поверхні правильної трикутної піраміди, сторона основи якої дорівнює 8 см, а апофема на 2 см більша за сторону основи піраміди.<|end|><|start|>assistant
<|channel|>analysis<|message|>Задача: обчислити площу бічної поверхні правильної трикутної піраміди. Сторона основи = 8 см. Апофема (висота бічної поверхні) = 8 + 2 = 10 см. Правильна трикутна піраміда: основа рівносторонній трикутнику. Бічна поверхня складається з трикутників, кожен з яких має однакові сторони. Бічна поверхня піраміди: 3 * (площа одного трикутника).

Площа трикутника: (1/2) * a * h, де a — сторона трикутника, h — висота трикутника. Отже, площа бічної поверхні = 3 * (1/2 * a * h) = (3a h) / 2.

Підставляємо a = 8, h = 10: (3 * 8 * 10) / 2 = 240 / 2 = 120 см².

Потрібно вивести результат. Формат: "120 см²" (або "120 см²" з правильною одиницею). У деяких стандартах використовують "см²" або "см²". В українській мові одиниця площі позначається "см²" (або "см²"). Але в тексті задачі використано "см". Тому вивід має бути "120 см²".

Підтвердити, що інші параметри (наприклад, висота основи піраміди) не впливають на площу бічної поверхні. Ні, оскільки апофема — це висота бічної поверхні.

Отже, правильна відповідь: 120 см².

Вивести: "120 см²".

Підтвердити, що апофема — це висота бічної поверхні, а не висота основи. У задачі сказано "апофема на 2 см більша за сторону основи піраміди". Отже, 10 см.

Тож відповідь: 120 см².<|end|><|start|>assistant<|channel|>final<|message|>Нам потрібно обчислити площу бічної поверхні правильної трикутної піраміди. 

- Сторона основи \(a = 8\) см.
- Апофема (висота бічної поверхні) \(h = a + 2 = 8 + 2 = 10\) см.

Бічна поверхня піраміди складається з трьох трикутників, кожен з яких має однакові сторони. Загальна площа бічної поверхні обчислюється як:

\[
\text{Площа} = 3 \times \frac{1}{2} \times a \times h = \frac{3a h}{2}
\]

Підставляємо відомі значення:

\[
\frac{3 \times 8 \times 10}{2} = \frac{240}{2} = 120 \text{ см}^2
\]

Отже, площа бічної поверхні правильної трикутної піраміди становить **120 см²**.
```

## Reasoning language: English, reasoning effort: high
```
<|start|>system<|message|>You are ChatGPT, a large language model trained by OpenAI.
Knowledge cutoff: 2024-06
Current date: 2025-08-29

Reasoning: high

# Valid channels: analysis, commentary, final. Channel must be included for every message.<|end|><|start|>developer<|message|># Instructions

reasoning language: English

<|end|><|start|>user<|message|>Обчисліть площу бічної поверхні правильної трикутної піраміди, сторона основи якої дорівнює 8 см, а апофема на 2 см більша за сторону основи піраміди.<|end|><|start|>assistant
<|channel|>analysis<|message|>Обчисліть площу бічної поверхні правильної трикутної піраміди, де сторона основи дорівнює 8 см, а апофема на 2 см більша за сторону основи піраміди. Площа бічної поверхні складається з трикутників, кожен з яких має однакову висоту (висоту трикутника). Сума всіх трикутників — це бічна поверхня. Площа бічної поверхні — це сума площ усіх трикутників.

Завдання: знайти площу бічної lateral

We need to compute the lateral surface area of a regular triangular pyramid (tetrahedron) with base side length 8 cm. The slant height (apothem?) is 2 cm longer than the base side. Wait: "апофема на 2 см більша за сторону основи піраміди піраміди" maybe apothem of the pyramid (slant height) is 2 cm greater than the base side. So slant height = 8 + 2 = 10 cm. But need to confirm what exactly the apothem refers to here.

The lateral surface area of a regular triangular pyramid (tetrahedron) is the sum of the areas of the three lateral faces. Each lateral face is a triangle with base side length 8 and height equal to the slant height. So each triangle area is (1/2 * base * height). So each triangle is 1/2 * 8 * 10 = 40. Multiply by 3 gives 120 cm².

But maybe the apothem refers to the apothem of the base (the base is a regular triangle). Wait, the problem statement: "площа бічної поверхні правильної трикутної піраміди, сторона основи якої дорівнює 8 см, а апофема на 2 см більша за сторону основи піраміди піраміди." So the apothem (apothema) of the pyramid is 2 cm greater than the side of the base. So slant height (apothem of the pyramid) = 8 + 2 = 10. So each lateral face is a triangle with base 8 and height 10. So each area is (1/2*8*10) = 40. 3 faces => 120.

But maybe there is a trick: the apothem of the pyramid is the slant height of the lateral faces. So yes.

But let's double-check the geometry. For a regular triangular pyramid, each lateral face is a triangle with base side length equal to the base side of the pyramid. The height of each lateral face is the slant height (apothem) of the pyramid. So yes.

Thus the lateral surface area = 3 * (1/2 * base * slant height) = 3 * (1/2 * 8 * 10) = 3 * 40 = 120.

But maybe the problem is not that trivial. Let's read the original Ukrainian text: "Обчисліть площу бічної поверхні правильної трикутної піраміди, сторона основи якої дорівнює 8 см, а апофема на 2 см більша за сторону основи піраміди піраміди. Площа бічної поверхні складається з трикутників, кожен з яких має однакову висоту (висоту трикутника). Сума всіх трикутників — це бічна поверхня. Площа бічної поверхні — це сума площ усіх трикутників."

So the lateral surface area is the sum of the areas of the three triangles. Each triangle has same height (the height of the triangle). The height of the triangle is the slant height of the pyramid. So each triangle area is (1/2 * base side * height). So indeed 1/2 * 8 * (8+2) = 1/2 * 8 * 10 = 40. Then sum for 3 triangles is 3 * 40 = 120.

But let's check if there's any other interpretation. For a regular triangular pyramid, the base is a regular triangle. The apothem of the pyramid is the slant height of the pyramid. So yes.

Alternatively, maybe "апофема" could be the apothem of the base (the distance from the center of the base to a side). But the problem says "апофема на 2 см більша за сторону основи піраміди піраміди" which suggests it's the apothem of the pyramid (the slant height). So yes.

Thus the answer should be 120 cm².

But maybe the problem expects a different approach. Let's re-read the problem:

"Обчисліть площу бічної поверхні правильної трикутної піраміди, сторона основи якої дорівнює 8 см, а апофема на 2 см більша за сторону основи піраміди піраміди. Площа бічної поверхні складається з трикутників, кожен з яких має однакову висоту (висоту трикутника). Сума всіх трикутників — це бічна поверхня. Площа бічної поверхні — це сума площ усіх трикутників."

So yes, it's exactly that. So answer is 120 cm².

But maybe the apothem is something else. Let's think: In a pyramid, the apothem (slant height) is the height of each lateral face. So each lateral face is a triangle with height equal to the apothem. So yes.

Thus each triangle area is 1/2 * base * apothem. So 1/2*8*10 = 40. Sum 3*40 = 120.

Thus answer: 120 cm².

But wait, the problem might be a trick: maybe the apothem is the apothem of the base (the distance from the center to a side). But the problem says "апофема на 2 см більша за сторону основи піраміди піраміди." So it's not the base's apothem. It's the pyramid's apothem. So yes.

So answer: 120.

But let's check the geometry: The lateral faces of a regular pyramid are congruent isosceles triangles. Each has base side length equal to the base side of the pyramid. The height of each lateral face is the slant height (apothem) of the pyramid. So yes.

Thus the lateral surface area is 3 * (1/2 * base side * slant height) = 3 * (1/2 * 8 * 10) = 3 * 40 = 120.

Thus answer: 120 cm².

But let's double-check that there is no confusion between apothem and slant height. In a pyramid, the apothem is the slant height. So yes.

Thus answer: 120.

But maybe the problem expects the answer in terms of cm². So 120 cm².

Thus the correct answer is 120 cm².

But let's think if there's any other possible misinterpretation. For example, maybe the apothem is the apothem of the base (the distance from the center of the base to a side). But the problem says "апофема на 2 см більша за сторону основи піраміди піраміди." So it's the apothem of the pyramid. So no.

Thus answer: 120 cm².

So final answer: 120 cm².

But let's check the original language: "правильної трикутної піраміди" which is a regular triangular pyramid. So yes.

Thus answer: 120 cm².

Thus the correct answer is 120. But maybe the units: cm². So 120 cm².

Thus final answer: 120 cm².

But let's check if there's any other geometry: For the lateral faces, each is a triangle with base side 8 and height 10. So each area is 40. So sum 3*40 = 120.

Yes.

Thus answer: 120 cm².

Thus the solution is 120 cm².

Thus the correct answer is 120.

Thus final answer: 120.

Thus the answer: 120 cm².

Thus the solution is 120.

So the answer: 120.

Thus the correct answer is 120.

So final answer: 120 cm².<|end|><|start|>assistant<|channel|>final<|message|>The lateral surface area of a regular triangular pyramid is the sum of the areas of its three lateral faces. Each face is a triangle with a base equal to the side of the pyramid (8 cm) and a height equal to the pyramid's apothem (10 cm, since it is 2 cm greater than the base side).

Area of one triangle:
\[
\frac{1}{2} \times 8 \, \text{cm} \times 10 \, \text{cm} = 40 \, \text{cm}^2
\]

Since there are three such triangles:
\[
3 \times 40 \, \text{cm}^2 = 120 \, \text{cm}^2
\]

\[
\boxed{120 \text{ cm}^2}
\]
```

# Other languages

## Reasoning language: Korean, reasoning effort: low
```
<|start|>system<|message|>You are ChatGPT, a large language model trained by OpenAI.
Knowledge cutoff: 2024-06
Current date: 2025-08-29

Reasoning: low

# Valid channels: analysis, commentary, final. Channel must be included for every message.<|end|><|start|>developer<|message|># Instructions

reasoning language: Korean

<|end|><|start|>user<|message|>Обчисліть площу бічної поверхні правильної трикутної піраміди, сторона основи якої дорівнює 8 см, а апофема на 2 см більша за сторону основи піраміди.<|end|><|start|>assistant
<|channel|>analysis<|message|>문제는 정삼각 피라미드의 옆면 표면적을 구하는 것. 밑면의 한 변이 8cm, 각 옆면의 높이(apofema)가 밑면 변보다 2cm 더 크다. 정삼각 피라미드의 옆면은 정삼각형이므로, 옆면의 높이와 밑면 변이 주어지면 각 옆면의 넓이를 구할 수 있다. 옆면 넓이 = (밑변 * 높이)/2. 주어진 값으로 대입하면 (8 * (8+2))/2 = 40cm². 피라미드의 옆면은 3개이므로 총 옆면 표면적은 3 * 40 = 120cm². 따라서 정답은 120cm². 출력 형식은 "120 cm²" 또는 "120 cm²"와 같은 형태로 제공. 

정리: 120 cm².<|end|><|start|>assistant<|channel|>final<|message|>Обчислимо площу бічної поверхні трикутної піраміди. Для правильної трикутної піраміди кожна бічна поверхня є рівнобедрним трикутником. 

1. **Дано:**
   - Сторона основи піраміди: \(a = 8\) см
   - Апофема (висота бічної поверхні): \(h = a + 2 = 8 + 2 = 10\) см

2. **Площа одного бічного трикутника:**
   \[
   S_{\text{бічна}} = \frac{a \cdot h}{2} = \frac{8 \cdot 10}{2} = 40 \text{ см}^2
   \]

3. **Кількість бічних трикутників:**
   Для правильної трикутної піраміди трикутна основа має три бічні трикутники.

4. **Загальна площа бічної поверхні:**
   \[
   S_{\text{загальна}} = 3 \cdot S_{\text{бічна}} = 3 \cdot 40 = 120 \text{ см}^2
   \]

Отже, площа бічної поверхні правильної трикутної піраміди становить **120 см²**.
```

## Reasoning language: Spanish, reasoning effort: medium (repetition_penalty=1.1)
```
<|start|>system<|message|>You are ChatGPT, a large language model trained by OpenAI.
Knowledge cutoff: 2024-06
Current date: 2025-08-29

Reasoning: medium

# Valid channels: analysis, commentary, final. Channel must be included for every message.<|end|><|start|>developer<|message|># Instructions

Reasoning language: Spanish

<|end|><|start|>user<|message|>You’re given a competitive programming problem.

Analyze the maximum input constraints and identify the optimal algorithmic approach and data structures needed to process the largest possible test cases within the time and memory limits, then explain why your chosen implementation strategy is the most efficient solution. Please reason step by step about your solution approach, then provide a complete implementation in Python 3 that is thoroughly optimized for both speed and memory usage.

Your solution must read input from standard input (input()), write output to standard output (print()).
Do not include any debug prints or additional output.

Put your final solution within a single code block:
'''python
<your code here>
'''

# Problem

You're given an integer $$$n$$$. For every integer $$$i$$$ from $$$2$$$ to $$$n$$$, assign a positive integer $$$a_i$$$ such that the following conditions hold:

- For any pair of integers $$$(i,j)$$$, if $$$i$$$ and $$$j$$$ are coprime, $$$a_i 
eq a_j$$$.
- The maximal value of all $$$a_i$$$ should be minimized (that is, as small as possible).

A pair of integers is called coprime if their greatest common divisor is $$$1$$$.

## Constraints
Time limit per test: 1.0 seconds
Memory limit per test: 256.0 megabytes

## Input Format
The only line contains the integer $$$n$$$ ($$$2 \le n \le 10^5$$$).

## Output Format
Print $$$n-1$$$ integers, $$$a_2$$$, $$$a_3$$$, $$$\ldots$$$, $$$a_n$$$ ($$$1 \leq a_i \leq n$$$).

If there are multiple solutions, print any of them.

## Examples
'''input
4
'''
'''output
1 2 1
'''
'''input
3
'''
'''output
2 1
'''<|end|><|start|>assistant
<|channel|>analysis<|message|>Para resolver este problema necesitamos asignar a cada entero i en el rango [2..n] un valor positivo a_i tal que si dos números son coprimos entonces sus valores sean distintos y el máximo de todos los valores sea lo más pequeño posible. 

Observaciones clave:
1. Si dos números comparten un factor primo p, pueden compartir el mismo valor porque no son coprimos. Por lo tanto, podemos agrupar los enteros según los factores primos comunes.
2. Un algoritmo eficiente para generar estos grupos es usar la técnica de **sieve** (cribado). Para cada número primo p, marcamos todos sus múltiplos y los agrupamos bajo el mismo valor.
3. El proceso:
   - Inicializamos una lista `a` con ceros del tamaño n+1.
   - Usamos una lista booleana `is_prime` para identificar los primos.
   - Iteramos desde 2 hasta n. Si el número es primo, asignamos un nuevo valor único a todos sus múltiplos que aún no hayan sido asignados.
   - Este método garantiza que cualquier par coprimo tendrá valores diferentes y minimiza el máximo valor asignado.
4. Complejidad: O(n log log n), adecuada para n ≤ 100000.

Ejemplo:
- Para n=4, el resultado es 1 2 1 (maximo 2).
- Para n=3, el resultado es 2 1 (maximo 2).

Implementación en Python:
- Se utiliza un sieve clásico para marcar primos.
- Se mantiene un contador `current_val` para asignar valores únicos a cada grupo de múltiplos de un primo.
- Al finalizar, se imprime la lista `a[2:]`.

Código optimizado:
'''python
n = int(input())
a = [0] * (n + 1)
is_prime = [True] * (n + 1)
if n >= 0:
    is_prime[0] = False
if n >= 1:
    is_prime[1] = False
for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, n + 1, i):
            is_prime[j] = False
current_val = 1
for p in range(2, n + 1):
    if is_prime[p]:
        for m in range(p, n + 1, p):
            if a[m] == 0:
                a[m] = current_val
        current_val += 1
print(' '.join(map(str, a[2:n+1]))
'''

Esta solución cumple con las condiciones del problema y funciona eficientemente dentro de los límites dados.<|end|><|start|>assistant<|channel|>final<|message|>To solve this problem, we need to assign values to each integer \(i\) from 2 to \(n\) such that if two numbers are coprimes, they receive different values, and the maximum assigned value is minimized.

### Approach
The key insight is to use the properties of prime factors. If two numbers share a common prime factor, they can have the same value because they are not coprimes. We can group numbers based on their smallest prime factor using a sieve-like approach. This ensures that any two coprimes will belong to different groups and thus have different values.

### Algorithm
1. Use a sieve to find all primes up to \(n\).
2. Assign a unique value to each prime and its multiples that haven't been assigned yet.
3. This ensures that numbers sharing a prime factor get the same value, while coprimes get different values.

### Complexity
The algorithm runs in \(O(n \log \log n)\) due to the sieve operation, which is efficient for \(n\) up to \(10^5\).

### Solution Code
Here is the Python implementation of the described approach:

'''python
def main():
    import sys
    n = int(sys.stdin.readline())
    
    # Initialize array to store the values for each number
    a = [0] * (n + 1)
    
    # Sieve of Eratosthenes to find primes
    is_prime = [True] * (n + 1)
    if n >= 0:
        is_prime[0] = False
    if n >= 1:
        is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    current_value = 1
    for p in range(2, n + 1):
        if is_prime[p]:
            # Assign current_value to all multiples of p that are not yet assigned
            for m in range(p, n + 1, p):
                if a[m] == 0:
                    a[m] = current_value
            current_value += 1
    
    # Output the result for a[2] to a[n]
    print(' '.join(map(str, a[2:n+1]))

if __name__ == "__main__":
    main()
'''

This code reads the input, computes the necessary values using a sieve-based approach, assigns values efficiently, and outputs the results ensuring that the maximum value is minimized while satisfying the coprimality condition.
```