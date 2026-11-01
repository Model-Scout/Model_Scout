---
license: cc-by-4.0
language:
- ko
- zh
---
Korean Tutoring Persona Dataset
---
Overview
---
This dataset is constructed to evaluate the impact of learner persona modeling in bilingual Korean tutoring systems.

Each instance includes:
- Learner persona information
- Task type (grammar, error correction, multi-turn dialogue)
- Input query
- Three responses generated under different persona configurations
---
Data Structure
---
Each data instance is formatted as:

- persona: learner profile (TOPIK level, native language, etc.)
- task: task type
- query: input question
- response_R1: full persona response
- response_R2: partial persona response
- response_R3: no persona response
---
Task Types
---
- Grammar Explanation
- Error Correction
- Multi-turn Dialogue
---
Purpose
---
This dataset is designed for:
- Evaluating instructional consistency
- Analyzing difficulty alignment
- Measuring error-targeted feedback

---
Citation
---
If you use this dataset, please cite:

@article{
  title={Evaluating the Impact of Learner Persona Modeling on Instructional Consistency and Adaptive Feedback in Bilingual AI Tutoring Systems},
  author={Yang, Cheng},
  year={2026}
}