---
language:
  - en
  - ko
license: cc-by-nc-nd-4.0
task_categories:
  - text-generation
pretty_name: OLA (Output Language Alignment Benchmark)
configs:
  - config_name: simple_en_matrix
    data_files: simple/EN_Matrix_KO_Content.csv
  - config_name: simple_ko_matrix
    data_files: simple/KO_Matrix_EN_Content.csv
  - config_name: complex_en_instr
    data_files: complex/EN_Instruction_KO_Content.csv
  - config_name: complex_ko_instr
    data_files: complex/KO_Instruction_EN_Content.csv
---

# OLA: Output Language Alignment Benchmark

OLA is a benchmark designed to evaluate LLMs' Output Language Alignment in code-switched interactions

## Dataset Structure

OLA consists of two settings: **Simple** and **Complex**.

### Simple Setting

The Simple setting focuses on intra-sentential code-switching, where the expected response language is the *matrix language*—the language providing the core grammatical structure into which elements from another language are embedded.

Located in `simple/`:
- **EN_Matrix_KO_Content.csv**: English matrix language with Korean embedded content 
- **KO_Matrix_EN_Content.csv**: Korean matrix language with English embedded content 

Each file contains three columns:
- `query`: The code-switched prompt
- `source`: Source identifier
- `expected_lang`: Expected response language

### Complex Setting

The Complex setting involves inter-sentential code-switching, where instruction and content languages differ, and the correct response language must be inferred from task semantics.

Located in `complex/`:
- **EN_Instruction_KO_Content.csv**: English instruction with Korean content 
- **KO_Instruction_EN_Content.csv**: Korean instruction with English content

Each file contains four columns:
- `InstrFirst`: Instruction-first query
- `ContentFirst`: Content-first query
- `source`: Source identifier
- `expected_lang`: Expected response language
