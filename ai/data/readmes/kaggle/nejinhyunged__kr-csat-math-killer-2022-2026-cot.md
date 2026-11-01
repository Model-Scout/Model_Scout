# KR-CSAT-Math-Killer-2022-2026-CoT

A high-difficulty reasoning benchmark featuring the most challenging math proble

🏆 KR-CSAT Math Killer CoT: 5-Year Reasoning Benchmark (2022-2026)

🚀 Unleashing the Frontier of AI Mathematical Reasoning

This dataset is a premium collection of the most notorious "Killer Problems" from the South Korean College Scholastic Ability Test (CSAT/Suneung), covering the years 2022 through 2026. The CSAT is globally recognized as one of the most rigorous high-school level exams, specifically designed to test deep logical reasoning beyond simple calculation.

🔥 Why This Dataset?

Standard math datasets often lack the complexity required to push $120\text{B}+$ parameter models to their limits. 

This corpus bridge that gap by providing:High-Difficulty Content: Focuses exclusively on the "Killer" problems (No. 14, 15, 21, 22, and 30) that decide the top 1% of students in Korea.Verified Chain-of-Thought (CoT): Every problem includes a meticulously structured, step-by-step reasoning trace.

Multi-Domain Coverage: Includes Calculus, Geometry, and Probability & Statistics.LaTeX Integration: All mathematical notations are provided in clean LaTeX for optimal tokenization and model comprehension.🛠 Dataset StructureThe data is provided in JSONL (JSON Lines) format, optimized for direct fine-tuning and instruction tuning.

Key Fields:instruction: Task-specific prompts for the model.input: The translated problem statement including LaTeX formulas.output: A detailed "Reasoning Path" followed by the final answer in a $\boxed{...}$.🔬 Sample Case: 2026 CSAT Common No. 15Task: Analyze sign changes in the derivative of an integral function to find a specific constant $k$.Reasoning: Step-by-step discriminant analysis ($D = a^2 - 4a \le 0$) and integration.Verified Answer: $\boxed{15/2}$.

📜 License & UsageLicense: Apache License 2.0This dataset is intended for use in the AI Mathematical Olympiad (AIMO) and broader research in autonomous mathematical problem-solving.

출처: Kaggle (nejinhyunged/kr-csat-math-killer-2022-2026-cot)
태그: artificial intelligence, nlp, korea, mathematics
라이선스: Apache 2.0
수정일: 2026-02-01T04:11:38.300Z
