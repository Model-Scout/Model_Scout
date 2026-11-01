---
license: mit
task_categories:
- feature-extraction
language:
- ko
size_categories:
- 10K<n<100K
---
# Resume-JD Pair Matching Dataset

A large-scale dataset for resume and job description (JD) matching tasks, generated using GPT-4o-mini. Ideal for training and evaluating models in HR tech, recommender systems, and information retrieval.

---

## Overview

This dataset includes:

- 1,320 Resumes  
- 1,320 Job Descriptions (JDs)  
- 30 Job Roles  
- 4 Experience Levels  
- 11 Tech Companies  
- 29,040 Total Pairs (14,520 positive + 14,520 negative)

Positive pairs were generated only when both job title and experience level matched. All other combinations are labeled as negative.

---

## Job Roles (30 Total)

1. Software Engineer  
2. Backend Engineer  
3. Frontend Developer  
4. Full Stack Engineer  
5. Machine Learning Researcher  
6. Data Scientist  
7. Data Engineer  
8. DevOps Engineer  
9. Site Reliability Engineer (SRE)  
10. Cloud Engineer  
11. Security Engineer  
12. QA Engineer  
13. Mobile Developer  
14. iOS Developer  
15. Android Developer  
16. Embedded Systems Engineer  
17. Computer Vision Engineer  
18. NLP Engineer  
19. AI Engineer  
20. Robotics Engineer  
21. Game Developer  
22. Blockchain Developer  
23. Systems Engineer  
24. Firmware Engineer  
25. Solutions Architect  
26. Product Manager (Technical)  
27. Technical Program Manager  
28. Research Scientist (AI/ML)  
29. Database Administrator  
30. IT Support Engineer

---

## 📊 Experience Levels

- Junior  
- Mid-level  
- Senior  
- Staff  

---

## 🏢 Companies

- Google  
- Meta  
- Amazon  
- Apple  
- Tesla  
- SpaceX  
- OpenAI  
- Perplexity  
- Microsoft  
- Netflix  
- Nvidia  

---

## Dataset Structure

Each entry in the dataset includes:

- `resume_text`: string  
- `jd_text`: string  
- `label`: binary (1 = match, 0 = non-match)

Available in CSV format.

---

## Positive Match Criteria

A pair is labeled as positive (1) if:

- Resume and JD share the same job role  
- Resume and JD share the same experience level

Otherwise, the pair is labeled as negative (0).

---

## Use Cases

- Resume-JD similarity modeling  
- ATS (Applicant Tracking System) benchmarking  
- Contrastive learning (Siamese/BERT-style)  
- Job recommendation engines  
- HR tech model fine-tuning

---

## Why Use This Dataset?

- High-quality synthetic generation using GPT-4o-mini  
- Balanced dataset for supervised learning  
- Wide coverage of roles, levels, and top companies  
- Useful for both retrieval and classification tasks

---

## License

[MIT]

---

## Citation & Contributions

If you use this dataset in your work, please star the repo and consider citing the dataset source.

---